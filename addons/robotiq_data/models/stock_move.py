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


class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.one
    def _get_price_from_invoice(self):
        if self.procurement_id:
            self.price_from_invoice = self.procurement_id.sale_line_id.\
                price_unit
        else:
            self.price_from_invoice = self.product_id.price

    price_from_invoice = fields.Float(
        string='Price Unit', compute='_get_price_from_invoice', store=False)

    @api.one
    def _get_product_description(self):
        if self.procurement_id:
            self.product_description = self.procurement_id.sale_line_id.name
        else:
            product = self.product_id

            name = product.default_code and "[%s] " % \
                product.default_code or ""

            self.product_description = "%s%s\n%s" % (
                name, self.product_id.name, self.product_id.description)

    product_description = fields.Text(
        string='Product Description',
        compute='_get_product_description', store=False)
