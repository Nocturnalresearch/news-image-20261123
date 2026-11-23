# Solemn Horizon — World News, Monday 23 November 2026

[![make.fun](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/c/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Nocturnalresearch/news-image-20261123/rank.svg)](https://make.fun/c/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Nocturnalresearch/news-image-20261123/reward.svg)](https://make.fun/c/news-image-20261123)

A newspaper front page for Monday, 23 November 2026, drawn entirely in
code (PIL) — no photographs, no AI-generated imagery. The program copies
the finished page to `/output/entry.png`.

## The four stories

1. **CLIMATE — COP31 collapses in Antalya.** The COP31 climate conference
   in Antalya, Turkey, collapsed on Sunday after more than two weeks of
   talks: nearly 200 countries failed to agree an overarching deal. The
   final "Antalya Pact" draft did not mention fossil fuels at all, and the
   EU, Panama, the Marshall Islands, Norway and others rejected it. The
   longest COP in history, and the first major breakdown since COP15
   Copenhagen 2009. COP31 president Murat Kurum conceded there was no
   consensus. The US was not part of the talks.
   Sources: CNN, Le Monde, NPR, phys.org, 22 Nov 2026.
2. **THE GULF — Bahrain: two hurt as Gulf war widens.** Bahrain said two
   people were injured in Iran's Saturday-night missile/drone attacks — a
   Bahraini citizen in stable condition and a Pakistani resident in
   critical condition; a fire broke out at a civilian industrial facility
   on Sitra Island. The IRGC claims it struck two US Patriot radars at the
   Al-Riffa and Awali bases. A Houthi ballistic missile was fired at
   western Saudi Arabia and intercepted by the Saudi-led coalition. 14+
   Iranian tankers sit at Kharg Island ready to try breaking the US
   blockade.
   Sources: thedefensenews (Reuters), military-affairs, thegenevatimes,
   22 Nov 2026.
3. **UKRAINE — Drone flattens Kyiv flats, 14 missing.** A Russian drone
   struck a five-storey apartment building in Demydiv (Dymer), Kyiv
   region, early Sunday: part of the entrance collapsed, nine evacuated,
   14 missing, two bodies later recovered. Zelenskyy said Russia launched
   ~2,700 drones, nearly 1,460 aerial bombs and 165 missiles across 20
   regions in the past week, and urged the US to release Patriot
   interceptor missiles Ukraine's partners already paid for. US-brokered
   talks open in Abu Dhabi on Tuesday.
   Sources: europesays (SANA), finwire, Al Jazeera, 22 Nov 2026.
4. **MEXICO — "El Chapo Isidro" captured in Sinaloa.** Mexican special
   forces captured Fausto Isidro Meza Flores, known as "El Chapo Isidro"
   — one of the FBI's 10 most wanted fugitives — in Guasave, Sinaloa, on
   Friday night; the firefight left 11 dead (four soldiers, seven
   gunmen). He was flown to Mexico City with his second-in-command and
   alleged financial operator to face US narcoterrorism and
   drug-trafficking charges. US intelligence helped the operation. (Not
   the same man as Joaquín "El Chapo" Guzmán.)
   Sources: CNN, AP/NPR, Al Jazeera/BBC, 21–22 Nov 2026.

Footer note: Democrats clinch US House majority — 258 seats, largest
since 1992.

## How to run

```sh
python3 draw_news.py   # redraws entry.png (1024x1024, deterministic)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png`. The program runs twice with no network and writes
identical bytes both times.

## Entry

- Competition: [news-image-20261123](https://make.fun/c/news-image-20261123)
- Entry name: **Solemn Horizon**
- Image: `entry.png` (1024×1024 PNG, under 1 MiB)
- License: MIT (see `LICENSE`)
