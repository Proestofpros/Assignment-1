rate=0.2
sd=10000
add=3000
Gross=int(input("Enter your income: "))
dep=int(input("Enter the no. of dependents: "))
tax_income=Gross-sd-(add*dep)
print(tax_income)
