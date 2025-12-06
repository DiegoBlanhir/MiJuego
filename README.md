🚀 SPACE FLIGHT

Un emocionante juego de acción desarrollado en Python con Pygame. ¡Evita enemigos, dispara balas y recoge monedas mientras compites por la mejor puntuación!

## 📋 Descripción

**SPACE FLIGHT** es un juego arcade clásico donde controlas una nave espacial que debe navegar a través de oleadas de enemigos. Dispara para destruirlos, recoge monedas para ganar puntos y alcanza el TOP 3 de las mejores puntuaciones.

## 🎮 Características

### Mecánicas de Juego
- ✅ **Control de jugador de 4 direcciones** con animación suave
- ✅ **Sistema de combate** - dispara con ESPACIO para eliminar enemigos
- ✅ **Colecciones de monedas** - +5 puntos por moneda
- ✅ **Destrucción de enemigos** - +10 puntos por enemigo eliminado
- ✅ **Dificultad dinámica** - enemigos y monedas respawnean continuamente

### Características de Presentación
- ✅ **Pantalla de inicio** con instrucciones de juego
- ✅ **Pantalla final (Game Over)** con puntuación actual
- ✅ **Sistema de TOP 3** con registro de nombres
- ✅ **Gráficos mejorados** con enemigos, balas y monedas estilizados
- ✅ **Fondo dinámico** que se desplaza constantemente

### Sistema de Puntuaciones
- ✅ **Base de datos SQLite** para persistencia de datos
- ✅ **Registro automático de puntuaciones** en TOP 3
- ✅ **Sistema de nombres** - pide nombre solo si entra en TOP 3
- ✅ **Visualización de mejores puntuaciones** al terminar

## 🛠️ Requisitos

- Python >= 3.9
- pygame==2.6.1
- sqlite3 (incluido en Python)

## 📦 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/space-flight.git
cd space-flight
```

### 2. Crear entorno virtual (recomendado)
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS
```

### 3. Instalar dependencias
```bash
pip install pygame==2.6.1
```

## 🎯 Cómo Jugar

### Controles
| Acción | Tecla |
|--------|-------|
| Mover Arriba | ⬆️ |
| Mover Abajo | ⬇️ |
| Mover Izquierda | ⬅️ |
| Mover Derecha | ➡️ |
| Disparar | ESPACIO |
| Salir | ESC o cerrar ventana |

### Objetivos
1. 🎯 **Evita los enemigos rojos** - Te eliminan al contacto
2. 💥 **Dispara a los enemigos** - +10 puntos por cada uno
3. 💰 **Recoge las monedas doradas** - +5 puntos por cada una
4. 🏆 **Entra al TOP 3** - Tu nombre quedará registrado

### Mecánica de Juego
- Los enemigos descienden constantemente desde la parte superior
- Las monedas caen más lentamente que los enemigos
- Si un enemigo te toca, ¡Game Over!
- Las balas eliminan enemigos y desaparecen
- Todo se regenera automáticamente

## 🚀 Ejecución

```bash
python main.py
```

## 📁 Estructura del Proyecto

```
space-flight/
├── main.py                      # Archivo principal del juego
├── database.py                  # Sistema de base de datos SQLite
├── jugador_direccional.py       # Control y animación del jugador
├── enemigos.py                  # Lógica y gráficos de enemigos
├── balas.py                     # Lógica y gráficos de balas
├── monedas.py                   # Lógica y gráficos de monedas
├── fondo.py                     # Sistema de fondo dinámico
├── colisiones.py                # Detección de colisiones
├── personaje_direcciones.png    # Sprite del personaje
├── fondo.png                    # Imagen de fondo
├── puntuaciones.db              # Base de datos (se crea automáticamente)
└── README.md                    # Este archivo
```

## 🎨 Especificaciones Visuales

### Resolución
- **Ancho:** 800 píxeles
- **Alto:** 600 píxeles
- **FPS:** 60 fotogramas por segundo

### Diseño de Enemigos
- Círculos rojos con ojos y boca
- Radio: 20 píxeles
- Velocidad: 5 píxeles/fotograma

### Diseño de Balas
- Rectángulos amarillos con punta naranja
- Tamaño: 5x10 píxeles
- Velocidad: 10 píxeles/fotograma hacia arriba

### Diseño de Monedas
- Círculos dorados con efecto 3D
- Radio: 10 píxeles
- Velocidad: 3 píxeles/fotograma hacia abajo

### Personaje del Jugador
- Sprite escalado a 64x64 píxeles
- Animación por dirección
- Velocidad de movimiento: 4 píxeles/fotograma

## 💾 Base de Datos

### Tabla: `puntuaciones`
```sql
CREATE TABLE puntuaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    puntos INTEGER NOT NULL
);
```

### Funciones Disponibles
- `crear_base_datos()` - Inicializa la BD
- `guardar_puntuacion(nombre, puntos)` - Guarda una puntuación
- `obtener_mejores_puntuaciones(limite)` - Obtiene TOP puntuaciones
- `es_top_3(puntos)` - Verifica si está en TOP 3

## 📊 Sistema de Puntuación

| Acción | Puntos |
|--------|--------|
| Enemigo destruido | +10 |
| Moneda recogida | +5 |
| Contacto con enemigo | Game Over |

## 🎓 Tecnologías Utilizadas

- **Pygame 2.6.1** - Motor gráfico 2D
- **Python 3.11** - Lenguaje de programación
- **SQLite3** - Base de datos

## 🐛 Solución de Problemas

### El sprite se ve cortado
- Verifica que `personaje_direcciones.png` esté en la carpeta del juego
- El juego usará un sprite azul como alternativa si no encuentra la imagen

### El fondo no se carga
- Verifica que `fondo.png` esté en la misma carpeta que `main.py`
- El juego funcionará sin fondo si no está disponible

### pygame no está instalado
```bash
pip install pygame==2.6.1
```

### Error de base de datos
- Elimina el archivo `puntuaciones.db`
- El juego creará uno nuevo automáticamente en la siguiente ejecución


## 📝 Notas de Desarrollo

El juego sigue una arquitectura modular donde cada sistema (jugador, enemigos, balas, monedas, colisiones) está en su propio módulo, facilitando el mantenimiento y la expansión.

**¡Diviértete jugando SPACE FLIGHT! 🚀✨**
