from helpers import Setup


class Memory:
    def __init__(self, R, postMemBuff, preMemBuff, opcodeStr, arg1, arg2, arg3, dataval, numInstructions, cache, cycleList):
        self.R = R
        self.postMemBuff = postMemBuff   # [value, instr index]
        self.preMemBuff = preMemBuff    # [instr index, instr index]
        self.opcodeStr = opcodeStr
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.dataval = dataval
        self.numInstructions = numInstructions
        self.cache = cache
        self.cycleList = cycleList

    def run(self):
        i = self.preMemBuff[0]  # i = 1st instruction Index, starts at i = -1

        if self.opcodeStr[i] == "LDUR":  # LDUR
            # TODO: CHECK CACHE FOR ADDRESS - correct?
            checkHitAndValue = self.cache.checkCache(self.preMemBuff[0], i,False,0)
            # Check for miss / hit
            if checkHitAndValue[0] is True:
                # TODO: perform operation - line directly below correct?
                self.postMemBuff = [checkHitAndValue[1], i]  # [data,instr index]

                i = self.preMemBuff[1]  # i = second instruction index, starts at i = -1
                self.preMemBuff = [i, -1]  # [2nd instruction index, -1]
            else:
                pass  # don't perform operation - leave in pre-Mem buffer until next cycle

        elif self.opcodeStr[i] == "STUR":  # STUR
            # TODO: CHECK CACHE FOR ADDRESS - correct?
            checkHitAndValue = self.cache.checkCache(self.preMemBuff[0], i, True, 0)
            # Cache full = wait until next cycle, still in pre-mem buffer
        else:
            pass