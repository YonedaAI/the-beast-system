# The Formalized State

*The Six Pillars of the Beast System*

The six-pillar framework identifies an invariant structure of human governance, supported by historical observation and given precise expression through mathematics.

The ideology changes. The institutional functions remain.

Every governance system answers six questions: who controls the resources, who makes the laws, who interprets them, who shapes beliefs, who enforces the rules, and who produces the wealth. This series of seven papers treats those questions as six functional pillars (financial, political, judicial, ideological, coercive and productive). It examines how six regime types distribute the pillars: market capitalism, communist party-states, democratic socialism, Islamic states, historical Catholic monarchies and secular democracies. Part VII formalizes the result as the Formalized State.

**Website:** [the-beast-system.vercel.app](https://the-beast-system.vercel.app)

## The papers

| Part | Paper | Question | PDF |
|---|---|---|---|
| I | Financial Power and Resource Command | Who controls the resources? | [PDF](papers/pdf/financial-power.pdf) |
| II | Political Power and Rule Making | Who makes the laws? | [PDF](papers/pdf/political-power.pdf) |
| III | Judicial Power and Legal Interpretation | Who interprets the laws? | [PDF](papers/pdf/judicial-power.pdf) |
| IV | Ideological Power and Legitimation | Who shapes the beliefs? | [PDF](papers/pdf/ideological-power.pdf) |
| V | Coercive Power and Enforcement | Who enforces the rules? | [PDF](papers/pdf/coercive-power.pdf) |
| VI | Productive Power and Social Reproduction | Who produces the wealth? | [PDF](papers/pdf/productive-power.pdf) |
| VII | The Formalized State: The Hierarchy of the Beast System | How do the six compose into one order? | [PDF](papers/pdf/formalized-state.pdf) |

LaTeX sources are in `papers/latex/`.

## What the series establishes

Each pillar paper derives the necessity of its function from a minimal axiom: scarcity, plurality, generality, coordination, defection or maintenance. It then shows the function's minimal informal form in stateless and consensus societies and compares its distribution across the six regime types at equal depth.

Part VII proves four results about the Formalized State, each relative to its stated axioms and preserved properties:

| Result | Statement |
|---|---|
| Representation | Every governance system that satisfies the axioms is equivalent, on the preserved governance properties, to a Formalized State. |
| Necessity | The axioms force all six functions and their full interdependence: every pillar reaches every other, and a failure in any one propagates to all six. |
| Minimality | Dropping or merging any pillar confuses two governance systems that the full structure distinguishes. |
| Uniqueness | The Formalized State is the coarsest abstraction that preserves those properties. It is unique up to unique isomorphism and has exactly six dimensions. |

Part VII also encodes seven earlier frameworks: Aristotle, Weber, Parsons, Easton, Almond, Luhmann and Mann. It shows, with an explicit pair of systems for each, that none of them is equivalent to the Formalized State.

The structure is universal; capture is not. Part VII proves that having the six-pillar structure does not imply that the pillars are captured by one coalition. Capture is a contingent, measurable property of particular regimes.

The regime analyses are qualitative and rest on the historical and ethnographic record. The concentration, contestability and integration indices are defined so that real polities can be scored quantitatively.

"Beast System" is a typological reading of Revelation 13 and 17 to 18, informed by scholarly commentary (Bauckham, Collins, Koester, Kraybill). It names the universal six-function structure. It is never a label for any religion, people, profession, regime or person.

## Reference implementation

`model/` holds a Python package, `beast_system`, that encodes the objects of Part VII: the six-layer multiplex, the concentration and integration indices, the axiom-generated dependency hypergraph, the capture predicate, the representation map, coarsenings, the uniqueness factorization and the predecessor encodings. Appendix A of Part VII maps each formal result to the code and tests that support it.

```bash
cd model
python3 -m pip install -e ".[test]"
python3 -m pytest
python3 examples/run_all.py
```

Requires Python 3.10 or later. The test suite has 335 tests. The regime profiles in `beast_system.regimes` are illustrative values chosen to show how the structure can be distributed. They are not measurements.

## Repository layout

| Path | Contents |
|---|---|
| `papers/latex/`, `papers/pdf/` | Paper sources and compiled PDFs |
| `model/` | Python reference implementation and tests |
| `website/` | Next.js site (static export) |
| `docs/papers/` | HTML versions of the papers |
| `images/` | Paper cover images |
| `context/` | The source framework paper this series extends |
| `reviews/`, `team/` | Peer review records, bibliography checks and cross-paper integration records |
| `posts/` | Announcement posts |

## Source

The series extends the five-function framework in *Hierarchy of the Beast System* (Largo, working paper, 14 October 2026), included in `context/`. The series splits the source's legal function into separate political and judicial pillars.

## Author

Matthew Long, The YonedaAI Collaboration, YonedaAI Research Collective, Chicago, IL. [yonedaai.com](https://yonedaai.com)
