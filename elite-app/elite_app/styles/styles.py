import reflex as rx

from enum import Enum
from elite_app.styles.colors import *

# Constants
MAX_WIDTH = "980px"

# Sizes

class Size(Enum):
    SMALL = "0.5em"
    DEFAULT = "1em"
    MEDIUM = "1.25em"
    BIG = "2em"
    
GLOBAL_STYLES = {
    rx.button: {
        "width": "100%",
        "height": "100%",
        "background_color": Color.BACKGROUND.value,
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.SMALL.value
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

button_tittle_style = dict(
    font_size=Size.DEFAULT.value
)
button_body_style = dict(
    font_size=Size.SMALL.value
)