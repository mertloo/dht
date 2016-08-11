'''KRPC protocal

A bencoded dictionary send over UDP. One packet sent, one packet reply.
3 types of message: 
    query, response, error

4 types of query: 
    ping, find_node, get_peers, announce_peer

The dictionary consists of 2 common key-value pairs: 
    't': 1 binary number transaction ID (16 bit)
    'y': 'q' or 'r' or 'e'

Contact Encoding
20-byte string of node ID, follow by 4-byte IP address, follow by 2-byte port
numbers. Network byte order.
'''
