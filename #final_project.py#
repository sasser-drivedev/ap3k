'''
    Main Program
    Takes input to initialize an instance of the class Contact in the messaging.py module
    Inializes the data sources as instances of the CLass Source in the grabbers module
    Executes an infinite loop
    Every 15m a random data source is chosen and a payload is fetched, filtered, and translated
    (time interval can be adjusted down for evaluatin purposes, see line 
    and sent to the contact via email and SMS

'''
    
import messaging, grabbers, time, random, os, translate, filters, platform, transmit, calendar, sqlite3
from redis import Redis
from rq import Connection, Queue


debug = False
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

   
    db = sqlite3.connect('ap3k')
    cursor = db.cursor()
    cursor.execute('''SELECT name, phone, email, sign, language, interval FROM contacts''')
    for row in cursor:
        current_contact = messaging.Contact(row[0],row[1],row[2],row[3],row[4],row[5])
    


    print ''
    
    
    time.sleep(1)

    # main program endless loop
    run = True
    scope_sent = False
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
            if scope_sent and (scope_timestamp - calendar.timegm(time.gmtime()) >= 86400):
                scope_sent = False
            if not scope_sent:
                transmit.send_scope(current_contact)
                print 'Horoscope sent at %(time)s' % \
                    {'time':str(time.ctime())}
                scope_sent = True
                scope_timestamp = calendar.timegm(time.gmtime())
                print
            else:
                print 'Horoscope already sent today, moving on...'
                print ''
        time.sleep(current_contact.interval)  

if __name__ == '__main__':
  main()
