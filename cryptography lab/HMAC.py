import hmac
import hashlib

# Choose a message and a secret key
message = b"This is a message to be authenticated"
secret_key = b"this is a secret key"

# Choose a hash function and the desired length of the hash output
hash_function = hashlib.sha256
hash_length = 32

# Calculate the HMAC
hmac_value = hmac.new(secret_key, message, hash_function).hexdigest()

# Output the HMAC
print(hmac_value)