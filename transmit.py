import messaging, grabbers, time, random, os, translate, filters, platform

# intializing instances of grabbers.source 

chuck_norris = grabbers.Source('chuck norris jokes',
                               'http://api.icndb.com/jokes/random/', 
                               False,
                               None,
                               False,
                               None)
dog_pics = grabbers.Source('funny dog pics',
                           'https://nijikokun-thedogapi.p.mashape.com/random', 
                           True,
                           'dog_pics.headers',
                           False,
                           None)
memes = grabbers.Source('memes',
                        'http://api.lordofthememe.com/v1/posts/random.json', 
                        False,
                        None,
                        False,
                        None)
scope = grabbers.Source('Horoscope',
                        'http://widgets.fabulously40.com/horoscope.json?',
                        False,
                        None,
                        True,
                        None)



'''
send functions 
these call the grabbers, filters, translators, and use the send_sms and send_email class methods.

'''

def send_joke(name):
    print "fetching joke..." 
    data = chuck_norris.get_source()
    joke = data['value']['joke']
    joke.encode('ascii','ignore')
    print "checking for profanity..."  
    is_safe = filters.profanity(joke)
    if is_safe and name.language == 2:
        print "no profanity detected." 
        print joke
        print "translating to Spanish...", 
        es_joke = translate.spanish(joke)
        time.sleep(1)
        print "Done."
        print es_joke
        name.send_sms(es_joke)
        name.send_email('Another Check Norris Joke :) ',joke)
    elif not is_safe: 
        print "profanity detected, joke not sent"
        print ''
    else:
        print "no profanity detected." 
        print joke
        name.send_sms(joke)
        name.send_email('Another Check Norris Joke :) ',joke)
        
def send_dog_pic(name):
    print "fetching hilarious dog pic..." 
    with open(dog_pics.header_file,'r') as inf:
        api_key = eval(inf.read())
    data = dog_pics.get_source(payload=api_key)
    link = data['source']
    print link
    name.send_sms(link)
    name.send_email('Hilarious Dog Enclosed',link)

def send_meme(name):
    print "fetching meme..." 
    data = memes.get_source()
    meme = data['post']['image']
    name.send_sms(meme)
    name.send_email('Check this out..',meme)
    print meme

def send_scope(name):
    print 'fetching horoscope...'
    sign = {'sign':name.sign}
    data = scope.get_source(payload=sign)
    horoscope = data['horoscope']['horoscope']
    horoscope = horoscope.encode('ascii','ignore')
    if name.language == 2:
        print horoscope
        print 'Translating to Spanish...'
        es_horoscope = translate.spanish(horoscope)
        es_horoscope = es_horoscope.encode('ascii','ignore')
        print es_horoscope
        name.send_sms(es_horoscope)
        name.send_email('Your horoscope...',es_horoscope)
    else:
        print horoscope
        name.send_sms(horoscope)
        name.send_email('Your horoscope...',horoscope)
    
