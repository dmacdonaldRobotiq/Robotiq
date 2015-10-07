# -*- coding: utf-8 -*-
# -*- python -*-
"""This is a template upgrade script.

The purpose is both to cover the most common use-case (updating all modules)
and to provide an example of how this works.
"""

from base64 import b64encode, b64decode
from cStringIO import StringIO
from PIL import Image, ImageDraw
from functools import wraps

from openerp.pooler import get_pool
from openerp.tools import config

client_module = 'robotiq'
dev_db_user = 'odoo8dev'
previous_version = "15.15.0"
target_version = "15.16.0"


def to_dev(session, logger):
    """Perform database manipulations to prod data when going into dev
    such as in staging or when testing on a dev station:
        * Set logo to indicate dev
        * Set test docubase url
        * Set all id_dms in ir.attachement to false as they are not in test
          server
    """

    def to_dev_logo():
        """Using PIL add 'DEV' to the company (and the main odoo) logo"""
        main_partner = session.registry('ir.model.data').get_object(
            session.cr, session.uid, 'base', 'main_partner',
            context=session.context)
        if main_partner.image:
            logo_data = b64decode(main_partner.image).strip()
            logo_img = Image.open(StringIO(logo_data))
        else:
            logo_img = Image.new('RGBA', (180, 180))
        dev_img = Image.new('RGBA', (20, 13))
        dev_draw = ImageDraw.Draw(dev_img)
        dev_draw.text((1, 0), "DEV", (255, 0, 0, 180))
        dev_img = dev_img.resize(logo_img.size)
        dev_img = dev_img.rotate(45)
        logo_img.paste(dev_img, (0, 0), dev_img)
        logo_stringio = StringIO()
        logo_img.save(logo_stringio, format='png')
        logo_data = b64encode(logo_stringio.getvalue())
        main_partner.write({'image': logo_data})

    # Only run if the current db user is dev (deploy with install.sh)
    if config.get('db_user', dev_db_user) != dev_db_user:
        return
    logger.info("db_user is %s, removing prod settings...", dev_db_user)
    # Set dev logo
    logger.info("Stamping 'DEV' on the server logo")
    to_dev_logo()


def prod_or_dev(func):
    """Wrap run to run to_dev after each return
    Exception when session.db_version < previous_version
    """

    @wraps(func)
    def wrapped(session, logger):
        ret = func(session, logger)
        if session.is_initialization or session.db_version >= previous_version:
            to_dev(session, logger)
        return ret

    return wrapped


def upgrade_15_15_0_to_15_16_0_uninstall_module_prototyper(session, logger):
    """
    Remove module prototyper

    This fails when droping table module_prototyper_module_rel table
    if triggered from the user interface.
    """

    class module_mock(object):
        """Mock class with proper fields for uninstall

        Inherit from this class if the model was a bit complex
        Add unlink overwrite if there was one
        """
        _log_access = False
        _pop_field = lambda c, n: n
        _fields  = {}

        def __init__(self, table_name):
            self._table = table_name

    # Get the pool from the session
    pool = get_pool(session.cr.dbname)

    # Add the mock modules to the pool
    pool.add("module_prototyper", module_mock(table_name="module_prototyper"))
    pool.add(
        "module_prototyper.module.export",
        module_mock(table_name="module_prototyper_module_export")
    )

    # Run the unintall

    cr, uid, context = session.cr, session.uid, session.context
    module_obj = session.registry('ir.module.module')
    module_id = module_obj.search(cr, uid, [
        ('name', '=', 'module_prototyper'),
    ], context=context)[0]
    module = module_obj.browse(cr, uid, module_id, context=context)
    logger.info('Uninstalling module_prototyper')
    module.module_uninstall()


@prod_or_dev
def run(session, logger):
    """Update all modules."""
    # Getting context
    try:
        session.context = session.registry('res.users').context_get(
            session.cr, session.uid
        )
    except Exception as e:
        logger.warn("Could not get context from user: %s", str(e))
        session.context = {'lang': 'fr_FR'}

    if session.is_initialization:
        logger.info("Usage of upgrade script for initialization detected. "
                    "Installing %s Module...", client_module)
        session.install_modules([client_module])
        return
    elif session.db_version >= target_version:
        logger.warn("Database is already at version %s. Skipping migrations.",
                    target_version)
        session.update_modules_list()
        session.update_modules(['all'])
        return
    elif session.db_version < previous_version:
        logger.warn("Database is at an older version: %s. "
                    "Please update to %s before running these migrations.",
                    session.db_version, previous_version)
        return

    # Pre-update

    # Update
    logger.info("Forcing installation of %s module", client_module)
    session.install_modules([client_module])
    logger.info("Default upgrade procedure: updating all modules.")
    session.update_modules_list()
    session.update_modules(['all'])

    # Post-update
    upgrade_15_15_0_to_15_16_0_uninstall_module_prototyper(session, logger)
