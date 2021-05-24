#!/usr/bin/env python3

import glob
import os
import re
import subprocess  # nosec

import yaml

import scan_to_paperless.process_schema
from scan_to_paperless import get_config


def main() -> None:
    config = get_config()
    for folder in glob.glob(os.path.join(os.path.expanduser(config["scan_folder"]), "*")):
        print(re.sub(r".", "-", folder))
        print(folder)

        if not os.path.exists(os.path.join(folder, "config.yaml")):
            print("No config")
        else:
            with open(os.path.join(folder, "config.yaml")) as config_file:
                job_config: scan_to_paperless.process_schema.Configuration = yaml.safe_load(
                    config_file.read()
                )

            if os.path.exists(os.path.join(folder, "error.yaml")):
                with open(os.path.join(folder, "error.yaml")) as error_file:
                    error = yaml.safe_load(error_file.read())
                    if error is not None and "error" in error:
                        print(error["error"])
                        if isinstance(error["error"], subprocess.CalledProcessError):
                            print(error["error"].output.decode())
                            if error["error"].stderr:
                                print(error["error"].stderr)
                        if "traceback" in error:
                            print("\n".join(error["traceback"]))
                    else:
                        print("Unknown error")
                        print(error)
            else:
                allready_proceed = True
                if "transformed_images" not in job_config:
                    allready_proceed = False
                else:
                    for img in job_config["transformed_images"]:
                        img = os.path.join(folder, os.path.basename(img))
                        if not os.path.exists(img):
                            allready_proceed = False
                if allready_proceed:
                    if os.path.exists(os.path.join(folder, "REMOVE_TO_CONTINUE")):
                        print("To be validated")
                    if os.path.exists(os.path.join(folder, "DONE")):
                        print("Process finish")
                    else:
                        print("Waiting to be imported")
                else:
                    print("Not ready")
