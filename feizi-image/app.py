from flask import Flask, request, render_template
from PIL import Image, ImageDraw
import numpy as np
import io, base64
app = Flask(__name__)

seg = []

@app.route('/', methods = ['GET', 'POST'])
def index():
   if request.method == 'POST':
      images = request.files.getlist("file")
      img_data = []
      for img in images:
         img_object = Image.open(img)
         buffered = io.BytesIO()
         img_object.save(buffered, format="JPEG")
         img_data.append(base64.b64encode(buffered.getvalue()).decode())
      return render_template('segment.html', image_data=img_data)
   else:
      return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True)
