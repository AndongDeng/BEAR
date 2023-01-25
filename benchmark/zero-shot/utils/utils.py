import torch
import clip
from data import prompts


# def accuracy(output, target, topk=(1,)):
#     """Computes the accuracy over the k top predictions for the specified values of k"""
#     with torch.no_grad():
#         maxk = max(topk)
#         batch_size = target.size(0)

#         _, pred = output.topk(maxk, 1, True, True)
#         pred = pred.t()
#         correct = pred.eq(target.view(1, -1).expand_as(pred))

#         for k in topk:
#             correct_k = correct[:k].reshape(-1).float().sum(0, keepdim=True)
#         return correct_k


@torch.no_grad()
def accuracy(output, target, topk=(1,)):
    pred = output.topk(max(topk), 1, True, True)[1].t()
    correct = pred.eq(target.view(1, -1).expand_as(pred))
    return [float(correct[:k].reshape(-1).float().sum(0, keepdim=True).cpu().numpy()) for k in topk]


@torch.no_grad()
def extract_text_features(model, class_names, templates, device):
    # code borrowed from: https://github.com/openai/CLIP/blob/fcab8b6eb92af684e7ff0a904464be7b99b49b88/notebooks/Prompt_Engineering_for_ImageNet.ipynb
    model.to(device)
    model.eval()

    zeroshot_weights = []
    for classname in class_names:
        texts = [template.format(classname) for template in templates]
        texts = clip.tokenize(texts).to(device)
        class_embeddings = model.encode_text(texts)
        class_embeddings /= class_embeddings.norm(dim=-1, keepdim=True)
        class_embedding = class_embeddings.mean(dim=0)
        class_embedding /= class_embedding.norm()
        zeroshot_weights.append(class_embedding)
    zeroshot_weights = torch.stack(zeroshot_weights, dim=1).to(device)
    return zeroshot_weights


def get_templates(dataset):
    if dataset in ['ucf101', 'xd_violence', 'hacs', 'mini_sports1m', 'mod20', 'coin']:
        templates = prompts.ucf101_templates
    elif dataset == 'ucf_crime':
        templates = prompts.ucf_crime_templates
    elif dataset == 'muvim':
        templates = prompts.muvim_templates
    elif dataset == 'wlasl':
        templates = prompts.wlasl_templates
    elif dataset == 'jester':
        templates = prompts.jester_templates
    elif dataset == 'uav_human':
        templates = prompts.uav_human_templates
    elif dataset == 'charades_ego':
        templates = prompts.charades_ego_templates
    elif dataset == 'toyota_smarthome':
        templates = prompts.toyota_smarthome_templates
    elif dataset == 'mpii_cooking':
        templates = prompts.mpii_cooking_templates
    elif dataset == 'fine_gym':
        templates = prompts.fine_gym_templates
    elif dataset == 'meccano':
        templates = prompts.meccano_templates
    elif dataset == 'inhard':
        templates = prompts.inhard_templates
    elif dataset == 'petraw':
        templates = prompts.petraw_templates  
    elif dataset == 'misaw':
        templates = prompts.misaw_templates
    return templates