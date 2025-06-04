import logging
from logging.handlers import RotatingFileHandler
from data.config import LOG_FILE
import det_mir.parse


def main():
    det_mir.parse.get_data()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            RotatingFileHandler(
                filename=LOG_FILE,
                maxBytes=5 * 1024 * 1024,  # 5 MB
                backupCount=3,
                encoding="utf-8"
            ),
            logging.StreamHandler()
    ])
    
    main()