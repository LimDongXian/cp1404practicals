from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Main application class for demonstrating Box Layout."""
    def build(self):
        """Build the application by loading the .kv layout file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Update the output label with a greeting message."""
        # print("test")
        # self.root.ids.output_label.text = "Hello "
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clear the input text and output label."""
        # print("clear")  # for testing use
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
