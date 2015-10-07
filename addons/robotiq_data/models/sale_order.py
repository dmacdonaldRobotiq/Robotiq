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

from openerp import models, api
from operator import attrgetter


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.one
    def _fix_lines_sequence(self):
        """
        Set sale order lines sequence to 1, 2, 3, ... x-1, x
        """
        lines = self.order_line.sorted(key=attrgetter('sequence'))
        count = 1
        for line in lines:
            line.sequence = count
            count += 1

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)

        res._fix_lines_sequence()

        return res

    @api.multi
    def write(self, vals):
        res = super(SaleOrder, self).write(vals)

        self.refresh()

        if 'order_line' in vals:
            self._fix_lines_sequence()

        return res
