#import the COCO Evaluator to use the COCO Metrics
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from detectron2.data import build_detection_test_loader
from detectron2.data.datasets import register_coco_instances
from detectron2.evaluation import COCOEvaluator, inference_on_dataset

#register your data
register_coco_instances("my_dataset_train", {}, "/code/detectron2/detectron2/instances_train2017.json", "/code/detectron2/detectron2/train2017")
register_coco_instances("my_dataset_val", {}, "/code/detectron2/detectron2/instances_val2017.json", "/code/detectron2/detectron2/val2017")
register_coco_instances("my_dataset_test", {}, "/code/detectron2/detectron2/instances_test2017.json", "/code/detectron2/detectron2/test2017")

#load the config file, configure the threshold value, load weights 
cfg = get_cfg()
cfg.merge_from_file("/code/detectron2/detectron2/output/custom_mask_rcnn_X_101_32x8d_FPN_3x_Iteration_3_dataset.yaml")
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model
cfg.MODEL.WEIGHTS = "/code/detectron2/detectron2/output/model_final.pth"

# Create predictor
predictor = DefaultPredictor(cfg)

#Call the COCO Evaluator function and pass the Validation Dataset
evaluator = COCOEvaluator("my_dataset_test", cfg, False, output_dir="./output/")
val_loader = build_detection_test_loader(cfg, "my_dataset_test")

#Use the created predicted model in the previous step
inference_on_dataset(predictor.model, val_loader, evaluator)