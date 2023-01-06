from Cython.Build import cythonize
from setuptools import setup, Extension
from subprocess import getstatusoutput


def pkgconfig(name):
    """
    Run pkg-config for the given package, and add the required flags to our
    list of build arguments.
    """
    status, output = getstatusoutput(f"pkg-config --libs --cflags {name}")
    if status:
        sys.exit(f"couldn't find package '{name}'")
    for token in output.split():
        opt, val = token[:2], token[2:]
        if opt == "-I":
            include_dirs.append(val)
        elif opt == "-l":
            libraries.append(val)
        elif opt == "-L":
            library_dirs.append(val)


include_dirs = []
libraries = []
library_dirs = []

pkgconfig("smf")

setup(
    ext_modules=cythonize(
        [
            Extension(
                name="smf",
                sources=[
                    "src/smf.pyx",
                ],
                include_dirs=include_dirs,
                libraries=libraries,
                library_dirs=library_dirs,
                extra_compile_args=[
                    "-fno-strict-aliasing",
                    "-Werror-implicit-function-declaration",
                    "-Wfatal-errors",
                ],
            )
        ],
        language_level=3,
    ),
)
