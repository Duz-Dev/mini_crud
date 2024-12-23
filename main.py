import interface as gui

menu_txt = """
-----------------------------------------------------
|                 BIBLIOTECA ANIME                  |
-----------------------------------------------------
| OPCIONES |                FUNCIONES               |
-----------------------------------------------------
|   1      | [Ver] lista actual de animes           |
|   2      | [AÑADIR] anime a la biblioteca         |
|   3      | [MODIFICAR] anime de la biblioteca     |
|   4      | [BUSCAR] anime de la biblioteca        |
|   5      | [ELIMINAR] anime de la biblioteca      |
|   6      | [SALIR] Salir del programa             |
-----------------------------------------------------

"""



def Menu():
    while True:
        print(menu_txt)
        print("¿Qué opción desea ingresar?: ")
        op = gui.Opciones(1,6)
        gui.cls_line(50)
        match op:
            case 1:
                gui.cls_line(50)
                gui.sleep(.5)
                if not gui.ver_anime():
                    print("Aviso. La biblioteca esta vacia. Deseas añadir un nuevo anime a la coleccion?[S/N]")
                    if input(">> ").upper().strip() == "S":
                        gui.cls_line(50)
                        gui.añadir_anime()
                        print("Aviso. Registro añadido con exito")
                        gui.sleep(1.1)
                        gui.cls_line(50)
                else:
                    while True:
                        print("¿Desea volver al menú principal?[S]")
                        if input(">> ").upper().strip() == "S":
                            gui.cls_line(50)
                            break
                        
                
            case 2:
                gui.sleep(.5)
                gui.cls_line(50)
                gui.añadir_anime()
                print("Aviso. Registro añadido con éxito")
                gui.sleep(1.5)
                gui.cls_line(50)
            case 3:
                if gui.modificar_anime():
                    print("Aviso. Registro añadido con éxito")
                    gui.sleep(1.2)
                else:
                    gui.sleep(2)
                gui.cls_line(50)
            case 4:
                gui.buscar_anime()
                gui.sleep(1.5)
                gui.cls_line(50)
            case 5:
                gui.eliminar_anime()
            case 6:
                print("cerrando crud.",end="")            
                for i in range(10):
                    print(f".", end="",flush=True)
                    gui.sleep(0.1)
                gui.cls_line(50)
                exit()
            case _:
                break
    return

Menu()