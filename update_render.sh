PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

msm mordor say "Updating world render..."
msm mordor worlds todisk
overviewer.py --config=/datadrive/minecraft-overviewer/server.txt
overviewer.py --config=/datadrive/minecraft-overviewer/server.txt --genPOI
msm mordor say "..done"
