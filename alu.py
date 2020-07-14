class ALU:
    # TODO: Add LSL,LSR,ASR,MOVK,MOVZ

    def __init__(self, R, postALUBuff, preALUBuff, opcodeStr, arg1, arg2, arg3):
        self.R = R
        self.postALUBuff = postALUBuff  # [value, instr index]
        self.preALUBuff = preALUBuff  # [instr index, instr index]
        self.opcodeStr = opcodeStr
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def run(self):

        i = self.preALUBuff[0]  # i = 1st instruction Index, starts at i = -1

        if i != -1:  # Right? needs to be valid and not -1
            if self.opcodeStr[i] == "ADD":     # ADD
                self.postALUBuff = [self.R[self.arg1[i]] + self.R[self.arg2[i]], i]   # [result,instruction index]
            elif self.opcodeStr[i] == "SUB":   # SUB
                self.postALUBuff = [self.R[self.arg1[i]] - self.R[self.arg2[i]], i]
            elif self.opcodeStr[i] == "ADDI":  # ADDI
                self.postALUBuff = [self.R[self.arg1[i]] + self.arg2[i], i]
            elif self.opcodeStr[i] == "SUBI":  # SUBI
                self.postALUBuff = [self.R[self.arg1[i]] - self.arg2[i], i]
            elif self.opcodeStr[i] == "AND":  # AND
                self.postALUBuff = [self.R[self.arg1[i]] & self.R[self.arg2[i]], i]
            elif self.opcodeStr[i] == "ORR":  # ORR
                self.postALUBuff = [self.R[self.arg1[i]] | self.R[self.arg2[i]], i]
            elif self.opcodeStr[i] == "EOR":  # EOR
                self.postALUBuff = [self.R[self.arg1[i]] ^ self.R[self.arg2[i]], i]

        i = self.preALUBuff[1]    # i = second instruction index, starts at i = -1
        self.preALUBuff = [i, -1]  # [2nd instruction index, -1]

        #  return self.postALUBuff, self.preALUBuff    # Output = POSTALUBUFF

    # TODO input values from appropriate functions/files
# [first Index, Second Index]
# [ Second Index, -1]
#

