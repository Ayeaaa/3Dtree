import h5py
import open3d as o3d


def makePlyFile(xyzs, fileName='makeply300.ply'):
    with open(fileName, 'w') as f:
        for i in range(len(xyzs)):
            x, y, z = xyzs[i]
            f.write('{} {} {} \n'.format(x, y, z))



# with h5py.File(r'E:\Ayeaaa\TreePartNet\data\Neural_Decomposition\tree_labeled_train.hdf5') as f:
#     print(f.keys(), len(f['primitive_id']), f['primitive_id'][1][:30])

with h5py.File(r'E:\Ayeaaa\TreePartNet\data\Foliage_Segmentation\tree_labeled_train.hdf5') as f1:
    print(f1.keys(), len(f1['points']))

# with h5py.File(r'E:\Ayeaaa\TreePartNet\data\Neural_Decomposition\tree_labeled_test.hdf5') as f2:
    # print(f2.keys(), len(f2['points']))

# with h5py.File(r'E:\Ayeaaa\TreePartNet\data\Neural_Decomposition\tree_labeled_val.hdf5') as f3:
#     print(f3.keys(), len(f3['points']))
#     print(f3['lc'][1][:20])
# 引入pcd
# pcd = o3d.io.read_point_cloud(r"makeply300.ply", format="xyz")

# o3d.visualization.draw_geometries([pcd])
# print(pcd)
# pcd = o3d.io.read_point_cloud(r"makeply.ply", format="xyz")
# aabb = pcd.get_axis_aligned_bounding_box() #轴对其包围盒
# aabb.color = (1, 0, 0) #红色
# obb = pcd.get_oriented_bounding_box()
# obb.color = (0, 1, 0) # 绿色
# o3d.visualization.draw_geometries([pcd, aabb, obb])
# hull, _ = pcd.compute_convex_hull()
pcd = o3d.io.read_point_cloud((r'treemesh.obj'))
# hull_ls = o3d.geometry.LineSet.create_from_triangle_mesh(hull)
# hull_ls.paint_uniform_color((1, 0, 0)) #凸包的颜色
# o3d.visualization.draw_geometries([pcd, hull_ls])
o3d.visualization.draw_geometries([pcd])
