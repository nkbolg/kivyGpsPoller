from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from plyer import gps


class GPSDemo(BoxLayout):
    def __init__(self, **kwargs):
        super(GPSDemo, self).__init__(**kwargs)

        self.gps = gps
        self.gps.configure(on_location=self.on_location)

        self.orientation = 'vertical'
        self.label = Label(text='Waiting for GPS data...')
        self.add_widget(self.label)

        self.start_gps()

    def start_gps(self):
        try:
            self.gps.start()
        except NotImplementedError:
            self.label.text = 'GPS is not available on your platform'

    def on_location(self, **kwargs):
        self.label.text = f'Latitude: {kwargs["lat"]}, Longitude: {kwargs["lon"]}'


class MyApp(App):
    def build(self):
        return GPSDemo()


if __name__ == '__main__':
    MyApp().run()
