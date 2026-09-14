
# ============================================================
# TAKE LIST PRICE FROM USER
# ============================================================
# input() always gives us a string.
# int() converts that string into an integer.
list_price = int(input("Enter list price: "))


# ============================================================
# PERCENTAGE FUNCTION
# ============================================================

# This function calculates a percentage value.
# Formula:
# Percentage Value = (value × percentage) / 100
def per_val(val1, val2):
    return val1 * val2 / 100


# ============================================================
# PURCHASE DATE FUNCTION
# ============================================================

# This function asks the user for the purchase date
# and returns the complete date as a string.
def purchase_date():

    # Ask the user for the date.
    date = int(input("Enter Date: "))

    # Validate the date.
    #
    # 'or' means either condition can make this True.
    #
    # If date is 0 OR greater than 31,
    # the function returns None.
    if date == 0 or date > 31:
        return None

    # Month is kept as a string so the user can enter
    # something like "September".
    month = input("Enter Month: ")

    # Year is converted into an integer.
    year = int(input("Enter Year: "))

    # f-string combines different values into one string.
    return f"{date}/{month}/{year}"


# ============================================================
# NET COST FUNCTION
# ============================================================

# This is the main function of the program.
#
# 'listprice' is a parameter.
# It receives the list price from the function call at the end.
def net_cost(listprice):

    # ========================================================
    # DEFAULT VALUES
    # ========================================================

    # We initialize these variables with 0.
    #
    # Why?
    # If the user says "no" to a discount/tax/expense,
    # these variables still need a value.
    #
    # Without default values, Python could give a
    # "local variable referenced before assignment" error.

    trade_per = 0
    tradeVal = 0

    cash_per = 0
    cashVal = 0

    tax = 0
    taxVal = 0


    # Default value for every possible expense.
    install_charges = 0
    test_run_charges = 0
    trans_charges = 0
    founda_charges = 0
    imp_exp_charges = 0
    custom_charges = 0
    overhouling_charges = 0
    insurane_transit_charges = 0
    octri_charges = 0
    pattern_charges = 0
    registration_charges = 0

    # This will store the total of all expenses.
    exp_sum = 0


    # ========================================================
    # PURCHASE DATE
    # ========================================================

    # Calling the purchase_date() function.
    #
    # Whatever the function returns will be stored in 'date'.
    date = purchase_date()


    # ========================================================
    # DISCOUNT
    # ========================================================

    # Ask whether any discount is available.
    #
    # .lower() converts the answer to lowercase.
    #
    # Example:
    # "YES" → "yes"
    # "Yes" → "yes"
    #
    # This makes our comparison easier.
    check_dis = input("Any Discount is available(Yes/No): ").lower()


    # Check whether discount is available.
    if check_dis == "yes":

        # ----------------------------------------------------
        # TRADE DISCOUNT
        # ----------------------------------------------------

        trade_dis = input(
            "Trade discount is available(Yes/No): "
        ).lower()

        if trade_dis == "yes":

            # Ask for trade discount percentage.
            trade_per = int(input("Enter trade discount: "))

            # Calculate the actual discount amount.
            #
            # Example:
            # List price = 100000
            # Trade discount = 10%
            # tradeVal = 10000
            tradeVal = per_val(listprice, trade_per)

            # Subtract trade discount from list price.
            after_price = listprice - tradeVal

        else:

            # No trade discount.
            # Therefore, price remains unchanged.
            after_price = listprice


        # ----------------------------------------------------
        # CASH DISCOUNT
        # ----------------------------------------------------

        cash_dis = input(
            "Cash discount is available(Yes/No): "
        ).lower()

        if cash_dis == "yes":

            # Ask for cash discount percentage.
            cash_per = int(input("Enter cash discount: "))

            # Cash discount is calculated on the price
            # AFTER trade discount.
            cashVal = per_val(after_price, cash_per)

            # Subtract cash discount from after_price.
            #
            # This gives us the invoice price.
            inv_price = after_price - cashVal

        else:

            # No cash discount.
            inv_price = after_price


    else:

        # No discount at all.
        #
        # Therefore:
        # List Price = After Price = Invoice Price
        after_price = listprice
        inv_price = listprice


    # ========================================================
    # TAX
    # ========================================================

    # Ask whether tax is applicable.
    ask_tax = input("Any tax is given(Yes/No): ").lower()

    if ask_tax == "yes":

        # Ask for tax percentage.
        tax = int(input("Enter sale tax: "))

        # Calculate tax on invoice price.
        taxVal = per_val(inv_price, tax)

        # Add tax to invoice price.
        #
        # This is the amount actually paid to the seller.
        paid_seller = inv_price + taxVal

    else:

        # If there is no tax,
        # the amount paid to seller remains invoice price.
        paid_seller = inv_price


    # ========================================================
    # ADDITIONAL EXPENSES
    # ========================================================

    # Ask whether any additional expenses exist.
    exp = input("Any expense is given(Yes/No): ").lower()

    if exp == "yes":

        # Ask for each individual expense.
        install_charges = int(
            input("Enter installation charges: ")
        )

        test_run_charges = int(
            input("Enter test run charges: ")
        )

        trans_charges = int(
            input("Enter transportation charges: ")
        )

        founda_charges = int(
            input("Enter foundation charges: ")
        )

        imp_exp_charges = int(
            input("Enter import/export charges: ")
        )

        custom_charges = int(
            input("Enter custom charges: ")
        )

        overhouling_charges = int(
            input("Enter overhauling charges: ")
        )

        insurane_transit_charges = int(
            input("Enter insurance in transit charges: ")
        )

        octri_charges = int(
            input("Enter octroi charges: ")
        )

        pattern_charges = int(
            input("Enter pattern charges: ")
        )

        registration_charges = int(
            input("Enter registration charges: ")
        )


        # ----------------------------------------------------
        # ADD ALL EXPENSES
        # ----------------------------------------------------

        # The '+' operator adds all individual expenses.
        #
        # exp_sum stores the total of every expense.
        exp_sum = (
            install_charges
            + test_run_charges
            + trans_charges
            + founda_charges
            + imp_exp_charges
            + custom_charges
            + overhouling_charges
            + insurane_transit_charges
            + octri_charges
            + pattern_charges
            + registration_charges
        )


    # ========================================================
    # FINAL NET COST
    # ========================================================

    # Net Cost = Cash Paid to Seller + Total Expenses
    #
    # This is the final cost of the fixed asset.
    netCost = paid_seller + exp_sum


    # ========================================================
    # DISPLAY OUTPUT
    # ========================================================

    print("  Net cost of fixed assets :  ")
    print()

    # List price with purchase date.
    print(f"List price ({date})                   = {listprice}")

    # Trade discount.
    print(f"Less Trade discount ({trade_per}%)    = ({tradeVal})")

    # Price after trade discount.
    print(f"                                      = {after_price}")

    # Cash discount.
    print(f"Less Cash discount ({cash_per}%)      = ({cashVal})")

    # Final invoice price after discounts.
    print(f"Invoice price                         = {inv_price}")

    # Tax added to invoice price.
    print(f"Add Sale tax ({tax}%)                 = {taxVal}")

    # Amount finally paid to seller.
    print(f"Cash paid to seller                   = {paid_seller}")

    print()

    # --------------------------------------------------------
    # EXPENSE DETAILS
    # --------------------------------------------------------

    print(f"Installation charges                  = {install_charges}")
    print(f"Test run charges                      = {test_run_charges}")
    print(f"Transportation charges                = {trans_charges}")
    print(f"Foundation charges                    = {founda_charges}")
    print(f"Import/export charges                 = {imp_exp_charges}")
    print(f"Custom charges                        = {custom_charges}")
    print(f"Overhauling charges                   = {overhouling_charges}")
    print(f"Insurance in transit charges          = {insurane_transit_charges}")
    print(f"Octroi charges                        = {octri_charges}")
    print(f"Pattern charges                       = {pattern_charges}")
    print(f"Registration charges                  = {registration_charges}")

    # Total of all additional expenses.
    print(f"Total expenses                        = {exp_sum}")

    print()

    # Final answer.
    print(f"Net Cost                              = {netCost}")


# ============================================================
# CALL THE MAIN FUNCTION
# ============================================================

# list_price was entered by the user at the beginning.
#
# We pass it to net_cost().
#
# Flow:
#
# User enters list price
#        ↓
# list_price
#        ↓
# net_cost(list_price)
#        ↓
# Discounts → Tax → Expenses
#        ↓
# Net Cost
net_cost(list_price)
