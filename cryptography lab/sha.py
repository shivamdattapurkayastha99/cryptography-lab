import hashlib
test_str = "password"
result = hashlib.shake_128(test_str.encode())
print(result.hexdigest()) 