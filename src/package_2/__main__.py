import logging

_LOGGER = logging.getLogger(__name__)
_LOGGING_FORMAT = "%(asctime)s %(levelname)s %(pathname)s %(message)s"
logging.basicConfig(
    format=_LOGGING_FORMAT,
    datefmt="%Y-%m-%d %H:%M:%S%z",
    handlers=[logging.StreamHandler()],
    level=logging.DEBUG,
)


def main() -> None:
    _LOGGER.info("this is a sample command")


if __name__ == "__main__":
    main()
