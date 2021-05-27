from odoo import models,fields,api

class Person(models.Model):
    _name='hotel.person'

    name=fields.Char(string='Person')
    age=fields.Integer(string='Age')
    weight=fields.Float(string='Weight')
    dob=fields.Date(string='Date of birth')
    marital_status=fields.Boolean(string='Marital Status')
    joining_date=fields.Datetime(string='Joining Date')
    gender=fields.Selection([('male','Male'),
                            ('female','Female'),
                            ('transgender','Trasgender')
                            ])
    orders=fields.One2many('restaurant.order','waiter_id', string='Orders')
    person_type=fields.Selection([('customer','Customer'),
        ('waiter','Waiter'),
        ('chef','Chef')], default='waiter')
    chef_orders=fields.Many2many('restaurant.order',string='Chef Orders')
