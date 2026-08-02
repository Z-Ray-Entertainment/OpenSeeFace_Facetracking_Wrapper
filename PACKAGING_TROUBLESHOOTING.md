# Facetracker Packaging Troubleshooting

Common issues and fixes for the Facetracker packaging builds.

## Build fails: `meson: command not found`

Install the Meson build system:

```bash
sudo apt-get install meson ninja-build
```

## AppImage crashes with `ModuleNotFoundError: No module named 'facetracker'`

The launcher script `usr/bin/facetracker-gui` ships with a hardcoded path `/usr/share/facetracker` that doesn't match the AppImage mount path. The workflow patches this to honour the `APPDIR` environment variable — if you built manually and skipped the patch, re-apply it:

```bash
sed -i 's|if environ.get("FLATPAK_ID") is not None:|if environ.get("APPDIR"):\n    pkgdatadir = environ.get("APPDIR") + pkgdatadir\nelif False:|' appdir/usr/bin/facetracker-gui
```

## AppImage launches but the UI is empty / no webcam shown

OpenSeeFace is not installed. Install it separately (see upstream README) or pass the `--no-tracker` flag to verify the GUI itself is working.

## Debian build fails: `dh: unknown sequence debhelper-compat`

Ensure `debhelper-compat (= 13)` is in `Build-Depends` and that `debian/compat` exists with `13`.

## RPM build fails: `rpmbuild: command not found`

On Ubuntu, install the `rpm` package:

```bash
sudo apt-get install rpm
```

## Python import errors for GTK / Adwaita

Ensure the typelib paths are set correctly. If running outside the AppImage:

```bash
export GI_TYPELIB_PATH=/usr/lib/x86_64-linux-gnu/girepository-1.0
```

## XDG_DATA_DIRS issues

The AppRun sets `XDG_DATA_DIRS` to include `${HERE}/usr/share`. If you launch `facetracker-gui` directly (without AppRun), do the same.

_Generated with AI assistance_
