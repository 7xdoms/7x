#!/data/data/com.termux/files/usr/bin/bash

echo -e "\n📦 Starting Full Termux Setup for Instagram High-Followers Hunter...\n"
sleep 1

pkg update -y && pkg upgrade -y
pkg install python git curl -y

pip install --upgrade pip intermix --quiet --disable-pip-version-check
pip install requests mechanize names render user_agent telethon python-cfonts pyfiglet colorama rich beautifulsoup4 pysocks pycryptodome --no-input --disable-pip-version-check

rm -rf 7x
git clone https://github.com/7xdoms/7x.git
cd 7x

echo -e "\n✅ Setup Complete!"
echo -e "🚀 Launching tool...\n"
python team7x.py