# ZooKeeper Znode Recursive Search Script

This Python script uses the Kazoo library to recursively search through all the znodes in a ZooKeeper cluster and store the data of each znode in a dictionary with the path of the znode as the key.
Prerequisites

## Before running the script, make sure you have the following prerequisites:

    Python 3.x
    Kazoo library (you can install it using pip install kazoo)
    Access to a ZooKeeper cluster

## Usage

1. Clone the repository or download the Python script.
2. Modify the script to specify the IP address and port of your ZooKeeper cluster.
3. Run the script using the following command: python znode_search.py.
4. The script will recursively search through all the znodes in the ZooKeeper cluster and store the data of each znode in a dictionary with the path of the znode as the key.
5. The dictionary will be printed to the console once the search is complete.

## License

This script is licensed under the MIT License. Feel free to modify and use it as needed.
