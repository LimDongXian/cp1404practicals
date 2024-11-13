from kivy.lang import Builder
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.label import Label


class DynamicLabels(App):
    """Application class for creating dynamic labels from a list of names."""
    text = StringProperty()

    def __init__(self, **kwargs):
        """Initialize the app with a list of names."""
        super(DynamicLabels, self).__init__(**kwargs)
        self.names = ["Teu", "Bob", "Charlie", "Limdx", "Kyle"]
        self.names = ["Teu", "Bob", "Charlie"]  # added to test the dynamic widget

    def build(self):
        """Build the application by loading the .kv layout file and creating widgets."""
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_widget()
        return self.root

    def create_widget(self):
        """Dynamically create labels for each name in the names list and add them to the layout."""
        for name in self.names:
            print(name)
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicLabels().run()
