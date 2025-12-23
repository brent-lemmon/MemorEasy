import sys
from pathlib import Path
import shutil
from .exceptions import *

# =========================================================================== #

"""
Find exiftool executable

Returns:
    Path to exiftool

Raises:
    DependencyError: If exiftool cannot be found
"""
def find_exiftool() -> str:

    exe_name = "exiftool.exe" if sys.platform.startswith("win") else "exiftool"

    # If bundle
    if getattr(sys, "frozen", False):
        base = Path(sys._MEIPASS)
        bundled = base / "bin" / exe_name
        if bundled.exists():
            return str(bundled)

    # Try system PATH
    system_path = shutil.which(exe_name)
    if system_path:
        return system_path

    raise DependencyError(
        "Exiftool not found. Please install exiftool or use the provided bundled executable."
        "For further installation instructions, reference the README."
    )

# =========================================================================== #

"""
Find ffmpeg executable.

Returns:
    Path to ffmpeg

Raises:
    DependencyError: If ffmpeg cannot be found
"""
def find_ffmpeg() -> str:

    exe_name = "ffmpeg.exe" if sys.platform.startswith("win") else "ffmpeg"

    # If bundle
    if getattr(sys, "frozen", False):
        base = Path(sys._MEIPASS)
        bundled = base / "bin" / exe_name
        if bundled.exists():
            return str(bundled)

    # Try system PATH
    system_path = shutil.which(exe_name)
    if system_path:
        return system_path

    raise DependencyError(
        "FFMpeg not found. Please install ffmpeg or use the provided bundled executable."
        "For further installation instructions, reference the README."
    )

# =========================================================================== #
