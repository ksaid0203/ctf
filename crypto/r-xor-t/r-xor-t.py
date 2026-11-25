# https://dreamhack.io/wargame/challenges/901

result2 = "C@qpl==Bppl@<=pG<>@l>@Blsp<@l@AArqmGr=B@A>q@@B=GEsmC@ArBmAGlA=@q"

#result[k] = result2 [k] ^ 3

result = [ord(x) ^ 3 for x in result2]

rot = result[::-1]

inp = [ (x - 13) & 0x7F for x in rot ]

print("".join(chr(x) for x in inp))