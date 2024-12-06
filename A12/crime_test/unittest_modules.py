import unittest
import pandas as pd
from validate_functions import validate_vict_sex, validate_vict_age
from stats_function import calculate_mean_and_median

class TestStatsFunction(unittest.TestCase):

    def test_calculate_mean_and_median_valid(self):
    
        df = pd.DataFrame({'Vict Age': [25, 30, 35, 40]})
        mean, median = calculate_mean_and_median(df)
        self.assertEqual(mean, 32.5)
        self.assertEqual(median, 32.5)

    def test_calculate_mean_and_median_no_data(self):
        
        df = pd.DataFrame({'Vict Age': [None, None, None]})
        with self.assertRaises(ValueError):
            calculate_mean_and_median(df)

    def test_calculate_mean_and_median_non_numeric(self):
        
        df = pd.DataFrame({'Vict Age': ['a', 'b', 'c']})
        with self.assertRaises(ValueError):
            calculate_mean_and_median(df)

class TestValidateFunctions(unittest.TestCase):

    def test_validate_vict_sex_valid(self):
        
        df = pd.DataFrame({'Vict Sex': ['M', 'F', 'M', 'F']})
        result = validate_vict_sex(df)
        self.assertTrue(result)

    def test_validate_vict_sex_invalid(self):
        
        df = pd.DataFrame({'Vict Sex': ['M', 'X', None]})
        result = validate_vict_sex(df)
        self.assertFalse(result)

    def test_validate_vict_age_valid(self):
        
        df = pd.DataFrame({'Vict Age': [25, 30, 35, 40]})
        result = validate_vict_age(df)
        self.assertTrue(result)

    def test_validate_vict_age_out_of_range(self):
        
        df = pd.DataFrame({'Vict Age': [0, 120, -5]})
        result = validate_vict_age(df)
        self.assertFalse(result)

    def test_validate_vict_age_non_numeric(self):
    
        df = pd.DataFrame({'Vict Age': ['a', 'b', 'c']})
        with self.assertRaises(TypeError):
            validate_vict_age(df)


if __name__ == "__main__":
    unittest.main()

