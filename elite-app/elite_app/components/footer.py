import reflex as rx
import datetime

import elite_app.styles.styles as styles

from elite_app.views.constants import *
from elite_app.views.links import footersocials


def footer() -> rx.Component:
    return rx.hstack(
        rx.image(src=LOGO, width="5em"),
        rx.hstack(
            rx.text(f"Copyright © 2023-{datetime.date.today().year} elite-app"),
            rx.link("POLITICAS", href="politicas"),
                width="100%",
                margin_y=styles.Size.DEFAULT
        ),
        footersocials()
    )