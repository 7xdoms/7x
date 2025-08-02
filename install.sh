#!/data/data/com.termux/files/usr/bin/bash

echo -e "\n📦 Starting Full Termux Setup for High-Followers Hunter...\n"
sleep 1

# 🔄 Update and upgrade Termux packages
pkg update -y && pkg upgrade -y

# 🧱 Install required packages
pkg install python git curl -y

# 🐍 Upgrade pip silently
pip install --upgrade pip intermix --quiet --disable-pip-version-check

# 📦 Install all necessary Python modules
pip install requests mechanize names render user_agent telethon python-cfonts pyfiglet colorama rich beautifulsoup4 pysocks pycryptodome --no-input --disable-pip-version-check

# 🌐 Clone the GitHub repository
echo -e "\n🌐 Cloning tool from GitHub...\n"
git clone https://github.com/7xdoms/7x.git

# 📁 Move into the folder
cd 7x

# 🚀 Run the main Python script
echo -e "\n🚀 Running the tool now...\n"
python 'High-Followers 💯 Meta [BY SQUAD 7X].py'