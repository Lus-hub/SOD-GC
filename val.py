import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('/Object_detection/LS/yolo11/yolo11-3/ultralytics-yolo11-main/runs/train/kitti-all4/weights/best.pt') # 选择训练好的权重路径
    model.val(data='/Object_detection/LS/yolo11/yolo11-1/ultralytics/cfg/datasets/kitti.yaml',
              split='val', # split可以选择train、val、test 根据自己的数据集情况来选择.
              imgsz=640,
              batch=16,
              device='1',
              # iou=0.7,
              # rect=False,
              save_json=True, # if you need to cal coco metrice
              project='runs/val',
              name='kitti-all4',
              )