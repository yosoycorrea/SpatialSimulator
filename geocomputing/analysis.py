"""
Análisis espacial avanzado para geocomputing

Proporciona funciones de análisis espacial incluyendo detección de clusters,
autocorrelación espacial y análisis de puntos calientes.
"""

import math
from typing import List, Tuple, Dict, Any
from .spatial_ops import calculate_distance


def detect_clusters(
    points: List[Tuple[float, float]], 
    radius: float = 1.0,
    min_points: int = 3
) -> List[List[int]]:
    """
    Detecta clusters espaciales usando un algoritmo simplificado tipo DBSCAN.
    
    Args:
        points: Lista de tuplas (lat, lon) representando puntos
        radius: Radio de búsqueda en kilómetros
        min_points: Número mínimo de puntos para formar un cluster
    
    Returns:
        Lista de clusters, donde cada cluster es una lista de índices de puntos
    """
    n = len(points)
    visited = [False] * n
    clusters = []
    noise = []
    
    for i in range(n):
        if visited[i]:
            continue
        
        visited[i] = True
        neighbors = _get_neighbors(points, i, radius)
        
        if len(neighbors) < min_points:
            noise.append(i)
        else:
            cluster = []
            _expand_cluster(points, i, neighbors, cluster, visited, radius, min_points)
            clusters.append(cluster)
    
    return clusters


def _get_neighbors(
    points: List[Tuple[float, float]], 
    index: int, 
    radius: float
) -> List[int]:
    """
    Obtiene los vecinos de un punto dentro de un radio dado.
    
    Args:
        points: Lista de puntos
        index: Índice del punto central
        radius: Radio de búsqueda en km
    
    Returns:
        Lista de índices de puntos vecinos
    """
    neighbors = []
    for i, point in enumerate(points):
        if i != index:
            dist = calculate_distance(points[index], point)
            if dist <= radius:
                neighbors.append(i)
    return neighbors


def _expand_cluster(
    points: List[Tuple[float, float]],
    index: int,
    neighbors: List[int],
    cluster: List[int],
    visited: List[bool],
    radius: float,
    min_points: int
) -> None:
    """
    Expande un cluster agregando puntos vecinos.
    
    Args:
        points: Lista de puntos
        index: Índice del punto central
        neighbors: Lista de vecinos iniciales
        cluster: Cluster a expandir
        visited: Lista de puntos visitados
        radius: Radio de búsqueda
        min_points: Mínimo de puntos para cluster
    """
    cluster.append(index)
    
    i = 0
    while i < len(neighbors):
        neighbor = neighbors[i]
        
        if not visited[neighbor]:
            visited[neighbor] = True
            new_neighbors = _get_neighbors(points, neighbor, radius)
            
            if len(new_neighbors) >= min_points:
                neighbors.extend(new_neighbors)
        
        if neighbor not in cluster:
            cluster.append(neighbor)
        
        i += 1


def spatial_autocorrelation(
    points: List[Tuple[float, float]], 
    values: List[float],
    method: str = "moran"
) -> float:
    """
    Calcula la autocorrelación espacial (Índice de Moran).
    
    Args:
        points: Lista de coordenadas (lat, lon)
        values: Valores asociados a cada punto
        method: Método de cálculo ('moran' o 'geary')
    
    Returns:
        Índice de autocorrelación espacial
    """
    if len(points) != len(values) or len(points) < 2:
        return 0.0
    
    n = len(points)
    mean_value = sum(values) / n
    
    if method == "moran":
        # Índice de Moran I
        numerator = 0.0
        denominator = 0.0
        w_sum = 0.0
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    # Peso basado en distancia inversa
                    dist = calculate_distance(points[i], points[j])
                    w_ij = 1.0 / (dist + 0.1)  # +0.1 para evitar división por cero
                    
                    numerator += w_ij * (values[i] - mean_value) * (values[j] - mean_value)
                    w_sum += w_ij
        
        for i in range(n):
            denominator += (values[i] - mean_value) ** 2
        
        if denominator == 0 or w_sum == 0:
            return 0.0
        
        moran_i = (n / w_sum) * (numerator / denominator)
        return moran_i
    
    return 0.0


def hotspot_analysis(
    points: List[Tuple[float, float]], 
    values: List[float],
    radius: float = 5.0
) -> List[Dict[str, Any]]:
    """
    Identifica puntos calientes (hotspots) y fríos (coldspots) estadísticamente significativos.
    
    Args:
        points: Lista de coordenadas (lat, lon)
        values: Valores de intensidad para cada punto
        radius: Radio de influencia en km
    
    Returns:
        Lista de diccionarios con información de hotspots
    """
    if len(points) != len(values) or len(points) == 0:
        return []
    
    n = len(points)
    mean_value = sum(values) / n
    std_value = math.sqrt(sum((v - mean_value) ** 2 for v in values) / n)
    
    if std_value == 0:
        return []
    
    hotspots = []
    
    for i in range(n):
        # Calcular estadístico local
        local_sum = 0.0
        local_count = 0
        
        for j in range(n):
            dist = calculate_distance(points[i], points[j])
            if dist <= radius:
                local_sum += values[j]
                local_count += 1
        
        if local_count > 0:
            local_mean = local_sum / local_count
            z_score = (local_mean - mean_value) / std_value
            
            # Clasificar como hotspot o coldspot
            if abs(z_score) > 1.96:  # 95% de confianza
                hotspot_type = "hot" if z_score > 0 else "cold"
                hotspots.append({
                    "index": i,
                    "coordinates": points[i],
                    "value": values[i],
                    "local_mean": local_mean,
                    "z_score": z_score,
                    "type": hotspot_type,
                    "confidence": "high" if abs(z_score) > 2.58 else "medium"
                })
    
    return hotspots
