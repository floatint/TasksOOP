# -*- coding: utf-8 -*-

# logic module

import segment


def get_unions(segments):
    if len(segments) == 1:
        return segments[0]
    segments.sort(key=lambda s: (s.x1, s.x2), reverse=True)
    # сюда
    partial = []
    while len(segments) != 1:
        seg1 = segments.pop()
        seg2 = segments.pop()
        if seg1 in seg2:
            segments.append(seg2)
        else:
            if seg1.x2 - seg2.x1 > 0:
                segments.append(segment.Segment(seg1.x1, seg2.x2))
            else:
                segments.append(seg2)
                partial.append(seg1)
    return sorted(segments + partial, key=lambda s: (s.x1, s.x2))
