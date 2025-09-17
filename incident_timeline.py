import re

logs = [
    "2025-09-17 08:51 Unauthorized access detected at server1.",
    "2025-09-17 08:52 Incident response team mobilized.",
    "2025-09-17 08:53 Server isolated from network.",
    "2025-09-17 08:54 Malware eradication script executed."
]

for entry in logs:
    timestamp = re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}', entry)
    action = entry.split(' ', 2)[2]
    print(f"{timestamp[0]}: {action}")
