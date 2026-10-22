---
reviewer: proof-check (Claude, read-only on the paper)
paper: papers/latex/formalized-state.tex (Part VII), numbering from formalized-state.pdf / .aux
date: 2026-10-22
inputs: reviews/formalized-state-review.md (Gemini round 1), model/beast_system (pytest: 324 passed), papers/pdf/*.pdf
note: CORRECTION. team/notation.md does exist (8.5 KB). Round 1 wrongly reported it missing and took notation from the paper and model/beast_system/pillars.py instead
---

# Part VII fix verification

**Bottom line.**
- The core mathematics is sound: forcing, the hub bounds, the U range, closure and reversibility, Perron, every witness pair, the terminal-object argument, and the claim that "c is P-preserving iff c is a bijection".
- **One WRONG item.** The second sentence of Thm 7.8 (it uses the undefined term "dimensions are unions") is false under a natural reading.
- **Thirteen GAPs.** Six are major (the sixth, the free-exit carve-out vs the Ju/'hoansi, is in Section 2b):
  - Thm 7.4(b) and every result that depends on it omit a hypothesis.
  - The new compliance clause does not make ℓ an output of the legitimation function.
  - Prop 4.4(a) does not verify the new entrant clause of Ax4\*.
  - Lemma 6.5 is false as literally stated.
  - The Thm 7.8 sentence above.
- The Gemini fixes (the actor set in the 7.5(a) witness, the surjectivity wording, the smallness of 𝒢\*, and the Ax3\*/Ax4\* alignment) are in place. The Ax3\*/Ax4\* strengthening opened the new items below.

Closure and reversibility are now **Theorem 8.5** (Section 8). The surrounding results are Def 8.4, Cor 8.6, Prop 8.7 and Remark 8.8.

## 1. Results

| Result | Status | Evidence or counterexample | Required fix |
|---|---|---|---|
| Lemma 4.1 Forcing | FIXED-OK | (a) Pr(S_n) ≤ (1−κ)Pr(S_{n−1}) by conditioning at the n-th unsolved disposition, a stopping time, and Π∩{N≥n} ⊆ S_n. (b) The unsolved count is eventually constant on Π, so solved/k → 1. | none |
| Lemma 4.2 Pillar necessity | GAP (minor) | F, J, I and W are fine. Part I Prop 3.3(b) matches the e^{−pT/8} bound, and Borel-Cantelli applies. **C:** Part V Thm 3.4 needs "a rule in force under a best-response profile", and Table 1's Ax5\* does not contain best response; Part V itself lists it as a further condition (p. 6). **J:** the proof says "Ax3\* *is* Assumptions 3.1 and 3.2 of Part III", but Ax3\* now adds Prop 3.6's clause and drops 3.1's "each reaches a disposition at some finite time", which Lemma 4.1's indexing needs. | Fix F2 and fix F3 (Table 1). In the proof, change "Ax3\* is" to "Ax3\* contains". |
| Thm 4.3 Structural necessity | GAP (minor, ordering) | The proof is complete given Lemma 5.4. That lemma comes later (it is not circular: 5.4 uses Lemma 4.2, not 4.3), so criterion (c) fails. | F12 |
| Prop 4.4 Consistency and independence | GAP (major) | (a) The strengthened Ax4\* requires that "entrants are parties to conflicts over goods in infinitely many periods". The model never says which member is replaced or who claims the plot. If the same slot is always replaced and members 1 and 2 always claim the plot, entrants never enter a conflict, so the clause fails. That in turn breaks Prop 5.10(a), which needs Struct here. The non-innateness and no-forgetting clauses are also not stated. (b) The six modifications are correct: each kills exactly Ax_k\* and Impl_{m_k} with no hazard triggered, once (a) is fixed. | F4 |
| Lemma 4.5 Minimal form | FIXED-OK | H = n(1/n)² = 1/n; U ≤ (1−q̄)/n because Σω = 1; κ_m(N) = 1 gives C = 1 and 𝓘 = 1. | none |
| Lemma 5.4 Derived dependencies | GAP (major) | **(i) Hyperarc ({I,C},J).** Ax3\* only says that ℓ is "the value it places on the procedure's legitimacy". Nothing says that ℓ = 0 when the legitimation function withholds its output, and Part III Prop 3.6 includes "reputation" in ℓ. So "withholding I and C ⇒ ℓ = σ = 0" is assumed, not derived. **(ii) Arcs W→m.** The argument "the stock is exhausted after X₀/k periods" is the persistence route that Remark 5.3 excludes, unless consumption is an input to each practice instance. The text never states that premise. **(iii) "Need not contain I→J or C→J".** No collective satisfying the hypotheses is exhibited. In the Prop 4.4(a) model, σ = 0, so I→J *is* present there. | F1, F3, F3b |
| Thm 5.9 Interdependence | GAP (minor) | The arcs, strong connectivity, cascade completeness and monotonicity are all correct (re-derived by hand and with `necessity.cascade_closure`). **P→F** cites Part II Lemma 3.5, whose hypothesis (Part II Assumption 3.3(ii), R_t ∈ V(e_t)) is not among Part VII's axioms. The needed step, that the new conflicts are in fact settled, comes from Lemma 4.2 and is not cited. **C→F** uses Part V Lemma 3.3 (best response), which inherits the Ax5\* issue. | F11, F2 |
| Prop 5.10 Role of each premise | GAP (minor) | (b) to (e) are verified by hand and by the model. D\* minus C→F is strongly connected with cl({C}) = {C}. J→P in place of J→F leaves the structure strongly connected and cascade-complete. Replacing the hyperarc by two arcs gives cl({C}) = M. **(a)** inherits the Prop 4.4(a) gap. "Foraging uses ... no output of any other function" is asserted, yet the model attaches a fine to "a rule of joint work" and a P-decision to the campsite. Neither is shown to be irrelevant to foraging, so C→W or P→W may hold. | F4 (second half) |
| Lemma 6.2 Hub bounds | FIXED-OK | (a) Σdeg = 2Σ_{m<n}C. (b) k(6−k)+k(k−1)/2 pairs; k = 1 gives c̄/3. (c) gives c·k(k−1)/30, and 2c/3 for k = 5. In 2,000 random draws, max(𝓘 − bound) = 0. | none |
| Lemma 6.4 Range of U | FIXED-OK | U is a convex combination of terms in [0,1]. Every probability vector has H ≥ 1/n > 0, which gives (b). | none |
| Lemma 6.5 Separation | GAP (major) | False as literally stated ("None refers to which agent performs a practice"). Three clauses depend on Λ: Impl_J's "procedure that neither party controls [alone]" (Part III Def 2.3); Ax2\*'s self-government clause and Impl_P's "practice of the members"; and Thm 4.3's practice-consumption condition. Counterexample: take Γ of Thm 6.6 and let Λ assign every determination to one party of each dispute. Impl_J fails, although Γ is unchanged. | F5 |
| Thm 6.6 A does not imply B | GAP (major) | All four corner values are correct by hand: (0,0) H = 1/2, U = 0, 𝓘 = 0; (0,1) U = 0, 𝓘 = 1; (1,0) U = 1, 𝓘 = 0; (1,1) U = 1, 𝓘 = 1 with one link. The model's `corner_polities` gives the same four (U, 𝓘) pairs. The threshold argument is correct. Two gaps: (i) the statement says "satisfying Ax1\*–Ax6\* and X1–X5, and hence Struct and Inter", but "hence" also needs Thm 4.3's practice-consumption hypothesis; (ii) the proof relies on Lemma 6.5 "under any assignment Λ", although Γ fixes the procedures ("majority vote", "lot drawn by the third"), which the corners reassign. | F1, F5 |
| Lemma 7.3 Preserved and forgotten | FIXED-OK | Each preserved quantity is a function of transported components. | none |
| Thm 7.4 Representation | GAP (major) | **(b) and (c) omit Thm 4.3's hypothesis** that "every practice of every pillar is performed by agents whose consumption is counted in Ax6\*". Without it, Thm 4.3 and Lemma 5.4 do not give D₀, so π(G) need not satisfy (F4). The same omission sits in the definition of 𝒢\* (Sec 7.3), and therefore in Thm 7.7(a) ("π(G) ∈ 𝓕 for every G ∈ 𝒢\*"). **(a)** asserts (F2) and (F3) from properties the paper never states: share rules return probability vectors supported on performers, constraints run only from performers, and weights lie on the simplex. The model enforces these as `CodedRecord` well-formedness ("On this domain F2 and F3 hold"); the paper does not. "Let G ∈ 𝒢" also lacks "with a coded record". | F1, F6 |
| Prop 7.5 Minimality | GAP (minor, edge case) | The witnesses are verified for **all 877 coarsenings** M → K∪{⊥} up to relabelling of K, with random λ (876 non-bijections; 0 failures), using both the model's construction and a paper-faithful one. Edge case: when every pillar is dropped (K = ∅), proof (a) needs "l₀ with c(l₀) ∈ K", and no such l₀ exists. The witness still exists. | F9 |
| Thm 7.7 Uniqueness | GAP (minor, definitional) | The direction is right: terminal = coarsest, since every P-preserving α has h∘α = Φ, so α's partition refines Φ's. h is well defined because α is P-preserving and unique because α is surjective. (c) is the standard unique-terminal argument, and (d) holds via β′∘β⁻¹. The scope sentence is in the statement ("Relative to the axioms ... and the preserved property set P"). The gap: (a) uses "G ≅_A G′", but Def 7.2 defines ≅_A only between G ∈ 𝒢 and F ∈ 𝓕. (a) also inherits the Thm 7.4(b) hypothesis gap. | F8, F1 |
| Thm 7.8 Six dimensions | **WRONG (sentence 2, as worded)** | **Sentence 1 ("Φ_c is P-preserving iff c is a bijection") is correct for all coarsenings, not only the exhibited ones.** Prop 7.5's witnesses are parameterized by any dropped m, or any merged pair (m,n) with μ = λ_m/(λ_m+λ_n), and the check above covers all 876 non-bijections. Bijections rename labels (0 mismatches on fixtures). **Sentence 2**, "Every P-preserving abstraction whose dimensions are unions of the six ... classes therefore has exactly six dimensions", uses an undefined notion. Counterexample: the abstraction with five blocks {F},{PJ},{I},{C},{W}, in which block PJ stores the pair (s^P, s^J, Q_P, Q_J, κ_P, κ_J, A^P, A^J) rather than λ-sums. Its dimensions are unions of classes, it is P-preserving (it is Φ relabelled), and it has five dimensions. Remark 7.9 repeats the phrase. | F7 |
| Thm 8.5 Closure and reversibility | FIXED-OK | (a) y_{n,t+1} ≤ 1 − δ_n y ≤ 1. (b) y_t ≤ Aᵗy₀ plus Gelfand. (c) 10/15. (d) and (e) by spectral monotonicity. (f) The bound V_{t+1} ≥ ρV_t − cV_t² is checked line by line, and the induction on μ = min{V₀, (1−maxδ)ε} is correct. A stress test on 2,385 random irreducible K with ρ(A) > 1 over 400 steps found 0 violations. | none |
| Cor 8.6 Oligarchy and replacement | GAP (minor) | The last sentence's proof shows only that the *sufficient* condition ρ(A) < 1 fails. It does not show that reversibility fails. | F10 |
| Prop 8.7 Common mode | FIXED-OK | Irreducible ⇔ strongly connected; a positive diagonal entry gives a primitive matrix, so (B/ρ)ᵗ → uwᵀ. | none |
| Remark 8.8 (label `prop:signremark`) | FIXED-OK | Numerically, ρ = 1.0500 and 0.98362 (= √0.9675). | cosmetic: rename the label to `rem:` |
| Prop 10.1 Witnesses | FIXED-OK | All 7 pairs are verified by hand and with the model (both constructions): V_{G1} = V_{G2}, the encodings are equal, and P differs. See the table below. Easton's 4-pillar block with λ = 1/4 gives μ = 1/2. | none |
| Thm 10.2 Novelty | FIXED-OK | Follows from 10.1: an abstraction isomorphic to Φ has Φ's partition and is therefore P-preserving. | none |
| Scope item: free-exit carve-out vs the Ju/'hoansi (Sec 3 l.173, Table 2, l.287, l.469, Sec 12 l.978) | GAP (major) | See Section 2b. The Ju/'hoansi (Woodburn's !Kung; Part I p.7 lists them as immediate-return) are outside the current *derivation* of J, because Ax3\*'s hazard clause is not established for them. Part III Table 1 says "Exit by moving camp resolves many disputes with no third party at all", and Part III Sec 3.3 names them as close to the Prop 3.4 counterexample. The paper nonetheless uses them as instances of the theorem: l.252 says the prediction "has a formal core"; l.287 says "which is what Proposition A requires"; l.469 lists derived arcs J→F and W→m among the Ju/'hoansi. Sec 12 narrows the claim "to collectives in which exit carries a cost", which contradicts the unqualified universality in the abstract, Thm 4.3, Thm 7.4(c) and Sec 13. | G-J1 (preferred) + G-J2; G-J3 only if G-J1 is rejected |

Definitions (not counted): Def 5.1 uses "the instances that the practices of m solve" for every m, but defines instances only for F (conflicts) and J (residual disputes). Add one line per pillar: P = collective decisions; I = entrants in a window; C = agent-periods under the rule; W = periods of production. This feeds Lemma 5.4 and Thm 5.9.

## 2. True-by-definition audit (Ax3\*, Ax4\* strengthening)

| Question | Finding |
|---|---|
| Does Struct follow trivially? | **No for Impl.** Prop 4.4(b) still exhibits persistent collectives lacking each function (valid once F4 is applied). **D₀ is now one step from the premises.** The arc I→F is the conjunction of three Ax4\* clauses (settlement procedures belong to the CK rule system; entrants are parties to conflicts infinitely often; entrants learn only through I) with Part I Def 2.2(b). That is an incidence axiom ("X4") folded into Ax4\*. The hyperarc ({I,C},J) is Part III Prop 3.6's hypothesis copied into Ax3\*. Neither is a tautology; each can fail. But the paper still says otherwise: line 365 reads "The six axioms ... constrain each function separately; they do not say that the problems arise about the same objects". That is now false, and no falsifier is stated for the new clauses. |
| Smuggled conclusion? | The one place a conclusion is assumed rather than derived is ℓ ≡ output of I (Lemma 5.4(i)). Fix F3 makes it an explicit premise with a falsifier. |
| Minimal forms | The paper makes no formal claim that the Nuer, the Ju/'hoansi or the commons satisfy Ax3\*/Ax4\*. Its line 469 attributions fit the new clauses: the arrow-owner rule is learned in public talk (I→F); Nuer compliance rests on value placed on the settlement plus fear of feud (ℓ, σ); commons "rules known to users". All are qualitative. The model codes the hard cases with `EXTENDED_AXIOMS` "as holding" (necessity.py, around line 535: "QUALITATIVE readings"). The Ju/'hoansi Ax3\* hazard is conceded weak in Sec 12. No evidence is cited that *entrants specifically* are parties to conflicts. Status: consistent and unverified. |
| Independence models (Prop 4.4) | Each still shows that its axiom is needed for its Impl. None shows that the new clauses are needed for D₀, and the paper does not claim this. Optional: add a Prop 5.10 item with entrants never party to conflicts (only lineage heads claim), so that I→F is absent. |

## 2b. Free-exit carve-out vs the Ju/'hoansi

**Verdict: neither (a) nor (b) as posed.**

| Question | Finding |
|---|---|
| Do the Ju/'hoansi satisfy the strengthened Ax3\*/Ax4\*? | Ax4\*: plausibly yes. The arrow-owner and sharing rules are learned in public talk, and entrants (by birth or marriage) are parties to sharing conflicts. All of this is qualitative. **Ax3\* (hazard clause): not established, and the series' own sources point the other way.** If the unit is the camp, moving away is exit at near-zero cost (Part III Table 1 and Sec 3.3; Part V p.~556 "Disputes are often resolved by moving away"). If the unit is the camp network (Part I p.7), moving between camps is not exit. By Part III Def 2.3 it is then *abandonment*, and the ethnography gives no evidence that abandonment carries a hazard κ > 0 for the network. Either way, the premise of Lemma 4.2's J step fails or is unverified. The compliance clause holds, but Part III Table 1 grounds it in "ridicule, gossip and the value of continued sharing relations". That is σ plus a relational value, not a legitimation output, which reinforces fix F3. |
| Do they have J? | **Yes, as an observation.** Impl_J needs only infinitely many determinations a.s. on Π, not a hazard. Lee (2013) and Wiessner (2005) record public talk-outs in which neither party controls the outcome alone and both act on it. So the Table 2 cell is ethnographically supported (thin, not absent). |
| So which is it? | The Ju/'hoansi lie **outside the theorem** (premise unverified) **but inside the conclusion** (J observed). Calling them minimal-form instances is fine as observation. It is **wrong as framed**: l.252 says "formal core", l.287 says "what Proposition A requires", and l.469 lists derived arcs, J→F among them. X3 itself is "subject to the hazard of Ax3\*", so J→F is not derived for them either. Sec 3 (l.173) already states the correct rule ("the presence of the function rests on the ethnographic record alone"), but the paper never applies it to the Ju/'hoansi. |
| Does the carve-out leave a governance system without J? | **Yes, under Def 2.1 as written, and the paper builds one itself.** Prop 4.4(b), k = 3, is a 3-member collective that functions at every date with probability one, abandons every residual dispute, and has no J. Part III Prop 3.4 (a regional population of bands with free exit) is another. So "Struct(G) for every G ∈ 𝒢" (Def 2.3) is false as mathematics. It is true only under the bridge hypothesis that every functioning *human* collective satisfies Ax3\*. **Sec 12's concession for immediate-return foragers is a concession that this bridge fails for a real class of collectives.** As a result, Thm 4.3's last sentence and Thm 7.4(c) rest on an antecedent that the paper itself doubts. The universality of J then holds for those collectives only by ethnography. No *documented* real collective without J is exhibited: the ethnographies record talk-based determinations. So universality is unproved for that class, not refuted. Def 2.1 also leaves the unit open (camp vs network vs region), so the same population can be coded inside or outside the hazard clause. |

**Fix G-J1 (preferred; narrows the carve-out and restores universality as a theorem-plus-bridge).** Weaken Ax3\* so that it needs only an inescapable subsequence of disputes. Then apply the forcing lemma to that subsequence.
- Table 1, Ax3\* row: replace the opening clause with "On the persistence event infinitely many residual disputes arise that a move to another group of the collective does not escape (disputes among co-resident kin, or over rights to territory, water or sharing that follow the parties wherever they move); each reaches a disposition at a finite time; and for these disputes a disposition by self-help, exit or abandonment ends functioning with conditional probability at least $\kappa>0$".
- Lemma 4.2, J step: replace the sentence beginning "$\pJ$: Ax3$^{*}$ is Assumptions 3.1 and 3.2 of Part III" with "$\pJ$: \cref{lem:formalized-state:forcing}(b), applied to the inescapable residual disputes of Ax3$^{*}$ with determination as solution, gives infinitely many determinations almost surely on $\Pi$; Theorem 3.3 of Part III is the case in which every residual dispute is inescapable."
- Sec 12, l.978: replace "but the claim is narrowed to collectives in which exit carries a cost" with "and the claim is narrowed to collectives in which some recurring class of residual disputes cannot be escaped by moving; a collective in which every residual dispute can be escaped at no cost falls outside the derivation, and Proposition 3.4 of Part III shows that such a collective can persist without determination."
- Sec 3, l.173: replace "collectives in which exit is free" with "collectives in which every residual dispute can be escaped by free exit".
- Table 3, J falsifier: replace "A persistent collective with costly exit whose residual disputes are always settled by force or left open" with "A persistent collective in which disputes that a move does not escape recur and are always settled by force or left open".
- Under G-J1 the Ju/'hoansi satisfy the revised Ax3\* *if* inescapable disputes (n!ore access, marital and sharing disputes among kin) recur with a hazard. That is an ethnographic coding claim, which the paper must state as such, citing Lee (2013) and Wiessner (2005).

**Fix G-J2 (unit of analysis; needed with either option).** Def 2.1: after "A *collective* $G$ is" insert "the largest group whose members make collective decisions as one body, so that a member's move between subgroups of $G$ is not exit from $G$; formally, $G$ is". Thm 4.3 / Thm 7.4(c): add the sentence "The bridge hypothesis is not established for collectives in which every residual dispute can be escaped at no cost (\cref{sec:objections})."

**Fix G-J3 (only if G-J1 is rejected; corrects the example instead).**
- Table 2 caption: append "For the Ju/'hoansi and other immediate-return foragers, exit is close to costless and the hazard clause of Ax3$^{*}$ is not established, so their $\pJ$ cell, and every arc into or out of $\pJ$ attributed to them in \cref{sec:dependency}, is an ethnographic observation, not an instance of \cref{thm:formalized-state:A,thm:formalized-state:interdependence}."
- l.287: change "which is what Proposition A requires" to "which is what Proposition A predicts".
- l.469: change "disputes over sharing are talked out ($\pJ\to\pF$)" to "disputes over sharing are talked out, an observed instance of $\pJ\to\pF$ outside the derivation".
- Abstract and Sec 13: change "every governance system" to "every governance system that satisfies the axioms, which excludes collectives whose every dispute can be escaped by free exit".

## 3. Cross-Part citations (papers/pdf)

All checked citations match the sibling PDFs:
- **Part I:** Def 2.1, Def 2.2(b)(c), Prop 3.3(b), Sec 3, Sec 5, Def 6.1.
- **Part II:** Def 2.2(a), Def 2.3, Def 2.4/Sec 2, Asm 3.2, Lemma 3.4, Lemma 3.5, Def 3.6, Thm 3.7, Sec 3, Sec 5, Sec 6 Eq. (2), Asm 6.1, Prop 6.2(a)(b), Prop 6.5.
- **Part III:** Defs 2.1–2.3, Asm 3.1–3.2, Thm 3.3, Props 3.4–3.6, Sec 2, Sec 5 (Caperton, Langborger, Maupeou, Argentina 1990).
- **Part IV:** Defs 2.1–2.2, Lemma 3.4, Thm 3.5, Sec 3, Sec 5.
- **Part V:** Def 2.2, Asm 3.1–3.2, Lemma 3.3, Thm 3.4, Prop 3.6, Cor 3.7 (including the bilateral-exclusion exception), Sec 5 (Senate 1975–76, terror of the late 1930s).
- **Part VI:** Lemmas 3.3–3.4, Prop 3.6.

Content mismatches (no numbering errors):

1. Def 2.2(iii) "a procedure that neither party controls". Part III Def 2.3 says "controls **alone**".
2. The Table 1 Ax3\* row omits Part III Asm 3.1's "each reaches a disposition at some finite time", and its compliance clause drops Part III's "including internalized obligation and reputation" (see F3).
3. The Table 1 Ax5\* row omits the best-response profile that Part V Thm 3.4 and Lemma 3.3 require (F2).

## 4. Witness pairs

Hand formulas: drop m gives H_m = 1 vs 1/2. Merge (m,n) at μ gives C^ov_mn = 0 vs max(μ, 1−μ), H = 1 vs μ²+(1−μ)², and Δ𝓘 = max(μ, 1−μ)/15 ≥ 1/30.

"Model" means `uniqueness.witness_coarsening` / `witness_pair`: a and b perform every pillar, with (1/2,1/2) elsewhere. "Paper" is a construction built to the text: a and b only in the named pillars (plus l₀), every other pillar held by its own organization. Both were run. V = V_{G1} = V_{G2}; Img = coarse images equal up to actor relabelling (`p_equal`); P≠ = `not p_equal(Φ(G1), Φ(G2))`.

| Pair | Construction | V | Img | P-values G1 vs G2 (hand = model) | OK |
|---|---|---|---|---|---|
| drop F | s^F = (1,0) vs (1/2,1/2); l₀ equal | Y | Y | H_F 1 vs 0.5 | Y |
| drop P | same, with m = P | Y | Y | H_P 1 vs 0.5 | Y |
| drop J | same, with m = J | Y | Y | H_J 1 vs 0.5 | Y |
| drop I | same, with m = I | Y | Y | H_I 1 vs 0.5 | Y |
| drop C | same, with m = C | Y | Y | H_C 1 vs 0.5 | Y |
| drop W | same, with m = W | Y | Y | H_W 1 vs 0.5 | Y |
| merge FP, FJ, FI, FC, FW | (1,0)/(0,1) vs (μ, 1−μ) twice; μ = 1/2 and random λ | Y | Y | C 0 vs 0.5 (random μ: 0 vs max(μ, 1−μ)), H 1 vs 0.5, Δ𝓘 = 1/30 | Y (5/5) |
| merge PJ, PI, PC, PW | same | Y | Y | same | Y (4/4) |
| merge JI, JC, JW | same | Y | Y | same | Y (3/3) |
| merge IC, IW, CW | same | Y | Y | same | Y (3/3) |
| Parsons | merge F,W, μ = 1/2 | Y | Y | H_F, H_W 1 vs 0.5; C_FW 0 vs 0.5 | Y |
| Mann | merge P,J, μ = 1/2 | Y | Y | H_P, H_J 1 vs 0.5; C_PJ 0 vs 0.5 | Y |
| Easton | merge P,J inside the 4-block, λ = 1/4 | Y | Y | H_P, H_J 1 vs 0.5; C_PJ 0 vs 0.5 | Y |
| Luhmann | merge F,W, μ = 1/2 | Y | Y | H_F, H_W 1 vs 0.5 | Y |
| Almond | drop F, l₀ = P | Y | Y | H_F 1 vs 0.5 | Y |
| Aristotle | J (1,0) vs (1/2,1/2); a,b equal in I; same P layer; L = ∅ | Y | Y (('one','correct') both) | H_J 1 vs 0.5 | Y |
| Weber | C (1,0) vs (1/2,1/2); a,b equal in I; both legal-rational with staff | Y | Y | H_C 1 vs 0.5 | Y |

Corners of Thm 6.6 (not pairs): (0,0), (0,1), (1,0), (1,1) recomputed by hand and with `capture.corner_polities()`. U and 𝓘 match, and only (1,1) has a link.

Script: `/private/tmp/claude-501/-Users-mlong-Documents-Development-the-beast-system/53a4f9b6-b8c1-4df4-96d8-300f973de288/scratchpad/verify_witnesses.py`. It checks 86 constructions: 28 paper pairs × the model and paper constructions, plus 15 merges at random λ in both. It also checks all 877 coarsenings, 2,385 cases of Thm 8.5(f) and 2,000 cases of Lemma 6.2(b), with 0 failures.

## 5. Exact fixes

- **F1 (practice condition; fixes Thm 7.4(b),(c), Thm 6.6, 𝒢\*, Thm 7.7(a), Lemma 5.4(ii)).**
  - Table 1, Ax6\* row: replace the content with: "The collective and its institutions consume at least $k>0$ per period from a finite initial stock; inflows are produced by some agent's productive activity; and every practice of every pillar is performed by agents whose consumption is counted here, in a period only if that consumption is met".
  - Thm 4.3: delete "and suppose that every practice of every pillar is performed by agents whose consumption is counted in Ax6$^{*}$".
  - Thm 4.3 proof: replace "Ax6$^{*}$, and the stated condition on practices" with "and Ax6$^{*}$ with its clause on practices".
  - Lemma 5.4 proof: begin with "By the last clause of Ax6$^{*}$, every practice is performed only when its performers' consumption is met."
- **F2 (best response).** Table 1, Ax5\* row: append ", and members best-respond to the sanction regime in force (Lemma 3.3 of Part V)".
- **F3 (Ax3\* clauses).** Table 1, Ax3\* row:
  - Change the opening to "On the persistence event infinitely many residual disputes arise and each reaches a disposition at a finite time".
  - Append: "here $\ell>0$ only if some practice of the legitimation class (Definition 2.1 of Part IV) has led the party to regard the procedure as rightful, and $\sigma>0$ only if some agent's practice answers defiance with a sanction".
  - Lemma 5.4, Interpretation: replace "With $\ell=\sigma=0$ no determination is effective" with "If legitimation and sanction both withhold their outputs, then $\ell=\sigma=0$ by Ax3$^{*}$ and no determination is effective".
  - Lemma 4.2 proof: change "Ax3$^{*}$ is Assumptions 3.1 and 3.2" to "Ax3$^{*}$ contains Assumptions 3.1 and 3.2".
- **F3b ("need not contain").** Lemma 5.4, end of Interpretation: replace the last sentence with "In the collective of \cref{prop:formalized-state:independence}(a) with the fine $d\ge g$ also attached to defiance of a determination, each determination is effective with either output alone, so neither $\pI\to\pJ$ nor $\pC\to\pJ$ belongs to $\mathcal{D}(G)$."
- **F4 (Prop 4.4(a) and Prop 5.10(a)).**
  - After "replaced by an entrant every $L$ periods" insert: "; the member replaced is always the longest-serving one, an entrant does not know the rule system at entry and no member forgets what it learns, and the plot is claimed in each period by the most recent entrant and one other member, so entrants are parties to conflicts over goods in every period".
  - Replace "a rule of joint work" with "a rule of camp chores".
  - Append "each member forages alone, at any campsite".
  - Prop 5.10(a) proof: "Foraging is individual, does not depend on the campsite chosen, uses no contested input and is not governed by the rule of camp chores, so no instance of $\pW$ uses an output of another function."
- **F5 (Lemma 6.5 and Thm 6.6).**
  - Lemma 6.5: after "the record of evidence on capture links." insert: "Call $\Lambda$ admissible if every agent it assigns to a practice is a member, or an organization of members, whose consumption is counted in Ax6$^{*}$; no party to a residual dispute alone controls its determination; and the practices of rule making are the members' own."
  - Lemma 6.5: change "are functions of $\Gamma$ alone" to "are, for admissible $\Lambda$, functions of $\Gamma$ alone".
  - Lemma 6.5 proof: add "Admissibility fixes the only clauses that mention performers: the party-control clause of $\Impl_{\pJ}$, the self-government clause of Ax2$^{*}$ and the practice clause of Ax6$^{*}$."
  - Thm 6.6 proof: change "under any assignment" to "under any admissible assignment". After "Four assignments give the corners." add: "In each corner the organizations consist of members, every determination is made by an organization that contains neither party (in $(0,1)$ by all members, so neither party controls it alone), and the procedures are those of $\Gamma$ with performers relabeled, so each assignment is admissible."
- **F6 (Thm 7.4(a)).**
  - Def 7.2: append "The record is well formed: each share rule returns a probability vector supported on the actors who perform practices of $m$, a constraint $(i,j,m)$ is recorded only if $i$ performs a practice of $m$, and the weights are nonnegative and sum to one."
  - Thm 7.4: change "Let $G\in\mathcal{G}$." to "Let $G\in\mathcal{G}$ come with a well-formed coded record."
- **F7 (Thm 7.8 WRONG).**
  - Replace "Every $P$-preserving abstraction whose dimensions are unions of the six axiom-derived problem classes therefore has exactly six dimensions" with "Every $P$-preserving coarsening $\Phi_c$ therefore has exactly $|K|=6$ dimensions".
  - Remark 7.9: replace "concerns abstractions built from the six axiom-derived problem classes" with "concerns coarsenings, whose blocks aggregate pillar data with the weights $\lambda$; an abstraction that groups pillars but keeps each pillar's components separately is $\Phi$ relabeled and is not a coarsening".
- **F8 (Thm 7.7(a)).** Def 7.2, last sentence: append "For $G,G'\in\mathcal{G}$ write $G\cong_AG'$ if a bijection $V_G\to V_{G'}$ carries $\pi(G)$ to $\pi(G')$."
- **F9 (Prop 7.5 edge case).** Proof (a):
  - Change "one pillar $l_0$ with $c(l_0)\in K$" to "one pillar $l_0\neq m$, with $c(l_0)\in K$ when $K\neq\emptyset$".
  - Add: "If $K=\emptyset$, both images consist of the actor set alone and coincide."
- **F10 (Cor 8.6).** Replace the last proof sentence with "The last follows from \cref{thm:formalized-state:conversion}(d): if $\delta_n=0$ then $y_{n,t}\ge y_{n,0}$ for all $t$, so $y_t\not\to0$ from any initial state with $y_{n,0}>0$."
- **F11 (Thm 5.9, P→F).** Replace "Lemma 3.5 of Part II gives a replacement between consecutive changes, and" with "by \cref{lem:formalized-state:pillars} all but finitely many of these conflicts are settled, so the rule system is replaced after all but finitely many changes, and".
- **F12 (Thm 4.3 ordering).** Either:
  - move Defs 5.1–5.2 and Lemma 5.4 ahead of Thm 4.3; or
  - restate Thm 4.3 for the six $\Impl_m$ only, and add after Lemma 5.4: "Corollary. Under the hypotheses of \cref{thm:formalized-state:A}, $\Struct(G)$ holds."
- **F13 (honesty after the Ax3\*/Ax4\* strengthening; text, not counted).**
  - Line 365: replace "The six axioms ... about the same objects. The next subsection adds that premise explicitly." with "Apart from the compliance clause of Ax3$^{*}$ and the settlement-procedure and entrant clauses of Ax4$^{*}$, the six axioms constrain each function separately. The next subsection adds the incidences on production, rule making, interpretation and coercion."
  - Line 365: change "$\pP$, $\pJ$ and $\pC$ have no arc to any function except through the disjunctive hyperarc" to "$\pP$ and $\pJ$ have no outgoing arc, and $\pC$ has one only through the disjunctive hyperarc".
  - Line 391: add "The incidence clauses of Ax4$^{*}$ fail for a collective whose entrants are never parties to conflicts over goods, or whose settlement procedures are run by specialists whose rules the parties need not know; the compliance clause of Ax3$^{*}$ fails for a losing party that complies with no legitimating belief and no expected sanction."
  - Def 2.2(iii): change "neither party controls" to "neither party controls alone".

SUMMARY: 24 results checked (23 numbered results + 1 scope item); OK 10, GAP 13, WRONG 1; witness pairs OK 28/28

---

# ROUND 2 SPOT-CHECK

Scope:
- Read-only check of formalized-state.tex/.pdf as of 13:32 (43 pp.); numbering taken from the new .aux.
- Re-derived only F1–F13 (plus F3b) and the results they touch.
- Model files are unchanged since round 1 (last modified 13:16). Re-runs: pytest 324 passed; `verify_witnesses.py` 86/86 constructions OK, so the **28/28 witness pairs still hold**; all 877 coarsenings give 0 failures.

**Result: 3 of the 14 fix labels (F4, F5, F6) leave follow-ups. There is 1 major new item (R1, created by the F3 + F4 interaction), 3 minor items (R2, R3, R5), and 1 carried-over partial fix (R4).**

| Fix | Location now | Status | Evidence |
|---|---|---|---|
| F1 practice clause | Table 1 Ax6\*; Lemma 5.4 Production; Thm 6.6; Thm 7.4(b) | OK | The clause is in Ax6\*, so "hence Struct and Inter" (Thm 6.6) and Thm 7.4(b) now follow. In Lemma 5.4, W→m uses consumption as a direct input of each practice instance, not persistence (Remark 5.3 respected). |
| F2 best response | Table 1 Ax5\* | OK | This now matches Part V Lemma 3.3 and Thm 3.4. Lemma 4.2(C) and Thm 5.10 C→F go through. |
| F3 Ax3\* clauses | Table 1 Ax3\*; Lemma 5.4 Interpretation; Lemma 4.2 | OK | The finite-disposition clause is present, and the ℓ/σ "only if" clauses make ({I,C},J) follow from withholding both outputs. Lemma 4.2 now says "contains". |
| F3b need-not-contain | Lemma 5.4 | OK | Prop 4.4(a) gives ℓ ≥ g from the initiation; adding d ≥ g to defiance means withholding I leaves σ ≥ g and withholding C leaves ℓ ≥ g. So neither single arc is in D(G). |
| F4 Prop 4.4(a) | Prop 4.4 proof | OK for (a); **creates R1 in (b)** | (a) checked clause by clause against all six strengthened axioms. Ax4\*: CK by initiation; turnover in every window; non-innate; no forgetting; the most recent entrant is party to every period's conflict. Ax3\*: ℓ comes from the initiation (a legitimation practice), σ = 0. Ax5\*: p = 1/2 > θ = 1/4 with best response, violation rate 1 − G(d) ≤ 1/4. Ax6\* holds. Prop 5.11(a), "no arc enters W", is now justified: foraging is individual, independent of campsite, uses no contested input, and is ungoverned by the chores rule. |
| F5 admissible Λ | Lemma 6.5; Thm 6.6 | OK; **R2 follows** | The admissibility definition covers exactly the three performer clauses, and Thm 6.6 asserts that each corner is admissible ((1,1) requires the disputants to lie outside the single organization, which the sentence asserts). But Prop 7.5 and Prop 10.1(c)(d) still invoke Lemma 6.5 without checking admissibility. |
| F6 well-formed record | Def 7.2; Thm 7.4 | OK; **R3 follows** | (F2)/(F3) now follow from the record clause. But 𝒢\* (Sec 7.3) still says "coded record", while Thm 7.7(a) applies Thm 7.4(b), which needs a well-formed one. |
| F7 Thm 7.8 | Thm 7.8; Remark 7.9 | OK | The restated sentence is exactly what the proof gives. Remark 7.9 now excludes the paired-block counterexample. |
| F8 G ≅_A G′ | Def 7.2 | OK | Thm 7.7(a) is now well-posed. |
| F9 K = ∅ | Prop 7.5(a) | OK | Edge case covered; the enumeration includes the all-drop map. |
| F10 Cor 8.6 | Cor 8.6 proof | OK | Uses y_{n,t} ≥ y_{n,0} > 0. |
| F11 P→F | Thm 5.10 | OK | Settlement of the new conflicts comes from Lemma 4.2 (all but finitely many settled), which forces replacement after all but finitely many changes. Part II Lemma 3.5 is no longer needed. |
| F12 ordering | Thm 4.3 → Lemma 5.4 → Cor 5.5 | OK | Thm 4.3 now claims only Impl. Lemma 5.4 uses Lemma 4.2 and the axioms (earlier results). Cor 5.5 combines them. Thm 7.4(b) cites Cor 5.5 and Thm 5.10. There is no forward dependency in any proof; Def 2.3's pointer to Lemma 5.4 is a definition, not a use. |
| F13 text and falsifiers | l.374, l.400, Def 2.2(iii) | OK; **R5 (minor)** | All three falsifiers name observations that can occur: (i) entrants never party to conflicts over goods; (ii) settlement run by specialists whose rules the parties need not know; (iii) compliance with neither a legitimating belief nor an expected sanction. Note that (ii) may be *met* in complex polities (tax codes, credit scoring). The reply would have to be that the specialists belong to the cooperating core and the parties anticipate through them, and that should be said. (iii) is testable only if ℓ and σ are measured independently of the compliance they explain, but l.312 extends the independence rule only to "every hazard". |

**Is Struct still not true by definition?**
- The Impl part is non-trivial only if every Prop 4.4(b) model works, and **k = 4 currently does not (R1)**.
- The D₀ part rests on explicitly declared incidence clauses (l.374) with stated falsifiers. The clauses are not tautologies, but the arcs I→F and ({I,C},J) are one step from them by design, and the paper now says so.
- Residual caution: "ℓ > 0 only if some practice of the legitimation class" is close to definitional, because Part IV Def 2.1's class is broad. Its falsifier is a party who regards a procedure as rightful without any regular belief-shaping practice behind that belief.
- Verdict: **not true by definition, conditional on R1.**

## Remaining fixes

- **R1 (major; the Prop 4.4(b) k = 4 model is broken by F3 + F4).**
  - Problem: in (a), the initiation is now the only source of ℓ. In k = 4 "no practice refines anyone's information", so either:
    - the initiation goes. Then ℓ = 0 (Ax3\* "only if"), σ = 0, every determination is defied, each dispute triggers κ = 1/2, and Pr(Π) = 0. The model no longer "functions at every date with probability one".
    - or the initiation stays as a validating ritual. Then a practice of the legitimation class operates every window, which contradicts l.248, "the function is absent".
  - Fix: replace "For $k=4$, let entrants know the rule system at entry, so no practice refines anyone's information." with "For $k=4$, let entrants know the rule system at entry, drop the initiation, and attach the fine $d\ge g$ to defiance of a determination, so no practice of the legitimation class operates and determinations rest on sanction alone."
  - Check: Ax3\* holds (σ ≥ g from a sanction practice), Ax4\* fails only in non-innateness, Impl_I fails, no hazard fires.
- **R2 (minor).**
  - Prop 7.5 proof: replace "By \cref{lem:formalized-state:separation}, $G_1$ and $G_2$ satisfy every axiom" with "Since $a$ and $b$ are organizations of members that are parties to no residual dispute, both assignments are admissible, and by \cref{lem:formalized-state:separation} $G_1$ and $G_2$ satisfy every axiom".
  - Prop 10.1 proof (c): replace "Both lie in $\mathcal{G}_*$ by \cref{lem:formalized-state:separation}." with "Both assignments are admissible as in the proof of \cref{prop:formalized-state:minimality6}, so both lie in $\mathcal{G}_*$ by \cref{lem:formalized-state:separation}."
- **R3 (minor).** Sec 7.3, definition of 𝒢\*: replace "and come with a coded record" with "and come with a well-formed coded record".
- **R4 (carried over; G-J1 is only partly applied).**
  - Problem: Sec 12 (l.993) now states the narrowed carve-out ("some recurring class of residual disputes cannot be escaped by moving"). But Table 1 Ax3\* and the J step of Lemma 4.2 still require the hazard on *every* residual dispute, so the derivation does not cover the collectives Sec 12 says it covers.
  - Fix: apply the rest of G-J1 (Section 2b above), namely:
    - the Ax3\* opening clause;
    - the Lemma 4.2 J step via Lemma 4.1(b) on the inescapable disputes;
    - l.173 "exit is free" → "every residual dispute can be escaped by free exit";
    - the Table 3 J falsifier.
  - Also change l.287 "requires" to "predicts".
- **R5 (minor).** l.312: replace "The same requirement applies to every hazard in \cref{tab:axioms}" with "The same requirement applies to every hazard in \cref{tab:axioms} and to the legitimacy value and expected sanction in the compliance clause of Ax3$^{*}$". At l.400, after the specialist falsifier, add: "where such specialists belong to the cooperating core and parties anticipate assignments through them, the clause holds".

ROUND 2 SUMMARY: 14 fix labels checked; OK 11, OK-with-follow-up 3 (F4, F5, F6); new items: R1 major, R2/R3/R5 minor, R4 carried over; witness pairs OK 28/28; 877-coarsening check 0 failures

## ROUND 2 (final pass): F1–F13 plus G-J1, G-J2, against the 44-page build of 13:33

- Model unchanged (last modified 13:16), so the re-run results above still stand: 28/28 witness pairs, 877 coarsenings with 0 failures, pytest 324 passed.
- No undefined references or citations in the log.
- F1–F13 statuses are unchanged from the table above.

| Item | Status | Evidence |
|---|---|---|
| G-J2: unit of the collective | OK | Def 2.1 now opens "the largest group whose members make collective decisions as one body, so that a member's move between subgroups of $G$ is not exit". |
| G-J1 (1): narrowed hazard drives Lemma 4.2's J step | OK, with **R6** | The Ax3\* row restricts the hazard to disputes "that a move to another group of the collective does not escape". Lemma 4.2(J) applies Lemma 4.1(b) to exactly those disputes, and each hypothesis checks: each dispute is disposed at a finite time; κ applies on non-determination; infinitely many arise on Π. Moving within the network counts as abandonment, so the hazard covers it. This gives infinitely many determinations a.s. on Π, which is Impl_J. **But X3 still says "residual disputes ... subject to the hazard of Ax3\*"**, and Thm 5.10's J→F still applies Part III Thm 3.3, which needs the hazard on *every* dispute. |
| G-J1 (2): Ju/'hoansi coding stated as a premise and cited | OK, with **R8** | The new Sec 4.5 paragraph cites lee2013, wiessner2005 and lee1979; all three bibitems are present (Lee 1979 *The !Kung San*; Lee 2013 *Dobe Ju/'hoansi* 4th ed.; Wiessner 2005 *Human Nature* 16(2)). It says explicitly that "The coding is an ethnographic reading of these sources, not a measurement of the hazard", so the coding is not assumed silently. Two overreaches remain: (i) "an instance of Thm 4.3" needs all six axioms, but the paragraph codes only Ax3\*'s clause; (ii) Lee 1979's homicide data show a risk to persons, and the reading that this is a hazard to the *network's functioning*, as Ax3\* requires, is left implicit. |
| G-J1 (3): Prop 4.4(b) still shows each axiom is needed | **NO: R1 open, plus R7** | k = 1, 2, 3, 5, 6 still work. k = 3 fails the narrowed hazard, provided (a)'s disputes count as inescapable, which (a) never states (R7). **k = 4 is unchanged and still broken (R1).** Dropping refinement removes the only source of ℓ, so determinations are defied, κ = 1/2 fires each period, and Pr(Π) = 0. Keeping the initiation instead contradicts "function absent" (l.248). |
| G-J1 other text | OK except l.287 | l.173, the Table 3 J falsifier and Sec 12 are updated consistently. l.287 still reads "which is what Proposition A requires". |
| Earlier R items | R1, R2, R3 open; R5 half done | R2: Prop 7.5 and Prop 10.1(c) still cite Lemma 6.5 without admissibility. R3: 𝒢\* (l.643) still says "coded record". R5: l.316 now covers ℓ and σ, but l.404 still lacks the specialist reply. |

Exact remaining fixes:
- **R1 (major).** Prop 4.4(b): replace "For $k=4$, let entrants know the rule system at entry, so no practice refines anyone's information." with "For $k=4$, let entrants know the rule system at entry, drop the initiation, and attach the fine $d\ge g$ to defiance of a determination, so no practice of the legitimation class operates and determinations rest on sanction alone."
- **R2.**
  - Prop 7.5 proof: replace "By \cref{lem:formalized-state:separation}, $G_1$ and $G_2$ satisfy every axiom" with "Since $a$ and $b$ are organizations of members that are parties to no residual dispute, both assignments are admissible, and by \cref{lem:formalized-state:separation} $G_1$ and $G_2$ satisfy every axiom".
  - Prop 10.1(c): replace "Both lie in $\mathcal{G}_*$ by \cref{lem:formalized-state:separation}." with "Both assignments are admissible as in the proof of \cref{prop:formalized-state:minimality6}, so both lie in $\mathcal{G}_*$ by \cref{lem:formalized-state:separation}."
- **R3.** l.643: "come with a coded record" → "come with a well-formed coded record".
- **R4 remainder.** l.287: "which is what Proposition A requires" → "which is what Proposition A predicts".
- **R5 remainder.** l.404: after "whose rules the parties need not know" insert "(where such specialists belong to the cooperating core and the parties anticipate assignments through them, the clause holds)".
- **R6.**
  - X3: "infinitely many residual disputes about its application arise" → "infinitely many residual disputes about its application arise that a move does not escape".
  - Thm 5.10, J→F: replace "Theorem 3.3 of Part III applied to the disputes about the open-textured procedure gives" with "\cref{lem:formalized-state:forcing}(a), applied to the inescapable disputes about the open-textured procedure, gives".
- **R7.** Prop 4.4(a), after "Take three members at every date": insert "; the collective has no subgroups, so no residual dispute can be escaped by a move and every residual dispute is inescapable in the sense of Ax3$^{*}$".
- **R8.** In the Ju/'hoansi paragraph:
  - Replace "Lee's records of homicide show that self-help between kin carried a real risk \citep{lee1979}" with "Lee's records of homicide show that self-help between kin carried a real risk of feud \citep{lee1979}, which we read as a hazard to the functioning of the camp network in the sense of Ax3$^{*}$".
  - Replace "With it, the Ju/'hoansi are an instance of \cref{thm:formalized-state:A}" with "With it and the codings of the other five axioms in Parts I to VI, the Ju/'hoansi are an instance of \cref{thm:formalized-state:A}".

ROUND 2 FINAL: F1–F13 OK (follow-ups below); G-J2 OK; G-J1 OK in the axiom, the lemma and Sec 12. Still open: R1 (major); R2, R3, R6, R7, R8 (minor); R4 and R5 partly done. Witness pairs OK 28/28; 877-coarsening check 0 failures.

## FINAL PASS (R1–R5 and the Thm 6.6 citation; build of 13:36, 44 pp., 0 undefined references)

- **R1: OK.** The k = 4 model checks out item by item:
  - Entrants know the rules at entry, and there is no initiation, so no practice of the legitimation class operates and Impl_I fails.
  - Ax4\* fails (non-innateness).
  - Ax3\* holds: ℓ = 0, and σ = d ≥ g comes from a sanction practice, so every determination is effective and κ never fires.
  - Ax1\* holds, because the rotation rule is known (innately).
  - Ax2\*, Ax5\* and Ax6\* are unchanged; the new fine is performed by members who best-respond.
  - No hazard fires, so Pr(Π) = 1.
  - Struct is therefore not true by definition, with all six independence models valid.
- **R2: OK.** Admissibility is now stated in the Prop 7.5 proof and in Prop 10.1(c).
- **R3: OK.** 𝒢\* and Thm 7.4 both say "well-formed coded record". The remaining l.597 occurrence of "coded record" is the definition itself.
- **R4: Accepted as kept** ("requires" at l.287, the lead's decision under G-J1).
- **R5: OK.** The specialist reply is now at l.404.
- **Thm 6.6: OK.** It now cites Cor 5.5 together with Thm 5.10 for Struct and Inter, which is correct after F12.
- **Still open (minor; outside R1–R5):**
  - **R6.** X3 still reads "residual disputes about its application arise, subject to the hazard of Ax3\*". Ax3\*'s hazard now covers only inescapable disputes, and Thm 5.10's J→F step still cites Part III Thm 3.3, which needs the hazard on every dispute. Fix: insert "that a move does not escape" after "arise", and cite Lemma 4.1(a) in the J→F step.
  - **R7** is cosmetic: a 3-member collective with no subgroups has only inescapable disputes.
  - **R8** is optional: say "with the codings of the other five axioms".

FINAL: R1–R5 OK; Thm 6.6 citation OK; one minor item open (R6); witness pairs OK 28/28; 877-coarsening check 0 failures.
