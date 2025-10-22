"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    def run(self):
        import main
        result = main.run

def index():
    return rx.box(
        rx.vstack(
        #title
            rx.box(
                rx.text("Nomad", font_family = 'Bytesized', size = '9', color = "black"),
                bg = "var(--bronze-12)",
                width = "100%",
                padding = "10px",
                border_bottom = "4px solid var(--gold-8)",
            ),
            text_align = "center",
            align = "center",
        
            
        ),
        bg = "var(--sand-2)",
        height = "100vh",
        width = "100%"
        
    ),
   
        

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Bytesized&family=Coral+Pixels&family=Jersey+15&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap",
    ],
)
app.add_page(index)