
from roboflow import Roboflow
rf = Roboflow(api_key="V5u5WlopyccC1Ddp24tB")
project = rf.workspace("salo7ty").project("safety-helmet-q3b8o-zlhhn")
version = project.version(1)
dataset = version.download("yolov11")
                