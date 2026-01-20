"""
SpatialSimulator - Seed Data for Testing

This module provides reusable seed data for testing the spatial simulation pipeline.
It defines example inputs across all required data dimensions.

Copyright 2026 Juan Antonio Pulido Correa
Licensed under the Apache License, Version 2.0
"""


# Example human data: narratives, demographics, social signals
HUMAN_DATA = {
    "narratives": [
        {
            "id": "narrative_001",
            "description": "Community seeks green spaces for social gatherings",
            "location": "downtown_plaza",
            "priority": "high",
            "stakeholders": ["residents", "local_businesses", "city_planners"]
        },
        {
            "id": "narrative_002",
            "description": "Workers need efficient public transport routes",
            "location": "industrial_district",
            "priority": "high",
            "stakeholders": ["workers", "transport_authority", "employers"]
        },
        {
            "id": "narrative_003",
            "description": "Students require accessible learning spaces",
            "location": "university_quarter",
            "priority": "medium",
            "stakeholders": ["students", "faculty", "educational_institutions"]
        }
    ],
    "demographics": {
        "population": 150000,
        "age_distribution": {
            "0-18": 0.22,
            "19-35": 0.35,
            "36-65": 0.33,
            "65+": 0.10
        },
        "income_distribution": {
            "low": 0.25,
            "medium": 0.50,
            "high": 0.25
        },
        "mobility_patterns": {
            "walking": 0.25,
            "cycling": 0.15,
            "public_transport": 0.35,
            "private_vehicle": 0.25
        }
    },
    "social_signals": {
        "community_engagement": 0.68,
        "environmental_awareness": 0.75,
        "technology_adoption": 0.62,
        "civic_participation": 0.54
    }
}


# Example spatial data: geographic layers, infrastructure, accessibility
SPATIAL_DATA = {
    "geographic_layers": {
        "urban_zones": [
            {"id": "zone_001", "type": "residential", "area_km2": 12.5, "density": "high"},
            {"id": "zone_002", "type": "commercial", "area_km2": 5.8, "density": "medium"},
            {"id": "zone_003", "type": "industrial", "area_km2": 8.2, "density": "low"},
            {"id": "zone_004", "type": "green_space", "area_km2": 15.3, "density": "minimal"}
        ],
        "boundaries": {
            "city_limits": "POLYGON((0 0, 20 0, 20 15, 0 15, 0 0))",
            "districts": 6
        }
    },
    "infrastructure": {
        "transport_network": {
            "roads": {"total_km": 450, "avg_condition": "good"},
            "bike_lanes": {"total_km": 85, "coverage": 0.42},
            "public_transit": {
                "bus_lines": 24,
                "metro_lines": 2,
                "stations": 45
            }
        },
        "utilities": {
            "water_coverage": 0.98,
            "electricity_coverage": 0.99,
            "internet_coverage": 0.87
        },
        "public_facilities": {
            "schools": 32,
            "hospitals": 5,
            "libraries": 8,
            "parks": 23
        }
    },
    "accessibility": {
        "walkability_score": 0.72,
        "public_transport_access": 0.65,
        "green_space_access": 0.58,
        "service_proximity": 0.71
    }
}


# Example temporal data: historical patterns, temporal dynamics
TEMPORAL_DATA = {
    "historical_patterns": {
        "population_growth": {
            "2020": 142000,
            "2021": 144500,
            "2022": 146800,
            "2023": 148200,
            "2024": 149500,
            "2025": 150000
        },
        "land_use_changes": [
            {"year": 2022, "change": "residential_expansion", "area_km2": 2.1},
            {"year": 2023, "change": "green_space_creation", "area_km2": 1.5},
            {"year": 2024, "change": "commercial_development", "area_km2": 0.8}
        ],
        "mobility_trends": {
            "2020": {"car": 0.45, "transit": 0.30, "active": 0.25},
            "2023": {"car": 0.35, "transit": 0.35, "active": 0.30},
            "2025": {"car": 0.25, "transit": 0.35, "active": 0.40}
        }
    },
    "temporal_dynamics": {
        "daily_patterns": {
            "peak_hours": ["07:00-09:00", "17:00-19:00"],
            "activity_distribution": {
                "morning": 0.35,
                "afternoon": 0.30,
                "evening": 0.25,
                "night": 0.10
            }
        },
        "seasonal_variations": {
            "spring": {"outdoor_activity": 0.75, "energy_demand": 0.60},
            "summer": {"outdoor_activity": 0.85, "energy_demand": 0.80},
            "fall": {"outdoor_activity": 0.70, "energy_demand": 0.65},
            "winter": {"outdoor_activity": 0.45, "energy_demand": 0.90}
        }
    },
    "future_projections": {
        "2026": {
            "population": 151500,
            "climate_impact": "moderate",
            "tech_integration": "high"
        },
        "2030": {
            "population": 160000,
            "climate_impact": "high",
            "tech_integration": "very_high"
        }
    }
}


# Example ecological data: biodiversity, climate, environmental constraints
ECOLOGICAL_DATA = {
    "biodiversity": {
        "native_species": {
            "flora": 124,
            "fauna": 68,
            "endangered": 8
        },
        "ecosystems": [
            {"type": "urban_forest", "area_km2": 8.5, "health": "good"},
            {"type": "wetland", "area_km2": 3.2, "health": "moderate"},
            {"type": "grassland", "area_km2": 4.8, "health": "good"}
        ],
        "habitat_connectivity": 0.62
    },
    "climate": {
        "current_conditions": {
            "avg_temperature_c": 18.5,
            "annual_precipitation_mm": 850,
            "extreme_events_per_year": 3
        },
        "climate_risks": [
            {"type": "heat_waves", "probability": 0.35, "severity": "medium"},
            {"type": "flooding", "probability": 0.22, "severity": "high"},
            {"type": "drought", "probability": 0.18, "severity": "low"}
        ],
        "carbon_budget": {
            "current_emissions_tons": 450000,
            "target_reduction": 0.40,
            "timeline_years": 5
        }
    },
    "environmental_constraints": {
        "protected_areas": {
            "total_area_km2": 6.5,
            "restrictions": ["no_construction", "limited_access", "ecological_restoration"]
        },
        "pollution_limits": {
            "air_quality_index_max": 50,
            "noise_level_db_max": 65,
            "water_quality_standard": "A"
        },
        "resource_limits": {
            "water_availability_m3_day": 85000,
            "renewable_energy_capacity_mw": 45,
            "waste_processing_tons_day": 320
        }
    }
}


# Example governance rules: policies, regulations, evaluation criteria
GOVERNANCE_RULES = {
    "policies": {
        "sustainability": {
            "renewable_energy_target": 0.60,
            "green_space_per_capita_m2": 12,
            "carbon_neutrality_year": 2030
        },
        "equity": {
            "affordable_housing_ratio": 0.25,
            "public_transport_access_radius_m": 500,
            "income_diversity_index_min": 0.65
        },
        "efficiency": {
            "land_use_optimization": True,
            "transport_efficiency_target": 0.75,
            "infrastructure_utilization_min": 0.70
        },
        "memory": {
            "heritage_preservation": True,
            "cultural_landmarks_protection": True,
            "community_narrative_integration": True
        }
    },
    "regulations": [
        {
            "id": "reg_001",
            "name": "Green Space Minimum",
            "type": "hard_constraint",
            "requirement": "min_15_percent_green_space"
        },
        {
            "id": "reg_002",
            "name": "Air Quality Standard",
            "type": "hard_constraint",
            "requirement": "aqi_below_50"
        },
        {
            "id": "reg_003",
            "name": "Affordable Housing",
            "type": "soft_constraint",
            "requirement": "25_percent_affordable_units"
        },
        {
            "id": "reg_004",
            "name": "Heritage Protection",
            "type": "hard_constraint",
            "requirement": "preserve_listed_buildings"
        }
    ],
    "evaluation_criteria": {
        "weights": {
            "efficiency": 0.25,
            "equity": 0.30,
            "biodiversity": 0.25,
            "memory": 0.20
        },
        "thresholds": {
            "minimum_score": 0.60,
            "acceptable_tradeoff": 0.15
        },
        "xai_requirements": {
            "explainability_level": "high",
            "transparency": True,
            "stakeholder_comprehension": "accessible"
        },
        "audit_requirements": {
            "traceability": True,
            "version_control": True,
            "compliance_reporting": "quarterly"
        }
    }
}


# Consolidated seed data for easy import
SEED_DATA = {
    "human_data": HUMAN_DATA,
    "spatial_data": SPATIAL_DATA,
    "temporal_data": TEMPORAL_DATA,
    "ecological_data": ECOLOGICAL_DATA,
    "governance_rules": GOVERNANCE_RULES
}
