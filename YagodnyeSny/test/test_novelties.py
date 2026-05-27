import unittest
from datetime import datetime, timedelta
import sys
import os

# Добавляем путь к папке static/JSON где лежит novelties.py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'static', 'JSON'))

# Теперь импорт работает
import novelties


class TestFormFields(unittest.TestCase):
    """Тесты для полей формы: автор, наименование, описание, дата"""
    
    def test_author_field(self):
        """Тесты для поля АВТОР (Имя/Ник)"""
        
        # ВАЛИДНЫЕ данные
        valid_authors = [
            "John",
            "John Doe",
            "John123",
            "JD2024",
            "Jo",
            "Dr.Smith",
            "Ivan",
            "Vasia2024",
            "A" * 50
        ]
        
        for author in valid_authors:
            is_valid, error = novelties.validate_author(author)
            self.assertTrue(is_valid, f"Author '{author}' should be valid. Error: {error}")
        
        # НЕВАЛИДНЫЕ данные
        invalid_authors = [
            ("", "Empty string"),
            ("J", "Less than 2 chars"),
            ("John12345", "5 digits (exceeds limit)"),
            ("12345", "Only digits"),
            ("User@#$", "Special chars"),
            ("A" * 51, "51 chars (exceeds)"),
            ("   ", "Only spaces")
        ]
        
        for author, reason in invalid_authors:
            is_valid, error = novelties.validate_author(author)
            self.assertFalse(is_valid, f"Author '{author}' should be INVALID. Reason: {reason}")
    
    def test_title_field(self):
        """Тесты для поля НАИМЕНОВАНИЕ НОВИНКИ"""
        
        valid_titles = [
            "New Strawberry",
            "New berry variety",
            "Berry 2025",
            "ABC",
            "Product #1",
            "A" * 100
        ]
        
        for title in valid_titles:
            is_valid, error = novelties.validate_title(title)
            self.assertTrue(is_valid, f"Title '{title}' should be valid. Error: {error}")
        
        invalid_titles = [
            ("", "Empty string"),
            ("12", "Less than 3 chars"),
            ("123", "Only digits"),
            ("12345", "Only digits"),
            ("   ", "Only spaces"),
            ("A" * 101, "101 chars (exceeds)")
        ]
        
        for title, reason in invalid_titles:
            is_valid, error = novelties.validate_title(title)
            self.assertFalse(is_valid, f"Title '{title}' should be INVALID. Reason: {reason}")
    
    def test_description_field(self):
        """Тесты для поля ОПИСАНИЕ"""
        
        valid_descriptions = [
            "Fresh organic berries from our farm",
            "A" * 10,
            "A" * 500,
            "Description in Russian language",
            "Description with 123 numbers",
            "Line 1\nLine 2\nLine 3"
        ]
        
        for desc in valid_descriptions:
            is_valid, error = novelties.validate_description(desc)
            self.assertTrue(is_valid, f"Description '{desc[:30]}...' should be valid. Error: {error}")
        
        invalid_descriptions = [
            ("", "Empty string"),
            ("A" * 9, "Less than 10 chars"),
            ("1234567890", "Only digits"),
            ("12345678901", "Only digits"),
            ("   ", "Only spaces"),
            ("A" * 501, "501 chars (exceeds)")
        ]
        
        for desc, reason in invalid_descriptions:
            is_valid, error = novelties.validate_description(desc)
            self.assertFalse(is_valid, f"Description '{desc}' should be INVALID. Reason: {reason}")
    
    def test_date_field(self):
        """Тесты для поля ДАТА"""
        
        today = datetime.now().date()
        tomorrow = (today + timedelta(days=1)).strftime('%Y-%m-%d')
        max_future = (today + timedelta(days=5*365)).strftime('%Y-%m-%d')
        
        valid_dates = [
            tomorrow,
            (today + timedelta(days=7)).strftime('%Y-%m-%d'),
            (today + timedelta(days=30)).strftime('%Y-%m-%d'),
            (today + timedelta(days=365)).strftime('%Y-%m-%d'),
            max_future
        ]
        
        for date_str in valid_dates:
            is_valid, error = novelties.validate_date(date_str)
            self.assertTrue(is_valid, f"Date '{date_str}' should be valid. Error: {error}")
        
        yesterday = (today - timedelta(days=1)).strftime('%Y-%m-%d')
        too_far = (today + timedelta(days=5*365 + 1)).strftime('%Y-%m-%d')
        
        invalid_dates = [
            ("", "Empty string"),
            (yesterday, "Date in the past"),
            (too_far, "More than 5 years ahead"),
            ("2026/05/27", "Wrong format (slashes)"),
            ("27-05-2026", "Wrong format (dd-mm-yyyy)"),
            ("2026-13-01", "Nonexistent month"),
            ("2026-02-30", "Nonexistent day"),
            ("invalid", "Not a date")
        ]
        
        for date_str, reason in invalid_dates:
            is_valid, error = novelties.validate_date(date_str)
            self.assertFalse(is_valid, f"Date '{date_str}' should be INVALID. Reason: {reason}")


if __name__ == '__main__':
    unittest.main(verbosity=2)
