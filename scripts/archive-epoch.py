#!/usr/bin/env python3
"""
纪元归档脚本
将当前src/目录完整复制到指定epoch目录下
用法: python scripts/archive-epoch.py epochA
"""

import shutil
import sys
import os
from pathlib import Path

def archive_epoch(epoch_name: str) -> None:
    """归档当前src到指定epoch目录"""
    project_root = Path(__file__).parent.parent
    src_dir = project_root / "src"
    target_dir = project_root / epoch_name / "src"
    
    if not src_dir.exists():
        print(f"错误: {src_dir} 不存在")
        sys.exit(1)
    
    if target_dir.exists():
        print(f"警告: {target_dir} 已存在，将覆盖")
        shutil.rmtree(target_dir)
    
    # 创建目标目录
    target_dir.parent.mkdir(exist_ok=True)
    
    # 复制整个src目录
    shutil.copytree(src_dir, target_dir)
    print(f"已归档: {src_dir} -> {target_dir}")
    
    # 验证归档
    if target_dir.exists():
        file_count = len(list(target_dir.rglob("*")))
        print(f"归档完成，共 {file_count} 个文件")
    else:
        print("归档失败")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python scripts/archive-epoch.py <epoch_name>")
        sys.exit(1)
    
    epoch = sys.argv[1]
    if not epoch.startswith("epoch"):
        print("错误: epoch名称必须以'epoch'开头，如epochA")
        sys.exit(1)
    
    archive_epoch(epoch)
