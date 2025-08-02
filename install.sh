#!/data/data/com.termux/files/usr/bin/bash

# 🌐 Update & Install Dependencies
pkg update -y && pkg upgrade -y
pkg install git python -y
pip install --upgrade pip --quiet --disable-pip-version-check
pip install requests mechanize names render user_agent telethon python-cfonts pyfiglet colorama rich beautifulsoup4 pysocks pycryptodome --no-input --disable-pip-version-check

# 🧹 Remove old clone if exists
rm -rf 7x

# ⬇️ Clone the Repo
echo -e "\n🌐 Cloning tool from GitHub...\n"
git clone https://github.com/7xdoms/7x.git

# 🚀 Start Tool
cd 7x

# Rename long script to simple name
mv "High-Followers 💯 Meta [BY SQUAD 7X].py" 7x.py

# Run it
echo -e "\n🚀 Running the tool now...\n"
python3 7x.py