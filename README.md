# micro-life-sim

一个专注于构建具有完整生命周期的单个自主 AI 智能体的模拟项目，该智能体在微观虚拟环境中运行。这个小型人工生命拥有内在需求、动态状态变化和独立决策能力，能够模拟自然生命活动 —— 从成长、行为模式、环境交互到衰老直至终结。项目在精简场景中探索人工生命的核心机制，重点在于无人类交互情况下的自主行为涌现。

## 项目结构

<!-- 注释：基于目录快照，模块化列出关键部分，便于导航 -->

- **docs/**: 项目文档，包括宏观路线图、产品需求等。
- **epoch0/**: 第零纪实现（点逝），包含 dot.py 和 dot.json。
- **epochA/**: 第 A 纪实现（节律），当前为空（待开发）。
- **scripts/**: 辅助脚本，如 archive-epoch.py。
- **src/**: 源代码，如 rhythm.py。
- **LICENSE**: 项目许可。
- **README.md**: 本文档。

## 安装

<!-- 注释：最小步骤，确保可测试；假设Python环境，如果需要requirements.txt，请手动创建 -->

1. 克隆仓库：`git clone https://github.com/yourusername/micro-life-sim.git`（替换为实际 URL）。
2. 进入目录：`cd micro-life-sim`。
3. 安装依赖：项目使用 Python 标准库，无外部依赖。如果未来添加，请运行`pip install -r requirements.txt`（当前无此文件）。

## 快速开始

<!-- 注释：基于dot.py示例，提供可复制命令，确保精确可测试 -->

运行第零纪模拟：

```
python epoch0/dot.py
```

- 这将模拟一个“dot”从 1.0 流逝到 0.0，间隔 1 秒，状态保存到 dot.json。
- 按 Ctrl+C 中断并保存进度。

## 路线图

<!-- 注释：提炼自宏观路线图.md，保持简洁，链接完整文档 -->

项目分阶段演化，从“点逝”到完整生命周期。关键阶段：

- **阶段 0 (点逝)**: 时间流逝机制。
- **阶段 A (节律)**: 生物钟和昼夜作息。
- **阶段 B-F**: 能量、脉动、记忆、环境、一生（详见[docs/宏观路线图.md](docs/宏观路线图.md)）。

哲学：内在驱动、生活节奏优先。

## 贡献

<!-- 注释：简单指南，参考记忆使用hyphens命名文件 -->

1. Fork 仓库。
2. 创建分支：`git checkout -b feature/new-feature`。
3. 提交变更：遵循 TDD，文件名用 hyphens（如 new-file.md）。
4. Push 并创建 Pull Request。

## 许可

<!-- 注释：链接现有LICENSE -->

详见[LICENSE](LICENSE)文件。
