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
            response_data = authUser
            print(f"Enviando resposta: {response_data}")
            return JsonResponse(headers=UserController.response_headers,status=HttpStatus.OK,data=authUser)
        
        return JsonResponse(headers=UserController.response_headers,status=HttpStatus.BAD_REQUEST,data={"erro":"Usuario não encontrado!!"})
    
    @Router.route("/signIn","POST")
    def cadastro(request: Request):
        user_data = request.body
        if 'id' in user_data and (user_data['id'] == 0 or user_data['id'] is None):
            del user_data['id']
        user = User(**user_data)

        newUser = UsuarioService().cadastro(user)
        print(f"Novo usuário cadastrado: {newUser}")
        
        return JsonResponse(headers=UserController.response_headers,status=HttpStatus.OK,data=newUser) if newUser else JsonResponse(headers=UserController.response_headers,status=HttpStatus.BAD_REQUEST,data={"erro":"Usuario não encontrado!!"})


    @Router.route("/user/{id}", "GET")
    def get_user_by_id(request: Request, id: int):
        id_user = int(id)
        user = UsuarioService().get_user_by_id(id_user)
        
        if user:
            return JsonResponse(
                headers=UserController.response_headers,
                status=HttpStatus.OK,
                data=user
            )
        
        return JsonResponse(
            headers=UserController.response_headers,
            status=HttpStatus.NOT_FOUND,
            data={"erro": "Usuário não encontrado!"}
        )



        
