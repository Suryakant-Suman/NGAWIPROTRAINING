import configparser

config = configparser.ConfigParser()
config.read("config/config.ini")


def get_url():
    return config["settings"]["url"]


def get_browser():
    return config["settings"]["browser"]


def get_explicit_wait():
    return int(config["settings"]["explicit_wait"])
