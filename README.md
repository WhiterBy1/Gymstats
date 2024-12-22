# Gymstats

Gymstats es una aplicación web diseñada para planificar, registrar y analizar entrenamientos de gimnasio. La aplicación permite a los usuarios personalizar sus rutinas, registrar el progreso de cada ejercicio y visualizar estadísticas detalladas para mejorar su rendimiento físico.

---

## **Tecnologías Principales**
- **Frontend**: Node.js o JavaScript Vanilla (pendiente de decisión), diseño responsivo con tema oscuro.
- **Backend**: FastAPI.
- **Base de Datos**: Supabase.
- **Análisis de Datos**: Python.

---

## **Características Principales**

### **Gestión de Planificaciones**
- **Planificación diaria** asignada a fechas específicas en un calendario.
- Cada planificación incluye:
  - **Nombre**: Definido por el usuario (ej. "Pecho y espalda", "Piernas", etc.).
  - **Estado**: Pendiente o completada.
  - **Vinculación al usuario**: Asociada al ID único del usuario.
- Solo se permite **una planificación por día**.
- **Acciones**: Crear, editar y eliminar planificaciones.

### **Gestión de Ejercicios**
- Los ejercicios tienen los siguientes atributos:
  - **Nombre**: Definido por el usuario o tomado de una lista inicial predefinida.
  - **Categoría**: Grupo muscular afectado (ej. pecho, espalda, etc.).
  - **Importancia**: Nivel de aislamiento o composición del ejercicio.
- **Acciones**:
  - Crear, editar o eliminar ejercicios.
  - Añadir ejercicios a una planificación.

### **Seguimiento de Ejercicios**
- Registro detallado durante los entrenamientos:
  - Peso utilizado.
  - Repeticiones realizadas.
  - Tiempo de descanso.
  - RPE (1-10, indicando el esfuerzo percibido).
- Autoprogreso:
  - Series completadas dentro de un ejercicio.
  - Ejercicios completados dentro de una planificación.
  - Estado de la planificación.

### **Análisis de Datos y Estadísticas**
- Visualización dinámica mediante gráficos:
  - Peso por ejercicio.
  - RPE promedio por ejercicio.
  - Fuerza acumulada total.
  - Comparación entre planificación y ejecución.
- Alertas automáticas:
  - Entrenamiento excesivo o insuficiente de un grupo muscular.
  - Anomalías en las marcas de progreso.

---

## **Validaciones Importantes**
1. **Usuarios**:
   - El email debe ser válido y único.
   - La contraseña debe cumplir con estándares mínimos (8 caracteres, incluyendo mayúsculas, números y símbolos).
2. **Planificaciones**:
   - No se pueden crear dos planificaciones en la misma fecha.
   - Cada planificación debe estar vinculada a un usuario existente.
3. **Ejercicios**:
   - Los nombres deben ser únicos por usuario.
   - Las categorías deben estar predefinidas o validadas.
4. **Contenido de los ejercicios**:
   - RPE debe estar entre 1 y 10.
   - Las series no pueden ser menores o iguales a 0.
   - JSON de los sets debe ser válido y seguir el esquema definido.
5. **General**:
   - Todos los IDs deben ser válidos y existir en la base de datos.
   - Ningún campo requerido puede estar vacío.

---
## Documentación Relacionada

- [Frontend - Detalles y Funcionalidades](README-frontend.md)
- [Backend - Detalles y Funcionalidades](README-backend.md)

Por favor, consulta estos archivos para obtener información detallada sobre cada módulo del proyecto.
---

## **Escalabilidad**
El proyecto está diseñado para ser escalable y adaptable a nuevas funcionalidades:
- Incorporar estadísticas globales de usuarios.
- Añadir nuevos campos en planificaciones o ejercicios.
- Integrar métricas avanzadas para el análisis de datos.

---
