# Prototipo Sistema Universidad Web
## Martin
## Descripción
Prototipo funcional en Python de la página de la universidad con:
- 🔐 Login simple
- 📄 Página de Inicio
- 👤 Perfil del Estudiante (nombre, ID, email, asignaturas, notas)
- 📅 Calendario (eventos académicos)
- 🗺️ Mapa (ubicaciones de edificios)

Sin base de datos, todo local con datos en memoria.

## Requisitos
- Python 3.8+
- Flask (para versión web)
- Tkinter (para interfaz gráfica)

## Instalación

```bash
# Clonar o descargar el proyecto
cd prototipo

# Instalar dependencias
pip install flask
```

## Estructura del Proyecto

```
prototipo/
├── README.md                 # Este archivo
├── main.py                   # Script principal con lógica de negocio
├── app.py                    # Aplicación Flask (versión web)
└── gui.py                    # Interfaz gráfica con Tkinter (futuro)
```

## Uso

### Opción 1: Ejecutar desde Terminal (CLI)
```bash
python main.py
```

### Opción 2: Ejecutar Aplicación Web (Flask)
```bash
python app.py
# Luego abre: http://localhost:5000
```

### Opción 3: Interfaz Gráfica (Tkinter - Futuro)
```bash
python gui.py
```

## Datos Mock Incluidos

### Estudiante
- **Nombre**: Juan Pérez
- **ID**: 2024001
- **Email**: juan.perez@universidad.edu
- **Facultad**: Ingeniería de Sistemas
- **Semestre**: 4

### Asignaturas
1. Programación Avanzada - Calificación: 4.5
2. Bases de Datos - Calificación: 4.2
3. Redes de Computadores - Calificación: 4.8
4. Ingeniería de Software - Calificación: 4.0

### Eventos Calendario
- Parcial 1 - 20 de Febrero
- Entrega Proyecto - 28 de Febrero
- Parcial 2 - 10 de Marzo

### Ubicaciones Mapa
- Edificio A: Aulas 101-110
- Edificio B: Laboratorios
- Edificio C: Biblioteca
- Edificio D: Cafetería

## Funcionalidades

### Login
- Email: `juan.perez@universidad.edu`
- Contraseña: `password`

### Componentes Disponibles
- **Inicio**: Bienvenida
- **Perfil**: Ver datos del estudiante
- **Calendario**: Ver eventos académicos
- **Mapa**: Ver ubicaciones
- **Logout**: Cerrar sesión

## API Endpoints (Flask)

```
POST   /login              - Autenticarse
GET    /inicio             - Página de inicio
GET    /perfil             - Ver perfil del estudiante
GET    /calendario         - Ver calendario
GET    /mapa              - Ver mapa
POST   /logout            - Cerrar sesión
```

## Próximos Pasos

1. ✅ Lógica de negocio (main.py) - HECHO
2. ⏳ API Flask (app.py) - EN PROGRESO
3. ⏳ Interfaz Gráfica (gui.py) - PENDIENTE
4. ⏳ Integración con BD - PENDIENTE
5. ⏳ Autenticación real - PENDIENTE

## Notas

- Todos los datos se almacenan en memoria (se pierden al cerrar)
- La contraseña es texto plano (solo para prototipo)
- No incluye validaciones de seguridad
- Diseñado para propósitos educativos

