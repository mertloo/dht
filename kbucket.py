from bitarray import bitarray
from binascii import hexlify, unhexlify
import random, hashlib

def hash_str():
  s = ""
  for i in range(20):
    s += chr(random.randint(0, 255))
  m = hashlib.sha1()
  m.update(s)
  return hexlify(m.digest())

def hash_to_bitarray(hash_str):
    bit_arr = bitarray(endian='little') 
    bit_arr.frombytes(unhexlify(hash_str))
    return bit_arr

class kbucket(object):

    def __init__(self, hash_str, ip, port):
        self.bit_arr = hash_to_bitarray(hash_str)
        self.ip = ip
        self.port = port
        self.attaches = dict()

    def attach_bucket(self, hash_str, ip, port):
        n_bit = self.nth_bit(hash_str)
        self.attaches[n_bit] = self.attaches.get(n_bit) if self.attaches.get(n_bit) else list()
        bucket = kbucket(hash_str, ip, port)
        self.attaches[n_bit].append(bucket)

    def nth_bit(self, hash_str):
        # FIXME: by xor compution
        bit_arr = hash_to_bitarray(hash_str)
        i = 0
        while i < len(bit_arr):
            if bit_arr[i] == self.bit_arr[i]:
                i += 1
            else:
                return i - 1

if __name__ == '__main__':
    print len(hash_str())
