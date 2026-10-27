# Practical 02: Privacy Impact Assessment

print("PRIVACY IMPACT ASSESSMENT")
print("=" * 50)

risks = [
    {
        "risk": "Unauthorized account access",
        "likelihood": "Medium",
        "impact": "High",
        "rating": "High",
        "mitigation": "Use strong authentication and role-based access control."
    },
    {
        "risk": "Excessive data collection",
        "likelihood": "Medium",
        "impact": "Medium",
        "rating": "Medium",
        "mitigation": "Collect only data necessary for the stated purpose."
    },
    {
        "risk": "Long data retention",
        "likelihood": "Medium",
        "impact": "Medium",
        "rating": "Medium",
        "mitigation": "Define and follow a data retention period."
    },
    {
        "risk": "Insider misuse",
        "likelihood": "Low",
        "impact": "High",
        "rating": "Medium",
        "mitigation": "Use least-privilege access and maintain access logs."
    }
]

for i, risk in enumerate(risks, start=1):
    print(f"\nRisk {i}: {risk['risk']}")
    print(f"Likelihood : {risk['likelihood']}")
    print(f"Impact     : {risk['impact']}")
    print(f"Risk Rating: {risk['rating']}")
    print(f"Mitigation : {risk['mitigation']}")

print("\n" + "=" * 50)
print("Privacy Impact Assessment completed.")
