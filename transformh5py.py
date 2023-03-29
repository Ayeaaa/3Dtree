import h5py
import open3d as o3d
import numpy as np

def makePlyFile(xyzs, fileName='makeply.ply'):
    with open(fileName, 'w') as f:
        for i in range(len(xyzs)):
            x, y, z = xyzs[i]
            f.write('{} {} {} \n'.format(x, y, z))


def makeObjFile(xyzs, fileName='tree.obj'):
    with open(fileName, 'w') as f:
        for i in range(len(xyzs)):
            x, y, z = xyzs[i]
            f.write('{} {} {} \n'.format(x, y, z))


with h5py.File(r'E:\Ayeaaa\TreePartNet\data\Neural_Decomposition\tree_labeled_test.hdf5') as f:
# with h5py.File(r'tree_test_pred.hdf5') as f:
# with h5py.File(r'E:\Ayeaaa\TreePartNet\foliage_seg.hdf5') as f:
    # pcd = o3d.io.read_point_cloud(f['points'])
    # o3d.visualization.draw_geometries([f['points'][1]])
    print(f.keys())
    xyzs=f['points'][1]
    makePlyFile(xyzs)
    # makeObjFile(xyzs)



# pcd = o3d.io.read_point_cloud(r"makeply.ply")
# pcd = o3d.io.read_point_cloud(r"E:\Ayeaaa\TreePartNet\foliage_seg.hdf5")

pcd = o3d.io.read_point_cloud(r"makeply.ply", format="xyz")
# o3d.visualization.draw_geometries([pcd])
voxel_down_pcd = pcd.voxel_down_sample(voxel_size=0.08)

# print('input')
# N = 2000
#
# armadillo = o3d.data.ArmadilloMesh()
# mesh = o3d.io.read_triangle_mesh(armadillo.path)
# pcd = mesh.sample_points_poisson_disk(N)
# # fit to unit cube
# pcd.scale(1 / np.max(pcd.get_max_bound() - pcd.get_min_bound()),
#           center=pcd.get_center())
# pcd.colors = o3d.utility.Vector3dVector(np.random.uniform(0, 1, size=(N, 3)))
# o3d.visualization.draw_geometries([pcd])
#
# print('octree division')
# octree = o3d.geometry.Octree(max_depth=4)
# octree.convert_from_point_cloud(pcd, size_expand=0.01)
# o3d.visualization.draw_geometries([octree])

pcd.paint_uniform_color([0.5, 0.5, 0.5])
pcd_tree = o3d.geometry.KDTreeFlann(pcd)
pcd.colors[500] = [1, 0, 0]
[k, idx, _] = pcd_tree.search_knn_vector_3d(pcd.points[500], 200)
np.asarray(pcd.colors)[idx[1:], :] = [0, 0, 1]
# [k, idx, _] = pcd_tree.search_radius_vector_3d(pcd.points[1500], 0.2)
# np.asarray(pcd.colors)[idx[1:], :] = [0, 1, 0]
o3d.visualization.draw_geometries([pcd],
                                  zoom=0.5599,
                                  front=[-0.4958, 0.8229, 0.2773],
                                  lookat=[2.1126, 1.0163, -1.8543],
                                  up=[0.1007, -0.2626, 0.9596])

# 原点云的点array
# pcd_ori = np.array(pcd.points)
# print(pcd_ori.shape, len(pcd_ori))
#
# xarray = []
# for i in range(len(pcd_ori)):
#     xstr = []
#     for x in pcd_ori[i]:
#         xstr.append(x)
#     xstr.append(i)
#     xarray.append(xstr)
# print(len(xarray))
# 加入序列号的点云

# o3d.visualization.draw_geometries([voxel_down_pcd])
# downstream = np.asarray(voxel_down_pcd.points)
# 降采样
# print(downstream.shape)
# 降采样后的点云
# narray = []
# nstr = []
# ids = []
# # 查询现存点云index
# for d in range(len(downstream)):
#     # if downstream[d] in pcd.points:
#     if downstream[d] in pcd_ori:
#         ids.append(d)
# print(ids, len(ids))

# for y in range(len(downstream)):
#     yid = 0
    # for j in range(2):
        # if downstream[y][j] != xarray[y][j]:
        #     print(downstream[y][j], xarray[y][j])
        #     break
        # else:
        #     nstr.append(xarray[y][3])

# print(len(nstr))
# o3d.io.write_point_cloud("downstream.ply", voxel_down_pcd")
# with open('downstream.ply', 'w') as fi:
#     for ds in downstream:
#         fi.write(str(ds))
