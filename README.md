# Nomad
A new way to visualize your journeys across the world!

<img width="648" height="473" src="https://github.com/user-attachments/assets/9336fcb2-d760-4032-9615-fff20c9a0a0d">

## Install (Note: This project will soon be a downloadable app)
1. **Clone Repository**
   git clone https://github.com/slowanimals/nomad.git
2. **Create Virtual Environment**

   - Mac/Linux:
     python3 -m venv venv
     source venv/bin/activate
   - Windows:
     python -m venv venv
     venv\Scripts\activate
     
3. **Install Dependencies**
   pip install -r requirements.txt
4. **Run App**
   python3 nomad.py

## Tech Stack:
- OSMnx
- Folium
- Exifread
- Pathlib
- Pillow
- Python
- Flask
- HTML5
- CSS3

## Description
This application was largely inspired by Mark Twain's _The Innocents Abroad_, as I loved the idea of a private travel log detailing your adventures.
Nomad plots images from your travels on a world map and shows you metrics from the images' metadata so that you can visualize how much of the world you've
seen.

## Features
- Rendering engine that
  - Plots images on a map
  - Draws polylines using OSMnx network graphs to approximate routes traveled 
- Interactive Folium map
- Dashboard that displays buttons, trips, and metrics

Additionally, images turned into thumbnails via Pillow and plotted in their approximate location. 

## How to Use:
- Click on "Upload" to upload any amount of images, then enter the folder name you want the images to go into
  - Entering the name of an existing folder will enter the images into that folder
- Click on "Generate" to run the plotting engine after making any changes
  - The engine is heavy, so it may take a minute or so for the new map to generate
- Click on the "Delete" button next to trip names in order to delete the folder

## Features I'm Working On
- Toggle custom colors for polylines
- Enter descriptions for trips
- Edit trip names
- Update images within trips
- Map type customization


