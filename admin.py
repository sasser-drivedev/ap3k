import messaging, sqlite3, calendar, time

db = sqlite3.connect('ap3k')
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
        print  "Saving contact information..."
        print "Done."
        cursor.execute('''INSERT INTO contacts(name, phone, email, sign, language, interval,timestamp)
                  VALUES(?,?,?,?,?,?,?)''', (name,phone,email,sign,language,interval,timestamp))
        db.commit()
        





init_contact()

