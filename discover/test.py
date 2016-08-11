import random, hashlib, socket, struct, re
from bencode import bencode, bdecode

bootstrap_nodes = (
    'router.bittorrent.com:6881',
    'router.utorrent.com:6881',
    'dht.transmissionbt.com:6881',
)

nid = lambda: ''.join([chr(random.randint(0, 255)) for _ in range(20)])

class KRPC(object):

    def __init__(self, nid):
        self.nid = nid
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __del__(self):
        self._sock.close()

    def ping(self, host, port):
        msg = {'t': 'aa', 'y': 'q', 'q': 'ping', 'a': {'id': self.nid}}
        bencoded = bencode(msg)
        self._sock.sendto(bencoded, (host, int(port)))
        self._sock.settimeout(8)
        res, addr = self._sock.recvfrom(1500)
        return bdecode(res), addr

BITTORRENT = ('67.215.246.10', 8991)
UTORRENT = ('82.221.103.244', 6881)
TRANSMISSIONBT = ('dht.transmissionbt.com', 6881)

def get_srv_nid(addr):
    msg = {'t': 'aa', 'y': 'q', 'q': 'ping', 'a': {'id': nid()}}
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(8)
    try:
        s.sendto(bencode(msg), addr)
        buf, addr = s.recvfrom(68)
    except:
        print 'Error'
    s.close()
    res = bdecode(buf)
    return res['r']['id'], addr

MAGNET = 'magnet:?xt=urn:btih:0ABFE05B88107038EC5C127B8494F2B44D47DD2A&dn=BangBros.18.Marina.Angel.Lily.Love.Fucked.Hardcore.XXX.seXyXpiXels.mp4'

def get_peers(ih):
    _nid = 'abcdefghij0123456789'
    msg = {'t': 'ab', 'y': 'q', 'q': 'get_peers', 'a': {'id': _nid, 'info_hash': ih}}
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(8)
    try:
        s.sendto(bencode(msg), TRANSMISSIONBT)
        #s.sendto(bencode(msg), BITTORRENT)
        buf, addr = s.recvfrom(4096)
    except:
        s.close()
        raise
    s.close()
    res = bdecode(buf)
    return res, _nid

if __name__ == '__main__':
    #print get_srv_nid(BITTORRENT)
    ih_patt = re.compile(r'xt=urn:btih:([^&]+).*')
    m = ih_patt.search(MAGNET)
    ih = m.group(1)
    res, _nid = get_peers(ih)
    print res
    print len(res['r']['id'])

