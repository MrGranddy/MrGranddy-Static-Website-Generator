import json
import re

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
        raw_content = f.read()

    m = re.search("---((.|\n|\r)*)---", raw_content)
    metadata = m.group(1).strip()
    lines = metadata.splitlines()

    content = {}
    for line in lines:
        tokens = line.strip().split(":")
        key = tokens[0].strip()
        value = ":".join(tokens[1:]).strip()
        content[key] = value

    return content
