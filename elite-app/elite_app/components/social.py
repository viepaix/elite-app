import reflex as rx

def medias(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(text, width="100%"),
        href=url,
        is_external=True,
        width="100%"
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