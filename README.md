# 概述
Tensorboard是google为了配合tensorflow而发布的简单易用的可视化框架

https://pytorch.org/tutorials/recipes/recipes/tensorboard_with_pytorch.html?highlight=tensorboard

# 部署
```shell script
python example/example.py
python example/example2.py

pip install requirements/requirements.txt

# tensorboard --logdir runs
TensorFlow installation not found - running with reduced feature set.

NOTE: Using experimental fast data loading logic. To disable, pass
    "--load_fast=false" and report issues on GitHub. More details:
    https://github.com/tensorflow/tensorboard/issues/4784

Serving TensorBoard on localhost; to expose to the network, use a proxy or pass --bind_all
TensorBoard 2.12.0 at http://localhost:6006/ (Press CTRL+C to quit)


# 共享训练模型
# tensorboard dev upload --logdir runs \
--name "My latest experiment" \ # optional
--description "Simple comparison of several hyperparameters" # optional

查看网址
https://tensorboard.dev/

tensorboard dev list


```

