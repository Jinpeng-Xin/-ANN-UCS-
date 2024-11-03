# 基于ANN的冻土UCS预测模型——基于python的函数模型

 本项目为论文《基于机器学习的冻土无侧限抗压强度预测模型》模型应用部分，本项目提供了两种模型应用方式：
 - 基于python语言的函数模型，可通过`import`方式进行调用，供熟练使用python语言的人群使用与讨论。
 - 基于python实现的图形用户界面（GUI），可直接通过运行代码弹出，使用便捷，预测结果可供相关从业者进行参考，具体使用方式见**链接**。



##  一、模块概述 
`frozen_soil_ucs`模块是一个用于加载基于人工神经网络（ANN）的冻土无侧限抗压强度（UCS）预测的 Python 模块。它主要功能是从指定的文件路径加载预训练的 ANN 模型，使得在其他 Python 代码中可以方便地获取和使用该模型。 
##  二、函数说明 
### `ann_ucs`函数 
- **功能**：
加载名为`冻土ucs.h5`的人工神经网络模型文件。此函数使用`keras.models.load_model`来加载模型，该模型应该是之前训练并保存为 HDF5 格式（`.h5`）的模型。 
- **参数**： 
此函数无输入参数。 
- **返回值**： 
返回加载后的模型对象。 
## 三、使用方法 
1. **导入模块** 
在需要使用模型的 Python 代码中，使用`import ann_model_loader`语句导入`ann_model_loader`模块。 
2. **调用函数** 
通过以下方式调用`ann_ucs`函数并获取模型对象：
```
 import frozen_soil_ucs
 model = frozen_soil_ucs.ann_ucs()
```
之后，可以使用`model`对象进行相应的操作，例如利用模型进行冻土UCS预测:
```
#导入数据
import pandas as pd
import numpy as np
data=r".\frozen_soil_ucs_01.xlsx"
df=pd.read_excel(data2)
X = df[['温度', '质量含水量', '干密度', '应变速率', '类别']]

#导入模型
import frozen_soil_ucs
model = frozen_soil_ucs.ann_ucs()

#冻土UCS预测
fs_ucs_pred=model.predict(X)
print(fs_ucs_pred)
```
在向模型输入数据时，**数据顺序应严格按照`['温度（绝对值）', '质量含水量', '干密度', '应变速率', '类别']`列表顺序进行排列**，确保模型能够正确处理输入数据并进行准确的预测。
## 四、注意事项 
 1. **模型文件路径** 
确保`冻土ucs.h5`模型文件在运行环境中的路径是正确的。如果模型文件不在当前工作目录下，可能需要修改加载模型的代码来指定正确的文件路径。 
 2. **依赖项** 
此模块依赖于`keras`库来加载模型。确保`keras`库已经正确安装在运行环境中，并且版本兼容所加载的模型。如果模型是使用特定版本的`keras`训练的，建议在相同版本的`keras`环境中进行加载。
