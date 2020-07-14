from helpers import Setup
import os
import masking_constants as MASKs
import sys


class Dissasembler:
    opcodeStr = []
    instrSpaced = []
    arg1 = []
    arg2 = []
    arg3 = []
    arg1Str = []
    arg2Str = []
    arg3Str = []
    destReg = []
    src1Reg = []
    src2Reg = []
    dataval = []
    rawdata = []
    address = []
    numInstructs = 0

    def run(self):
        instructions = []
        instructions = Setup.import_data_file()

        outputFileName = Setup.get_output_filename()

        print("raw output filename is", outputFileName)

        # create an address list with appropriate length
        for i in range(len(instructions)):
            self.address.append(96 + (i * 4))

        opcode = []

        # create an opcode list by selecting left 11 bits
        for z in instructions:
            opcode.append(int(z, base=2) >> 21)

        # decode
        # TODO: add support for destReg, src1Reg, src2Reg
        # TODO:     if no reg needed for lists, make neg. start at -1, for debugging. sequential = good
        for i in range(len(opcode)):
            self.numInstructs = self.numInstructs + 1
            if opcode[i] == 1112:
                self.instrSpaced.append(Setup.bin2StringspacedR(instructions[i]))
                self.opcodeStr.append("ADD")
                self.arg1.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKs.rmMask) >> 16)
                self.arg3.append(int(instructions[i], base=2) & MASKs.rdMask)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif opcode[i] == 1624:
                self.instrSpaced.append(Setup.bin2StringspacedR(instructions[i]))
                self.opcodeStr.append("SUB")
                self.arg1.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKs.rmMask) >> 16)
                self.arg3.append(int(instructions[i], base=2) & MASKs.rdMask)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif opcode[i] == 1104:
                self.instrSpaced.append(Setup.bin2StringspacedR(instructions[i]))
                self.opcodeStr.append("AND")
                self.arg1.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKs.rmMask) >> 16)
                self.arg3.append(int(instructions[i], base=2) & MASKs.rdMask)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif opcode[i] == 1360:
                self.instrSpaced.append(Setup.bin2StringspacedR(instructions[i]))
                self.opcodeStr.append("ORR")
                self.arg1.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKs.rmMask) >> 16)
                self.arg3.append(int(instructions[i], base=2) & MASKs.rdMask)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif opcode[i] == 1690:
                self.instrSpaced.append(Setup.bin2StringspacedR(instructions[i]))
                self.opcodeStr.append("LSR")
                self.arg1.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKs.shmtMask) >> 10)
                self.arg3.append(int(instructions[i], base=2) & MASKs.rdMask)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", #" + str(self.arg2[i]))
                self.destReg.append(-23)
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif opcode[i] == 1691:
                self.instrSpaced.append(Setup.bin2StringspacedR(instructions[i]))
                self.opcodeStr.append("LSL")
                self.arg1.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKs.shmtMask) >> 10)
                self.arg3.append(int(instructions[i], base=2) & MASKs.rdMask)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", #" + str(self.arg2[i]))
                self.destReg.append(-22)
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif opcode[i] == 1692:
                self.instrSpaced.append(Setup.bin2StringspacedR(instructions[i]))
                self.opcodeStr.append("ASR")
                self.arg1.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKs.shmtMask) >> 10)
                self.arg3.append(int(instructions[i], base=2) & MASKs.rdMask)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", #" + str(self.arg2[i]))
                self.destReg.append(-21)
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif opcode[i] == 1872:
                self.instrSpaced.append(Setup.bin2StringspacedR(instructions[i]))
                self.opcodeStr.append("EOR")
                self.arg1.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKs.rmMask) >> 16)
                self.arg3.append(int(instructions[i], base=2) & MASKs.rdMask)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif 1160 <= opcode[i] <= 1161:
                self.instrSpaced.append(Setup.bin2StringSpacedI(instructions[i]))
                self.opcodeStr.append("ADDI")
                self.arg1.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg2.append(((int(instructions[i], base=2) & MASKs.imMask) >> 10))
                self.arg3.append(int(instructions[i], base=2) & MASKs.rdMask)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", #" + str(self.arg2[i]))
                self.destReg.append(-20)
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif 1672 <= opcode[i] <= 1673:
                self.instrSpaced.append(Setup.bin2StringSpacedI(instructions[i]))
                self.opcodeStr.append("SUBI")
                self.arg1.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg2.append(((int(instructions[i], base=2) & MASKs.imMask) >> 10))
                self.arg3.append((int(instructions[i], base=2) & MASKs.rdMask))
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", #" + str(self.arg2[i]))
                self.destReg.append(-19)
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif 160 <= opcode[i] <= 191:
                self.instrSpaced.append(Setup.bin2StringSpacedB(instructions[i]))
                self.opcodeStr.append("B")
                self.arg1.append(Setup.imm_32_bit_unsigned_to_32_bit_signed_converter(Setup.imm_bit_to_32_bit_converter
                                                                            ((int(instructions[i], base=2) & MASKs.bMask), 26)))
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("\t#" + str(self.arg1[i]))
                self.arg2Str.append("")
                self.arg3Str.append("")
                self.destReg.append(-18)
                self.src1Reg.append(-17)
                self.src2Reg.append(-16)
            elif 1440 <= opcode[i] <= 1447:
                self.instrSpaced.append(Setup.bin2StringSpacedCB(instructions[i]))
                self.opcodeStr.append("CBZ")
                self.arg1.append(int(instructions[i], base=2) & MASKs.rdMask)
                self.arg2.append(Setup.imm_32_bit_unsigned_to_32_bit_signed_converter(Setup.imm_bit_to_32_bit_converter((
                                (int(instructions[i], base=2) & MASKs.addr2Mask) >> 5), 19)))
                self.arg3.append(0)
                self.arg1Str.append("\tR" + str(self.arg1[i]))
                self.arg2Str.append(", #" + str(self.arg2[i]))
                self.arg3Str.append("")
                self.destReg.append("")
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(-15)
            elif 1448 <= opcode[i] <= 1455:
                self.instrSpaced.append(Setup.bin2StringSpacedCB(instructions[i]))
                self.opcodeStr.append("CBNZ")
                self.arg1.append(int(instructions[i], base=2) & MASKs.rdMask)
                self.arg2.append(
                    Setup.imm_32_bit_unsigned_to_32_bit_signed_converter(Setup.imm_bit_to_32_bit_converter((
                            (int(instructions[i], base=2) & MASKs.addr2Mask) >> 5), 19)))
                self.arg3.append(0)
                self.arg1Str.append("\tR" + str(self.arg1[i]))
                self.arg2Str.append(", #" + str(self.arg2[i]))
                self.arg3Str.append("")
                self.destReg.append("")
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(-15)
            elif 1684 <= opcode[i] <= 1687:
                self.instrSpaced.append(Setup.bin2StringSpacedIM(instructions[i]))
                self.opcodeStr.append("MOVZ")
                self.arg1.append(int(instructions[i], base=2) & MASKs.rdMask)
                self.arg2.append((int(instructions[i], base=2) & MASKs.imdataMask) >> 5)
                self.arg3.append(((int(instructions[i], base=2) & MASKs.imsftMask) >> 21) * 16)
                self.arg1Str.append("\tR" + str(self.arg1[i]))
                self.arg2Str.append(", " + str(self.arg2[i]))
                self.arg3Str.append(", LSL " + str(self.arg3[i]))
                self.destReg.append("")
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(-14)
            elif 1940 <= opcode[i] <= 1943:
                self.instrSpaced.append(Setup.bin2StringSpacedIM(instructions[i]))
                self.opcodeStr.append("MOVK")
                self.arg1.append(int(instructions[i], base=2) & MASKs.rdMask)
                self.arg2.append((int(instructions[i], base=2) & MASKs.imdataMask) >> 5)
                self.arg3.append(((int(instructions[i], base=2) & MASKs.imsftMask) >> 21) * 16)
                self.arg1Str.append("\tR" + str(self.arg1[i]))
                self.arg2Str.append(", " + str(self.arg2[i]))
                self.arg3Str.append(", LSL " + str(self.arg3[i]))
                self.destReg.append("")
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(-13)
            elif opcode[i] == 1984:
                self.instrSpaced.append(Setup.bin2StringSpacedD(instructions[i]))
                self.opcodeStr.append("STUR")
                self.arg1.append(int(instructions[i], base=2) & MASKs.rdMask)
                self.arg2.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & MASKs.addrMask) >> 12)
                self.arg1Str.append("\tR" + str(self.arg1[i]))
                self.arg2Str.append(", [R" + str(self.arg2[i]))
                self.arg3Str.append(", #" + str(self.arg3[i]) + "]")
                self.destReg.append("")  # TODO: Does this have a destination reg?
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif opcode[i] == 1986:
                self.instrSpaced.append(Setup.bin2StringSpacedD(instructions[i]))
                self.opcodeStr.append("LDUR")
                self.arg1.append(int(instructions[i], base=2) & MASKs.rdMask)
                self.arg2.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & MASKs.addrMask) >> 12)
                self.arg1Str.append("\tR" + str(self.arg1[i]))
                self.arg2Str.append(", [R" + str(self.arg2[i]))
                self.arg3Str.append(", #" + str(self.arg3[i]) + "]")
                self.destReg.append("")  # TODO: Does this have a destination reg?
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif opcode[i] == 0:
                self.instrSpaced.append(Setup.bin2StringSpaced(instructions[i]))
                self.opcodeStr.append("NOP")
                self.arg1.append(0)
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("")
                self.arg2Str.append("")
                self.arg3Str.append("")
                self.destReg.append("")
                self.src1Reg.append(-12)
                self.src2Reg.append(-11)
            elif opcode[i] == 2038 and (int(instructions[i], base=2) & MASKs.specialMask) == 2031591:
                self.instrSpaced.append(Setup.bin2StringSpaced(instructions[i]))
                self.opcodeStr.append("BREAK")
                self.arg1.append(0)
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("")
                self.arg2Str.append("")
                self.arg3Str.append("")
                self.destReg.append("")
                self.src1Reg.append(-10)
                self.src2Reg.append(-9)
                print("breaking")
                break
            else:
                self.opcodeStr.append("unknown")
                self.arg1.append(0)
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("")
                self.arg2Str.append("")
                self.arg3Str.append("")
                self.destReg.append("")
                self.src1Reg.append(-8)
                self.src2Reg.append(-7)
                print("i =: " + str(i))
                print("opcode =:  " + str(opcode[i]))
                sys.exit("you have found an unknown instruction, investigate NOW")

        data = []
        count = 0

        for z in instructions:
            if count < self.numInstructs:
                pass
            else:
                data.append(int(z, 2))
                self.rawdata.append(z)
            count += 1

        for i in range(len(self.rawdata)):
            if data[i] >> 31 != 1:
                self.dataval.append(data[i])
            else:
                self.dataval.append(Setup.imm_32_bit_unsigned_to_32_bit_signed_converter(data[i] - 1) * -1)
        return {
            "instructions": instructions,
            "opcode": opcode,
            "opcodeStr": self.opcodeStr,
            "arg1": self.arg1,
            "arg1Str": self.arg1Str,
            "arg2": self.arg2,
            "arg2Str": self.arg2Str,
            "arg3": self.arg3,
            "arg3Str": self.arg3Str,
            "dataval": data,
            "address": self.address,
            "numInstructions": self.numInstructs, #sim = change to numInstructions
            "destReg": self.destReg,
            "src1Reg": self.src1Reg,
            "src2Reg": self.src2Reg

        }

    def print(self):
        outFile = open(Setup.get_output_filename() + "_dis.txt", 'w')
        for i in range(self.numInstructs):
            outFile.write(str('%-36s' % self.instrSpaced[i]) + '\t' + str(self.address[i]) + '\t' +
                          str(self.opcodeStr[i]) + str(self.arg1Str[i]) +
                          str(self.arg2Str[i]) + str(self.arg3Str[i]) + '\n')
        for i in range(len(self.dataval)):
            outFile.write(str(self.rawdata[i]) + '\t' + str(self.address[i + self.numInstructs]) + '\t' + str(
                self.dataval[i]) + '\n')

        outFile.close()
