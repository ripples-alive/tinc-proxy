## Usage

You can run multiple tinc instance or multiple nodes with one instance as fallback for the strategy proxy.

```bash
#!/bin/bash

VPN_SERVER_IP=1.1.1.1
VPN_LAN_IP=172.16.1.2
VPN_GATEWAY_IP=172.16.1.1
INTERFACE=interface
NODE=node
SRC_DIR=~/src/tinc-proxy
TINC_DIR=/etc/tinc/$INTERFACE

ln -s $SRC_DIR/tinc-up $TINC_DIR/tinc-up
ln -s $SRC_DIR/tinc-down $TINC_DIR/tinc-down
ln -s $SRC_DIR/host-up $TINC_DIR/hosts/$NODE-up
ln -s $SRC_DIR/host-down $TINC_DIR/hosts/$NODE-down

cat <<EOF > $TINC_DIR/tinc-env
VPN_IP=$VPN_LAN_IP
BYPASS=("$VPN_SERVER_IP")
EOF

cat <<EOF > $TINC_DIR/hosts/$NODE-env
VPN_GATEWAY=$VPN_GATEWAY_IP
EOF
```
