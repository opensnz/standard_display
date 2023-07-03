#################### Project dependencies installation #####################

# Install python dependencies
sudo apt install libopencv-dev python3-opencv -y
sudo pip install paho-mqtt
sudo pip install -U numpy





############# Detection Service Installation ############

sudo cp ./detection.service /lib/systemd/system/detection.service
echo  "Start Service Detection..."
sudo chmod 644 /lib/systemd/system/detection.service
chmod +x /home/pi/standard_display/detection/backend/detection.py
sudo systemctl daemon-reload
sudo systemctl enable detection.service
sudo systemctl start detection.service
echo -e "Finished\n"