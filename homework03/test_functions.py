import unittest
from datetime import datetime
from turbidity_test import calculate_turbidity, calculate_minimum_time

class TestTurbidityFunctions(unittest.TestCase):
    def test_calculate_turbidity(self):
        self.assertAlmostEqual(calculate_turbidity(3.0, 2.5), 7.5, places=4)
        self.assertAlmostEqual(calculate_turbidity(2.0, 3.0), 6.0, places=4)
        
        #negative values
        self.assertAlmostEqual(calculate_turbidity(-1.5, 2.0), -3.0, places=4)
        self.assertAlmostEqual(calculate_turbidity(1.0, -2.0), -2.0, places=4)

        #zero values
        self.assertAlmostEqual(calculate_turbidity(0.0, 2.0), 0.0, places=4)
        self.assertAlmostEqual(calculate_turbidity(1.0, 0.0), 0.0, places=4)

       
        self.assertAlmostEqual(calculate_turbidity(4.0, 1.5), 6.0, places=4)
        self.assertAlmostEqual(calculate_turbidity(0.5, 4.0), 2.0, places=4)

    def test_calculate_minimum_time(self):
        
        self.assertAlmostEqual(calculate_minimum_time(2.0, 4.0, 0.03), 0.0, places=2)
        self.assertAlmostEqual(calculate_minimum_time(3.0, 2.0, 0.015), 23.10, places=2)

        #negative values
        self.assertAlmostEqual(calculate_minimum_time(1.5, 0.5, -0.02), -34.66, places=2)
        self.assertAlmostEqual(calculate_minimum_time(-1.0, 0.5, 0.01), -46.05, places=2)

        #zero values
        self.assertEqual(calculate_minimum_time(1.0, 1.0, 0.02), 0.0)

        # Check if current turbidity is already below threshold
        self.assertEqual(calculate_minimum_time(2.0, 1.0, 0.03), 0.0)

        # Check for datetime input (should raise TypeError)
        with self.assertRaises(TypeError):
            calculate_minimum_time(2.0, 4.0, datetime.now())

if __name__ == '__main__':
    unittest.main(module='test_functions')
