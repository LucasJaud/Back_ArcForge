from src.controller.ControllerUser import UserController
from arcforge.core.conn import *
import logging

if __name__ == "__main__":
    UserController()
    
    

    server = WebServer(port=8080)
    try:
        server.start()  # O servidor ficará ativo até ser interrompido
    except KeyboardInterrupt:
        logging.info("Servidor interrompido via KeyboardInterrupt")
    finally:
        logging.info("Servidor encerrado.")
            



