#!/data/data/com.termux/files/usr/bin/bash

echo -e "\n📦 Starting Full Termux Setup for Instagram High-Followers Hunter...\n"
sleep 1

pkg update -y || true
pkg upgrade -y || true
pkg install python git curl -y || true

pip install --upgrade pip intermix --quiet --disable-pip-version-check || true
pip install requests mechanize names render user_agent telethon python-cfonts pyfiglet colorama rich beautifulsoup4 pysocks pycryptodome --no-input --disable-pip-version-check || true

[ -d "7x" ] && rm -rf 7x
git clone https://github.com/7xdoms/7x.git || {
    echo -e "\n❌ Failed to clone repo. Check your internet connection.\n"
    exit 1
}
cd 7x || exit

echo -e "\n✅ Setup Complete!"
echo -e "🚀 Launching tool...\n"
python team7x.py || echo -e "❌ team7x.py not found or failed to run."