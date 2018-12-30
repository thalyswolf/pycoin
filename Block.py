import hashlib
import time

class Block:
    def __init__(self, index, previousHash, timestamp, data, hash):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

class Blockchain:
    def __init__(self, genesisBlock):
        self.__chain = []
        self.__chain.append(genesisBlock)

    def getLatestBlock(self):
        return self.__chain[len(self.__chain) - 1]

    def generateNextBlock(self, data):
        previousBlock = self.getLatestBlock()
        nextIndex = previousBlock.index + 1
        nextTimestamp = int(round(time.time() * 1000))
        nextPreviousHash = previousBlock.hash
        newBlock = Block(nextIndex, nextPreviousHash, nextTimestamp, data,
                        calculateHash(nextIndex, nextPreviousHash, nextTimestamp, data))
        if validateBlock(newBlock) == True:
            self.__chain.append(newBlock)

    def validateBlock(self, newBlock):
        previousBlock = self.getLatestBlock()
        if previousBlock.index + 1 != newBlock.index
            return False
        elif previousBlock.hash != newBlock.previousHash
            return False
        return True

def calculateHash(index, previousHash, timestamp, data):
    return hashlib.sha256(str(index) + previousHash + str(timestamp) + data).hexdigest()

ts = int(round(time.time() * 1000))
genesisBlock = Block(0, "", ts, 'Genesis block',
                    calculateHash(0, "", ts, 'Genesis block'))
