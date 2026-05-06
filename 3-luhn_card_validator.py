
def verify_card_number(card_number):

    digits = card_number.replace(" ", "").replace("-", "")

    card_digits = [int(d) for d in digits]

    check_digit = card_digits[-1]

    payload = card_digits[:-1]
    reversed_payload = payload[::-1]
    
    total_sum = 0
    for i, digit in enumerate(reversed_payload):
        if i % 2 == 0:
            doubled = digit * 2
            if doubled > 9:
                doubled -= 9
            total_sum += doubled
        else:
            total_sum += digit

    total_sum += check_digit

    if total_sum % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"

def interactive_validator():
    print("--- CARD VALIDATOR (LUHN) ---")
    print("Type 'exit' to finish.")
    
    while True:
        entrance = input("\nEnter the card number to verify: ")
        
        if entrance.lower() == 'exit':
            break
            
        if not any(char.isdigit() for char in entrance):
            print("Error: Please enter a valid number.")
            continue
            
        result = verify_card_number(entrance)
        
        if result == "VALID!":
            print(f"✅ The number {entrance} is VALID.")
        else:
            print(f"❌ The number {entrance} is INVALID.")

if __name__ == "__main__":
    interactive_validator()
