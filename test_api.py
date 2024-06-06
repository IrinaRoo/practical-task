from main import Artwork, WorksOfArts
import requests
import pytest
import logging

# Настройка логгирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_get_artwork_by_id():
    # Выполняем запрос к API для получения информации о произведении искусства по идентификатору
    response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/437133")

    # Проверяем корректный HTTP статус
    assert response.status_code == 200

    # Проверяем соответствие возвращаемых данных модели объекта произведения искусства
    artwork_data = response.json()
    artwork = Artwork(**artwork_data)
    assert isinstance(artwork, Artwork)


def test_nonexistent_artwork_request():
    # Проверяем обработку запроса с несуществующим идентификатором
    response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/0")

    # Проверяем корректный HTTP статус для несуществующего идентификатора
    assert response.status_code == 404


def test_search_api():
    url = "https://collectionapi.metmuseum.org/public/collection/v1/search?q="
    keyword = "cat"

    # Логирование запроса
    logger.info(f"Отправка запроса на {url} с ключевым словом: {keyword}")
    response = requests.get(url, params={"keyword": keyword})

    # Логирование ответа
    logger.info(f"Ответ получен: {response.status_code}")

    assert response.status_code == 200

    data = response.json()
    # Проверяем соответствие возвращаемых данных модели произведения искусства
    works_of_arts = WorksOfArts(**data)

    assert works_of_arts.total > 0
    assert isinstance(works_of_arts.objectIDs, list)

    logger.info("Структура ответа API успешно проверена")


def test_limit_of_results():
    response = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/search?q=cat')
    data = response.json()
    works_of_arts = WorksOfArts(**data)
    assert len(works_of_arts.objectIDs) <= 50000


def test_search_sorting():
    response = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/search?q=1967')
    data = response.json()
    works_of_arts = WorksOfArts(**data)
    assert sorted(works_of_arts.objectIDs)


if __name__ == '__main':
    pytest.main()
