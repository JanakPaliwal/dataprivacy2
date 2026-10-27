# Practical 03: Regulation Compliance

print("PRIVACY REGULATION COMPLIANCE CHECKLIST")
print("=" * 60)

checks = [
    ("Data Inventory", 
     "Has the organization documented the personal data it collects?"),

    ("Purpose of Collection", 
     "Is there a defined purpose for collecting each type of data?"),

    ("Privacy Notice", 
     "Is a clear privacy notice provided to users?"),

    ("Access Control", 
     "Are data-access permissions limited to authorized personnel?"),

    ("Data Security", 
     "Are appropriate security measures used to protect personal data?"),

    ("Data Retention", 
     "Are data retention periods clearly defined?"),

    ("Data Deletion", 
     "Is there a process for securely deleting data when it is no longer required?"),

    ("Third-Party Sharing", 
     "Are data-sharing practices with third parties documented?"),

    ("Incident Response", 
     "Is there a plan for responding to privacy or security incidents?"),

    ("Employee Training", 
     "Do employees receive privacy and data-security training?")
]

for number, (area, question) in enumerate(checks, start=1):
    print(f"\n{number}. {area}")
    print(f"   {question}")
    print("   Status: REVIEW REQUIRED")

print("\n" + "=" * 60)
print("Compliance checklist completed.")
print("Note: This is an educational checklist, not legal advice.")
