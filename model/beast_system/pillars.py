"""Pillar and axiom vocabulary.

Pillars follow team/notation.md (index set M = {F, P, J, I, C, W}, M = 6); axioms follow
the working set Ax1..Ax6 of the knowledge base, Section 4.2 (Part VII owns and refines them).
"""

from __future__ import annotations

from enum import Enum
from itertools import combinations


class Pillar(Enum):
    """The six pillars. The source's rule function L is split into P and J (notation.md)."""

    F = "F"
    P = "P"
    J = "J"
    I = "I"  # noqa: E741  (pillar label, not the integration statistic)
    C = "C"
    W = "W"

    @property
    def label(self) -> str:
        """Long name, e.g. 'financial'."""
        return _LABELS[self]

    @property
    def question(self) -> str:
        """Guiding question of the Part that owns the pillar (notation.md table)."""
        return _QUESTIONS[self]

    @property
    def position(self) -> int:
        """Row/column of the pillar in 6x6 arrays (order F, P, J, I, C, W)."""
        return PILLARS.index(self)


_LABELS = {
    Pillar.F: "financial",
    Pillar.P: "political",
    Pillar.J: "judicial",
    Pillar.I: "ideological",
    Pillar.C: "coercive",
    Pillar.W: "productive",
}

_QUESTIONS = {
    Pillar.F: "Who controls the resources?",
    Pillar.P: "Who makes the laws?",
    Pillar.J: "Who interprets the laws?",
    Pillar.I: "Who shapes the beliefs?",
    Pillar.C: "Who enforces the rules?",
    Pillar.W: "Who produces the wealth that sustains everything?",
}

PILLARS: tuple[Pillar, ...] = tuple(Pillar)
M: int = len(PILLARS)
#: The M(M-1)/2 = 15 unordered pillar pairs (m < n) summed in the integration statistic.
PAIRS: tuple[tuple[Pillar, Pillar], ...] = tuple(combinations(PILLARS, 2))


class Axiom(Enum):
    """Working axioms about collective life (KB Section 4.2; notation.md CENTRAL THESIS).

    Statements follow Part VII's starred versions (Ax3*, Ax4*, Ax5*, Ax6* add clauses).
    """

    Ax1 = "scarcity"
    Ax2 = "plurality"
    Ax3 = "generality"
    Ax4 = "coordination"
    Ax5 = "defection"
    Ax6 = "maintenance"

    @property
    def label(self) -> str:
        return self.value

    @property
    def statement(self) -> str:
        return _STATEMENTS[self]

    @property
    def pillar(self) -> Pillar:
        """The pillar whose function solves the problem this axiom generates."""
        return AXIOM_TO_PILLAR[self]


_STATEMENTS = {
    Axiom.Ax1: "resources are finite and claims on them conflict",
    Axiom.Ax2: "members' preferences diverge and some collective choices must be made",
    Axiom.Ax3: (
        "rules are general, cases are particular, and disputes arise; each residual dispute "
        "reaches a disposition at a finite time; the loser complies iff ell + sigma >= g, "
        "with ell > 0 only via a legitimation practice and sigma > 0 only via a sanction "
        "practice"
    ),
    Axiom.Ax4: (
        "compliance and cooperation need shared beliefs or common knowledge; settlement "
        "procedures belong to the common-knowledge rule system; entrants are parties to "
        "conflicts in infinitely many periods"
    ),
    Axiom.Ax5: "some members sometimes break rules; members best-respond",
    Axiom.Ax6: (
        "the group and its institutions consume resources that someone produces; every "
        "practice is performed by agents whose consumption is counted, in a period only if "
        "that consumption is met"
    ),
}

#: Axiom -> pillar map (KB Section 4.2 table, 'Yields' column). It is a bijection.
AXIOM_TO_PILLAR: dict[Axiom, Pillar] = {
    Axiom.Ax1: Pillar.F,
    Axiom.Ax2: Pillar.P,
    Axiom.Ax3: Pillar.J,
    Axiom.Ax4: Pillar.I,
    Axiom.Ax5: Pillar.C,
    Axiom.Ax6: Pillar.W,
}
PILLAR_TO_AXIOM: dict[Pillar, Axiom] = {p: a for a, p in AXIOM_TO_PILLAR.items()}


class IncidenceAxiom(Enum):
    """Incidence axioms X_k (Part VII Assumptions 5.6 to 5.9: X1, X2, X3, X5).

    X_k states that the problem of Ax_k arises about the inputs or rules of a named pillar,
    which generates the arc pillar(Ax_k) -> that pillar. Each is an empirical premise with a
    stated falsifier, not a logical truth.
    """

    X1 = "contested inputs"
    X2 = "changing environment"
    X3 = "open-textured allocation rules"
    X5 = "tempting allocation rules"

    @property
    def label(self) -> str:
        return self.value

    @property
    def base(self) -> Axiom:
        """The axiom whose problem the incidence locates."""
        return _INCIDENCE[self][0]

    @property
    def target(self) -> Pillar:
        """The pillar whose inputs or rules the problem arises about."""
        return _INCIDENCE[self][1]

    @property
    def statement(self) -> str:
        return _INCIDENCE[self][2]

    @property
    def falsifier(self) -> str:
        return _INCIDENCE[self][3]


_INCIDENCE: dict[IncidenceAxiom, tuple[Axiom, Pillar, str, str]] = {
    IncidenceAxiom.X1: (
        Axiom.Ax1, Pillar.W,
        "productive activity uses inputs under conflicting claims, used only under an "
        "anticipable assignment",
        "a persistent collective whose productive inputs never meet conflicting claims",
    ),
    IncidenceAxiom.X2: (
        Axiom.Ax2, Pillar.F,
        "the environment changes infinitely often (Part II Ass 3.2) and each change creates "
        "conflicts no prior settlement procedure can settle",
        "a persistent collective whose prior settlement procedures settle every new conflict",
    ),
    IncidenceAxiom.X3: (
        Axiom.Ax3, Pillar.F,
        "some settlement procedure has open texture and generates infinitely many residual "
        "disputes",
        "settlement procedures that leave only finitely many residual disputes",
    ),
    IncidenceAxiom.X5: (
        Axiom.Ax5, Pillar.F,
        "Ax5 holds for some settlement procedure",
        "no member ever breaks any settlement procedure",
    ),
}
