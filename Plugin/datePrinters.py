class ISODatePrinter:
    def printDate(self, year, month, day):
        print(year + '-' + month + '-' + day)

class EuropeanDatePrinter:
    def printDate(self, year, month, day):
        print(day + '/' + month + '/' + year)

class AmericanDatePrinter:
    def printDate(self, year, month, day):
        print(month + '/' + day + '/' + year)

class DatePrinters:
    def get(self, formatType):
        return {
            'ISO': ISODatePrinter(),
            'European': EuropeanDatePrinter(),
            'American': AmericanDatePrinter()
        }[formatType]
