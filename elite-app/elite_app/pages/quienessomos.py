import reflex as rx

import elite_app.styles.styles as styles

from elite_app.views.constants import *
from elite_app.styles.colors import *
from elite_app.components.navbar import navbar
from elite_app.components.footer import footer
from elite_app.components.floatingbutton import floatingButton



def quienesSomos() -> rx.Component:
    return rx.box(
        navbar(),
        rx.section(
            rx.vstack(
            rx.text("Equipo de ", rx.text.strong("Elite")),
            rx.text("""Bienvenidos a Elite Cab Service, 
                    su mejor opción de transporte en Dallas. 
                    Somos una empresa de taxis comprometida a 
                    ofrecer un servicio de calidad, rápido y 
                    seguro para todos nuestros clientes. Nos 
                    enorgullece ser una compañía de latinos para 
                    latinos, entendiendo y atendiendo las necesidades 
                    específicas de nuestra comunidad con dedicación y 
                    esmero."""),
            rx.image(src=IMG2,
                     width=styles.Size.BIG), 
            bg_color=Color.BACKGROUND.value,
            color=TextColor.BODY.value
            ),
            rx.vstack(
                rx.section(
                    rx.heading("Elite Cab Service: Su Socio de Confianza para un Viaje Cómodo y Puntual en Dallas"),
                        rx.text("""
                                En Elite Cab Service, sabemos que cada viaje es importante. 
                                Ya sea que necesite transporte para ir al trabajo, una cita 
                                médica, o simplemente una salida nocturna, nuestros conductores
                                están preparados para llevarlo a su destino con puntualidad y
                                profesionalismo. Nuestros taxis están equipados con la última 
                                tecnología para garantizar una experiencia de viaje cómoda y eficiente.
                                Nuestra misión es proporcionar un servicio accesible y confiable, haciendo 
                                que moverse por Dallas sea una experiencia agradable. Valoramos a cada 
                                uno de nuestros clientes y trabajamos arduamente para ganarnos su confianza y preferencia.
                                """)
                    ),
                    rx.section(
                        rx.heading("Elite Cab Service: Transporte de Excelencia para la Comunidad Latina en Dallas"),
                        rx.text("""
                                En Elite Cab Service, redefinimos el concepto de transporte en Dallas.
                                Somos una empresa dedicada a ofrecer un servicio de taxis que combina
                                puntualidad, comodidad y seguridad, diseñado especialmente por latinos 
                                y para latinos. Nuestra meta es ser su aliado de confianza en cada trayecto, 
                                asegurando que llegue a su destino sin preocupaciones.
                                Nuestros taxis son operados por conductores experimentados y comprometidos, 
                                quienes entienden la importancia 
                                de un servicio al cliente excepcional. Cada viaje con Elite Cab Service es una 
                                oportunidad para demostrar nuestro compromiso con la excelencia, utilizando vehículos
                                modernos y bien mantenidos para su comodidad y seguridad.
                                """),
                    max_width=styles.MAX_WIDTH,
                    width="100%",
                    margin_y=styles.Size.DEFAULT
                    )
            ),
            footer(),
            floatingButton()
        )
    )