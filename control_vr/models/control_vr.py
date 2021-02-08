# -*- coding: utf-8 -*- 
from odoo import models, fields 
class ControlVR(models.Model): 
    _name = 'controlvr'
    _description = 'Control VR'
    name = fields.Char('Cliente', required=True)
    producto = fields.Char('Producto a alquilar', required=True)
    fecha_alquilar = fields.Date('Fecha alquiler', required=True)
    fecha_finalizacion = fields.Date('Fecha finalización', required=True)
    horas_estimadas = fields.Integer('Estimacion horas de uso diarias', required=True)
    precio = fields.Integer('Precio en €', required=True)    
    supervisor = fields.Many2one('res.users', 'Supervisor', required=True)
    devuelto = fields.Boolean('¿Devuelto producto?', required=True) 
    descripcion = fields.Text('¿Por qué lo eliges?', required=True)