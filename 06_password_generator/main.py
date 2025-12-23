from generator import generate_secure_password
from strength_checker import calculate_entropy


def main():
    print("--- Secure Password Generator & Analyzer ---")

    length = 16
    new_pw = generate_secure_password(length)
    entropy = calculate_entropy(new_pw)

    print(f"Generated Password: {new_pw}")
    print(f"Password Length: {len(new_pw)}")
    print(f"Estimated Entropy: {entropy} bits")

    if entropy < 60:
        print("Strength: Weak")
    elif entropy < 80:
        print("Strength: Medium")
    else:
        print("Strength: Strong")


if __name__ == "__main__":
    main()