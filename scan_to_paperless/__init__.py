import os.path
import sys
from typing import cast

from ruamel.yaml.main import YAML

if sys.version_info.minor >= 8:
    from scan_to_paperless import config as stp_config
else:
    from scan_to_paperless import config_old as stp_config  # type: ignore

CONFIG_FILENAME = "scan-to-paperless.yaml"

if "APPDATA" in os.environ:
    CONFIG_FOLDER = os.environ["APPDATA"]
elif "XDG_CONFIG_HOME" in os.environ:
    CONFIG_FOLDER = os.environ["XDG_CONFIG_HOME"]
else:
    CONFIG_FOLDER = os.path.expanduser("~/.config")

CONFIG_PATH = os.path.join(CONFIG_FOLDER, CONFIG_FILENAME)


def get_config() -> stp_config.Configuration:
    if os.path.exists(CONFIG_PATH):
        yaml = YAML(typ="safe")
        yaml.default_flow_style = False
        with open(CONFIG_PATH, encoding="utf-8") as config_file:
            return cast(stp_config.Configuration, yaml.load(config_file.read()))
    return {}
