# -*- coding: cp1251 -*- 
from pymorphy import get_morph # портируем необходимые модули
from pymorphy.contrib import tokenizers

morph = get_morph('C:/Python27/ru.sqlite-json/') # создаем объект класса pymorphy.Morph

text = (raw_input("Входные данные:  ")).decode('cp1251')

d = {} # словарь для хранения списка слов с одной нормальной формой
a = set() # множество, не допускающее повторений нормальных форм
part_d = {} # словарь для грамматической информации слова
part_a  = set() # множество, не допускающее повторений слов

for word in tokenizers.extract_tokens(text): # выделяем токены, узнаем часть речи
    if word.isalpha() == True: # отсеиваем пунктуацию
        info = morph.get_graminfo(word.upper()) # находим грамм. информацию слова
        part = info[0]['class'] # часть речи слова
        gram_info = info[0]['info'] # грамм. информация слова
        nf = info[0]['norm'] # нормальная форма слова
        print str('{0}({1})').format(word.encode('cp1251'),part.encode('cp1251')),
        # учитываем только сущ, глаголы и прил
        if part == u'С' or part == u'Г' or part == u'П' or part == u'ИНФИНИТИВ':
            # для имени не подбираем синоним
            if u'имя' in info[0]['info']:name = 1
            else:
                len_ = len(a)
                a.add(nf)
                if len_ == len(a): # есть ли уже такая нормальная форма?
                    l = d[nf]      # если есть, то добавляем слово в конец списка
                    l.append(word)
                    d[nf] = l
                else:              # иначе создаем ключ со значением списка
                    l = [word]
                    d[nf] = l
                    
                len_ = len(part_a)
                part_a.add(word)
                if len_ != len(part_a): # соотносим слово и его грам. инфо
                    part_d[word] = gram_info
    elif word.isspace() == False:
      print word,

# Выводим словарь:
print "\n\nСловарь 'Нормальная форма : слова'"
for key, value in d.items():
    print key, ":",
    for i in range(len(value)):
        print value[i], ',',
    print 

t = open('abr2w.txt','r+').readlines() # считываем словарь построчно в список

d_synonym = {} # словарь, соотносящий синонимы со списком слов
a_synonym = set() # множество, не пропускающее одинаковые синонимы

for key in d.keys(): # проссматриваем все ключи словаря нормальных форм
    if len(d[key]) > 1: # если слов в списке больше одного, то синонимизируем
        for s in t: # проходим по строкам текста
            # парсим строку
            s = str(s)
            key_ = key.encode('cp1251')
            if s.upper().find(key_) == 0:
                if s.upper().find('СМ.') != -1:
                    index_s = s.upper().find('СМ.')
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
                    synonym = 'синоним не найден'
                synonym = synonym.replace(',', '')
                synonym = synonym.replace('(', '')
                synonym = synonym.replace(')', '')
                # теперь слова принадлежат не нормальной форме, а синониму 
                l = d[key]
                d_synonym[synonym] = l
                break

# Выводим словарь:
print "\nСловарь 'Синоним : слова', где кол-во слов > 1"
for key, value in d_synonym.items():
    print key, ":",
    for i in range(len(value)):
        print value[i], ',',
    print 

text = text.encode('cp1251') # перегоняем входной текст из юникода в ascii

for key, value in d_synonym.items(): # получаем ключ и значение по словарю синонимов
    for i in range(len(value)): # получаем слова из списка
        # находим слово и заменяем его на синоним, представленный в той же грам. форме
        start = text.find(value[i].encode('cp1251'))
        text = text[:start] + text[start+len(value[i]):]
        sub = morph.inflect_ru((key).decode('cp1251').upper(),part_d[value[i]])
        text = text[:start] + sub.encode('cp1251') + text[start:]

print "\nВыходные данные:", text    
