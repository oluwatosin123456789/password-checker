def currency_converter():
    # Define exchange rates
    exchange_rate = {
        ("USD", "EUR"): 0.91,
        ("USD", "GBP"): 0.79,
        ("USD", "NGN"): 1500,
        ("EUR", "USD"): 1.123,
        ("EUR", "GBP"): 0.87,
        ("EUR", "NGN"): 2020,
        ("GBP", "USD"): 1.42,
        ("GBP", "EUR"): 1.12,
        ("GBP", "NGN"): 2072,
        ("NGN", "USD"): 0.013,
        ("NGN", "EUR"): 0.012,
        ("NGN", "GBP"): 0.010,
    }

    print("Available currencies: USD, EUR, GBP, NGN")
    from_currency = input("Enter the currency you have: ").upper()
    to_currency = input("Enter the currency you want to convert to: ").upper()
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    # Get the conversion rate
    rate = exchange_rate.get((from_currency, to_currency))

    if rate:
        converted = amount * rate
        print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")
    else:
        print("Conversion rate not available.")

# Run the function
currency_converter()
