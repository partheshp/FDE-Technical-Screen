# test_sort_packages.py

import unittest
from sort_packages import sort  # Import the function from sort_packages.py

class TestPackageSorting(unittest.TestCase):
    
    def test_standard_package(self):
        self.assertEqual(sort(30, 50, 100, 10), "STANDARD")
    
    def test_bulky_package(self):
        self.assertEqual(sort(200, 50, 100, 10), "SPECIAL")
    
    def test_heavy_package(self):
        self.assertEqual(sort(30, 50, 100, 25), "SPECIAL")
    
    def test_rejected_package(self):
        self.assertEqual(sort(200, 150, 150, 25), "REJECTED")
    
    def test_bulky_edge_case(self):
        self.assertEqual(sort(150, 50, 50, 10), "SPECIAL")
    
    def test_minimum_dimensions_and_mass(self):
        self.assertEqual(sort(0, 0, 0, 0), "STANDARD")
    
    def test_minimum_bulky_dimension(self):
        self.assertEqual(sort(150, 1, 1, 10), "SPECIAL")
    
    def test_minimum_heavy_mass(self):
        self.assertEqual(sort(1, 1, 1, 20), "SPECIAL")
    
    def test_exact_bulky_volume(self):
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")
    
    def test_extreme_values(self):
        self.assertEqual(sort(200, 200, 200, 50), "REJECTED")
    
    def test_just_under_heavy_threshold(self):
        self.assertEqual(sort(50, 50, 50, 19.9), "STANDARD")
    
    def test_just_over_bulky_threshold(self):
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")

if __name__ == '__main__':
    unittest.main()