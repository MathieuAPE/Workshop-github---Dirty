# Mini module de calcul pour une boutique en ligne
def apply_discount(total):
    """10% de remise a partir de 100 euros."""
    if total >= 100:
        return total * 0.9
    return total


def add_tax(total, rate=0.2):
    return total * (1 + rate)


def shipping_cost(weight):
    if weight < 1:
        return 3.5
    return 3.5 + (weight - 1) * 1.2


def format_price(value):
    return f"{value:.2f} EUR"
