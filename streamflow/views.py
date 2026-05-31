from django.shortcuts import render, redirect
from django.db import connection
from django.shortcuts import redirect

def index(request):
    return redirect('login')


ARTISTAS_IMAGENES = {
    'Bad Bunny': 'https://commons.wikimedia.org/wiki/Special:FilePath/Bad%20Bunny%202019%20by%20Glenn%20Francis%20(cropped).jpg',
    'Drake': 'https://commons.wikimedia.org/wiki/Special:FilePath/Drake%20at%20July%202016.jpg',
    'The Weeknd': 'https://commons.wikimedia.org/wiki/Special:FilePath/The%20Weeknd%20Portrait%20by%20Brian%20Ziff.jpg',
    'Taylor Swift': 'https://commons.wikimedia.org/wiki/Special:FilePath/Taylor%20Swift%20at%20the%202023%20MTV%20Video%20Music%20Awards.png',
    'Billie Eilish': 'https://commons.wikimedia.org/wiki/Special:FilePath/Billie%20Eilish%20Vogue%202023.jpg',
    'Dua Lipa': 'https://commons.wikimedia.org/wiki/Special:FilePath/Dua%20Lipa%20%2851630298836%29.jpg',
    'Karol G': 'https://commons.wikimedia.org/wiki/Special:FilePath/Karol%20G%20interview%202023.png',
    'Rauw Alejandro': 'https://commons.wikimedia.org/wiki/Special:FilePath/Rauw%20Alejandro%202021.jpg',
    'Kendrick Lamar': 'https://commons.wikimedia.org/wiki/Special:FilePath/Kendrick%20Lamar%202018.jpg',
    'Travis Scott': 'https://commons.wikimedia.org/wiki/Special:FilePath/Travis%20Scott%20-%20Openair%20Frauenfeld%202019%2008.jpg',
    'Post Malone': 'https://commons.wikimedia.org/wiki/Special:FilePath/Post%20Malone%202018.jpg',
    'SZA': 'https://commons.wikimedia.org/wiki/Special:FilePath/SZA%20Afropunk%202015.jpg',
    'Ariana Grande': 'https://commons.wikimedia.org/wiki/Special:FilePath/Ariana%20Grande%20Grammys%20Red%20Carpet%202020.png',
    'Harry Styles': 'https://commons.wikimedia.org/wiki/Special:FilePath/Harry%20Styles%20Wembley%20June%202022%20%28cropped%29.jpg',
    'Ed Sheeran': 'https://commons.wikimedia.org/wiki/Special:FilePath/Ed%20Sheeran-6886%20%28cropped%29.jpg',
    'Miley Cyrus': 'https://commons.wikimedia.org/wiki/Special:FilePath/Miley%20Cyrus%202019%20by%20Glenn%20Francis.jpg',
    'Sabrina Carpenter': 'https://commons.wikimedia.org/wiki/Special:FilePath/Sabrina%20Carpenter%20Vogue%202020.png',
    'Shakira': 'https://commons.wikimedia.org/wiki/Special:FilePath/Shakira%202014.jpg',
    'Rosalía': 'https://commons.wikimedia.org/wiki/Special:FilePath/Rosalia%20on%20the%20red%20carpet%20at%20the%2033rd%20Goya%20Awards%20in%202019.jpg',
    'J Balvin': 'https://commons.wikimedia.org/wiki/Special:FilePath/J%20Balvin%202019%20by%20Glenn%20Francis.jpg',
    'Maluma': 'https://commons.wikimedia.org/wiki/Special:FilePath/Maluma%20interview%202018.png',
    'Imagine Dragons': 'https://commons.wikimedia.org/wiki/Special:FilePath/Imagine%20Dragons%2C%20Roundhouse%2C%20London%20%2835390234536%29.jpg',
    'Coldplay': 'https://commons.wikimedia.org/wiki/Special:FilePath/ColdplayBBC071221%20%28cropped%29.jpg',
    'Linkin Park': 'https://commons.wikimedia.org/wiki/Special:FilePath/LinkinParkBerlin2010.jpg',
    'Arctic Monkeys': 'https://commons.wikimedia.org/wiki/Special:FilePath/Arctic%20Monkeys%20-%20Orange%20Stage%20-%20Roskilde%20Festival%202014.jpg',
    'Metallica': 'https://commons.wikimedia.org/wiki/Special:FilePath/Metallica%20at%20The%20O2%20Arena%20London%202008.jpg',
    'Queen': 'https://commons.wikimedia.org/wiki/Special:FilePath/Queen%20News%20Of%20The%20World%20%281977%20Press%20Kit%20Photo%2001%29.jpg',
    'Daft Punk': 'https://commons.wikimedia.org/wiki/Special:FilePath/Daft%20Punk%20in%202013%202.jpg',
    'Calvin Harris': 'https://commons.wikimedia.org/wiki/Special:FilePath/Calvin%20Harris%20-%20Rock%20in%20Rio%20Madrid%202012%20-%2004.jpg',
    'Beyoncé': 'https://commons.wikimedia.org/wiki/Special:FilePath/Beyonce%20-%20The%20Formation%20World%20Tour%2C%20at%20Wembley%20Stadium%20in%20London%2C%20England.jpg',
    'Rihanna': 'https://commons.wikimedia.org/wiki/Special:FilePath/Rihanna%20Fenty%202018.png',
    'Bruno Mars': 'https://commons.wikimedia.org/wiki/Special:FilePath/Bruno%20Mars%2C%20Las%20Vegas%202010.jpg'
}

ARTISTAS_IMAGENES.update({
    '21 Savage': 'https://commons.wikimedia.org/wiki/Special:FilePath/21%20Savage%20performing%20at%20Austin%20City%20Limits%20Music%20Festival%20-%202023%20-%2053437517570%20%28cropped%29.jpg',
    'Anuel AA': 'https://commons.wikimedia.org/wiki/Special:FilePath/Anuel%20AA%20in%202018.png',
    'Avicii': 'https://commons.wikimedia.org/wiki/Special:FilePath/Avicii%20In%20The%20Studio%20-%20The%20Making%20of%20Dancing%20In%20My%20Head.png',
    'Bizarrap': 'https://commons.wikimedia.org/wiki/Special:FilePath/Bizarrap%20in%202022.png',
    'Daddy Yankee': 'https://commons.wikimedia.org/wiki/Special:FilePath/Daddy%20Yankee%20in%202019.jpg',
    'Feid': 'https://commons.wikimedia.org/wiki/Special:FilePath/Feid%20in%202022.png',
    'Future': 'https://commons.wikimedia.org/wiki/Special:FilePath/Future%20%28rapper%29%202019.png',
    'HUMBE': None,
    'Junior H': None,
    'Karol G': 'https://commons.wikimedia.org/wiki/Special:FilePath/Karol%20G%20interview%202023.png',
    'Latin Mafia': None,
    'Maluma': 'https://commons.wikimedia.org/wiki/Special:FilePath/Maluma%20interview%202018.png',
    'Martin Garrix': 'https://commons.wikimedia.org/wiki/Special:FilePath/Martin%20Garrix%20-%20MTV%20EMA%202018%20%28cropped%29.png',
    'Morgan Wallen': 'https://commons.wikimedia.org/wiki/Special:FilePath/Morgan%20Wallen%20performing%20in%202019.jpg',
    'Nilo J': None,
    'Paulo Londra': 'https://commons.wikimedia.org/wiki/Special:FilePath/Paulo%20Londra%20%28cropped%29.jpg',
    'Peso Pluma': 'https://commons.wikimedia.org/wiki/Special:FilePath/Peso%20Pluma%20-%20MTV%20MIAW%202023%20%28cropped%29.png',
    'Rels B': 'https://commons.wikimedia.org/wiki/Special:FilePath/Rels%20B%20at%20the%202020%20Premios%20Ode%C3%B3n.jpg',
    'Wisin & Yandel': 'https://commons.wikimedia.org/wiki/Special:FilePath/Wisin%20%26%20Yandel%20in%202018.jpg',
    'Yandel': 'https://commons.wikimedia.org/wiki/Special:FilePath/Yandel%20in%202017.png'
})


def imagen_artista(nombre):

    return ARTISTAS_IMAGENES.get(nombre)


def artista_portada(nombre):

    return {
        'nombre': nombre,
        'imagen': imagen_artista(nombre)
    }

# =========================
# LOGIN
# =========================

def es_administrador(request):

    if 'tipoUsuario' not in request.session:
        return False

    return request.session['tipoUsuario'] == 'Administrador'


def es_gestor_o_admin(request):

    if 'tipoUsuario' not in request.session:
        return False

    return request.session['tipoUsuario'] in [
        'Administrador',
        'GestorContenido'
    ] 


def esta_logueado(request):

    return 'idUsuario' in request.session


def puede_ver_playlists(request):

    if 'tipoUsuario' not in request.session:
        return False

    return request.session['tipoUsuario'] in [
        'Administrador',
        'GestorContenido',
        'Premium'
    ]


def puede_modificar_playlist(request, idPlaylist):

    if es_gestor_o_admin(request):
        return True

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT idUsuarioCreador
            FROM Interaccion.Playlist
            WHERE idPlaylist = %s
        """, [idPlaylist])

        row = cursor.fetchone()

    if row is None:
        return False

    return row[0] == request.session['idUsuario']


def acceso_denegado(request):

    if 'idUsuario' not in request.session:
        return redirect('login')

    return render(request, 'home.html', {
        'error': 'Acceso denegado.'
    })
    
def login_view(request):

    if request.method == 'POST':

        email = request.POST['email']
        contrasena = request.POST['contrasena']

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT idUsuario, nombre, email, tipoUsuario, estado
                FROM Seguridad.Usuario
                WHERE email = %s
                  AND contrasena = %s
            """, [email, contrasena])

            row = cursor.fetchone()

        if row is not None:

            if row[4] != 'Activo':
                return render(request, 'login.html', {
                    'error': 'El usuario está inactivo.'
                })

            request.session['idUsuario'] = row[0]
            request.session['nombre'] = row[1]
            request.session['email'] = row[2]
            request.session['tipoUsuario'] = row[3]

            return redirect('home')

        return render(request, 'login.html', {
            'error': 'Correo o contraseña incorrectos.'
        })

    return render(request, 'login.html')


# =========================
# LOGOUT
# =========================

def logout_view(request):

    request.session.flush()

    return redirect('login')


# =========================
# HOME
# =========================

def home_view(request):

    if 'idUsuario' not in request.session:
        return redirect('login')

    mixes = [
        {
            'titulo': 'Mix diario 1',
            'descripcion': 'Bad Bunny, The Weeknd, Taylor Swift y Coldplay',
            'artistas': [
                artista_portada('Bad Bunny'),
                artista_portada('The Weeknd'),
                artista_portada('Taylor Swift'),
                artista_portada('Coldplay')
            ]
        },
        {
            'titulo': 'Mix diario 2',
            'descripcion': 'Queen, Linkin Park, Imagine Dragons y Daft Punk',
            'artistas': [
                artista_portada('Queen'),
                artista_portada('Linkin Park'),
                artista_portada('Imagine Dragons'),
                artista_portada('Daft Punk')
            ]
        },
        {
            'titulo': 'Mix diario 3',
            'descripcion': 'Taylor Swift, Beyoncé, Shakira y Bad Bunny',
            'artistas': [
                artista_portada('Taylor Swift'),
                artista_portada('Beyoncé'),
                artista_portada('Shakira'),
                artista_portada('Bad Bunny')
            ]
        },
        {
            'titulo': 'Mix diario 4',
            'descripcion': 'Coldplay, Linkin Park, Queen e Imagine Dragons',
            'artistas': [
                artista_portada('Coldplay'),
                artista_portada('Linkin Park'),
                artista_portada('Queen'),
                artista_portada('Imagine Dragons')
            ]
        },
        {
            'titulo': 'Mix diario 5',
            'descripcion': 'Daft Punk, The Weeknd, Beyoncé y Shakira',
            'artistas': [
                artista_portada('Daft Punk'),
                artista_portada('The Weeknd'),
                artista_portada('Beyoncé'),
                artista_portada('Shakira')
            ]
        }
    ]

    playlists_inicio = [
        {
            'titulo': 'Playlist 1',
            'descripcion': 'Pop global para empezar el día',
            'imagen': imagen_artista('Taylor Swift')
        },
        {
            'titulo': 'Playlist 2',
            'descripcion': 'Urbano latino y reggaetón',
            'imagen': imagen_artista('Bad Bunny')
        },
        {
            'titulo': 'Playlist 3',
            'descripcion': 'Rap y trap internacional',
            'imagen': imagen_artista('Kendrick Lamar')
        },
        {
            'titulo': 'Playlist 4',
            'descripcion': 'Rock, indie y clásicos',
            'imagen': imagen_artista('Arctic Monkeys')
        },
        {
            'titulo': 'Playlist 5',
            'descripcion': 'Electrónica y festival',
            'imagen': imagen_artista('Daft Punk')
        }
    ]

    return render(request, 'home.html', {
        'mixes': mixes,
        'playlists_inicio': playlists_inicio
    })
# =========================
# HOME
# =========================


# =========================
# CANCIONES
# =========================

def canciones_listar(request):

    if not esta_logueado(request):
        return redirect('login')

    busqueda = request.GET.get('buscar', '')
    idUsuario = request.session['idUsuario']

    parametros = [idUsuario]

    consulta = """
        SELECT
            c.idCancion,
            c.titulo,
            c.duracionSeg,
            c.estadoCancion,
            al.titulo,
            ar.nombreArtistico,
            CASE
                WHEN lc.idUsuario IS NULL THEN 0
                ELSE 1
            END AS tieneLike

        FROM Catalogo.Cancion c

        INNER JOIN Catalogo.Album al
            ON c.idAlbum = al.idAlbum

        INNER JOIN Catalogo.Artista ar
            ON al.idArtista = ar.idArtista

        LEFT JOIN Interaccion.LikeCancion lc
            ON lc.idCancion = c.idCancion
           AND lc.idUsuario = %s
    """

    if busqueda:
        consulta += """
            WHERE c.titulo LIKE %s
               OR al.titulo LIKE %s
               OR ar.nombreArtistico LIKE %s
        """
        texto = '%' + busqueda + '%'
        parametros.extend([texto, texto, texto])

    consulta += """
        ORDER BY ar.nombreArtistico, al.titulo, c.titulo
    """

    with connection.cursor() as cursor:

        cursor.execute(consulta, parametros)

        rows = cursor.fetchall()

    canciones = []

    for row in rows:

        minutos = row[2] // 60
        segundos = row[2] % 60

        canciones.append({
            'id': row[0],
            'titulo': row[1],
            'duracion': f'{minutos}:{segundos:02d}',
            'estado': row[3],
            'album': row[4],
            'artista': row[5],
            'tiene_like': row[6] == 1
        })

    return render(request, 'canciones_listar.html', {
        'canciones': canciones,
        'busqueda': busqueda
    })


def canciones_like(request, idCancion):

    if not esta_logueado(request):
        return redirect('login')

    if request.method == 'POST':

        with connection.cursor() as cursor:

            cursor.execute("""
                IF NOT EXISTS (
                    SELECT 1
                    FROM Interaccion.LikeCancion
                    WHERE idUsuario = %s
                      AND idCancion = %s
                )
                BEGIN
                    INSERT INTO Interaccion.LikeCancion
                    (idUsuario, idCancion, fechaLike)

                    VALUES (%s, %s, GETDATE())
                END
            """, [
                request.session['idUsuario'],
                idCancion,
                request.session['idUsuario'],
                idCancion
            ])

    return redirect('canciones_listar')


def canciones_quitar_like(request, idCancion):

    if not esta_logueado(request):
        return redirect('login')

    if request.method == 'POST':

        with connection.cursor() as cursor:

            cursor.execute("""
                DELETE FROM Interaccion.LikeCancion
                WHERE idUsuario = %s
                  AND idCancion = %s
            """, [
                request.session['idUsuario'],
                idCancion
            ])

    if request.POST.get('volver') == 'likes':
        return redirect('likes_listar')

    return redirect('canciones_listar')


# =========================
# ALBUMES
# =========================

def albumes_listar(request):

    if not esta_logueado(request):
        return redirect('login')

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT
                al.idAlbum,
                al.titulo,
                al.fechaLanzamiento,
                al.tipo,
                ar.nombreArtistico,
                COUNT(c.idCancion)

            FROM Catalogo.Album al

            INNER JOIN Catalogo.Artista ar
                ON al.idArtista = ar.idArtista

            LEFT JOIN Catalogo.Cancion c
                ON al.idAlbum = c.idAlbum

            GROUP BY
                al.idAlbum,
                al.titulo,
                al.fechaLanzamiento,
                al.tipo,
                ar.nombreArtistico

            ORDER BY al.fechaLanzamiento DESC, al.titulo
        """)

        rows = cursor.fetchall()

    albumes = []

    for row in rows:

        albumes.append({
            'id': row[0],
            'titulo': row[1],
            'fecha': row[2],
            'tipo': row[3],
            'artista': row[4],
            'canciones': row[5],
            'imagen': imagen_artista(row[4])
        })

    return render(request, 'albumes_listar.html', {
        'albumes': albumes
    })


# =========================
# MIS LIKES
# =========================

def likes_listar(request):

    if not esta_logueado(request):
        return redirect('login')

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT
                c.idCancion,
                c.titulo,
                c.duracionSeg,
                al.titulo,
                ar.nombreArtistico,
                lc.fechaLike

            FROM Interaccion.LikeCancion lc

            INNER JOIN Catalogo.Cancion c
                ON lc.idCancion = c.idCancion

            INNER JOIN Catalogo.Album al
                ON c.idAlbum = al.idAlbum

            INNER JOIN Catalogo.Artista ar
                ON al.idArtista = ar.idArtista

            WHERE lc.idUsuario = %s

            ORDER BY lc.fechaLike DESC
        """, [request.session['idUsuario']])

        rows = cursor.fetchall()

    canciones = []

    for row in rows:

        minutos = row[2] // 60
        segundos = row[2] % 60

        canciones.append({
            'id': row[0],
            'titulo': row[1],
            'duracion': f'{minutos}:{segundos:02d}',
            'album': row[3],
            'artista': row[4],
            'fecha': row[5]
        })

    return render(request, 'likes_listar.html', {
        'canciones': canciones
    })


# =========================
# PLAYLISTS
# =========================

def playlists_listar(request):

    if not esta_logueado(request):
        return redirect('login')

    if not puede_ver_playlists(request):
        return acceso_denegado(request)

    parametros = []

    consulta = """
        SELECT
            p.idPlaylist,
            p.nombrePlaylist,
            p.tipoPlaylist,
            p.fechaCreacion,
            u.nombre,
            COUNT(pc.idCancion)

        FROM Interaccion.Playlist p

        INNER JOIN Seguridad.Usuario u
            ON p.idUsuarioCreador = u.idUsuario

        LEFT JOIN Interaccion.PlaylistCancion pc
            ON p.idPlaylist = pc.idPlaylist
    """

    if request.session['tipoUsuario'] == 'Premium':
        consulta += """
            WHERE p.idUsuarioCreador = %s
        """
        parametros.append(request.session['idUsuario'])

    consulta += """
        GROUP BY
            p.idPlaylist,
            p.nombrePlaylist,
            p.tipoPlaylist,
            p.fechaCreacion,
            u.nombre

        ORDER BY p.fechaCreacion DESC
    """

    with connection.cursor() as cursor:

        cursor.execute(consulta, parametros)

        rows = cursor.fetchall()

    playlists = []

    for row in rows:

        playlists.append({
            'id': row[0],
            'nombre': row[1],
            'tipo': row[2],
            'fecha': row[3],
            'creador': row[4],
            'canciones': row[5]
        })

    return render(request, 'playlists_listar.html', {
        'playlists': playlists
    })


def playlists_crear(request):

    if not esta_logueado(request):
        return redirect('login')

    if not puede_ver_playlists(request):
        return acceso_denegado(request)

    if request.method == 'POST':

        idUsuarioCreador = request.session['idUsuario']

        if es_gestor_o_admin(request):
            idUsuarioCreador = request.POST['usuario']

        nombre = request.POST['nombre']
        tipo = request.POST['tipo']

        with connection.cursor() as cursor:

            cursor.execute("""
                INSERT INTO Interaccion.Playlist
                (idUsuarioCreador, nombrePlaylist, tipoPlaylist, fechaCreacion)

                VALUES (%s, %s, %s, GETDATE())
            """, [
                idUsuarioCreador,
                nombre,
                tipo
            ])

        return redirect('playlists_listar')

    usuarios = []

    if es_gestor_o_admin(request):

        with connection.cursor() as cursor:

            cursor.execute("""
                SELECT idUsuario, nombre, tipoUsuario
                FROM Seguridad.Usuario
                WHERE estado = 'Activo'
                ORDER BY nombre
            """)

            rows = cursor.fetchall()

        for row in rows:

            usuarios.append({
                'id': row[0],
                'nombre': row[1],
                'tipo': row[2]
            })

    return render(request, 'playlists_form.html', {
        'usuarios': usuarios
    })


def playlists_detalle(request, idPlaylist):

    if not esta_logueado(request):
        return redirect('login')

    if not puede_ver_playlists(request):
        return acceso_denegado(request)

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT
                p.idPlaylist,
                p.idUsuarioCreador,
                p.nombrePlaylist,
                p.tipoPlaylist,
                p.fechaCreacion,
                u.nombre

            FROM Interaccion.Playlist p

            INNER JOIN Seguridad.Usuario u
                ON p.idUsuarioCreador = u.idUsuario

            WHERE p.idPlaylist = %s
        """, [idPlaylist])

        row = cursor.fetchone()

    if row is None:
        return redirect('playlists_listar')

    if request.session['tipoUsuario'] == 'Premium' and row[1] != request.session['idUsuario']:
        return acceso_denegado(request)

    playlist = {
        'id': row[0],
        'usuario_id': row[1],
        'nombre': row[2],
        'tipo': row[3],
        'fecha': row[4],
        'creador': row[5]
    }

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT
                c.idCancion,
                c.titulo,
                c.duracionSeg,
                al.titulo,
                ar.nombreArtistico,
                pc.fechaAgregado

            FROM Interaccion.PlaylistCancion pc

            INNER JOIN Catalogo.Cancion c
                ON pc.idCancion = c.idCancion

            INNER JOIN Catalogo.Album al
                ON c.idAlbum = al.idAlbum

            INNER JOIN Catalogo.Artista ar
                ON al.idArtista = ar.idArtista

            WHERE pc.idPlaylist = %s

            ORDER BY pc.fechaAgregado DESC
        """, [idPlaylist])

        canciones_rows = cursor.fetchall()

        cursor.execute("""
            SELECT
                c.idCancion,
                c.titulo,
                al.titulo,
                ar.nombreArtistico

            FROM Catalogo.Cancion c

            INNER JOIN Catalogo.Album al
                ON c.idAlbum = al.idAlbum

            INNER JOIN Catalogo.Artista ar
                ON al.idArtista = ar.idArtista

            WHERE c.estadoCancion = 'Activo'
              AND c.idCancion NOT IN (
                    SELECT idCancion
                    FROM Interaccion.PlaylistCancion
                    WHERE idPlaylist = %s
              )

            ORDER BY ar.nombreArtistico, c.titulo
        """, [idPlaylist])

        disponibles_rows = cursor.fetchall()

    canciones = []

    for row in canciones_rows:

        minutos = row[2] // 60
        segundos = row[2] % 60

        canciones.append({
            'id': row[0],
            'titulo': row[1],
            'duracion': f'{minutos}:{segundos:02d}',
            'album': row[3],
            'artista': row[4],
            'fecha': row[5]
        })

    disponibles = []

    for row in disponibles_rows:

        disponibles.append({
            'id': row[0],
            'titulo': row[1],
            'album': row[2],
            'artista': row[3]
        })

    return render(request, 'playlists_detalle.html', {
        'playlist': playlist,
        'canciones': canciones,
        'disponibles': disponibles
    })


def playlists_agregar_cancion(request, idPlaylist):

    if not esta_logueado(request):
        return redirect('login')

    if not puede_ver_playlists(request):
        return acceso_denegado(request)

    if not puede_modificar_playlist(request, idPlaylist):
        return acceso_denegado(request)

    if request.method == 'POST':

        idCancion = request.POST['cancion']

        with connection.cursor() as cursor:

            cursor.execute("""
                IF NOT EXISTS (
                    SELECT 1
                    FROM Interaccion.PlaylistCancion
                    WHERE idPlaylist = %s
                      AND idCancion = %s
                )
                BEGIN
                    INSERT INTO Interaccion.PlaylistCancion
                    (idPlaylist, idCancion, fechaAgregado)

                    VALUES (%s, %s, GETDATE())
                END
            """, [
                idPlaylist,
                idCancion,
                idPlaylist,
                idCancion
            ])

    return redirect('playlists_detalle', idPlaylist=idPlaylist)


def playlists_quitar_cancion(request, idPlaylist, idCancion):

    if not esta_logueado(request):
        return redirect('login')

    if not puede_ver_playlists(request):
        return acceso_denegado(request)

    if not puede_modificar_playlist(request, idPlaylist):
        return acceso_denegado(request)

    if request.method == 'POST':

        with connection.cursor() as cursor:

            cursor.execute("""
                DELETE FROM Interaccion.PlaylistCancion
                WHERE idPlaylist = %s
                  AND idCancion = %s
            """, [
                idPlaylist,
                idCancion
            ])

    return redirect('playlists_detalle', idPlaylist=idPlaylist)




# =========================
# LISTAR USUARIOS
# =========================

def usuarios_listar(request):
    if not es_administrador(request):
        return acceso_denegado(request)

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT idUsuario, nombre, email, tipoUsuario, estado
            FROM Seguridad.Usuario
            ORDER BY idUsuario
        """)

        rows = cursor.fetchall()

    usuarios = []

    for row in rows:

        usuarios.append({
            'id': row[0],
            'nombre': row[1],
            'email': row[2],
            'tipo': row[3],
            'estado': row[4]
        })

    return render(request, 'usuarios_listar.html', {
        'usuarios': usuarios
    })


# =========================
# CREAR USUARIO
# =========================

def usuarios_crear(request):
    
    if not es_administrador(request):
        return acceso_denegado(request)

    if request.method == 'POST':

        nombre = request.POST['nombre']
        email = request.POST['email']
        contrasena = request.POST['contrasena']
        tipo = request.POST['tipo']

        with connection.cursor() as cursor:

            cursor.execute("""
                INSERT INTO Seguridad.Usuario
                (nombre, email, contrasena, tipoUsuario, estado)

                VALUES (%s, %s, %s, %s, 'Activo')
            """, [nombre, email, contrasena, tipo])

        return redirect('usuarios_listar')

    return render(request, 'usuarios_form.html')


# =========================
# EDITAR USUARIO
# =========================

def usuarios_editar(request, idUsuario):
    if not es_administrador(request):
        return acceso_denegado(request)

    with connection.cursor() as cursor:

        if request.method == 'POST':

            nombre = request.POST['nombre']
            email = request.POST['email']
            contrasena = request.POST['contrasena']
            tipo = request.POST['tipo']
            estado = request.POST['estado']

            cursor.execute("""
                UPDATE Seguridad.Usuario

                SET
                    nombre = %s,
                    email = %s,
                    contrasena = %s,
                    tipoUsuario = %s,
                    estado = %s

                WHERE idUsuario = %s
            """, [
                nombre,
                email,
                contrasena,
                tipo,
                estado,
                idUsuario
            ])

            return redirect('usuarios_listar')

        cursor.execute("""
            SELECT
                idUsuario,
                nombre,
                email,
                contrasena,
                tipoUsuario,
                estado

            FROM Seguridad.Usuario

            WHERE idUsuario = %s
        """, [idUsuario])

        row = cursor.fetchone()

    usuario = {
        'id': row[0],
        'nombre': row[1],
        'email': row[2],
        'contrasena': row[3],
        'tipo': row[4],
        'estado': row[5]
    }

    return render(request, 'usuarios_form.html', {
        'usuario': usuario
    })


# =========================
# ELIMINAR USUARIO
# =========================

def usuarios_eliminar(request, idUsuario):
    if not es_administrador(request):
        return acceso_denegado(request)

    with connection.cursor() as cursor:

        cursor.execute("""
            DELETE FROM Seguridad.Usuario
            WHERE idUsuario = %s
        """, [idUsuario])

    return redirect('usuarios_listar')

# =========================
# LISTAR ARTISTAS
# =========================

def artistas_listar(request):
    if not es_gestor_o_admin(request):
        return acceso_denegado(request)

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT
                a.idArtista,
                a.nombreArtistico,
                a.pais,
                a.estadoArtista,
                d.nombreDisquera

            FROM Catalogo.Artista a

            LEFT JOIN Catalogo.Discografia d
                ON a.idDiscografica = d.idDiscografica

            ORDER BY a.idArtista
        """)

        rows = cursor.fetchall()

    artistas = []

    for row in rows:

        artistas.append({
            'id': row[0],
            'nombre': row[1],
            'pais': row[2],
            'estado': row[3],
            'discografica': row[4]
        })

    return render(request, 'artistas_listar.html', {
        'artistas': artistas
    })


# =========================
# CREAR ARTISTA
# =========================

def artistas_crear(request):
    if not es_gestor_o_admin(request):
        return acceso_denegado(request)

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT idDiscografica, nombreDisquera
            FROM Catalogo.Discografia
        """)

        discograficas_rows = cursor.fetchall()

    discograficas = []

    for row in discograficas_rows:

        discograficas.append({
            'id': row[0],
            'nombre': row[1]
        })

    if request.method == 'POST':

        nombre = request.POST['nombre']
        biografia = request.POST['biografia']
        pais = request.POST['pais']
        estado = request.POST['estado']
        discografica = request.POST['discografica']

        with connection.cursor() as cursor:

            cursor.execute("""
                INSERT INTO Catalogo.Artista
                (
                    nombreArtistico,
                    biografia,
                    pais,
                    estadoArtista,
                    idDiscografica
                )

                VALUES (%s, %s, %s, %s, %s)
            """, [
                nombre,
                biografia,
                pais,
                estado,
                discografica
            ])

        return redirect('artistas_listar')

    return render(request, 'artistas_form.html', {
        'discograficas': discograficas
    })


# =========================
# EDITAR ARTISTA
# =========================

def artistas_editar(request, idArtista):
    if not es_gestor_o_admin(request):
        return acceso_denegado(request)

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT idDiscografica, nombreDisquera
            FROM Catalogo.Discografia
        """)

        discograficas_rows = cursor.fetchall()

    discograficas = []

    for row in discograficas_rows:

        discograficas.append({
            'id': row[0],
            'nombre': row[1]
        })

    with connection.cursor() as cursor:

        if request.method == 'POST':

            nombre = request.POST['nombre']
            biografia = request.POST['biografia']
            pais = request.POST['pais']
            estado = request.POST['estado']
            discografica = request.POST['discografica']

            cursor.execute("""
                UPDATE Catalogo.Artista

                SET
                    nombreArtistico = %s,
                    biografia = %s,
                    pais = %s,
                    estadoArtista = %s,
                    idDiscografica = %s

                WHERE idArtista = %s
            """, [
                nombre,
                biografia,
                pais,
                estado,
                discografica,
                idArtista
            ])

            return redirect('artistas_listar')

        cursor.execute("""
            SELECT
                idArtista,
                nombreArtistico,
                biografia,
                pais,
                estadoArtista,
                idDiscografica

            FROM Catalogo.Artista

            WHERE idArtista = %s
        """, [idArtista])

        row = cursor.fetchone()

    artista = {
        'id': row[0],
        'nombre': row[1],
        'biografia': row[2],
        'pais': row[3],
        'estado': row[4],
        'discografica': row[5]
    }

    return render(request, 'artistas_form.html', {
        'artista': artista,
        'discograficas': discograficas
    })


# =========================
# ELIMINAR ARTISTA
# =========================

def artistas_eliminar(request, idArtista):
    if not es_gestor_o_admin(request):
        return acceso_denegado(request)

    with connection.cursor() as cursor:

        cursor.execute("""
            DELETE FROM Catalogo.Artista
            WHERE idArtista = %s
        """, [idArtista])

    return redirect('artistas_listar')


# =========================
# RUTAS ADMIN PENDIENTES
# =========================

def albumes_admin(request):
    if not es_gestor_o_admin(request):
        return acceso_denegado(request)

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT
                al.idAlbum,
                al.titulo,
                al.fechaLanzamiento,
                al.tipo,
                ar.nombreArtistico,
                COUNT(c.idCancion)

            FROM Catalogo.Album al

            INNER JOIN Catalogo.Artista ar
                ON al.idArtista = ar.idArtista

            LEFT JOIN Catalogo.Cancion c
                ON al.idAlbum = c.idAlbum

            GROUP BY
                al.idAlbum,
                al.titulo,
                al.fechaLanzamiento,
                al.tipo,
                ar.nombreArtistico

            ORDER BY al.idAlbum DESC
        """)

        rows = cursor.fetchall()

    albumes = []

    for row in rows:

        albumes.append({
            'id': row[0],
            'titulo': row[1],
            'fecha': row[2],
            'tipo': row[3],
            'artista': row[4],
            'canciones': row[5],
            'imagen': imagen_artista(row[4])
        })

    return render(request, 'albumes_admin_listar.html', {
        'albumes': albumes
    })


def canciones_admin(request):
    if not es_gestor_o_admin(request):
        return acceso_denegado(request)

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT
                c.idCancion,
                c.titulo,
                c.duracionSeg,
                c.estadoCancion,
                al.titulo,
                ar.nombreArtistico

            FROM Catalogo.Cancion c

            INNER JOIN Catalogo.Album al
                ON c.idAlbum = al.idAlbum

            INNER JOIN Catalogo.Artista ar
                ON al.idArtista = ar.idArtista

            ORDER BY c.idCancion DESC
        """)

        rows = cursor.fetchall()

    canciones = []

    for row in rows:

        minutos = row[2] // 60
        segundos = row[2] % 60

        canciones.append({
            'id': row[0],
            'titulo': row[1],
            'duracion': f'{minutos}:{segundos:02d}',
            'estado': row[3],
            'album': row[4],
            'artista': row[5]
        })

    return render(request, 'canciones_admin_listar.html', {
        'canciones': canciones
    })


def reportes(request):
    if not es_gestor_o_admin(request):
        return acceso_denegado(request)

    with connection.cursor() as cursor:

        cursor.execute("SELECT COUNT(*) FROM Seguridad.Usuario")
        total_usuarios = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM Seguridad.Usuario WHERE estado = 'Activo'")
        usuarios_activos = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM Seguridad.Usuario WHERE estado <> 'Activo'")
        usuarios_inactivos = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM Catalogo.Artista")
        total_artistas = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM Catalogo.Album")
        total_albumes = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM Catalogo.Cancion")
        total_canciones = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM Interaccion.Playlist")
        total_playlists = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM Interaccion.LikeCancion")
        total_likes = cursor.fetchone()[0]

        cursor.execute("""
            SELECT tipoUsuario, COUNT(*)
            FROM Seguridad.Usuario
            GROUP BY tipoUsuario
            ORDER BY COUNT(*) DESC
        """)
        usuarios_por_tipo_rows = cursor.fetchall()

        cursor.execute("""
            SELECT estado, COUNT(*)
            FROM Seguridad.Usuario
            GROUP BY estado
            ORDER BY COUNT(*) DESC
        """)
        usuarios_por_estado_rows = cursor.fetchall()

        cursor.execute("""
            SELECT TOP 10
                c.titulo,
                ar.nombreArtistico,
                al.titulo,
                COUNT(lc.idUsuario) AS totalLikes

            FROM Catalogo.Cancion c

            INNER JOIN Catalogo.Album al
                ON c.idAlbum = al.idAlbum

            INNER JOIN Catalogo.Artista ar
                ON al.idArtista = ar.idArtista

            LEFT JOIN Interaccion.LikeCancion lc
                ON c.idCancion = lc.idCancion

            GROUP BY
                c.titulo,
                ar.nombreArtistico,
                al.titulo

            ORDER BY totalLikes DESC, c.titulo
        """)
        canciones_top_rows = cursor.fetchall()

        cursor.execute("""
            SELECT TOP 10
                p.nombrePlaylist,
                p.tipoPlaylist,
                u.nombre,
                COUNT(pc.idCancion) AS totalCanciones

            FROM Interaccion.Playlist p

            INNER JOIN Seguridad.Usuario u
                ON p.idUsuarioCreador = u.idUsuario

            LEFT JOIN Interaccion.PlaylistCancion pc
                ON p.idPlaylist = pc.idPlaylist

            GROUP BY
                p.nombrePlaylist,
                p.tipoPlaylist,
                u.nombre

            ORDER BY totalCanciones DESC, p.nombrePlaylist
        """)
        playlists_top_rows = cursor.fetchall()

        cursor.execute("""
            SELECT TOP 10
                ar.nombreArtistico,
                COUNT(c.idCancion) AS totalCanciones,
                COUNT(DISTINCT al.idAlbum) AS totalAlbumes

            FROM Catalogo.Artista ar

            LEFT JOIN Catalogo.Album al
                ON ar.idArtista = al.idArtista

            LEFT JOIN Catalogo.Cancion c
                ON al.idAlbum = c.idAlbum

            GROUP BY ar.nombreArtistico

            ORDER BY totalCanciones DESC, ar.nombreArtistico
        """)
        artistas_top_rows = cursor.fetchall()

        cursor.execute("""
            SELECT TOP 10
                u.nombre,
                u.email,
                u.tipoUsuario,
                COUNT(lc.idCancion) AS totalLikes

            FROM Seguridad.Usuario u

            LEFT JOIN Interaccion.LikeCancion lc
                ON u.idUsuario = lc.idUsuario

            GROUP BY
                u.nombre,
                u.email,
                u.tipoUsuario

            ORDER BY totalLikes DESC, u.nombre
        """)
        usuarios_likes_rows = cursor.fetchall()

        cursor.execute("""
            SELECT TOP 10
                u.nombre,
                u.email,
                u.tipoUsuario,
                COUNT(p.idPlaylist) AS totalPlaylists

            FROM Seguridad.Usuario u

            LEFT JOIN Interaccion.Playlist p
                ON u.idUsuario = p.idUsuarioCreador

            GROUP BY
                u.nombre,
                u.email,
                u.tipoUsuario

            ORDER BY totalPlaylists DESC, u.nombre
        """)
        usuarios_playlists_rows = cursor.fetchall()

        cursor.execute("""
            SELECT TOP 12
                u.idUsuario,
                u.nombre,
                u.email,
                u.tipoUsuario,
                u.estado

            FROM Seguridad.Usuario u

            WHERE u.estado <> 'Activo'

            ORDER BY u.idUsuario DESC
        """)
        usuarios_desconectados_rows = cursor.fetchall()

    usuarios_por_tipo = []
    for row in usuarios_por_tipo_rows:
        usuarios_por_tipo.append({
            'tipo': row[0],
            'total': row[1]
        })

    usuarios_por_estado = []
    for row in usuarios_por_estado_rows:
        usuarios_por_estado.append({
            'estado': row[0],
            'total': row[1]
        })

    canciones_top = []
    for row in canciones_top_rows:
        canciones_top.append({
            'titulo': row[0],
            'artista': row[1],
            'album': row[2],
            'likes': row[3]
        })

    playlists_top = []
    for row in playlists_top_rows:
        playlists_top.append({
            'nombre': row[0],
            'tipo': row[1],
            'creador': row[2],
            'canciones': row[3]
        })

    artistas_top = []
    for row in artistas_top_rows:
        artistas_top.append({
            'nombre': row[0],
            'canciones': row[1],
            'albumes': row[2]
        })

    usuarios_likes = []
    for row in usuarios_likes_rows:
        usuarios_likes.append({
            'nombre': row[0],
            'email': row[1],
            'tipo': row[2],
            'likes': row[3]
        })

    usuarios_playlists = []
    for row in usuarios_playlists_rows:
        usuarios_playlists.append({
            'nombre': row[0],
            'email': row[1],
            'tipo': row[2],
            'playlists': row[3]
        })

    usuarios_desconectados = []
    for row in usuarios_desconectados_rows:
        usuarios_desconectados.append({
            'id': row[0],
            'nombre': row[1],
            'email': row[2],
            'tipo': row[3],
            'estado': row[4]
        })

    return render(request, 'reportes.html', {
        'total_usuarios': total_usuarios,
        'usuarios_activos': usuarios_activos,
        'usuarios_inactivos': usuarios_inactivos,
        'total_artistas': total_artistas,
        'total_albumes': total_albumes,
        'total_canciones': total_canciones,
        'total_playlists': total_playlists,
        'total_likes': total_likes,
        'usuarios_por_tipo': usuarios_por_tipo,
        'usuarios_por_estado': usuarios_por_estado,
        'canciones_top': canciones_top,
        'playlists_top': playlists_top,
        'artistas_top': artistas_top,
        'usuarios_likes': usuarios_likes,
        'usuarios_playlists': usuarios_playlists,
        'usuarios_desconectados': usuarios_desconectados
    })
