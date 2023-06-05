from flask import Flask,  request, send_file
from PIL import Image
import detect
app = Flask(__name__)
i=1

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    
    # 保存上传的图片到服务器
    image = Image.open(file)
    image.save('to_be_detected/uploaded.jpg')
    opt = parse_opt()
    main(opt)
    # 从本地读取处理后的图片并传送到前端
    return send_file('runs/detect/exp'+str(i)+'.jpg',mimetype='image/jpg')

if __name__ == '__main__':
    app.run()
