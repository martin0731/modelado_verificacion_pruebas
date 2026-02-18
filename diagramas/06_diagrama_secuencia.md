# Diagrama de Secuencia

## Secuencia 1: Login

```mermaid
sequenceDiagram
    actor Estudiante
    participant UI
    participant Backend
    participant BD
    
    Estudiante->>UI: Ingresa email y password
    UI->>Backend: POST /login
    Backend->>BD: Buscar usuario
    BD-->>Backend: Usuario encontrado
    Backend->>Backend: Validar contraseña
    Backend-->>UI: Token JWT
    UI->>UI: Guardar token
    UI-->>Estudiante: Ir a Dashboard
```

## Secuencia 2: Ver Perfil

```mermaid
sequenceDiagram
    actor Estudiante
    participant UI
    participant Backend
    participant BD
    
    Estudiante->>UI: Click en Perfil
    UI->>Backend: GET /perfil {token}
    Backend->>BD: Select estudiante
    BD-->>Backend: Datos estudiante
    Backend->>BD: Select asignaturas
    BD-->>Backend: Asignaturas
    Backend->>BD: Select calificaciones
    BD-->>Backend: Calificaciones
    Backend-->>UI: JSON consolidado
    UI-->>Estudiante: Mostrar Perfil
```

## Secuencia 3: Ver Calendario

```mermaid
sequenceDiagram
    actor Estudiante
    participant UI
    participant Backend
    participant BD
    
    Estudiante->>UI: Click en Calendario
    UI->>Backend: GET /calendario
    Backend->>BD: Select eventos
    BD-->>Backend: Eventos
    Backend->>BD: Select horarios
    BD-->>Backend: Horarios
    Backend-->>UI: JSON eventos
    UI-->>Estudiante: Mostrar Calendario
```

## Secuencia 4: Ver Mapa

```mermaid
sequenceDiagram
    autonumber
    actor Estudiante
    participant Sistema as SistemaUniversidad
    participant JSON as Archivos JSON

    Note over Sistema, JSON: Fase de Inicialización
    Sistema->>JSON: _cargar_datos()
    JSON-->>Sistema: Carga estudiantes y ubicaciones

    Note over Estudiante, Sistema: Fase de Interacción (Sesión)
    Estudiante->>Sistema: login(email, contraseña)
    Sistema-->>Estudiante: Éxito (usuario_actual definido)

    Estudiante->>Sistema: obtener_perfil()
    Sistema-->>Estudiante: Perfil + Notas (Promedio)

    Estudiante->>Sistema: obtener_calendario()
    Sistema-->>Estudiante: Lista de Eventos

    Estudiante->>Sistema: obtener_mapa()
    Sistema-->>Estudiante: Lista de Ubicaciones

    Estudiante->>Sistema: logout()
    Sistema-->>Estudiante: Sesión cerrada (usuario_actual = None)
```

