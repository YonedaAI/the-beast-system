---
reviewer: gemini-4-argon
paper: judicial-power
round: 3
date: 2026-10-22T15:13:51Z
---


# Peer Review: *Judicial Power and Legal Interpretation* (Part III of *The Six Pillars of the Beast System*)

## 1. Dimensional Evaluation

### Mathematical Correctness
The formal results—Lemma 2.5, Propositions 2.8, 2.9, 3.4, 3.5, 3.6, 4.1, and 4.2, Theorem 3.3, and Corollary 3.7—are mathematically sound and their proofs are valid. The Borel–Cantelli-style geometric survival bound in Theorem 3.3 (lines 210–217) cleanly establishes that on the event of indefinite persistence $\Pi$, the number of non-determination dispositions $N$ is almost surely finite without requiring independence or stationarity across disputes. In Proposition 2.8 (lines 161–172), defining the components of $\mathbf{q}_t$ as sequential conditional probabilities (Definition 2.4, lines 124–130) makes the chain rule exact without an independence assumption. The contest equilibrium in Proposition 4.2 (lines 384–405) and the linear threshold in Proposition 4.1 (lines 355–370), including the boundary case $g \ge \delta L \iff \pi^* \ge 1$, are derived accurately. A few localized precision points in the formal statements (detailed under Minor Issues below) should be tightened.

### Clarity
The paper defines its concepts cleanly and maintains sharp analytical distinctions throughout: function versus office (lines 116, 219), act-level versus institution-level classification along Hart's secondary rules (line 85), coupling/fusion versus capture (lines 428, 480, 543, 553), and *de jure* versus *de facto* judicial independence (lines 500, 564). The two-tier aggregation result (Proposition 2.9, lines 180–187) and the multiplicative review chain (Proposition 2.8, lines 161–172) translate directly into clear empirical lessons for institutional measurement.

### Completeness
The manuscript covers the theoretical foundations, stateless and consensus baselines, formal counterexamples (costless exit and algorithmic execution), political-economy models of judicial independence and repeat-player advantage, comparative historical analysis across six regime types, observable indicators, eight falsifiable hypotheses, a typological reading of Revelation, and principal objections. The ethnographic and historical breadth—spanning the Nuer, Barotse, Arusha, Ju/'hoansi, Ottoman *qadi* courts, Safavid/modern Iranian councils, Castilian *chancillerías*, the Aragonese *Justicia*, French *parlements*, the Papal State, and Nordic corporatist labor courts—is well integrated and properly cited.

### Logical Structure
The progression from network primitives (Section 2) to the necessity theorem and its scope limits (Section 3), strategic and contest models (Section 4), comparative regime coding (Section 5), failure modes and checks (Section 6), measurement and hypotheses (Section 7), typological analysis (Section 8), and objections (Section 9) is coherent and cumulative. Every formal proposition in Sections 2–4 does analytical work in Sections 5–7. One internal cross-reference error (line 442) misdirects the reader to Section 6 instead of Section 4.2 for the insurance model.

### LaTeX Quality
The document compiles cleanly and uses `amsmath`, `amsthm`, `booktabs`, `tabularx`, `natbib`, and `cleveref` appropriately. However, the preamble loads several unused packages (lines 12–19), time subscripts and tier notation drift between defined macros and inline math, page and date ranges throughout the bibliography use single hyphens (`-`) instead of LaTeX en-dashes (`--`), and one bibliography entry has a triple-backtick ligature collision (line 943).

### Prose Quality and House Style
The prose largely adheres to the house style: sentences are direct, nominalizations and throat-clearing are rare, and qualifications generally follow stated findings. Where the prose falls short is at the paragraph boundary in a handful of places:
1. **Multi-claim "grab-bag" paragraphs** at the end of regime subsections (especially lines 432 and 444) bundle two or three distinct cross-pillar couplings ($C_{\pJ\pI}$, $C_{\pJ\pC}$, $C_{\pJ\pW}$) into a single paragraph with no unifying claim.
2. **Stitched transition paragraphs** (such as line 143) combine a mathematical observation about the preceding lemma with an unrelated definitional note about the next concept.
3. **Meta-commentary and signposting** in the coding conventions (line 416) announce which couplings are "developed most fully here" versus in other parts of the series—and state the opposite of what the comparative subsections actually emphasize.

---

## 2. Structured Feedback by Severity

### Critical Issues
None.

### Major Issues
None.

### Minor Issues

#### A. Formal Statements and Mathematical Precision
1. **Unstated non-control hypothesis and informal phrasing in Proposition 3.5 (lines 279–281, 288)**:
   - **Line 281 / Line 288**: Claim (i) states that on $X_0$, the program $c$ with designated encoding $\zeta_0$ is a determination procedure in the sense of Definition 2.3. Definition 2.3 (line 113) requires that *neither party controls the procedure alone*. The proof (line 288) asserts that "once both parties have agreed in advance to act on $c(\zeta_0(x))$ for $x \in X_0$, the program produces the verdict, neither party controls it, and both act on it." However, advance agreement to use $\zeta_0$ does not by itself guarantee that neither party unilaterally controls $\zeta_0$ (for example, if $\zeta_0$ is a self-reported delivery log or a price feed operated by one party). Add the explicit hypothesis to line 279 that neither party unilaterally controls $c$ or $\zeta_0$ on $X_0$.
   - **Line 279**: The statement "$O^*(r)$ also contains every case at which the rule and the program disagree" is informal because a rule $r$ has a set of readings $\Read(r)$ and the program has a set of encodings $\mathcal{E}(r)$. Match the precision of the proof (line 288) by writing: "$O^*(r)$ also contains every case at which some $\rho \in \Read(r)$ and some $c \circ \zeta$ ($\zeta \in \mathcal{E}(r)$) disagree."
2. **Feasibility domain of $\Delta$ when comparing links in Proposition 2.8 (line 167)**:
   - Line 167 states: "Raising link $k$ by $\Delta \in (0, 1 - q^k_t]$ reduces $P_{\mathrm{persist}}$ by $q_0 \Delta \prod_{j \neq k} q^j_t$; when every link is positive, this reduction is largest when $k$ is the link with the smallest value." Comparing the reduction for a common increment $\Delta$ across links $k$ requires that $\Delta$ be feasible for the links compared, i.e., $\Delta \in (0, 1 - \max_j q^j_t]$ (or else that the comparison be stated in terms of the marginal effect $-\partial P_{\mathrm{persist}} / \partial q^k_t = q_0 \prod_{j \neq k} q^j_t$).
3. **"Almost surely" qualification in the second sentence of Theorem 3.3 (line 212)**:
   - The first sentence of Theorem 3.3 carefully specifies "contained, up to a null set, in the event that adjudication is implemented," because $\Pi \cap \{N = \infty\}$ has probability zero rather than being empty. The second sentence ("If the collective persists with positive probability, the fraction of residual disputes disposed of by determination converges to one on the persistence event") should likewise read "converges to one *almost surely* on the persistence event."
4. **Process assumptions embedded inside Definition 2.3 (line 113)**:
   - Line 113 opens Definition 2.3 with an empirical/model assumption—"Every residual dispute reaches a disposition at some finite time, and the disposition takes one of four forms"—which the proof of Theorem 3.3 then invokes on line 216 ("each reaches exactly one of the four dispositions of `\cref{def:judicial-power:determination}`"). State finite termination and the exhaustive four-way partition either as part of the model setup preceding the definition or in Assumption 3.1, reserving Definition 2.3 for defining the four dispositions and implemented adjudication.
5. **Explicit domain of $\pi$ in Proposition 4.1 (line 357)**:
   - Line 357 specifies $\iota \in [0,1]$ and $\delta \in (0,1]$ in math mode, but leaves $\pi \in [0,1]$ implicit in the word "probability." Write "with probability $\pi \in [0,1]$" so the boundary claim at line 361 ("If $g \ge \delta L$, then $\pi^* \ge 1$ and independence is never strictly optimal") has its domain explicit.

#### B. Cross-References, Notation, and Terminology
6. **Broken section cross-reference for the insurance model (line 442)**:
   - Line 442 reads: `The insurance model in \cref{sec:mechanisms} predicts this: a ruling party that expects to stay in power gains little from independent courts.` The insurance model is in Section 4.2 (`\cref{sec:literature}` / `\cref{prop:judicial-power:insurance}`, lines 351–370), not Section 6 (`\cref{sec:mechanisms}`). Replace `\cref{sec:mechanisms}` with `\cref{prop:judicial-power:insurance}`.
7. **Inconsistent time subscripts and tier notation (lines 85, 182, 252, 327, 372, 409–506, 553–624)**:
   - Line 81 defines $C_{mn,t}$ with a time subscript $t$, and line 85 uses $C_{\pP\pJ,t}$, but every subsequent occurrence drops $t$ ($C_{\pJ\pC}$, $C_{\pP\pJ}$, $C_{\pJ\pI}$, $C_{\pJ\pW}$, $C_{\pF\pJ}$). Either note once in Section 2.1 that the subscript $t$ is suppressed when clear from context, or use $t$ consistently.
   - In the proof of Corollary 3.7 (line 327), the components $q^{\mathrm{dis}}, q^{\mathrm{acc}}, q^{\mathrm{ind}}, q^{\mathrm{cmp}}$ drop their $t$ subscript while $\Qchain$ (`Q^{\times}_{\pJ,t}`) retains it in the same sentence.
   - In Proposition 2.9 (line 182), $Q_\Pi$ and $Q_O$ drop the $\times$ superscript used for chain contestability (`\Qchain`).
8. **Spelling drift between `qadi` and `kadi` (lines 585, 632)**:
   - The paper uses `qadi` throughout (lines 59, 83, 462, 468, 527, 587, 626), properly reserving `"kadi justice"` for Weber's German-derived ideal type (lines 464, 626). However, lines 585 (`the registers of Ottoman kadi courts`) and 632 (`in the kadi court of Kayseri`) revert to `kadi` outside quotes. Standardize to `qadi` in both places.

#### C. LaTeX Quality and Bibliography Formatting
9. **Unused packages in the preamble (lines 12–19)**:
   - `\usepackage{graphicx}` (line 12), `\usepackage{xcolor}` (line 13), `\usepackage{tikz}` (line 14), `\usepackage{longtable}` (line 15), and `\usepackage{listings}` with `\lstset{...}` (lines 18–19) are never used in the document. Remove them unless required by a mandatory series preamble.
10. **Hyphens instead of en-dashes (`--`) in bibliography page and date ranges (lines 658–949)**:
    - Every page range and year range in `\begin{thebibliography}` uses a single hyphen `-` instead of a LaTeX en-dash `--`: lines 658 (`114-121`), 679 (`247-267`), 688 (`1469-1716`), 700 (`497-527`), 706 (`1500-1750`), 712 (`95-160`), 718 (`535-556`), 754 (`271-307`), 769 (`315-335`), 778 (`1917-1939`), 787 (`133-172`), 793 (`1500-1700`), 799 (`220-246`), 811 (`445-470`), 814 (`875-901`), 871 (`935-984`), 886 (`721-747`), 913 (`59-89`), 919 (`1754-1774`), 931 (`1560-1791`), 943 (`583-596`), 946 (`115-145`), and 949 (`431-451`). Replace `-` with `--` in all twenty-three entries.
11. **Quotation mark ligature collision in `\bibitem{whittington2005}` (line 943)**:
    - Line 943 writes ```` ```Interpose Your Friendly Hand' ````, which TeX typesets as `“‘` with no separation. Write `` ``\thinspace`Interpose Your Friendly Hand' ``.

#### D. Prose and Paragraph Coherence
12. **Redundant sentence in Section 2.5 (line 176)**:
    - The fifth sentence of line 176 ("The divergence between the additive and chain aggregates is also largest when one stage fails while the others work, not when failures cluster") repeats the opening sentence of line 143 and interrupts the paragraph's argument about how marginal indicators understate reversal probabilities when stage failures correlate. Cut or integrate it into the measurement claim.
13. **Word repetition and misleading topic sentence in Section 5.5 (line 470)**:
    - Line 470 opens: "Modern Saudi Arabia and Iran show two different modern arrangements." Aside from the repetition of "Modern ... modern," the paragraph discusses only Saudi Arabia (Iran is introduced four lines later at line 474), and its second sentence strings four statutory clauses together before stating the analytical point in line 472. Open line 470 with a direct claim about Saudi Arabia's coupling of uncodified juristic interpretation to royal appointment and enforcement, and merge it with line 472.

---

## 3. Weakest Three Paragraphs and Model Rewrite

### Weakest Paragraph 1 (Line 432)
> The legitimation coupling $C_{\pJ\pI}$ runs through law schools, the bar and the public reputation of courts, which Part IV treats as professional epistemic authority. The coercion coupling $C_{\pJ\pC}$ is moderate. Prosecutors exercise large discretion over which disputes reach courts, and the enforcement of judgments depends on executive agencies, as Hamilton observed. The production coupling $C_{\pJ\pW}$ runs through access to courts for workers and consumers, and through arbitration clauses in employment and consumer contracts that move disputes from public courts to private forums.

**Why it fails the house style:** This paragraph violates the rule of one identifiable claim per paragraph supported by evidence, reasoning, or citation. It is a three-item inventory that bundles three distinct couplings ($C_{\pJ\pI}$, $C_{\pJ\pC}$, and $C_{\pJ\pW}$) into a residual paragraph at the end of Section 5.2 without a governing claim or supporting empirical citations. (Line 444 in Section 5.3 has the same structural flaw.)

### Weakest Paragraph 2 (Line 416)
> Qualitative coding is the only defensible form of comparison at present, because no preregistered coding of $H$, $Q$, $U_t$ or $\Integ_t$ exists for any real polity, and the series does not report numbers without one \citep{largo2026hbs}. Each regime type is therefore compared on five questions: which institutions hold the judicial function; how concentrated control over final determinations is ($H_{\pJ,t}$) and how contestable it is ($\mathbf{q}_t$); how strongly the judicial function is coupled to the other five pillars; what preserves accountability; and which capture episodes and checks are documented. The couplings with legitimation, coercion and production ($C_{\pJ\pI}$, $C_{\pJ\pC}$, $C_{\pJ\pW}$) are developed most fully here. The couplings with rule-making and resources ($C_{\pP\pJ}$, $C_{\pF\pJ}$) are coded in Parts II and I, and they appear below wherever they are strong, which in four of the six types means they are the strongest.

**Why it fails the house style:** After a strong opening sentence, the second half of the paragraph lapses into cross-series signposting ("are developed most fully here," "are coded in Parts II and I, and they appear below wherever they are strong, which in four of the six types means they are the strongest") and nested subordination. Worse, the signposting is self-contradictory: $C_{\pP\pJ}$ and $C_{\pF\pJ}$ actually receive the fullest analysis in the comparative sections that follow, whereas $C_{\pJ\pI}$, $C_{\pJ\pC}$, and $C_{\pJ\pW}$ are often compressed into brief concluding remarks.

### Weakest Paragraph 3 (Line 143)
> The gap between the aggregates is widest when the components are dispersed, with one stage failing and the others working. The independence component depends heavily on the appointment channel, which Part II defines as the map from a coalition to the offices it fills in each pillar \citep{long2026political}.

**Why it fails the house style:** This two-sentence paragraph stitches together two unrelated claims: a mathematical observation about the bound in Lemma 2.5 and a cross-reference to Part II on judicial appointments. Neither sentence supports or qualifies the other.

---

### Model Rewrite (Rewriting Line 432)

To satisfy the house style, the single grab-bag paragraph at line 432 should either be unified around a single claim about how market-capitalist institutions privatize or filter the remaining couplings, or split so that the substantive claim about mandatory arbitration ($C_{\pJ\pW}$) stands as its own supported paragraph while the institutional separation of legal training and prosecution ($C_{\pJ\pI}, C_{\pJ\pC}$) is stated as a single coherent contrast:

> Outside the resource channel, market-capitalist systems separate adjudication from ideological training and policing while allowing private contracts to restrict court access in production ($C_{\pJ\pW}$). Law schools and bar associations operate independently of the state ($C_{\pJ\pI}$), and executive control over prosecution and enforcement keeps the coercion coupling ($C_{\pJ\pC}$) moderate \citep{hamilton1788}. In employment and consumer disputes, however, repeat-player firms use mandatory arbitration clauses to shift cases from public courts to private forums where rulings set no public precedent and repeat-litigant advantages grow \citep{galanter1974}.

VERDICT: MINOR REVISIONS (only minor issues)
