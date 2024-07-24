import shutil
import os

from pathlib import Path
import shutil
import subprocess
import sys
from VERSION import VERSION


def copy_folder_recursively(src, dst):
    src_path = Path(src)
    dst_path = Path(dst)

    # 检查目标文件夹是否存在，如果不存在则创建
    if not dst_path.exists():
        dst_path.mkdir(parents=True)

    # 递归复制文件夹
    shutil.copytree(src_path, dst_path, dirs_exist_ok=True)


if __name__ == "__main__":

    # 清除上一次pyinstaller编译过程中的文件
    try:
        shutil.rmtree(Path("dist"))
        shutil.rmtree(Path("build"))
        os.remove("main.spec")
    except:
        pass

    # pyinstaller
    cmd = r"pyinstaller main.py -y -w --icon=.meta/icon.ico -n ETDR-grading-app"
    subprocess.run(cmd, shell=True, stdout=sys.stdout, stderr=sys.stderr)

    # 复制.meta, .standards文件夹到dist/main
    copy_folder_recursively(".meta", "./dist/ETDR-grading-app/.meta")
    copy_folder_recursively(".standards", "./dist/ETDR-grading-app/.standards")

    # 创建setup.exe目录, 如.releases/1.0.0
    release_folder = Path(f".releases/{VERSION}")
    if release_folder.exists():
        shutil.rmtree(release_folder)
    release_folder.mkdir(parents=True)

    cmd = f"ISCC install.iss /DMyAppVersion={VERSION}"
    subprocess.run(cmd, shell=True, stdout=sys.stdout, stderr=sys.stderr)
