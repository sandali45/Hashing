import hmac
import hashlib

def generate_hmac(key, message, algorithm='sha256'):
    return hmac.new(key.encode(), message.encode(), hashlib.new(algorithm).name).hexdigest()
key = "nsbm45"
message = "Authenticate this message"
print("Modify Key")
print("HMAC (SHA-256):", generate_hmac(key, message, 'sha256'))

print("---------------------------------------------------------------------------")
key = "securekey123"
message = "Welcome to NSBM"
print("Modify the Message")
print("HMAC (SHA-256):", generate_hmac(key, message, 'sha256'))
