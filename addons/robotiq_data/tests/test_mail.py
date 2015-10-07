# -*- encoding: utf-8 -*-
# #############################################################################
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

from openerp.tests import common


class TestMailNotification(common.TransactionCase):
    def setUp(self):
        super(TestMailNotification, self).setUp()
        self.mail_notification_pool = self.env['mail.notification']
        self.res_partner_pool = self.env['res.partner']
        self.mail_message_pool = self.env['mail.message']

        partner_id = self.res_partner_pool.create({'name': 't_name'}).id
        message_id = self.mail_message_pool.create({}).id
        self.mail_notification = self.mail_notification_pool.create(
            {'partner_id': partner_id, 'message_id': message_id}
        )

    def test_get_signature_footer_return(self):
        """Check all reference to the company or to odoo in the email footer
        are removed.
        """
        self.assertEqual(self.mail_notification.get_signature_footer(), '')


class TestMailMail(common.TransactionCase):
    def setUp(self):
        super(TestMailMail, self).setUp()
        self.mail_mail_pool = self.env['mail.mail']
        self.mail_message_pool = self.env['mail.message']
        message_id = self.mail_message_pool.create({}).id

        self.mail_mail = self.mail_mail_pool.create({'message_id': message_id})

    def test_get_partner_access_link(self):
        """Check the link to the record from the email footer is removed."""
        self.assertEqual(self.mail_mail._get_partner_access_link(), '')
