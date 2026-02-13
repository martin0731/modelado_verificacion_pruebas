"""
Prototipo Web con Flask - Sistema Universidad
"""
## Martin Estrada y Juan Andrés Correa
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from main import SistemaUniversidad
import json

app = Flask(__name__)
app.secret_key = 'clave_secreta_prototipo'

# Iniciailizar sistema
sistema = SistemaUniversidad()


@app.route('/')
def index():
    """Página principal - redirigir a login si no hay sesión"""
    if 'usuario' in session:
        return redirect(url_for('inicio'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Página de login"""
    if request.method == 'POST':
        email = request.form.get('email')
        contraseña = request.form.get('contraseña')
        
        resultado = sistema.login(email, contraseña)
        
        if resultado['success']:
            session['usuario'] = email
            return redirect(url_for('inicio'))
        else:
            return f"""
            <!DOCTYPE html>
            <html>
            <head><title>Login - Universidad</title></head>
            <body>
                <h1>Error de Login</h1>
                <p>{resultado['mensaje']}</p>
                <a href="/login">Volver al login</a>
            </body>
            </html>
            """, 401
    
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Login - Sistema Universidad</title>
        <style>
            body { font-family: Arial; text-align: center; padding: 50px; }
            form { width: 300px; margin: 0 auto; }
            input { width: 100%; padding: 10px; margin: 10px 0; }
            button { width: 100%; padding: 10px; background: #007bff; color: white; border: none; cursor: pointer; }
        </style>
    </head>
    <body>
        <h1>🔐 Sistema Universidad Web</h1>
        <form method="post">
            <h2>Login</h2>
            <input type="email" name="email" placeholder="Email" required value="juan.perez@universidad.edu">
            <input type="password" name="contraseña" placeholder="Contraseña" required value="password">
            <button type="submit">Ingresar</button>
        </form>
        <p style="margin-top: 30px; color: #666;">
            <small>Credenciales de prueba:<br>
            Email: juan.perez@universidad.edu<br>
            Contraseña: password</small>
        </p>
    </body>
    </html>
    """


@app.route('/inicio')
def inicio():
    """Página de inicio"""
    if 'usuario' not in session:
        return redirect(url_for('login'))
    
    resultado = sistema.obtener_inicio()
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Inicio - Universidad</title>
        <style>
            body {{ font-family: Arial; margin: 20px; }}
            .menu {{ margin: 20px 0; }}
            a {{ display: inline-block; margin: 10px; padding: 15px 30px; background: #007bff; color: white; text-decoration: none; border-radius: 5px; }}
            a:hover {{ background: #0056b3; }}
            .logout {{ background: #dc3545; }}
            .logout:hover {{ background: #c82333; }}
        </style>
    </head>
    <body>
        <h1>{resultado['bienvenida']}</h1>
        <p>{resultado['mensaje']}</p>
        
        <div class="menu">
            <h2>Menú Principal</h2>
            <a href="/perfil">👤 Ver Perfil</a>
            <a href="/calendario">📅 Ver Calendario</a>
            <a href="/mapa">🗺️ Ver Mapa</a>
            <a href="/logout" class="logout">🚪 Cerrar Sesión</a>
        </div>
    </body>
    </html>
    """


@app.route('/perfil')
def perfil():
    """Página de perfil"""
    if 'usuario' not in session:
        return redirect(url_for('login'))
    
    resultado = sistema.obtener_perfil()
    
    if not resultado['success']:
        return f"<h1>Error</h1><p>{resultado['mensaje']}</p>"
    
    perfil = resultado['perfil']
    asignaturas_html = ''.join([
        f"<tr><td>{a['nombre']}</td><td>{a['creditos']}</td><td>{a['nota']}</td></tr>"
        for a in perfil['asignaturas']
    ])
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Perfil - Universidad</title>
        <style>
            body {{ font-family: Arial; margin: 20px; }}
            table {{ border-collapse: collapse; width: 100%; max-width: 600px; }}
            th, td {{ padding: 10px; border: 1px solid #ddd; text-align: left; }}
            th {{ background: #007bff; color: white; }}
            .info {{ margin: 20px 0; }}
            a {{ display: inline-block; margin: 10px 0; padding: 10px 20px; background: #007bff; color: white; text-decoration: none; border-radius: 5px; }}
        </style>
    </head>
    <body>
        <h1>👤 Perfil del Estudiante</h1>
        
        <div class="info">
            <p><strong>Nombre:</strong> {perfil['nombre']}</p>
            <p><strong>ID:</strong> {perfil['id']}</p>
            <p><strong>Email:</strong> {perfil['email']}</p>
            <p><strong>Facultad:</strong> {perfil['facultad']}</p>
            <p><strong>Semestre:</strong> {perfil['semestre']}</p>
            <p><strong>Promedio:</strong> {perfil['promedio']}</p>
        </div>
        
        <h2>Asignaturas</h2>
        <table>
            <tr>
                <th>Asignatura</th>
                <th>Créditos</th>
                <th>Calificación</th>
            </tr>
            {asignaturas_html}
        </table>
        
        <a href="/inicio">← Volver al Inicio</a>
    </body>
    </html>
    """


@app.route('/calendario')
def calendario():
    """Página de calendario"""
    if 'usuario' not in session:
        return redirect(url_for('login'))
    
    resultado = sistema.obtener_calendario()
    
    if not resultado['success']:
        return f"<h1>Error</h1><p>{resultado['mensaje']}</p>"
    
    eventos_html = ''.join([
        f"<tr><td>{e['nombre']}</td><td>{e['fecha']}</td><td>{e['tipo']}</td></tr>"
        for e in resultado['eventos']
    ])
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Calendario - Universidad</title>
        <style>
            body {{ font-family: Arial; margin: 20px; }}
            table {{ border-collapse: collapse; width: 100%; max-width: 600px; }}
            th, td {{ padding: 10px; border: 1px solid #ddd; text-align: left; }}
            th {{ background: #28a745; color: white; }}
            a {{ display: inline-block; margin: 10px 0; padding: 10px 20px; background: #007bff; color: white; text-decoration: none; border-radius: 5px; }}
        </style>
    </head>
    <body>
        <h1>📅 Calendario Académico</h1>
        
        <table>
            <tr>
                <th>Evento</th>
                <th>Fecha</th>
                <th>Tipo</th>
            </tr>
            {eventos_html}
        </table>
        
        <a href="/inicio">← Volver al Inicio</a>
    </body>
    </html>
    """


@app.route('/mapa')
def mapa():
    """Página de mapa"""
    if 'usuario' not in session:
        return redirect(url_for('login'))
    
    resultado = sistema.obtener_mapa()
    
    if not resultado['success']:
        return f"<h1>Error</h1><p>{resultado['mensaje']}</p>"
    
    ubicaciones_html = ''.join([
        f"<tr><td>{u['nombre']}</td><td>{u['facultad']}</td><td>{u['descripcion']}</td></tr>"
        for u in resultado['ubicaciones']
    ])
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mapa - Universidad</title>
        <style>
            body {{ font-family: Arial; margin: 20px; }}
            table {{ border-collapse: collapse; width: 100%; max-width: 800px; }}
            th, td {{ padding: 10px; border: 1px solid #ddd; text-align: left; }}
            th {{ background: #ff6b6b; color: white; }}
            a {{ display: inline-block; margin: 10px 0; padding: 10px 20px; background: #007bff; color: white; text-decoration: none; border-radius: 5px; }}
        </style>
    </head>
    <body>
        <h1>🗺️ Mapa de Ubicaciones</h1>
        
        <table>
            <tr>
                <th>Ubicación</th>
                <th>Facultad</th>
                <th>Descripción</th>
            </tr>
            {ubicaciones_html}
        </table>
        
        <a href="/inicio">← Volver al Inicio</a>
    </body>
    </html>
    """


@app.route('/logout')
def logout():
    """Cerrar sesión"""
    resultado = sistema.logout()
    session.pop('usuario', None)
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Logout - Universidad</title>
        <style>
            body {{ font-family: Arial; text-align: center; padding: 50px; }}
            a {{ display: inline-block; margin: 20px; padding: 10px 20px; background: #007bff; color: white; text-decoration: none; border-radius: 5px; }}
        </style>
    </head>
    <body>
        <h1>✓ {resultado['mensaje']}</h1>
        <p>Sesión cerrada correctamente</p>
        <a href="/login">Volver al Login</a>
    </body>
    </html>
    """


if __name__ == '__main__':
    print("=" * 50)
    print("SERVIDOR FLASK INICIADO")
    print("=" * 50)
    print("Abre tu navegador en: http://localhost:5000")
    print("Email: juan.perez@universidad.edu")
    print("Contraseña: password")
    print("=" * 50)
    app.run(debug=True)
