import os
import shutil

def delete_files_containing_word(directory, word):
    """Elimina archivos que contienen una palabra específica en su contenido."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if word in content:
                        print(f"Eliminando archivo: {file_path}")
                        os.remove(file_path)
            except Exception as e:
                print(f"Error al procesar {file_path}: {e}")

def rename_files_remove_text(directory, text):
    """Elimina un texto específico de los nombres de todos los archivos en un directorio."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if text in file:
                old_path = os.path.join(root, file)
                new_name = file.replace(text, '')
                new_path = os.path.join(root, new_name)
                print(f"Renombrando: {old_path} -> {new_path}")
                try:
                    os.rename(old_path, new_path)
                except Exception as e:
                    print(f"Error al renombrar {old_path}: {e}")

def replace_text_in_files(directory, old_text, new_text):
    """Reemplaza texto en el contenido de todos los archivos de un directorio."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if old_text in content:
                    new_content = content.replace(old_text, new_text)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Reemplazado texto en: {file_path}")
            except Exception as e:
                print(f"Error al procesar {file_path}: {e}")

def main():
    print("Gestor de Archivos")
    print("1. Eliminar documentos que contengan cierta palabra")
    print("2. Borrar texto de los nombres de los documentos")
    print("3. Reemplazar texto en el contenido de los documentos")
    print("4. Salir")

    while True:
        try:
            option = int(input("\nElige una opción: "))
            if option == 1:
                directory = input("Ingresa la ruta del directorio: ")
                word = input("Ingresa la palabra a buscar: ")
                delete_files_containing_word(directory, word)
            elif option == 2:
                directory = input("Ingresa la ruta del directorio: ")
                text = input("Ingresa el texto a eliminar de los nombres: ")
                rename_files_remove_text(directory, text)
            elif option == 3:
                directory = input("Ingresa la ruta del directorio: ")
                old_text = input("Ingresa el texto a reemplazar: ")
                new_text = input("Ingresa el nuevo texto: ")
                replace_text_in_files(directory, old_text, new_text)
            elif option == 4:
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()
