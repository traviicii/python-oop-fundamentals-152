phone = 5555555556

# phone number is a ten digit number
def format_phone(phone_number):
    phone = str(phone_number)

    if len(phone) == 10:
        return f"{phone[:3]}-{phone[3:6]}-{phone[6:]}"
    else:
        return "Your entry is too long/short"
    
new_num = format_phone(phone)

print(new_num)