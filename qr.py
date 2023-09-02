# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode


# String which represents the QR code
s = "file:///D:/TRF%20Level2/TRFqr.html"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg("TRFqr.svg", scale = 8)

# Create and save the png file naming "myqr.png"
url.png('TRFqr.png', scale = 6)


