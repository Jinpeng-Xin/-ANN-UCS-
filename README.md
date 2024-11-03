
# 基于 ANN 的冻土无侧限抗压强度预测模型


## 项目简介

本项目是论文《基于机器学习的冻土无侧限抗压强度预测模型》的模型应用部分。项目提供了两种模型应用方式：基于 Python 语言的函数模型和基于 Python 实现的图形用户界面（GUI）。
#### 项目作者
[XIN Jin-peng<sup>1</sup>](https://github.com/Jinpeng-Xin)   
WANG Jia-ting<sup>1</sup>  
RENG Hong-xin<sup>1</sup>   
LIU Qin-long<sup>1</sup>  
[PANG Yuan-en<sup>2</sup>](https://github.com/Yuanen-Pang)  
LI Xu<sup>1</sup>,<sup>*</sup>    
1.Key Laboratory of Urban Underground Engineering of Ministry of Education, Beijing Jiaotong University, Beijing 100044, China;  
2.Department of Civil and Environmental Engineering, Hong Kong University of Science and Technology, Hong Kong 999077, China

## 一、概述

### 函数模型

[`frozen_soil_ucs-ann`](https://github.com/Jinpeng-Xin/-ANN-UCS-/tree/f63a4fac57b6aa47e4580be367bf3a04c0084db3/frozen%20soil%20ucs-ann) 模块用于加载并运行基于人工神经网络（ANN）的冻土无侧限抗压强度（UCS）预测模型。该模块可通过 `import` 方式在 Python 代码中使用，适合熟悉 Python 编程的用户。

### GUI 模型

[`frozen_soil_ucs-GUI`](https://github.com/Jinpeng-Xin/-ANN-UCS-/tree/f63a4fac57b6aa47e4580be367bf3a04c0084db3/frozen%20soil%20ucs-GUI)模型是一个基于人工神经网络（ANN）的冻土无侧限抗压强度（UCS）预测工具。它使用 Python 实现了图形用户界面（GUI），方便用户输入参数并快速获取预测结果，无需深入编程知识，适合相关从业者使用。

![screenshot](https://github.com/Jinpeng-Xin/-ANN-UCS-/blob/f63a4fac57b6aa47e4580be367bf3a04c0084db3/other1/GUI%E7%95%8C%E9%9D%A2%E8%A7%86%E9%A2%9120241131947132.gif)
## 二、运行环境

### 依赖库

- `numpy`：用于数值计算。
- `pandas`：用于数据处理和分析。
- `tensorflow` 或 `keras`：用于加载和运行预训练的 ANN 模型。
- `tkinter`：用于创建 GUI 界面。
- `PIL`（Python Imaging Library）：用于图像处理，特别是加载和处理水印图像。
- `ttk`：`tkinter` 的主题化部件，用于创建具有特定样式的输入框等。

请确保在运行项目之前已经安装了上述依赖库。

## 三、使用方法

### 函数模型使用方法

1. **导入模块**

   在需要使用模型的 Python 代码中，使用 `import frozen_soil_ucs` 语句导入 `frozen_soil_ucs` 模块。

2. **调用函数**

   通过以下方式调用 `ann_ucs` 函数并获取模型对象：

   ```python
   import frozen_soil_ucs
   model = frozen_soil_ucs.ann_ucs()
   ```

3. **数据准备与预测**

   ```python
   import pandas as pd
   import numpy as np

   # 加载数据
   data = r".\frozen_soil_ucs_01.xlsx"
   df = pd.read_excel(data)
   X = df[['温度', '质量含水量', '干密度', '应变速率', '类别']]

   # 导入模型
   model = frozen_soil_ucs.ann_ucs()

   # 冻土 UCS 预测
   fs_ucs_pred = model.predict(X)
   print(fs_ucs_pred)
   ```

   注意：数据顺序应严格按照 `['温度', '质量含水量', '干密度', '应变速率', '类别']` 列表顺序进行排列。

### GUI 模型使用方法

1. **启动程序**

   运行代码后，将弹出名为“基于 ANN 的冻土 UCS 预测模型”的窗口。

2. **输入参数**

   - **温度（tempture）**：在“温度 tempture (℃) :”标签后的输入框中输入温度值（单位：℃）。
   - **质量含水量（mass water content）**：在“质量含水量 mass water content (%) :”标签后的输入框中输入质量含水量值（单位：%）。
   - **干密度（dry density）**：在“干密度 dry density (g/cm³):”标签后的输入框中输入干密度值（单位：g/cm³）。
   - **应变速率（strain rate）**：在“应变速率 strain rate (s⁻¹) :”标签后的输入框中输入应变速率值（单位：s⁻¹）。
   - **类别（category）**：通过“类别:”标签下的单选按钮选择土壤类别，可选项为“黏土”（值为“0”）、“粉土”（默认值为“1”）、“砂土”（值为“2”）。

3. **预测操作**

   点击“Predict”按钮进行预测。如果输入的参数值不合法（非数值类型），将弹出错误提示框。预测成功后，预测结果将显示在“Predicted UCS: [预测值]”格式的标签中，预测值保留两位小数，颜色为绿色。

4. **从文件加载数据预测**

   点击“Load Data”按钮，选择 Excel 文件进行预测。若读取或预测过程中出现错误，将弹出相应的错误提示框。

5. **清除输入和结果**

   点击“Clear”按钮，清空所有输入框和预测结果显示。

## 四、模型相关

两种应用方式都使用预训练的 ANN 模型 `冻土ucs.h5` 进行预测。请确保该文件在程序运行时可被正确访问。在函数模型中通过 `tf.keras.models.load_model('冻土ucs.h5')` 加载，在 GUI 程序启动时也进行加载。

## 五、界面特点（仅 GUI 相关）

### 界面布局

- 窗口顶部包含北京交通大学校徽水印。
- 窗口标题为“Prediction Model for Unconfined Compressive Strength of Frozen Soil Based on Machine Learning”及中文名称“基于机器学习的冻土 UCS 预测”。
- 输入参数部分包括标签、输入框和类别选择的单选按钮。
- 按钮包括“Predict”、“Load Data”和“Clear”。
- 预测结果显示标签。

### 界面样式

- 窗口背景颜色为 `#f0f0f0`。
- 输入框使用自定义的 `ttk` 样式，具有绿色边框效果。
- 按钮颜色区分功能：“Predict”按钮为绿色（`#4CAF50`）、“Load Data”按钮为蓝色（`#2196F3`）、“Clear”按钮为橙色（`#FF9800`）。
- 文本使用 Helvetica 字体，部分标签使用较大的字体以提高可读性。

## 六、注意事项

1. **模型文件路径**：确保 `冻土ucs.h5` 模型文件在运行环境中的路径是正确的。如果模型文件不在当前工作目录下，请修改加载模型的代码以指定正确的文件路径。
2. **依赖项**：此项目依赖于 `keras` 库来加载模型,请确保 `keras` 库已经正确安装。
