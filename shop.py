# Mini module de calcul pour une boutique en ligne
def apply_discount(total):
    """10% de remise a partir de 100 euros."""
    if total > 100:
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


def total_with_shipping(total, weight):
    return total + shipping_cost(weight)


def is_free_shipping(total):
    return total >= 50


def round_price(value):
    return round(value, 2)


def cart_total(prices):
    return sum(prices)


def count_items(prices):
    return len(prices)


def most_expensive(prices):
    return max(prices) if prices else 0


def average_price(prices):
    return sum(prices) / len(prices) if prices else 0


def is_empty(prices):
    return len(prices) == 0


def cheapest(prices):
    return min(prices) if prices else 0


def price_range(prices):
    return (min(prices), max(prices)) if prices else (0, 0)


def apply_coupon(total, coupon):
    return total - coupon if coupon < total else 0
