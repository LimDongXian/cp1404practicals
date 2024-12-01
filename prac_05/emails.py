"""
Emails
Estimate: 20 minutes
Actual:   26 minutes
"""

emails_to_name = {"lindsay.ward@jcu.edu.au": "Lindsay Ward", "abe@gmail.com": "Abe",
                  "jimbo546@hotmail.com": "Jimbo546", "dongxian.lim@jcu.edu.au": "Dong Xian"}

email = input("Email: ")
while email != "":
    try:
        is_user = input(f"Is your name {emails_to_name[email]} ? (Y/n) ").lower()
        if is_user == "n":
            new_name = input("Name: ").title()
            emails_to_name[email] = new_name
    except KeyError:
        print("Invalid Email")
    email = input("Email: ")

for email, name in emails_to_name.items():
    print(f"{name} ({email})")
