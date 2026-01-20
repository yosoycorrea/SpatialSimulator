# SpatialSimulator 2100 — Escenarios híbridos de inteligencias múltiples

## Objetivo
Generar escenarios del espacio híbrido (humano–IA–ecológico) en 2100, integrando datos multimodales, simulación multiagente y visualización 3D/AR/XR.

## Flujo
1. **Entradas**: humano, espacial, temporal, ecológico.
2. **Fusión semántica**: grafo de conocimiento.
3. **Dinámicas**: patrones, inequidades, riesgos.
4. **Simulación multiagente**: eficiencia, equidad, biodiversidad, memoria.
5. **Generación de escenarios**: base, disruptivo, utópico, híbrido.
6. **Evaluación**: trade-offs, XAI, auditoría ética.
7. **Visualización**: 3D/AR/XR con capas semánticas.
8. **Gobernanza**: reglas machine-readable y trazabilidad.

## Módulo Geocomputing

El módulo `/geocomputing` proporciona funcionalidades de procesamiento geoespacial para las simulaciones:

### Características principales

- **Operaciones espaciales básicas** (`spatial_ops.py`)
  - Transformación de coordenadas entre sistemas de referencia
  - Cálculo de distancias (Haversine, Euclidiana)
  - Cálculo de áreas de polígonos
  - Operaciones de superposición espacial (intersección, unión, diferencia)

- **Análisis espacial avanzado** (`analysis.py`)
  - Detección de clusters espaciales (DBSCAN)
  - Autocorrelación espacial (Índice de Moran)
  - Análisis de puntos calientes (hotspots/coldspots)

### Uso

```python
from geocomputing import (
    transform_coordinates,
    calculate_distance,
    detect_clusters,
    hotspot_analysis
)

# Transformar coordenadas
x, y = transform_coordinates(lat=19.43, lon=-99.13)

# Calcular distancia entre dos puntos
dist = calculate_distance(point1=(19.43, -99.13), point2=(20.66, -103.35))

# Detectar clusters espaciales
clusters = detect_clusters(puntos, radius=10.0, min_points=3)

# Análisis de hotspots
hotspots = hotspot_analysis(puntos, valores, radius=5.0)
```

### Ejemplo completo

Ejecuta el script de ejemplo para ver todas las funcionalidades:

```bash
python3 ejemplo_geocomputing.py
```

## Pseudocódigo

```python
def generar_escenario_2100(humano, espacial, temporal, ecologico, reglas):
    grafo = fusion_semantica(humano, espacial, temporal, ecologico)
    patrones, riesgos, inequidades = detectar_dinamicas(grafo)
    agentes = construir_agentes(["eficiencia", "equidad", "biodiversidad", "memoria"])
    negociado = simular_negociacion(agentes, patrones, restricciones=ecologico)
    futuros = generar_variantes(negociado, modos=["base","disruptivo","utopico","hibrido"])
    evaluado = evaluar_tradeoffs(futuros, reglas, xai=True, auditoria=True)
    return visualizar_xr(evaluado, overlays=["justice","risk","access","memory"])
