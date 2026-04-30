import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Three sample alerts representing different attack types
alerts = [
    {
        "timestamp": "2026-04-29T14:32:11Z",
        "source": "Splunk",
        "severity": "high",
        "rule_name": "Multiple Failed Login Attempts",
        "user": "admin@company.com",
        "source_ip": "203.0.113.42",
        "destination": "vpn.company.com",
        "event_count": 47,
        "time_window": "5 minutes",
        "geo_location": "Russia",
        "previous_logins_from_this_ip": 0
    },
    {
        "timestamp": "2026-04-29T15:18:44Z",
        "source": "QRadar",
        "severity": "medium",
        "rule_name": "Privilege Escalation Detected",
        "user": "j.smith@company.com",
        "host": "FINANCE-DB-01",
        "action": "User added to Domain Admins group",
        "performed_by": "j.smith@company.com",
        "previous_role": "Finance Analyst",
        "approval_ticket": "none"
    },
    {
        "timestamp": "2026-04-29T16:45:02Z",
        "source": "AWS GuardDuty",
        "severity": "critical",
        "rule_name": "Large Data Transfer to External IP",
        "instance_id": "i-0a1b2c3d4e5f",
        "instance_role": "production-web-server",
        "bytes_transferred": "8.4 GB",
        "time_window": "12 minutes",
        "destination_ip": "185.220.101.34",
        "destination_country": "Unknown (Tor exit node)",
        "normal_traffic_pattern": "outbound to CDN only"
    }
]

# Loop through all alerts
for i, alert in enumerate(alerts, 1):
    prompt = f"""You are a senior SOC analyst. Below is a security alert.

Provide:
1. A 2-sentence plain-English summary of what happened
2. Severity assessment (low/medium/high/critical) with brief justification
3. Recommended next action for a junior SOC analyst
When you do it, don't punt as title plain English and so on, just do each section in a more professional, but Non AI way, make it look more like real anaylsis output.

Alert JSON:
{alert}

Keep your response concise and actionable."""

    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    print("=" * 60)
    print(f"ALERT #{i} — {alert['rule_name']}")
    print("=" * 60)
    print(message.content[0].text)
    print()