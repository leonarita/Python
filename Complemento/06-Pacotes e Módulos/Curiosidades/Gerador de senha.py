import random

s = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*()_-+=[]{}^;/'.,"
l = 16

password = "".join(random.sample(s, l))
print(password)