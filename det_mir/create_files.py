import json
import logging
import os
from pathlib import Path

import pandas as pd

from data.config import RESULT_DIR
from det_mir.models import ObjectModel

logger = logging.getLogger(f"(Детский мир - работа с файлами){__name__}")


def save_to_files(current_time: str, objects: list[ObjectModel]):
    folder = Path(RESULT_DIR)
    if not folder.exists() or not folder.is_dir():
        os.mkdir(folder)
        logger.info(f'Создана папка {str(folder)}')
    
    file_name = f"det_mir_{current_time}"
    path_json_file = folder / f"{file_name}.json"
    path_xlsx_file = folder / f"{file_name}.xlsx"

    with open(path_json_file, "w", encoding="utf-8") as f:
        json.dump(
            [obj.model_dump() for obj in objects], f, ensure_ascii=False, indent=2
        )
    logger.info(f"Создан файл {file_name}.json")
    
    df = pd.DataFrame([obj.model_dump() for obj in objects])
    df = df.rename(
        columns={
            "id": "Артикул",
            "title": "Название",
            "current_price": "Текущая цена",
            "old_price": "Старая цена",
            "sale_percent": "Размер скидки",
        }
    )
    df.to_excel(path_xlsx_file, index=False)
    logger.info(f"Создан файл {file_name}.xlsx")
