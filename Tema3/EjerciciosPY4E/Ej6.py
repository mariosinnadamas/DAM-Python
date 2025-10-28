'''
Rewrite your pay computation with time-and-a-half for overtime and create
a function called computepay which takes two parameters (hours and rate).
'''
def computepay(hours, rate):
    if hours > 40:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate*1.5)
        return regular_pay+overtime_pay
    else:
        return hours*rate

hours = int(input("Introduce horas: "))
rate = int(input("Introduce ratio: "))
print(computepay(hours,rate))


