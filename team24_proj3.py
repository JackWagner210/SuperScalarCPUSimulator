import dissasembler
# import simulator
import sim

mydis = dissasembler.Dissasembler()
output = {}
output = mydis.run()

mydis.print()
print(output)

mysim = sim.simClass(**output)
mysim.run()
