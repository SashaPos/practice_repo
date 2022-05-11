#!/bin/bash
#Utility allows to safely remove USB-drive
read -p "Enter the name of the device: " device_name
udisksctl unmount -b $device_name ;
udisksctl power-off -b $device_name
