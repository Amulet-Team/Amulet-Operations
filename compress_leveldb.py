from __future__ import annotations
from amulet.api.selection import SelectionGroup
from amulet.api.data_types import Dimension
from amulet.api.level import BaseLevel
from amulet.level.formats.leveldb_world import LevelDBFormat


def compress_leveldb(
    world: BaseLevel,
    dimension: Dimension,
    selection: SelectionGroup,
    _
):
    wrapper = world.level_wrapper
    if isinstance(wrapper, LevelDBFormat):
        wrapper.level_db.compact()


export = {
    "name": "Compress LevelDB",  # the name of the plugin
    "operation": compress_leveldb  # the actual function to call when running the plugin
}
