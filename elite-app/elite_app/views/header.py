import reflex as rx

from elite_app.views.constants import LOGO

def header() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.image(src=LOGO, width="40em", height="100%", border_radius="50%"),
            margin_right="20px",
            margin_left="10px"
        ), rx.vstack(
        rx.text("Elite Cab Service", size="8"),
        rx.text("El mejor servicio de taxi en todo DFW."),
        rx.text("""Bienvenidos a Elite Cab Service, su compañía de taxi de confianza en 
                el área metropolitana de Dallas-Fort Worth. Nos enorgullecemos de ofrecer 
                un servicio de transporte de primera clase que combina comodidad, puntualidad
                y seguridad, garantizando una experiencia de viaje inigualable para nuestros clientes.""")
        )
    )