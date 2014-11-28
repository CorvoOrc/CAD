# -*- coding: cp1251 -*- 
import pyttsx

# Выбор голоса
Alena = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\Infovox Desktop v2.2\Alyona22k"

engine = pyttsx.init() # создаем двигатель с стандартным драйвером (текстировал на 'sapi5')

# Настройка голоса
rate = engine.getProperty('rate') # получаем скорость воспроизведения
engine.setProperty('rate', rate - 20) # слишком быстро, уменьшаем
engine.setProperty('voice', Alena) # используем голос Алены

stop = False 
while stop == False: # защита от случайного нажатия
    choose = (raw_input("Ввод из файла(F)/консоли(C): ")).decode('cp1251')
    if choose == 'F': # если выбрано считывание с файла
        text = open('input.txt', 'r+').readlines() # считываем построчно в файл
        for line in text: # построчно воспроизводим
            engine.say(line.decode('cp1251'))
        engine.runAndWait()
        stop = True
    elif choose == 'C': # если выбрано считывание с консоли
        text = (raw_input("Входные данные:  ")).decode('cp1251')
        engine.say(text) # воспроизводим полученный с консоли текст
        engine.runAndWait()
        stop = True
        

