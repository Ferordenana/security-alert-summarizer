# security-alert-summarizer
# Security Alert Summarizer

AI-powered triage tool for SOC analysts. Takes raw security alerts (JSON) and uses Claude to generate plain-English summaries, severity assessments, and recommended actions.

## Why

SOC analysts spend hours reading raw SIEM alerts. Most are noise. This tool compresses that triage work into seconds.

## Tech

Python · Anthropic Claude API · python-dotenv

## Run it
pip install anthropic python-dotenv

Create `.env` with `ANTHROPIC_API_KEY=your-key-here`, then:
python alert_summarizer.py

## Status

Active development. Part of a broader project building AI agents for cloud security automation.
