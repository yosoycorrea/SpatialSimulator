/**
 * Spatial Simulator Lite - Main Application
 * 
 * This application provides an educational tool for understanding spatial dynamics.
 * It includes features for mapping, spatial analysis, and interactive scenarios.
 * 
 * @author Spatial Simulator Team
 * @version 1.0.0
 */

// ===========================
// Application State
// ===========================

const AppState = {
    map: null,
    userLocation: null,
    elements: {
        pois: [],
        agents: [],
        zones: [],
        connections: []
    },
    markers: [],
    layers: {
        pois: null,
        agents: null,
        zones: null,
        connections: null
    },
    currentScenario: null,
    mapClickMode: null  // For interactive placement
};

// ===========================
// Tutorial System
// ===========================

const TutorialSteps = [
    {
        title: "Welcome to Spatial Simulator Lite! 🌍",
        content: `
            <p>This tool helps you understand spatial relationships and geographic dynamics in your environment.</p>
            <h4>What you'll learn:</h4>
            <ul>
                <li>How to map your environment</li>
                <li>Understanding spatial relationships</li>
                <li>Analyzing distances and accessibility</li>
                <li>Impact of urban planning decisions</li>
            </ul>
        `
    },
    {
        title: "Setting Your Location 📍",
        content: `
            <p><strong>Start by setting your location:</strong></p>
            <ol>
                <li>Go to the <strong>Location</strong> tab in the sidebar</li>
                <li>Enter an address or use "Use My Location"</li>
                <li>The map will center on your chosen location</li>
            </ol>
            <p class="text-muted">Tip: You can also click anywhere on the map to explore different areas!</p>
        `
    },
    {
        title: "Adding Elements 🏗️",
        content: `
            <p><strong>Build your spatial model:</strong></p>
            <ul>
                <li><strong>Points of Interest (POIs):</strong> Schools, hospitals, parks, stores</li>
                <li><strong>Agents:</strong> People who move through the environment (residents, workers, students)</li>
                <li><strong>Zones:</strong> Different area types (residential, commercial, industrial)</li>
                <li><strong>Connections:</strong> Transportation networks (roads, bus routes, bike paths)</li>
            </ul>
            <p>Click on elements on the map to place them, or use the Elements tab!</p>
        `
    },
    {
        title: "Running Scenarios 🎮",
        content: `
            <p><strong>Learn through interactive scenarios:</strong></p>
            <ul>
                <li><strong>Explore Your Environment:</strong> Discover nearby services and their distances</li>
                <li><strong>Transportation Impact:</strong> See how transport changes affect accessibility</li>
                <li><strong>Urban Planning:</strong> Design and analyze different city layouts</li>
                <li><strong>Distance Analysis:</strong> Calculate distances between important points</li>
            </ul>
            <p>Go to the <strong>Scenarios</strong> tab to get started!</p>
        `
    },
    {
        title: "Understanding Geography 🌐",
        content: `
            <h4>Key Concepts:</h4>
            <ul>
                <li><strong>Spatial Relationships:</strong> How locations relate to each other</li>
                <li><strong>Accessibility:</strong> How easy it is to reach different places</li>
                <li><strong>Distance Decay:</strong> Things get harder to access as distance increases</li>
                <li><strong>Network Effects:</strong> How connections shape movement and interaction</li>
            </ul>
            <p>These principles help us understand cities, communities, and environments!</p>
        `
    },
    {
        title: "Ready to Explore! 🚀",
        content: `
            <p>You're all set to start exploring spatial dynamics!</p>
            <h4>Quick Tips:</h4>
            <ul>
                <li>Start with a simple scenario</li>
                <li>Experiment with different elements</li>
                <li>Click the Help button (❓) anytime for assistance</li>
                <li>Use the Export button (💾) to save your work</li>
            </ul>
            <p><strong>Have fun learning about your spatial environment!</strong></p>
        `
    }
];

let currentTutorialStep = 0;

// ===========================
// Initialization
// ===========================

document.addEventListener('DOMContentLoaded', function() {
    initializeMap();
    initializeEventListeners();
    initializeTutorial();
    updateStatistics();
});

/**
 * Initialize the Leaflet map
 */
function initializeMap() {
    // Create map centered on a default location (can be changed by user)
    AppState.map = L.map('map').setView([40.7128, -74.0060], 13); // Default: New York City

    // Add OpenStreetMap tile layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        maxZoom: 19
    }).addTo(AppState.map);

    // Initialize layer groups for different element types
    AppState.layers.pois = L.layerGroup().addTo(AppState.map);
    AppState.layers.agents = L.layerGroup().addTo(AppState.map);
    AppState.layers.zones = L.layerGroup().addTo(AppState.map);
    AppState.layers.connections = L.layerGroup().addTo(AppState.map);

    // Add click handler for interactive placement
    AppState.map.on('click', onMapClick);

    // Add scale control
    L.control.scale().addTo(AppState.map);
}

/**
 * Initialize all event listeners
 */
function initializeEventListeners() {
    // Tab navigation
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.addEventListener('click', () => switchTab(btn.dataset.tab));
    });

    // Location controls
    document.getElementById('set-location-btn').addEventListener('click', setUserLocation);
    document.getElementById('use-current-location-btn').addEventListener('click', useCurrentLocation);

    // Element addition buttons
    document.getElementById('add-poi-btn').addEventListener('click', addPointOfInterest);
    document.getElementById('add-agent-btn').addEventListener('click', addAgent);
    document.getElementById('add-zone-btn').addEventListener('click', addZone);
    document.getElementById('add-connection-btn').addEventListener('click', enableConnectionMode);

    // Scenario buttons
    document.querySelectorAll('.btn-scenario').forEach(btn => {
        btn.addEventListener('click', () => runScenario(btn.dataset.scenario));
    });

    // Visualization controls
    document.getElementById('clear-map-btn').addEventListener('click', clearMap);
    document.getElementById('export-btn').addEventListener('click', exportData);
    document.getElementById('help-btn').addEventListener('click', showHelp);

    // Tutorial
    document.getElementById('tutorial-btn').addEventListener('click', openTutorial);
    document.querySelector('.close-modal').addEventListener('click', closeTutorial);
    document.getElementById('prev-tutorial').addEventListener('click', previousTutorialStep);
    document.getElementById('next-tutorial').addEventListener('click', nextTutorialStep);

    // Close modal when clicking outside
    document.getElementById('tutorial-modal').addEventListener('click', function(e) {
        if (e.target === this) {
            closeTutorial();
        }
    });
}

// ===========================
// Tab Management
// ===========================

function switchTab(tabName) {
    // Update tab buttons
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.tab === tabName);
    });

    // Update tab content
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.toggle('active', content.id === `${tabName}-tab`);
    });
}

// ===========================
// Location Management
// ===========================

/**
 * Set user location from address input
 */
async function setUserLocation() {
    const locationInput = document.getElementById('user-location').value.trim();
    
    if (!locationInput) {
        showInfo('Please enter a location');
        return;
    }

    // Use Nominatim for geocoding (free OSM service)
    try {
        const response = await fetch(
            `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(locationInput)}`
        );
        const data = await response.json();

        if (data && data.length > 0) {
            const lat = parseFloat(data[0].lat);
            const lon = parseFloat(data[0].lon);
            
            AppState.userLocation = [lat, lon];
            AppState.map.setView(AppState.userLocation, 15);

            // Add marker for user location
            const marker = L.marker(AppState.userLocation, {
                icon: L.divIcon({
                    className: 'user-location-marker',
                    html: '📍',
                    iconSize: [30, 30]
                })
            }).addTo(AppState.map);
            
            marker.bindPopup(`<strong>Your Location</strong><br>${data[0].display_name}`).openPopup();

            document.getElementById('current-coords').innerHTML = 
                `<strong>Current Location:</strong><br>Lat: ${lat.toFixed(4)}, Lon: ${lon.toFixed(4)}`;

            showInfo(`Location set to: ${data[0].display_name}`);
        } else {
            showInfo('Location not found. Please try another address.');
        }
    } catch (error) {
        console.error('Geocoding error:', error);
        showInfo('Error finding location. Please try again.');
    }
}

/**
 * Use browser geolocation to get current position
 */
function useCurrentLocation() {
    if (!navigator.geolocation) {
        showInfo('Geolocation is not supported by your browser');
        return;
    }

    showInfo('Getting your location...');

    navigator.geolocation.getCurrentPosition(
        (position) => {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            
            AppState.userLocation = [lat, lon];
            AppState.map.setView(AppState.userLocation, 15);

            const marker = L.marker(AppState.userLocation, {
                icon: L.divIcon({
                    className: 'user-location-marker',
                    html: '📍',
                    iconSize: [30, 30]
                })
            }).addTo(AppState.map);
            
            marker.bindPopup('<strong>Your Current Location</strong>').openPopup();

            document.getElementById('current-coords').innerHTML = 
                `<strong>Current Location:</strong><br>Lat: ${lat.toFixed(4)}, Lon: ${lon.toFixed(4)}`;

            showInfo('Location set successfully!');
        },
        (error) => {
            console.error('Geolocation error:', error);
            showInfo('Unable to get your location. Please enter manually.');
        }
    );
}

// ===========================
// Element Management
// ===========================

/**
 * Add a Point of Interest
 */
function addPointOfInterest() {
    const poiType = document.getElementById('poi-type').value;
    const poiName = document.getElementById('poi-name').value.trim() || `${getTypeLabel(poiType)} ${AppState.elements.pois.length + 1}`;

    // If user location is set, add POI nearby
    let location;
    if (AppState.userLocation) {
        // Add some random offset (within ~500m)
        const offset = 0.005;
        location = [
            AppState.userLocation[0] + (Math.random() - 0.5) * offset,
            AppState.userLocation[1] + (Math.random() - 0.5) * offset
        ];
    } else {
        // Use map center
        const center = AppState.map.getCenter();
        location = [center.lat, center.lng];
    }

    const poi = {
        id: Date.now(),
        type: poiType,
        name: poiName,
        location: location
    };

    AppState.elements.pois.push(poi);
    renderPOI(poi);
    updateElementList('poi');
    updateStatistics();

    // Clear input
    document.getElementById('poi-name').value = '';

    showInfo(`Added ${poiName}`);
}

/**
 * Render a POI on the map
 */
function renderPOI(poi) {
    const icon = getPOIIcon(poi.type);
    
    const marker = L.marker(poi.location, {
        icon: L.divIcon({
            className: 'poi-marker',
            html: icon,
            iconSize: [30, 30]
        }),
        draggable: true
    }).addTo(AppState.layers.pois);

    marker.bindPopup(`
        <strong>${poi.name}</strong><br>
        Type: ${getTypeLabel(poi.type)}<br>
        <button onclick="removePOI(${poi.id})" class="btn-remove">Remove</button>
    `);

    // Update location on drag
    marker.on('dragend', function(e) {
        const newPos = e.target.getLatLng();
        poi.location = [newPos.lat, newPos.lng];
    });

    poi.marker = marker;
}

/**
 * Add an Agent (person)
 */
function addAgent() {
    const agentType = document.getElementById('agent-type').value;
    const agentName = document.getElementById('agent-name').value.trim() || `${getTypeLabel(agentType)} ${AppState.elements.agents.length + 1}`;

    let location;
    if (AppState.userLocation) {
        const offset = 0.005;
        location = [
            AppState.userLocation[0] + (Math.random() - 0.5) * offset,
            AppState.userLocation[1] + (Math.random() - 0.5) * offset
        ];
    } else {
        const center = AppState.map.getCenter();
        location = [center.lat, center.lng];
    }

    const agent = {
        id: Date.now(),
        type: agentType,
        name: agentName,
        location: location
    };

    AppState.elements.agents.push(agent);
    renderAgent(agent);
    updateElementList('agent');
    updateStatistics();

    document.getElementById('agent-name').value = '';
    showInfo(`Added ${agentName}`);
}

/**
 * Render an Agent on the map
 */
function renderAgent(agent) {
    const icon = getAgentIcon(agent.type);
    
    const marker = L.marker(agent.location, {
        icon: L.divIcon({
            className: 'agent-marker',
            html: icon,
            iconSize: [30, 30]
        }),
        draggable: true
    }).addTo(AppState.layers.agents);

    marker.bindPopup(`
        <strong>${agent.name}</strong><br>
        Type: ${getTypeLabel(agent.type)}<br>
        <button onclick="removeAgent(${agent.id})" class="btn-remove">Remove</button>
    `);

    marker.on('dragend', function(e) {
        const newPos = e.target.getLatLng();
        agent.location = [newPos.lat, newPos.lng];
    });

    agent.marker = marker;
}

/**
 * Add a Zone
 */
function addZone() {
    const zoneType = document.getElementById('zone-type').value;
    const zoneName = document.getElementById('zone-name').value.trim() || `${getTypeLabel(zoneType)} Zone ${AppState.elements.zones.length + 1}`;

    let centerLocation;
    if (AppState.userLocation) {
        const offset = 0.01;
        centerLocation = [
            AppState.userLocation[0] + (Math.random() - 0.5) * offset,
            AppState.userLocation[1] + (Math.random() - 0.5) * offset
        ];
    } else {
        const center = AppState.map.getCenter();
        centerLocation = [center.lat, center.lng];
    }

    const zone = {
        id: Date.now(),
        type: zoneType,
        name: zoneName,
        center: centerLocation,
        radius: 200 // meters
    };

    AppState.elements.zones.push(zone);
    renderZone(zone);
    updateElementList('zone');
    updateStatistics();

    document.getElementById('zone-name').value = '';
    showInfo(`Added ${zoneName}`);
}

/**
 * Render a Zone on the map
 */
function renderZone(zone) {
    const color = getZoneColor(zone.type);
    
    const circle = L.circle(zone.center, {
        color: color,
        fillColor: color,
        fillOpacity: 0.2,
        radius: zone.radius
    }).addTo(AppState.layers.zones);

    circle.bindPopup(`
        <strong>${zone.name}</strong><br>
        Type: ${getTypeLabel(zone.type)}<br>
        Radius: ${zone.radius}m<br>
        <button onclick="removeZone(${zone.id})" class="btn-remove">Remove</button>
    `);

    zone.circle = circle;
}

/**
 * Enable connection drawing mode
 */
let connectionPoints = [];

function enableConnectionMode() {
    const connectionType = document.getElementById('connection-type').value;
    
    showInfo('Click two points on the map to create a connection');
    connectionPoints = [];
    
    AppState.mapClickMode = 'connection';
    AppState.currentConnectionType = connectionType;
}

/**
 * Handle map clicks for various modes
 */
function onMapClick(e) {
    if (AppState.mapClickMode === 'connection') {
        connectionPoints.push([e.latlng.lat, e.latlng.lng]);
        
        // Temporary marker
        L.circleMarker([e.latlng.lat, e.latlng.lng], {
            radius: 5,
            color: '#f59e0b'
        }).addTo(AppState.map);

        if (connectionPoints.length === 2) {
            createConnection(connectionPoints[0], connectionPoints[1], AppState.currentConnectionType);
            connectionPoints = [];
            AppState.mapClickMode = null;
        }
    }
}

/**
 * Create a connection between two points
 */
function createConnection(point1, point2, type) {
    const connection = {
        id: Date.now(),
        type: type,
        points: [point1, point2],
        name: `${getTypeLabel(type)} Connection`
    };

    AppState.elements.connections.push(connection);
    renderConnection(connection);
    updateElementList('connection');
    updateStatistics();

    showInfo(`Created ${connection.name}`);
}

/**
 * Render a Connection on the map
 */
function renderConnection(connection) {
    const color = getConnectionColor(connection.type);
    const dashArray = getConnectionDashArray(connection.type);
    
    const polyline = L.polyline(connection.points, {
        color: color,
        weight: 4,
        dashArray: dashArray
    }).addTo(AppState.layers.connections);

    const distance = calculateDistance(connection.points[0], connection.points[1]);

    polyline.bindPopup(`
        <strong>${connection.name}</strong><br>
        Type: ${getTypeLabel(connection.type)}<br>
        Distance: ${distance.toFixed(2)} km<br>
        <button onclick="removeConnection(${connection.id})" class="btn-remove">Remove</button>
    `);

    connection.polyline = polyline;
}

// ===========================
// Element Removal Functions
// ===========================

function removePOI(id) {
    const index = AppState.elements.pois.findIndex(p => p.id === id);
    if (index !== -1) {
        const poi = AppState.elements.pois[index];
        if (poi.marker) {
            AppState.layers.pois.removeLayer(poi.marker);
        }
        AppState.elements.pois.splice(index, 1);
        updateElementList('poi');
        updateStatistics();
    }
}

function removeAgent(id) {
    const index = AppState.elements.agents.findIndex(a => a.id === id);
    if (index !== -1) {
        const agent = AppState.elements.agents[index];
        if (agent.marker) {
            AppState.layers.agents.removeLayer(agent.marker);
        }
        AppState.elements.agents.splice(index, 1);
        updateElementList('agent');
        updateStatistics();
    }
}

function removeZone(id) {
    const index = AppState.elements.zones.findIndex(z => z.id === id);
    if (index !== -1) {
        const zone = AppState.elements.zones[index];
        if (zone.circle) {
            AppState.layers.zones.removeLayer(zone.circle);
        }
        AppState.elements.zones.splice(index, 1);
        updateElementList('zone');
        updateStatistics();
    }
}

function removeConnection(id) {
    const index = AppState.elements.connections.findIndex(c => c.id === id);
    if (index !== -1) {
        const connection = AppState.elements.connections[index];
        if (connection.polyline) {
            AppState.layers.connections.removeLayer(connection.polyline);
        }
        AppState.elements.connections.splice(index, 1);
        updateElementList('connection');
        updateStatistics();
    }
}

// ===========================
// Element List Updates
// ===========================

function updateElementList(type) {
    const listId = `${type}-list`;
    const list = document.getElementById(listId);
    if (!list) return;

    const elements = AppState.elements[`${type}s`] || [];
    
    list.innerHTML = '';
    
    elements.forEach(element => {
        const item = document.createElement('div');
        item.className = 'element-item';
        item.innerHTML = `
            <div class="element-item-info">
                <div class="element-item-name">${element.name}</div>
                <div class="element-item-type">${getTypeLabel(element.type)}</div>
            </div>
            <button class="btn-remove" onclick="remove${capitalizeFirst(type)}(${element.id})">×</button>
        `;
        list.appendChild(item);
    });
}

// ===========================
// Scenarios
// ===========================

function runScenario(scenarioType) {
    AppState.currentScenario = scenarioType;
    
    switch(scenarioType) {
        case 'explore':
            exploreEnvironmentScenario();
            break;
        case 'transport':
            transportationImpactScenario();
            break;
        case 'urban':
            urbanPlanningScenario();
            break;
        case 'distance':
            distanceAnalysisScenario();
            break;
    }
}

/**
 * Scenario: Explore Your Environment
 */
function exploreEnvironmentScenario() {
    showInfo(`
        <h4>🔍 Explore Your Environment</h4>
        <p>This scenario helps you discover key features around your location.</p>
        <ol>
            <li>Add some Points of Interest (schools, hospitals, parks)</li>
            <li>Notice the distances between them</li>
            <li>Think about how accessible they are from your location</li>
        </ol>
    `);

    // If no POIs exist, add some examples
    if (AppState.elements.pois.length === 0 && AppState.userLocation) {
        showInfo('Adding sample points of interest...');
        
        // Add sample POIs
        const samplePOIs = [
            { type: 'school', name: 'Sample School' },
            { type: 'hospital', name: 'Sample Hospital' },
            { type: 'park', name: 'Sample Park' }
        ];

        samplePOIs.forEach((poi, index) => {
            setTimeout(() => {
                document.getElementById('poi-type').value = poi.type;
                document.getElementById('poi-name').value = poi.name;
                addPointOfInterest();
            }, index * 300);
        });
    }
}

/**
 * Scenario: Transportation Impact
 */
function transportationImpactScenario() {
    showInfo(`
        <h4>🚌 Transportation Impact Analysis</h4>
        <p>Explore how transportation networks affect accessibility.</p>
        <ol>
            <li>Add some destinations (stores, schools, etc.)</li>
            <li>Create connections (roads, bus routes)</li>
            <li>Observe how different transport modes change accessibility</li>
            <li>Try removing a connection - what happens?</li>
        </ol>
        <p><strong>Key Concept:</strong> Better transportation = Better accessibility</p>
    `);
}

/**
 * Scenario: Urban Planning
 */
function urbanPlanningScenario() {
    showInfo(`
        <h4>🏘️ Urban Planning Simulation</h4>
        <p>Design and analyze different urban layouts.</p>
        <ol>
            <li>Create different zones (residential, commercial, industrial)</li>
            <li>Add agents (residents, workers)</li>
            <li>Consider: Where do people live? Where do they work?</li>
            <li>Add connections to link zones</li>
        </ol>
        <p><strong>Think about:</strong> How far should people travel to work? Where should parks be located?</p>
    `);
}

/**
 * Scenario: Distance Analysis
 */
function distanceAnalysisScenario() {
    showInfo(`
        <h4>📊 Distance Analysis</h4>
        <p>Calculate and visualize distances between important points.</p>
        <ol>
            <li>Add at least two points of interest</li>
            <li>Click "Add Connection" and select two points</li>
            <li>The distance will be calculated automatically</li>
            <li>Compare different routes and distances</li>
        </ol>
    `);

    // Switch to connections for easy access
    switchTab('elements');
}

// ===========================
// Utility Functions
// ===========================

/**
 * Calculate distance between two lat/lng points (Haversine formula)
 */
function calculateDistance(point1, point2) {
    const R = 6371; // Earth's radius in km
    const lat1 = point1[0] * Math.PI / 180;
    const lat2 = point2[0] * Math.PI / 180;
    const dLat = (point2[0] - point1[0]) * Math.PI / 180;
    const dLon = (point2[1] - point1[1]) * Math.PI / 180;

    const a = Math.sin(dLat/2) * Math.sin(dLat/2) +
              Math.cos(lat1) * Math.cos(lat2) *
              Math.sin(dLon/2) * Math.sin(dLon/2);
    
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
    
    return R * c;
}

/**
 * Get icon for POI type
 */
function getPOIIcon(type) {
    const icons = {
        school: '🏫',
        hospital: '🏥',
        park: '🌳',
        store: '🏪',
        restaurant: '🍽️'
    };
    return icons[type] || '📍';
}

/**
 * Get icon for Agent type
 */
function getAgentIcon(type) {
    const icons = {
        resident: '🏠',
        worker: '💼',
        student: '🎓',
        visitor: '🚶'
    };
    return icons[type] || '👤';
}

/**
 * Get color for Zone type
 */
function getZoneColor(type) {
    const colors = {
        residential: '#10b981',
        commercial: '#3b82f6',
        industrial: '#f59e0b',
        recreational: '#8b5cf6'
    };
    return colors[type] || '#6b7280';
}

/**
 * Get color for Connection type
 */
function getConnectionColor(type) {
    const colors = {
        road: '#374151',
        bus: '#3b82f6',
        train: '#8b5cf6',
        bike: '#10b981',
        walk: '#f59e0b'
    };
    return colors[type] || '#6b7280';
}

/**
 * Get dash array for Connection type
 */
function getConnectionDashArray(type) {
    const patterns = {
        road: null,
        bus: '10, 10',
        train: '15, 5',
        bike: '5, 5',
        walk: '2, 8'
    };
    return patterns[type] || null;
}

/**
 * Get human-readable label for type
 */
function getTypeLabel(type) {
    const labels = {
        // POI types
        school: 'School',
        hospital: 'Hospital',
        park: 'Park',
        store: 'Store',
        restaurant: 'Restaurant',
        // Agent types
        resident: 'Resident',
        worker: 'Worker',
        student: 'Student',
        visitor: 'Visitor',
        // Zone types
        residential: 'Residential',
        commercial: 'Commercial',
        industrial: 'Industrial',
        recreational: 'Recreational',
        // Connection types
        road: 'Road',
        bus: 'Bus Route',
        train: 'Train Line',
        bike: 'Bike Path',
        walk: 'Walking Path'
    };
    return labels[type] || type;
}

/**
 * Capitalize first letter
 */
function capitalizeFirst(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}

/**
 * Update statistics panel
 */
function updateStatistics() {
    document.getElementById('stat-poi').textContent = AppState.elements.pois.length;
    document.getElementById('stat-agents').textContent = AppState.elements.agents.length;
    document.getElementById('stat-zones').textContent = AppState.elements.zones.length;
    document.getElementById('stat-connections').textContent = AppState.elements.connections.length;
}

/**
 * Show information in the info panel
 */
function showInfo(message) {
    const infoContent = document.getElementById('info-content');
    infoContent.innerHTML = message;
}

/**
 * Clear the map of all elements
 */
function clearMap() {
    if (confirm('Are you sure you want to clear all elements from the map?')) {
        // Clear all layers
        AppState.layers.pois.clearLayers();
        AppState.layers.agents.clearLayers();
        AppState.layers.zones.clearLayers();
        AppState.layers.connections.clearLayers();

        // Clear state
        AppState.elements.pois = [];
        AppState.elements.agents = [];
        AppState.elements.zones = [];
        AppState.elements.connections = [];

        // Update UI
        updateElementList('poi');
        updateElementList('agent');
        updateElementList('zone');
        updateElementList('connection');
        updateStatistics();

        showInfo('Map cleared. Start fresh!');
    }
}

/**
 * Export data as JSON
 */
function exportData() {
    const data = {
        userLocation: AppState.userLocation,
        elements: {
            pois: AppState.elements.pois.map(poi => ({
                id: poi.id,
                type: poi.type,
                name: poi.name,
                location: poi.location
            })),
            agents: AppState.elements.agents.map(agent => ({
                id: agent.id,
                type: agent.type,
                name: agent.name,
                location: agent.location
            })),
            zones: AppState.elements.zones.map(zone => ({
                id: zone.id,
                type: zone.type,
                name: zone.name,
                center: zone.center,
                radius: zone.radius
            })),
            connections: AppState.elements.connections.map(conn => ({
                id: conn.id,
                type: conn.type,
                name: conn.name,
                points: conn.points
            }))
        },
        timestamp: new Date().toISOString()
    };

    const dataStr = JSON.stringify(data, null, 2);
    const dataBlob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(dataBlob);
    
    const link = document.createElement('a');
    link.href = url;
    link.download = `spatial-simulator-${Date.now()}.json`;
    link.click();
    
    URL.revokeObjectURL(url);
    showInfo('Data exported successfully!');
}

/**
 * Show help information
 */
function showHelp() {
    showInfo(`
        <h4>❓ Quick Help</h4>
        <ul>
            <li><strong>Set Location:</strong> Use the Location tab to center the map</li>
            <li><strong>Add Elements:</strong> Use the Elements tab to add POIs, agents, zones, and connections</li>
            <li><strong>Run Scenarios:</strong> Try interactive learning scenarios in the Scenarios tab</li>
            <li><strong>Interact:</strong> Click and drag markers to reposition them</li>
            <li><strong>Export:</strong> Save your work using the Export button</li>
        </ul>
        <p>Click the Tutorial button in the header for a full walkthrough!</p>
    `);
}

// ===========================
// Tutorial Functions
// ===========================

function initializeTutorial() {
    currentTutorialStep = 0;
}

function openTutorial() {
    const modal = document.getElementById('tutorial-modal');
    modal.classList.add('active');
    currentTutorialStep = 0;
    showTutorialStep(currentTutorialStep);
}

function closeTutorial() {
    const modal = document.getElementById('tutorial-modal');
    modal.classList.remove('active');
}

function showTutorialStep(stepIndex) {
    const step = TutorialSteps[stepIndex];
    const content = document.getElementById('tutorial-content');
    
    content.innerHTML = `
        <h2>${step.title}</h2>
        ${step.content}
    `;

    document.getElementById('tutorial-progress').textContent = 
        `Step ${stepIndex + 1} of ${TutorialSteps.length}`;

    // Update button states
    document.getElementById('prev-tutorial').disabled = stepIndex === 0;
    document.getElementById('next-tutorial').textContent = 
        stepIndex === TutorialSteps.length - 1 ? 'Finish' : 'Next →';
}

function previousTutorialStep() {
    if (currentTutorialStep > 0) {
        currentTutorialStep--;
        showTutorialStep(currentTutorialStep);
    }
}

function nextTutorialStep() {
    if (currentTutorialStep < TutorialSteps.length - 1) {
        currentTutorialStep++;
        showTutorialStep(currentTutorialStep);
    } else {
        closeTutorial();
    }
}

// ===========================
// Make removal functions globally accessible
// ===========================
window.removePOI = removePOI;
window.removeAgent = removeAgent;
window.removeZone = removeZone;
window.removeConnection = removeConnection;
