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


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # In the report, we need the sequence to start at 1 instead of 10.
    sequence = fields.Integer(default=1000000)

    @api.multi
    def product_id_change(
            self, pricelist, product, *args, **kwargs):
        res = super(SaleOrderLine, self).product_id_change(
            pricelist, product, *args, **kwargs)

        if not product:
            return res

        if not res.get('value', False):
            res['value'] = {}

        product = self.env['product.product'].browse(product)

        if product.description:
            res['value']['name'] = "%s\n%s" % (
                product.name, product.description)
        else:
            res['value']['name'] = product.name

        return res
