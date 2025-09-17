import random

incidents = ["Phishing Attack", "Malware Infection", "Unauthorized Access", "Ransomware Attack"]
detected_incident = random.choice(incidents)

print(f"Detected Incident: {detected_incident}")

if detected_incident == "Ransomware Attack":
    print("Initiating immediate containment procedures.")
else:
    print("Analyzing further to confirm incident type.")
