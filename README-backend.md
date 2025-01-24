# Backend - Gymstats

## **Descripción General**
El backend de Gymstats está construido con FastAPI para gestionar la lógica de negocio, realizar validaciones y facilitar la comunicación con el frontend. Utiliza Supabase como base de datos para garantizar una integración fluida, un almacenamiento seguro y escalable, y soporte para autenticación.

---

## **Características Principales**

### **1. Gestión de Usuarios**
- **Endpoints**:
  - Registro de nuevos usuarios.
  - Inicio de sesión (login) y cierre de sesión (logout).
  - Recuperación y cambio de contraseña.
  - Actualización de datos del perfil.
- **Validaciones**:
  - Email único y con formato válido.
  - Contraseña con al menos 8 caracteres, una mayúscula, un número y un carácter especial.
  - Tokens para autenticación (JWT o alternativa similar).
- **Sugerencias de Implementación**:
  - Usar Supabase para la autenticación nativa y encriptar contraseñas con herramientas como `bcrypt`.
  - Implementar middleware para gestionar sesiones y permisos (ej. usuario autenticado, roles).

---

### **2. Gestión de Planificaciones**
- **Endpoints**:
  - Crear nuevas planificaciones.
  - Consultar planificaciones por fecha, rango de fechas o estado.
  - Editar el nombre o estado de una planificación.
  - Eliminar planificaciones.
- **Validaciones**:
  - Cada planificación debe estar vinculada a un usuario.
  - Una planificación por día por usuario.
  - Fecha válida (no permitir fechas pasadas salvo explícito retroactivo).
- **Sugerencias de Implementación**:
  - Definir un modelo de datos para planificaciones con campos como:
    - `id`, `user_id`, `fecha`, `nombre`, `estado` (pendiente/completado).
  - Utilizar consultas parametrizadas para filtrar por usuario y fecha en Supabase.
  - Crear una capa de servicios para gestionar la lógica de negocio, evitando duplicación en controladores.

---

### **3. Gestión de Ejercicios**
- **Endpoints**:
  - Crear nuevos ejercicios.
  - Editar o eliminar ejercicios existentes.
  - Consultar ejercicios por usuario o categoría.
  - Recuperar una lista inicial de ejercicios predefinidos (si se decide incluirlos).
- **Validaciones**:
  - Nombres únicos por usuario.
  - Categoría válida (grupos musculares predefinidos).
  - Opcional: Validar nivel de importancia si se utiliza.
- **Sugerencias de Implementación**:
  - Almacenar una lista inicial de ejercicios predefinidos en una tabla separada.
  - Diseñar el modelo con campos como `id`, `user_id`, `nombre`, `categoría`, `importancia`.
  - Implementar un endpoint para que el usuario pueda clonar ejercicios predefinidos a su cuenta.

---

### **4. Seguimiento de Progreso**
- **Endpoints**:
  - Registrar datos de progreso para una planificación específica:
    - Peso utilizado.
    - Repeticiones realizadas.
    - Tiempo de descanso.
    - RPE.
  - Consultar progreso de ejercicios individuales o de una planificación completa.
  - Marcar ejercicios y planificaciones como completados.
- **Validaciones**:
  - Peso mayor a 0.
  - RPE entre 1 y 10.
  - Series y repeticiones mayores a 0.
  - Formato JSON válido para los sets.
- **Sugerencias de Implementación**:
  - Utilizar un modelo con campos como:
    - `id`, `planificacion_id`, `ejercicio_id`, `datos_set` (almacenado como JSON).
  - Implementar validaciones personalizadas para verificar la integridad de los datos JSON.
  - Usar tareas asíncronas para calcular automáticamente el progreso general de la planificación.

---

### **5. Análisis de Datos y Estadísticas**
- **Endpoints**:
  - Consultar métricas clave:
    - Peso promedio por ejercicio.
    - RPE promedio por ejercicio.
    - Fuerza acumulada total.
    - Comparación entre planificación y ejecución.
  - Alertas automáticas basadas en patrones de entrenamiento.
- **Validaciones**:
  - Fechas válidas para filtros.
  - Datos consistentes con los registros existentes.
- **Sugerencias de Implementación**:
  - Crear procedimientos almacenados en Supabase para calcular métricas complejas.
  - Utilizar librerías como `pandas` para el procesamiento avanzado de datos.
  - Implementar websockets o colas de mensajes para actualizar estadísticas en tiempo real.

---

## **Estructura de la Base de Datos**

### **1. Tabla: Usuarios**
| Campo           | Tipo          | Descripción                                  |
|------------------|---------------|----------------------------------------------|
| `id`            | UUID          | Identificador único del usuario.            |
| `password` | String        | Contraseña encriptada.                      |
| `usuario`     | String        | Nombre del usuario.                         |

### **2. Tabla: Planificaciones**
| Campo           | Tipo          | Descripción                                  |
|------------------|---------------|----------------------------------------------|
| `id`            | UUID          | Identificador único de la planificación.    |
| `id_user`       | UUID          | Relación con el usuario.                    |
| `date`         | Date          | Fecha de la planificación.                  |
| `routine_name`        | String        | Nombre de la planificación.           |
| `status`        | String        | Pendiente o completada.                     |

### **3. Tabla: Ejercicios**
| Campo           | Tipo          | Descripción                                  |
|------------------|---------------|----------------------------------------------|
| `id`            | UUID          | Identificador único del ejercicio.          |
| `name`        | String        | Nombre del ejercicio.                       |
| `category`     | String        | Grupo muscular al que afecta.               |
| `importance`   | Integer       | Nivel de aislamiento (opcional).            |

### **4. Tabla: Contenido de planificacion**
| Campo           | Tipo          | Descripción                                  |
|------------------|---------------|----------------------------------------------|
| `id`            | UUID          | Identificador único del progreso.           |
| `planificacion_id` | UUID       | Relación con la planificación.              |
| `ejercicio_id`  | UUID          | Relación con el ejercicio.                  |
| `set_detail`     | JSON          | Detalles de las series (peso, repeticiones, RPE). |

---

## **Validaciones Críticas**
1. **General**:
   - IDs deben ser válidos y existir en la base de datos.
   - Campos obligatorios no pueden ser nulos o vacíos.
2. **Usuarios**:
   - Email único y con formato válido.
   - Contraseñas encriptadas y seguras.
3. **Planificaciones**:
   - Una planificación por fecha por usuario.
   - Estado limitado a valores válidos (pendiente, completada).
4. **Progreso**:
   - Series y repeticiones mayores a 0.
   - RPE dentro del rango de 1 a 10.
   - JSON de sets válido según el esquema definido.

---

## **Escalabilidad**
El backend está diseñado para:
- Añadir nuevas funcionalidades sin afectar las existentes.
- Escalar horizontalmente mediante microservicios.
- Integrarse con servicios externos para análisis avanzados.


