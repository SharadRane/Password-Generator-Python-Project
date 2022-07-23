# Password Generator using Python

import random

lower="acdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER="0123456789"
Symbol=".,/@!#$%&*+_-?"

all=lower+upper+NUMBER+Symbol
length=12

password="".join(random.sample(all,length))
print("The Password You Generated is :",password)

