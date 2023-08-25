# Consisaug: A Consistency-based Augmentation for Polyp Detection in Endoscopy Image Analysis (MIML2023)

## 1. Data preparation 
The code is changed from yolov5, and the detection for the data format is yolov5.
Download pretrained yolov5 checkpoint from [yolov5](https://github.com/ultralytics/yolov5) responsitory and move them to ./trained_model.
Change the data configuration file [coco.yaml](data/coco.yaml).
The hyper-parameter file is [hyp.scratch-high.yaml](data/hyps/hyp.scratch-high.yaml).


## 2. Train
```Shell
python train.py
```

## 3. Validation
```Shell
python val.py
```

## 4. Test
```Shell
python detect.py
```