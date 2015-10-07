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
import openerp.addons.decimal_precision as dp
from operator import attrgetter


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.one
    def _get_sale_order(self):
        sale_order = self.env['sale.order'].search(
            [('name', '=', self.origin)])

        if sale_order:
            self.origin_sale_order = sale_order[0].id

        else:
            stock_picks = self.env['stock.picking'].search(
                [('name', '=', self.origin)])

            if stock_picks and stock_picks[0].sale_id:
                self.origin_sale_order = stock_picks[0].sale_id.id

    @api.one
    @api.depends('residual')
    def _compute_amount_paid(self):
        self.amount_paid = self.state == 'draft' and 0 or \
            self.amount_total - self.residual

    origin_sale_order = fields.Many2one(
        string='Sale Order', comodel_name='sale.order',
        compute=_get_sale_order, store=False)

    amount_paid = fields.Float(
        string='Amount Paid', digits=dp.get_precision('Account'),
        compute='_compute_amount_paid', store=True)

    @api.multi
    def invoice_print(self):
        """
        Change the report being rendered when cliking on Print Invoice
        """
        res = super(AccountInvoice, self).invoice_print()
        res['report_name'] = 'robotiq_data.report_sale_invoice'
        return res

    @api.onchange('payment_term')
    def onchange_payment_term(self):
        if self.payment_term:
            self.comment = self.payment_term.note

    @api.one
    def _fix_lines_sequence(self):
        """
        Set invoice lines sequence to 1, 2, 3, ... x-1, x
        """
        lines = self.invoice_line.sorted(key=attrgetter('sequence'))
        count = 1
        for line in lines:
            line.sequence = count
            count += 1

    @api.model
    def create(self, vals):
        if 'payment_term' in vals:
            payment_term = self.env['account.payment.term'].browse(
                vals['payment_term'])
            vals['comment'] = payment_term.note

        res = super(AccountInvoice, self).create(vals)

        res._fix_lines_sequence()

        return res

    @api.multi
    def write(self, vals):
        res = super(AccountInvoice, self).write(vals)

        self.refresh()

        if 'invoice_line' in vals:
            self._fix_lines_sequence()

        return res
