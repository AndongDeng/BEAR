import torch
import torch.nn as nn

def setup_seed(seed):
     torch.manual_seed(seed)
     torch.cuda.manual_seed_all(seed)
     torch.backends.cudnn.deterministic = True

setup_seed(20)

x_2d = torch.randn(1, 3, 32, 32)
x_3d = torch.stack([x_2d]*8, dim=2)

conv_2d = nn.Conv2d(3, 7, kernel_size=3, padding=1)
conv_2d.weight = nn.Parameter(torch.ones_like(conv_2d.weight))
conv2d_weight = conv_2d.weight
conv3d_weight = torch.stack([conv_2d.weight]*3, dim=2) / 3
conv_3d = nn.Conv3d(3, 7, kernel_size=(3, 3, 3), padding=1)
conv_3d.weight = nn.Parameter(conv3d_weight)

bias = nn.Parameter(torch.ones_like(conv_2d.bias))
conv_2d.bias = bias
conv_3d.bias = bias

y2d = conv_2d(x_2d)
y3d = conv_3d(x_3d)

# print(y2d.size(), y2d)
# print('='*100)
# print(y3d.size(), y3d)
print('='*100)
print('y 2d output')
print(y2d[0, 0, :, :])
for i in range(7):
    print('='*100)
    print('y 3d output index{}'.format(i))
    print(y3d[0, 0, i, :, :])

