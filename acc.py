# 导入我们所需的库 as：即给库取别名，方便书写
import matplotlib.pyplot as plt
import numpy as np
import h5py

# 定义数据

with h5py.File(r'tree_test_pred.hdf5') as f:
    print(f.keys())
    accp = []
    xp = []
    lth = len(f['isforks'])
    print(lth)
    for p in range(lth):
        xp.append(p)
        plabels = f['isforks'][p]
        pres = f['pred_isfork'][p]
        ap = 0
        for a in range(len(pres)):
            if plabels[a] == pres[a]:
                ap += 1
        acc = ap/len(pres)
        accp.append(acc)
    print(accp)
    print(xp)
    # accp.sort()
    # x1 = 0
    # x2 = 0
    # x3 = 0
    # x4 = 0
    # x5 = 0
    # print(accp[0], accp[-1])
    # for ac in accp:
    #     if ac <= 0.75:
    #         x1 += 1
    #     elif ac <= 0.80:
    #         x2 += 1
    #     elif ac <= 0.85:
    #         x3 += 1
    #     elif ac <= 0.90:
    #         x4 += 1
    #     else:
    #         x5 += 1
    # print(x1,x2,x3,x4,x5)
    # plt.figure(figsize=(600, 400), dpi=100)
    # # plt.plot(xp[:250], y, c='blue',label='accuracy')
    # plt.scatter(xp, accp, c='blue',label='accuracy')
    # y_ticks = range(1)
    # plt.grid(True, linestyle='--', alpha=0.5)
    # plt.xlabel("echo", fontdict={'size': 20})
    # plt.ylabel("accuracy", fontdict={'size': 20})
 #    xvla = []
 #    yvla = []
 #
 #    for i in range(10):
 #        xvla.append(i)
 #        accs = 0
 #        for j in range(400):
 #            if plabels[400*i+j] == pres[400*i+j]:
 #                accs += 1
 #        yvla.append(accs/400)
 #
 #    print(len(xvla),len(yvla))
 #
 #    # 绘图
 #    # 1.确定画布
 #    plt.figure(figsize=(8, 4))
 #
 #    colors = ['red', 'green']  # 建立颜色列表
 #    labels = ['reality', 'predition']  # 建立标签类别列表
 #
 #    # 2.绘图
 # # shape[] 类别的种类数量(2)
 #    plt.plot(xvla,  # 横坐标
 #                    yvla,  # 纵坐标
 #                    c='blue',  # 颜色
 #                    label='acc')  # 标签

    # 3.展示图形
    # plt.legend()  # 显示图例
    # # plt.savefig('acc_scatter.jpg')
    # plt.show()  # 显示图片




