inputs = [ 1, 2, 3]

def convert_to_byte_string(inputs):
    lst = str(inputs).strip('[').strip(']')
    lst = [ l for l in lst if l != " " ]
    lst = [ ord(char) for char in lst ]
    return lst

print(convert_to_byte_string(inputs))

