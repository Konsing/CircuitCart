from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['sha256_crypt'], deprecated="auto")

def verify_password(plain_pass, hashed_pass) -> bool:
    return pwd_context.verify(plain_pass, hashed_pass)

def get_hashed_password(password: str) -> str:
    return pwd_context.hash(password)