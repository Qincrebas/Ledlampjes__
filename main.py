from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ListProperty
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivymd.theming import ThemeManager
from kivy.animation import Animation
#from jnius import cast,autoclass

#BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')
#BluetoothDevice = autoclass('android.bluetooth.BluetoothDevice')
#BluetoothSocket = autoclass('android.bluetooth.BluetoothSocket')
#UUID = autoclass('java.util.UUID')



class RootWidget(ScreenManager):
    mainscreen__ = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard = self.android_back_click)
        self.previousscreen = "main"
        Clock.schedule_interval(self.animation,2)
        Clock.schedule_interval(self.animation_, 2)
        
   #voor de knop naar de juiste kleur gaan 
    def animation(self, dtx):
        anim = Animation(btn_size=(80,80), t= 'in_quad', duration=1)
        anim +=Animation(btn_size=(100,100), t ='in_quad', duration=1)
        tgt = self.mainscreen__.ids.bluetooth
        anim.start(tgt)
        
    def animation_(self, dtx):
        anim = Animation(btn_size=(80,80), t= 'in_quad', duration=1)
        anim +=Animation(btn_size=(100,100), t ='in_quad', duration=1)
        tgt = self.mainscreen__.ids.reset
        anim.start(tgt)
        
    def android_back_click(self, window, key, *largs):
        if key == 27 or key == 32:
            self.current = self.previousscreen
            return True
        
class MainScreen(Screen):
    colorpicker = ObjectProperty(None)
    color = ListProperty([1,0,0,1])
    
    #hier wil ik nog dat de kleur word die je hebt aangetikt in het wheele maar daarvoor heb ik die id & root nodig enzo maar dat gaat net niet goed.
    def animate_button(self, widget, *args):
        anim = Animation(background_color=(0,0,0,1))
        anim += Animation(background_color=(1,1,1,0.50))
        anim.start(widget)
        anim.bind(on_complete=self.callback)   
     
    
    def sentcolor(self):
        print (self.colorpicker.color)
    def callback(self, *args):
        pass
        #background.color: self.colorpicker.color    
    
    def connectbluetooth(name):
        paired_devices = BluetoothAdapter.getDefailtAdapater().getBoundedDevices().toArray
        socket = None
        for device in paired_devices:
            if device.getName() == name:
                socket = device.createRfcommSocketToServiceRecord(
                    UUID.fromString("00001101-0000-1000-8000-00805F9B34FB"))
                recv_stream = socket.getInputStream()
                send_stream = socket.getOutputStream()
                break
        socket.connect()
        return recv_stream, send_stream
    
    def build(self):
        self.recv_stream, self.send_stream = connectbluetooth('linvor')
        return Builder.load_string(kv)
    
    def send(self, cmd):
        self.send_stream.write('{}\n'.format(cmd))
        self.send_stream.flush()
        
    def reset(self, btns):
        for btn in btns:
            btn.state = 'normal'
        self.send('0\n')
#Bluetooth().run()

        





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
            #text = 'very good'
            pass
        elif self.searchbar.text == 'wit':
            pass
        
        


class patternscreen(Screen):
    pass

class bluetoothscreen(Screen):
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
