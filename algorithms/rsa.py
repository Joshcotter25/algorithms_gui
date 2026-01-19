import random


def gcd(a: int, b: int) -> int:
    """Greatest common divisor (Euclid)."""
    while b:
        a, b = b, a % b
    return a


def egcd(a: int, b: int):
    """
    Extended Euclidean Algorithm.
    Returns (g, x, y) such that: a*x + b*y = g = gcd(a, b)
    """
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def modinv(a: int, m: int) -> int:
    """Modular inverse of a mod m (only exists if gcd(a, m) == 1)."""
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
    
    if low < 2:
        low = 2
    while True:
        candidate = random.randrange(low, high)
        if candidate % 2 == 0:
            candidate += 1
        if candidate >= high:
            continue
        if is_prime(candidate):
            return candidate




def generate_keypair(
    p: int | None = None,
    q: int | None = None,
    prime_low: int = 2000,
    prime_high: int = 8000
):
    if p is None:
        p = generate_prime(prime_low, prime_high)

    if q is None:
        q = generate_prime(prime_low, prime_high)
        while q == p:
            q = generate_prime(prime_low, prime_high)

    if not is_prime(p) or not is_prime(q):
        raise ValueError("p and q must be prime numbers.")

    n = p * q
    phi = (p - 1) * (q - 1)

    
    e = 65537
    if e >= phi or gcd(e, phi) != 1:
        e = 3
        while e < phi and gcd(e, phi) != 1:
            e += 2
        if e >= phi:
            raise ValueError("Could not find a valid public exponent e.")

    d = modinv(e, phi)
    return n, e, d, p, q




def encrypt_text(message: str, n: int, e: int) -> list[int]:
    
    cipher = []
    for ch in message:
        m = ord(ch)
        if m >= n:
            raise ValueError(
                "Key is too small for this character. Use larger primes."
            )
        cipher.append(pow(m, e, n))
    return cipher


def decrypt_to_text(ciphertext: list[int], n: int, d: int) -> str:
    
    chars = []
    for c in ciphertext:
        m = pow(int(c), d, n)
        chars.append(chr(m))
    return "".join(chars)




def parse_ciphertext(text: str) -> list[int]:
   
    cleaned = text.strip()
    if cleaned.startswith("[") and cleaned.endswith("]"):
        cleaned = cleaned[1:-1]

    if "," in cleaned:
        parts = [p.strip() for p in cleaned.split(",") if p.strip()]
    else:
        parts = [p.strip() for p in cleaned.split() if p.strip()]

    if not parts:
        return []

    return [int(p) for p in parts]