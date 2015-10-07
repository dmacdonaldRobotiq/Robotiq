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
    'name': 'Robotiq',
    'version': '15.14',
    'author': 'Savoir-faire Linux',
    'maintainer': 'Savoir-faire Linux',
    'website': 'http://www.savoirfairelinux.com',
    'license': 'AGPL-3',
    'category': 'Others',
    'summary': 'Robotiq base module',
    'description': """
Robotiq
=======
This module contains the dependencies.
The data are stored in robotiq_data module.
The aim is to keep the main module as empty as possible. It should just install
dependencies.
This module contains the dependencies, configuration and data to setup a
database and test Robotiq configuration.

Contributors
------------
* Bruno Joliveau <bruno.joliveau@savoirfairelinux.com>
* Jordi Riera <jordi.riera@savoirfairelinux.com>
* David Dufresne <david.dufresne@savoirfairelinux.com>

""",
    'depends': [
        'admin_technical_features',
        'account',
        'account_accountant',
        'account_anglo_saxon',
        'account_banking_reconciliation',
        'account_chart',
        'account_check_writing',
        'account_followup',
        'account_reversal',
        'account_voucher',
        'analytic',
        'auth_crypt',
        'auth_signup',
        'base',
        'base_action_rule',
        'base_iban',
        'base_import',
        'base_import_module',
        'base_setup',
        'base_user_signature_logo',
        'base_vat',
        'board',
        'bus',
        'calendar',
        'claim_from_delivery',
        'contacts',
        'crm',
        'crm_action',
        'crm_claim',
        'crm_lead_sale_link',
        'decimal_precision',
        'delivery',
        'document',
        'edi',
        'email_template',
        'fetchmail',
        'gamification',
        'gamification_sale_crm',
        'hr',
        'hr_attendance',
        'hr_contract',
        'hr_expense',
        'hr_gamification',
        'hr_timesheet',
        'hr_timesheet_invoice',
        'hr_timesheet_sheet',
        'im_chat',
        'im_odoo_support',
        'knowledge',
        'l10n_ca',
        'l10n_ca_account_check_writing',
        'l10n_ca_toponyms',
        'mail',
        'marketing',
        'mass_editing',
        'mrp',
        'mrp_bom_reference_selection',
        'mrp_operations',
        'mrp_repair',
        'payment',
        'payment_transfer',
        'portal',
        'portal_claim',
        'portal_gamification',
        'portal_project',
        'portal_sale',
        'portal_stock',
        'procurement',
        'product',
        'product_internal_reference_kanban',
        'product_template_kanban',
        'project',
        'purchase',
        'purchase_order_carrier_id',
        'robotiq_data',
        'report',
        'res_company_accounting_contact',
        'res_currency_print_on_check',
        'resource',
        'sale',
        'sale_order_dates',
        'sale_order_revision',
        'sale_order_revision_sequence',
        'sales_expected_shipping_date_field',
        'sale_crm',
        'sale_mrp',
        'sale_stock',
        'sales_team',
        'share',
        'stock',
        'stock_account',
        'web',
        'web_calendar',
        'web_diagram',
        'web_gantt',
        'web_graph',
        'web_kanban',
        'web_kanban_gauge',
        'web_kanban_sparkline',
        'web_tests',
        'web_view_editor',
    ],
    'external_dependencies': {
        'python': [],
    },
    'data': [
        'res_partner_timezone_admin.xml',
        'webclient_templates.xml',
        'data/company_details.xml'
    ],
    'installable': True,
    'application': True,
}
