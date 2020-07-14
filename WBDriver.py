import writeBack

R = [0, 1, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
postMemBuff = [-1, -1]  # first number is value, second is instr index
postALUBuff = [-1, -1]
destReg = [3, 4, 5, 6, 7, '']

WB = writeBack.WriteBack(R, postMemBuff, postALUBuff, destReg)

output = {}
output = WB.run()

if __name__ == '__main__':
    print(output)