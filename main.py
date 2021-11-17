from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
import socket
global homework

def callback(instance):
    print('hello')

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'top'
        BoxLayout:
            orientation: 'vertical'
            size_hint: [1, .5]
            Button:
                background_color: (.54, .31, .70, 1)
                text: 'Домашняя задание'
                on_press: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'homework'
            Button:
                background_color: (.14, .30, .82, 1)
                text: 'Написать разработчику'
                on_press: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'developer'

            Button:
                text: 'Помощь'
                
                on_press: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'help'
                
            Button:
                text: 'Выйти'
                background_color: (1, 0, 0, 1)
                on_press: app.stop()

<HomeworkScreen>:
    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'top'
        BoxLayout:
            orientation: 'vertical'
            size_hint: [1, .5]
            Button:
                text: 'Узнать домашную работу'
                
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'homework2'
            
            Button:
                text: 'Написать домашную работу'
                
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'countHomework'
                
            Button:
                text: 'Назад'
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'menu'

<Homework2Screen>:
    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'top'
        BoxLayout:
            orientation: 'vertical'
            
            size_hint: [1, .5]

            Label:
                text: app.homework2
                font_size: 20
            
                color: '000000'

            Button: 
                text: 'Узнать домашную работу'

                on_release: root.callback()



            Button:
                text:'Назад'

                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'homework'

<countHomeworkScreen>:
    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'top'
        BoxLayout:
            orientation: 'vertical'
            
            size_hint: [1, .5]
            
            TextInput:

            Button:
                text: 'Отправить'

                on_release: root.callback(app.homework_out)
                
            Button:
                text: 'Назад'
                
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'homework'


<DeveloperScreen>
    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'top'
        BoxLayout:
            orientation: 'vertical'
            
            size_hint: [1, .5]
            
            TextInput:
                
            Button:
                text: 'Отправить разработчику'
                
            Button:
                text: 'Назад'
                
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'menu' 
                    
<helpScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'text'
            font_size: 20
            
            color: '000000'
            
        
        Button:
            text: 'Назад'
        
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'menu'
""")

# Declare both screens

class countHomeworkScreen(Screen):
    pass

class helpScreen(Screen):
    pass

class MenuScreen(Screen):
    pass


class HomeworkScreen(Screen):
    pass

class Homework2Screen(Screen):
    def callback(instance):
        home = open('homework.txt', 'w')

        try:
            client = socket.socket(

	        socket.AF_INET,      #Настройка протокола итернет
            socket.SOCK_STREAM,  #TCP/IP

	        )

            client.connect(
	        ("52.17.245.199", 1235)#подключается к серверу
            )

            client.send('homework'.encode('utf-8'))

            data = client.recv(2048)

            if data.decode('utf-8') == 'OK':

                data = client.recv(2048)

                home.write(data.decode('utf-8'))

        except:
            pass

        home.close()

class DeveloperScreen(Screen):
    pass


class TestApp(App):
    homework_read = open('homework.txt')
    homework2 = str(homework_read.read())

    homework_out = TextInput()

    def build(self):
        # Create the screen manager
        


        Window.clearcolor = (.9, .9, .9, 1)
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(HomeworkScreen(name='homework'))
        sm.add_widget(helpScreen(name='help'))
        sm.add_widget(DeveloperScreen(name='developer'))
        sm.add_widget(Homework2Screen(name='homework2'))
        sm.add_widget(countHomeworkScreen(name='countHomework'))

        return sm
    
    homework_read.close()

if __name__ == '__main__':
    TestApp().run()