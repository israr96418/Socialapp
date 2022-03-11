from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hasing_password(password):
    return pwd_context.hash(password)

def password_verificaion(plan_passwrd, hash_passwrd):
    passwrd_matching = pwd_context.verify(plan_passwrd,hash_passwrd)
    return passwrd_matching