"""Draw the WORLD NEWS front page for Monday, 23 November 2026.

Deterministic PIL drawing (no network, no randomness): a 1024x1024 PNG
newspaper front page with four verified stories of 23 Nov 2026.

Run:  python3 draw_news.py   (writes entry.png beside this file)
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
HERE = Path(__file__).resolve().parent

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS_I = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"
DEJAVU_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    """Greedy word wrap returning a list of lines that fit max_width."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


# ---------------------------------------------------------------- palette
PAPER = (248, 244, 232)
INK = (20, 20, 20)
NAVY = (22, 35, 63)
GOLD = (233, 196, 106)
RED = (179, 38, 30)
GREY = (90, 90, 90)
RULE = (180, 170, 150)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------------------------------------------------------------- masthead
d.rectangle([0, 0, W, 124], fill=NAVY)
d.rectangle([0, 124, W, 129], fill=GOLD)
f_title = font(SERIF_B, 58)
title = "WORLD NEWS"
tw = d.textlength(title, font=f_title)
d.text(((W - tw) / 2, 14), title, font=f_title, fill=(255, 255, 255))
f_date = font(SANS_B, 27)
date = "MONDAY, 23 NOVEMBER 2026"
dw = d.textlength(date, font=f_date)
d.text(((W - dw) / 2, 82), date, font=f_date, fill=GOLD)

# ---------------------------------------------------------------- lead: COP31
LX, LW = 36, 600
f_tag = font(DEJAVU_B, 19)
d.text((LX, 146), "CLIMATE  —  ANTALYA, TURKEY", font=f_tag, fill=RED)
f_head = font(SERIF_B, 37)
lead_head = wrap(d, "COP31 COLLAPSES — NO CLIMATE DEAL", f_head, LW)
y = draw_lines(d, lead_head, LX, 176, f_head, INK, 44)
f_sub = font(SANS, 21)
lead_sub = wrap(
    d,
    "Longest summit in history ends without agreement as the EU rejects "
    "a pact that never mentions fossil fuels. Nearly 200 countries fail "
    "to agree; COP31 president Murat Kurum concedes there is no consensus.",
    f_sub, LW,
)
draw_lines(d, lead_sub, LX, y + 8, f_sub, (40, 40, 40), 27)

# Lead illustration: a cracked globe over Antalya.
IX, IY, IW, IH = 668, 146, 320, 236
d.rectangle([IX, IY, IX + IW, IY + IH], fill=(207, 227, 238))
d.rectangle([IX, IY, IX + IW, IY + IH], outline=INK, width=2)
d.ellipse([IX + 18, IY + 14, IX + 62, IY + 58], fill=(245, 200, 90))  # sun
cx, cy, r = IX + 165, IY + 128, 88
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(46, 109, 164))  # globe
d.ellipse([cx - 52, cy - 58, cx + 6, cy - 8], fill=(74, 160, 90))
d.ellipse([cx - 6, cy + 18, cx + 58, cy + 62], fill=(74, 160, 90))
d.ellipse([cx - 78, cy + 22, cx - 30, cy + 58], fill=(74, 160, 90))
# red crack across the globe
d.line([(cx - 70, cy - 70), (cx - 28, cy - 18), (cx - 52, cy + 22),
        (cx - 4, cy + 52), (cx + 30, cy + 78)], fill=RED, width=6)
d.line([(cx - 70, cy - 70), (cx - 28, cy - 18)], fill=RED, width=6)
f_cap = font(SANS_I, 15)
cap = "COP31 in Antalya ends in collapse."
d.text((IX, IY + IH + 8), cap, font=f_cap, fill=GREY)
d.line([36, 448, W - 36, 448], fill=RULE, width=2)

# ---------------------------------------------------------------- bottom row
COLS = [
    {
        "tag": "THE GULF  —  BAHRAIN",
        "head": "BAHRAIN: TWO HURT AS GULF WAR WIDENS",
        "sub": "Missiles hit US Patriot sites; Houthis strike Saudi "
               "Arabia. 14 tankers mass at Kharg to test the blockade.",
        "kind": "bahrain",
    },
    {
        "tag": "UKRAINE  —  KYIV REGION",
        "head": "DRONE FLATTENS KYIV FLATS — 14 MISSING",
        "sub": "Zelenskyy urges US to release Patriots after a week of "
               "2,700 drones. Abu Dhabi talks open Tuesday.",
        "kind": "ukraine",
    },
    {
        "tag": "MEXICO  —  SINALOA",
        "head": "\u201cEL CHAPO ISIDRO\u201d CAPTURED IN SINALOA",
        "sub": "FBI most-wanted cartel boss seized as 11 die in the raid; "
               "flown to Mexico City to face US charges.",
        "kind": "mexico",
    },
]

f_ctag = font(DEJAVU_B, 16)
f_chead = font(SERIF_B, 23)
f_csub = font(SANS, 18)
COL_W, COL_GAP, COL_Y = 304, 20, 470
for i, col in enumerate(COLS):
    x = 36 + i * (COL_W + COL_GAP)
    # illustration box
    iy, ih = COL_Y, 168
    if col["kind"] == "bahrain":
        d.rectangle([x, iy, x + COL_W, iy + ih], fill=(28, 43, 69))
        # radar arcs + explosion burst
        d.arc([x + 30, iy + 60, x + 130, iy + 160], 180, 360,
              fill=(120, 200, 120), width=4)
        d.arc([x + 55, iy + 85, x + 105, iy + 135], 180, 360,
              fill=(120, 200, 120), width=4)
        d.line([(x + 80, iy + 110), (x + 80, iy + 160)], fill=(120, 200, 120), width=4)
        bx, by = x + 215, iy + 70
        for dx, dy in [(0, -34), (24, -24), (34, 0), (24, 24), (0, 34),
                       (-24, 24), (-34, 0), (-24, -24)]:
            d.line([(bx, by), (bx + dx, by + dy)], fill=(245, 160, 60), width=5)
        d.ellipse([bx - 16, by - 16, bx + 16, by + 16], fill=(245, 200, 90))
        d.line([(x + 20, iy + 20), (bx - 20, by - 10)], fill=(255, 255, 255), width=3)
    elif col["kind"] == "ukraine":
        d.rectangle([x, iy, x + COL_W, iy + ih], fill=(196, 205, 214))
        # apartment block, top corner broken away, smoke above
        d.rectangle([x + 60, iy + 55, x + 244, iy + 168], fill=(138, 138, 138))
        d.polygon([(x + 60, iy + 55), (x + 150, iy + 55), (x + 150, iy + 95),
                   (x + 110, iy + 95), (x + 110, iy + 75), (x + 60, iy + 95)],
                  fill=(70, 70, 70))
        for wx in (x + 80, x + 120, x + 160, x + 200):
            for wy in (iy + 105, iy + 135):
                d.rectangle([wx, wy, wx + 22, wy + 18], fill=(250, 220, 90))
        d.ellipse([x + 90, iy + 8, x + 140, iy + 48], fill=(120, 120, 120))
        d.ellipse([x + 130, iy + 18, x + 180, iy + 58], fill=(150, 150, 150))
        d.polygon([(x + 150, iy + 95), (x + 175, iy + 60), (x + 195, iy + 95)],
                  fill=(230, 110, 40))
    else:  # mexico: police badge + handcuffs
        d.rectangle([x, iy, x + COL_W, iy + ih], fill=(36, 72, 52))
        sx, sy = x + 152, iy + 84
        star = []
        import math
        for k in range(10):
            ang = math.pi / 2 + k * math.pi / 5
            rr = 62 if k % 2 == 0 else 26
            star.append((sx + rr * math.cos(ang), sy - rr * math.sin(ang)))
        d.polygon(star, fill=(233, 196, 106), outline=(120, 90, 20))
        d.ellipse([sx - 26, sy - 26, sx + 26, sy + 26], fill=(36, 72, 52))
        d.ellipse([sx - 26, sy - 26, sx + 26, sy + 26], outline=(233, 196, 106), width=3)
        d.ellipse([x + 42, iy + 128, x + 82, iy + 168], outline=(220, 220, 220), width=5)
        d.ellipse([x + 222, iy + 128, x + 262, iy + 168], outline=(220, 220, 220), width=5)
        d.line([(x + 82, iy + 148), (x + 222, iy + 148)], fill=(220, 220, 220), width=5)
    d.rectangle([x, iy, x + COL_W, iy + ih], outline=INK, width=2)

    ty = COL_Y + ih + 14
    d.text((x, ty), col["tag"], font=f_ctag, fill=RED)
    head_lines = wrap(d, col["head"], f_chead, COL_W)
    y2 = draw_lines(d, head_lines, x, ty + 26, f_chead, INK, 28)
    sub_lines = wrap(d, col["sub"], f_csub, COL_W)
    draw_lines(d, sub_lines, x, y2 + 6, f_csub, (40, 40, 40), 23)

# ---------------------------------------------------------------- footer
d.line([36, 952, W - 36, 952], fill=RULE, width=2)
f_foot = font(SANS, 16)
foot1 = "Also: Democrats clinch US House majority \u2014 258 seats, largest since 1992."
fw = d.textlength(foot1, font=f_foot)
d.text(((W - fw) / 2, 962), foot1, font=f_foot, fill=(40, 40, 40))
f_src = font(SANS_I, 14)
foot2 = "Sources: CNN, Le Monde, NPR, AP, Al Jazeera, BBC \u2014 21\u201323 November 2026"
fw2 = d.textlength(foot2, font=f_src)
d.text(((W - fw2) / 2, 986), foot2, font=f_src, fill=GREY)

img.save(HERE / "entry.png", format="PNG", optimize=True)
print("wrote", HERE / "entry.png", img.size)
