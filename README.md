# Weather Dashboard - GOES Satellite Animations

A real-time weather dashboard featuring live GOES satellite imagery, weather forecasts, and severe weather alerts. Built with vanilla HTML, CSS, and JavaScript.

## Features

### 🌤️ Weather Information
- **Current Conditions**: Real-time temperature, weather description, wind, and humidity
- **7-Day Forecast**: Detailed weather predictions with clickable links to NOAA graphical forecasts
- **Location Management**: Easy ZIP code updates with automatic coordinate conversion
- **Dynamic Forecast Maps**: Temperature and precipitation forecast maps that update based on selected location

### 🛰️ Satellite Imagery
- **Live GOES-19 Animations**: 24-frame animations showing weather patterns over time
- **Multiple Satellite Bands**: 
  - CONUS GeoColor (true color view of the US)
  - Snow/Ice Detection
  - Day/Night Cloud Combo
  - Full Disk GeoColor
  - Air Mass RGB
  - Sandwich RGB
  - Ozone Detection
  - Water Vapor (Lower, Mid, Upper)
  - Dust RGB
- **Interactive Controls**: Hover to pause animations, click to open full NOAA pages

### ⚠️ Weather Alerts
- **Severe Weather Warnings**: Real-time alerts from NOAA Weather Service
- **Dismissible Alerts**: Click the × button to close individual warnings
- **Color-Coded Severity**: Different colors for minor, warning, and watch alerts

### 🎨 User Interface
- **Responsive Design**: Optimized for desktop viewing
- **Dark Theme**: Easy on the eyes for extended viewing
- **Grid Layout**: Organized satellite imagery in a 4-column grid
- **Hover Effects**: Interactive overlays with satellite band information

## Setup

### Prerequisites
- Python 3.x (for local development server)
- Modern web browser with JavaScript enabled

### Installation
1. Clone or download the project files
2. Navigate to the project directory
3. Start the local development server:
   ```bash
   python3 -m http.server 8000
   ```
4. Open your browser and navigate to `http://localhost:8000`

## Usage

### Changing Location
1. Click the "Change" button next to the current ZIP code
2. Enter a new 5-digit ZIP code
3. Click "Update" or press Enter
4. The dashboard will automatically update with weather data for the new location

### Viewing Satellite Imagery
- **Hover** over any satellite image to pause the animation
- **Click** on any satellite image to open the full NOAA page with detailed information
- **Forecast Maps**: Click the "Temperature Forecast Map" or "Precipitation Forecast Map" links for interactive NOAA maps

### Managing Alerts
- **View**: Weather alerts appear at the top of the dashboard when active
- **Dismiss**: Click the × button on any alert to remove it from view
- **Severity Levels**: 
  - Minor (gray): Low-impact weather events
  - Warning (yellow): Moderate weather threats
  - Watch (orange): Severe weather conditions

## Data Sources

- **Weather Data**: NOAA National Weather Service API
- **Satellite Imagery**: GOES-19 satellite via NOAA STAR
- **Geocoding**: Zippopotam.us API for ZIP code to coordinate conversion
- **Forecast Maps**: NOAA Digital Weather.gov

## Technical Details

- **Frontend**: Vanilla HTML5, CSS3, JavaScript (ES6+)
- **APIs**: RESTful APIs with fetch() for data retrieval
- **Animations**: Custom frame-based animation system
- **Responsive**: CSS Grid and Flexbox for layout
- **No Dependencies**: Pure vanilla web technologies

## File Structure

```
weatherpage/
├── index.html          # Main dashboard interface
├── styles.css          # Styling and layout
├── README.md           # Project documentation
└── links.txt           # External resource links
```

## Browser Compatibility

- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the dashboard. 