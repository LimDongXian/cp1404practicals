from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesKm(App):
    output_km = StringProperty()

    def build(self):
        self.title = "Convert Miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self):
        value = self.get_valid_number()
        result = value * MILES_TO_KM
        self.root.ids.output_km.text = str(result)

    def handle_increment(self, modify):
        new_value = self.get_valid_number() + modify
        self.root.ids.input_miles.text = str(new_value)

    def get_valid_number(self):
        try:
            number = float(self.root.ids.input_miles.text)
            return number
        except ValueError:
            return 0


ConvertMilesKm().run()
