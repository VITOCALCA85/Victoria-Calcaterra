#Abrir un archivo de texto, leer su contenido y mostrarlo.
def leer_archivo(nombre_archivo):
    archivo = None
    try:
        archivo = open(nombre_archivo, "r", encoding="utf-8")
        contenido = archivo.read()
        print("Contenido del archivo:\n")
        print(contenido)
#Excepciones para archivos que no existan. Usar finally, para cerrar correctamente el archivo.        
    except FileNotFoundError:
        print(f"Error: el archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print("Ocurrió un error inesperado:", e)
    finally:
        if archivo:
            archivo.close()
            print("\nEl archivo se ha cerrado correctamente.")
            
