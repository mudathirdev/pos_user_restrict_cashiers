# -*- coding: utf-8 -*-
from odoo import models, fields, api
#from escpos.printer import Network

class productCategory(models.Model):
    _inherit = "res.users"
    pos_config_id = fields.Many2one('pos.config')


class posNetworkPrinterConfig(models.Model):
    _inherit = "pos.config"

    user_ids = fields.One2many('res.users','pos_config_id')
