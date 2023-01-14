from typing import List, Tuple, Dict, Optional, Any


def to_tree(data: List[Tuple[Optional[str], str]]) -> Dict[str, Any]:
    children: Dict[str, Any] = {o: {} for _, o in data}
    tree: Dict[str, Any] = {}
    for parent, offspring in data:
        if parent is None:
            tree[offspring] = children[offspring]
        else:
            children[parent][offspring] = children[offspring]
    return tree