look_up = [

	0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,

	0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,

	0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,

	0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,

	0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,

	0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,

	0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,

	0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,

	0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,

	0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,

	0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,

	0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,

	0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,

	0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,

	0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,

	0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]

state = [
        1,2,3,4,
        5,6,7,8,
        9,1,2,3,
        4,5,6,7]


def subbyte(state):
    state2 = []
    for i in range(16):
        indice = state[i]
        ind = look_up[indice]
        state2.append(ind)
    return state2

def shiftrows(state):           
    temp=state[4]
    state[4]=state[5]
    state[5]=state[6]
    state[6]=state[7]
    state[7]=temp

    temp=state[8]
    temp1=state[9]
    state[8]=state[10]
    state[9]=state[11]
    state[10]=temp
    state[11]=temp1

    temp=state[12]
    temp2=state[13]
    temp3=state[14]
    state[12]=state[15]
    state[13]=temp
    state[14]=temp2
    state[15]=temp3 
    return state 

def multiplicationBy2(val):
    s = val << 1
    s &= 0xff
    if (val & 128) != 0:
        s = s ^ 0x1b
    return s

# Note: es2li haroun lmarra jeya aaleh hedhy mamchetech 
'''def multiplicationBy2(val):  
    s = val << 1
    if (val & 128) != 0:
        s = s ^ 0x11b
    return s '''

def multiplicationBy3(val):
    return multiplicationBy2(val) ^ val
     
def mixColWahed(col):
    c1 = multiplicationBy2(col[0]) ^ multiplicationBy3(col[1]) ^ col[2] ^ col[3] 
    c2 = col[0] ^ multiplicationBy2(col[1]) ^ multiplicationBy3(col[2]) ^ col[3] 
    c3 = col[0] ^ col[1] ^ multiplicationBy2(col[2]) ^ multiplicationBy3(col[3])
    c4 = multiplicationBy3(col[0]) ^ col[1] ^ col[2] ^ multiplicationBy2(col[3])
    col[0]=c1
    col[1]=c2
    col[2]=c3
    col[3]=c4
    return col
    
def mixCols(state):
    i=0
    col1=[]
    col2=[]
    col3=[]
    col4=[]

    for i in range (4):
        col1.append(state[i])
        col2.append(state[i+1])
        col3.append(state[i+2])
        col4.append(state[i+3])
        i+=3 

    col1=mixColWahed(col1)
    col2=mixColWahed(col2)
    col2=mixColWahed(col2)
    col3=mixColWahed(col3)

    state= col1 + col2 + col3 + col4
    return state

def rotword(val):
    temp=val[0]
    val[0]=val[1]
    val[1]=val[2]
    val[2]=val[3]
    val[3]=temp
    return val

def subbyte_word(val):
    for i in range(4):
        val[i]=look_up[val[i]]
    return val
rci=[1, 2, 4, 8, 10, 20, 40, 80, 27, 36]

def roundConst(val, i):
    i = int(i/10)
    if i == 1:
        rc = 1
    if (i>1):
        rc = rci[i-1]
    rc = rc >> 24
    rndcnst = [rc, 0, 0, 0]
    for i in range(4):
        val[i] = val[i] ^ rndcnst[i] 
    return val

def g(val,i):
    val = subbyte_word(rotword(val))
    i = i/4
    val = roundConst(val,i)
    return val
    
def key_expansion(key):
    i=0
    key_expanded=[]
    key_expanded.extend(key)
    for i in range(4,44):
        if (i%16==0):
            w=[]
            i=i*4
            w1=g(key_expanded[i-4:i],i) 
            w2=key_expanded[i-16:i-12]
            for j in range (4):
                w.append(w1[j] ^ w2[j])
            key_expanded.extend(w)
        else: 
            u=[]
            i = i*4
            w1=key_expanded[i-4:i] 
            w2=key_expanded[i-16:i-12]
            for k in range (4):
                u.append(w1[k] ^ w2[k])
            key_expanded.extend(u)
    return key_expanded

key = [
    234, 210, 73, 21,
    181, 141, 186, 210,
    31, 43, 245, 60,
    127, 141, 29, 47
]

def addRoundKey(state, key_expanded, round):
    round = round *16                    #rounds start at 0
    roundKey = key_expanded[round:round+16]
    for i in range(16):
        state[i]= state[i] ^ roundKey[i]
    return state


key_expanded=key_expansion(key)
stateRound_0 = addRoundKey(state, key_expanded, 0)   #round 0
print('ROUND : 0 \n' )
print('state after round 0: \n', state)

for i in range(1,10):                                 # rounds ml 1 lil 9
    print('ROUND ',i,': \n' )
    state=subbyte(state)
    print('state after subbyte: \n',state)
    state= shiftrows(state)
    print('state after shiftrows: \n',state)
    state= mixCols(state)
    print('state after mixing columns: \n',state)
    state= addRoundKey(state, key_expanded, 1)
    print('state after round' , i,' : \n', state)


print('LAST ROUND \n')                                    #round 10
state=subbyte(state)
print('state after subbyte: \n',state)
state= shiftrows(state)
print('state after shiftrows: \n',state)
state= addRoundKey(state, key_expanded, 10)
print('state after round 10: \n', state)
