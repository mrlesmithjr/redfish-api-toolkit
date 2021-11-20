"""redfish_api_toolkit/__main__.py"""
# from redfish_api_toolkit.cli import cli_args
from redfish_api_toolkit.logger import setup_logger


def main():
    """Main execution of package."""

    # Setup root logger
    setup_logger()

    # Capture CLI arguments
    # args = cli_args()


if __name__ == "__main__":
    main()
