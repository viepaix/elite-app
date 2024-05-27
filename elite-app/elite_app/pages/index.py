import reflex as rx

import elite_app.styles.styles as styles

from elite_app.views.constants import *
from elite_app.views.links import social

def index() -> rx.Component:
    return rx.box(
        rx.section(
            rx.container(
                rx.heading("Tu servicio de Taxi en Dallas FW a la mano", size="5"),
                rx.vstack(
                    rx.text("App hecha de latinos para latinos", size="3"),
                    rx.text("""
                    Viaja por todo dallas y sus alrededores usando Elite,
                    deja las otras viejas aplicaciones y obten un 20% en tu primer viaje con el codigo:
                    """, rx.code("NewElite")),
                    align="center",
                    spacing="7"
                ), 
                rx.hstack(
                    rx.image(src=IMG1, 
                        alt="Elite taxi", 
                        width="28em"),
                    rx.vstack(
                        rx.heading("Pide tu servicio"),
                        rx.text("con alguna de nuestras plataformas o llamando al ", rx.link("+1 (469) 988-7767", href="tel:4699887767", size="4")),
                        social(),
                        align="center",
                        align_items="center"
                    )
                )
            ),
            align="center"
        )
    )