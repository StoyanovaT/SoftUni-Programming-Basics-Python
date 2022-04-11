import phonenumbers
from phonenumbers import geocoder, timezone, carrier

cr_number = "+447533931993"
current_num = phonenumbers.parse(cr_number)
time_zone = timezone.time_zones_for_number(current_num)
print(time_zone)

number = phonenumbers.parse(cr_number, "CH")
print(geocoder.description_for_number(number, "en"))

number = phonenumbers.parse(cr_number, "RO")
print(carrier.name_for_number(number, "en"))
