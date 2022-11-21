salary = float(input("What is your salary "))
if salary <12000:
  print("Your salary is ", salary)
elif salary <37500:
  tax = salary*0.20
  pension = salary*0.03
  pay = salary - tax - pension
  print("Your pay is",pay/12,"a month.")
elif salary <150000:
  tax = salary*0.4
  pension = salary*0.06
  pay = salary - tax - pension
  print("Your pay is",pay/12,"a month.")
elif salary >150000:
  tax = salary*0.45
  pension = salary*0.10
  pay = salary - tax - pension
  print("Your pay is",pay/12,"a month")