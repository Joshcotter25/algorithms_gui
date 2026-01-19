import random



def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def egcd(a: int, b: int):
    
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def modinv(a: int, m: int) -> int:
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError("No modular inverse exists for these values.")
    return x % m

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def generate_prime(low: int, high: int) -> int:
    
    while True:
        candidate = random.randrange(low, high)
        if candidate % 2 == 0:
            candidate += 1
        if is_prime(candidate):
            return candidate



def generate_keypair(p: int | None = None, q: int | None = None, e: int = 65537,
                     prime_low: int = 200, prime_high: int = 600):
   
    if p is None:
        p = generate_prime(prime_low, prime_high)
    if q is None:
        q = generate_prime(prime_low, prime_high)
        while q == p:
            q = generate_prime(prime_low, prime_high)

    if not (is_prime(p) and is_prime(q)):
        raise ValueError("p and q must be prime.")

    n = p * q
    phi = (p - 1) * (q - 1)

    
    if e <= 1 or e >= phi or gcd(e, phi) != 1:
        e = 3
        while e < phi and gcd(e, phi) != 1:
            e += 2
        if e >= phi:
            raise ValueError("Could not find a valid public exponent e.")

    d = modinv(e, phi)
    return n, e, d, p, q

def text_to_int(message: str) -> int:
    data = message.encode("utf-8")
    return int.from_bytes(data, byteorder="big")

def int_to_text(x: int) -> str:
    if x == 0:
        return ""
    length = (x.bit_length() + 7) // 8
    return x.to_bytes(length, byteorder="big").decode("utf-8")

def encrypt_text(message: str, n: int, e: int) -> int:
    m = text_to_int(message)
    if m >= n:
        raise ValueError("Message is too large for this key (m >= n). Use larger primes or shorter message.")
    return pow(m, e, n)

def decrypt_to_text(ciphertext: int, n: int, d: int) -> str:
    m = pow(ciphertext, d, n)
    return int_to_text(m)