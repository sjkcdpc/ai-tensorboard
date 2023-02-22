# 概述
Tensorboard是google为了配合tensorflow而发布的简单易用的可视化框架

https://pytorch.org/tutorials/recipes/recipes/tensorboard_with_pytorch.html?highlight=tensorboard

# 部署
```shell script
# pip install requirements/requirements.txt
# python example/example.py
# python example/example2.py

# tensorboard --logdir runs
TensorFlow installation not found - running with reduced feature set.

NOTE: Using experimental fast data loading logic. To disable, pass
    "--load_fast=false" and report issues on GitHub. More details:
    https://github.com/tensorflow/tensorboard/issues/4784

Serving TensorBoard on localhost; to expose to the network, use a proxy or pass --bind_all
TensorBoard 2.12.0 at http://localhost:6006/ (Press CTRL+C to quit)


# 共享训练数据
# tensorboard dev upload --logdir runs \
--name "我的实验数据" \
--description "共享训练数据"

# 查看网址
https://tensorboard.dev/

# 终端查看共享数据
# tensorboard dev list
TensorFlow installation not found - running with reduced feature set.
https://tensorboard.dev/experiment/doLJGrLbQdaeW26WFa75eA/
        Name                 我的实验数据
        Description          共享训练数据
        Id                   doLJGrLbQdaeW26WFa75eA
        Created              2023-02-22 11:44:40 (54 seconds ago)
        Updated              2023-02-22 11:44:47 (47 seconds ago)
        Runs                 6
        Tags                 5
        Scalars              6250
        Tensor bytes         0
        Binary object bytes  2434
Total: 1 experiment(s)

```

