from pathlib import Path
from random import sample

# begin voor nu ff met de effecten map
# TODO later zelf kiezen welke map, en welke submappen je wel wilt


def load_plugin_folder(base_path) -> dict[Path, list[Path]]:
    """
    Keyword arguments:
    argument -- description
    Return:  type --> vst dict. Both `type` and `vst` are Paths pointing to either the
                      parent folder representing the type of plugin, and a list of paths
                      that represent the VSTs in the folder of that type.
    """

    types = list(base_path.glob("*"))
    # vsts = list(base_path.glob("**/*.fst"))

    type_vst_dict = {}
    for type in types:
        vsts = list(type.glob("**/*.fst"))
        type_vst_dict[type] = vsts

        # subdirs = [x for x in type.iterdir() if x.is_dir()]
        # for subdir in subdirs:
        #     vsts += list(subdir.glob("*.fst"))

    return type_vst_dict


def select_random_vst(type_vst_dict: dict[Path, list[Path]], vst_type: Path):
    vsts = type_vst_dict[vst_type]
    return sample(vsts, 1)[0]


if __name__ == "__main__":
    base_path = Path(
        r"C:\Users\Jokme\Documents\Image-Line\FL Studio\Presets\Plugin database\Effects\3. Type"
    )
    type_vst_dict = load_plugin_folder(base_path)
    vst_type_selected = sample(list(type_vst_dict.keys()), 1)[0]
    print(vst_type_selected.name)

    selected_vst = select_random_vst(vst_type_selected)
    print(selected_vst.name)
