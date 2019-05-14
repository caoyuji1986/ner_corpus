# ner_corpus
## 中文ner标准数据集
# dat/msra
mara公开的ner数据集：样本分割比例5：5：90

    - dev.bio.txt 开发集
    - test.bio.txt 测试集
    - train.bio.txt 训练集
    - train.txt 原始数据
# dat/renmin_ribaothe_people_daily
人民日报的ner数据集：样本分割比例5：5：90

    - dev.bio.txt 开发集
    - test.bio.txt 测试集
    - train.bio.txt 训练集
    - train.txt 原始数据
    
# src
    - msra.py msra数据集样本分割脚本
    - renmin.py 人民日报数据集样本分割脚本
    - sigma_transformer.py BIO BMES 等标注方法转换脚本 