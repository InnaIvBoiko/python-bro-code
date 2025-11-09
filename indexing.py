# indexing = accessing elements of a sequence using [] (index operator)
#            [start:stop:step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])        # '1'
print(credit_number[5])        # '5'
print(credit_number[-1])       # '6'
print(credit_number[-4])       # '3'
print(credit_number[0:4])      # '1234'
print(credit_number[5:9])      # '5678'
print(credit_number[0:16:5])   # '1591'
print(credit_number[:4])       # '1234'
print(credit_number[5:])       # '5678-9012-3456'
print(credit_number[::2])      # '1345791356'
print(credit_number[::-1])     # '6543-2109-8765-4321' (reverses the string)

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")  # 'XXXX-XXXX-XXXX-3456'