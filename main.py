def read_coords(filepath):
    file = open(filepath, 'r', encoding='utf-8')
    for star in file:
        starinfo = star.rstrip('\n').split(' ', maxsplit=6)
        x = starinfo[0]
        y = starinfo[1]
        henrydraper = starinfo[3]
        magnitude = starinfo[4]
        names = []
        if len(starinfo) > 6:  # En caso de que la estrella tenga nombre(s)
            names = starinfo[6].split("; ")
        starcoords[henrydraper] = (x, y)
        starlight[henrydraper] = magnitude
        for name in names:
            starnames[name] = henrydraper
    file.close()


def read_constellation(filepath, constellation_name):
    file = open(filepath, 'r', encoding='utf-8')
    constellations[constellation_name] = []
    for constellation in file:
        cons = constellation.rstrip('\n').split(',')  # Removemos el salto de línea
        constellations[constellation_name].append((cons[0], cons[1]))
    file.close()


def read_constellations():
    read_constellation('files/constellations/Boyero.txt', 'BOYERO')
    read_constellation('files/constellations/Casiopea.txt', 'CASIOPEA')
    read_constellation('files/constellations/Cazo.txt', 'CAZO')
    read_constellation('files/constellations/Cygnet.txt', 'CYGNET')
    read_constellation('files/constellations/Geminis.txt', 'GEMINIS')
    read_constellation('files/constellations/Hydra.txt', 'HYDRA')
    read_constellation('files/constellations/OsaMayor.txt', 'OSA MAYOR')
    read_constellation('files/constellations/OsaMenor.txt', 'OSA MENOR')


# Prueba
starcoords = dict()
starlight = dict()
starnames = dict()
read_coords('files/stars.txt')

constellations = dict()
read_constellations()
print(constellations['BOYERO'])
print('\n')
print(constellations['CASIOPEA'])
print('\n')
print(constellations['CAZO'])
print('\n')
print(constellations['CYGNET'])
print('\n')
print(constellations['GEMINIS'])
print('\n')
print(constellations['HYDRA'])
print('\n')
print(constellations['OSA MAYOR'])
print('\n')
print(constellations['OSA MENOR'])
