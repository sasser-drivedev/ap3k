'''
Filters module
Profanity method takes string from final_project.py
Check for profnaity using the wdyl API
Returns a boolean value 'safe'

'''

import urllib, json, requests, time, logging

def profanity(text_to_check):
    logging.info('FILTERS - checking for profanity...')
    url = 'http://www.wdyl.com/profanity?'
    payload = {'q':text_to_check}
    r = requests.get(url,params=payload).content
    j = json.loads(r)
    if j['response'] == "false":
        safe = True
        logging.info('FILTERS - no profanity detected.')

    else:
        safe = False
        logging.warning('FILTERS - profanity detected, joke not sent')
    return safe
