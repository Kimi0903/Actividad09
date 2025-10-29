import unittest
from src.main import main

class TestMain(unittest.TestCase):
    def test_main_output(self):
        # Prueba simple: verificar que la función principal exista
        self.assertTrue(callable(main))

if __name__ == "__main__":
    unittest.main()
