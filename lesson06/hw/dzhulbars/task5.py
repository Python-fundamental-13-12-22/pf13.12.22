def bank():
  n=float(input("Enter the deposit amount: "))
  years=int(input("Enter the deposit period: "))
  for a in range(years):
    n+=n*0.10
  return n
print(f"The invested amount that will be received: {bank()}")
