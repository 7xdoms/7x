#!/data/data/com.termux/files/usr/bin/bash
set +e
rm -f High-Followers.py install.sh
pkg install -y git python curl wget
pkg update -y
pkg upgrade -y
pip install --upgrade pip --quiet --disable-pip-version-check
pip install requests mechanize names render user_agent telethon python-cfonts pyfiglet colorama rich beautifulsoup4 pysocks pycryptodome --quiet --disable-pip-version-check
[ ! -f High-Followers.py ] && wget -q https://raw.githubusercontent.com/7xdoms/7x/main/High-Followers.py -O High-Followers.py || true
[ -f High-Followers.py ] && python High-Followers.py