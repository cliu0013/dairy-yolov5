import torch
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
model.eval()


def detect(img):
    """img is a numpy array, return type models.common.Detections (.save, .show, .print, etc.)"""
    return model(img)
