#!/data/data/com.termux/files/usr/bin/bash
set +e  # Ignore errors and continue

echo -e "\n📦 Starting Termux Setup for Instagram High-Followers Tool...\n"
sleep 1

# First install git with -y to ensure git is available
pkg install -y git || true

# Then update and install other dependencies
pkg update -y || true
pkg upgrade -y || true
pkg install -y python curl wget || true

# Upgrade pip and install Python modules
pip install --upgrade pip intermix --quiet --disable-pip-version-check || true
pip install requests mechanize names render user_agent telethon python-cfonts pyfiglet colorama rich beautifulsoup4 pysocks pycryptodome --quiet --disable-pip-version-check || true

# Download High-Followers.py
wget -q https://raw.githubusercontent.com/7xdoms/7x/main/High-Followers.py -O High-Followers.py || {
    echo "❌ Failed to download High-Followers.py"
    exit 1
}

# Run High-Followers directly
echo -e "\n🚀 Launching High-Followers Tool...\n"
python High-Followers.py || echo -e "❌ Failed to run High-Followers.py."