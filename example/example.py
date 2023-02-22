#!/usr/bin/env python
# encoding: utf-8

"""
@author: dongsheng.ma
@contact: 1455975151@qq.com
@site: https://www.mdslq.cn/
@software: PyCharm
@file: example.py
@time: 2023/2/22 11:04 上午
"""

import numpy as np
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter(comment='tensorboard_test')

for x in range(50):
    writer.add_scalar('y=2x', x * 2, x)
    writer.add_scalar('y=pow(2, x)', 2 ** x, x)

    writer.add_scalars('data/scalar_group', {"xsinx": x * np.sin(x),
                                             "xcosx": x * np.cos(x),
                                             "arctanx": np.arctan(x)}, x)
writer.close()
