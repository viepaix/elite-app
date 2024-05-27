import reflex as rx

from elite_app.styles.colors import *

def floatingButton():
    return rx.box(
        rx.button(
            rx.icon("phone"),
            on_click=lambda: rx.redirect("tel:+1234567890"),
            style={"position": "fixed",
                "bottom": "20px",
                "right": "20px",
                "background-color": Color.SECONDARY.value,
                "color": "#fff",
                "border": "none",
                "border-radius": "50%",
                "width": "50px",
                "height": "50px",
                "display": "flex",
                "align-items": "center",
                "justify-content": "center",
                "box-shadow": "0 2px 10px rgba(0,0,0,0.5)",
                "cursor": "pointer",
                "font-size": "16px"
            }
        ),
        id="floatingButton"
    )