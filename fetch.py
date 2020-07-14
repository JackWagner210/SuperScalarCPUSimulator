class Fetch:
    def __init__(self, instructions, opcodeStr, dataval, address, arg1, arg2, arg3, numInstructions, destReg, src1Reg, src2Reg,
                 R, preIssueBuff, preMemBuff, postMemBuff, preALUBuff, postALUBuff, PC, cache):
        self.instructions = instructions
        self.opcodeStr = opcodeStr
        self.dataval = dataval
        self.address = address
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.numInstructions = numInstructions
        self.destReg = destReg
        self.src1Reg = src1Reg
        self.src2Reg = src2Reg
        self.R = R
        self.preIssueBuff = preIssueBuff
        self.preMemBuff = preMemBuff
        self.postMemBuff = postMemBuff
        self.preALUBuff = preALUBuff
        self.postALUBuff = postALUBuff
        self.PC = PC
        self.cache = cache

    def run(self):
        toProccess = False




        return toProccess
