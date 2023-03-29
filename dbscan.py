import matplotlib.pyplot as plt
import numpy as np
import h5py
import open3d as o3d


def makePlyFile(xyzs, fileName='centers.ply'):
    with open(fileName, 'w') as f:
        for i in range(len(xyzs)):
            x, y, z = xyzs[i]
            f.write('{} {} {} \n'.format(x, y, z))
#


# 读取点云
pcd = o3d.io.read_point_cloud(r"forks.ply", format="xyz")
# o3d.visualization.draw_geometries([pcd])

with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
    labels = np.array(pcd.cluster_dbscan(eps=0.02, min_points=5, print_progress=True))

max_label = labels.max()
print(f"point cloud has {max_label + 1} clusters")
colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))

colors[labels < 0] = 0
pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])
# o3d.visualization.draw_geometries([pcd], "o3d dbscanclusting origin", width=400, height=400)

print(labels, len(labels))
min = labels.min()
max = labels.max()
# print('min: ', min, " max: ", max)

# 打印聚类非0的点云下标，点云数
print(np.nonzero(labels), '  type: ', type(np.nonzero(labels)), ' size: ', len(np.array(np.nonzero(labels)[0])))

zero_index = np.where(labels == 0)  # 提取分类为0的聚类点云下标
zero_pcd = pcd.select_by_index(np.array(zero_index)[0])  # 根据下标提取点云点
print(zero_pcd)
print('zero_index: ', zero_index, " size: ", len(np.array(zero_index)[0]))
centers = []
for label in range(min, max+1):
    label_index = np.where(labels == label)  # 提取分类为label的聚类点云下标
    label_pcd = pcd.select_by_index(np.array(label_index)[0])  # 根据下标提取点云点
    # for p in label_pcd.points:
    #     centers.append(p)
    centers.append(label_pcd.get_center())
    # print('label: ', str(label), '点云数：', len(label_pcd.points), label_pcd.get_center())

    # 可视化
    # o3d.visualization.draw_geometries([label_pcd], "o3d dbscanclusting " + str(label) + " results", width=400,
    #                                   height=400)
    # 分别按分类写入文件
    # o3d.io.write_point_cloud("./" + str(label) + ".pcd", label_pcd)

makePlyFile(centers)

# 读取点云
pcd_center = o3d.io.read_point_cloud(r"centers.ply", format="xyz")
pcd_center.paint_uniform_color([1, 0, 0])
o3d.visualization.draw_geometries([pcd_center])
