'''
Translate Module
Migrated from BING API to GoSlate library
Better reliability and no rate-limits
Utilizes Google

'''


import goslate, logging, time

logging.basicConfig(filename='ap3k.log',level=logging.DEBUG)

def spanish(text_to_translate):
    logging.info('TRANSLATE - translating to Spanish...')
    gs = goslate.Goslate()
    es = gs.translate(text_to_translate, 'es')
    logging.info('TRANSLATE - Translation complete at %(time)s' % \
                 {'time':str(time.ctime())})
    logging.info('TRANSMIT - %(es_joke)s ' % \
                      {'es_joke':es})
    
    return es


