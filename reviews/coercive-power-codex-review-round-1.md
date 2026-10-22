---
reviewer: codex (OpenAI) gpt-5.6-sol
type: formatting
paper: coercive-power
round: 1
date: 2026-10-22T17:08:44Z
---
Reading additional input from stdin...
2026-10-22T17:08:45.059186Z ERROR codex_models_manager::cache: failed to load models cache: missing field `base_instructions` at line 139 column 5
OpenAI Codex v0.145.0
--------
workdir: /Users/mlong/Documents/Development/the-beast-system
model: gpt-5.6-sol
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a16496-2c11-7533-a6f5-557e8c66c179
--------
user
Read ONLY the file papers/latex/coercive-power.tex (do not explore other files or directories). Review it for LaTeX formatting issues: compilation errors, missing packages, broken references, inconsistent styling, overfull/underfull boxes, spacing problems. List all issues with line numbers and concrete fixes. End your response with a VERDICT line — exactly one of: VERDICT: PASS (no issues remain) or VERDICT: NEEDS_FIX (issues listed above must be fixed).
warning: Under-development features enabled: chronicle. Under-development features are incomplete and may behave unpredictably. To suppress this warning, set `suppress_unstable_features_warning = true` in /Users/mlong/.codex/config.toml.
warning: clamping SessionEnd hook timeout to 3s in /Users/mlong/.codex/plugins/cache/openai-codex/codex/1.0.6/hooks/hooks.json
2026-10-22T17:08:46.597888Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server linear: OAuth token refresh failed: Server returned error response: invalid_grant: Grant not found
2026-10-22T17:08:47.542238Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server resend: OAuth token refresh failed: Server returned error response: invalid_grant: Refresh token has been revoked
warning: Exceeded skills context budget of 2%. All skill descriptions were removed and 108 additional skills were not included in the model-visible skills list.
hook: SessionStart
hook: SessionStart
hook: SessionStart
hook: SessionStart
hook: SessionStart
hook: SessionStart
hook: SessionStart
hook: SessionStart Completed
hook: SessionStart Completed
hook: SessionStart Completed
hook: SessionStart Completed
hook: SessionStart Completed
hook: SessionStart Completed
hook: SessionStart Completed
hook: UserPromptSubmit
hook: UserPromptSubmit Completed
2026-10-22T17:08:52.530438Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
codex
I’ll inspect only that TeX file, using line-numbered text and file-local checks—no directory exploration or auxiliary-file lookup.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'nl -ba papers/latex/coercive-power.tex' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	\documentclass[11pt,letterpaper]{article}
     2	
     3	\usepackage[T1]{fontenc}
     4	\usepackage{lmodern}
     5	\usepackage{microtype}
     6	\usepackage[margin=1in]{geometry}
     7	\linespread{1.0}
     8	\setlength{\parskip}{0pt}
     9	\setlength{\parindent}{1.5em}
    10	
    11	\usepackage{amsmath,amssymb,amsthm}
    12	\usepackage{graphicx}
    13	\usepackage{xcolor}
    14	\usepackage{tikz}
    15	\usepackage{booktabs,tabularx,array,longtable}
    16	\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
    17	\newcolumntype{Y}{>{\raggedright\arraybackslash}X}
    18	\usepackage{listings}
    19	\lstset{basicstyle=\ttfamily\footnotesize,breaklines=true,columns=fullflexible,frame=single,framesep=4pt,showstringspaces=false,captionpos=b}
    20	\usepackage[round,authoryear]{natbib}
    21	\usepackage[hidelinks]{hyperref}
    22	\usepackage{cleveref}
    23	
    24	\newtheorem{theorem}{Theorem}[section]
    25	\newtheorem{proposition}[theorem]{Proposition}
    26	\newtheorem{lemma}[theorem]{Lemma}
    27	\newtheorem{corollary}[theorem]{Corollary}
    28	\theoremstyle{definition}
    29	\newtheorem{definition}[theorem]{Definition}
    30	\newtheorem{assumption}[theorem]{Assumption}
    31	\theoremstyle{remark}
    32	\newtheorem{remark}[theorem]{Remark}
    33	\AddToHook{env/proposition/begin}{\crefalias{theorem}{proposition}}
    34	\AddToHook{env/lemma/begin}{\crefalias{theorem}{lemma}}
    35	\AddToHook{env/corollary/begin}{\crefalias{theorem}{corollary}}
    36	\AddToHook{env/definition/begin}{\crefalias{theorem}{definition}}
    37	\AddToHook{env/assumption/begin}{\crefalias{theorem}{assumption}}
    38	\AddToHook{env/remark/begin}{\crefalias{theorem}{remark}}
    39	\crefname{assumption}{assumption}{assumptions}
    40	\Crefname{assumption}{Assumption}{Assumptions}
    41	
    42	% Pillar labels and shared objects (notation owned by the source paper)
    43	\newcommand{\pF}{\mathsf{F}}
    44	\newcommand{\pP}{\mathsf{P}}
    45	\newcommand{\pJ}{\mathsf{J}}
    46	\newcommand{\pI}{\mathsf{I}}
    47	\newcommand{\pC}{\mathsf{C}}
    48	\newcommand{\pW}{\mathsf{W}}
    49	\newcommand{\Mset}{\mathcal{M}}
    50	\newcommand{\Integ}{\mathcal{I}}
    51	\newcommand{\E}{\operatorname{\mathbb{E}}}
    52	\renewcommand{\Pr}{\operatorname{Pr}}
    53	
    54	\title{Coercive Power and Enforcement\\[4pt]
    55	  {\normalsize Part V of \emph{The Six Pillars of the Beast System}}}
    56	\author{Matthew Long\\
    57	  \small The YonedaAI Collaboration, YonedaAI Research Collective\\
    58	  \small Chicago, IL\\
    59	  \small \texttt{matthew@yonedaai.com} \quad \url{https://yonedaai.com}}
    60	\date{October 2026}
    61	
    62	\begin{document}
    63	\maketitle
    64	
    65	\begin{abstract}
    66	Every governance system must decide who enforces its rules. This paper derives the coercive function from a single axiom about collective life, that some members sometimes have reason to break the rules, and compares how six regime types distribute it. A deterrence theorem shows that when the share of agents tempted to violate a rule exceeds the violation rate the collective can tolerate, compliance requires that violators' continuation payoffs fall because of their own conduct. A sanction regime of some kind is therefore necessary, but no particular institution is. Gossip, ostracism and coalition action against would-be dominants satisfy the lemma as well as police and armies do, and the ethnography of the Nuer, the Ju/'hoansi, Amazonian societies and Ostrom's commons documents these minimal forms. A second result shows why costly coercion at scale depends on provisioning or on shared norms of punishment. The paper then separates two properties of any enforcement apparatus: its conduct margin, how much more likely a violator is to be sanctioned than a complier, and its allegiance margin, how much more likely an opponent is to be sanctioned than a supporter. The two margins vary independently, so the necessity of coercion does not imply its capture. When capacity is limited, or opponents are targeted regardless of conduct, allegiance targeting raises the volume of coercion while weakening deterrence, which is why spending and arrest counts mismeasure coercive power. The main limitation is that the margins have not yet been estimated for any regime.
    67	\end{abstract}
    68	
    69	\section{Introduction}
    70	\label{sec:intro}
    71	
    72	Every polity must settle who enforces its rules, and polities differ more in how they distribute that task than in whether they perform it. A Ju/'hoansi camp answers it with teasing, gossip and avoidance \citep{lee2013,wiessner2005}. A Habsburg monarchy of the late sixteenth century answered it with contracted soldiers, garrisons that mutinied when unpaid, and the lay familiars of the Inquisition \citep{parker1972,thompson1976,kamen1997}. The German Democratic Republic answered it with a security ministry that ran a dense network of unofficial informants \citep{gieseke2014}. Sweden answers it with a police force under parliamentary control and a Parliamentary Ombudsman whose office was established with the Instrument of Government of 1809 \citep{jo2026}. These are different institutions. They discharge the same function.
    73	
    74	This paper is Part~V of a series that treats governance as six functions: allocation of resources ($\pF$), rule-making ($\pP$), interpretation ($\pJ$), legitimation ($\pI$), coercion ($\pC$) and production ($\pW$). The series takes its vocabulary and its formal objects from the working paper by \citet{largo2026hbs}, which describes a ``Hierarchy of the Beast System'' and borrows its name from the typological imagery of Revelation 13 and 17 to 18. The series thesis has two parts that must be kept apart. Proposition~A holds that the six functions and their dependencies are present in every functioning governance system; Part~VII proves it in general from six axioms. Proposition~B holds that the functions can become concentrated and integrated so that independent accountability fails. B is contingent and measurable, and A does not imply B. In this series ``Beast System'' names the universal six-function structure. It never labels a religion, a people, a profession, a regime or a person.
    75	
    76	The coercive pillar is the place where the distinction between A and B is easiest to blur. Coercion looks like domination even when it is accountable, and the existence of police, soldiers and prisons is often treated as evidence of capture. The source paper warns against this inference and proposes that coercive power be measured by discretionary and asymmetric deployment rather than by spending \citep[Section 4]{largo2026hbs}. The present paper gives that warning a formal basis.
    77	
    78	The argument has four steps. \Cref{sec:necessity} derives the coercive function from the axiom of defection (Ax5). A deterrence theorem shows that rule compliance above the rate set by agents' temptations requires a nonzero sanction regime, and a second result shows that, when sanctioning is costly, sanctioners themselves need provisioning, a norm of punishment, a higher-order sanction or a direct stake in deterrence. Both results are stated at the level of the role, not of any institution, and the ethnographic record of stateless societies shows the minimal forms they predict. \Cref{sec:comparative} compares the distribution of the function across six regime types with equal depth. \Cref{sec:mechanisms} introduces the distinction that carries the paper's argument about capture: the conduct margin of an enforcement apparatus, which measures how much it responds to what people do, and its allegiance margin, which measures how much it responds to whose side they are on. The two margins are separable, so a strong coercive function can coexist with zero capture. They trade off when coercive capacity is fixed or when opponents are targeted without regard to conduct, and then deterrence of ordinary rule-breaking weakens while the volume of coercion rises. \Cref{sec:measurement} turns these results into indicators and falsifiable hypotheses, and \cref{sec:revelation} reads Revelation 13 against Romans 13 as two typological images of the sword: one conditioned on conduct, the other on worship.
    79	
    80	The paper makes four contributions. It gives a necessity lemma for coercion that is explicit about the axiom it needs and about the counterexamples that would refute it. It derives the dependence of coercion on resources ($\pF \to \pC$) and on legitimation ($\pI \to \pC$) as a disjunction rather than an assertion, and states the condition on sanctioning technology under which the disjunction binds at scale. It defines the conduct and allegiance margins, proves their separability, which gives the pillar-level form of the claim that A does not imply B, and proves that they trade off under a capacity constraint. It supplies comparative static results for coup-proofing and for the political trajectory of dependent coercive corps, each with a stated falsifier.
    81	
    82	\section{The coercive pillar as a layer of the multiplex network}
    83	\label{sec:layer}
    84	
    85	\subsection{Shared objects}
    86	
    87	The series represents a polity at time $t$ as a directed multiplex network $G_t = (V_t, E_t)$ whose nodes are organizations or coherent actor groups and whose layers $A^m_t$ are indexed by the pillar set $\Mset = \{\pF, \pP, \pJ, \pI, \pC, \pW\}$, $M = |\Mset| = 6$ \citep{largo2026hbs}. An edge weight $a^m_{ij,t} \in [0,1]$ records the documented capacity of actor $i$ to constrain a feasible action of actor $j$ through mechanism $m$. A many-to-many role map assigns each actor the pillars in which it acts. Each actor holds a normalized control share $s^m_{i,t}$ in pillar $m$, with $\sum_i s^m_{i,t} = 1$, and the concentration of the pillar is the Herfindahl-Hirschman index $H_{m,t} = \sum_i (s^m_{i,t})^2$. Contestability $Q_{m,t} \in [0,1]$ summarizes transparency, appeal rights, institutional independence, competition and the credible replacement of decision makers. The source combines these into an illustrative index of unaccountable concentration,
    88	\begin{equation}
    89	U_t = \sum_{m \in \Mset} \omega_m H_{m,t}(1 - Q_{m,t}), \qquad \omega_m \ge 0, \quad \sum_m \omega_m = 1,
    90	\label{eq:U}
    91	\end{equation}
    92	whose weights must be preregistered. Cross-pillar integration $C_{mn,t} \in [0,1]$ measures the extent to which one coalition commands appointments, budgets, sanctions or agenda in both $m$ and $n$, and the integration statistic is $\Integ_t = \frac{2}{M(M-1)} \sum_{m<n} C_{mn,t}$, the mean over fifteen pairs. A capture link $(i \to j, m)$ requires privileged access or discretion, a resulting weakening of applicable accountability, and material evidence tying the asymmetry to an institutional output. A strong Beast System classification in the source's sense requires both high $U_t$ and high $\Integ_t$. All of these objects belong to the source paper; this Part uses them and does not redefine them. Part~VII formalizes them for the series.
    93	
    94	\subsection{Pillar-specific definitions}
    95	
    96	The coercive layer $A^{\pC}_t$ records capacities to impose costs on actors in response to their conduct or their status. The following definitions are owned by this Part.
    97	
    98	\begin{definition}[Coercive act, sanction and sanction function]
    99	\label{def:coercive-power:sanction}
   100	A \emph{coercive act} is a cost imposed on an agent by one or more other agents in response to the agent's conduct or status. The cost may be material (fines, seizure, detention, injury, death), relational (withdrawal of cooperation, exclusion from exchange, exile) or reputational (ridicule, gossip, loss of standing). A \emph{sanction} is a coercive act that responds to an observed or alleged violation of a rule. The \emph{sanction function} $\pC$ of a collective is the set of practices by which violations are detected and sanctions are decided and delivered. It is \emph{implemented} if, when violations occur and are detected, they are met with sanctions with non-trivial regularity, whether through designated offices, through coalitions formed for the occasion, or through dispersed individual responses.
   101	\end{definition}
   102	
   103	The definition is broad on the form of the cost and narrow on what makes a cost a sanction. Costs that fall on an agent regardless of what the agent does or is (a drought, a tax schedule applied equally to all) are not coercive acts. Costs that respond to status rather than to a rule violation, such as surveillance of an opposition party whose members have broken no rule, are coercive acts but not sanctions. The coercive layer records both, because the distinction between them is what \cref{def:coercive-power:margins} measures.
   104	
   105	\begin{definition}[Coercive control share]
   106	\label{def:coercive-power:share}
   107	The coercive control share $s^{\pC}_{i,t}$ of actor $i$ is its share of decision-relevant control over the deployment of coercive acts: the authority to order detection, detention, force or exclusion. Control over a deployment decision is attributed along the chain of command as follows. If actor $i$ can countermand a decision or remove the actor $j$ who takes it, and $j$ follows $i$'s directives in a share $\lambda_{ij} \in [0,1]$ of such decisions, then $i$ receives the share $\lambda_{ij}$ of the control attached to the decision and $j$ retains $1 - \lambda_{ij}$; the rule is applied recursively up the chain, so shares sum to one. Spending, headcount and equipment enter only insofar as they are subject to deployment decisions. We write $H^{\pC}_t := H_{\pC,t}$, and $H^{\pC}_{(1),t}$ for the concentration computed among the organizations immediately below the apex, each treated as a unit, before attribution to the apex.
   108	\end{definition}
   109	
   110	Two consequences of this definition matter later. A national army under one effective chain of command has its control attributed largely to the top of that chain, so its contribution to $H^{\pC}$ is large regardless of its size. A federation in which many local police forces answer to separately elected authorities has low $H^{\pC}$ even when total coercive capacity is high. The two concentration measures can diverge: a ruler who divides coercion among several organizations that all answer to the ruler lowers $H^{\pC}_{(1)}$ while $H^{\pC}$ stays high. Concentration in either sense is distinct from Weber's monopoly of legitimate violence, which Part~II (Section~2) uses to describe the relation between rule-making and enforcement. Weber's monopoly concerns the claim that only authorized agents may use force. It is a statement about the dependency of coercion on legitimation, not about who commands. A polity can make that claim successfully while dispersing command across many agencies, and a polity can concentrate command while failing to make the claim credible.
   111	
   112	\begin{definition}[Coercive contestability]
   113	\label{def:coercive-power:qc}
   114	Coercive contestability is $Q^{\pC}_t := Q_{\pC,t} = \sum_{k=1}^{6} \beta_k c_{k,t}$, with preregistered weights $\beta_k \ge 0$, $\sum_k \beta_k = 1$, and component scores $c_{k,t} \in [0,1]$ for:
   115	(1) appointment and removal of coercive commanders by an accountable authority distinct from the force itself;
   116	(2) judicial authorization of intrusive measures such as searches, interception and detention;
   117	(3) independent complaint and inspection bodies with access to records;
   118	(4) individual legal liability of agents for unlawful force;
   119	(5) protected refusal of manifestly unlawful orders; and
   120	(6) disclosure of coercive budgets and intelligence activities to a legislature or equivalent body.
   121	\end{definition}
   122	
   123	Component (1) is a contestability score, and it should not be confused with the integration coefficient $C_{\pP\pC}$, although the two are related. Part~II's appointment channel (Definition~2.8) assigns each coalition $S$ an appointment share $\alpha_{S,\pC}$, the weighted share of coercive offices whose holders $S$ can unilaterally appoint or remove. Proposition~6.5 of Part~II bounds the coalition-overlap measure of integration by this share. Let $\lambda_S$ be the average share of decisions in which $S$'s appointees follow its directives. Then $C^{\mathrm{ov}}_{\pP\pC} \ge \min\{s^{\pP}(S), \lambda_S\alpha_{S,\pC}\}$ for every coalition. If command runs only through appointment, the overlap is at most $\bar\lambda \max_S \alpha_{S,\pC}$ when loyalty is bounded by $\bar\lambda$, and it is zero when no coalition can unilaterally appoint or remove any coercive commander. The hypothesis that command runs only through appointment is restrictive for coercion. Budgets, business holdings and patronage give coalitions command over coercive organizations whose heads they do not formally appoint, as the Iranian case in \cref{sec:islamic} shows, so a low appointment share does not by itself imply low integration. A high score on component (1) lowers the appointment share of any single coalition, and Part~II's result then limits the integration that appointment alone can produce. Component (2) depends on the judicial contestability $Q^{\pJ}$ whose components Part~III defines (Definition~2.4).
   124	
   125	\begin{definition}[Sanction regime and deterrence margin]
   126	\label{def:coercive-power:regime}
   127	Consider agents $i \in N = \{1,\dots,n\}$ who in each period $t$ choose $v_{i,t} \in \{0,1\}$, where $v_{i,t} = 1$ means violating a given rule. Let $\sigma$ be a strategy profile and $h_t$ a history. For $v \in \{0,1\}$ let $W_i(h_t, v)$ be $i$'s expected discounted payoff from period $t$ onward, excluding the current temptation term, when $i$ chooses $v$ at $(t,h_t)$, follows $\sigma_i$ thereafter, and the other agents follow $\sigma_{-i}$ throughout. The \emph{deterrence margin} faced by $i$ at $(t,h_t)$ is
   128	\begin{equation}
   129	d_{i,t} = W_i(h_t, 0) - W_i(h_t, 1),
   130	\label{eq:margin}
   131	\end{equation}
   132	with discount factor $\delta \in [0,1)$. The \emph{sanction regime} of $\sigma$ is the map $(i, h_t) \mapsto d_{i,t}$. The regime is \emph{trivial} if $d_{i,t} \le 0$ at every reachable node.
   133	\end{definition}
   134	
   135	The margin compares two unilateral continuations, so it is defined at every node, including nodes at which $\sigma_i$ prescribes compliance and violation is off the path of play. It includes $i$'s own optimal future behavior, which may itself change after a violation; an agent excluded from cooperation, for example, faces different future margins from one in good standing. Under the payoff assumption of \cref{sec:necessity}, a violation affects $i$'s future only through other agents' responses, so the margin is zero whenever $\sigma_{-i}$ does not condition on $i$'s violations. A positive margin therefore requires that others respond to $i$'s violation in a way that lowers $i$'s payoff. The response may be a beating, a lawsuit, a boycott or a refusal to share meat. The definition does not ask who responds or whether they hold an office.
   136	
   137	\begin{definition}[Conduct and allegiance margins]
   138	\label{def:coercive-power:margins}
   139	Fix a \emph{reference rule set} $\mathcal{R}^0$: a preregistered set of rules in force whose content does not refer to political alignment, such as prohibitions of theft, assault and fraud. Let $v \in \{0,1\}$ indicate whether an agent violated a rule in $\mathcal{R}^0$ in the period, and let each agent carry an alignment $y \in \{\mathrm{al}, \mathrm{op}\}$, aligned with or opposed to the coalition that directs the coercive apparatus. Let $\psi(v,y) \in [0,1]$ be the per-period probability that an agent with violation status $v$ and alignment $y$ is the target of a coercive act of magnitude $\mu > 0$. The \emph{conduct margin} for alignment $y$ is $\Delta^{\mathrm{c}}(y) = \psi(1,y) - \psi(0,y)$. The \emph{allegiance margin} at violation status $v$ is $\Delta^{\mathrm{a}}(v) = \psi(v,\mathrm{op}) - \psi(v,\mathrm{al})$.
   140	\end{definition}
   141	
   142	The conduct margin is the enforcement of rules. The allegiance margin is the enforcement of loyalty. Rule-of-law ideals ask for $\Delta^{\mathrm{c}}(y) > 0$ and $\Delta^{\mathrm{a}}(v) = 0$: violators are targeted more than compliers, and opponents are treated like supporters with the same conduct. The reference rule set is what keeps the two margins distinct. If loyalty were itself a rule in $\mathcal{R}^0$, violation status and alignment would coincide for that rule and the allegiance margin would collapse into the conduct margin. Rules whose content is allegiance, such as an obligation to worship an image or a prohibition of opposition, are therefore excluded from $\mathcal{R}^0$. Coercive acts that enforce them appear in this framework as an allegiance margin, and their enactment is rule-making capture, which Part~II analyzes. A third pattern is distinct from both margins: \emph{arbitrariness}, in which $\Delta^{\mathrm{c}}(y)$ falls toward zero for every alignment, so that coercion responds neither to conduct nor to allegiance. \Cref{sec:mechanisms} shows that the conduct and allegiance margins can be chosen independently and analyzes the conditions under which they trade off.
   143	
   144	\subsection{Dependencies and integration}
   145	
   146	Two different relations connect the coercive pillar to the other five, and they must be kept apart. A \emph{dependency} $m \to \pC$ holds when the coercive function needs an output of pillar $m$ in order to operate. The \emph{integration coefficient} $C_{m\pC}$ of the source measures something else: the extent to which one coalition commands appointments, budgets, sanctions or agenda in both pillars. Dependencies are present in every polity, as Part~VII argues for the whole dependency structure; high integration is contingent. Dependency is evidence of Proposition~A, and integration is an ingredient of Proposition~B.
   147	
   148	The dependencies of coercion run as follows. Coercion must be provisioned ($\pF \to \pC$); Part~I owns the financing side of the fiscal-military state and the pair $C_{\pF\pC}$, including the fusion of financial and coercive control in one organization (Part~I, Section~6), and this Part treats the coercive side. Commanders are appointed ($\pP \to \pC$), and Part~II's appointment channel measures how far appointment produces integration. Sanctions follow determinations of wrongdoing ($\pJ \to \pC$); Part~III treats that pair, and its Proposition~3.6 shows that an effective judicial determination requires either legitimacy or an expected sanction for defiance, a dependency in the opposite direction. Sanctions must be recognized as legitimate to be distinguished from predation ($\pI \to \pC$); Part~IV defines the legitimation function (Definition~2.1) and treats the pair $C_{\pI\pC}$. The pair of coercion and production is the primary responsibility of this Part. Conscription is a dependency $\pW \to \pC$: it converts the labor time of the producing population into coercive capacity. Coerced labor is a dependency $\pC \to \pW$: it converts coercive capacity into production. The integration coefficient $C_{\pC\pW}$ is high only when one coalition commands both the coercive apparatus and the allocation of labor. \Cref{sec:cw} treats the pair.
   149	
   150	\section{Necessity of the coercive pillar}
   151	\label{sec:necessity}
   152	
   153	\subsection{The axiom of defection}
   154	
   155	Part~VII states six working axioms about collective life and derives one pillar from each. The axiom behind the coercive pillar is Ax5 (defection): some members sometimes break rules. Hobbes put the consequence in a sentence that has organized the subject since: ``covenants, without the sword, are but words'' \citep[ch.~17]{hobbes1651}. Hobbes drew from it the conclusion that a sovereign must hold the sword. The argument below accepts the premise and rejects that conclusion. Defection makes sanctioning necessary; it does not make a sovereign necessary.
   156	
   157	To give Ax5 content we state it as a claim about temptation rather than about observed violations. In each period agent $i$ privately observes a net temptation $\tau_{i,t} \in \mathbb{R}$, the gain from violating the rule minus every cost of violation that does not pass through other agents' responses. Internalized norms, guilt and shame lower $\tau_{i,t}$; so do any direct material costs of violation to the violator. Temptations are drawn independently across agents and periods from a distribution with cumulative distribution function $G$, and $p := \Pr(\tau_{i,t} > 0) = 1 - G(0)$ is the probability that an agent would gain from violation if nobody responded.
   158	
   159	A rule is useful to a collective only if violations stay below some rate. Call that rate the \emph{tolerance} $\theta \in [0,1)$: if the expected frequency of violations exceeds $\theta$ in the long run, the rule no longer coordinates behavior and the collective either abandons it or fails to persist. Formally, the rule is \emph{in force} under $\sigma$ if
   160	\[
   161	\limsup_{T \to \infty} \frac{1}{nT} \sum_{t=1}^{T} \sum_{i=1}^{n} \Pr(v_{i,t} = 1) \le \theta .
   162	\]
   163	
   164	\begin{assumption}[Ax5, defection, formal version]
   165	\label{ass:ax5}
   166	For the rule under consideration, $p > \theta$: the probability that an agent gains from violation in the absence of any response by others exceeds the violation rate the collective can tolerate.
   167	\end{assumption}
   168	
   169	The assumption is empirical, not logical, and it is stronger than the informal statement of Ax5. Observed violations are compatible with $p \le \theta$, since a collective may tolerate occasional violations of a rule that few are tempted to break. A population of saints, or one so thoroughly socialized that internal costs exceed every temptation, would have $p \le \theta$ for every rule. To connect the theorem below to Proposition~A, which concerns every functioning governance system, we therefore need a bridge.
   170	
   171	\begin{assumption}[Bridge]
   172	\label{ass:bridge}
   173	Every functioning governance system has at least one rule in force for which \cref{ass:ax5} holds.
   174	\end{assumption}
   175	
   176	The bridge carries the empirical content of the coercive pillar's place in Proposition~A. It is not true by definition: it would fail for a collective whose every rule is one that almost nobody is tempted to break, and \cref{sec:counter} states how to test it with a measurement of $p$ that is independent of sanction practices. We also assume that the agent's payoff depends on its own violation only through $\tau_{i,t}$ and through other agents' responses. Any direct effect of $i$'s violation on $i$'s own future (for example, overgrazing that also harms the violator's herd) is folded into $\tau_{i,t}$.
   177	
   178	\subsection{The deterrence lemma}
   179	
   180	\begin{lemma}[Deterrence]
   181	\label{lem:coercive-power:deterrence}
   182	Let $\sigma$ be a strategy profile in which every agent best-responds at every node. At $(t, h_t)$, agent $i$ violates if $\tau_{i,t} > d_{i,t}$ and complies if $\tau_{i,t} < d_{i,t}$. The probability that $i$ violates at that node is at least $1 - G(d_{i,t})$, with equality when $G$ has no atom at $d_{i,t}$ or ties are resolved toward compliance.
   183	\end{lemma}
   184	
   185	\begin{proof}
   186	By \cref{def:coercive-power:regime}, $i$'s expected payoff from period $t$ onward is $\tau_{i,t} + W_i(h_t,1)$ if it violates and $W_i(h_t,0)$ if it complies, where both continuations include $i$'s own optimal future play. The difference between violating and complying is $\tau_{i,t} - d_{i,t}$. A best-responding agent violates when this difference is positive and complies when it is negative. Because $\tau_{i,t}$ is drawn from $G$ independently of $h_t$, the probability of violation is at least $\Pr(\tau_{i,t} > d_{i,t}) = 1 - G(d_{i,t})$; ties at $\tau_{i,t} = d_{i,t}$ can only add violations.
   187	\end{proof}
   188	
   189	The lemma is a dynamic version of the deterrence condition in the economics of crime: a rational offender is deterred when the expected cost of punishment exceeds the gain \citep{becker1968}. In the simplest regimes $d_{i,t} = \pi\mu$, the product of the detection probability and the sanction magnitude. The general form \eqref{eq:margin} also covers sanctions that are not punishments in the legal sense: the loss of future cooperation in a repeated game, a damaged reputation in a trading network, or exclusion from the next meat distribution.
   190	
   191	\begin{theorem}[Necessity of the sanction function]
   192	\label{thm:coercive-power:necessity}
   193	Suppose \cref{ass:ax5} holds for a rule that is in force under a best-response profile $\sigma$. Let $\bar{\mathbb{E}}_T[x] = \frac{1}{nT}\sum_{t\le T}\sum_{i} \E[x_{i,t}]$ denote the expected average over agents and the first $T$ periods. Then
   194	\begin{equation}
   195	\liminf_{T\to\infty} \bar{\mathbb{E}}_T\bigl[G(d) - G(0)\bigr] \ge p - \theta > 0,
   196	\label{eq:necessity}
   197	\end{equation}
   198	and the long-run expected share of agent-periods with a strictly positive deterrence margin is at least $(p - \theta)/p$. In particular, the sanction regime of $\sigma$ is non-trivial.
   199	\end{theorem}
   200	
   201	\begin{proof}
   202	By \cref{lem:coercive-power:deterrence} and the law of iterated expectations, $\Pr(v_{i,t} = 1) \ge \E[1 - G(d_{i,t})]$, so the expected violation frequency up to $T$ is at least $\bar{\mathbb{E}}_T[1 - G(d)]$. Because the rule is in force, $\limsup_T \bar{\mathbb{E}}_T[1 - G(d)] \le \theta$, which gives $\liminf_T \bar{\mathbb{E}}_T[G(d)] \ge 1 - \theta$. Since $G(0) = 1 - p$, subtracting gives \eqref{eq:necessity}. For the second claim, each term satisfies $G(d_{i,t}) - G(0) \le p \cdot \mathbf{1}[d_{i,t} > 0]$, because the difference is zero when $d_{i,t} \le 0$ and at most $1 - G(0) = p$ otherwise. Hence $\liminf_T \bar{\mathbb{E}}_T[\mathbf{1}[d > 0]] \ge (p - \theta)/p$. A trivial regime would make the left side of \eqref{eq:necessity} non-positive, contradicting $p > \theta$.
   203	\end{proof}
   204	
   205	The theorem is stated in expectation. Realized frequencies converge to the same limits: the differences $v_{i,t} - \Pr(v_{i,t} = 1 \mid h_t)$ are bounded martingale differences, so by the strong law of large numbers for such differences their average tends to zero almost surely. The theorem is a necessity statement about a role, in the sense required by Part~VII: some agents must respond to violations in a way that costs the violator. It is silent on who those agents are, on whether they specialize, and on whether the cost is physical. It also gives two quantitative floors. The sanction regime must shift at least $p - \theta$ of probability mass from violation to compliance, and at least a fraction $(p-\theta)/p$ of agent-periods must face a positive margin. Sanctions that are too weak or too rarely threatened fail these bounds even when they exist on paper.
   206	
   207	A positive margin is a threat. \Cref{def:coercive-power:sanction} counts the function as implemented only if violations, when they occur, are actually met with sanctions. The two notions coincide whenever violations occur on the path of play. If $G$ has unbounded support, so that $\Pr(\tau > x) > 0$ for every $x$, then by \cref{lem:coercive-power:deterrence} violations occur with positive probability at every node, and a positive margin can be sustained only if they are in fact sanctioned with positive probability. A collective in which temptations are bounded and every agent is perfectly deterred would have the threat without observed sanctions; we know of no such collective, and \cref{tab:hardcases} records frequent sanctions in the societies closest to that ideal.
   208	
   209	\begin{corollary}[Magnitude]
   210	\label{cor:coercive-power:magnitude}
   211	If every agent faces the same margin $d = \pi\mu$, compliance at rate at least $1 - \theta$ requires $\pi\mu \ge G^{-1}(1 - \theta)$, where $G^{-1}$ is the right-continuous generalized inverse. A rise in temptation (a rightward shift of $G$) or a fall in detection $\pi$ must be offset by a larger sanction magnitude $\mu$ or a larger detection probability $\pi$; otherwise the collective must accept a higher tolerance $\theta$.
   212	\end{corollary}
   213	
   214	\begin{proof}
   215	With a common margin the violation rate is $1 - G(\pi\mu)$ when ties are resolved toward compliance, and $1 - G(\pi\mu) \le \theta$ holds if and only if $G(\pi\mu) \ge 1 - \theta$, which is $\pi\mu \ge G^{-1}(1-\theta)$ for the generalized inverse.
   216	\end{proof}
   217	
   218	\subsection{The second-order problem}
   219	
   220	A sanction is an act, and acts have costs. A Ju/'hoansi who criticizes a boastful hunter risks a quarrel; a Nuer kinsman who joins a feud risks his life; a police officer who arrests a powerful man risks a career. If nobody is willing to bear these costs, the deterrence margin collapses to zero and \cref{thm:coercive-power:necessity} fails. The following result states what must be true of sanctioners when sanctioning is costly.
   221	
   222	\begin{proposition}[Second-order enforcement]
   223	\label{prop:coercive-power:second-order}
   224	Suppose that delivering a sanction against $i$ requires an act by some agent $j \neq i$ at private cost $c_j > 0$, and that $d_{i,t} > 0$ in a best-response profile. Decompose the private return to $j$ of sanctioning into four terms: (a) a material transfer to $j$ conditional on sanctioning, such as pay, provisioning or a share of seized goods; (b) an intrinsic or social reward, such as esteem, a sense of duty or satisfaction from punishing; (c) avoidance of a sanction that $j$ would itself suffer for failing to sanction; and (d) $j$'s own share of the benefit of deterring $i$ and, through the example, third parties, weighted by the probability that $j$'s act is decisive. Then for some such $j$ the sum of (a) to (d) is at least $c_j$.
   225	\end{proposition}
   226	
   227	\begin{proof}
   228	The four terms are a decomposition of $j$'s payoff from its own sanctioning act: transfers conditioned on the act, $j$'s preferences over the act itself, others' responses to the act or its omission, and the act's effect on the behavior of $i$ and of others. We take this decomposition as the definition of the private return. If, for every $j$ whose act is required, the sum were below $c_j$, then not sanctioning would be a strict best response for each such $j$. No sanction would be delivered against $i$ for a violation at $(t,h_t)$, so $\sigma_{-i}$ would not respond to $v_{i,t}$ and $d_{i,t} = 0$, a contradiction.
   229	\end{proof}
   230	
   231	The proposition is a disjunction, and its interpretation needs care. Term (a) is the dependency $\pF \to \pC$: paid soldiers and police are provisioned out of resources that someone allocates. Term (b) is the dependency $\pI \to \pC$: a norm that makes punishing violators honorable, or a belief that the sanctioning authority is legitimate, supplies the reward. Term (c) is coercion applied to the coercers. In repeated games it can close the regress in equilibrium without transfers or intrinsic rewards: community-enforcement equilibria, in which those who fail to punish are themselves punished, need only that agents coordinate on the same punishment norm. Whether that coordination counts as legitimation is a question for Part~IV, and this paper does not settle it by definition. Term (d) needs no other pillar. The structure parallels Proposition~3.6 of Part~III, where an effective judicial determination needs legitimacy or sanction: in both cases the incoming dependency is a disjunction, which Part~VII must treat as a hyperedge of the dependency digraph rather than as separate arcs.
   232	
   233	The scale argument is conditional on the technology of sanctioning.
   234	
   235	\begin{corollary}[Costly sanctions at scale]
   236	\label{cor:coercive-power:scale}
   237	Suppose sanctions are costly to the sanctioner ($c_j \ge \underline{c} > 0$), the benefit of deterrence is shared across the collective so that the probability that any one sanctioner's act is decisive tends to zero as $n$ grows, and higher-order sanctions (term (c)) are absent. Then for $n$ large enough, a non-trivial sanction regime requires that term (a) or term (b) be positive for some sanctioner.
   238	\end{corollary}
   239	
   240	\begin{proof}
   241	Term (d) is bounded by the benefit of deterrence to $j$ times the probability that $j$'s act is decisive, and the second factor tends to zero, so for $n$ large enough term (d) is below $\underline{c}$. Term (c) is zero by hypothesis. \Cref{prop:coercive-power:second-order} then requires (a) or (b) to make up the difference.
   242	\end{proof}
   243	
   244	The hypotheses matter. When sanctions take the form of bilateral exclusion, as in the trading coalition discussed in \cref{sec:counter}, each excluder's act is decisive for its own relationship whatever the size of the collective, and the cost may be zero or negative: refusing to rehire a cheat can save money. Then the premise $c_j > 0$ fails, and coercion of this kind depends on no other pillar. The corollary applies to sanctions that are costly public goods, such as detaining, fighting or punishing strangers, which is the form that coercion against serious violations takes in large polities. Under that condition the sanction function at scale must be provisioned or legitimated. This is a micro-foundation for Tilly's coupling of war-making to extraction \citep{tilly1990} and for the military-fiscal bargains studied in \cref{sec:catholic}. Wherever term (a) dominates, the sanctioner's loyalty follows the paymaster, which is the root of the guardian problem treated in \cref{sec:mechanisms}. Experimental evidence supports term (b): subjects in public-goods experiments pay to punish free riders even when they cannot expect future gains from doing so, and cooperation is sustained when punishment is available \citep{fehr2002}. In a band of thirty, by contrast, a person harmed by a thief has a direct interest in stopping the theft and a real chance that the intervention matters, so term (d) can carry the load. This is the collective-action logic of \citet{olson1965} applied to enforcement.
   245	
   246	\subsection{Minimal forms in stateless and consensus societies}
   247	\label{sec:minimal}
   248	
   249	\Cref{thm:coercive-power:necessity} predicts that every persistent collective satisfying Ax5 has some sanction practice. It does not predict police. The next result shows that the deterrence margins the theorem requires can be produced with no specialized role at all. Whether the sanctioners are willing to produce them is the separate second-order question.
   250	
   251	\begin{proposition}[Minimal form]
   252	\label{prop:coercive-power:minimal-form}
   253	Consider $n$ agents who play the rule-compliance game in every period and also cooperate in a joint activity that yields each participant a per-period surplus $b > 0$. Let the profile be: every agent cooperates with every other agent who is not excluded; an agent who violates is excluded from cooperation for the next $L$ periods, and a violation by an excluded agent restarts the exclusion. Detection is perfect within the group. Then an agent with $r \in \{0, \dots, L\}$ future periods of exclusion remaining faces the deterrence margin
   254	\[
   255	d = b \sum_{k=r+1}^{L} \delta^k ,
   256	\]
   257	which equals $b\,\delta(1-\delta^L)/(1-\delta) > 0$ for an agent in good standing ($r = 0$). No agent holds a specialized sanctioning role, and with equal participation each agent's coercive control share is $1/n$, so $H^{\pC} = 1/n$.
   258	\end{proposition}
   259	
   260	\begin{proof}
   261	An agent with $r$ periods of exclusion remaining who complies at $t$ is excluded in periods $t+1, \dots, t+r$ and cooperates from $t+r+1$ onward. If it violates, it is excluded in periods $t+1, \dots, t+L$. The two continuations differ only in periods $t+r+1, \dots, t+L$, in which the complier receives $b$ and the violator does not, so $d = b\sum_{k=r+1}^{L}\delta^k$ by \eqref{eq:margin}. For $r = 0$ the sum is $b\,\delta(1-\delta^L)/(1-\delta)$. Exclusion is delivered by each agent withholding its own cooperation, so no agent holds authority over another's response, and under equal participation each holds an equal share $1/n$ of the decision-relevant control over coercive acts. Then $H^{\pC} = n \cdot (1/n)^2 = 1/n$.
   262	\end{proof}
   263	
   264	The margin is smallest, and equal to zero, for an agent already excluded for the full $L$ periods, which is why such profiles are usually combined with graduated sanctions or with longer exclusion for repeat violators. The proposition computes margins; it does not show that the profile is an equilibrium for the excluders. Each excluder forgoes its own surplus from cooperating with the violator, which is the second-order cost of \cref{prop:coercive-power:second-order}. Extending the profile so that anyone who cooperates with an excluded agent is also excluded supplies term (c). Whether the extended profile is an equilibrium depends on whether the surplus an agent would lose by being excluded from the whole group exceeds the surplus it forgoes by withholding cooperation from one violator, and we do not claim that it is an equilibrium in general. The ethnographic record suggests that terms (b) and (d) also operate: people are angered by violations, and in small groups each person's response matters.
   265	
   266	The ethnographic record of societies described as stateless or radically egalitarian supplies sanction practices of exactly this distributed kind. \Cref{tab:hardcases} summarizes them.
   267	
   268	\begin{table}[!htbp]
   269	\centering
   270	\small
   271	\caption{Minimal forms of the sanction function in societies commonly described as lacking coercive authority. The right column states the strongest reading on which the function is absent and the reason it does not hold.}
   272	\label{tab:hardcases}
   273	\renewcommand{\arraystretch}{1.15}
   274	\begin{tabularx}{\textwidth}{@{}L{2.3cm}YY@{}}
   275	\toprule
   276	Case & Documented sanction practice & Strongest counter-reading and reply \\
   277	\midrule
   278	Nuer \citep{evanspritchard1940} & Feud and the threat of retaliation by agnatic kin, settled by cattle compensation through the leopard-skin chief as mediator. & The leopard-skin chief has no power to compel. The sanction is held by kin groups, not by the mediator, so the function is present and the office is absent. \\
   279	Ju/'hoansi \citep{lee2013,marshall1976,wiessner2005} & Teasing, criticism, gossip and avoidance, with talk about norm violations recorded in camp conversations, and lethal violence in rare extreme cases. & This is the case most often cited as lacking hierarchy. The absence of an office is real, but the sanctions are frequent and documented. \\
   280	Amazonian societies \citep{clastres1987} & A chief who tries to command is abandoned or, in Clastres's reports, killed. & Clastres argues that these societies prevent power from separating from society. That supports the claim that concentration is contingent, while the group itself sanctions the chief. \\
   281	Foraging bands \citep{boehm1999,boehm2012} & Coalitions of subordinates use ridicule, disobedience, ostracism, exile and execution against would-be dominants. & Boehm calls the result a reverse dominance hierarchy. Egalitarianism is produced by sanctions rather than by their absence. \\
   282	Immediate-return societies \citep{woodburn1982} & Leveling mechanisms such as obligatory sharing, mockery and avoidance of anyone who claims authority. & Disputes are often resolved by moving away. Leaving costs the violator cooperation, which is a sanction when the violator values it. \\
   283	Commons \citep{ostrom1990,ostromdesign2010,cox2010} & Monitoring by users or accountable monitors, and graduated sanctions for those who break the rules. & Commons are often cited as order without a state. Ostrom's own design principles include monitoring and graduated sanctions. \\
   284	\bottomrule
   285	\end{tabularx}
   286	\end{table}
   287	
   288	Three features of the table deserve emphasis. The sanctions are distributed, so $H^{\pC}$ is low. They are rarely specialized: no person makes a living from them. And they are not mild. Boehm's reverse dominance hierarchy includes execution of persistent would-be dominants \citep{boehm1999}, and Lee recorded homicides among the Ju/'hoansi \citep{lee1979}. The egalitarian character of these societies does not come from the absence of coercion. It comes from the fact that coercion is held by the collective and directed against attempts to concentrate it. In the vocabulary of this series, the societies of \cref{tab:hardcases} have the coercive function (Proposition~A) and low concentration with high contestability (the negation of Proposition~B). Woodburn's phrase for the mechanism, institutions of leveling, describes a coercive pillar whose output is the prevention of capture \citep{woodburn1982}.
   289	
   290	The ethnographic evidence has known limits. Most of it was gathered after contact with states and markets, from groups living in marginal environments, and foraging societies vary more than the classic accounts suggest \citep{kelly1995}. \citet{graeber2021} argue that some societies moved seasonally between egalitarian and hierarchical arrangements, including temporary policing authority during collective hunts. If correct, this strengthens the present argument: the sanction function persists while its holders change with the season.
   291	
   292	\subsection{Counterexample attempts}
   293	\label{sec:counter}
   294	
   295	The strongest attempt to refute the necessity of coercion appeals to self-enforcing cooperation. Axelrod showed that reciprocal strategies can sustain cooperation without a central authority \citep{axelrod1984}. Greif showed that the eleventh-century Maghribi traders enforced agency contracts through a coalition in which cheated merchants were refused future employment by all members \citep{greif1993}. Edwards and Ogilvie dispute this reading and argue that the traders also relied on formal legal institutions \citep{edwards2012}; on either reading the case contains sanctions. Ellickson found that cattle ranchers in Shasta County settled disputes by neighborly norms rather than by law \citep{ellickson1991}. None of these is a counterexample. In each case an agent's continuation payoff depends on the agent's own past conduct: the reciprocator retaliates, the coalition refuses to deal, and the neighbor gossips or engages in self-help. Each mechanism is a sanction regime in the sense of \cref{def:coercive-power:regime}. What these cases refute is the Hobbesian inference from the need for sanctions to the need for a sovereign.
   296	
   297	A second attempt appeals to internalization. If socialization makes norm violation intrinsically costly, temptations may never be positive, and sanctions are unnecessary. The theorem accepts this as a logical possibility: internalization lowers $p$, and if $p \le \theta$ Ax5 fails and the coercive pillar is not derived for that rule. The bridge assumption claims that no functioning governance system achieves $p \le \theta$ for every rule it keeps in force. The societies that come closest, those of \cref{tab:hardcases}, are also the ones in which ethnographers record continual sanctioning talk \citep{wiessner2005}. Internalization and sanction are complements, not substitutes: shared norms reduce temptation and also supply the motive for punishing those who remain tempted (term (b) of \cref{prop:coercive-power:second-order}).
   298	
   299	A third attempt appeals to exit. Where dissatisfied members can simply leave, perhaps the collective needs no sanctions. Exit is a sanction when those who leave take with them something the violator valued. When exit costs the violator nothing, \cref{lem:coercive-power:deterrence} predicts violations at the unsanctioned rate $p$. A collective then persists only by relying on fewer rules that matter, which is what immediate-return foragers appear to do: with little storage there is less to steal and less to hoard \citep{woodburn1982}. Exit narrows the set of rules that require enforcement; it does not remove the function for the rules that remain.
   300	
   301	These replies define the falsifier, and the falsifier must not be immunized. The replies to the second and third attempts could be used to reclassify any compliant, unsanctioned collective as one with $p \le \theta$, which would make the necessity claim true by definition. To prevent this, the temptation share $p$ must be measured independently of the sanction practices it is used to explain, and before they are observed. Designs that offer members an unobserved opportunity to break a rule, so that no response by others is possible, measure the share who would violate in the absence of sanctions. Proposition~A for the coercive pillar is refuted by a persistent collective in which such a measurement gives $p > \theta$ for a rule in force, compliance is nonetheless above $1 - \theta$, and violators suffer no material, relational or reputational cost of any kind. A collective in which the measured $p$ is below $\theta$ for every rule in force refutes the bridge assumption instead. We found no documented case of either kind in the sources reviewed, and we know of no study that has carried out this measurement in a stateless society.
   302	
   303	\subsection{Functional necessity without functionalist explanation}
   304	
   305	The theorem claims the necessity of a function, not of an institution. That distinction answers the classic objection of \citet{hempel1959}: from the premise that a system needs some sanction practice, it does not follow that it needs a police force, because many functional equivalents can meet the need. \Cref{tab:hardcases} lists several. The theorem also makes no causal claim about why any particular polity has the coercive institutions it has. \citet{elster1979,elster1983} argued that explaining an institution by its beneficial effects requires a feedback mechanism from effects to institution. \Cref{thm:coercive-power:necessity} is a condition of persistence, not a functional explanation: collectives without a sanction regime do not keep rules in force, but the theorem says nothing about which sanction regime a collective adopts or why. That question belongs to the comparative analysis of \cref{sec:comparative}, where design varies with threats, finances and legitimating beliefs.
   306	
   307	\section{Literature on coercive power}
   308	\label{sec:literature}
   309	
   310	\subsection{Coercion and the making of states}
   311	
   312	Modern discussion of coercion begins with Weber's definition of the state as the human community that successfully claims the monopoly of the legitimate use of physical force within a territory \citep{weber1946,weber1978}. Part~II uses it where it treats the coupling of rule-making to enforcement. For the coercive pillar, the important word is ``claims''. Weber's definition concerns legitimacy, and \cref{sec:layer} has already separated it from command concentration.
   313	
   314	Tilly made coercion the engine of European state formation. Rulers who made war had to extract resources to pay for it, and the bargains they struck with those who held capital produced different state forms: coercion-intensive paths where rulers squeezed agrarian populations, capital-intensive paths where they borrowed from merchant cities, and capitalized-coercion paths in between \citep{tilly1990}. In an earlier essay Tilly compared war making and state making to organized crime, since the state sells protection against threats that it partly produces itself \citep{tilly1985}. The analogy is a heuristic, not an equivalence, and this paper treats it as a hypothesis about when coercion becomes capture. Karaman and Pamuk extended the fiscal side of the argument to show that the effect of warfare on state capacity depended on economic structure and regime type across Europe and the Ottoman Empire \citep{karaman2013}. The financing side of this literature belongs to Part~I; here the question is how the coercive apparatus that resulted was controlled.
   315	
   316	Mann distinguished despotic power, the range of actions rulers can take without negotiation with civil society, from infrastructural power, the capacity to penetrate society and implement decisions \citep{mann1984}. The distinction maps onto the two margins of \cref{def:coercive-power:margins}. A state with high infrastructural power can enforce rules widely (a large conduct margin is feasible); a state with high despotic power can direct enforcement as it pleases (a large allegiance margin is feasible). North, Wallis and Weingast described most of recorded history as limited-access orders in which specialists in violence agree not to fight because they share rents \citep{nww2009}. In the vocabulary of this series, such orders have high $C_{\pF\pC}$ by construction.
   317	
   318	\subsection{The guardian problem}
   319	
   320	If coercion is provisioned (term (a) of \cref{prop:coercive-power:second-order}), the agents who hold it can turn it against those who provision them. Civil-military relations theory is the study of this problem. Huntington proposed objective civilian control: a professional officer corps, autonomous in military matters and politically neutral \citep{huntington1957}. Janowitz replied that professionalism alone does not secure neutrality and that the military should be integrated into civilian society as a constabulary force \citep{janowitz1960}. Finer catalogued the forms of military intervention in politics \citep{finer1962}, and Huntington and Perlmutter described praetorian societies in which armed forces become ordinary political contestants \citep{huntington1968,perlmutter1969}. Feaver recast the relationship as a principal-agent problem in which civilians choose monitoring mechanisms and soldiers choose whether to work or shirk \citep{feaver1999,feaver2003}. Kohn emphasized that civilian control is a practice that must be exercised, not merely a constitutional provision \citep{kohn1997}.
   321	
   322	Authoritarian rulers face the guardian problem in a sharper form. Svolik showed that dictators face two separate problems: sharing power with the allied elites who help them rule, and controlling the masses they rule \citep{svolik2012}. Coercive agents are useful against the second problem and dangerous in the first. Quinlivan described the coup-proofing practices of Middle Eastern regimes: reliance on family, ethnic and religious loyalties, the creation of parallel military forces, and multiple overlapping internal security agencies \citep{quinlivan1999}. Pilster and B\"ohmelt found that coup-proofing reduced battlefield effectiveness in interstate wars between 1967 and 1999 \citep{pilster2011}. Greitens argued that the design of coercive institutions depends on whether rulers perceive their main threat as coming from elites or from the masses: elite threats favor fragmented and socially exclusive organizations, mass threats favor unified and inclusive ones, and these designs in turn shape patterns of state violence \citep{greitens2016}. Slater showed that elites who fear contentious mass politics may accept stronger coercive and extractive institutions as protection pacts \citep{slater2010}.
   323	
   324	\subsection{Repression and its limits}
   325	
   326	Repression is the use of coercion against political opponents, and it is the most direct observable form of the allegiance margin. Davenport's review defines repression broadly, from surveillance and bans to arrests, torture and mass killing, and organizes the field around the problem of how authorities use coercion against domestic challengers \citep{davenport2007}. Poe and Tate found in a 153-country analysis of the 1980s that democracy and participation in civil or international war had substantively important effects on repression of personal integrity rights \citep{poe1994}. Hill and Jones, using cross-validation rather than significance tests, found that few proposed explanations improve out-of-sample prediction much; democratic institutions predict some kinds of repression far better than others, and features of domestic legal systems perform well \citep{hill2014}. Wintrobe modeled dictators as trading off repression and the purchase of loyalty \citep{wintrobe1998}. Rejali documented a boundary case: democracies under public monitoring developed and exported torture techniques that leave few marks \citep{rejali2007}. Democracy constrains what coercers can be seen to do; it does not by itself eliminate the allegiance margin.
   327	
   328	Whether coercive agents carry out repression is not guaranteed. Bellin attributed the durability of Middle Eastern authoritarianism to the will and capacity of coercive apparatuses to repress, and after the Arab uprisings of 2011 she examined why some militaries defected and others did not \citep{bellin2004,bellin2012}. Albrecht and Ohl applied Hirschman's categories of exit, voice and loyalty to military behavior during unrest \citep{albrecht2016}, and Chenoweth and Stephan argued that nonviolent campaigns succeed in part by inducing defections among security forces \citep{chenoweth2011}. Gerschewski placed repression beside legitimation and co-optation as the three pillars of autocratic stability \citep{gerschewski2013}.
   329	
   330	\subsection{Policing, punishment and legitimacy}
   331	
   332	Within consolidated states, the main question about ordinary enforcement is why people comply. Tyler found that people obey the law more because they judge the authorities legitimate and the procedures fair than because they fear sanctions \citep{tyler1990}, and Jackson and colleagues found the same pattern in survey data on policing \citep{jackson2012}. These findings do not contradict \cref{thm:coercive-power:necessity}. They show that legitimation lowers the temptation distribution and supplies the motive for cooperation with enforcement, which in the present model shifts $G$ and strengthens term (b). Foucault traced the shift from spectacular punishment to the disciplinary prison and the surveillance it made possible \citep{foucault1977}. Pratt documented the comparatively low imprisonment rates and humane prison conditions of the Nordic countries and traced them to egalitarian welfare states, while warning that populist pressures could erode them \citep{pratt2008a,pratt2008b}.
   333	
   334	\subsection{Contribution}
   335	
   336	The literatures above mostly study either the necessity of order (from Hobbes to the economics of deterrence) or the dangers of coercive power (from civil-military relations to repression), and they rarely connect the two formally. The deterrence literature from \citet{becker1968} onward models the conduct margin and assumes enforcement is impartial. The repression literature studies the allegiance margin and largely takes the conduct margin for granted. This Part treats both as properties of a single sanction-probability function, which shows that the necessity of coercion and its capture are logically separate and empirically distinguishable. It also places the evidence of six regime types on a common scale, so that the comparison asks how each type distributes a function that all of them share.
   337	
   338	\section{Comparative analysis across six regime types}
   339	\label{sec:comparative}
   340	
   341	Each regime type below is asked the same five questions: which institutions hold the coercive function, how concentrated and contestable it is, how it depends on and is integrated with the other five pillars, what preserves accountability, and which capture episodes and checks are documented. Every claimed capture episode is held to the same standard, the three-part capture link of the source paper as applied to coercion in \cref{sec:mechanisms}, and each subsection reports at least one documented episode or standing risk and one documented check. The types are ideal types rather than mutually exclusive classes. The United States, for instance, is both a market-capitalist society and a secular democracy; each illustration is assigned to the type whose defining feature it shows. No numerical value of $U_t$ or $\Integ_t$ is reported for any real polity, because none has been coded under a preregistered scheme. Statements about concentration and integration are qualitative orderings that a coding exercise could confirm or overturn.
   342	
   343	\subsection{Market-capitalist societies}
   344	\label{sec:market}
   345	
   346	In market-capitalist societies the coercive function is held by public police forces, militaries and intelligence agencies under elected civilian authority, together with a private sector that manufactures weapons, supplies services and provides security for property. The defining feature for this pillar is the participation of private capital in producing coercive capacity and its interest in how that capacity is used.
   347	
   348	The link between private enterprise and coercion is older than industrial capitalism. Parrott showed that the armies of early modern Europe were raised and supplied to a large extent by military entrepreneurs who treated war as a business, and that this system was more effective than older accounts of state-led military modernization allowed \citep{parrott2012}. The modern form is the defense industry. In his farewell address of January 1961, President Eisenhower warned the American public against the acquisition of unwarranted influence by what he called the military-industrial complex \citep{eisenhower1961}. In the vocabulary of this series, the warning describes a possible capture link in which producers of coercive capacity gain privileged access to the decisions that set budgets, procurement and deployment, raising $C_{\pF\pC}$.
   349	
   350	Concentration differs sharply between the military and the police. Command of the armed forces is concentrated in a national executive, so the military contributes a large share to $H^{\pC}$, while legislative control of budgets divides authority over provisioning. Policing in the United States is dispersed across federal, state and local agencies, each answering to a different elected authority, which lowers $H^{\pC}$ for ordinary enforcement. The theory of civilian control was developed largely on the American case: Huntington's objective control, Janowitz's constabulary force and Feaver's agency model all address how elected civilians can command a professional military that they cannot fully monitor \citep{huntington1957,janowitz1960,feaver2003}. Accountability rests on component (1) of $Q^{\pC}$, appointment and removal by elected civilians; on components (2) and (4), judicial authorization of searches and the civil and criminal liability of agents; and on component (6), legislative scrutiny of budgets. Kohn argued that these provisions secure control only when civilians actually exercise them \citep{kohn1997}.
   351	
   352	The capture hypothesis specific to this regime type is that concentrated private interests shape the use of coercion. It meets the source paper's standard for a capture link only if three things are shown: privileged access by a private party, a weakening of the accountability that would otherwise apply, and material evidence that the access changed an enforcement outcome \citep{largo2026hbs}. Eisenhower's warning is evidence that a senior insider regarded the risk as serious; it is not evidence that capture occurred in any particular decision. A better documented episode comes from industrial conflict. The federal Commission on Industrial Relations reported in 1915 that ``practically every industrial State has at some relatively recent time permitted its institutions to be used by one party or the other to an industrial dispute (almost without exception the employers)''. It found that sheriffs in many counties deputized guards ``in the employment and pay of corporations'' and that militia were at times recruited from corporate guards and employees \citep[pp.~147 to 148]{cir1915}. Each element of the capture link is present in that finding: privileged access through deputization, the displacement of publicly accountable police by employer-paid agents, and enforcement outcomes against strikers. In the notation of \cref{def:coercive-power:margins}, the allegiance margin was indexed by the side a person took in an industrial dispute. The report was itself the check. A public commission with investigative powers documented the practice and recommended rules for the conduct of the militia \citep{cir1915}.
   353	
   354	For the present, following the source's proposal for narrow projects, the test of the military-industrial hypothesis is a preregistered sample of procurement decisions, not a selection of scandals. The rival explanation is that defense spending responds to external threats and that contractors compete for contracts under rules they do not control. Tilly's protection-racket analogy suggests a related hypothesis about ordinary policing: if public coercion protects some forms of property more than others, it transfers value to their owners \citep{tilly1985}. This predicts a positive allegiance margin indexed by economic position, which is an empirical question about arrest and prosecution rates conditional on conduct.
   355	
   356	\subsection{Communist party-states}
   357	\label{sec:communist}
   358	
   359	In communist party-states the ruling party holds the coercive function through security organs that answer to its leadership, through political officers embedded in the armed forces, and through the police and militia. In the Soviet case the line of security organs ran from the Cheka, founded as Lenin's political police \citep{leggett1981}, through its successors to the KGB, whose own successors after 1991 Knight traced \citep{knight1996}. In the German Democratic Republic the Ministry for State Security built an apparatus of full-time officers and unofficial informants that reached into local society \citep{gieseke2014,bruce2010,koehler1999}. In the People's Republic of China the party maintains command of the People's Liberation Army \citep{shambaugh2002}, and the police carry heavy burdens of stability maintenance that Scoggins and O'Brien describe from the officers' own perspective \citep{scoggins2016}.
   360	
   361	Concentration is high at the apex: the party leadership appoints and removes the heads of every coercive organization through the appointment channel analyzed in Part~II, so $H^{\pC}$ is high and the integration $C_{\pP\pC}$ is close to its maximum. Below the apex, however, the apparatus is divided, so $H^{\pC}_{(1)}$ is lower. Army, security service and police are separate organizations with separate chains of command, and party organs inside the army provide a further check. Colton's study of Soviet military politics found that the relationship between commissars and commanders was less a struggle between party and army than a structured form of military participation in politics, with the military's role largely confined to its own institutional concerns \citep{colton1979}. The division of the coercive apparatus is a form of counterbalancing, and the comparative static of \cref{prop:coercive-power:coup-proofing} applies to it.
   362	
   363	Integration with the ideological pillar is direct, since the same party commands both: political officers and party organizations inside the coercive organs make doctrinal loyalty part of the job, so $C_{\pI\pC}$ is high. Integration with production is also high. The Soviet camp system used forced labor on a large scale under the direction of the same party-state that set production plans \citep{applebaum2003,gregory2003}, so the dependency $\pC \to \pW$ and the integration $C_{\pC\pW}$ were both at the center of the Soviet economy for several decades. \Cref{sec:cw} returns to it. Contestability from outside the party is low: there is no independent judiciary able to review security operations, no competitive legislature able to audit them, and no free press able to expose them. The internal checks are party discipline and periodic purges. Purges can be used against security chiefs, but they are themselves exercises of the coercive function, so they check particular holders of power without raising $Q^{\pC}$.
   364	
   365	The terror of the late 1930s is the episode with the largest consequences, and it shows why arbitrariness and allegiance must be distinguished. The security organs were turned against party members, officers and ordinary citizens \citep{conquest1990}. Coercion fell on people who had broken no rule in any allegiance-neutral reference set, so the conduct margin collapsed across alignments, which is the arbitrariness of \cref{prop:coercive-power:arbitrary}. Whether the episode was also capture in the source's sense turns on the material-evidence step: how far the targeting was directed from the center against categories defined by political suspicion. That is exactly the question on which Conquest and revisionist historians disagree. Getty argued that the purges grew in part out of conflicts and confusion within the party apparatus rather than from a single central plan \citep{getty1985}. On Conquest's reading the episode meets all three conditions of a capture link; on Getty's it is closer to arbitrariness produced by an apparatus that the center did not fully control. Either way it is a failure of the coercive pillar, and the numbers on either side should be cited with that debate in view. The documented checks are of two kinds. Party supremacy over the military meant that the Soviet army did not seize power \citep{colton1979}. And the deterrent power of the apparatus rested on beliefs: when those beliefs shifted in 1989, regimes that had seemed secure fell with little warning \citep{kuran1991}.
   366	
   367	Reform socialism, which introduced markets inside party-states, did not change who held coercion. Kornai's account of the socialist system treats the reforms as changes in coordination mechanisms under continued party rule \citep{kornai1992}. For this reason the coercive pillar of market socialism as practiced is analyzed here rather than in the next subsection.
   368	
   369	\subsection{Social democracy and democratic socialism}
   370	\label{sec:socdem}
   371	
   372	In the social democracies of Northern Europe the coercive function is held by national police and armed forces under parliamentary control, with independent oversight bodies and a long tradition of citizen armies. The distinctive feature of this regime type for the coercive pillar is the combination of a centralized apparatus with high contestability and low reliance on punishment.
   373	
   374	Sweden illustrates the oversight structure. Its Parliamentary Ombudsman was established with the Instrument of Government of 1809 to supervise how judges and civil servants apply the law, and its supervision was later extended to local government \citep{jo2026}. Ombudsman supervision of public authorities contributes to components (3) and (4) of $Q^{\pC}$: complaints can reach an independent office with access to records, and officials can be held to account for unlawful conduct. Civilian control of the armed forces has varied with the perceived external threat. Hedlund's study of Swedish civil-military relations from 1984 to 2011 found that civilian control over the officer rank system and over professional officer education changed as perceptions of threat changed \citep{hedlund2011}.
   375	
   376	The Nordic countries are best known in this domain for penal moderation. Pratt described comparatively low imprisonment rates and humane prison conditions, rooted in egalitarian welfare states with high social trust, and warned that the pattern was under pressure from more punitive politics \citep{pratt2008a,pratt2008b}. Penal moderation is not the absence of the coercive function. \Cref{thm:coercive-power:necessity} requires a positive deterrence margin, not a large sanction magnitude, and \cref{cor:coercive-power:magnitude} shows that a high detection probability or a temptation distribution shifted toward compliance permits smaller sanctions. Legitimacy research suggests the second mechanism. Where people regard the police and courts as fair, they comply for reasons other than fear of punishment \citep{tyler1990,jackson2012}, which lowers the temptation distribution and strengthens the motive to cooperate with enforcement.
   377	
   378	The Nordic security services also supply documented episodes of the allegiance margin, and documented checks on it. In Norway the parliament appointed a commission to examine allegations of illegal surveillance. Its report of 1996, known by the name of its chair, found that the police security service had carried out widespread illegal political surveillance, particularly in the 1960s and 1970s, of individuals and organizations on the political left \citep{eos2026}. The response was a parliamentary oversight committee for all the secret services, established under a separate law of 1995 and elected for the first time in 1996 \citep{eos2026}. In Sweden the government appointed a commission in 1999 to examine the security services' surveillance of domestic political groups since 1945. Its directive records that the security police were barred in 1969 from registering a person solely on account of political views, that a general constitutional ban on such registration followed in 1977, and that military intelligence had registered communists from 1955 \citep{dir1999}. The commission reported in 2002 \citep{sou2002}. These episodes meet the capture-link test in the form the source requires: discretion over surveillance, use of it against political opponents who had broken no rule, and documentary evidence assembled by official inquiries. They also show the check working, though decades late: legislatures with investigative powers exposed the practices and created standing oversight.
   379	
   380	Dependencies and integration take an unusual form in this regime type. Conscript armies draw on the labor time of the whole population, so the dependency $\pW \to \pC$ runs through a universal obligation rather than through a professional caste, and it involves no integration of command over coercion and production. Appointment runs through parliament rather than through a party, and provisioning runs through the general budget of a high-tax state. Concentration $H^{\pC}$ is moderate to high because national police and military command are centralized, but contestability $Q^{\pC}$ is high on most components, so the contribution of the coercive pillar to $U_t$ in \eqref{eq:U} is small. This is the case that the source paper's Proposition~4 anticipates: concentration combined with high-quality review can coexist with competent services and low arbitrary sanctioning \citep{largo2026hbs}.
   381	
   382	Democratic socialism as a program, as distinct from the social-democratic welfare states that partly realized it, has no separate record of coercive institutions in the sources reviewed. Its claims about coercion are claims about how the institutions of the previous paragraphs should be governed, and they are evaluated by the same measures.
   383	
   384	\subsection{Islamic states}
   385	\label{sec:islamic}
   386	
   387	Islamic states are polities in which political legitimacy has been derived in significant part from religious law, and they differ widely: Sunni and Shi'i, dynastic and revolutionary, imperial and national. The coercive function has been held by caliphal armies paid through state registers, by corps of slave soldiers, by tribal levies, by dynastic guards and by revolutionary ideological forces. The common thread is not a single institution but a recurring problem: how a ruler whose legitimacy rests on religious law commands armed men whose loyalty may run to tribe, faction or their own corps.
   388	
   389	In the early caliphates soldiers were paid from the revenues of conquest through state registers, which made coercion directly dependent on the fiscal system \citep{kennedy2001}. From the ninth century, rulers came to rely on soldiers of slave origin, recruited from outside the societies they governed. Crone argued that military slavery offered rulers a source of armed force independent of the tribal and local elites whose loyalty they could not trust \citep{crone1980}, and Pipes traced the genesis of the system \citep{pipes1981}. The term slave soldier is the scholars' term for a legal status of military servitude that could lead to command, wealth and rule. It differs from chattel slavery in the household or the field, and this paper uses it only in that technical sense. The Mamluk sultanate that ruled Egypt and Syria from 1250 was governed by such soldiers and their successors \citep{irwin1986}.
   390	
   391	The Ottoman Empire built the most elaborate version. Its kul system recruited the sultan's servants, including the Janissary infantry, as personal dependents of the ruler, and Kunt traced how the households of these servants transformed provincial government between 1550 and 1650 \citep{kunt1983}. Agoston showed that the Ottoman state sustained a large military and a domestic weapons industry over centuries, adapting to European military change more successfully than older accounts of decline allowed \citep{agoston2005,agoston2014}. Tezcan dates a transformation of the Ottoman polity toward a more limited monarchy to the period from about 1580 to 1826 and treats the deposition and killing of Sultan Osman II in 1622, in which the sultan's own soldiers took part, as its turning point \citep{tezcan2010}. The pattern, a dependent corps recruited for loyalty that later acquires interests and power of its own, is the subject of \cref{prop:coercive-power:outsider}.
   392	
   393	In the Islamic Republic of Iran the coercive function is divided between the regular army and the Islamic Revolutionary Guard Corps, created after the revolution as an ideological guardian of the new order \citep{katzman1993,arjomand1988}. Buchta mapped the parallel institutions through which the Leader, the Guardian Council and the Guard share power \citep{buchta2000}. Wehrey and colleagues documented the Guard's expanding domestic political, economic and security roles \citep{wehrey2009}. Alfoneh argued that the Guard was transforming the state from theocracy into military dictatorship \citep{alfoneh2013}; his account comes from an advocacy institute and is best read alongside the more cautious RAND assessment. Either way, one organization commanding both coercive forces and large economic holdings raises the integration $C_{\pF\pC}$, and its ideological mandate under the same leadership raises $C_{\pI\pC}$.
   394	
   395	Saudi Arabia shows a dynastic version of counterbalancing. The kingdom maintains a regular army and a separate National Guard, a duality that Cordesman described and that Quinlivan treated as an instance of coup-proofing \citep{cordesman2003,quinlivan1999}. Gause placed it within the dynastic security structures of the Gulf monarchies \citep{gause1994}. The alliance between the Al Saud and the Wahhabi religious establishment supplies the legitimating side \citep{alrasheed2002}. The storming of the Grand Mosque in Mecca in November 1979 by Juhayman al-'Utaybi and his followers, whose origins and legacy Hegghammer and Lacroix reconstruct from fieldwork, challenged both arrangements at once: it contested the rulers' religious legitimacy and their coercive control of the holy places \citep{hegghammer2007}.
   396	
   397	Accountability in these polities has rested on different mechanisms from those of constitutional democracies. Where scholars of religious law held moral authority independent of the ruler, coercion depended on legitimation ($\pI \to \pC$) supplied by a group the ruler did not command, which is evidence of low rather than high $C_{\pI\pC}$ and a potential constraint on the ruler. Its strength varied across these polities and has not been measured on a common scale. Counterbalancing among forces is an internal check that protects rulers more than subjects. The capture-link test can be applied to the dependent-corps episodes. In the Mamluk case the corps used its control of deployment to take rule itself, and the change of rulers is documented \citep{irwin1986}. In the Ottoman case of 1622 the sultan's soldiers used their arms against the sultan, and Tezcan documents the lasting change in the distribution of power that followed \citep{tezcan2010}. Both are capture of the ruler by the coercive corps rather than capture of the coercive pillar by an outside coalition, which is the form \cref{prop:coercive-power:outsider} predicts. The documented checks are counterbalancing among separate forces and long periods in which the Ottoman state sustained and supplied its military establishment from the center \citep{agoston2005}.
   398	
   399	\subsection{Catholic monarchies}
   400	\label{sec:catholic}
   401	
   402	In the Catholic monarchies of early modern Europe royal authority was intertwined with the Church, and the coercive function was held by royal armies officered by nobles and by purchasers of commissions, by mercenary and contracted companies, by Swiss and other foreign troops, by the papal forces of the Papal States, and in Spain by the lay familiars who assisted the Inquisition. Internal diversity was considerable: Habsburg Spain, Bourbon France and the Papal States differed in fiscal structure, in their relations with Rome, and in the strength of their representative assemblies.
   403	
   404	Habsburg Spain fought across Europe with an army that depended on long supply lines and on credit. Parker's study of the Army of Flanders and the Spanish Road between 1567 and 1659 showed how logistics, finance and pay shaped military operations, and how unpaid troops mutinied \citep{parker1972}. Thompson examined how the Spanish crown governed war between 1560 and 1620, including its reliance on contractors and the sale of offices \citep{thompson1976}, and Elliott's survey places these developments in the history of the monarchy \citep{elliott1963}. Mutiny is a sanction by soldiers against their paymaster. It is also direct evidence for term (a) of \cref{prop:coercive-power:second-order}: when provisioning failed, so did the willingness of the coercers to coerce on the crown's behalf.
   405	
   406	Bourbon France built one of the largest armies in Europe. Lynn traced its growth between 1610 and 1715 \citep{lynn1997}. Rowlands showed that under Louis XIV royal service and private interest were intertwined: officers invested their own resources in their units, and the crown relied on that investment while trying to control it \citep{rowlands2002}. Venal commissions integrate finance and force at the level of the individual officer, who is both a creditor of the state and an agent of its force. Parker's thesis of a military revolution, in which new fortifications and tactics drove the growth of armies and states, frames these developments \citep{parker1988}, and Tilly's account of coercion and capital explains why monarchies with access to commercial credit could field such armies \citep{tilly1990}.
   407	
   408	The Papal States combined spiritual and temporal sovereignty. Their military forces, including the Swiss Guard, are documented from 1796 onward in Alvarez's history, which drew on the Guard's archive \citep{alvarez2011}; the verified sources reviewed for this paper do not cover the papal forces of earlier centuries. The Church also wielded sanctions of its own, including excommunication and interdict, which are ideological sanctions in the sense of \cref{def:coercive-power:sanction}: they impose relational and reputational costs and rely on belief for their force. In Spain the Inquisition drew on lay familiars who assisted its officials; Kamen's revisionist history of the Inquisition argues that its scale and severity were smaller than the older black legend held \citep{kamen1997}.
   409	
   410	Contestability came from three sources. Representative assemblies, where they retained the power to grant taxes, could limit the provisioning of armies. Contracted soldiers could refuse service when unpaid. And the Church could withhold legitimation, although in practice the crowns of Spain and France exercised considerable control over the churches within their kingdoms. Concentration of command rose over the period as monarchs replaced contracted forces with standing armies, while venality kept part of the control over units in private hands. Ertman's comparative account of state building shows how the timing of military competition shaped whether such states became patrimonial or bureaucratic \citep{ertman1997}. The capture-link test is harder to apply here than in the modern cases, because the documented material concerns the structure of command rather than its use against particular groups. What is documented is a standing risk: venal and contracted command made units partly private property, which gave their owners discretion over a public function. The documented check is the mutiny, in which soldiers withdrew coercion from a crown that failed to pay \citep{parker1972}, together with the fiscal power of estates where it survived and the limits that dependence on credit imposed on royal war-making.
   411	
   412	\subsection{Secular democracies}
   413	\label{sec:secular}
   414	
   415	In secular democracies authority is distributed among elected officials, courts and private institutions, and the legitimacy of coercion rests on constitutional law rather than on religious or party doctrine. The coercive function is held by professional armed forces under civilian command, police forces whose intrusive measures require judicial authorization, and intelligence services subject to legislative oversight. The defining feature for this pillar is the attempt to raise every component of $Q^{\pC}$ by constitutional design.
   416	
   417	The core mechanisms are civilian control of the military, judicial warrants for intrusive policing, and legislative oversight of intelligence. Kohn's account of how democracies control the military stresses that control is a practice of appointment, budget, doctrine and promotion that civilians must actively exercise \citep{kohn1997}. Born and Caparini compared the models by which democracies try to subject intelligence services to democratic control \citep{born2007}. These mechanisms map onto components (1), (2) and (6) of \cref{def:coercive-power:qc}, and their effectiveness depends on the judicial independence analyzed in Part~III. Janowitz's argument that a professional military should remain integrated with civilian society, rather than isolated from it, describes a further safeguard: a force that shares the values of those it might be ordered against is less likely to obey an order to target them \citep{janowitz1960}.
   418	
   419	The best documented capture episode in this regime type, and the best documented check, come from the same inquiry. In 1975 the United States Senate established a select committee, chaired by Frank Church, to study the government's intelligence operations. Its final report of April 1976 concluded that ``the Government has often undertaken the secret surveillance of citizens on the basis of their political beliefs, even when those beliefs posed no threat of violence or illegal acts on behalf of a hostile foreign power'' \citep[Book II, Part I, Section C]{church1976}. The committee examined the surveillance record against the lawful character of the targets' activities, which supplies the material evidence the capture-link test requires. In the notation of \cref{def:coercive-power:margins}, the finding describes a positive allegiance margin among non-violators: $\psi(0,\mathrm{op}) > \psi(0,\mathrm{al})$. The same report documents the check. A legislature with investigative powers exposed the practice, and a permanent Senate intelligence committee followed.
   420	
   421	Rejali's study of torture in democracies is the hard boundary case. Democracies that were monitored by a free press and human-rights organizations developed interrogation techniques that left few visible marks, so that public monitoring changed the form of abuse rather than ending it \citep{rejali2007}. Cross-national evidence nonetheless shows that democracy is associated with less repression of personal integrity rights \citep{poe1994}, although Hill and Jones caution that the relationship is stronger for some forms of repression than for others \citep{hill2014}. Coups are rare in consolidated democracies, and the dataset of Powell and Thyne permits this claim to be tested rather than assumed \citep{powell2011}.
   422	
   423	Concentration in secular democracies varies with constitutional structure. Unitary states with national police forces have higher $H^{\pC}$ than federal states with local forces, but both may have high $Q^{\pC}$. Integration with the political pillar is limited because civilian appointment is shared among elected bodies and constrained by professional norms of neutrality. The dependency on the judicial pillar runs through warrants and liability, and the dependency on legitimation runs through public acceptance of the constitution and of the police, which Tyler's research measures directly \citep{tyler1990}. The main risk specific to this type is that oversight bodies depend on information that the overseen agencies control, which is the principal-agent problem of Feaver's model applied to intelligence \citep{feaver2003}. The episodes of this subsection and of \cref{sec:socdem} show that risk realized for decades before legislatures intervened.
   424	
   425	\subsection{Summary across regimes}
   426	
   427	\Cref{tab:regimes} summarizes the comparison. Every regime type has the coercive function, as Proposition~A requires. They differ in who holds it, how concentrated and contestable it is, and how it depends on and is integrated with the other pillars.
   428	
   429	\begin{table}[!htbp]
   430	\centering
   431	\small
   432	\caption{The coercive function across six regime types. Orderings of concentration and contestability are qualitative and await preregistered coding.}
   433	\label{tab:regimes}
   434	\renewcommand{\arraystretch}{1.15}
   435	\begin{tabularx}{\textwidth}{@{}L{2.2cm}YYY@{}}
   436	\toprule
   437	Regime type & Principal holders of the function & Concentration, contestability and strongest integration & Documented capture episode or risk, and check \\
   438	\midrule
   439	Market-capitalist & Public police and militaries under elected civilians, with private producers of weapons and security services & Command of the military is concentrated, policing is dispersed, and the distinctive integration is between finance and coercion & Employer-paid deputies and militia in industrial disputes were documented in 1915, and a federal commission exposed the practice \\
   440	Communist party-state & Party-controlled security organs, armies with political officers, and police & Command is concentrated at the party apex with internal division among organs, contestability from outside the party is low, and the strongest integration is with political appointment & The terror of the late 1930s was arbitrary and possibly also capture, and party supremacy prevented military takeover \\
   441	Social democracy & National police and conscript or professional armies under parliamentary control & Concentration is moderate to high, contestability is high through ombudsmen and courts, and conscription makes coercion depend on universal service & Political surveillance by the security services was exposed by official inquiries, which led to standing parliamentary oversight \\
   442	Islamic states & Caliphal armies, slave-soldier corps, dynastic guards and revolutionary guards & Rulers counterbalance separate forces, and integration with legitimation and, in Iran, with finance is strong & Mamluk rule and the regicide of 1622 show corps becoming principals, and counterbalancing protected rulers more than subjects \\
   443	Catholic monarchies & Royal armies with venal officers, contracted companies, papal forces and Inquisition familiars & Concentration rose as standing armies replaced contractors, and finance and force were fused in venal command & The risk was units held partly as private property, and the checks were mutiny and the fiscal power of estates \\
   444	Secular democracy & Professional forces under civilian command, warrant-bound police and overseen intelligence services & Concentration varies with constitutional structure, and contestability is designed to be high on every component & Surveillance of citizens exposed by the Senate inquiry of 1975 to 1976 is both a capture episode and a check \\
   445	\bottomrule
   446	\end{tabularx}
   447	\end{table}
   448	
   449	\section{Mechanisms, failure modes and checks}
   450	\label{sec:mechanisms}
   451	
   452	\Cref{thm:coercive-power:necessity} requires that violators be sanctioned more than compliers. It says nothing about whom else the apparatus targets. This section shows that the coercive function and its capture are governed by different parameters, states when they nonetheless trade off, derives the main failure modes, and identifies the checks that interrupt them.
   453	
   454	\subsection{Conduct and allegiance}
   455	
   456	Return to the targeting probabilities $\psi(v,y)$ of \cref{def:coercive-power:margins}. In the one-period version of the deterrence lemma, an agent with alignment $y$ faces the margin $d = \Delta^{\mathrm{c}}(y)\mu$, so it violates a rule in $\mathcal{R}^0$ if $\tau > \Delta^{\mathrm{c}}(y)\mu$.
   457	
   458	\begin{proposition}[Separability]
   459	\label{prop:coercive-power:separability}
   460	Fix a magnitude $\mu > 0$ and a temptation distribution $G$. (i) The violation rate of agents with alignment $y$ is $1 - G(\Delta^{\mathrm{c}}(y)\mu)$, which depends on $\psi$ only through the conduct margin $\Delta^{\mathrm{c}}(y)$. (ii) For any common conduct margin $e \in (0,1)$ and any allegiance margin $x \in [0, 1-e]$, there is a targeting function with $\Delta^{\mathrm{c}}(\mathrm{al}) = \Delta^{\mathrm{c}}(\mathrm{op}) = e$ and $\Delta^{\mathrm{a}}(0) = \Delta^{\mathrm{a}}(1) = x$. In particular, the same deterrence of rule violations is compatible with a zero allegiance margin and with a positive one.
   461	\end{proposition}
   462	
   463	\begin{proof}
   464	Part (i) follows from \cref{lem:coercive-power:deterrence} with $d = \Delta^{\mathrm{c}}(y)\mu$, resolving ties toward compliance. For (ii), set $\psi(0,\mathrm{al}) = 0$, $\psi(1,\mathrm{al}) = e$, $\psi(0,\mathrm{op}) = x$ and $\psi(1,\mathrm{op}) = e + x$. All four values lie in $[0,1]$ because $x \le 1 - e$, and the margins are as stated.
   465	\end{proof}
   466	
   467	The proposition is the pillar-level form of the series claim that A does not imply B. Proposition~A, through \cref{thm:coercive-power:necessity}, constrains the conduct margin. A positive allegiance margin is a necessary ingredient of capture in the coercive pillar, and the theorem places no constraint on it. A collective can have an effective coercive pillar with no allegiance margin, and, if it has enough coercive capacity, the same effectiveness with a substantial one. The existence of police tells us nothing about which case obtains; only the margins do.
   468	
   469	A positive allegiance margin is not yet capture. Throughout this paper capture means the source's three-part capture link \citep{largo2026hbs}. A capture link $(i \to j, \pC)$ exists when actor $i$ has discretion over deployment, $j$'s allegiance margin is positive because of that discretion in a way that weakens accountability that would otherwise apply, and material evidence connects the two: for example, records showing that $i$'s orders produced surveillance, arrests or prosecutions of opponents who had broken no rule in $\mathcal{R}^0$, at rates that differ from those of supporters with the same conduct. The comparative section applies this test to each episode it discusses.
   470	
   471	\subsection{Arbitrary sanction and the capacity trade-off}
   472	
   473	The first failure mode occurs when coercion becomes insensitive to conduct within an alignment group. Its consequences are counterintuitive: coercion increases while the enforcement of rules decreases.
   474	
   475	\begin{proposition}[Arbitrary sanction]
   476	\label{prop:coercive-power:arbitrary}
   477	Fix an alignment $y$, hold $\psi(1,y)$ and $\mu$ fixed, and suppose $G$ has a density $g$. As $\psi(0,y)$ rises toward $\psi(1,y)$: (i) the conduct margin $\Delta^{\mathrm{c}}(y)$ falls to zero and the violation rate of the group rises toward the unsanctioned rate $p$; (ii) the expected number of coercive acts per member of the group,
   478	\[
   479	S(y) = \psi(0,y) + \Delta^{\mathrm{c}}(y)\bigl[1 - G(\Delta^{\mathrm{c}}(y)\mu)\bigr],
   480	\]
   481	is non-decreasing in $\psi(0,y)$.
   482	\end{proposition}
   483	
   484	\begin{proof}
   485	(i) $\Delta^{\mathrm{c}}(y) = \psi(1,y) - \psi(0,y)$ is decreasing in $\psi(0,y)$ and equals zero when the two probabilities are equal. The violation rate $1 - G(\Delta^{\mathrm{c}}(y)\mu)$ is non-increasing in $\Delta^{\mathrm{c}}(y)$, so it rises, and at $\Delta^{\mathrm{c}}(y) = 0$ it equals $1 - G(0) = p$. (ii) Write $\psi_0 = \psi(0,y)$ and $D = \psi(1,y) - \psi_0$. A member is targeted with probability $\psi_0$ if it complies and $\psi_0 + D$ if it violates, so $S = \psi_0 + D[1 - G(D\mu)]$. Differentiating in $\psi_0$, with $\partial D/\partial \psi_0 = -1$,
   486	\[
   487	\frac{\partial S}{\partial \psi_0} = 1 - \bigl[1 - G(D\mu)\bigr] + D\mu\, g(D\mu) = G(D\mu) + D\mu\, g(D\mu) \ge 0. \qedhere
   488	\]
   489	\end{proof}
   490	
   491	The proposition explains the source paper's proposal to measure coercive power by discretionary and asymmetric deployment rather than by spending \citep[Section 4]{largo2026hbs}. Arrest counts, prison populations and security budgets can all rise as the coercive apparatus stops responding to conduct. When the group in question is the opposition and $\psi(0,\mathrm{al})$ does not change, raising $\psi(0,\mathrm{op})$ toward $\psi(1,\mathrm{op})$ raises the allegiance margin $\Delta^{\mathrm{a}}(0)$ and lowers the conduct margin $\Delta^{\mathrm{c}}(\mathrm{op})$ at the same time. Targeting opponents without regard to their conduct therefore weakens deterrence among opponents, even though it increases coercion against them.
   492	
   493	Separability shows that an allegiance margin can be added without weakening deterrence, but only by adding coercive capacity. When capacity is fixed, the two margins trade off. Let the alignment groups have masses $n_{\mathrm{al}}, n_{\mathrm{op}} > 0$, and suppose that maintaining the targeting probabilities requires monitoring and enforcement capacity
   494	\[
   495	\Sigma(\psi) = \sum_{y} n_y\bigl[\kappa_1 \psi(1,y) + \kappa_0 \psi(0,y)\bigr] \le \bar{B},
   496	\]
   497	with $\kappa_0, \kappa_1 > 0$: capacity is spent on watching and acting against each status class in each group.
   498	
   499	\begin{proposition}[Capacity trade-off]
   500	\label{prop:coercive-power:capacity}
   501	Suppose the capacity constraint binds at $\psi$, and the apparatus raises $\psi(0,\mathrm{op})$ by $\varepsilon > 0$ without lowering $\psi(0,\mathrm{al})$, while $\bar{B}$ is unchanged. Then $\sum_y n_y \psi(1,y)$ must fall by at least $\kappa_0 n_{\mathrm{op}}\varepsilon/\kappa_1$. Consequently the conduct margin of at least one group falls, and that group's violation rate weakly rises.
   502	\end{proposition}
   503	
   504	\begin{proof}
   505	The new targeting function $\psi'$ must satisfy $\Sigma(\psi') \le \bar{B} = \Sigma(\psi)$. The change in the $\kappa_0$ terms is at least $\kappa_0 n_{\mathrm{op}}\varepsilon$, so the change in $\kappa_1\sum_y n_y\psi(1,y)$ is at most $-\kappa_0 n_{\mathrm{op}}\varepsilon$, which gives the bound. Since $\sum_y n_y \psi(1,y)$ falls, $\psi(1,y)$ falls for some $y$. For that $y$, $\psi(0,y)$ has not fallen, so $\Delta^{\mathrm{c}}(y)$ falls, and by \cref{prop:coercive-power:separability}(i) its violation rate $1 - G(\Delta^{\mathrm{c}}(y)\mu)$ weakly rises.
   506	\end{proof}
   507	
   508	The two propositions together give the paper's claim about allegiance-conditioned coercion its exact scope. Allegiance targeting weakens the enforcement of ordinary rules when coercive capacity is limited, and when opponents are targeted without regard to their conduct. When a regime adds capacity to fund an allegiance margin while keeping its conduct margins, separability says that rule enforcement can survive; what changes is the cost of opposition. Wintrobe's model of the dictator's trade-off between repression and the purchase of loyalty reaches related conclusions by a different route \citep{wintrobe1998}.
   509	
   510	A second failure mode concerns supporters. If $\psi(1,\mathrm{al})$ falls toward $\psi(0,\mathrm{al})$, supporters enjoy impunity: their conduct margin falls and their violation rate rises toward $p$. Allegiance-conditioned enforcement can therefore damage compliance on both sides of the political line. Total coercive activity may rise or fall in this case, depending on the relative size of the two groups and on how much the targeting of opponents increases.
   511	
   512	\subsection{The guardian problem and coup-proofing}
   513	
   514	Term (a) of \cref{prop:coercive-power:second-order} makes the loyalty of provisioned coercers depend on their paymaster, and a coercive apparatus strong enough to protect a ruler is strong enough to remove the ruler. Rulers respond by dividing coercive capacity among several organizations that watch one another. The following comparative static states when they divide more.
   515	
   516	\begin{proposition}[Coup-proofing]
   517	\label{prop:coercive-power:coup-proofing}
   518	A ruler chooses the number $k \in \{1, \dots, K\}$ of independent armed organizations. Let $c(k)$ be the probability of a successful coup, non-increasing in $k$, and $e(k)$ any function giving the loss of external military effectiveness. The ruler minimizes $f(k; r) = r\, c(k) + e(k)$, where $r > 0$ is the expected cost of losing office to a coup relative to the stakes of external effectiveness. If $r' > r$, then the largest minimizer at $r'$ is at least as large as the largest minimizer at $r$.
   519	\end{proposition}
   520	
   521	\begin{proof}
   522	Let $k$ be the largest minimizer at $r$ and $k'$ the largest minimizer at $r'$, and suppose $k' < k$. Optimality gives $f(k; r) \le f(k'; r)$ and $f(k'; r') \le f(k; r')$. Adding the two inequalities and cancelling the $e$ terms yields $(r' - r)\bigl(c(k') - c(k)\bigr) \le 0$. Since $k' < k$ and $c$ is non-increasing, $c(k') \ge c(k)$, and since $r' > r$ the product is non-negative, so it is zero and $c(k') = c(k)$. Then $f(k; r') - f(k'; r') = e(k) - e(k') = f(k; r) - f(k'; r) \le 0$, so $k$ also minimizes $f(\cdot\,; r')$. This contradicts the choice of $k'$ as the largest minimizer at $r'$, since $k > k'$.
   523	\end{proof}
   524	
   525	The proof uses no property of $e$; the effectiveness cost matters for the level of $k$ but not for the direction of the comparative static. The parameter $r$ is the salience of the elite threat: it rises with the probability that the ruler's own armed allies could and would remove the ruler, which can be proxied by recent coup attempts in the polity or its neighbors \citep{powell2011}, and it falls with the stakes of interstate war. The model has one threat parameter and does not represent mass threat. It therefore captures the fragmentation side of Greitens's argument, that elite threats produce fragmented coercive institutions \citep{greitens2016}, but not the prediction that mass threats produce unified and intrusive ones. It is consistent with Quinlivan's account of coup-proofing in Middle Eastern regimes \citep{quinlivan1999} and with the finding of Pilster and B\"ohmelt that coup-proofing has battlefield costs \citep{pilster2011}. It describes the Saudi army and National Guard, the Iranian army and Revolutionary Guard, and the division of Soviet coercion among army, security service and police. In democracies the analogous counterweights are civilian ministries, separate services and judicial oversight. The comparative static would be falsified by evidence that the number and independence of armed organizations are unrelated to measured elite threat once external threat is held constant.
   526	
   527	Coup-proofing raises $k$ but does not raise $Q^{\pC}$. Counterweights protect the ruler from the guardians; they do not protect citizens from the ruler. In a party-state or a dynastic monarchy, all $k$ organizations may answer to the same apex. Then the concentration $H^{\pC}_{(1)}$ among the organizations below the apex falls, while $H^{\pC}$, which attributes their control to the apex under \cref{def:coercive-power:share}, stays high, and so does the integration $C_{\pP\pC}$. This is the reason the source paper requires both $U_t$ and $\Integ_t$ for a strong classification: a measure of dispersion below the apex would miss the concentration above it.
   528	
   529	\subsection{Dependent corps and the outsider strategy}
   530	
   531	Rulers have long tried to solve the guardian problem by recruiting coercers who have no independent social base: foreigners, captives, slaves or men cut off from their families. The Abbasid and Mamluk slave soldiers, the Ottoman kul and the papal Swiss Guard are instances. The following proposition states why the strategy works at first and why it tends to fail later.
   532	
   533	\begin{proposition}[Dependent corps]
   534	\label{prop:coercive-power:outsider}
   535	A corps receives compensation $w_t \le \bar{w}$ per period from a ruler whose fiscal capacity bounds $\bar{w}$. The corps accumulates capacity $Z_t$: arms, offices, property, marriages and local recruitment. The value to the corps of seizing control is $\Gamma(Z_t)$, non-decreasing in $Z_t$, and an attempt costs $\chi > 0$. The corps remains subordinate in period $t$ only if $\sum_{k \ge 0}\delta^k w_{t+k} \ge \Gamma(Z_t) - \chi$. If $Z_t$ is non-decreasing and $\lim_{t\to\infty}\Gamma(Z_t) > \bar{w}/(1-\delta) + \chi$, then there is a finite $T$ such that for all $t \ge T$ the corps is not subordinate, unless the ruler lowers $Z_t$, raises $\chi$, or raises the ceiling $\bar{w}$.
   536	\end{proposition}
   537	
   538	\begin{proof}
   539	The left side of the subordination condition is at most $\bar{w}/(1-\delta)$. Because $\Gamma(Z_t)$ is non-decreasing in $t$ and its limit exceeds $\bar{w}/(1-\delta) + \chi$, there is a finite $T$ with $\Gamma(Z_T) - \chi > \bar{w}/(1-\delta)$, and the inequality persists for all $t \ge T$. The condition can be restored only by changing one of $Z_t$, $\chi$ or $\bar{w}$.
   540	\end{proof}
   541	
   542	The proposition is simple, and its interest lies in what it explains. It treats an attempt as successful; a probability of success below one lowers the expected value of seizure and delays $T$ without changing the logic. Recruiting outsiders lowers $Z_0$: a corps with no kin, land or local allies gains little from seizing power because it cannot rule alone. This is the logic Crone attributed to the adoption of military slavery \citep{crone1980}. Over time the corps acquires exactly the assets that raise $Z_t$. The value of seizing a polity is bounded by what the polity produces, so the threshold condition, not unbounded growth, is what matters: the corps must come to value control more than the most the ruler can pay. The ruler's three countermeasures correspond to the three escape clauses. Rotation of commanders, prohibition of property holding and periodic purges keep $Z_t$ low. Counterweights of the kind analyzed in \cref{prop:coercive-power:coup-proofing} raise the cost $\chi$ of an attempt. Fiscal expansion raises $\bar{w}$. The Mamluks, who became rulers of Egypt and Syria \citep{irwin1986}, and the Janissaries, whose part in the deposition and killing of Osman II in 1622 marked a lasting change in Ottoman politics \citep{tezcan2010}, are the paradigm cases. The proposition also applies to modern forces whose economic holdings grow, since business activity raises $Z_t$ directly. This is the mechanism behind the concern that the economic expansion of Iran's Revolutionary Guard increases its political autonomy \citep{wehrey2009,alfoneh2013}. In democracies the analogous measures are term limits for commanders, prohibitions on military business and civilian control of promotions.
   543	
   544	\subsection{Coercion and production}
   545	\label{sec:cw}
   546	
   547	The pair of coercion and production is the primary responsibility of this Part among the fifteen cross-pillar pairs. The dependencies run in both directions, and the integration coefficient $C_{\pC\pW}$ measures something narrower than either.
   548	
   549	From production to coercion ($\pW \to \pC$), every army and police force consumes labor time. Conscription takes it directly from the producing population as an obligation. Professional forces take it through wages paid from taxes. Slave-soldier systems took it by acquiring people as a resource. The mode of recruitment shapes accountability: a conscript army is drawn from the whole population and depends on its consent, while a professional or outsider force depends on its paymaster. This is a further reason why term (a) of \cref{prop:coercive-power:second-order} carries political consequences.
   550	
   551	From coercion to production ($\pC \to \pW$), sanctions can compel work. The categories must be kept distinct, and this paper uses the bondage spectrum of Part~VI (Definition~2.4). Wage labor and taxation leave lawful mobility and personal ownership with the producer; the sanctions behind them are the general law of contract and of revenue. Serfdom ties the producer to land or lord. Compelled state labor, which includes corv\'ee, labor drafts and penal labor, is compelled by sanction for a term. Chattel slavery makes the person property. Only the last three are forms of bondage, and the coercive pillar is directly engaged in each of them. The Soviet camp system combined penal labor with economic planning on a scale that made coercion a direct input to production \citep{applebaum2003,gregory2003}. The series uses the language of bondage beyond these legal categories only in the disciplined, metaphorical sense of the source paper \citep{largo2026hbs}. Part~VI treats the production side of the pair, including the exit and voice that producers can use against dependence (Part~VI, Definition~2.5).
   552	
   553	A high value of $C_{\pC\pW}$ means that the same coalition commands both the coercive apparatus and the allocation of labor. In the extreme case, the deterrence margin of \cref{def:coercive-power:regime} is applied to failures to work. Proposition~B for this pair requires such integration together with a positive allegiance margin, so that the obligation to work falls more heavily on opponents, and with low contestability. The Gulag combined all three, since the same party-state directed the security organs that filled the camps and the plans that used their labor, and political offenses were among the grounds of confinement \citep{applebaum2003}. Universal conscription in a democracy with high $Q^{\pC}$ involves the dependency $\pW \to \pC$ but neither high integration nor an allegiance margin.
   554	
   555	\subsection{Checks that interrupt transmission}
   556	
   557	The source paper's second proposition holds that effective independent review and voice reduce the probability that attempted capture yields persistent unreviewable outcomes \citep{largo2026hbs}. In the coercive pillar the checks act on the margins directly. Judicial authorization of intrusive measures raises the evidentiary threshold for coercive acts, which lowers $\psi(0,y)$ for everyone and so raises the conduct margin. Independent complaint bodies make a positive allegiance margin visible and therefore costly. Individual liability of agents for unlawful force raises the private cost of arbitrary coercion for the coercers themselves. Protected refusal of unlawful orders introduces a veto at the point of execution: when soldiers or police refuse to fire on peaceful crowds, the allegiance margin is cut off at its source, which is the mechanism that Chenoweth and Stephan and Albrecht and Ohl identify in security-force defection \citep{chenoweth2011,albrecht2016}.
   558	
   559	These checks have small-scale analogues. Ostrom's design principles for long-enduring commons include monitors who are accountable to users and graduated sanctions that begin with small penalties \citep{ostrom1990,ostromdesign2010}. Graduated sanctions keep the magnitude $\mu$ proportional to the violation, which limits the damage when $\psi(0,y)$ is positive by mistake. Accountability of monitors to users is a small-scale version of component (1) of $Q^{\pC}$. The reverse dominance hierarchy of foraging bands is a check of the same kind: the collective holds the sanction and directs it against those who try to concentrate it \citep{boehm1999}. Madison's argument that ambition must be made to counteract ambition is the constitutional statement of the same principle \citep{madison1788}.
   560	
   561	Checks can fail. Each depends on another pillar: judicial authorization on judicial independence (Part~III), complaints and refusal on legitimating beliefs (Part~IV), and appointments on the political pillar (Part~II). Capture of any of these pillars by the coalition that commands coercion removes the corresponding check. This is the mechanism by which high cross-pillar integration $\Integ_t$ turns a concentrated coercive pillar into an unaccountable one, and it is why the coercive pillar cannot be assessed in isolation.
   562	
   563	\section{Measurement and hypotheses}
   564	\label{sec:measurement}
   565	
   566	\subsection{Indicators}
   567	
   568	The source paper rejects military expenditure as a measure of coercive power, and \cref{prop:coercive-power:arbitrary} shows why sanction counts are equally misleading. The objects that matter are the control share, the components of contestability and the two margins. \Cref{tab:indicators} lists indicators for each.
   569	
   570	\begin{table}[!htbp]
   571	\centering
   572	\small
   573	\caption{Indicators for the coercive pillar. Each indicator measures a defined object of \cref{sec:layer} or \cref{sec:mechanisms}; none has been coded for a real polity under a preregistered scheme.}
   574	\label{tab:indicators}
   575	\renewcommand{\arraystretch}{1.15}
   576	\begin{tabularx}{\textwidth}{@{}L{3.0cm}YY@{}}
   577	\toprule
   578	Object & Indicator & Main threat to validity \\
   579	\midrule
   580	Control share $s^{\pC}_i$ and concentrations $H^{\pC}$ and $H^{\pC}_{(1)}$ & Share of heads of coercive organizations whom a single actor can appoint and remove, with the share of their decisions that follow that actor's directives, coded from statutes and records & Formal authority may differ from practice, so appointment records should be checked against actual removals \\
   581	Contestability $Q^{\pC}$ & Scores for the six components of \cref{def:coercive-power:qc}, coded from law and from the reports of oversight bodies & Oversight bodies may exist on paper without access to records or power to compel testimony \\
   582	Conduct margin $\Delta^{\mathrm{c}}(y)$ & Difference in targeting rates between violators and non-violators, measured against an independent record of conduct such as victimization surveys or audits & The apparatus that sanctions also records violations, so official data cannot measure conduct independently \\
   583	Allegiance margin $\Delta^{\mathrm{a}}(v)$ & Difference in targeting rates between opponents and supporters with the same conduct under the reference rules, for example in surveillance, arrest or prosecution & Opponents and supporters may differ in unobserved conduct, which requires matched designs or outcome tests \\
   584	Repression & Standards-based scales coded from human-rights reports, as in Poe and Tate and in Hill and Jones, and V-Dem civil-liberties indicators & Reporting improves where monitoring improves, which can make better-governed states appear more repressive \\
   585	Coups and counterweights & Coup attempts from the Powell and Thyne dataset, and the number of armed organizations outside the regular military chain of command & Counterweights are often secret or nominally civilian \\
   586	Integration $C_{\pF\pC}$ & Share of coercive organizations' revenue from their own business holdings & Holdings are often opaque and require primary documents \\
   587	Dependency $\pC \to \pW$ and integration $C_{\pC\pW}$ & Legal scope of conscription and of forced and penal labor, and the share of output produced under them & Legal categories may not match practice \\
   588	\bottomrule
   589	\end{tabularx}
   590	\end{table}
   591	
   592	The allegiance margin is the hardest object to measure and the most important. Two designs are available. The first compares the treatment of opponents and supporters with matched conduct, as recorded by a source independent of the coercive apparatus: a court that acquits, a victimization survey, or an archive of the targets' own activities. The Senate inquiry of 1975 to 1976 is an example of the third kind, since it compared the surveillance record with the lawful character of the targets' activities \citep{church1976}. The second design adapts the outcome test from the economics of discrimination. Knowles, Persico and Todd showed that if officers maximize successful searches, the rate at which searches find contraband should be equal across groups in the absence of bias \citep{knowles2001}. The analogous test here compares the rate at which coercive acts against opponents and supporters are later upheld by independent review. A systematically lower rate for opponents indicates that opponents are targeted on weaker evidence, which is a positive $\Delta^{\mathrm{a}}(0)$. The test has two known weaknesses. Average rates can differ even without bias if the marginal cases differ across groups, the problem of infra-marginality, so the test is informative only under the conditions that Knowles, Persico and Todd state for equilibrium search behavior. And the independent review may itself be captured, which is the concern of Part~III; the test is only as good as the judicial contestability $Q^{\pJ}$ of the reviewing body. Repression scales \citep{poe1994,hill2014} and V-Dem indicators \citep{coppedge2011} measure the level of coercion against citizens but do not separate the two margins, so they are useful as outcomes rather than as measures of capture. Coup data \citep{powell2011} measure the guardian problem directly.
   593	
   594	\subsection{Hypotheses with falsifiers}
   595	
   596	The hypotheses below refine the source paper's generic hypotheses H1 to H6 for the coercive pillar; the parent hypothesis is given in brackets. Each states the result that would count against it.
   597	
   598	\begin{description}
   599	\item[HC1 (threat environment; H3).] Rulers who face greater elite threat build fragmented and loyalty-based coercive institutions; rulers who face mass threat build unified and intrusive ones \citep{greitens2016}. The first half is motivated by \cref{prop:coercive-power:coup-proofing}; the second half is not modeled here. Falsifier: the number and independence of armed organizations are unrelated to measured elite threat once external threat is controlled.
   600	\item[HC2 (coup-proofing trade-off; H6).] Coup-proofing lowers coup success and also lowers military effectiveness \citep{quinlivan1999,pilster2011}. Falsifier: higher counterbalancing shows no association with battlefield performance in comparable conflicts.
   601	\item[HC3 (security-force defection; H5).] The cohesion, composition and professionalism of security forces predict whether they defect or repress during mass unrest \citep{bellin2012,albrecht2016,chenoweth2011}. Falsifier: these characteristics show no association with defection across episodes.
   602	\item[HC4 (fiscal basis; H3).] Coercive organizations financed by taxation of a broad population face more contestation than those financed by resource rents or foreign transfers \citep{tilly1990,karaman2013}. The hypothesis is motivated by term (a) of \cref{prop:coercive-power:second-order}, which ties the loyalty of coercers to their provisioning, but the proposition does not model contestation. Falsifier: the source of financing is unrelated to $Q^{\pC}$.
   603	\item[HC5 (dependent corps; H2).] Corps recruited for dependence become political actors as their capacity grows, unless rulers rotate, disperse or replace them, raise the cost of an attempt, or raise pay \citep{crone1980,pipes1981}. This is the empirical counterpart of \cref{prop:coercive-power:outsider}. Falsifier: outsider corps whose holdings and offices grow remain subordinate without such countermeasures.
   604	\item[HC6 (democracy and repression; H1).] Democracy and judicial independence reduce repression \citep{poe1994,hill2014}. Falsifier: no effect once civil conflict is controlled. Rejali's evidence on torture in democracies is a boundary case that the hypothesis must accommodate \citep{rejali2007}.
   605	\item[HC7 (integration of finance and force; H2).] Business activity by coercive organizations raises $C_{\pF\pC}$ and lowers coercive contestability. Falsifier: military business holdings are unrelated to $Q^{\pC}$. Rival explanation: such holdings supply public goods or substitute for an inadequate budget.
   606	\item[HC8 (checks; H1 and H4).] Independent complaint mechanisms and judicial authorization lower the allegiance margin. Falsifier: the margin is unchanged after such reforms are introduced. As the source paper warns, reforms can raise reported abuses by making them visible, so reporting effects must be separated from changes in behavior \citep{largo2026hbs}.
   607	\item[HC9 (volume and compliance; H1).] When coercive acts against opponents rise while independently measured compliance with the reference rules falls among opponents, and neither changes among supporters with matched conduct, the allegiance margin is rising and the conduct margin among opponents is falling. The comparison with supporters is needed because a temptation shock, such as a crime wave, also raises both violations and coercive acts with no allegiance margin at all; it affects both groups. This is the pattern \cref{prop:coercive-power:arbitrary} predicts when opponents are targeted without regard to conduct. Falsifier: in documented episodes of politically selective repression, opponents' compliance with the reference rules does not fall relative to supporters'.
   608	\item[HC10 (separability; H6).] Across polities, measured conduct margins and measured allegiance margins are weakly correlated: the absolute correlation is below a preregistered threshold, for example 0.5, and polities with a conduct margin above the sample median include some with an allegiance margin indistinguishable from zero. This is the empirical content of \cref{prop:coercive-power:separability} and of the claim that A does not imply B. Falsifier: the two margins are so strongly correlated that effective rule enforcement is never observed without a positive allegiance margin, which would suggest that capture accompanies coercion structurally.
   609	\end{description}
   610	
   611	HC10 is the hypothesis whose failure would most damage this paper's argument. The separability proposition shows that the margins can vary independently, but if they never do in practice, the distinction between necessity and capture would be logical rather than empirical.
   612	
   613	\section{Revelation 13 as typological image}
   614	\label{sec:revelation}
   615	
   616	The series reads Revelation typologically. It does not identify the beast, the mark or Babylon with any present government, party, technology, person, religion or institution. Futurist readings that make such identifications have a long history of failure \citep{boyer1992,fuller1995,mcginn1998}, and historicist readings that identified the beast with particular churches belong to the history of polemic \citep{kovacs2004}. In the preterist reading, which supplies the historical anchor, the first beast is Roman imperial power and the setting is the imperial cult of the cities of Asia Minor \citep{bauckham1993,friesen2001,koester2014}. In the typological reading the series adopts, the beast is a recurring pattern of power that claims ultimate loyalty \citep{bauckham1993,wink1992}. The use of the image here is an interpretive claim of this project, not a settled exegetical result.
   617	
   618	Revelation 13 is saturated with coercion. The first beast is given authority to make war: ``it was given unto him to make war with the saints, and to overcome them: and power was given him over all kindreds, and tongues, and nations'' (Rev.~13:7, KJV). Its worshippers ask, ``Who is like unto the beast? who is able to make war with him?'' (13:4). The second beast exercises the authority of the first and causes the earth to worship it, and it brings an image to life that should ``cause that as many as would not worship the image of the beast should be killed'' (13:15). The chapter ends with the mark, without which ``no man might buy or sell'' (13:17). Kraybill has read these passages against the economic life of the province, in which participation in trade was entangled with the imperial cult \citep{kraybill1996}.
   619	
   620	The coercive content of 13:15 has a precise structure in the terms of \cref{def:coercive-power:margins}. Inside the image's own order, refusal to worship is the violation. But that rule is a rule whose content is allegiance, which is exactly the kind of rule excluded from the reference set $\mathcal{R}^0$. Measured against allegiance-neutral rules, the death sanction of 13:15 is conditioned entirely on allegiance and not at all on conduct, and the enactment of the rule is itself an image of rule-making capture. The economic exclusion of 13:16 to 17 has the same structure: the cost falls on those without the mark, whatever they have done. The text's image of the beast is, among other things, an image of a coercive apparatus whose conduct margin has been displaced by an allegiance margin.
   621	
   622	Another canonical text, Paul's letter to the Romans, describes the coercive function with the opposite conditioning. Romans 13 says that ``rulers are not a terror to good works, but to the evil,'' and that the ruler ``beareth not the sword in vain: for he is the minister of God, a revenger to execute wrath upon him that doeth evil'' (Rom.~13:3 to 4, KJV). The sword in Romans 13 is conditioned on conduct: it falls on the one who does evil. The sword in Revelation 13 is conditioned on worship: it falls on the one who will not bow. Readers have long asked how the two chapters fit together. Yoder read Romans 13 as a call to be subject to authorities whose power is itself ordered under God, not as an endorsement of whatever those authorities do \citep{yoder1972}, a reading that leaves room for Revelation's judgment on authority that demands worship. In the framework of this paper the chapters describe the same function under different parameters. Romans 13 describes a sanction regime with a positive conduct margin and no allegiance margin. \Cref{thm:coercive-power:necessity} shows that every persistent collective needs the first property; the second is what distinguishes accountable coercion from captured coercion. Revelation 13 describes a regime in which the allegiance margin has displaced the conduct margin, and \cref{prop:coercive-power:arbitrary,prop:coercive-power:capacity} show why such a regime weakens the enforcement of the ordinary rules it claims to protect. The reading is consistent with the series distinction between Proposition~A, the universal function, and Proposition~B, its contingent capture.
   623	
   624	The same chapter addresses those who suffer coercion: ``He that leadeth into captivity shall go into captivity: he that killeth with the sword must be killed with the sword. Here is the patience and the faith of the saints'' (13:10). The KJV wording follows one textual tradition. The verse echoes Jeremiah 15:2, its wording varies among manuscripts, and many modern editions and commentators read it as a call to the faithful to accept captivity and death rather than as a statement that the coercer will meet the same fate; the commentaries discuss the problem at this verse \citep{aune1998b,koester2014}. Because the reading is uncertain, this paper draws no institutional inference from it. On either reading the verse rules out armed resistance by the faithful, which places the response it commends in endurance and witness rather than in counter-coercion.
   625	
   626	Revelation 17 supplies a closer image of the guardian problem of \cref{sec:mechanisms}. The ten kings ``have one mind, and shall give their power and strength unto the beast'' (17:13), and yet ``the ten horns which thou sawest upon the beast, these shall hate the whore, and shall make her desolate and naked'' (17:16). Allies who lend their force to a power can turn it against the power they served. Read typologically, the passage is an image of the dependent-corps dynamic of \cref{prop:coercive-power:outsider}, in which those who supply coercion come to hold it on their own account. This too is the project's interpretive claim, not an exegetical result. Collins argued that the Apocalypse addressed a perceived crisis and offered its readers a form of catharsis \citep{collins1984}, and Thompson questioned whether the Domitianic period saw the systematic persecution that older readings assumed \citep{thompson1990}. On either reading the text's concern is not the existence of the sword but its direction: whom it strikes, and why.
   627	
   628	\section{Objections and scope conditions}
   629	\label{sec:objections}
   630	
   631	The first objection is that the necessity theorem is trivial, since any cost can be called a sanction. The definition blocks this. A sanction must respond to an observed or alleged violation, and the deterrence margin is the difference in continuation payoffs between compliance and violation. Both are observable. The theorem can fail, and \cref{sec:counter} states the observation that would refute it, together with the requirement that temptation be measured independently of sanction practices so that no compliant collective can be reclassified after the fact. Its content lies in Ax5 and the bridge assumption, which are empirical claims about temptations, and in the conclusion that the sanction regime must shift at least $p - \theta$ of probability mass toward compliance.
   632	
   633	The second objection is Hobbesian: order requires a sovereign with a monopoly of force, so the distributed sanctions of stateless societies are a primitive stage rather than a functional equivalent. The evidence of \cref{tab:hardcases} is against this. Distributed sanctions sustained order in many societies over long periods, and the theorem requires a positive margin, not a concentrated holder. The objection has more force at scale, and \cref{prop:coercive-power:second-order} explains why: as collectives grow, term (d) weakens and coercion must be provisioned or legitimated. That is a reason for specialization, not for concentration without accountability.
   634	
   635	The third objection comes from the opposite direction. Clastres, Graeber and Wengrow, and anarchist anthropology more generally, argue that hierarchy is not inevitable and that many societies deliberately prevented the emergence of coercive authority \citep{clastres1987,graeber2021}. The paper agrees about hierarchy and disagrees about coercion. The societies they describe sanction those who try to command; they do not lack sanctions. Their achievement is a coercive pillar with $H^{\pC}$ near $1/n$ and contestability near one, which is the clearest empirical evidence that Proposition~B is contingent.
   636	
   637	The fourth objection is Marxian: coercion in class societies serves the ruling class, so the distinction between rule enforcement and capture is ideological. The framework accommodates the claim as a hypothesis about the allegiance margin. If coercion is applied more heavily to one class for the same conduct, or if the rules themselves were written to protect one class's property, the first case shows up as a positive allegiance margin indexed by class, and the second belongs to the analysis of rule-making in Part~II. In both cases the claim becomes measurable. What the framework rejects is the inference from the existence of police to the existence of class capture, which is the inference from A to B.
   638	
   639	The fifth objection is the public-goods objection: concentrated coercion provides security, which benefits everyone, so it should not be treated with suspicion. The paper accepts the premise. The source paper's fourth proposition and hypothesis H6 state that concentration with high-quality review can coexist with competent services and low arbitrary sanctioning \citep{largo2026hbs}, and the social democracies of \cref{sec:socdem} are the leading illustration. The margins framework is designed to distinguish this case from capture rather than to presume either.
   640	
   641	Five scope conditions limit the results. The capacity trade-off of \cref{prop:coercive-power:capacity} rests on a linear capacity constraint, which is an assumption about the technology of enforcement rather than a derived result. The model treats a single rule with a binary violation decision, while real polities enforce many rules of different gravity, and the tolerance $\theta$ differs among them. Equilibria in repeated games are typically multiple, so the theorem establishes that some sanction regime is necessary without predicting which one arises. The analysis concerns enforcement inside a polity; war between polities enters only through the guardian problem and the fiscal basis of coercion. And the conduct margin can be measured only with an independent record of conduct, which is often unavailable precisely where capture is most likely.
   642	
   643	\section{Conclusion}
   644	\label{sec:conclusion}
   645	
   646	Every governance system settles who enforces its rules, because when members are sometimes tempted to break rules, compliance requires that violators' prospects fall because of what they did. The answer need not be a police force. Gossip, ridicule, ostracism and coalition action satisfy the deterrence lemma as well as armies do, and the societies that seem to lack coercion are those in which the collective holds it and directs it against concentration. The function is universal; its institutional form varies.
   647	
   648	Capture in the coercive pillar requires a change in what coercion responds to. The conduct margin measures enforcement of rules, the allegiance margin measures enforcement of loyalty, and the two are separable: necessity constrains the first and is silent about the second. They trade off when coercive capacity is limited, and when opponents are targeted without regard to their conduct; under those conditions the volume of coercion rises while compliance with ordinary rules falls. That is why spending and arrest counts mismeasure coercive power, and why the contrast between Romans 13 and Revelation 13 concerns the direction of the sword rather than its existence.
   649	
   650	The comparison of six regime types shows the same function distributed in different ways: through private producers and civilian control in market-capitalist societies, party organs in communist states, ombudsmen, parliamentary oversight and conscription in social democracies, counterbalanced and dependent corps in Islamic states, venal and contracted command in Catholic monarchies, and constitutional oversight in secular democracies. What remains uncertain is the size of the two margins in any of them. Measuring the allegiance margin, against an independent record of conduct, is the task on which the empirical claims of this paper depend.
   651	
   652	\begin{thebibliography}{200}
   653	\small
   654	\setlength{\itemsep}{2pt}
   655	
   656	\bibitem[\'Agoston(2005)]{agoston2005}
   657	\'Agoston, G\'abor (2005). \emph{Guns for the Sultan: Military Power and the Weapons Industry in the Ottoman Empire}. Cambridge University Press.
   658	
   659	\bibitem[\'Agoston(2014)]{agoston2014}
   660	\'Agoston, G\'abor (2014). Firearms and Military Adaptation: The Ottomans and the European Military Revolution, 1450-1800. \emph{Journal of World History} 25(1):85-124. doi:10.1353/jwh.2014.0005.
   661	
   662	\bibitem[Al-Rasheed(2002)]{alrasheed2002}
   663	Al-Rasheed, Madawi (2002). \emph{A History of Saudi Arabia}. Cambridge University Press. doi:10.1017/cbo9780511993510.
   664	
   665	\bibitem[Albrecht and Ohl(2016)]{albrecht2016}
   666	Albrecht, Holger and Ohl, Dorothy (2016). Exit, Resistance, Loyalty: Military Behavior during Unrest in Authoritarian Regimes. \emph{Perspectives on Politics} 14(1):38-52. doi:10.1017/S1537592715003217.
   667	
   668	\bibitem[Alfoneh(2013)]{alfoneh2013}
   669	Alfoneh, Ali (2013). \emph{Iran Unveiled: How the Revolutionary Guards Is Transforming Iran from Theocracy into Military Dictatorship}. AEI Press.
   670	
   671	\bibitem[Alvarez(2011)]{alvarez2011}
   672	Alvarez, David (2011). \emph{The Pope's Soldiers: A Military History of the Modern Vatican}. University Press of Kansas.
   673	
   674	\bibitem[Applebaum(2003)]{applebaum2003}
   675	Applebaum, Anne (2003). \emph{Gulag: A History}. Doubleday.
   676	
   677	\bibitem[Arjomand(1988)]{arjomand1988}
   678	Arjomand, Said Amir (1988). \emph{The Turban for the Crown: The Islamic Revolution in Iran}. Oxford University Press.
   679	
   680	\bibitem[Aune(1998)]{aune1998b}
   681	Aune, David E. (1998). \emph{Revelation 6-16}. Word Biblical Commentary 52B. Thomas Nelson.
   682	
   683	\bibitem[Axelrod(1984)]{axelrod1984}
   684	Axelrod, Robert (1984). \emph{The Evolution of Cooperation}. Basic Books.
   685	
   686	\bibitem[Bauckham(1993)]{bauckham1993}
   687	Bauckham, Richard (1993). \emph{The Theology of the Book of Revelation}. Cambridge University Press. doi:10.1017/cbo9780511819858.
   688	
   689	\bibitem[Becker(1968)]{becker1968}
   690	Becker, Gary S. (1968). Crime and Punishment: An Economic Approach. \emph{Journal of Political Economy} 76(2):169-217. doi:10.1086/259394.
   691	
   692	\bibitem[Bellin(2004)]{bellin2004}
   693	Bellin, Eva (2004). The Robustness of Authoritarianism in the Middle East: Exceptionalism in Comparative Perspective. \emph{Comparative Politics} 36(2):139-157. doi:10.2307/4150140.
   694	
   695	\bibitem[Bellin(2012)]{bellin2012}
   696	Bellin, Eva (2012). Reconsidering the Robustness of Authoritarianism in the Middle East: Lessons from the Arab Spring. \emph{Comparative Politics} 44(2):127-149. doi:10.5129/001041512798838021.
   697	
   698	\bibitem[Boehm(1999)]{boehm1999}
   699	Boehm, Christopher (1999). \emph{Hierarchy in the Forest: The Evolution of Egalitarian Behavior}. Harvard University Press. doi:10.2307/j.ctvjf9xr4.
   700	
   701	\bibitem[Boehm(2012)]{boehm2012}
   702	Boehm, Christopher (2012). \emph{Moral Origins: The Evolution of Virtue, Altruism, and Shame}. Basic Books.
   703	
   704	\bibitem[Born and Caparini(2007)]{born2007}
   705	Born, Hans and Caparini, Marina (eds.) (2007). \emph{Democratic Control of Intelligence Services: Containing Rogue Elephants}. Ashgate.
   706	
   707	\bibitem[Boyer(1992)]{boyer1992}
   708	Boyer, Paul (1992). \emph{When Time Shall Be No More: Prophecy Belief in Modern American Culture}. Harvard University Press (Belknap). doi:10.2307/jj.41480279.
   709	
   710	\bibitem[Bruce(2010)]{bruce2010}
   711	Bruce, Gary (2010). \emph{The Firm: The Inside Story of the Stasi}. Oxford University Press.
   712	
   713	\bibitem[Buchta(2000)]{buchta2000}
   714	Buchta, Wilfried (2000). \emph{Who Rules Iran? The Structure of Power in the Islamic Republic}. Washington Institute for Near East Policy and Konrad Adenauer Stiftung.
   715	
   716	\bibitem[Chenoweth and Stephan(2011)]{chenoweth2011}
   717	Chenoweth, Erica and Stephan, Maria J. (2011). \emph{Why Civil Resistance Works: The Strategic Logic of Nonviolent Conflict}. Columbia University Press.
   718	
   719	\bibitem[Clastres(1987)]{clastres1987}
   720	Clastres, Pierre (1987). \emph{Society against the State: Essays in Political Anthropology}. Translated by Robert Hurley. Zone Books. doi:10.2307/j.ctv1595m3p.
   721	
   722	\bibitem[Collins(1984)]{collins1984}
   723	Collins, Adela Yarbro (1984). \emph{Crisis and Catharsis: The Power of the Apocalypse}. Westminster Press.
   724	
   725	\bibitem[Colton(1979)]{colton1979}
   726	Colton, Timothy J. (1979). \emph{Commissars, Commanders, and Civilian Authority: The Structure of Soviet Military Politics}. Harvard University Press. doi:10.4159/harvard.9780674497443.
   727	
   728	\bibitem[Conquest(1990)]{conquest1990}
   729	Conquest, Robert (1990). \emph{The Great Terror: A Reassessment}. Oxford University Press.
   730	
   731	\bibitem[Coppedge et~al.(2011)]{coppedge2011}
   732	Coppedge, Michael and Gerring, John and Altman, David and Bernhard, Michael and Fish, Steven and Hicken, Allen and Kroenig, Matthew and Lindberg, Staffan I. and McMann, Kelly and Paxton, Pamela and Semetko, Holli A. and Skaaning, Svend-Erik and Staton, Jeffrey and Teorell, Jan (2011). Conceptualizing and Measuring Democracy: A New Approach. \emph{Perspectives on Politics} 9(2):247-267. doi:10.1017/S1537592711000880.
   733	
   734	\bibitem[Cordesman(2003)]{cordesman2003}
   735	Cordesman, Anthony H. (2003). \emph{Saudi Arabia Enters the Twenty-First Century: The Military and International Security Dimensions}. Praeger.
   736	
   737	\bibitem[Cox et~al.(2010)]{cox2010}
   738	Cox, Michael and Arnold, Gwen and Villamayor Tomas, Sergio (2010). A Review of Design Principles for Community-based Natural Resource Management. \emph{Ecology and Society} 15(4), article 38. doi:10.5751/ES-03704-150438.
   739	
   740	\bibitem[Crone(1980)]{crone1980}
   741	Crone, Patricia (1980). \emph{Slaves on Horses: The Evolution of the Islamic Polity}. Cambridge University Press. doi:10.1017/cbo9780511563508.
   742	
   743	\bibitem[Davenport(2007)]{davenport2007}
   744	Davenport, Christian (2007). State Repression and Political Order. \emph{Annual Review of Political Science} 10:1-23. doi:10.1146/annurev.polisci.10.101405.143216.
   745	
   746	\bibitem[Edwards and Ogilvie(2012)]{edwards2012}
   747	Edwards, Jeremy and Ogilvie, Sheilagh (2012). Contract Enforcement, Institutions, and Social Capital: The Maghribi Traders Reappraised. \emph{Economic History Review} 65(2):421-444. doi:10.1111/j.1468-0289.2011.00635.x.
   748	
   749	\bibitem[Eisenhower(1961)]{eisenhower1961}
   750	Eisenhower, Dwight D. (1961). \emph{Farewell Radio and Television Address to the American People, 17 January 1961}. Public Papers of the Presidents. \url{https://www.eisenhowerlibrary.gov/research/online-documents/farewell-address}.
   751	
   752	\bibitem[Ellickson(1991)]{ellickson1991}
   753	Ellickson, Robert C. (1991). \emph{Order without Law: How Neighbors Settle Disputes}. Harvard University Press. doi:10.4159/9780674036437.
   754	
   755	\bibitem[Elliott(1963)]{elliott1963}
   756	Elliott, J. H. (1963). \emph{Imperial Spain 1469-1716}. Edward Arnold.
   757	
   758	\bibitem[Elster(1979)]{elster1979}
   759	Elster, Jon (1979). \emph{Ulysses and the Sirens: Studies in Rationality and Irrationality}. Cambridge University Press.
   760	
   761	\bibitem[Elster(1983)]{elster1983}
   762	Elster, Jon (1983). \emph{Explaining Technical Change: A Case Study in the Philosophy of Science}. Cambridge University Press.
   763	
   764	\bibitem[Ertman(1997)]{ertman1997}
   765	Ertman, Thomas (1997). \emph{Birth of the Leviathan: Building States and Regimes in Medieval and Early Modern Europe}. Cambridge University Press. doi:10.1017/cbo9780511529016.
   766	
   767	\bibitem[Evans-Pritchard(1940)]{evanspritchard1940}
   768	Evans-Pritchard, E. E. (1940). \emph{The Nuer: A Description of the Modes of Livelihood and Political Institutions of a Nilotic People}. Clarendon Press.
   769	
   770	\bibitem[Feaver(1999)]{feaver1999}
   771	Feaver, Peter D. (1999). Civil-Military Relations. \emph{Annual Review of Political Science} 2:211-241. doi:10.1146/annurev.polisci.2.1.211.
   772	
   773	\bibitem[Feaver(2003)]{feaver2003}
   774	Feaver, Peter D. (2003). \emph{Armed Servants: Agency, Oversight, and Civil-Military Relations}. Harvard University Press. doi:10.4159/9780674036772.
   775	
   776	\bibitem[Fehr and G\"achter(2002)]{fehr2002}
   777	Fehr, Ernst and G\"achter, Simon (2002). Altruistic Punishment in Humans. \emph{Nature} 415:137-140. doi:10.1038/415137a.
   778	
   779	\bibitem[Finer(1962)]{finer1962}
   780	Finer, Samuel E. (1962). \emph{The Man on Horseback: The Role of the Military in Politics}. Pall Mall Press.
   781	
   782	\bibitem[Foucault(1977)]{foucault1977}
   783	Foucault, Michel (1977). \emph{Discipline and Punish: The Birth of the Prison}. Pantheon Books.
   784	
   785	\bibitem[Friesen(2001)]{friesen2001}
   786	Friesen, Steven J. (2001). \emph{Imperial Cults and the Apocalypse of John: Reading Revelation in the Ruins}. Oxford University Press. doi:10.1093/0195131533.001.0001.
   787	
   788	\bibitem[Fuller(1995)]{fuller1995}
   789	Fuller, Robert C. (1995). \emph{Naming the Antichrist: The History of an American Obsession}. Oxford University Press. doi:10.1093/acprof:oso/9780195109795.001.0001.
   790	
   791	\bibitem[Gause(1994)]{gause1994}
   792	Gause, F. Gregory III (1994). \emph{Oil Monarchies: Domestic and Security Challenges in the Arab Gulf States}. Council on Foreign Relations Press.
   793	
   794	\bibitem[Gerschewski(2013)]{gerschewski2013}
   795	Gerschewski, Johannes (2013). The Three Pillars of Stability: Legitimation, Repression, and Co-optation in Autocratic Regimes. \emph{Democratization} 20(1):13-38. doi:10.1080/13510347.2013.738860.
   796	
   797	\bibitem[Getty(1985)]{getty1985}
   798	Getty, J. Arch (1985). \emph{Origins of the Great Purges: The Soviet Communist Party Reconsidered, 1933-1938}. Cambridge University Press. doi:10.1017/cbo9780511572616.
   799	
   800	\bibitem[Gieseke(2014)]{gieseke2014}
   801	Gieseke, Jens (2014). \emph{The History of the Stasi: East Germany's Secret Police, 1945-1990}. Berghahn Books. doi:10.3167/9781782382546.
   802	
   803	\bibitem[Graeber and Wengrow(2021)]{graeber2021}
   804	Graeber, David and Wengrow, David (2021). \emph{The Dawn of Everything: A New History of Humanity}. Farrar, Straus and Giroux.
   805	
   806	\bibitem[Gregory and Lazarev(2003)]{gregory2003}
   807	Gregory, Paul R. and Lazarev, Valery (eds.) (2003). \emph{The Economics of Forced Labor: The Soviet Gulag}. Hoover Institution Press.
   808	
   809	\bibitem[Greif(1993)]{greif1993}
   810	Greif, Avner (1993). Contract Enforceability and Economic Institutions in Early Trade: The Maghribi Traders' Coalition. \emph{American Economic Review} 83(3):525-548. \url{https://www.jstor.org/stable/2117532}.
   811	
   812	\bibitem[Greitens(2016)]{greitens2016}
   813	Greitens, Sheena Chestnut (2016). \emph{Dictators and Their Secret Police: Coercive Institutions and State Violence}. Cambridge University Press. doi:10.1017/cbo9781316489031.
   814	
   815	\bibitem[Hedlund(2011)]{hedlund2011}
   816	Hedlund, Erik (2011). Civil-Military Control over the Swedish Military Profession. \emph{Armed Forces \& Society} 39(1):135-157. Published online 2011; print issue 2013. doi:10.1177/0095327X11426256.
   817	
   818	\bibitem[Hegghammer and Lacroix(2007)]{hegghammer2007}
   819	Hegghammer, Thomas and Lacroix, St\'ephane (2007). Rejectionist Islamism in Saudi Arabia: The Story of Juhayman al-'Utaybi Revisited. \emph{International Journal of Middle East Studies} 39(1):103-122. doi:10.1017/s0020743807002553.
   820	
   821	\bibitem[Hempel(1959)]{hempel1959}
   822	Hempel, Carl G. (1959). The Logic of Functional Analysis. In Llewellyn Gross (ed.), \emph{Symposium on Sociological Theory}. Harper \& Row.
   823	
   824	\bibitem[Hill and Jones(2014)]{hill2014}
   825	Hill, Daniel W. and Jones, Zachary M. (2014). An Empirical Evaluation of Explanations for State Repression. \emph{American Political Science Review} 108(3):661-687. doi:10.1017/S0003055414000306.
   826	
   827	\bibitem[Hobbes(1651)]{hobbes1651}
   828	Hobbes, Thomas (1651). \emph{Leviathan}. Edited by Richard Tuck. Cambridge University Press, 1996. doi:10.1017/CBO9780511808166.
   829	
   830	\bibitem[Huntington(1957)]{huntington1957}
   831	Huntington, Samuel P. (1957). \emph{The Soldier and the State: The Theory and Politics of Civil-Military Relations}. Harvard University Press. doi:10.2307/j.ctvjf9wx3.
   832	
   833	\bibitem[Huntington(1968)]{huntington1968}
   834	Huntington, Samuel P. (1968). \emph{Political Order in Changing Societies}. Yale University Press.
   835	
   836	\bibitem[Irwin(1986)]{irwin1986}
   837	Irwin, Robert (1986). \emph{The Middle East in the Middle Ages: The Early Mamluk Sultanate 1250-1382}. Southern Illinois University Press.
   838	
   839	\bibitem[Jackson et~al.(2012)]{jackson2012}
   840	Jackson, Jonathan and Bradford, Ben and Hough, Mike and Myhill, Andy and Quinton, Paul and Tyler, Tom R. (2012). Why Do People Comply with the Law? Legitimacy and the Influence of Legal Institutions. \emph{British Journal of Criminology} 52(6):1051-1071. doi:10.1093/bjc/azs032.
   841	
   842	\bibitem[Janowitz(1960)]{janowitz1960}
   843	Janowitz, Morris (1960). \emph{The Professional Soldier: A Social and Political Portrait}. Free Press.
   844	
   845	\bibitem[Kamen(1997)]{kamen1997}
   846	Kamen, Henry (1997). \emph{The Spanish Inquisition: A Historical Revision}. Yale University Press.
   847	
   848	\bibitem[Karaman and Pamuk(2013)]{karaman2013}
   849	Karaman, K. K{\i}van\c{c} and Pamuk, \c{S}evket (2013). Different Paths to the Modern State in Europe: The Interaction between Warfare, Economic Structure, and Political Regime. \emph{American Political Science Review} 107(3):603-626. doi:10.1017/S0003055413000312.
   850	
   851	\bibitem[Katzman(1993)]{katzman1993}
   852	Katzman, Kenneth (1993). \emph{The Warriors of Islam: Iran's Revolutionary Guard}. Westview Press.
   853	
   854	\bibitem[Kelly(1995)]{kelly1995}
   855	Kelly, Robert L. (1995). \emph{The Foraging Spectrum: Diversity in Hunter-Gatherer Lifeways}. Smithsonian Institution Press. doi:10.2307/j.ctv2sx9gc9.
   856	
   857	\bibitem[Kennedy(2001)]{kennedy2001}
   858	Kennedy, Hugh (2001). \emph{The Armies of the Caliphs: Military and Society in the Early Islamic State}. Routledge.
   859	
   860	\bibitem[Knight(1996)]{knight1996}
   861	Knight, Amy (1996). \emph{Spies without Cloaks: The KGB's Successors}. Princeton University Press. doi:10.2307/j.ctt15sk83q.
   862	
   863	\bibitem[Knowles et~al.(2001)]{knowles2001}
   864	Knowles, John and Persico, Nicola and Todd, Petra (2001). Racial Bias in Motor Vehicle Searches: Theory and Evidence. \emph{Journal of Political Economy} 109(1):203-229. doi:10.1086/318603.
   865	
   866	\bibitem[Koehler(1999)]{koehler1999}
   867	Koehler, John O. (1999). \emph{Stasi: The Untold Story of the East German Secret Police}. Westview Press.
   868	
   869	\bibitem[Koester(2014)]{koester2014}
   870	Koester, Craig R. (2014). \emph{Revelation: A New Translation with Introduction and Commentary}. Yale University Press (Anchor Yale Bible 38A). doi:10.12987/9780300211030.
   871	
   872	\bibitem[Kohn(1997)]{kohn1997}
   873	Kohn, Richard H. (1997). How Democracies Control the Military. \emph{Journal of Democracy} 8(4):140-153. doi:10.1353/jod.1997.0060.
   874	
   875	\bibitem[Kornai(1992)]{kornai1992}
   876	Kornai, J\'anos (1992). \emph{The Socialist System: The Political Economy of Communism}. Princeton University Press. doi:10.2307/j.ctv1ddczdr.
   877	
   878	\bibitem[Kovacs and Rowland(2004)]{kovacs2004}
   879	Kovacs, Judith and Rowland, Christopher (2004). \emph{Revelation: The Apocalypse of Jesus Christ}. Blackwell (Blackwell Bible Commentaries). doi:10.1002/9780470773512.
   880	
   881	\bibitem[Kraybill(1996)]{kraybill1996}
   882	Kraybill, J. Nelson (1996). \emph{Imperial Cult and Commerce in John's Apocalypse}. Sheffield Academic Press (JSNT Supplement 132).
   883	
   884	\bibitem[Kunt(1983)]{kunt1983}
   885	Kunt, I. Metin (1983). \emph{The Sultan's Servants: The Transformation of Ottoman Provincial Government, 1550-1650}. Columbia University Press.
   886	
   887	\bibitem[Kuran(1991)]{kuran1991}
   888	Kuran, Timur (1991). Now Out of Never: The Element of Surprise in the East European Revolution of 1989. \emph{World Politics} 44(1):7-48. doi:10.2307/2010422.
   889	
   890	\bibitem[Largo(2026)]{largo2026hbs}
   891	Largo, Mateo (2026). \emph{The Hierarchy of the Beast System: Institutional Power, Elite Coordination, and Economic Dependency Across Political Regimes}. Working paper, 14 October 2026.
   892	
   893	\bibitem[Lee(1979)]{lee1979}
   894	Lee, Richard B. (1979). \emph{The !Kung San: Men, Women, and Work in a Foraging Society}. Cambridge University Press.
   895	
   896	\bibitem[Lee(2013)]{lee2013}
   897	Lee, Richard B. (2013). \emph{The Dobe Ju/'hoansi}. 4th edition. Wadsworth/Cengage Learning.
   898	
   899	\bibitem[Leggett(1981)]{leggett1981}
   900	Leggett, George (1981). \emph{The Cheka: Lenin's Political Police}. Oxford University Press.
   901	
   902	\bibitem[Lynn(1997)]{lynn1997}
   903	Lynn, John A. (1997). \emph{Giant of the Grand Si\`ecle: The French Army, 1610-1715}. Cambridge University Press. doi:10.1017/cbo9780511572548.
   904	
   905	\bibitem[Madison(1788)]{madison1788}
   906	Madison, James (1788). \emph{The Federalist No. 51: The Structure of the Government Must Furnish the Proper Checks and Balances}. Independent Journal, 6 February 1788. \url{https://avalon.law.yale.edu/18th_century/fed51.asp}.
   907	
   908	\bibitem[Mann(1984)]{mann1984}
   909	Mann, Michael (1984). The Autonomous Power of the State: Its Origins, Mechanisms and Results. \emph{European Journal of Sociology} 25(2):185-213. doi:10.1017/S0003975600004239.
   910	
   911	\bibitem[Marshall(1976)]{marshall1976}
   912	Marshall, Lorna (1976). \emph{The !Kung of Nyae Nyae}. Harvard University Press. doi:10.4159/harvard.9780674180574.
   913	
   914	\bibitem[McGinn(1998)]{mcginn1998}
   915	McGinn, Bernard (1998). \emph{Antichrist: Two Thousand Years of the Human Fascination with Evil}. Columbia University Press.
   916	
   917	\bibitem[North et~al.(2009)]{nww2009}
   918	North, Douglass C. and Wallis, John Joseph and Weingast, Barry R. (2009). \emph{Violence and Social Orders: A Conceptual Framework for Interpreting Recorded Human History}. Cambridge University Press. doi:10.1017/CBO9780511575839.
   919	
   920	\bibitem[{EOS Committee}(2026)]{eos2026} Norwegian Parliamentary Oversight Committee on Intelligence and Security Services (EOS Committee) (2026). History of the EOS Committee. \url{https://eos-utvalget.no/en/home/about-the-eos-committee/history}. Accessed 22 October 2026.
   921	
   922	\bibitem[Olson(1965)]{olson1965}
   923	Olson, Mancur (1965). \emph{The Logic of Collective Action: Public Goods and the Theory of Groups}. Harvard University Press. doi:10.4159/9780674041660.
   924	
   925	\bibitem[Ostrom(1990)]{ostrom1990}
   926	Ostrom, Elinor (1990). \emph{Governing the Commons: The Evolution of Institutions for Collective Action}. Cambridge University Press. doi:10.1017/CBO9780511807763.
   927	
   928	\bibitem[Ostrom(2010)]{ostromdesign2010}
   929	Ostrom, Elinor (2010). Beyond Markets and States: Polycentric Governance of Complex Economic Systems. \emph{American Economic Review} 100(3):641-672. doi:10.1257/aer.100.3.641.
   930	
   931	\bibitem[Parker(1972)]{parker1972}
   932	Parker, Geoffrey (1972). \emph{The Army of Flanders and the Spanish Road, 1567-1659}. Cambridge University Press.
   933	
   934	\bibitem[Parker(1988)]{parker1988}
   935	Parker, Geoffrey (1988). \emph{The Military Revolution: Military Innovation and the Rise of the West, 1500-1800}. Cambridge University Press.
   936	
   937	\bibitem[Parrott(2012)]{parrott2012}
   938	Parrott, David (2012). \emph{The Business of War: Military Enterprise and Military Revolution in Early Modern Europe}. Cambridge University Press. doi:10.1017/cbo9781139023337.
   939	
   940	\bibitem[Perlmutter(1969)]{perlmutter1969}
   941	Perlmutter, Amos (1969). The Praetorian State and the Praetorian Army: Toward a Taxonomy of Civil-Military Relations in Developing Polities. \emph{Comparative Politics} 1(3):382-404. doi:10.2307/421446.
   942	
   943	\bibitem[Pilster and B\"ohmelt(2011)]{pilster2011}
   944	Pilster, Ulrich and B\"ohmelt, Tobias (2011). Coup-Proofing and Military Effectiveness in Interstate Wars, 1967-99. \emph{Conflict Management and Peace Science} 28(4):331-350. doi:10.1177/0738894211413062.
   945	
   946	\bibitem[Pipes(1981)]{pipes1981}
   947	Pipes, Daniel (1981). \emph{Slave Soldiers and Islam: The Genesis of a Military System}. Yale University Press.
   948	
   949	\bibitem[Poe and Tate(1994)]{poe1994}
   950	Poe, Steven C. and Tate, C. Neal (1994). Repression of Human Rights to Personal Integrity in the 1980s: A Global Analysis. \emph{American Political Science Review} 88(4):853-872. doi:10.2307/2082712.
   951	
   952	\bibitem[Powell and Thyne(2011)]{powell2011}
   953	Powell, Jonathan M. and Thyne, Clayton L. (2011). Global Instances of Coups from 1950 to 2010: A New Dataset. \emph{Journal of Peace Research} 48(2):249-259. doi:10.1177/0022343310397436.
   954	
   955	\bibitem[Pratt(2008a)]{pratt2008a}
   956	Pratt, John (2008a). Scandinavian Exceptionalism in an Era of Penal Excess. Part I: The Nature and Roots of Scandinavian Exceptionalism. \emph{British Journal of Criminology} 48(2):119-137. doi:10.1093/bjc/azm072.
   957	
   958	\bibitem[Pratt(2008b)]{pratt2008b}
   959	Pratt, John (2008b). Scandinavian Exceptionalism in an Era of Penal Excess. Part II: Does Scandinavian Exceptionalism Have a Future? \emph{British Journal of Criminology} 48(3):275-292. doi:10.1093/bjc/azm073.
   960	
   961	\bibitem[Quinlivan(1999)]{quinlivan1999}
   962	Quinlivan, James T. (1999). Coup-proofing: Its Practice and Consequences in the Middle East. \emph{International Security} 24(2):131-165. doi:10.1162/016228899560202.
   963	
   964	\bibitem[Rejali(2007)]{rejali2007}
   965	Rejali, Darius (2007). \emph{Torture and Democracy}. Princeton University Press. doi:10.1515/9781400830879.
   966	
   967	\bibitem[Riksdagens ombudsm\"an(2026)]{jo2026}
   968	Riksdagens ombudsm\"an (Parliamentary Ombudsmen of Sweden) (2026). History of the Parliamentary Ombudsmen. \url{https://www.jo.se/en/about-jo/history/}. Accessed 22 October 2026.
   969	
   970	\bibitem[Rowlands(2002)]{rowlands2002}
   971	Rowlands, Guy (2002). \emph{The Dynastic State and the Army under Louis XIV: Royal Service and Private Interest, 1661-1701}. Cambridge University Press. doi:10.1017/cbo9780511496882.
   972	
   973	\bibitem[{S\"akerhetstj\"anstkommissionen}(2002)]{sou2002} S\"akerhetstj\"anstkommissionen (2002). \emph{Rikets s\"akerhet och den personliga integriteten: De svenska s\"akerhetstj\"ansternas f\"orfattningsskyddande verksamhet sedan \aa{}r 1945}. SOU 2002:87. Stockholm: Justitiedepartementet. \url{https://regeringen.se/rattsliga-dokument/statens-offentliga-utredningar/2002/01/sou-200287/}.
   974	
   975	\bibitem[Scoggins and O'Brien(2016)]{scoggins2016}
   976	Scoggins, Suzanne E. and O'Brien, Kevin J. (2016). China's Unhappy Police. \emph{Asian Survey} 56(2):225-242. doi:10.1525/as.2016.56.2.225.
   977	
   978	\bibitem[Shambaugh(2002)]{shambaugh2002}
   979	Shambaugh, David (2002). \emph{Modernizing China's Military: Progress, Problems, and Prospects}. University of California Press. doi:10.1525/9780520938106.
   980	
   981	\bibitem[Slater(2010)]{slater2010}
   982	Slater, Dan (2010). \emph{Ordering Power: Contentious Politics and Authoritarian Leviathans in Southeast Asia}. Cambridge University Press. doi:10.1017/cbo9780511760891.
   983	
   984	\bibitem[Svolik(2012)]{svolik2012}
   985	Svolik, Milan W. (2012). \emph{The Politics of Authoritarian Rule}. Cambridge University Press. doi:10.1017/CBO9781139176040.
   986	
   987	\bibitem[{Swedish Government}(1999)]{dir1999} Swedish Government (1999). Kommission f\"or granskning av de svenska s\"akerhetstj\"ansternas f\"orfattningsskyddande verksamhet. Committee directive Dir. 1999:26, 25 March 1999. \url{https://data.riksdagen.se/dokument/GNB126}.
   988	
   989	\bibitem[Tezcan(2010)]{tezcan2010}
   990	Tezcan, Baki (2010). \emph{The Second Ottoman Empire: Political and Social Transformation in the Early Modern World}. Cambridge University Press.
   991	
   992	\bibitem[Thompson(1976)]{thompson1976}
   993	Thompson, I. A. A. (1976). \emph{War and Government in Habsburg Spain, 1560-1620}. Athlone Press.
   994	
   995	\bibitem[Thompson(1990)]{thompson1990}
   996	Thompson, Leonard L. (1990). \emph{The Book of Revelation: Apocalypse and Empire}. Oxford University Press. doi:10.1093/oso/9780195055511.001.0001.
   997	
   998	\bibitem[Tilly(1985)]{tilly1985}
   999	Tilly, Charles (1985). War Making and State Making as Organized Crime. In Peter B. Evans, Dietrich Rueschemeyer and Theda Skocpol (eds.), \emph{Bringing the State Back In}. Cambridge University Press. doi:10.1017/cbo9780511628283.008.
  1000	
  1001	\bibitem[Tilly(1990)]{tilly1990}
  1002	Tilly, Charles (1990). \emph{Coercion, Capital, and European States, AD 990-1990}. Blackwell.
  1003	
  1004	\bibitem[Tyler(1990)]{tyler1990}
  1005	Tyler, Tom R. (1990). \emph{Why People Obey the Law}. Yale University Press. doi:10.1515/9781400828609.
  1006	
  1007	\bibitem[{Commission on Industrial Relations}(1915)]{cir1915} United States Commission on Industrial Relations (1915). \emph{Final Report of the Commission on Industrial Relations}. Washington, DC. \url{https://archive.org/details/finalreportofcom00unitiala}.
  1008	
  1009	\bibitem[{United States Senate}(1976)]{church1976} United States Senate, Select Committee to Study Governmental Operations with Respect to Intelligence Activities (1976). \emph{Intelligence Activities and the Rights of Americans}. Final Report, Book II, S. Rep. No. 94-755. U.S. Government Printing Office.
  1010	
  1011	\bibitem[Weber(1946)]{weber1946}
  1012	Weber, Max (1946). Politics as a Vocation. In H. H. Gerth and C. Wright Mills (eds.), \emph{From Max Weber: Essays in Sociology}. Oxford University Press.
  1013	
  1014	\bibitem[Weber(1978)]{weber1978}
  1015	Weber, Max (1978). \emph{Economy and Society: An Outline of Interpretive Sociology}. University of California Press. doi:10.4159/9780674240827.
  1016	
  1017	\bibitem[Wehrey et~al.(2009)]{wehrey2009}
  1018	Wehrey, Frederic and Green, Jerrold D. and Nichiporuk, Brian and Nader, Alireza and Hansell, Lydia and Nafisi, Rasool and Bohandy, S. R. (2009). \emph{The Rise of the Pasdaran: Assessing the Domestic Roles of Iran's Islamic Revolutionary Guards Corps}. RAND Corporation, MG-821-OSD.
  1019	
  1020	\bibitem[Wiessner(2005)]{wiessner2005}
  1021	Wiessner, Polly (2005). Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity? \emph{Human Nature} 16(2):115-145. doi:10.1007/s12110-005-1000-9.
  1022	
  1023	\bibitem[Wink(1992)]{wink1992}
  1024	Wink, Walter (1992). \emph{Engaging the Powers: Discernment and Resistance in a World of Domination}. Fortress Press. doi:10.2307/j.ctt1tm7j16.
  1025	
  1026	\bibitem[Wintrobe(1998)]{wintrobe1998}
  1027	Wintrobe, Ronald (1998). \emph{The Political Economy of Dictatorship}. Cambridge University Press. doi:10.1017/cbo9781139174916.
  1028	
  1029	\bibitem[Woodburn(1982)]{woodburn1982}
  1030	Woodburn, James (1982). Egalitarian Societies. \emph{Man (N.S.)} 17(3):431-451. doi:10.2307/2801707.
  1031	
  1032	\bibitem[Yoder(1972)]{yoder1972}
  1033	Yoder, John Howard (1972). \emph{The Politics of Jesus}. Eerdmans.
  1034	
  1035	\end{thebibliography}
  1036	
  1037	\end{document}

2026-10-22T17:08:57.603240Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '130,329p' papers/latex/coercive-power.tex | nl -ba -v130" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   130	\label{eq:margin}
   131	\end{equation}
   132	with discount factor $\delta \in [0,1)$. The \emph{sanction regime} of $\sigma$ is the map $(i, h_t) \mapsto d_{i,t}$. The regime is \emph{trivial} if $d_{i,t} \le 0$ at every reachable node.
   133	\end{definition}
   134	
   135	The margin compares two unilateral continuations, so it is defined at every node, including nodes at which $\sigma_i$ prescribes compliance and violation is off the path of play. It includes $i$'s own optimal future behavior, which may itself change after a violation; an agent excluded from cooperation, for example, faces different future margins from one in good standing. Under the payoff assumption of \cref{sec:necessity}, a violation affects $i$'s future only through other agents' responses, so the margin is zero whenever $\sigma_{-i}$ does not condition on $i$'s violations. A positive margin therefore requires that others respond to $i$'s violation in a way that lowers $i$'s payoff. The response may be a beating, a lawsuit, a boycott or a refusal to share meat. The definition does not ask who responds or whether they hold an office.
   136	
   137	\begin{definition}[Conduct and allegiance margins]
   138	\label{def:coercive-power:margins}
   139	Fix a \emph{reference rule set} $\mathcal{R}^0$: a preregistered set of rules in force whose content does not refer to political alignment, such as prohibitions of theft, assault and fraud. Let $v \in \{0,1\}$ indicate whether an agent violated a rule in $\mathcal{R}^0$ in the period, and let each agent carry an alignment $y \in \{\mathrm{al}, \mathrm{op}\}$, aligned with or opposed to the coalition that directs the coercive apparatus. Let $\psi(v,y) \in [0,1]$ be the per-period probability that an agent with violation status $v$ and alignment $y$ is the target of a coercive act of magnitude $\mu > 0$. The \emph{conduct margin} for alignment $y$ is $\Delta^{\mathrm{c}}(y) = \psi(1,y) - \psi(0,y)$. The \emph{allegiance margin} at violation status $v$ is $\Delta^{\mathrm{a}}(v) = \psi(v,\mathrm{op}) - \psi(v,\mathrm{al})$.
   140	\end{definition}
   141	
   142	The conduct margin is the enforcement of rules. The allegiance margin is the enforcement of loyalty. Rule-of-law ideals ask for $\Delta^{\mathrm{c}}(y) > 0$ and $\Delta^{\mathrm{a}}(v) = 0$: violators are targeted more than compliers, and opponents are treated like supporters with the same conduct. The reference rule set is what keeps the two margins distinct. If loyalty were itself a rule in $\mathcal{R}^0$, violation status and alignment would coincide for that rule and the allegiance margin would collapse into the conduct margin. Rules whose content is allegiance, such as an obligation to worship an image or a prohibition of opposition, are therefore excluded from $\mathcal{R}^0$. Coercive acts that enforce them appear in this framework as an allegiance margin, and their enactment is rule-making capture, which Part~II analyzes. A third pattern is distinct from both margins: \emph{arbitrariness}, in which $\Delta^{\mathrm{c}}(y)$ falls toward zero for every alignment, so that coercion responds neither to conduct nor to allegiance. \Cref{sec:mechanisms} shows that the conduct and allegiance margins can be chosen independently and analyzes the conditions under which they trade off.
   143	
   144	\subsection{Dependencies and integration}
   145	
   146	Two different relations connect the coercive pillar to the other five, and they must be kept apart. A \emph{dependency} $m \to \pC$ holds when the coercive function needs an output of pillar $m$ in order to operate. The \emph{integration coefficient} $C_{m\pC}$ of the source measures something else: the extent to which one coalition commands appointments, budgets, sanctions or agenda in both pillars. Dependencies are present in every polity, as Part~VII argues for the whole dependency structure; high integration is contingent. Dependency is evidence of Proposition~A, and integration is an ingredient of Proposition~B.
   147	
   148	The dependencies of coercion run as follows. Coercion must be provisioned ($\pF \to \pC$); Part~I owns the financing side of the fiscal-military state and the pair $C_{\pF\pC}$, including the fusion of financial and coercive control in one organization (Part~I, Section~6), and this Part treats the coercive side. Commanders are appointed ($\pP \to \pC$), and Part~II's appointment channel measures how far appointment produces integration. Sanctions follow determinations of wrongdoing ($\pJ \to \pC$); Part~III treats that pair, and its Proposition~3.6 shows that an effective judicial determination requires either legitimacy or an expected sanction for defiance, a dependency in the opposite direction. Sanctions must be recognized as legitimate to be distinguished from predation ($\pI \to \pC$); Part~IV defines the legitimation function (Definition~2.1) and treats the pair $C_{\pI\pC}$. The pair of coercion and production is the primary responsibility of this Part. Conscription is a dependency $\pW \to \pC$: it converts the labor time of the producing population into coercive capacity. Coerced labor is a dependency $\pC \to \pW$: it converts coercive capacity into production. The integration coefficient $C_{\pC\pW}$ is high only when one coalition commands both the coercive apparatus and the allocation of labor. \Cref{sec:cw} treats the pair.
   149	
   150	\section{Necessity of the coercive pillar}
   151	\label{sec:necessity}
   152	
   153	\subsection{The axiom of defection}
   154	
   155	Part~VII states six working axioms about collective life and derives one pillar from each. The axiom behind the coercive pillar is Ax5 (defection): some members sometimes break rules. Hobbes put the consequence in a sentence that has organized the subject since: ``covenants, without the sword, are but words'' \citep[ch.~17]{hobbes1651}. Hobbes drew from it the conclusion that a sovereign must hold the sword. The argument below accepts the premise and rejects that conclusion. Defection makes sanctioning necessary; it does not make a sovereign necessary.
   156	
   157	To give Ax5 content we state it as a claim about temptation rather than about observed violations. In each period agent $i$ privately observes a net temptation $\tau_{i,t} \in \mathbb{R}$, the gain from violating the rule minus every cost of violation that does not pass through other agents' responses. Internalized norms, guilt and shame lower $\tau_{i,t}$; so do any direct material costs of violation to the violator. Temptations are drawn independently across agents and periods from a distribution with cumulative distribution function $G$, and $p := \Pr(\tau_{i,t} > 0) = 1 - G(0)$ is the probability that an agent would gain from violation if nobody responded.
   158	
   159	A rule is useful to a collective only if violations stay below some rate. Call that rate the \emph{tolerance} $\theta \in [0,1)$: if the expected frequency of violations exceeds $\theta$ in the long run, the rule no longer coordinates behavior and the collective either abandons it or fails to persist. Formally, the rule is \emph{in force} under $\sigma$ if
   160	\[
   161	\limsup_{T \to \infty} \frac{1}{nT} \sum_{t=1}^{T} \sum_{i=1}^{n} \Pr(v_{i,t} = 1) \le \theta .
   162	\]
   163	
   164	\begin{assumption}[Ax5, defection, formal version]
   165	\label{ass:ax5}
   166	For the rule under consideration, $p > \theta$: the probability that an agent gains from violation in the absence of any response by others exceeds the violation rate the collective can tolerate.
   167	\end{assumption}
   168	
   169	The assumption is empirical, not logical, and it is stronger than the informal statement of Ax5. Observed violations are compatible with $p \le \theta$, since a collective may tolerate occasional violations of a rule that few are tempted to break. A population of saints, or one so thoroughly socialized that internal costs exceed every temptation, would have $p \le \theta$ for every rule. To connect the theorem below to Proposition~A, which concerns every functioning governance system, we therefore need a bridge.
   170	
   171	\begin{assumption}[Bridge]
   172	\label{ass:bridge}
   173	Every functioning governance system has at least one rule in force for which \cref{ass:ax5} holds.
   174	\end{assumption}
   175	
   176	The bridge carries the empirical content of the coercive pillar's place in Proposition~A. It is not true by definition: it would fail for a collective whose every rule is one that almost nobody is tempted to break, and \cref{sec:counter} states how to test it with a measurement of $p$ that is independent of sanction practices. We also assume that the agent's payoff depends on its own violation only through $\tau_{i,t}$ and through other agents' responses. Any direct effect of $i$'s violation on $i$'s own future (for example, overgrazing that also harms the violator's herd) is folded into $\tau_{i,t}$.
   177	
   178	\subsection{The deterrence lemma}
   179	
   180	\begin{lemma}[Deterrence]
   181	\label{lem:coercive-power:deterrence}
   182	Let $\sigma$ be a strategy profile in which every agent best-responds at every node. At $(t, h_t)$, agent $i$ violates if $\tau_{i,t} > d_{i,t}$ and complies if $\tau_{i,t} < d_{i,t}$. The probability that $i$ violates at that node is at least $1 - G(d_{i,t})$, with equality when $G$ has no atom at $d_{i,t}$ or ties are resolved toward compliance.
   183	\end{lemma}
   184	
   185	\begin{proof}
   186	By \cref{def:coercive-power:regime}, $i$'s expected payoff from period $t$ onward is $\tau_{i,t} + W_i(h_t,1)$ if it violates and $W_i(h_t,0)$ if it complies, where both continuations include $i$'s own optimal future play. The difference between violating and complying is $\tau_{i,t} - d_{i,t}$. A best-responding agent violates when this difference is positive and complies when it is negative. Because $\tau_{i,t}$ is drawn from $G$ independently of $h_t$, the probability of violation is at least $\Pr(\tau_{i,t} > d_{i,t}) = 1 - G(d_{i,t})$; ties at $\tau_{i,t} = d_{i,t}$ can only add violations.
   187	\end{proof}
   188	
   189	The lemma is a dynamic version of the deterrence condition in the economics of crime: a rational offender is deterred when the expected cost of punishment exceeds the gain \citep{becker1968}. In the simplest regimes $d_{i,t} = \pi\mu$, the product of the detection probability and the sanction magnitude. The general form \eqref{eq:margin} also covers sanctions that are not punishments in the legal sense: the loss of future cooperation in a repeated game, a damaged reputation in a trading network, or exclusion from the next meat distribution.
   190	
   191	\begin{theorem}[Necessity of the sanction function]
   192	\label{thm:coercive-power:necessity}
   193	Suppose \cref{ass:ax5} holds for a rule that is in force under a best-response profile $\sigma$. Let $\bar{\mathbb{E}}_T[x] = \frac{1}{nT}\sum_{t\le T}\sum_{i} \E[x_{i,t}]$ denote the expected average over agents and the first $T$ periods. Then
   194	\begin{equation}
   195	\liminf_{T\to\infty} \bar{\mathbb{E}}_T\bigl[G(d) - G(0)\bigr] \ge p - \theta > 0,
   196	\label{eq:necessity}
   197	\end{equation}
   198	and the long-run expected share of agent-periods with a strictly positive deterrence margin is at least $(p - \theta)/p$. In particular, the sanction regime of $\sigma$ is non-trivial.
   199	\end{theorem}
   200	
   201	\begin{proof}
   202	By \cref{lem:coercive-power:deterrence} and the law of iterated expectations, $\Pr(v_{i,t} = 1) \ge \E[1 - G(d_{i,t})]$, so the expected violation frequency up to $T$ is at least $\bar{\mathbb{E}}_T[1 - G(d)]$. Because the rule is in force, $\limsup_T \bar{\mathbb{E}}_T[1 - G(d)] \le \theta$, which gives $\liminf_T \bar{\mathbb{E}}_T[G(d)] \ge 1 - \theta$. Since $G(0) = 1 - p$, subtracting gives \eqref{eq:necessity}. For the second claim, each term satisfies $G(d_{i,t}) - G(0) \le p \cdot \mathbf{1}[d_{i,t} > 0]$, because the difference is zero when $d_{i,t} \le 0$ and at most $1 - G(0) = p$ otherwise. Hence $\liminf_T \bar{\mathbb{E}}_T[\mathbf{1}[d > 0]] \ge (p - \theta)/p$. A trivial regime would make the left side of \eqref{eq:necessity} non-positive, contradicting $p > \theta$.
   203	\end{proof}
   204	
   205	The theorem is stated in expectation. Realized frequencies converge to the same limits: the differences $v_{i,t} - \Pr(v_{i,t} = 1 \mid h_t)$ are bounded martingale differences, so by the strong law of large numbers for such differences their average tends to zero almost surely. The theorem is a necessity statement about a role, in the sense required by Part~VII: some agents must respond to violations in a way that costs the violator. It is silent on who those agents are, on whether they specialize, and on whether the cost is physical. It also gives two quantitative floors. The sanction regime must shift at least $p - \theta$ of probability mass from violation to compliance, and at least a fraction $(p-\theta)/p$ of agent-periods must face a positive margin. Sanctions that are too weak or too rarely threatened fail these bounds even when they exist on paper.
   206	
   207	A positive margin is a threat. \Cref{def:coercive-power:sanction} counts the function as implemented only if violations, when they occur, are actually met with sanctions. The two notions coincide whenever violations occur on the path of play. If $G$ has unbounded support, so that $\Pr(\tau > x) > 0$ for every $x$, then by \cref{lem:coercive-power:deterrence} violations occur with positive probability at every node, and a positive margin can be sustained only if they are in fact sanctioned with positive probability. A collective in which temptations are bounded and every agent is perfectly deterred would have the threat without observed sanctions; we know of no such collective, and \cref{tab:hardcases} records frequent sanctions in the societies closest to that ideal.
   208	
   209	\begin{corollary}[Magnitude]
   210	\label{cor:coercive-power:magnitude}
   211	If every agent faces the same margin $d = \pi\mu$, compliance at rate at least $1 - \theta$ requires $\pi\mu \ge G^{-1}(1 - \theta)$, where $G^{-1}$ is the right-continuous generalized inverse. A rise in temptation (a rightward shift of $G$) or a fall in detection $\pi$ must be offset by a larger sanction magnitude $\mu$ or a larger detection probability $\pi$; otherwise the collective must accept a higher tolerance $\theta$.
   212	\end{corollary}
   213	
   214	\begin{proof}
   215	With a common margin the violation rate is $1 - G(\pi\mu)$ when ties are resolved toward compliance, and $1 - G(\pi\mu) \le \theta$ holds if and only if $G(\pi\mu) \ge 1 - \theta$, which is $\pi\mu \ge G^{-1}(1-\theta)$ for the generalized inverse.
   216	\end{proof}
   217	
   218	\subsection{The second-order problem}
   219	
   220	A sanction is an act, and acts have costs. A Ju/'hoansi who criticizes a boastful hunter risks a quarrel; a Nuer kinsman who joins a feud risks his life; a police officer who arrests a powerful man risks a career. If nobody is willing to bear these costs, the deterrence margin collapses to zero and \cref{thm:coercive-power:necessity} fails. The following result states what must be true of sanctioners when sanctioning is costly.
   221	
   222	\begin{proposition}[Second-order enforcement]
   223	\label{prop:coercive-power:second-order}
   224	Suppose that delivering a sanction against $i$ requires an act by some agent $j \neq i$ at private cost $c_j > 0$, and that $d_{i,t} > 0$ in a best-response profile. Decompose the private return to $j$ of sanctioning into four terms: (a) a material transfer to $j$ conditional on sanctioning, such as pay, provisioning or a share of seized goods; (b) an intrinsic or social reward, such as esteem, a sense of duty or satisfaction from punishing; (c) avoidance of a sanction that $j$ would itself suffer for failing to sanction; and (d) $j$'s own share of the benefit of deterring $i$ and, through the example, third parties, weighted by the probability that $j$'s act is decisive. Then for some such $j$ the sum of (a) to (d) is at least $c_j$.
   225	\end{proposition}
   226	
   227	\begin{proof}
   228	The four terms are a decomposition of $j$'s payoff from its own sanctioning act: transfers conditioned on the act, $j$'s preferences over the act itself, others' responses to the act or its omission, and the act's effect on the behavior of $i$ and of others. We take this decomposition as the definition of the private return. If, for every $j$ whose act is required, the sum were below $c_j$, then not sanctioning would be a strict best response for each such $j$. No sanction would be delivered against $i$ for a violation at $(t,h_t)$, so $\sigma_{-i}$ would not respond to $v_{i,t}$ and $d_{i,t} = 0$, a contradiction.
   229	\end{proof}
   230	
   231	The proposition is a disjunction, and its interpretation needs care. Term (a) is the dependency $\pF \to \pC$: paid soldiers and police are provisioned out of resources that someone allocates. Term (b) is the dependency $\pI \to \pC$: a norm that makes punishing violators honorable, or a belief that the sanctioning authority is legitimate, supplies the reward. Term (c) is coercion applied to the coercers. In repeated games it can close the regress in equilibrium without transfers or intrinsic rewards: community-enforcement equilibria, in which those who fail to punish are themselves punished, need only that agents coordinate on the same punishment norm. Whether that coordination counts as legitimation is a question for Part~IV, and this paper does not settle it by definition. Term (d) needs no other pillar. The structure parallels Proposition~3.6 of Part~III, where an effective judicial determination needs legitimacy or sanction: in both cases the incoming dependency is a disjunction, which Part~VII must treat as a hyperedge of the dependency digraph rather than as separate arcs.
   232	
   233	The scale argument is conditional on the technology of sanctioning.
   234	
   235	\begin{corollary}[Costly sanctions at scale]
   236	\label{cor:coercive-power:scale}
   237	Suppose sanctions are costly to the sanctioner ($c_j \ge \underline{c} > 0$), the benefit of deterrence is shared across the collective so that the probability that any one sanctioner's act is decisive tends to zero as $n$ grows, and higher-order sanctions (term (c)) are absent. Then for $n$ large enough, a non-trivial sanction regime requires that term (a) or term (b) be positive for some sanctioner.
   238	\end{corollary}
   239	
   240	\begin{proof}
   241	Term (d) is bounded by the benefit of deterrence to $j$ times the probability that $j$'s act is decisive, and the second factor tends to zero, so for $n$ large enough term (d) is below $\underline{c}$. Term (c) is zero by hypothesis. \Cref{prop:coercive-power:second-order} then requires (a) or (b) to make up the difference.
   242	\end{proof}
   243	
   244	The hypotheses matter. When sanctions take the form of bilateral exclusion, as in the trading coalition discussed in \cref{sec:counter}, each excluder's act is decisive for its own relationship whatever the size of the collective, and the cost may be zero or negative: refusing to rehire a cheat can save money. Then the premise $c_j > 0$ fails, and coercion of this kind depends on no other pillar. The corollary applies to sanctions that are costly public goods, such as detaining, fighting or punishing strangers, which is the form that coercion against serious violations takes in large polities. Under that condition the sanction function at scale must be provisioned or legitimated. This is a micro-foundation for Tilly's coupling of war-making to extraction \citep{tilly1990} and for the military-fiscal bargains studied in \cref{sec:catholic}. Wherever term (a) dominates, the sanctioner's loyalty follows the paymaster, which is the root of the guardian problem treated in \cref{sec:mechanisms}. Experimental evidence supports term (b): subjects in public-goods experiments pay to punish free riders even when they cannot expect future gains from doing so, and cooperation is sustained when punishment is available \citep{fehr2002}. In a band of thirty, by contrast, a person harmed by a thief has a direct interest in stopping the theft and a real chance that the intervention matters, so term (d) can carry the load. This is the collective-action logic of \citet{olson1965} applied to enforcement.
   245	
   246	\subsection{Minimal forms in stateless and consensus societies}
   247	\label{sec:minimal}
   248	
   249	\Cref{thm:coercive-power:necessity} predicts that every persistent collective satisfying Ax5 has some sanction practice. It does not predict police. The next result shows that the deterrence margins the theorem requires can be produced with no specialized role at all. Whether the sanctioners are willing to produce them is the separate second-order question.
   250	
   251	\begin{proposition}[Minimal form]
   252	\label{prop:coercive-power:minimal-form}
   253	Consider $n$ agents who play the rule-compliance game in every period and also cooperate in a joint activity that yields each participant a per-period surplus $b > 0$. Let the profile be: every agent cooperates with every other agent who is not excluded; an agent who violates is excluded from cooperation for the next $L$ periods, and a violation by an excluded agent restarts the exclusion. Detection is perfect within the group. Then an agent with $r \in \{0, \dots, L\}$ future periods of exclusion remaining faces the deterrence margin
   254	\[
   255	d = b \sum_{k=r+1}^{L} \delta^k ,
   256	\]
   257	which equals $b\,\delta(1-\delta^L)/(1-\delta) > 0$ for an agent in good standing ($r = 0$). No agent holds a specialized sanctioning role, and with equal participation each agent's coercive control share is $1/n$, so $H^{\pC} = 1/n$.
   258	\end{proposition}
   259	
   260	\begin{proof}
   261	An agent with $r$ periods of exclusion remaining who complies at $t$ is excluded in periods $t+1, \dots, t+r$ and cooperates from $t+r+1$ onward. If it violates, it is excluded in periods $t+1, \dots, t+L$. The two continuations differ only in periods $t+r+1, \dots, t+L$, in which the complier receives $b$ and the violator does not, so $d = b\sum_{k=r+1}^{L}\delta^k$ by \eqref{eq:margin}. For $r = 0$ the sum is $b\,\delta(1-\delta^L)/(1-\delta)$. Exclusion is delivered by each agent withholding its own cooperation, so no agent holds authority over another's response, and under equal participation each holds an equal share $1/n$ of the decision-relevant control over coercive acts. Then $H^{\pC} = n \cdot (1/n)^2 = 1/n$.
   262	\end{proof}
   263	
   264	The margin is smallest, and equal to zero, for an agent already excluded for the full $L$ periods, which is why such profiles are usually combined with graduated sanctions or with longer exclusion for repeat violators. The proposition computes margins; it does not show that the profile is an equilibrium for the excluders. Each excluder forgoes its own surplus from cooperating with the violator, which is the second-order cost of \cref{prop:coercive-power:second-order}. Extending the profile so that anyone who cooperates with an excluded agent is also excluded supplies term (c). Whether the extended profile is an equilibrium depends on whether the surplus an agent would lose by being excluded from the whole group exceeds the surplus it forgoes by withholding cooperation from one violator, and we do not claim that it is an equilibrium in general. The ethnographic record suggests that terms (b) and (d) also operate: people are angered by violations, and in small groups each person's response matters.
   265	
   266	The ethnographic record of societies described as stateless or radically egalitarian supplies sanction practices of exactly this distributed kind. \Cref{tab:hardcases} summarizes them.
   267	
   268	\begin{table}[!htbp]
   269	\centering
   270	\small
   271	\caption{Minimal forms of the sanction function in societies commonly described as lacking coercive authority. The right column states the strongest reading on which the function is absent and the reason it does not hold.}
   272	\label{tab:hardcases}
   273	\renewcommand{\arraystretch}{1.15}
   274	\begin{tabularx}{\textwidth}{@{}L{2.3cm}YY@{}}
   275	\toprule
   276	Case & Documented sanction practice & Strongest counter-reading and reply \\
   277	\midrule
   278	Nuer \citep{evanspritchard1940} & Feud and the threat of retaliation by agnatic kin, settled by cattle compensation through the leopard-skin chief as mediator. & The leopard-skin chief has no power to compel. The sanction is held by kin groups, not by the mediator, so the function is present and the office is absent. \\
   279	Ju/'hoansi \citep{lee2013,marshall1976,wiessner2005} & Teasing, criticism, gossip and avoidance, with talk about norm violations recorded in camp conversations, and lethal violence in rare extreme cases. & This is the case most often cited as lacking hierarchy. The absence of an office is real, but the sanctions are frequent and documented. \\
   280	Amazonian societies \citep{clastres1987} & A chief who tries to command is abandoned or, in Clastres's reports, killed. & Clastres argues that these societies prevent power from separating from society. That supports the claim that concentration is contingent, while the group itself sanctions the chief. \\
   281	Foraging bands \citep{boehm1999,boehm2012} & Coalitions of subordinates use ridicule, disobedience, ostracism, exile and execution against would-be dominants. & Boehm calls the result a reverse dominance hierarchy. Egalitarianism is produced by sanctions rather than by their absence. \\
   282	Immediate-return societies \citep{woodburn1982} & Leveling mechanisms such as obligatory sharing, mockery and avoidance of anyone who claims authority. & Disputes are often resolved by moving away. Leaving costs the violator cooperation, which is a sanction when the violator values it. \\
   283	Commons \citep{ostrom1990,ostromdesign2010,cox2010} & Monitoring by users or accountable monitors, and graduated sanctions for those who break the rules. & Commons are often cited as order without a state. Ostrom's own design principles include monitoring and graduated sanctions. \\
   284	\bottomrule
   285	\end{tabularx}
   286	\end{table}
   287	
   288	Three features of the table deserve emphasis. The sanctions are distributed, so $H^{\pC}$ is low. They are rarely specialized: no person makes a living from them. And they are not mild. Boehm's reverse dominance hierarchy includes execution of persistent would-be dominants \citep{boehm1999}, and Lee recorded homicides among the Ju/'hoansi \citep{lee1979}. The egalitarian character of these societies does not come from the absence of coercion. It comes from the fact that coercion is held by the collective and directed against attempts to concentrate it. In the vocabulary of this series, the societies of \cref{tab:hardcases} have the coercive function (Proposition~A) and low concentration with high contestability (the negation of Proposition~B). Woodburn's phrase for the mechanism, institutions of leveling, describes a coercive pillar whose output is the prevention of capture \citep{woodburn1982}.
   289	
   290	The ethnographic evidence has known limits. Most of it was gathered after contact with states and markets, from groups living in marginal environments, and foraging societies vary more than the classic accounts suggest \citep{kelly1995}. \citet{graeber2021} argue that some societies moved seasonally between egalitarian and hierarchical arrangements, including temporary policing authority during collective hunts. If correct, this strengthens the present argument: the sanction function persists while its holders change with the season.
   291	
   292	\subsection{Counterexample attempts}
   293	\label{sec:counter}
   294	
   295	The strongest attempt to refute the necessity of coercion appeals to self-enforcing cooperation. Axelrod showed that reciprocal strategies can sustain cooperation without a central authority \citep{axelrod1984}. Greif showed that the eleventh-century Maghribi traders enforced agency contracts through a coalition in which cheated merchants were refused future employment by all members \citep{greif1993}. Edwards and Ogilvie dispute this reading and argue that the traders also relied on formal legal institutions \citep{edwards2012}; on either reading the case contains sanctions. Ellickson found that cattle ranchers in Shasta County settled disputes by neighborly norms rather than by law \citep{ellickson1991}. None of these is a counterexample. In each case an agent's continuation payoff depends on the agent's own past conduct: the reciprocator retaliates, the coalition refuses to deal, and the neighbor gossips or engages in self-help. Each mechanism is a sanction regime in the sense of \cref{def:coercive-power:regime}. What these cases refute is the Hobbesian inference from the need for sanctions to the need for a sovereign.
   296	
   297	A second attempt appeals to internalization. If socialization makes norm violation intrinsically costly, temptations may never be positive, and sanctions are unnecessary. The theorem accepts this as a logical possibility: internalization lowers $p$, and if $p \le \theta$ Ax5 fails and the coercive pillar is not derived for that rule. The bridge assumption claims that no functioning governance system achieves $p \le \theta$ for every rule it keeps in force. The societies that come closest, those of \cref{tab:hardcases}, are also the ones in which ethnographers record continual sanctioning talk \citep{wiessner2005}. Internalization and sanction are complements, not substitutes: shared norms reduce temptation and also supply the motive for punishing those who remain tempted (term (b) of \cref{prop:coercive-power:second-order}).
   298	
   299	A third attempt appeals to exit. Where dissatisfied members can simply leave, perhaps the collective needs no sanctions. Exit is a sanction when those who leave take with them something the violator valued. When exit costs the violator nothing, \cref{lem:coercive-power:deterrence} predicts violations at the unsanctioned rate $p$. A collective then persists only by relying on fewer rules that matter, which is what immediate-return foragers appear to do: with little storage there is less to steal and less to hoard \citep{woodburn1982}. Exit narrows the set of rules that require enforcement; it does not remove the function for the rules that remain.
   300	
   301	These replies define the falsifier, and the falsifier must not be immunized. The replies to the second and third attempts could be used to reclassify any compliant, unsanctioned collective as one with $p \le \theta$, which would make the necessity claim true by definition. To prevent this, the temptation share $p$ must be measured independently of the sanction practices it is used to explain, and before they are observed. Designs that offer members an unobserved opportunity to break a rule, so that no response by others is possible, measure the share who would violate in the absence of sanctions. Proposition~A for the coercive pillar is refuted by a persistent collective in which such a measurement gives $p > \theta$ for a rule in force, compliance is nonetheless above $1 - \theta$, and violators suffer no material, relational or reputational cost of any kind. A collective in which the measured $p$ is below $\theta$ for every rule in force refutes the bridge assumption instead. We found no documented case of either kind in the sources reviewed, and we know of no study that has carried out this measurement in a stateless society.
   302	
   303	\subsection{Functional necessity without functionalist explanation}
   304	
   305	The theorem claims the necessity of a function, not of an institution. That distinction answers the classic objection of \citet{hempel1959}: from the premise that a system needs some sanction practice, it does not follow that it needs a police force, because many functional equivalents can meet the need. \Cref{tab:hardcases} lists several. The theorem also makes no causal claim about why any particular polity has the coercive institutions it has. \citet{elster1979,elster1983} argued that explaining an institution by its beneficial effects requires a feedback mechanism from effects to institution. \Cref{thm:coercive-power:necessity} is a condition of persistence, not a functional explanation: collectives without a sanction regime do not keep rules in force, but the theorem says nothing about which sanction regime a collective adopts or why. That question belongs to the comparative analysis of \cref{sec:comparative}, where design varies with threats, finances and legitimating beliefs.
   306	
   307	\section{Literature on coercive power}
   308	\label{sec:literature}
   309	
   310	\subsection{Coercion and the making of states}
   311	
   312	Modern discussion of coercion begins with Weber's definition of the state as the human community that successfully claims the monopoly of the legitimate use of physical force within a territory \citep{weber1946,weber1978}. Part~II uses it where it treats the coupling of rule-making to enforcement. For the coercive pillar, the important word is ``claims''. Weber's definition concerns legitimacy, and \cref{sec:layer} has already separated it from command concentration.
   313	
   314	Tilly made coercion the engine of European state formation. Rulers who made war had to extract resources to pay for it, and the bargains they struck with those who held capital produced different state forms: coercion-intensive paths where rulers squeezed agrarian populations, capital-intensive paths where they borrowed from merchant cities, and capitalized-coercion paths in between \citep{tilly1990}. In an earlier essay Tilly compared war making and state making to organized crime, since the state sells protection against threats that it partly produces itself \citep{tilly1985}. The analogy is a heuristic, not an equivalence, and this paper treats it as a hypothesis about when coercion becomes capture. Karaman and Pamuk extended the fiscal side of the argument to show that the effect of warfare on state capacity depended on economic structure and regime type across Europe and the Ottoman Empire \citep{karaman2013}. The financing side of this literature belongs to Part~I; here the question is how the coercive apparatus that resulted was controlled.
   315	
   316	Mann distinguished despotic power, the range of actions rulers can take without negotiation with civil society, from infrastructural power, the capacity to penetrate society and implement decisions \citep{mann1984}. The distinction maps onto the two margins of \cref{def:coercive-power:margins}. A state with high infrastructural power can enforce rules widely (a large conduct margin is feasible); a state with high despotic power can direct enforcement as it pleases (a large allegiance margin is feasible). North, Wallis and Weingast described most of recorded history as limited-access orders in which specialists in violence agree not to fight because they share rents \citep{nww2009}. In the vocabulary of this series, such orders have high $C_{\pF\pC}$ by construction.
   317	
   318	\subsection{The guardian problem}
   319	
   320	If coercion is provisioned (term (a) of \cref{prop:coercive-power:second-order}), the agents who hold it can turn it against those who provision them. Civil-military relations theory is the study of this problem. Huntington proposed objective civilian control: a professional officer corps, autonomous in military matters and politically neutral \citep{huntington1957}. Janowitz replied that professionalism alone does not secure neutrality and that the military should be integrated into civilian society as a constabulary force \citep{janowitz1960}. Finer catalogued the forms of military intervention in politics \citep{finer1962}, and Huntington and Perlmutter described praetorian societies in which armed forces become ordinary political contestants \citep{huntington1968,perlmutter1969}. Feaver recast the relationship as a principal-agent problem in which civilians choose monitoring mechanisms and soldiers choose whether to work or shirk \citep{feaver1999,feaver2003}. Kohn emphasized that civilian control is a practice that must be exercised, not merely a constitutional provision \citep{kohn1997}.
   321	
   322	Authoritarian rulers face the guardian problem in a sharper form. Svolik showed that dictators face two separate problems: sharing power with the allied elites who help them rule, and controlling the masses they rule \citep{svolik2012}. Coercive agents are useful against the second problem and dangerous in the first. Quinlivan described the coup-proofing practices of Middle Eastern regimes: reliance on family, ethnic and religious loyalties, the creation of parallel military forces, and multiple overlapping internal security agencies \citep{quinlivan1999}. Pilster and B\"ohmelt found that coup-proofing reduced battlefield effectiveness in interstate wars between 1967 and 1999 \citep{pilster2011}. Greitens argued that the design of coercive institutions depends on whether rulers perceive their main threat as coming from elites or from the masses: elite threats favor fragmented and socially exclusive organizations, mass threats favor unified and inclusive ones, and these designs in turn shape patterns of state violence \citep{greitens2016}. Slater showed that elites who fear contentious mass politics may accept stronger coercive and extractive institutions as protection pacts \citep{slater2010}.
   323	
   324	\subsection{Repression and its limits}
   325	
   326	Repression is the use of coercion against political opponents, and it is the most direct observable form of the allegiance margin. Davenport's review defines repression broadly, from surveillance and bans to arrests, torture and mass killing, and organizes the field around the problem of how authorities use coercion against domestic challengers \citep{davenport2007}. Poe and Tate found in a 153-country analysis of the 1980s that democracy and participation in civil or international war had substantively important effects on repression of personal integrity rights \citep{poe1994}. Hill and Jones, using cross-validation rather than significance tests, found that few proposed explanations improve out-of-sample prediction much; democratic institutions predict some kinds of repression far better than others, and features of domestic legal systems perform well \citep{hill2014}. Wintrobe modeled dictators as trading off repression and the purchase of loyalty \citep{wintrobe1998}. Rejali documented a boundary case: democracies under public monitoring developed and exported torture techniques that leave few marks \citep{rejali2007}. Democracy constrains what coercers can be seen to do; it does not by itself eliminate the allegiance margin.
   327	
   328	Whether coercive agents carry out repression is not guaranteed. Bellin attributed the durability of Middle Eastern authoritarianism to the will and capacity of coercive apparatuses to repress, and after the Arab uprisings of 2011 she examined why some militaries defected and others did not \citep{bellin2004,bellin2012}. Albrecht and Ohl applied Hirschman's categories of exit, voice and loyalty to military behavior during unrest \citep{albrecht2016}, and Chenoweth and Stephan argued that nonviolent campaigns succeed in part by inducing defections among security forces \citep{chenoweth2011}. Gerschewski placed repression beside legitimation and co-optation as the three pillars of autocratic stability \citep{gerschewski2013}.
   329	

exec
/usr/local/bin/zsh -lc "sed -n '730,1037p' papers/latex/coercive-power.tex | nl -ba -v730" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   730	
   731	\bibitem[Coppedge et~al.(2011)]{coppedge2011}
   732	Coppedge, Michael and Gerring, John and Altman, David and Bernhard, Michael and Fish, Steven and Hicken, Allen and Kroenig, Matthew and Lindberg, Staffan I. and McMann, Kelly and Paxton, Pamela and Semetko, Holli A. and Skaaning, Svend-Erik and Staton, Jeffrey and Teorell, Jan (2011). Conceptualizing and Measuring Democracy: A New Approach. \emph{Perspectives on Politics} 9(2):247-267. doi:10.1017/S1537592711000880.
   733	
   734	\bibitem[Cordesman(2003)]{cordesman2003}
   735	Cordesman, Anthony H. (2003). \emph{Saudi Arabia Enters the Twenty-First Century: The Military and International Security Dimensions}. Praeger.
   736	
   737	\bibitem[Cox et~al.(2010)]{cox2010}
   738	Cox, Michael and Arnold, Gwen and Villamayor Tomas, Sergio (2010). A Review of Design Principles for Community-based Natural Resource Management. \emph{Ecology and Society} 15(4), article 38. doi:10.5751/ES-03704-150438.
   739	
   740	\bibitem[Crone(1980)]{crone1980}
   741	Crone, Patricia (1980). \emph{Slaves on Horses: The Evolution of the Islamic Polity}. Cambridge University Press. doi:10.1017/cbo9780511563508.
   742	
   743	\bibitem[Davenport(2007)]{davenport2007}
   744	Davenport, Christian (2007). State Repression and Political Order. \emph{Annual Review of Political Science} 10:1-23. doi:10.1146/annurev.polisci.10.101405.143216.
   745	
   746	\bibitem[Edwards and Ogilvie(2012)]{edwards2012}
   747	Edwards, Jeremy and Ogilvie, Sheilagh (2012). Contract Enforcement, Institutions, and Social Capital: The Maghribi Traders Reappraised. \emph{Economic History Review} 65(2):421-444. doi:10.1111/j.1468-0289.2011.00635.x.
   748	
   749	\bibitem[Eisenhower(1961)]{eisenhower1961}
   750	Eisenhower, Dwight D. (1961). \emph{Farewell Radio and Television Address to the American People, 17 January 1961}. Public Papers of the Presidents. \url{https://www.eisenhowerlibrary.gov/research/online-documents/farewell-address}.
   751	
   752	\bibitem[Ellickson(1991)]{ellickson1991}
   753	Ellickson, Robert C. (1991). \emph{Order without Law: How Neighbors Settle Disputes}. Harvard University Press. doi:10.4159/9780674036437.
   754	
   755	\bibitem[Elliott(1963)]{elliott1963}
   756	Elliott, J. H. (1963). \emph{Imperial Spain 1469-1716}. Edward Arnold.
   757	
   758	\bibitem[Elster(1979)]{elster1979}
   759	Elster, Jon (1979). \emph{Ulysses and the Sirens: Studies in Rationality and Irrationality}. Cambridge University Press.
   760	
   761	\bibitem[Elster(1983)]{elster1983}
   762	Elster, Jon (1983). \emph{Explaining Technical Change: A Case Study in the Philosophy of Science}. Cambridge University Press.
   763	
   764	\bibitem[Ertman(1997)]{ertman1997}
   765	Ertman, Thomas (1997). \emph{Birth of the Leviathan: Building States and Regimes in Medieval and Early Modern Europe}. Cambridge University Press. doi:10.1017/cbo9780511529016.
   766	
   767	\bibitem[Evans-Pritchard(1940)]{evanspritchard1940}
   768	Evans-Pritchard, E. E. (1940). \emph{The Nuer: A Description of the Modes of Livelihood and Political Institutions of a Nilotic People}. Clarendon Press.
   769	
   770	\bibitem[Feaver(1999)]{feaver1999}
   771	Feaver, Peter D. (1999). Civil-Military Relations. \emph{Annual Review of Political Science} 2:211-241. doi:10.1146/annurev.polisci.2.1.211.
   772	
   773	\bibitem[Feaver(2003)]{feaver2003}
   774	Feaver, Peter D. (2003). \emph{Armed Servants: Agency, Oversight, and Civil-Military Relations}. Harvard University Press. doi:10.4159/9780674036772.
   775	
   776	\bibitem[Fehr and G\"achter(2002)]{fehr2002}
   777	Fehr, Ernst and G\"achter, Simon (2002). Altruistic Punishment in Humans. \emph{Nature} 415:137-140. doi:10.1038/415137a.
   778	
   779	\bibitem[Finer(1962)]{finer1962}
   780	Finer, Samuel E. (1962). \emph{The Man on Horseback: The Role of the Military in Politics}. Pall Mall Press.
   781	
   782	\bibitem[Foucault(1977)]{foucault1977}
   783	Foucault, Michel (1977). \emph{Discipline and Punish: The Birth of the Prison}. Pantheon Books.
   784	
   785	\bibitem[Friesen(2001)]{friesen2001}
   786	Friesen, Steven J. (2001). \emph{Imperial Cults and the Apocalypse of John: Reading Revelation in the Ruins}. Oxford University Press. doi:10.1093/0195131533.001.0001.
   787	
   788	\bibitem[Fuller(1995)]{fuller1995}
   789	Fuller, Robert C. (1995). \emph{Naming the Antichrist: The History of an American Obsession}. Oxford University Press. doi:10.1093/acprof:oso/9780195109795.001.0001.
   790	
   791	\bibitem[Gause(1994)]{gause1994}
   792	Gause, F. Gregory III (1994). \emph{Oil Monarchies: Domestic and Security Challenges in the Arab Gulf States}. Council on Foreign Relations Press.
   793	
   794	\bibitem[Gerschewski(2013)]{gerschewski2013}
   795	Gerschewski, Johannes (2013). The Three Pillars of Stability: Legitimation, Repression, and Co-optation in Autocratic Regimes. \emph{Democratization} 20(1):13-38. doi:10.1080/13510347.2013.738860.
   796	
   797	\bibitem[Getty(1985)]{getty1985}
   798	Getty, J. Arch (1985). \emph{Origins of the Great Purges: The Soviet Communist Party Reconsidered, 1933-1938}. Cambridge University Press. doi:10.1017/cbo9780511572616.
   799	
   800	\bibitem[Gieseke(2014)]{gieseke2014}
   801	Gieseke, Jens (2014). \emph{The History of the Stasi: East Germany's Secret Police, 1945-1990}. Berghahn Books. doi:10.3167/9781782382546.
   802	
   803	\bibitem[Graeber and Wengrow(2021)]{graeber2021}
   804	Graeber, David and Wengrow, David (2021). \emph{The Dawn of Everything: A New History of Humanity}. Farrar, Straus and Giroux.
   805	
   806	\bibitem[Gregory and Lazarev(2003)]{gregory2003}
   807	Gregory, Paul R. and Lazarev, Valery (eds.) (2003). \emph{The Economics of Forced Labor: The Soviet Gulag}. Hoover Institution Press.
   808	
   809	\bibitem[Greif(1993)]{greif1993}
   810	Greif, Avner (1993). Contract Enforceability and Economic Institutions in Early Trade: The Maghribi Traders' Coalition. \emph{American Economic Review} 83(3):525-548. \url{https://www.jstor.org/stable/2117532}.
   811	
   812	\bibitem[Greitens(2016)]{greitens2016}
   813	Greitens, Sheena Chestnut (2016). \emph{Dictators and Their Secret Police: Coercive Institutions and State Violence}. Cambridge University Press. doi:10.1017/cbo9781316489031.
   814	
   815	\bibitem[Hedlund(2011)]{hedlund2011}
   816	Hedlund, Erik (2011). Civil-Military Control over the Swedish Military Profession. \emph{Armed Forces \& Society} 39(1):135-157. Published online 2011; print issue 2013. doi:10.1177/0095327X11426256.
   817	
   818	\bibitem[Hegghammer and Lacroix(2007)]{hegghammer2007}
   819	Hegghammer, Thomas and Lacroix, St\'ephane (2007). Rejectionist Islamism in Saudi Arabia: The Story of Juhayman al-'Utaybi Revisited. \emph{International Journal of Middle East Studies} 39(1):103-122. doi:10.1017/s0020743807002553.
   820	
   821	\bibitem[Hempel(1959)]{hempel1959}
   822	Hempel, Carl G. (1959). The Logic of Functional Analysis. In Llewellyn Gross (ed.), \emph{Symposium on Sociological Theory}. Harper \& Row.
   823	
   824	\bibitem[Hill and Jones(2014)]{hill2014}
   825	Hill, Daniel W. and Jones, Zachary M. (2014). An Empirical Evaluation of Explanations for State Repression. \emph{American Political Science Review} 108(3):661-687. doi:10.1017/S0003055414000306.
   826	
   827	\bibitem[Hobbes(1651)]{hobbes1651}
   828	Hobbes, Thomas (1651). \emph{Leviathan}. Edited by Richard Tuck. Cambridge University Press, 1996. doi:10.1017/CBO9780511808166.
   829	
   830	\bibitem[Huntington(1957)]{huntington1957}
   831	Huntington, Samuel P. (1957). \emph{The Soldier and the State: The Theory and Politics of Civil-Military Relations}. Harvard University Press. doi:10.2307/j.ctvjf9wx3.
   832	
   833	\bibitem[Huntington(1968)]{huntington1968}
   834	Huntington, Samuel P. (1968). \emph{Political Order in Changing Societies}. Yale University Press.
   835	
   836	\bibitem[Irwin(1986)]{irwin1986}
   837	Irwin, Robert (1986). \emph{The Middle East in the Middle Ages: The Early Mamluk Sultanate 1250-1382}. Southern Illinois University Press.
   838	
   839	\bibitem[Jackson et~al.(2012)]{jackson2012}
   840	Jackson, Jonathan and Bradford, Ben and Hough, Mike and Myhill, Andy and Quinton, Paul and Tyler, Tom R. (2012). Why Do People Comply with the Law? Legitimacy and the Influence of Legal Institutions. \emph{British Journal of Criminology} 52(6):1051-1071. doi:10.1093/bjc/azs032.
   841	
   842	\bibitem[Janowitz(1960)]{janowitz1960}
   843	Janowitz, Morris (1960). \emph{The Professional Soldier: A Social and Political Portrait}. Free Press.
   844	
   845	\bibitem[Kamen(1997)]{kamen1997}
   846	Kamen, Henry (1997). \emph{The Spanish Inquisition: A Historical Revision}. Yale University Press.
   847	
   848	\bibitem[Karaman and Pamuk(2013)]{karaman2013}
   849	Karaman, K. K{\i}van\c{c} and Pamuk, \c{S}evket (2013). Different Paths to the Modern State in Europe: The Interaction between Warfare, Economic Structure, and Political Regime. \emph{American Political Science Review} 107(3):603-626. doi:10.1017/S0003055413000312.
   850	
   851	\bibitem[Katzman(1993)]{katzman1993}
   852	Katzman, Kenneth (1993). \emph{The Warriors of Islam: Iran's Revolutionary Guard}. Westview Press.
   853	
   854	\bibitem[Kelly(1995)]{kelly1995}
   855	Kelly, Robert L. (1995). \emph{The Foraging Spectrum: Diversity in Hunter-Gatherer Lifeways}. Smithsonian Institution Press. doi:10.2307/j.ctv2sx9gc9.
   856	
   857	\bibitem[Kennedy(2001)]{kennedy2001}
   858	Kennedy, Hugh (2001). \emph{The Armies of the Caliphs: Military and Society in the Early Islamic State}. Routledge.
   859	
   860	\bibitem[Knight(1996)]{knight1996}
   861	Knight, Amy (1996). \emph{Spies without Cloaks: The KGB's Successors}. Princeton University Press. doi:10.2307/j.ctt15sk83q.
   862	
   863	\bibitem[Knowles et~al.(2001)]{knowles2001}
   864	Knowles, John and Persico, Nicola and Todd, Petra (2001). Racial Bias in Motor Vehicle Searches: Theory and Evidence. \emph{Journal of Political Economy} 109(1):203-229. doi:10.1086/318603.
   865	
   866	\bibitem[Koehler(1999)]{koehler1999}
   867	Koehler, John O. (1999). \emph{Stasi: The Untold Story of the East German Secret Police}. Westview Press.
   868	
   869	\bibitem[Koester(2014)]{koester2014}
   870	Koester, Craig R. (2014). \emph{Revelation: A New Translation with Introduction and Commentary}. Yale University Press (Anchor Yale Bible 38A). doi:10.12987/9780300211030.
   871	
   872	\bibitem[Kohn(1997)]{kohn1997}
   873	Kohn, Richard H. (1997). How Democracies Control the Military. \emph{Journal of Democracy} 8(4):140-153. doi:10.1353/jod.1997.0060.
   874	
   875	\bibitem[Kornai(1992)]{kornai1992}
   876	Kornai, J\'anos (1992). \emph{The Socialist System: The Political Economy of Communism}. Princeton University Press. doi:10.2307/j.ctv1ddczdr.
   877	
   878	\bibitem[Kovacs and Rowland(2004)]{kovacs2004}
   879	Kovacs, Judith and Rowland, Christopher (2004). \emph{Revelation: The Apocalypse of Jesus Christ}. Blackwell (Blackwell Bible Commentaries). doi:10.1002/9780470773512.
   880	
   881	\bibitem[Kraybill(1996)]{kraybill1996}
   882	Kraybill, J. Nelson (1996). \emph{Imperial Cult and Commerce in John's Apocalypse}. Sheffield Academic Press (JSNT Supplement 132).
   883	
   884	\bibitem[Kunt(1983)]{kunt1983}
   885	Kunt, I. Metin (1983). \emph{The Sultan's Servants: The Transformation of Ottoman Provincial Government, 1550-1650}. Columbia University Press.
   886	
   887	\bibitem[Kuran(1991)]{kuran1991}
   888	Kuran, Timur (1991). Now Out of Never: The Element of Surprise in the East European Revolution of 1989. \emph{World Politics} 44(1):7-48. doi:10.2307/2010422.
   889	
   890	\bibitem[Largo(2026)]{largo2026hbs}
   891	Largo, Mateo (2026). \emph{The Hierarchy of the Beast System: Institutional Power, Elite Coordination, and Economic Dependency Across Political Regimes}. Working paper, 14 October 2026.
   892	
   893	\bibitem[Lee(1979)]{lee1979}
   894	Lee, Richard B. (1979). \emph{The !Kung San: Men, Women, and Work in a Foraging Society}. Cambridge University Press.
   895	
   896	\bibitem[Lee(2013)]{lee2013}
   897	Lee, Richard B. (2013). \emph{The Dobe Ju/'hoansi}. 4th edition. Wadsworth/Cengage Learning.
   898	
   899	\bibitem[Leggett(1981)]{leggett1981}
   900	Leggett, George (1981). \emph{The Cheka: Lenin's Political Police}. Oxford University Press.
   901	
   902	\bibitem[Lynn(1997)]{lynn1997}
   903	Lynn, John A. (1997). \emph{Giant of the Grand Si\`ecle: The French Army, 1610-1715}. Cambridge University Press. doi:10.1017/cbo9780511572548.
   904	
   905	\bibitem[Madison(1788)]{madison1788}
   906	Madison, James (1788). \emph{The Federalist No. 51: The Structure of the Government Must Furnish the Proper Checks and Balances}. Independent Journal, 6 February 1788. \url{https://avalon.law.yale.edu/18th_century/fed51.asp}.
   907	
   908	\bibitem[Mann(1984)]{mann1984}
   909	Mann, Michael (1984). The Autonomous Power of the State: Its Origins, Mechanisms and Results. \emph{European Journal of Sociology} 25(2):185-213. doi:10.1017/S0003975600004239.
   910	
   911	\bibitem[Marshall(1976)]{marshall1976}
   912	Marshall, Lorna (1976). \emph{The !Kung of Nyae Nyae}. Harvard University Press. doi:10.4159/harvard.9780674180574.
   913	
   914	\bibitem[McGinn(1998)]{mcginn1998}
   915	McGinn, Bernard (1998). \emph{Antichrist: Two Thousand Years of the Human Fascination with Evil}. Columbia University Press.
   916	
   917	\bibitem[North et~al.(2009)]{nww2009}
   918	North, Douglass C. and Wallis, John Joseph and Weingast, Barry R. (2009). \emph{Violence and Social Orders: A Conceptual Framework for Interpreting Recorded Human History}. Cambridge University Press. doi:10.1017/CBO9780511575839.
   919	
   920	\bibitem[{EOS Committee}(2026)]{eos2026} Norwegian Parliamentary Oversight Committee on Intelligence and Security Services (EOS Committee) (2026). History of the EOS Committee. \url{https://eos-utvalget.no/en/home/about-the-eos-committee/history}. Accessed 22 October 2026.
   921	
   922	\bibitem[Olson(1965)]{olson1965}
   923	Olson, Mancur (1965). \emph{The Logic of Collective Action: Public Goods and the Theory of Groups}. Harvard University Press. doi:10.4159/9780674041660.
   924	
   925	\bibitem[Ostrom(1990)]{ostrom1990}
   926	Ostrom, Elinor (1990). \emph{Governing the Commons: The Evolution of Institutions for Collective Action}. Cambridge University Press. doi:10.1017/CBO9780511807763.
   927	
   928	\bibitem[Ostrom(2010)]{ostromdesign2010}
   929	Ostrom, Elinor (2010). Beyond Markets and States: Polycentric Governance of Complex Economic Systems. \emph{American Economic Review} 100(3):641-672. doi:10.1257/aer.100.3.641.
   930	
   931	\bibitem[Parker(1972)]{parker1972}
   932	Parker, Geoffrey (1972). \emph{The Army of Flanders and the Spanish Road, 1567-1659}. Cambridge University Press.
   933	
   934	\bibitem[Parker(1988)]{parker1988}
   935	Parker, Geoffrey (1988). \emph{The Military Revolution: Military Innovation and the Rise of the West, 1500-1800}. Cambridge University Press.
   936	
   937	\bibitem[Parrott(2012)]{parrott2012}
   938	Parrott, David (2012). \emph{The Business of War: Military Enterprise and Military Revolution in Early Modern Europe}. Cambridge University Press. doi:10.1017/cbo9781139023337.
   939	
   940	\bibitem[Perlmutter(1969)]{perlmutter1969}
   941	Perlmutter, Amos (1969). The Praetorian State and the Praetorian Army: Toward a Taxonomy of Civil-Military Relations in Developing Polities. \emph{Comparative Politics} 1(3):382-404. doi:10.2307/421446.
   942	
   943	\bibitem[Pilster and B\"ohmelt(2011)]{pilster2011}
   944	Pilster, Ulrich and B\"ohmelt, Tobias (2011). Coup-Proofing and Military Effectiveness in Interstate Wars, 1967-99. \emph{Conflict Management and Peace Science} 28(4):331-350. doi:10.1177/0738894211413062.
   945	
   946	\bibitem[Pipes(1981)]{pipes1981}
   947	Pipes, Daniel (1981). \emph{Slave Soldiers and Islam: The Genesis of a Military System}. Yale University Press.
   948	
   949	\bibitem[Poe and Tate(1994)]{poe1994}
   950	Poe, Steven C. and Tate, C. Neal (1994). Repression of Human Rights to Personal Integrity in the 1980s: A Global Analysis. \emph{American Political Science Review} 88(4):853-872. doi:10.2307/2082712.
   951	
   952	\bibitem[Powell and Thyne(2011)]{powell2011}
   953	Powell, Jonathan M. and Thyne, Clayton L. (2011). Global Instances of Coups from 1950 to 2010: A New Dataset. \emph{Journal of Peace Research} 48(2):249-259. doi:10.1177/0022343310397436.
   954	
   955	\bibitem[Pratt(2008a)]{pratt2008a}
   956	Pratt, John (2008a). Scandinavian Exceptionalism in an Era of Penal Excess. Part I: The Nature and Roots of Scandinavian Exceptionalism. \emph{British Journal of Criminology} 48(2):119-137. doi:10.1093/bjc/azm072.
   957	
   958	\bibitem[Pratt(2008b)]{pratt2008b}
   959	Pratt, John (2008b). Scandinavian Exceptionalism in an Era of Penal Excess. Part II: Does Scandinavian Exceptionalism Have a Future? \emph{British Journal of Criminology} 48(3):275-292. doi:10.1093/bjc/azm073.
   960	
   961	\bibitem[Quinlivan(1999)]{quinlivan1999}
   962	Quinlivan, James T. (1999). Coup-proofing: Its Practice and Consequences in the Middle East. \emph{International Security} 24(2):131-165. doi:10.1162/016228899560202.
   963	
   964	\bibitem[Rejali(2007)]{rejali2007}
   965	Rejali, Darius (2007). \emph{Torture and Democracy}. Princeton University Press. doi:10.1515/9781400830879.
   966	
   967	\bibitem[Riksdagens ombudsm\"an(2026)]{jo2026}
   968	Riksdagens ombudsm\"an (Parliamentary Ombudsmen of Sweden) (2026). History of the Parliamentary Ombudsmen. \url{https://www.jo.se/en/about-jo/history/}. Accessed 22 October 2026.
   969	
   970	\bibitem[Rowlands(2002)]{rowlands2002}
   971	Rowlands, Guy (2002). \emph{The Dynastic State and the Army under Louis XIV: Royal Service and Private Interest, 1661-1701}. Cambridge University Press. doi:10.1017/cbo9780511496882.
   972	
   973	\bibitem[{S\"akerhetstj\"anstkommissionen}(2002)]{sou2002} S\"akerhetstj\"anstkommissionen (2002). \emph{Rikets s\"akerhet och den personliga integriteten: De svenska s\"akerhetstj\"ansternas f\"orfattningsskyddande verksamhet sedan \aa{}r 1945}. SOU 2002:87. Stockholm: Justitiedepartementet. \url{https://regeringen.se/rattsliga-dokument/statens-offentliga-utredningar/2002/01/sou-200287/}.
   974	
   975	\bibitem[Scoggins and O'Brien(2016)]{scoggins2016}
   976	Scoggins, Suzanne E. and O'Brien, Kevin J. (2016). China's Unhappy Police. \emph{Asian Survey} 56(2):225-242. doi:10.1525/as.2016.56.2.225.
   977	
   978	\bibitem[Shambaugh(2002)]{shambaugh2002}
   979	Shambaugh, David (2002). \emph{Modernizing China's Military: Progress, Problems, and Prospects}. University of California Press. doi:10.1525/9780520938106.
   980	
   981	\bibitem[Slater(2010)]{slater2010}
   982	Slater, Dan (2010). \emph{Ordering Power: Contentious Politics and Authoritarian Leviathans in Southeast Asia}. Cambridge University Press. doi:10.1017/cbo9780511760891.
   983	
   984	\bibitem[Svolik(2012)]{svolik2012}
   985	Svolik, Milan W. (2012). \emph{The Politics of Authoritarian Rule}. Cambridge University Press. doi:10.1017/CBO9781139176040.
   986	
   987	\bibitem[{Swedish Government}(1999)]{dir1999} Swedish Government (1999). Kommission f\"or granskning av de svenska s\"akerhetstj\"ansternas f\"orfattningsskyddande verksamhet. Committee directive Dir. 1999:26, 25 March 1999. \url{https://data.riksdagen.se/dokument/GNB126}.
   988	
   989	\bibitem[Tezcan(2010)]{tezcan2010}
   990	Tezcan, Baki (2010). \emph{The Second Ottoman Empire: Political and Social Transformation in the Early Modern World}. Cambridge University Press.
   991	
   992	\bibitem[Thompson(1976)]{thompson1976}
   993	Thompson, I. A. A. (1976). \emph{War and Government in Habsburg Spain, 1560-1620}. Athlone Press.
   994	
   995	\bibitem[Thompson(1990)]{thompson1990}
   996	Thompson, Leonard L. (1990). \emph{The Book of Revelation: Apocalypse and Empire}. Oxford University Press. doi:10.1093/oso/9780195055511.001.0001.
   997	
   998	\bibitem[Tilly(1985)]{tilly1985}
   999	Tilly, Charles (1985). War Making and State Making as Organized Crime. In Peter B. Evans, Dietrich Rueschemeyer and Theda Skocpol (eds.), \emph{Bringing the State Back In}. Cambridge University Press. doi:10.1017/cbo9780511628283.008.
  1000	
  1001	\bibitem[Tilly(1990)]{tilly1990}
  1002	Tilly, Charles (1990). \emph{Coercion, Capital, and European States, AD 990-1990}. Blackwell.
  1003	
  1004	\bibitem[Tyler(1990)]{tyler1990}
  1005	Tyler, Tom R. (1990). \emph{Why People Obey the Law}. Yale University Press. doi:10.1515/9781400828609.
  1006	
  1007	\bibitem[{Commission on Industrial Relations}(1915)]{cir1915} United States Commission on Industrial Relations (1915). \emph{Final Report of the Commission on Industrial Relations}. Washington, DC. \url{https://archive.org/details/finalreportofcom00unitiala}.
  1008	
  1009	\bibitem[{United States Senate}(1976)]{church1976} United States Senate, Select Committee to Study Governmental Operations with Respect to Intelligence Activities (1976). \emph{Intelligence Activities and the Rights of Americans}. Final Report, Book II, S. Rep. No. 94-755. U.S. Government Printing Office.
  1010	
  1011	\bibitem[Weber(1946)]{weber1946}
  1012	Weber, Max (1946). Politics as a Vocation. In H. H. Gerth and C. Wright Mills (eds.), \emph{From Max Weber: Essays in Sociology}. Oxford University Press.
  1013	
  1014	\bibitem[Weber(1978)]{weber1978}
  1015	Weber, Max (1978). \emph{Economy and Society: An Outline of Interpretive Sociology}. University of California Press. doi:10.4159/9780674240827.
  1016	
  1017	\bibitem[Wehrey et~al.(2009)]{wehrey2009}
  1018	Wehrey, Frederic and Green, Jerrold D. and Nichiporuk, Brian and Nader, Alireza and Hansell, Lydia and Nafisi, Rasool and Bohandy, S. R. (2009). \emph{The Rise of the Pasdaran: Assessing the Domestic Roles of Iran's Islamic Revolutionary Guards Corps}. RAND Corporation, MG-821-OSD.
  1019	
  1020	\bibitem[Wiessner(2005)]{wiessner2005}
  1021	Wiessner, Polly (2005). Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity? \emph{Human Nature} 16(2):115-145. doi:10.1007/s12110-005-1000-9.
  1022	
  1023	\bibitem[Wink(1992)]{wink1992}
  1024	Wink, Walter (1992). \emph{Engaging the Powers: Discernment and Resistance in a World of Domination}. Fortress Press. doi:10.2307/j.ctt1tm7j16.
  1025	
  1026	\bibitem[Wintrobe(1998)]{wintrobe1998}
  1027	Wintrobe, Ronald (1998). \emph{The Political Economy of Dictatorship}. Cambridge University Press. doi:10.1017/cbo9781139174916.
  1028	
  1029	\bibitem[Woodburn(1982)]{woodburn1982}
  1030	Woodburn, James (1982). Egalitarian Societies. \emph{Man (N.S.)} 17(3):431-451. doi:10.2307/2801707.
  1031	
  1032	\bibitem[Yoder(1972)]{yoder1972}
  1033	Yoder, John Howard (1972). \emph{The Politics of Jesus}. Eerdmans.
  1034	
  1035	\end{thebibliography}
  1036	
  1037	\end{document}

exec
/usr/local/bin/zsh -lc "sed -n '530,729p' papers/latex/coercive-power.tex | nl -ba -v530" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   530	
   531	Rulers have long tried to solve the guardian problem by recruiting coercers who have no independent social base: foreigners, captives, slaves or men cut off from their families. The Abbasid and Mamluk slave soldiers, the Ottoman kul and the papal Swiss Guard are instances. The following proposition states why the strategy works at first and why it tends to fail later.
   532	
   533	\begin{proposition}[Dependent corps]
   534	\label{prop:coercive-power:outsider}
   535	A corps receives compensation $w_t \le \bar{w}$ per period from a ruler whose fiscal capacity bounds $\bar{w}$. The corps accumulates capacity $Z_t$: arms, offices, property, marriages and local recruitment. The value to the corps of seizing control is $\Gamma(Z_t)$, non-decreasing in $Z_t$, and an attempt costs $\chi > 0$. The corps remains subordinate in period $t$ only if $\sum_{k \ge 0}\delta^k w_{t+k} \ge \Gamma(Z_t) - \chi$. If $Z_t$ is non-decreasing and $\lim_{t\to\infty}\Gamma(Z_t) > \bar{w}/(1-\delta) + \chi$, then there is a finite $T$ such that for all $t \ge T$ the corps is not subordinate, unless the ruler lowers $Z_t$, raises $\chi$, or raises the ceiling $\bar{w}$.
   536	\end{proposition}
   537	
   538	\begin{proof}
   539	The left side of the subordination condition is at most $\bar{w}/(1-\delta)$. Because $\Gamma(Z_t)$ is non-decreasing in $t$ and its limit exceeds $\bar{w}/(1-\delta) + \chi$, there is a finite $T$ with $\Gamma(Z_T) - \chi > \bar{w}/(1-\delta)$, and the inequality persists for all $t \ge T$. The condition can be restored only by changing one of $Z_t$, $\chi$ or $\bar{w}$.
   540	\end{proof}
   541	
   542	The proposition is simple, and its interest lies in what it explains. It treats an attempt as successful; a probability of success below one lowers the expected value of seizure and delays $T$ without changing the logic. Recruiting outsiders lowers $Z_0$: a corps with no kin, land or local allies gains little from seizing power because it cannot rule alone. This is the logic Crone attributed to the adoption of military slavery \citep{crone1980}. Over time the corps acquires exactly the assets that raise $Z_t$. The value of seizing a polity is bounded by what the polity produces, so the threshold condition, not unbounded growth, is what matters: the corps must come to value control more than the most the ruler can pay. The ruler's three countermeasures correspond to the three escape clauses. Rotation of commanders, prohibition of property holding and periodic purges keep $Z_t$ low. Counterweights of the kind analyzed in \cref{prop:coercive-power:coup-proofing} raise the cost $\chi$ of an attempt. Fiscal expansion raises $\bar{w}$. The Mamluks, who became rulers of Egypt and Syria \citep{irwin1986}, and the Janissaries, whose part in the deposition and killing of Osman II in 1622 marked a lasting change in Ottoman politics \citep{tezcan2010}, are the paradigm cases. The proposition also applies to modern forces whose economic holdings grow, since business activity raises $Z_t$ directly. This is the mechanism behind the concern that the economic expansion of Iran's Revolutionary Guard increases its political autonomy \citep{wehrey2009,alfoneh2013}. In democracies the analogous measures are term limits for commanders, prohibitions on military business and civilian control of promotions.
   543	
   544	\subsection{Coercion and production}
   545	\label{sec:cw}
   546	
   547	The pair of coercion and production is the primary responsibility of this Part among the fifteen cross-pillar pairs. The dependencies run in both directions, and the integration coefficient $C_{\pC\pW}$ measures something narrower than either.
   548	
   549	From production to coercion ($\pW \to \pC$), every army and police force consumes labor time. Conscription takes it directly from the producing population as an obligation. Professional forces take it through wages paid from taxes. Slave-soldier systems took it by acquiring people as a resource. The mode of recruitment shapes accountability: a conscript army is drawn from the whole population and depends on its consent, while a professional or outsider force depends on its paymaster. This is a further reason why term (a) of \cref{prop:coercive-power:second-order} carries political consequences.
   550	
   551	From coercion to production ($\pC \to \pW$), sanctions can compel work. The categories must be kept distinct, and this paper uses the bondage spectrum of Part~VI (Definition~2.4). Wage labor and taxation leave lawful mobility and personal ownership with the producer; the sanctions behind them are the general law of contract and of revenue. Serfdom ties the producer to land or lord. Compelled state labor, which includes corv\'ee, labor drafts and penal labor, is compelled by sanction for a term. Chattel slavery makes the person property. Only the last three are forms of bondage, and the coercive pillar is directly engaged in each of them. The Soviet camp system combined penal labor with economic planning on a scale that made coercion a direct input to production \citep{applebaum2003,gregory2003}. The series uses the language of bondage beyond these legal categories only in the disciplined, metaphorical sense of the source paper \citep{largo2026hbs}. Part~VI treats the production side of the pair, including the exit and voice that producers can use against dependence (Part~VI, Definition~2.5).
   552	
   553	A high value of $C_{\pC\pW}$ means that the same coalition commands both the coercive apparatus and the allocation of labor. In the extreme case, the deterrence margin of \cref{def:coercive-power:regime} is applied to failures to work. Proposition~B for this pair requires such integration together with a positive allegiance margin, so that the obligation to work falls more heavily on opponents, and with low contestability. The Gulag combined all three, since the same party-state directed the security organs that filled the camps and the plans that used their labor, and political offenses were among the grounds of confinement \citep{applebaum2003}. Universal conscription in a democracy with high $Q^{\pC}$ involves the dependency $\pW \to \pC$ but neither high integration nor an allegiance margin.
   554	
   555	\subsection{Checks that interrupt transmission}
   556	
   557	The source paper's second proposition holds that effective independent review and voice reduce the probability that attempted capture yields persistent unreviewable outcomes \citep{largo2026hbs}. In the coercive pillar the checks act on the margins directly. Judicial authorization of intrusive measures raises the evidentiary threshold for coercive acts, which lowers $\psi(0,y)$ for everyone and so raises the conduct margin. Independent complaint bodies make a positive allegiance margin visible and therefore costly. Individual liability of agents for unlawful force raises the private cost of arbitrary coercion for the coercers themselves. Protected refusal of unlawful orders introduces a veto at the point of execution: when soldiers or police refuse to fire on peaceful crowds, the allegiance margin is cut off at its source, which is the mechanism that Chenoweth and Stephan and Albrecht and Ohl identify in security-force defection \citep{chenoweth2011,albrecht2016}.
   558	
   559	These checks have small-scale analogues. Ostrom's design principles for long-enduring commons include monitors who are accountable to users and graduated sanctions that begin with small penalties \citep{ostrom1990,ostromdesign2010}. Graduated sanctions keep the magnitude $\mu$ proportional to the violation, which limits the damage when $\psi(0,y)$ is positive by mistake. Accountability of monitors to users is a small-scale version of component (1) of $Q^{\pC}$. The reverse dominance hierarchy of foraging bands is a check of the same kind: the collective holds the sanction and directs it against those who try to concentrate it \citep{boehm1999}. Madison's argument that ambition must be made to counteract ambition is the constitutional statement of the same principle \citep{madison1788}.
   560	
   561	Checks can fail. Each depends on another pillar: judicial authorization on judicial independence (Part~III), complaints and refusal on legitimating beliefs (Part~IV), and appointments on the political pillar (Part~II). Capture of any of these pillars by the coalition that commands coercion removes the corresponding check. This is the mechanism by which high cross-pillar integration $\Integ_t$ turns a concentrated coercive pillar into an unaccountable one, and it is why the coercive pillar cannot be assessed in isolation.
   562	
   563	\section{Measurement and hypotheses}
   564	\label{sec:measurement}
   565	
   566	\subsection{Indicators}
   567	
   568	The source paper rejects military expenditure as a measure of coercive power, and \cref{prop:coercive-power:arbitrary} shows why sanction counts are equally misleading. The objects that matter are the control share, the components of contestability and the two margins. \Cref{tab:indicators} lists indicators for each.
   569	
   570	\begin{table}[!htbp]
   571	\centering
   572	\small
   573	\caption{Indicators for the coercive pillar. Each indicator measures a defined object of \cref{sec:layer} or \cref{sec:mechanisms}; none has been coded for a real polity under a preregistered scheme.}
   574	\label{tab:indicators}
   575	\renewcommand{\arraystretch}{1.15}
   576	\begin{tabularx}{\textwidth}{@{}L{3.0cm}YY@{}}
   577	\toprule
   578	Object & Indicator & Main threat to validity \\
   579	\midrule
   580	Control share $s^{\pC}_i$ and concentrations $H^{\pC}$ and $H^{\pC}_{(1)}$ & Share of heads of coercive organizations whom a single actor can appoint and remove, with the share of their decisions that follow that actor's directives, coded from statutes and records & Formal authority may differ from practice, so appointment records should be checked against actual removals \\
   581	Contestability $Q^{\pC}$ & Scores for the six components of \cref{def:coercive-power:qc}, coded from law and from the reports of oversight bodies & Oversight bodies may exist on paper without access to records or power to compel testimony \\
   582	Conduct margin $\Delta^{\mathrm{c}}(y)$ & Difference in targeting rates between violators and non-violators, measured against an independent record of conduct such as victimization surveys or audits & The apparatus that sanctions also records violations, so official data cannot measure conduct independently \\
   583	Allegiance margin $\Delta^{\mathrm{a}}(v)$ & Difference in targeting rates between opponents and supporters with the same conduct under the reference rules, for example in surveillance, arrest or prosecution & Opponents and supporters may differ in unobserved conduct, which requires matched designs or outcome tests \\
   584	Repression & Standards-based scales coded from human-rights reports, as in Poe and Tate and in Hill and Jones, and V-Dem civil-liberties indicators & Reporting improves where monitoring improves, which can make better-governed states appear more repressive \\
   585	Coups and counterweights & Coup attempts from the Powell and Thyne dataset, and the number of armed organizations outside the regular military chain of command & Counterweights are often secret or nominally civilian \\
   586	Integration $C_{\pF\pC}$ & Share of coercive organizations' revenue from their own business holdings & Holdings are often opaque and require primary documents \\
   587	Dependency $\pC \to \pW$ and integration $C_{\pC\pW}$ & Legal scope of conscription and of forced and penal labor, and the share of output produced under them & Legal categories may not match practice \\
   588	\bottomrule
   589	\end{tabularx}
   590	\end{table}
   591	
   592	The allegiance margin is the hardest object to measure and the most important. Two designs are available. The first compares the treatment of opponents and supporters with matched conduct, as recorded by a source independent of the coercive apparatus: a court that acquits, a victimization survey, or an archive of the targets' own activities. The Senate inquiry of 1975 to 1976 is an example of the third kind, since it compared the surveillance record with the lawful character of the targets' activities \citep{church1976}. The second design adapts the outcome test from the economics of discrimination. Knowles, Persico and Todd showed that if officers maximize successful searches, the rate at which searches find contraband should be equal across groups in the absence of bias \citep{knowles2001}. The analogous test here compares the rate at which coercive acts against opponents and supporters are later upheld by independent review. A systematically lower rate for opponents indicates that opponents are targeted on weaker evidence, which is a positive $\Delta^{\mathrm{a}}(0)$. The test has two known weaknesses. Average rates can differ even without bias if the marginal cases differ across groups, the problem of infra-marginality, so the test is informative only under the conditions that Knowles, Persico and Todd state for equilibrium search behavior. And the independent review may itself be captured, which is the concern of Part~III; the test is only as good as the judicial contestability $Q^{\pJ}$ of the reviewing body. Repression scales \citep{poe1994,hill2014} and V-Dem indicators \citep{coppedge2011} measure the level of coercion against citizens but do not separate the two margins, so they are useful as outcomes rather than as measures of capture. Coup data \citep{powell2011} measure the guardian problem directly.
   593	
   594	\subsection{Hypotheses with falsifiers}
   595	
   596	The hypotheses below refine the source paper's generic hypotheses H1 to H6 for the coercive pillar; the parent hypothesis is given in brackets. Each states the result that would count against it.
   597	
   598	\begin{description}
   599	\item[HC1 (threat environment; H3).] Rulers who face greater elite threat build fragmented and loyalty-based coercive institutions; rulers who face mass threat build unified and intrusive ones \citep{greitens2016}. The first half is motivated by \cref{prop:coercive-power:coup-proofing}; the second half is not modeled here. Falsifier: the number and independence of armed organizations are unrelated to measured elite threat once external threat is controlled.
   600	\item[HC2 (coup-proofing trade-off; H6).] Coup-proofing lowers coup success and also lowers military effectiveness \citep{quinlivan1999,pilster2011}. Falsifier: higher counterbalancing shows no association with battlefield performance in comparable conflicts.
   601	\item[HC3 (security-force defection; H5).] The cohesion, composition and professionalism of security forces predict whether they defect or repress during mass unrest \citep{bellin2012,albrecht2016,chenoweth2011}. Falsifier: these characteristics show no association with defection across episodes.
   602	\item[HC4 (fiscal basis; H3).] Coercive organizations financed by taxation of a broad population face more contestation than those financed by resource rents or foreign transfers \citep{tilly1990,karaman2013}. The hypothesis is motivated by term (a) of \cref{prop:coercive-power:second-order}, which ties the loyalty of coercers to their provisioning, but the proposition does not model contestation. Falsifier: the source of financing is unrelated to $Q^{\pC}$.
   603	\item[HC5 (dependent corps; H2).] Corps recruited for dependence become political actors as their capacity grows, unless rulers rotate, disperse or replace them, raise the cost of an attempt, or raise pay \citep{crone1980,pipes1981}. This is the empirical counterpart of \cref{prop:coercive-power:outsider}. Falsifier: outsider corps whose holdings and offices grow remain subordinate without such countermeasures.
   604	\item[HC6 (democracy and repression; H1).] Democracy and judicial independence reduce repression \citep{poe1994,hill2014}. Falsifier: no effect once civil conflict is controlled. Rejali's evidence on torture in democracies is a boundary case that the hypothesis must accommodate \citep{rejali2007}.
   605	\item[HC7 (integration of finance and force; H2).] Business activity by coercive organizations raises $C_{\pF\pC}$ and lowers coercive contestability. Falsifier: military business holdings are unrelated to $Q^{\pC}$. Rival explanation: such holdings supply public goods or substitute for an inadequate budget.
   606	\item[HC8 (checks; H1 and H4).] Independent complaint mechanisms and judicial authorization lower the allegiance margin. Falsifier: the margin is unchanged after such reforms are introduced. As the source paper warns, reforms can raise reported abuses by making them visible, so reporting effects must be separated from changes in behavior \citep{largo2026hbs}.
   607	\item[HC9 (volume and compliance; H1).] When coercive acts against opponents rise while independently measured compliance with the reference rules falls among opponents, and neither changes among supporters with matched conduct, the allegiance margin is rising and the conduct margin among opponents is falling. The comparison with supporters is needed because a temptation shock, such as a crime wave, also raises both violations and coercive acts with no allegiance margin at all; it affects both groups. This is the pattern \cref{prop:coercive-power:arbitrary} predicts when opponents are targeted without regard to conduct. Falsifier: in documented episodes of politically selective repression, opponents' compliance with the reference rules does not fall relative to supporters'.
   608	\item[HC10 (separability; H6).] Across polities, measured conduct margins and measured allegiance margins are weakly correlated: the absolute correlation is below a preregistered threshold, for example 0.5, and polities with a conduct margin above the sample median include some with an allegiance margin indistinguishable from zero. This is the empirical content of \cref{prop:coercive-power:separability} and of the claim that A does not imply B. Falsifier: the two margins are so strongly correlated that effective rule enforcement is never observed without a positive allegiance margin, which would suggest that capture accompanies coercion structurally.
   609	\end{description}
   610	
   611	HC10 is the hypothesis whose failure would most damage this paper's argument. The separability proposition shows that the margins can vary independently, but if they never do in practice, the distinction between necessity and capture would be logical rather than empirical.
   612	
   613	\section{Revelation 13 as typological image}
   614	\label{sec:revelation}
   615	
   616	The series reads Revelation typologically. It does not identify the beast, the mark or Babylon with any present government, party, technology, person, religion or institution. Futurist readings that make such identifications have a long history of failure \citep{boyer1992,fuller1995,mcginn1998}, and historicist readings that identified the beast with particular churches belong to the history of polemic \citep{kovacs2004}. In the preterist reading, which supplies the historical anchor, the first beast is Roman imperial power and the setting is the imperial cult of the cities of Asia Minor \citep{bauckham1993,friesen2001,koester2014}. In the typological reading the series adopts, the beast is a recurring pattern of power that claims ultimate loyalty \citep{bauckham1993,wink1992}. The use of the image here is an interpretive claim of this project, not a settled exegetical result.
   617	
   618	Revelation 13 is saturated with coercion. The first beast is given authority to make war: ``it was given unto him to make war with the saints, and to overcome them: and power was given him over all kindreds, and tongues, and nations'' (Rev.~13:7, KJV). Its worshippers ask, ``Who is like unto the beast? who is able to make war with him?'' (13:4). The second beast exercises the authority of the first and causes the earth to worship it, and it brings an image to life that should ``cause that as many as would not worship the image of the beast should be killed'' (13:15). The chapter ends with the mark, without which ``no man might buy or sell'' (13:17). Kraybill has read these passages against the economic life of the province, in which participation in trade was entangled with the imperial cult \citep{kraybill1996}.
   619	
   620	The coercive content of 13:15 has a precise structure in the terms of \cref{def:coercive-power:margins}. Inside the image's own order, refusal to worship is the violation. But that rule is a rule whose content is allegiance, which is exactly the kind of rule excluded from the reference set $\mathcal{R}^0$. Measured against allegiance-neutral rules, the death sanction of 13:15 is conditioned entirely on allegiance and not at all on conduct, and the enactment of the rule is itself an image of rule-making capture. The economic exclusion of 13:16 to 17 has the same structure: the cost falls on those without the mark, whatever they have done. The text's image of the beast is, among other things, an image of a coercive apparatus whose conduct margin has been displaced by an allegiance margin.
   621	
   622	Another canonical text, Paul's letter to the Romans, describes the coercive function with the opposite conditioning. Romans 13 says that ``rulers are not a terror to good works, but to the evil,'' and that the ruler ``beareth not the sword in vain: for he is the minister of God, a revenger to execute wrath upon him that doeth evil'' (Rom.~13:3 to 4, KJV). The sword in Romans 13 is conditioned on conduct: it falls on the one who does evil. The sword in Revelation 13 is conditioned on worship: it falls on the one who will not bow. Readers have long asked how the two chapters fit together. Yoder read Romans 13 as a call to be subject to authorities whose power is itself ordered under God, not as an endorsement of whatever those authorities do \citep{yoder1972}, a reading that leaves room for Revelation's judgment on authority that demands worship. In the framework of this paper the chapters describe the same function under different parameters. Romans 13 describes a sanction regime with a positive conduct margin and no allegiance margin. \Cref{thm:coercive-power:necessity} shows that every persistent collective needs the first property; the second is what distinguishes accountable coercion from captured coercion. Revelation 13 describes a regime in which the allegiance margin has displaced the conduct margin, and \cref{prop:coercive-power:arbitrary,prop:coercive-power:capacity} show why such a regime weakens the enforcement of the ordinary rules it claims to protect. The reading is consistent with the series distinction between Proposition~A, the universal function, and Proposition~B, its contingent capture.
   623	
   624	The same chapter addresses those who suffer coercion: ``He that leadeth into captivity shall go into captivity: he that killeth with the sword must be killed with the sword. Here is the patience and the faith of the saints'' (13:10). The KJV wording follows one textual tradition. The verse echoes Jeremiah 15:2, its wording varies among manuscripts, and many modern editions and commentators read it as a call to the faithful to accept captivity and death rather than as a statement that the coercer will meet the same fate; the commentaries discuss the problem at this verse \citep{aune1998b,koester2014}. Because the reading is uncertain, this paper draws no institutional inference from it. On either reading the verse rules out armed resistance by the faithful, which places the response it commends in endurance and witness rather than in counter-coercion.
   625	
   626	Revelation 17 supplies a closer image of the guardian problem of \cref{sec:mechanisms}. The ten kings ``have one mind, and shall give their power and strength unto the beast'' (17:13), and yet ``the ten horns which thou sawest upon the beast, these shall hate the whore, and shall make her desolate and naked'' (17:16). Allies who lend their force to a power can turn it against the power they served. Read typologically, the passage is an image of the dependent-corps dynamic of \cref{prop:coercive-power:outsider}, in which those who supply coercion come to hold it on their own account. This too is the project's interpretive claim, not an exegetical result. Collins argued that the Apocalypse addressed a perceived crisis and offered its readers a form of catharsis \citep{collins1984}, and Thompson questioned whether the Domitianic period saw the systematic persecution that older readings assumed \citep{thompson1990}. On either reading the text's concern is not the existence of the sword but its direction: whom it strikes, and why.
   627	
   628	\section{Objections and scope conditions}
   629	\label{sec:objections}
   630	
   631	The first objection is that the necessity theorem is trivial, since any cost can be called a sanction. The definition blocks this. A sanction must respond to an observed or alleged violation, and the deterrence margin is the difference in continuation payoffs between compliance and violation. Both are observable. The theorem can fail, and \cref{sec:counter} states the observation that would refute it, together with the requirement that temptation be measured independently of sanction practices so that no compliant collective can be reclassified after the fact. Its content lies in Ax5 and the bridge assumption, which are empirical claims about temptations, and in the conclusion that the sanction regime must shift at least $p - \theta$ of probability mass toward compliance.
   632	
   633	The second objection is Hobbesian: order requires a sovereign with a monopoly of force, so the distributed sanctions of stateless societies are a primitive stage rather than a functional equivalent. The evidence of \cref{tab:hardcases} is against this. Distributed sanctions sustained order in many societies over long periods, and the theorem requires a positive margin, not a concentrated holder. The objection has more force at scale, and \cref{prop:coercive-power:second-order} explains why: as collectives grow, term (d) weakens and coercion must be provisioned or legitimated. That is a reason for specialization, not for concentration without accountability.
   634	
   635	The third objection comes from the opposite direction. Clastres, Graeber and Wengrow, and anarchist anthropology more generally, argue that hierarchy is not inevitable and that many societies deliberately prevented the emergence of coercive authority \citep{clastres1987,graeber2021}. The paper agrees about hierarchy and disagrees about coercion. The societies they describe sanction those who try to command; they do not lack sanctions. Their achievement is a coercive pillar with $H^{\pC}$ near $1/n$ and contestability near one, which is the clearest empirical evidence that Proposition~B is contingent.
   636	
   637	The fourth objection is Marxian: coercion in class societies serves the ruling class, so the distinction between rule enforcement and capture is ideological. The framework accommodates the claim as a hypothesis about the allegiance margin. If coercion is applied more heavily to one class for the same conduct, or if the rules themselves were written to protect one class's property, the first case shows up as a positive allegiance margin indexed by class, and the second belongs to the analysis of rule-making in Part~II. In both cases the claim becomes measurable. What the framework rejects is the inference from the existence of police to the existence of class capture, which is the inference from A to B.
   638	
   639	The fifth objection is the public-goods objection: concentrated coercion provides security, which benefits everyone, so it should not be treated with suspicion. The paper accepts the premise. The source paper's fourth proposition and hypothesis H6 state that concentration with high-quality review can coexist with competent services and low arbitrary sanctioning \citep{largo2026hbs}, and the social democracies of \cref{sec:socdem} are the leading illustration. The margins framework is designed to distinguish this case from capture rather than to presume either.
   640	
   641	Five scope conditions limit the results. The capacity trade-off of \cref{prop:coercive-power:capacity} rests on a linear capacity constraint, which is an assumption about the technology of enforcement rather than a derived result. The model treats a single rule with a binary violation decision, while real polities enforce many rules of different gravity, and the tolerance $\theta$ differs among them. Equilibria in repeated games are typically multiple, so the theorem establishes that some sanction regime is necessary without predicting which one arises. The analysis concerns enforcement inside a polity; war between polities enters only through the guardian problem and the fiscal basis of coercion. And the conduct margin can be measured only with an independent record of conduct, which is often unavailable precisely where capture is most likely.
   642	
   643	\section{Conclusion}
   644	\label{sec:conclusion}
   645	
   646	Every governance system settles who enforces its rules, because when members are sometimes tempted to break rules, compliance requires that violators' prospects fall because of what they did. The answer need not be a police force. Gossip, ridicule, ostracism and coalition action satisfy the deterrence lemma as well as armies do, and the societies that seem to lack coercion are those in which the collective holds it and directs it against concentration. The function is universal; its institutional form varies.
   647	
   648	Capture in the coercive pillar requires a change in what coercion responds to. The conduct margin measures enforcement of rules, the allegiance margin measures enforcement of loyalty, and the two are separable: necessity constrains the first and is silent about the second. They trade off when coercive capacity is limited, and when opponents are targeted without regard to their conduct; under those conditions the volume of coercion rises while compliance with ordinary rules falls. That is why spending and arrest counts mismeasure coercive power, and why the contrast between Romans 13 and Revelation 13 concerns the direction of the sword rather than its existence.
   649	
   650	The comparison of six regime types shows the same function distributed in different ways: through private producers and civilian control in market-capitalist societies, party organs in communist states, ombudsmen, parliamentary oversight and conscription in social democracies, counterbalanced and dependent corps in Islamic states, venal and contracted command in Catholic monarchies, and constitutional oversight in secular democracies. What remains uncertain is the size of the two margins in any of them. Measuring the allegiance margin, against an independent record of conduct, is the task on which the empirical claims of this paper depend.
   651	
   652	\begin{thebibliography}{200}
   653	\small
   654	\setlength{\itemsep}{2pt}
   655	
   656	\bibitem[\'Agoston(2005)]{agoston2005}
   657	\'Agoston, G\'abor (2005). \emph{Guns for the Sultan: Military Power and the Weapons Industry in the Ottoman Empire}. Cambridge University Press.
   658	
   659	\bibitem[\'Agoston(2014)]{agoston2014}
   660	\'Agoston, G\'abor (2014). Firearms and Military Adaptation: The Ottomans and the European Military Revolution, 1450-1800. \emph{Journal of World History} 25(1):85-124. doi:10.1353/jwh.2014.0005.
   661	
   662	\bibitem[Al-Rasheed(2002)]{alrasheed2002}
   663	Al-Rasheed, Madawi (2002). \emph{A History of Saudi Arabia}. Cambridge University Press. doi:10.1017/cbo9780511993510.
   664	
   665	\bibitem[Albrecht and Ohl(2016)]{albrecht2016}
   666	Albrecht, Holger and Ohl, Dorothy (2016). Exit, Resistance, Loyalty: Military Behavior during Unrest in Authoritarian Regimes. \emph{Perspectives on Politics} 14(1):38-52. doi:10.1017/S1537592715003217.
   667	
   668	\bibitem[Alfoneh(2013)]{alfoneh2013}
   669	Alfoneh, Ali (2013). \emph{Iran Unveiled: How the Revolutionary Guards Is Transforming Iran from Theocracy into Military Dictatorship}. AEI Press.
   670	
   671	\bibitem[Alvarez(2011)]{alvarez2011}
   672	Alvarez, David (2011). \emph{The Pope's Soldiers: A Military History of the Modern Vatican}. University Press of Kansas.
   673	
   674	\bibitem[Applebaum(2003)]{applebaum2003}
   675	Applebaum, Anne (2003). \emph{Gulag: A History}. Doubleday.
   676	
   677	\bibitem[Arjomand(1988)]{arjomand1988}
   678	Arjomand, Said Amir (1988). \emph{The Turban for the Crown: The Islamic Revolution in Iran}. Oxford University Press.
   679	
   680	\bibitem[Aune(1998)]{aune1998b}
   681	Aune, David E. (1998). \emph{Revelation 6-16}. Word Biblical Commentary 52B. Thomas Nelson.
   682	
   683	\bibitem[Axelrod(1984)]{axelrod1984}
   684	Axelrod, Robert (1984). \emph{The Evolution of Cooperation}. Basic Books.
   685	
   686	\bibitem[Bauckham(1993)]{bauckham1993}
   687	Bauckham, Richard (1993). \emph{The Theology of the Book of Revelation}. Cambridge University Press. doi:10.1017/cbo9780511819858.
   688	
   689	\bibitem[Becker(1968)]{becker1968}
   690	Becker, Gary S. (1968). Crime and Punishment: An Economic Approach. \emph{Journal of Political Economy} 76(2):169-217. doi:10.1086/259394.
   691	
   692	\bibitem[Bellin(2004)]{bellin2004}
   693	Bellin, Eva (2004). The Robustness of Authoritarianism in the Middle East: Exceptionalism in Comparative Perspective. \emph{Comparative Politics} 36(2):139-157. doi:10.2307/4150140.
   694	
   695	\bibitem[Bellin(2012)]{bellin2012}
   696	Bellin, Eva (2012). Reconsidering the Robustness of Authoritarianism in the Middle East: Lessons from the Arab Spring. \emph{Comparative Politics} 44(2):127-149. doi:10.5129/001041512798838021.
   697	
   698	\bibitem[Boehm(1999)]{boehm1999}
   699	Boehm, Christopher (1999). \emph{Hierarchy in the Forest: The Evolution of Egalitarian Behavior}. Harvard University Press. doi:10.2307/j.ctvjf9xr4.
   700	
   701	\bibitem[Boehm(2012)]{boehm2012}
   702	Boehm, Christopher (2012). \emph{Moral Origins: The Evolution of Virtue, Altruism, and Shame}. Basic Books.
   703	
   704	\bibitem[Born and Caparini(2007)]{born2007}
   705	Born, Hans and Caparini, Marina (eds.) (2007). \emph{Democratic Control of Intelligence Services: Containing Rogue Elephants}. Ashgate.
   706	
   707	\bibitem[Boyer(1992)]{boyer1992}
   708	Boyer, Paul (1992). \emph{When Time Shall Be No More: Prophecy Belief in Modern American Culture}. Harvard University Press (Belknap). doi:10.2307/jj.41480279.
   709	
   710	\bibitem[Bruce(2010)]{bruce2010}
   711	Bruce, Gary (2010). \emph{The Firm: The Inside Story of the Stasi}. Oxford University Press.
   712	
   713	\bibitem[Buchta(2000)]{buchta2000}
   714	Buchta, Wilfried (2000). \emph{Who Rules Iran? The Structure of Power in the Islamic Republic}. Washington Institute for Near East Policy and Konrad Adenauer Stiftung.
   715	
   716	\bibitem[Chenoweth and Stephan(2011)]{chenoweth2011}
   717	Chenoweth, Erica and Stephan, Maria J. (2011). \emph{Why Civil Resistance Works: The Strategic Logic of Nonviolent Conflict}. Columbia University Press.
   718	
   719	\bibitem[Clastres(1987)]{clastres1987}
   720	Clastres, Pierre (1987). \emph{Society against the State: Essays in Political Anthropology}. Translated by Robert Hurley. Zone Books. doi:10.2307/j.ctv1595m3p.
   721	
   722	\bibitem[Collins(1984)]{collins1984}
   723	Collins, Adela Yarbro (1984). \emph{Crisis and Catharsis: The Power of the Apocalypse}. Westminster Press.
   724	
   725	\bibitem[Colton(1979)]{colton1979}
   726	Colton, Timothy J. (1979). \emph{Commissars, Commanders, and Civilian Authority: The Structure of Soviet Military Politics}. Harvard University Press. doi:10.4159/harvard.9780674497443.
   727	
   728	\bibitem[Conquest(1990)]{conquest1990}
   729	Conquest, Robert (1990). \emph{The Great Terror: A Reassessment}. Oxford University Press.

exec
/usr/local/bin/zsh -lc "sed -n '330,529p' papers/latex/coercive-power.tex | nl -ba -v330" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   330	\subsection{Policing, punishment and legitimacy}
   331	
   332	Within consolidated states, the main question about ordinary enforcement is why people comply. Tyler found that people obey the law more because they judge the authorities legitimate and the procedures fair than because they fear sanctions \citep{tyler1990}, and Jackson and colleagues found the same pattern in survey data on policing \citep{jackson2012}. These findings do not contradict \cref{thm:coercive-power:necessity}. They show that legitimation lowers the temptation distribution and supplies the motive for cooperation with enforcement, which in the present model shifts $G$ and strengthens term (b). Foucault traced the shift from spectacular punishment to the disciplinary prison and the surveillance it made possible \citep{foucault1977}. Pratt documented the comparatively low imprisonment rates and humane prison conditions of the Nordic countries and traced them to egalitarian welfare states, while warning that populist pressures could erode them \citep{pratt2008a,pratt2008b}.
   333	
   334	\subsection{Contribution}
   335	
   336	The literatures above mostly study either the necessity of order (from Hobbes to the economics of deterrence) or the dangers of coercive power (from civil-military relations to repression), and they rarely connect the two formally. The deterrence literature from \citet{becker1968} onward models the conduct margin and assumes enforcement is impartial. The repression literature studies the allegiance margin and largely takes the conduct margin for granted. This Part treats both as properties of a single sanction-probability function, which shows that the necessity of coercion and its capture are logically separate and empirically distinguishable. It also places the evidence of six regime types on a common scale, so that the comparison asks how each type distributes a function that all of them share.
   337	
   338	\section{Comparative analysis across six regime types}
   339	\label{sec:comparative}
   340	
   341	Each regime type below is asked the same five questions: which institutions hold the coercive function, how concentrated and contestable it is, how it depends on and is integrated with the other five pillars, what preserves accountability, and which capture episodes and checks are documented. Every claimed capture episode is held to the same standard, the three-part capture link of the source paper as applied to coercion in \cref{sec:mechanisms}, and each subsection reports at least one documented episode or standing risk and one documented check. The types are ideal types rather than mutually exclusive classes. The United States, for instance, is both a market-capitalist society and a secular democracy; each illustration is assigned to the type whose defining feature it shows. No numerical value of $U_t$ or $\Integ_t$ is reported for any real polity, because none has been coded under a preregistered scheme. Statements about concentration and integration are qualitative orderings that a coding exercise could confirm or overturn.
   342	
   343	\subsection{Market-capitalist societies}
   344	\label{sec:market}
   345	
   346	In market-capitalist societies the coercive function is held by public police forces, militaries and intelligence agencies under elected civilian authority, together with a private sector that manufactures weapons, supplies services and provides security for property. The defining feature for this pillar is the participation of private capital in producing coercive capacity and its interest in how that capacity is used.
   347	
   348	The link between private enterprise and coercion is older than industrial capitalism. Parrott showed that the armies of early modern Europe were raised and supplied to a large extent by military entrepreneurs who treated war as a business, and that this system was more effective than older accounts of state-led military modernization allowed \citep{parrott2012}. The modern form is the defense industry. In his farewell address of January 1961, President Eisenhower warned the American public against the acquisition of unwarranted influence by what he called the military-industrial complex \citep{eisenhower1961}. In the vocabulary of this series, the warning describes a possible capture link in which producers of coercive capacity gain privileged access to the decisions that set budgets, procurement and deployment, raising $C_{\pF\pC}$.
   349	
   350	Concentration differs sharply between the military and the police. Command of the armed forces is concentrated in a national executive, so the military contributes a large share to $H^{\pC}$, while legislative control of budgets divides authority over provisioning. Policing in the United States is dispersed across federal, state and local agencies, each answering to a different elected authority, which lowers $H^{\pC}$ for ordinary enforcement. The theory of civilian control was developed largely on the American case: Huntington's objective control, Janowitz's constabulary force and Feaver's agency model all address how elected civilians can command a professional military that they cannot fully monitor \citep{huntington1957,janowitz1960,feaver2003}. Accountability rests on component (1) of $Q^{\pC}$, appointment and removal by elected civilians; on components (2) and (4), judicial authorization of searches and the civil and criminal liability of agents; and on component (6), legislative scrutiny of budgets. Kohn argued that these provisions secure control only when civilians actually exercise them \citep{kohn1997}.
   351	
   352	The capture hypothesis specific to this regime type is that concentrated private interests shape the use of coercion. It meets the source paper's standard for a capture link only if three things are shown: privileged access by a private party, a weakening of the accountability that would otherwise apply, and material evidence that the access changed an enforcement outcome \citep{largo2026hbs}. Eisenhower's warning is evidence that a senior insider regarded the risk as serious; it is not evidence that capture occurred in any particular decision. A better documented episode comes from industrial conflict. The federal Commission on Industrial Relations reported in 1915 that ``practically every industrial State has at some relatively recent time permitted its institutions to be used by one party or the other to an industrial dispute (almost without exception the employers)''. It found that sheriffs in many counties deputized guards ``in the employment and pay of corporations'' and that militia were at times recruited from corporate guards and employees \citep[pp.~147 to 148]{cir1915}. Each element of the capture link is present in that finding: privileged access through deputization, the displacement of publicly accountable police by employer-paid agents, and enforcement outcomes against strikers. In the notation of \cref{def:coercive-power:margins}, the allegiance margin was indexed by the side a person took in an industrial dispute. The report was itself the check. A public commission with investigative powers documented the practice and recommended rules for the conduct of the militia \citep{cir1915}.
   353	
   354	For the present, following the source's proposal for narrow projects, the test of the military-industrial hypothesis is a preregistered sample of procurement decisions, not a selection of scandals. The rival explanation is that defense spending responds to external threats and that contractors compete for contracts under rules they do not control. Tilly's protection-racket analogy suggests a related hypothesis about ordinary policing: if public coercion protects some forms of property more than others, it transfers value to their owners \citep{tilly1985}. This predicts a positive allegiance margin indexed by economic position, which is an empirical question about arrest and prosecution rates conditional on conduct.
   355	
   356	\subsection{Communist party-states}
   357	\label{sec:communist}
   358	
   359	In communist party-states the ruling party holds the coercive function through security organs that answer to its leadership, through political officers embedded in the armed forces, and through the police and militia. In the Soviet case the line of security organs ran from the Cheka, founded as Lenin's political police \citep{leggett1981}, through its successors to the KGB, whose own successors after 1991 Knight traced \citep{knight1996}. In the German Democratic Republic the Ministry for State Security built an apparatus of full-time officers and unofficial informants that reached into local society \citep{gieseke2014,bruce2010,koehler1999}. In the People's Republic of China the party maintains command of the People's Liberation Army \citep{shambaugh2002}, and the police carry heavy burdens of stability maintenance that Scoggins and O'Brien describe from the officers' own perspective \citep{scoggins2016}.
   360	
   361	Concentration is high at the apex: the party leadership appoints and removes the heads of every coercive organization through the appointment channel analyzed in Part~II, so $H^{\pC}$ is high and the integration $C_{\pP\pC}$ is close to its maximum. Below the apex, however, the apparatus is divided, so $H^{\pC}_{(1)}$ is lower. Army, security service and police are separate organizations with separate chains of command, and party organs inside the army provide a further check. Colton's study of Soviet military politics found that the relationship between commissars and commanders was less a struggle between party and army than a structured form of military participation in politics, with the military's role largely confined to its own institutional concerns \citep{colton1979}. The division of the coercive apparatus is a form of counterbalancing, and the comparative static of \cref{prop:coercive-power:coup-proofing} applies to it.
   362	
   363	Integration with the ideological pillar is direct, since the same party commands both: political officers and party organizations inside the coercive organs make doctrinal loyalty part of the job, so $C_{\pI\pC}$ is high. Integration with production is also high. The Soviet camp system used forced labor on a large scale under the direction of the same party-state that set production plans \citep{applebaum2003,gregory2003}, so the dependency $\pC \to \pW$ and the integration $C_{\pC\pW}$ were both at the center of the Soviet economy for several decades. \Cref{sec:cw} returns to it. Contestability from outside the party is low: there is no independent judiciary able to review security operations, no competitive legislature able to audit them, and no free press able to expose them. The internal checks are party discipline and periodic purges. Purges can be used against security chiefs, but they are themselves exercises of the coercive function, so they check particular holders of power without raising $Q^{\pC}$.
   364	
   365	The terror of the late 1930s is the episode with the largest consequences, and it shows why arbitrariness and allegiance must be distinguished. The security organs were turned against party members, officers and ordinary citizens \citep{conquest1990}. Coercion fell on people who had broken no rule in any allegiance-neutral reference set, so the conduct margin collapsed across alignments, which is the arbitrariness of \cref{prop:coercive-power:arbitrary}. Whether the episode was also capture in the source's sense turns on the material-evidence step: how far the targeting was directed from the center against categories defined by political suspicion. That is exactly the question on which Conquest and revisionist historians disagree. Getty argued that the purges grew in part out of conflicts and confusion within the party apparatus rather than from a single central plan \citep{getty1985}. On Conquest's reading the episode meets all three conditions of a capture link; on Getty's it is closer to arbitrariness produced by an apparatus that the center did not fully control. Either way it is a failure of the coercive pillar, and the numbers on either side should be cited with that debate in view. The documented checks are of two kinds. Party supremacy over the military meant that the Soviet army did not seize power \citep{colton1979}. And the deterrent power of the apparatus rested on beliefs: when those beliefs shifted in 1989, regimes that had seemed secure fell with little warning \citep{kuran1991}.
   366	
   367	Reform socialism, which introduced markets inside party-states, did not change who held coercion. Kornai's account of the socialist system treats the reforms as changes in coordination mechanisms under continued party rule \citep{kornai1992}. For this reason the coercive pillar of market socialism as practiced is analyzed here rather than in the next subsection.
   368	
   369	\subsection{Social democracy and democratic socialism}
   370	\label{sec:socdem}
   371	
   372	In the social democracies of Northern Europe the coercive function is held by national police and armed forces under parliamentary control, with independent oversight bodies and a long tradition of citizen armies. The distinctive feature of this regime type for the coercive pillar is the combination of a centralized apparatus with high contestability and low reliance on punishment.
   373	
   374	Sweden illustrates the oversight structure. Its Parliamentary Ombudsman was established with the Instrument of Government of 1809 to supervise how judges and civil servants apply the law, and its supervision was later extended to local government \citep{jo2026}. Ombudsman supervision of public authorities contributes to components (3) and (4) of $Q^{\pC}$: complaints can reach an independent office with access to records, and officials can be held to account for unlawful conduct. Civilian control of the armed forces has varied with the perceived external threat. Hedlund's study of Swedish civil-military relations from 1984 to 2011 found that civilian control over the officer rank system and over professional officer education changed as perceptions of threat changed \citep{hedlund2011}.
   375	
   376	The Nordic countries are best known in this domain for penal moderation. Pratt described comparatively low imprisonment rates and humane prison conditions, rooted in egalitarian welfare states with high social trust, and warned that the pattern was under pressure from more punitive politics \citep{pratt2008a,pratt2008b}. Penal moderation is not the absence of the coercive function. \Cref{thm:coercive-power:necessity} requires a positive deterrence margin, not a large sanction magnitude, and \cref{cor:coercive-power:magnitude} shows that a high detection probability or a temptation distribution shifted toward compliance permits smaller sanctions. Legitimacy research suggests the second mechanism. Where people regard the police and courts as fair, they comply for reasons other than fear of punishment \citep{tyler1990,jackson2012}, which lowers the temptation distribution and strengthens the motive to cooperate with enforcement.
   377	
   378	The Nordic security services also supply documented episodes of the allegiance margin, and documented checks on it. In Norway the parliament appointed a commission to examine allegations of illegal surveillance. Its report of 1996, known by the name of its chair, found that the police security service had carried out widespread illegal political surveillance, particularly in the 1960s and 1970s, of individuals and organizations on the political left \citep{eos2026}. The response was a parliamentary oversight committee for all the secret services, established under a separate law of 1995 and elected for the first time in 1996 \citep{eos2026}. In Sweden the government appointed a commission in 1999 to examine the security services' surveillance of domestic political groups since 1945. Its directive records that the security police were barred in 1969 from registering a person solely on account of political views, that a general constitutional ban on such registration followed in 1977, and that military intelligence had registered communists from 1955 \citep{dir1999}. The commission reported in 2002 \citep{sou2002}. These episodes meet the capture-link test in the form the source requires: discretion over surveillance, use of it against political opponents who had broken no rule, and documentary evidence assembled by official inquiries. They also show the check working, though decades late: legislatures with investigative powers exposed the practices and created standing oversight.
   379	
   380	Dependencies and integration take an unusual form in this regime type. Conscript armies draw on the labor time of the whole population, so the dependency $\pW \to \pC$ runs through a universal obligation rather than through a professional caste, and it involves no integration of command over coercion and production. Appointment runs through parliament rather than through a party, and provisioning runs through the general budget of a high-tax state. Concentration $H^{\pC}$ is moderate to high because national police and military command are centralized, but contestability $Q^{\pC}$ is high on most components, so the contribution of the coercive pillar to $U_t$ in \eqref{eq:U} is small. This is the case that the source paper's Proposition~4 anticipates: concentration combined with high-quality review can coexist with competent services and low arbitrary sanctioning \citep{largo2026hbs}.
   381	
   382	Democratic socialism as a program, as distinct from the social-democratic welfare states that partly realized it, has no separate record of coercive institutions in the sources reviewed. Its claims about coercion are claims about how the institutions of the previous paragraphs should be governed, and they are evaluated by the same measures.
   383	
   384	\subsection{Islamic states}
   385	\label{sec:islamic}
   386	
   387	Islamic states are polities in which political legitimacy has been derived in significant part from religious law, and they differ widely: Sunni and Shi'i, dynastic and revolutionary, imperial and national. The coercive function has been held by caliphal armies paid through state registers, by corps of slave soldiers, by tribal levies, by dynastic guards and by revolutionary ideological forces. The common thread is not a single institution but a recurring problem: how a ruler whose legitimacy rests on religious law commands armed men whose loyalty may run to tribe, faction or their own corps.
   388	
   389	In the early caliphates soldiers were paid from the revenues of conquest through state registers, which made coercion directly dependent on the fiscal system \citep{kennedy2001}. From the ninth century, rulers came to rely on soldiers of slave origin, recruited from outside the societies they governed. Crone argued that military slavery offered rulers a source of armed force independent of the tribal and local elites whose loyalty they could not trust \citep{crone1980}, and Pipes traced the genesis of the system \citep{pipes1981}. The term slave soldier is the scholars' term for a legal status of military servitude that could lead to command, wealth and rule. It differs from chattel slavery in the household or the field, and this paper uses it only in that technical sense. The Mamluk sultanate that ruled Egypt and Syria from 1250 was governed by such soldiers and their successors \citep{irwin1986}.
   390	
   391	The Ottoman Empire built the most elaborate version. Its kul system recruited the sultan's servants, including the Janissary infantry, as personal dependents of the ruler, and Kunt traced how the households of these servants transformed provincial government between 1550 and 1650 \citep{kunt1983}. Agoston showed that the Ottoman state sustained a large military and a domestic weapons industry over centuries, adapting to European military change more successfully than older accounts of decline allowed \citep{agoston2005,agoston2014}. Tezcan dates a transformation of the Ottoman polity toward a more limited monarchy to the period from about 1580 to 1826 and treats the deposition and killing of Sultan Osman II in 1622, in which the sultan's own soldiers took part, as its turning point \citep{tezcan2010}. The pattern, a dependent corps recruited for loyalty that later acquires interests and power of its own, is the subject of \cref{prop:coercive-power:outsider}.
   392	
   393	In the Islamic Republic of Iran the coercive function is divided between the regular army and the Islamic Revolutionary Guard Corps, created after the revolution as an ideological guardian of the new order \citep{katzman1993,arjomand1988}. Buchta mapped the parallel institutions through which the Leader, the Guardian Council and the Guard share power \citep{buchta2000}. Wehrey and colleagues documented the Guard's expanding domestic political, economic and security roles \citep{wehrey2009}. Alfoneh argued that the Guard was transforming the state from theocracy into military dictatorship \citep{alfoneh2013}; his account comes from an advocacy institute and is best read alongside the more cautious RAND assessment. Either way, one organization commanding both coercive forces and large economic holdings raises the integration $C_{\pF\pC}$, and its ideological mandate under the same leadership raises $C_{\pI\pC}$.
   394	
   395	Saudi Arabia shows a dynastic version of counterbalancing. The kingdom maintains a regular army and a separate National Guard, a duality that Cordesman described and that Quinlivan treated as an instance of coup-proofing \citep{cordesman2003,quinlivan1999}. Gause placed it within the dynastic security structures of the Gulf monarchies \citep{gause1994}. The alliance between the Al Saud and the Wahhabi religious establishment supplies the legitimating side \citep{alrasheed2002}. The storming of the Grand Mosque in Mecca in November 1979 by Juhayman al-'Utaybi and his followers, whose origins and legacy Hegghammer and Lacroix reconstruct from fieldwork, challenged both arrangements at once: it contested the rulers' religious legitimacy and their coercive control of the holy places \citep{hegghammer2007}.
   396	
   397	Accountability in these polities has rested on different mechanisms from those of constitutional democracies. Where scholars of religious law held moral authority independent of the ruler, coercion depended on legitimation ($\pI \to \pC$) supplied by a group the ruler did not command, which is evidence of low rather than high $C_{\pI\pC}$ and a potential constraint on the ruler. Its strength varied across these polities and has not been measured on a common scale. Counterbalancing among forces is an internal check that protects rulers more than subjects. The capture-link test can be applied to the dependent-corps episodes. In the Mamluk case the corps used its control of deployment to take rule itself, and the change of rulers is documented \citep{irwin1986}. In the Ottoman case of 1622 the sultan's soldiers used their arms against the sultan, and Tezcan documents the lasting change in the distribution of power that followed \citep{tezcan2010}. Both are capture of the ruler by the coercive corps rather than capture of the coercive pillar by an outside coalition, which is the form \cref{prop:coercive-power:outsider} predicts. The documented checks are counterbalancing among separate forces and long periods in which the Ottoman state sustained and supplied its military establishment from the center \citep{agoston2005}.
   398	
   399	\subsection{Catholic monarchies}
   400	\label{sec:catholic}
   401	
   402	In the Catholic monarchies of early modern Europe royal authority was intertwined with the Church, and the coercive function was held by royal armies officered by nobles and by purchasers of commissions, by mercenary and contracted companies, by Swiss and other foreign troops, by the papal forces of the Papal States, and in Spain by the lay familiars who assisted the Inquisition. Internal diversity was considerable: Habsburg Spain, Bourbon France and the Papal States differed in fiscal structure, in their relations with Rome, and in the strength of their representative assemblies.
   403	
   404	Habsburg Spain fought across Europe with an army that depended on long supply lines and on credit. Parker's study of the Army of Flanders and the Spanish Road between 1567 and 1659 showed how logistics, finance and pay shaped military operations, and how unpaid troops mutinied \citep{parker1972}. Thompson examined how the Spanish crown governed war between 1560 and 1620, including its reliance on contractors and the sale of offices \citep{thompson1976}, and Elliott's survey places these developments in the history of the monarchy \citep{elliott1963}. Mutiny is a sanction by soldiers against their paymaster. It is also direct evidence for term (a) of \cref{prop:coercive-power:second-order}: when provisioning failed, so did the willingness of the coercers to coerce on the crown's behalf.
   405	
   406	Bourbon France built one of the largest armies in Europe. Lynn traced its growth between 1610 and 1715 \citep{lynn1997}. Rowlands showed that under Louis XIV royal service and private interest were intertwined: officers invested their own resources in their units, and the crown relied on that investment while trying to control it \citep{rowlands2002}. Venal commissions integrate finance and force at the level of the individual officer, who is both a creditor of the state and an agent of its force. Parker's thesis of a military revolution, in which new fortifications and tactics drove the growth of armies and states, frames these developments \citep{parker1988}, and Tilly's account of coercion and capital explains why monarchies with access to commercial credit could field such armies \citep{tilly1990}.
   407	
   408	The Papal States combined spiritual and temporal sovereignty. Their military forces, including the Swiss Guard, are documented from 1796 onward in Alvarez's history, which drew on the Guard's archive \citep{alvarez2011}; the verified sources reviewed for this paper do not cover the papal forces of earlier centuries. The Church also wielded sanctions of its own, including excommunication and interdict, which are ideological sanctions in the sense of \cref{def:coercive-power:sanction}: they impose relational and reputational costs and rely on belief for their force. In Spain the Inquisition drew on lay familiars who assisted its officials; Kamen's revisionist history of the Inquisition argues that its scale and severity were smaller than the older black legend held \citep{kamen1997}.
   409	
   410	Contestability came from three sources. Representative assemblies, where they retained the power to grant taxes, could limit the provisioning of armies. Contracted soldiers could refuse service when unpaid. And the Church could withhold legitimation, although in practice the crowns of Spain and France exercised considerable control over the churches within their kingdoms. Concentration of command rose over the period as monarchs replaced contracted forces with standing armies, while venality kept part of the control over units in private hands. Ertman's comparative account of state building shows how the timing of military competition shaped whether such states became patrimonial or bureaucratic \citep{ertman1997}. The capture-link test is harder to apply here than in the modern cases, because the documented material concerns the structure of command rather than its use against particular groups. What is documented is a standing risk: venal and contracted command made units partly private property, which gave their owners discretion over a public function. The documented check is the mutiny, in which soldiers withdrew coercion from a crown that failed to pay \citep{parker1972}, together with the fiscal power of estates where it survived and the limits that dependence on credit imposed on royal war-making.
   411	
   412	\subsection{Secular democracies}
   413	\label{sec:secular}
   414	
   415	In secular democracies authority is distributed among elected officials, courts and private institutions, and the legitimacy of coercion rests on constitutional law rather than on religious or party doctrine. The coercive function is held by professional armed forces under civilian command, police forces whose intrusive measures require judicial authorization, and intelligence services subject to legislative oversight. The defining feature for this pillar is the attempt to raise every component of $Q^{\pC}$ by constitutional design.
   416	
   417	The core mechanisms are civilian control of the military, judicial warrants for intrusive policing, and legislative oversight of intelligence. Kohn's account of how democracies control the military stresses that control is a practice of appointment, budget, doctrine and promotion that civilians must actively exercise \citep{kohn1997}. Born and Caparini compared the models by which democracies try to subject intelligence services to democratic control \citep{born2007}. These mechanisms map onto components (1), (2) and (6) of \cref{def:coercive-power:qc}, and their effectiveness depends on the judicial independence analyzed in Part~III. Janowitz's argument that a professional military should remain integrated with civilian society, rather than isolated from it, describes a further safeguard: a force that shares the values of those it might be ordered against is less likely to obey an order to target them \citep{janowitz1960}.
   418	
   419	The best documented capture episode in this regime type, and the best documented check, come from the same inquiry. In 1975 the United States Senate established a select committee, chaired by Frank Church, to study the government's intelligence operations. Its final report of April 1976 concluded that ``the Government has often undertaken the secret surveillance of citizens on the basis of their political beliefs, even when those beliefs posed no threat of violence or illegal acts on behalf of a hostile foreign power'' \citep[Book II, Part I, Section C]{church1976}. The committee examined the surveillance record against the lawful character of the targets' activities, which supplies the material evidence the capture-link test requires. In the notation of \cref{def:coercive-power:margins}, the finding describes a positive allegiance margin among non-violators: $\psi(0,\mathrm{op}) > \psi(0,\mathrm{al})$. The same report documents the check. A legislature with investigative powers exposed the practice, and a permanent Senate intelligence committee followed.
   420	
   421	Rejali's study of torture in democracies is the hard boundary case. Democracies that were monitored by a free press and human-rights organizations developed interrogation techniques that left few visible marks, so that public monitoring changed the form of abuse rather than ending it \citep{rejali2007}. Cross-national evidence nonetheless shows that democracy is associated with less repression of personal integrity rights \citep{poe1994}, although Hill and Jones caution that the relationship is stronger for some forms of repression than for others \citep{hill2014}. Coups are rare in consolidated democracies, and the dataset of Powell and Thyne permits this claim to be tested rather than assumed \citep{powell2011}.
   422	
   423	Concentration in secular democracies varies with constitutional structure. Unitary states with national police forces have higher $H^{\pC}$ than federal states with local forces, but both may have high $Q^{\pC}$. Integration with the political pillar is limited because civilian appointment is shared among elected bodies and constrained by professional norms of neutrality. The dependency on the judicial pillar runs through warrants and liability, and the dependency on legitimation runs through public acceptance of the constitution and of the police, which Tyler's research measures directly \citep{tyler1990}. The main risk specific to this type is that oversight bodies depend on information that the overseen agencies control, which is the principal-agent problem of Feaver's model applied to intelligence \citep{feaver2003}. The episodes of this subsection and of \cref{sec:socdem} show that risk realized for decades before legislatures intervened.
   424	
   425	\subsection{Summary across regimes}
   426	
   427	\Cref{tab:regimes} summarizes the comparison. Every regime type has the coercive function, as Proposition~A requires. They differ in who holds it, how concentrated and contestable it is, and how it depends on and is integrated with the other pillars.
   428	
   429	\begin{table}[!htbp]
   430	\centering
   431	\small
   432	\caption{The coercive function across six regime types. Orderings of concentration and contestability are qualitative and await preregistered coding.}
   433	\label{tab:regimes}
   434	\renewcommand{\arraystretch}{1.15}
   435	\begin{tabularx}{\textwidth}{@{}L{2.2cm}YYY@{}}
   436	\toprule
   437	Regime type & Principal holders of the function & Concentration, contestability and strongest integration & Documented capture episode or risk, and check \\
   438	\midrule
   439	Market-capitalist & Public police and militaries under elected civilians, with private producers of weapons and security services & Command of the military is concentrated, policing is dispersed, and the distinctive integration is between finance and coercion & Employer-paid deputies and militia in industrial disputes were documented in 1915, and a federal commission exposed the practice \\
   440	Communist party-state & Party-controlled security organs, armies with political officers, and police & Command is concentrated at the party apex with internal division among organs, contestability from outside the party is low, and the strongest integration is with political appointment & The terror of the late 1930s was arbitrary and possibly also capture, and party supremacy prevented military takeover \\
   441	Social democracy & National police and conscript or professional armies under parliamentary control & Concentration is moderate to high, contestability is high through ombudsmen and courts, and conscription makes coercion depend on universal service & Political surveillance by the security services was exposed by official inquiries, which led to standing parliamentary oversight \\
   442	Islamic states & Caliphal armies, slave-soldier corps, dynastic guards and revolutionary guards & Rulers counterbalance separate forces, and integration with legitimation and, in Iran, with finance is strong & Mamluk rule and the regicide of 1622 show corps becoming principals, and counterbalancing protected rulers more than subjects \\
   443	Catholic monarchies & Royal armies with venal officers, contracted companies, papal forces and Inquisition familiars & Concentration rose as standing armies replaced contractors, and finance and force were fused in venal command & The risk was units held partly as private property, and the checks were mutiny and the fiscal power of estates \\
   444	Secular democracy & Professional forces under civilian command, warrant-bound police and overseen intelligence services & Concentration varies with constitutional structure, and contestability is designed to be high on every component & Surveillance of citizens exposed by the Senate inquiry of 1975 to 1976 is both a capture episode and a check \\
   445	\bottomrule
   446	\end{tabularx}
   447	\end{table}
   448	
   449	\section{Mechanisms, failure modes and checks}
   450	\label{sec:mechanisms}
   451	
   452	\Cref{thm:coercive-power:necessity} requires that violators be sanctioned more than compliers. It says nothing about whom else the apparatus targets. This section shows that the coercive function and its capture are governed by different parameters, states when they nonetheless trade off, derives the main failure modes, and identifies the checks that interrupt them.
   453	
   454	\subsection{Conduct and allegiance}
   455	
   456	Return to the targeting probabilities $\psi(v,y)$ of \cref{def:coercive-power:margins}. In the one-period version of the deterrence lemma, an agent with alignment $y$ faces the margin $d = \Delta^{\mathrm{c}}(y)\mu$, so it violates a rule in $\mathcal{R}^0$ if $\tau > \Delta^{\mathrm{c}}(y)\mu$.
   457	
   458	\begin{proposition}[Separability]
   459	\label{prop:coercive-power:separability}
   460	Fix a magnitude $\mu > 0$ and a temptation distribution $G$. (i) The violation rate of agents with alignment $y$ is $1 - G(\Delta^{\mathrm{c}}(y)\mu)$, which depends on $\psi$ only through the conduct margin $\Delta^{\mathrm{c}}(y)$. (ii) For any common conduct margin $e \in (0,1)$ and any allegiance margin $x \in [0, 1-e]$, there is a targeting function with $\Delta^{\mathrm{c}}(\mathrm{al}) = \Delta^{\mathrm{c}}(\mathrm{op}) = e$ and $\Delta^{\mathrm{a}}(0) = \Delta^{\mathrm{a}}(1) = x$. In particular, the same deterrence of rule violations is compatible with a zero allegiance margin and with a positive one.
   461	\end{proposition}
   462	
   463	\begin{proof}
   464	Part (i) follows from \cref{lem:coercive-power:deterrence} with $d = \Delta^{\mathrm{c}}(y)\mu$, resolving ties toward compliance. For (ii), set $\psi(0,\mathrm{al}) = 0$, $\psi(1,\mathrm{al}) = e$, $\psi(0,\mathrm{op}) = x$ and $\psi(1,\mathrm{op}) = e + x$. All four values lie in $[0,1]$ because $x \le 1 - e$, and the margins are as stated.
   465	\end{proof}
   466	
   467	The proposition is the pillar-level form of the series claim that A does not imply B. Proposition~A, through \cref{thm:coercive-power:necessity}, constrains the conduct margin. A positive allegiance margin is a necessary ingredient of capture in the coercive pillar, and the theorem places no constraint on it. A collective can have an effective coercive pillar with no allegiance margin, and, if it has enough coercive capacity, the same effectiveness with a substantial one. The existence of police tells us nothing about which case obtains; only the margins do.
   468	
   469	A positive allegiance margin is not yet capture. Throughout this paper capture means the source's three-part capture link \citep{largo2026hbs}. A capture link $(i \to j, \pC)$ exists when actor $i$ has discretion over deployment, $j$'s allegiance margin is positive because of that discretion in a way that weakens accountability that would otherwise apply, and material evidence connects the two: for example, records showing that $i$'s orders produced surveillance, arrests or prosecutions of opponents who had broken no rule in $\mathcal{R}^0$, at rates that differ from those of supporters with the same conduct. The comparative section applies this test to each episode it discusses.
   470	
   471	\subsection{Arbitrary sanction and the capacity trade-off}
   472	
   473	The first failure mode occurs when coercion becomes insensitive to conduct within an alignment group. Its consequences are counterintuitive: coercion increases while the enforcement of rules decreases.
   474	
   475	\begin{proposition}[Arbitrary sanction]
   476	\label{prop:coercive-power:arbitrary}
   477	Fix an alignment $y$, hold $\psi(1,y)$ and $\mu$ fixed, and suppose $G$ has a density $g$. As $\psi(0,y)$ rises toward $\psi(1,y)$: (i) the conduct margin $\Delta^{\mathrm{c}}(y)$ falls to zero and the violation rate of the group rises toward the unsanctioned rate $p$; (ii) the expected number of coercive acts per member of the group,
   478	\[
   479	S(y) = \psi(0,y) + \Delta^{\mathrm{c}}(y)\bigl[1 - G(\Delta^{\mathrm{c}}(y)\mu)\bigr],
   480	\]
   481	is non-decreasing in $\psi(0,y)$.
   482	\end{proposition}
   483	
   484	\begin{proof}
   485	(i) $\Delta^{\mathrm{c}}(y) = \psi(1,y) - \psi(0,y)$ is decreasing in $\psi(0,y)$ and equals zero when the two probabilities are equal. The violation rate $1 - G(\Delta^{\mathrm{c}}(y)\mu)$ is non-increasing in $\Delta^{\mathrm{c}}(y)$, so it rises, and at $\Delta^{\mathrm{c}}(y) = 0$ it equals $1 - G(0) = p$. (ii) Write $\psi_0 = \psi(0,y)$ and $D = \psi(1,y) - \psi_0$. A member is targeted with probability $\psi_0$ if it complies and $\psi_0 + D$ if it violates, so $S = \psi_0 + D[1 - G(D\mu)]$. Differentiating in $\psi_0$, with $\partial D/\partial \psi_0 = -1$,
   486	\[
   487	\frac{\partial S}{\partial \psi_0} = 1 - \bigl[1 - G(D\mu)\bigr] + D\mu\, g(D\mu) = G(D\mu) + D\mu\, g(D\mu) \ge 0. \qedhere
   488	\]
   489	\end{proof}
   490	
   491	The proposition explains the source paper's proposal to measure coercive power by discretionary and asymmetric deployment rather than by spending \citep[Section 4]{largo2026hbs}. Arrest counts, prison populations and security budgets can all rise as the coercive apparatus stops responding to conduct. When the group in question is the opposition and $\psi(0,\mathrm{al})$ does not change, raising $\psi(0,\mathrm{op})$ toward $\psi(1,\mathrm{op})$ raises the allegiance margin $\Delta^{\mathrm{a}}(0)$ and lowers the conduct margin $\Delta^{\mathrm{c}}(\mathrm{op})$ at the same time. Targeting opponents without regard to their conduct therefore weakens deterrence among opponents, even though it increases coercion against them.
   492	
   493	Separability shows that an allegiance margin can be added without weakening deterrence, but only by adding coercive capacity. When capacity is fixed, the two margins trade off. Let the alignment groups have masses $n_{\mathrm{al}}, n_{\mathrm{op}} > 0$, and suppose that maintaining the targeting probabilities requires monitoring and enforcement capacity
   494	\[
   495	\Sigma(\psi) = \sum_{y} n_y\bigl[\kappa_1 \psi(1,y) + \kappa_0 \psi(0,y)\bigr] \le \bar{B},
   496	\]
   497	with $\kappa_0, \kappa_1 > 0$: capacity is spent on watching and acting against each status class in each group.
   498	
   499	\begin{proposition}[Capacity trade-off]
   500	\label{prop:coercive-power:capacity}
   501	Suppose the capacity constraint binds at $\psi$, and the apparatus raises $\psi(0,\mathrm{op})$ by $\varepsilon > 0$ without lowering $\psi(0,\mathrm{al})$, while $\bar{B}$ is unchanged. Then $\sum_y n_y \psi(1,y)$ must fall by at least $\kappa_0 n_{\mathrm{op}}\varepsilon/\kappa_1$. Consequently the conduct margin of at least one group falls, and that group's violation rate weakly rises.
   502	\end{proposition}
   503	
   504	\begin{proof}
   505	The new targeting function $\psi'$ must satisfy $\Sigma(\psi') \le \bar{B} = \Sigma(\psi)$. The change in the $\kappa_0$ terms is at least $\kappa_0 n_{\mathrm{op}}\varepsilon$, so the change in $\kappa_1\sum_y n_y\psi(1,y)$ is at most $-\kappa_0 n_{\mathrm{op}}\varepsilon$, which gives the bound. Since $\sum_y n_y \psi(1,y)$ falls, $\psi(1,y)$ falls for some $y$. For that $y$, $\psi(0,y)$ has not fallen, so $\Delta^{\mathrm{c}}(y)$ falls, and by \cref{prop:coercive-power:separability}(i) its violation rate $1 - G(\Delta^{\mathrm{c}}(y)\mu)$ weakly rises.
   506	\end{proof}
   507	
   508	The two propositions together give the paper's claim about allegiance-conditioned coercion its exact scope. Allegiance targeting weakens the enforcement of ordinary rules when coercive capacity is limited, and when opponents are targeted without regard to their conduct. When a regime adds capacity to fund an allegiance margin while keeping its conduct margins, separability says that rule enforcement can survive; what changes is the cost of opposition. Wintrobe's model of the dictator's trade-off between repression and the purchase of loyalty reaches related conclusions by a different route \citep{wintrobe1998}.
   509	
   510	A second failure mode concerns supporters. If $\psi(1,\mathrm{al})$ falls toward $\psi(0,\mathrm{al})$, supporters enjoy impunity: their conduct margin falls and their violation rate rises toward $p$. Allegiance-conditioned enforcement can therefore damage compliance on both sides of the political line. Total coercive activity may rise or fall in this case, depending on the relative size of the two groups and on how much the targeting of opponents increases.
   511	
   512	\subsection{The guardian problem and coup-proofing}
   513	
   514	Term (a) of \cref{prop:coercive-power:second-order} makes the loyalty of provisioned coercers depend on their paymaster, and a coercive apparatus strong enough to protect a ruler is strong enough to remove the ruler. Rulers respond by dividing coercive capacity among several organizations that watch one another. The following comparative static states when they divide more.
   515	
   516	\begin{proposition}[Coup-proofing]
   517	\label{prop:coercive-power:coup-proofing}
   518	A ruler chooses the number $k \in \{1, \dots, K\}$ of independent armed organizations. Let $c(k)$ be the probability of a successful coup, non-increasing in $k$, and $e(k)$ any function giving the loss of external military effectiveness. The ruler minimizes $f(k; r) = r\, c(k) + e(k)$, where $r > 0$ is the expected cost of losing office to a coup relative to the stakes of external effectiveness. If $r' > r$, then the largest minimizer at $r'$ is at least as large as the largest minimizer at $r$.
   519	\end{proposition}
   520	
   521	\begin{proof}
   522	Let $k$ be the largest minimizer at $r$ and $k'$ the largest minimizer at $r'$, and suppose $k' < k$. Optimality gives $f(k; r) \le f(k'; r)$ and $f(k'; r') \le f(k; r')$. Adding the two inequalities and cancelling the $e$ terms yields $(r' - r)\bigl(c(k') - c(k)\bigr) \le 0$. Since $k' < k$ and $c$ is non-increasing, $c(k') \ge c(k)$, and since $r' > r$ the product is non-negative, so it is zero and $c(k') = c(k)$. Then $f(k; r') - f(k'; r') = e(k) - e(k') = f(k; r) - f(k'; r) \le 0$, so $k$ also minimizes $f(\cdot\,; r')$. This contradicts the choice of $k'$ as the largest minimizer at $r'$, since $k > k'$.
   523	\end{proof}
   524	
   525	The proof uses no property of $e$; the effectiveness cost matters for the level of $k$ but not for the direction of the comparative static. The parameter $r$ is the salience of the elite threat: it rises with the probability that the ruler's own armed allies could and would remove the ruler, which can be proxied by recent coup attempts in the polity or its neighbors \citep{powell2011}, and it falls with the stakes of interstate war. The model has one threat parameter and does not represent mass threat. It therefore captures the fragmentation side of Greitens's argument, that elite threats produce fragmented coercive institutions \citep{greitens2016}, but not the prediction that mass threats produce unified and intrusive ones. It is consistent with Quinlivan's account of coup-proofing in Middle Eastern regimes \citep{quinlivan1999} and with the finding of Pilster and B\"ohmelt that coup-proofing has battlefield costs \citep{pilster2011}. It describes the Saudi army and National Guard, the Iranian army and Revolutionary Guard, and the division of Soviet coercion among army, security service and police. In democracies the analogous counterweights are civilian ministries, separate services and judicial oversight. The comparative static would be falsified by evidence that the number and independence of armed organizations are unrelated to measured elite threat once external threat is held constant.
   526	
   527	Coup-proofing raises $k$ but does not raise $Q^{\pC}$. Counterweights protect the ruler from the guardians; they do not protect citizens from the ruler. In a party-state or a dynastic monarchy, all $k$ organizations may answer to the same apex. Then the concentration $H^{\pC}_{(1)}$ among the organizations below the apex falls, while $H^{\pC}$, which attributes their control to the apex under \cref{def:coercive-power:share}, stays high, and so does the integration $C_{\pP\pC}$. This is the reason the source paper requires both $U_t$ and $\Integ_t$ for a strong classification: a measure of dispersion below the apex would miss the concentration above it.
   528	
   529	\subsection{Dependent corps and the outsider strategy}

2026-10-22T17:09:02.417617Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
codex
The first pass was truncated by the file’s length. I’m narrowing the remaining reads into smaller, non-overlapping ranges, then I’ll cross-check labels, citations, environments, and layout-risk constructs entirely within this file.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '245,394p' papers/latex/coercive-power.tex | nl -ba -v245" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   245	
   246	\subsection{Minimal forms in stateless and consensus societies}
   247	\label{sec:minimal}
   248	
   249	\Cref{thm:coercive-power:necessity} predicts that every persistent collective satisfying Ax5 has some sanction practice. It does not predict police. The next result shows that the deterrence margins the theorem requires can be produced with no specialized role at all. Whether the sanctioners are willing to produce them is the separate second-order question.
   250	
   251	\begin{proposition}[Minimal form]
   252	\label{prop:coercive-power:minimal-form}
   253	Consider $n$ agents who play the rule-compliance game in every period and also cooperate in a joint activity that yields each participant a per-period surplus $b > 0$. Let the profile be: every agent cooperates with every other agent who is not excluded; an agent who violates is excluded from cooperation for the next $L$ periods, and a violation by an excluded agent restarts the exclusion. Detection is perfect within the group. Then an agent with $r \in \{0, \dots, L\}$ future periods of exclusion remaining faces the deterrence margin
   254	\[
   255	d = b \sum_{k=r+1}^{L} \delta^k ,
   256	\]
   257	which equals $b\,\delta(1-\delta^L)/(1-\delta) > 0$ for an agent in good standing ($r = 0$). No agent holds a specialized sanctioning role, and with equal participation each agent's coercive control share is $1/n$, so $H^{\pC} = 1/n$.
   258	\end{proposition}
   259	
   260	\begin{proof}
   261	An agent with $r$ periods of exclusion remaining who complies at $t$ is excluded in periods $t+1, \dots, t+r$ and cooperates from $t+r+1$ onward. If it violates, it is excluded in periods $t+1, \dots, t+L$. The two continuations differ only in periods $t+r+1, \dots, t+L$, in which the complier receives $b$ and the violator does not, so $d = b\sum_{k=r+1}^{L}\delta^k$ by \eqref{eq:margin}. For $r = 0$ the sum is $b\,\delta(1-\delta^L)/(1-\delta)$. Exclusion is delivered by each agent withholding its own cooperation, so no agent holds authority over another's response, and under equal participation each holds an equal share $1/n$ of the decision-relevant control over coercive acts. Then $H^{\pC} = n \cdot (1/n)^2 = 1/n$.
   262	\end{proof}
   263	
   264	The margin is smallest, and equal to zero, for an agent already excluded for the full $L$ periods, which is why such profiles are usually combined with graduated sanctions or with longer exclusion for repeat violators. The proposition computes margins; it does not show that the profile is an equilibrium for the excluders. Each excluder forgoes its own surplus from cooperating with the violator, which is the second-order cost of \cref{prop:coercive-power:second-order}. Extending the profile so that anyone who cooperates with an excluded agent is also excluded supplies term (c). Whether the extended profile is an equilibrium depends on whether the surplus an agent would lose by being excluded from the whole group exceeds the surplus it forgoes by withholding cooperation from one violator, and we do not claim that it is an equilibrium in general. The ethnographic record suggests that terms (b) and (d) also operate: people are angered by violations, and in small groups each person's response matters.
   265	
   266	The ethnographic record of societies described as stateless or radically egalitarian supplies sanction practices of exactly this distributed kind. \Cref{tab:hardcases} summarizes them.
   267	
   268	\begin{table}[!htbp]
   269	\centering
   270	\small
   271	\caption{Minimal forms of the sanction function in societies commonly described as lacking coercive authority. The right column states the strongest reading on which the function is absent and the reason it does not hold.}
   272	\label{tab:hardcases}
   273	\renewcommand{\arraystretch}{1.15}
   274	\begin{tabularx}{\textwidth}{@{}L{2.3cm}YY@{}}
   275	\toprule
   276	Case & Documented sanction practice & Strongest counter-reading and reply \\
   277	\midrule
   278	Nuer \citep{evanspritchard1940} & Feud and the threat of retaliation by agnatic kin, settled by cattle compensation through the leopard-skin chief as mediator. & The leopard-skin chief has no power to compel. The sanction is held by kin groups, not by the mediator, so the function is present and the office is absent. \\
   279	Ju/'hoansi \citep{lee2013,marshall1976,wiessner2005} & Teasing, criticism, gossip and avoidance, with talk about norm violations recorded in camp conversations, and lethal violence in rare extreme cases. & This is the case most often cited as lacking hierarchy. The absence of an office is real, but the sanctions are frequent and documented. \\
   280	Amazonian societies \citep{clastres1987} & A chief who tries to command is abandoned or, in Clastres's reports, killed. & Clastres argues that these societies prevent power from separating from society. That supports the claim that concentration is contingent, while the group itself sanctions the chief. \\
   281	Foraging bands \citep{boehm1999,boehm2012} & Coalitions of subordinates use ridicule, disobedience, ostracism, exile and execution against would-be dominants. & Boehm calls the result a reverse dominance hierarchy. Egalitarianism is produced by sanctions rather than by their absence. \\
   282	Immediate-return societies \citep{woodburn1982} & Leveling mechanisms such as obligatory sharing, mockery and avoidance of anyone who claims authority. & Disputes are often resolved by moving away. Leaving costs the violator cooperation, which is a sanction when the violator values it. \\
   283	Commons \citep{ostrom1990,ostromdesign2010,cox2010} & Monitoring by users or accountable monitors, and graduated sanctions for those who break the rules. & Commons are often cited as order without a state. Ostrom's own design principles include monitoring and graduated sanctions. \\
   284	\bottomrule
   285	\end{tabularx}
   286	\end{table}
   287	
   288	Three features of the table deserve emphasis. The sanctions are distributed, so $H^{\pC}$ is low. They are rarely specialized: no person makes a living from them. And they are not mild. Boehm's reverse dominance hierarchy includes execution of persistent would-be dominants \citep{boehm1999}, and Lee recorded homicides among the Ju/'hoansi \citep{lee1979}. The egalitarian character of these societies does not come from the absence of coercion. It comes from the fact that coercion is held by the collective and directed against attempts to concentrate it. In the vocabulary of this series, the societies of \cref{tab:hardcases} have the coercive function (Proposition~A) and low concentration with high contestability (the negation of Proposition~B). Woodburn's phrase for the mechanism, institutions of leveling, describes a coercive pillar whose output is the prevention of capture \citep{woodburn1982}.
   289	
   290	The ethnographic evidence has known limits. Most of it was gathered after contact with states and markets, from groups living in marginal environments, and foraging societies vary more than the classic accounts suggest \citep{kelly1995}. \citet{graeber2021} argue that some societies moved seasonally between egalitarian and hierarchical arrangements, including temporary policing authority during collective hunts. If correct, this strengthens the present argument: the sanction function persists while its holders change with the season.
   291	
   292	\subsection{Counterexample attempts}
   293	\label{sec:counter}
   294	
   295	The strongest attempt to refute the necessity of coercion appeals to self-enforcing cooperation. Axelrod showed that reciprocal strategies can sustain cooperation without a central authority \citep{axelrod1984}. Greif showed that the eleventh-century Maghribi traders enforced agency contracts through a coalition in which cheated merchants were refused future employment by all members \citep{greif1993}. Edwards and Ogilvie dispute this reading and argue that the traders also relied on formal legal institutions \citep{edwards2012}; on either reading the case contains sanctions. Ellickson found that cattle ranchers in Shasta County settled disputes by neighborly norms rather than by law \citep{ellickson1991}. None of these is a counterexample. In each case an agent's continuation payoff depends on the agent's own past conduct: the reciprocator retaliates, the coalition refuses to deal, and the neighbor gossips or engages in self-help. Each mechanism is a sanction regime in the sense of \cref{def:coercive-power:regime}. What these cases refute is the Hobbesian inference from the need for sanctions to the need for a sovereign.
   296	
   297	A second attempt appeals to internalization. If socialization makes norm violation intrinsically costly, temptations may never be positive, and sanctions are unnecessary. The theorem accepts this as a logical possibility: internalization lowers $p$, and if $p \le \theta$ Ax5 fails and the coercive pillar is not derived for that rule. The bridge assumption claims that no functioning governance system achieves $p \le \theta$ for every rule it keeps in force. The societies that come closest, those of \cref{tab:hardcases}, are also the ones in which ethnographers record continual sanctioning talk \citep{wiessner2005}. Internalization and sanction are complements, not substitutes: shared norms reduce temptation and also supply the motive for punishing those who remain tempted (term (b) of \cref{prop:coercive-power:second-order}).
   298	
   299	A third attempt appeals to exit. Where dissatisfied members can simply leave, perhaps the collective needs no sanctions. Exit is a sanction when those who leave take with them something the violator valued. When exit costs the violator nothing, \cref{lem:coercive-power:deterrence} predicts violations at the unsanctioned rate $p$. A collective then persists only by relying on fewer rules that matter, which is what immediate-return foragers appear to do: with little storage there is less to steal and less to hoard \citep{woodburn1982}. Exit narrows the set of rules that require enforcement; it does not remove the function for the rules that remain.
   300	
   301	These replies define the falsifier, and the falsifier must not be immunized. The replies to the second and third attempts could be used to reclassify any compliant, unsanctioned collective as one with $p \le \theta$, which would make the necessity claim true by definition. To prevent this, the temptation share $p$ must be measured independently of the sanction practices it is used to explain, and before they are observed. Designs that offer members an unobserved opportunity to break a rule, so that no response by others is possible, measure the share who would violate in the absence of sanctions. Proposition~A for the coercive pillar is refuted by a persistent collective in which such a measurement gives $p > \theta$ for a rule in force, compliance is nonetheless above $1 - \theta$, and violators suffer no material, relational or reputational cost of any kind. A collective in which the measured $p$ is below $\theta$ for every rule in force refutes the bridge assumption instead. We found no documented case of either kind in the sources reviewed, and we know of no study that has carried out this measurement in a stateless society.
   302	
   303	\subsection{Functional necessity without functionalist explanation}
   304	
   305	The theorem claims the necessity of a function, not of an institution. That distinction answers the classic objection of \citet{hempel1959}: from the premise that a system needs some sanction practice, it does not follow that it needs a police force, because many functional equivalents can meet the need. \Cref{tab:hardcases} lists several. The theorem also makes no causal claim about why any particular polity has the coercive institutions it has. \citet{elster1979,elster1983} argued that explaining an institution by its beneficial effects requires a feedback mechanism from effects to institution. \Cref{thm:coercive-power:necessity} is a condition of persistence, not a functional explanation: collectives without a sanction regime do not keep rules in force, but the theorem says nothing about which sanction regime a collective adopts or why. That question belongs to the comparative analysis of \cref{sec:comparative}, where design varies with threats, finances and legitimating beliefs.
   306	
   307	\section{Literature on coercive power}
   308	\label{sec:literature}
   309	
   310	\subsection{Coercion and the making of states}
   311	
   312	Modern discussion of coercion begins with Weber's definition of the state as the human community that successfully claims the monopoly of the legitimate use of physical force within a territory \citep{weber1946,weber1978}. Part~II uses it where it treats the coupling of rule-making to enforcement. For the coercive pillar, the important word is ``claims''. Weber's definition concerns legitimacy, and \cref{sec:layer} has already separated it from command concentration.
   313	
   314	Tilly made coercion the engine of European state formation. Rulers who made war had to extract resources to pay for it, and the bargains they struck with those who held capital produced different state forms: coercion-intensive paths where rulers squeezed agrarian populations, capital-intensive paths where they borrowed from merchant cities, and capitalized-coercion paths in between \citep{tilly1990}. In an earlier essay Tilly compared war making and state making to organized crime, since the state sells protection against threats that it partly produces itself \citep{tilly1985}. The analogy is a heuristic, not an equivalence, and this paper treats it as a hypothesis about when coercion becomes capture. Karaman and Pamuk extended the fiscal side of the argument to show that the effect of warfare on state capacity depended on economic structure and regime type across Europe and the Ottoman Empire \citep{karaman2013}. The financing side of this literature belongs to Part~I; here the question is how the coercive apparatus that resulted was controlled.
   315	
   316	Mann distinguished despotic power, the range of actions rulers can take without negotiation with civil society, from infrastructural power, the capacity to penetrate society and implement decisions \citep{mann1984}. The distinction maps onto the two margins of \cref{def:coercive-power:margins}. A state with high infrastructural power can enforce rules widely (a large conduct margin is feasible); a state with high despotic power can direct enforcement as it pleases (a large allegiance margin is feasible). North, Wallis and Weingast described most of recorded history as limited-access orders in which specialists in violence agree not to fight because they share rents \citep{nww2009}. In the vocabulary of this series, such orders have high $C_{\pF\pC}$ by construction.
   317	
   318	\subsection{The guardian problem}
   319	
   320	If coercion is provisioned (term (a) of \cref{prop:coercive-power:second-order}), the agents who hold it can turn it against those who provision them. Civil-military relations theory is the study of this problem. Huntington proposed objective civilian control: a professional officer corps, autonomous in military matters and politically neutral \citep{huntington1957}. Janowitz replied that professionalism alone does not secure neutrality and that the military should be integrated into civilian society as a constabulary force \citep{janowitz1960}. Finer catalogued the forms of military intervention in politics \citep{finer1962}, and Huntington and Perlmutter described praetorian societies in which armed forces become ordinary political contestants \citep{huntington1968,perlmutter1969}. Feaver recast the relationship as a principal-agent problem in which civilians choose monitoring mechanisms and soldiers choose whether to work or shirk \citep{feaver1999,feaver2003}. Kohn emphasized that civilian control is a practice that must be exercised, not merely a constitutional provision \citep{kohn1997}.
   321	
   322	Authoritarian rulers face the guardian problem in a sharper form. Svolik showed that dictators face two separate problems: sharing power with the allied elites who help them rule, and controlling the masses they rule \citep{svolik2012}. Coercive agents are useful against the second problem and dangerous in the first. Quinlivan described the coup-proofing practices of Middle Eastern regimes: reliance on family, ethnic and religious loyalties, the creation of parallel military forces, and multiple overlapping internal security agencies \citep{quinlivan1999}. Pilster and B\"ohmelt found that coup-proofing reduced battlefield effectiveness in interstate wars between 1967 and 1999 \citep{pilster2011}. Greitens argued that the design of coercive institutions depends on whether rulers perceive their main threat as coming from elites or from the masses: elite threats favor fragmented and socially exclusive organizations, mass threats favor unified and inclusive ones, and these designs in turn shape patterns of state violence \citep{greitens2016}. Slater showed that elites who fear contentious mass politics may accept stronger coercive and extractive institutions as protection pacts \citep{slater2010}.
   323	
   324	\subsection{Repression and its limits}
   325	
   326	Repression is the use of coercion against political opponents, and it is the most direct observable form of the allegiance margin. Davenport's review defines repression broadly, from surveillance and bans to arrests, torture and mass killing, and organizes the field around the problem of how authorities use coercion against domestic challengers \citep{davenport2007}. Poe and Tate found in a 153-country analysis of the 1980s that democracy and participation in civil or international war had substantively important effects on repression of personal integrity rights \citep{poe1994}. Hill and Jones, using cross-validation rather than significance tests, found that few proposed explanations improve out-of-sample prediction much; democratic institutions predict some kinds of repression far better than others, and features of domestic legal systems perform well \citep{hill2014}. Wintrobe modeled dictators as trading off repression and the purchase of loyalty \citep{wintrobe1998}. Rejali documented a boundary case: democracies under public monitoring developed and exported torture techniques that leave few marks \citep{rejali2007}. Democracy constrains what coercers can be seen to do; it does not by itself eliminate the allegiance margin.
   327	
   328	Whether coercive agents carry out repression is not guaranteed. Bellin attributed the durability of Middle Eastern authoritarianism to the will and capacity of coercive apparatuses to repress, and after the Arab uprisings of 2011 she examined why some militaries defected and others did not \citep{bellin2004,bellin2012}. Albrecht and Ohl applied Hirschman's categories of exit, voice and loyalty to military behavior during unrest \citep{albrecht2016}, and Chenoweth and Stephan argued that nonviolent campaigns succeed in part by inducing defections among security forces \citep{chenoweth2011}. Gerschewski placed repression beside legitimation and co-optation as the three pillars of autocratic stability \citep{gerschewski2013}.
   329	
   330	\subsection{Policing, punishment and legitimacy}
   331	
   332	Within consolidated states, the main question about ordinary enforcement is why people comply. Tyler found that people obey the law more because they judge the authorities legitimate and the procedures fair than because they fear sanctions \citep{tyler1990}, and Jackson and colleagues found the same pattern in survey data on policing \citep{jackson2012}. These findings do not contradict \cref{thm:coercive-power:necessity}. They show that legitimation lowers the temptation distribution and supplies the motive for cooperation with enforcement, which in the present model shifts $G$ and strengthens term (b). Foucault traced the shift from spectacular punishment to the disciplinary prison and the surveillance it made possible \citep{foucault1977}. Pratt documented the comparatively low imprisonment rates and humane prison conditions of the Nordic countries and traced them to egalitarian welfare states, while warning that populist pressures could erode them \citep{pratt2008a,pratt2008b}.
   333	
   334	\subsection{Contribution}
   335	
   336	The literatures above mostly study either the necessity of order (from Hobbes to the economics of deterrence) or the dangers of coercive power (from civil-military relations to repression), and they rarely connect the two formally. The deterrence literature from \citet{becker1968} onward models the conduct margin and assumes enforcement is impartial. The repression literature studies the allegiance margin and largely takes the conduct margin for granted. This Part treats both as properties of a single sanction-probability function, which shows that the necessity of coercion and its capture are logically separate and empirically distinguishable. It also places the evidence of six regime types on a common scale, so that the comparison asks how each type distributes a function that all of them share.
   337	
   338	\section{Comparative analysis across six regime types}
   339	\label{sec:comparative}
   340	
   341	Each regime type below is asked the same five questions: which institutions hold the coercive function, how concentrated and contestable it is, how it depends on and is integrated with the other five pillars, what preserves accountability, and which capture episodes and checks are documented. Every claimed capture episode is held to the same standard, the three-part capture link of the source paper as applied to coercion in \cref{sec:mechanisms}, and each subsection reports at least one documented episode or standing risk and one documented check. The types are ideal types rather than mutually exclusive classes. The United States, for instance, is both a market-capitalist society and a secular democracy; each illustration is assigned to the type whose defining feature it shows. No numerical value of $U_t$ or $\Integ_t$ is reported for any real polity, because none has been coded under a preregistered scheme. Statements about concentration and integration are qualitative orderings that a coding exercise could confirm or overturn.
   342	
   343	\subsection{Market-capitalist societies}
   344	\label{sec:market}
   345	
   346	In market-capitalist societies the coercive function is held by public police forces, militaries and intelligence agencies under elected civilian authority, together with a private sector that manufactures weapons, supplies services and provides security for property. The defining feature for this pillar is the participation of private capital in producing coercive capacity and its interest in how that capacity is used.
   347	
   348	The link between private enterprise and coercion is older than industrial capitalism. Parrott showed that the armies of early modern Europe were raised and supplied to a large extent by military entrepreneurs who treated war as a business, and that this system was more effective than older accounts of state-led military modernization allowed \citep{parrott2012}. The modern form is the defense industry. In his farewell address of January 1961, President Eisenhower warned the American public against the acquisition of unwarranted influence by what he called the military-industrial complex \citep{eisenhower1961}. In the vocabulary of this series, the warning describes a possible capture link in which producers of coercive capacity gain privileged access to the decisions that set budgets, procurement and deployment, raising $C_{\pF\pC}$.
   349	
   350	Concentration differs sharply between the military and the police. Command of the armed forces is concentrated in a national executive, so the military contributes a large share to $H^{\pC}$, while legislative control of budgets divides authority over provisioning. Policing in the United States is dispersed across federal, state and local agencies, each answering to a different elected authority, which lowers $H^{\pC}$ for ordinary enforcement. The theory of civilian control was developed largely on the American case: Huntington's objective control, Janowitz's constabulary force and Feaver's agency model all address how elected civilians can command a professional military that they cannot fully monitor \citep{huntington1957,janowitz1960,feaver2003}. Accountability rests on component (1) of $Q^{\pC}$, appointment and removal by elected civilians; on components (2) and (4), judicial authorization of searches and the civil and criminal liability of agents; and on component (6), legislative scrutiny of budgets. Kohn argued that these provisions secure control only when civilians actually exercise them \citep{kohn1997}.
   351	
   352	The capture hypothesis specific to this regime type is that concentrated private interests shape the use of coercion. It meets the source paper's standard for a capture link only if three things are shown: privileged access by a private party, a weakening of the accountability that would otherwise apply, and material evidence that the access changed an enforcement outcome \citep{largo2026hbs}. Eisenhower's warning is evidence that a senior insider regarded the risk as serious; it is not evidence that capture occurred in any particular decision. A better documented episode comes from industrial conflict. The federal Commission on Industrial Relations reported in 1915 that ``practically every industrial State has at some relatively recent time permitted its institutions to be used by one party or the other to an industrial dispute (almost without exception the employers)''. It found that sheriffs in many counties deputized guards ``in the employment and pay of corporations'' and that militia were at times recruited from corporate guards and employees \citep[pp.~147 to 148]{cir1915}. Each element of the capture link is present in that finding: privileged access through deputization, the displacement of publicly accountable police by employer-paid agents, and enforcement outcomes against strikers. In the notation of \cref{def:coercive-power:margins}, the allegiance margin was indexed by the side a person took in an industrial dispute. The report was itself the check. A public commission with investigative powers documented the practice and recommended rules for the conduct of the militia \citep{cir1915}.
   353	
   354	For the present, following the source's proposal for narrow projects, the test of the military-industrial hypothesis is a preregistered sample of procurement decisions, not a selection of scandals. The rival explanation is that defense spending responds to external threats and that contractors compete for contracts under rules they do not control. Tilly's protection-racket analogy suggests a related hypothesis about ordinary policing: if public coercion protects some forms of property more than others, it transfers value to their owners \citep{tilly1985}. This predicts a positive allegiance margin indexed by economic position, which is an empirical question about arrest and prosecution rates conditional on conduct.
   355	
   356	\subsection{Communist party-states}
   357	\label{sec:communist}
   358	
   359	In communist party-states the ruling party holds the coercive function through security organs that answer to its leadership, through political officers embedded in the armed forces, and through the police and militia. In the Soviet case the line of security organs ran from the Cheka, founded as Lenin's political police \citep{leggett1981}, through its successors to the KGB, whose own successors after 1991 Knight traced \citep{knight1996}. In the German Democratic Republic the Ministry for State Security built an apparatus of full-time officers and unofficial informants that reached into local society \citep{gieseke2014,bruce2010,koehler1999}. In the People's Republic of China the party maintains command of the People's Liberation Army \citep{shambaugh2002}, and the police carry heavy burdens of stability maintenance that Scoggins and O'Brien describe from the officers' own perspective \citep{scoggins2016}.
   360	
   361	Concentration is high at the apex: the party leadership appoints and removes the heads of every coercive organization through the appointment channel analyzed in Part~II, so $H^{\pC}$ is high and the integration $C_{\pP\pC}$ is close to its maximum. Below the apex, however, the apparatus is divided, so $H^{\pC}_{(1)}$ is lower. Army, security service and police are separate organizations with separate chains of command, and party organs inside the army provide a further check. Colton's study of Soviet military politics found that the relationship between commissars and commanders was less a struggle between party and army than a structured form of military participation in politics, with the military's role largely confined to its own institutional concerns \citep{colton1979}. The division of the coercive apparatus is a form of counterbalancing, and the comparative static of \cref{prop:coercive-power:coup-proofing} applies to it.
   362	
   363	Integration with the ideological pillar is direct, since the same party commands both: political officers and party organizations inside the coercive organs make doctrinal loyalty part of the job, so $C_{\pI\pC}$ is high. Integration with production is also high. The Soviet camp system used forced labor on a large scale under the direction of the same party-state that set production plans \citep{applebaum2003,gregory2003}, so the dependency $\pC \to \pW$ and the integration $C_{\pC\pW}$ were both at the center of the Soviet economy for several decades. \Cref{sec:cw} returns to it. Contestability from outside the party is low: there is no independent judiciary able to review security operations, no competitive legislature able to audit them, and no free press able to expose them. The internal checks are party discipline and periodic purges. Purges can be used against security chiefs, but they are themselves exercises of the coercive function, so they check particular holders of power without raising $Q^{\pC}$.
   364	
   365	The terror of the late 1930s is the episode with the largest consequences, and it shows why arbitrariness and allegiance must be distinguished. The security organs were turned against party members, officers and ordinary citizens \citep{conquest1990}. Coercion fell on people who had broken no rule in any allegiance-neutral reference set, so the conduct margin collapsed across alignments, which is the arbitrariness of \cref{prop:coercive-power:arbitrary}. Whether the episode was also capture in the source's sense turns on the material-evidence step: how far the targeting was directed from the center against categories defined by political suspicion. That is exactly the question on which Conquest and revisionist historians disagree. Getty argued that the purges grew in part out of conflicts and confusion within the party apparatus rather than from a single central plan \citep{getty1985}. On Conquest's reading the episode meets all three conditions of a capture link; on Getty's it is closer to arbitrariness produced by an apparatus that the center did not fully control. Either way it is a failure of the coercive pillar, and the numbers on either side should be cited with that debate in view. The documented checks are of two kinds. Party supremacy over the military meant that the Soviet army did not seize power \citep{colton1979}. And the deterrent power of the apparatus rested on beliefs: when those beliefs shifted in 1989, regimes that had seemed secure fell with little warning \citep{kuran1991}.
   366	
   367	Reform socialism, which introduced markets inside party-states, did not change who held coercion. Kornai's account of the socialist system treats the reforms as changes in coordination mechanisms under continued party rule \citep{kornai1992}. For this reason the coercive pillar of market socialism as practiced is analyzed here rather than in the next subsection.
   368	
   369	\subsection{Social democracy and democratic socialism}
   370	\label{sec:socdem}
   371	
   372	In the social democracies of Northern Europe the coercive function is held by national police and armed forces under parliamentary control, with independent oversight bodies and a long tradition of citizen armies. The distinctive feature of this regime type for the coercive pillar is the combination of a centralized apparatus with high contestability and low reliance on punishment.
   373	
   374	Sweden illustrates the oversight structure. Its Parliamentary Ombudsman was established with the Instrument of Government of 1809 to supervise how judges and civil servants apply the law, and its supervision was later extended to local government \citep{jo2026}. Ombudsman supervision of public authorities contributes to components (3) and (4) of $Q^{\pC}$: complaints can reach an independent office with access to records, and officials can be held to account for unlawful conduct. Civilian control of the armed forces has varied with the perceived external threat. Hedlund's study of Swedish civil-military relations from 1984 to 2011 found that civilian control over the officer rank system and over professional officer education changed as perceptions of threat changed \citep{hedlund2011}.
   375	
   376	The Nordic countries are best known in this domain for penal moderation. Pratt described comparatively low imprisonment rates and humane prison conditions, rooted in egalitarian welfare states with high social trust, and warned that the pattern was under pressure from more punitive politics \citep{pratt2008a,pratt2008b}. Penal moderation is not the absence of the coercive function. \Cref{thm:coercive-power:necessity} requires a positive deterrence margin, not a large sanction magnitude, and \cref{cor:coercive-power:magnitude} shows that a high detection probability or a temptation distribution shifted toward compliance permits smaller sanctions. Legitimacy research suggests the second mechanism. Where people regard the police and courts as fair, they comply for reasons other than fear of punishment \citep{tyler1990,jackson2012}, which lowers the temptation distribution and strengthens the motive to cooperate with enforcement.
   377	
   378	The Nordic security services also supply documented episodes of the allegiance margin, and documented checks on it. In Norway the parliament appointed a commission to examine allegations of illegal surveillance. Its report of 1996, known by the name of its chair, found that the police security service had carried out widespread illegal political surveillance, particularly in the 1960s and 1970s, of individuals and organizations on the political left \citep{eos2026}. The response was a parliamentary oversight committee for all the secret services, established under a separate law of 1995 and elected for the first time in 1996 \citep{eos2026}. In Sweden the government appointed a commission in 1999 to examine the security services' surveillance of domestic political groups since 1945. Its directive records that the security police were barred in 1969 from registering a person solely on account of political views, that a general constitutional ban on such registration followed in 1977, and that military intelligence had registered communists from 1955 \citep{dir1999}. The commission reported in 2002 \citep{sou2002}. These episodes meet the capture-link test in the form the source requires: discretion over surveillance, use of it against political opponents who had broken no rule, and documentary evidence assembled by official inquiries. They also show the check working, though decades late: legislatures with investigative powers exposed the practices and created standing oversight.
   379	
   380	Dependencies and integration take an unusual form in this regime type. Conscript armies draw on the labor time of the whole population, so the dependency $\pW \to \pC$ runs through a universal obligation rather than through a professional caste, and it involves no integration of command over coercion and production. Appointment runs through parliament rather than through a party, and provisioning runs through the general budget of a high-tax state. Concentration $H^{\pC}$ is moderate to high because national police and military command are centralized, but contestability $Q^{\pC}$ is high on most components, so the contribution of the coercive pillar to $U_t$ in \eqref{eq:U} is small. This is the case that the source paper's Proposition~4 anticipates: concentration combined with high-quality review can coexist with competent services and low arbitrary sanctioning \citep{largo2026hbs}.
   381	
   382	Democratic socialism as a program, as distinct from the social-democratic welfare states that partly realized it, has no separate record of coercive institutions in the sources reviewed. Its claims about coercion are claims about how the institutions of the previous paragraphs should be governed, and they are evaluated by the same measures.
   383	
   384	\subsection{Islamic states}
   385	\label{sec:islamic}
   386	
   387	Islamic states are polities in which political legitimacy has been derived in significant part from religious law, and they differ widely: Sunni and Shi'i, dynastic and revolutionary, imperial and national. The coercive function has been held by caliphal armies paid through state registers, by corps of slave soldiers, by tribal levies, by dynastic guards and by revolutionary ideological forces. The common thread is not a single institution but a recurring problem: how a ruler whose legitimacy rests on religious law commands armed men whose loyalty may run to tribe, faction or their own corps.
   388	
   389	In the early caliphates soldiers were paid from the revenues of conquest through state registers, which made coercion directly dependent on the fiscal system \citep{kennedy2001}. From the ninth century, rulers came to rely on soldiers of slave origin, recruited from outside the societies they governed. Crone argued that military slavery offered rulers a source of armed force independent of the tribal and local elites whose loyalty they could not trust \citep{crone1980}, and Pipes traced the genesis of the system \citep{pipes1981}. The term slave soldier is the scholars' term for a legal status of military servitude that could lead to command, wealth and rule. It differs from chattel slavery in the household or the field, and this paper uses it only in that technical sense. The Mamluk sultanate that ruled Egypt and Syria from 1250 was governed by such soldiers and their successors \citep{irwin1986}.
   390	
   391	The Ottoman Empire built the most elaborate version. Its kul system recruited the sultan's servants, including the Janissary infantry, as personal dependents of the ruler, and Kunt traced how the households of these servants transformed provincial government between 1550 and 1650 \citep{kunt1983}. Agoston showed that the Ottoman state sustained a large military and a domestic weapons industry over centuries, adapting to European military change more successfully than older accounts of decline allowed \citep{agoston2005,agoston2014}. Tezcan dates a transformation of the Ottoman polity toward a more limited monarchy to the period from about 1580 to 1826 and treats the deposition and killing of Sultan Osman II in 1622, in which the sultan's own soldiers took part, as its turning point \citep{tezcan2010}. The pattern, a dependent corps recruited for loyalty that later acquires interests and power of its own, is the subject of \cref{prop:coercive-power:outsider}.
   392	
   393	In the Islamic Republic of Iran the coercive function is divided between the regular army and the Islamic Revolutionary Guard Corps, created after the revolution as an ideological guardian of the new order \citep{katzman1993,arjomand1988}. Buchta mapped the parallel institutions through which the Leader, the Guardian Council and the Guard share power \citep{buchta2000}. Wehrey and colleagues documented the Guard's expanding domestic political, economic and security roles \citep{wehrey2009}. Alfoneh argued that the Guard was transforming the state from theocracy into military dictatorship \citep{alfoneh2013}; his account comes from an advocacy institute and is best read alongside the more cautious RAND assessment. Either way, one organization commanding both coercive forces and large economic holdings raises the integration $C_{\pF\pC}$, and its ideological mandate under the same leadership raises $C_{\pI\pC}$.
   394	

2026-10-22T17:09:05.934231Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '395,544p' papers/latex/coercive-power.tex | nl -ba -v395" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   395	Saudi Arabia shows a dynastic version of counterbalancing. The kingdom maintains a regular army and a separate National Guard, a duality that Cordesman described and that Quinlivan treated as an instance of coup-proofing \citep{cordesman2003,quinlivan1999}. Gause placed it within the dynastic security structures of the Gulf monarchies \citep{gause1994}. The alliance between the Al Saud and the Wahhabi religious establishment supplies the legitimating side \citep{alrasheed2002}. The storming of the Grand Mosque in Mecca in November 1979 by Juhayman al-'Utaybi and his followers, whose origins and legacy Hegghammer and Lacroix reconstruct from fieldwork, challenged both arrangements at once: it contested the rulers' religious legitimacy and their coercive control of the holy places \citep{hegghammer2007}.
   396	
   397	Accountability in these polities has rested on different mechanisms from those of constitutional democracies. Where scholars of religious law held moral authority independent of the ruler, coercion depended on legitimation ($\pI \to \pC$) supplied by a group the ruler did not command, which is evidence of low rather than high $C_{\pI\pC}$ and a potential constraint on the ruler. Its strength varied across these polities and has not been measured on a common scale. Counterbalancing among forces is an internal check that protects rulers more than subjects. The capture-link test can be applied to the dependent-corps episodes. In the Mamluk case the corps used its control of deployment to take rule itself, and the change of rulers is documented \citep{irwin1986}. In the Ottoman case of 1622 the sultan's soldiers used their arms against the sultan, and Tezcan documents the lasting change in the distribution of power that followed \citep{tezcan2010}. Both are capture of the ruler by the coercive corps rather than capture of the coercive pillar by an outside coalition, which is the form \cref{prop:coercive-power:outsider} predicts. The documented checks are counterbalancing among separate forces and long periods in which the Ottoman state sustained and supplied its military establishment from the center \citep{agoston2005}.
   398	
   399	\subsection{Catholic monarchies}
   400	\label{sec:catholic}
   401	
   402	In the Catholic monarchies of early modern Europe royal authority was intertwined with the Church, and the coercive function was held by royal armies officered by nobles and by purchasers of commissions, by mercenary and contracted companies, by Swiss and other foreign troops, by the papal forces of the Papal States, and in Spain by the lay familiars who assisted the Inquisition. Internal diversity was considerable: Habsburg Spain, Bourbon France and the Papal States differed in fiscal structure, in their relations with Rome, and in the strength of their representative assemblies.
   403	
   404	Habsburg Spain fought across Europe with an army that depended on long supply lines and on credit. Parker's study of the Army of Flanders and the Spanish Road between 1567 and 1659 showed how logistics, finance and pay shaped military operations, and how unpaid troops mutinied \citep{parker1972}. Thompson examined how the Spanish crown governed war between 1560 and 1620, including its reliance on contractors and the sale of offices \citep{thompson1976}, and Elliott's survey places these developments in the history of the monarchy \citep{elliott1963}. Mutiny is a sanction by soldiers against their paymaster. It is also direct evidence for term (a) of \cref{prop:coercive-power:second-order}: when provisioning failed, so did the willingness of the coercers to coerce on the crown's behalf.
   405	
   406	Bourbon France built one of the largest armies in Europe. Lynn traced its growth between 1610 and 1715 \citep{lynn1997}. Rowlands showed that under Louis XIV royal service and private interest were intertwined: officers invested their own resources in their units, and the crown relied on that investment while trying to control it \citep{rowlands2002}. Venal commissions integrate finance and force at the level of the individual officer, who is both a creditor of the state and an agent of its force. Parker's thesis of a military revolution, in which new fortifications and tactics drove the growth of armies and states, frames these developments \citep{parker1988}, and Tilly's account of coercion and capital explains why monarchies with access to commercial credit could field such armies \citep{tilly1990}.
   407	
   408	The Papal States combined spiritual and temporal sovereignty. Their military forces, including the Swiss Guard, are documented from 1796 onward in Alvarez's history, which drew on the Guard's archive \citep{alvarez2011}; the verified sources reviewed for this paper do not cover the papal forces of earlier centuries. The Church also wielded sanctions of its own, including excommunication and interdict, which are ideological sanctions in the sense of \cref{def:coercive-power:sanction}: they impose relational and reputational costs and rely on belief for their force. In Spain the Inquisition drew on lay familiars who assisted its officials; Kamen's revisionist history of the Inquisition argues that its scale and severity were smaller than the older black legend held \citep{kamen1997}.
   409	
   410	Contestability came from three sources. Representative assemblies, where they retained the power to grant taxes, could limit the provisioning of armies. Contracted soldiers could refuse service when unpaid. And the Church could withhold legitimation, although in practice the crowns of Spain and France exercised considerable control over the churches within their kingdoms. Concentration of command rose over the period as monarchs replaced contracted forces with standing armies, while venality kept part of the control over units in private hands. Ertman's comparative account of state building shows how the timing of military competition shaped whether such states became patrimonial or bureaucratic \citep{ertman1997}. The capture-link test is harder to apply here than in the modern cases, because the documented material concerns the structure of command rather than its use against particular groups. What is documented is a standing risk: venal and contracted command made units partly private property, which gave their owners discretion over a public function. The documented check is the mutiny, in which soldiers withdrew coercion from a crown that failed to pay \citep{parker1972}, together with the fiscal power of estates where it survived and the limits that dependence on credit imposed on royal war-making.
   411	
   412	\subsection{Secular democracies}
   413	\label{sec:secular}
   414	
   415	In secular democracies authority is distributed among elected officials, courts and private institutions, and the legitimacy of coercion rests on constitutional law rather than on religious or party doctrine. The coercive function is held by professional armed forces under civilian command, police forces whose intrusive measures require judicial authorization, and intelligence services subject to legislative oversight. The defining feature for this pillar is the attempt to raise every component of $Q^{\pC}$ by constitutional design.
   416	
   417	The core mechanisms are civilian control of the military, judicial warrants for intrusive policing, and legislative oversight of intelligence. Kohn's account of how democracies control the military stresses that control is a practice of appointment, budget, doctrine and promotion that civilians must actively exercise \citep{kohn1997}. Born and Caparini compared the models by which democracies try to subject intelligence services to democratic control \citep{born2007}. These mechanisms map onto components (1), (2) and (6) of \cref{def:coercive-power:qc}, and their effectiveness depends on the judicial independence analyzed in Part~III. Janowitz's argument that a professional military should remain integrated with civilian society, rather than isolated from it, describes a further safeguard: a force that shares the values of those it might be ordered against is less likely to obey an order to target them \citep{janowitz1960}.
   418	
   419	The best documented capture episode in this regime type, and the best documented check, come from the same inquiry. In 1975 the United States Senate established a select committee, chaired by Frank Church, to study the government's intelligence operations. Its final report of April 1976 concluded that ``the Government has often undertaken the secret surveillance of citizens on the basis of their political beliefs, even when those beliefs posed no threat of violence or illegal acts on behalf of a hostile foreign power'' \citep[Book II, Part I, Section C]{church1976}. The committee examined the surveillance record against the lawful character of the targets' activities, which supplies the material evidence the capture-link test requires. In the notation of \cref{def:coercive-power:margins}, the finding describes a positive allegiance margin among non-violators: $\psi(0,\mathrm{op}) > \psi(0,\mathrm{al})$. The same report documents the check. A legislature with investigative powers exposed the practice, and a permanent Senate intelligence committee followed.
   420	
   421	Rejali's study of torture in democracies is the hard boundary case. Democracies that were monitored by a free press and human-rights organizations developed interrogation techniques that left few visible marks, so that public monitoring changed the form of abuse rather than ending it \citep{rejali2007}. Cross-national evidence nonetheless shows that democracy is associated with less repression of personal integrity rights \citep{poe1994}, although Hill and Jones caution that the relationship is stronger for some forms of repression than for others \citep{hill2014}. Coups are rare in consolidated democracies, and the dataset of Powell and Thyne permits this claim to be tested rather than assumed \citep{powell2011}.
   422	
   423	Concentration in secular democracies varies with constitutional structure. Unitary states with national police forces have higher $H^{\pC}$ than federal states with local forces, but both may have high $Q^{\pC}$. Integration with the political pillar is limited because civilian appointment is shared among elected bodies and constrained by professional norms of neutrality. The dependency on the judicial pillar runs through warrants and liability, and the dependency on legitimation runs through public acceptance of the constitution and of the police, which Tyler's research measures directly \citep{tyler1990}. The main risk specific to this type is that oversight bodies depend on information that the overseen agencies control, which is the principal-agent problem of Feaver's model applied to intelligence \citep{feaver2003}. The episodes of this subsection and of \cref{sec:socdem} show that risk realized for decades before legislatures intervened.
   424	
   425	\subsection{Summary across regimes}
   426	
   427	\Cref{tab:regimes} summarizes the comparison. Every regime type has the coercive function, as Proposition~A requires. They differ in who holds it, how concentrated and contestable it is, and how it depends on and is integrated with the other pillars.
   428	
   429	\begin{table}[!htbp]
   430	\centering
   431	\small
   432	\caption{The coercive function across six regime types. Orderings of concentration and contestability are qualitative and await preregistered coding.}
   433	\label{tab:regimes}
   434	\renewcommand{\arraystretch}{1.15}
   435	\begin{tabularx}{\textwidth}{@{}L{2.2cm}YYY@{}}
   436	\toprule
   437	Regime type & Principal holders of the function & Concentration, contestability and strongest integration & Documented capture episode or risk, and check \\
   438	\midrule
   439	Market-capitalist & Public police and militaries under elected civilians, with private producers of weapons and security services & Command of the military is concentrated, policing is dispersed, and the distinctive integration is between finance and coercion & Employer-paid deputies and militia in industrial disputes were documented in 1915, and a federal commission exposed the practice \\
   440	Communist party-state & Party-controlled security organs, armies with political officers, and police & Command is concentrated at the party apex with internal division among organs, contestability from outside the party is low, and the strongest integration is with political appointment & The terror of the late 1930s was arbitrary and possibly also capture, and party supremacy prevented military takeover \\
   441	Social democracy & National police and conscript or professional armies under parliamentary control & Concentration is moderate to high, contestability is high through ombudsmen and courts, and conscription makes coercion depend on universal service & Political surveillance by the security services was exposed by official inquiries, which led to standing parliamentary oversight \\
   442	Islamic states & Caliphal armies, slave-soldier corps, dynastic guards and revolutionary guards & Rulers counterbalance separate forces, and integration with legitimation and, in Iran, with finance is strong & Mamluk rule and the regicide of 1622 show corps becoming principals, and counterbalancing protected rulers more than subjects \\
   443	Catholic monarchies & Royal armies with venal officers, contracted companies, papal forces and Inquisition familiars & Concentration rose as standing armies replaced contractors, and finance and force were fused in venal command & The risk was units held partly as private property, and the checks were mutiny and the fiscal power of estates \\
   444	Secular democracy & Professional forces under civilian command, warrant-bound police and overseen intelligence services & Concentration varies with constitutional structure, and contestability is designed to be high on every component & Surveillance of citizens exposed by the Senate inquiry of 1975 to 1976 is both a capture episode and a check \\
   445	\bottomrule
   446	\end{tabularx}
   447	\end{table}
   448	
   449	\section{Mechanisms, failure modes and checks}
   450	\label{sec:mechanisms}
   451	
   452	\Cref{thm:coercive-power:necessity} requires that violators be sanctioned more than compliers. It says nothing about whom else the apparatus targets. This section shows that the coercive function and its capture are governed by different parameters, states when they nonetheless trade off, derives the main failure modes, and identifies the checks that interrupt them.
   453	
   454	\subsection{Conduct and allegiance}
   455	
   456	Return to the targeting probabilities $\psi(v,y)$ of \cref{def:coercive-power:margins}. In the one-period version of the deterrence lemma, an agent with alignment $y$ faces the margin $d = \Delta^{\mathrm{c}}(y)\mu$, so it violates a rule in $\mathcal{R}^0$ if $\tau > \Delta^{\mathrm{c}}(y)\mu$.
   457	
   458	\begin{proposition}[Separability]
   459	\label{prop:coercive-power:separability}
   460	Fix a magnitude $\mu > 0$ and a temptation distribution $G$. (i) The violation rate of agents with alignment $y$ is $1 - G(\Delta^{\mathrm{c}}(y)\mu)$, which depends on $\psi$ only through the conduct margin $\Delta^{\mathrm{c}}(y)$. (ii) For any common conduct margin $e \in (0,1)$ and any allegiance margin $x \in [0, 1-e]$, there is a targeting function with $\Delta^{\mathrm{c}}(\mathrm{al}) = \Delta^{\mathrm{c}}(\mathrm{op}) = e$ and $\Delta^{\mathrm{a}}(0) = \Delta^{\mathrm{a}}(1) = x$. In particular, the same deterrence of rule violations is compatible with a zero allegiance margin and with a positive one.
   461	\end{proposition}
   462	
   463	\begin{proof}
   464	Part (i) follows from \cref{lem:coercive-power:deterrence} with $d = \Delta^{\mathrm{c}}(y)\mu$, resolving ties toward compliance. For (ii), set $\psi(0,\mathrm{al}) = 0$, $\psi(1,\mathrm{al}) = e$, $\psi(0,\mathrm{op}) = x$ and $\psi(1,\mathrm{op}) = e + x$. All four values lie in $[0,1]$ because $x \le 1 - e$, and the margins are as stated.
   465	\end{proof}
   466	
   467	The proposition is the pillar-level form of the series claim that A does not imply B. Proposition~A, through \cref{thm:coercive-power:necessity}, constrains the conduct margin. A positive allegiance margin is a necessary ingredient of capture in the coercive pillar, and the theorem places no constraint on it. A collective can have an effective coercive pillar with no allegiance margin, and, if it has enough coercive capacity, the same effectiveness with a substantial one. The existence of police tells us nothing about which case obtains; only the margins do.
   468	
   469	A positive allegiance margin is not yet capture. Throughout this paper capture means the source's three-part capture link \citep{largo2026hbs}. A capture link $(i \to j, \pC)$ exists when actor $i$ has discretion over deployment, $j$'s allegiance margin is positive because of that discretion in a way that weakens accountability that would otherwise apply, and material evidence connects the two: for example, records showing that $i$'s orders produced surveillance, arrests or prosecutions of opponents who had broken no rule in $\mathcal{R}^0$, at rates that differ from those of supporters with the same conduct. The comparative section applies this test to each episode it discusses.
   470	
   471	\subsection{Arbitrary sanction and the capacity trade-off}
   472	
   473	The first failure mode occurs when coercion becomes insensitive to conduct within an alignment group. Its consequences are counterintuitive: coercion increases while the enforcement of rules decreases.
   474	
   475	\begin{proposition}[Arbitrary sanction]
   476	\label{prop:coercive-power:arbitrary}
   477	Fix an alignment $y$, hold $\psi(1,y)$ and $\mu$ fixed, and suppose $G$ has a density $g$. As $\psi(0,y)$ rises toward $\psi(1,y)$: (i) the conduct margin $\Delta^{\mathrm{c}}(y)$ falls to zero and the violation rate of the group rises toward the unsanctioned rate $p$; (ii) the expected number of coercive acts per member of the group,
   478	\[
   479	S(y) = \psi(0,y) + \Delta^{\mathrm{c}}(y)\bigl[1 - G(\Delta^{\mathrm{c}}(y)\mu)\bigr],
   480	\]
   481	is non-decreasing in $\psi(0,y)$.
   482	\end{proposition}
   483	
   484	\begin{proof}
   485	(i) $\Delta^{\mathrm{c}}(y) = \psi(1,y) - \psi(0,y)$ is decreasing in $\psi(0,y)$ and equals zero when the two probabilities are equal. The violation rate $1 - G(\Delta^{\mathrm{c}}(y)\mu)$ is non-increasing in $\Delta^{\mathrm{c}}(y)$, so it rises, and at $\Delta^{\mathrm{c}}(y) = 0$ it equals $1 - G(0) = p$. (ii) Write $\psi_0 = \psi(0,y)$ and $D = \psi(1,y) - \psi_0$. A member is targeted with probability $\psi_0$ if it complies and $\psi_0 + D$ if it violates, so $S = \psi_0 + D[1 - G(D\mu)]$. Differentiating in $\psi_0$, with $\partial D/\partial \psi_0 = -1$,
   486	\[
   487	\frac{\partial S}{\partial \psi_0} = 1 - \bigl[1 - G(D\mu)\bigr] + D\mu\, g(D\mu) = G(D\mu) + D\mu\, g(D\mu) \ge 0. \qedhere
   488	\]
   489	\end{proof}
   490	
   491	The proposition explains the source paper's proposal to measure coercive power by discretionary and asymmetric deployment rather than by spending \citep[Section 4]{largo2026hbs}. Arrest counts, prison populations and security budgets can all rise as the coercive apparatus stops responding to conduct. When the group in question is the opposition and $\psi(0,\mathrm{al})$ does not change, raising $\psi(0,\mathrm{op})$ toward $\psi(1,\mathrm{op})$ raises the allegiance margin $\Delta^{\mathrm{a}}(0)$ and lowers the conduct margin $\Delta^{\mathrm{c}}(\mathrm{op})$ at the same time. Targeting opponents without regard to their conduct therefore weakens deterrence among opponents, even though it increases coercion against them.
   492	
   493	Separability shows that an allegiance margin can be added without weakening deterrence, but only by adding coercive capacity. When capacity is fixed, the two margins trade off. Let the alignment groups have masses $n_{\mathrm{al}}, n_{\mathrm{op}} > 0$, and suppose that maintaining the targeting probabilities requires monitoring and enforcement capacity
   494	\[
   495	\Sigma(\psi) = \sum_{y} n_y\bigl[\kappa_1 \psi(1,y) + \kappa_0 \psi(0,y)\bigr] \le \bar{B},
   496	\]
   497	with $\kappa_0, \kappa_1 > 0$: capacity is spent on watching and acting against each status class in each group.
   498	
   499	\begin{proposition}[Capacity trade-off]
   500	\label{prop:coercive-power:capacity}
   501	Suppose the capacity constraint binds at $\psi$, and the apparatus raises $\psi(0,\mathrm{op})$ by $\varepsilon > 0$ without lowering $\psi(0,\mathrm{al})$, while $\bar{B}$ is unchanged. Then $\sum_y n_y \psi(1,y)$ must fall by at least $\kappa_0 n_{\mathrm{op}}\varepsilon/\kappa_1$. Consequently the conduct margin of at least one group falls, and that group's violation rate weakly rises.
   502	\end{proposition}
   503	
   504	\begin{proof}
   505	The new targeting function $\psi'$ must satisfy $\Sigma(\psi') \le \bar{B} = \Sigma(\psi)$. The change in the $\kappa_0$ terms is at least $\kappa_0 n_{\mathrm{op}}\varepsilon$, so the change in $\kappa_1\sum_y n_y\psi(1,y)$ is at most $-\kappa_0 n_{\mathrm{op}}\varepsilon$, which gives the bound. Since $\sum_y n_y \psi(1,y)$ falls, $\psi(1,y)$ falls for some $y$. For that $y$, $\psi(0,y)$ has not fallen, so $\Delta^{\mathrm{c}}(y)$ falls, and by \cref{prop:coercive-power:separability}(i) its violation rate $1 - G(\Delta^{\mathrm{c}}(y)\mu)$ weakly rises.
   506	\end{proof}
   507	
   508	The two propositions together give the paper's claim about allegiance-conditioned coercion its exact scope. Allegiance targeting weakens the enforcement of ordinary rules when coercive capacity is limited, and when opponents are targeted without regard to their conduct. When a regime adds capacity to fund an allegiance margin while keeping its conduct margins, separability says that rule enforcement can survive; what changes is the cost of opposition. Wintrobe's model of the dictator's trade-off between repression and the purchase of loyalty reaches related conclusions by a different route \citep{wintrobe1998}.
   509	
   510	A second failure mode concerns supporters. If $\psi(1,\mathrm{al})$ falls toward $\psi(0,\mathrm{al})$, supporters enjoy impunity: their conduct margin falls and their violation rate rises toward $p$. Allegiance-conditioned enforcement can therefore damage compliance on both sides of the political line. Total coercive activity may rise or fall in this case, depending on the relative size of the two groups and on how much the targeting of opponents increases.
   511	
   512	\subsection{The guardian problem and coup-proofing}
   513	
   514	Term (a) of \cref{prop:coercive-power:second-order} makes the loyalty of provisioned coercers depend on their paymaster, and a coercive apparatus strong enough to protect a ruler is strong enough to remove the ruler. Rulers respond by dividing coercive capacity among several organizations that watch one another. The following comparative static states when they divide more.
   515	
   516	\begin{proposition}[Coup-proofing]
   517	\label{prop:coercive-power:coup-proofing}
   518	A ruler chooses the number $k \in \{1, \dots, K\}$ of independent armed organizations. Let $c(k)$ be the probability of a successful coup, non-increasing in $k$, and $e(k)$ any function giving the loss of external military effectiveness. The ruler minimizes $f(k; r) = r\, c(k) + e(k)$, where $r > 0$ is the expected cost of losing office to a coup relative to the stakes of external effectiveness. If $r' > r$, then the largest minimizer at $r'$ is at least as large as the largest minimizer at $r$.
   519	\end{proposition}
   520	
   521	\begin{proof}
   522	Let $k$ be the largest minimizer at $r$ and $k'$ the largest minimizer at $r'$, and suppose $k' < k$. Optimality gives $f(k; r) \le f(k'; r)$ and $f(k'; r') \le f(k; r')$. Adding the two inequalities and cancelling the $e$ terms yields $(r' - r)\bigl(c(k') - c(k)\bigr) \le 0$. Since $k' < k$ and $c$ is non-increasing, $c(k') \ge c(k)$, and since $r' > r$ the product is non-negative, so it is zero and $c(k') = c(k)$. Then $f(k; r') - f(k'; r') = e(k) - e(k') = f(k; r) - f(k'; r) \le 0$, so $k$ also minimizes $f(\cdot\,; r')$. This contradicts the choice of $k'$ as the largest minimizer at $r'$, since $k > k'$.
   523	\end{proof}
   524	
   525	The proof uses no property of $e$; the effectiveness cost matters for the level of $k$ but not for the direction of the comparative static. The parameter $r$ is the salience of the elite threat: it rises with the probability that the ruler's own armed allies could and would remove the ruler, which can be proxied by recent coup attempts in the polity or its neighbors \citep{powell2011}, and it falls with the stakes of interstate war. The model has one threat parameter and does not represent mass threat. It therefore captures the fragmentation side of Greitens's argument, that elite threats produce fragmented coercive institutions \citep{greitens2016}, but not the prediction that mass threats produce unified and intrusive ones. It is consistent with Quinlivan's account of coup-proofing in Middle Eastern regimes \citep{quinlivan1999} and with the finding of Pilster and B\"ohmelt that coup-proofing has battlefield costs \citep{pilster2011}. It describes the Saudi army and National Guard, the Iranian army and Revolutionary Guard, and the division of Soviet coercion among army, security service and police. In democracies the analogous counterweights are civilian ministries, separate services and judicial oversight. The comparative static would be falsified by evidence that the number and independence of armed organizations are unrelated to measured elite threat once external threat is held constant.
   526	
   527	Coup-proofing raises $k$ but does not raise $Q^{\pC}$. Counterweights protect the ruler from the guardians; they do not protect citizens from the ruler. In a party-state or a dynastic monarchy, all $k$ organizations may answer to the same apex. Then the concentration $H^{\pC}_{(1)}$ among the organizations below the apex falls, while $H^{\pC}$, which attributes their control to the apex under \cref{def:coercive-power:share}, stays high, and so does the integration $C_{\pP\pC}$. This is the reason the source paper requires both $U_t$ and $\Integ_t$ for a strong classification: a measure of dispersion below the apex would miss the concentration above it.
   528	
   529	\subsection{Dependent corps and the outsider strategy}
   530	
   531	Rulers have long tried to solve the guardian problem by recruiting coercers who have no independent social base: foreigners, captives, slaves or men cut off from their families. The Abbasid and Mamluk slave soldiers, the Ottoman kul and the papal Swiss Guard are instances. The following proposition states why the strategy works at first and why it tends to fail later.
   532	
   533	\begin{proposition}[Dependent corps]
   534	\label{prop:coercive-power:outsider}
   535	A corps receives compensation $w_t \le \bar{w}$ per period from a ruler whose fiscal capacity bounds $\bar{w}$. The corps accumulates capacity $Z_t$: arms, offices, property, marriages and local recruitment. The value to the corps of seizing control is $\Gamma(Z_t)$, non-decreasing in $Z_t$, and an attempt costs $\chi > 0$. The corps remains subordinate in period $t$ only if $\sum_{k \ge 0}\delta^k w_{t+k} \ge \Gamma(Z_t) - \chi$. If $Z_t$ is non-decreasing and $\lim_{t\to\infty}\Gamma(Z_t) > \bar{w}/(1-\delta) + \chi$, then there is a finite $T$ such that for all $t \ge T$ the corps is not subordinate, unless the ruler lowers $Z_t$, raises $\chi$, or raises the ceiling $\bar{w}$.
   536	\end{proposition}
   537	
   538	\begin{proof}
   539	The left side of the subordination condition is at most $\bar{w}/(1-\delta)$. Because $\Gamma(Z_t)$ is non-decreasing in $t$ and its limit exceeds $\bar{w}/(1-\delta) + \chi$, there is a finite $T$ with $\Gamma(Z_T) - \chi > \bar{w}/(1-\delta)$, and the inequality persists for all $t \ge T$. The condition can be restored only by changing one of $Z_t$, $\chi$ or $\bar{w}$.
   540	\end{proof}
   541	
   542	The proposition is simple, and its interest lies in what it explains. It treats an attempt as successful; a probability of success below one lowers the expected value of seizure and delays $T$ without changing the logic. Recruiting outsiders lowers $Z_0$: a corps with no kin, land or local allies gains little from seizing power because it cannot rule alone. This is the logic Crone attributed to the adoption of military slavery \citep{crone1980}. Over time the corps acquires exactly the assets that raise $Z_t$. The value of seizing a polity is bounded by what the polity produces, so the threshold condition, not unbounded growth, is what matters: the corps must come to value control more than the most the ruler can pay. The ruler's three countermeasures correspond to the three escape clauses. Rotation of commanders, prohibition of property holding and periodic purges keep $Z_t$ low. Counterweights of the kind analyzed in \cref{prop:coercive-power:coup-proofing} raise the cost $\chi$ of an attempt. Fiscal expansion raises $\bar{w}$. The Mamluks, who became rulers of Egypt and Syria \citep{irwin1986}, and the Janissaries, whose part in the deposition and killing of Osman II in 1622 marked a lasting change in Ottoman politics \citep{tezcan2010}, are the paradigm cases. The proposition also applies to modern forces whose economic holdings grow, since business activity raises $Z_t$ directly. This is the mechanism behind the concern that the economic expansion of Iran's Revolutionary Guard increases its political autonomy \citep{wehrey2009,alfoneh2013}. In democracies the analogous measures are term limits for commanders, prohibitions on military business and civilian control of promotions.
   543	
   544	\subsection{Coercion and production}

2026-10-22T17:09:08.058417Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '545,694p' papers/latex/coercive-power.tex | nl -ba -v545" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   545	\label{sec:cw}
   546	
   547	The pair of coercion and production is the primary responsibility of this Part among the fifteen cross-pillar pairs. The dependencies run in both directions, and the integration coefficient $C_{\pC\pW}$ measures something narrower than either.
   548	
   549	From production to coercion ($\pW \to \pC$), every army and police force consumes labor time. Conscription takes it directly from the producing population as an obligation. Professional forces take it through wages paid from taxes. Slave-soldier systems took it by acquiring people as a resource. The mode of recruitment shapes accountability: a conscript army is drawn from the whole population and depends on its consent, while a professional or outsider force depends on its paymaster. This is a further reason why term (a) of \cref{prop:coercive-power:second-order} carries political consequences.
   550	
   551	From coercion to production ($\pC \to \pW$), sanctions can compel work. The categories must be kept distinct, and this paper uses the bondage spectrum of Part~VI (Definition~2.4). Wage labor and taxation leave lawful mobility and personal ownership with the producer; the sanctions behind them are the general law of contract and of revenue. Serfdom ties the producer to land or lord. Compelled state labor, which includes corv\'ee, labor drafts and penal labor, is compelled by sanction for a term. Chattel slavery makes the person property. Only the last three are forms of bondage, and the coercive pillar is directly engaged in each of them. The Soviet camp system combined penal labor with economic planning on a scale that made coercion a direct input to production \citep{applebaum2003,gregory2003}. The series uses the language of bondage beyond these legal categories only in the disciplined, metaphorical sense of the source paper \citep{largo2026hbs}. Part~VI treats the production side of the pair, including the exit and voice that producers can use against dependence (Part~VI, Definition~2.5).
   552	
   553	A high value of $C_{\pC\pW}$ means that the same coalition commands both the coercive apparatus and the allocation of labor. In the extreme case, the deterrence margin of \cref{def:coercive-power:regime} is applied to failures to work. Proposition~B for this pair requires such integration together with a positive allegiance margin, so that the obligation to work falls more heavily on opponents, and with low contestability. The Gulag combined all three, since the same party-state directed the security organs that filled the camps and the plans that used their labor, and political offenses were among the grounds of confinement \citep{applebaum2003}. Universal conscription in a democracy with high $Q^{\pC}$ involves the dependency $\pW \to \pC$ but neither high integration nor an allegiance margin.
   554	
   555	\subsection{Checks that interrupt transmission}
   556	
   557	The source paper's second proposition holds that effective independent review and voice reduce the probability that attempted capture yields persistent unreviewable outcomes \citep{largo2026hbs}. In the coercive pillar the checks act on the margins directly. Judicial authorization of intrusive measures raises the evidentiary threshold for coercive acts, which lowers $\psi(0,y)$ for everyone and so raises the conduct margin. Independent complaint bodies make a positive allegiance margin visible and therefore costly. Individual liability of agents for unlawful force raises the private cost of arbitrary coercion for the coercers themselves. Protected refusal of unlawful orders introduces a veto at the point of execution: when soldiers or police refuse to fire on peaceful crowds, the allegiance margin is cut off at its source, which is the mechanism that Chenoweth and Stephan and Albrecht and Ohl identify in security-force defection \citep{chenoweth2011,albrecht2016}.
   558	
   559	These checks have small-scale analogues. Ostrom's design principles for long-enduring commons include monitors who are accountable to users and graduated sanctions that begin with small penalties \citep{ostrom1990,ostromdesign2010}. Graduated sanctions keep the magnitude $\mu$ proportional to the violation, which limits the damage when $\psi(0,y)$ is positive by mistake. Accountability of monitors to users is a small-scale version of component (1) of $Q^{\pC}$. The reverse dominance hierarchy of foraging bands is a check of the same kind: the collective holds the sanction and directs it against those who try to concentrate it \citep{boehm1999}. Madison's argument that ambition must be made to counteract ambition is the constitutional statement of the same principle \citep{madison1788}.
   560	
   561	Checks can fail. Each depends on another pillar: judicial authorization on judicial independence (Part~III), complaints and refusal on legitimating beliefs (Part~IV), and appointments on the political pillar (Part~II). Capture of any of these pillars by the coalition that commands coercion removes the corresponding check. This is the mechanism by which high cross-pillar integration $\Integ_t$ turns a concentrated coercive pillar into an unaccountable one, and it is why the coercive pillar cannot be assessed in isolation.
   562	
   563	\section{Measurement and hypotheses}
   564	\label{sec:measurement}
   565	
   566	\subsection{Indicators}
   567	
   568	The source paper rejects military expenditure as a measure of coercive power, and \cref{prop:coercive-power:arbitrary} shows why sanction counts are equally misleading. The objects that matter are the control share, the components of contestability and the two margins. \Cref{tab:indicators} lists indicators for each.
   569	
   570	\begin{table}[!htbp]
   571	\centering
   572	\small
   573	\caption{Indicators for the coercive pillar. Each indicator measures a defined object of \cref{sec:layer} or \cref{sec:mechanisms}; none has been coded for a real polity under a preregistered scheme.}
   574	\label{tab:indicators}
   575	\renewcommand{\arraystretch}{1.15}
   576	\begin{tabularx}{\textwidth}{@{}L{3.0cm}YY@{}}
   577	\toprule
   578	Object & Indicator & Main threat to validity \\
   579	\midrule
   580	Control share $s^{\pC}_i$ and concentrations $H^{\pC}$ and $H^{\pC}_{(1)}$ & Share of heads of coercive organizations whom a single actor can appoint and remove, with the share of their decisions that follow that actor's directives, coded from statutes and records & Formal authority may differ from practice, so appointment records should be checked against actual removals \\
   581	Contestability $Q^{\pC}$ & Scores for the six components of \cref{def:coercive-power:qc}, coded from law and from the reports of oversight bodies & Oversight bodies may exist on paper without access to records or power to compel testimony \\
   582	Conduct margin $\Delta^{\mathrm{c}}(y)$ & Difference in targeting rates between violators and non-violators, measured against an independent record of conduct such as victimization surveys or audits & The apparatus that sanctions also records violations, so official data cannot measure conduct independently \\
   583	Allegiance margin $\Delta^{\mathrm{a}}(v)$ & Difference in targeting rates between opponents and supporters with the same conduct under the reference rules, for example in surveillance, arrest or prosecution & Opponents and supporters may differ in unobserved conduct, which requires matched designs or outcome tests \\
   584	Repression & Standards-based scales coded from human-rights reports, as in Poe and Tate and in Hill and Jones, and V-Dem civil-liberties indicators & Reporting improves where monitoring improves, which can make better-governed states appear more repressive \\
   585	Coups and counterweights & Coup attempts from the Powell and Thyne dataset, and the number of armed organizations outside the regular military chain of command & Counterweights are often secret or nominally civilian \\
   586	Integration $C_{\pF\pC}$ & Share of coercive organizations' revenue from their own business holdings & Holdings are often opaque and require primary documents \\
   587	Dependency $\pC \to \pW$ and integration $C_{\pC\pW}$ & Legal scope of conscription and of forced and penal labor, and the share of output produced under them & Legal categories may not match practice \\
   588	\bottomrule
   589	\end{tabularx}
   590	\end{table}
   591	
   592	The allegiance margin is the hardest object to measure and the most important. Two designs are available. The first compares the treatment of opponents and supporters with matched conduct, as recorded by a source independent of the coercive apparatus: a court that acquits, a victimization survey, or an archive of the targets' own activities. The Senate inquiry of 1975 to 1976 is an example of the third kind, since it compared the surveillance record with the lawful character of the targets' activities \citep{church1976}. The second design adapts the outcome test from the economics of discrimination. Knowles, Persico and Todd showed that if officers maximize successful searches, the rate at which searches find contraband should be equal across groups in the absence of bias \citep{knowles2001}. The analogous test here compares the rate at which coercive acts against opponents and supporters are later upheld by independent review. A systematically lower rate for opponents indicates that opponents are targeted on weaker evidence, which is a positive $\Delta^{\mathrm{a}}(0)$. The test has two known weaknesses. Average rates can differ even without bias if the marginal cases differ across groups, the problem of infra-marginality, so the test is informative only under the conditions that Knowles, Persico and Todd state for equilibrium search behavior. And the independent review may itself be captured, which is the concern of Part~III; the test is only as good as the judicial contestability $Q^{\pJ}$ of the reviewing body. Repression scales \citep{poe1994,hill2014} and V-Dem indicators \citep{coppedge2011} measure the level of coercion against citizens but do not separate the two margins, so they are useful as outcomes rather than as measures of capture. Coup data \citep{powell2011} measure the guardian problem directly.
   593	
   594	\subsection{Hypotheses with falsifiers}
   595	
   596	The hypotheses below refine the source paper's generic hypotheses H1 to H6 for the coercive pillar; the parent hypothesis is given in brackets. Each states the result that would count against it.
   597	
   598	\begin{description}
   599	\item[HC1 (threat environment; H3).] Rulers who face greater elite threat build fragmented and loyalty-based coercive institutions; rulers who face mass threat build unified and intrusive ones \citep{greitens2016}. The first half is motivated by \cref{prop:coercive-power:coup-proofing}; the second half is not modeled here. Falsifier: the number and independence of armed organizations are unrelated to measured elite threat once external threat is controlled.
   600	\item[HC2 (coup-proofing trade-off; H6).] Coup-proofing lowers coup success and also lowers military effectiveness \citep{quinlivan1999,pilster2011}. Falsifier: higher counterbalancing shows no association with battlefield performance in comparable conflicts.
   601	\item[HC3 (security-force defection; H5).] The cohesion, composition and professionalism of security forces predict whether they defect or repress during mass unrest \citep{bellin2012,albrecht2016,chenoweth2011}. Falsifier: these characteristics show no association with defection across episodes.
   602	\item[HC4 (fiscal basis; H3).] Coercive organizations financed by taxation of a broad population face more contestation than those financed by resource rents or foreign transfers \citep{tilly1990,karaman2013}. The hypothesis is motivated by term (a) of \cref{prop:coercive-power:second-order}, which ties the loyalty of coercers to their provisioning, but the proposition does not model contestation. Falsifier: the source of financing is unrelated to $Q^{\pC}$.
   603	\item[HC5 (dependent corps; H2).] Corps recruited for dependence become political actors as their capacity grows, unless rulers rotate, disperse or replace them, raise the cost of an attempt, or raise pay \citep{crone1980,pipes1981}. This is the empirical counterpart of \cref{prop:coercive-power:outsider}. Falsifier: outsider corps whose holdings and offices grow remain subordinate without such countermeasures.
   604	\item[HC6 (democracy and repression; H1).] Democracy and judicial independence reduce repression \citep{poe1994,hill2014}. Falsifier: no effect once civil conflict is controlled. Rejali's evidence on torture in democracies is a boundary case that the hypothesis must accommodate \citep{rejali2007}.
   605	\item[HC7 (integration of finance and force; H2).] Business activity by coercive organizations raises $C_{\pF\pC}$ and lowers coercive contestability. Falsifier: military business holdings are unrelated to $Q^{\pC}$. Rival explanation: such holdings supply public goods or substitute for an inadequate budget.
   606	\item[HC8 (checks; H1 and H4).] Independent complaint mechanisms and judicial authorization lower the allegiance margin. Falsifier: the margin is unchanged after such reforms are introduced. As the source paper warns, reforms can raise reported abuses by making them visible, so reporting effects must be separated from changes in behavior \citep{largo2026hbs}.
   607	\item[HC9 (volume and compliance; H1).] When coercive acts against opponents rise while independently measured compliance with the reference rules falls among opponents, and neither changes among supporters with matched conduct, the allegiance margin is rising and the conduct margin among opponents is falling. The comparison with supporters is needed because a temptation shock, such as a crime wave, also raises both violations and coercive acts with no allegiance margin at all; it affects both groups. This is the pattern \cref{prop:coercive-power:arbitrary} predicts when opponents are targeted without regard to conduct. Falsifier: in documented episodes of politically selective repression, opponents' compliance with the reference rules does not fall relative to supporters'.
   608	\item[HC10 (separability; H6).] Across polities, measured conduct margins and measured allegiance margins are weakly correlated: the absolute correlation is below a preregistered threshold, for example 0.5, and polities with a conduct margin above the sample median include some with an allegiance margin indistinguishable from zero. This is the empirical content of \cref{prop:coercive-power:separability} and of the claim that A does not imply B. Falsifier: the two margins are so strongly correlated that effective rule enforcement is never observed without a positive allegiance margin, which would suggest that capture accompanies coercion structurally.
   609	\end{description}
   610	
   611	HC10 is the hypothesis whose failure would most damage this paper's argument. The separability proposition shows that the margins can vary independently, but if they never do in practice, the distinction between necessity and capture would be logical rather than empirical.
   612	
   613	\section{Revelation 13 as typological image}
   614	\label{sec:revelation}
   615	
   616	The series reads Revelation typologically. It does not identify the beast, the mark or Babylon with any present government, party, technology, person, religion or institution. Futurist readings that make such identifications have a long history of failure \citep{boyer1992,fuller1995,mcginn1998}, and historicist readings that identified the beast with particular churches belong to the history of polemic \citep{kovacs2004}. In the preterist reading, which supplies the historical anchor, the first beast is Roman imperial power and the setting is the imperial cult of the cities of Asia Minor \citep{bauckham1993,friesen2001,koester2014}. In the typological reading the series adopts, the beast is a recurring pattern of power that claims ultimate loyalty \citep{bauckham1993,wink1992}. The use of the image here is an interpretive claim of this project, not a settled exegetical result.
   617	
   618	Revelation 13 is saturated with coercion. The first beast is given authority to make war: ``it was given unto him to make war with the saints, and to overcome them: and power was given him over all kindreds, and tongues, and nations'' (Rev.~13:7, KJV). Its worshippers ask, ``Who is like unto the beast? who is able to make war with him?'' (13:4). The second beast exercises the authority of the first and causes the earth to worship it, and it brings an image to life that should ``cause that as many as would not worship the image of the beast should be killed'' (13:15). The chapter ends with the mark, without which ``no man might buy or sell'' (13:17). Kraybill has read these passages against the economic life of the province, in which participation in trade was entangled with the imperial cult \citep{kraybill1996}.
   619	
   620	The coercive content of 13:15 has a precise structure in the terms of \cref{def:coercive-power:margins}. Inside the image's own order, refusal to worship is the violation. But that rule is a rule whose content is allegiance, which is exactly the kind of rule excluded from the reference set $\mathcal{R}^0$. Measured against allegiance-neutral rules, the death sanction of 13:15 is conditioned entirely on allegiance and not at all on conduct, and the enactment of the rule is itself an image of rule-making capture. The economic exclusion of 13:16 to 17 has the same structure: the cost falls on those without the mark, whatever they have done. The text's image of the beast is, among other things, an image of a coercive apparatus whose conduct margin has been displaced by an allegiance margin.
   621	
   622	Another canonical text, Paul's letter to the Romans, describes the coercive function with the opposite conditioning. Romans 13 says that ``rulers are not a terror to good works, but to the evil,'' and that the ruler ``beareth not the sword in vain: for he is the minister of God, a revenger to execute wrath upon him that doeth evil'' (Rom.~13:3 to 4, KJV). The sword in Romans 13 is conditioned on conduct: it falls on the one who does evil. The sword in Revelation 13 is conditioned on worship: it falls on the one who will not bow. Readers have long asked how the two chapters fit together. Yoder read Romans 13 as a call to be subject to authorities whose power is itself ordered under God, not as an endorsement of whatever those authorities do \citep{yoder1972}, a reading that leaves room for Revelation's judgment on authority that demands worship. In the framework of this paper the chapters describe the same function under different parameters. Romans 13 describes a sanction regime with a positive conduct margin and no allegiance margin. \Cref{thm:coercive-power:necessity} shows that every persistent collective needs the first property; the second is what distinguishes accountable coercion from captured coercion. Revelation 13 describes a regime in which the allegiance margin has displaced the conduct margin, and \cref{prop:coercive-power:arbitrary,prop:coercive-power:capacity} show why such a regime weakens the enforcement of the ordinary rules it claims to protect. The reading is consistent with the series distinction between Proposition~A, the universal function, and Proposition~B, its contingent capture.
   623	
   624	The same chapter addresses those who suffer coercion: ``He that leadeth into captivity shall go into captivity: he that killeth with the sword must be killed with the sword. Here is the patience and the faith of the saints'' (13:10). The KJV wording follows one textual tradition. The verse echoes Jeremiah 15:2, its wording varies among manuscripts, and many modern editions and commentators read it as a call to the faithful to accept captivity and death rather than as a statement that the coercer will meet the same fate; the commentaries discuss the problem at this verse \citep{aune1998b,koester2014}. Because the reading is uncertain, this paper draws no institutional inference from it. On either reading the verse rules out armed resistance by the faithful, which places the response it commends in endurance and witness rather than in counter-coercion.
   625	
   626	Revelation 17 supplies a closer image of the guardian problem of \cref{sec:mechanisms}. The ten kings ``have one mind, and shall give their power and strength unto the beast'' (17:13), and yet ``the ten horns which thou sawest upon the beast, these shall hate the whore, and shall make her desolate and naked'' (17:16). Allies who lend their force to a power can turn it against the power they served. Read typologically, the passage is an image of the dependent-corps dynamic of \cref{prop:coercive-power:outsider}, in which those who supply coercion come to hold it on their own account. This too is the project's interpretive claim, not an exegetical result. Collins argued that the Apocalypse addressed a perceived crisis and offered its readers a form of catharsis \citep{collins1984}, and Thompson questioned whether the Domitianic period saw the systematic persecution that older readings assumed \citep{thompson1990}. On either reading the text's concern is not the existence of the sword but its direction: whom it strikes, and why.
   627	
   628	\section{Objections and scope conditions}
   629	\label{sec:objections}
   630	
   631	The first objection is that the necessity theorem is trivial, since any cost can be called a sanction. The definition blocks this. A sanction must respond to an observed or alleged violation, and the deterrence margin is the difference in continuation payoffs between compliance and violation. Both are observable. The theorem can fail, and \cref{sec:counter} states the observation that would refute it, together with the requirement that temptation be measured independently of sanction practices so that no compliant collective can be reclassified after the fact. Its content lies in Ax5 and the bridge assumption, which are empirical claims about temptations, and in the conclusion that the sanction regime must shift at least $p - \theta$ of probability mass toward compliance.
   632	
   633	The second objection is Hobbesian: order requires a sovereign with a monopoly of force, so the distributed sanctions of stateless societies are a primitive stage rather than a functional equivalent. The evidence of \cref{tab:hardcases} is against this. Distributed sanctions sustained order in many societies over long periods, and the theorem requires a positive margin, not a concentrated holder. The objection has more force at scale, and \cref{prop:coercive-power:second-order} explains why: as collectives grow, term (d) weakens and coercion must be provisioned or legitimated. That is a reason for specialization, not for concentration without accountability.
   634	
   635	The third objection comes from the opposite direction. Clastres, Graeber and Wengrow, and anarchist anthropology more generally, argue that hierarchy is not inevitable and that many societies deliberately prevented the emergence of coercive authority \citep{clastres1987,graeber2021}. The paper agrees about hierarchy and disagrees about coercion. The societies they describe sanction those who try to command; they do not lack sanctions. Their achievement is a coercive pillar with $H^{\pC}$ near $1/n$ and contestability near one, which is the clearest empirical evidence that Proposition~B is contingent.
   636	
   637	The fourth objection is Marxian: coercion in class societies serves the ruling class, so the distinction between rule enforcement and capture is ideological. The framework accommodates the claim as a hypothesis about the allegiance margin. If coercion is applied more heavily to one class for the same conduct, or if the rules themselves were written to protect one class's property, the first case shows up as a positive allegiance margin indexed by class, and the second belongs to the analysis of rule-making in Part~II. In both cases the claim becomes measurable. What the framework rejects is the inference from the existence of police to the existence of class capture, which is the inference from A to B.
   638	
   639	The fifth objection is the public-goods objection: concentrated coercion provides security, which benefits everyone, so it should not be treated with suspicion. The paper accepts the premise. The source paper's fourth proposition and hypothesis H6 state that concentration with high-quality review can coexist with competent services and low arbitrary sanctioning \citep{largo2026hbs}, and the social democracies of \cref{sec:socdem} are the leading illustration. The margins framework is designed to distinguish this case from capture rather than to presume either.
   640	
   641	Five scope conditions limit the results. The capacity trade-off of \cref{prop:coercive-power:capacity} rests on a linear capacity constraint, which is an assumption about the technology of enforcement rather than a derived result. The model treats a single rule with a binary violation decision, while real polities enforce many rules of different gravity, and the tolerance $\theta$ differs among them. Equilibria in repeated games are typically multiple, so the theorem establishes that some sanction regime is necessary without predicting which one arises. The analysis concerns enforcement inside a polity; war between polities enters only through the guardian problem and the fiscal basis of coercion. And the conduct margin can be measured only with an independent record of conduct, which is often unavailable precisely where capture is most likely.
   642	
   643	\section{Conclusion}
   644	\label{sec:conclusion}
   645	
   646	Every governance system settles who enforces its rules, because when members are sometimes tempted to break rules, compliance requires that violators' prospects fall because of what they did. The answer need not be a police force. Gossip, ridicule, ostracism and coalition action satisfy the deterrence lemma as well as armies do, and the societies that seem to lack coercion are those in which the collective holds it and directs it against concentration. The function is universal; its institutional form varies.
   647	
   648	Capture in the coercive pillar requires a change in what coercion responds to. The conduct margin measures enforcement of rules, the allegiance margin measures enforcement of loyalty, and the two are separable: necessity constrains the first and is silent about the second. They trade off when coercive capacity is limited, and when opponents are targeted without regard to their conduct; under those conditions the volume of coercion rises while compliance with ordinary rules falls. That is why spending and arrest counts mismeasure coercive power, and why the contrast between Romans 13 and Revelation 13 concerns the direction of the sword rather than its existence.
   649	
   650	The comparison of six regime types shows the same function distributed in different ways: through private producers and civilian control in market-capitalist societies, party organs in communist states, ombudsmen, parliamentary oversight and conscription in social democracies, counterbalanced and dependent corps in Islamic states, venal and contracted command in Catholic monarchies, and constitutional oversight in secular democracies. What remains uncertain is the size of the two margins in any of them. Measuring the allegiance margin, against an independent record of conduct, is the task on which the empirical claims of this paper depend.
   651	
   652	\begin{thebibliography}{200}
   653	\small
   654	\setlength{\itemsep}{2pt}
   655	
   656	\bibitem[\'Agoston(2005)]{agoston2005}
   657	\'Agoston, G\'abor (2005). \emph{Guns for the Sultan: Military Power and the Weapons Industry in the Ottoman Empire}. Cambridge University Press.
   658	
   659	\bibitem[\'Agoston(2014)]{agoston2014}
   660	\'Agoston, G\'abor (2014). Firearms and Military Adaptation: The Ottomans and the European Military Revolution, 1450-1800. \emph{Journal of World History} 25(1):85-124. doi:10.1353/jwh.2014.0005.
   661	
   662	\bibitem[Al-Rasheed(2002)]{alrasheed2002}
   663	Al-Rasheed, Madawi (2002). \emph{A History of Saudi Arabia}. Cambridge University Press. doi:10.1017/cbo9780511993510.
   664	
   665	\bibitem[Albrecht and Ohl(2016)]{albrecht2016}
   666	Albrecht, Holger and Ohl, Dorothy (2016). Exit, Resistance, Loyalty: Military Behavior during Unrest in Authoritarian Regimes. \emph{Perspectives on Politics} 14(1):38-52. doi:10.1017/S1537592715003217.
   667	
   668	\bibitem[Alfoneh(2013)]{alfoneh2013}
   669	Alfoneh, Ali (2013). \emph{Iran Unveiled: How the Revolutionary Guards Is Transforming Iran from Theocracy into Military Dictatorship}. AEI Press.
   670	
   671	\bibitem[Alvarez(2011)]{alvarez2011}
   672	Alvarez, David (2011). \emph{The Pope's Soldiers: A Military History of the Modern Vatican}. University Press of Kansas.
   673	
   674	\bibitem[Applebaum(2003)]{applebaum2003}
   675	Applebaum, Anne (2003). \emph{Gulag: A History}. Doubleday.
   676	
   677	\bibitem[Arjomand(1988)]{arjomand1988}
   678	Arjomand, Said Amir (1988). \emph{The Turban for the Crown: The Islamic Revolution in Iran}. Oxford University Press.
   679	
   680	\bibitem[Aune(1998)]{aune1998b}
   681	Aune, David E. (1998). \emph{Revelation 6-16}. Word Biblical Commentary 52B. Thomas Nelson.
   682	
   683	\bibitem[Axelrod(1984)]{axelrod1984}
   684	Axelrod, Robert (1984). \emph{The Evolution of Cooperation}. Basic Books.
   685	
   686	\bibitem[Bauckham(1993)]{bauckham1993}
   687	Bauckham, Richard (1993). \emph{The Theology of the Book of Revelation}. Cambridge University Press. doi:10.1017/cbo9780511819858.
   688	
   689	\bibitem[Becker(1968)]{becker1968}
   690	Becker, Gary S. (1968). Crime and Punishment: An Economic Approach. \emph{Journal of Political Economy} 76(2):169-217. doi:10.1086/259394.
   691	
   692	\bibitem[Bellin(2004)]{bellin2004}
   693	Bellin, Eva (2004). The Robustness of Authoritarianism in the Middle East: Exceptionalism in Comparative Perspective. \emph{Comparative Politics} 36(2):139-157. doi:10.2307/4150140.
   694	

2026-10-22T17:09:10.068268Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '695,769p' papers/latex/coercive-power.tex | nl -ba -v695" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   695	\bibitem[Bellin(2012)]{bellin2012}
   696	Bellin, Eva (2012). Reconsidering the Robustness of Authoritarianism in the Middle East: Lessons from the Arab Spring. \emph{Comparative Politics} 44(2):127-149. doi:10.5129/001041512798838021.
   697	
   698	\bibitem[Boehm(1999)]{boehm1999}
   699	Boehm, Christopher (1999). \emph{Hierarchy in the Forest: The Evolution of Egalitarian Behavior}. Harvard University Press. doi:10.2307/j.ctvjf9xr4.
   700	
   701	\bibitem[Boehm(2012)]{boehm2012}
   702	Boehm, Christopher (2012). \emph{Moral Origins: The Evolution of Virtue, Altruism, and Shame}. Basic Books.
   703	
   704	\bibitem[Born and Caparini(2007)]{born2007}
   705	Born, Hans and Caparini, Marina (eds.) (2007). \emph{Democratic Control of Intelligence Services: Containing Rogue Elephants}. Ashgate.
   706	
   707	\bibitem[Boyer(1992)]{boyer1992}
   708	Boyer, Paul (1992). \emph{When Time Shall Be No More: Prophecy Belief in Modern American Culture}. Harvard University Press (Belknap). doi:10.2307/jj.41480279.
   709	
   710	\bibitem[Bruce(2010)]{bruce2010}
   711	Bruce, Gary (2010). \emph{The Firm: The Inside Story of the Stasi}. Oxford University Press.
   712	
   713	\bibitem[Buchta(2000)]{buchta2000}
   714	Buchta, Wilfried (2000). \emph{Who Rules Iran? The Structure of Power in the Islamic Republic}. Washington Institute for Near East Policy and Konrad Adenauer Stiftung.
   715	
   716	\bibitem[Chenoweth and Stephan(2011)]{chenoweth2011}
   717	Chenoweth, Erica and Stephan, Maria J. (2011). \emph{Why Civil Resistance Works: The Strategic Logic of Nonviolent Conflict}. Columbia University Press.
   718	
   719	\bibitem[Clastres(1987)]{clastres1987}
   720	Clastres, Pierre (1987). \emph{Society against the State: Essays in Political Anthropology}. Translated by Robert Hurley. Zone Books. doi:10.2307/j.ctv1595m3p.
   721	
   722	\bibitem[Collins(1984)]{collins1984}
   723	Collins, Adela Yarbro (1984). \emph{Crisis and Catharsis: The Power of the Apocalypse}. Westminster Press.
   724	
   725	\bibitem[Colton(1979)]{colton1979}
   726	Colton, Timothy J. (1979). \emph{Commissars, Commanders, and Civilian Authority: The Structure of Soviet Military Politics}. Harvard University Press. doi:10.4159/harvard.9780674497443.
   727	
   728	\bibitem[Conquest(1990)]{conquest1990}
   729	Conquest, Robert (1990). \emph{The Great Terror: A Reassessment}. Oxford University Press.
   730	
   731	\bibitem[Coppedge et~al.(2011)]{coppedge2011}
   732	Coppedge, Michael and Gerring, John and Altman, David and Bernhard, Michael and Fish, Steven and Hicken, Allen and Kroenig, Matthew and Lindberg, Staffan I. and McMann, Kelly and Paxton, Pamela and Semetko, Holli A. and Skaaning, Svend-Erik and Staton, Jeffrey and Teorell, Jan (2011). Conceptualizing and Measuring Democracy: A New Approach. \emph{Perspectives on Politics} 9(2):247-267. doi:10.1017/S1537592711000880.
   733	
   734	\bibitem[Cordesman(2003)]{cordesman2003}
   735	Cordesman, Anthony H. (2003). \emph{Saudi Arabia Enters the Twenty-First Century: The Military and International Security Dimensions}. Praeger.
   736	
   737	\bibitem[Cox et~al.(2010)]{cox2010}
   738	Cox, Michael and Arnold, Gwen and Villamayor Tomas, Sergio (2010). A Review of Design Principles for Community-based Natural Resource Management. \emph{Ecology and Society} 15(4), article 38. doi:10.5751/ES-03704-150438.
   739	
   740	\bibitem[Crone(1980)]{crone1980}
   741	Crone, Patricia (1980). \emph{Slaves on Horses: The Evolution of the Islamic Polity}. Cambridge University Press. doi:10.1017/cbo9780511563508.
   742	
   743	\bibitem[Davenport(2007)]{davenport2007}
   744	Davenport, Christian (2007). State Repression and Political Order. \emph{Annual Review of Political Science} 10:1-23. doi:10.1146/annurev.polisci.10.101405.143216.
   745	
   746	\bibitem[Edwards and Ogilvie(2012)]{edwards2012}
   747	Edwards, Jeremy and Ogilvie, Sheilagh (2012). Contract Enforcement, Institutions, and Social Capital: The Maghribi Traders Reappraised. \emph{Economic History Review} 65(2):421-444. doi:10.1111/j.1468-0289.2011.00635.x.
   748	
   749	\bibitem[Eisenhower(1961)]{eisenhower1961}
   750	Eisenhower, Dwight D. (1961). \emph{Farewell Radio and Television Address to the American People, 17 January 1961}. Public Papers of the Presidents. \url{https://www.eisenhowerlibrary.gov/research/online-documents/farewell-address}.
   751	
   752	\bibitem[Ellickson(1991)]{ellickson1991}
   753	Ellickson, Robert C. (1991). \emph{Order without Law: How Neighbors Settle Disputes}. Harvard University Press. doi:10.4159/9780674036437.
   754	
   755	\bibitem[Elliott(1963)]{elliott1963}
   756	Elliott, J. H. (1963). \emph{Imperial Spain 1469-1716}. Edward Arnold.
   757	
   758	\bibitem[Elster(1979)]{elster1979}
   759	Elster, Jon (1979). \emph{Ulysses and the Sirens: Studies in Rationality and Irrationality}. Cambridge University Press.
   760	
   761	\bibitem[Elster(1983)]{elster1983}
   762	Elster, Jon (1983). \emph{Explaining Technical Change: A Case Study in the Philosophy of Science}. Cambridge University Press.
   763	
   764	\bibitem[Ertman(1997)]{ertman1997}
   765	Ertman, Thomas (1997). \emph{Birth of the Leviathan: Building States and Regimes in Medieval and Early Modern Europe}. Cambridge University Press. doi:10.1017/cbo9780511529016.
   766	
   767	\bibitem[Evans-Pritchard(1940)]{evanspritchard1940}
   768	Evans-Pritchard, E. E. (1940). \emph{The Nuer: A Description of the Modes of Livelihood and Political Institutions of a Nilotic People}. Clarendon Press.
   769	

2026-10-22T17:09:19.358323Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '330,337p' papers/latex/coercive-power.tex | nl -ba -v330" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   330	\subsection{Policing, punishment and legitimacy}
   331	
   332	Within consolidated states, the main question about ordinary enforcement is why people comply. Tyler found that people obey the law more because they judge the authorities legitimate and the procedures fair than because they fear sanctions \citep{tyler1990}, and Jackson and colleagues found the same pattern in survey data on policing \citep{jackson2012}. These findings do not contradict \cref{thm:coercive-power:necessity}. They show that legitimation lowers the temptation distribution and supplies the motive for cooperation with enforcement, which in the present model shifts $G$ and strengthens term (b). Foucault traced the shift from spectacular punishment to the disciplinary prison and the surveillance it made possible \citep{foucault1977}. Pratt documented the comparatively low imprisonment rates and humane prison conditions of the Nordic countries and traced them to egalitarian welfare states, while warning that populist pressures could erode them \citep{pratt2008a,pratt2008b}.
   333	
   334	\subsection{Contribution}
   335	
   336	The literatures above mostly study either the necessity of order (from Hobbes to the economics of deterrence) or the dangers of coercive power (from civil-military relations to repression), and they rarely connect the two formally. The deterrence literature from \citet{becker1968} onward models the conduct margin and assumes enforcement is impartial. The repression literature studies the allegiance margin and largely takes the conduct margin for granted. This Part treats both as properties of a single sanction-probability function, which shows that the necessity of coercion and its capture are logically separate and empirically distinguishable. It also places the evidence of six regime types on a common scale, so that the comparison asks how each type distributes a function that all of them share.
   337	

2026-10-22T17:09:21.585090Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
2026-10-22T17:09:31.223416Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
codex
A file-local structural check hit the workspace’s read-only restriction because the shell tried to create a temporary heredoc. No file was changed; I’m rerunning the same check as a direct one-liner.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "ruby -e 's=File.read(ARGV[0]); labels=s.scan(/\\\\label\\{(["'^}]+)'"\\}/).flatten; refs=s.scan(/\\\\(?:[Cc]ref|eqref|ref)\\{(["'^}]+)'"\\}/).flatten.flat_map{|x|x.split(\",\")}; bibs=s.scan(/\\\\bibitem(?:\\[["'^'"\\]]*\\])?\\{(["'^}]+)'"\\}/).flatten; cites=s.scan(/\\\\cite(?:t|p)?(?:\\[["'^'"\\]]*\\])?\\{(["'^}]+)'"\\}/).flatten.flat_map{|x|x.split(\",\")}; eb=s.scan(/\\\\begin\\{(["'^}]+)'"\\}/).flatten.tally; ee=s.scan(/\\\\end\\{(["'^}]+)'"\\}/).flatten.tally; p duplicate_labels: labels.tally.select{|_,v|v>1}; p undefined_refs:(refs-labels).uniq.sort; p unreferenced_labels:(labels-refs).uniq.sort; p duplicate_bibkeys:bibs.tally.select{|_,v|v>1}; p missing_bibitems:(cites-bibs).uniq.sort; p uncited_bibitems:(bibs-cites).uniq.sort; p environment_mismatches:(eb.keys|ee.keys).select{|k|eb[k]"'!=ee[k]}.to_h{|k|[k,[eb[k],ee[k]]]}'"' papers/latex/coercive-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
{duplicate_labels: {}}
{undefined_refs: []}
{unreferenced_labels: ["ass:bridge", "cor:coercive-power:scale", "prop:coercive-power:minimal-form", "sec:communist", "sec:conclusion", "sec:intro", "sec:literature", "sec:market", "sec:minimal", "sec:objections", "sec:secular"]}
{duplicate_bibkeys: {}}
{missing_bibitems: []}
{uncited_bibitems: []}
{environment_mismatches: {}}

2026-10-22T17:09:37.916466Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "LC_ALL=C rg -n '["'^'"\\x00-\\x7F]' papers/latex/coercive-power.tex || true
rg -n '\\\\(includegraphics|input|include|bibliography|addbibresource)|\\\\href\\{|\\\\url\\{' papers/latex/coercive-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
59:  \small \texttt{matthew@yonedaai.com} \quad \url{https://yonedaai.com}}
750:Eisenhower, Dwight D. (1961). \emph{Farewell Radio and Television Address to the American People, 17 January 1961}. Public Papers of the Presidents. \url{https://www.eisenhowerlibrary.gov/research/online-documents/farewell-address}.
810:Greif, Avner (1993). Contract Enforceability and Economic Institutions in Early Trade: The Maghribi Traders' Coalition. \emph{American Economic Review} 83(3):525-548. \url{https://www.jstor.org/stable/2117532}.
906:Madison, James (1788). \emph{The Federalist No. 51: The Structure of the Government Must Furnish the Proper Checks and Balances}. Independent Journal, 6 February 1788. \url{https://avalon.law.yale.edu/18th_century/fed51.asp}.
920:\bibitem[{EOS Committee}(2026)]{eos2026} Norwegian Parliamentary Oversight Committee on Intelligence and Security Services (EOS Committee) (2026). History of the EOS Committee. \url{https://eos-utvalget.no/en/home/about-the-eos-committee/history}. Accessed 22 October 2026.
968:Riksdagens ombudsm\"an (Parliamentary Ombudsmen of Sweden) (2026). History of the Parliamentary Ombudsmen. \url{https://www.jo.se/en/about-jo/history/}. Accessed 22 October 2026.
973:\bibitem[{S\"akerhetstj\"anstkommissionen}(2002)]{sou2002} S\"akerhetstj\"anstkommissionen (2002). \emph{Rikets s\"akerhet och den personliga integriteten: De svenska s\"akerhetstj\"ansternas f\"orfattningsskyddande verksamhet sedan \aa{}r 1945}. SOU 2002:87. Stockholm: Justitiedepartementet. \url{https://regeringen.se/rattsliga-dokument/statens-offentliga-utredningar/2002/01/sou-200287/}.
987:\bibitem[{Swedish Government}(1999)]{dir1999} Swedish Government (1999). Kommission f\"or granskning av de svenska s\"akerhetstj\"ansternas f\"orfattningsskyddande verksamhet. Committee directive Dir. 1999:26, 25 March 1999. \url{https://data.riksdagen.se/dokument/GNB126}.
1007:\bibitem[{Commission on Industrial Relations}(1915)]{cir1915} United States Commission on Industrial Relations (1915). \emph{Final Report of the Commission on Industrial Relations}. Washington, DC. \url{https://archive.org/details/finalreportofcom00unitiala}.

2026-10-22T17:09:45.214644Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "rg -n 'doi:' papers/latex/coercive-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
660:\'Agoston, G\'abor (2014). Firearms and Military Adaptation: The Ottomans and the European Military Revolution, 1450-1800. \emph{Journal of World History} 25(1):85-124. doi:10.1353/jwh.2014.0005.
663:Al-Rasheed, Madawi (2002). \emph{A History of Saudi Arabia}. Cambridge University Press. doi:10.1017/cbo9780511993510.
666:Albrecht, Holger and Ohl, Dorothy (2016). Exit, Resistance, Loyalty: Military Behavior during Unrest in Authoritarian Regimes. \emph{Perspectives on Politics} 14(1):38-52. doi:10.1017/S1537592715003217.
687:Bauckham, Richard (1993). \emph{The Theology of the Book of Revelation}. Cambridge University Press. doi:10.1017/cbo9780511819858.
690:Becker, Gary S. (1968). Crime and Punishment: An Economic Approach. \emph{Journal of Political Economy} 76(2):169-217. doi:10.1086/259394.
693:Bellin, Eva (2004). The Robustness of Authoritarianism in the Middle East: Exceptionalism in Comparative Perspective. \emph{Comparative Politics} 36(2):139-157. doi:10.2307/4150140.
696:Bellin, Eva (2012). Reconsidering the Robustness of Authoritarianism in the Middle East: Lessons from the Arab Spring. \emph{Comparative Politics} 44(2):127-149. doi:10.5129/001041512798838021.
699:Boehm, Christopher (1999). \emph{Hierarchy in the Forest: The Evolution of Egalitarian Behavior}. Harvard University Press. doi:10.2307/j.ctvjf9xr4.
708:Boyer, Paul (1992). \emph{When Time Shall Be No More: Prophecy Belief in Modern American Culture}. Harvard University Press (Belknap). doi:10.2307/jj.41480279.
720:Clastres, Pierre (1987). \emph{Society against the State: Essays in Political Anthropology}. Translated by Robert Hurley. Zone Books. doi:10.2307/j.ctv1595m3p.
726:Colton, Timothy J. (1979). \emph{Commissars, Commanders, and Civilian Authority: The Structure of Soviet Military Politics}. Harvard University Press. doi:10.4159/harvard.9780674497443.
732:Coppedge, Michael and Gerring, John and Altman, David and Bernhard, Michael and Fish, Steven and Hicken, Allen and Kroenig, Matthew and Lindberg, Staffan I. and McMann, Kelly and Paxton, Pamela and Semetko, Holli A. and Skaaning, Svend-Erik and Staton, Jeffrey and Teorell, Jan (2011). Conceptualizing and Measuring Democracy: A New Approach. \emph{Perspectives on Politics} 9(2):247-267. doi:10.1017/S1537592711000880.
738:Cox, Michael and Arnold, Gwen and Villamayor Tomas, Sergio (2010). A Review of Design Principles for Community-based Natural Resource Management. \emph{Ecology and Society} 15(4), article 38. doi:10.5751/ES-03704-150438.
741:Crone, Patricia (1980). \emph{Slaves on Horses: The Evolution of the Islamic Polity}. Cambridge University Press. doi:10.1017/cbo9780511563508.
744:Davenport, Christian (2007). State Repression and Political Order. \emph{Annual Review of Political Science} 10:1-23. doi:10.1146/annurev.polisci.10.101405.143216.
747:Edwards, Jeremy and Ogilvie, Sheilagh (2012). Contract Enforcement, Institutions, and Social Capital: The Maghribi Traders Reappraised. \emph{Economic History Review} 65(2):421-444. doi:10.1111/j.1468-0289.2011.00635.x.
753:Ellickson, Robert C. (1991). \emph{Order without Law: How Neighbors Settle Disputes}. Harvard University Press. doi:10.4159/9780674036437.
765:Ertman, Thomas (1997). \emph{Birth of the Leviathan: Building States and Regimes in Medieval and Early Modern Europe}. Cambridge University Press. doi:10.1017/cbo9780511529016.
771:Feaver, Peter D. (1999). Civil-Military Relations. \emph{Annual Review of Political Science} 2:211-241. doi:10.1146/annurev.polisci.2.1.211.
774:Feaver, Peter D. (2003). \emph{Armed Servants: Agency, Oversight, and Civil-Military Relations}. Harvard University Press. doi:10.4159/9780674036772.
777:Fehr, Ernst and G\"achter, Simon (2002). Altruistic Punishment in Humans. \emph{Nature} 415:137-140. doi:10.1038/415137a.
786:Friesen, Steven J. (2001). \emph{Imperial Cults and the Apocalypse of John: Reading Revelation in the Ruins}. Oxford University Press. doi:10.1093/0195131533.001.0001.
789:Fuller, Robert C. (1995). \emph{Naming the Antichrist: The History of an American Obsession}. Oxford University Press. doi:10.1093/acprof:oso/9780195109795.001.0001.
795:Gerschewski, Johannes (2013). The Three Pillars of Stability: Legitimation, Repression, and Co-optation in Autocratic Regimes. \emph{Democratization} 20(1):13-38. doi:10.1080/13510347.2013.738860.
798:Getty, J. Arch (1985). \emph{Origins of the Great Purges: The Soviet Communist Party Reconsidered, 1933-1938}. Cambridge University Press. doi:10.1017/cbo9780511572616.
801:Gieseke, Jens (2014). \emph{The History of the Stasi: East Germany's Secret Police, 1945-1990}. Berghahn Books. doi:10.3167/9781782382546.
813:Greitens, Sheena Chestnut (2016). \emph{Dictators and Their Secret Police: Coercive Institutions and State Violence}. Cambridge University Press. doi:10.1017/cbo9781316489031.
816:Hedlund, Erik (2011). Civil-Military Control over the Swedish Military Profession. \emph{Armed Forces \& Society} 39(1):135-157. Published online 2011; print issue 2013. doi:10.1177/0095327X11426256.
819:Hegghammer, Thomas and Lacroix, St\'ephane (2007). Rejectionist Islamism in Saudi Arabia: The Story of Juhayman al-'Utaybi Revisited. \emph{International Journal of Middle East Studies} 39(1):103-122. doi:10.1017/s0020743807002553.
825:Hill, Daniel W. and Jones, Zachary M. (2014). An Empirical Evaluation of Explanations for State Repression. \emph{American Political Science Review} 108(3):661-687. doi:10.1017/S0003055414000306.
828:Hobbes, Thomas (1651). \emph{Leviathan}. Edited by Richard Tuck. Cambridge University Press, 1996. doi:10.1017/CBO9780511808166.
831:Huntington, Samuel P. (1957). \emph{The Soldier and the State: The Theory and Politics of Civil-Military Relations}. Harvard University Press. doi:10.2307/j.ctvjf9wx3.
840:Jackson, Jonathan and Bradford, Ben and Hough, Mike and Myhill, Andy and Quinton, Paul and Tyler, Tom R. (2012). Why Do People Comply with the Law? Legitimacy and the Influence of Legal Institutions. \emph{British Journal of Criminology} 52(6):1051-1071. doi:10.1093/bjc/azs032.
849:Karaman, K. K{\i}van\c{c} and Pamuk, \c{S}evket (2013). Different Paths to the Modern State in Europe: The Interaction between Warfare, Economic Structure, and Political Regime. \emph{American Political Science Review} 107(3):603-626. doi:10.1017/S0003055413000312.
855:Kelly, Robert L. (1995). \emph{The Foraging Spectrum: Diversity in Hunter-Gatherer Lifeways}. Smithsonian Institution Press. doi:10.2307/j.ctv2sx9gc9.
861:Knight, Amy (1996). \emph{Spies without Cloaks: The KGB's Successors}. Princeton University Press. doi:10.2307/j.ctt15sk83q.
864:Knowles, John and Persico, Nicola and Todd, Petra (2001). Racial Bias in Motor Vehicle Searches: Theory and Evidence. \emph{Journal of Political Economy} 109(1):203-229. doi:10.1086/318603.
870:Koester, Craig R. (2014). \emph{Revelation: A New Translation with Introduction and Commentary}. Yale University Press (Anchor Yale Bible 38A). doi:10.12987/9780300211030.
873:Kohn, Richard H. (1997). How Democracies Control the Military. \emph{Journal of Democracy} 8(4):140-153. doi:10.1353/jod.1997.0060.
876:Kornai, J\'anos (1992). \emph{The Socialist System: The Political Economy of Communism}. Princeton University Press. doi:10.2307/j.ctv1ddczdr.
879:Kovacs, Judith and Rowland, Christopher (2004). \emph{Revelation: The Apocalypse of Jesus Christ}. Blackwell (Blackwell Bible Commentaries). doi:10.1002/9780470773512.
888:Kuran, Timur (1991). Now Out of Never: The Element of Surprise in the East European Revolution of 1989. \emph{World Politics} 44(1):7-48. doi:10.2307/2010422.
903:Lynn, John A. (1997). \emph{Giant of the Grand Si\`ecle: The French Army, 1610-1715}. Cambridge University Press. doi:10.1017/cbo9780511572548.
909:Mann, Michael (1984). The Autonomous Power of the State: Its Origins, Mechanisms and Results. \emph{European Journal of Sociology} 25(2):185-213. doi:10.1017/S0003975600004239.
912:Marshall, Lorna (1976). \emph{The !Kung of Nyae Nyae}. Harvard University Press. doi:10.4159/harvard.9780674180574.
918:North, Douglass C. and Wallis, John Joseph and Weingast, Barry R. (2009). \emph{Violence and Social Orders: A Conceptual Framework for Interpreting Recorded Human History}. Cambridge University Press. doi:10.1017/CBO9780511575839.
923:Olson, Mancur (1965). \emph{The Logic of Collective Action: Public Goods and the Theory of Groups}. Harvard University Press. doi:10.4159/9780674041660.
926:Ostrom, Elinor (1990). \emph{Governing the Commons: The Evolution of Institutions for Collective Action}. Cambridge University Press. doi:10.1017/CBO9780511807763.
929:Ostrom, Elinor (2010). Beyond Markets and States: Polycentric Governance of Complex Economic Systems. \emph{American Economic Review} 100(3):641-672. doi:10.1257/aer.100.3.641.
938:Parrott, David (2012). \emph{The Business of War: Military Enterprise and Military Revolution in Early Modern Europe}. Cambridge University Press. doi:10.1017/cbo9781139023337.
941:Perlmutter, Amos (1969). The Praetorian State and the Praetorian Army: Toward a Taxonomy of Civil-Military Relations in Developing Polities. \emph{Comparative Politics} 1(3):382-404. doi:10.2307/421446.
944:Pilster, Ulrich and B\"ohmelt, Tobias (2011). Coup-Proofing and Military Effectiveness in Interstate Wars, 1967-99. \emph{Conflict Management and Peace Science} 28(4):331-350. doi:10.1177/0738894211413062.
950:Poe, Steven C. and Tate, C. Neal (1994). Repression of Human Rights to Personal Integrity in the 1980s: A Global Analysis. \emph{American Political Science Review} 88(4):853-872. doi:10.2307/2082712.
953:Powell, Jonathan M. and Thyne, Clayton L. (2011). Global Instances of Coups from 1950 to 2010: A New Dataset. \emph{Journal of Peace Research} 48(2):249-259. doi:10.1177/0022343310397436.
956:Pratt, John (2008a). Scandinavian Exceptionalism in an Era of Penal Excess. Part I: The Nature and Roots of Scandinavian Exceptionalism. \emph{British Journal of Criminology} 48(2):119-137. doi:10.1093/bjc/azm072.
959:Pratt, John (2008b). Scandinavian Exceptionalism in an Era of Penal Excess. Part II: Does Scandinavian Exceptionalism Have a Future? \emph{British Journal of Criminology} 48(3):275-292. doi:10.1093/bjc/azm073.
962:Quinlivan, James T. (1999). Coup-proofing: Its Practice and Consequences in the Middle East. \emph{International Security} 24(2):131-165. doi:10.1162/016228899560202.
965:Rejali, Darius (2007). \emph{Torture and Democracy}. Princeton University Press. doi:10.1515/9781400830879.
971:Rowlands, Guy (2002). \emph{The Dynastic State and the Army under Louis XIV: Royal Service and Private Interest, 1661-1701}. Cambridge University Press. doi:10.1017/cbo9780511496882.
976:Scoggins, Suzanne E. and O'Brien, Kevin J. (2016). China's Unhappy Police. \emph{Asian Survey} 56(2):225-242. doi:10.1525/as.2016.56.2.225.
979:Shambaugh, David (2002). \emph{Modernizing China's Military: Progress, Problems, and Prospects}. University of California Press. doi:10.1525/9780520938106.
982:Slater, Dan (2010). \emph{Ordering Power: Contentious Politics and Authoritarian Leviathans in Southeast Asia}. Cambridge University Press. doi:10.1017/cbo9780511760891.
985:Svolik, Milan W. (2012). \emph{The Politics of Authoritarian Rule}. Cambridge University Press. doi:10.1017/CBO9781139176040.
996:Thompson, Leonard L. (1990). \emph{The Book of Revelation: Apocalypse and Empire}. Oxford University Press. doi:10.1093/oso/9780195055511.001.0001.
999:Tilly, Charles (1985). War Making and State Making as Organized Crime. In Peter B. Evans, Dietrich Rueschemeyer and Theda Skocpol (eds.), \emph{Bringing the State Back In}. Cambridge University Press. doi:10.1017/cbo9780511628283.008.
1005:Tyler, Tom R. (1990). \emph{Why People Obey the Law}. Yale University Press. doi:10.1515/9781400828609.
1015:Weber, Max (1978). \emph{Economy and Society: An Outline of Interpretive Sociology}. University of California Press. doi:10.4159/9780674240827.
1021:Wiessner, Polly (2005). Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity? \emph{Human Nature} 16(2):115-145. doi:10.1007/s12110-005-1000-9.
1024:Wink, Walter (1992). \emph{Engaging the Powers: Discernment and Resistance in a World of Domination}. Fortress Press. doi:10.2307/j.ctt1tm7j16.
1027:Wintrobe, Ronald (1998). \emph{The Political Economy of Dictatorship}. Cambridge University Press. doi:10.1017/cbo9781139174916.
1030:Woodburn, James (1982). Egalitarian Societies. \emph{Man (N.S.)} 17(3):431-451. doi:10.2307/2801707.

2026-10-22T17:09:59.533648Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "rg -n '\\\\begin\\{(theorem|proposition|lemma|corollary|definition|assumption|remark)\\}' papers/latex/coercive-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
98:\begin{definition}[Coercive act, sanction and sanction function]
105:\begin{definition}[Coercive control share]
112:\begin{definition}[Coercive contestability]
125:\begin{definition}[Sanction regime and deterrence margin]
137:\begin{definition}[Conduct and allegiance margins]
164:\begin{assumption}[Ax5, defection, formal version]
171:\begin{assumption}[Bridge]
180:\begin{lemma}[Deterrence]
191:\begin{theorem}[Necessity of the sanction function]
209:\begin{corollary}[Magnitude]
222:\begin{proposition}[Second-order enforcement]
235:\begin{corollary}[Costly sanctions at scale]
251:\begin{proposition}[Minimal form]
458:\begin{proposition}[Separability]
475:\begin{proposition}[Arbitrary sanction]
499:\begin{proposition}[Capacity trade-off]
516:\begin{proposition}[Coup-proofing]
533:\begin{proposition}[Dependent corps]

2026-10-22T17:10:08.405828Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "rg -n '[0-9]-[0-9]' papers/latex/coercive-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
660:\'Agoston, G\'abor (2014). Firearms and Military Adaptation: The Ottomans and the European Military Revolution, 1450-1800. \emph{Journal of World History} 25(1):85-124. doi:10.1353/jwh.2014.0005.
666:Albrecht, Holger and Ohl, Dorothy (2016). Exit, Resistance, Loyalty: Military Behavior during Unrest in Authoritarian Regimes. \emph{Perspectives on Politics} 14(1):38-52. doi:10.1017/S1537592715003217.
681:Aune, David E. (1998). \emph{Revelation 6-16}. Word Biblical Commentary 52B. Thomas Nelson.
690:Becker, Gary S. (1968). Crime and Punishment: An Economic Approach. \emph{Journal of Political Economy} 76(2):169-217. doi:10.1086/259394.
693:Bellin, Eva (2004). The Robustness of Authoritarianism in the Middle East: Exceptionalism in Comparative Perspective. \emph{Comparative Politics} 36(2):139-157. doi:10.2307/4150140.
696:Bellin, Eva (2012). Reconsidering the Robustness of Authoritarianism in the Middle East: Lessons from the Arab Spring. \emph{Comparative Politics} 44(2):127-149. doi:10.5129/001041512798838021.
732:Coppedge, Michael and Gerring, John and Altman, David and Bernhard, Michael and Fish, Steven and Hicken, Allen and Kroenig, Matthew and Lindberg, Staffan I. and McMann, Kelly and Paxton, Pamela and Semetko, Holli A. and Skaaning, Svend-Erik and Staton, Jeffrey and Teorell, Jan (2011). Conceptualizing and Measuring Democracy: A New Approach. \emph{Perspectives on Politics} 9(2):247-267. doi:10.1017/S1537592711000880.
738:Cox, Michael and Arnold, Gwen and Villamayor Tomas, Sergio (2010). A Review of Design Principles for Community-based Natural Resource Management. \emph{Ecology and Society} 15(4), article 38. doi:10.5751/ES-03704-150438.
744:Davenport, Christian (2007). State Repression and Political Order. \emph{Annual Review of Political Science} 10:1-23. doi:10.1146/annurev.polisci.10.101405.143216.
747:Edwards, Jeremy and Ogilvie, Sheilagh (2012). Contract Enforcement, Institutions, and Social Capital: The Maghribi Traders Reappraised. \emph{Economic History Review} 65(2):421-444. doi:10.1111/j.1468-0289.2011.00635.x.
756:Elliott, J. H. (1963). \emph{Imperial Spain 1469-1716}. Edward Arnold.
771:Feaver, Peter D. (1999). Civil-Military Relations. \emph{Annual Review of Political Science} 2:211-241. doi:10.1146/annurev.polisci.2.1.211.
777:Fehr, Ernst and G\"achter, Simon (2002). Altruistic Punishment in Humans. \emph{Nature} 415:137-140. doi:10.1038/415137a.
795:Gerschewski, Johannes (2013). The Three Pillars of Stability: Legitimation, Repression, and Co-optation in Autocratic Regimes. \emph{Democratization} 20(1):13-38. doi:10.1080/13510347.2013.738860.
798:Getty, J. Arch (1985). \emph{Origins of the Great Purges: The Soviet Communist Party Reconsidered, 1933-1938}. Cambridge University Press. doi:10.1017/cbo9780511572616.
801:Gieseke, Jens (2014). \emph{The History of the Stasi: East Germany's Secret Police, 1945-1990}. Berghahn Books. doi:10.3167/9781782382546.
810:Greif, Avner (1993). Contract Enforceability and Economic Institutions in Early Trade: The Maghribi Traders' Coalition. \emph{American Economic Review} 83(3):525-548. \url{https://www.jstor.org/stable/2117532}.
816:Hedlund, Erik (2011). Civil-Military Control over the Swedish Military Profession. \emph{Armed Forces \& Society} 39(1):135-157. Published online 2011; print issue 2013. doi:10.1177/0095327X11426256.
819:Hegghammer, Thomas and Lacroix, St\'ephane (2007). Rejectionist Islamism in Saudi Arabia: The Story of Juhayman al-'Utaybi Revisited. \emph{International Journal of Middle East Studies} 39(1):103-122. doi:10.1017/s0020743807002553.
825:Hill, Daniel W. and Jones, Zachary M. (2014). An Empirical Evaluation of Explanations for State Repression. \emph{American Political Science Review} 108(3):661-687. doi:10.1017/S0003055414000306.
837:Irwin, Robert (1986). \emph{The Middle East in the Middle Ages: The Early Mamluk Sultanate 1250-1382}. Southern Illinois University Press.
840:Jackson, Jonathan and Bradford, Ben and Hough, Mike and Myhill, Andy and Quinton, Paul and Tyler, Tom R. (2012). Why Do People Comply with the Law? Legitimacy and the Influence of Legal Institutions. \emph{British Journal of Criminology} 52(6):1051-1071. doi:10.1093/bjc/azs032.
849:Karaman, K. K{\i}van\c{c} and Pamuk, \c{S}evket (2013). Different Paths to the Modern State in Europe: The Interaction between Warfare, Economic Structure, and Political Regime. \emph{American Political Science Review} 107(3):603-626. doi:10.1017/S0003055413000312.
864:Knowles, John and Persico, Nicola and Todd, Petra (2001). Racial Bias in Motor Vehicle Searches: Theory and Evidence. \emph{Journal of Political Economy} 109(1):203-229. doi:10.1086/318603.
873:Kohn, Richard H. (1997). How Democracies Control the Military. \emph{Journal of Democracy} 8(4):140-153. doi:10.1353/jod.1997.0060.
885:Kunt, I. Metin (1983). \emph{The Sultan's Servants: The Transformation of Ottoman Provincial Government, 1550-1650}. Columbia University Press.
888:Kuran, Timur (1991). Now Out of Never: The Element of Surprise in the East European Revolution of 1989. \emph{World Politics} 44(1):7-48. doi:10.2307/2010422.
903:Lynn, John A. (1997). \emph{Giant of the Grand Si\`ecle: The French Army, 1610-1715}. Cambridge University Press. doi:10.1017/cbo9780511572548.
909:Mann, Michael (1984). The Autonomous Power of the State: Its Origins, Mechanisms and Results. \emph{European Journal of Sociology} 25(2):185-213. doi:10.1017/S0003975600004239.
929:Ostrom, Elinor (2010). Beyond Markets and States: Polycentric Governance of Complex Economic Systems. \emph{American Economic Review} 100(3):641-672. doi:10.1257/aer.100.3.641.
932:Parker, Geoffrey (1972). \emph{The Army of Flanders and the Spanish Road, 1567-1659}. Cambridge University Press.
935:Parker, Geoffrey (1988). \emph{The Military Revolution: Military Innovation and the Rise of the West, 1500-1800}. Cambridge University Press.
941:Perlmutter, Amos (1969). The Praetorian State and the Praetorian Army: Toward a Taxonomy of Civil-Military Relations in Developing Polities. \emph{Comparative Politics} 1(3):382-404. doi:10.2307/421446.
944:Pilster, Ulrich and B\"ohmelt, Tobias (2011). Coup-Proofing and Military Effectiveness in Interstate Wars, 1967-99. \emph{Conflict Management and Peace Science} 28(4):331-350. doi:10.1177/0738894211413062.
950:Poe, Steven C. and Tate, C. Neal (1994). Repression of Human Rights to Personal Integrity in the 1980s: A Global Analysis. \emph{American Political Science Review} 88(4):853-872. doi:10.2307/2082712.
953:Powell, Jonathan M. and Thyne, Clayton L. (2011). Global Instances of Coups from 1950 to 2010: A New Dataset. \emph{Journal of Peace Research} 48(2):249-259. doi:10.1177/0022343310397436.
956:Pratt, John (2008a). Scandinavian Exceptionalism in an Era of Penal Excess. Part I: The Nature and Roots of Scandinavian Exceptionalism. \emph{British Journal of Criminology} 48(2):119-137. doi:10.1093/bjc/azm072.
959:Pratt, John (2008b). Scandinavian Exceptionalism in an Era of Penal Excess. Part II: Does Scandinavian Exceptionalism Have a Future? \emph{British Journal of Criminology} 48(3):275-292. doi:10.1093/bjc/azm073.
962:Quinlivan, James T. (1999). Coup-proofing: Its Practice and Consequences in the Middle East. \emph{International Security} 24(2):131-165. doi:10.1162/016228899560202.
971:Rowlands, Guy (2002). \emph{The Dynastic State and the Army under Louis XIV: Royal Service and Private Interest, 1661-1701}. Cambridge University Press. doi:10.1017/cbo9780511496882.
976:Scoggins, Suzanne E. and O'Brien, Kevin J. (2016). China's Unhappy Police. \emph{Asian Survey} 56(2):225-242. doi:10.1525/as.2016.56.2.225.
993:Thompson, I. A. A. (1976). \emph{War and Government in Habsburg Spain, 1560-1620}. Athlone Press.
1002:Tilly, Charles (1990). \emph{Coercion, Capital, and European States, AD 990-1990}. Blackwell.
1009:\bibitem[{United States Senate}(1976)]{church1976} United States Senate, Select Committee to Study Governmental Operations with Respect to Intelligence Activities (1976). \emph{Intelligence Activities and the Rights of Americans}. Final Report, Book II, S. Rep. No. 94-755. U.S. Government Printing Office.
1021:Wiessner, Polly (2005). Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity? \emph{Human Nature} 16(2):115-145. doi:10.1007/s12110-005-1000-9.
1030:Woodburn, James (1982). Egalitarian Societies. \emph{Man (N.S.)} 17(3):431-451. doi:10.2307/2801707.

2026-10-22T17:10:22.064465Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "ruby -e 's=File.read(ARGV[0]); clean=s.lines.map{|l| l.sub(/(?<"'!'"\\\\)%.*"'$/," ")}.join; braces=clean.gsub(/'"\\\\[{}]/,\"\"); puts \"brace_balance=#{braces.count(\"{\")-braces.count(\"}\")}\"; bad=clean.lines.each_with_index.select{|l,i| l.gsub(/\\\\\\"'$/ , "").count("$").odd?}.map{|_,i|i+1}; p odd_dollar_lines:bad; stack=[]; errors=[]; clean.to_enum(:scan,/'"\\\\(begin|end)\\{(["'^}]+)'"\\}/).each{m=Regexp.last_match; if m[1]==\"begin\"; stack << [m[2], clean[0...m.begin(0)].count(\"\\n\")+1]; else; x=stack.pop; errors << [m[2],x,clean[0...m.begin(0)].count(\"\\n\")+1] if "'!x || x[0]!=m[2]; end}; p nesting_errors:errors; p unclosed_environments:stack'"' papers/latex/coercive-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
brace_balance=0
{odd_dollar_lines: []}
{nesting_errors: []}
{unclosed_environments: []}

2026-10-22T17:10:46.395778Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "rg -n '(?<"'!'"\\\\)&' papers/latex/coercive-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 exited 2 in 0ms:
rg: regex parse error:
    (?:(?<!\\)&)
       ^^^^
error: look-around, including look-ahead and look-behind, is not supported

Consider enabling PCRE2 with the --pcre2 flag, which can handle backreferences
and look-around.

2026-10-22T17:11:00.245620Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "rg --pcre2 -n '(?<"'!'"\\\\)&' papers/latex/coercive-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
276:Case & Documented sanction practice & Strongest counter-reading and reply \\
278:Nuer \citep{evanspritchard1940} & Feud and the threat of retaliation by agnatic kin, settled by cattle compensation through the leopard-skin chief as mediator. & The leopard-skin chief has no power to compel. The sanction is held by kin groups, not by the mediator, so the function is present and the office is absent. \\
279:Ju/'hoansi \citep{lee2013,marshall1976,wiessner2005} & Teasing, criticism, gossip and avoidance, with talk about norm violations recorded in camp conversations, and lethal violence in rare extreme cases. & This is the case most often cited as lacking hierarchy. The absence of an office is real, but the sanctions are frequent and documented. \\
280:Amazonian societies \citep{clastres1987} & A chief who tries to command is abandoned or, in Clastres's reports, killed. & Clastres argues that these societies prevent power from separating from society. That supports the claim that concentration is contingent, while the group itself sanctions the chief. \\
281:Foraging bands \citep{boehm1999,boehm2012} & Coalitions of subordinates use ridicule, disobedience, ostracism, exile and execution against would-be dominants. & Boehm calls the result a reverse dominance hierarchy. Egalitarianism is produced by sanctions rather than by their absence. \\
282:Immediate-return societies \citep{woodburn1982} & Leveling mechanisms such as obligatory sharing, mockery and avoidance of anyone who claims authority. & Disputes are often resolved by moving away. Leaving costs the violator cooperation, which is a sanction when the violator values it. \\
283:Commons \citep{ostrom1990,ostromdesign2010,cox2010} & Monitoring by users or accountable monitors, and graduated sanctions for those who break the rules. & Commons are often cited as order without a state. Ostrom's own design principles include monitoring and graduated sanctions. \\
437:Regime type & Principal holders of the function & Concentration, contestability and strongest integration & Documented capture episode or risk, and check \\
439:Market-capitalist & Public police and militaries under elected civilians, with private producers of weapons and security services & Command of the military is concentrated, policing is dispersed, and the distinctive integration is between finance and coercion & Employer-paid deputies and militia in industrial disputes were documented in 1915, and a federal commission exposed the practice \\
440:Communist party-state & Party-controlled security organs, armies with political officers, and police & Command is concentrated at the party apex with internal division among organs, contestability from outside the party is low, and the strongest integration is with political appointment & The terror of the late 1930s was arbitrary and possibly also capture, and party supremacy prevented military takeover \\
441:Social democracy & National police and conscript or professional armies under parliamentary control & Concentration is moderate to high, contestability is high through ombudsmen and courts, and conscription makes coercion depend on universal service & Political surveillance by the security services was exposed by official inquiries, which led to standing parliamentary oversight \\
442:Islamic states & Caliphal armies, slave-soldier corps, dynastic guards and revolutionary guards & Rulers counterbalance separate forces, and integration with legitimation and, in Iran, with finance is strong & Mamluk rule and the regicide of 1622 show corps becoming principals, and counterbalancing protected rulers more than subjects \\
443:Catholic monarchies & Royal armies with venal officers, contracted companies, papal forces and Inquisition familiars & Concentration rose as standing armies replaced contractors, and finance and force were fused in venal command & The risk was units held partly as private property, and the checks were mutiny and the fiscal power of estates \\
444:Secular democracy & Professional forces under civilian command, warrant-bound police and overseen intelligence services & Concentration varies with constitutional structure, and contestability is designed to be high on every component & Surveillance of citizens exposed by the Senate inquiry of 1975 to 1976 is both a capture episode and a check \\
578:Object & Indicator & Main threat to validity \\
580:Control share $s^{\pC}_i$ and concentrations $H^{\pC}$ and $H^{\pC}_{(1)}$ & Share of heads of coercive organizations whom a single actor can appoint and remove, with the share of their decisions that follow that actor's directives, coded from statutes and records & Formal authority may differ from practice, so appointment records should be checked against actual removals \\
581:Contestability $Q^{\pC}$ & Scores for the six components of \cref{def:coercive-power:qc}, coded from law and from the reports of oversight bodies & Oversight bodies may exist on paper without access to records or power to compel testimony \\
582:Conduct margin $\Delta^{\mathrm{c}}(y)$ & Difference in targeting rates between violators and non-violators, measured against an independent record of conduct such as victimization surveys or audits & The apparatus that sanctions also records violations, so official data cannot measure conduct independently \\
583:Allegiance margin $\Delta^{\mathrm{a}}(v)$ & Difference in targeting rates between opponents and supporters with the same conduct under the reference rules, for example in surveillance, arrest or prosecution & Opponents and supporters may differ in unobserved conduct, which requires matched designs or outcome tests \\
584:Repression & Standards-based scales coded from human-rights reports, as in Poe and Tate and in Hill and Jones, and V-Dem civil-liberties indicators & Reporting improves where monitoring improves, which can make better-governed states appear more repressive \\
585:Coups and counterweights & Coup attempts from the Powell and Thyne dataset, and the number of armed organizations outside the regular military chain of command & Counterweights are often secret or nominally civilian \\
586:Integration $C_{\pF\pC}$ & Share of coercive organizations' revenue from their own business holdings & Holdings are often opaque and require primary documents \\
587:Dependency $\pC \to \pW$ and integration $C_{\pC\pW}$ & Legal scope of conscription and of forced and penal labor, and the share of output produced under them & Legal categories may not match practice \\

2026-10-22T17:11:02.381884Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
codex
Source-only review found two formatting issues. No missing packages, malformed environments, unmatched braces, undefined references/citations, or duplicate labels/keys were found.

1. **Incorrect typography for numeric ranges.** Lines 660, 666, 681, 690, 693, 696, 732, 744, 747, 756, 771, 777, 795, 798, 801, 810, 816, 819, 825, 837, 840, 849, 864, 873, 885, 888, 903, 909, 929, 932, 935, 941, 944, 950, 953, 956, 959, 962, 971, 976, 993, 1002, 1021, and 1030 use a single hyphen for page, year, volume, or chapter ranges. In LaTeX these render as hyphens rather than en dashes. Replace, for example, `85-124` with `85--124` and `1450-1800` with `1450--1800`. Preserve hyphens inside DOI strings and the report number `94-755` on line 1009.

2. **DOIs are inconsistently formatted and not linked.** The DOI-bearing entries on lines 660, 663, 666, 687, 690, 693, 696, 699, 708, 720, 726, 732, 738, 741, 744, 747, 753, 765, 771, 774, 777, 786, 789, 795, 798, 801, 813, 816, 819, 825, 828, 831, 840, 849, 855, 861, 864, 870, 873, 876, 879, 888, 903, 909, 912, 918, 923, 926, 929, 938, 941, 944, 950, 953, 956, 959, 962, 965, 971, 976, 979, 982, 985, 996, 999, 1005, 1015, 1021, 1024, 1027, and 1030 use plain `doi:...` text, while ordinary URLs use `\url{...}`. This also gives TeX fewer safe breakpoints and can contribute to overfull bibliography lines. Replace each with `\url{https://doi.org/<DOI>}`; `hyperref` is already loaded, so no additional package is needed.

Actual overfull/underfull warnings cannot be confirmed without compiling and inspecting a log, which would exceed the requested single-file read-only scope.

VERDICT: NEEDS_FIX
hook: Stop
hook: Stop
hook: Stop Completed
hook: Stop Completed
tokens used
81,869
Source-only review found two formatting issues. No missing packages, malformed environments, unmatched braces, undefined references/citations, or duplicate labels/keys were found.

1. **Incorrect typography for numeric ranges.** Lines 660, 666, 681, 690, 693, 696, 732, 744, 747, 756, 771, 777, 795, 798, 801, 810, 816, 819, 825, 837, 840, 849, 864, 873, 885, 888, 903, 909, 929, 932, 935, 941, 944, 950, 953, 956, 959, 962, 971, 976, 993, 1002, 1021, and 1030 use a single hyphen for page, year, volume, or chapter ranges. In LaTeX these render as hyphens rather than en dashes. Replace, for example, `85-124` with `85--124` and `1450-1800` with `1450--1800`. Preserve hyphens inside DOI strings and the report number `94-755` on line 1009.

2. **DOIs are inconsistently formatted and not linked.** The DOI-bearing entries on lines 660, 663, 666, 687, 690, 693, 696, 699, 708, 720, 726, 732, 738, 741, 744, 747, 753, 765, 771, 774, 777, 786, 789, 795, 798, 801, 813, 816, 819, 825, 828, 831, 840, 849, 855, 861, 864, 870, 873, 876, 879, 888, 903, 909, 912, 918, 923, 926, 929, 938, 941, 944, 950, 953, 956, 959, 962, 965, 971, 976, 979, 982, 985, 996, 999, 1005, 1015, 1021, 1024, 1027, and 1030 use plain `doi:...` text, while ordinary URLs use `\url{...}`. This also gives TeX fewer safe breakpoints and can contribute to overfull bibliography lines. Replace each with `\url{https://doi.org/<DOI>}`; `hyperref` is already loaded, so no additional package is needed.

Actual overfull/underfull warnings cannot be confirmed without compiling and inspecting a log, which would exceed the requested single-file read-only scope.

VERDICT: NEEDS_FIX
