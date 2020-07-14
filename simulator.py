from helpers import Setup
import os
import masking_constants as MASKs
import sys


class State:
    dataval = []
    PC = 96
    cycle = 1
    R = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self, opcodes, opcodeStr, arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, dataval, address,
                 numInstructs):
        self.opcode = opcodes
        self.opcodeStr = opcodeStr
        self.arg1 = arg1
        self.arg1Str = arg1Str
        self.arg2 = arg2
        self.arg2Str = arg2Str
        self.arg3 = arg3
        self.arg3Str = arg3Str
        self.dataval = dataval
        self.address = address
        self.numInstructs = numInstructs

    # '''
    def getIndexofMemAddress(self, currentAddress):
        addressIndex = self.address.index(currentAddress)
        return addressIndex

    # '''
    '''
    def getIndexofMemAddress(self, currentAddress):
       index = 0
        for i in self.address:
            if i == currentAddress:
                return index
            index += 1
    #'''

    def incrementPC(self):
        self.PC = self.PC + 4

    def printState(self):
        outputFileName = Setup.get_output_filename()

        # print("raw output filename is", outputFileName)

        with open(outputFileName + "_sim.txt", 'a') as outFile:
            i = self.getIndexofMemAddress(self.PC)
            outFile.write("====================\n")
            outFile.write(
                "cycle:" + str(self.cycle) + "\t" + str(self.PC) + "\t" + self.opcodeStr[i] +
                self.arg1Str[i] + self.arg2Str[i] + self.arg3Str[i] + "\n")
            outFile.write("\n")
            outFile.write("registers:\n")
            outStr = "r00:"
            for i in range(0, 8):
                outStr = outStr + "\t" + str(self.R[i])
            outFile.write(outStr + "\n")
            outStr = "r08:"
            for i in range(8, 16):
                outStr = outStr + "\t" + str(self.R[i])
            outFile.write(outStr + "\n")
            outStr = "r16:"
            for i in range(16, 24):
                outStr = outStr + "\t" + str(self.R[i])
            outFile.write(outStr + "\n")
            outStr = "r24:"
            for i in range(24, 32):
                outStr = outStr + "\t" + str(self.R[i])
            outFile.write(outStr + "\n")
            outFile.write("\ndata:\n")
            for i in range(len(self.dataval)):
                if i % 8 == 0 and i != 0 or i == len(self.dataval):
                    outFile.write(outStr + "\n")
                if i % 8 == 0:
                    outStr = str(self.address[i + self.numInstructs]) + ":\t" + str(self.dataval[i])
                if i % 8 != 0:
                    outStr = outStr + "\t" + str(self.dataval[i])
            outFile.write(outStr + "\n")
            outFile.close()


class Simulator:

    def __init__(self, opcode, dataval, address, arg1, arg2, arg3, numInstructs,
                 opcodeStr, arg1Str, arg2Str, arg3Str):
        self.opcode = opcode
        self.opcodeStr = opcodeStr
        self.arg1 = arg1
        self.arg1Str = arg1Str
        self.arg2 = arg2
        self.arg2Str = arg2Str
        self.arg3 = arg3
        self.arg3Str = arg3Str
        self.dataval = dataval
        self.address = address
        self.numInstructs = numInstructs
        self.specialMask = MASKs.specialMask

    def run(self):
        foundBreak = False
        armState = State(self.opcode, self.opcodeStr, self.arg1, self.arg1Str, self.arg2, self.arg2Str,
                         self.arg3, self.arg3Str, self.dataval, self.address, self.numInstructs)
        sturPC = 0

        while not foundBreak:
            jumpAddr = armState.PC
            # get next instruction
            i = armState.getIndexofMemAddress(armState.PC)
            if self.opcode[i] == 0:  # NOP
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top
            elif self.opcode[i] >= 160 and self.opcode[i] <= 191:  # B
                jumpAddr = jumpAddr + ((self.arg1[i] * 4) - 4)  # -4 takes care of incrementing pc later
                armState.printState()
                armState.PC = jumpAddr
                armState.incrementPC()
                armState.cycle += 1
                continue
                # go back to top
            elif self.opcode[i] == 2038 and self.opcodeStr[i] == "BREAK":
                print("breaking")
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                foundBreak = True
            elif self.opcode[i] == 1112:  # ADD
                armState.R[self.arg3[i]] = armState.R[self.arg1[i]] + armState.R[self.arg2[i]]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue
            elif self.opcode[i] == 1624:  # SUB
                armState.R[self.arg3[i]] = armState.R[self.arg1[i]] - armState.R[self.arg2[i]]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue
            elif 1160 <= self.opcode[i] <= 1161:  # ADDI
                armState.R[self.arg3[i]] = armState.R[self.arg1[i]] + self.arg2[i]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue
            elif 1672 <= self.opcode[i] <= 1673:  # SUBI
                armState.R[self.arg3[i]] = armState.R[self.arg1[i]] - self.arg2[i]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue
            elif self.opcode[i] == 1104:  # AND
                armState.R[self.arg3[i]] = armState.R[self.arg1[i]] & armState.R[self.arg2[i]]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue
            elif self.opcode[i] == 1872:  # EOR
                armState.R[self.arg3[i]] = armState.R[self.arg1[i]] ^ armState.R[self.arg2[i]]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue
            elif self.opcode[i] == 1360:  # ORR
                armState.R[self.arg3[i]] = armState.R[self.arg1[i]] | armState.R[self.arg2[i]]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue
            elif 1684 <= self.opcode[i] <= 1687:  # MOVZ
                armState.R[self.arg2[i]] = armState.R[self.arg3[i]] << armState.R[self.arg1[i]]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue
            elif 1940 <= self.opcode[i] <= 1943:  # MOVK
                armState.R[self.arg2[i]] += armState.R[self.arg3[i]] << armState.R[self.arg1[i]]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue
            elif 1440 <= self.opcode[i] <= 1447:  # CBZ
                if armState.R[self.arg1[i]] == armState.R[self.arg3[i]]:
                    jumpAddr = jumpAddr + ((self.arg2[i] * 4) - 4)  # -4 takes care of incrementing pc later
                    armState.printState()
                    armState.PC = jumpAddr
                    armState.incrementPC()
                    armState.cycle += 1
                    continue
                else:
                    armState.printState()
                    armState.incrementPC()
                    armState.cycle += 1
                    continue
            elif 1448 <= self.opcode[i] <= 1455:  # CBNZ
                if armState.R[self.arg1[i]] != armState.R[self.arg3[i]]:
                    jumpAddr = jumpAddr + ((self.arg2[i] * 4) - 4)  # -4 takes care of incrementing pc later
                    armState.printState()
                    armState.PC = jumpAddr
                    armState.incrementPC()
                    armState.cycle += 1
                    continue
                else:
                    armState.printState()
                    armState.incrementPC()
                    armState.cycle += 1
                    continue
            elif self.opcode[i] == 1691:  # LSL
                armState.R[self.arg3[i]] = armState.R[self.arg1[i]] << self.arg2[i]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue
            elif self.opcode[i] == 1690:  # LSR RD, RN, SHAMT, RN<< SHAMT
                armState.R[self.arg3[i]] = (armState.R[self.arg2[i]] % (1 << 32) >> self.arg1[i])
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue
            elif self.opcode[i] == 1692:  # ASR
                armState.R[self.arg3[i]] = armState.R[self.arg1[i]] >> self.arg2[i]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue
            elif self.opcode[i] == 1984:  # STUR
                # STUR arg1 [arg2, arg3] && STUR Rd
                # STUR	R2, [R4, #1]
                # put value of R2  in value (SOMEHOW FIGURED OUT BY ARG2, ARG3. IDK HOW. 152 FROM 160 AND #1???)
                #   Supposed to be: Value pointed to by R4 plus 1 byte
                # Add the offset in address register to Rn to get target address.
                # Either load value in Rt into address or get value at address and put into Rt
                '''
                    if address[-1] <= target address
                        not so good, need to make lastz element <= target
                        armState.dataval.append(0)
                        self.address.append(self.address[-1] + 4).
                        check again. If still not <= target, repeat.
                    else
                        good to store/load
                '''
                target = (armState.R[self.arg2[i]] + (4 * self.arg3[i]) + 100 - (armState.PC+4))  # need to calculate this to fix it. r4, #1 -> under r3
                sturPC = armState.PC
                while self.address[-1] <= target:
                    armState.dataval.append(0)
                    self.address.append(self.address[-1] + 4)

                # armState.dataval.append(0)
                armState.dataval.append(armState.R[self.arg1[i]])

                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue
            elif self.opcode[i] == 1986:   # LDUR
                # LDUR arg1 [arg2, arg3]
                # LDUR	R1, [R4, #1] # = in R1, store value from dataval denoted by [R4, #1]
                # print(armState.R[self.arg2[i]]) # value
                # print(self.arg2[i]) # index
                argValue = int((armState.PC - sturPC)/4)
                indexValue = (self.arg2[argValue-1] + (4 * self.arg3[i]) + 100 - (sturPC+4))
                target = armState.getIndexofMemAddress(indexValue)  # index of value pointed to
                # by [R4, #1] (dataval[10] <==> data 152 <==> int 11

                armState.R[self.arg1[i]] = armState.dataval[target-3]

                # armState.R[self.arg1[i]] = armState.R[self.arg2[i] + self.arg3[i]]

                # TODO: LDUR
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue
            else:
                print("IN SIM---- UNKNOWN INSTRUCTION -----------------!!!!")
                armState.printState()
                armState.PC = jumpAddr
                armState.incrementPC()
                armState.cycle += 1