# hr - Hourly Rate
# hs - Hours


hs = input("Enter Hours: ")
hr = input("Enter Rate: ")


fr = float(hr)
fh = float(hs)

if fh > 40:
    pay = (40 * fr) + ((fh - 40) * (fr * 0.5))
    print("Overtime")

if fh <= 40:
    pay = fr * fh
    print("Regular")


print("Total Pay:", pay)
