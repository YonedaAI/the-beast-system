---
reviewer: claude-fallback-referee (agy timed out twice)
paper: coercive-power
round: 1
date: 2026-10-22T16:52:09Z
---


# Peer Review: *Coercive Power and Enforcement* (Part V of *The Six Pillars of the Beast System*)

Object numbers below follow the compiled `coercive-power.aux`: Def 2.1 sanction, Def 2.2 control share, Def 2.3 $Q^{\pC}$, Def 2.4 sanction regime, Def 2.5 margins, Assumption 3.1 (Ax5), Lemma 3.2, Theorem 3.3, Corollary 3.4, Proposition 3.5 (second-order), Proposition 3.6 (minimal form), Propositions 6.1 to 6.4. Line numbers refer to `papers/latex/coercive-power.tex`. I did not compile or edit the paper.

**Summary judgment.** This is the most carefully argued pillar paper I have seen in the series. It states its axiom, says what would refute it, and keeps the necessity of a function apart from the necessity of an institution. The conduct-margin and allegiance-margin vocabulary is a real contribution. Two problems sit at the centre of the capture half of the argument, though. First, the paper's own definitions do not let the allegiance margin be defined consistently. Second, the headline claim that allegiance-conditioned sanctioning weakens deterrence contradicts Proposition 6.1(ii). Several proofs in Section 3 also need repair, and the comparative section applies an uneven standard of evidence across regime types.

---

## 1. Mathematical correctness

### 1.1 Definitions

- **Def 2.1 vs Def 2.5 (lines 88, 90 to 95, 129 to 134).** Def 2.1 counts a cost as a sanction only if it responds to "an observed or alleged violation of a rule", and line 95 excludes costs that "fall on an agent regardless of what the agent does". Line 88, however, says that the coercive layer records costs imposed in response to "conduct or status". The allegiance margin $A(0) = q(0,\mathrm{op}) - q(0,\mathrm{al})$ measures costs imposed on non-violators because of their status. Under Def 2.1 those costs are either not sanctions at all, or they are sanctions for violating some other rule ("do not oppose the coalition"). In the second case the violation indicator $v$ and the alignment $a$ are collinear for that rule, and the separation between the two margins disappears. The paper never says which rules are admissible arguments of $q(v,a)$. This is the conceptual gap behind Critical issue 1.
- **Def 2.2 (lines 97 to 102).** The control share includes the authority "to appoint or remove those who carry out such orders", but the definition gives no rule for dividing control along a chain of command, even though shares must sum to one. Do the minister who appoints the police chief and the chief who orders arrests both hold the share, or only one of them? Line 102 settles this implicitly in favour of the apex: a single chain gives concentration "at the top of that chain ... regardless of its size". Lines 326 and 477 then say that $H^{\pC}$ "below the apex falls" when the apex divides its forces into $k$ organizations it still appoints. Under line 102's reading, $H^{\pC}$ does not fall. A local or layered concentration measure is needed, or the two passages contradict each other.
- **Def 2.4 (lines 117 to 125).** $\E[\Phi_{i,t}\mid v_{i,t}=1,h_t]$ conditions on an action that is off-path whenever $\sigma_i$ prescribes compliance. The margin should be defined through the continuation under the unilateral deviation, holding $\sigma_{-i}$ fixed. It should also be stated whether $i$'s own future strategy is held fixed or re-optimized (see 1.2).
- **Def 2.3 component (1), line 115.** The restatement of Part II Proposition 6.5(c) drops Part II's hypothesis that "command runs only through appointment" ($\gamma_S = 0$). For coercion the omitted channel is exactly the one that matters: budgets, business holdings and patronage, as with the IRGC case at lines 360 and 492. Line 115 also turns a bound on the integration measure $C^{\mathrm{ov}}_{\pP\pC}$ into "the formal content" of a contestability component. Integration and contestability are different objects in the source's $U_t$ and $\Integ_t$.

### 1.2 Lemma 3.2 and Theorem 3.3

- **Lemma 3.2 proof (line 166).** The decomposition $\tau_{i,t}v_{i,t} + \Phi_{i,t} + K_{i,t}$ with $K_{i,t}$ independent of $v_{i,t}$ fails in a dynamic game. $K_{i,t}$ contains $i$'s own future temptation payoffs $\sum_k \delta^k \tau_{i,t+k} v_{i,t+k}$. Under best responses, $i$'s future choices depend on future margins, and those margins depend on the history, including $v_{i,t}$. Proposition 3.6 shows the effect: an excluded agent faces a different margin from one in good standing. The clean fix is to define $\varsigma_{i,t}$ as the difference in *total* expected continuation value, excluding $\tau_{i,t}$, between compliance and violation under the continuation of $\sigma$. The lemma then holds as stated.
- **Theorem 3.3 (lines 171 to 183).** (a) $\bar\mu$, "the long-run average", need not exist. Use $\limsup$ or $\liminf$ and state which. (b) The proof equates the realized violation frequency with $\bar\mu[1-G(\varsigma_{i,t})]$. Because $\varsigma_{i,t}$ is history-dependent and random, this needs a martingale strong law, since $v_{i,t} - (1-G(\varsigma_{i,t}))$ is a martingale difference, or else a statement in expectation. (c) Ties are harmless. A tie raises the violation rate above $1 - G(\varsigma)$, so the inequality's direction survives, and a sentence saying so would help. (d) The bound can be sharpened at no cost. Each term satisfies $G(\varsigma)-G(0) \le 1-G(0) = p$, so the long-run share of agent-periods with $\varsigma_{i,t} > 0$ is at least $(p-\theta)/p$. That is a more useful statement than "positive".
- **Corollary 3.4** is correct for the right-continuous generalized inverse.

### 1.3 Bridge from Theorem 3.3 to Proposition A

- **Informal vs formal Ax5 (lines 145 to 156).** "Some members sometimes break rules" is about observed violations. Assumption 3.1 ($p > \theta$) is about counterfactual temptations, and it is strictly stronger: observed violations are compatible with $p \le \theta$. To deliver Proposition A for every $G \in \mathcal{G}$, the paper needs an explicit existential bridge: every functioning governance system has at least one rule in force with $p > \theta$. Without that bridge it is unclear whether "functioning" is doing definitional work.
- **Regime vs implemented function.** Theorem 3.3 proves a positive deterrence *margin*, which is a threat. Def 2.1 says the function is *implemented* only if "sanctions occur with non-trivial regularity". If $G$ has bounded support and $\varsigma > \sup \tau$, there are no on-path violations and no sanctions, so the theorem's conclusion holds while Def 2.1's implementation condition fails. The paper must say which notion Proposition A requires for $\pC$.

### 1.4 Proposition 3.5 (second-order enforcement)

The proof is valid given its premise. The exhaustiveness claim (line 206) is a partition by assertion. It also omits general deterrence of third parties, the benefit to $j$ of deterring agents other than $i$, which belongs in (d). The larger problem is the interpretation at lines 209 to 211, on which Parts I and VII rely: Part I cites Prop 3.5 for $\pF\to\pC$, and line 209 asks Part VII to treat it as a hyperedge.

- The claim that term (c) "can close the regress in equilibrium only if agents share common knowledge ... which again requires legitimation (Ax4)" is not proved. Equilibrium requires correct beliefs about strategies. If equilibrium beliefs count as "legitimation", then $\pI\to\pC$ holds by definition, which the series' proof standard forbids. Community-enforcement equilibria in large random-matching populations, Kandori-style contagion, are a standard counterexample: they need neither transfers nor an intrinsic norm.
- The claim that term (d) "is decisive only in small groups" follows Olson for *public-good* sanctions. For *bilateral* exclusion, as in the Maghribi coalition or Prop 3.6, each excluder's act is decisive for its own relationship whatever $n$ is, and the cost $c_j$ is often non-positive: refusing to rehire a cheat saves money. In that case the proposition's premise $c_j > 0$ fails, and the dependency on $\pF$ or $\pI$ does not follow.

State the large-$n$ dependency as a conditional proposition, with explicit assumptions on sanction technology (costly, public-good type), or as a conjecture.

### 1.5 Proposition 3.6 (minimal form)

- **The margin formula is false at reachable nodes.** Take $L = 2$ and an agent who violated at $t-1$, so it is excluded in periods $t$ and $t+1$. Violating at $t$ extends exclusion to $t+2$ only, so $\varsigma = b\delta^2$, not $b\delta(1+\delta)$. Since $1 - G(\varsigma) > 0$ generically, such nodes are reached with positive probability. The proposition should state the margin for agents in good standing and give the state-dependent margin otherwise: $b\sum_{k=r+1}^{L}\delta^k$ with $r$ periods of exclusion remaining.
- **The profile does not meet Theorem 3.3's hypothesis.** Line 216 says the result "shows that the theorem's requirements can be met with no specialized role". Theorem 3.3 assumes a best-response profile for *all* agents, including sanctioners, and line 227 concedes that the profile is not shown to be an equilibrium. Either give a sufficient condition under which the extended profile is subgame perfect, via the one-shot deviation principle with a bound in $n$, $\delta$ and $L$, or soften line 216.

### 1.6 Section 6 propositions

- **Proposition 6.1** is correct. Note that (ii) is exactly the construction that refutes the abstract's headline claim (Critical issue 2).
- **Proposition 6.2** is correct. The derivative $G(Es) + Esg(Es)$ checks out. But the proposition is about conduct-insensitivity *within* one alignment ($q(0,a)\to q(1,a)$). It says nothing about the allegiance margin unless $q(1,\mathrm{op})$ is held fixed while only $q(0,\mathrm{op})$ rises. Lines 458 and 572 read it as a result about allegiance.
- **Line 460**, on the symmetric failure mode: "busier than before" is not shown. With supporters' sanctions falling, total volume can fall if supporters are numerous.
- **Proposition 6.3** is correct. It is a decreasing-differences comparative static, and the proof is sound. The assumption that $e$ is non-decreasing is never used. HC1 says the result is about "elite threat" vs "mass threat", but the model has one parameter $r$ and does not represent mass threat at all.
- **Proposition 6.4.** (a) $\Psi(K_t)\to\infty$ does all the work and is implausible, because the value of seizing a polity is bounded by its surplus, which also bounds $\bar w$. Replace it with $\lim_t \Psi(K_t) > \bar w/(1-\delta) + \chi$. (b) The left side should be $\sum_k \delta^k w_{t+k}$, not $w_t/(1-\delta)$. (c) "Only a reduction of $K_t$ can restore the condition" (line 489) is false outside the infinite case: raising $\chi$, for example with Proposition 6.3's counterweights, or raising $\bar w$ also works. (d) The probability of success is not modelled.

---

## 2. Clarity and completeness

The prose is direct, and the paper is unusually honest about its limits (lines 253, 304, 347, 589). The gaps:

1. **Dependency vs integration.** Lines 102, 345, 364 and 503 use the integration coefficient $C_{mn}$, which measures one coalition commanding both pillars, for what are dependency arcs. Line 102 calls Weber's legitimacy claim "the coupling ... $C_{\pI\pC}$". Line 364 calls ulama authority that *constrains* rulers a coupling $C_{\pI\pC}$, but authority held by a distinct group is evidence of *low* $C_{\pI\pC}$. Conscription (lines 345, 503) is a $\pW\to\pC$ dependency, not co-command of production. Line 138 defines $C_{m\pC}$ correctly, so the later usage contradicts it. This matters because $C_{mn}$ feeds $\Integ_t$ and the strong classification.
2. **Capture definition drift.** Line 434 says capture "is a positive allegiance margin attached to a coalition". Line 436 correctly restores the source's three-part capture link. The comparative section labels the Terror (line 332) a capture episode, yet line 332 describes $q(0,a)$ rising toward $q(1,a)$ for all $a$, including party members. That is arbitrariness, not allegiance, so under line 434 it would not be capture. Use one definition throughout.
3. **HC1, HC4 and HC9.** These claim to "follow from" propositions that do not imply them (see Major 8 and Minor 4).
4. **The abstract** attributes the theorem's content to "a deterrence lemma" (line 58).

## 3. Logical structure

The spine is followed and is not at issue. Inside it, the argument has one structural weak point. The paper's thesis that A does not imply B in this pillar rests on the separability of the two margins, but the narrative sections (abstract, line 70, Section 8, conclusion line 596) rely on a *trade-off* between them, which the formal section does not deliver. The fix is to add the missing constraint. Under a fixed sanctioning capacity, $\sum_a n_a S(a) \le \bar B$, diverting capacity to non-violating opponents must lower some conduct margin. That is a genuine proposition the paper could prove, and it would make Section 8 and HC9 follow from the formal results rather than from intuition.

The necessity argument (Section 3) is well ordered. Its counterexample subsection (lines 258 to 264) is strong, apart from the immunization problem in Major 4.

## 4. LaTeX quality

The source is clean. Theorem environments share one counter, `\cref` is used consistently (53 uses), tables use `tabularx` with `booktabs` and captions above, and the `\qedhere` placement in Proposition 6.2 is correct. The cross-reference labels resolve in the existing `.aux`. Remaining items:

- Notation collisions:
  - $s$ is both the control share $s^{\pC}_{i,t}$ (line 99) and the sanction magnitude (line 131).
  - $E(a)$ is the conduct margin while $\E$ is expectation.
  - $A(v)$ clashes with the adjacency $A^m_t$ and with "Proposition A".
  - $a$ is both alignment and the edge weight $a^m_{ij,t}$.
  - $q(v,a)$ clashes with the contestability components $q_{k,t}$.
  - $K_{i,t}$ (line 166) and $K_t$ (line 485) clash with each other and with Part VI's maintenance requirement $K_t$. $\Psi$ also appears in Part VI.
  - `\varsigma` is easily misread as a final sigma.
- Bibliography details: see Section 6.

## 5. Guardrails

| Guardrail | Status | Notes |
|---|---|---|
| Six regime types at equal depth | **Partly met** | Word counts run from 493 (secular democracy, lines 379 to 391) to 726 (Islamic states, lines 351 to 365), a ratio of 1.47. More important is the **unequal standard of evidence**, set out below. |
| No polemic on Islam or Catholicism | Met | Sunni/Shi'i and dynastic/revolutionary diversity is noted (line 354). "Slave soldier" is confined to its technical sense (line 356). Alfoneh is paired with RAND (line 360). The Habsburg, Bourbon and Papal cases are differentiated. Small gaps: Kamen's revision is called "contested" (line 375) and Conquest's numbers "debated" (line 332), but no critic is cited in either case (KB guardrail 6). |
| Revelation with scholars, never futurist | **Mostly met** | Typological reading, explicit refusal of identifications, Bauckham, Koester, Kraybill and Collins all present (lines 566 to 574). **But** the reading of 13:10 (line 574) rests on the KJV/Textus Receptus wording without acknowledging the well-known textual and interpretive crux (Major 10). Romans 13 is read with no scholarly source. Rev 17 to 18, which the brief lists, is unused. |
| Differentiation is not capture | Met | Lines 68, 317, 434 to 436 and 585 are exemplary. |
| A is not true by definition | **At risk** | Two routes to definitional truth: the reclassification escape in the falsifier (Major 4), and the claim that equilibrium common knowledge is "legitimation" (Major 5). |
| "Beast System" never labels a group | Met | Line 66. |

**Unequal standard of evidence (major).** For market-capitalist societies the paper insists on the full three-part capture-link test and rejects Eisenhower's warning as evidence (line 317). This is correct, but the same test is not applied elsewhere:

- The Mamluk seizure of rule, the Janissaries' "emergence as a political actor" (line 364) and the Terror (line 332) are labelled "documented capture episodes" without the material-evidence step.
- The Janissary claim at line 358 has no citation. Kunt (1983) concerns provincial households, not Janissary politics.
- The social-democratic subsection reports no capture case "in the Nordic sources reviewed" (line 347). Yet there are well-known episodes of exactly the allegiance-margin type the paper models in the Church Committee case. Two leads for the author to verify and cite from scholarly or official sources: the Swedish IB affair (1973), the exposure of military-intelligence surveillance of the political left, and the Norwegian Lund Commission report (1996) on police-security surveillance.
- The market-capitalist subsection has a hypothesis but no documented episode or check of its own, since its checks are deferred to Section 5.6 at line 315. A verified case of private or public coercion in labour disputes would give it parity.

Applying one standard to all six types, and giving each a documented episode and a documented check, is required for even-handedness.

## 6. Citations

I checked every cite key against the KB status tags and resolved the seven keys absent from the KB through Crossref or primary text.

- **All seven non-KB entries exist and match:**
  - becker1968: JPE 76(2):169 to 217.
  - edwards2012: EHR 65(2):421 to 444, online 2011.
  - hedlund2011: AFS 39(1):135 to 157. Online 2011, but 39(1) is the 2013 print issue. The abstract confirms "1984 to 2011" and the rank-system and education findings.
  - knowles2001: JPE 109(1):203 to 229.
  - pilster2011: CMPS 28(4):331 to 350.
  - church1976: S. Rep. 94-755.
  - jo2026: URL, not re-fetched.
- **All 113 KB-sourced keys carry VERIFIED tags.** No cited key is missing from the bibliography, and none is uncited.
- **Quotation altered (major).** Line 386 quotes the Church Committee as saying beliefs "posed no threat of violence or illegal acts''" and closes the quotation there. The original sentence (Book II, Summary, checked against the archive.org text of the final report) continues "... or illegal acts *on behalf of a hostile foreign power*." The truncation has no ellipsis and changes the scope of the finding. Restore the full clause or mark the omission, and add a page number.
- **Hobbes (line 145):** the text is "covenants, without the sword, are but words", not "mere words". Quote it exactly or mark it as a paraphrase.
- **KJV quotations (lines 568 to 574)** of Rev 13:4, 13:7, 13:10, 13:15, 13:17 and Rom 13:3 to 4 match the KJV verbatim.
- **Bibliographic details:**
  - Incomplete page ranges: Bellin 2004 (line 638, should be 139 to 157), Perlmutter 1969 (line 881, 382 to 404), Woodburn 1982 (line 961, 431 to 451) and Greif 1993 (line 752, no pages, 525 to 548 per KB).
  - "Reciprocity?." double punctuation (line 952).
  - The Boyer DOI resolves to a 2009 reissue record (line 653).
- No invented DOIs found. Every DOI I tested resolves to the stated work.

---

## 7. Numbered issue list

### Critical

1. **The allegiance margin is not well defined under the paper's own definitions (lines 88, 90 to 95, 129 to 134, 332, 570).**
   - *Issue:* Def 2.1 makes sanctions responses to rule violations. Costs imposed on non-violating opponents are then either not sanctions, or sanctions for violating a loyalty rule, in which case $v$ and $a$ are collinear and $A(v)$ collapses into $E$. The Rev 13:15 reading (line 570) has the same problem: under the decree, refusal to worship *is* the violation. The Terror (line 332) is coded as capture although the paper describes arbitrariness across alignments.
   - *Fix:* (a) Extend Def 2.1 so that costs triggered by status count as coercive acts. (b) Restrict $q(v,a)$ to a preregistered set of allegiance-neutral rules taken from $\pP$. (c) Assign loyalty-encoding rules to Part II as rule-making capture (line 585 already gestures at this). (d) Separate arbitrariness ($E\to 0$ for all $a$) from allegiance ($A>0$) in Section 5 and the Revelation reading.

2. **The headline trade-off contradicts Proposition 6.1(ii) (lines 58, 70, 572, 596).**
   - *Issue:* The abstract states that "allegiance-conditioned sanctioning raises the volume of coercion while weakening deterrence". Proposition 6.1(ii) constructs a regime with allegiance margin $x>0$ and unchanged deterrence: for example $q(0,\mathrm{al})=0$, $q(1,\mathrm{al})=0.5$, $q(0,\mathrm{op})=0.3$, $q(1,\mathrm{op})=0.8$. Proposition 6.2 concerns within-alignment arbitrariness, not allegiance.
   - *Fix:* State and prove the trade-off under an explicit sanctioning-capacity constraint, or restate the claim conditionally ("when sanctions on opponents are raised without raising sanctions on opposing violators"), consistently in the abstract, introduction, Section 8 and conclusion.

### Major

1. **Lemma 3.2's payoff decomposition fails dynamically (line 166).** Own future payoffs depend on $v_{i,t}$ through history-dependent margins. Redefine $\varsigma$ as the full continuation-value difference, and define it through unilateral deviation (Def 2.4).
2. **Proposition 3.6 is false at reachable nodes and does not meet Theorem 3.3's hypothesis (lines 216 to 227).** Counterexample: $L=2$, an excluded agent has $\varsigma=b\delta^2$. Restrict the claim to agents in good standing, give the state-dependent margin, and either prove equilibrium under a stated condition or soften line 216.
3. **The bridge from Theorem 3.3 to Proposition A is unstated (lines 92, 145 to 156, 171 to 183).** Formal Ax5 is strictly stronger than informal Ax5. The theorem yields a positive margin (a threat), not an "implemented" function in Def 2.1's sense. State the existential bridge assumption and say which notion of $\pC$ Proposition A requires.
4. **The falsifier is immunized (lines 260, 264, 579).** $p$ is unobservable. Any compliant, unsanctioned case is reclassified as $p\le\theta$ (line 260) rather than counted as a refutation. Commit in advance to an independent measurement of $p$, for example anonymous-opportunity designs, before sanction practices are observed. Otherwise the necessity claim risks being true by definition.
5. **The large-$n$ dependency on $\pF$ or $\pI$ is asserted, not derived (lines 209, 211, 72).** Equating equilibrium beliefs with legitimation makes $\pI\to\pC$ definitional, and community-enforcement equilibria are counterexamples. Term (d) does not vanish with $n$ for bilateral exclusion, where $c_j\le 0$. Restate as a conditional proposition with assumptions on sanction technology. Notify Parts I and VII, which cite it.
6. **The control share is undefined for nested command, and the text contradicts itself (lines 97 to 102, 326, 477).** Specify how shares are divided along chains. Either drop "$H^{\pC}$ below the apex falls" or define a layered concentration measure.
7. **Dependency arcs are conflated with the integration coefficient $C_{mn}$ (lines 102, 345, 364, 503).** Use arc notation ($\pI\to\pC$) for dependencies and reserve $C_{mn}$ for co-command, consistent with line 138.
8. **HC9 is not identified (lines 458, 557).** A temptation shock with fixed $q$ and $E>0$ raises both violations and $S(a)$ with zero allegiance margin, so "sanctions up, compliance down" also fits a crime wave. Add the condition that the rise is concentrated among measured opponents with matched conduct, or drop the claim that this is "the signature".
9. **The standard of evidence is unequal across regime types (lines 317, 332, 347, 358, 364).** Apply the three-part capture-link test to every claimed episode. Cite the Janissary claim. Investigate and verify Nordic surveillance episodes (IB affair 1973; Lund Commission 1996). Give the market-capitalist type its own verified episode and check.
10. **The Revelation 13:10 reading rests on one textual tradition (line 574).** The KJV/Textus Receptus wording supports "the coercer under the same rule". Critical texts and most modern commentators read the verse, echoing Jeremiah 15:2, as a call to accept captivity and death. Acknowledge the crux and engage Koester or Bauckham on it, or drop the inference to component (4). Also line 572 says Theorem 3.3 shows every collective needs a regime with "no allegiance margin". The theorem constrains only the conduct margin.
11. **Church Committee quotation truncated without ellipsis (line 386).** The omitted clause is "on behalf of a hostile foreign power". Restore it and add a page reference.

### Minor

1. Theorem 3.3: replace $\bar\mu$ with $\limsup$ or $\liminf$, justify realized frequency by a martingale strong law or state the result in expectation, and add the sharper bound: share of positive-margin agent-periods $\ge (p-\theta)/p$.
2. Proposition 6.4: replace $\Psi\to\infty$ with a threshold condition, use $\sum\delta^k w_{t+k}$, and correct "only a reduction of $K_t$" (raising $\chi$ or $\bar w$ also works).
3. Proposition 6.3: drop or use the unused monotonicity of $e$, and state how $r$ maps to measured elite threat.
4. HC1 and HC4 say they "follow from" Propositions 6.3 and 3.5. Neither proposition models mass threat or contestation. Write "are motivated by".
5. Line 460: "busier than before" is unproved. Total sanctions can fall when supporters predominate.
6. Line 115: restate Part II Prop 6.5(c)'s $\gamma_S=0$ hypothesis, and do not equate an integration bound with a contestability score.
7. Notation collisions ($s$, $E$/$\E$, $A$, $a$, $q$, $K$, $\Psi$, `\varsigma`): rename locally.
8. Lines 138 and 209 cite Part III Proposition 3.7 for the disjunctive dependency. My count of the current `judicial-power.tex` source (Assumptions 3.1 and 3.2, Theorem 3.3, Propositions 3.4 to 3.6, Corollary 3.7) puts it at 3.6. Check against a fresh Part III compile.
9. Proposition 3.5: add general deterrence of third parties to term (d), and present exhaustiveness as a payoff-decomposition assumption.
10. Hobbes (line 145): use "but words" or mark it as a paraphrase.
11. Bibliography: complete page ranges (Bellin, Perlmutter, Woodburn, Greif); fix "Reciprocity?."; note Hedlund's online and print years; cite a critic for Conquest and for Kamen.
12. Equal depth: bring secular democracy (493 words) and social democracy (535 words) closer to the others.
13. Outcome test (line 542): address infra-marginality, and the possibility that the "independent review" is itself captured, which is Part III's concern.
14. Section 8: give Romans 13 at least one scholarly anchor and a citation for "often read as contradictory". Consider Rev 17:16 to 17, read with the cited commentators, as the typological image for Proposition 6.4.
15. Harmonize capture language (line 434 vs line 436), and map each HC hypothesis to the source's H1 to H6. Give HC10 a threshold.

VERDICT: MAJOR REVISIONS (major issues remain)
