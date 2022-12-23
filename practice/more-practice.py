import random
import string
letter=string.ascii_lowercase
asd="awwmb58g"
final=''
file=open('rate.txt','a')
number="1234567890"
for i in range(0,2001):
    res = ''.join(random.choices(string.ascii_lowercase +string.digits, k=8))
    file.write(res)
    file.write('\n')