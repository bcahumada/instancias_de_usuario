import json
import logging
from usuario import Usuario  

# Configuración del logging
logging.basicConfig(filename='error.log', level=logging.ERROR)

def crear_instancias_usuario(archivo_usuarios, archivo_error):
    lista_usuarios = []
    
    with open(archivo_usuarios, 'r') as file:
        for linea in file:
            try:
                # Parsear la línea en formato JSON
                datos_usuario = json.loads(linea.strip())
                
                # Crear instancia de Usuario con los datos extraídos del JSON
                usuario = Usuario(
                    nombre=datos_usuario.get('nombre'),
                    apellido=datos_usuario.get('apellido'),
                    email=datos_usuario.get('email'),
                    genero=datos_usuario.get('genero')
                )
                
                # Añadir a la lista de usuarios
                lista_usuarios.append(usuario)
                
            except (json.JSONDecodeError, TypeError) as e:
                # Manejar excepciones de JSON y creación de instancias
                logging.error(f'Error al procesar la línea: "{linea.strip()}" - Error: {e}')
    
    return lista_usuarios

# Ejecutar la función
if __name__ == "__main__":
    usuarios = crear_instancias_usuario('usuarios.txt', 'error.log')
    print(f'Se han creado {len(usuarios)} instancias de Usuario.')
