"""
Operaciones espaciales básicas para geocomputing

Proporciona funciones fundamentales para procesamiento geoespacial
incluyendo transformaciones de coordenadas, cálculos de distancia y área.
"""

import math
from typing import Tuple, List, Dict, Any

# Constantes
DEGREES_TO_KM = 111.0  # Aproximación: 1 grado ≈ 111 km (varía con latitud)
WEB_MERCATOR_MAX_LAT = 85.06  # Latitud máxima válida para Web Mercator


def transform_coordinates(
    lat: float, 
    lon: float, 
    from_crs: str = "EPSG:4326", 
    to_crs: str = "EPSG:3857"
) -> Tuple[float, float]:
    """
    Transforma coordenadas entre sistemas de referencia.
    
    Args:
        lat: Latitud
        lon: Longitud
        from_crs: Sistema de referencia origen (por defecto WGS84)
        to_crs: Sistema de referencia destino (por defecto Web Mercator)
    
    Returns:
        Tupla (x, y) con coordenadas transformadas
    """
    # Implementación simplificada para WGS84 a Web Mercator
    if from_crs == "EPSG:4326" and to_crs == "EPSG:3857":
        # Validar límites de latitud para Web Mercator
        if abs(lat) > WEB_MERCATOR_MAX_LAT:
            raise ValueError(
                f"Latitud {lat} fuera del rango válido para Web Mercator "
                f"(±{WEB_MERCATOR_MAX_LAT} grados)"
            )
        
        x = lon * 20037508.34 / 180.0
        y = math.log(math.tan((90 + lat) * math.pi / 360.0)) / (math.pi / 180.0)
        y = y * 20037508.34 / 180.0
        return (x, y)
    
    # Por defecto retorna las coordenadas originales
    return (lon, lat)


def calculate_distance(
    point1: Tuple[float, float], 
    point2: Tuple[float, float],
    method: str = "haversine"
) -> float:
    """
    Calcula la distancia entre dos puntos geográficos.
    
    Args:
        point1: Tupla (lat, lon) del primer punto
        point2: Tupla (lat, lon) del segundo punto
        method: Método de cálculo ('haversine' o 'euclidean')
    
    Returns:
        Distancia en kilómetros
    """
    if method == "haversine":
        lat1, lon1 = point1
        lat2, lon2 = point2
        
        # Radio de la Tierra en km
        R = 6371.0
        
        # Convertir a radianes
        lat1_rad = math.radians(lat1)
        lat2_rad = math.radians(lat2)
        delta_lat = math.radians(lat2 - lat1)
        delta_lon = math.radians(lon2 - lon1)
        
        # Fórmula haversine
        a = (math.sin(delta_lat / 2) ** 2 + 
             math.cos(lat1_rad) * math.cos(lat2_rad) * 
             math.sin(delta_lon / 2) ** 2)
        c = 2 * math.asin(math.sqrt(a))
        
        return R * c
    
    elif method == "euclidean":
        # NOTA: Este método no es apropiado para coordenadas geográficas
        # ya que trata lat/lon como coordenadas planas. Use solo para 
        # coordenadas proyectadas o como aproximación burda.
        return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    
    raise ValueError(f"Método desconocido: {method}")


def calculate_area(coordinates: List[Tuple[float, float]]) -> float:
    """
    Calcula el área de un polígono definido por coordenadas.
    
    NOTA: Esta es una aproximación simplificada que no considera la naturaleza
    esférica de la Tierra. Para áreas grandes o precisión crítica, se recomienda
    usar bibliotecas especializadas como GeoPandas o Shapely.
    
    Args:
        coordinates: Lista de tuplas (lat, lon) que definen el polígono
    
    Returns:
        Área aproximada en kilómetros cuadrados
    """
    if len(coordinates) < 3:
        return 0.0
    
    # Fórmula del área usando coordenadas geográficas (aproximación)
    area = 0.0
    n = len(coordinates)
    
    for i in range(n):
        j = (i + 1) % n
        area += coordinates[i][0] * coordinates[j][1]
        area -= coordinates[j][0] * coordinates[i][1]
    
    area = abs(area) / 2.0
    
    # Convertir a km² (aproximación simplificada)
    area_km2 = area * (DEGREES_TO_KM ** 2)
    
    return area_km2


def spatial_overlay(
    layer1: List[Dict[str, Any]], 
    layer2: List[Dict[str, Any]],
    operation: str = "intersection"
) -> List[Dict[str, Any]]:
    """
    Realiza operaciones de superposición espacial entre dos capas.
    
    Args:
        layer1: Primera capa de datos espaciales
        layer2: Segunda capa de datos espaciales
        operation: Tipo de operación ('intersection', 'union', 'difference')
    
    Returns:
        Lista de features resultantes de la operación
    """
    # Implementación simplificada
    result = []
    
    if operation == "intersection":
        # Retorna elementos que están en ambas capas
        for f1 in layer1:
            for f2 in layer2:
                if _features_intersect(f1, f2):
                    result.append({
                        **f1,
                        **f2,
                        "overlay_type": "intersection"
                    })
    
    elif operation == "union":
        # Retorna todos los elementos de ambas capas
        result = layer1 + layer2
    
    elif operation == "difference":
        # Retorna elementos de layer1 que no están en layer2
        for f1 in layer1:
            intersects = any(_features_intersect(f1, f2) for f2 in layer2)
            if not intersects:
                result.append(f1)
    
    return result


def _features_intersect(feature1: Dict[str, Any], feature2: Dict[str, Any]) -> bool:
    """
    Verifica si dos features se intersectan (implementación simplificada).
    
    Args:
        feature1: Primer feature
        feature2: Segundo feature
    
    Returns:
        True si se intersectan, False en caso contrario
    """
    # Implementación básica basada en proximidad de puntos
    if "geometry" in feature1 and "geometry" in feature2:
        geom1 = feature1["geometry"]
        geom2 = feature2["geometry"]
        
        if "coordinates" in geom1 and "coordinates" in geom2:
            coords1 = geom1["coordinates"]
            coords2 = geom2["coordinates"]
            
            # Verificación simplificada
            if isinstance(coords1, (list, tuple)) and isinstance(coords2, (list, tuple)):
                if len(coords1) >= 2 and len(coords2) >= 2:
                    dist = calculate_distance(
                        (coords1[0], coords1[1]),
                        (coords2[0], coords2[1])
                    )
                    return dist < 1.0  # 1 km de umbral
    
    return False
