# Frontend - Gymstats

## **Descripción General**
El frontend de Gymsats está diseñado para ofrecer una interfaz de usuario intuitiva y responsiva. Permite la gestión de planificaciones, registro de ejercicios y visualización de estadísticas en tiempo real.

---

## **Características Principales**
1. **Calendario Interactivo**:
   - Navegación entre días, semanas, meses y años.
   - Visualización de planificaciones en fechas específicas.
   - Acceso rápido a detalles de cada planificación.

2. **Gestión de Planificaciones**:
   - Crear, editar y eliminar planificaciones directamente desde el calendario.
   - Añadir ejercicios personalizados a cada planificación.

3. **Seguimiento en Tiempo Real**:
   - Registrar peso, repeticiones, RPE y tiempo de descanso durante los entrenamientos.
   - Actualización automática de progreso para ejercicios y planificaciones.

4. **Visualización de Estadísticas**:
   - Gráficos dinámicos y personalizables.
   - Filtros para visualizar datos en rangos de tiempo específicos.
   - Alertas sobre entrenamiento excesivo o insuficiente.

---

## **Estructura de la Aplicación**

### **1. Página Principal**
- **Vista predeterminada**: Calendario con las planificaciones del usuario.
- **Acciones disponibles**:
  - Navegar por el calendario (días, semanas, meses, años).
  - Hacer clic en una fecha para ver, editar o eliminar la planificación correspondiente.
  - Crear una nueva planificación en fechas sin planificaciones.

### **2. Vista de Planificación**
- **Muestra**:
  - Nombre de la planificación.
  - Lista de ejercicios asociados.
  - Estado de la planificación (pendiente o completada).
- **Acciones disponibles**:
  - Editar el nombre de la planificación.
  - Añadir, editar o eliminar ejercicios de la planificación.
  - Marcar la planificación como completada.

### **3. Seguimiento de Ejercicios**
- **Muestra**:
  - Lista de ejercicios en la planificación actual.
  - Detalles de cada ejercicio (peso, repeticiones, series planificadas).
  - Progreso general de la planificación.
- **Acciones disponibles**:
  - Registrar datos en tiempo real:
    - Peso levantado.
    - Número de repeticiones.
    - Tiempo de descanso.
    - RPE.
  - Marcar series como completadas.
  - Marcar ejercicios como completados.
  - Finalizar la planificación.

### **4. Estadísticas**
- **Muestra**:
  - Gráficos personalizados basados en el historial de entrenamientos.
  - Métricas clave:
    - Peso promedio por ejercicio.
    - RPE promedio.
    - Fuerza acumulada.
    - Comparación entre planificación y ejecución.
  - Alertas y recomendaciones.
- **Acciones disponibles**:
  - Aplicar filtros por rango de fechas.
  - Alternar entre diferentes tipos de gráficos.
  - Descargar datos en formatos compatibles (opcional, dependiendo de implementación futura).

### **5. Gestión de Ejercicios**
- **Muestra**:
  - Lista de ejercicios creados por el usuario.
  - Lista inicial predefinida (si se decide incluirla).
- **Acciones disponibles**:
  - Crear nuevos ejercicios personalizados:
    - Nombre.
    - Categoría (ej. pecho, espalda, piernas, etc.).
    - Nivel de importancia (opcional).
  - Editar o eliminar ejercicios existentes.
  - Seleccionar ejercicios desde un desplegable al planificar.

---

## **Diseño de Interfaz**
- **Tema Oscuro**: Por defecto, con posibilidad de alternar a un tema claro en futuras versiones.
- **Diseño Responsivo**:
  - Adaptado para pantallas de escritorio, tabletas y dispositivos móviles.
- **Componentes Reutilizables**:
  - Modales para añadir/editar planificaciones y ejercicios.
  - Tarjetas para visualizar ejercicios y estadísticas.
  - Gráficos dinámicos integrados (librería por definir).

---

## **Escalabilidad**
El frontend está diseñado para:
- Integrar nuevas vistas o secciones sin afectar las existentes.
- Incorporar módulos adicionales para análisis avanzados o personalización.
- Facilitar la implementación de actualizaciones en el diseño o la funcionalidad.

---

## **Próximos Pasos**
- Definir la librería para gráficos dinámicos (ej. Chart.js, D3.js).
- Implementar pruebas de usabilidad en dispositivos móviles y de escritorio.
- Añadir funcionalidades futuras, como:
  - Compartir estadísticas con otros usuarios.
  - Notificaciones personalizadas.
