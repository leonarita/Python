import phonenumbers
from phonenumbers import carrier

mobileNo = input("Enter mobile number with country code: ")
service = phonenumbers.parse(mobileNo)

print(carrier.name_for_number(service, "en"))
