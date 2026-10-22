# Contract: coercive-power (Part V)

## Defines (objects this Part owns; other Parts cite, never redefine)
- Sanction function (pillar C content): imposition of a cost on an agent conditional on an observed or alleged rule violation; implemented formally, informally, distributed or specialized — `def:coercive-power:sanction`
- Sanction regime sigma and deterrence margin d_{i,t} = W_i(h_t,0) - W_i(h_t,1), unilateral-deviation continuation-value gap between compliance and violation — `def:coercive-power:regime`
- Conduct margin \Delta^c(y) and allegiance margin \Delta^a(v) of a targeting function \psi(v, y), relative to a preregistered allegiance-neutral reference rule set R^0 — `def:coercive-power:margins`
- Coercive contestability Q^C components (civilian control, judicial authorization, independent complaints/inspection, individual legal liability, refusal of unlawful orders, budget and intelligence transparency) — `def:coercive-power:qc`
- Coercive control share s^C_i measured by command over deployment decisions (not spending) — `def:coercive-power:share`
- Necessity lemma for C from Ax5 (deterrence lemma: compliance above 1-p requires a nonzero sanction regime) — `thm:coercive-power:necessity`
- Second-order enforcement lemma (sanctioners need provisioning F, motive I, or higher-order sanction): derives edges F->C and I->C as a disjunction — `prop:coercive-power:second-order`
- Minimal-form proposition for C in stateless/consensus societies — `prop:coercive-power:minimal-form`
- Separability of conduct and allegiance margins (pillar-level A-not-implies-B illustration) — `prop:coercive-power:separability`
- Arbitrary-sanction proposition (allegiance-conditioned sanction erodes deterrence of rule violation) — `prop:coercive-power:arbitrary`
- Coup-proofing comparative static (number of counterweight forces increasing in elite-threat salience) — `prop:coercive-power:coup-proofing`
- Outsider-corps (guardian) proposition: dependent coercive corps become principals when their accumulated capacity outgrows replacement — `prop:coercive-power:outsider`
- Institutional analysis of monopoly of legitimate violence, coup-proofing, civil-military relations, secret police and intelligence (KB Section 10)
- Primary treatment of cross-pillar pair CW (conscription, forced and penal labor, policing of labor)

## Imports (objects this Part uses but does not own)
- G_t, A^m_t, a^m_{ij,t}, role map, s^m, H_{m,t}, Q_{m,t}, U_t, C_{mn,t}, \mathcal{I}_t, capture link, x_t, coalition objective, Props 1-4, H1-H6 — source paper (largo2026hbs)
- Proposition A, Ax1-6, dependency structure, A-does-not-imply-B — Part VII (formalized-state)
- Fiscal-military state (financing side), rentier state, capture, pair FC — Part I (financial-power)
- Weber's definition of the state (monopoly of legitimate violence), appointment channel (def:political-power:appointment-channel, prop:political-power:appointment-bound), pair PC, Michels condition — Part II (political-power)
- Judicial independence, rule of law vs rule by law, pair JC (enforcement of judgments) — Part III (judicial-power)
- Hegemony, legitimacy production, pair IC, Mann IEMP overview — Part IV (ideological-power)
- Exit, voice, loyalty (Hirschman) — Part VI (productive-power)

## Notation
- Pillar labels \mathsf{F},\mathsf{P},\mathsf{J},\mathsf{I},\mathsf{C},\mathsf{W}; integration statistic \mathcal{I}_t
- tau_{i,t}: net private temptation of a violation; p = Pr(tau > 0)
- sigma: sanction regime; d_{i,t}: deterrence margin
- pi: detection probability; \mu: sanction magnitude
- \psi(v,y): targeting probability given violation v of a rule in R^0 and alignment y in {al, op}
- \Delta^c(y) = \psi(1,y) - \psi(0,y) conduct margin; \Delta^a(v) = \psi(v,op) - \psi(v,al) allegiance margin
- Q^C weights \omega^{C}_k, components q_{k,t}; appointee loyalty \bar f_S (Part II Prop 6.5)
- Coup-proofing: \phi(k) coup probability, \ell(k) effectiveness loss, \rho elite-threat salience; dependent corps capacity Z_t, seizure value \Gamma
- Result numbers: Thm 3.4 necessity, Ass 3.2 bridge, Prop 3.6 second-order, Cor 3.7 scale, Prop 3.8 minimal form, Props 6.1 separability, 6.2 arbitrary, 6.3 capacity, 6.4 coup-proofing, 6.5 dependent corps
- Q^C_t := Q_{\mathsf{C},t}; H^C_t := H_{\mathsf{C},t}
- k: number of counterweight forces (coup-proofing)

## Cross-references I will make
- Part I: fiscal-military state (financing side), pair FC, rentier state
- Part II: Weber definition of the state, appointment channel for security chiefs, pair PC
- Part III: judicial independence and enforcement of judgments, pair JC
- Part IV: legitimacy, pair IC
- Part VI: exit and voice; labor side of pair CW
- Part VII: general necessity theorem (Proposition A) and A-not-implies-B
