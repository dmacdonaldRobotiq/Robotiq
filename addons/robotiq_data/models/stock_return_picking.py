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

from openerp import models


class StockReturnPicking(models.Model):
    _inherit = 'stock.return.picking'

    def default_get(self, cr, uid, fields, context=None):
        """Overcharge the method to set 2binvoiced as the default value for
        invoice_state as required in
        https://projects.savoirfairelinux.com/issues/68214

        :return: dict
        """
        res = super(StockReturnPicking, self).default_get(
            cr, uid, fields, context=context
        )
        res.update({'invoice_state': '2binvoiced'})
        return res
