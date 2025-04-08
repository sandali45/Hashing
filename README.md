# 🔐Hashing in Python

## 🧪 Tasks Overview

### ✅ Generating Hash Values
- Generated SHA-256 and MD5 hashes for a sample message using Python.
- Observed how even a small change (like changing `!` to `?`) resulted in a completely different hash.
- **Insight:** Hashes are highly sensitive to input changes (avalanche effect).

### ✅ Task 2: Pre-Image Resistance
- Tried to reverse a hash using online tools like([https://www.md5hashgenerator.com/](https://md5hashing.net/hash)).
- **Result:** “Reverse decryption failed.” — original message could not be recovered.
- **Conclusion:** Pre-image resistance is confirmed.

### ✅ Task 3: Second Pre-Image Resistance
- Attempted to find a different input with the same hash — not successful.
- **Conclusion:** Secure hashes prevent finding another input that produces the same hash.

### ✅ Task 4: Collision Resistance
- Compared hash outputs of messages with tiny differences (e.g., `Hello` vs `hello`).
- **Observation:** All hashes were completely different.
- **Conclusion:** Collision resistance ensures unique outputs for unique inputs.

### ✅ Task 5: Implementing HMAC
- Used Python's `hmac` module to generate HMAC values with a key and message.
- **Insight:** Changing either the key or message changes the HMAC, ensuring message integrity and authentication.

## 💡 Key Learnings
- Cryptographic hash functions are **one-way**, **deterministic**, and **collision-resistant**.
- **HMAC** is used for secure message authentication.
- MD5 is outdated and vulnerable; **SHA-256 or SHA-3** is recommended for strong security.

## 🧷 Tools Used
- Python 3 (hashlib, hmac)
- Online tools: md5hashgenerator.com, crackstation.net


