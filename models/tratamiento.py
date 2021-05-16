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



                                   
                                                    
class tratamiento(models.Model):
    """Registra tratamiento del Pacientes"""
    _name = 'hemodialisis_tratamiento'
    
    hemodialisis_paciente_id = fields.Many2one('hemodialisis_paciente','Paciente', required=True, 
                                                help='Id del Paciente')
    nombre_paciente = fields.Char(string='Nombre Paciente', size=40)                                            
    hemodialisis_medico_id = fields.Many2one('hemodialisis_medico','Médico', required=True, 
                                                help='Id del Medico')
    hemodialisis_maquina_id = fields.Many2one('hemodialisis_maquina','Maquina', required=True, 
                                                help='Id de la Maquina')
                                                                                            
    fecha_tratamiento = fields.Date(string = 'Fecha Tratamiento', required=True, help='Fecha Tratamiento')
    duracion = fields.Float(string="Duración", help='Registra la duración',digits=(2,2))
    Peso_pre_hd = fields.Float(string="Peso PRE-HD", help='Registra peso PRE-HD', digits=(3,2))
    Peso_post_hd = fields.Float(string="Peso PRE-POST", help='Registra peso POST-HD', digits=(3,2))
    balance = fields.Char(string='Balance')
    ta_pre = fields.Char(string='TA-PRE', size=10)
    ta_post = fields.Char(string='TA-POST', size=10)
    heparina = fields.Char(string='Heparina', size=10)
    transfución = fields.Boolean(string='Transfución', default = False)
    observacion = fields.Text(string='Observación')


    @api.onchange('hemodialisis_paciente_id')
    def generar_nombre(self):
        if self.hemodialisis_paciente_id:
            self.nombre_paciente = self.hemodialisis_paciente_id.nombre
            
            
            
            
