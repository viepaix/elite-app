import reflex as rx

from elite_app.components.social import medias, apps, footermedias
from elite_app.views.constants import *

def social() -> rx.Component:
    return rx.vstack(
        medias("Reservas Online", ONDELIGHT),
        rx.hstack(
            medias("Google Play", GOOGLE_PLAY_DOWNLOAD),
            medias("Apple Store", APPLE_STORE_DOWNLOAD),
        ),
        widht= "100%"
    )

def redes() -> rx.Component:
    return rx.hstack(
        apps("Instagram", INSTAGRAM)
    )

def footersocials() -> rx.Component:
    return rx.vstack(
        footermedias("facebook", FACEBOOK),
        footermedias("instagram", INSTAGRAM),
        footermedias("message-circle", WHATSAPP)
    )