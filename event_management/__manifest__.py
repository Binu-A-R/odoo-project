{
    'name': 'Events Management',
    'version': '16.0.4.0.0',
    'category':'Event Management',
    'summary': 'Managing online events and booking events',
    'description': 'Managing online events and booking events',
    'depends': [
        'base','mail','account_payment'
     ],
    'data':[
        'security/ir.model.access.csv',
        'views/event_views.xml',
        'views/event_booking.xml',
        'views/event_service.xml',
        'data/event_type_data.xml',
        'data/scheduled_action.xml',
        'data/event_service_data.xml',
        'views/catering.xml',
        'data/sequence.xml',
        'views/catering_menu.xml',
        'data/catering_menu_data.xml'

    ],
    'installable': True,
    'application': True

}
