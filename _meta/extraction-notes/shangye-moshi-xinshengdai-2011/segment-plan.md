# Segment Plan

| segment_id | level | title | source_file | role | process |
| --- | --- | --- | --- | --- | --- |
| S00 | frontmatter | 书名页、版权页、创新七张面孔、目录 | ch001-ch017 | frontmatter | merge/raw-only |
| S01 | part | 画布 | ch018-ch060 | framework | keep |
| S02 | part | 式样 | ch061-ch124 | pattern-library | keep |
| S03 | part | 设计 | ch125-ch181 | design-method | keep |
| S04 | part | 战略 | ch182-ch222 | strategy-method | keep |
| S05 | part | 流程 | ch223-ch233 | workflow | keep |
| S06 | part | 展望 | ch234-ch246 | outlook | merge |
| S07 | backmatter | 后记、参考文献、市场反响、作者简介 | ch247-ch255 | backmatter | raw-only/merge |

## Processing Notes

The EPUB is visually fragmented. The stable structure is the table of contents, not individual HTML files. Formal compilation uses TOC-level modules and source ranges, while `chapter-inventory.md` preserves every extracted spine item.
