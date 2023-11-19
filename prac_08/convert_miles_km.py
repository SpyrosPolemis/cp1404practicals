"""
CP1404 Practical_08
Kivy GUI program to convert miles to km
Spyros Polemis
Start: 11/11
Estimated time: First session 10 minutes
Actual: 35 minutes
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesApp(App):
    """Kivy app for converting miles to km."""
    kilometres = StringProperty()

    def build(self):
        """Build the kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def adjust_miles(self, change):
        """Adjust miles by +-1 depending on user input."""
        try:
            miles = float(self.root.ids.miles_input.text)
            miles += change
            self.root.ids.miles_input.text = str(miles)
        except ValueError:
            if change == 1:
                self.root.ids.miles_input.text = "1"
            else:
                self.root.ids.miles_input.text = "-1"

    def convert_to_kilometres(self, miles):
        """Convert miles to kilometres."""
        try:
            miles = float(miles)
            kilometres = MILES_TO_KM * float(miles)
            self.root.ids.conversion_output.text = str(kilometres)
        except ValueError:
            pass


ConvertMilesApp().run()
