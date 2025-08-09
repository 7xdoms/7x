#!/data/data/com.termux/files/usr/bin/bash

set +e  # Continue even if a command fails

echo -e "\n📦 Starting Full Termux Setup for Instagram High-Followers Hunter...\n"
sleep 1

pkg update -y
pkg upgrade -y
pkg install -y python git curl

pip install --upgrade pip intermix --quiet --disable-pip-version-check
pip install -y requests mechanize names render user_agent telethon python-cfonts pyfiglet colorama rich beautifulsoup4 pysocks pycryptodome --no-input --disable-pip-version-check

# Remove old repo if exists
[ -d "7x" ] && rm -rf 7x

# Clone only the required file
git clone --filter=blob:none --no-checkout https://github.com/7xdoms/7x.git 7x
cd 7x || exit
git sparse-checkout init --cone
git sparse-checkout set "2k12-13[team7x].py"
git checkout

echo -e "\n✅ Setup Complete!"
echo -e "🚀 Launching tool...\n"
python "2k12-13[team7x].py" || echo -e "❌ Failed to run 2k12-13[team7x].py"