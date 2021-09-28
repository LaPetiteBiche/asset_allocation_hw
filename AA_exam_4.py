#I decided to simulate the CPPI using a multiplier of 2, an initial asset level of 100,
# an initial investment in stock of 50 and a floor of 75.
# Each time the value of stock market can increase by 10%, remain the same or decrease by 10%.
# I simulated in a horizon of 10 years and reproduced the process 2’000 times.
import random
from matplotlib import pyplot as plt
case = [0.9,1,1.1]
e_all = []
a_all = []
for i in range(2000):
    value_a = 100
    value_e = 50
    value_m = 100
    value_cash = 50
    floor = 75
    m = 4
    z = 1
    for ii in range(10):
        x = random.randint(0,2)
        value_m = value_m * case[x]
        value_e = value_e * case[x]
        value_a = value_e + value_cash
        cushion = value_a - floor
        value_enew = cushion * m
        value_cash -= (value_enew - value_e)
        value_e = value_enew

        if value_a <= 75 :
            z = 0
    if z == 0 :
        value_a = 75
    else :
        value_a = value_cash + value_e
    e_all.append(value_m)
    a_all.append(value_a)
plt.scatter(e_all, a_all)
plt.title("AA-Q1.4 - Payoff Diagram for CPPI")
plt.xlabel("Value of Stock Market")
plt.ylabel("Value of Assets")
plt.show()
print(a_all)

