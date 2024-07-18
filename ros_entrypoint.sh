#!/bin/bash
# set -e

# # Source the ROS 2 setup file
# source "/opt/ros/foxy/setup.bash"

# # Set DISPLAY environment variable for GUI applications
# export DISPLAY=$DISPLAY
# export QT_X11_NO_MITSHM=1

# # Enable strict mode.
# set -euo pipefail
# # ... Run whatever commands ...

# # Temporarily disable strict mode and activate conda:
# set +euo pipefail
conda activate MonoGS
conda env update -f environment_1.yml

# Re-enable strict mode:
# set -euo pipefail

# export LIBGL_ALWAYS_INDIRECT=0
# export MESA_GL_VERSION_OVERRIDE=4.5
# export MESA_GLSL_VERSION_OVERRIDE=450
# export LIBGL_ALWAYS_SOFTWARE=1

# Execute the command passed to the script
exec "$@"
sh /MonoGS/start_vnc.sh

