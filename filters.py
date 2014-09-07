'''
Filters module
Profanity method takes string from final_project.py
Check for profnaity using the wdyl API
Returns a boolean value 'safe'

'''

import urllib, json, requests

def profanity(text_to_check):
    url = 'http://www.wdyl.com/profanity?'
    payload = {'q':text_to_check}
    r = requests.get(url,params=payload).content
    j = json.loads(r)
    if j['response'] == "false":
        safe = True
    else:
        safe = False
    return safe
