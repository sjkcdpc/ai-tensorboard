#!/usr/bin/env python
# encoding: utf-8

"""
@author: dongsheng.ma
@contact: 1455975151@qq.com
@site: https://www.mdslq.cn/
@software: PyCharm
@file: example2.py
@time: 2023/2/22 11:12 上午
"""


import torch
from torch.autograd import Variable
import torch.nn.functional as functional
from tensorboardX import SummaryWriter

import matplotlib.pyplot as plt
import numpy as np

# x的shape大小
x = torch.from_numpy(np.linspace(-1, 1, 50).reshape([50, 1])).type(torch.FloatTensor)
# y的shape大小
y = torch.sin(x) + 0.2 * torch.rand(x.size())


class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        # Applies a linear transformation to the incoming data: :math:y = xA^T + b
        # 全连接层，公式为y = xA^T + b
        self.hidden = torch.nn.Linear(n_feature, n_hidden)
        self.predict = torch.nn.Linear(n_hidden, n_output)

    def forward(self, x):
        # 隐含层的输出
        hidden_layer = functional.relu(self.hidden(x))
        output_layer = self.predict(hidden_layer)
        return output_layer


# 类的建立
net = Net(n_feature=1, n_hidden=10, n_output=1)

writer = SummaryWriter(comment='tensorboard_example02',)
graph_inputs = torch.from_numpy(np.random.rand(2, 1)).type(torch.FloatTensor)
writer.add_graph(net, (graph_inputs,))

# torch.optim是优化器模块
optimizer = torch.optim.Adam(net.parameters(), lr=1e-3)

# 均方差loss
loss_func = torch.nn.MSELoss()

for t in range(2000):
    prediction = net(x)
    loss = loss_func(prediction, y)

    # 反向传递步骤
    # 1、初始化梯度
    optimizer.zero_grad()
    # 2、计算梯度
    loss.backward()
    # 3、进行optimizer优化
    optimizer.step()

    writer.add_scalar('loss', loss, t)

writer.close()

