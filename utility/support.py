import os, shutil
from utility.exceptions import NAME_MISMATCH_ERROR


def check_name_mismatch(config_name, template_name):

    if config_name != template_name:
        raise NAME_MISMATCH_ERROR(
            config_name,
            template_name,
            "Config and template name of a page should be the same.",
        )


def prepare_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

def copy_folder(source, target):
    if os.path.exists(target):
        shutil.rmtree(target)
    shutil.copytree(source, target)