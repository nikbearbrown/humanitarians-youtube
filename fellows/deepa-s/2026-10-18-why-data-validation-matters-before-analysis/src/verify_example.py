from decimal import Decimal
raw=Decimal(10)+Decimal(2000)
correct=Decimal(10)+Decimal(2000)/Decimal(100)
assert raw==2010 and correct==30
print("Fictional units example: naive total $2010; documented cents conversion yields $30.")
