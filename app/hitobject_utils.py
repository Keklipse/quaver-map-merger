from hit_object import HitObject


def merge_files_hitobjects(files_hitobjects: list[list[HitObject]]) -> list[HitObject]:
    result = []
    for file in files_hitobjects:
        for hitobject in file:
            result.append(hitobject)
    return result



def prevent_overlaps(hitobjects: list[HitObject]) -> list[HitObject]:
    occupied_space = set()
    result = []
    for hitobject in hitobjects:
        if (hitobject.start_time, hitobject.lane) not in occupied_space:
            occupied_space.add((hitobject.start_time, hitobject.lane))
            result.append(hitobject)
    return result



def order_hitobjects(hitobjects: list[HitObject]) -> list[HitObject]:
    hitobjects.sort(key=lambda hitobject: (hitobject.start_time, hitobject.lane))
    return hitobjects