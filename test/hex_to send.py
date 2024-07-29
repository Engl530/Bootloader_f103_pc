import struct
f = open('BIKEMI_for_btl.hex', 'r')
OpenedFile = f.read(60)
f.close()
OpenedFileLen = len(OpenedFile)
print('len =', OpenedFileLen)
cmd=0
for e in range(0,OpenedFileLen):
    if OpenedFile[e] == ':':
        cmd = bytes(OpenedFile[e+1:e+3], encoding = 'utf-8')
        if cmd == b'10':
            #print("cmd = ", cmd)
            adr=[]
            adr.append((OpenedFile[e+3:e+5]))
            adr.append((OpenedFile[e+5:e+7]))
            data=[]
            for b in range(0,16):
                data.append((OpenedFile[e+9+2*b:e+11+2*b]))
            buf = []
            buf = adr +data
            crc = 0
            for c in range(0, len(buf)):
                crc= int(buf[c], 16)
                print(crc)
            print((buf))
            
            

data = [0x12, 0x54, 0x65, 0xab, 0x2f]
lenth = len(data)
#print(lenth)
ret_val=0
for k in range(0,lenth):
    ret_val = ret_val+ data[k]
    if ret_val >= 256:
        ret_val=ret_val-256    
#print(256-ret_val)   

