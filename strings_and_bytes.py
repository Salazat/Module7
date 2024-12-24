# print('hello') #ASCII
# print(ord('h')) # ord - Численное представление
# print(ord('e'))

# a = 'hello'
# chars = []
# for i in a:
#     chars.append(ord(i))
# s = ''
# for i in chars:
#     s += chr(i)
# print(s)

# for i in range(900, 1300):
#     print(chr(i))

print(hex(ord('h')))
bb = b'\x68'
print(bb.decode())