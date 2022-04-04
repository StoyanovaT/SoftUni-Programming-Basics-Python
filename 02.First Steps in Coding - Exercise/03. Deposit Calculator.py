deposit_amount = float(input())
term_in_months = int(input())
yearly_dividend_percent = float(input())
dividend = deposit_amount * yearly_dividend_percent / 100
dividend_for_one_month = dividend / 12
end_of_period_amount = deposit_amount + (term_in_months * dividend_for_one_month)
print(end_of_period_amount)