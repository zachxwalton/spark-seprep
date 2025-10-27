#!/bin/sh

echo "------------------------------------"
echo " Welcome to the Info Script! "
echo "------------------------------------"

echo "Hello!"
echo "Here’s some system info from inside the container:"
echo "------------------------------------"

# Show the current date and time
date

# Show current user
echo "Current user: $(whoami)"

# Show the OS version
echo "OS version: $(cat /etc/os-release | grep PRETTY_NAME | cut -d= -f2)"

# Show disk usage summary
echo "Disk usage:"
df -h | head -n 5

echo "------------------------------------"
echo "Script complete. Goodbye, $name!"
