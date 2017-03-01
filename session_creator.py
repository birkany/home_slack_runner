import phue
import nest
from config import  read_value


def create_hue_session():
    bridge = read_value(hue_bridge)
    