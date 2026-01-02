import money_converter as UC
usd = int(input("dollars: "))
print(UC.USD_EUR(usd, True))
print(UC.USD_GBP(usd, True))
print(UC.USD_JPY(usd, True))
print("now make ur own conversion")
cash = int(input("how many usd: "))
rate = float(input("what is the rate per dollar: "))
print("here: " + (UC.converter(cash,rate,True)))