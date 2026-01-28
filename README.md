# Spatial Simulator Lite 🌍

## Overview

**Spatial Simulator Lite** is an educational web-based tool designed to help new users understand spatial dynamics and geography in an interactive, engaging way. This lightweight version provides an intuitive interface for exploring spatial relationships, mapping environments, and learning about geographic principles through hands-on exercises.

The tool emphasizes geography as a bridge science, connecting physical, human, and interdisciplinary dimensions to foster a holistic understanding of how space shapes our world.

## 🎯 Key Features

### 1. **Simple User Interface**
- Clean, intuitive design requiring no prior GIS knowledge
- Easy location input via address search or geolocation
- Interactive map-based interface using Leaflet.js
- Responsive design that works on desktop and mobile devices

### 2. **Interactive Visualization Tools**
- Real-time mapping with OpenStreetMap integration
- Distance calculations between points
- Visual representation of zones and connections
- Drag-and-drop marker positioning
- Color-coded elements for easy identification

### 3. **Educational Scenarios**
Four pre-built learning scenarios to guide exploration:
- **🔍 Explore Your Environment**: Discover key features in your area
- **🚌 Transportation Impact**: Analyze how transport affects accessibility
- **🏘️ Urban Planning**: Design and evaluate urban layouts
- **📊 Distance Analysis**: Calculate and visualize spatial relationships

### 4. **Modular Customization**
Easily add and modify spatial elements:
- **Points of Interest (POIs)**: Schools, hospitals, parks, stores, restaurants
- **Agents**: People with different roles (residents, workers, students, visitors)
- **Zones**: Different area types (residential, commercial, industrial, recreational)
- **Connections**: Transportation networks (roads, bus routes, trains, bike paths, walking paths)

### 5. **Interactive Tutorials**
- Step-by-step guided tutorial system
- Contextual help and tooltips throughout the interface
- Educational content explaining geographic concepts
- Real-time feedback on user actions

## 🚀 Getting Started

### Quick Start (No Installation Required!)

1. **Open the Application**
   - Simply open `index.html` in a modern web browser (Chrome, Firefox, Safari, Edge)
   - No server or installation needed - works directly from your file system

2. **Set Your Location**
   - Click on the "📍 Location" tab
   - Enter an address or click "Use My Location"
   - The map will center on your chosen location

3. **Start Learning**
   - Click "📚 Start Tutorial" for a guided walkthrough
   - Or jump right in with the "🎮 Scenarios" tab

### First Steps Tutorial

When you first open the application, we recommend:

1. **Click the "Start Tutorial" button** in the header to get a comprehensive walkthrough
2. **Set your location** to make the experience more relevant to you
3. **Try the "Explore Your Environment" scenario** to get familiar with adding elements
4. **Experiment freely** - you can always clear the map and start fresh!

## 📖 How to Use

### Adding Elements to Your Map

#### Points of Interest (POIs)
1. Go to the **Elements** tab
2. Select a POI type from the dropdown (school, hospital, park, etc.)
3. Enter a name (optional - one will be generated automatically)
4. Click "➕ Add POI"
5. The POI will appear on the map near your location

#### Agents (People)
1. In the **Elements** tab, scroll to the Agents section
2. Enter an agent name
3. Select the agent type (resident, worker, student, visitor)
4. Click "➕ Add Agent"

#### Zones
1. In the **Elements** tab, find the Zones section
2. Select a zone type (residential, commercial, industrial, recreational)
3. Enter a zone name
4. Click "➕ Add Zone"
5. A circular zone will appear on the map

#### Connections (Transportation)
1. In the **Elements** tab, go to Connections
2. Select a connection type (road, bus, train, bike path, walking path)
3. Click "➕ Add Connection"
4. Click two points on the map to create the connection
5. The distance will be calculated automatically

### Using Scenarios

Each scenario provides a structured learning experience:

1. **Click on a scenario** in the Scenarios tab
2. **Read the instructions** that appear in the info panel
3. **Follow the guided steps** to complete the exercise
4. **Experiment** with different configurations
5. **Observe** how changes affect the spatial relationships

### Interacting with the Map

- **Click markers** to see information and options
- **Drag markers** to reposition elements
- **Click the map** to place connections
- **Use zoom controls** to navigate
- **Click popup buttons** to remove elements

### Saving and Exporting

- Click the **💾 Export** button to save your current map as JSON
- The exported file includes all elements and their positions
- Can be used for documentation or sharing with others

## 🎓 Educational Concepts

### Key Geographic Principles Taught

1. **Spatial Relationships**
   - Understanding how locations relate to each other
   - Distance and proximity concepts
   - Accessibility and connectivity

2. **Distance Decay**
   - Things become harder to access as distance increases
   - Importance of nearby services
   - Impact on daily life and decision-making

3. **Transportation Networks**
   - How connections shape movement patterns
   - Impact of different transport modes
   - Accessibility analysis

4. **Urban Planning**
   - Zoning and land use concepts
   - Relationship between residential, commercial, and industrial areas
   - Importance of balanced spatial distribution

5. **Geographic Thinking**
   - Analyzing "where" and "why there"
   - Understanding spatial patterns
   - Making location-based decisions

## 🛠️ Technical Details

### Technologies Used

- **HTML5**: Structure and semantics
- **CSS3**: Styling with modern responsive design
- **JavaScript (ES6+)**: Application logic and interactivity
- **Leaflet.js**: Interactive mapping library
- **OpenStreetMap**: Free and open-source map tiles
- **Nominatim**: Geocoding service for address lookup

### Browser Compatibility

- Chrome (recommended): v90+
- Firefox: v88+
- Safari: v14+
- Edge: v90+

### File Structure

```
SpatialSimulator/
├── index.html          # Main application page
├── styles.css          # All styling and theming
├── app.js             # Application logic and functionality
├── README.md          # This documentation
└── LICENSE            # License information
```

### No Dependencies Required

All libraries are loaded via CDN:
- Leaflet.js (v1.9.4) - for mapping functionality
- OpenStreetMap tiles - for map visualization

This means:
- ✅ No npm install needed
- ✅ No build process required
- ✅ Works offline (after initial CDN load)
- ✅ Easy to deploy anywhere

## 🎨 Customization

### For Educators

The tool is designed to be easily customizable:

1. **Modify Scenarios**: Edit the `runScenario()` functions in `app.js`
2. **Add New Element Types**: Extend the type dropdowns in `index.html`
3. **Change Colors/Icons**: Modify the utility functions in `app.js`
4. **Customize Tutorial**: Edit the `TutorialSteps` array in `app.js`
5. **Adjust Styling**: Modify CSS variables in `styles.css`

### Code Structure

The application follows a modular structure:

- **State Management**: `AppState` object holds all application data
- **Initialization**: `initializeMap()` and `initializeEventListeners()`
- **Element Management**: Separate functions for POIs, agents, zones, connections
- **Scenarios**: Modular scenario functions for easy extension
- **Utilities**: Helper functions for calculations and rendering

All code includes detailed comments to help new contributors understand the functionality.

## 📚 Contributing

We welcome contributions from developers and educators! The code is well-documented to support new contributors:

### How to Contribute

1. **Fork the repository**
2. **Make your changes** (add features, fix bugs, improve documentation)
3. **Test thoroughly** in multiple browsers
4. **Submit a pull request** with a clear description

### Code Style

- Use meaningful variable and function names
- Add comments for complex logic
- Follow the existing code structure
- Keep functions focused and modular

### Areas for Contribution

- Additional scenarios and exercises
- New element types (e.g., public services, green spaces)
- Enhanced visualization options
- Multilingual support
- Accessibility improvements
- Mobile optimization
- Data import/export features

## 🎯 Use Cases

### For Students
- Learn geographic concepts interactively
- Understand your local environment
- Practice spatial thinking
- Complete geography assignments

### For Educators
- Teach spatial analysis concepts
- Create custom exercises
- Demonstrate urban planning principles
- Engage students with interactive content

### For Researchers
- Quick spatial prototyping
- Visualize geographic data
- Explain research concepts
- Create educational materials

### For Community Planners
- Communicate ideas to the public
- Analyze local accessibility
- Visualize proposed changes
- Gather community feedback

## 🔒 Privacy & Data

- **No data collection**: The tool runs entirely in your browser
- **No account required**: Start using immediately
- **Local processing**: All calculations happen on your device
- **No tracking**: No analytics or third-party tracking
- **Export control**: You control your data exports

## 📄 License

This project is licensed under the terms specified in the LICENSE file.

## 🌟 Goals & Vision

We aim to:
- Make geographic education accessible to everyone
- Foster spatial literacy in new learners
- Bridge the gap between theory and practice
- Cultivate understanding of how geography shapes our world
- Enable informed decision-making about spatial issues

By emphasizing the integrative nature of geography, Spatial Simulator Lite aspires to contribute to a more cohesive view of our world, helping users understand how geographical factors influence socio-economic and environmental outcomes.

## 🆘 Support & Feedback

- **Issues**: Report bugs or request features via GitHub issues
- **Questions**: Check the built-in tutorial and help system
- **Contributions**: See the Contributing section above

---

**Start exploring your spatial world today! 🌍**