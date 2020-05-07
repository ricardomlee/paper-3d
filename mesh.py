# off模型批量转换成obj文件
# 安装open3d 0.9.0

import open3d as o3d
import os

def off2obj(offile):
    portion = os.path.splitext(offile)  # 分离文件名和后缀
    mof=o3d.io.read_triangle_mesh(offile)  # Open3D读取off到mesh
    objfile=portion[0] + '.obj'  # 要保存的文件名 Todo: 自定义保存目录
    o3d.io.write_triangle_mesh(objfile,mof)  # mesh保存为obj文件

def test(path):
    files = os.listdir(path)  # 获取当前目录的所有文件及文件夹
    for file in files:
        try:
            file_path = os.path.join(path, file)  # 获取绝对路径
            if os.path.isdir(file_path):  # 判断是否是文件夹
                test(file_path)  # 如果是文件夹，就递归调用自己
            else:
                print(file_path)
                extension_name = os.path.splitext(file_path)  # 将文件的绝对路径中的后缀名分离出来
                if extension_name[1] == '.off':
                    off2obj(file_path)
        except:
            continue


test(r'F:\ModelNetS')
