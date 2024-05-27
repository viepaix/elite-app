import reflex as rx

import elite_app.styles.styles as styles

from elite_app.components.navbar import navbar


def conductores() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
        rx.heading("Trabaja con nosotros"),
        rx.center(
            rx.flex(
                rx.text("Prueba")
                )
            )
        )
    )