import pyqrcode
import png
from pyqrcode import QRCode

qr_url = "https://www.facebook.com/stoyan.stoyanov.505"
url = pyqrcode.create(qr_url)
url.png("my_qrcode.png", scale=8)
