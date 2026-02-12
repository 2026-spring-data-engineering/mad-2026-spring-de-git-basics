def main():
    """
    Modularity practice: this file intentionally contains only main() with
    redundant code blocks. Please create functions to remove redundancy as
    directed by the TODO comments.
    """

    # ---------- Section: Banner (repeated) ----------
    # TODO: Extract this banner into a function with NO parameters and NO return value.
    # By "banner", I just mean the lines that print the ====== (equal signs). It's fine
    # to keep the print of "Festival Order Summary" in main().
    print("==============================")
    print("  Festival Order Summary")
    print("==============================")

    # ---------- Section: Order Items (redundant computations) ----------
    # We have three items with quantities and unit prices. The pattern of
    # computing a line total and accumulating an order total is repeated.
    # TODO: Extract the repeated pattern into a function that USES PARAMETERS
    #       (e.g., quantity, unit_price, label) and RETURNS the line total.
    order_total = 0.0
    total_items = 0

    # Item 1: Pizza slices
    pizza_qty = 8
    pizza_price = 3.50
    pizza_line_total = pizza_qty * pizza_price
    print(f"Pizza x{pizza_qty} @ ${pizza_price:.2f} -> ${pizza_line_total:.2f}")
    order_total = order_total + pizza_line_total
    total_items = total_items + pizza_qty

    # Item 2: Sodas
    soda_qty = 5
    soda_price = 1.75
    soda_line_total = soda_qty * soda_price
    print(f"Soda x{soda_qty} @ ${soda_price:.2f} -> ${soda_line_total:.2f}")
    order_total = order_total + soda_line_total
    total_items = total_items + soda_qty

    # Item 3: T-Shirts
    shirt_qty = 2
    shirt_price = 15.00
    shirt_line_total = shirt_qty * shirt_price
    print(f"T-Shirt x{shirt_qty} @ ${shirt_price:.2f} -> ${shirt_line_total:.2f}")
    order_total = order_total + shirt_line_total
    total_items = total_items + shirt_qty

    # ---------- Section: Banner again (repeated) ----------
    # TODO: Reuse your no-arg/no-return banner function instead of repeating.
    print("==============================")
    print("        Subtotals")
    print("==============================")

    print(f"Items subtotal: {total_items} items")
    print(f"Order subtotal: ${order_total:.2f}")

    # ---------- Section: Tax and Total (parameter + return candidate) ----------
    # The pattern of applying a rate to a base value and returning a result
    # will be helpful in many programs.
    # TODO: Extract tax/total computations into a function that takes PARAMETERS
    #       (e.g., base_amount, rate) and RETURNS the computed value.
    tax_rate = 0.055  # 5.5%
    tax_amount = order_total * tax_rate
    grand_total = order_total + tax_amount

    # ---------- Section: Banner again (repeated) ----------
    # TODO: Reuse your no-arg/no-return banner function again.
    print("==============================")
    print("         Totals")
    print("==============================")

    # ---------- Section: Formatting summary (parameter + return candidate) ----------
    # TODO: Consider extracting this into a function that RETURNS a summary string
    #       so main() can return it and it can be printed outside main().
    summary = (
        f"Summary -> Items: {total_items}, Subtotal: ${order_total:.2f}, "
        f"Tax: ${tax_amount:.2f}, Grand Total: ${grand_total:.2f}"
    )


if __name__ == "__main__":
    main()
    # print(????)  # We want to display the summary here. We do not want to display
    # it in the main() function. How?
