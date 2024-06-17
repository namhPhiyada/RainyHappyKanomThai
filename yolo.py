from ultralytics import YOLO

datapath = r"C:\Users\LENOVO\Desktop\pro\img"
model = YOLO("yolov8m-cls.pt")
result = model.train(data=datapath, epochs=1, imgsz=640)
