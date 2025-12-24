import unittest
import sys
import os

# Add the path of the script 09 folder to enable the import of the converters module
# This allows the test suite to locate files in the preceding directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../09_unit_converter')))
import converters

class TestUnitConverter(unittest.TestCase):
    """Test suite for the Unit Converter logic."""

    def test_celsius_to_fahrenheit(self):
        """Test temperature conversion cases."""
        # Punto di congelamento
        self.assertEqual(converters.celsius_to_fahrenheit(0), 32.0)
        # Punto di ebollizione
        self.assertEqual(converters.celsius_to_fahrenheit(100), 212.0)
        # Valore negativo
        self.assertEqual(converters.celsius_to_fahrenheit(-40), -40.0)

    def test_km_to_miles(self):
        """Test distance conversion cases."""
        # Test base: 1 km
        self.assertEqual(converters.km_to_miles(1), 0.62)
        # Test 10 km
        self.assertEqual(converters.km_to_miles(10), 6.21)
        # Test zero
        self.assertEqual(converters.km_to_miles(0), 0.0)

if __name__ == '__main__':
    unittest.main()