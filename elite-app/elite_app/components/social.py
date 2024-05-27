import reflex as rx

import elite_app.styles.styles as styles


def medias(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(text, style=styles.button_tittle_style, width="100%", height="3em"),
        href=url,
        is_external=True,
    )

def apps(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(text),
        is_external=True,
        href=url
    )

def footermedias(text: str, url: str) -> rx.Component:
    return rx.flex(
        rx.icon(
            text, 
            on_click= rx.redirect(url),
            style={
                "cursor": "pointer"
            }
        )
    )