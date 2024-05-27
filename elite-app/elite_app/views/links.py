import reflex as rx

from elite_app.components.social import medias, apps, footermedias
from elite_app.views.constants import *
from elite_app.styles.colors import *

def social() -> rx.Component:
    return rx.container(
            rx.vstack(
            medias("Reservas Online! Que esperas", ONDELIGHT),
            rx.hstack(
                medias("Google Play", GOOGLE_PLAY_DOWNLOAD),
                medias("Apple Store", APPLE_STORE_DOWNLOAD),
            )
        ),
        height="100px"
    )

def redes() -> rx.Component:
    return rx.hstack(
        apps("Instagram", INSTAGRAM)
    )

def footersocials() -> rx.Component:
    return rx.vstack(
        footermedias("facebook", FACEBOOK),
        footermedias("instagram", INSTAGRAM),
        footermedias("message-circle", WHATSAPP),
        color=TextColor.FOOTER.value,
        padding_right="25em"
    )