'''
Translate Module
Migrated from BING API to GoSlate library
Better reliability and no rate-limits
Utilizes Google

'''


import goslate

def spanish(text_to_translate):
    gs = goslate.Goslate()
    es = gs.translate(text_to_translate, 'es')
    return es


