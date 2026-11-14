# Project Title: Currency Converter

# Exchange rates (base currency: INR)
exchange_rates = {
    "INR": 1,
    "USD": 83,
    "EUR": 90,
    "GBP": 105
}


def convert_to_inr(amount, currency):
    return amount * exchange_rates[currency]


def convert_currency(amount, from_currency, to_currency):
    # Convert source currency into INR
    amount_in_inr = convert_to_inr(amount, from_currency)

    # Convert INR into target currency
    result = amount_in_inr / exchange_rates[to_currency]

    return round(result, 2)


def main():
    print("===== CURRENCY CONVERTER =====")
    print("Supported currencies: INR, USD, EUR, GBP")

    # Get amount
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Enter a number.")
        return

    # Validate amount
    if amount < 0:
        print("Amount cannot be negative.")
        return

    # Get currencies
    from_currency = input("From currency: ").strip().upper()
    to_currency = input("To currency: ").strip().upper()

    # Validate currency codes
    if from_currency not in exchange_rates:
        print(
            f"Unsupported currency '{from_currency}'. "
            "Available: INR, USD, EUR, GBP."
        )
        return

    if to_currency not in exchange_rates:
        print(
            f"Unsupported currency '{to_currency}'. "
            "Available: INR, USD, EUR, GBP."
        )
        return

    # Convert and display result
    result = convert_currency(
        amount, from_currency, to_currency
    )

    print(
        f"{amount:g} {from_currency} = "
        f"{result:.2f} {to_currency}"
    )


if __name__ == "__main__":
    main()