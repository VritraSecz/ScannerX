# !/bin/bash
# Created by Alex Butler (VritraSecz)
# Don't be a copy cat, Be original always

cat .ban
echo
echo

if [ -d "/data/data/com.termux/files" ];then
    echo '[*] Setting up it in your termux'
    apt update -y
    apt upgrade -y
    apt install python3 termux-tools wget -y
    touch scanx
    echo 'python /data/data/com.termux/ScannerX/scannerx.py $1' > scanx
    chmod +x scanx scannerx.py
    mv scanx /data/data/com.termux/files/usr/bin
    rm -rf /data/data/com.termux/ScannerX
    mkdir /data/data/com.termux/ScannerX
    mv scannerx.py /data/data/com.termux/ScannerX
    rm -rf *
else
    sudo echo '[*] Setting up it in your Linux'
    sudo apt update -y
    sudo apt upgrade -y
    sudo apt install python3 wget -y
    sudo touch scanx
    sudo echo 'python3 /usr/local/ScannerX/scannerx.py $1' > scanx
    sudo chmod +x scanx scannerx.py
    sudo mv scanx /usr/local/bin
    sudo rm -rf /usr/local/ScannerX
    sudo mkdir /usr/local/ScannerX
    sudo mv scannerx.py /usr/local/ScannerX
    sudo rm -rf *

fi

echo
echo "[*] Installation is finished, So now you can launch ScannerX by command 'scanx <domain>'"
echo
echo
