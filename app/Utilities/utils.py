from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_pwd(plaintext: str):
    return pwd_context.hash(plaintext)

def verify_pwd(plaintext: str, hashtext: str) -> bool:
    return pwd_context.verify(plaintext, hashtext)
