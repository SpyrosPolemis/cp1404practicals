"""
CP1404 Practical_08
Kivy GUI program to convert miles to km
Spyros Polemis
Start: 11/11
Estimated time:
Actual: 35 minutes
"""
from kivy.app import App
from kivy.lang import Builder


class ConvertMilesApp(App):
    """Kivy app for converting miles to km."""

    def build(self):
        """Build the kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root


ConvertMilesApp().run()