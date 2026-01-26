"""
Módulo de geocomputing para SpatialSimulator 2100

Este módulo proporciona funcionalidades de procesamiento geoespacial
para simulaciones de escenarios híbridos.
"""

from .spatial_ops import (
    transform_coordinates,
    calculate_distance,
    calculate_area,
    spatial_overlay
)

from .analysis import (
    detect_clusters,
    spatial_autocorrelation,
    hotspot_analysis
)

__version__ = "0.1.0"
__all__ = [
    "transform_coordinates",
    "calculate_distance", 
    "calculate_area",
    "spatial_overlay",
    "detect_clusters",
    "spatial_autocorrelation",
    "hotspot_analysis"
]
