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


class MailNotification(models.Model):
    _inherit = 'mail.notification'

    def get_signature_footer(self, *args, **kwargs):
        """Remove all reference to the company or to odoo in the email footer.

        :return: empty string
        """
        return ''


class MailMail(models.Model):
    _inherit = 'mail.mail'

    def _get_partner_access_link(self, *args, **kwargs):
        """Remove the link to the record from the email footer.

        :return: empty string
        """
        return ''
