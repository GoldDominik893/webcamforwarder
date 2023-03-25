$ echo "Installing dependancies for webcamforwarder..."
sudo apt-get install python3-pip
pip --version
pip install Flask
pip install opencv-python

read -n1 -s -r -p $'Press space to continue...\n' key

if [ "$key" = ' ' ]; then

else