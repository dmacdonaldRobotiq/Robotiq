# -*- encoding: utf-8 -*-
# #############################################################################
#
#    Odoo, Open Source Management Solution
#    This module copyright (C) 2015 JPJ
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
    'name': 'Product Internal Reference Kanban',
    'version': '0.2',
    'author': 'JPJ',
    'maintainer': 'Savoir-faire Linux',
    'website': 'http://www.savoirfairelinux.com',
    'license': 'AGPL-3',
    'category': 'Sales',
    'summary': 'Print Internal Reference in product.product in Kanban view',
    'description': """
Product Internal Reference Kanban
=================================

need to see Internal Reference field in Kanban View.

This module show the product.template's Internal Reference field in Kanban view
no new fields are created

only the view is modified: product.template (Kanban):
ext. ID: product.product_kanban_view

    * Module exported by the Module Prototyper module for version 8.0.
    * If you have any questions, please contact Savoir-faire Linux
      <support@savoirfairelinux.com>

""",
    'depends': ['sale', ],
    'external_dependencies': {
        'python': [],
    },

    'data': [
        'views/product_template_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
