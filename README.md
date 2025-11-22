# Nomad
A new way to visualize your journeys across the world!

<img width="648" height="473" alt="Screenshot 2025-11-20 at 2 58 15 PM" src="https://github.com/user-attachments/assets/708cabb5-f62d-41e3-ad82-0478e2896f76" />

## Installation
1. **Clone Repository**
   - `git clone https://github.com/slowanimals/nomad.git`
2. **Create Virtual Environment**
   - Mac/Linux:
     - `python3 -m venv venv`
     - `source venv/bin/activate`
   - Windows:
     - `python -m venv venv`
     - `venv\Scripts\activate`
     
3. **Install Dependencies**
   - `pip install -r requirements.txt`
4. **Run App**
   - `python3 nomad.py`
      - Go to the localhost link outputted in terminal (ex: `Running on http://127.0.0.1:8000`)
5. **_(Optional)_ Load in a Desktop Window (via PyFlaDesk)**
   - Scroll to the bottom of the file **app.py** until you see the line `app.run(port=8000, debug=True)`
      - Comment it out and then uncomment the line `init_gui(app)` to open Nomad in a separate desktop window

## How to Use:
- Click on **Upload** to upload any amount of images, then enter the name of the folder you want the images to go into
  - Entering the name of an existing folder will place the images in that folder
- Click on **Generate** to run the plotting engine after making any changes
  - OSMnx takes a bit of time to load new graph data, so the first generation attempt might take about a minute
- Click on **Delete** next to any trip name in order to delete its folder
- Click on **Clear Cache** to delete the cache
   - The cache saves OSMNx graph data, so generating after deleting the cache might take longer

## Features
- Rendering engine that
  - Plots images on a map
  - Draws polylines using OSMnx network graphs to approximate routes traveled 
- Interactive Folium map
- Dashboard that displays buttons, trips, and metrics
- Thumbnail generation via Pillow to show image previews
   - Thumbnail folder is automatically deleted and repopulated whenever map is regenerating
- Cache that encodes graph data in binary for efficient plotting

## Idea
I wanted to build a desktop app that uses images from your travels to help visualize all of your trips on one map. I also wanted to learn how network graphs work for routing in mapping apps, so I learned the OSMnx library in order to work with coordinates for constructing visual paths.

## Tech Stack
- OSMnx
- Folium
- Exifread
- Pillow
- Python
- Flask
- PyFladesk
- HTML5
- CSS3
  
## Features I'm Working On
- Toggle custom colors for polylines
- Enter descriptions for trips
- Edit trip names
- Update images within trips
- Map type customization



