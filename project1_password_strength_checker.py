import math
import string

def calculate_entropy(password):
    pass_len = len(password)
    pool_size = 0
    
    if any(c.islower() for c in password):
        pool_size += 26
    if any(c.isupper() for c in password):
        pool_size += 26
    if any(c.isdigit() for c in password):
        pool_size += 10
    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)
        
    if pool_size == 0:
        return 0, 0
        
    entropy = pass_len * math.log2(pool_size)
    return entropy, pool_size

def main():
    password = input("Enter a password to validate: ")
    entropy, pool_size = calculate_entropy(password)
    print(f"Password Length: {len(password)}")
    print(f"Character Pool Size: {pool_size}")
    print(f"Estimated Entropy: {entropy:.2f} bits")
    
    if entropy < 28:
        print("Strength: Very Weak")
    elif entropy < 36:
        print("Strength: Weak")
    elif entropy < 60:
        print("Strength: Reasonable")
    elif entropy < 128:
        print("Strength: Strong")
    else:
        print("Strength: Very Strong")

if __name__ == "__main__":
    main()
