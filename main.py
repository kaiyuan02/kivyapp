import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import requests
import json
import time

Window.size = (458,500)
Window.clearcolor = ('#FFFFFF')

class LogInPage(Screen):
#    firebase_url = "https://pythonassignmentkivyapp-default-rtdb.asia-southeast1.firebasedatabase.app/.json"
    #button_get(retrieve), post(upload), put(update), and delete(remove)
    def login_button(self):
        pass

    def register_button(self):
        pass

#        print("Button Pressed")
#        json_data = '{"User ID": "abcd", "password": "123"}'
#        res = requests.patch(url=self.firebase_url, json=json.loads(json_data))
#        print(res)


class RegisterPage(Screen):
    def finishRegister_button(self):
        pass
    def backtoLogin_button(self):
        pass

class InfoPage(Screen):
    def gotoPicturing_button(self):
        pass

class PicturingPage(Screen):
    def capture_image(self):
        camera = self.ids.camera
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")
        #texture = Texture.create(size=(camera.width, camera.height), colorfmt='rgb')
        #texture.blit_buffer(camera.texture.pixels, colorfmt='rgb', bufferfmt='ubyte')
        #texture.save('captured_image.png')
        #print("Image captured and saved as captured_image.png")


class WindowManager(ScreenManager):
    pass


class myKivy(App):
    pass
    #def build(self):
    #    self.window = GridLayout()
    #    self.window.cols = 1
    #    self.window.rows = 10
    #    self.window.size_hint = (.6, .7)
    #    self.window.pos_hint = {'center_x': .5, 'center_y': .5}

    #    self.window.add_widget(Image(source=("OWL.png")))

    #   self.userName = Label(text="What is your name?", font_size=24, color='#000000')
    #    self.window.add_widget(self.userName)

    #    self.textInput01 = TextInput(multiline=False, size_hint=(1, .5))
    #    self.window.add_widget(self.textInput01)

    #    self.userAge = Label(text="What is your age?", font_size=24, color='#000000')
    #    self.window.add_widget(self.userAge)

    #    self.textInput02 = TextInput(multiline=False, size_hint=(1, .5))
    #    self.window.add_widget(self.textInput02)

    #    self.button = Button(text="Submit", font_size=24, bold=True, size_hint=(1, .5), background_color="94c71d",
    #                         background_normal="")
    #    self.button.bind(on_press=self.calling)
    #    self.window.add_widget(self.button)

     #   return self.window

    #def calling(self, instance):
    #    self.userName.text = "Hello " + self.textInput01.text + " !"
    #   self.userAge.text = "Your age: " + self.textInput02.text


if __name__ == "__main__":
    myKivy().run()
