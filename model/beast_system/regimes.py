"""Stylized regime profiles for the six regime types (notation.md 'The six regime types').

ILLUSTRATIVE ASSUMPTIONS, NOT MEASUREMENTS. Every share, contestability value Q_m and
integration value C_mn below is a stylized assumption chosen to show how the universal
six-pillar structure (Proposition A) can be DISTRIBUTED differently. None is an estimate for
any country or period, and none should be cited as data.

Every profile satisfies Proposition A by construction of its coded practices. No profile
carries a capture link, because a capture link requires cited material evidence (source
Section 5); hence no profile satisfies Proposition B, whatever its U and I. Variants within
the Islamic and Catholic types differ in their checks, so no value attaches capture to a
religion as such (guardrail 1).
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

from .capture import Polity
from .indices import integration_matrix
from .necessity import formal_system
from .pillars import PAIRS, Pillar

ILLUSTRATIVE = True
DISCLAIMER = "Illustrative assumption, not a measurement."

F, P, J, I, C, W = Pillar.F, Pillar.P, Pillar.J, Pillar.I, Pillar.C, Pillar.W  # noqa: E741


@dataclass(frozen=True)
class RegimeProfile:
    """One stylized profile. ``polity`` holds the illustrative inputs; ``rationale`` the story."""

    regime_type: str
    variant: str
    polity: Polity
    rationale: str
    illustrative: bool = ILLUSTRATIVE

    @property
    def label(self) -> str:
        return f"{self.regime_type} ({self.variant})" if self.variant else self.regime_type


def _profile(
    regime_type: str,
    variant: str,
    shares: Mapping[Pillar, Mapping[str, float]],
    q: tuple[float, float, float, float, float, float],
    c_pairs: Mapping[tuple[Pillar, Pillar], float],
    c_default: float,
    rationale: str,
) -> RegimeProfile:
    name = f"{regime_type} ({variant})" if variant else regime_type
    holders = {m: [a for a, v in s.items() if v > 0] for m, s in shares.items()}
    polity = Polity(
        name=name,
        system=formal_system(name, holders, source=DISCLAIMER),
        shares=shares,
        contestability=dict(zip((F, P, J, I, C, W), q)),
        integration=integration_matrix(c_pairs, default=c_default),
    )
    return RegimeProfile(regime_type, variant, polity, f"{rationale} {DISCLAIMER}")


def _pairs_among(pillars: tuple[Pillar, ...], value: float) -> dict[tuple[Pillar, Pillar], float]:
    return {(m, n): value for m, n in PAIRS if m in pillars and n in pillars}


def regime_profiles() -> tuple[RegimeProfile, ...]:
    """The stylized profiles, two variants each for the Islamic and Catholic types."""
    return (
        _profile(
            "Market capitalism", "",
            {F: {"Financial firms": 4, "Non-financial firms": 3, "State budget": 2, "Households": 1},
             P: {"Legislature": 4, "Executive": 4, "Organized interests": 2},
             J: {"Courts": 7, "Private arbitration": 2, "Regulators": 1},
             I: {"Media firms": 3, "Platforms": 3, "Universities": 2, "Religious bodies": 2},
             C: {"Police": 5, "Military": 3, "Private security": 2},
             W: {"Wage workers": 5, "Non-financial firms": 3, "Households": 2}},
            (0.45, 0.60, 0.70, 0.55, 0.55, 0.40),
            {(F, P): 0.50, (F, I): 0.45, (F, J): 0.35, (F, W): 0.50, (P, J): 0.30,
             (P, I): 0.30, (P, C): 0.30, (P, W): 0.30},
            0.20,
            "Wealth-to-rules pathway (source Prop 3): C_FP, C_FI, C_FW elevated.",
        ),
        _profile(
            "Communist party-state", "",
            {F: {"Party": 6, "SOE management": 3, "Households": 1},
             P: {"Party": 9, "People's congress": 1},
             J: {"Party": 6, "Courts": 4},
             I: {"Party": 7, "Universities": 2, "Religious bodies": 1},
             C: {"Party": 6, "Security services": 4},
             W: {"Workers": 6, "SOE management": 3, "Households": 1}},
            (0.20, 0.10, 0.15, 0.15, 0.10, 0.25),
            _pairs_among((F, P, J, I, C), 0.80),
            0.45,
            "Appointments-to-resources pathway (nomenklatura): party-centred pairs high.",
        ),
        _profile(
            "Democratic socialism", "",
            {F: {"State budget": 3, "Firms": 3, "Public pension funds": 2, "Cooperatives": 1,
                 "Households": 1},
             P: {"Parliament": 5, "Government": 3, "Social partners": 2},
             J: {"Courts": 8, "Ombudsman": 2},
             I: {"Public broadcaster": 3, "Private media": 3, "Universities": 2,
                 "Churches and civil society": 2},
             C: {"Police": 6, "Military": 4},
             W: {"Unions": 4, "Firms": 3, "Workers": 3}},
            (0.65, 0.75, 0.80, 0.70, 0.70, 0.70),
            {(P, W): 0.45, (F, W): 0.40, (F, P): 0.35},
            0.15,
            "Corporatist bargaining couples P, F and W; high Q offsets concentration.",
        ),
        _profile(
            "Islamic state", "plural juristic authority",
            {F: {"Ruler's treasury": 4, "Waqf endowments": 3, "Merchants": 3},
             P: {"Ruler": 5, "Jurists (plural schools)": 3, "Notables council": 2},
             J: {"Qadi courts": 5, "Jurists (plural schools)": 3, "Ruler's grievance court": 2},
             I: {"Jurists (plural schools)": 5, "Sufi orders": 3, "Ruler": 2},
             C: {"Ruler's army": 6, "Local militias": 2, "Market inspectors": 2},
             W: {"Peasants": 5, "Artisan guilds": 3, "Merchants": 2}},
            (0.45, 0.35, 0.55, 0.50, 0.30, 0.40),
            {(P, C): 0.55, (F, P): 0.45, (J, I): 0.45, (F, C): 0.40, (P, I): 0.35,
             (P, J): 0.35},
            0.20,
            "Juristic class trained and endowed apart from the ruler checks P via J and I.",
        ),
        _profile(
            "Islamic state", "centralized clerical-political authority",
            {F: {"Clerical-political center": 5, "State budget": 3, "Merchants": 2},
             P: {"Clerical-political center": 5, "Vetting council": 3, "Elected assembly": 2},
             J: {"Clerical-political center": 5, "State courts": 5},
             I: {"Clerical-political center": 6, "Seminaries": 3, "Media": 1},
             C: {"Clerical-political center": 6, "Regular army": 4},
             W: {"Workers": 5, "Center-linked enterprises": 3, "Merchants": 2}},
            (0.25, 0.25, 0.20, 0.20, 0.15, 0.30),
            _pairs_among((F, P, J, I, C), 0.70),
            0.40,
            "One center commands appointments across P, J, I, C; elected assembly is checked.",
        ),
        _profile(
            "Catholic monarchy", "estates and Church-crown rivalry",
            {F: {"Crown treasury": 4, "Church benefices": 3, "Bankers": 2, "Nobility": 1},
             P: {"Crown": 5, "Estates assembly": 3, "Nobility": 2},
             J: {"Royal courts": 4, "Parlements": 3, "Church courts": 3},
             I: {"Church": 6, "Universities": 2, "Crown": 2},
             C: {"Crown army": 5, "Nobility": 3, "Town militias": 2},
             W: {"Peasants": 6, "Guilds": 3, "Merchants": 1}},
            (0.40, 0.40, 0.45, 0.35, 0.30, 0.30),
            {(F, P): 0.45, (P, I): 0.40, (P, J): 0.40, (F, C): 0.40},
            0.20,
            "Estates, parlements and an autonomous Church contest the crown.",
        ),
        _profile(
            "Catholic monarchy", "absolutist with venal offices",
            {F: {"Crown": 6, "Tax farmers": 3, "Church benefices": 1},
             P: {"Crown": 9, "Royal council": 1},
             J: {"Crown": 5, "Venal office holders": 4, "Church courts": 1},
             I: {"Church hierarchy": 6, "Crown": 3, "Universities": 1},
             C: {"Crown": 8, "Nobility": 2},
             W: {"Peasants": 6, "Guilds": 3, "Tax farmers": 1}},
            (0.20, 0.10, 0.25, 0.20, 0.15, 0.20),
            {**_pairs_among((F, P, J, C), 0.75), (P, I): 0.70},
            0.40,
            "Crown fuses F, P, J, C; venality couples F and J; Church aligned with crown.",
        ),
        _profile(
            "Secular democracy", "",
            {F: {"Central bank": 2, "Firms": 3, "State budget": 3, "Households": 2},
             P: {"Legislature": 4, "Executive": 3, "Subnational governments": 3},
             J: {"Constitutional court": 3, "Ordinary courts": 6, "Administrative tribunals": 1},
             I: {"Public media": 2, "Private media": 3, "Universities": 2, "Religious bodies": 1,
                 "Civil society": 2},
             C: {"Police": 5, "Military": 3, "Oversight bodies": 2},
             W: {"Workers": 5, "Firms": 3, "Unions": 2}},
            (0.60, 0.75, 0.80, 0.70, 0.65, 0.55),
            {(F, P): 0.30},
            0.15,
            "Authority distributed among elected officials, courts and private bodies.",
        ),
    )
