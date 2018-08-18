from sshtunnel import SSHTunnelForwarder
from time import sleep
import sys

import config as conf

server = SSHTunnelForwarder(
    (conf.REMOTE_SERVER_HOST, 22),
    ssh_username = conf.REMOTE_SERVER_USERNAME,
    ssh_pkey = conf.REMOTE_SERVER_PRIVATE_KEY,
    remote_bind_address=(conf.PRIVATE_SERVER_HOST, conf.PRIVATE_SERVER_PORT),
    local_bind_address=(conf.LOCAL_HOST, conf.LOCAL_PORT)
)

server.start()

print("SSH Tunnel running. Listening on port=" + str(server.local_bind_port))  # show assigned local port
# work with `SECRET SERVICE` through `server.local_bind_port`.

try:
    while True:
        # press Ctrl-C for stopping
        sleep(1)
except:
    print("Shutting down SSH tunnel")
    server.stop()
    sys.exit()
