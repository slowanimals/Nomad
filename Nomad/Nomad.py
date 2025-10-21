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
                rx.html("<iframe src='/themap.html'></iframe>"), height = "500px", width = "100%"
            ),
            #dashboard
            rx.box("dashboard area", bg="gray.100", width="30%"),
            height = "100vh",
            width = "100%",
            align_itmes = "stretch"
        ),
        height = "100vh",
        width = "100%",

    )

app = rx.App()
app.add_page(index)