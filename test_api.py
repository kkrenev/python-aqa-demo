import allure
import pytest
import requests


@allure.title("Проверка GET /posts/{post_id}")
@allure.description("Убедиться, что запрос к JSONPlaceholder возвращает статус 200 и валидные поля")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("post_id", [1, 50, 100])
def test_get_post(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == post_id
    assert "userId" in data and data["userId"] >= 1
    assert isinstance(data["title"], str) and data["title"].strip()
    assert isinstance(data["body"], str) and data["body"].strip()
