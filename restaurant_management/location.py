import phonenumbers
from phonenumbers import geocoder, carrier


def track_phone_number(phone_number):
    try:
        # Parse phone number
        parsed_number = phonenumbers.parse(phone_number)

        # Get location
        location = geocoder.description_for_number(parsed_number, 'en')

        # Get carrier info
        carrier_info = carrier.name_for_number(parsed_number, 'en')

        return {
            "Location": location,
            "Carrier": carrier_info
        }
    except phonenumbers.phonenumberutil.NumberParseException as e:
        return {"Error": str(e)}


# Input the phone number
number = input("Enter the phone number (with country code): ")
result = track_phone_number(number)

print(result)
