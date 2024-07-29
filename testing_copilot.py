print('hello')
def encode(text, shift=3):
    encoded = ''
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encoded += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encoded += char
    return encoded

def decode(encoded_text, shift=3):
    return encode(encoded_text, -shift)

# Example usage
original_text = "Nigga what the fuck are you doing"
encoded_text = encode(original_text)
decoded_text = decode(encoded_text)

print(f"Original: {original_text}")
print(f"Encoded: {encoded_text}")
print(f"Decoded: {decoded_text}")