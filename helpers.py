import sys


class Setup:

    def __init__(self):
        pass

    @classmethod
    def get_input_filename(cls):
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-i' and i < (len(sys.argv) - 1):
                inputFileName = sys.argv[i + 1]
        return inputFileName

    @classmethod
    def get_output_filename(cls):
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-o' and i < (len(sys.argv) - 1):
                outputFileName = sys.argv[i + 1]
        return outputFileName

    @classmethod
    def import_data_file(cls):
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-i' and i < (len(sys.argv) - 1):
                inputFileName = sys.argv[i + 1]
        try:
            instructions = [line.rstrip() for line in open(inputFileName, 'r')]
        except IOError:
            print("Could not open input file")
        return instructions

    @classmethod
    def imm_bit_to_32_bit_converter(cls, num, bitsize):

        if bitsize == 12:  # I
            negBitMask = 0x800
            extendMask = 0xFFFFF000
        elif bitsize == 16:  # IM
            negBitMask = 0x8000
            extendMask = 0xFFFF0000
        elif bitsize == 19:  # CB
            negBitMask = 0x40000
            extendMask = 0xFFF80000
        elif bitsize == 26:  # B
            negBitMask = 0x2000000
            extendMask = 0xFC000000
        else:
            print("Invalid Bit length")

        if (negBitMask & num) > 0:
            num = num | extendMask
            num = num + 1
            num = num * -1
        return num

    @classmethod
    def bin2StringSpaced(cls, s):
        spacedStr = s[0:8] + " " + s[8:11] + " " + s[11:16] + " " + s[16:21] + " " + s[21:26] + " " + s[26:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedD(cls, s):
        spacedStr = s[0:11] + " " + s[11:20] + " " + s[20:22] + " " + s[22:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedIM(cls, s):
        spacedStr = s[0:9] + " " + s[9:11] + " " + s[11:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedCB(cls, s):
        spacedStr = s[0:8] + " " + s[8:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedI(cls, s):
        spacedStr = s[0:10] + " " + s[10:22] + " " + s[22:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringspacedR(cls, s):
        spacedStr = s[0:11] + " " + s[11:16] + " " + s[16:22] + " " + s[22:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedB(cls, s):
        spacedStr = s[0:6] + " " + s[6:32]
        return spacedStr

    @classmethod
    def imm_32_bit_unsigned_to_32_bit_signed_converter(cls, num):
        if (num >> 31) == 0:
            # if 0x7FFFFFF < num < 0x80000000:
            return num
        return num ^ 0xFFFFFFFF

    @classmethod
    def decimalToBinary(cls, num):
        if num > 1:
            cls.decimalToBinary(num // 2)
        print(num % 2, end='')

    @classmethod
    def binaryToDecimal(cls, binary):
        print("\n")
        print(int(binary, 2))

    @classmethod
    def getIndexOfMemAddress(cls, currAddr, isSW, dataval, address, numInstructs):
        tempIndex = 0
        try:
            if isSW:
                # make sure there is enough spaces in dataval
                # there has to be even num of elements in dataval

                #if the length of the address list is greater than num inst
                if len(address) > numInstructs:
                    lastInstructAddr = ((numInstructs - 1) * 4) + 96
                    lastMemAddr = lastInstructAddr + 4 * len(dataval)

                    if currAddr == lastMemAddr:
                        dataval.append(0)
                        dataval.append(0)
                        address.append(lastMemAddr + 4)
                        address.append(lastMemAddr + 8)
                        # add at least one more dataval address space
                    if currAddr > lastMemAddr:
                        addIndex = (currAddr - lastMemAddr) / 4
                        for i in range(int(addIndex)):
                            dataval.append(0)
                            address.append(lastMemAddr + (4 * (i + 1)))
                tempIndex = address.index(currAddr)  # slide says tmpIndex, or temp ??
                tempIndex = tempIndex - numInstructs
            else:
                tempIndex = address.index(currAddr)
                if tempIndex >= numInstructs:
                    tempIndex = tempIndex - numInstructs
            return tempIndex
        except ValueError:
            print("ERROR: Did not find mem address currAddr " + str(currAddr))
