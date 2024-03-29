import messaging, sqlite3, calendar, time

db = sqlite3.connect('ap3k', timeout=10)
cursor = db.cursor()



def init_contact():
        print "Setup Contact Info"
        print ''
        name = raw_input('Name: ')
        phone = raw_input('Phone: ')
        email = raw_input('Email: ')
        sign = raw_input('Astrological Sign: ')
        language = raw_input('Language Preference? 1-English 2-Spanish: ')
        interval = raw_input('Send interval (minutes): ')
        timestamp = int(calendar.timegm(time.gmtime()))
       
        cursor.execute('''INSERT INTO contacts(name, phone, email, sign, language, interval,timestamp)
                  VALUES(?,?,?,?,?,?,?)''', (name,phone,email,sign,language,interval,timestamp))
        db.commit()
        cursor.execute('''SELECT id FROM contacts WHERE email=?''', (email,))
        result = cursor.fetchone()
        contact_id = int(result[0])
        next_run = timestamp + (int(interval) * 60)
        print contact_id
        
        print 
        cursor.execute('''INSERT INTO run(contact_id, last_run, next_run)
                  VALUES(?,0,?)''',(contact_id, next_run))
        print  "Saving contact information..."
        db.commit()
        print "Done."






init_contact()

