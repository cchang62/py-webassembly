import matplotlib.pyplot as plt
import io
import base64

def generate_line_image():
    plt.figure()
    plt.plot([0, 1, 2, 3], [0, 1, 4, 9])
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')
