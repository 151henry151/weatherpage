# AGENTS.md

## Cursor Cloud specific instructions

### Product overview
Weather Dashboard — a vanilla HTML/CSS/JS single-page app displaying live GOES-19 satellite imagery, NOAA forecasts, and severe weather alerts. No build step, no bundler, no Node.js dependencies.

### Running the development server
```bash
python3 -m http.server 8000          # serves index.html + styles.css on http://localhost:8000
python3 proxy_gif.py                  # Flask proxy for NOAA forecast GIFs on port 5001
```
Both commands should be started from the repo root (`/workspace`).

### Python dependencies
Only `flask` and `requests` are needed (for `proxy_gif.py`). Install with:
```
pip3 install flask requests
```

### Key caveats
- **No linter / test suite / build step exists.** The project is pure vanilla HTML/CSS/JS with no package manager or config files. There is nothing to lint or unit-test.
- **Satellite imagery requires internet access.** All data comes from public NOAA APIs (`api.weather.gov`, `cdn.star.nesdis.noaa.gov`). The app cannot function offline.
- **CONUS GeoColor satellite panel** expects a reverse proxy at path `/weatherpage/proxy-satellite/...` to reach `cdn.star.nesdis.noaa.gov`. This proxy is not included in the repo, so the satellite animation tile on the left will show a broken image in local dev. The temperature/precipitation forecast maps and all weather data still work fine.
- **`proxy_gif.py`** is optional — it proxies two specific NOAA GIF URLs for the Temperature/Precipitation forecast map modals. The upstream NOAA server may sometimes return errors (502); this is not a code bug.
- The entire application logic lives inside `index.html` (inline `<script>` block, ~1500 lines of JS). There is no separate JS file.
