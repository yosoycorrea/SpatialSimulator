# Deployment Guide - Spatial Simulator Lite

## 📦 Deployment Options

### Option 1: Direct File Access (Simple - Recommended for Testing)

**Best for**: Quick testing, local development, offline demos

1. Simply open `index.html` in a web browser
2. Works with Chrome, Firefox, Safari, Edge
3. Requires internet connection for CDN libraries (Leaflet.js, OpenStreetMap)

**Steps**:
```bash
# Just open the file
open index.html  # macOS
start index.html  # Windows
xdg-open index.html  # Linux
```

**Note**: Some browsers may block certain features (geolocation, external resources) when opening files directly. For full functionality, use a local server (Option 2).

### Option 2: Local HTTP Server (Recommended for Full Functionality)

**Best for**: Development, full testing with all features

Using Python:
```bash
# Python 3
python3 -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

Using Node.js:
```bash
# Install http-server globally
npm install -g http-server

# Run server
http-server -p 8000
```

Using PHP:
```bash
php -S localhost:8000
```

Then open: `http://localhost:8000/index.html`

### Option 3: Web Hosting (For Production/Sharing)

**Best for**: Sharing with students, public access, production use

#### GitHub Pages (Free)
1. Push the repository to GitHub
2. Go to repository Settings > Pages
3. Select branch and root folder
4. Your site will be available at `https://username.github.io/SpatialSimulator`

#### Netlify (Free)
1. Drag and drop the entire folder to Netlify
2. Or connect your GitHub repository
3. Automatic deployment on every commit

#### Vercel (Free)
1. Install Vercel CLI: `npm install -g vercel`
2. Run `vercel` in the project directory
3. Follow the prompts

#### Traditional Web Hosting
Upload all files to your web server via FTP/SFTP:
- `index.html`
- `styles.css`
- `app.js`
- `README.md`
- `CONTRIBUTING.md`
- `LICENSE`

## 🌐 CDN Dependencies

The application uses these external libraries loaded via CDN:

- **Leaflet.js** (v1.9.4): Interactive maps
  - CSS: `https://unpkg.com/leaflet@1.9.4/dist/leaflet.css`
  - JS: `https://unpkg.com/leaflet@1.9.4/dist/leaflet.js`
- **OpenStreetMap Tiles**: Map visualization
- **Nominatim API**: Geocoding (address search)

### For Offline/Intranet Deployment

If you need to run completely offline or on an intranet:

1. **Download Leaflet.js locally**:
```bash
mkdir lib
cd lib
# Download Leaflet
wget https://unpkg.com/leaflet@1.9.4/dist/leaflet.css
wget https://unpkg.com/leaflet@1.9.4/dist/leaflet.js
wget https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png
wget https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png
wget https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png
```

2. **Update index.html** to use local files:
```html
<!-- Replace CDN links with local -->
<link rel="stylesheet" href="lib/leaflet.css" />
<script src="lib/leaflet.js"></script>
```

3. **For map tiles**, you'll need to:
   - Set up a local tile server (e.g., using TileServer GL)
   - Or use a different tile source that's available on your network

## ⚙️ Configuration

### Customizing Default Map Center

Edit `app.js`, line ~138:
```javascript
// Change default coordinates (currently New York City)
AppState.map = L.map('map').setView([40.7128, -74.0060], 13);
```

### Changing Color Theme

Edit `styles.css`, lines 7-17:
```css
:root {
    --primary-color: #2563eb;  /* Main blue color */
    --secondary-color: #10b981; /* Green accent */
    --accent-color: #f59e0b;    /* Orange */
    /* ... modify as needed */
}
```

### Adding Custom Scenarios

See `CONTRIBUTING.md` for detailed instructions on adding new scenarios.

## 🔒 Security Considerations

### For Public Deployment

1. **HTTPS**: Always use HTTPS for production deployments
2. **CSP Headers**: Consider adding Content Security Policy headers
3. **Input Validation**: The app validates user inputs, but always sanitize on server if adding backend
4. **API Rate Limits**: Be aware of Nominatim API usage limits (1 request/second)

### Privacy

- No user data is collected or stored on servers
- All processing happens in the browser
- Geocoding requests go to OpenStreetMap's Nominatim service
- No cookies or tracking

## 📱 Mobile Optimization

The application is responsive and works on mobile devices, but for best experience:
- Use landscape orientation on phones
- Tablets provide ideal screen size
- Desktop/laptop recommended for educational settings

## 🌍 Browser Requirements

### Minimum Versions
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

### Required Features
- ES6 JavaScript support
- CSS Grid and Flexbox
- HTML5 Canvas (for future features)
- Geolocation API (optional, for location services)
- LocalStorage (for future features)

## 🐛 Troubleshooting

### Map doesn't appear
- Check browser console for errors
- Verify internet connection (for CDN resources)
- Try a different browser
- Check browser security settings (may block external resources)

### Geolocation not working
- Ensure HTTPS connection (required for geolocation)
- Grant location permissions in browser
- Try manual location input instead

### Performance issues
- Limit number of elements on map
- Use modern browser
- Close other browser tabs
- Check internet speed (for tile loading)

## 📊 Monitoring and Analytics

If you want to add analytics (optional):

1. **Google Analytics**: Add tracking code to `index.html`
2. **Plausible/Fathom**: Privacy-friendly alternatives
3. **Self-hosted**: Matomo, Umami

**Important**: Always disclose analytics to users and comply with privacy regulations (GDPR, CCPA, etc.)

## 🔄 Updates and Maintenance

To update the application:

1. Pull latest changes from repository
2. Review CHANGELOG (if available)
3. Test in staging environment
4. Deploy to production
5. Clear browser caches if needed

## 💾 Backup

Recommended backup items:
- All application files
- User-generated content (if storing)
- Configuration files
- Custom scenarios/modifications

## 📧 Support

For deployment issues:
- Check the README.md
- Review browser console errors
- Check GitHub Issues
- Consult CONTRIBUTING.md for development setup

---

**Need help?** Open an issue on GitHub or consult the documentation.
