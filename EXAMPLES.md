# Ejemplos de Uso - SpatialSimulator 2100

Este documento proporciona ejemplos prácticos de cómo usar el SpatialSimulator.

## Uso Básico

### Ejecutar simulación de ejemplo

```bash
python spatial_simulator.py
```

Este comando ejecuta una simulación con datos sintéticos y genera escenarios para el año 2100.

## Uso Programático

### Ejemplo 1: Simulación Básica

```python
from spatial_simulator import generar_escenario_2100

# Definir entradas
humano = {
    "poblacion": 10_000_000,
    "diversidad_cultural": 0.8,
    "necesidades_basicas": ["vivienda", "salud", "educacion"]
}

espacial = {
    "area_km2": 50_000,
    "conectividad": 0.7,
    "infraestructura_verde": 0.4
}

temporal = {
    "horizonte": "2100",
    "proyeccion_demografica": "crecimiento_moderado"
}

ecologico = {
    "biodiversidad_perdida": 0.3,
    "temperatura_aumento": 1.8,
    "recursos_renovables": 0.7
}

reglas = {
    "min_sostenibilidad": 0.5,
    "min_equidad": 0.5
}

# Ejecutar simulación
resultado = generar_escenario_2100(humano, espacial, temporal, ecologico, reglas)

# Acceder a resultados
print(f"Escenarios generados: {len(resultado['evaluacion']['escenarios'])}")
print(f"Mejor escenario: {resultado['evaluacion']['explicacion_xai']}")
```

### Ejemplo 2: Análisis de Trade-offs

```python
from spatial_simulator import generar_escenario_2100
import json

# ... (definir entradas como en ejemplo 1) ...

resultado = generar_escenario_2100(humano, espacial, temporal, ecologico, reglas)

# Analizar trade-offs entre escenarios
tradeoffs = resultado['evaluacion']['tradeoffs']
print("\nTrade-offs entre escenarios:")
print(json.dumps(tradeoffs, indent=2))

# Revisar auditoría ética
auditoria = resultado['evaluacion']['auditoria_etica']
print("\nRiesgos éticos identificados:")
for riesgo in auditoria['riesgos_eticos']:
    print(f"  - {riesgo}")
```

### Ejemplo 3: Usar Funciones Individuales

```python
from spatial_simulator import (
    fusion_semantica,
    detectar_dinamicas,
    construir_agentes,
    simular_negociacion
)

# Fusionar datos
grafo = fusion_semantica(humano, espacial, temporal, ecologico)
print(f"Grafo creado con {len(grafo.nodes)} nodos")

# Detectar dinámicas
patrones, riesgos, inequidades = detectar_dinamicas(grafo)
print(f"\nPatrones: {patrones}")
print(f"Riesgos: {riesgos}")
print(f"Inequidades: {inequidades}")

# Construir agentes
agentes = construir_agentes(["eficiencia", "equidad", "biodiversidad", "memoria"])
print(f"\nAgentes creados: {[a.nombre for a in agentes]}")

# Simular negociación
negociado = simular_negociacion(agentes, patrones, restricciones=ecologico)
print(f"\nConsensos alcanzados: {len(negociado['consensos'])}")
```

### Ejemplo 4: Visualización XR

```python
from spatial_simulator import generar_escenario_2100
import json

resultado = generar_escenario_2100(humano, espacial, temporal, ecologico, reglas)

# Obtener configuración de visualización
viz = resultado['visualizacion']

print("Configuración XR:")
print(f"  Tipo: {viz['tipo']}")
print(f"  Escenarios: {len(viz['escenarios'])}")
print(f"  Capas semánticas: {list(viz['capas_semanticas'].keys())}")

# Exportar para motor de visualización 3D/AR
with open('escenarios_xr.json', 'w', encoding='utf-8') as f:
    json.dump(viz, f, indent=2, ensure_ascii=False)

print("\nConfiguración exportada a 'escenarios_xr.json'")
```

### Ejemplo 5: Escenario Personalizado

```python
from spatial_simulator import generar_variantes, construir_agentes, simular_negociacion

# Crear agentes personalizados
agentes_custom = construir_agentes(["eficiencia", "memoria"])

# Simular con restricciones específicas
restricciones_custom = {
    "max_uso_suelo": 0.6,
    "min_areas_protegidas": 0.3,
    "max_densidad_urbana": 15000
}

negociado = simular_negociacion(
    agentes_custom, 
    patrones=["urbanizacion_rapida"], 
    restricciones=restricciones_custom
)

# Generar solo escenarios específicos
escenarios = generar_variantes(negociado, modos=["base", "hibrido"])

for esc in escenarios:
    print(f"\nEscenario {esc.modo}:")
    print(f"  {esc.descripcion}")
    print(f"  Métricas: {esc.metricas}")
    print(f"  Recomendaciones: {esc.recomendaciones}")
```

## Estructura de Datos

### Entrada: Datos Humanos
```python
humano = {
    "poblacion": int,                    # Población total
    "diversidad_cultural": float,        # 0.0 - 1.0
    "necesidades_basicas": List[str],    # Lista de necesidades
    "desigualdad_recursos": float        # 0.0 - 1.0 (opcional)
}
```

### Entrada: Datos Espaciales
```python
espacial = {
    "area_km2": float,                   # Área en km²
    "conectividad": float,               # 0.0 - 1.0
    "infraestructura_verde": float,      # 0.0 - 1.0
    "acceso_desigual": bool             # True/False (opcional)
}
```

### Entrada: Datos Temporales
```python
temporal = {
    "horizonte": str,                    # Ej: "2100"
    "proyeccion_demografica": str,       # Descripción textual
    "tendencias_climaticas": str         # Descripción textual (opcional)
}
```

### Entrada: Datos Ecológicos
```python
ecologico = {
    "biodiversidad_perdida": float,      # 0.0 - 1.0
    "temperatura_aumento": float,        # Grados Celsius
    "recursos_renovables": float,        # 0.0 - 1.0
    "capacidad_carga": float            # 0.0 - 1.0 (opcional)
}
```

### Entrada: Reglas de Gobernanza
```python
reglas = {
    "min_sostenibilidad": float,         # 0.0 - 1.0
    "min_equidad": float,                # 0.0 - 1.0
    "max_temperatura": float,            # Grados Celsius (opcional)
    "preservacion_biodiversidad": bool   # True/False (opcional)
}
```

### Salida: Estructura de Resultados
```python
resultado = {
    "version": str,                      # Versión del simulador
    "timestamp": str,                    # ISO 8601 timestamp
    "visualizacion": {
        "tipo": str,
        "escenarios": List[Dict],
        "capas_semanticas": Dict,
        "interactividad": Dict
    },
    "evaluacion": {
        "escenarios": List[Dict],
        "tradeoffs": Dict,
        "explicacion_xai": str,
        "auditoria_etica": Dict
    },
    "grafo_conocimiento": Dict,
    "dinamicas": {
        "patrones": List[str],
        "riesgos": List[str],
        "inequidades": List[str]
    },
    "gobernanza": Dict
}
```

## Casos de Uso Avanzados

### Integración con API REST

```python
from flask import Flask, request, jsonify
from spatial_simulator import generar_escenario_2100

app = Flask(__name__)

@app.route('/api/v1/simular', methods=['POST'])
def simular():
    data = request.json
    
    resultado = generar_escenario_2100(
        humano=data['humano'],
        espacial=data['espacial'],
        temporal=data['temporal'],
        ecologico=data['ecologico'],
        reglas=data['reglas']
    )
    
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
```

### Procesamiento por Lotes

```python
from spatial_simulator import generar_escenario_2100
import json

# Cargar múltiples configuraciones
with open('configuraciones.json', 'r') as f:
    configs = json.load(f)

resultados = []
for config in configs:
    resultado = generar_escenario_2100(
        humano=config['humano'],
        espacial=config['espacial'],
        temporal=config['temporal'],
        ecologico=config['ecologico'],
        reglas=config['reglas']
    )
    resultados.append(resultado)

# Guardar resultados
with open('resultados_batch.json', 'w', encoding='utf-8') as f:
    json.dump(resultados, f, indent=2, ensure_ascii=False)
```

## Notas

- Todos los valores numéricos de métricas están normalizados entre 0.0 y 1.0
- Los escenarios se generan en el orden: base, disruptivo, utópico, híbrido
- La explicabilidad XAI está activada por defecto
- La auditoría ética verifica cumplimiento de reglas de gobernanza
- Los overlays de visualización son: justice, risk, access, memory
