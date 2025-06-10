import logging
from logging.handlers import RotatingFileHandler
from data.config import LOG_FILE
import det_mir.parse
from work_with_files.file import find_difference_csv_json


def main():
    # det_mir_json_filename = det_mir.parse.get_data()
    find_difference_csv_json(
        csv_file_name="../kubik/results/Аналитика по ценам - Lego.csv",
        json_file_name="../kubik/results/det_mir_06-06-2025_00-47-30.json",
    )


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
