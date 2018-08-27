# coding: utf-8
from googletrans import Translator
translator= Translator(service_urls=[
'translate.google.com',
'translate.google.co.kr',
])
translations= translator.translate(['long long sentense'], dest='ko')
for tr in translations:
    print(tr.origin, '=>', tr.text)
    
