import io
import qrcode
from PIL import Image
import sys
sys.path.insert(0, "..") 
import config
box_size = config.QR_BOX_SIZE
border = config.QR_BORDER

def generate_qr(data):
    qr = qrcode.QRCode(version=1, box_size=box_size, border=border)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')

    # QR kodu resmini bellekte oluştur
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    qr_image = buffered.getvalue()
    return qr_image



