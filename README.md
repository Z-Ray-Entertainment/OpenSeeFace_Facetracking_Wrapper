# OpenSeeFace Facetracking Wrapper

<div style="text-align: center;">

![logo](https://codeberg.org/ZRayEntertainment/Facetracker/raw/tag/25.2.1/facetracker/data/icons/hicolor/scalable/apps/de.z_ray.Facetracker.svg)

</div>

Simple wrapper UI for OpenSeeFace's facetracker.

- Start / Stop the tracker
- Select Webcam
- Select video mode (width, height, frames per second)
- Select tracking model used by the facetracker
- Set IP and Port for the tracker to listen

<div style="text-align: center;">

![screenshot](https://codeberg.org/ZRayEntertainment/Facetracker/raw/tag/25.2.1/facetracker/data/screenshots/facetracker.png)
![screenshot](https://codeberg.org/ZRayEntertainment/Facetracker/raw/tag/25.2.1/facetracker/data/screenshots/facetracker_2.png)
![screenshot](https://codeberg.org/ZRayEntertainment/Facetracker/raw/tag/25.2.1/facetracker/data/screenshots/facetracker_3.png)

</div>

### Download

<div style="text-align: center;">
<a href="https://flathub.org/apps/de.z_ray.Facetracker">
  <img width='240' alt='Download on Flathub' src='https://dl.flathub.org/assets/badges/flathub-badge-en.png'/>
</a>
</div>

[Flathub Build Project](https://github.com/flathub/de.z_ray.Facetracker)

## Development Requirements

- gcc
- cmake
- cairo-devel
- python3-devel
- python3-pip
- gobject-introspection-devel
- v4l-utils
- typelib-1_0-Gtk-4_0
- typelib-1_0-Adw-1

### Setup

#### Gnome Builder
- Install Builder
- Open Source Directory of Facetracker
- Run

# Webcams tested
The following cams have been tested with this application in functioning and gathering device capabilities properly

- NB Pro: BisonCam
- Logitec C922 Pro Stream Webcam
- USB3.0 capture (yes an actual capture card)
- Logitec HD WebCam C270
- pulsonic HDR webcam
- Integrated Camera of Lenovo V15 G4 AMN