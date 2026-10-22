---
reviewer: gemini-4-argon
paper: ideological-power
round: 1
date: 2026-10-22T14:37:26Z
---


### Summary Evaluation

This paper examines the ideological pillar ($\pI$) of a six-pillar model of governance, deriving the necessity of a public recognition function from a common-knowledge coordination axiom, analyzing the informational value of independent versus captured endorsements, and comparing institutional configurations across six regime types.

1. **Mathematical Correctness**: The proofs of Lemma 2.5, Proposition 2.9, Proposition 5.4, and Proposition 5.6 are correct. However, two formal defects weaken the theoretical core. First, Proposition 5.1 (lines 466–486) contains an internal game-theoretic inconsistency: an informed coalition that knows $\theta \in \{G, B\}$ chooses the authority's independence $\lambda \in [\lambda_{\min}, 1]$, yet the public's posterior $\mu_1(\lambda)$ is evaluated using the exogenous prior $\pi = \Prob(\theta = G)$, as though the public observes the chosen $\lambda$ without updating its belief about $\theta$ from the coalition's choice. Second, Theorem 3.4 (lines 250–261) does not use Assumption 3.3 (Non-innateness, lines 241–244), because Assumption 3.2 (Renewal, lines 236–239) already assumes the required ignorance directly. Several smaller technical issues also appear: $\mu_0$ is undefined at $\lambda = 0$ (lines 185, 194); Proposition 5.1 misses that $V_G(\lambda; \rho)$ is strictly convex in $\lambda$, making the coalition's optimal choice bang-bang on $\{\lambda_{\min}, 1\}$; and Corollary 5.3 (line 498) states that $\mu_1(\hat{\lambda}) - \mu_1(\lambda)$ is a function of the difference $\hat{\lambda} - \lambda$ alone.
2. **Clarity and Logical Structure**: The progression from network definitions (Section 2) to necessity (Section 3), comparative cases (Section 5), and failure modes (Section 6) is mostly clear, but the endorsement model is split across Section 2.5 (lines 178–221) and Section 6.2 (lines 462–506), separated by 240 lines of axiomatic derivation, literature review, and historical narrative. In addition, placing the typological reading of Revelation 13 (Section 8, lines 624–648) between Measurement (Section 7) and Objections and Scope Conditions (Section 9) interrupts the analytical transition from empirical identification to methodological scope conditions.
3. **Completeness**: The paper is not self-contained. It relies repeatedly on formal objects and propositions in unpublished companion parts—such as the rule of change (Definition 3.6 of Part II, line 112), the exit option (Definition 2.5 of Part VI, line 171), agenda control (Definition 2.9 of Part II, line 339), conversion elasticity (Definition 6.1 of Part I, line 380), the appointment channel (Definition 2.8 of Part II, line 390), and the latent veto (Proposition 3.5 of Part VI, line 566)—without defining them inline. Substantively, the comparative analysis omits digital platforms and algorithmic curation (acknowledged only as an omission on line 670), even though Section 4.3 (line 353) and Section 5.2 (line 392) rely on social media censorship evidence \citep{king2013}.
4. **LaTeX Quality**: The preamble loads unused packages (`graphicx`, `xcolor`, `tikz`, `longtable`, `listings`, lines 12–19) and defines unused environments and macros (`example`, `\Rules`, lines 31, 36, 47). The bibliography uses single hyphens (`-`) rather than en-dashes (`--`) for page and date ranges throughout lines 681–947, embeds translator and editor credits inside italicized book titles (lines 744, 789, 801, 831), and contains double punctuation (`?.` on line 882). Table 1 (line 286) packs four author-year citations into a 2.5 cm column, causing severe line wrapping.
5. **Prose Quality and House Style**: Most paragraphs state claims briskly and avoid heavy jargon, but several paragraphs violate the house style through roadmap signposting (lines 74, 78, 369, 374), multi-claim laundry lists (lines 78, 87–92, 412, 670), and nested subordination (lines 78, 670).

---

### Weakest Three Paragraphs and Model Rewrite

#### 1. Paragraph 5 of Section 1 ( line 78 )
> The paper makes four contributions. It derives the necessity of the ideological function from the coordination axiom (Ax4) of the series, adding two auxiliary assumptions that do real work: membership turns over, and rules vary across societies, so they cannot be innate. The derivation yields a recognition function, a recurring public practice that makes the operative rules common knowledge (\cref{thm:ideological-power:necessity}). It does not yield the necessity of belief in the rightness of rules, and the paper says so. It then develops an endorsement model in which an authority is independent with some probability and captured otherwise. Three results follow: a captured authority's endorsement is uninformative; independence helps coalitions whose rules are sound and hurts coalitions whose rules are unsound (\cref{prop:ideological-power:credibility}); and coordinated control of several authorities lowers the chance that an error is disclosed below what independent control achieves at the same average independence (\cref{prop:ideological-power:disclosure}). The third contribution is a comparison of the six regime types of the series at equal depth. The fourth is a set of measurable hypotheses, each with a stated falsifier.

*Critique*: This paragraph bundles four distinct claims into a single roadmap paragraph, relies on meta-discursive signposting ("The paper makes four contributions... It then develops... The third contribution is... The fourth is..."), inserts colloquial filler ("adding two auxiliary assumptions that do real work", "and the paper says so", "at equal depth"), and ends its second point with nested subordination ("lowers the chance that an error is disclosed below what independent control achieves at the same average independence").

#### 2. Paragraph 1 of Section 5 ( line 374 )
> Each subsection asks the same questions: which institutions hold the ideological function, how concentrated control over authoritative outputs is, how strongly the pillar is coupled to the other five, what preserves accountability, and which capture episodes and checks are documented. Concentration and coupling are described qualitatively. No numerical value of $H^{\pI}$, $Q^{\pI}$, $U_t$ or $\Int_t$ is reported for any polity, because no preregistered coding exists. Pair-level couplings follow the series convention: $C_{\pF\pI}$ is treated primarily in Part I, $C_{\pP\pI}$ in Part II and $C_{\pJ\pI}$ in Part III; $C_{\pI\pC}$ and $C_{\pI\pW}$ are treated primarily here.

*Critique*: This paragraph advances no substantive claim about regimes. It consists entirely of procedural signposting ("Each subsection asks the same questions..."), methodological qualification before any comparative finding is stated, and administrative cross-referencing across the series.

#### 3. Paragraph 1 of Section 8.5 ( line 670 )
> The comparison relies on secondary literature and codes concentration and coupling qualitatively. The regime types are ideal types with large internal variation, which the comparative sections record for Islamic states and Catholic monarchies in particular and which holds for the other four as well. The selection of historical illustrations is not a sample, and nothing in \cref{sec:comparative} estimates the frequency of capture in any regime type. Digital platforms and algorithmic curation create a configuration of the ideological layer, with few organizations controlling the reach of very many speakers, that this paper does not analyze; the framework accommodates them as channels whose control shares and contestability can be coded, but we report no evidence about them. The ethnographic cases carry the caveats stated in \cref{sec:necessity}. Finally, the formal models are deliberately simple. They treat soundness as binary, independence as a probability and disclosure as independent across authorities given their type; richer models would change magnitudes but not the direction of the results that the proofs establish.

*Critique*: This paragraph violates the one-claim-per-paragraph rule by combining six unrelated disclaimers—qualitative coding, internal variation within ideal types, non-random case selection, omitted digital platforms, ethnographic caveats, and simplifying formal assumptions—into a catch-all list, while embedding parenthetical subordination inside a relative clause ("create a configuration of the ideological layer, with few organizations controlling the reach of very many speakers, that this paper does not analyze").

#### Model Rewrite (replacing Line 78 with two focused paragraphs, each stating one claim directly before qualification)
> Every persistent collective with membership turnover and locally variable rules must implement a recurring public practice that makes its operative rules common knowledge (\cref{thm:ideological-power:necessity}). Because rules vary across societies, new entrants do not know them at entry; because coordination requires common knowledge of the rules, private instruction cannot suffice. This derivation establishes the necessity of rule recognition, not of normative belief in the rightness of rule.
>
> Independent authorities increase public confidence in sound rules and reduce it in unsound ones, whereas a captured authority's endorsement conveys no information (\cref{prop:ideological-power:credibility}). When a single coalition coordinates appointments across multiple authorities, the probability that at least one authority discloses an error falls below the level achieved by independently appointed authorities with the same average independence (\cref{prop:ideological-power:disclosure}). These mechanisms generate falsifiable predictions across market-capitalist, communist party-state, social-democratic, Islamic, Catholic-monarchical, and secular-democratic regimes.

---

### Structured Feedback by Severity

#### Critical Issues
None. The paper contains no fatal mathematical errors or irreparable empirical flaws, though two major theoretical defects require substantive revision before publication.

#### Major Issues

1. **Inconsistent information structure in the coalition's choice of independence (Section 5.2, Proposition 5.1, lines 466–488; Remark 5.2, lines 490–492)**
   In Proposition 5.1 (line 468), the governing coalition knows the state $\theta \in \{G, B\}$ before choosing $\lambda \in [\lambda_{\min}, 1]$ to maximize $V_\theta(\lambda; \rho) = \beta \E[\mu \mid \theta](\lambda) + \rho(1-\lambda)$, where $\E[\mu \mid \theta](\lambda)$ is taken from Definition 2.8 and Proposition 2.9. That specification makes three incompatible assumptions simultaneously:
   - The coalition knows $\theta$ when choosing $\lambda$ (line 468).
   - The public observes the chosen $\lambda$ (otherwise the posterior upon $e = 1$ is $\mu_1(\hat{\lambda})$ for a fixed conjecture $\hat{\lambda}$, not $\mu_1(\lambda)$).
   - The public still uses the exogenous prior $\pi = \Prob(\theta = G)$ after observing $\lambda$.

   If the public is Bayesian and observes the informed coalition's choice of $\lambda$, then $\lambda$ is a signaling action. Because a coalition with an unsound rule ($\theta = B$) uniquely chooses $\lambda = \lambda_{\min}$ for every $\rho \ge 0$ by Proposition 5.1(a), any choice $\lambda > \lambda_{\min}$ by a coalition with a sound rule ($\theta = G$) separates the two types: observing $\lambda > \lambda_{\min}$ causes the public to update its belief to $\Prob(G \mid \lambda) = 1$ before any endorsement occurs, and observing $\lambda = \lambda_{\min}$ causes the public to update its belief to $\Prob(G \mid \lambda_{\min}) = 0$. Conversely, if the coalition chooses $\lambda$ *covertly* while the public holds a fixed conjecture $\hat{\lambda} > 0$, then expected confidence given $\theta$ is
   \[
   \E_\lambda[\mu(\hat{\lambda}) \mid \theta] = \mu_1(\hat{\lambda}) - \lambda \Prob(s = 0 \mid \theta)\bigl(\mu_1(\hat{\lambda}) - \mu_0\bigr),
   \]
   which is strictly *decreasing* in actual independence $\lambda$ even when $\theta = G$ (since $\Prob(s = 0 \mid G) = 1 - q > 0$ and $\mu_1(\hat{\lambda}) > \mu_0$). Finally, if the coalition commits to $\lambda$ *before* learning $\theta$, then $\E[\mu] = \pi$ by the martingale property of posteriors. To make Proposition 5.1 coherent, either (a) specify that $\lambda$ is chosen ex ante (before $\theta$ is realized) by a designer or coalition whose payoff places higher weight $\beta_G > \beta_B$ on public confidence when rules are sound than when they are unsound, or (b) formulate and solve the signaling game with noisy observation of $\lambda$.

2. **Redundancy of Assumption 3.3 (Non-innateness) and gap in the justification of Assumption 3.2 (Renewal) (Section 3.1–3.2, lines 236–261; Abstract, line 64; Introduction, line 78)**
   The Abstract (line 64) and Introduction (line 78) state that Theorem 3.4 is derived from the coordination axiom (Ax4) together with membership turnover and the non-innateness (cross-cultural variability) of rules. In the formal text, however, Theorem 3.4 (line 252) invokes only Assumption 3.1 (`\cref{ax:coordination}`) and Assumption 3.2 (`\cref{ax:turnover}`), never citing Assumption 3.3 (`\cref{ax:noninnate}`). Assumption 3.3 is unused because Assumption 3.2 (lines 236–239) directly postulates the intermediate conclusion: that in every window $[t, t+L]$ some member $i \in N^\ast_{t+L}$ satisfies $\omega \notin K_{i,\tau_i} E_{t+L}$.
   Furthermore, the informal deduction on line 246 ("If a member enters within the window, non-innateness implies that the entrant did not know the rule set at entry") does not establish Assumption 3.2 from Assumption 3.3:
   - Assumption 3.3 (line 243) states that an entrant $e$ at date $\tau_e$ satisfies $\mathcal{P}_{e,\tau_e}(\omega) \not\subseteq E_{\tau_e}$ (ignorance of the rule set in force at $\tau_e$), whereas Assumption 3.2 (line 238) requires $\mathcal{P}_{e,\tau_e}(\omega) \not\subseteq E_{t+L}$ (ignorance at $\tau_e$ of the rule set in force at $t+L$).
   - Assumption 3.2 requires that the entrant $e$ belong to the cooperating core $N^\ast_{t+L}$ at $t+L$, not merely to $N_{t+L}$.

   Replace Assumption 3.2 with a genuine demographic turnover assumption—that within every window $[t, t+L]$ at least one member of $N^\ast_{t+L}$ entered during $[t, t+L]$—and strengthen Assumption 3.3 so that an entrant's initial cell $\mathcal{P}_{e,\tau_e}(\omega)$ is not contained in $E_s$ for any $s \ge \tau_e$. Then prove Renewal as a lemma from Turnover and Non-innateness before stating Theorem 3.4.

3. **Unresolved ontology of time-varying partitions vs. static state space in Theorem 3.4 (lines 238, 256–261)**
   Definition 2.4 (lines 127–130) defines knowledge operators on a static state space $\Omega$, where an event $F \subseteq \Omega$ is a subset of states. In the proof of Theorem 3.4 (line 260), the author writes that $F^\ast = \bigcap_{n \ge 1} K^n_{t+L} E_{t+L}$ is a public event that "therefore came into being within the window." As a subset of $\Omega$, $F^\ast$ exists timelessly; what changes between $\tau_i$ and $t+L$ is the profile of information partitions $\{\mathcal{P}_{j,s}\}_{j \in N^\ast_{t+L}}$, so that $F^\ast$ is not common-knowledge-certifying under the partitions at $s = \tau_i$ (or $i$ is not yet in the collective) and becomes public and contained in $\bigcap_{j \in N^\ast_{t+L}} K_{j,t+L} E_{t+L}$ under the partitions at $s = t+L$. State explicitly how the partition $\mathcal{P}_{i,s}$ is defined prior to member $i$'s entry date $\tau_i$, and rephrase (ii) in Theorem 3.4 (line 252) in terms of the refinement of the partition profile $\{\mathcal{P}_{j,s}\}$ rather than a subset $F^\ast$ "coming into being."

4. **Omission of digital platforms and algorithmic curation in the comparative analysis (Section 4, lines 376–430; Section 8.5, line 670)**
   Section 8.5 (line 670) notes that digital platforms and algorithmic curation "create a configuration of the ideological layer, with few organizations controlling the reach of very many speakers, that this paper does not analyze." Yet the paper's empirical claims cover contemporary market-capitalist, communist party-state, and secular-democratic regimes, and Sections 4.3 (line 353), 5.2 (line 392), and Table 3 (line 592) already rely on evidence from Chinese social media censorship \citep{king2013}. Treating contemporary media concentration ($H^{\pI}$) and exit/reviewability ($Q^{\pI}$) solely through print, broadcast, and state licensing while relegating platform distribution and algorithmic filtering to a scope-condition disclaimer leaves a major gap in Sections 5.1, 5.2, and 5.6. Integrate platform intermediaries and algorithmic curation into those comparative subsections and Table 3.

5. **Over-reliance on undefined concepts from companion papers (lines 74, 98, 112, 171, 227, 263, 339, 380, 390, 566)**
   The manuscript frequently delegates core definitions and proofs to Parts I, II, III, V, VI, and VII of the series—including "rule of change (Definition 3.6 of Part II)" (line 112), "the exit option that Part VI defines (Definition 2.5 of Part VI)" (line 171), "agenda control as an object of rule-making (Definition 2.9 of Part II)" (line 339), "conversion elasticity (Definition 6.1 of Part I)" (line 380), "the party's appointment channel (Definition 2.8 of Part II)" (line 390), and "its latent-veto result (Proposition 3.5 of Part VI)" (line 566)—while listing the only cited source paper \citep{largo2026hbs} as an unpublished working paper (line 846). Every formal term used in an argument should be defined concisely in this paper, and cross-references to unobtainable companion manuscripts should be replaced with self-contained statements.

6. **Structural placement of the endorsement model and the Revelation 13 section (Section 2.5, lines 178–221; Section 6.2, lines 462–506; Section 8, lines 624–648)**
   - The Bayesian endorsement model is introduced in Section 2.5 (Definition 2.8 and Proposition 2.9) and then resumed 240 lines later in Section 6.2 (Proposition 5.1, Remark 5.2, Corollary 5.3). Either keep the entire formal endorsement and disclosure analysis together in Section 6 (with a brief qualitative preview of $\lambda$ in Section 2.4) or place all formal models in Section 2/3 before the comparative applications.
   - Section 8 ("A typological reading of Revelation 13", lines 624–648) sits between Section 7 ("Measurement") and Section 9 ("Objections and scope conditions"). Moving from empirical identification problems (line 622) to biblical typology (line 624) and then back to social-scientific measurement objections (line 666) breaks the analytical arc. Move Section 8 to an appendix or place it after Section 9 as a concluding interpretive coda.

---

#### Minor Issues

1. **Undefined posterior $\mu_0$ at $\lambda = 0$ (Definition 2.8, line 185; Proposition 2.9, lines 194, 200)**
   In Definition 2.8 (line 184), $\lambda \in [0, 1]$. At $\lambda = 0$, the authority is captured with probability $1$ and always endorses ($e = 1$), so $\Prob(e = 0) = \lambda a = 0$ (line 200). Consequently, $\mu_0 = \Prob(G \mid e = 0)$ is undefined by Bayes' rule at $\lambda = 0$. Specify in Definition 2.8 and Proposition 2.9(b) that $\mu_0 = \Prob(G \mid e = 0) = \pi(1-q)/a$ is defined for $\lambda \in (0, 1]$ (with continuous extension to $\lambda = 0$).

2. **Strict convexity and bang-bang optima in Proposition 5.1 (lines 466–486)**
   In the proof of Proposition 5.1(c) (line 485), $\frac{d}{d\lambda}\E[\mu \mid G] = a(\mu_1(\lambda) - \mu_0)^2 / \pi$ is strictly increasing in $\lambda$. Thus $\E[\mu \mid G](\lambda)$ and $V_G(\lambda; \rho) = \beta \E[\mu \mid G](\lambda) + \rho(1-\lambda)$ are strictly convex on $[\lambda_{\min}, 1]$. Because a strictly convex function on a compact interval attains its maximum only at the endpoints, the coalition's optimal choice when $\theta = G$ is always in $\{\lambda_{\min}, 1\}$, and $\lambda = 1$ is the unique maximizer if and only if
   \[
   \rho < \beta\,\frac{\E[\mu \mid G](1) - \E[\mu \mid G](\lambda_{\min})}{1 - \lambda_{\min}}.
   \]
   The condition stated in Proposition 5.1(c), $\rho < \beta a(\mu_1(\lambda_{\min}) - \mu_0)^2 / \pi$, is only the tangent slope at $\lambda_{\min}$ (sufficient, not necessary). Stating the strict convexity and exact threshold would sharpen both Proposition 5.1(b) and 5.1(c).

3. **Imprecise comparative static phrasing in Corollary 5.3 (line 498)**
   Line 498 states that $\mu_1(\hat{\lambda}) > \mu_1(\lambda)$ if and only if $\hat{\lambda} > \lambda$, "and the gap increases with $\hat{\lambda} - \lambda$." Because $\mu_1(\cdot)$ is nonlinear, $\mu_1(\hat{\lambda}) - \mu_1(\lambda)$ is not a function of $\hat{\lambda} - \lambda$ alone. Revise to: "and the gap $\mu_1(\hat{\lambda}) - \mu_1(\lambda)$ is strictly increasing in $\hat{\lambda}$ and strictly decreasing in $\lambda$."

4. **Attainability of the upper bound in Proposition 5.4(a) (lines 515, 524, 536)**
   In Proposition 5.4(a) (line 515), the upper bound $D \le 1 - (1-p)^{\lambda K}$ derived via Jensen's inequality (line 524) is attainable if and only if $\lambda K$ is an integer (since $N \in \{0, 1, \dots, K\}$ is integer-valued). When $\lambda K \notin \mathbb{Z}$, the maximum over distributions of $N$ with $\E[N] = \lambda K$ is attained by a two-point distribution supported on $\{\lfloor \lambda K \rfloor, \lceil \lambda K \rceil\}$. Note this integer constraint briefly on line 524 or line 536.

5. **Unused packages, macros, and theorem environments in the LaTeX preamble (lines 12–19, 31, 36, 47)**
   Remove `\usepackage{graphicx}`, `\usepackage{xcolor}`, `\usepackage{tikz}`, `longtable`, `\usepackage{listings}`, `\lstset{...}`, `\newtheorem{example}[theorem]{Example}`, `\crefname{example}{Example}{Examples}`, and `\newcommand{\Rules}{\mathcal{R}}`, none of which are used in the document.

6. **Table formatting and punctuation (Tables 1–4, lines 281–298, 434–451, 578–597, 601–620)**
   - In Table 1 (line 286), the first column has width `L{2.5cm}`, which forces `Ju/'hoansi \citep{lee1979,lee2013,marshall1976,wiessner2005}` (line 290) into a cramped multi-line block. Widen the first column to at least `3.2cm` or move the citations into the second column.
   - Cells across Tables 1–4 omit terminal periods, including cells that contain two sentences separated by an internal period (e.g., lines 290–295). Either end all multi-sentence table entries with a period or rewrite them as parallel noun phrases.

7. **Typography and bibliography formatting (lines 641, 681–947)**
   - On line 641, replace `(13:16 to 13:17)` with `(13:16--13:17)` for consistency with standard biblical citation format.
   - Throughout the bibliography (lines 681–947), replace single hyphens (`-`) in page ranges and year spans with en-dashes (`--`) (e.g., `1236--1239` on line 696, `1540--1770` on line 816, `1917--1929` on line 828).
   - Move translator and editor credits outside `\emph{...}` on lines 744, 789, 801, and 831 (e.g., `\emph{Society against the State: Essays in Political Anthropology} (1974), trans. Robert Hurley`).
   - On line 882, remove the period after `\emph{Why Trust Science?}` to eliminate the double punctuation `?.`.
   - On line 846, clarify the relationship between `Largo, Mateo (2026)` and the author `Matthew Long` (line 54), and provide an institutional repository or URL for the working paper.

8. **Additional paragraph-focus revisions for house style (lines 87–92, 412)**
   - Lines 87–92 (Section 2.1, Paragraph 1) pack twelve definitions from the source framework into a single 14-sentence paragraph with no governing claim. Split it into one paragraph defining the network and intra-pillar concentration ($G_t, s^m_{i,t}, H_{m,t}, Q_{m,t}, U_t$) and a second paragraph defining cross-pillar integration and capture links ($C_{mn,t}, \Int_t$).
   - Line 412 (Section 5.4, Paragraph 4) combines juristic pluralism, medieval endowments, modern educational fragmentation, urban-rural religious differences, and the Kuru–Rubin debate into a single paragraph. Split the medieval checks from the modern fragmentation and developmental debates.

VERDICT: MAJOR REVISIONS (major issues remain)
