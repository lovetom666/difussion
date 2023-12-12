import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 以示例文件路径为例，你需要替换为实际的.npy文件路径
npz_file_path = './result/samples_100x512x512x3.npz'
# 加载 .npz 文件
data = np.load(npz_file_path)
keys = data.keys()
print(keys)
for key in keys:
    # value = data[key]
    print(f"Key: {key}")

# 获取图像数组
image_array = data['arr_0']

# 迭代每个图像
for i, image in enumerate(image_array):
    # 创建 PIL.Image 对象
    pil_image = Image.fromarray(image)

    # 保存图像到本地
    image_path = f'./result/512_512/output_{i}.png'
    pil_image.save(image_path)

    print(f"Image {i+1} saved to {image_path}")

# # 显示图像
# plt.imshow(image_array[3])
# plt.title('Image')
# plt.show()