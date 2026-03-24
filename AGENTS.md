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
- **NOAA CDN serves `Access-Control-Allow-Origin: *`**, so satellite images load directly from `cdn.star.nesdis.noaa.gov` without any proxy. No reverse proxy is needed for local development.
- **Satellite image timestamps** are computed from the current UTC time. CONUS GEOCOLOR images appear at 5-minute intervals (minutes 01, 06, 11, ...), Full Disk images at 10-minute intervals (00, 10, 20, ...), and EXTENT3 Lightning Mapper at 5-minute intervals (01, 06, 11, ...). If images don't load, the timestamp calculation is likely hitting a gap — check the CDN directory listing to verify available timestamps.
- **`proxy_gif.py`** is optional — it proxies two specific NOAA GIF URLs for the Temperature/Precipitation forecast map modals. The upstream NOAA server may sometimes return errors (502); this is not a code bug.
- The entire application logic lives inside `index.html` (inline `<script>` block, ~1500 lines of JS). There is no separate JS file.
