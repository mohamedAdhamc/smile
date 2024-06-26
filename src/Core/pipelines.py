import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst


def createMainFeedPipeline():
        # Create the GStreamer pipeline using gst_parse_launch
        pipeline = Gst.parse_launch("v4l2src device=/dev/video0 ! videoconvert ! gtksink name=gtksink")
        return pipeline