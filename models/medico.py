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



class medico(models.Model):
    """Registra los Pacientes"""
    _name = 'hemodialisis_medico'
    _rec_name = 'nombre'
    
    cedula = fields.Integer('Nro. Cedula', size=15, help='Registre Nro. Cedula del Medico', required=True)
    nombre = fields.Char(string='Apellido(s), Nombre(s)', size=40, help='Registre Apellido(s), Nombre(s) del Medico', required=True)
    hemodialisis_paciente_ids = fields.One2many('hemodialisis_paciente','id', string="Pacientes", deleted="cascade",
                          help='Registra las Hemodialisis', required=True)    
    _sql_constraints = [('cedula', 'unique(cedula)', 'La cedula del Medico, debe ser Unica!')]

