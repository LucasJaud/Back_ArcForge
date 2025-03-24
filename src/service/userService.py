from arcforge.core.db import DAO, QueryBuilder 
from src.models.user import User
import re

class DAOUser(DAO):
    _model = User

class UsuarioService:

    EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    PASSWORD_REGEX = r"^[a-zA-Z0-9]{5,}$"

    def __init__(self):
        self.dao = DAOUser()

    def login(self,user: User):
        if not re.match(self.EMAIL_REGEX, user.email):
            return None  # E-mail inválido
        
        if not re.match(self.PASSWORD_REGEX, user.password):
            return None

        auth = QueryBuilder(User).filter(email=user.email,password= user.password).execute()
        return auth if auth else None

    
    def cadastro(self,user: User):
        if not re.match(self.EMAIL_REGEX, user.email):
            return None  # E-mail inválido
        
        if not re.match(self.PASSWORD_REGEX, user.password):
            return None
        
        if user.name == "":
            return None
        
        newUser = self.dao.save(user)
        return newUser if newUser else None
    
    def get_user_by_id(self, id: int):
        # user = QueryBuilder(User).filter(id=id).execute()
        user = self.dao.read(id)
        return user if user else None