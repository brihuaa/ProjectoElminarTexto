import os
import shutil

def delete_files_containing_word(directory, word):
    """Elimina archivos que contienen una palabra específica en su contenido."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.txt', '.pdf', '.epub')):
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
            if text in file and file.endswith(('.txt', '.pdf', '.epub')):
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
            if file.endswith(('.txt', '.pdf', '.epub')):
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
    print("""
    ██████╗ ██████╗ ██╗███████╗██╗    ██╗ █████╗  ██████╗ █████╗ 
    ██╔══██╗██╔══██╗██║██╔════╝██║    ██║██╔══██╗██╔════╝██╔══██╗
    ██████╔╝██████╔╝██║█████╗  ██║ █╗ ██║███████║██║     ███████║
    ██╔═══╝ ██╔═══╝ ██║██╔══╝  ██║███╗██║██╔══██║██║     ██╔══██║
    ██║     ██║     ██║███████╗╚███╔███╔╝██║  ██║╚██████╗██║  ██║
    ╚═╝     ╚═╝     ╚═╝╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
    """)

    language = input("Choose your language / Elige tu idioma (en/es): ").strip().lower()

    if language == "en":
        menu = {
            "title": "File Management Tool",
            "options": [
                "1. Delete documents containing a specific word",
                "2. Remove text from document names",
                "3. Replace text in document content",
                "4. Exit"
            ],
            "prompts": {
                "directory": "Enter the directory path: ",
                "word": "Enter the word to search: ",
                "remove_text": "Enter the text to remove: ",
                "old_text": "Enter the text to replace: ",
                "new_text": "Enter the new text: ",
                "invalid_option": "Invalid option. Try again.",
                "exit": "Exiting the program."
            }
        }
    else:
        menu = {
            "title": "Gestor de Archivos",
            "options": [
                "1. Eliminar documentos que contengan cierta palabra",
                "2. Borrar texto de los nombres de los documentos",
                "3. Reemplazar texto en el contenido de los documentos",
                "4. Salir"
            ],
            "prompts": {
                "directory": "Ingresa la ruta del directorio: ",
                "word": "Ingresa la palabra a buscar: ",
                "remove_text": "Ingresa el texto a eliminar: ",
                "old_text": "Ingresa el texto a reemplazar: ",
                "new_text": "Ingresa el nuevo texto: ",
                "invalid_option": "Opción no válida. Intenta de nuevo.",
                "exit": "Saliendo del programa."
            }
        }

    print(menu["title"])
    for option in menu["options"]:
        print(option)

    while True:
        try:
            option = int(input("\n" + menu["prompts"]["directory"] + ": "))
            if option == 1:
                directory = input(menu["prompts"]["directory"])
                word = input(menu["prompts"]["word"])
                delete_files_containing_word(directory, word)
            elif option == 2:
                directory = input(menu["prompts"]["directory"])
                text = input(menu["prompts"]["remove_text"])
                rename_files_remove_text(directory, text)
            elif option == 3:
                directory = input(menu["prompts"]["directory"])
                old_text = input(menu["prompts"]["old_text"])
                new_text = input(menu["prompts"]["new_text"])
                replace_text_in_files(directory, old_text, new_text)
            elif option == 4:
                print(menu["prompts"]["exit"])
                break
            else:
                print(menu["prompts"]["invalid_option"])
        except ValueError:
            print(menu["prompts"]["invalid_option"])

if __name__ == "__main__":
    main()