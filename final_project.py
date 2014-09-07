'''
    Main Program
    Takes input to initialize an instance of the class Contact in the messaging.py module
    Inializes the data sources as instances of the CLass Source in the grabbers module
    Executes an infinite loop
    Every 15m a random data source is chosen and a payload is fetched, filtered, and translated
    (time interval can be adjusted down for evaluatin purposes, see line 
    and sent to the contact via email and SMS

'''
    

import messaging, grabbers, time, random, os, translate, filters, platform, transmit

debug = True

def main():
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
        interval = raw_input('Send interval (minutes): ')
        print  "Saving contact information..."
        current_contact = messaging.Contact(name, phone, email, sign, int(language),int(interval))
        time.sleep(1)
        print "Done."
        return current_contact

    if debug:
        current_contact = messaging.Contact('John', '6502008204', 'sasser.email.test@gmail.com', 'virgo', 2,5)
    else:
        init_contact()
    print ''
    time.sleep(1)

    # main program endless loop
    run = True
    print '***Started at %(time)s ***' % \
        {'time':str(time.ctime())}
    print ''
    while run:
        num = random.randint(1,4)
        if num == 1:
            transmit.send_joke(current_contact)
            print 'Joke sent at %(time)s' % \
                {'time':str(time.ctime())}
            print
        elif num == 2:
            transmit.send_dog_pic(current_contact)
            print 'Dog pic at %(time)s' % \
                {'time':str(time.ctime())}
            print
        elif num == 3:
            transmit.send_meme(current_contact)
            print 'Meme sent at %(time)s' % \
                {'time':str(time.ctime())}
            print
        elif num == 4:
            transmit.send_scope(current_contact)
            print 'Horoscope sent at %(time)s' % \
                {'time':str(time.ctime())}
            print
        time.sleep(current_contact.interval)  

if __name__ == '__main__':
  main()
