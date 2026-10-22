---
paper: coercive-power (Part V)
checked: papers/latex/coercive-power.tex and papers/pdf/coercive-power.pdf (both 2026-10-22 12:15)
against: reviews/coercive-power-review.md, section 7 (2 critical, 11 major, 15 minor)
date: 2026-10-22
---

# Fix verification: Part V, Coercive Power and Enforcement

Result numbers below follow the final PDF (pdftotext): Def 2.1 to 2.5, Ass 3.1 (Ax5), Ass 3.2 (Bridge), Lemma 3.3, Thm 3.4, Cor 3.5, Prop 3.6 (second-order), Cor 3.7 (scale), Prop 3.8 (minimal form), Props 6.1 (separability), 6.2 (arbitrary), 6.3 (capacity), 6.4 (coup-proofing), 6.5 (dependent corps). Line numbers (L) refer to the final .tex. No `??` in the PDF. Cross-part references checked against the sibling PDFs: Part III Prop 3.6 and Def 2.4, Part II Def 2.8 and Prop 6.5, Part IV Def 2.1, and Part VI Defs 2.4 and 2.5 all resolve. Part I (financial-power.tex L478) and the Part VII model (model/beast_system/necessity.py L88 to 92) now cite Part V Prop 3.6, Cor 3.7 and Thm 3.4 with the correct numbers and conditions.

## Status table

| # | Sev | Issue (short) | Status | Evidence | Remaining fix |
|---|---|---|---|---|---|
| C1 | critical | Allegiance margin ill-defined under Def 2.1 | FIXED | Def 2.1 (L113) now defines a *coercive act* by "conduct or status", with a *sanction* as a subtype. L116 places status-based costs among coercive acts. Def 2.5 (L152) adds a preregistered allegiance-neutral reference set R⁰. L155 excludes loyalty rules from R⁰, assigns their enactment to Part II as rule-making capture, and defines arbitrariness separately. The Terror (L378) is recoded as arbitrariness, with capture depending on the Conquest/Getty evidence. The Rev 13:15 reading (L633) uses R⁰. | None. |
| C2 | critical | Headline trade-off contradicts Prop 6.1(ii) | PARTIAL | New Prop 6.3 (L512 to 519) proves the deterrence half under a capacity constraint. L521 states the scope correctly. **But** the abstract (L79), the intro (L91) and the conclusion (L661) still say that, when capacity is limited, allegiance targeting "raises the volume of coercion". Prop 6.3 says nothing about volume, and the claim fails inside the paper's own model. Counterexample: n_al = n_op = 1, κ₁ = 1, κ₀ = 10, μ = 1, τ ~ U[−0.1, 0.9], start at ψ(1,·) = 0.5, ψ(0,·) = 0, B̄ = 1. Raising ψ(0,op) to 0.05 forces ψ(1,al) = ψ(1,op) = 0.25. Conduct margins fall, but expected coercive acts (the S of Prop 6.2) fall from 0.400 to 0.353. | Attach "volume rises" only to the conduct-blind case (Prop 6.2). Suggested abstract wording: "When capacity is limited, allegiance targeting weakens deterrence for at least one group; when opponents are targeted regardless of conduct, it also raises the volume of coercion against them." Make the same edit at L91 and L661. |
| M1 | major | Lemma decomposition fails dynamically | FIXED | Def 2.4 (L140 to 145) defines d via unilateral-deviation continuations W_i(h,v), which include own optimal future play (L148). The proof of Lemma 3.3 (L199) uses only τ + W(h,1) vs W(h,0). Re-checked: correct. | None. |
| M2 | major | Prop 3.6 (now 3.8) false at reachable nodes; not an equilibrium | PARTIAL | The state-dependent formula d = bΣ_{k=r+1}^{L}δ^k was added (L266 to 270), and the equilibrium claim was softened (L262, L277). **But** the proof (L274) assumes the agent never violates again ("cooperates from t+r+1 onward"). That contradicts the new Def 2.4, which includes i's own best-response future play. Under Lemma 3.3 the agent violates later whenever τ exceeds the margin it then faces, so the formula is only an upper bound, and it is strict whenever Pr(τ > d) > 0 at some reachable state. Value iteration with L=2, b=1, δ=0.9, τ~U[−1,3] gives exact d(0) = 1.27 vs formula 1.71, and d(1) = 0.37 vs formula 0.81 (the reviewer's bδ² case). Also, r = L is unreachable (after a violation at t−1, L−1 excluded periods remain at t), so the sentence at L277 that "the margin is smallest, and equal to zero" for an agent excluded for the full L periods describes no reachable node. | (1) Restate as an upper bound: "d(r) ≤ bΣ_{k=r+1}^{L}δ^k, with equality iff i complies at every later node (e.g. if Pr(τ > bδ^L) = 0)". Or give the exact recursion d(r) = δ[b·1{r=0} + U(max(r−1,0)) − U(L−1)], with U the agent's value function. (2) Add "d(r) > 0 for all reachable r ∈ {0,…,L−1}" (it holds whenever G(0) > 0). (3) Fix or delete the "equal to zero" sentence at L277. |
| M3 | major | Thm-to-Prop-A bridge unstated | PARTIAL | Ass 3.2 (Bridge, L184 to 189) now states the existential bridge, and L182 concedes that formal Ax5 is stronger than informal Ax5. L220 separates the threat from the implemented function and shows that they coincide when G has unbounded support. **Missing:** the paper never says which notion Proposition A for C asserts. Unbounded support (or on-path violations) is invoked conditionally but is not assumed anywhere. Thm 3.4 also needs agents to best-respond to temptation, which the bridge does not state for real collectives. | Add one sentence after Ass 3.2. Either: "Proposition A for C asserts the implemented function of Def 2.1; it follows from Thm 3.4 under Ass 3.2 together with (i) members best-respond to temptations and (ii) G has unbounded support, so violations occur on path." Or say that Proposition A asserts only a non-trivial sanction regime (a threat). |
| M4 | major | Falsifier immunized | PARTIAL | The requested fix is done. L314 commits to measuring p independently of sanction practices and *before* they are observed, via unobserved-opportunity designs, and adds a separate falsifier for the bridge. **Residual immunization through θ:** θ is defined by an unobservable counterfactual (L172) and is never measured or preregistered. Both falsifiers are written as "p > θ" and "p below θ". A defender facing measured p = 0.30, observed violations 0.05 and no sanctions can assert θ ≥ 0.30 and say the falsifier's premise fails. Yet Lemma 3.3 alone is contradicted by that observation, since zero margin implies a violation rate ≥ p. Also, "no … cost of any kind" cannot be certified in practice. | (1) Restate the necessity falsifier without θ: "measured p exceeds the observed violation frequency by more than sampling error, and violators' subsequent treatment (cooperation, exchange, standing) is no worse than that of matched compliers". This refutes Lemma 3.3 directly. (2) For the bridge falsifier, require θ to be preregistered per rule, with its measurement stated (e.g. the violation rate at which comparable collectives abandoned the rule). |
| M5 | major | Large-n F/I dependency asserted | PARTIAL | Prop 3.6 interpretation (L244): term (c) is acknowledged as community enforcement, and "this paper does not settle it by definition". New Cor 3.7 (L248 to 255) is conditional on costly public-good sanctions with no term (c). L257 handles bilateral exclusion with c_j ≤ 0. Parts I and VII are updated (see header). **Residual:** Objection 2 (L646) restates the result unconditionally: "as collectives grow, term (d) weakens and coercion must be provisioned or legitimated". It drops both the public-good condition and the term-(c) route. The abstract (L79), "costly coercion at scale depends on provisioning or on shared norms of punishment", also omits the term-(c) exception. | L646: "as collectives grow, term (d) weakens, and where sanctions are costly public goods and higher-order sanctions are absent (Cor 3.7), coercion must be provisioned or legitimated." Abstract: add "absent higher-order sanctions" or "when sanctions are costly public goods". |
| M6 | major | Control share undefined for nested command; H^C contradiction | FIXED | Def 2.2 (L120) adds recursive λ_ij attribution and a separate H^C_(1) below the apex. L123, L374 and L540 consistently say that H^C_(1) falls while H^C stays high. | None. |
| M7 | major | Dependency arcs conflated with C_mn | FIXED | New §2.3 (L159) separates dependency from integration. Weber is now "dependency of coercion on legitimation" (L123). Independent ulama are "evidence of low rather than high C_IC" (L410). Conscription is W→C (L161, L393, L562). The remaining C_mn uses (L329, L361, L376, L406, L419, L618) all describe co-command. | None. |
| M8 | major | HC9 not identified | FIXED | HC9 (L620) now requires the pattern among opponents with no change among matched supporters, and explains the crime-wave confound. | None. |
| M9 | major | Unequal standard of evidence | FIXED | L354 applies one standard and requires one episode or risk plus one check per type. Market: CIR 1915 with page cites (L365). Communist: Terror vs Getty (L378). Social democracy: Norway (Lund 1996, EOS) and Sweden (Dir. 1999:26, SOU 2002:87) (L391). Islamic: Mamluk and 1622 run through the capture-link test, with the Janissary claim cited to Tezcan (L404, L410). Catholic: a standing risk, with the reason stated (L423). Secular: Church (L432). | None for the item. A new chronology slip is listed as N3 below. |
| M10 | major | Rev 13:10 rests on one textual tradition; Thm misdescribed | FIXED | L637 acknowledges the crux, citing Jer 15:2, manuscript variation, Aune and Koester, and draws no inference. L635 now says Thm 3.4 requires a positive conduct margin, with the allegiance margin as the distinguishing property. | None. |
| M11 | major | Church quotation truncated | FIXED | L432 has the full clause "… or illegal acts on behalf of a hostile foreign power" with the pinpoint [Book II, Part I, Section C]. | Optional: add the page number as well (not verified here). |
| m1 | minor | Thm: μ̄, martingale, sharper bound | FIXED | Thm 3.4 (L204 to 216) is stated in expectation with liminf/limsup and the bound (p−θ)/p. L218 adds the martingale remark. Proof re-checked: correct. | Optional wording: in the proof, "the difference is zero when d ≤ 0" should read "non-positive". At L218, "converge to the same limits" overstates the martingale SLLN, which gives realized minus conditional frequency → 0 a.s.; "satisfy the same bounds a.s." is accurate. |
| m2 | minor | Prop 6.4 (now 6.5): Ψ→∞, w sum, "only K_t" | FIXED | Prop 6.5 (L548) uses the threshold lim Γ > w̄/(1−δ)+χ and Σδ^k w_{t+k}, and lists three escape clauses. L555 discusses success probability. Proof re-checked: correct. | None. |
| m3 | minor | Prop 6.3 (now 6.4): unused monotonicity; r mapping | FIXED | e(k) is "any function" (L531), L538 says the proof uses no property of e, and r is mapped to elite threat with a Powell-Thyne proxy and the mass-threat limit stated. Proof re-checked: correct. | None. |
| m4 | minor | HC1/HC4 "follow from" | FIXED | Both now read "motivated by", with the limits stated (L612, L615). | None. |
| m5 | minor | "Busier than before" unproved | FIXED | L523: "Total coercive activity may rise or fall." | None. |
| m6 | minor | Part II γ_S=0 hypothesis; integration vs contestability | FIXED | L136 restates the appointment-only hypothesis, its weakness for coercion (the IRGC), and the warning that component (1) is not C_PC. This is consistent with Part II Prop 6.5(a) to (c). | None. |
| m7 | minor | Notation collisions | PARTIAL | All listed collisions are resolved: s→μ, E→Δᶜ, A→Δᵃ, a→y, q→ψ, K_{i,t} removed, K_t→Z_t, Ψ→Γ, ς→d. **New collisions were introduced:** c is used for the Q^C component scores c_{k,t} (L127), the sanctioner cost c_j (L237) and the coup probability c(k) (L531). e is both the common conduct margin in Prop 6.1(ii) (L473) and the effectiveness loss e(k) (L531). r is both the remaining exclusion periods (Prop 3.8) and the threat parameter (Prop 6.4). | Rename c(k)→φ(k), e(k)→η(k), the Prop 6.1(ii) e→ē (or Δ̄), and the threat parameter r→ρ. Optionally rename c_{k,t}→q_{k,t} to match the source's contestability components. |
| m8 | minor | Part III prop number | FIXED | L161 and L244 cite Part III Prop 3.6. The judicial-power PDF confirms "Proposition 3.6 (Disjunctive dependency)". | None. |
| m9 | minor | Prop 3.5 (now 3.6): third parties; exhaustiveness | FIXED | Term (d) now includes third parties (L237), and L241 says "We take this decomposition as the definition of the private return." | None. |
| m10 | minor | Hobbes quotation | FIXED | L168: "covenants, without the sword, are but words". | None. |
| m11 | minor | Bibliography | FIXED | Bellin 139-157, Perlmutter 382-404, Woodburn 431-451 and Greif 525-548 are complete. "Reciprocity?" has no doubled period (L1035). Hedlund carries the note "Published online 2011; print issue 2013". Getty is cited against Conquest (L378). For Kamen, the unsupported word "contested" has been removed and the claim is now attributed ("Kamen's revisionist history argues", L421), which resolves the guardrail concern. | None. |
| m12 | minor | Equal depth | PARTIAL | Word counts, excluding citations and math: market 676, communist 703, social democracy 698, Islamic 814, Catholic 643, secular 584. The max/min ratio fell from 1.47 to 1.39, and social democracy is now mid-pack. Secular democracy is still the shortest, and its gap to the longest is unchanged (~230 words then and now) because the Islamic section grew. | Add ~100 words to §5.6 (e.g. a second documented check, or a non-US episode), or trim ~100 from §5.4. |
| m13 | minor | Outcome test: infra-marginality, captured reviewer | FIXED | L605 states both weaknesses and ties the second to Q^J (Part III). | None. |
| m14 | minor | Romans 13 anchor; Rev 17 | FIXED | Yoder anchors Romans 13 (L635). Rev 17:13 and 17:16 are read as a typological image for Prop 6.5 and labeled an interpretive claim (L639). | None. |
| m15 | minor | Capture language; HC→H map; HC10 threshold | FIXED | L480 to 482 call a positive allegiance margin a necessary ingredient of capture, but not capture without the three-part link. Every HC carries its parent H1 to H6. HC10 has a preregistered threshold (example 0.5). | None. |

## Series-rule flag (pillar independence)

Cor 3.7 is a statement about the F/I → C arc only, and the house rule permits it. Two sentences go further and claim that a form of coercion depends on **no other pillar**. That contradicts universal interdependence and Part VII's own encoding: the model's hyperarc W → C ("practitioners consume produced resources") applies to every pillar, and Part V's own §2.3 (L161) lists J → C and W → C.

| Line | Text | Required fix |
|---|---|---|
| L244 | "Term (d) needs no other pillar." | "Term (d) does not route the dependency through F or I." |
| L257 | "Then the premise c_j > 0 fails, and coercion of this kind depends on no other pillar." | "…and coercion of this kind does not need the F → C or I → C arc of Cor 3.7; it still depends on the other pillars through the arcs of §2.3 (for example W → C)." |

No other sentence claims independence. L159 ("Dependencies are present in every polity") and L574 ("cannot be assessed in isolation") are consistent with the series.

## New issues found during verification (not in the review)

| # | Sev | Issue | Fix |
|---|---|---|---|
| N1 | minor | Cor 3.5 (L224) says "right-continuous generalized inverse". The equivalence G(x) ≥ u ⇔ x ≥ G⁻¹(u) used in the proof holds for G⁻¹(u) = inf{x : G(x) ≥ u}, which is *left*-continuous in u. With the right-continuous inverse inf{x : G(x) > u}, the equivalence fails wherever G is flat at level 1−θ. | Define G⁻¹(u) := inf{x : G(x) ≥ u} explicitly and drop "right-continuous". |
| N2 | minor | §8 now leans on Prop 6.3. The capacity function Σ(ψ) (L508) charges κ₁ψ(1,y) on the whole group mass n_y, not on the mass of violators. The paper declares this an assumption (L654), so this is acceptable as is. | Optional: one clause saying Σ prices *maintaining* a targeting probability over the group, not acts delivered. |
| N3 | minor | L391 calls the EOS Committee, "established under a separate law of 1995", "the response" to the Lund report of 1996. A 1995 law cannot respond to a 1996 report. | "A parallel response to the revelations that led to the inquiry was a parliamentary oversight committee …", or similar. |

## Open items

7 review items open (C2, M2, M3, M4, M5, m7, m12), plus 1 series-rule flag (L244/L257) and 2 required new minor fixes (N1, N3). N2 is optional.

SUMMARY: critical 1/2 fixed, major 6/11 fixed, minor 13/15 fixed; open: 10

## ROUND 2 SPOT-CHECK (2026-10-22; .tex 12:34, PDF 12:35, no `??`)

### Prop 3.8 two-sided bound: correct, with one missing hypothesis

| Check | Result |
|---|---|
| Coupling | Correct. With identical future actions, the paths agree from the period after the first later violation s onward, because the violation at s excludes s+1..s+L in both branches and s+L > t+L. Before that they differ only in periods t+r+1..min(t+L, s), where the complier gets b. Period s itself is in the interval, because a violation affects exclusion only from s+1. So the difference is bΣ_{k=r+1}^{min(L,s−t)} δ^k, as stated. |
| Upper bound | Correct. Copying the complier's optimal actions into the violating branch gives a feasible but suboptimal payoff ≤ W(h,1), so d ≤ E[bΣ…] ≤ bΣ_{k=r+1}^{L} δ^k. Equality holds under compliance at every later node. |
| Lower bound | Correct. Copying the violator's optimal actions into the complying branch gives ≤ W(h,0), so d ≥ E[bΣ…] ≥ 0 at every reachable node. With d ≥ 0, a draw τ<0 implies strict compliance. Independence across periods then gives Pr(s > t+r+1) ≥ Pr(τ<0)^{r+1}, and r+1 ≤ L keeps the term bδ^{r+1} in the sum. |
| Missing hypothesis (required) | Both steps compare against the agent's **optimal** continuation ("optimal future actions"), but the statement never says the agent best-responds. Def 2.4 evaluates W under σ_i, and if σ_i is not optimal, "W(h,1) ≥ payoff of the copied strategy" fails. **Fix:** add to the statement "and each agent best-responds in its compliance decision (as in Lemma 3.3)". |
| Sharper lower bound (optional) | Only the r draws in t+1..t+r need to be negative: s ≥ t+r+1 already keeps k=r+1 in the sum. So d(r) ≥ bδ^{r+1}Pr(τ<0)^{r}, which gives d(0) ≥ bδ with no probability factor. The stated bound is valid as written. |

### Numerical check (value iteration, exact best-response margins)

| Case | Lower bound | Exact d | Upper bound | Inside? |
|---|---|---|---|---|
| L=2, b=1, δ=.9, τ~U[−1,3], r=0 | 0.225 | 1.268 | 1.71 | yes |
| same, r=1 | 0.051 | 0.368 | 0.81 | yes |
| 300 random cases (L 1 to 5, random b, δ, uniform support) | | | | 0 failures |

### Other round-1 fixes

| Item | Status | Evidence |
|---|---|---|
| C2 | FIXED | Abstract (L75), intro (L87) and conclusion (L662) all read "When capacity is limited, allegiance targeting weakens deterrence for at least one group; when opponents are targeted regardless of conduct, it also raises the volume of coercion against them." |
| M3 | FIXED | L186: Proposition A for C "asserts the implemented function of Def 2.1". It follows under the bridge, best response and unbounded support of G. |
| M4 | FIXED | L313: the necessity falsifier no longer uses θ (measured p exceeds the observed violation frequency beyond sampling error, and violators are treated no worse than matched compliers). The bridge falsifier requires θ to be preregistered per rule. |
| M5 | FIXED | Abstract (L75) and Objection 2 (L647) are now conditional on costly public-good sanctions with no higher-order sanctions. |
| Series rule | FIXED | L241: "Term (d) does not route the dependency through F or I." L254: "...does not need the F→C or I→C arc of Cor 3.7; it still depends on the other pillars through the arcs of §2.3, for example W→C." No "no other pillar" wording remains. |
| N3 | FIXED | L390: "A parallel response to the revelations that led to the inquiry..." |

ROUND 2: one required clause (best-response hypothesis in Prop 3.8); everything else spot-checked is OK.
