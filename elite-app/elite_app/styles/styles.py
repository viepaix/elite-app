import reflex as rx

from enum import Enum


# Constants
MAX_WIDTH = "980px"

# Sizes

class Size(Enum):
    SMALL = "0.5em"
    DEFAULT = "1em"
    BIG = "2em"
    
GLOBAL_STYLES = {
    rx.button: {
        "width": "100%",
        "height": "100%",
        "background_color": "gray",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.SMALL.value
    }
}