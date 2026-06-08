# ComfyUI Ideogram4 直接 JSON 修改版

这是一个用于 Ideogram 4 结构化 caption JSON 的 ComfyUI 节点，支持直接导入 JSON、可视化编辑 bbox，并输出可直接连接使用的 JSON 提示词。

本项目基于 [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes) 中的 Ideogram 4 prompt builder 修改而来，保留原 GPLv3 许可证。插件名、节点 id、显示名、Python 模块名和前端扩展名都与 KJNodes 不同，可以和 KJNodes 同时安装，避免云平台上覆盖原插件。

## 修改目的

原 KJNodes 节点把 `import_json` 更像是前端编辑器的导入辅助：连接后第一次运行会先把 JSON 推到前端，后端输出可能仍然是旧状态或空状态。

本修改版改变了这个流程：

- 如果编辑器为空，且 `import_json` 是有效的 Ideogram caption JSON，同一次运行会直接输出该 JSON。
- 导入的 JSON 会同步加载到可视化编辑器，方便检查和调整框。
- 手动移动、缩放、添加或删除框后，编辑器状态优先，输出 JSON 会反映修改后的 bbox。
- `import_json` 与缓存 JSON 会按解析后的对象比较，不再因为空格、换行或压缩格式不同而误判为新输入。

## 节点

显示名：

```text
Ideogram 4 直接 JSON 构建器（修改版）
```

节点 id：

```text
Ideogram4DirectJSONBuilderModified
```

分类：

```text
Ideogram4/修改版
```

## 输出

- `提示词`：Ideogram 4 结构化 caption JSON。
- `预览`：带区域框和编号的可视化预览。
- `BBOX`：供 BoundingBox 消费节点使用的像素级 bbox。
- `宽度`：最终画布宽度。
- `高度`：最终画布高度。

## 基本用法

1. 将生成好的 Ideogram 4 caption JSON 连接或粘贴到 `import_json`。
2. 运行一次。节点会立即输出 JSON，并在编辑器中显示区域框。
3. 在编辑器里移动、缩放、添加或删除区域。
4. 再运行一次。输出 JSON 会使用编辑后的 bbox 坐标。

## 许可证与署名

这是 ComfyUI-KJNodes Ideogram 4 prompt builder 的 GPLv3 修改衍生版本。

原项目：

```text
https://github.com/kijai/ComfyUI-KJNodes
```

许可证：

```text
GNU General Public License v3.0
```

详见 [LICENSE](LICENSE)。
