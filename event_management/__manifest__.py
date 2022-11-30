{
    'name': 'Events Management',
    'version': '16.0.3.0.0',
    'category':'Event Management',
    'sequence':'1',
    'summary': 'Managing online events and booking events',
    'description': 'Managing online events and booking events',
    'depends': [
        'base','mail'
     ],
    'data':[
        'security/ir.model.access.csv',
        'views/event_views.xml',
        'views/event_booking.xml',
        'views/event_service.xml',
        'data/event_type_data.xml',
        'data/event_service_data.xml',
        'views/catering.xml',
        'data/sequence.xml',
        'views/catering_menu.xml',

    ],
    'installable': True,
    'application': True

}
