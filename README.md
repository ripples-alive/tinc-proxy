## Usage

You can run multiple tinc instance or multiple nodes with one instance as fallback for the strategy proxy.

Remember to append your VPN server ip to `BYPASS` in `tinc-env`.

```bash
#!/bin/bash
# file: tinc-up
export VPN_IP=172.16.1.2
export SET_NAME=tinc_bypass
/tinc-proxy/tinc-up
```

```bash
#!/bin/bash
# file: tinc-down
export VPN_IP=172.16.1.2
export SET_NAME=tinc_bypass
/tinc-proxy/tinc-down
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
