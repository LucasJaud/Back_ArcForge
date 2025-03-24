from arcforge.core.conn import *
from ..models.user import User
from ..service.userService import UsuarioService

class UserController(Controller):

    

    @Router.route("/login","POST")
    def login(request: Request):
        user_data = request.body

        user = User(**user_data)
        authUser = UsuarioService().login(user)
        
        if authUser:
            return JsonResponse(HttpStatus.OK,authUser)
        
        return JsonResponse(HttpStatus.BAD_REQUEST,{"erro":"Usuario não encontrado!!"})
    
    @Router.route("/signIn","POST")
    def cadastro(request: Request):
        user_data = request.body
        user = User(**user_data)

        newUser = UsuarioService().cadastro(user)
        print(newUser)

        return JsonResponse(HttpStatus.OK,newUser) if newUser else JsonResponse(HttpStatus.BAD_REQUEST,{"erro":"Usuario não encontrado!!"})






        
