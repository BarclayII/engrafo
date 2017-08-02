# -*- coding: utf-8 -*-
import json
import sys
from pandocfilters import walk
from .footnotes import inline_footnotes
from .images import replace_pdf_images, replace_tikz_images
from .labels import (process_display_math, insert_figure_labels,
                     insert_table_labels, insert_section_labels,
                     make_explicit_figure_captions, replace_references)


def main():
    doc = json.loads(sys.stdin.read())
    blocks = doc['blocks']
    meta = doc['meta']
    fmt = 'latex'

    altered = blocks

    for action in [
            process_display_math,
            replace_pdf_images,
            replace_tikz_images,
            insert_figure_labels,
            insert_table_labels,
            insert_section_labels,
            make_explicit_figure_captions,
            replace_references,
            inline_footnotes,
    ]:
        altered = walk(altered, action, fmt, meta)

    doc['blocks'] = altered

    json.dump(doc, sys.stdout)
    sys.stdout.flush()


if __name__ == '__main__':
    main()