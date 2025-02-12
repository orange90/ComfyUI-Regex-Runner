# ComfyUI-Regex-Runner

ComfyUI-Regex-Runner 是一个 ComfyUI 的自定义节点插件，它允许你在 ComfyUI 工作流中直接运行正则表达式操作。

## 功能特点

- 在 ComfyUI 中执行正则表达式匹配和替换
- 支持所有标准的 Python 正则表达式语法
- 可以轻松处理文本输入和输出
- 完全集成到 ComfyUI 工作流程中

## 安装方法

1. 进入你的 ComfyUI 自定义节点目录：

```bash
cd ComfyUI/custom_nodes/
```

2. 克隆此仓库：

```bash
git clone https://github.com/ltdrdata/ComfyUI-Regex-Runner
```

## 使用方法

### 基本节点介绍

插件提供以下节点：

- **Regex Match**: 执行正则表达式匹配操作
- **Regex Replace**: 执行正则表达式替换操作

### 节点参数说明

#### Regex Match 节点
- `text`: 输入要匹配的文本
- `pattern`: 正则表达式模式
- `flags`: 正则表达式标志（可选）
- 输出：匹配到的文本列表

#### Regex Replace 节点
- `text`: 输入要处理的文本
- `pattern`: 正则表达式模式
- `replacement`: 替换文本
- `flags`: 正则表达式标志（可选）
- 输出：替换后的文本

### 使用示例

1. **提取数字**
```python
输入文本: "图片尺寸为 512x512"
正则模式: "\d+"
输出: ["512", "512"]
```

2. **替换文本**
```python
输入文本: "prompt: a cat"
正则模式: "^prompt: "
替换文本: "negative prompt: "
输出: "negative prompt: a cat"
```

## 常见问题

1. **正则表达式不匹配？**
   - 检查正则表达式语法是否正确
   - 确认是否需要使用原始字符串（r"pattern"）
   - 验证特殊字符是否正确转义

2. **如何使用正则表达式标志？**
   - 支持标准 Python 正则表达式标志
   - 例如：`re.IGNORECASE`, `re.MULTILINE` 等

## 贡献指南

欢迎提交 Pull Requests 来改进这个项目。请确保：

1. 代码符合 Python 编码规范
2. 提供适当的测试用例
3. 更新相关文档

## 许可证

MIT License

## 问题反馈

如果你遇到任何问题或有改进建议，请：

1. 在 GitHub 上提交 Issue
2. 提供详细的问题描述和复现步骤
3. 附上相关的错误信息和日志 