"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    def run(self):
        import main
        result = main.run

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
                box_shadow = '10px 10px 50px 5px var(--gray-11), -10px -10px 50px 5px var(--gray-11)',

            ),
            
            #dashboard
            rx.vstack(
            #title
                rx.box(
                    rx.text("Nomad", 
                            font_family = 'Bytesized', 
                            color = "black",
                            size = '9',
                            ),
                    bg = "var(--bronze-12)",
                    width = "50%",
                    padding = "3px",
                    margin_top = "5px",
                    border = "4px solid var(--gold-8)",
                    border_radius = "30px",
                    style = {'user-select': 'none', 'font-size' : '5vw'},
                    _hover={'cursor':'pointer', 'font-weight':'bold'}
                    
                ),
                width = "30%",
                #border = "4px solid black",
                border_radius = "30px",
                align = "center",
                margin_right = "13px",
                margin_left = "10px",
                margin_top = "10px",
                margin_bottom = "10px",
                height = "97vh",
                bg = 'var(--mauve-11)',
                #box_shadow = '10px 10px 50px 5px gray, -10px -10px 50px 0px gray'
                _hover = {'cursor':'pointer'},
                box_shadow = '12px 15px 30px 4px var(--mauve-7)',
                
            ),
            text_align = "center",
            justify = "end",
            bg = "var(--mauve-9)",
            height = "100vh",
            width = "100%",
            align = 'center',
            
        ),
        
        
    ),
   
        

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Bytesized&family=Coral+Pixels&family=Jersey+15&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap",
    ],
)
app.add_page(index)