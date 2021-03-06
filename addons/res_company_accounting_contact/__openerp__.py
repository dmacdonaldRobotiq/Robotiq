# -*- encoding: utf-8 -*-
# #############################################################################
#
#    Odoo, Open Source Management Solution
#    This module copyright (C) 2015 Savoir-faire Linux
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

{
    'name': 'Company Accounting Contact',
    'version': '0.1',
    'author': 'Savoir-faire Linux',
    'maintainer': 'Savoir-faire Linux',
    'website': 'http://www.savoirfairelinux.com',
    'license': 'AGPL-3',
    'category': 'Sales',
    'summary': 'Company Accounting Contact',
    'description': """
Company Accounting Contact
==========================

Add the field accounting_contact_id on res_company

Contributors
------------
* Bruno Joliveau <bruno.joliveau@savoirfairelinux.com>
* Jordi Riera <jordi.riera@savoirfairelinux.com>
* David Dufresne <david.dufresne@savoirfairelinux.com>
""",
    'depends': [
        'base',
    ],
    'external_dependencies': {
        'python': [],
    },
    'data': [
        'views/res_company_view.xml',
    ],
    'demo': [
    ],
    'js': [],
    'css': [],
    'qweb': [],
    'installable': True,
}
