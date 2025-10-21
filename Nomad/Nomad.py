"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    def run(self):
        import main
        result = main.run

def index():
    return rx.vstack(
        #logo
        rx.box("Nomad", bg="gray.200", height="100px"),
        
        #map, dashboard
        rx.hstack(
            #map
            rx.box(
                rx.html("<iframe src='/themap.html'></iframe>")
            ),
            #dashboard
            rx.box("dashboard area", bg="gray.100", width="40%"),
        ),
    )

app = rx.App()
app.add_page(index)