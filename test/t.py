import random
import matplotlib.pyplot as plt

# 定义硬币正反面状态
HEADS = 0
TAILS = 1

# 模拟抛硬币的过程并统计正反面出现的次数和频率
num_flips = int(input("请输入抛硬币的次数: "))
results = []
head_freqs = []
for i in range(num_flips):
    # 生成随机数模拟硬币正反面的结果
    result = random.randint(0, 1)
    results.append(result)

    # 计算正反面出现的频率
    heads = results.count(HEADS)
    head_freq = heads / (i+1)
    head_freqs.append(head_freq)

# 绘制统计图
plt.plot(range(1, num_flips+1), head_freqs)
plt.xlabel('抛硬币的次数')
plt.ylabel('正面出现的频率')
plt.title('硬币正面出现频率随抛硬币次数变化图')
plt.show()
