# -*- coding: cp1251 -*- 
from pymorphy import get_morph
from pymorphy.contrib import tokenizers

morph = get_morph('C:/Python27/ru.sqlite-json/')

text = (raw_input()).decode('cp1251')

d = {}
a = set()
part_d = {}
part_a  = set()

for word in tokenizers.extract_tokens(text):
    if word.isalpha() == True:
        info = morph.get_graminfo(word.upper())
        part = info[0]['class']
        gram_info = info[0]['info']
        nf = info[0]['norm']
        print str('{0}({1})').format(word.encode('cp1251'),part.encode('cp1251')),
        
        if part == u'Ñ' or part == u'Ã' or part == u'Ï' or part == u'ÈÍÔÈÍÈÒÈÂ':
            if u'èìÿ' in info[0]['info']:name = 1
            else:
                len_ = len(a)
                a.add(nf)
                if len_ == len(a):
                    l = d[nf]
                    l.append(word)
                    d[nf] = l
                else:
                    l = [word]
                    d[nf] = l
                    
                len_ = len(part_a)
                part_a.add(word)
                if len_ != len(part_a):
                    part_d[word] = gram_info
    elif word.isspace() == False:
      print word,


print "\n\nÑëîâàðü 'Íîðìàëüíàÿ ôîðìà : ñëîâà'"
for key, value in d.items():
    print key, ":",
    for i in range(len(value)):
        print value[i], ',',
    print 

t = open('abr2w.txt','r+').readlines()

d_synonym = {}
a_synonym = set()

for key in d.keys():
    if len(d[key]) > 1:
        for s in t:
            s = str(s)
            key_ = key.encode('cp1251')
            if s.upper().find(key_) == 0:
                if s.upper().find('ÑÌ.') != -1:
                    index_s = s.upper().find('ÑÌ.')
                    if s.upper().find(' ',index_s+1) != -1:
                        index_f = s.upper().find(' ', index_s+4)
                        synonym = s[index_s+4:index_f]
                    elif s.upper().find(',',index_s+1) != -1:
                        index_f = s.upper().find(',', index_s+4)
                        synonym = s[index_s+4:index_f]
                    else:
                        synonym = s[:index_s+3]
                elif s.upper().find(', ') != -1:
                    index_s = s.upper().find(', ')
                    index_f = s.upper().find(' ', index_s+2)
                    synonym = s[index_s+2:index_f]
                else:
                    synonym = 'ñèíîíèì íå íàéäåí'
                synonym = synonym.replace(',', '')
                synonym = synonym.replace('(', '')
                synonym = synonym.replace(')', '')

                l = d[key]
                d_synonym[synonym] = l
                break


print "\nÑëîâàðü 'Ñèíîíèì : ñëîâà', ãäå êîë-âî ñëîâ > 1"
for key, value in d_synonym.items():
    print key, ":",
    for i in range(len(value)):
        print value[i], ',',
    print 

text = text.encode('cp1251')

for key, value in d_synonym.items():
    for i in range(len(value)):
        start = text.find(value[i].encode('cp1251'))
        text = text[:start] + text[start+len(value[i]):]
        sub = morph.inflect_ru((key).decode('cp1251').upper(),part_d[value[i]])
        text = text[:start] + sub.encode('cp1251') + text[start:]

print "\nÂûõîäíûå äàííûå:", text    
