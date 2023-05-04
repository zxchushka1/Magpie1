from kivy.config import Config

Config.set('graphics', 'resizable', '1')
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from random import randint


class Magpie(App):

    def build(self):

        bl = BoxLayout(orientation = 'vertical')
        gl = GridLayout(rows = 7, cols = 2)

        self.mainlbl = Label(text = 'Magpie', size_hint = [1, .1])
        self.lbl1 = Label(text = 'Исходое\nсообщние')
        self.lbl2 = Label(text = 'Зашифрованное\nсообщение')
        self.lbl3 = Label(text = 'Расшифрованное\nсообщение')

        self.okno1 = TextInput()
        self.okno2 = TextInput()
        self.okno3 = TextInput()

        self.zashifr = Button(text = 'Зашифровать')
        self.zashifr.bind(on_press = self.on_press_zashifr)
        self.rasshifr = Button(text = 'Расшифровать')
        self.rasshifr.bind(on_press = self.on_press_rasshifr)



        self.deleteall = Button(text = 'Обновить')
        self.deleteall.bind(on_press = self.on_press_deleteall)



        bl.add_widget(self.mainlbl)

        gl.add_widget(self.lbl1)
        gl.add_widget(self.okno1)
        gl.add_widget(Widget())
        gl.add_widget(self.zashifr)

        gl.add_widget(self.lbl2)
        gl.add_widget(self.okno2)
        gl.add_widget(Widget())
        gl.add_widget(self.rasshifr)

        gl.add_widget(self.lbl3)
        gl.add_widget(self.okno3)
        gl.add_widget(Widget())
        gl.add_widget(self.deleteall)

        bl.add_widget(gl)

        return bl




    def on_press_zashifr(self, instance):
        self.okno2.text = ''
        vstr = self.okno1.text
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890.,?!_"()+-=*/:;<>%[]`'
        obrstr = ''
        sdvig = ''
        scount = ''
        shifr = ''
        vstr = vstr.replace(' ', '_')
        for i in vstr:
            if i in alphabet:
                obrstr = obrstr + i
            for i in obrstr:
                random_number = randint(1, 99)
            sdvig = sdvig + str(random_number)
            if random_number < 10:
                scount = scount + '0'
            else:
                scount = scount + '1'
            if random_number > 149:
                random_number = random_number - 149
            ind = alphabet.index(i) + random_number
            if ind > 148:
                ind = ind - 149
            shifr = shifr + alphabet[ind]

        random_shifr = randint(0, 1)
        if random_shifr == 1:
            shifr = shifr[::-1]
        random_sdvig = randint(0, 1)
        if random_sdvig == 1:
            sdvig = sdvig[::-1]
        random_scount = randint(0, 1)
        if random_scount == 1:
            scount = scount[::-1]

        a = shifr + ' ' + sdvig + ' ' + scount + ' ' + str(random_shifr) + ' ' + str(random_sdvig) + ' ' + str(
            random_scount)
        self.okno2.text = a



    def on_press_rasshifr(self, instance):
        self.okno3.text = ''
        shifr_str = self.okno2.text
        alphabet1 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890.,?!_"()+-=*/:;<>%[]`'
        shifr_str = shifr_str.split()
        shifr = shifr_str[0]
        sdvig = shifr_str[1]
        scount = shifr_str[2]
        random_shifr = shifr_str[3]
        random_sdvig = shifr_str[4]
        random_scount = shifr_str[5]

        if random_shifr == '1':
            shifr = shifr[::-1]
        if random_sdvig == '1':
            sdvig = sdvig[::-1]
        if random_scount == '1':
            scount = scount[::-1]

        a = 0
        b = 0
        rasshifr = ''

        for i in shifr:
            if scount[a] == '1':
                sdvig_bukva = int(sdvig[b] + sdvig[b + 1])
                b = b + 2
                a = a + 1
            else:
                sdvig_bukva = int(sdvig[b])
                b = b + 1
                a = a + 1
            if sdvig_bukva > 148:
                sdvig_bukva = sdvig_bukva - 149
            if sdvig_bukva > alphabet1.index(i):
                ind_bukva = 149 - (sdvig_bukva - alphabet1.index(i))
            else:
                ind_bukva = alphabet1.index(i) - sdvig_bukva
            rasshifr = rasshifr + alphabet1[ind_bukva]
            rasshifr = rasshifr.replace('_', ' ')
            self.okno3.text = rasshifr

    def on_press_deleteall(self, instance):
        self.okno1.text = ''
        self.okno2.text = ''
        self.okno3.text = ''



Magpie().run()