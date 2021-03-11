"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """


import sys
import controller
from DISClib.ADT import list as lt


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
iniciando=True
def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2-Crear sublista y ordenarla")
    print("3-Top x videos con mas views de un pais")
    print("4-Dias mas trending ")
    print("5-Buscar por tag")
    print("0- Salir")


def initCatalog1():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog1()
def initCatalog2():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog2()
def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)
def printVideo(video):
    print(video['title'], video["channel_title"],str(video["trending_date"]), str(video['views']),str(video["likes"]),str(video["dislikes"]))
def printBestVideos(videos):
    size = lt.size(videos)
    if size:
        print(' Estos son los mejores libros: ')
        for video in lt.iterator(videos):
            print('Titulo: ' + video['title'] +  "Visitas: " + video['views'])
    else:
        print('No se encontraron libros')
catalog=None
def printCategorys(catalog):
    categorias=catalog["categorys"]
    size = lt.size(categorias)
    if size:
        for category in lt.iterator(categorias):
            print(category['id'], category['name'])
    else:
        print('No se encontraron categorias')
def printtag(video):
    print(video['title'], video["channel_title"],str(video["publish_time"]), str(video['views']),str(video["likes"]),str(video["dislikes"]),str(video["tags"]))
"""
Menu principal
"""
while iniciando== True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        opcion= int (input("Seleccione la estructura que va a tener su lista:\n 1.Array_List o 2 u otro numero 1.Linked_List:\n"))
        if opcion==1:
           catalog = initCatalog1()
        else:
            catalog= initCatalog2()
        print("Cargando información de los archivos ....")   
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        primervideo=controller.getfirst(catalog)
        printVideo(primervideo)
        printCategorys(catalog)
        True
    if int(inputs[0]) == 2:

            num=int(input("Porfavor ingrese el tamaño de la sublista:\n"))
            print("Ingrese la opcion con la que se desea organizar la lista")
            opcion_sort=int(input("1.Selection 2.Insertion 3.Shell 4.Merge 5.Quick\n"))
            if 6>opcion_sort>0:
               result=controller.getBestVideos(catalog,num,opcion_sort)
               print("Para la muestra de", num, " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))
               print(result[1])
            else:print("Ingrese una opcion valida")
    if int(inputs[0])==3:
        tamaño=int(input("Porfavor ingrese el numero de videos x del top: "))
        pais=str(input("Ingrese el pais: "))
        nombrecategoria=(input("Ingrese la categoria de los videos: "))
        lista=controller.topvideospais(catalog,nombrecategoria,pais,tamaño)
        for video in lt.iterator(lista):
            printVideo(video)
    if int(inputs[0])==0:


        iniciando=False
    if int(inputs[0])==4:
       pais=input("Ingrese el pais: ")
       result=controller.listapais(catalog,pais)
       printVideo(result[0])
       print(result[1])
    if int(inputs[0])==5:
        tag=input("Ingrese el tag: ")
        lista=controller.listatag(catalog,tag)
        for video in lt.iterator(lista):
            printtag(video)

        
