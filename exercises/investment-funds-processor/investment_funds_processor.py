# =====================
# Import Python Modules
# =====================
import csv
import requests

def get_fund_forecast(fund_name) -> dict:
    try:
        r = requests.get(f"http://investments.com/forecast/{fund_name}")
        if r.status_code == '200':
            return r.json()
        return None
    except:
        return None

class FundProcessor:
    def __init__(self, fund_input_file, fund_output_file="investment_funds_output.csv"):
        self.fund_input_file = fund_input_file
        self.fund_output_file = fund_output_file
        self.no_information = "N/A"
    
    def _extract_fund_info(self) -> list:
        with open(self.fund_input_file) as f:
            csv_reader = csv.DictReader(f)
            self._fieldnames = csv_reader.fieldnames
            self._fund_info = [row for row in csv_reader]
            return

    def _get_investment_decision(self, profitability, forecast):
        if isinstance(profitability, str) or isinstance(forecast, str):
            return self.no_information         
        else:  
            return "Yes" if forecast > profitability else "No"

    def _get_forecast(self, fund):
        forecast = get_fund_forecast(fund)
        if forecast:
            return forecast
        else:
            return self.no_information

    def _update_fund_info(self):
        with open(self.fund_output_file, mode="w", newline='') as f:
            fieldnames = self._fieldnames + ["Forecast[%]", "Invest"]
            csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
            csv_writer.writeheader()
            for row in self._fund_info:
                row["Forecast[%]"] = self._get_forecast(row["Fund"])
                row["Invest"] = self._get_investment_decision(row["Profitability[%]"],
                    row["Forecast[%]"])
                csv_writer.writerow(row)                

    def process_funds(self):
        self._extract_fund_info()
        self._update_fund_info()
        

if __name__ == "__main__":
    fund_processor = FundProcessor("investment_funds_input.csv")
    fund_processor.process_funds()

