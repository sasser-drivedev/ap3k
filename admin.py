import messaging, sqlite3

db = sqlite3.connect('ap3k')
cursor = db.cursor()



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
        print "Done."
        cursor.execute('''INSERT INTO contacts(name, phone, email, sign, language, interval)
                  VALUES(?,?,?,?,?,?)''', (name,phone,email,sign,language,interval))
        db.commit()
        
        return current_contact





init_contact()
print current_contact.name

