from kivy.app import App
from kivy.lang import Builder


class ConvertMilesKm(App):
    def build(self):
        self.title = "Convert Miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertMilesKm().run()