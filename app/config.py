import logging
import sys
from os.path import abspath, exists, isfile

from yaml import YAMLError, safe_load

log = logging.getLogger(__name__)


class Settings:
    @staticmethod
    def _invalid_config_exit(message: str):
        log.error(
            "Unable to start due to error %s while parsing configuration file. Exiting...",
            message,
        )
        sys.exit(1)

    @staticmethod
    def _get_config(config_file_path: str) -> dict:  # type: ignore

        config_file_path = abspath(config_file_path)
        if not exists(config_file_path) or not isfile(config_file_path):
            Settings._invalid_config_exit(
                "Missing configuration file %s" % (config_file_path)
            )

        try:
            with open(config_file_path, "r") as f:
                config = safe_load(f)
                log.info(
                    f"Configuration read from file {config_file_path} with configurations: {config.keys()}"
                )
                return config

        except YAMLError as err:
            Settings._invalid_config_exit(
                f"Got exception when reading invalid YAML in {config_file_path} {err}"
            )
        except Exception as e:
            Settings._invalid_config_exit(
                f"Unknown error {e} reading configuration file {config_file_path}"
            )


settings = Settings._get_config("./config.yaml")
