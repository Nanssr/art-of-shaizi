# # 导入所需的库
# from PIL import Image
# import numpy as np
# from skimage import io, color

# # 读取图片并转换成灰度图片
# img = io.imread ('tx.jpg')
# gray = color.rgb2gray (img)

# # 定义区域的大小，比如10*10
# block_size = 100

# # 获取图片的宽度和高度
# width, height = gray.shape
# print (width, height)
# # 创建一个空的列表，用来存储每个区域的平均灰度值
# avg_values = []

# # 用双重循环遍历图片的每个区域
# for i in range (0, width, block_size):
#     for j in range (0, height, block_size):
#         # 获取当前区域的灰度值矩阵
#         block = gray [i:i+block_size, j:j+block_size]
#         # 计算当前区域的平均灰度值
#         avg = np.mean (block)
#         # 将平均灰度值添加到列表中
#         avg_values.append (avg)

# # 打印每个区域的平均灰度值
# print (avg_values)

# # 创建一个空的列表，用来存储分级后的灰度值
# graded_values = []

# # 遍历灰度值列表
# for value in avg_values:
#     # 判断灰度值属于哪个等级
#     for i in range (7):
#         # 计算当前等级的最小和最大灰度值
#         min_i = i / 7
#         max_i = (i + 1) / 7
#         # 如果灰度值在当前等级的范围内，就用当前等级的数字来替换
#         if value >= min_i and value <= max_i:
#             # 计算灰度值对应的等级
#             level = i
#             graded_values.append (level)
#             break

# # 打印分级后的灰度值
# print (graded_values)

# 导入所需的库
from PIL import Image
import numpy as np
from skimage import io, color

# 读取图片并转换成灰度图片
img = io.imread ('shu.jpg')
# 去掉alpha通道，只保留前三个通道
img = img [:,:,:3]
gray = color.rgb2gray (img)

# 定义区域的大小，比如10*10
block_size = 10

# 获取图片的宽度和高度
width, height = gray.shape
print (width, height)
# 计算图片的实际区域的数量
# actual_width = width - (width % block_size)
# actual_height = height - (height % block_size)
# print (actual_width, actual_height )
# 创建一个空的二维列表，用来存储分级后的灰度值矩阵
graded_matrix = []

# 用双重循环遍历图片的每个区域
for i in range (0, width, block_size):
    # 创建一个空的列表，用来存储当前行的灰度值
    row = []
    for j in range (0, height, block_size):
        # 获取当前区域的灰度值矩阵
        block = gray [i:i+block_size, j:j+block_size]
        # 计算当前区域的平均灰度值
        avg = np.mean (block)
        # 判断灰度值属于哪个等级
        for k in range (7):
            # 计算当前等级的最小和最大灰度值
            min_k = k / 7
            max_k = (k + 1) / 7
            # 如果灰度值在当前等级的范围内，就用当前等级的数字来替换
            if avg >= min_k and avg <=max_k:
                # 计算灰度值对应的等级
                level = k
                # 将灰度值添加到当前行的列表中
                row.append (level)
                break
    # 将当前行的列表添加到二维列表中
    graded_matrix.append (row)

# 打印分级后的灰度值矩阵
for row in graded_matrix:
    print (row)
