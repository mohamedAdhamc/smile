import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="smile")
        self.set_default_size(700, 700)

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        #add drawing area
        self.drawingArea = Gtk.DrawingArea()
        
        self.vbox.pack_start(self.drawingArea, True, True, 0)

        #add tool buttons in a box at the bottom
        self.toolBox = Gtk.Box(spacing=0)
        self.pictureButton = Gtk.Button(label="Picture")
        self.videoButton = Gtk.Button(label="Video")
        self.toolBox.pack_start(self.pictureButton, True, True, 0)
        self.toolBox.pack_start(self.videoButton, True, True, 0)    
        
        self.vbox.pack_start(self.toolBox, False, True, 0)    

        self.add(self.vbox)