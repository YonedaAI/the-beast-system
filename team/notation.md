# Shared notation (pre-seeded by the orchestrator; owned by the source paper)

Every Part cites the source paper for the objects below and never redefines them.
Bib entry (use this exact key in every Part):

    @misc{largo2026hbs,
      author = {Mateo Largo},
      title  = {The Hierarchy of the Beast System: Institutional Power, Elite Coordination, and Economic Dependency Across Political Regimes},
      year   = {2026},
      note   = {Working paper, 14 October 2026}
    }

The source used five functions (R, L, K, E, W). This series uses SIX pillars: the source's
rule function L is split into political rule-making (P) and judicial interpretation (J).

| Source | Series pillar | Symbol | Part | Guiding question |
|---|---|---|---|---|
| R | Financial power | F | I   | Who controls the resources? |
| L (legislation, administration) | Political power | P | II  | Who makes the laws? |
| L (adjudication, regulation review) | Judicial power | J | III | Who interprets the laws? |
| K | Ideological power | I | IV  | Who shapes the beliefs? |
| E | Coercive power | C | V   | Who enforces the rules? |
| W | Productive power | W | VI  | Who produces the wealth that sustains everything? |

Pillar index set: \mathcal{M} = {F, P, J, I, C, W}, |\mathcal{M}| = M = 6.

## Core objects (cite as \citep{largo2026hbs}; LaTeX macros recommended)

| Object | Notation | Meaning |
|---|---|---|
| Polity network | G_t = (V_t, E_t) | Directed multiplex network at time t; V_t = organizations or coherent actor groups |
| Layer | A^m_t, m in \mathcal{M} | Adjacency of pillar-layer m |
| Edge weight | a^m_{ij,t} in [0,1] | Documented capacity of actor i to constrain a feasible action of actor j through mechanism m |
| Role map | F: V -> 2^{\mathcal{M}} | Many-to-many assignment of actors to pillars (call it the role map; do NOT reuse F for the financial pillar in math, write \mathsf{F} for the pillar label) |
| Control share | s^m_{i,t}, sum_i s^m_{i,t} = 1 | Actor i's normalized share of decision-relevant control in pillar m |
| Concentration | H_{m,t} = sum_i (s^m_{i,t})^2 | Herfindahl-Hirschman concentration of pillar m |
| Contestability | Q_{m,t} in [0,1] | Transparency, appeal rights, independence, competition, credible replacement |
| Unaccountable concentration | U_t = sum_m \omega_m H_{m,t} (1 - Q_{m,t}), sum \omega_m = 1, \omega_m >= 0 | Illustrative index, weights must be preregistered |
| Cross-pillar integration | C_{mn,t} in [0,1] | Extent one coalition commands appointments, budgets, sanctions or agenda in both m and n |
| Integration statistic | I_t = (2 / (M(M-1))) sum_{m<n} C_{mn,t}, M = 6 | Mean pairwise integration (15 pairs) |
| Capture link | (i -> j, m) | Influence meeting all three: (i) privileged access or discretion, (ii) weakens applicable accountability or contestability, (iii) material evidence ties the asymmetry to an institutional output |
| State vector | x_t = (F_t, P_t, J_t, I_t^{cap}, C_t, W_t) | Aggregate pillar capacities; dynamics x_{t+1} = B_t x_t + D_t z_t + \epsilon_t |
| Coalition objective | max_{p,c,g} \Pi = B(p) + \rho(c) - \kappa(g) - \phi(opposition, oversight) | Representative governing coalition; preferences must be supplied and tested |

Notation clash to avoid: the integration statistic I_t and the ideological pillar label I.
Convention: write the pillar labels in sans-serif (\mathsf{F}, \mathsf{P}, \mathsf{J}, \mathsf{I}, \mathsf{C}, \mathsf{W})
and the integration statistic as \mathcal{I}_t.

## Strong "Beast System" claim (source's criterion, owned by the source; Part VII formalizes it)

A strong HBS classification requires BOTH high unaccountable concentration (U_t) AND high
cross-pillar integration (\mathcal{I}_t). Differentiation alone (wealthy people, officials,
judges, academics, police, workers exist) never suffices (source Proposition 1).

Source propositions to cite (not redefine): Prop 1 integration not implied by differentiation;
Prop 2 checks can interrupt transmission; Prop 3 control paths differ by regime; Prop 4 public
benefit is compatible with hierarchy. Source hypotheses H1 to H6.

## The six regime types every pillar paper compares

1. Market-capitalist societies (private capital with large political influence)
2. Communist party-states (ruling party at the center)
3. Democratic and market socialism / social democracy
4. Islamic states (political legitimacy derived from religious law; e.g. historical caliphates, Ottoman, modern Iran, Saudi Arabia; note internal diversity)
5. Historical Catholic monarchies (royal authority intertwined with the Church; e.g. Habsburg Spain, Bourbon France, Papal States)
6. Secular democracies (authority distributed among elected officials, courts, private institutions)

## Label convention

Pillar-specific objects: def:<slug>:<name>, thm:<slug>:<name>, prop:<slug>:<name>.
Part numbers: I financial-power, II political-power, III judicial-power, IV ideological-power,
V coercive-power, VI productive-power, VII formalized-state.

## CENTRAL THESIS (author's clarification, binding on every Part)

The Beast System is NOT a historical anomaly that some regimes develop. It is an unavoidable
structural property of organized human governance. Two propositions are kept strictly apart:

- Proposition A (structural necessity; Part VII proves it as a theorem). Let \mathcal{G} be the class
  of functioning human governance systems and B(G) the statement that G contains the six-function
  structure {F,P,J,I,C,W} together with the dependency relations among the functions. Then
  for all G in \mathcal{G}, B(G); equivalently no G in \mathcal{G} has not-B(G). The functions may be
  distributed across institutions, fused inside one institution, or exercised informally.
- Proposition B (institutional capture). The functions become concentrated or coordinated so
  that independent accountability fails (high U_t AND high \mathcal{I}_t, capture links present).
  B is CONTINGENT and measurable. A does not imply B; Part VII proves this non-implication and
  states the conditional axioms under which capture tendencies arise (Michels-type delegation
  costs, Olson-type organization asymmetries) and the checks that interrupt them.

Proof standard for A: NOT true-by-definition. Part VII starts from minimal axioms about collective
life and DERIVES each function as necessary. Working axiom set (Part VII refines and owns it):
  Ax1 scarcity: resources are finite and claims on them conflict           -> F (allocation)
  Ax2 plurality: members' preferences diverge; collective choices are made -> P (rule-making)
  Ax3 generality: rules are general, cases are particular; disputes arise   -> J (interpretation)
  Ax4 coordination: compliance and cooperation need shared beliefs/common knowledge -> I (legitimation)
  Ax5 defection: some members sometimes break rules                         -> C (sanction)
  Ax6 maintenance: the group and its institutions consume resources that someone produces -> W
Minimal-form lemma: in small consensus or stateless societies each function still exists in an
informal, distributed form (gossip and shunning as C; elders or mediators as J; consensus
meetings as P; myth and ritual as I; sharing norms as F; foraging and household labor as W).
Hard cases each pillar paper must confront: !Kung/Ju/'hoansi, Nuer "ordered anarchy"
(Evans-Pritchard), Clastres "Society Against the State", Boehm's reverse dominance hierarchy,
Ostrom commons (monitoring, graduated sanctions, conflict resolution), Hart's primary and
secondary rules (rules of change ~ P, adjudication ~ J, recognition ~ I).

Consequence for Parts I to VI: each pillar paper (a) derives its pillar from its axiom and shows
its minimal form in stateless/consensus societies, (b) then compares how the universal function is
DISTRIBUTED across the six regime types (which institutions hold it, how concentrated, how coupled
to other pillars, what preserves accountability), and (c) states when coordination in that pillar
turns into capture. Historical comparison asks HOW the universal structure manifests, not WHETHER
a civilization "has" the Beast System. Every regime type has it; this is why the comparison is
even-handed by construction.

Revised guardrail 1: "Beast System" names the universal six-function structure (Proposition A),
present in every governance system. It is never a label for a particular religion, people,
profession, regime or named person. Capture (Proposition B) is the contingent, evidence-based claim.
