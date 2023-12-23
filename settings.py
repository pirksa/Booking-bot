import yaml


def load_config():
    with open('config.yml') as f:
        conf_dict = yaml.safe_load(f)
    return conf_dict
