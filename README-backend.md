# Backend - Gymstats

## **Descripción General**
El backend de Gymstats está desarrollado en FastAPI y utilizará Supabase como base de datos. Este componente gestiona la lógica del negocio, las validaciones y la comunicación con el frontend.

---

## **Endpoints Principales**
1. **Usuarios**:
   - Registro de nuevos usuarios.
   - Autenticación y autorización.
   - Gestión de datos del perfil.
2. **Planificaciones**:
   - Crear, editar y eliminar planificaciones.
   - Consultar planificaciones por usuario, fecha o rango de fechas.
3. **Ejercicios**:
   - Crear, editar y eliminar ejercicios.
   - Consultar ejercicios disponibles (predefinidos o personalizados).
4. **Progreso**:
   - Registrar datos de entrenamiento por serie.
   - Consultar progreso de un ejercicio o planificación específica.

---

## **Validaciones Críticas**
1. **Usuarios**:
   - Email único y formato válido.
   - Contraseñas encriptadas para seguridad.
2. **Planificaciones**:
   - Una planificación por día por usuario.
   - Validar fechas (no se pueden planificar fechas pasadas, salvo para registro retroactivo explícito).
3. **Ejercicios**:
   - Nombres únicos por usuario.
   - Validación de categorías y niveles de importancia.
4. **Datos de Progreso**:
   - RPE entre 1 y 10.
   - Series mayores a 0.
   - Validación de sets en formato JSON.

---

## **Principios de Desarrollo**
- Código modular y reutilizable siguiendo principios SOLID.
- Validaciones centralizadas para minimizar duplicación.
- Endpoints RESTful con respuestas claras y detalladas.

---

## **Base de Datos**
- Tablas principales:
  - **Usuarios**: ID, email, contraseña, nombre.
  - **Planificaciones**: ID, usuario_id, fecha, nombre, estado.
  - **Ejercicios**: ID, nombre, categoría, importancia.
  - **Progreso**: planificación_id, ejercicio_id, datos del set (JSON).
- Integración con Supabase para gestionar autenticación y almacenamiento.

---

## **Escalabilidad**
El backend está diseñado para:
- Añadir nuevos endpoints sin alterar los existentes.
- Extender las validaciones y el modelo de datos.
- Facilitar la conexión con servicios externos (ej. analíticas avanzadas).
