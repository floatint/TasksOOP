# -*- coding: utf-8 -*-

# logic module

import segment


def get_union(segments):
    if len(segments) < 2:
        raise Exception("Segment list too small.")
    segments.sort()
    cnt = len(segments) - 1
    cur = 0
    unions = []
    while cnt > 0:
        union = segments[cur] - segments[cur + 1]
        if union is None:
            cur += 1
            cnt -= 1
            continue
        else:
            unions.append(union)
            cur += 1
            cnt -= 1
    return unions
