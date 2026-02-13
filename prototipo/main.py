"""
Prototipo de Sistema Universidad Web - Lógica de Negocio
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional


class Estudiante:
    """Clase que representa un estudiante"""
    
    def __init__(self, id: str, nombre: str, email: str, facultad: str, semestre: int):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.facultad = facultad
        self.semestre = semestre
        self.asignaturas = {}
        self.eventos = []
    
    def agregar_asignatura(self, nombre: str, codigo: str, creditos: int, nota: float):
        """Agregar una asignatura al estudiante"""
        self.asignaturas[codigo] = {
            'nombre': nombre,
            'codigo': codigo,
            'creditos': creditos,
            'nota': nota
        }
    
    def obtener_promedio(self) -> float:
        """Calcular promedio de calificaciones"""
        if not self.asignaturas:
            return 0.0
        total_notas = sum(a['nota'] for a in self.asignaturas.values())
        return round(total_notas / len(self.asignaturas), 2)
    
    def to_dict(self) -> Dict:
        """Convertir estudiante a diccionario"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'facultad': self.facultad,
            'semestre': self.semestre,
            'promedio': self.obtener_promedio()
        }


class Evento:
    """Clase que representa un evento académico"""
    
    def __init__(self, nombre: str, fecha: str, tipo: str, descripcion: str = ""):
        self.nombre = nombre
        self.fecha = fecha
        self.tipo = tipo
        self.descripcion = descripcion
    
    def to_dict(self) -> Dict:
        """Convertir evento a diccionario"""
        return {
            'nombre': self.nombre,
            'fecha': self.fecha,
            'tipo': self.tipo,
            'descripcion': self.descripcion
        }


class Ubicacion:
    """Clase que representa una ubicación en el mapa"""
    
    def __init__(self, nombre: str, facultad: str, latitud: float, longitud: float, descripcion: str = ""):
        self.nombre = nombre
        self.facultad = facultad
        self.latitud = latitud
        self.longitud = longitud
        self.descripcion = descripcion
    
    def to_dict(self) -> Dict:
        """Convertir ubicación a diccionario"""
        return {
            'nombre': self.nombre,
            'facultad': self.facultad,
            'latitud': self.latitud,
            'longitud': self.longitud,
            'descripcion': self.descripcion
        }


class SistemaUniversidad:
    """Sistema principal de la universidad"""
    
    def __init__(self):
        self.estudiantes = {}
        self.usuario_actual = None
        self.eventos = []
        self.ubicaciones = []
        self._inicializar_datos()
    
    def _inicializar_datos(self):
        """Inicializar datos de prueba"""
        
        # Crear estudiante
        estudiante = Estudiante(
            id="2024001",
            nombre="Juan Pérez",
            email="juan.perez@universidad.edu",
            facultad="Ingeniería de Sistemas",
            semestre=4
        )
        
        # Agregar asignaturas
        estudiante.agregar_asignatura("Programación Avanzada", "IS201", 3, 4.5)
        estudiante.agregar_asignatura("Bases de Datos", "IS202", 3, 4.2)
        estudiante.agregar_asignatura("Redes de Computadores", "IS203", 3, 4.8)
        estudiante.agregar_asignatura("Ingeniería de Software", "IS204", 4, 4.0)
        
        self.estudiantes[estudiante.email] = {
            'estudiante': estudiante,
            'contraseña': 'password'
        }
        
        # Crear eventos
        hoy = datetime.now()
        self.eventos = [
            Evento("Parcial 1", (hoy + timedelta(days=7)).strftime("%Y-%m-%d"), "Evaluación", "Primera prueba escrita"),
            Evento("Entrega Proyecto", (hoy + timedelta(days=15)).strftime("%Y-%m-%d"), "Entrega", "Proyecto final"),
            Evento("Parcial 2", (hoy + timedelta(days=25)).strftime("%Y-%m-%d"), "Evaluación", "Segunda prueba escrita"),
            Evento("Examen Final", (hoy + timedelta(days=35)).strftime("%Y-%m-%d"), "Examen", "Evaluación final"),
        ]
        
        # Crear ubicaciones
        self.ubicaciones = [
            Ubicacion("Edificio A", "Rectoría", 4.7489, -74.0891, "Aulas 101-110"),
            Ubicacion("Edificio B", "Ingeniería", 4.7490, -74.0892, "Laboratorios de Cómputo"),
            Ubicacion("Biblioteca Central", "Servicios", 4.7491, -74.0893, "3 pisos, 50000 libros"),
            Ubicacion("Cafetería", "Servicios", 4.7488, -74.0890, "Zona de descanso"),
            Ubicacion("Edificio C", "Facultad de Ciencias", 4.7492, -74.0894, "Aulas 201-210"),
            Ubicacion("Laboratorio de Sistemas", "Ingeniería", 4.7489, -74.0889, "Equipos y software especializado"),
        ]
    
    def login(self, email: str, contraseña: str) -> Dict:
        """Autenticar usuario"""
        if email not in self.estudiantes:
            return {'success': False, 'mensaje': 'Email no encontrado'}
        
        usuario = self.estudiantes[email]
        if usuario['contraseña'] != contraseña:
            return {'success': False, 'mensaje': 'Contraseña incorrecta'}
        
        self.usuario_actual = usuario['estudiante']
        return {
            'success': True,
            'mensaje': f'Bienvenido {usuario["estudiante"].nombre}',
            'estudiante': usuario['estudiante'].to_dict()
        }
    
    def logout(self) -> Dict:
        """Cerrar sesión"""
        if self.usuario_actual:
            nombre = self.usuario_actual.nombre
            self.usuario_actual = None
            return {'success': True, 'mensaje': f'Hasta luego {nombre}'}
        return {'success': False, 'mensaje': 'No hay sesión activa'}
    
    def obtener_perfil(self) -> Dict:
        """Obtener perfil del usuario actual"""
        if not self.usuario_actual:
            return {'success': False, 'mensaje': 'No hay sesión activa'}
        
        return {
            'success': True,
            'perfil': {
                'id': self.usuario_actual.id,
                'nombre': self.usuario_actual.nombre,
                'email': self.usuario_actual.email,
                'facultad': self.usuario_actual.facultad,
                'semestre': self.usuario_actual.semestre,
                'promedio': self.usuario_actual.obtener_promedio(),
                'asignaturas': list(self.usuario_actual.asignaturas.values())
            }
        }
    
    def obtener_calendario(self) -> Dict:
        """Obtener eventos del calendario"""
        if not self.usuario_actual:
            return {'success': False, 'mensaje': 'No hay sesión activa'}
        
        return {
            'success': True,
            'eventos': [evento.to_dict() for evento in self.eventos]
        }
    
    def obtener_mapa(self) -> Dict:
        """Obtener ubicaciones del mapa"""
        if not self.usuario_actual:
            return {'success': False, 'mensaje': 'No hay sesión activa'}
        
        return {
            'success': True,
            'ubicaciones': [ubicacion.to_dict() for ubicacion in self.ubicaciones]
        }
    
    def obtener_inicio(self) -> Dict:
        """Obtener información de inicio"""
        if not self.usuario_actual:
            return {'success': False, 'mensaje': 'No hay sesión activa'}
        
        return {
            'success': True,
            'bienvenida': f'¡Bienvenido {self.usuario_actual.nombre}!',
            'mensaje': 'Selecciona una opción del menú',
            'estudiante': self.usuario_actual.nombre
        }


def main():
    """Función principal para pruebas"""
    print("=" * 50)
    print("PROTOTIPO SISTEMA UNIVERSIDAD WEB")
    print("=" * 50)
    
    sistema = SistemaUniversidad()
    
    # Prueba de Login
    print("\n1. PROBANDO LOGIN")
    resultado = sistema.login("juan.perez@universidad.edu", "password")
    print(f"   Resultado: {resultado['mensaje']}")
    
    # Prueba de Inicio
    print("\n2. PROBANDO INICIO")
    resultado = sistema.obtener_inicio()
    print(f"   {resultado['bienvenida']}")
    print(f"   {resultado['mensaje']}")
    
    # Prueba de Perfil
    print("\n3. PROBANDO PERFIL")
    resultado = sistema.obtener_perfil()
    if resultado['success']:
        perfil = resultado['perfil']
        print(f"   Nombre: {perfil['nombre']}")
        print(f"   ID: {perfil['id']}")
        print(f"   Email: {perfil['email']}")
        print(f"   Facultad: {perfil['facultad']}")
        print(f"   Promedio: {perfil['promedio']}")
        print(f"   Asignaturas:")
        for asig in perfil['asignaturas']:
            print(f"     - {asig['nombre']}: {asig['nota']}")
    
    # Prueba de Calendario
    print("\n4. PROBANDO CALENDARIO")
    resultado = sistema.obtener_calendario()
    if resultado['success']:
        print(f"   Eventos próximos:")
        for evento in resultado['eventos']:
            print(f"     - {evento['nombre']} ({evento['fecha']})")
    
    # Prueba de Mapa
    print("\n5. PROBANDO MAPA")
    resultado = sistema.obtener_mapa()
    if resultado['success']:
        print(f"   Ubicaciones disponibles:")
        for ubicacion in resultado['ubicaciones']:
            print(f"     - {ubicacion['nombre']} ({ubicacion['facultad']})")
    
    # Prueba de Logout
    print("\n6. PROBANDO LOGOUT")
    resultado = sistema.logout()
    print(f"   {resultado['mensaje']}")
    
    # Prueba de acceso sin sesión
    print("\n7. PROBANDO ACCESO SIN SESIÓN")
    resultado = sistema.obtener_perfil()
    print(f"   Resultado: {resultado['mensaje']}")
    
    print("\n" + "=" * 50)
    print("FIN DE PRUEBAS")
    print("=" * 50)


if __name__ == "__main__":
    main()
