import json

from utility.exceptions import EXTENSION_ERROR


def parse_config(config_path):

    ext = config_path.split(".")[-1]

    if ext != "json":
        message = (
            "Error: There seems to be a problem with '%s', please make sure the file extension is correct."
            % config_path
        )
        raise EXTENSION_ERROR("json", ext, message)

    with open(config_path, "r") as f:
        config = json.load(f)

    return config


def parse_content(content_path):

    ext = content_path.split(".")[-1]

    if ext != "md":
        message = (
            "Error: There seems to be a problem with '%s', please make sure the file extension is correct."
            % content_path
        )
        raise EXTENSION_ERROR("md", ext, message)

    with open(content_path, "r") as f:
        content = json.load(f)

    return content
