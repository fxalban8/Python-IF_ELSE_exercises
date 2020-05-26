nativeVLAN = 1
dataVLAN = 100
#Running the program for the first time

print("FIRST RUN OF THE PROGRAM")
if nativeVLAN == dataVLAN:
 print("The native VLAN and the data VLAN are the same.")
else:
 print("The native VLAN and the data VLAN are different.")


print("SECOND RUN OF THE PROGRAM")
nativeVLAN = 1
dataVLAN = 1
if nativeVLAN == dataVLAN:
 print("The native VLAN and the data VLAN are the same.")
else:
 print("The native VLAN and the data VLAN are different.")
