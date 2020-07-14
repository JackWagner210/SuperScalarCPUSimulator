from helpers import Setup
import cache
import fetch
import writeBack
import alu
import issue
import memory

global_cycle = 0

class simClass:
    def __init__(self, instructions, opcode, opcodeStr, dataval, address, arg1, arg2, arg3, arg1Str, arg2Str, arg3Str,
                 numInstructions, destReg, src1Reg, src2Reg):
        self.instructions = instructions
        self.opcode = opcode
        self.opcodeStr = opcodeStr
        self.dataval = dataval
        self.address = address
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg1Str = arg1Str
        self.arg2Str = arg2Str
        self.arg3Str = arg3Str
        self.numInstructions = numInstructions
        self.destReg = destReg
        self.src1Reg = src1Reg
        self.src2Reg = src2Reg
        self.PC = 96
        self.cycle = 1
        ### LISTS ###
        self.cycleList = [0]
        self.R = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.postMemBuff = [-1, -1]  # first number is value, second is instr index
        self.postALUBuff = [-1, -1]
        self.preMemBuff = [-1, -1]
        self.preALUBuff = [-1, -1]
        self.preIssueBuff = [-1, -1, -1, -1]
        ### OBJECTS ###
        self.WB = writeBack.WriteBack(self.R, self.postMemBuff, self.postALUBuff, destReg)
        self.cache = cache.Cache(numInstructions, instructions, dataval, address)
        self.ALU = alu.ALU(self.R, self.postALUBuff, self.preALUBuff, opcodeStr, arg1, arg2, arg3)
        self.MEM = memory.Memory(self.R, self.postMemBuff, self.preMemBuff, opcodeStr, arg1, arg2, arg3, dataval,
                                 self.numInstructions, self.cache, self.cycleList)
        self.issue = issue.Issue(instructions, opcodeStr, dataval, address, arg1, arg2, arg3, self.numInstructions, destReg,
                                 src1Reg, src2Reg, self.R, self.preIssueBuff, self.preMemBuff, self.postMemBuff,
                                 self.preALUBuff, self.postALUBuff)
        self.fetch = fetch.Fetch(instructions, opcodeStr, dataval, address, arg1, arg2, arg3, self.numInstructions, destReg,
                                 src1Reg, src2Reg, self.R, self.preIssueBuff, self.preMemBuff, self.postMemBuff, self.preALUBuff,
                                 self.postALUBuff, self.PC, self.cache)
        self.outputFileName = Setup.get_output_filename()

    # TODO: Make sure all run functions work
    def run(self):
        go = True
        while go:  # Executing in reverse order, so cache stays up to date
            self.WB.run()
            self.ALU.run()
            self.MEM.run()
            self.issue.run()
            go = self.fetch.run()
            self.printState()
            self.cycle += 1

    # TODO:
    def printState(self):
        with open(self.outputFileName + "_sim.txt", 'a') as outFile:
            outFile.truncate(0)  # clear file before writing

            outFile.write("--------------------\n")
            outFile.write("Cycle:" + str(self.cycle) + "\n\n")

            outFile.write("Pre-Issue Buffer:\n")
            for i in range(len(self.preIssueBuff)):
                outFile.write("\tEntry:" + str(i) + "\t" + "\n")  # TODO: Need to see if insturction is pressent, then wrap in [] at index

            outFile.write("Pre_ALU Queue:\n")
            for i in range(len(self.preALUBuff)):
                outFile.write("\tEntry " + str(i) + ":\t" + "\n")

            outFile.write("Post_ALU Queue:\n")
            outFile.write("\tEntry 0:" + "\t" + "\n")
            outFile.write("Pre_MEM Queue:\n")

            for i in range(len(self.preMemBuff)):
                outFile.write("\tEntry " + str(i) + ":\t" + "\n")

            outFile.write("Post_MEM Queue:\n")
            outFile.write("\tEntry 0:" + "\t" + "\n")

            outFile.write("\nRegisters\n")
            outstr = "R00:\t"
            for i in range(8):
                outstr += str(self.R[i]) + "\t"
            outstr += "\nR08:\t"
            for i in range(8, 16):
                outstr += str(self.R[i]) + "\t"
            outstr += "\nR16:\t"
            for i in range(16, 24):
                outstr += str(self.R[i]) + "\t"
            outstr += "\nR24:\t"
            for i in range(24, 32):
                outstr += str(self.R[i]) + "\t"

            outFile.write(outstr + "\n")
            outstr = ""
            outFile.write("\nCache\n")

            for i in range(len(self.cache.cacheSets)):
                outstr += "Set " + str(i) + ": " + "LRU=" + str(self.cache.lruBit[i]) + "\n"
                for j in range(2):
                    outstr += "\tEntry " + str(j) + ":[("
                    for k in range(0, 2):
                        outstr += str(self.cache.cacheSets[i][j][k])
                    outstr += ")<"
                    for k in range (3, 5):
                        outstr += str(self.cache.cacheSets[i][j][k])
                    outstr += ">]\n"

            outFile.write(outstr)
            outstr = ""
            outFile.write("\nData\n")

            for i in range(len(self.dataval)):
                if i % 8 == 0 and i != 0 or i == len(self.dataval):
                    outFile.write(outstr + "\n")
                if i % 8 == 0:
                    outstr = str(self.address[i + self.numInstructs]) + ":\t" + str(self.dataval[i])
                if i % 8 != 0:
                    outstr = outstr + "\t" + str(self.dataval[i])

            outFile.write(outstr + "\n")
            outFile.close()

    def incrementPC(self):
        self.PC = self.PC + 4
