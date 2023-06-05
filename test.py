import torch
from PIL import Image
from torchvision.transforms import functional as F


# 加载模型
model = torch.hub.load('ultralytics/yolov5', 'custom', path_or_model='runs/train/exp5/weights/best.pt')

# 进行目标检测
results = model(image_tensor)
image = cv2.imread('to_be_detected/缺失001.jpg.jpg')

# 执行目标检测
results = model(image)
class_name = results.pandas().xyxy[0]['name']
print(class_name)
