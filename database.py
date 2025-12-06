import sqlite3
import os

# Ruta de la base de datos
DB_PATH = os.path.join(os.path.dirname(__file__), "puntuaciones.db")

def crear_base_datos():
    """Crea la base de datos si no existe"""
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS puntuaciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            puntos INTEGER NOT NULL
        )
    ''')
    
    conexion.commit()
    conexion.close()

def guardar_puntuacion(nombre, puntos):
    """Guarda una puntuación en la base de datos"""
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    
    cursor.execute("INSERT INTO puntuaciones (nombre, puntos) VALUES (?, ?)", (nombre, puntos))
    
    conexion.commit()
    conexion.close()

def obtener_mejores_puntuaciones(limite=5):
    """Obtiene las mejores puntuaciones de la base de datos"""
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    
    cursor.execute("SELECT nombre, puntos FROM puntuaciones ORDER BY puntos DESC LIMIT ?", (limite,))
    resultados = cursor.fetchall()
    
    conexion.close()
    return resultados

def obtener_puntuacion_maxima():
    """Obtiene la puntuación máxima registrada"""
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    
    cursor.execute("SELECT MAX(puntos) FROM puntuaciones")
    resultado = cursor.fetchone()
    
    conexion.close()
    
    return resultado[0] if resultado[0] is not None else 0

def obtener_total_partidas():
    """Obtiene el total de partidas jugadas"""
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM puntuaciones")
    resultado = cursor.fetchone()
    
    conexion.close()
    
    return resultado[0]

def es_top_3(puntos):
    """Verifica si la puntuación está en el TOP 3"""
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM puntuaciones WHERE puntos > ?", (puntos,))
    mejor_que = cursor.fetchone()[0]
    
    conexion.close()
    
    return mejor_que < 3
