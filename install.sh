#!/data/data/com.termux/files/usr/bin/bash
set +e  # Ignore errors and continue

echo -e "\n📦 Starting Full Termux Setup for Instagram 2k12-13 Hunter...\n"
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

# Run hunter directly
echo -e "\n🚀 Launching Accounts Hunter...\n"
python "2k12-13[team7x].py" || echo -e "❌ Failed to run hunter."