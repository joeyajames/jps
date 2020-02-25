# DICTIONARIES
# Create a new dictionary with 3 key-value pairs
prices = {'shrimp':8.52, 'chicken':4.35, 'beef':6.28}
print(prices.items())

# to get one item from our prices dictionary, use its key 'chicken' as the index
print('chicken: ', prices['chicken'])

# UPDATE AND ADD TO A DICTIONARY
# if beef already exists, this will update the price.
# if not, it will add beef to the dictionary
prices['beef'] = 2.99
prices['pork'] = 7.55

print(prices.keys())
print(prices.values())
