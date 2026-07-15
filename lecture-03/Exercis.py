houre_worked =int(input("Enter you hours: "))
hourly_pay_rate =int(input("Enter you pay_rate: "))

if houre_worked <=40 :
    gross_pay = (houre_worked * hourly_pay_rate)
else:
    regular_pay = 40 * hourly_pay_rate
    overtime_pay = (houre_worked - 40) * hourly_pay_rate * 1.5
    gross_pay = regular_pay + overtime_pay
print(f"Your gross pay is {gross_pay}")






