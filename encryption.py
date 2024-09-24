def encrypt_text(text):
    """Encrypts the input string by shifting characters by +1 ASCII value."""
    return ''.join([chr(ord(char) + 1) for char in text])


def decrypt_text(text):
    """Decrypts the input string by shifting characters by -1 ASCII value."""
    return ''.join([chr(ord(char) - 1) for char in text])
