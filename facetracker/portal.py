import gi
gi.require_version("Xdp", "1.0")
from gi.repository import GLib
from gi.repository import Xdp

portal = Xdp.Portal.new()