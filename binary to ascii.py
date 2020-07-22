Byte = input()
binary_int = int(Byte, 2)
byte_number = binary_int.bit_length() + 7 // 8
binary_array = binary_int.to_bytes(byte_number, byteorder="big")
arr = str(binary_array)[1:]
print(arr.replace('\\x00', ''))
