from matplotlib import pyplot as plt
import PIL
import main


def read_coords(filepath):
    file = open(filepath, 'r', encoding='utf-8')
    for star in file:
        starinfo = star.rstrip('\n').split(' ', maxsplit=6)
        x = float(starinfo[0])
        y = float(starinfo[1])
        henrydraper = starinfo[3]
        magnitude = float(starinfo[4])
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
    read_constellation('files/constellations/Cygnet.txt', 'CYGNET')
    read_constellation('files/constellations/Geminis.txt', 'GEMINIS')
    read_constellation('files/constellations/Hydra.txt', 'HYDRA')
    read_constellation('files/constellations/OsaMayor.txt', 'OSA MAYOR')
    read_constellation('files/constellations/OsaMenor.txt', 'OSA MENOR')
    read_constellation('files/constellations/Cazo.txt', 'CAZO')


def plot_stars():
    x, y, s = [], [], []
    for star in starcoords:
        xi, yi = starcoords[star]
        x.append(xi)
        y.append(yi)
        s.append((5 / (starlight[star] + 2)) ** 2)

    fig = plt.figure(figsize=(12, 12))
    fig.patch.set_facecolor('#000000')

    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(x, y, s=s, marker='s', c='white')
    ax.patch.set_facecolor('#000000')
    ax.patch.set_alpha(0.5)
    return fig, ax


def plot_constellation(name, fig, ax, color):
    for union in constellations[name]:
        p1, p2 = union
        x1, y1 = starcoords[starnames[p1]]
        x2, y2 = starcoords[starnames[p2]]
        ax.plot([x1, x2], [y1, y2], c=color)
    return fig, ax


def plot_stars_and_constellations():
    fig, ax = plot_stars()
    colors = ['red', 'yellow', 'green', 'blue', 'cyan', 'magenta', 'white', '#FF5733']
    i = 0
    for constellation_name in constellations:
        fig, ax = plot_constellation(constellation_name, fig, ax, colors[i])
        i += 1
    save(fig)


def plot_stars_and_constellation(constellation_name):
    fig, ax = plot_stars()
    fig, ax = plot_constellation(constellation_name, fig, ax, 'yellow')
    save(fig)


def save(fig):
    fig.savefig('output.png', facecolor=fig.get_facecolor(), edgecolor='none')
    im = PIL.Image.open('output.png')
    im = im.crop((150, 150, 1070, 1070))
    im.save('output.png', 'png')
    print("Se ha guardado la imagen como output.png.")


starcoords = dict()
starlight = dict()
starnames = dict()
constellations = dict()

read_coords('files/stars.txt')
read_constellations()
plot_stars_and_constellations()
main.main()
