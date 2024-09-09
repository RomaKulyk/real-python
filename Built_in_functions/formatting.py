class Formatter:
    @staticmethod
    def as_currency(value):
        return f"${value:,.2f}"
    
    @staticmethod
    def as_percent(value):
        return f"{value:.2%}"
    
from formatting import Formatter
print(Formatter.as_currency(1000))
print(Formatter.as_percent(0.75))
formatter = Formatter()
print(formatter.as_currency(1000))
print(formatter.as_percent(0.8))