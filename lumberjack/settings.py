from django.conf import settings

LOGGING = {
    'formatters': {
        'error':{
            '()':'lumberjack.formatters.tb.TracebackFormatter',
            'output':'terminal',
            },
        'sql' : {
            '()':'lumberjack.formatters.sql.SQLFormatter',
            'format':'[%(name)s] %(levelname)s (%(duration)sms) %(message)s',
            'output':'terminal',
        },
        'default' : {
            'format' : '[%(name)s] %(levelname)s %(message)s',
        },
    },
    'handlers' : {
        'sqlstream' : {
            'class' : 'logging.StreamHandler',
            'formatter' : 'sql',
        },
        'errorstream' : {
            'class' : 'logging.StreamHandler',
            'formatter' : 'error',
            },
        'stream' : {
            'class' : 'logging.StreamHandler',
            'formatter' : 'default',
        },
        #'errorarecibo' : {
        #    'class' : 'lumberjack.handlers.AreciboHandler',
        #    'server': 'http://your-arebico-instance.appspot.com/',
        #    'account': 'public_account_password',
        #    },
        # requires python-arecibo lib
    },
    'loggers' : {
        'django.db' : {
            'level' : 'DEBUG',
            'handlers' : ['sqlstream'],   #add additional handlers here (ie:email)
            },
        'django.errors' : {
            'level' : 'DEBUG',
            'handlers' : ['errorstream'],   #add additional handlers here (ie:email)
            },
        },
}

LOGGING = getattr(settings, 'LOGGING', LOGGING)