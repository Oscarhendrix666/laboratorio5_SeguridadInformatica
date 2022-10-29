import DiffieHellman as ds
import CryptoDes as CD
import Client as C
import Server as S
from ds import DH_Endpoint


def Main():

    c_public=23
    c_private=33
    Cliente = DH_Endpoint(c_public, s_public, c_private)

    s_public=83
    s_private=77
    Servidor = DH_Endpoint(c_public, s_public, s_private)

    c_partial=Cliente.generate_partial_key()
    s_partial=Servidor.generate_partial_key()

    c_full=Cliente.generate_full_key(c_partial)
    s_full=Servidor.generate_full_key(s_partial)
    
    if c_full==s_full:
        archivo = open("mensajeentrada.txt","r")
        mensaje = str(archivo.readline().lower())
        codigo =  ds.encriptacion(mensaje)
        archivo.close()

    file = open("mensajerecibido.txt","w")
    desco = ds.desencriptacion(codigo)
    file.write(str(desco))
    file.close()
