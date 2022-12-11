import zlib

data='qefioFHGUQeouqeOOEFQHFEHFHFFOFHEofeqFGwrg'
data=data.encode()

zip_data=zlib.compress(data)
print(data)
print(zip_data)