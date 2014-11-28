from pymorphy import get_morph # портируем необходимые модули
from pymorphy.contrib import tokenizers

morph = get_morph('C:/Python27/ru.sqlite-json/') # создаем объект класса pymorphy.Morph

text = (raw_input("Входные данные():  ")).decode('cp1251')
print "Выходные данные():",
for word in tokenizers.extract_tokens(text): # выделяем токены, узнаем часть речи
    if word.isalpha() == True: # отсеиваем пунктуацию
        info = morph.get_graminfo(word.upper())
        print str('{0}({1})').format(word.encode('cp1251'), info[0]['class'].encode('cp1251')),
    elif word.isspace() == False: # пробелы вводит print, их не выводим
        print word,
        
while True:
    q = (raw_input("\n\nПоказать расшифровку?Y/N: "))
    if q == 'Y':
        print 'С  - существительное'
        print 'П  - прилагательное'
        print 'МС - местоимение'
        print 'Г  - глагол в личной форме'
        print 'Н  - наречие'
        print 'ПРИЧАСТИЕ    - причастие'
        print 'ДЕЕПРИЧАСТИЕ - деепричастие'
        print 'ИНФИНИТИВ    - инфинитив'
        print 'МС-ПРЕДК     - местоимение предикатив'
        print 'МС-П   - местоимение прилагательное'
        print 'ЧИСЛ   - числительное(количественное)'
        print 'ЧИСЛ-П - порядковое числительное'
        print 'ПРЕДК  - предикатив'
        print 'ПРЕДЛ  - предлог'
        print 'СОЮЗ   - союз'
        print 'МЕЖД   - междометие'
        print 'ЧАСТ   - частица'
        print 'ВВОДН  - вводное слово'
        print 'КР_ПРИЛ- краткое прилагательное'
        print 'КР_ПРИЧАСТИЕ - краткое причастие'
        print 'ПОСЛ - пословица'
        break
    elif q != 'N':
        print 'Некорректный ввод',
    else:
        break

# Лабораторная работа №3, Стешенко А.С.
