Practical-05: Anonymization Techniques

Implementation of Data Anonymization Techniques on a Real-World Dataset

⸻

 Aim

To understand and implement different data anonymization techniques, such as k-anonymity, data masking, and differential privacy, and apply them to a real-world dataset to protect sensitive information while maintaining data utility.

⸻

 Objectives

The objectives of this practical are:

1. To understand the concept of data anonymization.
2. To identify personally identifiable information (PII) and sensitive attributes.
3. To implement k-anonymity.
4. To implement data masking.
5. To implement differential privacy.
6. To compare the dataset before and after anonymization.
7. To understand the privacy-utility trade-off.
8. To understand real-world applications of data anonymization.

⸻

1. Introduction

Data anonymization is the process of modifying or transforming data so that information about individuals cannot be easily associated with a specific person.

Organizations often collect and process personal information for:

* Research
* Education
* Healthcare
* Banking
* Marketing
* Government services
* Machine learning

Before sharing such datasets, sensitive information should be protected.

Basic Process

Original Dataset
       ↓
Identify Sensitive Information
       ↓
Apply Anonymization Techniques
       ↓
Anonymized Dataset
       ↓
Data Analysis / Sharing

⸻

2. What is Data Anonymization?

Data anonymization removes or transforms identifying information so that individuals cannot be directly or easily identified from the released dataset.

For example, consider:

Name	Age	City	Course	Marks
Rahul	21	Delhi	BCA	85
Priya	22	Delhi	BCA	91

The names can be removed or transformed:

Age	City	Course	Marks
20–25	Delhi	BCA	85
20–25	Delhi	BCA	91

This reduces the possibility of directly identifying individuals.

⸻

3. Types of Data Attributes

Data attributes can be classified into different categories.

3.1 Direct Identifiers

Direct identifiers can directly identify a person.

Examples:

* Name
* Email address
* Phone number
* Aadhaar number
* Passport number
* Student ID

Example:

Name = Rahul Sharma
Email = rahul@example.com

⸻

3.2 Quasi-Identifiers

Quasi-identifiers may not uniquely identify a person individually, but combinations of them can potentially identify an individual.

Examples:

* Age
* Gender
* ZIP/PIN code
* City
* Date of birth
* Education

For example:

Age + City + Gender

may be sufficient to distinguish an individual in a small dataset.

⸻

3.3 Sensitive Attributes

Sensitive attributes contain private information about an individual.

Examples:

* Salary
* Medical condition
* Exam marks
* Financial information
* Political preferences
* Personal records

⸻

4. Dataset Used

For this practical, a student dataset is used.

Example attributes:

Attribute	Type	Category
Name	String	Direct Identifier
Email	String	Direct Identifier
Phone	String	Direct Identifier
Age	Integer	Quasi-Identifier
Gender	Categorical	Quasi-Identifier
City	String	Quasi-Identifier
Course	String	Quasi-Identifier
Marks	Integer	Sensitive Attribute

Example Dataset

Name,Email,Phone,Age,Gender,City,Course,Marks
Rahul Sharma,rahul@gmail.com,9876543210,21,Male,Delhi,BCA,85
Priya Singh,priya@gmail.com,9876543211,22,Female,Delhi,BCA,91
Aman Kumar,aman@gmail.com,9876543212,21,Male,Noida,BCA,78
Neha Gupta,neha@gmail.com,9876543213,22,Female,Noida,BCA,88
Rohit Verma,rohit@gmail.com,9876543214,23,Male,Ghaziabad,BCA,72
Anjali Sharma,anjali@gmail.com,9876543215,21,Female,Delhi,BCA,95

Note: The dataset used for demonstration contains synthetic/example student information and does not represent real individuals.

⸻

5. Technologies Used

Programming Language

Python

Environment

Google Colab / Jupyter Notebook

Libraries

pandas
numpy
matplotlib

⸻

6. Installation

Run the following command in Google Colab:

!pip install pandas numpy matplotlib

⸻

7. Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

⸻

8. Creating the Dataset

data = {
    "Name": [
        "Rahul Sharma",
        "Priya Singh",
        "Aman Kumar",
        "Neha Gupta",
        "Rohit Verma",
        "Anjali Sharma"
    ],
    "Email": [
        "rahul@gmail.com",
        "priya@gmail.com",
        "aman@gmail.com",
        "neha@gmail.com",
        "rohit@gmail.com",
        "anjali@gmail.com"
    ],
    "Phone": [
        "9876543210",
        "9876543211",
        "9876543212",
        "9876543213",
        "9876543214",
        "9876543215"
    ],
    "Age": [21, 22, 21, 22, 23, 21],
    "Gender": [
        "Male",
        "Female",
        "Male",
        "Female",
        "Male",
        "Female"
    ],
    "City": [
        "Delhi",
        "Delhi",
        "Noida",
        "Noida",
        "Ghaziabad",
        "Delhi"
    ],
    "Course": [
        "BCA",
        "BCA",
        "BCA",
        "BCA",
        "BCA",
        "BCA"
    ],
    "Marks": [85, 91, 78, 88, 72, 95]
}
df = pd.DataFrame(data)
print("Original Dataset:")
display(df)

⸻

9. Inspecting the Dataset

print("Dataset Shape:")
print(df.shape)
print("\nDataset Information:")
df.info()
print("\nStatistical Summary:")
display(df.describe())

⸻

10. Identifying Sensitive Information

The following attributes contain information that should be protected:

Direct Identifiers

Name
Email
Phone

Quasi-Identifiers

Age
Gender
City
Course

Sensitive Attribute

Marks

⸻

11. Technique 1 – Data Masking

Definition

Data masking is a technique in which sensitive information is replaced or partially hidden so that the original value cannot be easily viewed.

For example:

9876543210

can become:

XXXXXX3210

Similarly:

rahul@gmail.com

can become:

r****@gmail.com

⸻

11.1 Masking Phone Numbers

df_masked = df.copy()
df_masked["Phone"] = df_masked["Phone"].apply(
    lambda x: "X" * (len(x) - 4) + x[-4:]
)
display(df_masked)

Example Output

Name	Phone
Rahul Sharma	XXXXXX3210
Priya Singh	XXXXXX3211
Aman Kumar	XXXXXX3212

⸻

12. Masking Email Addresses

def mask_email(email):
    username, domain = email.split("@")
    
    if len(username) <= 2:
        masked_username = "X" * len(username)
    else:
        masked_username = username[0] + "X" * (len(username) - 2) + username[-1]
    
    return masked_username + "@" + domain
df_masked["Email"] = df_masked["Email"].apply(mask_email)
display(df_masked)

Example

rahul@gmail.com

becomes:

rXXXl@gmail.com

⸻

13. Removing Direct Identifiers

Another anonymization technique is removing direct identifiers completely.

df_removed = df.copy()
df_removed = df_removed.drop(
    columns=["Name", "Email", "Phone"]
)
display(df_removed)

The resulting dataset contains only the information required for analysis.

⸻

14. Technique 2 – k-Anonymity

Definition

k-anonymity is a privacy model in which each combination of selected quasi-identifiers appears in at least k records.

For example, if:

k = 2

then every combination of quasi-identifiers should occur in at least two records.

Formula

A dataset satisfies k-anonymity if:

|Equivalence Class| ≥ k

where an equivalence class contains records having the same quasi-identifier values.

⸻

15. Generalization

One way to achieve k-anonymity is generalization.

Instead of storing exact age:

21
22
23

we can store:

20-25
20-25
20-25

⸻

15.1 Age Generalization

df_k = df.copy()
def generalize_age(age):
    if 18 <= age <= 25:
        return "18-25"
    elif 26 <= age <= 35:
        return "26-35"
    else:
        return "36+"
df_k["Age"] = df_k["Age"].apply(generalize_age)
display(df_k)

⸻

16. City Generalization

Cities can also be generalized into broader geographical regions.

city_mapping = {
    "Delhi": "Delhi-NCR",
    "Noida": "Delhi-NCR",
    "Ghaziabad": "Delhi-NCR"
}
df_k["City"] = df_k["City"].replace(city_mapping)
display(df_k)

Now several cities are represented as:

Delhi-NCR

This reduces the uniqueness of individual records.

⸻

17. Checking k-Anonymity

We can group records based on quasi-identifiers.

quasi_identifiers = [
    "Age",
    "Gender",
    "City",
    "Course"
]
equivalence_classes = (
    df_k.groupby(quasi_identifiers)
    .size()
    .reset_index(name="Count")
)
print("Equivalence Classes:")
display(equivalence_classes)

⸻

Checking k = 2

k = 2
equivalence_classes["Meets_k"] = (
    equivalence_classes["Count"] >= k
)
display(equivalence_classes)

A record belongs to an equivalence class that satisfies k-anonymity when its class count is at least k.

⸻

18. Technique 3 – Differential Privacy

Definition

Differential privacy is a mathematical framework for limiting what can be learned about an individual from the output of a data analysis.

Instead of releasing exact statistics, controlled random noise can be added.

For example:

Actual Average Marks = 84.83
Released Average Marks = 85.41

The released result remains useful for analysis while making it harder to infer the contribution of a particular individual.

⸻

19. Differential Privacy using Laplace Noise

The Laplace mechanism can be used to add noise to numerical queries.

The basic form is:

Noisy Result = Actual Result + Laplace Noise

The amount of noise depends on:

* Sensitivity
* Privacy parameter ε (epsilon)

Smaller ε generally means stronger privacy and more noise.

⸻

20. Implementing Differential Privacy

First calculate the actual average.

actual_average = df["Marks"].mean()
print("Actual Average Marks:", actual_average)

⸻

Adding Laplace Noise

epsilon = 1.0
sensitivity = (
    df["Marks"].max() - df["Marks"].min()
) / len(df)
noise = np.random.laplace(
    loc=0,
    scale=sensitivity / epsilon
)
private_average = actual_average + noise
print("Actual Average:", actual_average)
print("Noise Added:", noise)
print("Differentially Private Average:", private_average)

⸻

21. Comparing Different Privacy Levels

We can observe the effect of different values of ε.

actual_average = df["Marks"].mean()
epsilons = [0.1, 0.5, 1.0, 2.0]
results = []
for epsilon in epsilons:
    
    noise = np.random.laplace(
        loc=0,
        scale=sensitivity / epsilon
    )
    
    private_average = actual_average + noise
    
    results.append({
        "Epsilon": epsilon,
        "Noise": noise,
        "Private Average": private_average
    })
dp_results = pd.DataFrame(results)
display(dp_results)

⸻

22. Visualizing Differential Privacy

plt.figure(figsize=(8, 5))
plt.plot(
    dp_results["Epsilon"],
    dp_results["Private Average"],
    marker="o"
)
plt.axhline(
    actual_average,
    linestyle="--",
    label="Actual Average"
)
plt.xlabel("Epsilon (ε)")
plt.ylabel("Average Marks")
plt.title("Effect of Differential Privacy")
plt.legend()
plt.grid(True)
plt.show()

⸻

23. Complete Anonymization Workflow

The overall workflow is:

                 Original Dataset
                        │
                        ▼
             Identify Sensitive Data
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
     Data Masking   k-Anonymity   Differential
                                   Privacy
          │             │             │
          ▼             ▼             ▼
     Mask Direct     Generalize     Add Controlled
     Identifiers     Attributes        Noise
          │             │             │
          └─────────────┼─────────────┘
                        ▼
                Anonymized Data
                        │
                        ▼
                 Data Analysis

⸻

24. Before vs After Anonymization

Before

Name          Email              Phone        Age  City
----------------------------------------------------------
Rahul Sharma  rahul@gmail.com    9876543210   21   Delhi
Priya Singh   priya@gmail.com    9876543211   22   Delhi
Aman Kumar    aman@gmail.com     9876543212   21   Noida

The dataset contains directly identifiable information.

⸻

After Data Masking

Name          Email              Phone
------------------------------------------------
Rahul Sharma  rXXXl@gmail.com    XXXXXX3210
Priya Singh   pXXXa@gmail.com    XXXXXX3211
Aman Kumar    aXXn@gmail.com     XXXXXX3212

Sensitive values are partially hidden.

⸻

After Removing Direct Identifiers

Age       Gender       City          Course
--------------------------------------------
18-25     Male         Delhi-NCR     BCA
18-25     Female       Delhi-NCR     BCA
18-25     Male         Delhi-NCR     BCA

Direct identifiers are removed and quasi-identifiers are generalized.

⸻

25. Privacy-Utility Trade-off

Anonymization introduces a trade-off between privacy and data utility.

More Privacy
     ↑
     │
     │       Generalization
     │      / Masking
     │
     │
     │
     └────────────────────→
                    More Utility

If too much information is removed or generalized:

Privacy ↑
Utility ↓

If very little information is changed:

Privacy ↓
Utility ↑

Therefore, an appropriate balance should be maintained.

⸻

26. Comparison of Techniques

Technique	Main Purpose	Method	Example
Data Masking	Hide sensitive values	Replace part of data	XXXX3210
k-Anonymity	Reduce re-identification	Generalization/suppression	21 → 18-25
Differential Privacy	Protect individual contribution	Add mathematical noise	85 → 85.7

⸻

27. Advantages

Data Masking

* Simple to implement
* Easy to understand
* Useful for displaying sensitive data
* Protects direct identifiers

k-Anonymity

* Reduces uniqueness of records
* Useful when publishing datasets
* Easy to understand conceptually
* Helps reduce re-identification risk

Differential Privacy

* Provides a formal privacy framework
* Protects individual contributions to statistical outputs
* Useful for statistical analysis
* Can provide quantifiable privacy guarantees under the model’s assumptions

⸻

28. Limitations

Data Masking

* Masking may not protect against all re-identification attacks.
* Some information can remain inferable.
* Improper masking can expose sensitive information.

k-Anonymity

* Vulnerable to some attacks involving sensitive-attribute distributions.
* Excessive generalization can reduce data utility.
* Choosing an appropriate value of k is important.

Differential Privacy

* Adding too much noise can reduce accuracy.
* The privacy parameter ε must be selected carefully.
* More complex to understand and implement correctly.

⸻


