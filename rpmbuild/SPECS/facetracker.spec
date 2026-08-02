Name:           facetracker
Version:        25.9
Release:        1%{?dist}
Summary:        Face tracking made easy - graphical interface for OpenSeeFace

License:        MIT
URL:            https://codeberg.org/ZRayEntertainment/Facetracker
Source0:        https://github.com/Z-Ray-Entertainment/Facetracker/archive/v%{version}/facetracker-%{version}.tar.gz

BuildRequires:  meson >= 0.62.0
BuildRequires:  ninja-build
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  pkgconfig
BuildRequires:  libgtk-4-devel
BuildRequires:  libadwaita-1-devel
BuildRequires:  python3-gobject
BuildRequires:  gobject-introspection-devel
BuildRequires:  glib2-devel
BuildRequires:  python3-pillow
BuildRequires:  python3-numpy

Requires:       python3
Requires:       python3-gobject
Requires:       gtk4
Requires:       libadwaita-1
Requires:       python3-pillow
Requires:       python3-numpy
Requires:       v4l-utils

%description
A graphical user interface to launch a face tracker locally on your machine
to gain tracking data from a webcam. These tracking data can then be used by
other applications like VTubbing Software to bring a virtual avatar to life.

Facetracker is a graphical user interface for OpenSeeFace, providing:
 * Start / Stop the tracker
 * Select Webcam
 * Select video mode (width, height, frames per second)
 * Select tracking model
 * Set IP and Port for the tracker to listen

%prep
%autosetup

%build
meson setup builddir --prefix=/usr
ninja -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install

%files
%{_bindir}/facetracker-gui
%{_datadir}/facetracker/
%{_datadir}/applications/de.z_ray.Facetracker.desktop
%{_datadir}/metainfo/de.z_ray.Facetracker.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/de.z_ray.Facetracker.svg
%{_datadir}/icons/hicolor/symbolic/apps/de.z_ray.Facetracker-symbolic.svg
%{_datadir}/locale/*/LC_MESSAGES/facetracker.mo
%license LICENSE
%doc README.md

%changelog
* Wed Sep 03 2025 Z-Ray Entertainment Packaging <packaging@z-ray.de> - 25.9-1
- Initial RPM package release