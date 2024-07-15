#!/bin/bash
set -e

# Source the ROS 2 setup file
source "/opt/ros/foxy/setup.bash"

# Set DISPLAY environment variable for GUI applications
export DISPLAY=$DISPLAY
export QT_X11_NO_MITSHM=1

# Execute the command passed to the script
exec "$@"

conda init
