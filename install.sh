#!/data/data/com.termux/files/usr/bin/bash
set +e  # Ignore errors and continue

echo -e "\n📦 Starting Full Termux Setup for Instagram 2k12-13 hunter...\n"
sleep 1

# Update and install dependencies
pkg update -y
pkg upgrade -y
pkg install -y python git curl

# Upgrade pip and install Python modules
pip install --upgrade pip intermix --quiet --disable-pip-version-check
pip install requests mechanize names render user_agent telethon python-cfonts pyfiglet colorama rich beautifulsoup4 pysocks pycryptodome --no-input --disable-pip-version-check

# Remove old folder if exists
[ -d "7x" ] && rm -rf 7x

# Clone only the hunter file
git clone --filter=blob:none --no-checkout https://github.com/7xdoms/7x.git 7x
cd 7x || exit
git sparse-checkout init --cone
git sparse-checkout set "2k12-13[team7x].py"
git checkout

# Ask for token in bash
echo -e "\n➤ Please enter your BOT TOKEN (will be passed to script):"
read -r BOT_TOKEN

# Create a wrapper runner for the hunter
cat > run_hunter.py <<PY
import sys
try:
    BOT_TOKEN = "${BOT_TOKEN}"
    if not BOT_TOKEN.strip():
        print("❌ No token provided. Exiting.")
        sys.exit()
    print(f"✅ Token loaded: {BOT_TOKEN[:5]}****")
    from pathlib import Path
    hunter_file = Path("2k12-13[team7x].py")
    if not hunter_file.exists():
        print("❌ Hunter script missing.")
        sys.exit()
    exec(hunter_file.read_text())
except Exception as e:
    print(f"❌ Error: {e}")
PY

# Run hunter with token
echo -e "\n🚀 Launching Accounts Hunter...\n"
python run_hunter.py || echo -e "❌ Failed to run hunter."