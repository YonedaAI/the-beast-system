---
reviewer: gemini-4-argon
paper: judicial-power
round: 1
date: 2026-10-22T14:37:24Z
---


# Peer Review: *Judicial Power and Legal Interpretation* (Part III of *The Six Pillars of the Beast System*)

## 1. General Evaluation

This paper argues that any governance system with general rules and costly exit must implement a third-party determination procedure to survive recurrent disputes (Proposition A), while the concentration and capture of that procedure vary contingently with institutional design and cross-pillar couplings (Proposition B). The paper's core analytical contributions—the persistence proof for adjudication (Theorem 3.3), the exit-substitution boundary condition (Proposition 3.4), the disjunctive dependency on legitimacy or coercion (Proposition 3.6), and the multiplicative review-chain model of judicial contestability (Proposition 5.4)—are well-conceived and substantively illuminating.

However, the manuscript requires major revisions before publication. The proof of the repeat-player contest (Proposition 5.3) contains a garbled first-order condition; the discussion of correlation among review links (Section 5.4) gets the direction of the probability bound backward; Proposition 3.5 overstates in its theorem statement what its proof actually establishes and formalizes a fixed encoding rather than the contested input classification described in the text; and the multiplex-network quantities introduced in Section 2 ($A^{\pJ}_t, s^{\pJ}_{i,t}, H_{\pJ,t}, C_{\pJ n,t}$) are disconnected from the formal propositions in Sections 3 and 5. Several paragraphs also violate the house style by bundling three to five distinct claims, relying on meta-discourse about other parts of the series, or listing citations without a governing claim.

---

## 2. Summary Evaluation by Criterion

- **Mathematical Correctness:** Generally sound in Theorem 3.3 and Propositions 3.4, 3.6, 5.2, and 5.5, but flawed in the proof of Proposition 5.3 (line 439), imprecise in the statement of Proposition 3.5 (line 223) and Proposition 5.4 (line 454), and mistaken in the informal probabilistic claim about correlated links following Proposition 5.4 (line 461).
- **Clarity:** Definitions and proofs are crisp, and the distinction between coupling and capture is maintained carefully across regimes. Ambiguities remain around how control shares $s^{\pJ}_{i,t}$ are assigned across appellate hierarchies and multimember bodies (line 116) and how non-resolution is timed as a hazard event (lines 111, 153, 164).
- **Completeness:** The paper relies heavily on unquoted formal objects from unpublished companion papers (Parts I, II, IV, V, and VII; e.g., lines 68, 83, 130, 248, 288, 493), none of which appears in the bibliography.
- **Logical Structure:** The progression from definitions (Section 2) to necessity (Section 3), literature (Section 4), comparative analysis (Section 5), formal mechanisms (Section 6), and measurement (Section 7) is logical, except that Section 5 (*Comparative analysis*) precedes Section 6 (*Mechanisms, failure modes and checks*) while repeatedly forward-referencing Definitions and Propositions from Section 6 (lines 130, 288, 290, 300, 302, 330). Moving Section 6 before Section 5—or moving Definition 6.1 into Section 2—would eliminate these forward dependencies. Section 8 (*Judgment in Revelation 13 to 19*) sits awkwardly between the empirical hypotheses (Section 7) and methodological objections (Section 9).
- **LaTeX Quality:** Clean macro usage and cross-referencing via `cleveref`, but marred by unused packages and environments (lines 12–19, 27), mismatched citation keys and dates (lines 585, 672, 690, 723, 756), redundant case citations (lines 284, 288, 290, 314), and hyphens (`-`) where en-dashes (`--`) are required across almost all page and date ranges in the bibliography (lines 598–781).
- **Prose Quality (House Style):** Sentence-level prose is mostly direct and free of jargon, with active verbs and minimal nested subordination. At the paragraph level, however, the manuscript frequently violates the "one identifiable claim per paragraph" rule by packing disparate historical episodes, multiple cross-pillar couplings, and series-level housekeeping into single paragraphs (e.g., lines 79, 248, 288, 322, 330, 340, 461, 568) and by using meta-signposting ("This Part...", "The following proposition...", "Table X summarizes...").

---

## 3. Structured Feedback by Severity

### Critical Issues

1. **Garbled first-order condition in the proof of Proposition 5.3 (Line 439):**
   In the proof of the repeat-player Tullock contest, line 439 states:
   > "In a lottery contest with valuations $A$ and $B$, the first-order conditions $B\,e_B/(e_A+e_B)^2=1/A\cdot A\,e_B/(e_A+e_B)^2$ reduce to $Ae_B=(e_A+e_B)^2$ and $Be_A=(e_A+e_B)^2$, so $e_A/e_B=A/B$..."

   The equation $B\,e_B/(e_A+e_B)^2=1/A\cdot A\,e_B/(e_A+e_B)^2$ is mathematically false: the right-hand side simplifies to $e_B/(e_A+e_B)^2$, which implies $B=1$, and the derivative of player $B$'s win probability $e_B/(e_A+e_B)$ with respect to $e_B$ has $e_A$, not $e_B$, in the numerator. The correct first-order conditions for maximizing $A\,e_A/(e_A+e_B) - e_A$ and $B\,e_B/(e_A+e_B) - e_B$ are
   $$\frac{A\,e_B}{(e_A+e_B)^2} = 1 \quad \text{and} \quad \frac{B\,e_A}{(e_A+e_B)^2} = 1,$$
   which immediately yield $A e_B = (e_A+e_B)^2$ and $B e_A = (e_A+e_B)^2$.

2. **Incorrect probabilistic reasoning on correlated review links (Lines 124–127, 450–453, 461):**
   - First, Definition 2.4 (line 124) defines $q^{\mathrm{dis}}_t, q^{\mathrm{acc}}_t, q^{\mathrm{ind}}_t, q^{\mathrm{cmp}}_t$ as unconditional (or loosely conditioned) probabilities, whereas Proposition 5.4 (lines 450–453) defines them as sequential conditional probabilities along a chain. If each link $k$ is defined conditional on the success of all preceding links $1, \dots, k-1$, then $\Pr(\text{reversal}) = q^{\mathrm{dis}} q^{\mathrm{acc}} q^{\mathrm{ind}} q^{\mathrm{cmp}}$ is an exact identity by the chain rule of probability, not a "conditional-independence structure" as claimed on line 461.
   - Second, if $q^k$ are instead treated as marginal probabilities of binary events $E_k$ within a case (or random variables across cases/polities), positive correlation among the links means $\Pr(\bigcap_{k=1}^4 E_k) > \prod_{k=1}^4 \Pr(E_k)$. Thus, for fixed marginal probabilities $q^k$, positive correlation *increases* the probability of reversal and *reduces* $P_{\mathrm{persist}}$ relative to the independence benchmark $\Qchain$. Moreover, across regimes, when failures cluster ("a government that ignores courts also tends to pack them," line 461), a regime with one near-zero link also tends to have low values on the remaining links, which causes the additive index $\Qadd$ and the multiplicative index $\Qchain$ to move together. The divergence between $\Qadd$ and $\Qchain$ is largest when one link fails while the other three remain high (high dispersion across links, as in the proof on line 458), not when failures cluster.

3. **Mismatch between statement, proof, and interpretation in Proposition 3.5 (Lines 59, 89, 221–230):**
   - *Overclaim in proposition statement:* Line 223 states unconditionally that if $w \notin W_0$ lies in $O(r)$, "disputes at $w$ are residual disputes about the rule and require a determination procedure outside the program." As the proof (line 227) acknowledges, a dispute at $w$ is residual only *if unassisted bargaining fails*, and even then Theorem 3.3 implies only that all but finitely many residual disputes are resolved by determination on the persistence event, not that every dispute at $w$ requires a determination procedure.
   - *Mismatch between formal setup and mechanism:* The abstract (line 59) and post-proof discussion (line 230) argue that when rules are executed by code, "interpretation relocates to the classification of inputs"—that is, parties disagree over how the world state $w$ is mapped to the program input $z = \zeta(w)$ (e.g., whether an oracle or sensor properly classified delivery). Yet Proposition 3.5 treats the encoding $\zeta: W \to Z$ as a single fixed map and locates open texture in $w \in O(r) \setminus W_0$. To formalize the relocation of open texture to input classification, $\Read(r)$ in a code-executed system should induce a set of admissible encodings $\zeta, \zeta': X \to Z$ such that $c(\zeta(x)) \neq c(\zeta'(x))$. Also, $W$ is introduced on line 223 as "world states" without equating it to the case set $X$ of Definition 2.1, even though line 223 writes $w \in O(r) \subseteq X$.

---

### Major Issues

4. **Disconnect between the formal network quantities in Section 2 and the formal models in Sections 3 and 5 (Lines 79, 81, 116, 278, 386–495):**
   Section 2.1 and Section 2.3 introduce a directed multiplex network $G_t = (V_t, E_t)$, adjacency matrix $A^{\pJ}_t$ with edge weights $a^{\pJ}_{ij,t}$, node control shares $s^{\pJ}_{i,t}$, Herfindahl index $H_{\pJ,t} = \sum_i (s^{\pJ}_{i,t})^2$, unaccountable concentration $U_t$, and cross-pillar integration $C_{mn,t}$. None of these variables appears in any theorem, proposition, or proof in Section 3 or Section 5. Conversely, the formal parameters of Section 5 ($\iota$ in Proposition 5.2; $m, \theta, n, \lambda$ in Proposition 5.3; $\varphi$ in Proposition 5.5) are not mapped back to $s^{\pJ}_{i,t}$, $H_{\pJ,t}$, or $C_{\pJ n,t}$. Explicitly linking $\iota$ to $1 - C_{\pP\pJ,t}$ (or $q^{\mathrm{ind}}_t$), and linking repeat-player advantage in Proposition 5.3 to $C_{\pF\pJ,t}$ and $q^{\mathrm{acc}}_t$, would integrate the paper's formal architecture.

5. **Under-specification of control shares $s^{\pJ}_{i,t}$ in hierarchical and multimember courts (Line 116):**
   Line 116 defines actor $i$'s control share $s^{\pJ}_{i,t}$ "in proportion to the stake-weighted share of final determinations in which $i$ has the last word, whether by deciding, by directing the decider, or by reversing the decision." Because $\sum_i s^{\pJ}_{i,t} = 1$ (line 79), this rule is ambiguous in two standard settings:
   - When an apex court has discretionary appellate jurisdiction over lower courts (as in the United States, line 286) and leaves 99% of lower-court judgments unreviewed, does the lower court or the apex court hold "the last word" on unappealed or cert-denied cases? If the apex court holds the last word by virtue of potential reversal, $H_{\pJ,t}$ is near 1 across all cases, contradicting line 286 ("Across ordinary litigation, control over final determinations is spread across thousands of judges, so $H_{\pJ,t}$ is low"). If only actual decisions count, then a party committee that rarely intervenes because judges anticipate its preferences would appear to have a low $s^{\pJ}_{i,t}$.
   - How are control shares divided among members of a multimember tribunal or between two bodies whose concurrence is required?

6. **Timing of "non-resolution" in Definition 2.3, Assumption 3.2, and Theorem 3.3 (Lines 111, 153, 164):**
   Definition 2.3 (line 111) defines "non-resolution" as "the dispute stays open." Assumption 3.2 (line 153) conditions on "the history up to the resolution of any residual dispute" and assigns a dissolution probability of at least $\kappa$ to "a resolution by self-help, by exit, or by non-resolution." Calling "non-resolution" a "resolution" is a contradiction in terms, and if a dispute simply stays open over continuous time, there is no well-defined stopping time at which the collective "survives each of the first $n$" non-resolutions (line 164). Define each residual dispute as reaching a finite disposition stage $t_k$ at which it is either determined, fought over (self-help), exited from, or abandoned unresolved, with each of the last three dispositions triggering an immediate dissolution hazard of at least $\kappa$.

7. **Division by zero and boundary constraints in Proposition 5.4 (Lines 454, 458):**
   Line 454 states that for a fixed improvement $\Delta$ in link $k$, "the reduction in $P_{\mathrm{persist}}$ is $q_0\Delta\,\Qchain/q^{k}$, which is largest when the improved link $k$ is the weakest." When $q^k = 0$, $\Qchain / q^k$ is $0/0$ (undefined). In the proof (line 458), the author restricts this expression to $q^k > 0$. State the reduction in the proposition as $q_0 \Delta \prod_{j \neq k} q^j$ (with $0 < \Delta \le 1 - q^k$), and add the condition $q^j > 0$ for all $j$ so that the weakest link is uniquely well-defined and the marginal reduction is strictly positive.

8. **Unresolved external references to unpublished companion parts (Lines 68, 83, 130, 248, 288, 493):**
   The text imports specific numbered definitions and propositions from other parts of the series—Part I, Definition 6.1 (line 288); Part II, Definitions 2.3, 2.8, and 3.6 (lines 83, 130); Part IV, Definition 2.2 (lines 83, 248); Part V, Proposition 6.1 (line 493); and Part VII's axioms and theorems (lines 68, 98, 248)—without stating those definitions or listing Parts I, II, IV, V, or VII in the bibliography. Every formal object required to evaluate this paper's claims (especially the appointment channel determining $q^{\mathrm{ind}}_t$ on line 130) should be stated self-containedly in Section 2, and companion papers should be cited in the bibliography.

9. **Extensive violations of the house style's paragraph and signposting rules (Throughout; see Section 4 below):**
   - *Multi-claim paragraphs:* Lines 79, 248, 288, 308, 326, 328, 330, 340, 461, and 568 each bundle multiple distinct claims, couplings, or mechanisms into a single paragraph.
   - *Literature-catalog paragraphs without a governing claim:* Lines 269, 322, and 551 list five to six authors in succession ("X's study shows... Y's study shows... Z's study shows...") without stating an analytical claim that the citations jointly establish.
   - *Meta-signposting:* Remove self-referential scaffolding such as "Two propositions organize the series, and this Part keeps them apart" (line 68), "The paper makes five contributions" (line 70), "These objects are cited here, not redefined" (line 79), "The weight of a node in the judicial layer can now be stated" (line 116), "\Cref{tab:minimal} summarizes the cases" (line 175), "The following proposition shows that..." (lines 206, 237, 400), "The present paper enters at the junction of these literatures" (line 271), and "\Cref{tab:regimes} summarizes the comparison" (line 358). Integrate table references parenthetically into substantive claims.

---

### Minor Issues

10. **Strict vs. weak monotonicity in Proposition 5.3 (Line 435):**
    Line 435 states that "$p_R$ increases in $n$ and $\theta$." When $\theta = 0$, $p_R = m/(m+1)$ is constant in $n$; when $n = 1$, $p_R = m/(m+1)$ is constant in $\theta$. Specify that $p_R$ is strictly increasing in $n$ for $\theta > 0$ and in $\theta$ for $n > 1$ (or weakly increasing on the full domain).

11. **Knife-edge case $\pi = \pi^*$ in Proposition 5.2 (Lines 404–408):**
    Proposition 5.2 specifies $\iota^* = 1$ for $\pi > \pi^*$ and $\iota^* = 0$ for $\pi < \pi^*$, omitting that any $\iota \in [0,1]$ is optimal when $\pi = \pi^*$.

12. **Omitted lame-duck condition in Remark 5.1 (Lines 421–423):**
    Remark 5.1 states that ruling against the incumbent risks $(1-\pi)s$ and ruling for it risks $\pi s$, so the judge defects when $\pi > 1/2$. This calculation assumes that the incumbent cannot sanction the judge in the current period before leaving office and that the case pits the incumbent directly against the next office holder. State both assumptions explicitly.

13. **Inconsistency between "necessity lemma" and `theorem` environment (Lines 27, 70, 142, 158):**
    Line 27 defines `\newtheorem{lemma}[theorem]{Lemma}`, and lines 70 and 142 refer to the result of Section 3.1 as "a necessity lemma" / `\subsection{The necessity lemma}`, but line 158 declares it as `\begin{theorem}[Necessity of adjudication]`. Use either "theorem" or "lemma" consistently.

14. **Section 7 title vs. biblical text range (Lines 70, 542, 549):**
    Lines 70 and 542 title the section "Judgment in Revelation 13 to 19," but line 549 relies on Revelation 6:10 and Revelation 20:4 for its central claim that judgment is relocated to those who refused the mark. Update the range to Revelation 6--20 (or "Judgment in the Book of Revelation") and use an en-dash (`13--19`, `13:16--17` on line 547) rather than the word "to."

15. **Symbol overloading of $V$ and $\ell$ (Lines 79, 89, 241, 404, 414, 439):**
    $V$ denotes the vertex set $V_t$ (line 79), the set of verdicts $V$ (line 89), the incumbent's value function $V(\iota)$ (line 414), and the repeat player's valuation $V_R$ (line 439). Similarly, $\ell$ denotes legitimacy value in Proposition 3.6 (line 241) and loss from abuse in Proposition 5.2 (line 404). Use distinct symbols (e.g., $\mathcal{V}$ for verdicts and $L$ for loss in Proposition 5.2).

16. **Unused LaTeX packages and definitions in the preamble (Lines 12–19, 27):**
    `\usepackage{graphicx}` (line 12), `\usepackage{xcolor}` (line 13), `\usepackage{tikz}` (line 14), `\usepackage{longtable}` (line 15), `\usepackage{listings}` and `\lstset{...}` (lines 18–19), and `\newtheorem{lemma}` (line 27) are never used in the document and should be removed. On line 6, simplify `\usepackage[margin=1in,left=1.25in,right=1.25in]{geometry}` to `\usepackage[top=1in,bottom=1in,left=1.25in,right=1.25in]{geometry}`.

17. **Bibliography formatting, en-dashes, and citation keys (Lines 284, 288, 290, 314, 585–781):**
    - Replace single hyphens `-` with en-dashes `--` in all page ranges and date ranges in the bibliography (lines 598, 612, 621, 636, 642, 648, 654, 668, 673, 681, 687, 692, 698, 709, 712, 728, 739, 754, 757, 765, 775, 778, 781).
    - Align mismatched citation keys with their actual publication years: `\bibitem[Bell(1994)]{bell2004}` (line 585), `\bibitem[Hirschl(2001)]{hirschl2000}` (line 672), `\bibitem[Kaufmann et~al.(2011)]{kaufmann2010}` (line 690), `\bibitem[McGinn(1994)]{mcginn1998}` (line 723), and `\bibitem[Swann(1995)]{swann2003}` (line 756).
    - Avoid duplicating case names in prose and parenthetical citations on lines 284 (`since \emph{Marbury v.\ Madison} in 1803 ... \citep{marbury1803}`), 288 (`In \emph{Citizens United v.\ Federal Election Commission} ... \citep{citizensunited2010}`), 290 (`\emph{Caperton v.\ A.\,T.\ Massey Coal Co.} \citep{caperton2009}`), and 314 (`in \emph{Langborger v.\ Sweden} ... \citep{langborger1989}`).

---

## 4. Three Weakest Paragraphs and Model Rewrite

### Weakest Paragraph 1 (Line 340)

> In Bourbon France the parlements, of which the Parlement of Paris was the most important, registered royal legislation and could remonstrate against it before registration. Julian Swann's study of the Parlement of Paris under Louis XV traces the use of remonstrances, the crown's use of the formal session called the lit de justice to compel registration, and Chancellor Maupeou's suppression and reconstruction of the parlements in 1771, which was reversed in 1774 \citep{swann2003}. Part II codes registration and remonstrance as a veto in rule-making; this Part is concerned with the parlements as appellate courts. In that capacity they also adjudicated conflicts with the Church. Dale Van Kley's account of the religious origins of the French Revolution shows the parlements intervening in the 1750s against clergy who refused sacraments to Jansenists \citep{vankley1996}, a case in which the judicial pillar contested the authority of the legitimation pillar. William Doyle's study of venality explains why the parlements could resist: judicial offices were purchased and heritable property, so the crown could not remove judges without compensating them \citep{doyle1996}. Venality secured independence from the crown and entrenched a corporate interest in the offices themselves, which ties adjudication to resources, the coupling Part I codes as $C_{\pF\pJ}$. Bell's study of the Paris barristers shows the legal profession acquiring a political voice in the same period \citep{bell2004}.

- **Critique:** This paragraph violates the one-claim-per-paragraph rule by combining four distinct topics: legislative registration and remonstrance ($C_{\pP\pJ}$), appellate intervention against clergy over Jansenist sacraments ($C_{\pJ\pI}$), venality of office as the fiscal basis of independence ($C_{\pF\pJ}$), and the political rise of the Paris bar. It also buries its core explanatory mechanism—that property rights in judicial office enabled the *parlements* to resist both crown and Church—in the sixth sentence, and interrupts the argument with cross-part housekeeping ("Part II codes... this Part is concerned with...", "the coupling Part I codes as $C_{\pF\pJ}$").

### Weakest Paragraph 2 (Line 330)

> The Iranian design produces high concentration at the apex and high couplings with rule-making and legitimation: the Leader's appointments reach both the interpretive council and the judiciary, and the Council's religious jurists determine whether legislation is valid. Asghar Schirazi's analysis documents repeated conflict between parliament and the Guardian Council in the 1980s and the creation of a further council to resolve deadlocks between them \citep{schirazi1997}. Wilfried Buchta's study of the power structure describes the Council's use of its electoral supervision to screen candidates \citep{buchta2000}. Part II codes the Council's vetting of bills and its screening of candidates as acts in the rule-making layer, a veto over legislation and over entry. The judgments on which the vetting rests, whether a bill conforms to Islamic criteria and to the Constitution, are interpretive determinations in this Part's sense. One body performing both kinds of act is fusion, and it raises the coupling $C_{\pP\pJ}$ that Part II measures. Whether it amounts to capture in the sense of \cref{def:judicial-power:capture} depends on evidence about privileged access and material effect in particular screening decisions, which this Part does not code. The checks within the system include the plurality of senior clerical authorities outside the state, which Muhammad Qasim Zaman's study of the contemporary ulama documents across Muslim societies \citep{zaman2002}, and the judicial tenure and administrative-review provisions just described.

- **Critique:** This paragraph merges at least three separate claims: (1) Iran's Guardian Council fuses legislative veto power with constitutional and religious interpretation ($C_{\pP\pJ}$ and $C_{\pJ\pI}$), (2) whether that fusion constitutes capture requires case-level evidence of privileged access, and (3) external clerical plurality and administrative courts check the judiciary. It also suffers from self-referential signposting ("in this Part's sense," "that Part II measures," "which this Part does not code," "provisions just described") and vague reference ("a further council" instead of naming the Expediency Council).

### Weakest Paragraph 3 (Line 248)

> In the series' terms, the judicial function depends on the legitimation pillar or the coercion pillar, and on neither specifically. The term $\ell$ is the compliance value supplied by what Part IV calls normative legitimacy (Part IV, Definition 2.2), and $\sigma$ is the expected sanction that Part V analyzes. The Nuer settlement and the Ju/'hoansi talking-out rest mainly on legitimacy and the value of continued relations; an imposed verdict in a party-state's political case rests mainly on sanction. Hamilton's executive arm is one way to supply $\sigma$; the reservoir of public support that James Gibson and coauthors measured for the United States Supreme Court is a way to supply $\ell$ \citep{gibson2003}. The disjunction matters for Part VII, which owns the dependency digraph among the six functions. At the judicial node the incoming dependency from legitimation and coercion is an or-condition, so a proof that the digraph is strongly connected must treat it as a hyperedge rather than as two separate arcs. The judicial function also feeds the others. Interpretation changes rules through precedent, which is input to Part II's rule of change. Reasoned judgments are public acts that shape common beliefs, which is input to Part IV's legitimation function.

- **Critique:** This paragraph shifts across three distinct claims: the incoming disjunctive dependency of adjudication on legitimacy or coercion, a technical graph-theoretic instruction for Part VII on hyperedges, and the outgoing effects of adjudication on rule-making and legitimation. Four of its nine sentences are meta-commentary about which companion paper "owns" or "analyzes" which concept.

---

### Model Rewrite of Weakest Paragraph 1 (Line 340)

> In Bourbon France, venal officeholding gave the appellate *parlements* the independence to check both the crown and the Church while tying adjudication directly to private wealth ($C_{\pF\pJ}$). Because judges owned their offices as heritable property, the crown could not remove them without compensation \citep{doyle1996}. That tenure security enabled the Parlement of Paris to remonstrate against royal edicts, forcing Louis XV to compel registration through the *lit de justice* until Chancellor Maupeou suppressed and reconstructed the *parlements* between 1771 and 1774 \citep{swann2003}. It also allowed the *parlements* to contest the Church's legitimating authority in the 1750s by prosecuting clergy who denied sacraments to Jansenists \citep{vankley1996}. Yet the same property right that insulated judges from the monarch entrenched a closed corporate elite whose privileges the courts defended against fiscal reform \citep{doyle1996}.

*(Why this works: It opens directly with the governing claim connecting venality, judicial independence, and the $C_{\pF\pJ}$ coupling; supports that claim with the mechanism and historical evidence from Doyle, Swann, and Van Kley; eliminates all cross-part signposting; and concludes with the qualification that venality entrenched corporate privilege.)*

---

VERDICT: MAJOR REVISIONS (major issues remain)
