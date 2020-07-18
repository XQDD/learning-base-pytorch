import numpy as np
import time
import matplotlib.pyplot as plt


def main():
    # 普通数组
    list1 = [1, 2, 3, 4, 5]
    print(list1)
    # nd-array(N-dimensional Array)
    nd1 = np.array(list1)
    print(nd1)
    print(type(nd1))
    list2 = [[1, 2, 3], [4, 5, 6]]
    print(list2)
    nd2 = np.array(list2)
    print(nd2)

    # 随机
    nd3 = np.random.random([3, 3])
    print(nd3)
    print("nd3的形状为", nd3.shape)

    # 保持数据一致性，可以用随机种子
    np.random.seed(123)
    nd4 = np.random.randn(2, 3)
    # 打乱前
    print(nd4)
    # 打乱后
    np.random.shuffle(nd4)
    print(nd4)
    # 对角矩阵
    print(np.diag([2, 4, 5, 6, 5, 2]))
    # 持久化
    np.savetxt("a.txt", nd4)
    nd5 = np.loadtxt("a.txt")
    print(nd5)
    # 范围
    print(np.arange(1, 10, 0.5))
    print(np.linspace(1, 10, 3))
    print(np.logspace(0, 1))

    # 访问元素
    np.random.seed(2019)
    nd11 = np.random.random([10])
    print("nd11:", nd11)
    print(nd11[3])
    print(nd11[3:6])
    print(nd11[1:6:2])
    print("倒序取数，间隔为2")
    print(nd11[::-2])
    nd12 = np.arange(25).reshape([5, 5])
    print(nd12)
    # 行列同时限制
    print(nd12[1:3, 1:3])
    # 筛选
    print(nd12[(nd12 > 3) & (nd12 < 10)])
    # 访问行
    print(nd12[[1, 2]])
    # 访问列
    print(nd12[:, 1:3])
    # 第3行到倒数第2行，然后按列取完后再数2取，取完为止
    print(nd12[2::2, ::2])

    # 函数随机采样
    np.random.seed(int(time.time()))
    a = np.arange(1, 25)
    # 放回式
    print(np.random.choice(a, (3, 4)))
    # 不放回，replace：偿还，归还
    print(np.random.choice(a, (3, 4), replace=False))
    # 自定义概率
    print(np.random.choice(a, (3, 4), p=a / np.sum(a)))

    # 对应元素相乘
    print(2 * np.multiply([1, 3], [3, 4]))


if __name__ == '__main__':
    main()
