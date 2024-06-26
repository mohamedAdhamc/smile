import gi
import Core.pipelines as pipelines

gi.require_version("Gtk", "3.0")
gi.require_version('Gst', '1.0')
from gi.repository import Gtk, Gst


class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="smile")
        self.set_default_size(700, 700)

        self.connect("destroy", Gtk.main_quit)
        self.connect("realize", self.on_realize)

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        #add box for the feed
        self.feedBox = Gtk.Box()
        
        self.vbox.pack_start(self.feedBox, True, True, 0)

        #add tool buttons in a box at the bottom
        self.toolBox = Gtk.Box(spacing=0)
        self.pictureButton = Gtk.Button(label="Picture")
        self.videoButton = Gtk.Button(label="Video")
        self.toolBox.pack_start(self.pictureButton, True, True, 0)
        self.toolBox.pack_start(self.videoButton, True, True, 0)    
        
        self.vbox.pack_start(self.toolBox, False, True, 0)    

        self.add(self.vbox)

        self.show_all()

    def on_realize(self, widget):
        self.init_pipeline()

    def init_pipeline(self):
        # Initialize GStreamer
        Gst.init(None)

        # Create the GStreamer pipeline using gst_parse_launch
        self.pipeline = pipelines.createMainFeedPipeline()
        
        # Get the gtksink element from the pipeline
        self.gtksink = self.pipeline.get_by_name("gtksink")
        
        # Get the GtkWidget from gtksink
        # self.video_widget = self.gtksink.get_property("widget")
        self.video_widget = self.gtksink.props.widget
        self.feedBox.pack_start(self.video_widget, True, True, 0)
        self.gtksink.props.widget.show()

        # Start playing
        self.pipeline.set_state(Gst.State.PLAYING)

        # self.gtksink.set_window_handle(self.video_widget.get_window().get_xid())

        