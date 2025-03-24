from src.controller import ControllerUser
from arcforge.core.conn import *
import logging

if __name__ == "__main__":
    ControllerUser()

    server = WebServer(port=8080)
    try:
        server.start()  # O servidor ficará ativo até ser interrompido
    except KeyboardInterrupt:
        logging.info("Servidor interrompido via KeyboardInterrupt")
    finally:
        logging.info("Servidor encerrado.")
            



