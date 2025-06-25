from flask import Flask, Response, send_file
import requests
from io import BytesIO

app = Flask(__name__)

GIF_URLS = {
    'TemperatureLoop.gif': 'https://graphical.weather.gov/images/conus/TemperatureLoop.gif',
    'PrecipitationLoop.gif': 'https://graphical.weather.gov/images/conus/PrecipitationLoop.gif',
}

@app.route('/proxy/<gif_name>')
def proxy_gif(gif_name):
    url = GIF_URLS.get(gif_name)
    if not url:
        return 'Not found', 404
    r = requests.get(url, stream=True)
    if r.status_code != 200:
        return 'Failed to fetch', 502
    return Response(r.content, mimetype='image/gif', headers={
        'Cache-Control': 'public, max-age=600',
        'Content-Disposition': f'inline; filename="{gif_name}"'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001) 