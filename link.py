import os

rules = [
    "sudo ufw default deny incoming",
    "sudo ufw default allow outgoing",
    "sudo ufw allow ssh",
    "sudo ufw allow 80/tcp",
    "sudo ufw enable"
]

for rule in rules:
    os.system(rule)

print("Firewall rules applied successfully.")
