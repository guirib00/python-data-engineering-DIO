import random
import string

def generate_simple_password(length=8):
    """Gera uma senha simples com caracteres alfanuméricos."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def generate_complex_password(length=12):
    """Gera uma senha complexa com letras maiúsculas, minúsculas, números e caracteres especiais."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))
