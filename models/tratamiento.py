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
    hemodialisis_maquina_id = fields.Many2one('hemodialisis_maquina','Maquina', required=True, 
                                                help='Id de la Maquina')
                                                                                            
    fecha_tratamiento = fields.Date(string = 'Fecha Tratamiento', required=True, help='Fecha Tratamiento',
                               default = date.today().strftime('%Y-%m-%d'))
    duracion = fields.Float(string="Duración", help='Registra la duración',digits=(2,2), required=True)
    peso_pre_hd = fields.Float(string="Peso PRE-HD", help='Registra peso PRE-HD', digits=(3,2), required=True)
    peso_post_hd = fields.Float(string="Peso PRE-POST", help='Registra peso POST-HD', digits=(3,2), required=True)
    balance = fields.Char(string='Balance', required=True)
    ta_pre = fields.Char(string='TA-PRE', size=10, required=True)
    ta_post = fields.Char(string='TA-POST', size=10, required=True)
    heparina = fields.Boolean(string='Heparina', default=False)
    transfucion = fields.Boolean(string='Transfución', default = False)
    tratamiento_pre = fields.Text(string="Tratamiento PRE")
    tratamiento_post = fields.Text(string="Tratamiento POST")
    observacion = fields.Text(string='Observación')
    
    _sql_constraints = [('hemodialisis_tratamiento_id', 'unique(hemodialisis_paciente_id, fecha_tratamiento)', 'El Paciente ya fué Dialisado en esa Fecha de Tratamiento')]  
    _order = 'fecha_tratamiento' 

    @api.onchange('hemodialisis_paciente_id')
    def generar_nombre(self):
        if self.hemodialisis_paciente_id:
            self.nombre_paciente = self.hemodialisis_paciente_id.nombre
            
            
    @api.onchange('fecha_tratamiento')
    def val_fecha_tratamiento(self):
        if self.fecha_tratamiento:
            fechaActual = datetime.now().date()
            fechaTratamiento = self.fecha_tratamiento
            if fechaTratamiento > fechaActual:
                self.fecha_tratamiento = fechaActual
                res = {}
                mensaje = "La Fecha Del Tratamiento no puede ser superior a la Fecha Actual"  
                warning = {
                    'title': "Advertencia!",
                    'message': mensaje,
                }
                res.update({
                'warning':warning
                })
                return res
                
