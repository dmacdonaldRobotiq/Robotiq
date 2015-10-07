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

from openerp import models, fields, api


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    # In the report, we need the sequence to start at 1 instead of 10.
    # The default sequence is set to a high level
    # When the account invoice record is written
    # The lines sequence is restored to 1, 2, 3, ... x-1, x
    sequence = fields.Integer(default=1000000)

    @api.multi
    def product_id_change(
        self, product, uom_id, qty=0, name='', type='out_invoice',
        partner_id=False, fposition_id=False, price_unit=False,
        currency_id=False, company_id=None
    ):
        """
        :param product: product.product id
        """
        res = super(AccountInvoiceLine, self).product_id_change(
            product, uom_id, qty=qty, name=name, type=type,
            partner_id=partner_id, fposition_id=fposition_id,
            price_unit=price_unit,
            currency_id=currency_id, company_id=company_id
        )

        if not product:
            return res

        if not res.get('value'):
            res['value'] = {}

        product_obj = self.env['product.product'].browse(product)

        if product_obj.description:
            res['value']['name'] = "%s\n%s" % (
                product_obj.name, product_obj.description)
        else:
            res['value']['name'] = product_obj.name

        return res
