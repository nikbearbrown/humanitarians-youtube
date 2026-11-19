# Week of 10-12-2026: From a Report Table to a Textbook Table

**Fellow:** Risa Samanta
**Project:** Medhavy cancer textbook (CAJAL)
**Role:** Machine Learning Engineer
**Note on dating:** This report was written on 10-12-2026, after the week it covers. The method it describes comes from my table-building chat.

---

## Summary

A how-to on turning a table from a CAJAL report into a finished MDX table with a PDF preview. 

## The method

1. Give Claude one finished table file (`ch14_visual11.mdx`) and its preview as the style template.
2. Give it the chapter's audit file, whose entries are marked "Type: Table".
3. Ask for matching MDX files and a PDF preview.
4. Check every row against the chapter text, and ask about anything left out.

## Examples

- **Chapter 25:** Visual 6 (TKI Target Classification) and Visual 18 (Biomarker Type Classification), with `ch25_tables_preview.pdf`. No red, because nothing in them is negative.
- **Chapter 23:** Table 23.2.1 has no G1 row (the chapter names no G1-specific drug class). Table 23.5.2 goes between line 126 and the next heading in the 23.5 file.
- **Chapter 32:** Mesenchymal and Neural subtypes carry a gray note, because the source gives no treatment response.

## Open items

- Line 124 of the 23.5 file still says "non-proliferating" where Evin's note says "slow cycling".
- Whether Evin wants a G1 row in Table 23.2.1.

## Hours

30 hours 

## Videos this week

- How-to: from a report table to a textbook table (cli-explainer, Bella). https://drive.google.com/file/d/1dQgfo1mCXDn-rZmYvVDhU7vOxL7our3E/view?usp=drive_link
