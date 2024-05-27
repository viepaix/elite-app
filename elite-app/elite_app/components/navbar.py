import reflex as rx

import elite_app.styles.styles as styles

import elite_app.styles.styles as styles
import elite_app.styles.colors as colors

#from elite_app.routes import Route

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Elite Cab Service",
            height="100%",
            margin_x="100px",
        ),
            rx.chakra.breadcrumb(
            rx.chakra.breadcrumb_item(
                rx.chakra.breadcrumb_link("home", href="/")
            ),
            rx.chakra.breadcrumb_item(
                rx.chakra.breadcrumb_link("Blogs", href="blogs")
            ),
            rx.chakra.breadcrumb_item(
                rx.chakra.breadcrumb_link("Links", href="links")
            ),
            rx.chakra.breadcrumb_item(
                rx.chakra.breadcrumb_link("Conductor", href="conductores")
            ),
            rx.chakra.breadcrumb_item(
                rx.chakra.breadcrumb_link("Pasajero", href="monta")
            ),
            rx.chakra.breadcrumb_item(
                rx.chakra.breadcrumb_link("Quienes somos", href="quienesSomos")
            ),
            separator="  ",
        ),
        position="sticky",
        bg=colors.Color.SECONDARY,
        padding_x=styles.Size.SMALL,
        padding_y=styles.Size.SMALL,
        width="100%",
        z_index="999",
        justify="between"
    )
