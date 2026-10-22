# Integration review, Parts I to VI (round 2, final)

Reviewer: integration gate, 2026-10-22. Read-only on the papers.

Sources checked: the current .tex files (12:27 to 12:34 local) and the PDFs rebuilt from them (12:27 to 12:35). Numbering ground truth is `pdftotext papers/pdf/<slug>.pdf`. Result numbers in all six PDFs are identical to round 1. Every cited section number was re-checked in both the .tex and the PDF.

**Start here (optional, 1 minute):** coercive-power.tex L116, replace the 3 occurrences of `\lambda_{ij}` with `f_{ij}` (item 18). It is the only open item, and it does not block integration.

## Counts (round 2)

| Severity | Open | Resolved since round 1 |
|---|---|---|
| WRONG-NUMBER | 0 | 7 |
| WRONG-CONTENT | 0 | 4 |
| REDEFINITION | 0 | 1 |
| NOTATION | 1 (new, non-blocking) | 5 |
| "Depends on no other pillar" sentences | 0 | n/a |

All 48 numbered cross-Part references resolve to the right object in the target PDF:

| Part | Refs |
|---|---|
| I | 10 |
| II | 5 |
| III | 1 (new: Part II Def 2.1) |
| IV | 8 |
| V | 10 |
| VI | 14 |

No new breakage.

## Summary table

| Part | (a) Single ownership | (b) Cross-refs: numbered refs / broken | (c) Notation | Shared codings | No-dependency sentences |
|---|---|---|---|---|---|
| I financial | PASS | 10 / 0 | PASS | PASS (parlements recoded, L370) | none |
| II political | PASS | 5 / 0 | PASS (no \lambda left) | PASS (reference coding) | none |
| III judicial | PASS (Def 2.1 now cites II) | 1 / 0, plus unnumbered refs correct | PASS (\Read = \mathfrak{R}) | PASS (Guardian Council cell recoded, L550) | none (see note W1) |
| IV ideological | PASS | 8 / 0 | PASS (owns lambda_k) | PASS | none |
| V coercive | PASS | 10 / 0 | NOTE: lambda_{ij} at L116 (item 18) | PASS (bondage per VI Def 2.4) | none (see note W2) |
| VI productive | PASS | 14 / 0 | PASS | PASS | none |

## Round 1 items: resolution

| # | Severity | Part, location | Status (current text) |
|---|---|---|---|
| 1 | WRONG-NUMBER | financial L476 | RESOLVED: "Proposition 6.7 of \citealt{long2026productive}" = VI Rentier comparative static |
| 2 | WRONG-NUMBER | financial L547 | RESOLVED: "Definition 2.8 and Proposition 6.8" = VI Instruments on the outside option, Gate |
| 3 | WRONG-NUMBER | political L267 | RESOLVED: "Proposition~6.4" = V Coup-proofing |
| 4 | WRONG-NUMBER | ideological L624 | RESOLVED: "Proposition 3.6 of Part VI" = VI Latent veto |
| 5 | WRONG-NUMBER | productive L163 | RESOLVED: "its Proposition 4.3" = III Repeat-player contest |
| 6 | WRONG-NUMBER | productive L419 | RESOLVED: "its Proposition 4.3" |
| 7 | WRONG-NUMBER | productive L340 | RESOLVED: "its Sections 5.4 and 6.3" = I Islamic states, Soft budgets, rents and fusion |
| 8 | WRONG-CONTENT | coercive L565 | RESOLVED: the metaphorical-bondage sentence is gone (0 hits). It now reads "Following Part~VI, the series reserves the word bondage ..." |
| 9 | WRONG-CONTENT | financial L370 | RESOLVED: "on the Parlements' registration and remonstrance of royal edicts (a rule-making veto in Part~II's coding)" |
| 10 | WRONG-CONTENT | judicial L550 | RESOLVED: "Iran's Guardian Council jurists rule on the Islamic and constitutional validity of bills (the resulting veto and candidate screening are coded $\pP$)" |
| 11 | WRONG-CONTENT | financial L305 | RESOLVED: "Part IV summarizes it \citep[Section 4.2]{long2026ideological}, and Part VII compares it". IV Sec 4.2 holds the Mann paragraph (PDF-confirmed) |
| 12 | REDEFINITION | judicial L108 | RESOLVED: "rule system with open texture ... $R$ a rule system in the sense of \citet[Definition~2.1]{long2026political}" |
| 13 | NOTATION | political Prop 6.5, coercive L132 | RESOLVED for the cited object: \lambda_S and \bar\lambda are now \bar f_S and \bar f in II (0 \lambda left in II) and in V L132. See item 18 for a second lambda in V that round 1 missed |
| 14 | NOTATION | judicial L60 | RESOLVED: `\newcommand{\Read}{\mathfrak{R}}` |
| 15 | NOTATION | coercive | RESOLVED: 0 occurrences of \mathcal{R}^0; the reference rule set is $R^0$ |
| 16 | NOTATION | coercive L123 | RESOLVED: weights are \omega^{\pC}_k; 0 occurrences of \beta_k |
| 17 | NOTATION | contracts | RESOLVED: judicial contract L34 is \mathbf{q}_t = (q^{dis}, q^{acc}, q^{ind}, q^{cmp}); coercive contract L5 to L6 and L31 to L34 use d_{i,t}, \psi(v,y), \Delta^c, \Delta^a, \mu, R^0 |

## Conflicts (round 2)

18. (coercive-power, coercive control share chain-of-command rule in Def 2.2 at L116, replace every "\lambda_{ij}" with "f_{ij}" (3 occurrences on L116, including "1 - \lambda_{ij}")). NOTATION. Here lambda_{ij} is the share of decisions in which j follows i's directives, so high means controlled. In IV, lambda_k is the probability that an authority is independent, so high means uncontrolled. This is the same reversed polarity that item 13 removed from II, and round 1 missed this occurrence. f_{ij} matches Part II's f_{S,o}, the share of a holder's decisions that follow S's directives, and is unused in V. Non-blocking.

## No-dependency scan

**Result: 0 sentences in any Part say a pillar depends on no other pillar.**

What was scanned:
- Every sentence in all six Parts (bibliographies excluded) was checked for these phrases: "no other pillar", "depends on no", "needs/requires no other", "independent of the other pillars", "on neither", "does not depend on", "need not", "self-sufficient", "in isolation", "stands alone", "without ... pillar", "does not route", "does not need".
- Every sentence was also checked for negated forms of depend, require, need, rely or presuppose near a pillar term.

Round 1 had one such sentence, at Part V Cor 3.7, "coercion of this kind depends on no other pillar". It now reads (L254): "does not need the $\pF \to \pC$ or $\pI \to \pC$ arc ...; it still depends on the other pillars through the arcs of \cref{sec:depint}, for example $\pW \to \pC$."

Watch items. These are not conflicts: each says the pillar depends on SOME other pillar, but each is weaker than a pairwise reading of "full interdependence". The author should confirm that the ruling permits disjunctive (hyperedge) dependencies.
- **W1** (judicial-power L322): "The judicial function therefore depends on the legitimation pillar or on the coercion pillar, and on neither specifically." Prop 3.6 is an OR-dependency on I or C, and III L326 also states that J feeds P and I. If the ruling requires every ordered pair to be an arc, delete ", and on neither specifically" from L322; otherwise leave it.
- **W2** (coercive-power L241): "Term (d) does not route the dependency through $\pF$ or $\pI$." L254 then names W→C as the remaining dependency. Consistent with the ruling as written.

Also reviewed and not flagged:
- financial L358 and L476: a rentier state "does not depend on taxpayers". This concerns domestic tax bargaining, not the productive pillar. Part VI Lemma 3.4 (relocation) covers the dependence on production elsewhere.
- productive L743: "a status that no other pillar has". This concerns the latent veto, not dependency, and the same sentence affirms that all six functions depend on one another.

## Other checks with no finding

- **(a) Ownership:** the list of numbered environments is unchanged in all six PDFs. No Part re-defines a shared core object (G_t, layers, weights, s, H, Q, U_t, C_{mn}, \mathcal{I}_t, capture link) or a sibling's pillar object.
- **(b) Recently renumbered results:** every citation of a recently renumbered result resolves:
  - III Prop 3.6 (cited by V L158 and L241).
  - IV Prop 6.2 and Sec 6.6 (cited by I L326 and VI L604).
  - V Prop 3.6 and Cor 3.7 (cited by I L478, with Cor 3.7's three conditions stated).
  - II Prop 6.5 (cited by V L132, paraphrase matches (a) to (c)).
- **(b) Unnumbered claims:** unnumbered sibling claims in Parts II, IV, V and VI were re-read after the fix-verification edits; all remain accurate. For example, V L575 and IV L622 agree that refusal of unlawful orders depends on legitimating beliefs.
- **(c) Notation:**
  - All six papers define \pF to \pW as \mathsf and \Int or \Integ as \mathcal{I}. No bare I_t appears.
  - \mathcal{R} now has one meaning across the series: Part II's class of rule systems.
- **Codings:**
  - Guardian Council (vetting and screening are P, constitutional interpretation is J) and Bourbon parlements (registration and remonstrance are P, appellate is J) are consistent across I, II, III and V.
  - Part V uses Part VI Def 2.4's bondage categories and terminology rule.

VERDICT: INTEGRATED
