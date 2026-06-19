# RICE Image Style Guide

## C86 × South × St. Expedite Press

RICE images should feel like evidence from a regional counterculture: photocopied but precise, devotional without nostalgia, agricultural without pastoral sentiment, and severe without becoming sterile.

The image system combines three registers:

- **C86:** amateur immediacy, xerox grain, flash photography, clipped framing, DIY print artifacts.
- **The South:** weather, labor, infrastructure, crops, water, roadside light, parish records, devotional residue.
- **St. Expedite Press:** ritual severity, archival attention, black fields, registration marks, objects treated as charged evidence.

The goal is not “vintage Southern photography.” The goal is a contemporary document whose surface remembers print.

---

## 1. Governing principles

### Evidence over atmosphere

Every image should contain something specific enough to be examined:

- a pump housing;
- an invoice number;
- a bent rice head;
- a flood gauge;
- a receipt;
- a fluorescent fixture;
- a saint card taped inside a machine cabinet.

Atmosphere may surround the evidence, but cannot replace it.

### The present tense

Avoid presenting the South as vanished, sepia, quaint, or safely historical. Contemporary machinery, plastic, power lines, security lights, drainage systems, and cheap materials belong in frame.

### Beauty under pressure

Images may be beautiful, but their beauty should be interrupted by labor, accounting, weather, infrastructure, debt, or use.

### One unresolved element

Every principal image should contain one detail that is not immediately explained: a distant light, cropped notation, open cabinet, registration symbol, torn edge, or object outside the expected context.

---

## 2. Core visual grammar

### Tonality

- Primarily black and white.
- Dense blacks; paper-colored highlights rather than pure white.
- Midtones may be compressed like a photocopy.
- Retain important shadow detail around the subject.
- Avoid polished silver-gelatin luxury.

Recommended treatment:

```css
filter: grayscale(100%) contrast(1.15) brightness(0.96);
```

Hover or active state:

```css
filter: grayscale(15%) contrast(1.08);
```

### Accent color

Use only one registration accent per image or layout.

Primary:

```text
Acid registration yellow
#D9FF00
```

Secondary exceptions:

```text
Survey orange     #FF5A1F
Faded process blue #4D72A8
Oxide red          #8A281F
```

Do not combine accent colors in normal editorial imagery. Multiple process colors are reserved for printer marks, proof sheets, or deliberate misregistration.

### Paper

Preferred paper tones:

```text
Warm stock      #F9F8F4
Ledger stock    #E8E1D1
Newsprint       #D8D4C8
Copy-bed black  #090909
```

### Texture

Approved:

- photocopy grain;
- toner dropout;
- dust and scanner marks;
- paper fibers;
- soft water damage;
- staple or binding shadows;
- slight registration drift;
- restrained halftone;
- imperfect cut edges.

Avoid:

- generic film scratches;
- heavy fake VHS damage;
- decorative grunge brushes;
- blanket distressed overlays that obscure evidence;
- antique sepia filters.

---

## 3. Composition

### Default frame

- Wide 16:9 for features.
- 4:3 for archival records and physical objects.
- 3:4 for portraits and vertical social crops.
- Keep a recognizable horizon or document edge whenever possible.

### Subject placement

Favor asymmetric placement:

- subject in the upper-right;
- quiet shadow or low-detail field in the lower-left;
- horizon above or below center;
- machinery cropped by one edge;
- documents entering from outside the frame.

This reserved space accommodates captions, metadata, or editorial panels without covering the evidence.

### Distance

Use three preferred distances:

1. **Field distance:** broad landscape with infrastructure visible.
2. **Working distance:** machine, table, room, or object in context.
3. **Evidence distance:** crop, stain, handwriting, fastener, serial number.

Avoid generic medium-wide “cinematic” compositions with no material focus.

### Camera behavior

- Locked-off or deadpan.
- Direct flash for portraits and interiors.
- Overhead copy-bed view for documents.
- Slightly low viewpoint for machines and structures.
- No excessive depth-of-field blur.
- No dramatic drone photography.

---

## 4. Recurring subject vocabulary

### Agriculture

- rice heads;
- crawfish traps;
- irrigation gates;
- flooded rows;
- drainage ditches;
- grain elevators;
- bags, scales, and grading tables.

### Infrastructure

- pump houses;
- levees;
- power lines;
- culverts;
- security lights;
- pipelines;
- highway frontage;
- industrial fans and control boxes.

### Documents

- ledgers;
- receipts;
- crop liens;
- survey maps;
- invoices;
- weather logs;
- handwritten maintenance notes;
- parish forms.

### Devotional residue

- saint cards;
- votive wax;
- prayer slips;
- faded church bulletins;
- red cloth;
- medals attached to work spaces.

Use devotional material as lived evidence, never as gothic decoration.

### Domestic and roadside

- fluorescent kitchens;
- convenience stores;
- screen doors;
- motel curtains;
- dashboard shrines;
- plastic chairs;
- hand-painted signs;
- damp drywall.

---

## 5. Image families

### A. Section feature

Purpose: introduce a body of writing.

Rules:

- wide documentary composition;
- one dominant material subject;
- quiet region for interface or metadata;
- black-and-white base;
- one registration accent;
- no embedded title text generated into the image.

Current examples:

- `images/feature-essays.jpg`
- `images/feature-fiction.jpg`
- `images/feature-poetry.jpg`
- `images/feature-archive.png`

### B. Article figure

Purpose: complicate or document the prose.

Rules:

- caption always includes figure number, source, location, or accession;
- may escape the reading column;
- should add information rather than merely repeat mood;
- no decorative stock photography.

### C. Archive object

Purpose: present a record as evidence.

Rules:

- straight-on or overhead;
- full object visible in the primary record;
- detail crops permitted in secondary views;
- identify reconstructions clearly;
- preserve provenance and accession data;
- do not fabricate historical claims from model-generated text.

### D. Author portrait

Purpose: identify a contributor without literary glamour.

Rules:

- direct flash or hard window light;
- ordinary working or domestic environment;
- subject may look away;
- hands and clothing remain natural;
- no soft lifestyle portraiture;
- no staged writing desk, typewriter, or books-as-props.

### E. Physical publication

Purpose: show RICE as a manufactured object.

Rules:

- copier bed, packing table, floor, or printer surface;
- emphasize paper, staples, folds, ink density, and scale;
- include ruler, crop marks, or edition notation;
- avoid luxury-product lighting.

Current example:

- `images/issue-specimen.jpg`

### F. Social crop

Purpose: announce without turning into generic promotional graphics.

Rules:

- crop from an existing editorial image;
- add no more than title, author, issue, and URL;
- preserve paper margins;
- use type as a registration label, not a centered ad headline;
- never place more than one call to action.

---

## 6. Typography inside images

Prefer adding typography in HTML, CSS, or layout software after image generation.

When text must exist inside an image:

- use only labels, stamps, accession marks, handwritten notes, or object-native printing;
- generated text must not carry factual historical claims;
- keep body text illegible or incidental;
- verify all prominent words manually.

Display typography:

- grotesque;
- condensed;
- black;
- tightly tracked;
- cropped by the frame when appropriate.

Metadata typography:

- monospace;
- uppercase;
- small;
- spaced like a filing label.

---

## 7. Model-generation prompt structure

Use this order:

```text
[documentary format]
[specific Gulf South subject]
[time/weather/light]
[material evidence]
[composition and reserved space]
[tonal treatment]
[single accent]
[exclusions]
```

### Universal prompt suffix

```text
Contemporary documentary realism, severe independent-literary-magazine
art direction, monochrome photocopy texture, dense blacks, warm paper
highlights, one tiny acid-yellow registration accent, specific material
evidence, no nostalgia, no cinematic glamour, no people unless requested,
no title text, no logo, no decorative frame.
```

### Universal negative prompt

```text
sepia nostalgia, plantation romance, cowboy imagery, generic rural sunset,
luxury editorial photography, shallow depth of field, teal-and-orange color,
fashion pose, gothic cliché, abandoned-house tourism, decorative grunge,
fake film border, handwritten inspirational quote, random typography,
watermark, logo, illegible headline
```

---

## 8. Prompt presets

### Essay feature

```text
Wide documentary photograph of [specific object or infrastructure] in
[parish/location], with [ledger/map/receipt/tool] visible as material
evidence. Reserve the lower-left half as quiet low-detail shadow for an
editorial panel; place the strongest subject in the upper-right. Hard
available light, contemporary Gulf South, unsentimental, monochrome
photocopy grain, one tiny acid-yellow registration mark.
```

### Fiction feature

```text
Locked-off nocturnal photograph of [location] during [weather event or
shift], one active machine or fluorescent source, evidence of recent human
use but no visible person. Keep the lower-left dark and quiet for a title
panel; place the structure and light in the upper-right. Dense black-and-
white toner texture, realistic water and electrical infrastructure.
```

### Poetry feature

```text
Wide field image of [precise natural and manufactured details], devotional
but unsentimental, insects and water rendered as material facts rather than
symbols. Reserve lower-left negative space; concentrate stalks, traps, and
machinery toward the upper-right. High-contrast monochrome, rough paper
grain, tiny acid-yellow survey mark.
```

### Archive composition

```text
Overhead archival copy-bed arrangement of [specific records], authentic
paper damage, ruled forms, accession stamp, ruler, map fragments, and
handwritten maintenance notation. Keep the lower-left half as clean black
copy-bed space for a title card; arrange documents along the top and right.
Straight overhead, no hands, no decorative props.
```

### Author portrait

```text
Direct-flash documentary portrait of [writer description] in [ordinary
specific environment], neutral posture, practical clothing, visible room
texture, no literary props, no glamour retouching. Hard black-and-white,
slightly off-register photocopy reproduction, plain wall or workplace
evidence, contemporary and unsentimental.
```

---

## 9. Cropping and responsive behavior

### Desktop

- preserve full environmental context;
- use `object-position` to keep evidence away from overlaid metadata;
- permit a 40–60% quiet region when a panel sits inside the frame.

### Mobile

- crop toward the primary evidence, not merely the center;
- title and metadata remain separate HTML layers;
- reduce caption width;
- test at 390 × 844;
- never crop out the material clue that gives the image meaning.

Recommended:

```css
object-fit: cover;
object-position: 68% center;
```

Adjust per image rather than applying one universal focal point.

---

## 10. Archive and AI disclosure

Model-generated archival images are **visual reconstructions**, not authenticated documents.

Required handling:

- label them as reconstructions in captions or metadata;
- do not attribute them to a real archive unless that archive supplied the source;
- do not imply generated names, dates, weights, or signatures are factual;
- use real scans whenever publication rights and source quality permit;
- retain prompt and model provenance internally.

Suggested caption:

```text
RICE visual reconstruction / generated from editorial direction /
not an authenticated historical record
```

---

## 11. Rejection checklist

Reject an image if:

- it could illustrate any generic Southern publication;
- it romanticizes poverty, labor, or rural decay;
- the only regional signal is Spanish moss or a sunset;
- the image has no inspectable material detail;
- texture overwhelms subject;
- color appears without editorial purpose;
- the composition leaves no usable type or metadata space;
- generated text makes unsupported claims;
- it resembles commercial lifestyle, tourism, or luxury publishing;
- it looks “old” but says nothing about the present.

---

## 12. Final test

An approved RICE image should answer yes to at least four:

- Is there evidence?
- Is there pressure?
- Is there a specific place or system?
- Does the present remain visible?
- Could it survive photocopying?
- Does it leave room for editorial intervention?
- Is its beauty complicated?
- Does it belong to RICE and not merely “the South”?

