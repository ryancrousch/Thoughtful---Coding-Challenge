"""
Unit tests for package sorting.
"""

import unittest
from package_sorter import sort


class TestPackageSorter(unittest.TestCase):
    
    def test_standard_package(self):
        self.assertEqual(sort(50, 50, 50, 10), "STANDARD")
        self.assertEqual(sort(100, 100, 90, 15), "STANDARD")
        self.assertEqual(sort(1, 1, 1, 0.1), "STANDARD")
    
    def test_bulky_by_volume(self):
        # Volume = 1,000,000 cm³ (exactly at threshold)
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")
        
        # Volume > 1,000,000 cm³
        self.assertEqual(sort(150, 100, 100, 10), "SPECIAL")
        self.assertEqual(sort(200, 100, 100, 15), "SPECIAL")
    
    def test_bulky_by_dimension(self):
        # Width >= 150
        self.assertEqual(sort(150, 50, 50, 10), "SPECIAL")
        self.assertEqual(sort(200, 50, 50, 10), "SPECIAL")
        
        # Height >= 150
        self.assertEqual(sort(50, 150, 50, 10), "SPECIAL")
        self.assertEqual(sort(50, 200, 50, 10), "SPECIAL")
        
        # Length >= 150
        self.assertEqual(sort(50, 50, 150, 10), "SPECIAL")
        self.assertEqual(sort(50, 50, 200, 10), "SPECIAL")
    
    def test_heavy_package(self):
        # Mass = 20 kg (exactly at threshold)
        self.assertEqual(sort(50, 50, 50, 20), "SPECIAL")
        
        # Mass > 20 kg
        self.assertEqual(sort(50, 50, 50, 25), "SPECIAL")
        self.assertEqual(sort(100, 100, 90, 30), "SPECIAL")
    
    def test_rejected_packages(self):
        # Bulky by volume and heavy
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")
        self.assertEqual(sort(100, 100, 100, 25), "REJECTED")
        
        # Bulky by dimension and heavy
        self.assertEqual(sort(150, 50, 50, 20), "REJECTED")
        self.assertEqual(sort(200, 100, 100, 30), "REJECTED")
        self.assertEqual(sort(50, 150, 50, 25), "REJECTED")
        self.assertEqual(sort(50, 50, 150, 20), "REJECTED")
    
    def test_edge_cases_below_threshold(self):
        # Just below heavy threshold (19.9 kg)
        self.assertEqual(sort(50, 50, 50, 19.9), "STANDARD")
        
        # Just below bulky dimension threshold (149 cm)
        self.assertEqual(sort(149, 50, 50, 10), "STANDARD")
        self.assertEqual(sort(50, 149, 50, 10), "STANDARD")
        self.assertEqual(sort(50, 50, 149, 10), "STANDARD")
        
        # Volume just below bulky threshold (999,999 cm³)
        self.assertEqual(sort(99.9, 100, 100, 10), "STANDARD")
    
    def test_edge_cases_at_threshold(self):
        # Exactly at heavy threshold (20 kg)
        self.assertEqual(sort(50, 50, 50, 20), "SPECIAL")
        
        # Exactly at bulky dimension threshold (150 cm)
        self.assertEqual(sort(150, 50, 50, 10), "SPECIAL")
        self.assertEqual(sort(50, 150, 50, 10), "SPECIAL")
        self.assertEqual(sort(50, 50, 150, 10), "SPECIAL")
        
        # Volume exactly at bulky threshold (1,000,000 cm³)
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")
    
    def test_zero_values(self):
        self.assertEqual(sort(0, 0, 0, 0), "STANDARD")
        self.assertEqual(sort(0, 0, 0, 25), "SPECIAL")
        self.assertEqual(sort(150, 0, 0, 0), "SPECIAL")
    
    def test_large_values(self):
        # Very large dimensions
        self.assertEqual(sort(1000, 1000, 1000, 100), "REJECTED")
        
        # Very large mass
        self.assertEqual(sort(50, 50, 50, 1000), "SPECIAL")
    
    def test_decimal_values(self):
        self.assertEqual(sort(50.5, 50.5, 50.5, 10.5), "STANDARD")
        self.assertEqual(sort(149.9, 50, 50, 19.9), "STANDARD")
        self.assertEqual(sort(150.1, 50, 50, 20.1), "REJECTED")
    
    def test_invalid_inputs(self):
        # Negative dimensions
        with self.assertRaises(ValueError):
            sort(-1, 50, 50, 10)
        
        with self.assertRaises(ValueError):
            sort(50, -1, 50, 10)
        
        with self.assertRaises(ValueError):
            sort(50, 50, -1, 10)
        
        # Negative mass
        with self.assertRaises(ValueError):
            sort(50, 50, 50, -1)


if __name__ == "__main__":
    unittest.main(verbosity=2)