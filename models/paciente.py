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


class paciente(models.Model):
    """Registra los Pacientes"""
    _name = 'hemodialisis_paciente'
    _rec_name = 'cedula'
    
    cedula = fields.Integer('Nro. Cedula', size=15, help='Registre Nro. Cedula del Paciente', required=True)
    nombre = fields.Char(string='Apellido(s), Nombre(s)', size=40, help='Registre Apellido(s), Nombre(s) del Paciente', required=True)
    fecha_nacimiento = fields.Date(string='Fecha Nacimiento', help='Registre Fecha de Nacimiento del Paciente', required=True)
    edad = fields.Integer('Edad', help='Registre edad del Paciente', required=True)
    conclusiones = fields.Text('Conclusiones', help='Conclusiones')
 
    hemodialisis_tratamiento_ids = fields.One2many('hemodialisis_tratamiento','hemodialisis_paciente_id', string="Paciente", deleted="cascade",
                          help='Registra las Hemodialisis', required=True)    
    _sql_constraints = [('cedula', 'unique(cedula)', 'La cedula del paciente, debe ser Unica!')]
