from kazoo.client import KazooClient

# Connect to ZooKeeper
zk = KazooClient(hosts='172.20.0.2:2181')
zk.start()

# Recursive function to search through all znodes
def search_znodes(znode, znodes):
    # Get the data of the current znode
    data, stat = zk.get(znode)
    # Store the data in the dictionary with the path of the znode as the key
    znodes[znode] = data.decode()
    # Recursively search through all child znodes
    for child in zk.get_children(znode):
        search_znodes(znode + '/' + child, znodes)

# Call the recursive function to search through all znodes
znodes = {}
search_znodes('/', znodes)

# Print the dictionary of znodes and their data
print(znodes)
