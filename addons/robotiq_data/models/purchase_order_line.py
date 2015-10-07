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


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    sequence = fields.Integer('Sequence', default=1000000)

    @api.multi
    def onchange_product_id(
        self, pricelist_id, product_id, qty, uom_id,
        partner_id, date_order=False, fiscal_position_id=False,
            date_planned=False, name=False, price_unit=False, state=False):

        res = super(PurchaseOrderLine, self).onchange_product_id(
            pricelist_id, product_id, qty, uom_id,
            partner_id, date_order, fiscal_position_id,
            date_planned, name, price_unit, state)

        if not product_id:
            return res

        if not res.get('value', False):
            res['value'] = {}

        product = self.env['product.product'].browse(product_id)

        if product.description:
            res['value']['name'] = "%s\n%s" % (
                product.name, product.description)
        else:
            res['value']['name'] = product.name

        return res
