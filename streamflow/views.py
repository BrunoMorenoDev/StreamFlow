from django.shortcuts import render, redirect
from django.db import connection
from django.shortcuts import redirect

def index(request):
    return redirect('login')

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

    return render(request, 'home.html')
# =========================
# HOME
# =========================




# =========================
# LISTAR USUARIOS
# =========================

def usuarios_listar(request):
    if not es_administrador(request):
     return redirect('home') 

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
     return redirect('home') 

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
     return redirect('home') 

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
     return redirect('home')

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

    with connection.cursor() as cursor:

        cursor.execute("""
            DELETE FROM Catalogo.Artista
            WHERE idArtista = %s
        """, [idArtista])

    return redirect('artistas_listar')