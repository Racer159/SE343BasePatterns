from datePrinters import DatePrinters
import sys

print("\nEnter a date...\n")
print("year: ")
year = sys.stdin.readline().rstrip('\n')
print("month: ")
month = sys.stdin.readline().rstrip('\n')
print("day: ")
day = sys.stdin.readline().rstrip('\n')

print("\nPick a date format...\n(ISO, European, or American)\n")
formatType = sys.stdin.readline().rstrip('\n')

DatePrinters().get(formatType).printDate(year, month, day);
