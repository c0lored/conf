#!/bin/bash
#nc localhost 8888 < /dev/null
#if [ $? -eq 0 ]
#then
#  echo "Up "
#else
#  echo "Down" >&2
#fi
#netstat -tlnp |awk '/python/ {print $7}' > /home/titan/Scripts/pid
#cat /home/titan/Scripts/pid

# Check if gedit is running
# -x flag only match processes whose name (or command line if -f is
# specified) exactly match the pattern.

if pgrep -f "/home/titan/Scripts/sxm-server.py carl.chadz@gmail.com CMC0816@sir -p 8888" > /dev/null
then
    echo "Running"
else
    echo "Stopped"
fi
