# https://dreamhack.io/wargame/challenges/1569

with open('encrypted', 'rb') as f:
    data = f.read()
    
unk_2004 = [0xDE, 0xAD, 0xBE, 0xEF]

i = 0

tmp = []
for d in data:
    d -= 19
    d %= 256
    d ^= unk_2004[i % 4]
    i += 1
    tmp.append(d)
    
with open('flag.png', 'wb') as f:
    f.write((bytes(tmp)))