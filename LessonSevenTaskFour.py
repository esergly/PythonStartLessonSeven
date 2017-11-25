import math

for i in range(10):
    f = '{:.'+str(i+2)+'f}'
    pi_value = f.format(math.pi)
    print(pi_value)
