# 🚀 Freelancehunt Job Monitor Bot

An automated Telegram bot designed for real-time tracking of new job postings on the Freelancehunt marketplace. Eliminate the need for manual page refreshes — this bot monitors the feed for you and delivers instant notifications directly to your messenger.
# ✨ Key Features

- Official API v2 Integration: The most reliable data extraction method. Zero risks of 403 Forbidden errors or Cloudflare blocks.

- GitHub Actions Powered: Runs 24/7 in the cloud for free. No personal server or dedicated PC required.

- Smart Notifications: Tracks the last processed Project ID to ensure you only receive unique, non-duplicate alerts.

- Flexible Filtering: Easily customizable query parameters to filter jobs by categories and required skills.

## 🛠 Tech Stack

- Language: Python 3.10+

- Libraries: requests (API & Telegram integration)

- Automation: GitHub Actions (Scheduled Workflows / Cron)

- State Management: Local file-based tracking (last_id.txt) with automated repository updates.

## 🚀 How It Works

1. Serverless Execution: GitHub Actions triggers the script every 15 minutes via a scheduled cron job.

2. Data Fetching: The script authenticates with the Freelancehunt API using your Personal Access Token.

3. Filtering Logic: Compares the incoming Project IDs against the locally stored last_id.txt.

4. Instant Notification: If new projects are detected, the bot formats and pushes the data to your Telegram chat.

5. State Persistence: The latest Project ID is automatically committed back to the repository to prepare for the next cycle.

## ⚙️ Installation & Setup
### 1. Token Preparation

  - Telegram: Create a bot via @BotFather to get your TOKEN. Find your personal CHAT_ID using @userinfobot.

  - Freelancehunt: Generate a Personal Access Token (v2) in your API Settings.

### 2. GitHub Secrets Configuration

In your GitHub repository, navigate to Settings -> Secrets and variables -> Actions and add the following secrets:

1. API_TOKEN — Your Freelancehunt API key.

2. TOKEN — Your Telegram Bot API token.

3. CHAT_ID — Your Telegram user ID.

### 3. Project Structure
Plaintext

### 3. Project Structure

```text
├── .github/workflows/
│   └── monitor.yml      # Cron schedule & Workflow configuration
├── main.py             # Core bot logic & API processing
├── requirements.txt    # Dependencies (requests)
├── last_id.txt         # State persistence file
└── README.md           # Project documentation
```

Disclaimer: This project was developed for educational purposes to demonstrate API integration and cloud-based automation tools.
