# -*- encoding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    This module copyright (C) 2015 JPJ
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

from openerp import models, fields
from openerp.tools.translate import _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    qte_kanban_commander = fields.Integer(
        string=_("Quantite Kanban a commander"),
        required=False,
        translate=False,
        readonly=False,
        help=_("Quantite qu'il faut commander lorsqu'il "
               "reste Quantite Kanban min."),
    )

    qte_kanban_min = fields.Integer(
        string=_("Quantite Kanban min"),
        required=False,
        translate=False,
        readonly=False,
        help=_("Quantite a laquelle il faut passer une commande."),
    )
