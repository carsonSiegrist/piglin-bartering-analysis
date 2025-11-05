# piglin_barter_rates.py
# Calculates expected item output rate for Piglin bartering
# Based on data provided from the wiki found at: https://minecraft.fandom.com/wiki/Bartering

# Barter parameters
T = 8.0  # seconds per barter
DENOMINATOR = 459  # total weight
HOPPER_RATE = 2.5  # items/sec per hopper

# Data: item_name, chance numerator, lower bound qty, upper bound qty
drops = [
    ("Soul_Speed", 5, 1, 1),
    ("Iron_Boots", 8, 1, 1),
    ("Fire_Res", 8, 1, 1),
    ("Fire_Res_Splash", 8, 1, 1),
    ("Water_Bottle", 10, 1, 1),
    ("Dried_Ghast", 10, 1, 1),
    ("Iron_Nugget", 10, 10, 36),
    ("Ender_Pearl", 10, 2, 4),
    ("String", 20, 3, 9),
    ("Quartz", 20, 5, 12),
    ("Obsidian", 40, 1, 1),
    ("Crying_Obsidian", 40, 1, 3),
    ("Fire_Charge", 40, 1, 1),
    ("Leather", 40, 2, 4),
    ("Soul_Sand", 40, 2, 8),
    ("Nether_Brick", 40, 2, 8),
    ("Arrow", 40, 6, 12),
    ("Gravel", 40, 8, 16),
    ("Blackstone", 40, 8, 16),
]

# Compute expectations
#p_i = probability of that item being selected
#E[count] is expected count, assuming items are uniformly picked along range
#p_i*E[count] tells us how many items this contributes per barter
#avg_cost tells us how many gold ingots are required on avg to get 1 of that item
expected_per_barter = 0.0
print(f"{'Item':<20}{'p_i':>8}{'E[count]':>12}{'p_i*E[count]':>16}{'avg_cost':>12}")
print("-" * 56)

for name, num, lo, hi in drops:
    p = num / DENOMINATOR
    e_count = (lo + hi) / 2  # expected count per drop
    contribution = p * e_count
    expected_per_barter += contribution
    cost = 1 / contribution 
    print(f"{name:<20}{p:8.4f}{e_count:12.2f}{contribution:16.3f}{cost:12.3f}")

items_per_second = expected_per_barter / T
items_per_minute = items_per_second * 60
hopper_fraction = items_per_second / HOPPER_RATE

print("\nSummary:")
print(f"Expected items per barter: {expected_per_barter:.3f}")
print(f"Expected items per second: {items_per_second:.3f}")
print(f"Expected items per minute: {items_per_minute:.1f}")
print(f"Hopper load fraction: {hopper_fraction*100:.1f}% of one hopper capacity")