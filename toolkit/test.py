import csv
import sys
import os
sys.path.append("..")


predict_labels = {}   # 预加载实体到标注的映射字典
filePath = os.getcwd()
with open(filePath+'/predict_labels.txt','r',encoding="utf-8") as csvfile:
	reader = csv.reader(csvfile, delimiter=' ')
	for row in reader:
		predict_labels[str(row[0])] = int(row[1])
        print(int(row[1]))
print('predicted labels load over!')