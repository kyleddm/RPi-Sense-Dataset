mosquitto_sub -h "192.168.0.100" -t "#" -v | tee BKP/backup_data2.out
#This command does two things:
#1. It subscribes to all (#) messages on the hub 192.168.0.100
#2. it dumps the output to a file.
