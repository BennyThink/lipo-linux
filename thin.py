#!/usr/bin/env python3
# coding: utf-8
import contextlib
import subprocess
from pathlib import Path

from tqdm import tqdm


def check_universal(fp):
    f = Path(fp)
    with contextlib.suppress(UnicodeDecodeError):
        output = subprocess.check_output(['file', f]).decode("u8")
        if "Mach-O universal binary with 2 architectures" in output:
            return True


def extract(architecture, fp):
    f = Path(fp)
    with contextlib.suppress(subprocess.CalledProcessError):
        subprocess.check_call(['lipo', '-thin', architecture, '-output', f, f])


def thin_app(app, architecture):
    count = len(list(app.glob("**/*")))
    for file in tqdm(app.glob("**/*"), total=count, desc="Processing..."):
        if file.is_file() and check_universal(file):
            # extract.delay(architecture, file.as_posix())
            extract(architecture, file.as_posix())


if __name__ == '__main__':
    app_path = Path("/Users/benny/Downloads/new/")
    arch = "arm64"
    thin_app(app_path, arch)
