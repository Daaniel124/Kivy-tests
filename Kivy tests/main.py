from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout

class BoxApp(App):
    def build(self):
        #Box Layout
        #-------
        #bl = BoxLayout(orientation = 'horizontal', padding = [50], spacing = 100)
        #bl.add_widget(Button(text = 'Кнопка 1'))
        #bl.add_widget(Button(text = 'Кнопка 2'))
        #bl.add_widget(Button(text = 'Кнопка 3'))
        #bl.add_widget(Button(text = 'Кнопка 4'))


        #Grid Layout
        #-------
        #bl = GridLayout(cols = 10, padding = [30], spacing = 3)
        #for i in range(50):
            #bl.add_widget(Button(text = '1'))


        #Anchor Layout
        #-------
        #bl = AnchorLayout(anchor_x = 'left', anchor_y = 'top')
        #bl.add_widget(Button(text = 'Кнопка', size_hint = [.5, .5]))


        #Login
        #-------
        al = AnchorLayout()
        bl = BoxLayout(orientation = 'vertical', size_hint = [.5, .5])

        bl.add_widget(TextInput())
        bl.add_widget(TextInput())
        bl.add_widget(Button(text = 'Войти'))

        al.add_widget(bl)
        return al

if __name__ == '__main__':
    BoxApp().run()
