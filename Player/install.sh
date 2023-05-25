echo "Installation of Mosquitto..."
sudo chmod a+x ./mosquitto.sh
source ./mosquitto.sh

echo "Installation of Player Service..."
sudo chmod a+x ./player.sh
source ./player.sh

echo "Installation of Detection Service..."
sudo chmod a+x ./detection.sh
source ./detection.sh

echo "Installation of GUI Service..."
sudo chmod a+x ./gui.sh
source ./gui.sh