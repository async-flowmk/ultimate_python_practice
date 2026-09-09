list_price = int(input("Enter list price: "))


def per_val(val1, val2):
        return val1 * val2 / 100


def purchase_date():
        
        date = int(input("Enter Date: "))

        if date == 0 or date > 31:
            return None

        month = input("Enter Month: ")
        year = int(input("Enter Year: "))

        return f"{date}/{month}/{year}"


def net_cost(listprice):

        # Default values
        trade_per = 0
        tradeVal = 0
        cash_per = 0
        cashVal = 0
        tax = 0
        taxVal = 0

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
        exp_sum = 0

        date = purchase_date()

        # Discount
        check_dis = input("Any Discount is available: ").lower()

        if check_dis == "yes":

            trade_dis = input("Trade discount is available: ").lower()

            if trade_dis == "yes":
                trade_per = int(input("Enter trade discount: "))
                tradeVal = per_val(listprice, trade_per)
                after_price = listprice - tradeVal
            else:
                after_price = listprice

            cash_dis = input("Cash discount is available: ").lower()

            if cash_dis == "yes":
                cash_per = int(input("Enter cash discount: "))
                cashVal = per_val(after_price, cash_per)
                inv_price = after_price - cashVal
            else:
                inv_price = after_price

        else:
            after_price = listprice
            inv_price = listprice

        # Tax
        ask_tax = input("Any tax is given: ").lower()

        if ask_tax == "yes":
            tax = int(input("Enter sale tax: "))
            taxVal = per_val(inv_price, tax)
            paid_seller = inv_price + taxVal
        else:
            paid_seller = inv_price

        # Expenses
        exp = input("Any expense is given: ").lower()

        if exp == "yes":

            install_charges = int(input("Enter installation charges: "))
            test_run_charges = int(input("Enter test run charges: "))
            trans_charges = int(input("Enter transportation charges: "))
            founda_charges = int(input("Enter foundation charges: "))
            imp_exp_charges = int(input("Enter import/export charges: "))
            custom_charges = int(input("Enter custom charges: "))
            overhouling_charges = int(input("Enter overhauling charges: "))
            insurane_transit_charges = int(
                input("Enter insurance in transit charges: ")
            )
            octri_charges = int(input("Enter octroi charges: "))
            pattern_charges = int(input("Enter pattern charges: "))
            registration_charges = int(input("Enter registration charges: "))

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

        netCost = paid_seller + exp_sum

        # Output
        print("  Net cost of fixed assets :  ")
        print()
        print(f"List price ({date})                   = {listprice}")
        print(f"Less Trade discount ({trade_per}%)    = ({tradeVal})")
        print(f"                                      = {after_price}")
        print(f"Less Cash discount ({cash_per}%)      = ({cashVal})")
        print(f"Invoice price                         = {inv_price}")
        print(f"Add Sale tax ({tax}%)                 = {taxVal}")
        print(f"Cash paid to seller                   = {paid_seller}")
        print()
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
        print(f"Total expenses                        = {exp_sum}")
        print()
        print(f"Net Cost                              = {netCost}")


net_cost(list_price)