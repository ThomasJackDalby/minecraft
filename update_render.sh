PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

msm mordor say "Updating world render..."
msm mordor worlds todisk
overviewer.py --config=/datadrive/minecraft/config.py
overviewer.py --config=/datadrive/minecraft/config.py --genPOI
msm mordor say "..done"
