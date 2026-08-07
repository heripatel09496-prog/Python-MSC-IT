password=(input("Enter  password"))
upper=False
lower=False
digit=False
special=False
repeate=False
special_chars="`~!@#$%^&*()_-<>?/|,.;:'{[]}";
for i in range(len(password)):
    ch=password[i]
    if ch.isupper():
        upper=True
    elif ch.islower():
        lower=True
    elif ch.isdigit():
        digit=True
    elif ch. inspecial_chars:
        special=True

if i>0 and password[i]==password[i-1]:
    repeated=True
    print("password strength analyzer:" )
    print("\n upper case letter:",upper)
    print("\n lower case letter",lower)
    print("\n  special character",special)
    print("\n repeated consicutive character",repeated)