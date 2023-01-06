# -*- coding: utf-8 -*-
from odoo import http
# from odoo.exceptions import ValidationError
from odoo.http import request


class WebsitePage(http.Controller):
    @http.route('/event_booking/form', type='http', auth='public', website=True)
    def event_page(self, **kw):
        customer = request.env['res.partner'].sudo().search([])
        event_type = request.env['event.property'].sudo().search([])
        return http.request.render('event_management.website_page', {'customer': customer, 'event_type': event_type
                                                                     })

    @http.route(['/event_booking/form/submit'], type='http', auth="public", website=True)
    def event_form_submit(self, **post):

        print(post)
        print('event-type---->', post.get('event_type'))
        booking = request.env['event.booking'].sudo().create({
            'event_type_id': int(post.get('event')),
            'partner_id': int(post.get('partner')),
            'booking_date': post.get('booking_date'),
            'start_date': post.get('start_date'),
            'end_date': post.get('end_date'),
        })

        welcome_drink = request.env['catering.menu'].sudo().search([('category', '=', 'Welcome Drink')])
        break_fast = request.env['catering.menu'].sudo().search([('category', '=', 'Break Fast')])
        lunch = request.env['catering.menu'].sudo().search([('category', '=', 'Lunch')])
        dinner = request.env['catering.menu'].sudo().search([('category', '=', 'Dinner')])
        snack_drinks = request.env['catering.menu'].sudo().search([('category', '=', 'Snacks and Drinks')])
        beverages = request.env['catering.menu'].sudo().search([('category', '=', 'Beverages')])
        price_subtotal = request.env['catering'].sudo().search([])

        vals = {
            'booking': booking,
            'welcome_drink': welcome_drink,
            'break_fast': break_fast,
            'lunch': lunch,
            'dinner': dinner,
            'snack_drinks': snack_drinks,
            'beverages': beverages,
            'price_subtotal': price_subtotal

        }
        print('vals--->',vals)

        booking.action_catering_service()

        return request.render("event_management.tmp_event_form_success", vals)

    @http.route(['/event_booking/form/submit/catering'], type='http', auth="public", website=True)
    def catering_form_submit(self, **post):
        print(post)

        catering = request.env['catering'].sudo().create({
            'event_id': post.get('event'),
            'guest': post.get('number_of_guest'),

        })
        print('catering---->', catering)

        if post.get('welcome'):
            catering.update({'is_welcome_drink': True,
                             'category_welcome_drink_ids': [(0, 0, {'menu_id': int(post.get('welcome')),
                                                                    'quantity': post.get('welcome_quantity')
                                                                    }
                                                             )]
                             }),
        if post.get('break_fast'):
            catering.update({'is_break_fast': True,
                             'category_break_fast_ids': [(0, 0, {'menu_id': int(post.get('break_fast')),
                                                                 'quantity': post.get('break_fast_quantity')
                                                                 }
                                                          )]
                             })

        if post.get('lunch'):
            catering.update({'is_lunch': True,
                             'category_lunch_ids': [(0, 0, {'menu_id': int(post.get('lunch')),
                                                            'quantity': post.get('lunch_quantity')
                                                            }
                                                     )]
                             })

        if post.get('dinner'):
            catering.update({'is_dinner': True,
                             'category_dinner_ids': [(0, 0, {'menu_id': int(post.get('dinner')),
                                                             'quantity': post.get('dinner_quantity')
                                                             }
                                                      )]
                             })

        if post.get('snack_drinks'):
            catering.update({'is_snack_drinks': True,
                             'category_snack_drinks_ids': [(0, 0, {'menu_id': int(post.get('snack_drinks')),
                                                                   'quantity': post.get('snack_drinks_quantity')
                                                                   }
                                                            )]
                             })

        if post.get('beverages'):
            catering.update({'is_beverages': True,
                             'category_beverages_ids': [(0, 0, {'menu_id': int(post.get('beverages')),
                                                                'quantity': post.get('beverages_quantity')

                                                                }
                                                         )]
                             })

        val = {
            'catering': catering,
        }
        catering.compute_grand_total()
        print('val', val)
        return request.render("event_management.tmp_catering_form_success", val)

    @http.route('/event_booking', type='http', auth='public', website=True)
    def create_tree_view(self):
        booking_tree = request.env['event.booking'].sudo().search([])
        val = {
            'booking_tree': booking_tree
        }
        return request.render('event_management.event_booking', val)
