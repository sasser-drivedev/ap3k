import messaging, grabbers, time, random, os, translate, filters, platform, json, logging

logging.basicConfig(filename='ap3k.log',level=logging.DEBUG)

# intializing instances of grabbers.source 
sources_cfg = json.load(open('sources.cfg'))
logging.info('TRANSMIT - Initializing data sources...')

chuck_norris = grabbers.Source(sources_cfg['chuck_norris']['name'],
                               sources_cfg['chuck_norris']['url'],
                               bool(int(sources_cfg['chuck_norris']['headers'])),
                               sources_cfg['chuck_norris']['header_file'],
                               bool(int(sources_cfg['chuck_norris']['parameters'])),
                               sources_cfg['chuck_norris']['parameter_file'])

dog_pics = grabbers.Source(sources_cfg['dog_pics']['name'],
                               sources_cfg['dog_pics']['url'],
                               bool(int(sources_cfg['dog_pics']['headers'])),
                               sources_cfg['dog_pics']['header_file'],
                               bool(int(sources_cfg['dog_pics']['parameters'])),
                               sources_cfg['dog_pics']['parameter_file'])

memes = grabbers.Source(sources_cfg['memes']['name'],
                               sources_cfg['memes']['url'],
                               bool(int(sources_cfg['memes']['headers'])),
                               sources_cfg['memes']['header_file'],
                               bool(int(sources_cfg['memes']['parameters'])),
                               sources_cfg['memes']['parameter_file'])

scope = grabbers.Source(sources_cfg['scope']['name'],
                               sources_cfg['scope']['url'],
                               bool(int(sources_cfg['scope']['headers'])),
                               sources_cfg['scope']['header_file'],
                               bool(int(sources_cfg['scope']['parameters'])),
                               sources_cfg['scope']['parameter_file'])

logging.info('TRANSMIT - Data sources initialized at %(time)s' % \
             {'time':str(time.ctime())})

'''
send functions 
these call the grabbers, filters, translators, and use the send_sms and send_email class methods.

'''
def send_joke(name):
    logging.info('TRANSMIT - Fetching joke...')
    data = chuck_norris.get_source()
    joke = data['value']['joke']
    joke.encode('ascii','ignore')
    is_safe = filters.profanity(joke)
    if is_safe and name.language == 2:
        logging.info('TRANSMIT - Joke fetched:')
        logging.info('TRANSMIT -  %(joke)s' % \
                      {'joke':joke})
        logging.info('TRANSMIT - sending dog pic to%(name)s :' % \
                 {'name':name.name})
        es_joke = translate.spanish(joke)
        name.send_sms(es_joke)
        #name.send_email('Another Check Norris Joke :) ',joke)
        logging.info('TRANSMIT - Joke sent to %(name)s at %(time)s' % \
                {'time':str(time.ctime()), 'name':name.name})
    elif is_safe:
        logging.info('TRANSMIT - Joke fetched:')
        logging.info('TRANSMIT -  %(joke)s' % \
                      {'joke':joke})
        logging.info('TRANSMIT - sending dog pic to%(name)s :' % \
                 {'name':name.name})
        name.send_sms(joke)
        #name.send_email('Another Check Norris Joke :) ',joke)
        logging.info('TRANSMIT - Joke sent to %(name)s at %(time)s' % \
                {'time':str(time.ctime()), 'name':name.name})
        
def send_dog_pic(name):
    logging.info('TRANSMIT - fetching hilarious dog pic...')
    with open(dog_pics.header_file,'r') as inf:
        api_key = eval(inf.read())
    data = dog_pics.get_source(payload=api_key)
    link = data['source']
    logging.info('TRANSMIT - dog pic fetched:')
    logging.info('TRANSMIT - %(link)s' % \
                 {'link':link})
    logging.info('TRANSMIT - sending dog pic to%(name)s :' % \
                 {'name':name.name})
    name.send_sms(link)
    #name.send_email('Hilarious Dog Enclosed',link)
    logging.info('TRANSMIT - Dog pic sent to %(name)s at %(time)s' % \
                {'time':str(time.ctime()), 'name':name.name})

def send_meme(name):
    logging.info('TRANSMIT - fetching meme...')
    data = memes.get_source()
    meme = data['post']['image']
    logging.info('TRANSMIT - Meme fetched:')
    logging.info('TRANSMIT - %(meme)s' % \
                 {'meme':meme})
    logging.info('TRANSMIT - sending meme to %(name)s :' % \
                 {'name':name.name})
    name.send_sms(meme)
    #name.send_email('Check this out..',meme)
    logging.info('TRANSMIT - Meme sent to %(name)s at %(time)s' % \
                {'time':str(time.ctime()), 'name':name.name})

def send_scope(name):
    logging.info('TRANSMIT - fetching horoscope...')
    sign = {'sign':name.sign}
    data = scope.get_source(payload=sign)
    horoscope = data['horoscope']['horoscope']
    horoscope = horoscope.encode('ascii','ignore')
    logging.info('TRANSMIT - Horoscope fetched:')
    if name.language == 2:
        es_horoscope = translate.spanish(horoscope)
        es_horoscope = es_horoscope.encode('ascii','ignore')
        logging.info('TRANSMIT - %(scope)s' % \
                      {'scope':es_horoscope})
        logging.info('TRANSMIT - sending horoscope to%(name)s :' % \
                 {'name':name.name})
        name.send_sms(es_horoscope)
        #name.send_email('Your horoscope...',es_horoscope)
    else:
        logging.info('TRANSMIT - %(scope)s' % \
                      {'scope':horoscope})
        logging.info('TRANSMIT - sending horoscope to%(name)s :' % \
                 {'name':name.name})
        name.send_sms(horoscope)
        #name.send_email('Your horoscope...',horoscope)
    
