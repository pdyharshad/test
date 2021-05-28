from odoo import models,fields,api
from odoo.exceptions import RedirectWarning, UserError, ValidationError, AccessError

class RestaurantOrderLine(models.Model):
    _name='restaurant.orderline'

    dish=fields.Char('Dish')
    quantity=fields.Integer('Quantity')
    price=fields.Float('Price', default=100)
    total=fields.Float('Total')
    order_id=fields.Many2one('restaurant.order', string='Order')
    state=fields.Selection([('new','New'),
                            ('kitchen','Kitchen'),
                            ('in_process','In Process'),
                            ('ready','Ready'),
                            ('delivered','Delivered'),
                            ('bill','Bill')])
    
    @api.model
    def create(self,vals):
        print('vals 1st time',vals)
        print('self',self)
        qty=vals.get('quantity',0)
        price=vals.get('price',0)
        vals.update({'total': qty*price})
        print('vals 2nd time',vals)
        return super(RestaurantOrderLine, self).create(vals)
    
    def write(self,vals):
        print('self', self)
        #self is a recordset
        print('vals', vals)
        if vals.get('quantity',False) or vals.get('price'):
            print('entering if statement')
            qty=vals.get('quantity',False)
            print('quantity',qty)
            price=vals.get('price',False)
            print('price',price)
            if not qty:
                print('in if not qty')
                qty=self.quantity
            if not price:
                print('in if not price')
                price=self.price
            print('quantity',qty)
            print('price',price)

            vals.update({'total':qty*price})
        print(vals)
        return super(RestaurantOrderLine,self).write(vals)
    
    def unlink(self):
        print(self)
        for order in self:
            if order.state in ['ready','delivered','bill']:
                raise ValidationError('You cannot delete an order once it is\
                processed')
        return super(RestaurantOrderLine,self).unlink()

    def set_new(self):
        vals={'state':'new'} 
        self.write(vals)
        return True

    def duplicate_order(self):
        print("self.waiter_id",self.waiter_id)
        print('self.waiter_id.name',self.waiter_id.name)
        print('self.waiter_id.id',self.waiter_id.id)
        print('self.waiter_id.age',self.waiter_id.age)
        print('self.waiter_id.dob',self.waiter_id.dob)
        vals={'dish':self.dish,
                'price':self.price,
                'quantity':self.quantity,
                'total': self.total,
                'waiter_id':self.waiter_id.id,
                'state':self.state}
        res=self.create(vals)
        return res
        

class RestaurantOrder(models.Model):
    _name='restaurant.order'

    customer=fields.Char('Customer')
    waiter_id=fields.Many2one('hotel.person',string='Waiter',
            domain=[('person_type','=','waiter')])
    order_line=fields.One2many('restaurant.orderline','order_id',string='OrderLines')
    order_total=fields.Float('Order Total')
