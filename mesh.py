import open3d as o3d
import os

def off2obj(offile):
    portion = os.path.splitext(offile)
    mof=o3d.io.read_triangle_mesh(offile)
    objfile=portion[0] + '.obj'
    o3d.io.write_triangle_mesh(objfile,mof)

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
            continue  # 可能会报错，所以用了try-except,如果要求比较严格，不需要报错，就删除异常处理，自己调试


test(r'F:\ModelNetS')
