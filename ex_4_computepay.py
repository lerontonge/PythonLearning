hours = input("Enter Hours Worked: ")
rate = input("Enter Hourly Rate: ")


def errorlog():
    return "Error Error Error"


try:
    num_hrs = float(hours)
    num_rate = float(rate)
except:
    print(errorlog())
    quit()

def calculate_pay(hrs, rte):

    if hrs <= 40:
        return  hrs * rte
    
    if hrs > 40:
        return (rte * 40)+((hrs-40)*(rte/2))

print("Total Pay:", calculate_pay(num_hrs,num_rate))