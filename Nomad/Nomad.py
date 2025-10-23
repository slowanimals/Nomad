"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    def run(self):
        import main
        result = main.run()

        
class ForeachState(rx.State):
    from pathlib import Path
    trips: list[str] = [f.name for f in Path('Trips').iterdir()]
    
def card_trip(trip_name):
    return rx.box(
        rx.text(trip_name, font_family = 'BBH Sans Bartle', color = 'black', font_weight = 'bold', size = '5'), 
        bg = 'var(--gray-12)',
        border_radius = '25px',
        text_align = 'center',
        padding = '10px',
        width = '90%',
        height = '10%',
        _hover = {'background-color' : 'var(--gray-7)', 'cursor':'pointer'},
        box_shadow = '12px 15px 60px 1px var(--gray-11), inset 0.5px 0.5px 1px white, inset -0.5px -0.5px 1px white',
        ),

def gen_cardtrip():
    rx.foreach(ForeachState.trips, card_trip)

def index():
    return rx.box(
        rx.hstack(
            #map
            rx.box(
                rx.html("<iframe src='/themap.html' height='100%' width='100%' style='border:none; border-radius: 27px;'></iframe>",
                        height = '100%',
                        width = '100%',
                        display = 'block',
                        ),

                #border = '4px solid black',
                width = '70%',
                height = '90vh',
                margin_top = '10px',
                margin_left = '1.5%',
                border_radius = '30px',
                box_shadow = '3px 4px 40px 5px var(--gray-10), inset 0.3px 0.3px 2px white, inset -0.3px -0.3px 2px white',

            ),
            
            #dashboard
            rx.vstack(
                #title
                rx.box(
                    rx.text("Nomad", 
                            font_family = 'Bytesized', 
                            color = "white",
                            size = '9',
                            ),
                    bg = "var(--mauve-4)",
                    width = "50%",
                    padding = "3px",
                    margin_top = "15px",
                    margin_bottom = '20px',
                    #border = "4px solid var(--gray-8)",
                    border_radius = "20px",
                    style = {'user-select': 'none', 'font-size' : '5vw'},
                    _hover={'cursor':'pointer', 'font-weight':'bold'},
                    box_shadow = '3px 4px 60px 3px var(--gray-5), inset 0.3px 0.3px 2px white, inset -0.3px -0.3px 2px white',
                ),
                #trips
                rx.foreach(ForeachState.trips, card_trip),
                

                width = "30%",
                #border = "4px solid black",
                border_radius = "30px",
                align = "center",
                margin_right = "13px",
                margin_left = "10px",
                margin_top = "10px",
                margin_bottom = "10px",
                height = "97vh",
                bg = 'var(--mauve-10)',
                box_shadow = '10px 10px 30px 4px var(--mauve-7), inset 0.5px 1px 3px white, inset -0.5px -1px 2px white',
                overflow_y = 'auto',
                
            ),
            text_align = "center",
            justify = "end",
            bg = "var(--mauve-7)",
            height = "100vh",
            width = "100%",
            align = 'center',
            
        ),
        
        
    ),
   
        

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=BBH+Sans+Bartle&family=Bytesized&family=Coral+Pixels&family=Jacquard+12&family=Roboto:ital,wght@0,100..900;1,100..900&family=Rubik+Mono+One&family=Staatliches&display=swap"
    ],
)
app.add_page(index)