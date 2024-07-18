
import open3d as o3d
import numpy as np

def generate_point_cloud():
    new_pcd = o3d.geometry.PointCloud()
    points = np.random.rand(100, 3)
    new_pcd.points = o3d.utility.Vector3dVector(points)
    return new_pcd

def update_point_cloud(window, widget, geom_pcd):
    index_to_replace = np.random.randint(0, 100)
    rand_pt = np.random.rand(1, 3)
    geom_pcd.points[index_to_replace] = rand_pt[0]
    #widget.scene.update_geometry(geom_pcd)
    print("update_point_cloud")
    #widget.scene.update_geometry(geom_pcd)
    #widget.scene.update_renderer()
    #widget.scene.update()
    #widget.force_redraw()
    #geom_pcd = o3d.cpu.pybind.t.geometry.PointCloud.create_from_point_cloud(geom_pcd)
    #widget.scene.scene.update_geometry("Geometry", geom_pcd, o3d.visualization.rendering.Scene.UPDATE_POINTS_FLAG)
    #widget.scene.scene.update_geometry(geom_pcd)
    return True

def main():
    app = o3d.visualization.gui.Application.instance
    app.initialize()
    app.run()

if __name__ == '__main__':
    print("Open3D version:", o3d.__version__)
    main()
