from odoo import models, fields

class DiscountWizard(models.TransientModel):
    _name='discount.wizard'

    percent=fields.Float('Discount %')
    
    def make_discount(self):
        #active_id contains the id of the record from which this wizard is
        #called
        active_id=self.env.context.get('active_id',False)
        print('active_id',active_id)
        #active_ids is a list of ids of the records from which this wizard is
        #called
        active_ids=self.env.context.get('active_ids',False)
        print('active_ids',active_ids)
        #active_model contains the name of the model from which wizard id
        #called
        active_model=self.env.context.get('active_model',False)
        print('active_model',active_model)
        print('self.env.context', self.env.context)
        discount_percent=self.percent
        #browse method takes the id and creates the record object 
        order=self.env['restaurant.order'].browse(active_id)
        print('order+++++',order)
        total=order.order_total
        discount= total*discount_percent/100
        discounted_amount=total-discount
        order.write({'order_total':discounted_amount})






