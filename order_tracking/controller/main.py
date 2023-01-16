# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class OrderTracking(http.Controller):
    @http.route('/order_tracking', type='http', auth='public', website=True)
    def menu_page(self):
        print('-------------------------------------------------')
        order = request.env['stock.picking'].sudo().search([('backorder_id', '=', False)])
        print('order------>',order)
        return request.render('order_tracking.track_order_temp', {'order': order, 'check': False})
#

    @http.route(['/order_tracking/details'], type='http', auth="public", website=True)
    def details_form(self, **post):

        print("post-------->", post)
        post_order = post.get('name')
        order_details = request.env['stock.picking'].sudo().search([('backorder_id', '=', False)])
        order_id = request.env['stock.picking'].sudo().search([('id', '=', post_order)])
        # orders = request.env['stock.move'].sudo().search([('id', '=', post_order)])

        print(order_id)
        order = order_id.name
        from_loc = order_id.location_id.complete_name
        to_loc = order_id.location_dest_id.complete_name
        product = order_id.move_line_nosuggest_ids
        print('order_id', order_id)
        print('prod', product)
        list = []
        for rec in product:
            print('rec.product_id.name')
            list.append(rec.product_id.name)
            print('qqqqqqqqqqq', list)

        return request.render('order_tracking.track_order_temp', {
            'check': True,
            'order': order_details,
            'order_no': order,
            'from_loc': from_loc,
            'to_loc': to_loc,
            'product': list,

        })

