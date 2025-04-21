import re

def check_password_strength(password):
    score = 0
    feedback = []

    # It Check Some Critria for password
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character.")

    # Strength
    strength = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Extremely Weak"
    }

    return strength[score], feedback



if __name__ == "__main__":
    user_password = input("Enter your password: ")
    strength, suggestions = check_password_strength(user_password)

    print(f"\nPassword Strength: {strength}")
    if suggestions:
        print("Suggestions to improve your password:")
        for tip in suggestions:
            print(f"- {tip}")
