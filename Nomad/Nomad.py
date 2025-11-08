"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

class UploadState(rx.State):
    folder_name: str = ""
    img: list[str]

    async def handle_upload(self, files: list[rx.UploadFile]):
        from pathlib import Path

        if not self.folder_name:
            print("No folder name set!")
            return

        out_dir = Path('assets/Trips') / self.folder_name
        out_dir.mkdir(parents=True, exist_ok=True)

        for file in files:
            upload_data = await file.read()
            outfile = out_dir / file.name

            with outfile.open("wb") as file_object:
                file_object.write(upload_data)

            self.img.append(str(outfile))



class RunState(rx.State):
    from typing import Any, Optional
    loading: bool = False
    progress: float = 0.0
    status: str = 'ready'
    result: Optional[dict] = None
    
    @rx.event(background=True)
    async def run(self):
        import main
        import multiprocessing as mp
        from concurrent.futures import ProcessPoolExecutor
        import time

        async with self:
            self.loading = True
            self.progress = 0.0
            self.status = "Starting…"
            yield

        # ----- 2. One-time multiprocessing manager (shared across runs) --
        if not hasattr(RunState, "_mgr"):
            RunState._mgr = mp.Manager()
        result_q: mp.Queue = RunState._mgr.Queue()
        prog_q: mp.Queue = RunState._mgr.Queue()

        # ----- 3. Submit the worker ------------------------------------
        def _worker():
            try:
                res = run_with_progress(prog_q)
                result_q.put(("success", res))
            except Exception as exc:
                tb = traceback.format_exc()
                result_q.put(("error", f"{exc}\n{tb}"))
            finally:
                result_q.put(("done", None))

        with ProcessPoolExecutor(max_workers=1) as pool:
            self._future = pool.submit(_worker)

            # ----- 4. Poll loop (keeps Reflex alive) --------------------
            while not self._future.done():
                # ---- progress updates -----------------------------------
                while not prog_q.empty():
                    prog = prog_q.get_nowait()
                    async with self:
                        self.progress = float(prog)
                        self.status = f"Processing… {prog:.1f}%"
                        yield

                # ---- keep the event alive --------------------------------
                await rx.sleep(0.15)          # < 1 s → no timeout
                async with self:
                    yield

            # ----- 5. Collect final result -------------------------------
            while not result_q.empty():
                typ, payload = result_q.get_nowait()
                if typ == "success":
                    async with self:
                        self.result = payload
                        self.status = "Complete!"
                        self.progress = 100.0
                        yield
                elif typ == "error":
                    async with self:
                        self.status = f"Error: {payload}"
                        self.progress = 0.0
                        yield

        # ----- 6. Clean up UI -------------------------------------------
        async with self:
            self.loading = False
            self._future = None
            yield
        
        

class ForeachState(rx.State):
    from pathlib import Path
    trips: list[str] = [f.name for f in Path('assets/Trips').iterdir()]
    
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
        style = {'user-select': 'none'},
        ),

def gen_cardtrip():
    rx.foreach(ForeachState.trips, card_trip)

def index():
    return rx.box(
        rx.hstack(
            #map
            rx.box(
                rx.cond(
                    RunState.loading,
                    rx.center(
                        rx.spinner(
                            size = '3'
                        ),
                        #border = '4px solid black',
                        height = '100%'
                    ),
                    rx.html("<iframe src='/themap.html' height='100%' width='100%' style='border:none; border-radius: 27px;'></iframe>",
                        height = '100%',
                        width = '100%',
                        display = 'block',
                        ),
                ),
                
                
                #border = '4px solid black',
                width = '70%',
                height = '90vh',
                margin_top = '10px',
                margin_left = '1.5%',
                border_radius = '30px',
                box_shadow = '0px 0px 60px var(--gray-11), inset 0.3px 0.3px 2px white, inset -0.3px -0.3px 2px white',

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
                    box_shadow = '0px 0px 60px var(--gray-7), inset 0.3px 0.3px 2px var(--mauve-11), inset -0.3px -0.3px 2px var(--mauve-11)',
                ),
                #generate map, add folder
                rx.hstack(
                    rx.button(rx.text("Generate Map", size = '6'),
                              _hover = {'cursor':'pointer', 'background-color':'var(--green-10)'},
                              height = '100%',
                              width = '50%',
                              border_radius = '15px',
                              on_click = rx.event(RunState.run()),
                              bg = 'var(--green-11)',
                              box_shadow = '0px 0px 10px var(--green-8), inset 0.3px 0.3px 2px white, inset -0.3px -0.3px 2px var(--green-11)',
                              ),
                    rx.button(rx.text("Add Trip", size = '6'),
                              _hover = {'cursor':'pointer', 'background-color':'var(--blue-10)'},
                              height = '100%',
                              width = '50%',
                              border_radius = '15px',
                              on_click = RunState.run(),
                              bg = 'var(--blue-11)',
                              box_shadow = '0px 0px 10px var(--blue-8), inset 0.3px 0.3px 2px white, inset -0.3px -0.3px 2px var(--blue-10)',
                              ),
                    #border = '4px solid black',
                    width = '90%',
                    height = '10%',
                    justify = 'center',
                    margin_bottom = '20px',
                    style = {'user-select': 'none'},
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