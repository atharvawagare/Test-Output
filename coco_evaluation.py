#import the COCO Evaluator to use the COCO Metrics
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from detectron2.data import build_detection_test_loader
from detectron2.data.datasets import register_coco_instances
from detectron2.evaluation import COCOEvaluator, inference_on_dataset

#register your data
#register_coco_instances("my_dataset_train", {}, "./detectron2/coco/annotations/instances_train2017.json", "./detectron2/coco/train2017")
#register_coco_instances("my_dataset_val", {}, "./detectron2/coco/annotations/instances_val2017.json", "./detectron2/coco/val2017")
#register_coco_instances("my_dataset_test", {}, "./detectron2/coco/annotations/instances_val2017_100.json", "./detectron2/coco/val2017")
register_coco_instances("my_dataset_test", {}, "./datasets/coco/annotations/instances_val2017_100.json", "./datasets/coco/val2017")

#load the config file, configure the threshold value, load weights 
cfg = get_cfg()
cfg.merge_from_file("./configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model
cfg.MODEL.WEIGHTS = "/root/.torch/iopath_cache/detectron2/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl"

# Create predictor
predictor = DefaultPredictor(cfg)

#Call the COCO Evaluator function and pass the Validation Dataset
evaluator = COCOEvaluator("my_dataset_test", cfg, False, output_dir="./output/")
val_loader = build_detection_test_loader(cfg, "my_dataset_test")

#Use the created predicted model in the previous step
inference_on_dataset(predictor.model, val_loader, evaluator)
