subdir('icons')
subdir('po')

gnome = import('gnome')

gschema_file = 'de.z_ray.Facetracker.gschema.xml'
install_data(gschema_file, install_dir: join_paths(get_option('datadir'), 'glib-2.0', 'schemas')
)

gnome.compile_schemas(build_by_default: true, depend_files: gschema_file)