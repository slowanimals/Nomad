import webview
from pathlib import Path

app_path = (Path(__file__).parent / "src" / "index.html").resolve()

webview.create_window(
    "Nomad",
    app_path.as_uri(),
    width=1200,
    height=800,
    resizable=True
)


webview.start()