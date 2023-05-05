#################### Project dependencies installation #####################

sudo apt remove lxplug-ptbatt -y
# Disable Low Voltage Warning
########## Edit config file
#sudo nano /boot/config.txt
########## Add this line
#avoid_warnings=1

# Install python dependencies
sudo apt install python3-pil.imagetk -y
sudo pip install paho-mqtt
sudo pip install python-vlc
sudo pip install screeninfo


############# GUI Service Installation ############

sudo cp ./client.conf /etc/pulse/client.conf        
sudo sed -i '/^pulse-access:/ s/$/root,pi/' /etc/group  
sudo cp ./pulseaudio.service /lib/systemd/system/pulseaudio.service
echo  "Start Service pulseaudio..."
sudo chmod 644 /lib/systemd/system/pulseaudio.service
sudo systemctl daemon-reload
sudo systemctl --system enable pulseaudio.service
sudo systemctl --system start pulseaudio.service
echo -e "Finished\n"


sudo cp ./gui.service /lib/systemd/system/gui.service
echo  "Start Service GUI..."
sudo chmod 644 /lib/systemd/system/gui.service
chmod +x /home/pi/standard_display/Player/gui/gui.py
sudo systemctl daemon-reload
sudo systemctl enable gui.service
sudo systemctl start gui.service
echo -e "Finished\n"