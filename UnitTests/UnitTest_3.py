import unittest
from unittest.mock import MagicMock

class TestDatabase:
    def test_save(self):
        # Utwórz stub bazy danych
        db = MagicMock()

        # Ustaw zachowanie stuba tak, aby zwracał 1 po wywołaniu metody save
        db.save.return_value = 1

        # Wywołaj metodę save i sprawdź, czy zwraca 1
        result = db.save()
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
