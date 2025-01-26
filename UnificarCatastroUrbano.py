# Unificar capas urbanas del Catastro y guardados en un geopackage

import processing
import os, fnmatch
import geopandas as gpd

# Funcion rastrear ficheros en la carpeta de trabajo
def rastrea_ficheros (carpeta_trabajo, extension_fichero):
    for carpeta_trabajo, carpetas, ficheros in os.walk(carpeta_trabajo, extension_fichero):
        for fichero in fnmatch.filter(ficheros, extension_fichero):
            yield os.path.join (carpeta_trabajo, fichero)
            
# Definir la carpeta de trabjo y extension de fichero (.zip)
carpeta_trabajo = 'G:\\GIS\\layer\\vectorial\\oficial\\Catastro\\Catastro_2024mar_urbano\\'
extension_fichero = '*.zip'

# Crea la lista vacía
lista_todas_las_capas = []

# Detecta todas capas
for capas in rastrea_ficheros(carpeta_trabajo, extension_fichero):
    # Deducir la carpeta y nombre de fichero en la que se encuentran
    (carpeta_trabajo_carpeta, nombre_fichero_capas)= os.path.split (capas)
    # Crear lista con todos las capas
    lista_todas_las_capas.extend([capas])

    # Definir la terminación del nombre de las capas .zip
    localiza_capas_de_altipun = 'ALTIPUN'
    localiza_capas_de_carvia = 'CARVIA'
    localiza_capas_de_constru = 'CONSTRU'
    localiza_capas_de_ejes = 'EJES'
    localiza_capas_de_elemlin = 'ELEMLIN'
    localiza_capas_de_elempun = 'ELEMPUN'
    localiza_capas_de_elemtex = 'ELEMTEX'
    localiza_capas_de_hojas = 'HOJAS'
    localiza_capas_de_limites = 'LIMITES'
    localiza_capas_de_mapa = 'MAPA'
    localiza_capas_de_masa = 'MASA'
    localiza_capas_de_parcela = 'PARCELA'
    localiza_capas_de_subparce = 'SUBPARCE'

    # Crear sublista con capa tipo de capa
    sublista_altipun = [lista for lista in lista_todas_las_capas if localiza_capas_de_altipun in lista]
    sublista_carvia = [lista for lista in lista_todas_las_capas if localiza_capas_de_carvia in lista]
    sublista_constru = [lista for lista in lista_todas_las_capas if localiza_capas_de_constru in lista]
    sublista_ejes = [lista for lista in lista_todas_las_capas if localiza_capas_de_ejes in lista]
    sublista_elemlin = [lista for lista in lista_todas_las_capas if localiza_capas_de_elemlin in lista]
    sublista_elempun = [lista for lista in lista_todas_las_capas if localiza_capas_de_elempun in lista]
    sublista_elemtex = [lista for lista in lista_todas_las_capas if localiza_capas_de_elemtex in lista]
    sublista_hojas = [lista for lista in lista_todas_las_capas if localiza_capas_de_hojas in lista]
    sublista_limites = [lista for lista in lista_todas_las_capas if localiza_capas_de_limites in lista]
    sublista_mapa = [lista for lista in lista_todas_las_capas if localiza_capas_de_mapa in lista]
    sublista_masa = [lista for lista in lista_todas_las_capas if localiza_capas_de_masa in lista]
    sublista_parcela = [lista for lista in lista_todas_las_capas if localiza_capas_de_parcela in lista]
    sublista_subparce = [lista for lista in lista_todas_las_capas if localiza_capas_de_subparce in lista]

# Unir las todas las capas altipun
processing.run("native:mergevectorlayers", {'LAYERS':sublista_altipun,'CRS':QgsCoordinateReferenceSystem('EPSG:25830'),'OUTPUT':'ogr:dbname=\'G:/GIS/Catastro.gpkg\' table="uraltipun" (geom)'})
processing.run("native:mergevectorlayers", {'LAYERS':sublista_carvia,'CRS':QgsCoordinateReferenceSystem('EPSG:25830'),'OUTPUT':'ogr:dbname=\'G:/GIS/Catastro.gpkg\' table="urcarvia" (geom)'})
processing.run("native:mergevectorlayers", {'LAYERS':sublista_constru,'CRS':QgsCoordinateReferenceSystem('EPSG:25830'),'OUTPUT':'ogr:dbname=\'G:/GIS/Catastro.gpkg\' table="urconstru" (geom)'})
processing.run("native:mergevectorlayers", {'LAYERS':sublista_ejes,'CRS':QgsCoordinateReferenceSystem('EPSG:25830'),'OUTPUT':'ogr:dbname=\'G:/GIS/Catastro.gpkg\' table="urejes" (geom)'})
processing.run("native:mergevectorlayers", {'LAYERS':sublista_elemlin,'CRS':QgsCoordinateReferenceSystem('EPSG:25830'),'OUTPUT':'ogr:dbname=\'G:/GIS/Catastro.gpkg\' table="urelemlin" (geom)'})
processing.run("native:mergevectorlayers", {'LAYERS':sublista_elempun,'CRS':QgsCoordinateReferenceSystem('EPSG:25830'),'OUTPUT':'ogr:dbname=\'G:/GIS/Catastro.gpkg\' table="urelempun" (geom)'})
processing.run("native:mergevectorlayers", {'LAYERS':sublista_elemtex,'CRS':QgsCoordinateReferenceSystem('EPSG:25830'),'OUTPUT':'ogr:dbname=\'G:/GIS/Catastro.gpkg\' table="urelemtex" (geom)'})
processing.run("native:mergevectorlayers", {'LAYERS':sublista_hojas,'CRS':QgsCoordinateReferenceSystem('EPSG:25830'),'OUTPUT':'ogr:dbname=\'G:/GIS/Catastro.gpkg\' table="urhojas" (geom)'})
processing.run("native:mergevectorlayers", {'LAYERS':sublista_limites,'CRS':QgsCoordinateReferenceSystem('EPSG:25830'),'OUTPUT':'ogr:dbname=\'G:/GIS/Catastro.gpkg\' table="urlimites" (geom)'})
processing.run("native:mergevectorlayers", {'LAYERS':sublista_mapa,'CRS':QgsCoordinateReferenceSystem('EPSG:25830'),'OUTPUT':'ogr:dbname=\'G:/GIS/Catastro.gpkg\' table="urmapa" (geom)'})
processing.run("native:mergevectorlayers", {'LAYERS':sublista_masa,'CRS':QgsCoordinateReferenceSystem('EPSG:25830'),'OUTPUT':'ogr:dbname=\'G:/GIS/Catastro.gpkg\' table="urmasa" (geom)'})
processing.run("native:mergevectorlayers", {'LAYERS':sublista_parcela,'CRS':QgsCoordinateReferenceSystem('EPSG:25830'),'OUTPUT':'ogr:dbname=\'G:/GIS/Catastro.gpkg\' table="urparcela" (geom)'})
processing.run("native:mergevectorlayers", {'LAYERS':sublista_subparce,'CRS':QgsCoordinateReferenceSystem('EPSG:25830'),'OUTPUT':'ogr:dbname=\'G:/GIS/Catastro.gpkg\' table="ursubparce" (geom)'})