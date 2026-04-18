from hit_object import HitObject


def instantiate_hitobject_from_str(hit_object_str: str) -> HitObject:
    lines = hit_object_str.split("\n")
    data = list(map(lambda s: s.strip().split(" ")[1], lines))
    data_to_int = list(map(int, data))
    return HitObject(*data_to_int)



def get_qua_data(filepath: str) -> tuple[str, list[HitObject]]:
    if filepath[-4:] != ".qua":
        raise ValueError("Provided file is not a .qua file.")
    
    with open(filepath, "r") as qua_file:
        file_string = qua_file.read()
    
    file_base, file_hitobjects_str = file_string.split("HitObjects:\n- ")
    file_base = file_base + "HitObjects:\n"

    file_hitobjects_str_list = file_hitobjects_str.strip().strip("KeySounds: []").strip().split("\n  KeySounds: []\n- ")
    file_hitobjects = list(map(instantiate_hitobject_from_str, file_hitobjects_str_list))

    return file_base, file_hitobjects