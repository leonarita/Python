import uuid

print("Your MAC address in formatted way id : ", end="")
print(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0, 8*6, 8)][::-1]))