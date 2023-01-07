import os
import re

def open_and_extract(filepath, regex, line_match):
    with open(filepath) as input_file:
        lines = input_file.readlines()

        for line in lines:
            if line.startswith(line_match):
                match = regex.match(line)

                if match:
                    return match.group(1)

class TestVersion:
    def test_versions_match(self):
        version = None
        smf_version = None

        pyproject_ver = re.compile(r"version = \"(.*)\"")
        smf_pyx_ver = re.compile(r"__version__ = \"(.*)\"")

        version = open_and_extract("pyproject.toml", pyproject_ver, "version")
        smf_version = open_and_extract("src/smf.pyx", smf_pyx_ver, "__version__")

        assert version is not None
        assert smf_version is not None
        assert version == smf_version
