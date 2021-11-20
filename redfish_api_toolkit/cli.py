"""redfish_api_toolkit/cli.py"""

import argparse
from redfish_api_toolkit.release import __package_name__, __version__


def cli_args():
    """Console script for redfish_api_toolkit."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--version", action="version", version=f"{__package_name__} {__version__}"
    )
    args = parser.parse_args()

    return args
