
import messaging, grabbers, time, random, os, translate, filters, platform, transmit, calendar, sqlite3, logging
from redis import Redis
from rq import Connection, Queue

if 'Win' in platform.system():
        os.system('cls')
else:
        os.system('clear')

db = sqlite3.connect('ap3k')
cursor = db.cursor()
run = True
scope_sent = False
scope_timestamp = 1

def tick():
    global scope_sent, scope_timestamp
    q = Queue(connection=Redis())
    cursor.execute('''SELECT name, phone, email, sign, language, interval FROM contacts''')
    for row in cursor:
        current_contact = messaging.Contact(row[0],row[1],row[2],row[3],row[4],row[5])
	num = random.randint(1,4)
        if num == 1:
            q.enqueue(transmit.send_joke, current_contact)
            #transmit.send_joke(current_contact)
            print 'Joke sent to %(name)s at %(time)s' % \
                {'time':str(time.ctime()), 'name':current_contact.name}
            print
        elif num == 2:
            #transmit.send_dog_pic(current_contact)
            q.enqueue(transmit.send_dog_pic, current_contact)
            print 'Dog pic to %(name)s at %(time)s' % \
                {'time':str(time.ctime()), 'name':current_contact.name}
            print
        elif num == 3:
            #transmit.send_meme(current_contact)
            q.enqueue(transmit.send_meme, current_contact)
            print 'Meme sent to %(name)s at %(time)s' % \
                {'time':str(time.ctime()), 'name':current_contact.name}
            print
        elif num == 4:
            if scope_sent and (scope_timestamp - calendar.timegm(time.gmtime()) >= 86400):
                scope_sent = False
            if not scope_sent:
                transmit.send_scope(current_contact)
                q.enqueue(transmit.send_scope, current_contact)
                print 'Horoscope sent to %(name)s at %(time)s' % \
                    {'time':str(time.ctime()), 'name':current_contact.name}
                scope_sent = True
                scope_timestamp = calendar.timegm(time.gmtime())
                print
            else:
                print 'Horoscope already sent today, moving on...'
                print ''
                tick()
        
        time.sleep(1)
                

while run:
    tick()
    time.sleep(5)
