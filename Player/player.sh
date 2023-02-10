#################### Project dependencies installation #####################

# Remove already installed Chromium and reinstall it with chromedriver:

sudo apt purge --remove chromium-browser -y
sudo apt -y autoremove && sudo apt -y autoclean 
sudo apt install chromium-chromedriver -y 

# Reboot

# Install python dependencies
pip install selenium==4.7.2
pip install psutil==5.9.4
pip install websockets==10.4
pip install pillow

# Disable Low Voltage Warning
########## Edit config file
#sudo nano /boot/config.txt
########## Add this line
#avoid_warnings=1


############# Player Service Installation ############

sudo cp ./player.service /lib/systemd/system/player.service
echo  "Start Service Player..."
sudo chmod 644 /lib/systemd/system/player.service
chmod +x /home/pi/standard_display/Player/backend/player.py
sudo systemctl daemon-reload
sudo systemctl enable player.service
sudo systemctl start player.service
echo -e "Finished\n"