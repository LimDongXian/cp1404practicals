from kivy.lang import Builder
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.label import Label


class DynamicLabels(App):
    text = StringProperty()

    def __init__(self, **kwargs):
        super(DynamicLabels, self).__init__(**kwargs)
        self.names = ["Teu", "Bob", "Charlie", "Limdx", "Kyle"]
        self.names = ["Teu", "Bob", "Charlie"]  # added to test the dynamic widget

    def build(self):
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_widget()
        return self.root

    def create_widget(self):
        for name in self.names:
            print(name)
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicLabels().run()
