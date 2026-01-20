# SpatialSimulator 2026 — Escenarios híbridos de inteligencias múltiples

## Objetivo
Generar escenarios del espacio híbrido (humano–IA–ecológico), integrando datos multimodales, simulación multiagente y visualización 3D/AR/XR.

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/yosoycorrea/SpatialSimulator.git
cd SpatialSimulator

# No se requieren dependencias adicionales
# El simulador usa solo la biblioteca estándar de Python
```

## Uso Rápido

```bash
# Ejecutar simulación de ejemplo
python spatial_simulator.py
```

## Flujo
1. **Entradas**: humano, espacial, temporal, ecológico.
2. **Fusión semántica**: grafo de conocimiento.
3. **Dinámicas**: patrones, inequidades, riesgos.
4. **Simulación multiagente**: eficiencia, equidad, biodiversidad, memoria.
5. **Generación de escenarios**: base, disruptivo, utópico, híbrido.
6. **Evaluación**: trade-offs, XAI, auditoría ética.
7. **Visualización**: 3D/AR/XR con capas semánticas.
8. **Gobernanza**: reglas machine-readable y trazabilidad.

## Implementación

### Función Principal: `/spatialSimulator/main`

La función `generar_escenario_2100()` es el punto de entrada principal (main key) que orquesta todo el flujo:

```python
from spatial_simulator import generar_escenario_2100

resultado = generar_escenario_2100(humano, espacial, temporal, ecologico, reglas)
```

### Componentes Implementados

- ✅ `fusion_semantica()` - Fusión de datos multimodales en grafo de conocimiento
- ✅ `detectar_dinamicas()` - Detección de patrones, riesgos e inequidades
- ✅ `construir_agentes()` - Construcción de agentes multiobjetivo
- ✅ `simular_negociacion()` - Simulación multi-agente con restricciones
- ✅ `generar_variantes()` - Generación de 4 escenarios futuros
- ✅ `evaluar_tradeoffs()` - Evaluación con XAI y auditoría ética
- ✅ `visualizar_xr()` - Preparación para visualización 3D/AR/XR

### API REST

El simulador puede usarse como servicio web:

```bash
# Con Flask
python -c "from api import crear_app_flask; app = crear_app_flask(); app.run()"

# Endpoint: POST /spatialSimulator/main
```

Ver `api.py` y `EXAMPLES.md` para más detalles.

## Ejemplos de Uso

### Ejemplo Básico

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

Ver `EXAMPLES.md` para más ejemplos detallados.

## Arquitectura

```python
def generar_escenario_(humano, espacial, temporal, ecologico, reglas):
    grafo = fusion_semantica(humano, espacial, temporal, ecologico)
    patrones, riesgos, inequidades = detectar_dinamicas(grafo)
    agentes = construir_agentes(["eficiencia", "equidad", "biodiversidad", "memoria"])
    negociado = simular_negociacion(agentes, patrones, restricciones=ecologico)
    futuros = generar_variantes(negociado, modos=["base","disruptivo","utopico","hibrido"])
    evaluado = evaluar_tradeoffs(futuros, reglas, xai=True, auditoria=True)
    return visualizar_xr(evaluado, overlays=["justice","risk","access","memory"])





v1.2

Tu texto ya está muy sólido. Solo voy a:

Mantener todo tu contenido.  
Asegurar que todas las referencias al futuro extremo digan 2026 (no 2100).

Te lo dejo limpio y coherente:

SpatialSimulator 2026 — Escenarios híbridos de inteligencias múltiples

Objetivo
Generar escenarios del espacio híbrido (humano–IA–ecológico), integrando datos multimodales, simulación multiagente y visualización 3D/AR/XR.

Flujo
Entradas: humano, espacial, temporal, ecológico.  
Fusión semántica: grafo de conocimiento.  
Dinámicas: patrones, inequidades, riesgos.  
Simulación multiagente: eficiencia, equidad, biodiversidad, memoria.  
Generación de escenarios: base, disruptivo, utópico, híbrido.  
Evaluación: trade-offs, XAI, auditoría ética.  
Visualización: 3D/AR/XR con capas semánticas.  
Gobernanza: reglas machine-readable y trazabilidad.

Pseudocódigo

def generar_escenario_(humano, espacial, temporal, ecologico, reglas):
    grafo = fusion_semantica(humano, espacial, temporal, ecologico)
    patrones, riesgos, inequidades = detectar_dinamicas(grafo)
    agentes = construir_agentes(["eficiencia", "equidad", "biodiversidad", "memoria"])
    negociado = simular_negociacion(agentes, patrones, restricciones=ecologico)
    futuros = generar_variantes(negociado, modos=["base","disruptivo","utopico","hibrido"])
    evaluado = evaluar_tradeoffs(futuros, reglas, xai=True, auditoria=True)
    return visualizar_xr(evaluado, overlays=["justice","risk","access","memory"])

Copyright 2026 Juan Antonio Pulido Correa  

Licensed under the Apache License, Version 2.0 (the "License");  
you may not use this file except in compliance with the License.  
You may obtain a copy of the License at:

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software  
distributed under the License is distributed on an "AS IS" BASIS,  
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
See the License for the specific language governing permissions and  
limitations under the License.

Si quieres, después puedo ayudarte a añadir una mini sección arriba tipo “Contexto: por qué 2026 es el punto de partida de SpatialSimulator”.


Copyright 2026 Juan Antonio Pulido Correa

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

