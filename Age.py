from datetime import datetime
while True:
    try:
        dob_input = input("Enter your date of birth (yyyy-mm-dd): ")
        dob = datetime.strptime(dob_input, "%Y-%m-%d")
        break
    except ValueError:
        print("Invalid date format. Please use yyyy-mm-dd.")
current_date = datetime.now()
years = current_date.year - dob.year
months = current_date.month - dob.month
days = current_date.day - dob.day
if days < 0:
    months -= 1
    days += 30  # Assuming 30 days per month for simplicity
if months < 0:
    years -= 1
    months += 12
print(f"Age: {years} years, {months} months, {days} days")
