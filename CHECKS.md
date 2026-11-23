# CHECKS — news-image-20261123 ("Solemn Horizon")

## Competition exists live
- Confirmed 2026-11-23 ~07:10 WIB via https://make.fun/api/competitions
  (95 competitions, limit=100, full list read, next_cursor None).
- news-image-20261123: published 2026-11-23T00:00:00Z (07:00 WIB, on time),
  deadline 2026-11-25T00:00:00Z (Tue 25 Nov 07:00 WIB), $100 prize.
- Entry fee: none (entryFeesUsd "0.00"). Top 50 paid ($20/$12/$6,
  $2 ranks 4–10, $1.20 ranks 11–50). 46 submissions at check time.

## Escrow locked
- RULES.txt: escrow GmraU3gZW4xR2cH4htNvNXyVWETCKcTgpRCn7fvy2BTU, vault
  BidqmVyx46bVRv4tv2dEUw4njWDUApW13v3bbE6Zq4z7, mint
  EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v, rules_sha256
  444e0a0c67da67369a24059109d7452aa035327b2d45eb1896b1da1e989cb999
  matching the kit bundle_sha256. "Total $100.00 ... paid from the
  escrow." — no HTTP 409 "Reward is not locked in escrow yet" expected.

## Grading
- AI judge pairwise, judge z-ai/glm-5.3-flash, no news feed, not told the
  day. Criteria in order: (1) names the day — specific 23 Nov 2026 events,
  date shown; (2) selection/breadth across regions/fields; (3) readability
  from the image alone; (4) faithful, no hype/speculation as fact;
  (5) craft, legible at ~300px, no garbled text.
- Program runs twice, no network, both runs same bytes.

## Cost / credential
- None. Free entry, no provider key, no paid dependency.

## Stories + sources (all verified, 21–23 Nov 2026)
1. CLIMATE — COP31 collapses in Antalya (lead): CNN, Le Monde, NPR,
   phys.org, 22 Nov 2026.
2. THE GULF — Bahrain: two hurt, war spreads to Saudi Arabia:
   thedefensenews (Reuters), military-affairs, thegenevatimes, 22 Nov 2026.
3. UKRAINE — Drone hits Kyiv flats, 14 missing: europesays (SANA),
   finwire, Al Jazeera, 22 Nov 2026.
4. MEXICO — "El Chapo Isidro" captured, 11 dead: CNN, AP/NPR,
   Al Jazeera/BBC, 21–22 Nov 2026.
- Footer: Democrats clinch US House majority — 258 seats (not a story).

## Image verification (in-session)
- entry.png: 1024x1024 PNG, ≤1 MiB.
- main.py run twice → identical sha256 (see PARENT-HANDOFF.md).
- Viewed at full size and at ~300px: masthead date "MONDAY, 23 NOVEMBER
  2026" and all four headlines legible, no garbled text, no overlap.

## Repo
- New repo Nocturnalresearch/news-image-20261123, all files written fresh
  in-session (main.py, draw_news.py, entry.png, README.md, LICENSE,
  CHECKS.md). No files copied from the 17/18/19/20/21/22 Nov repos.
- README carries the three live make.fun badges for news-image-20261123
  (competition badge + rank + reward), no {owner} placeholders, no
  shields.io badge.
- LICENSE is MIT with an SPDX-License-Identifier: MIT line.
- No .makefun/owner.json created locally (parent creates it in the
  browser with wallet Tyjmw5GN1LTzwx3Tkks9xZgSntEJrjRQ9K5YGWssWir).
