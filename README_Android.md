
# 使用 Buildozer 将 Zuoyou Game 打包为 Android APK

本项目包含 `zuoyou_game.py`（游戏主代码）和 `buildozer.spec`（打包配置文件）。

## 触控控制说明
- 左半屏上半部：控制左挡板向上
- 左半屏下半部：控制左挡板向下
- 右半屏上半部：控制右挡板向上
- 右半屏下半部：控制右挡板向下

## 打包步骤（Linux 环境）
1. 安装依赖：
```bash
sudo apt install -y build-essential git zip unzip openjdk-17-jdk
pip install buildozer
```

2. 将本项目中的 buildozer.spec 放入项目目录

3. 编译 APK：
```bash
buildozer -v android debug
```

更多内容详见 README 原文。
