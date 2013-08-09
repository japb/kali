#!/bin/bash

for address in $(seq 1 254); do
ping 192.168.241.$address -c 1 | grep "bytes from" | cut -d " " -f 4 | cut -d ":" -f 1 &
done

