f = open('BIKEMI_for_btl.hex', 'r')
OpenedFile = f.read()
f.close()
OpenedFileLen = len(OpenedFile)
print(OpenedFileLen)
cmd=0
adr=0
data=0
buf = []
for e in range(0,OpenedFileLen):
    if OpenedFile[e] == ':':
        cmd = bytes(OpenedFile[e+1:e+3], encoding = 'utf-8')
        if cmd == b'10':
            print("cmd = ", cmd)
            adr = bytes(OpenedFile[e+3:e+7], encoding = 'utf-8')
            print("adr = ", adr)
            data = bytes(OpenedFile[e+9:e+41], encoding = 'utf-8')
            print(data)
            
