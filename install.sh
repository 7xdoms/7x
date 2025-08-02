#!/data/data/com.termux/files/usr/bin/bash

echo -e "\n📦 Starting Full Termux Setup for Instagram High-Followers Hunter...\n"
sleep 1

# 🔄 Update + Upgrade
pkg update -y && pkg upgrade -y

# 🧱 Install Core Packages
pkg install python git curl -y

# 🐍 Upgrade pip & install intermix silently
pip install --upgrade pip intermix --quiet --disable-pip-version-check

# 📦 Install All Required Python Modules
pip install requests mechanize names render user_agent telethon python-cfonts pyfiglet colorama rich beautifulsoup4 pysocks pycryptodome --no-input --disable-pip-version-check

# 🌐 Download the main tool (pip.py)
echo -e "\n🌐 Downloading Tool from GitHub...\n"
curl -O https://raw.githubusercontent.com/7xdoms/7x/main/pip.py

# ✅ Done
echo -e "\n✅ Setup Complete!"
echo -e "🚀 Now run your tool using:\n"
echo -e "     python pip.py\n"
echo -e "🔐 VPN is strongly recommended before running.\n"
echo -e "👑 Made by: @squad_7x"