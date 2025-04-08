import hashlib

def generate_hash(message, algorithm='sha256'):
    hash_function = hashlib.new(algorithm)
    hash_function.update(message.encode('utf-8'))
    return hash_function.hexdigest()

message = "Cryptography"
print("Cryptography")
print("SHA-256 Hash:", generate_hash(message, 'sha256'))
print("MD5 Hash:", generate_hash(message, 'md5'))
print("---------------------------------------------------------------------------------------")
message = "CRYPTOGRAPHY"
print("CRYPTOGRAPHY")
print("SHA-256 Hash:", generate_hash(message, 'sha256'))
print("MD5 Hash:", generate_hash(message, 'md5'))
print("---------------------------------------------------------------------------------------")
message = "CRYPTOGRAPHY"
print("Modify the message")
print("CRYPTOGRAPHY!")
print("SHA-256 Hash:", generate_hash(message, 'sha256'))
print("MD5 Hash:", generate_hash(message, 'md5'))
