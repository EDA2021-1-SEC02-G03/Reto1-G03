from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.DataStructures import arraylist as array
from datetime import datetime, timedelta
import time
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog1():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y videos. Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'authors': None,
               'categorys': None}

    catalog['videos'] = lt.newList('ARRAY_LIST')
    catalog['categorys'] = lt.newList('ARRAY_LIST',
                                 cmpfunction=comparetagnames)

    return catalog
def newCatalog2():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y videos. Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'authors': None,
               'categorys': None}

    catalog['videos'] = lt.newList("SINGLE_LINKED")
    catalog['category'] = lt.newList("SINGLE_LINKED",
                                 cmpfunction=comparetagnames)

    return catalog


# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['videos'], video)
    # Se obtienen los autores del libro
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
def addVideoAuthor(catalog, authorname, video):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    authors = catalog['authors']
    posauthor = lt.isPresent(authors, authorname)
    if posauthor > 0:
        author = lt.getElement(authors, posauthor)
    else:
        author = newAuthor(authorname)
        lt.addLast(authors, author)
    lt.addLast(author['videos'], video)


def addCategory(catalog, category):
    """
    Adiciona un tag a la lista de tags
    """
    lt.addLast(catalog['categorys'], category)

# Funciones para creacion de datos
def newAuthor(name):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    author = {'name': "", "videos": None,  "visitas": 0}
    author['name'] = name
    author['videos'] = lt.newList('ARRAY_LIST')
    return author
def newCategory(name, id):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    tag = {'name': '', 'category_id': ''}
    tag['name'] = name
    tag['category_id'] = id
    return tag


# Funciones de consulta
def getVideosByAuthor(catalog, authorname):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    posauthor = lt.isPresent(catalog['authors'], authorname)
    if posauthor > 0:
        author = lt.getElement(catalog['authors'], posauthor)
        return author
    return None
def getBestVideos(catalog,num,opcionsort):
    """
    Retorna los mejores videos
    """
    sub_list=lt.subList(catalog['videos'], 1, num)
    sub_list=sub_list.copy()
    start_time = time.process_time()
    if opcionsort==4:
        nsblista=ms.mergesort(sub_list,cmpVideosByViews)
    elif opcionsort==5:
        nsblista=qs.quicksortf(sub_list,cmpVideosByViews)
    elif opcionsort==1:
        nsblista=sortselect(sub_list,cmpVideosByViews)
    elif opcionsort==2:
        nsblista=sortinsert(sub_list,cmpVideosByViews)
    elif opcionsort==3:
        nsblista=sortshell(sub_list,cmpVideosByViews)
    stop_time =time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg,nsblista

# Funciones utilizadas para comparar elementos dentro de una lista
def compareauthors(authorname1, author):
    if (authorname1.lower() in author['name'].lower()):
        return 0
    return -1
def compareratings(video1, video2):
    return (float(video1['views']) > float(video2['views']))
def comparetagnames(name, tag):
    return (name == tag['name'])
def cmpVideosByViews(video1, video2):
    visitas1=video1["views"]
    visitas2=video2["views"]
    if visitas1<visitas2:
        return False
    else:
        return True
def cmpVideosByTrendingdate(video1, video2):
    fecha1=video1["trending_date"]
    fecha2=video2["trending_date"]
    if fecha1<fecha2:
        return False
    else:
        return True
# Funciones de ordenamiento
def sortBooks(catalog):
    sa.sort(catalog['videos'], compareratings)
def sortinsert(lst, cmpfunction):
    size = lt.size(lst)
    pos1 = 1
    while pos1 <= size:
        pos2 = pos1
        while (pos2 > 1) and (cmpfunction(
               lt.getElement(lst, pos2), lt.getElement(lst, pos2-1))):
            lt.exchange(lst, pos2, pos2-1)
            pos2 -= 1
        pos1 += 1
    return lst
def sortselect(lst, cmpfunction):
    size = lt.size(lst)
    pos1 = 1
    while pos1 < size:
        minimum = pos1    # minimun tiene el menor elemento
        pos2 = pos1 + 1
        while (pos2 <= size):
            if (cmpfunction(lt.getElement(lst, pos2),
               (lt.getElement(lst, minimum)))):
                minimum = pos2  # minimum = posición elemento más pequeño
            pos2 += 1
        lt.exchange(lst, pos1, minimum)  # elemento más pequeño -> elem pos1
        pos1 += 1
    return lst
def sortshell(lst, cmpfunction):
    n = lt.size(lst)
    h = 1
    while h < n/3:   # primer gap. La lista se h-ordena con este tamaño
        h = 3*h + 1
    while (h >= 1):
        for i in range(h, n):
            j = i
            while (j >= h) and cmpfunction(
                                lt.getElement(lst, j+1),
                                lt.getElement(lst, j-h+1)):
                lt.exchange(lst, j+1, j-h+1)
                j -= h
        h //= 3    # h se decrementa en un tercio
    return lst
def getfirst(catalog):
    elemento=array.firstElement(catalog["videos"])
    return elemento
def listcategory(catalog,category):
    listacat= lt.newList('ARRAY_LIST')
    videos=catalog["videos"]
    for video in lt.iterator(videos):
        if video["category_id"]==category:
            lt.addLast(listacat, video)
    return listacat
def listpais1(catalog,pais):
    listacat= lt.newList('ARRAY_LIST')
    videos=catalog["videos"]
    for video in lt.iterator(videos):
        if video["country"] == pais:
            lt.addLast(listacat, video)
    return listacat
def listpais2(lista,pais):
    listacat= lt.newList('ARRAY_LIST')
    for video in lt.iterator(lista):
        if video["country"] == pais:
            lt.addLast(listacat, video)
    return listacat
def categoryid(catalog,category_name):
    categorys=catalog["categorys"]
    for category in lt.iterator(categorys):
        if category["name"] ==category_name:
            cid=category["id"]
            break
    return cid
def diastrending(lista):
    for i in range(1,lt.size(lista)):
        posvid1=i
        posvid2=i+1
        video1=lt.getElement(lista,posvid1)
        video2=lt.getElement(lista,posvid2)
        fechacad1=video1["trending_date"]
        fechacad2=video2["trending_date"]
        fecha1=time.strptime(fechacad1, '%y.%d.%m')
        fecha2 = time.strptime(fechacad2, '%y.%d.%m')
        fecha1=fecha1[0]+2000+ fecha1[1]+fecha1[2]
        fecha2=fecha2[0]+2000+fecha2[1]+fecha2[2]
        diastrend =fecha2-fecha1
        masdiastrend=0
        video=None
        if diastrend>=masdiastrend:
            video=video1
            masdiastrend=diastrend
    return video,masdiastrend
def topvideoscategoriapais(catalog,categoria,pais,tamaño):
    categoria_id=categoryid(catalog,categoria)
    listacategoria=listcategory(catalog,categoria_id)
    listapais=listpais2(listacategoria,pais)
    listaordenada=sortshell(listapais,cmpVideosByViews)
    sub_list=lt.subList(listaordenada, 1,tamaño)
    return sub_list
def toptrendingdatepais(catalog,pais):
    listapais=listpais1(catalog,pais)
    listaordenada=sortshell(listapais,cmpVideosByTrendingdate)
    video=diastrending(listaordenada)
    return video
def listatag(catalog,tag):
    listacat= lt.newList('ARRAY_LIST')
    videos=catalog["videos"]
    for video in lt.iterator(videos):
        if video["tags"] == tag:
            lt.addLast(listacat, video)
    return listacat