# -*- coding= utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError
from odoo.osv import expression




#from Datetime import Date, Datetime,timedelta
#from odoo import pooler
#fr delom Datetime import  Datetime
from time import time

from datetime import date
from datetime import datetime

formatter_string = "%d-%m-%y" 
#from tools.translate import_
#from odoo import tools
#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")
#Importamos la libreria logger
import logging, csv, operator
#Definimos la Variable Global
_logger = logging.getLogger(__name__)



class maquina(models.Model):
    """Registra los Pacientes"""
    _name = 'hemodialisis_maquina'
    _rec_name = 'codigo'
    
    codigo = fields.Char('Código', size=20, help='Registre Código De La Maquina', required=True)
    serial = fields.Char(string='Serial', size=20, help='Registre Serial Maquina', required=True)
    operatividad = fields.Boolean(string='Operatividad', required=True, default=True)
    observacion = fields.Text(string="Observación" )
    _sql_constraints = [('codigo', 'unique(codigo)', 'El ccódigo de la Maquina, debe ser Unica!')]

