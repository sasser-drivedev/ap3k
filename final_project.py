'''
Main Program
Takes input to initialize an instance of the class Contact in the messaging.py module
Inializes the data sources as instances of the CLass Source in the grabbers module
Executes an infinite loop
Every 15m a random data source is chosen and a payload is fetched, filtered, and translated
(time interval can be adjusted down for evaluatin purposes, see line 
and sent to the contact via email and SMS

'''



import messaging, grabbers, time, random, os, translate, filters, platform

if 'Win' in platform.system():
    os.system('cls')
else:
    os.system('clear')

print ''
print '                              ***AutoPoster 3000***'
print ''
print "this app will send jokes, pics, memes, ect to a contact of your choice throughout the day"
print ''
time.sleep(1)

# setup contact information

def init_contact():
    global current_contact
    print "Setup Contact Info"
    print ''
    name = raw_input('Name: ')
    phone = raw_input('Phone: ')
    email = raw_input('Email: ')
    sign = raw_input('Astrological Sign: ')
    language = raw_input('Language Preference? 1-English 2-Spanish: ')
    print  "Saving contact information..."
    current_contact = messaging.Contact(name, phone, email, sign, int(language))
    time.sleep(1)
    print "Done."
    return current_contact

init_contact()
print ''
time.sleep(1)

# intializing instances of grabbers.source 
print "Setting up data sources...", 

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
time.sleep(1)
print "Done."
print ''


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
    

# main program endless loop
run = True
print '***Started at %(time)s ***' % \
    {'time':str(time.ctime())}
print ''
while run:
    num = random.randint(1,4)
    if num == 1:
        send_joke(current_contact)
        print 'Joke sent at %(time)s' % \
            {'time':str(time.ctime())}
        print
    elif num == 2:
        send_dog_pic(current_contact)
        print 'Dog pic at %(time)s' % \
            {'time':str(time.ctime())}
        print
    elif num == 3:
        send_meme(current_contact)
        print 'Meme sent at %(time)s' % \
            {'time':str(time.ctime())}
        print
    elif num == 4:
        send_scope(current_contact)
        print 'Horoscope sent at %(time)s' % \
            {'time':str(time.ctime())}
        print
    time.sleep(15) # change this to 5 for evaluation purposes 
