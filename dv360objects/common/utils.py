from __future__ import annotations


class Utils:
    def __init__(self):
        pass

    def deduplication_object_list(self, object_list, object_dedupe_key):
        seen_objects = set()
        deduped_list_of_objects = []
        for object in object_list:
            if object[object_dedupe_key] not in seen_objects:
                deduped_list_of_objects.append(object)
                seen_objects.add(object[object_dedupe_key])
        return deduped_list_of_objects
