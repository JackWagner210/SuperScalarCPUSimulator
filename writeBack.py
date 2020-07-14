import sim

class WriteBack:
    def __init__(self, R, postMemBuff, postALUBuff, destReg):
        self.R = R
        self.postMemBuff = postMemBuff  # index 0 is data, index 1 is instruction.
        self.postALUBuff = postALUBuff
        self.destReg = destReg  # TODO: important to make sure dissassembler works, as dest reg is determined there.
                                # TODO: this is a list, ex: [0, 0, 1, 6] is input. destReg[2] will indicate R1 is dest. [3] = R6

    def run(self):
        # sim.R[sim.DestReg[sim.PostALUBuff[1]]] = sim.postALUBuff[0]  # TODO: ex looks like this? Lists are mutable, passed back

        # If no issues, valid instruction to do, update and then reset.
        if self.postMemBuff[1] != -1:
            self.R[self.destReg[self.postMemBuff[1]]] = self.postMemBuff[0]
            self.postMemBuff[0] = -1  # Reset buff to empty, after executed.
            self.postMemBuff[1] = -1
        if self.postALUBuff[1] != -1:
            self.R[self.destReg[self.postALUBuff[1]]] = self.postALUBuff[0]
            self.postALUBuff[0] = -1
            self.postALUBuff[1] = -1
        # For the testing driver
        return {
            "R": self.R,
            "postMemBuff": self.postMemBuff,
            "postALUBuff": self.postALUBuff,
            "destReg": self.destReg
        }