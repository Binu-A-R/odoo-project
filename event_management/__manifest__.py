{
    'name': 'Events Management',
    'version': '16.0.1.0.0',
    'category':'Event Management',
    'summary': 'Managing online events and booking events',
    'description': 'Managing online events and booking events',
    'depends': [
        'base','mail'
     ],
    'data':[
        'security/ir.model.access.csv',
        'views/event_views.xml',
        'views/event_booking.xml',
        'views/event_service.xml'
    ],
    'installable': True,
    'application': True

}
