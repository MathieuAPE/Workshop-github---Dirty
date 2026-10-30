from shop import apply_discount

assert apply_discount(50) == 50, "pas de remise sous 100 euros"
assert apply_discount(100) == 90, "remise de 10% attendue des 100 euros pile"
assert apply_discount(200) == 180, "remise de 10% attendue au-dela de 100 euros"
print("OK")
