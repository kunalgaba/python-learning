import re

email = input("What's your email? ").strip()
print(
    r"\n"
)  # This is how raw strings are reprensented. The escape char is ingored here.
# \w means [a-zA-Z0-9]
if re.search(r"^(\w+)@(\w+)[.]{1}([a-z.]+)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
