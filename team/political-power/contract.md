# Contract: political-power (Part II)

## Defines (objects this Part owns; other Parts cite, never redefine)
- Rule-making function (pillar P content): making, changing, and setting general rules; legislation, executive decree, administrative rule-making, party-state appointment and agenda setting. Label `def:political-power:rule-making`
- Rule-making profile of a collective (procedure set, initiators, ratifiers, veto holders) — `def:political-power:profile`
- Hart's rule of change, as used in the series (the P member of Hart's triad; III owns adjudication, IV owns recognition) — `def:political-power:rule-of-change`
- Appointment channel: the map from a coalition to the offices it fills in pillar n; C_{Pn} channel through appointment — `def:political-power:appointment-channel` (III uses it for judges, V for security chiefs)
- Agenda control / non-decision (Bachrach-Baratz, Lukes faces of power) as a P-layer object — `def:political-power:agenda-control` (IV applies it to preference shaping)
- Veto player set and effective veto players — `def:political-power:veto-players`
- Political contestability Q^P components (electoral replacement, legislative oversight, free party formation, rule-making transparency, exit) — `def:political-power:qp`
- Necessity lemma for P from Ax2 plurality — `thm:political-power:necessity`
- Minimal-form proposition for P in stateless/consensus societies — `prop:political-power:minimal-form`
- Michels-type delegation condition (conditional tendency toward P concentration; not necessity) — `prop:political-power:michels`
- Appointment-channel integration bound (C_{Pn} bounded below by appointment share) — `prop:political-power:appointment-bound`
- Veto-player comparative static (more effective veto players: lower persistence of preferential rules, lower responsiveness) — `prop:political-power:veto`
- Weber legitimacy types as they bear on who makes rules; monopoly of legitimate violence definition (Weber) cited here, institutional analysis in V
- Madison/Montesquieu separation of powers; Michels's iron law and critics; Lane-Ross bureaucratic divisions (per KB Section 10)
- Primary treatment of cross-pillar pairs PJ, PI, PC, PW (KB Section 10)

## P/J boundary (coordination with Part III)
- P makes or changes general rules (legislation, decrees, regulations, party resolutions, fatwa-to-statute codification by rulers, royal pragmatics/ordonnances).
- J applies and interprets general rules in particular cases (courts, qadis, muftis issuing case opinions, Parlements in their judicial capacity, constitutional review).
- Mixed cases are split by act: a constitutional court striking a statute is J; a legislature overriding by amendment is P. Parlement registration/remonstrance of royal edicts is treated as a P veto (a rule-making act) while its appellate jurisdiction is J. Guardian Council (Iran) vetting of legislation is a P veto; its constitutional interpretation is J.
- Appointment of judges is P (appointment channel, C_{PJ}); judicial independence and the conduct of adjudication are III.

## Imports (objects this Part uses but does not own)
- G_t, A^m_t, a^m_{ij,t}, role map, s^m, H_{m,t}, Q_{m,t}, U_t, C_{mn,t}, \mathcal{I}_t, capture link, x_t, coalition objective, Props 1-4, H1-H6 — source paper (largo2026hbs)
- Proposition A, axioms Ax1-6, dependency structure, A-does-not-imply-B — Part VII (formalized-state)
- Capture, regulatory capture, rent seeking, state capture (Hellman), soft budget constraint — Part I (financial-power)
- Adjudication, rule of law vs rule by law, judicial independence, Hart's rule of adjudication — Part III (judicial-power)
- Hegemony, Hart's rule of recognition, media systems, Mann IEMP overview — Part IV (ideological-power)
- Coercive apparatus, coup-proofing institutional analysis — Part V (coercive-power)
- Exit, voice, loyalty (Hirschman) — Part VI (productive-power)

## Notation
- Pillar labels: \mathsf{F}, \mathsf{P}, \mathsf{J}, \mathsf{I}, \mathsf{C}, \mathsf{W}; integration statistic \mathcal{I}_t
- \mathcal{R}_t : rule set in force at t; \Delta(\mathcal{R}_t) rule changes
- \mathcal{V}^P_t : veto player set; k_t = number of effective veto players
- \alpha_{S,n} : appointment share of coalition S in pillar n
- Q^P_t := Q_{\mathsf{P},t}

## Cross-references I will make
- Part I: capture, state capture, F->P wealth-to-rules path
- Part III: adjudication half of source L; Hart's rule of adjudication; judicial independence
- Part IV: rule of recognition, hegemony, preference-shaping face of power
- Part V: coercion apparatus; appointment of security chiefs uses my appointment channel
- Part VI: exit and voice
- Part VII: general necessity theorem (Proposition A) and A-not-implies-B
