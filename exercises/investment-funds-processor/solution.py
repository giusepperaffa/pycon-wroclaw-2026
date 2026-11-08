# =====================
# Import Python Modules
# =====================
import csv
import unittest
from unittest.mock import patch

import investment_funds_processor

# =================
# Script Parameters
# =================
TEST_FILE_INPUT = "investment_funds_input.csv"
TEST_FILE_OUTPUT = "investment_funds_output.csv"

def load_csv_file(csv_file) -> dict:
    with open(csv_file) as f:
        csv_reader = csv.DictReader(f)
        return [row for row in csv_reader] 
    

class TestFundProcessor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fund_processor = investment_funds_processor.FundProcessor(TEST_FILE_INPUT, TEST_FILE_OUTPUT)

    @patch("investment_funds_processor.get_fund_forecast")
    def test_forecast_not_available(self, mock_get_fund_forecast):
        mock_get_fund_forecast.return_value = "N/A"
        self.fund_processor.process_funds()
        fund_processor_output = load_csv_file(TEST_FILE_OUTPUT)
        mock_get_fund_forecast.assert_called()
        self.assertEqual(mock_get_fund_forecast.call_count, len(fund_processor_output))
        self.assertTrue(all(record["Invest"] == "N/A" for record in fund_processor_output))

    @patch("investment_funds_processor.get_fund_forecast")
    def test_forecast_low_and_high_values(self, mock_get_fund_forecast):
        for value, expected in zip((5, 90), ("No", "Yes")):
            with self.subTest(value=value, expected=expected):
                mock_get_fund_forecast.side_effect = lambda x: value
                self.fund_processor.process_funds()
                fund_processor_output = load_csv_file(TEST_FILE_OUTPUT)
                mock_get_fund_forecast.assert_called()
                self.assertTrue(all(record["Invest"] == expected for record in fund_processor_output))


if __name__ == "__main__":
    unittest.main()

