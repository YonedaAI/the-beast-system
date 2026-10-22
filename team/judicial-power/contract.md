# Contract: judicial-power (Part III)

## Defines (objects this Part owns; other Parts cite, never redefine)
- Rule system with open texture (cases X, verdicts V, admissible readings, open set O(r)); formal statement of Ax3 for this Part — `def:judicial-power:open-texture`
- Dispute and residual dispute (open-texture case where bilateral settlement fails) — `def:judicial-power:dispute`
- Determination procedure / implemented adjudication (the minimal J function: a procedure not controlled by either party alone whose outputs both parties act on; office not required) — `def:judicial-power:determination`
- Necessity lemma for J (Ax3 + costly self-help + costly exit + persistence => adjudication implemented infinitely often a.s.) — `thm:judicial-power:necessity`
- Exit-substitution proposition (cheap exit removes the forcing; narrows the claim) — `prop:judicial-power:exit`
- Relocation proposition ("code is law": open texture moves to input classification; J relocates, does not vanish) — `prop:judicial-power:relocation`
- Disjunctive enforcement dependency of J (an effective determination needs compliance from legitimacy I OR sanction C) — `prop:judicial-power:disjunctive`
- Operationalization of the source's Q_{J,t}: component vector (appointment insulation, tenure security, access, appeal, reason-giving, compliance by the powerful) and the multiplicative "review-chain" aggregator — `def:judicial-power:qj`
- Ruler-boundness beta_t (rule of law vs rule by law) and two-tier (dual-state) J layer — `def:judicial-power:boundness`, `prop:judicial-power:dualstate`
- Review-chain persistence proposition (pillar-level refinement of source Prop 2) — `prop:judicial-power:chain`
- Insurance model of delegated judicial independence (Landes-Posner, Ramseyer, Stephenson) — `prop:judicial-power:insurance`
- Repeat-player contest (Galanter; legal mobilization object; legal-aid offset) — `prop:judicial-power:repeat`
- Judicial capture link (source capture link restricted to layer J) — `def:judicial-power:capture`
- Hart's secondary rule of adjudication (Part II owns the rule of change, Part IV the rule of recognition)
- Primary treatment of cross-pillar pairs C_{JI}, C_{JC}, C_{JW}
- Hypotheses HJ1-HJ8 with falsifiers

## Imports (objects this Part uses but does not own)
- G_t, A^m_t, a^m_{ij,t}, role map, s^m_{i,t}, H_{m,t}, Q_{m,t}, U_t, C_{mn,t}, \mathcal{I}_t, capture link, x_t, coalition objective, Props 1-4, H1-H6 — source paper (\citep{largo2026hbs})
- Proposition A (general necessity theorem), Ax1-Ax6, dependency digraph D, non-implication A -/-> B — Part VII (formalized-state)
- Appointment channel (who appoints judges); Hart's rule of change; Madison/Montesquieu separation of powers; primary treatment of C_{PJ} — Part II (political-power)
- Resource advantage, regulatory capture, rent seeking; primary treatment of C_{FJ} — Part I (financial-power)
- Rule of recognition, religious ideological authority, professions as epistemic authority — Part IV (ideological-power)
- Enforcement of judgments, procuracy/police as sanction apparatus — Part V (coercive-power)
- Exit, voice, loyalty (Hirschman); unions — Part VI (productive-power)

## Notation
- \mathsf{J} : judicial pillar label (sans-serif); \mathcal{I}_t integration statistic
- X, V, \mathcal{R}(r), O(r) : cases, verdicts, admissible readings of rule r, open set of r
- \delta : determination procedure
- \mathbf{q}_t = (q^{dis}, q^{acc}, q^{ind}, q^{cmp})
- \beta_t : ruler-boundness (compliance of the governing coalition with adverse final determinations)
- \pi : incumbent's probability of losing office (insurance model); \iota : court independence
- n, \theta : repeat player's caseload and precedential weight (repeat-player contest)

## Cross-references I will make
- Part VII: general necessity theorem (Proposition A), Ax3, non-implication A -/-> B, dependency digraph
- Part II: appointment channel, rule of change, C_{PJ}, separation of powers
- Part I: resource advantage, capture/rent seeking, C_{FJ}
- Part IV: rule of recognition, ulama/clergy as producers of belief
- Part V: enforcement of judgments
- Part VI: exit/voice, unions and labor courts on the W side
