@Echo off
apt-get install python3-pip
pip --version
pip install Flask
pip install opencv-python

read -n1 -s -r -p $'Press space to continue...\n' key

if [ "$key" = ' ' ]; then
    # Space pressed, do something
    # echo [$key] is empty when SPACE is pressed # uncomment to trace
else
    # Anything else pressed, do whatever else.
    # echo [$key] not empty