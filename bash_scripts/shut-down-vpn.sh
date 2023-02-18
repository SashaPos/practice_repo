#!/bin/bash

# Get the path of the VPN session
vpn_path=$(openvpn3 sessions-list | awk '/Path:/ {print $2}')

# Stop the VPN session
openvpn3 session-manage --session-path "$vpn_path" --disconnect
