import urllib.request
from datetime import datetime

from schedule import every

IMG_URL = 'https://your.image/url.jpg'
INTERVAL_SECONDS = 60 * 15  # every 15 minutes


def download_and_store_image():
    filename = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    path = f'./download/{filename}.jpg'
    urllib.request.urlretrieve(IMG_URL, path)


print('▶ Scheduled')
every(INTERVAL_SECONDS, download_and_store_image)
