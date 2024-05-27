"""Elite WEBSITE"""
import reflex as rx

import elite_app.styles.styles as styles

from elite_app.components.navbar import navbar
from elite_app.components.footer import footer
from elite_app.components.floatingbutton import floatingButton
from elite_app.views.header import header
from elite_app.views.links import social
from elite_app.pages.index import index as main
from elite_app.pages.politicas import politicas_pagina
from elite_app.pages.conductores import conductores
from elite_app.pages.quienessomos import quienesSomos as qs



class State(rx.State):
    pass

def quienesSomos():
    return qs()

def politicas():
    return politicas_pagina()

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                main(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.DEFAULT
            )
        ),
        footer(),
        floatingButton()
    )
        


app = rx.App(
    style=styles.GLOBAL_STYLES
)

app.add_page(index, route="/index")
app.add_page(politicas, route="/politicas")
app.add_page(qs, route="/quienesSomos")
app.add_page(conductores, route="/conductores")