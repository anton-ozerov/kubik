import datetime as dt
import logging
import re
import time

import requests as rq
from bs4 import BeautifulSoup

from det_mir.config import cookies, get_headers
from det_mir.create_files import save_to_files
from det_mir.models import ObjectModel, ResultModel

logger = logging.getLogger(f"(Детский мир){__name__}")


def clean_price(text: str) -> int:
    """
    Удалит все (включая \\xa0, \\u2009, ₽, обычные пробелы и др.), кроме цифр
    """
    digits_only = re.sub(r"[^\d]", "", text)
    return int(digits_only)


def parse_page(page: int = 1, max_page: int = 1) -> ResultModel | None:
    """Получение объектов с сайта детского мира для указанной страницы

    Args:
        page (int): Номер страницы (целое число больше 0). Если page<1, возвращается None. Defaults to 1.
        max_page (int): Номер последней страницы. Если page>max_page, возвращается None. Defaults to 1.

    Returns:
        ResultModel: Если ошибка какая-то при запросе или непавильно переданы страницы, то вернет None. Иначе - ResultModel
    """
    if page < 1 or page > max_page:
        return None

    page_string = "" if page == 1 else f"?page={page}"

    try:
        response = rq.get(
            f"https://www.detmir.ru/catalog/index/name/igry_i_igrushki/{page_string}",
            headers=get_headers(),
            cookies=cookies,
        )
    except Exception:
        logger.exception(f"Ошибка в получении данных со страницы {page}")
        return None
    logger.info(f"Успешно получили данные со страницы {page}")

    src = response.text
    soup = BeautifulSoup(src, "lxml")

    num_pages = int(soup.find_all("span", class_="lC")[-1].text)
    cards = soup.find_all("section", class_="fk fn fr _2Z")
    list_objects = []
    for card in cards:
        id = card.get("data-product-id")
        title = card.find("span", class_="fu").text.strip()
        try:
            if (
                card.find("span", class_="XD bhg bg_1 bg_6") is not None
            ):  # значит, что есть скидка
                current_price = clean_price(card.find("span", class_="Vq Vs").text)
                old_price = clean_price(card.find("span", class_="Vr").text)
                sale_percent = int(
                    card.find("span", class_="XD bhg bg_1 bg_6")
                    .text.replace("−", "")
                    .replace("%", "")
                    .strip()
                )
            else:
                current_price = clean_price(card.find("span", class_="Vq").text)
                old_price, sale_percent = None, None
        except ValueError:
            logger.exception("Ошибка в валидации данных")
        obj = ObjectModel(
            id=id,
            title=title,
            current_price=current_price,
            old_price=old_price,
            sale_percent=sale_percent,
        )
        list_objects.append(obj)
    logger.info(f"На странице {page} - {len(list_objects)} карточек")
    return ResultModel(current_page=page, max_page=num_pages, objects=list_objects)


def get_data() -> None:
    """
    Проходится по всем страницам "Игрушки для детей" и записывает данные в 2 файла - json и xlsx
    """
    start_time = dt.datetime.now()
    datetime_format = "%d-%m-%Y_%H-%M-%S"
    current_time = start_time.strftime(datetime_format)

    logger.info(f"Начался парсинг в {current_time}")

    current_page, max_page = 1, 1
    page_info = parse_page(page=current_page, max_page=max_page)
    objects: list[ObjectModel] = []
    while page_info is not None:
        if len(page_info.objects) != 0:
            current_page = page_info.current_page
            max_page = page_info.max_page
            objects.extend(page_info.objects)
            current_page += 1
        else:
            seconds_to_sleep = 1
            logger.info(
                f"0 карточек - не нормально. Пробуем ещё раз через секунд: {seconds_to_sleep}"
            )
            time.sleep(seconds_to_sleep)
        page_info = parse_page(page=current_page, max_page=max_page)
    
    save_to_files(current_time=current_time, objects=objects)  # сохраняем данные во файлах нужных форматов

    end_time = dt.datetime.now()
    logger.info(
        f"Парсинг закончился в {end_time.strftime(datetime_format)}. Заняло времени: {end_time - start_time}"
    )
