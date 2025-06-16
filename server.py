import logging
import threading
from typing import Tuple, Any

debugging = False

# Use this function for debugging
def debug(format, *args):
    if debugging:
        logging.info(format % args)

# Put or Append
class PutAppendArgs:
    # Add definitions here if needed
    def __init__(self, key, value):
        self.key = key
        self.value = value

class PutAppendReply:
    # Add definitions here if needed
    def __init__(self, value):
        self.value = value

class GetArgs:
    # Add definitions here if needed
    def __init__(self, key):
        self.key = key

class GetReply:
    # Add definitions here if needed
    def __init__(self, value):
        self.value = value

class KVServer:
    def __init__(self, cfg):
        self.mu = threading.Lock()
        self.cfg = cfg
        self.kv_store = {} # KV store
        
        # Your definitions here.

    def Get(self, args: GetArgs):
        # reply = GetReply(None)

        # Your code here.
        with self.mu:
            value = self.kv_store.get(args.key, "")
            return GetReply(value)

        # return reply

    def Put(self, args: PutAppendArgs):
        # reply = PutAppendReply(None)

        # Your code here.
        with self.mu:
            self.kv_store[args.key] = args.value
            return PutAppendReply("")

        # return reply

    def Append(self, args: PutAppendArgs):
        # reply = PutAppendReply(None)

        # Your code here.
        with self.mu:
            old_value = self.kv_store.get(args.key, "")
            self.kv_store[args.key] = old_value + args.value
            return PutAppendReply(old_value)

        # return reply
