# 导入所需的库
from PIL import Image
import numpy as np
from skimage import io, color

# 读取图片并转换成灰度图片
img = io.imread ('in_img/kb.jpg')
# 去掉alpha通道，只保留前三个通道
img = img [:,:,:3]
gray = color.rgb2gray (img)

# 定义区域的大小，比如10*10
block_size = 10

# 获取图片的宽度和高度
width, height = gray.shape
print (width, height)

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
            if avg >= min_k and avg <= max_k:
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

# 创建一个空的列表，用来存储图片的路径或者链接
dice_images = []

# 添加图片的路径或者链接，按照点数的顺序排列
dice_images.append ('source_shaizi/shaizi/0.jpg')
dice_images.append ('source_shaizi/shaizi/1.jpg')
dice_images.append ('source_shaizi/shaizi/2.jpg')
dice_images.append ('source_shaizi/shaizi/3.jpg')
dice_images.append ('source_shaizi/shaizi/4.jpg')
dice_images.append ('source_shaizi/shaizi/5.jpg')
dice_images.append ('source_shaizi/shaizi/6.jpg')
shaizixiangsu=10  #10X10的骰子图片
# 创建一个新的画布，大小为图片的宽度乘以矩阵的行数，高度为图片的高度乘以矩阵的列数
canvas = Image.new ('RGB', (shaizixiangsu * len (graded_matrix [0]), shaizixiangsu * len (graded_matrix)))
print (len (graded_matrix [0]),len (graded_matrix), len (graded_matrix [0])*len (graded_matrix))
# 用双重循环遍历矩阵的每个元素
for i in range (len (graded_matrix)):
    for j in range (len (graded_matrix [0])):
        # 获取当前元素的值，也就是灰度值对应的等级
        value = graded_matrix [i][j]
        # 获取当前等级对应的图片的路径或者链接
        image_path = dice_images [value]
        # 打开图片
        image = Image.open (image_path)
        # 计算图片的粘贴位置，也就是左上角的坐标
        x = j * shaizixiangsu
        y = i * shaizixiangsu
        # 将图片粘贴到画布上
        canvas.paste (image, (x, y))

# 显示画布
canvas.show ()
# 保存画布
canvas.save('out_img/kb.png')
