import reflex as rx

import elite_app.styles.styles as styles

from elite_app.components.navbar import navbar

text = """
Bienvenido a Elite app. En Elite app, valoramos su privacidad y nos comprometemos a proteger la seguridad de sus datos 
personales. Esta Política de Privacidad tiene como objetivo proporcionarle información clara y transparente sobre cómo 
recopilamos, utilizamos y compartimos sus datos en el contexto de nuestra aplicación Elite app. Al hacer uso de nuestros 
servicios, usted acepta las prácticas descritas en esta política.

Datos Recopilados:
Recopilamos datos de ubicación de su dispositivo móvil con el fin de habilitar la funcionalidad de recibir servicios cercanos 
en la aplicación Elite app, incluso cuando la aplicación está cerrada o no está siendo utilizada activamente.

Uso de los Datos:
Los datos de ubicación se utilizan exclusivamente para permitir la funcionalidad de recibir servicios cercanos en la aplicación 
Elite app. Estos datos solo se recopilan y utilizan cuando el usuario tiene una sesión activa en la plataforma, es decir, cuando 
ha iniciado sesión en la aplicación. No recopilamos ni utilizamos datos de ubicación cuando el usuario decide cerrar sesión en la 
plataforma.

Compartir los Datos:
Los datos de ubicación recopilados se utilizan únicamente para el servicio específico de Elite app y no se comparten con 
ninguna otra plataforma, empresa o entidad. Su privacidad es de suma importancia para nosotros y nos comprometemos a 
protegerla.

Seguridad de los Datos:
En Elite app, implementamos medidas de seguridad adecuadas para proteger sus datos personales contra el acceso no autorizado, 
la divulgación, la alteración o la destrucción. Utilizamos prácticas de seguridad estándar de la industria para proteger su 
información.

Sus Derechos:
Usted tiene derechos con respecto a sus datos personales, que incluyen el derecho a acceder, corregir, eliminar y objetar el 
procesamiento de sus datos. Si tiene alguna pregunta o solicitud relacionada con sus datos personales, no dude en ponerse en 
contacto con nuestro equipo de soporte a través de la aplicación Elite app.

Contacto: 
Si tiene alguna pregunta o inquietud sobre esta Política de Privacidad o sobre cómo tratamos sus datos personales, no dude en 
ponerse en contacto con nosotros en la dirección de correo electrónico contacto@elite-app.co.

Gracias por confiar en Elite app para sus necesidades de servicios cercanos. Nos comprometemos a brindarle la mejor experiencia 
posible mientras protegemos su privacidad y sus datos personales.
"""

def politicas_pagina() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.heading("Politicas De Privacidad De Elite App", align="center"),
                rx.divider(decorative=True),
                rx.chakra.text(text), 
            max_width=styles.MAX_WIDTH,
            width="100%",
            margin_y=styles.Size.DEFAULT
            )
        )
    )