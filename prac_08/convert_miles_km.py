from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesKm(App):
    """Application class for converting miles to kilometers."""
    output_km = StringProperty()

    def build(self):
        """Build the application by loading the .kv layout file."""
        self.title = "Convert Miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self):
        """Calculate and display the conversion from miles to kilometers."""
        value = self.get_valid_number()
        result = value * MILES_TO_KM
        self.root.ids.output_km.text = str(result)

    def handle_increment(self, modify):
        """Increment the miles input by a specified amount."""
        new_value = self.get_valid_number() + modify
        self.root.ids.input_miles.text = str(new_value)

    def get_valid_number(self):
        """Retrieve and validate the input number; return 0 if invalid."""
        try:
            number = float(self.root.ids.input_miles.text)
            return number
        except ValueError:
            return 0


ConvertMilesKm().run()
