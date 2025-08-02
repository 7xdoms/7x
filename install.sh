#!/data/data/com.termux/files/usr/bin/bash

clear
echo -e "\033[1;36m🌐 Updating & Installing Dependencies...\033[0m"
pkg update -y && pkg upgrade -y
pkg install python git -y
pip install --upgrade pip --quiet --disable-pip-version-check
pip install requests mechanize names render user_agent telethon python-cfonts pyfiglet colorama rich beautifulsoup4 pysocks pycryptodome --no-input --disable-pip-version-check

echo -e "\033[1;32m✅ Dependencies installed successfully.\033[0m"

echo -e "\n\033[1;36m📦 Cloning Tool Repository...\033[0m"
git clone https://github.com/7xdoms/7x.git

cd 7x || exit

echo -e "\n\033[1;33m🚀 Running Tool Now...\033[0m"

# Handle spaces or emojis in filename
filename=$(ls | grep -i "High-Followers" | head -n 1)

if [ -f "$filename" ]; then
    python "$filename"
else
    echo -e "\033[1;31m❌ Tool script not found. Please check the filename.\033[0m"
fi