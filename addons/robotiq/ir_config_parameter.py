# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2010 - 2015 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

"""Add webkit path from config to default config parameters by hijacking a cr
from an earlier stack level.
"""

import platform
import os
import inspect

from openerp import pooler, SUPERUSER_ID
from openerp.tools import config
from openerp.sql_db import Cursor


def get_webkit_path():
    """Get webkit path from conf and get the proper binary for arch

    :returns: str -- path to webkit binary or False
    """

    arch = platform.machine()
    if arch == 'x86_64':
        arch = 'amd64'
    webkit_path = config.get('webkit_path', False)
    if webkit_path and os.path.isdir(webkit_path):
        webkit_path = os.path.join(
            webkit_path, 'wkhtmltopdf-%s' % arch
        )
    return webkit_path


def get_cr_from_stack():
    """Hack: Search up the stack for valid cursor to set a config_parameter

    :returns: Cursor -- A cursor from the execution which is installing the
    module or None
    """
    frame = inspect.currentframe()
    cr = None
    while(frame):
        cr = frame.f_locals.get('cr')
        if isinstance(cr, Cursor):
            break
        frame = frame.f_back
    return cr

webkit_path = get_webkit_path()
cr = get_cr_from_stack()

if cr and webkit_path:
    pool = pooler.get_pool(cr.dbname)
    pool['ir.config_parameter'].set_param(
        cr, SUPERUSER_ID, 'webkit_path', webkit_path
    )
