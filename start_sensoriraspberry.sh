#!/bin/bash
raspcpu=$(top -bn 2 -d 0.01 | grep 'Cpu(s)' | tail -n 1 | awk '{print $2+$4+$6}')
uptime=$(uptime | awk '{print int($3+$5/1440),"giorni"}')
disco_occ=$(df -h | grep /dev/root | awk '{print $5}')
ram_occ=$(free -m | awk 'FNR == 2 {print int($3/$2*100)}')

mosquitto_pub -h 192.168.10.114 -m "$raspcpu" -t raspcpu -u 'user' -P 'password' -r
mosquitto_pub -h 192.168.10.114 -m "$uptime" -t uptime -u 'user' -P 'password' -r
mosquitto_pub -h 192.168.10.114 -m "$disco_occ" -t disco_occ -u 'user' -P 'password' -r
mosquitto_pub -h 192.168.10.114 -m "$ram_occ" -t ram_occ -u 'user' -P 'password' -r
