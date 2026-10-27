# Practical 07: Privacy-Enhancing Technologies

print("PRIVACY-ENHANCING TECHNOLOGIES (PETs)")
print("=" * 55)

pets = {
    "Encryption": "Protects data by converting it into an unreadable form.",
    "Anonymization": "Removes or modifies identifying information from data.",
    "Pseudonymization": "Replaces direct identifiers with artificial identifiers.",
    "Differential Privacy": "Adds controlled noise to data or query results.",
    "Access Control": "Restricts data access to authorized users.",
    "Secure Multi-Party Computation": "Allows parties to compute results without revealing private inputs."
}

for number, (technology, description) in enumerate(pets.items(), start=1):
    print(f"\n{number}. {technology}")
    print(f"   {description}")

print("\n" + "=" * 55)
print("PET overview completed.")
