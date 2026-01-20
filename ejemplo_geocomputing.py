#!/usr/bin/env python3
"""
Ejemplo de uso del módulo geocomputing para SpatialSimulator 2100

Este script demuestra las capacidades principales del módulo de geocomputing.
"""

import sys
import os

# Agregar el directorio raíz al path para importar el módulo
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from geocomputing import (
    transform_coordinates,
    calculate_distance,
    calculate_area,
    spatial_overlay,
    detect_clusters,
    spatial_autocorrelation,
    hotspot_analysis
)


def ejemplo_transformacion_coordenadas():
    """Ejemplo de transformación de coordenadas."""
    print("=" * 60)
    print("1. TRANSFORMACIÓN DE COORDENADAS")
    print("=" * 60)
    
    # Coordenadas de ejemplo (Ciudad de México)
    lat, lon = 19.4326, -99.1332
    print(f"Coordenadas originales (WGS84): lat={lat}, lon={lon}")
    
    # Transformar a Web Mercator
    x, y = transform_coordinates(lat, lon)
    print(f"Coordenadas transformadas (Web Mercator): x={x:.2f}, y={y:.2f}")
    print()


def ejemplo_calculo_distancia():
    """Ejemplo de cálculo de distancias."""
    print("=" * 60)
    print("2. CÁLCULO DE DISTANCIAS")
    print("=" * 60)
    
    # Puntos de ejemplo
    cdmx = (19.4326, -99.1332)  # Ciudad de México
    guadalajara = (20.6597, -103.3496)  # Guadalajara
    
    print(f"Ciudad de México: {cdmx}")
    print(f"Guadalajara: {guadalajara}")
    
    # Calcular distancia con método haversine
    dist = calculate_distance(cdmx, guadalajara, method="haversine")
    print(f"Distancia (Haversine): {dist:.2f} km")
    print()


def ejemplo_calculo_area():
    """Ejemplo de cálculo de área."""
    print("=" * 60)
    print("3. CÁLCULO DE ÁREA")
    print("=" * 60)
    
    # Polígono de ejemplo (aproximadamente un cuadrado de 1 grado)
    poligono = [
        (19.0, -99.0),
        (20.0, -99.0),
        (20.0, -98.0),
        (19.0, -98.0)
    ]
    
    print(f"Polígono con {len(poligono)} vértices")
    area = calculate_area(poligono)
    print(f"Área aproximada: {area:.2f} km²")
    print()


def ejemplo_deteccion_clusters():
    """Ejemplo de detección de clusters espaciales."""
    print("=" * 60)
    print("4. DETECCIÓN DE CLUSTERS ESPACIALES")
    print("=" * 60)
    
    # Puntos de ejemplo distribuidos en grupos
    puntos = [
        # Cluster 1 (zona centro)
        (19.43, -99.13),
        (19.44, -99.14),
        (19.42, -99.12),
        (19.45, -99.13),
        # Cluster 2 (zona norte)
        (19.50, -99.10),
        (19.51, -99.11),
        (19.49, -99.09),
        # Punto aislado
        (19.30, -99.30)
    ]
    
    print(f"Analizando {len(puntos)} puntos...")
    clusters = detect_clusters(puntos, radius=10.0, min_points=3)
    
    print(f"Clusters detectados: {len(clusters)}")
    for i, cluster in enumerate(clusters):
        print(f"  Cluster {i+1}: {len(cluster)} puntos - índices {cluster}")
    print()


def ejemplo_autocorrelacion():
    """Ejemplo de autocorrelación espacial."""
    print("=" * 60)
    print("5. AUTOCORRELACIÓN ESPACIAL (Índice de Moran)")
    print("=" * 60)
    
    # Puntos con valores asociados
    puntos = [
        (19.40, -99.10),
        (19.41, -99.11),
        (19.42, -99.12),
        (19.43, -99.13),
        (19.44, -99.14)
    ]
    
    # Valores con patrón espacial (valores altos cerca entre sí)
    valores = [10.0, 12.0, 15.0, 14.0, 11.0]
    
    print(f"Analizando {len(puntos)} puntos con valores asociados...")
    moran_i = spatial_autocorrelation(puntos, valores, method="moran")
    
    print(f"Índice de Moran I: {moran_i:.4f}")
    if moran_i > 0:
        print("  → Autocorrelación positiva (valores similares agrupados)")
    elif moran_i < 0:
        print("  → Autocorrelación negativa (valores disímiles agrupados)")
    else:
        print("  → Sin autocorrelación espacial")
    print()


def ejemplo_hotspots():
    """Ejemplo de análisis de puntos calientes."""
    print("=" * 60)
    print("6. ANÁLISIS DE PUNTOS CALIENTES (HOTSPOTS)")
    print("=" * 60)
    
    # Puntos con valores de intensidad
    puntos = [
        (19.40, -99.10),
        (19.41, -99.11),
        (19.42, -99.12),
        (19.43, -99.13),
        (19.44, -99.14),
        (19.50, -99.20),
        (19.51, -99.21)
    ]
    
    # Valores de intensidad (simulando temperatura, densidad, etc.)
    valores = [25.0, 28.0, 30.0, 29.0, 27.0, 15.0, 16.0]
    
    print(f"Analizando {len(puntos)} puntos...")
    hotspots = hotspot_analysis(puntos, valores, radius=10.0)
    
    print(f"Hotspots/Coldspots detectados: {len(hotspots)}")
    for hs in hotspots:
        tipo = "CALIENTE" if hs["type"] == "hot" else "FRÍO"
        print(f"  Punto {hs['index']} ({tipo}):")
        print(f"    Coordenadas: {hs['coordinates']}")
        print(f"    Z-score: {hs['z_score']:.2f}")
        print(f"    Confianza: {hs['confidence']}")
    print()


def ejemplo_overlay():
    """Ejemplo de superposición espacial."""
    print("=" * 60)
    print("7. SUPERPOSICIÓN ESPACIAL")
    print("=" * 60)
    
    # Dos capas de ejemplo
    capa1 = [
        {"id": 1, "geometry": {"coordinates": [19.43, -99.13]}, "tipo": "parque"},
        {"id": 2, "geometry": {"coordinates": [19.44, -99.14]}, "tipo": "plaza"}
    ]
    
    capa2 = [
        {"id": 3, "geometry": {"coordinates": [19.43, -99.13]}, "tipo": "estación"},
        {"id": 4, "geometry": {"coordinates": [19.50, -99.20]}, "tipo": "mercado"}
    ]
    
    print(f"Capa 1: {len(capa1)} features")
    print(f"Capa 2: {len(capa2)} features")
    
    # Operación de intersección
    resultado = spatial_overlay(capa1, capa2, operation="intersection")
    print(f"Intersección: {len(resultado)} features")
    
    # Operación de unión
    resultado_union = spatial_overlay(capa1, capa2, operation="union")
    print(f"Unión: {len(resultado_union)} features")
    print()


def main():
    """Ejecuta todos los ejemplos."""
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "  GEOCOMPUTING - SpatialSimulator 2100".center(58) + "║")
    print("║" + "  Ejemplos de funcionalidades geocomputacionales".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "═" * 58 + "╝")
    print("\n")
    
    try:
        ejemplo_transformacion_coordenadas()
        ejemplo_calculo_distancia()
        ejemplo_calculo_area()
        ejemplo_deteccion_clusters()
        ejemplo_autocorrelacion()
        ejemplo_hotspots()
        ejemplo_overlay()
        
        print("=" * 60)
        print("✓ Todos los ejemplos ejecutados exitosamente")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ Error durante la ejecución: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
