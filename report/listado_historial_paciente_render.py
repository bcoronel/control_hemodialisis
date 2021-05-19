# -*- coding= utf-8 -*-

from odoo import api, fields, models
from odoo.tools import float_round
from odoo.exceptions import ValidationError
from time import time

from datetime import date
from datetime import datetime


class ListadoHistorialPacienteRender(models.AbstractModel):
    _name = "report.hemodialisis.listado_historial_paciente_render"
    
    def m_observacion(self, observa):
        if observa == None:
            return observa
        else:   
            observa = str(observa)
            if len(observa) > 110:
                observa = observa[0:100] + "[...]"        
            return observa

    def mayuscula(self, cadena):
        return cadena.upper()

    def fecha_formato(self, fecha):
        fechaF = fecha[8:10] + "/" + fecha[5:7] + "/" + fecha[0:4] 
        return fechaF


        
    @api.model
    def _get_report_values(self, docids, data):
        """in this function can access the data returned from the button
        click function"""
        today = fields.Datetime.now()
        fecha = today.strftime('%d/%m/%Y')
        
   
        return {
            'docs': data['historial_paciente_data'],
            'titulo':'CONTROL DE PACIENTES EN HEMODIALISIS',
            'sw_fecha':data["sw_fecha"],
            'intervalo':data["intervalo"],
            'date_today': fecha,
            'm_observacion': self.m_observacion,
            'mayuscula': self.mayuscula,
            'fecha_formato':self.fecha_formato,
            
        }
        
