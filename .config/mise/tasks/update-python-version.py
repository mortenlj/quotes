#!/usr/bin/env python
#MISE description="Update the project to use a newer version of Python"
#USAGE arg <version> help="The version of Python to use, in the form <major>.<minor>"

import os
import re
import subprocess
from tempfile import NamedTemporaryFile


def _update_file(file_path, pattern, version):
    print(f"Updating {file_path} ...")
    with open(file_path, "r") as f:
        lines = f.readlines()
    with NamedTemporaryFile("w", delete=False) as f:
        for line in lines:
            if m := re.match(pattern, line):
                line = line.replace(m.group(1), version)
            f.write(line)
    os.replace(f.name, file_path)


def _update_pyproject(version):
    _update_file("backend/pyproject.toml", r"requires-python = \"~=(\d\.\d+)\"", version)
    _update_file("backend/pyproject.toml", r"target-version = [\"py(\d+)\"]", version.replace(".", ""))



def _update_mise(version):
    print("Telling mise to use the new version ...")
    subprocess.run(["mise", "use", f"python@{version}"], check=True)


def _sync_uv():
    print(f"Syncing virtualenv ...")
    subprocess.run(["uv", "sync"], check=True, cwd="backend")


def _update_earthfiles(version):
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in filenames:
            if filename == "Earthfile":
                earthfile_path = os.path.join(dirpath, filename)
                _update_file(earthfile_path, r"\s*FROM python:(\d\.\d+)", version)


def main():
    version = os.getenv("usage_version")
    print(f"Updating to Python {version} ...")
    _update_pyproject(version)
    _update_mise(version)
    _update_earthfiles(version)
    _sync_uv()


if __name__ == '__main__':
    main()
