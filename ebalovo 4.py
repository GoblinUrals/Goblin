
# import logging
# logging.basicConfig(filename='example.log',encoding='utf-8',level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this,too')
# logging.error('And non-ASCII stuff, too, like result and malno')

import requests

url = 'http://api.forismatic.com/api/1.0/'
payload  = {'method': 'getQuote', 'format': 'json', 'lang': 'ru'}
res = requests.get(url, params=payload))