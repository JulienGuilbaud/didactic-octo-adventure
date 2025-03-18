def format_price(price, remise):
    """Formate le prix en tenant compte de la remise et du cas où le prix est 0."""
    if price == 0:
        return "9999.99 CAD"
    else:
        return "{:.2f} CAD".format(price * remise)

def format_sale_price(price):
    """Formate le prix de vente en tenant compte du cas où le prix est 0."""
    if price == 0:
        return "9999.99 CAD"
    else:
        return "{:.2f} CAD".format(price)
