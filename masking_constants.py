bMask = 0x3FFFFFF
jAddrMask = 0xFC000000
specialMask = 0x1FFFFF
rnMask = 0x3E0  # 1st arg ARM Rn
rmMask = 0x1F0000  # second argument ARM Rm
rdMask = 0x1F  # destination ARM Rd
imMask = 0x3FFC00  # ARM I immediate
shmtMask = 0xFC00  # ARM ShAMT
addrMask = 0x1FF000  # ARM Address for ld and st
addr2Mask = 0xFFFFE0  # addr for CB
imsftMask = 0x600000  # shift for IM
imdataMask = 0x1FFFE0  # data for IM type
