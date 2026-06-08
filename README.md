# ComfyUI Ideogram4 DirectJSON Modified

Standalone modified ComfyUI node for Ideogram 4 structured caption JSON with visual bbox editing.

This project is a modified derivative of the Ideogram 4 prompt builder in [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes). It keeps the original GPLv3 license and is intentionally packaged with a different plugin name, node id, display name, Python module, and frontend extension name so it can coexist with KJNodes on cloud platforms.

## Why This Modified Version Exists

The original KJNodes node treats `import_json` as an editor import helper: when connected, the JSON is pushed to the frontend after execution, so the first run can output the previous or empty editor state.

This modified node changes that workflow:

- If the visual editor is empty and `import_json` contains a valid Ideogram caption JSON, the same execution outputs that JSON immediately.
- The imported JSON is also loaded into the visual editor, so the boxes are visible for inspection and manual editing.
- After boxes are manually moved, resized, added, or removed, the hidden editor state takes priority and the output JSON reflects the edited bbox positions.

## Node

Display name:

```text
Ideogram 4 Direct JSON Builder Modified
```

Node id:

```text
Ideogram4DirectJSONBuilderModified
```

Category:

```text
Ideogram4/modified
```

## Outputs

- `prompt`: Ideogram 4 structured caption JSON.
- `preview`: visual preview with boxes and labels.
- `bboxes`: pixel-space bbox output for BoundingBox consumers.
- `width`: resolved canvas width.
- `height`: resolved canvas height.

## Basic Workflow

1. Connect or paste a generated Ideogram 4 caption JSON into `import_json`.
2. Run once. The node outputs the JSON immediately and loads the visual boxes.
3. Move or resize boxes in the editor.
4. Run again. The output JSON reflects the edited box positions.

## License And Attribution

This is a GPLv3 modified derivative of ComfyUI-KJNodes' Ideogram 4 prompt builder.

Original project:

```text
https://github.com/kijai/ComfyUI-KJNodes
```

License:

```text
GNU General Public License v3.0
```

See [LICENSE](LICENSE).
