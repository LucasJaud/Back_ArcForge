from arcforge.core.conn import *
from ..models.user import User
from ..service.userService import UsuarioService

class UserController(Controller):

    response_headers = {
        "Access-Control-Allow-Origin": "*",  
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, Authorization"
    }

    

    @Router.route("/login","POST")
    def login(request: Request):
        user_data = request.body

        user = User(**user_data)
        authUser = UsuarioService().login(user)
        
        if authUser:
            return JsonResponse(headers=UserController.response_headers,status=HttpStatus.OK,data=authUser)
        
        return JsonResponse(headers=UserController.response_headers,status=HttpStatus.BAD_REQUEST,data={"erro":"Usuario não encontrado!!"})
    
    @Router.route("/signIn","POST")
    def cadastro(request: Request):
        user_data = request.body
        user = User(**user_data)

        newUser = UsuarioService().cadastro(user)
        print(newUser)

        return JsonResponse(headers=UserController.response_headers,status=HttpStatus.OK,data=newUser) if newUser else JsonResponse(headers=UserController.response_headers,status=HttpStatus.BAD_REQUEST,data={"erro":"Usuario não encontrado!!"})






        
