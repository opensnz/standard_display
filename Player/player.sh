#################### Project dependencies installation #####################

# Install python dependencies
sudo pip install psutil==5.9.4
sudo pip install pillow
sudo pip install paho-mqtt
sudo pip install websocket-client



############# Player Service Installation ############

sudo cp ./player.service /lib/systemd/system/player.service
echo  "Start Service Player..."
sudo chmod 644 /lib/systemd/system/player.service
chmod +x /home/pi/standard_display/Player/backend/player.py
sudo systemctl daemon-reload
sudo systemctl enable player.service
sudo systemctl start player.service
echo -e "Finished\n"
