#Generate a random numeric OTP using the random module and a function.
import random

def generate_otp():
    otp = random.randint(100000, 999999)
    return otp


otp = generate_otp()

print("Your OTP is:", otp)