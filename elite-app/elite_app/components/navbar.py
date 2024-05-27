import reflex as rx

import elite_app.styles.styles as styles

from elite_app.styles.colors import *

#from elite_app.routes import Route

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Elite Cab Service",
            height="100%",
            margin_x="100px",
            size="6"
        ),
            rx.chakra.breadcrumb(
            rx.chakra.breadcrumb_item(
                rx.chakra.breadcrumb_link("home", href="/")
            ),
            rx.chakra.breadcrumb_item(
                rx.chakra.breadcrumb_link("Blogs", href="blogs")
            ),
            rx.chakra.breadcrumb_item(
                rx.chakra.breadcrumb_link("Conduce", href="conductores")
            ),
            rx.chakra.breadcrumb_item(
                rx.chakra.breadcrumb_link("Pasajero", href="monta")
            ),
            rx.chakra.breadcrumb_item(
                rx.chakra.breadcrumb_link("Quienes somos", href="quienesSomos")
            ),
            separator="  ",
            font_size=styles.Size.MEDIUM.value
        ),
        position="sticky",
        bg_color=Color.SECONDARY.value,
        color="rgb(255,255,255)",
        padding_x=styles.Size.SMALL,
        padding_y=styles.Size.SMALL,
        width="100%",
        z_index="999",
        justify="between"
    )
