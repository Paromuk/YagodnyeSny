import unittest
from datetime import datetime, timedelta
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'static', 'JSON'))
import novelties


class TestFormValidation(unittest.TestCase):
    """Тесты для всех полей формы"""
    
    def test_1_author_field(self):
        """Тест поля АВТОР: корректные и некорректные значения"""
        
        # Корректные значения
        valid_authors = ["John", "Иван", "John123", "JD2024", "Dr.Smith", "Jo"]
        for author in valid_authors:
            is_valid, error = novelties.validate_author(author)
            self.assertTrue(is_valid, f"'{author}' должен быть валидным. Ошибка: {error}")
        
        # Некорректные значения
        invalid_authors = ["J", "John12345", "Dr.John.Smith", "User@#$"]
        for author in invalid_authors:
            is_valid, _ = novelties.validate_author(author)
            self.assertFalse(is_valid, f"'{author}' должен быть НЕвалидным")
    
    def test_2_title_field(self):
        """Тест поля НАИМЕНОВАНИЕ: корректные и некорректные значения"""
        
        # Корректные значения
        valid_titles = ["Strawberry", "Клубника", "Berry 2025", "Новый сорт!", "ABC"]
        for title in valid_titles:
            is_valid, error = novelties.validate_title(title)
            self.assertTrue(is_valid, f"'{title}' должен быть валидным. Ошибка: {error}")
        
        # Некорректные значения
        invalid_titles = ["12", "123", "Title!!!", "Заголовок@#$"]
        for title in invalid_titles:
            is_valid, _ = novelties.validate_title(title)
            self.assertFalse(is_valid, f"'{title}' должен быть НЕвалидным")
    
    def test_3_description_field(self):
        """Тест поля ОПИСАНИЕ: корректные и некорректные значения"""
        
        # Корректные значения
        valid_descriptions = [
            "Fresh organic berries from our farm",
            "Свежие ягоды с нашей фермы",
            "Вкусно! Полезно? Да, очень.",
            "A" * 10,
            "A" * 500
        ]
        for desc in valid_descriptions:
            is_valid, error = novelties.validate_description(desc)
            self.assertTrue(is_valid, f"'{desc[:30]}' должно быть валидным. Ошибка: {error}")
        
        # Некорректные значения
        invalid_descriptions = ["A" * 9, "1234567890", "Описание!!!", "Текст с @ символом"]
        for desc in invalid_descriptions:
            is_valid, _ = novelties.validate_description(desc)
            self.assertFalse(is_valid, f"'{desc}' должно быть НЕвалидным")
    
    def test_4_date_field(self):
        """Тест поля ДАТА: корректные и некорректные значения"""
    
        today = datetime.now().date()
    
        # Корректные значения
        valid_dates = [
            today.strftime('%Y-%m-%d'),
            (today + timedelta(days=1)).strftime('%Y-%m-%d'),
            (today + timedelta(days=30)).strftime('%Y-%m-%d'),
            (today + timedelta(days=365)).strftime('%Y-%m-%d')
        ]
        for date_str in valid_dates:
            is_valid, error = novelties.validate_date(date_str)
            self.assertTrue(is_valid, f"'{date_str}' должна быть валидной. Ошибка: {error}")
    
        # Некорректные значения
        invalid_dates = [
            (today - timedelta(days=1)).strftime('%Y-%m-%d'),           # вчера
            "2026/05/27",                                                # неверный формат
            "27-05-2026",                                                # неверный формат
            "2026-13-01",                                                # несуществующий месяц
            "invalid"                                                    # не дата
        ]
        for date_str in invalid_dates:
            is_valid, _ = novelties.validate_date(date_str)
            self.assertFalse(is_valid, f"'{date_str}' должна быть НЕвалидной")
