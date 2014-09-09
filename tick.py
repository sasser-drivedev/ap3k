
import messaging, grabbers, time, random, os, translate, filters, platform, transmit, calendar, sqlite3, logging, json
from redis import Redis
from rq import Connection, Queue

run = True
logging.basicConfig(filename='ap3k.log',level=logging.DEBUG)
if 'Win' in platform.system():
        os.system('cls')
else:
        os.system('clear')

logging.info('TICKER - Loading config file')
print('TICKER - Loading config file')
config = json.load(open('ap3k.cfg'))
logging.info('TICKER - Connecting to the contacts database...')
print('TICKER - Connecting to the contacts database...')
db = sqlite3.connect('ap3k')
cursor = db.cursor()   

logging.info('TICKER - %(db)s made at %(time)s' % \
             {'db':str(db),'time':str(time.ctime())})
print('TICKER - %(db)s made at %(time)s' % \
             {'db':str(db),'time':str(time.ctime())})
logging.info('TICKER - Ticker starting at %(time)s at a %(intv)s sec interval' % \
             {'time':str(time.ctime()),'intv':config['ticker']})
print('TICKER - Ticker starting at %(time)s at a %(intv)s sec interval' % \
             {'time':str(time.ctime()),'intv':config['ticker']})

scope_sent = False
scope_timestamp = 1
#go = True
def tick():
    
    global scope_sent, scope_timestamp
    print ('TICKER - tick started at %(time)s' % \
            {'time':str(time.ctime())})
    q = Queue(connection=Redis())
    cursor.execute('''SELECT name, phone, email, sign, language, interval, timestamp FROM contacts''')
    for row in cursor:
        current_contact = messaging.Contact(row[0],row[1],row[2],row[3],row[4],row[5],False)
	timestamp = row[6]
        current_time = int(calendar.timegm(time.gmtime()))
        interval = current_contact.interval*60
        next_send = int(interval - (current_time - timestamp))
        if current_time - timestamp >= interval:
                go = True
                print ('TICKER - Contact: %(name)s - Interval: %(int)s mins - Transmission SENT at %(time)s' % \
                       {'name':current_contact.name,'int':current_contact.interval,'time':str(time.ctime())})
                cursor.execute('''UPDATE contacts SET timestamp = ? WHERE name = ? ''', 
                       (current_time, current_contact.name))
                
        else:
                go = False
                print ('TICKER - Contact: %(name)s - Interval: %(int)s mins - NOTHING SENT - Next Transmission in %(next)s seconds' % \
                       {'name':current_contact.name,'int':current_contact.interval,'next':next_send})
        num = random.randint(1,4)
        #num = 1
        if num == 1 and go:
            q.enqueue(transmit.send_joke, current_contact)
        elif num == 2 and go:
            q.enqueue(transmit.send_dog_pic, current_contact)
        elif num == 3 and go:
            q.enqueue(transmit.send_meme, current_contact)
        elif num == 4 and go:
            if scope_sent and (scope_timestamp - calendar.timegm(time.gmtime()) >= 86400):
                scope_sent = False
            if not scope_sent:
                q.enqueue(transmit.send_scope, current_contact)
                scope_sent = True
                scope_timestamp = calendar.timegm(time.gmtime())
                print
            else:
                print 'Horoscope already sent today, moving on...'
                print ''
                tick()
    db.commit()    
    print ('TICKER - tick ended at %(time)s' % \
            {'time':str(time.ctime())})
    
                
while run:
    tick()
    config = json.load(open('ap3k.cfg'))
    run = bool(int(config['run']))
    time.sleep(int(config['ticker']))
