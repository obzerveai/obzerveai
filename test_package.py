from obzerveai import ObzerveAI

obzerve_ai = ObzerveAI()

for i in range(10):
    text = """
Name: John Doe
Address: 123 Main St, City, State, 12345
Email: johndoe@example.com
Phone: 555-555-5555
SSN: 123-45-6789
PASSPORT: J8369954
DRIVING LICENSE: RJ1420140033640
DOB: 1995-01-01 01-01-1995 12/12/98 12/12/1998 24/12/95 24/12/1995
Credit Card: 1234 5678 9012 3456
Health Info: 987-65-4321
Financial Info: 9876 5432 1098 7654
"""
    redcated = obzerve_ai.redact_sensitive_info(text)
    print(redcated)