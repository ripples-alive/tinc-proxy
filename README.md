## Usage

You can run multiple tinc instance or multiple nodes with one instance as fallback for the strategy proxy.

```bash
#!/bin/bash
# file: tinc-up
ip link set $INTERFACE up
ip addr add 172.16.1.1/24 dev $INTERFACE

export VPN_GATEWAY=172.16.1.1
export SET_NAME=tinc_bypass
/tinc-proxy/tinc-up
```

```bash
#!/bin/bash
# file: tinc-down
export VPN_GATEWAY=172.16.1.1
export SET_NAME=tinc_bypass
/tinc-proxy/tinc-down

ip link set $INTERFACE down
```

```bash
#!/bin/bash
# file: host-up
export VPN_GATEWAY=172.16.1.1
export SET_NAME=tinc_bypass
export ROUTE_TABLE=200
/tinc-proxy/host-up
```

```bash
#!/bin/bash
# file: host-down
export VPN_GATEWAY=172.16.1.1
export SET_NAME=tinc_bypass
export ROUTE_TABLE=200
/tinc-proxy/host-down
```
