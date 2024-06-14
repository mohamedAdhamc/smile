import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="smile")
        self.set_default_size(700, 700)