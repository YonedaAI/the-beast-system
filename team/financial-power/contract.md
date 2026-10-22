# Contract: financial-power (Part I)

## Defines (objects this Part owns; other Parts cite, never redefine)
- Allocation problem and settlement of conflicting claims (Ax1 formalized for the pillar) — label `def:financial-power:allocation-problem`, `def:financial-power:settlement`
- Settlement modes of the financial pillar (sharing norm, property and exchange, command allocation, endowment, credit) — `def:financial-power:settlement-modes`
- Allocation regime (holders, H^F, Q^F, couplings C_{Fn}) — `def:financial-power:allocation-regime`
- Necessity lemma for the financial pillar (settlement share tends to one under persistence) — `prop:financial-power:necessity`
- Pillar-level non-implication (necessity of F constrains neither H^F nor Q^F) — `prop:financial-power:nonimplication`
- Aggregation gap of financial concentration across subdomains (equals cross-domain variance of shares) — `prop:financial-power:aggregation-gap`
- Conversion elasticity / institutional conversion rate (resource-to-rule conversion; Walzer, Bourdieu) — `def:financial-power:conversion`
- Influence-investment comparative statics (Olson-Stigler threshold; conditional) — `prop:financial-power:influence`
- Repeated sovereign credit constraint (Conklin; Drelichman-Voth) — `prop:financial-power:sovereign-credit`
- Owned shared concepts per KB Section 10: rent seeking, regulatory capture, soft budget constraint, state capture (Hellman et al.), rentier state (allocation side), fiscal-military state (financing side), resource advantage of repeat players (introduced; Part III owns legal mobilization)
- Primary treatment of cross-pillar pairs FP, FJ, FI, FC, FW

## Imports (objects used but not owned)
- G_t, A^m_t, a^m_{ij,t}, role map, s^m_{i,t}, H_{m,t}, Q_{m,t}, U_t, C_{mn,t}, \mathcal{I}_t, capture link, x_t, coalition objective, strong HBS criterion, Props 1-4, H1-H6 — owned by source (largo2026hbs)
- Proposition A (general necessity theorem), axioms Ax1-6, dependency digraph, non-implication A -/-> B — owned by Part VII (formalized-state)
- Appointment channel, Michels's law, separation of powers — Part II (political-power)
- Legal mobilization and repeat players in courts, judicial independence — Part III (judicial-power)
- Mann IEMP presentation, hegemony, media systems — Part IV (ideological-power)
- Tilly's coercion thesis, coercive organizations' business arms (coercion side) — Part V (coercive-power)
- Exit/voice/loyalty, welfare regimes, unions, tax compliance — Part VI (productive-power)

## Notation
- \mathsf{F} : financial pillar label (sans-serif); F (italic) is NOT used for the pillar
- s^{\mathsf F}_{i,t}, H_{\mathsf F,t}, Q_{\mathsf F,t} : control share, concentration, contestability of the financial pillar
- H^*_{\mathsf F,t} = (H - 1/n)/(1 - 1/n) : size-normalized concentration
- u_{\mathsf F,t} = H_{\mathsf F,t}(1 - Q_{\mathsf F,t}) : financial term of U_t
- \varepsilon_{\mathsf F \to n} : conversion elasticity from resource share to outputs of pillar n
- \mathcal{I}_t : integration statistic (never I_t)

## Cross-references I will make
- Part VII, Proposition A and non-implication A -/-> B (general theorem)
- Part II, appointment channel (party-state allocation pathway)
- Part III, legal mobilization of repeat players (C_{FJ})
- Part IV, Mann's IEMP model (C_{FI})
- Part V, coercion side of the fiscal-military state; security-force business arms (C_{FC})
- Part VI, exit and voice; taxation as compliance (C_{FW})
