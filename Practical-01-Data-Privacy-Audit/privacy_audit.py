from dataclasses import dataclass

@dataclass
class DataAsset:
    name: str
    category: str
    purpose: str
    storage: str
    access: str
    retention: str
    risk: str

assets = [
    DataAsset("Student name", "Personal", "Academic administration",
              "College database", "Authorized staff", "Course duration + 1 year", "Low"),
    DataAsset("Email address", "Personal", "Communication",
              "College database", "Authorized staff", "Course duration + 1 year", "Medium"),
    DataAsset("Phone number", "Personal", "Emergency/contact",
              "College database", "Authorized staff", "Course duration + 1 year", "Medium"),
    DataAsset("Government ID", "Sensitive", "Identity verification",
              "Restricted storage", "Limited authorized staff", "Minimum necessary period", "High"),
]

controls = {
    "Low": "Maintain access control and documented retention.",
    "Medium": "Use least privilege, encryption in transit and regular review.",
    "High": "Restrict access, encrypt at rest, log access and minimize retention."
}

print("DATA PRIVACY AUDIT")
print("=" * 70)

for asset in assets:
    print(f"Data: {asset.name}")
    print(f"Category: {asset.category}")
    print(f"Purpose: {asset.purpose}")
    print(f"Storage: {asset.storage}")
    print(f"Access: {asset.access}")
    print(f"Retention: {asset.retention}")
    print(f"Risk: {asset.risk}")
    print(f"Recommended control: {controls[asset.risk]}")
    print("-" * 70)

print("Audit completed.")
