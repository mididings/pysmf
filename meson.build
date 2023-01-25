project(
  'pysmf',
  'c', 'cython',
  version: '0.1.1',
)

cc = meson.get_compiler('c')
add_project_arguments(
  cc.get_supported_arguments([
    '-fno-strict-aliasing',
    '-Werror-implicit-function-declaration',
    '-Wfatal-errors',
  ]),
  language: 'c'
)

py = import('python').find_installation()

# Create the external C module using the python3 module helper function
py.extension_module(
  'smf',
  [ 'src/smf.pyx' ],
  dependencies : [ dependency('smf'), dependency('python3'), ],
  install: true,
)

# Run tests with `meson setup builddir && meson test -C builddir`
test('smf',
  py,
  args: [
    '-m',
    'pytest',
    '--verbose',
  ],
  workdir: meson.current_source_dir(),
  env: [ 'PYTHONPATH=' + meson.current_build_dir() ]
)
