# List price:
list_price = int(input("Enter list price: "))
date = int(input("Enter date: "))
month = input("Month: ")
year = int(input("Year: "))

if date > 31:
    print("Invalid date!")
else:
    # Trade discount
    trade_dis = int(input("Enter trade discount %: "))
    if trade_dis >= 2:
        trade_dis_amount = trade_dis * list_price / 100
        new_list_price = list_price - trade_dis_amount
    else:
        print("Trade discount = None")
        new_list_price = list_price

    # Cash discount
    cash_dis_percent = int(input("Enter cash discount %: "))
    if cash_dis_percent == 0:
        print("No Cash discount")
        invoice_price = new_list_price
        print(f"Invoice price: {invoice_price}")
    else:
        discount_period = int(input("Enter discount days: "))
        total_days = int(input("Enter total no of days: "))
        print(f"Credit term is {cash_dis_percent}/{discount_period}, n/{total_days}")

        payment_date = int(input("Enter payment date: "))

        if payment_date > discount_period:
            print("Payment after discount period")
            invoice_price = new_list_price
            print(f"Invoice price (no cash discount): {invoice_price}")
        else:
            cash_dis_amount = cash_dis_percent * new_list_price / 100
            invoice_price = new_list_price - cash_dis_amount
            print(f"Invoice price (after cash discount): {invoice_price}")

    # Sale Tax (optional)
    sale_tax = int(input("Enter sale tax: "))
    if sale_tax == 0:
        cash_paid = invoice_price
        print(f"Cash paid to seller: {cash_paid}")
    else:
        cash_paid = invoice_price + sale_tax
        print(f"Cash paid to seller (after sale tax): {cash_paid}")

    # Expenses
    install_charges          = int(input("Enter installation charges: "))
    test_run_charges         = int(input("Enter test run charges: "))
    trans_charges            = int(input("Enter transportation charges: "))
    founda_charges           = int(input("Enter foundation charges: "))
    imp_exp_charges          = int(input("Enter import/export charges: "))
    custom_charges           = int(input("Enter custom charges: "))
    overhouling_charges      = int(input("Enter overhauling charges: "))
    insurane_transit_charges = int(input("Enter insurance in transit charges: "))
    octri_charges            = int(input("Enter octroi charges: "))
    pattern_charges          = int(input("Enter pattern charges: "))
    registration_charges     = int(input("Enter registration charges: "))

    expenses = (install_charges + test_run_charges + trans_charges +
                founda_charges + imp_exp_charges + custom_charges +
                overhouling_charges + insurane_transit_charges +
                octri_charges + pattern_charges + registration_charges)

    # Net Cost
    net_cost = cash_paid + expenses
    print(f"Net cost is {net_cost}")