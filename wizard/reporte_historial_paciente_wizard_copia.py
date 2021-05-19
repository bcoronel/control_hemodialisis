# -*- coding: utf-8 -*-

from odoo import api, fields, models



from odoo.exceptions import ValidationError

#import logging, csv, operator
##Definimos la Variable Global
#_logger = logging.getLogger(__name__)
import logging.config
from time import time

from datetime import date
from datetime import datetime

formatter_string = "%d-%m-%y"



class ReoporteHistorialPacienteWizard(models.TransientModel):
    _name = 'hemodialisis.reporte.historial.paciente.wizard'
    paciente_id = fields.Many2one('hemodialisis_paciente', string='Cedula Paciente', required=True, 
                                   help='Ingrese número de cedula del paciente')
    nombre_paciente = fields.Char(string='Paciente')
    intervalo_fecha = fields.Boolean(string='Seleccionar Intervalo De Fecha', default=True)
    fecha_desde = fields.Date(string='Fecha Desde', help='Ingrese Fecha Desde', required=True)
    fecha_hasta = fields.Date(string='Fecha Hasta', help='Ingrese Fecha Hasta', required=True)



    @api.onchange('paciente_id')
    def generar_nombre(self):
        if self.paciente_id:
            self.nombre_paciente = self.paciente_id.nombre
            
    @api.onchange('intervalo_fecha')
    def val_intervalo_fecha(self):
        self.fecha_desde = ""
        self.fecha_hasta = ""
                    
    @api.onchange('fecha_desde')
    def val_fecha_desde(self):
        if self.fecha_desde:
            fechaActual = datetime.now().date()
            fechaDesde = self.fecha_desde
            if fechaDesde > fechaActual:
                raise ValidationError('La Fecha DESDE no puede ser mayor a la Fecha ACTUAL')


    @api.onchange('fecha_hasta')
    def val_fecha_hasta(self):
        if self.fecha_hasta:
            fechaDesde = self.fecha_desde
            fechaHasta = self.fecha_hasta
            if fechaDesde > fechaHasta:
                raise ValidationError('La Fecha HASTA no puede ser mayor a la Fecha DESDE')
            
            fechaActual = datetime.now().date()
            if fechaHasta > fechaActual:
                raise ValidationError('La Fecha HASTA no puede ser mayor a la Fecha ACTUAL')





    def action_report_historial_paciente(self):
        value=[]
        paciente_id = self.paciente_id.id
        
        
        sw_fecha = 0
        intervalo = ''
        fechaDesde = self.fecha_desde
        fechaHasta = self.fecha_hasta
        if fechaDesde != fechaHasta:
            intervalo = "INTERVALO FECHA DESDE " + str(fechaDesde) + " HASTA " + str(fechaHasta) 
        else:
           intervalo = "FECHA = " + str(fechaDesde)
                
        datas = {
            'ids' : self.env.context.get('active_ids',[]),
            'intervalo' : intervalo,
        } 
        
        query = "SELECT ht.*, hp.cedula, hp.nombre "
        query = query + " FROM hemodialisis_tratamiento ht "
        query = query + "inner join hemodialisis_paciente hp on ht.hemodialisis_paciente_id = hp.id "
        query = query + "where  ht.hemodialisis_paciente_id = " + str(paciente_id)
        query =  query + " and (ht.fecha_tratamiento>='" + str(fechaDesde) + "' and ht.fecha_tratamiento<='" + str(fechaHasta) + "') "
        query = query + " order by ht.fecha_tratamiento"
        
        self._cr.execute(query, value)
        record = self._cr.dictfetchall()
        
        datas['historial_paciente_data'] = record
        return self.env.ref('hemodialisis.action_report_historial_paciente').report_action(self, data=datas)        


        
 #       raise ValidationError('generar consulta')
        
"""
        sede = self.bienes_sedes_id.sedes_nombre
        oficina = self.bienes_oficinas_id.oficinas_nombre
        
        domain = []
        domain = [('bienes_oficinas_id','=',self.bienes_oficinas_id.id)]
        
        bienes_data = self.env['bienes'].search_read(domain,order='bienes_numbien asc')
        
        tot_costo = 0.00
        #Permite obtener total de bienes
        for rec in bienes_data:
            tot_costo = tot_costo + rec['costo']
        tot_costo = "{0:.7f}".format(tot_costo)
        
        #cantidad = self.env['bienes'].search_count(domain)
        cantidad = len(bienes_data)
        
        datas = {
            'ids' : self.env.context.get('active_ids',[]),
            'sede' : sede,
            'oficina' : oficina,
            'nro_bienes' : cantidad,
            'tot_costo': tot_costo, 
        }         
        
        if cantidad == 0:
            raise ValidationError('No existen Bienes asociado a la consulta realizada')
        else:
            datas['bienes_data'] = bienes_data
            return self.env.ref('bienes.action_report_bien_oficina').report_action(self, data=datas)
   
            
"""            
            

        
        
        
        

        
        
        
        
        #raise ValidationError('Hay Datos ' + str(oficina))
        
        ##fields = ['nombre','fecha_pago','estudiante_tarifa']
        #bienes_data = self.env['bienes'].search_read(domain, fields)

        #if bienes_data:
        #   raise ValidationError('Hay Datos')
        #raise ValidationError('NOOOOO Hay Datos')    


        #datas['estudiante_data'] = estudiante_data     
        #return self.env.ref('escuela.action_report_personalizado_estudiante').report_action(self, data=datas)




        #datas = {
        #    'ids' : self.env.context.get('active_ids',[]),
        #    'title' : self.title, 
        #    'date_init' : self.date_init,          
        #}
        #value=[]

        #Con execute
        
        
        #query = """SELECT * FROM escuela_estudiante as ee """
        #if self.date_init:
        #   date_init = str(self.date_init)
        #   query = query + "WHERE ee.fecha_pago <= '" + date_init + "'"
        #self._cr.execute(query, value)

        #record = self._cr.dictfetchall()
        #datas['estudiante_data'] = record
        #return self.env.ref('escuela.action_report_personalizado_estudiante').report_action(self, data=datas)


        #Sin execute 

        #domain = []
        #if self.date_init:
        #    domain = [('fecha_pago','<=',datas["date_init"])]
        #fields = ['nombre','fecha_pago','estudiante_tarifa']
        #estudiante_data = self.env['escuela.estudiante'].search_read(domain,fields)
        #datas['estudiante_data'] = estudiante_data     
        #return self.env.ref('escuela.action_report_personalizado_estudiante').report_action(self, data=datas)
        
       

            
