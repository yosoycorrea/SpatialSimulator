"""
API REST para SpatialSimulator 2100

Este módulo proporciona una API REST para el SpatialSimulator.
Endpoint principal: POST /spatialSimulator/main
"""

from typing import Dict, Any
import json


def api_handler(event: Dict[str, Any]) -> Dict[str, Any]:
    """
    Handler principal para API Gateway / Serverless
    
    Endpoint: POST /spatialSimulator/main
    
    Args:
        event: Evento con datos de entrada
        
    Returns:
        Respuesta HTTP con resultados de la simulación
    """
    try:
        # Importar la función principal
        from spatial_simulator import generar_escenario_2100
        
        # Parsear el cuerpo de la solicitud
        if isinstance(event.get('body'), str):
            body = json.loads(event['body'])
        else:
            body = event.get('body', {})
        
        # Validar entradas requeridas
        required_fields = ['humano', 'espacial', 'temporal', 'ecologico', 'reglas']
        for field in required_fields:
            if field not in body:
                return {
                    'statusCode': 400,
                    'headers': {'Content-Type': 'application/json'},
                    'body': json.dumps({
                        'error': f'Campo requerido faltante: {field}'
                    })
                }
        
        # Ejecutar simulación
        resultado = generar_escenario_2100(
            humano=body['humano'],
            espacial=body['espacial'],
            temporal=body['temporal'],
            ecologico=body['ecologico'],
            reglas=body['reglas']
        )
        
        # Retornar respuesta exitosa
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(resultado, ensure_ascii=False)
        }
        
    except Exception as e:
        # Manejo de errores
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'error': 'Error interno del servidor',
                'mensaje': str(e)
            })
        }


# Ejemplo de uso con Flask
def crear_app_flask():
    """Crea una aplicación Flask para el SpatialSimulator"""
    try:
        from flask import Flask, request, jsonify
        from spatial_simulator import generar_escenario_2100
    except ImportError:
        print("Flask no está instalado. Ejecute: pip install flask")
        return None
    
    app = Flask(__name__)
    
    @app.route('/spatialSimulator/main', methods=['POST'])
    def main_endpoint():
        """Endpoint principal del SpatialSimulator"""
        try:
            data = request.get_json()
            
            # Validar entrada
            if not data:
                return jsonify({'error': 'No se proporcionaron datos'}), 400
            
            # Ejecutar simulación
            resultado = generar_escenario_2100(
                humano=data.get('humano', {}),
                espacial=data.get('espacial', {}),
                temporal=data.get('temporal', {}),
                ecologico=data.get('ecologico', {}),
                reglas=data.get('reglas', {})
            )
            
            return jsonify(resultado), 200
            
        except Exception as e:
            return jsonify({
                'error': 'Error al procesar la solicitud',
                'mensaje': str(e)
            }), 500
    
    @app.route('/health', methods=['GET'])
    def health_check():
        """Endpoint de verificación de salud"""
        return jsonify({
            'status': 'healthy',
            'service': 'SpatialSimulator 2100',
            'version': '1.0.0'
        }), 200
    
    return app


# Ejemplo de uso con FastAPI
def crear_app_fastapi():
    """Crea una aplicación FastAPI para el SpatialSimulator"""
    try:
        from fastapi import FastAPI, HTTPException
        from pydantic import BaseModel
        from spatial_simulator import generar_escenario_2100
    except ImportError:
        print("FastAPI no está instalado. Ejecute: pip install fastapi uvicorn")
        return None
    
    app = FastAPI(
        title="SpatialSimulator 2100 API",
        description="API para generar escenarios híbridos humano-IA-ecológico",
        version="1.0.0"
    )
    
    class SimulationRequest(BaseModel):
        humano: dict
        espacial: dict
        temporal: dict
        ecologico: dict
        reglas: dict
    
    @app.post("/spatialSimulator/main")
    async def main_endpoint(request: SimulationRequest):
        """Endpoint principal del SpatialSimulator"""
        try:
            resultado = generar_escenario_2100(
                humano=request.humano,
                espacial=request.espacial,
                temporal=request.temporal,
                ecologico=request.ecologico,
                reglas=request.reglas
            )
            return resultado
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    @app.get("/health")
    async def health_check():
        """Endpoint de verificación de salud"""
        return {
            "status": "healthy",
            "service": "SpatialSimulator 2100",
            "version": "1.0.0"
        }
    
    return app


if __name__ == "__main__":
    print("Ejemplo de uso de la API:")
    print("\n1. Con Flask:")
    print("   flask_app = crear_app_flask()")
    print("   flask_app.run(host='0.0.0.0', port=5000)")
    print("\n2. Con FastAPI:")
    print("   fastapi_app = crear_app_fastapi()")
    print("   uvicorn api:fastapi_app --host 0.0.0.0 --port 8000")
    print("\n3. Ejemplo de solicitud:")
    print("""
    curl -X POST http://localhost:5000/spatialSimulator/main \\
      -H "Content-Type: application/json" \\
      -d '{
        "humano": {"poblacion": 10000000, "diversidad_cultural": 0.8},
        "espacial": {"area_km2": 50000, "conectividad": 0.7},
        "temporal": {"horizonte": "2100"},
        "ecologico": {"biodiversidad_perdida": 0.3, "temperatura_aumento": 1.8},
        "reglas": {"min_sostenibilidad": 0.5, "min_equidad": 0.5}
      }'
    """)
