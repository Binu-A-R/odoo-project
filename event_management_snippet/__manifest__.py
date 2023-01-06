{
    'name': "Latest Events Snippet",
    'version': '16.0.1.0.0',
    'summary': 'Snippet',
    'description': 'Snippet',
    'sequence': '1',
    'category': 'Latest events ',
    'depends': [
        'base', 'website', 'event_management'
    ],
    'data': [
        'views/snippet.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            '/event_management_snippet/static/src/js/snippet.js',
            # 'https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css'
        ]

    },
    'installable': True,
    'application': True
}
