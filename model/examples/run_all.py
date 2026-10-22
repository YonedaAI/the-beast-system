"""Print the Part VII summary table: regime profiles, counter-model, dependency graph.

Run from model/:  python3 examples/run_all.py
Regime values are ILLUSTRATIVE ASSUMPTIONS, not measurements (see beast_system.regimes).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from beast_system.capture import Assessment, CaptureThresholds, a_does_not_imply_b, assess  # noqa: E402
from beast_system.dynamics import negative_feedback_example  # noqa: E402
from beast_system.necessity import (  # noqa: E402
    AXIOM_INDEPENDENCE,
    BRIEF_ARCS,
    D0_KEYS,
    D_STAR_KEYS,
    FURTHER_RULES,
    HARD_CASES,
    arc_key,
    cascade_closure,
    check_proposition_a,
    critical_edges,
    generate_dependencies,
    is_cascade_complete,
    is_strongly_connected,
    sinks_and_sources,
    underlying_digraph,
    without_axiom,
)
from beast_system.pillars import PILLARS, IncidenceAxiom, Pillar  # noqa: E402
from beast_system.regimes import regime_profiles  # noqa: E402


def _yn(flag: bool) -> str:
    return "yes" if flag else "no"


def _row(label: str, a: Assessment) -> str:
    hs = " ".join(f"{a.H[m]:.2f}" for m in PILLARS)
    b = a.prop_b
    return (f"{label:<58} {hs}  {a.U:.3f}  {a.I:.3f}  {_yn(a.prop_a.holds):<3}  "
            f"{_yn(b.thresholds_met):<6}  {a.u_high_fraction:.2f}  {b.n_links}  {_yn(b.holds)}")


def main() -> None:
    th = CaptureThresholds()
    head_h = " ".join(f"H_{m.name:<3}" for m in PILLARS)
    header = (f"{'profile':<58} {head_h} U      I      A    U,I>=*  P(U>=u*)  L  B")
    print(f"Thresholds u* = {th.u_star}, i* = {th.i_star}. "
          "Regime values: ILLUSTRATIVE ASSUMPTIONS, not measurements.")
    print(header)
    print("-" * len(header))
    for prof in regime_profiles():
        print(_row(prof.label, assess(prof.polity, th)))
    print("-" * len(header))
    cm = a_does_not_imply_b(th)
    print(_row("[counter-model] " + cm.plural.name, cm.plural))
    print(_row("[counter-model] " + cm.fused.name, cm.fused))
    print(f"A does not imply B (constructive counter-model): {cm.demonstrates_non_implication}")
    print("P(U>=u*) = share of 2000 uniform weight draws with U >= u* (weight sensitivity).")
    print("L = evidenced capture links; regime profiles carry none, so B never holds for them.")

    print("\nHard cases (Theorem A check):")
    for sys_ in HARD_CASES:
        r = check_proposition_a(sys_)
        forms = ", ".join(f"{d.pillar.name}:{d.form}" for d in r.derivations.values())
        print(f"  {sys_.name:<36} struct={_yn(r.struct)} interdependent={_yn(r.interdependent)} "
              f"A={_yn(r.holds)} counterexample={_yn(r.counterexample)}  {forms}")

    print("\nAxiom independence models (Ax_k dropped, pillar k absent):")
    for ax, sys_ in AXIOM_INDEPENDENCE.items():
        r = check_proposition_a(sys_)
        print(f"  without {ax.name}: missing={sorted(m.name for m in r.missing)} "
              f"antecedent={_yn(r.antecedent)} counterexample={_yn(r.counterexample)}")

    print("\nGenerated dependency hypergraph (provider -> dependent; OR-hyperarc {I,C}->J):")
    precedent = next(r for r in FURTHER_RULES if r.premise == "precedent (Hart)")
    cases = [("D0", D0_KEYS), ("D* (Ax1..Ax6 + X1,X2,X3,X5)", D_STAR_KEYS)]
    cases += [(f"D* without {x.name}", generate_dependencies(without_axiom(x)))
              for x in IncidenceAxiom]
    cases.append(("D* with X3 replaced by J->P",
                  (D_STAR_KEYS - {arc_key(Pillar.J, Pillar.F)}) | {precedent.key}))
    for label, arcs in cases:
        print(f"  {label:<30} strongly connected = "
              f"{is_strongly_connected(underlying_digraph(arcs))!s:<5}; cascade-complete = "
              f"{is_cascade_complete(arcs)!s:<5}; cl({{C}}) = "
              f"{''.join(sorted(m.name for m in cascade_closure(arcs, {Pillar.C})))}")
    print("  critical arcs of D*: "
          + ", ".join(f"{u.name}->{v.name}" for u, v in critical_edges(underlying_digraph(D_STAR_KEYS))))
    brief = underlying_digraph(BRIEF_ARCS)
    sinks, _ = sinks_and_sources(brief)
    print(f"  six brief relations alone: strongly connected = {is_strongly_connected(brief)}; "
          f"sinks = {sorted(m.name for m in sinks)}")

    fb = negative_feedback_example()
    print("\nDynamics: same positive links, rho(B+) = "
          f"{fb.rho_positive:.3f} (some deviation persists), rho(B+ with negative feedback) = "
          f"{fb.rho_feedback:.3f} (decays); same positive links = {fb.same_positive_links}")


if __name__ == "__main__":
    main()
