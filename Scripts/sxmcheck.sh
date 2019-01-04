#!/bin/bash
nc localhost 8888 < /dev/null
if [ $? -eq 0 ]
then
  echo "Up "
else
  echo "Down" >&2
fi
netstat -tlnp |awk '/python/ {print $7}' > /home/titan/Scripts/pid
cat /home/titan/Scripts/pid
