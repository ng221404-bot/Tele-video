# 🚀 Telegram File Drip Bot

A premium Telegram bot designed to deliver files (videos, photos, documents) in a sequence with controlled cooldowns, verification systems, and advanced admin management.

## ✨ Features

### 👤 User Features
- **Premium Verification:** Users must verify their identity via phone number sharing.
- **Drip Delivery:** Files are sent one by one in a specific sequence.
- **Cooldown System:** Intelligent waiting period between files (Individual or Global).
- **Auto-Delete:** Files automatically disappear after a set time to maintain privacy/exclusivity.
- **Content Protection:** Files can be restricted to prevent forwarding or saving.
- **Status Alerts:** Instant feedback on remaining cooldown time.

### 🛠 Admin Features (`/adm`)
- **Secure Access:** Protected by a secret key system.
- **File Management:**
  - **Upload:** Send any file type (Video, Photo, Document).
  - **Rename:** Update file captions anytime.
  - **Reorder:** Move files up or down in the sequence.
  - **Delete:** Remove files and auto-reorder the list.
- **Per-File Settings:**
  - Custom Cooldown (1h, 6h, 12h, 24h, or Custom).
  - Toggle Content Protection (ON/OFF).
  - Custom Auto-Delete timer.
- **Global Settings:** Set a fallback cooldown for all files.
- **Live Stats:** Track total users, verified members, and total files.

## 🛠 Setup & Installation

### 1. Prerequisites
- Python 3.8+
- Telegram Bot Token (from [@BotFather](https://t.me/BotFather))

### 2. Environment Variables
Create a `.env` file in the root directory:
```env
BOT_TOKEN=your_bot_token_here
ADMIN_CHAT_ID=your_telegram_id
ADMIN_SECRET=admin123
WELCOME_IMAGE_URL=https://your-image-url.com
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Bot
```bash
python bot.py
```

## 📂 Project Structure
- `bot/main.py`: Entry point and handler registration.
- `bot/handlers.py`: Core logic for user and admin flows.
- `bot/database.py`: SQLite database schema and connection management.
- `bot/keyboards.py`: All inline and reply keyboard structures.
- `bot/config.py`: Configuration and state management.

## 📝 Admin Commands
- `/adm`: Open the admin authentication prompt.
- Use the secret key set in `.env` to unlock the panel.

## 📜 License
MIT License. Feel free to use and modify!
