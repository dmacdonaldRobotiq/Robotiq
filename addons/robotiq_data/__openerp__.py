# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2010 - 2014 Savoir-faire Linux
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

{
    'name': 'Robotiq_data',
    'version': '1.0',
    'author': 'Savoir-faire Linux',
    'maintainer': 'Savoir-faire Linux',
    'website': 'http://www.savoirfairelinux.com',
    'license': 'AGPL-3',
    'category': 'Data',
    'summary': 'Robotiq data base module',
    'description': """
Robotiq Data
============
This module contains the data of the client.

It is splitted from the main module to keep the main module as an empty shell
that install the system

Contributors
------------
* Bruno Joliveau <bruno.joliveau@savoirfairelinux.com>
* Jordi Riera <jordi.riera@savoirfairelinux.com>
* David Dufresne <david.dufresne@savoirfairelinux.com>

""",
    'depends': [
        'stock',
        'product',
        'delivery',
        'mail',
        'sale_reason_to_export',
        'mrp',
        'crm',
        'stock',
        'res_company_accounting_contact',
        'purchase_order_carrier_id',
        'stock_account',
        'base_user_signature_logo',  # needed for reports
        'sale_order_dates',  # needed for reports
        'sales_expected_shipping_date_field',  # needed for reports
        'portal',  # needed for emails footer customization
    ],
    'external_dependencies': {
        'python': [],
    },
    'data': [
        'data/decimal_precision.xml',
        'data/report_sale_order.xml',
        'data/report_purchase_order.xml',
        'data/report_packing_slip.xml',
        'data/report_commercial_invoice.xml',
        'data/report_layout.xml',
        'data/report_styles.xml',
        'data/report_sale_invoice.xml',
        'data/stock_return_picking.xml',
        'views/crm_lead_view.xml',
        'views/mail_thread_view.xml',
        'data/stock_transfer_details.xml',
        'views/stock_picking_view.xml',
        'views/purchase_order_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}
