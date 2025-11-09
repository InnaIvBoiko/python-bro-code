# Format Specifiers = {:flags} format a value based on what flags are inserted

# .(number)f = round to that. many decimal places (fixed point)
# :(number) = allocate that many spaces for the value
# :< = left align within allocated spaces
# :> = right align within allocated spaces
# :^ = center align within allocated spaces
# :+ = always show sign (+ or -)
# :- = only show - for negative numbers
# : space = show leading space for positive numbers, - for negative numbers
# :, = include commas as thousand separators
# :_ = include underscores as thousand separators
# :b = binary format
# :o = octal format
# :x = hexadecimal format (lowercase)
# :X = hexadecimal format (uppercase)
# :% = percentage format (multiplies by 100 and adds % sign)    


price1 = 49.9978
price2 = 9.99
price3 = -914.65
price4 = 299.99
price5 = 1004.9989

print(f"Price 1: ${price1:.2f}")               # rounds to 2 decimal places
print(f"Price 2: ${price2:>8.2f}")              # right align in 8 spaces, 2 decimal places
print(f"Price 3: ${price3:+.2f}")              # always show sign, 2 decimal places
print(f"Price 4: ${price4: <10.2f}")             # left align in 10 spaces, 2 decimal places
print(f"Price 5: ${price5:,.2f}")             # include commas as thousand separators, 2 decimal places    
