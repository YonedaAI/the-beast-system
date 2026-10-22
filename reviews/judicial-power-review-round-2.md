---
reviewer: gemini-4-argon
paper: judicial-power
round: 2
date: 2026-10-22T14:51:55Z
---


# Peer Review: *Judicial Power and Legal Interpretation (Part III of The Six Pillars of the Beast System)*

## 1. General Evaluation

### Mathematical Correctness
The mathematical core of the paper—the necessity of adjudication under recurrent residual disputes and bounded dissolution hazards (\cref{thm:judicial-power:necessity}, lines 176–183), the ordering of additive and multiplicative contestability aggregates (\cref{lem:judicial-power:ordering}, lines 134–141), the exit-substitution counterexample (\cref{prop:judicial-power:exit}, lines 226–233), the disjunctive compliance condition (\cref{prop:judicial-power:disjunctive}, lines 266–273), the two-period judicial insurance model (\cref{prop:judicial-power:insurance}, lines 440–455), and the Tullock repeat-player litigation contest (\cref{prop:judicial-power:repeat}, lines 469–490)—is sound and its proofs are valid. Several formal statements, however, contain boundary omissions, inverted quantifier orderings, or notational inconsistencies that require correction:
- **Omitted positivity condition in \cref{prop:judicial-power:chain} (lines 498–509):** Line 500 introduces the capture probability $q_0$ without requiring $q_0 \in (0,1]$. If $q_0 = 0$, then $P_{\mathrm{persist}} = q_0(1-\Qchain) = 0$ for all $\mathbf{q}_t \in [0,1]^4$, which falsifies both the claim that different contestability vectors yield different persistence probabilities (line 505) and the proof's conclusion of a "strictly smaller persistence probability" (line 509).
- **Inverted quantifier order and weight mismatch in \cref{prop:judicial-power:dualstate} (lines 517–524):** Line 519 fixes $\varphi \in (0,1)$ before quantifying over $\varepsilon \in (0,1)$ ("Let a share $\varphi\in(0,1)$... For any $\varepsilon\in(0,1)$ there are two-tier layers..."), which reads as $\forall \varphi \in (0,1), \forall \varepsilon \in (0,1)$, whereas the proof on line 523 selects $\varphi \le \varepsilon$ after $\varepsilon$ is given. In the same two sentences on line 519, $\varphi$ is defined as a share of "stake-weighted cases," but $\bar{Q} = (1-\varphi)Q_O + \varphi Q_\Pi$ is immediately called "caseload-weighted contestability."
- **Underspecified reading set and code-rule mismatch in \cref{prop:judicial-power:relocation}(ii) (lines 239–255):** Item (ii) (line 248) claims that disputes can arise at any $x \in (O(r) \cup O_c(r)) \setminus X_0$, and the proof (lines 254–255) invokes \cref{def:judicial-power:dispute} separately for $\Read(r)$ and $\Read_c(r) = \{c \circ \zeta : \zeta \in \mathcal{E}(r)\}$. However, the statement does not define the combined admissible reading set on $X \setminus X_0$ as $\Read(r) \cup \Read_c(r)$, and consequently misses the case where $x \notin O(r) \cup O_c(r)$ (so all $\rho \in \Read(r)$ agree on $v_1$ and all $\zeta \in \mathcal{E}(r)$ agree on $c(\zeta(x)) = v_2$), yet the code diverges from the underlying rule ($v_1 \neq v_2$).
- **Implicit dispute ordering in \cref{thm:judicial-power:necessity} (lines 176–183):** Line 182 defines $D_k$ and $N_k$ among "the first $k$ residual disputes" and asserts $D_k + N_k = k$. Because \cref{def:judicial-power:determination} (line 113) requires only that each residual dispute reach a disposition at *some* finite time (not necessarily in arrival order), the proof should specify whether disputes are indexed by arrival time or disposition time.

### Clarity and Completeness
The paper is clear when developing its own definitions and historical cases, particularly the distinction between functional necessity and institutional form in \cref{sec:necessity} and the treatment of Weber's "kadi justice" against Ottoman court registers in \cref{sec:comparative} (line 357). Its completeness as a standalone research paper is compromised by heavy reliance on six unprinted companion working papers (\citealp{long2026financial,long2026political,long2026ideological,long2026coercive,long2026productive,long2026formalized}) and an unpublished foundational paper (\citealp{largo2026hbs}). Key formal concepts used in the paper's arguments—including the "appointment channel" map (lines 143, 331, 457), "conversion elasticity from resources to rulings" (line 492), "normative legitimacy" (line 275), "a sanction regime whose margin is pure allegiance" (line 599), and "Part V, Proposition 6.1" on sanction separability (line 545)—are invoked without self-contained definitions.

### Logical Structure
The macro-structure suffers from two architectural problems:
1. **Inversion of comparative application (\cref{sec:comparative}) and formal mechanisms (\cref{sec:mechanisms}):** The comparative analysis in \cref{sec:comparative} (lines 304–428) repeatedly relies on formal propositions that are not stated or proved until \cref{sec:mechanisms} (lines 429–548)—specifically \cref{prop:judicial-power:repeat} on repeat players (cited at line 319), \cref{prop:judicial-power:chain} on review chains (cited at lines 132 and 323), and \cref{prop:judicial-power:insurance} on judicial insurance (cited at line 335). Likewise, \cref{sec:layer} defines $\Qchain$ (line 128) and two-tier judicial layers (line 147), but defers the propositions that justify those definitions (\cref{prop:judicial-power:chain,prop:judicial-power:dualstate,cor:judicial-power:nonimplication}) to lines 498–535. Moving the formal mechanisms of \cref{sec:mechanisms} before the comparative analysis in \cref{sec:comparative} would eliminate these forward references and allow the regime comparisons to test and illustrate established propositions.
2. **Duplication between \cref{sec:objections} (lines 607–623) and earlier sections:** The first objection in \cref{sec:objections} (line 610) repeats almost verbatim the reply to the triviality objection in Section 3.5 (line 285). The fourth objection (line 616) repeats the ideal-type qualification in Section 5.1 (line 311). The fifth objection (line 618) repeats the typological disclaimers in Section 8 (line 597).

### LaTeX Quality
The LaTeX source compiles cleanly in structure and makes appropriate use of `amsmath`, `amsthm`, `booktabs`, `tabularx`, `natbib`, and `cleveref`, but contains several technical defects:
- **Unused packages in preamble (lines 12–19):** `graphicx` (line 12), `xcolor` (line 13), `tikz` (line 14), `longtable` (line 15), and `listings` along with `\lstset` (lines 18–19) are loaded but never used.
- **Redundant `geometry` options (line 6):** `\usepackage[margin=1in,left=1.25in,right=1.25in]{geometry}` sets `margin=1in` and immediately overrides the horizontal margins.
- **Time-subscript mismatch in macro expansion (lines 44–45, 502, 508):** The macros `\Qadd` and `\Qchain` hardcode the time subscript $t$ (`Q^{+}_{\pJ,t}` and `Q^{\times}_{\pJ,t}` on lines 44–45), but \cref{prop:judicial-power:chain} and its proof (lines 500–509) drop $t$ from the component probabilities, producing $\Qchain = q^{\mathrm{dis}} q^{\mathrm{acc}} q^{\mathrm{ind}} q^{\mathrm{cmp}}$ on line 502 with $t$ present on the left-hand side and absent on the right-hand side.
- **Hyphens instead of en-dashes in bibliography ranges (lines 652–925) and scripture citations (line 599):** All page ranges and year ranges in `thebibliography` use single hyphens (`114-121`, `1500-1750`, `1469-1716`, etc.) instead of `--`, and line 599 writes `(Rev 13:16 to 17)` instead of `(Rev 13:16--17)`.
- **Bibliography key/year mismatches and alphabetization errors (lines 639–891):** Five `\bibitem` entries have keys whose years do not match the publication year (`bell2004` for 1994 at line 639; `hirschl2000` for 2001 at line 750; `kaufmann2010` for 2011 at line 774; `mcginn1998` for 1994 at line 834; `swann2003` for 1995 at line 891). Moreover, `\bibitem[{\emph{Stallarholmens v.\ Sweden}}(1990)]{stallarholmens1990}` (line 690) and `\bibitem[{\emph{Langborger v.\ Sweden}}(1989)]{langborger1989}` (line 693) use case names in their `natbib` optional labels (so in-text citations print *Langborger v. Sweden* (1989)), but begin the bibliography text with `European Commission of Human Rights` and `European Court of Human Rights` and are alphabetized under `E` (with `Stallarholmens` before `Langborger`), whereas US cases (`Caperton`, `Citizens United`, `Marbury`) are alphabetized under their case names.

### Prose Quality Against the House Style
Much of the prose is crisp, direct, and free of ornate academic clutter. Nevertheless, the paper violates the house style in four recurring ways:
1. **Multi-claim catalogue paragraphs:** Several paragraphs bundle four to seven distinct claims or constitutional facts without a single unifying claim supported by reasoning (e.g., lines 70, 367, 573).
2. **Procedural signposting and meta-commentary:** Paragraphs and sentences announce where topics belong across the seven-part series rather than stating substantive claims (e.g., lines 66, 68, 70, 309, 579).
3. **Qualification or meta-framing before the finding:** In several places the prose states what a model omits or how it relates to the series before stating what it actually shows (e.g., line 492).
4. **Opaque series jargon where ordinary language is equally precise:** Terms imported from companion papers—such as "positive conversion elasticity from resources to rulings" and "reduce the conversion of concentration into dependency" (line 492)—obscure simple analytical claims.

---

## 2. Weakest Three Paragraphs and Model Rewrite

### Weakest Paragraph 1 (Line 70)
> Adjudication is necessary for any collective that persists with general rules, recurrent disputes, and costly self-help and exit. When exit is free the necessity argument fails, and the ethnography of mobile foragers shows the thin adjudication that this predicts. The judicial function depends on legitimation or on coercion, but on neither specifically. Captured rulings persist with a probability governed by the product of four review links (disclosure, access, independence and compliance), so additive judicial-independence indices can rate a judiciary well while one broken link leaves capture unchecked. A comparison of six regime types at equal depth finds the function in all of them and finds both capture episodes and checks within each. Eight hypotheses state the evidence that would refute these claims, and a typological reading of judgment in the Book of Revelation places the series' theological frame on the same footing.

**Critique:** This paragraph violates the house rule of one identifiable claim per paragraph supported by evidence, reasoning, or citation, as well as the prohibition on signposting. It compresses six distinct claims (the necessity theorem, the exit-substitution proposition, the disjunctive dependency proposition, the multiplicative review-chain proposition, the six-regime comparison, and the hypotheses and Revelation section) into six consecutive sentences without supporting reasoning, repeating the abstract (line 59) nearly sentence for sentence.

### Weakest Paragraph 2 (Line 309)
> Each regime type is described with the same five questions: which institutions hold the judicial function; how concentrated control over final determinations is ($H_{\pJ,t}$) and how contestable it is ($\mathbf{q}_t$); how strongly the judicial function is coupled to the other five pillars ($C_{\pJ n,t}$); what preserves accountability; and which capture episodes and checks are documented. Concentration and contestability are described qualitatively. The series does not report numerical values of $H$, $Q$, $U_t$ or $\Integ_t$ for any real polity without a documented and preregistered coding \citep{largo2026hbs}, and none has yet been carried out. This Part gives primary treatment to the couplings of the judicial pillar with legitimation ($C_{\pJ\pI}$), coercion ($C_{\pJ\pC}$) and production ($C_{\pJ\pW}$). The coupling with rule-making ($C_{\pP\pJ}$) belongs to Part II and the coupling with resources ($C_{\pF\pJ}$) to Part I; both are noted where they matter.

**Critique:** This paragraph consists entirely of procedural signposting, passive constructions ("is described," "are described," "has yet been carried out," "are noted"), and nominalizations ("treatment," "coding") rather than a substantive claim about judicial institutions. Worse, its final two sentences contradict the actual analysis in \cref{sec:comparative} and \cref{tab:regimes} (lines 412–423), where $C_{\pF\pJ}$ and $C_{\pP\pJ}$ are in fact identified as the *strongest* couplings in four of the six regime types (market-capitalist societies, communist party-states, Islamic states, and secular democracies).

### Weakest Paragraph 3 (Line 492)
> The proposition isolates one of Galanter's mechanisms, playing for rules. His article identifies others, including expertise, economies of scale and informal relations with court personnel \citep{galanter1974}, and those would add to the advantage. The result gives a precise sense to the claim that repeat players come out ahead even when merits are equal. It also states the size of the legal-aid subsidy needed to neutralize the advantage, which grows with the repeat player's caseload and the precedential weight of rulings. In network terms, the repeat-player advantage is one mechanism behind a positive conversion elasticity from resources to rulings, an object Part I defines \citep{long2026financial}, and legal aid acts on the access component $q^{\mathrm{acc}}_t$. This is the judicial version of the source's hypothesis that worker voice and access reduce the conversion of concentration into dependency \citep{largo2026hbs}, and it is the core of the coupling $C_{\pJ\pW}$: access to courts is the channel through which producers can contest the rules that govern their work.

**Critique:** This paragraph violates four rules of the house style. First, it opens with a qualification about what \cref{prop:judicial-power:repeat} omits rather than stating the finding first. Second, it uses filler meta-phrases ("gives a precise sense to the claim," "states the size of"). Third, it packs multiple claims—about precedent, legal-aid subsidies, resource-to-ruling conversion, and producer access—into a single paragraph. Fourth, it substitutes undefined technical nominalizations from companion papers ("a positive conversion elasticity from resources to rulings, an object Part I defines," "reduce the conversion of concentration into dependency") for ordinary language that is more precise.

### Model Rewrite of Weakest Paragraph 3 (Line 492)
> Repeat litigants win more often than one-shot litigants with equally meritorious cases whenever rulings set precedent, because a repeat litigant bids for future cases as well as the case at hand (\cref{prop:judicial-power:repeat}). Legal aid eliminates this advantage only when the public subsidy to the one-shot litigant matches the share of the repeat litigant's stake that comes from future precedent, $\lambda = \theta(n-1)/[1+\theta(n-1)]$. Because this required subsidy rises with both the repeat litigant's caseload $n$ and the precedential weight $\theta$, modest legal-aid budgets leave repeat players ahead in common-law and appellate forums. \citet{galanter1974} notes that repeat litigants also enjoy expertise, economies of scale, and informal ties to court staff; those advantages compound the precedent effect modeled here and raise the subsidy needed for equal access ($q^{\mathrm{acc}}_t$).

---

## 3. Structured Feedback by Severity

### Critical Issues
None. The central theorem and formal propositions are mathematically sound and contain no fatal errors that invalidate the paper's core conclusions.

### Major Issues

1. **Missing positivity assumption $q_0 \in (0,1]$ in \cref{prop:judicial-power:chain} (lines 500–509):**
   - *Issue:* Line 500 states "Suppose an attempted capture produces a favorable determination with probability $q_0$" without specifying $q_0 > 0$. When $q_0 = 0$, $P_{\mathrm{persist}} = 0$ regardless of $\mathbf{q}_t$. Consequently, the claim on line 504 that raising link $k$ reduces $P_{\mathrm{persist}}$ most when $k$ is the smallest link fails (all reductions are zero), and the claim on lines 504–505 and 509 that the two constructed contestability vectors have "different persistence probabilities" and a "strictly smaller persistence probability" is false.
   - *Fix:* Specify $q_0 \in (0,1]$ on line 500.

2. **Inverted quantifiers and inconsistent weighting terminology in \cref{prop:judicial-power:dualstate} (lines 517–524):**
   - *Issue:* Line 519 writes: "Let a share $\varphi\in(0,1)$ of stake-weighted cases fall in the politically salient tier... The caseload-weighted contestability is $\bar Q=(1-\varphi)Q_O+\varphi Q_\Pi$. For any $\varepsilon\in(0,1)$ there are two-tier layers with $\bar Q\ge 1-\varepsilon$ and $Q_\Pi=0$." Placing "Let a share $\varphi \in (0,1)$" outside "For any $\varepsilon \in (0,1)$" fixes $\varphi$ before $\varepsilon$, contradicting the proof on line 523 ("Take $\varphi \le \varepsilon$"). In addition, line 519 shifts from "stake-weighted cases" in the first sentence to "caseload-weighted contestability" in the second.
   - *Fix:* Define $\bar{Q}(\varphi, Q_O, Q_\Pi) = (1-\varphi)Q_O + \varphi Q_\Pi$ for a two-tier layer with political-tier share $\varphi \in (0,1)$, use either "caseload-weighted" or "stake-weighted" consistently (or note that the bound holds under either weighting whenever $\varphi \le \varepsilon$), and state: "For any $\varepsilon \in (0,1)$, there exist two-tier layers with $\varphi \in (0, \varepsilon]$ such that $\bar{Q} \ge 1-\varepsilon$ and $Q_\Pi = 0$."

3. **Incomplete specification of admissible readings and code-rule divergence in \cref{prop:judicial-power:relocation}(ii) (lines 241–255):**
   - *Issue:* On $X \setminus X_0$, parties have not agreed that the program output $c(\zeta_0(x))$ settles the case. The proof of (ii) on lines 254–255 treats $O(r) \setminus X_0$ as a dispute under $(r, \Read(r))$ and $O_c(r) \setminus X_0$ as a dispute under $(r_c, \{c \circ \zeta : \zeta \in \mathcal{E}(r)\})$. It does not specify that the effective set of admissible readings on $X \setminus X_0$ is $\Read(r) \cup \{c \circ \zeta : \zeta \in \mathcal{E}(r)\}$. Under that union, a dispute can also arise at a case $x \notin O(r) \cup O_c(r)$ whenever the unanimous reading of the verbal rule $\rho(x)$ differs from the unanimous output of the code $c(\zeta(x))$ (i.e., a specification bug or unexpected edge case where code and rule diverge even without internal ambiguity in either).
   - *Fix:* Explicitly define the admissible readings on $X \setminus X_0$ as $\Read^*(r) = \Read(r) \cup \{c \circ \zeta : \zeta \in \mathcal{E}(r)\}$, whose open set contains $O(r) \cup O_c(r)$ as well as any case $x$ where $\rho(x) \neq c(\zeta(x))$.

4. **Structural inversion of \cref{sec:comparative} (lines 304–428) and \cref{sec:mechanisms} (lines 429–548):**
   - *Issue:* The comparative section (\cref{sec:comparative}) uses the formal propositions of \cref{sec:mechanisms} to explain regime patterns before those propositions have been stated or proved: line 319 cites \cref{prop:judicial-power:repeat}, line 323 (and line 132) cites \cref{prop:judicial-power:chain}, and line 335 cites the insurance model of \cref{sec:mechanisms} (\cref{prop:judicial-power:insurance}). Meanwhile, \cref{sec:layer} introduces $\Qchain$ (line 128) and two-tier layers (line 147), but leaves their motivating propositions (\cref{prop:judicial-power:chain,prop:judicial-power:dualstate,cor:judicial-power:nonimplication}) forty paragraphs later in \cref{sec:mechanisms}.
   - *Fix:* Place \cref{sec:mechanisms} (together with the literature synthesis in \cref{sec:literature}) before \cref{sec:comparative}, or move \cref{prop:judicial-power:chain,prop:judicial-power:dualstate,cor:judicial-power:nonimplication} into \cref{sec:layer} immediately after \cref{lem:judicial-power:ordering} and \cref{def:judicial-power:boundness}.

5. **Unexplained concepts and propositions imported from unpublished companion papers (lines 66, 143, 275, 277, 331, 457, 492, 545, 599):**
   - *Issue:* The manuscript relies on seven unpublished working papers (\citealp{largo2026hbs,long2026financial,long2026political,long2026ideological,long2026coercive,long2026productive,long2026formalized}) for analytical terms that are never defined in this text, including the "appointment channel" map (lines 143, 331, 457), "conversion elasticity from resources to rulings" (line 492), "Part V, Proposition 6.1" (line 545), and "a sanction regime whose margin is pure allegiance" (line 599).
   - *Fix:* Define every mathematical or conceptual object used in this paper's arguments within this paper in self-contained terms, or replace cross-paper jargon with ordinary language where the formal object from another part is not needed for a proof here.

6. **Substantial redundancy between \cref{sec:objections} (lines 607–623) and earlier sections (lines 285, 311, 597):**
   - *Issue:* Paragraph 1 of \cref{sec:objections} (line 610) repeats Paragraph 2 of Section 3.5 (line 285) on whether the necessity theorem is trivial by definition. Paragraph 4 of \cref{sec:objections} (line 616) repeats Paragraph 2 of Section 5.1 (line 311) on why the six regime types overlap. Paragraph 5 of \cref{sec:objections} (line 618) repeats Paragraph 1 of \cref{sec:revelation} (line 597) on why the Revelation typology does not identify modern institutions with the beast.
   - *Fix:* Consolidate each objection and reply in one place—either integrate the remaining two unique objections in \cref{sec:objections} (legal realism at line 612 and historical commensurability at line 614) into Sections 2.1 and 5.1, or cut the earlier preemptive defenses and keep a streamlined \cref{sec:objections}.

7. **House-style violations in multi-claim, signposting, and jargon-heavy paragraphs (lines 70, 218, 309, 367, 492, 573):**
   - *Issue:* Lines 70 and 309 are roadmap/housekeeping paragraphs; lines 218, 367, and 573 are multi-claim literature or constitutional catalogues lacking a single argument-driven claim; line 492 buries its main finding behind a qualification and undefined cross-paper jargon.
   - *Fix:* Cut or merge the roadmap paragraph at line 70; replace the housekeeping paragraph at line 309 with a direct claim about why qualitative coding and pathway comparisons are used; reorganize lines 218, 367, and 573 around a single clear claim per paragraph; and rewrite line 492 as shown in the model rewrite above.

---

### Minor Issues

1. **Ordering of residual disputes in the proof of \cref{thm:judicial-power:necessity} (line 182):**
   - Specify that residual disputes in $D_k + N_k = k$ are indexed in order of disposition time (with simultaneous dispositions ordered arbitrarily), since \cref{def:judicial-power:determination} (line 113) requires only that each residual dispute reach a disposition in finite time rather than in arrival order.

2. **Time-subscript inconsistency in \cref{prop:judicial-power:chain} (lines 44–45, 502, 504, 508):**
   - Because `\Qadd` and `\Qchain` expand to $Q^{+}_{\pJ,t}$ and $Q^{\times}_{\pJ,t}$ (lines 44–45), dropping the subscript $t$ on $q^{\mathrm{dis}}, q^{\mathrm{acc}}, q^{\mathrm{ind}}, q^{\mathrm{cmp}}$ and $q^k$ in lines 502–508 creates a mismatch in $\Qchain = q^{\mathrm{dis}} q^{\mathrm{acc}} q^{\mathrm{ind}} q^{\mathrm{cmp}}$. Restore the subscript $t$ on the components in \cref{prop:judicial-power:chain} and its proof.

3. **Inconsistent superscript/subscript placement for pillar and component indices (lines 44–45, 79–81, 118, 126–128):**
   - Pillar $m \in \Mset$ appears as a superscript in $A^m_t, a^m_{ij,t}, s^m_{i,t}, s^{\pJ}_{i,t}$ (lines 79, 83, 118) but as a subscript in $H_{m,t}, Q_{m,t}, \omega_m, C_{mn,t}, Q^{+}_{\pJ,t}, Q^{\times}_{\pJ,t}$ (lines 44–45, 79–81, 136). Standardizing pillar indices in one position (or noting the convention) will improve notational consistency.

4. **Bibliography alphabetization and format for European human rights cases (lines 690–694):**
   - `\bibitem[{\emph{Stallarholmens v.\ Sweden}}(1990)]{stallarholmens1990}` (line 690) and `\bibitem[{\emph{Langborger v.\ Sweden}}(1989)]{langborger1989}` (line 693) are cited in text by case name (*Langborger v. Sweden* (1989) at line 349), but are alphabetized in the bibliography under `E` (`European Commission...` and `European Court...`), making them difficult to locate. Format and alphabetize them by case name, matching `Caperton` (line 663), `Citizens United` (line 666), and `Marbury` (line 825).

5. **Citation key and publication year mismatches in `thebibliography` (lines 639, 750, 774, 834, 891):**
   - Align the citation keys with the actual publication years for `bell2004` (1994, line 639), `hirschl2000` (2001, line 750), `kaufmann2010` (2011, line 774), `mcginn1998` (1994, line 834), and `swann2003` (1995, line 891).

6. **Hyphens instead of en-dashes in page/date ranges (lines 599, 652–925):**
   - Replace single hyphens with `--` in all numeric ranges in the bibliography (lines 652, 673, 679, 682, 700, 709, 718, 738, 751, 757, 763, 769, 775, 784, 787, 796, 864, 885, 892, 916, 922, 925) and change `(Rev 13:16 to 17)` on line 599 to `(Rev 13:16--17)`.

7. **Unused LaTeX packages and redundant geometry specification (lines 6, 12–19):**
   - Remove unused packages `graphicx`, `xcolor`, `tikz`, `longtable`, and `listings` (lines 12–19), and simplify `\usepackage[margin=1in,left=1.25in,right=1.25in]{geometry}` on line 6 to `\usepackage[top=1in,bottom=1in,left=1.25in,right=1.25in]{geometry}`.

8. **Two-sentence stub paragraphs at the end of \cref{sec:objections} (lines 620–622):**
   - Lines 620 and 622 are two-sentence paragraphs summarizing scope conditions on the theoretical models and empirical claims; merge them into a single paragraph stating the paper's scope limits directly.

VERDICT: MAJOR REVISIONS (major issues remain)
