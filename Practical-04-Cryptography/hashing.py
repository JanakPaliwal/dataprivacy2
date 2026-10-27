import hashlib

data = "Student privacy practical"
digest = hashlib.sha256(data.encode()).hexdigest()

print("Input :", data)
print("SHA-256:", digest)
