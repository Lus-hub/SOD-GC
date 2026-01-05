# import os
# os.environ['CUDA_VISIBLE_DEVICES']='1'
import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO


if __name__ == '__main__':
    prefix = 'kitti-'
    for yaml_name in ['SOD-GC']:
        model = YOLO(f'/***/{yaml_name}.yaml')
        model.train(data='/***/datasets/kitti.yaml',
                    # cache=False,
                    imgsz=640,
                    epochs=100,
                    batch=16,
                    close_mosaic=0,
                    workers=32,
                    device=0,
                    optimizer='SGD',  # using SGD
                    # patience=0, # set 0 to close earlystop.
                    # resume=True, # 断点续训,YOLO初始化时选择last.pt
                    # amp=False, # close amp
                    # fraction=0.2,
                    project='runs/train/',
                    name=f'{prefix}{yaml_name}',
                    # name='exp'
                    )
        #'RFPN-EIE'有问题
# if __name__ == '__main__':
#     model = YOLO("/Object_detection/LS/yolo11/yolo11-2/ultralytics/cfg/models/my/yolo11x.yaml")
#     # model = YOLOv10("/Object_detection/YJ/v8/ultralytics/cfg/models/v10/yolov10l-transcpca.yaml")
#     model.train(data="/Object_detection/LS/yolo11/yolo11-1/ultralytics/cfg/datasets/kitti.yaml",
#                 epochs=100,
#                 imgsz=640,
#                 batch=16,
#                 device=[0],
#                 optimizer='SGD',
#                 close_mosaic=0,
#                 project="runs/train/",
#                 name="kitti-GCYOLOx",
#                 workers = 32)  # 训练