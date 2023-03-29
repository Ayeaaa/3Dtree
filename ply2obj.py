import open3d as o3d
import h5py


# 定义新写入的obj文件(有顶点）
def makeObjFile(xyzs, fileName):
    with open(fileName, 'w') as f:
        for i in range(len(xyzs)):
            x, y, z = xyzs[i]
            f.write('v {} {} {} \n'.format(x, y, z))


# 定义新写入的ply文件(无顶点）
def makePlyFile(xyzs, fileName):
    with open(fileName, 'w') as f:
        for i in range(len(xyzs)):
            x, y, z = xyzs[i]
            f.write('{} {} {} \n'.format(x, y, z))


# 加载h5py文件提取点云坐标
with h5py.File(r'foliage_seg.hdf5') as f:
    print(f.keys())
    # print(f['samples'][0])
    points = f['points'][1]
    data = []
    # for i in points:
    #     for t in i:
    #         data.append(t)
    print(len(data), len(points))
    makePlyFile(points, 'treepoint.ply')
    # makeObjFile(data, 'treepoint.obj')


# 生成mesh
pcd = o3d.io.read_point_cloud(r"treepoint.ply", format="xyz")
# o3d.io.write_point_cloud(r"tree_point_origin.pcd", pcd)
# pcd2 = o3d.io.read_point_cloud("tree_point_origin.pcd")
# # # o3d.visualization.draw_geometries([pcd2])
# mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(pcd2, 0.03)
# mesh.compute_vertex_normals()
# o3d.visualization.draw_geometries([mesh], mesh_show_back_face=True)
# # 降采样
# downpcd = pcd2.voxel_down_sample(voxel_size=0.1)
# trimesh = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(pcd2, 255)
# 可视化
o3d.visualization.draw_geometries([pcd])
# o3d.visualization.draw_geometries([trimesh])
# # 写入mesh文件
# o3d.io.write_triangle_mesh(r"tree_mesh_origin.obj", mesh)


# # print(downpcd)
#
# trimesh = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(downpcd, 13)
# # print(trimesh)
# # o3d.visualization.draw_geometries([downpcd])
#
# trimesh.compute_vertex_normals()
# o3d.visualization.draw_geometries([trimesh], mesh_show_back_face=True)
# o3d.io.write_triangle_mesh(r"E:/testpro/jiojio/canding725/LXY_L_footxyzmesh.obj", trimesh)
# print("ok")
