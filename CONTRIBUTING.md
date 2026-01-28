# Contributing to Spatial Simulator Lite

Thank you for your interest in contributing to Spatial Simulator Lite! This document provides guidelines and information for contributors.

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Code Structure](#code-structure)
- [How to Contribute](#how-to-contribute)
- [Coding Standards](#coding-standards)
- [Adding Features](#adding-features)
- [Testing](#testing)

## 🚀 Getting Started

### Prerequisites

- A modern web browser (Chrome, Firefox, Safari, or Edge)
- A text editor or IDE (VS Code, Sublime Text, etc.)
- Basic knowledge of HTML, CSS, and JavaScript
- Familiarity with Git and GitHub

### Setting Up Development Environment

1. Fork and clone the repository:
```bash
git clone https://github.com/yourusername/SpatialSimulator.git
cd SpatialSimulator
```

2. Open `index.html` in your browser to see the application

3. Make changes to the code and refresh the browser to see updates

That's it! No build process or dependencies to install.

## 📁 Code Structure

### File Organization

```
SpatialSimulator/
├── index.html          # Main HTML structure
├── styles.css          # All CSS styling
├── app.js             # JavaScript application logic
├── README.md          # Main documentation
├── CONTRIBUTING.md    # This file
└── LICENSE            # License information
```

### Application Architecture

The application follows a simple, modular architecture:

#### `index.html`
- Defines the page structure
- Contains semantic HTML5 markup
- Includes all UI elements (sidebar, map, modals)
- Loads external libraries (Leaflet.js)

#### `styles.css`
- Uses CSS variables for theming (see `:root` section)
- Follows mobile-first responsive design
- Organized by component sections
- Includes utility classes

#### `app.js`
Main sections:
1. **Application State** (`AppState` object)
   - Stores all application data
   - Manages map instance
   - Tracks elements and layers

2. **Initialization Functions**
   - `initializeMap()`: Sets up Leaflet map
   - `initializeEventListeners()`: Binds UI events
   - `initializeTutorial()`: Prepares tutorial system

3. **Element Management**
   - Functions for adding POIs, agents, zones, connections
   - Render functions for each element type
   - Removal functions

4. **Scenarios**
   - Pre-defined educational exercises
   - Each scenario has its own function

5. **Utilities**
   - Helper functions for calculations
   - Icon and color mapping
   - Distance calculations

6. **Tutorial System**
   - Step-based walkthrough
   - Modal management

## 🤝 How to Contribute

### Types of Contributions Welcome

1. **Bug Fixes**
   - Fix UI issues
   - Correct calculation errors
   - Improve browser compatibility

2. **New Features**
   - Additional scenarios
   - New element types
   - Enhanced visualizations
   - Data import/export improvements

3. **Documentation**
   - Improve README
   - Add code comments
   - Create tutorials
   - Translate to other languages

4. **Educational Content**
   - Design new scenarios
   - Create lesson plans
   - Develop exercises

### Contribution Workflow

1. **Create an Issue**
   - Describe the bug or feature
   - Explain why it's needed
   - Discuss approach if complex

2. **Fork and Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**
   - Write clean, commented code
   - Follow existing code style
   - Test thoroughly

4. **Commit**
   ```bash
   git add .
   git commit -m "Add: Brief description of changes"
   ```
   Use commit prefixes:
   - `Add:` for new features
   - `Fix:` for bug fixes
   - `Update:` for improvements
   - `Docs:` for documentation

5. **Push and Create Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```
   - Provide clear PR description
   - Reference related issues
   - Add screenshots for UI changes

## 💻 Coding Standards

### JavaScript Style Guide

```javascript
// Use meaningful variable names
const userLocation = [lat, lon];  // Good
const ul = [lat, lon];            // Bad

// Add comments for complex logic
/**
 * Calculate distance between two lat/lng points using Haversine formula
 * @param {Array} point1 - [lat, lon] of first point
 * @param {Array} point2 - [lat, lon] of second point
 * @returns {Number} Distance in kilometers
 */
function calculateDistance(point1, point2) {
    // Implementation...
}

// Use const by default, let when needed, avoid var
const PI = 3.14159;
let counter = 0;

// Prefer template literals
const message = `Location: ${lat}, ${lon}`;  // Good
const message = 'Location: ' + lat + ', ' + lon;  // Bad

// Use arrow functions for callbacks
elements.forEach(element => {
    console.log(element);
});
```

### HTML Best Practices

```html
<!-- Use semantic HTML -->
<header>...</header>  <!-- Good -->
<div class="header">...</div>  <!-- Less ideal -->

<!-- Include ARIA labels for accessibility -->
<button aria-label="Close modal" class="close-modal">&times;</button>

<!-- Use meaningful IDs and classes -->
<div id="poi-list" class="element-list"></div>
```

### CSS Guidelines

```css
/* Use CSS variables for theming */
:root {
    --primary-color: #2563eb;
}

.button {
    background-color: var(--primary-color);
}

/* Follow BEM-like naming for complex components */
.element-item { }
.element-item-name { }
.element-item-type { }

/* Mobile-first responsive design */
.container {
    padding: 1rem;
}

@media (min-width: 768px) {
    .container {
        padding: 2rem;
    }
}
```

## ✨ Adding Features

### Adding a New Element Type

1. **Update HTML** (`index.html`)
```html
<!-- Add option to dropdown -->
<select id="poi-type">
    <option value="library">📚 Library</option>
</select>
```

2. **Update JavaScript** (`app.js`)
```javascript
// Add icon mapping
function getPOIIcon(type) {
    const icons = {
        library: '📚',
        // ... existing icons
    };
    return icons[type] || '📍';
}

// Add label mapping
function getTypeLabel(type) {
    const labels = {
        library: 'Library',
        // ... existing labels
    };
    return labels[type] || type;
}
```

### Adding a New Scenario

1. **Update HTML** (`index.html`)
```html
<div class="scenario-card">
    <h4>🎯 Your New Scenario</h4>
    <p>Description of the scenario.</p>
    <button class="btn-scenario" data-scenario="your-scenario">Start Scenario</button>
</div>
```

2. **Update JavaScript** (`app.js`)
```javascript
function runScenario(scenarioType) {
    switch(scenarioType) {
        case 'your-scenario':
            yourNewScenario();
            break;
        // ... existing scenarios
    }
}

function yourNewScenario() {
    showInfo(`
        <h4>🎯 Your New Scenario</h4>
        <p>Instructions for users...</p>
        <ol>
            <li>Step 1</li>
            <li>Step 2</li>
        </ol>
    `);
    
    // Add scenario logic here
}
```

### Adding a Tutorial Step

```javascript
// In app.js, update the TutorialSteps array
const TutorialSteps = [
    // ... existing steps
    {
        title: "Your New Tutorial Step",
        content: `
            <p>Content of your tutorial step...</p>
            <ul>
                <li>Point 1</li>
                <li>Point 2</li>
            </ul>
        `
    }
];
```

## 🧪 Testing

### Manual Testing Checklist

Before submitting a PR, test:

- [ ] Works in Chrome
- [ ] Works in Firefox
- [ ] Works in Safari (if available)
- [ ] Works in Edge
- [ ] Mobile responsive (use browser dev tools)
- [ ] All buttons work
- [ ] No console errors
- [ ] Tutorial flows correctly
- [ ] Elements can be added and removed
- [ ] Map interactions work
- [ ] Export functionality works

### Browser Testing

Use browser developer tools:

1. **Console**: Check for JavaScript errors
2. **Network**: Verify external resources load
3. **Responsive Design Mode**: Test mobile layouts
4. **Accessibility**: Check screen reader compatibility

### Cross-Browser Issues

Common issues to watch for:
- CSS Grid/Flexbox support
- Modern JavaScript features (use ES6+)
- Geolocation API permissions
- LocalStorage availability

## 🎨 Design Guidelines

### Color Palette

Follow the established color scheme:
- Primary: Blue (`#2563eb`)
- Secondary: Green (`#10b981`)
- Accent: Orange (`#f59e0b`)
- Danger: Red (`#ef4444`)

### Icons

Use emoji icons for consistency:
- Keep them semantic (🏫 for school, 🏥 for hospital)
- Ensure they work across platforms
- Maintain similar visual weight

### Spacing

Use the spacing scale:
- 0.25rem (4px) - tiny gaps
- 0.5rem (8px) - small gaps
- 1rem (16px) - medium gaps
- 1.5rem (24px) - large gaps
- 2rem (32px) - section spacing

## 📝 Documentation

When adding features, update:

1. **Code Comments**: Explain complex logic
2. **README.md**: Document user-facing features
3. **CONTRIBUTING.md**: Add development guidelines
4. **In-app Help**: Update help text if needed

### Comment Style

```javascript
/**
 * Function description
 * @param {Type} paramName - Parameter description
 * @returns {Type} Return value description
 */
function myFunction(paramName) {
    // Implementation
}
```

## 🌍 Internationalization

To add language support:

1. Extract all user-facing strings
2. Create translation files
3. Implement language switcher
4. Update documentation

(Future enhancement - contributions welcome!)

## 🐛 Reporting Bugs

When reporting bugs, include:

1. **Description**: What happened vs. what should happen
2. **Steps to Reproduce**: How to trigger the bug
3. **Browser/OS**: What you're using
4. **Screenshots**: Visual bugs benefit from images
5. **Console Errors**: Any JavaScript errors

## 💡 Feature Requests

When requesting features:

1. **Use Case**: Why is this needed?
2. **Proposed Solution**: How might it work?
3. **Alternatives**: Other approaches considered?
4. **Impact**: Who benefits from this?

## 📞 Getting Help

- Check existing issues and documentation
- Ask questions in issue discussions
- Review code comments for implementation details

## 🙏 Thank You!

Every contribution helps make spatial education more accessible. Whether you're fixing a typo, adding a feature, or improving documentation, your work is valued!

---

Happy contributing! 🚀
