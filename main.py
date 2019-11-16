from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ListProperty
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivymd.theming import ThemeManager
from kivy.animation import Animation



class RootWidget(ScreenManager):
    mainscreen__ = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard = self.android_back_click)
        self.previousscreen = "main"
        #Clock.schedule_interval(self.animation,1)
        

        
    def android_back_click(self, window, key, *largs):
        if key == 27 or key == 32:
            self.current = self.previousscreen
            return True
        
class MainScreen(Screen):
    colorpicker = ObjectProperty(None)
    color = ListProperty([1,0,0,1])
    def connectbluetooth(self):
        pass
        
    #hier wil ik nog dat de kleur word die je hebt aangetikt in het wheele maar daarvoor heb ik die id & root nodig enzo maar dat gaat net niet goed.
    def animate_button(self, widget, *args):
        anim = Animation(background_color=(0,0,0,1))
        anim.start(widget)
        anim.bind(on_complete=self.callback)
    '''    
    def animation(self, dtx):
        anim = Animation(btn_size=(60,60), t= 'in_quad', duration=0.5)
        anim +=Animation(btn_size=(70,70), t ='in_quad', duration=0.5)
        tgt = self.ids.cta
        anim.start(tgt)
    '''
    def sentcolor(self):
        print (self.colorpicker.color)
    def callback(self, *args):
        pass
        #background.color: self.colorpicker.color




class colourscreen(Screen):
    colorpicker = ObjectProperty(None)
    searchbar = ObjectProperty(None)
    color = ListProperty([1,0,0,1])
    
    def sentcolour(self):    
        print (self.colorpicker.color)
        pass
    
    def searchcolor(self):
        if (self.searchbar.text == 'zwart' or 'Zwart' or 'black' or 'Black'):
            #ik wil hier terug naar de kv om de achtergrond te veranderen maar weet niet hoe dat moet
            pass
        elif self.searchbar.text == 'wit':
            pass
        
        


class patternscreen(Screen):
    pass
        
class QinApp(App):
    theme_cls = ThemeManager()
    
    def build(self):
       # self.recv_stream, self.send_stream = get_socket_stream('linvor')
        self.theme_cls.theme_style = 'Dark'
        return Builder.load_file("main.kv")

if __name__ == "__main__":
    Builder.load_file("mycolorpicker.kv")
    QinApp().run()
