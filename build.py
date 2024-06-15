from math import e
import shutil
import os

from pathlib import Path
import shutil
import subprocess
import sys

def copy_folder_recursively(src, dst):
    src_path = Path(src)
    dst_path = Path(dst)
    
    # 检查目标文件夹是否存在，如果不存在则创建
    if not dst_path.exists():
        dst_path.mkdir(parents=True)
        
    # 递归复制文件夹
    shutil.copytree(src_path, dst_path, dirs_exist_ok=True)



if __name__ == "__main__":
    
    VERSION = "1.0.2"
    source_folder = '.meta'
    destination_folder = './dist/MainWindowImpl/.meta'
    
    # 清除上一次pyinstaller编译过程中的文件
    try:
        shutil.rmtree(Path("dist"))
        shutil.rmtree(Path("build"))
        os.remove("MainWindowImpl.spec")
    except:
        pass
    
    # pyinstaller
    cmd = r"pyinstaller MainWindowImpl.py -y --icon=.meta/icon.ico"
    subprocess.run(cmd, shell=True, stdout=sys.stdout, stderr=sys.stderr)
    

    # 复制.meta文件到dist/MainWindowImpl
    copy_folder_recursively(source_folder, destination_folder)
    
    
    # 创建.data文件dist/MainWindowImpl
    data_folder = Path("./dist/MainWindowImpl/.data")
    if not data_folder.exists():
        data_folder.mkdir(parents=True)
        
    # 创建setup.exe目录, 如.releases/1.0.2
    release_folder = Path(f".releases/{VERSION}")
    if release_folder.exists():
        shutil.rmtree(release_folder)
    release_folder.mkdir(parents=True)
    
    
    cmd = f"ISCC install.iss /DMyAppVersion={VERSION}"
    subprocess.run(cmd, shell=True, stdout=sys.stdout, stderr=sys.stderr)