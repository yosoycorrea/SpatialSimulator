# Quick Start Guide - Spatial Simulator Lite

Welcome to Spatial Simulator Lite! This guide will help you get started with the application in just a few minutes.

## 🚀 Getting Started (3 Steps)

### Step 1: Open the Application

**Option A: Simple File Access**
1. Download or clone the repository
2. Open `index.html` in your web browser
3. You're ready to go! (Requires internet for maps)

**Option B: Local Server (Recommended)**
```bash
# Navigate to the folder
cd SpatialSimulator

# Start a local server (Python)
python3 -m http.server 8000

# Open in browser
# Visit: http://localhost:8000/index.html
```

### Step 2: Take the Tutorial

1. Click the **"📚 Start Tutorial"** button in the header
2. Follow the 6-step guided walkthrough
3. Learn about all the features and how to use them

### Step 3: Start Exploring!

1. Set your location (Location tab)
2. Add elements (Elements tab)
3. Run a scenario (Scenarios tab)

## 🎯 Common Tasks

### How to Set Your Location

**Method 1: Use Your Current Location**
1. Click the **Location** tab
2. Click **"📡 Use My Location"**
3. Grant location permission when prompted

**Method 2: Enter an Address**
1. Click the **Location** tab
2. Type an address in the text field (e.g., "London, UK")
3. Click **"📍 Set Location"**

### How to Add Points of Interest

1. Go to the **Elements** tab
2. Select a POI type from the dropdown (🏫 School, 🏥 Hospital, etc.)
3. Optionally enter a custom name
4. Click **"➕ Add POI"**
5. The point will appear on the map near your location

### How to Add Agents (People)

1. Go to the **Elements** tab
2. Scroll to the "Agents" section
3. Enter an agent name
4. Select the agent type (Resident, Worker, Student, Visitor)
5. Click **"➕ Add Agent"**

### How to Create Zones

1. Go to the **Elements** tab
2. Scroll to the "Zones" section
3. Select a zone type (Residential, Commercial, Industrial, Recreational)
4. Enter a zone name
5. Click **"➕ Add Zone"**
6. A circular zone will appear on the map

### How to Draw Connections

1. Go to the **Elements** tab
2. Scroll to the "Connections" section
3. Select a connection type (Road, Bus Route, Train, etc.)
4. Click **"➕ Add Connection"**
5. Click TWO points on the map to create the connection
6. The distance will be calculated automatically

### How to Run Scenarios

1. Go to the **Scenarios** tab
2. Choose a scenario:
   - **🔍 Explore Your Environment**: Learn about nearby features
   - **🚌 Transportation Impact**: See how transport affects accessibility
   - **🏘️ Urban Planning**: Design urban layouts
   - **📊 Distance Analysis**: Calculate distances
3. Click **"Start Scenario"**
4. Follow the instructions in the Information panel

### How to Save Your Work

1. Click the **"💾 Export"** button in the visualization area
2. A JSON file will be downloaded with all your data
3. Save it for later reference or documentation

### How to Clear the Map

1. Click the **"🗑️ Clear"** button in the visualization area
2. Confirm you want to clear all elements
3. Start fresh with a clean map

## 💡 Tips for Success

### For Students
- Start with the "Explore Your Environment" scenario
- Add familiar places from your neighborhood
- Experiment with different element types
- Try to think about why certain places are located where they are

### For Educators
- Use scenarios as structured lesson plans
- Have students compare different urban layouts
- Discuss the importance of accessibility and distance
- Encourage exploration and experimentation

### Best Practices
1. **Start Simple**: Add just a few elements to understand the interface
2. **Use Scenarios**: They provide guided learning experiences
3. **Experiment**: Try different combinations and see what happens
4. **Take Notes**: Use the export feature to save interesting configurations
5. **Ask "Why?"**: Think about why elements are placed where they are

## 🐛 Troubleshooting

### Map Doesn't Appear
- **Check internet connection**: The map requires internet for tiles
- **Use Chrome or Firefox**: Best browser support
- **Try the demo**: Open `demo.html` for a non-map version

### Location Not Found
- **Try a well-known place**: Use "New York, NY" or "London, UK"
- **Use coordinates**: Enter latitude and longitude directly
- **Check spelling**: Make sure the address is spelled correctly

### Geolocation Not Working
- **Use HTTPS**: Geolocation requires a secure connection
- **Grant permission**: Allow location access when prompted
- **Try manual entry**: Enter your location manually instead

### Elements Not Appearing
- **Set location first**: Make sure you've set a location on the map
- **Zoom in**: The map might be zoomed too far out
- **Check the right tab**: Elements appear in their respective layers

## 📱 Mobile Usage

The application works on mobile devices:
- Use **landscape mode** for better viewing
- Tap elements to see information
- Pinch to zoom the map
- Use two fingers to pan

## ⌨️ Keyboard Shortcuts

- **Tab**: Navigate between form fields
- **Enter**: Submit forms (location, element names)
- **Esc**: Close tutorial modal

## 🎓 Learning Objectives

After using this tool, you should understand:

1. **Spatial Relationships**: How locations relate to each other
2. **Distance and Accessibility**: How far things are and how easy to reach
3. **Urban Planning**: How cities are organized
4. **Transportation Networks**: How connections shape movement
5. **Geographic Thinking**: Analyzing "where" and "why there"

## 📖 Additional Resources

- **README.md**: Full documentation and features
- **CONTRIBUTING.md**: For developers wanting to contribute
- **DEPLOYMENT.md**: Hosting and deployment options
- **Tutorial**: In-app 6-step guided tour

## 🆘 Need Help?

1. Click the **"❓ Help"** button for quick tips
2. Review the **Tutorial** for a complete walkthrough
3. Check the **README.md** for detailed documentation
4. Open an issue on GitHub for technical problems

---

**Ready to explore? Click "📚 Start Tutorial" to begin!** 🌍
