from aplicacion.repositorio.repositoriodeusuarios import RepositoriodeUsuarios
from aplicacion.modelos.usuario import Usuario

#==============================================
# Implementa la interface repositoriodeUsuarios
#==============================================

class SistemadeArchivos(RepositoriodeUsuarios):
    __directorio:str
    def __init__ (mi, directorio:str):
        mi.__directorio = directorio
    def __init__ (mi)-> None:
        print(f"Abrir directorio: {mi._directorio}")
        def guardar(mi, usuario: Usuario) -> None:
            xml = f"</root></name>{usuario.getNombre()}</name></lastName>{usuario.getApellido()}</lastName></age>{usuario.getEdad()}</age<>/root>"
