"""Standalone modified Ideogram 4 direct JSON builder for ComfyUI.

Modified from ComfyUI-KJNodes' Ideogram 4 prompt builder.
Original project: https://github.com/kijai/ComfyUI-KJNodes
License: GNU GPL v3, see LICENSE.
"""

from .nodes.direct_json_nodes import Ideogram4DirectJSONBuilderModified


NODE_CLASS_MAPPINGS = {
    "Ideogram4DirectJSONBuilderModified": Ideogram4DirectJSONBuilderModified,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Ideogram4DirectJSONBuilderModified": "Ideogram 4 Direct JSON Builder Modified",
}

WEB_DIRECTORY = "./web"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
