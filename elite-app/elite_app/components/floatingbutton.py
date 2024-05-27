import reflex as rx

def floatingButton():
    return rx.box(
        rx.button(
            rx.icon("phone"),
            on_click=lambda: rx.redirect("tel:+1234567890"),
            style={"position": "fixed",
                "bottom": "20px",
                "right": "20px",
                "background-color": "#007bff",
                "color": "#fff",
                "border": "none",
                "border-radius": "50%",
                "width": "60px",
                "height": "60px",
                "display": "flex",
                "align-items": "center",
                "justify-content": "center",
                "box-shadow": "0 2px 10px rgba(0,0,0,0.2)",
                "cursor": "pointer",
                "font-size": "24px"
            }
        ),
        id="floatingButton"
    )