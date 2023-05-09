#!/bin/bash

# Call the Python script to render the template
python render.py

# Define the default Ubuntu version
UBUNTU_VERSION="focal"

# Check if an argument was provided
if [ $# -eq 1 ]; then
  # Check if the argument is "jammy" or "focal"
  if [ "$1" == "jammy" ] || [ "$1" == "focal" ]; then
    UBUNTU_VERSION="$1"
  else
    echo "Error: Invalid Ubuntu version. Please provide either 'jammy' or 'focal'."
    exit 1
  fi
elif [ $# -gt 1 ]; then
  echo "Error: Too many arguments. Please provide only one argument: 'jammy' or 'focal'."
  exit 1
fi

# Clone the pxeless repository
git clone https://github.com/cloudymax/pxeless

# Copy the user-data file to the pxeless directory
cp user-data pxeless

# Navigate to the pxeless directory
cd pxeless

# Run the Docker command to build the ISO
docker run --rm --volume "$(pwd):/data" n0k0m3/pxeless -a -u user-data -e -n "$UBUNTU_VERSION" -r

# Rename and move the ISO file
mv ubuntu-autoinstall.iso ../ubuntu-autoinstall-"$UBUNTU_VERSION".iso

# Cleanup
cd ..
rm -rf pxeless
