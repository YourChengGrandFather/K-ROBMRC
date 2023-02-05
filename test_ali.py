# from model.KGBert import KGBert
# print(KGBert)
# from easynlp.appzoo import ClassificationDataset
# from easynlp.appzoo import get_application_model, get_application_evaluator
# from easynlp.core import Trainer
# from easynlp.utils import initialize_easynlp, get_args
# from easynlp.utils.global_vars import parse_user_defined_parameters
# from easynlp.utils import get_pretrain_model_path

# initialize_easynlp()
# # args = get_args()
# # args.app_name = 
# user_defined_parameters = parse_user_defined_parameters('pretrain_model_name_or_path=alibaba-pai/pai-dkplm-medical-small-zh')
# model = get_application_model(app_name="text_classify",
#                               pretrained_model_name_or_path=get_pretrain_model_path("alibaba-pai/pai-dkplm-medical-small-zh"),
#                               num_labels=2,
#                               user_defined_parameters=user_defined_parameters)

# print('model', model.parameters)
import torch
print(torch.cuda.device_count())

print(torch.cuda.is_available())