import torch
from ultralytics import YOLO
import numpy as np
from cfg_manager import *

class ObjectDetection:
    def __init__(self):
        super().__init__()
        
        # checking cuda is available or not
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print(f"Using Device: {self.device}\n")

        # loading model
        self.model = self._load_model()

        # get model classes names
        self.cls_names = self.model.names

        # setting output destination path
        if MODEL_SETTINGS['destination'] != None:
            self.dst = MODEL_SETTINGS['destination']

    # initialize model
    def _load_model(self):
        
        # if model path is not set, use the pretrained model
        if MODEL_SETTINGS['model_path'] == None:
            print(f"Using pretrianed model: yolov8n.pt")
            model = YOLO('yolov8n.pt')
        else:
            print(f"Loading model from {Path('/') / Path.cwd() / MODEL_SETTINGS['model_path']}")
            model = YOLO(MODEL_SETTINGS['model_path'])
        
        if MODEL_SETTINGS['model_fuse']:
            model.fuse()
            print('\n')

        return model

    # Start predicting images and return the results as a list
    def predict(self) -> list:
        results = self.model.predict(**PREDICT_SETTINGS)
        return results
