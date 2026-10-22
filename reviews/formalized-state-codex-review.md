---
reviewer: codex (OpenAI) gpt-5.6-sol
type: formatting
paper: formalized-state
round: 3
date: 2026-10-22T19:04:31Z
---
Reading additional input from stdin...
2026-10-22T19:04:32.287841Z ERROR codex_models_manager::cache: failed to load models cache: missing field `base_instructions` at line 139 column 5
OpenAI Codex v0.145.0
--------
workdir: /Users/mlong/Documents/Development/the-beast-system
model: gpt-5.6-sol
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a16500-2cb8-76e0-9960-30f2d7504a1b
--------
user
Read ONLY the files papers/latex/formalized-state.tex and papers/latex/formalized-state.log (do not explore other files). Review the paper for LaTeX formatting issues: compilation errors or warnings, missing packages, broken or wrong cross-references, inconsistent styling, overfull or underfull boxes, table and figure layout, bibliography formatting, citation consistency. House rules you must NOT flag: no em or en dashes anywhere (ranges written with 'to', hyphens in bibliography page ranges), the mandated preamble skeleton (11pt article, hmargin 1.25in, packages as given), the series section order. The appendix is intentionally short at this stage. List each issue with its line number and a concrete fix, briefly. End with exactly one line: VERDICT: PASS or VERDICT: NEEDS_FIX.
warning: Under-development features enabled: chronicle. Under-development features are incomplete and may behave unpredictably. To suppress this warning, set `suppress_unstable_features_warning = true` in /Users/mlong/.codex/config.toml.
warning: clamping SessionEnd hook timeout to 3s in /Users/mlong/.codex/plugins/cache/openai-codex/codex/1.0.6/hooks/hooks.json
2026-10-22T19:04:33.640340Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server linear: OAuth token refresh failed: Server returned error response: invalid_grant: Grant not found
2026-10-22T19:04:34.675292Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server resend: OAuth token refresh failed: Server returned error response: invalid_grant: Refresh token has been revoked
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
2026-10-22T19:04:40.437073Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
codex
I’ll inspect exactly those two files, correlate source lines with the compile log, and keep the review limited to actionable LaTeX-formatting issues.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'wc -l papers/latex/formalized-state.tex papers/latex/formalized-state.log && nl -ba papers/latex/formalized-state.tex && nl -ba papers/latex/formalized-state.log' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
    1304 papers/latex/formalized-state.tex
    1045 papers/latex/formalized-state.log
    2349 total
     1	\documentclass[11pt,letterpaper]{article}
     2	
     3	\usepackage[T1]{fontenc}
     4	\usepackage{lmodern}
     5	\usepackage{microtype}
     6	\usepackage[hmargin=1.25in,vmargin=1in]{geometry}
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
    21	\setlength{\bibsep}{2pt plus 1pt}
    22	\usepackage{enumitem}
    23	\usepackage[hidelinks]{hyperref}
    24	\usepackage[capitalise]{cleveref}
    25	
    26	\definecolor{grokgray}{RGB}{110,110,110}
    27	\AddToHook{shipout/background}{%
    28	  \ifnum\value{page}=1
    29	    \put(30pt,-0.5\paperheight){\makebox(0,0){\rotatebox{90}{\footnotesize\sffamily\color{grokgray}%
    30	      GrokRxiv:2026.10.formalized-state\quad [\,econ.GN\,]\quad 22 Oct 2026}}}%
    31	  \fi
    32	}
    33	
    34	\newtheorem{theorem}{Theorem}[section]
    35	\newtheorem{proposition}[theorem]{Proposition}
    36	\newtheorem{lemma}[theorem]{Lemma}
    37	\newtheorem{corollary}[theorem]{Corollary}
    38	\theoremstyle{definition}
    39	\newtheorem{definition}[theorem]{Definition}
    40	\newtheorem{assumption}[theorem]{Assumption}
    41	\theoremstyle{remark}
    42	\newtheorem{remark}[theorem]{Remark}
    43	\AddToHook{env/proposition/begin}{\crefalias{theorem}{proposition}}
    44	\AddToHook{env/lemma/begin}{\crefalias{theorem}{lemma}}
    45	\AddToHook{env/corollary/begin}{\crefalias{theorem}{corollary}}
    46	\AddToHook{env/definition/begin}{\crefalias{theorem}{definition}}
    47	\AddToHook{env/assumption/begin}{\crefalias{theorem}{assumption}}
    48	\AddToHook{env/remark/begin}{\crefalias{theorem}{remark}}
    49	\crefname{assumption}{assumption}{assumptions}
    50	\Crefname{assumption}{Assumption}{Assumptions}
    51	
    52	\newcommand{\pF}{\mathsf{F}}
    53	\newcommand{\pP}{\mathsf{P}}
    54	\newcommand{\pJ}{\mathsf{J}}
    55	\newcommand{\pI}{\mathsf{I}}
    56	\newcommand{\pC}{\mathsf{C}}
    57	\newcommand{\pW}{\mathsf{W}}
    58	\newcommand{\Mset}{\mathcal{M}}
    59	\newcommand{\Integ}{\mathcal{I}}
    60	\newcommand{\Struct}{\mathsf{Struct}}
    61	\newcommand{\Inter}{\mathsf{Inter}}
    62	\newcommand{\Capt}{\mathsf{Cap}}
    63	\newcommand{\Impl}{\mathsf{Impl}}
    64	\newcommand{\Dzero}{\mathcal{D}_0}
    65	\newcommand{\Dstar}{\mathcal{D}^{*}}
    66	\newcommand{\cl}{\operatorname{cl}}
    67	\newcommand{\ov}{\mathrm{ov}}
    68	\newcommand{\E}{\mathbb{E}}
    69	
    70	\title{The Formalized State\\[2pt]
    71	  {\large The Hierarchy of the Beast System}\\[4pt]
    72	  {\normalsize Part VII of \emph{The Six Pillars of the Beast System}}}
    73	\author{Matthew Long\\
    74	  \small The YonedaAI Collaboration, YonedaAI Research Collective\\
    75	  \small Chicago, IL\\
    76	  \small \texttt{matthew@yonedaai.com}\quad \url{https://yonedaai.com}}
    77	\date{October 2026}
    78	
    79	\begin{document}
    80	\maketitle
    81	
    82	\begin{abstract}
    83	The six-pillar framework identifies an invariant structure of human governance, supported by historical observation and given precise expression through mathematics. Every governance system decides who controls resources, makes and interprets rules, shapes beliefs, enforces and produces. This paper defines the Formalized State, a class of structures with six layers of control, a role map and a dependency hypergraph, and proves four results relative to stated axioms and a stated set of preserved properties: roles, control shares, concentration, contestability, integration and dependencies. Representation: every governance system satisfying the axioms is equivalent to a Formalized State structure; content, ideology and procedure are forgotten. Necessity: six axioms about collective life (scarcity, plurality, generality, coordination, defection and maintenance) force the six functions, each axiom can fail in a persistent model, and four incidence axioms with falsifiers make the functions fully interdependent, although interpretation needs legitimation or coercion rather than both. Minimality: dropping or merging any pillar identifies systems that differ in a preserved property, with explicit witness pairs. Uniqueness: the abstraction is the coarsest one preserving those properties, unique up to unique isomorphism, with exactly six dimensions. Encodings of Aristotle, Weber, Parsons, Easton, Almond, Luhmann and Mann each identify two systems the abstraction distinguishes, so none is equivalent to it. Capture is a property of instances: structures satisfying every axiom occupy all four corners of the concentration and integration square. The regime analyses rest on the historical and ethnographic record, and the indices are defined so that real polities can be scored quantitatively.
    84	\end{abstract}
    85	
    86	\section{Introduction}
    87	\label{sec:intro}
    88	
    89	Every governance system answers six questions. Who controls the resources? Who makes the laws? Who interprets the laws? Who shapes the beliefs? Who enforces the rules? Who produces the wealth that sustains everything? The answers range from a Ju/'hoansi camp talking a dispute out at night to a party committee that appoints judges, editors and generals. This paper argues that one mathematical structure represents all of these answers, that the structure is forced by premises about collective life that could be false, and that nothing in it implies that the answers are held by one coalition beyond review.
    90	
    91	The organizing claim of the series is that the six-pillar framework identifies an invariant structure of human governance, supported by historical observation and given precise expression through mathematics. Each part of the claim has a specific home. The invariant structure is the Formalized State: \cref{thm:formalized-state:representation} shows that every governance system satisfying the axioms is represented by it, and \cref{thm:formalized-state:uniqueness,thm:formalized-state:six} show that it is invariant across all of them up to $\cong_A$ and unique for the properties it preserves. The historical observation is the comparison of six regime types in Parts I to VI, the minimal forms of the stateless societies in \cref{tab:hardcases}, and the falsifiable hypotheses of \cref{tab:hypotheses}. The mathematics is the axioms, the theorems, and the reference implementation mapped in \cref{app:code}. Historical observation supports the axioms; it does not prove them. The theorems are proofs relative to the axioms, and the axioms remain open to the falsifiers stated with each of them.
    92	
    93	The paper is the seventh and last Part of a series that adopts the vocabulary and the multiplex-network model of \citet{largo2026hbs}. The source paper named the configuration the Hierarchy of the Beast System after the imagery of Revelation 13 and used five functions. The series splits the source's legal-administrative function into rule making and interpretation and treats the resulting six pillars in Parts I to VI: control of resources ($\pF$), rule making ($\pP$), interpretation ($\pJ$), legitimation ($\pI$), coercion ($\pC$) and production ($\pW$) \citep{long2026financial,long2026political,long2026judicial,long2026ideological,long2026coercive,long2026productive}. In the series, the name ``Beast System'' is the typological, theological reading of the universal structure. It is not a mathematical conclusion about the moral character of any government, and it never labels a religion, a people, a profession, a regime or a person.
    94	
    95	The Formalized State is an abstraction, not a form of government. \Cref{def:formalized-state:F} defines it as a class $\mathcal{F}$ of structures: six layers of control over a set of actors, a many-to-many role map, control shares, contestability and coalition data, and a dependency hypergraph that is strongly connected and cascade-complete. \Cref{thm:formalized-state:representation} proves that every governance system satisfying the axioms is equivalent to a member of $\mathcal{F}$ under a relation $\cong_A$ that preserves roles, shares, concentration, contestability, integration and dependencies, and forgets the content of rules, beliefs and procedures. The class of governance systems is defined without reference to the six functions (\cref{def:formalized-state:collective}), so the theorem can fail, and \cref{sec:representation} exhibits collectives for which it does.
    96	
    97	Four results are kept distinct. Representation says that every governance system is an instance of the abstraction. Necessity says why: the properties that membership in $\mathcal{F}$ requires follow from axioms. \Cref{thm:formalized-state:A} derives the six functions from six axioms, assembling the pillar-level results of Parts I to VI under one persistence condition, and \cref{prop:formalized-state:independence} shows that each axiom can fail in a persistent model in which its function is absent. \Cref{thm:formalized-state:interdependence} derives full interdependence from four further incidence axioms with falsifiers, using a directed hypergraph because interpretation depends on legitimation or on coercion and not necessarily both (Proposition 3.6 of Part III). Minimality says that the abstraction cannot be made coarser: \cref{prop:formalized-state:minimality6} exhibits, for every way of dropping or merging pillars, two governance systems that the coarser abstraction confuses. Uniqueness says that the abstraction is the coarsest one that preserves the stated properties, unique up to a unique isomorphism, and that it has exactly six dimensions (\cref{thm:formalized-state:uniqueness,thm:formalized-state:six}). All four results are relative to the axioms and to the preserved properties. \Cref{thm:formalized-state:novelty} then shows that encodings of seven classical frameworks, from Aristotle to Mann, each fail to distinguish a pair of systems that the Formalized State distinguishes.
    98	
    99	The series keeps two propositions apart. Proposition A states that every functioning governance system contains the six functions and the dependencies among them; in the language of this paper it is the representation theorem. Proposition B states that in some systems the functions become concentrated and coordinated so that independent accountability fails. Concentration, capture, autonomy and accountability are properties of instances, measured by $U_t$, $\Integ_t$ and capture links, and they are not conditions of membership. \Cref{thm:formalized-state:nonimplication} shows that structures satisfying every axiom occupy all four corners of the concentration and integration square, and \cref{thm:formalized-state:conversion} gives conditions under which a coalition's foothold in several pillars dies out or persists. The six regime types of the series are implementations of the abstraction that differ in where integration concentrates and what checks it.
   100	
   101	\section{The six-layer model}
   102	\label{sec:model}
   103	
   104	\subsection{Shared objects}
   105	
   106	The formal objects come from \citet{largo2026hbs}, and the series uses them without redefinition. A polity at time $t$ is a directed multiplex network $G_t=(V_t,E_t)$ whose nodes are organizations or coherent actor groups. Each pillar $m\in\Mset=\{\pF,\pP,\pJ,\pI,\pC,\pW\}$, with $M=|\Mset|=6$, has a layer with adjacency $A^m_t$ and edge weights $a^m_{ij,t}\in[0,1]$, the documented capacity of actor $i$ to constrain a feasible action of actor $j$ through mechanism $m$. A role map assigns actors to pillars, many to many. Actor $i$ holds a control share $s^m_{i,t}$ in pillar $m$, with $\sum_i s^m_{i,t}=1$, and concentration is the Herfindahl index $H_{m,t}=\sum_i(s^m_{i,t})^2$. The multiplex formalism follows the standard treatment of multilayer networks \citep{kivela2014}.
   107	
   108	Contestability $Q_{m,t}\in[0,1]$ summarizes transparency, appeal rights, independence, competition and credible replacement. Unaccountable concentration is the illustrative index $U_t=\sum_m\omega_mH_{m,t}(1-Q_{m,t})$ with nonnegative preregistered weights that sum to one. Cross-pillar integration $C_{mn,t}\in[0,1]$ is the extent to which one coalition commands appointments, budgets, sanctions or agenda in both $m$ and $n$, and the integration statistic is
   109	\[
   110	\Integ_t=\frac{2}{M(M-1)}\sum_{m<n}C_{mn,t},
   111	\]
   112	the mean over the fifteen pairs. A capture link $(i\to j,m)$ requires privileged access or discretion, a weakening of applicable accountability or contestability, and material evidence that ties the asymmetry to an institutional output. The source's strong classification requires both high $U_t$ and high $\Integ_t$ \citep{largo2026hbs}. The aggregate capacities $x_t=(\pF_t,\pP_t,\pJ_t,\pI^{\mathrm{cap}}_t,\pC_t,\pW_t)$ follow $x_{t+1}=B_tx_t+D_tz_t+\varepsilon_t$, where $B_t$ collects dependencies, $z_t$ external shocks and $\varepsilon_t$ unobserved influences.
   113	
   114	Three notational collisions need a convention. The integration statistic is written $\Integ_t$ and the legitimation pillar $\pI$. The source's role map is not written $F$, since $\pF$ is the resource pillar. The series' central statement writes the structural predicate of Proposition A as $B(G)$; this paper writes it $\Struct(G)$, so that it cannot be confused with the dynamics matrix $B_t$ or with Proposition B.
   115	
   116	\subsection{Functions as classes of practices}
   117	
   118	A function is defined by the problem it solves, not by the institution that solves it. This is the distinction that \citet{hempel1959} required of functional analysis and that \citet{merton1968} called the problem of functional alternatives: from the need for a function nothing follows about which institution meets it. Each pillar Part fixed a problem and a class of practices that solve it. The present section fixes a common frame in which the six results can be combined.
   119	
   120	\begin{definition}[Collective, functioning and persistence]
   121	\label{def:formalized-state:collective}
   122	A \emph{collective} $G$ is the largest group whose members make collective decisions as one body, so that a member's move between subgroups of $G$ is not exit from $G$; formally, $G$ is a set $N_t$ of at least two human members at each date $t=1,2,\dots$, a rule system $R_t$, and a probability space $(\Omega,\mathcal{F},\Pr)$ with a filtration $(\mathcal{F}_t)$ that records its history. $G$ \emph{functions} at date $t$ if members make collective decisions and comply with $R_t$ and recognize its office holders often enough for those decisions to be carried out, and if the stock that sustains the collective is nonnegative. The \emph{persistence event} is $\Pi=\{G\text{ functions at every date}\}$. $G$ is \emph{persistent} if $\Pr(\Pi)>0$. The class $\mathcal{G}$ of functioning governance systems is the class of persistent human collectives.
   123	\end{definition}
   124	
   125	The definition of $\mathcal{G}$ mentions collective decisions, rules and compliance. It does not mention allocation, rule making, interpretation, legitimation, sanction or production. A collective in which nobody settled conflicting claims, nobody determined disputes and nobody produced anything would still belong to $\mathcal{G}$ if it persisted. Proposition A says that such a collective does not persist, and that is a substantive claim.
   126	
   127	\begin{definition}[Implementation]
   128	\label{def:formalized-state:implementation}
   129	For each pillar $m$, the predicate $\Impl_m(G)$ is the conclusion of the pillar's necessity result, stated in that Part's vocabulary:
   130	\begin{enumerate}[label=(\roman*)]
   131	\item $\Impl_{\pF}$: almost surely on $\Pi$, only finitely many conflicts over goods are unsettled and infinitely many are settled by a procedure in the collective's repertoire (Definitions 2.1 and 2.2 of Part I);
   132	\item $\Impl_{\pP}$: on $\Pi$, every collective decision is produced by a practice of the members that selects among alternatives over which their preferences diverge (Definition 2.2(a) of Part II);
   133	\item $\Impl_{\pJ}$: almost surely on $\Pi$, infinitely many residual disputes are disposed of by determination, a procedure that neither party controls alone and on which both act (Definitions 2.2 and 2.3 of Part III);
   134	\item $\Impl_{\pI}$: on $\Pi$, in every window of length $L$ some practice refines members' information so that the rule system in force becomes common knowledge among the cooperating members (Definition 2.1 and Theorem 3.5 of Part IV);
   135	\item $\Impl_{\pC}$: the sanction regime of the strategy profile in force is nontrivial, with a long-run share of at least $(p-\theta)/p$ of agent-periods facing a strictly positive deterrence margin (Theorem 3.4 of Part V);
   136	\item $\Impl_{\pW}$: on $\Pi$, productive activity occurs in infinitely many periods and the long-run average inflow is at least the per-period consumption $k>0$ (Lemma 3.3 of Part VI).
   137	\end{enumerate}
   138	\end{definition}
   139	
   140	Each predicate is a property of observable dispositions: counts of settled and unsettled conflicts, the procedures that produced decisions and determinations, the information of entrants, the responses that violations meet, and the flows that replenish the collective's stock. None is satisfied by naming an office. A predicate can fail in a persistent collective, and \cref{prop:formalized-state:independence} constructs such collectives.
   141	
   142	\begin{definition}[Structural predicate]
   143	\label{def:formalized-state:struct}
   144	$\Struct(G)$ holds if $\Impl_m(G)$ holds for every $m\in\Mset$ and the dependency relations $\Dzero$ of \cref{lem:formalized-state:D0} hold in $G$. Proposition A is the statement that $\Struct(G)$ and the interdependence predicate $\Inter(G)$ of \cref{def:formalized-state:cascade} hold for every $G\in\mathcal{G}$.
   145	\end{definition}
   146	
   147	The functions may be distributed across many institutions, fused inside one, or exercised informally. $\Struct(G)$ is silent on these alternatives, because it is a statement about the support of the role map and not about the values of $H$, $Q$ or $C$.
   148	
   149	\section{Axioms}
   150	\label{sec:axioms}
   151	
   152	The series works from six axioms about collective life. In their informal versions they are short: resources are finite and claims on them conflict (Ax1, scarcity); members' preferences diverge and collective choices are made (Ax2, plurality); rules are general, cases particular, and disputes arise (Ax3, generality); cooperation requires shared knowledge of the rules (Ax4, coordination); some members sometimes break rules (Ax5, defection); and the group and its institutions consume resources that someone produces (Ax6, maintenance). The informal versions are too weak to carry a proof, and each pillar Part supplied the auxiliary assumptions its derivation needed. The refined axiom $\mathrm{Ax}k^{*}$ is the bundle that the Part actually used. \Cref{tab:axioms} records the bundles.
   153	
   154	\begin{table}[!htbp]
   155	\centering
   156	\small
   157	\caption{The refined axioms. Each refined axiom is the set of assumptions under which the cited pillar result was proved; the right column names the result.}
   158	\label{tab:axioms}
   159	\begin{tabularx}{\textwidth}{@{}L{1.7cm}YL{2.6cm}@{}}
   160	\toprule
   161	Axiom & Refined content & Pillar result \\
   162	\midrule
   163	Ax1$^{*}$ scarcity & While the collective exists, a conflict over goods occurs in each period with conditional probability at least $p>0$, and an unsettled conflict ends functioning with conditional probability at least $q>0$ & Proposition 3.3 of Part I \\
   164	Ax2$^{*}$ plurality & Collective decisions recur, members' preferences diverge over every decision's alternatives, and decisions and rule changes are produced by the members' own practices & Theorem 3.7 of Part II \\
   165	Ax3$^{*}$ generality & On the persistence event infinitely many residual disputes arise that a move to another group of the collective does not escape (disputes among co-resident kin, or over rights to territory, water or sharing that follow the parties wherever they move); each reaches a disposition at a finite time; for these disputes a disposition by self-help, exit or abandonment ends functioning with conditional probability at least $\kappa>0$; and a losing party complies with a determination if and only if the value it places on the procedure's legitimacy plus the expected sanction is at least its gain from defiance, where the value is positive only if some practice of the legitimation class (Definition 2.1 of Part IV) has led the party to regard the procedure as rightful, and the expected sanction is positive only if some agent's practice answers defiance with a sanction & Theorem 3.3 and Proposition 3.6 of Part III \\
   166	Ax4$^{*}$ coordination & When the collective functions, its rule system, including its settlement procedures, is common knowledge among a cooperating core, members turn over within a bounded horizon $L$, entrants cannot infer the rules from innate endowment, members do not forget what they learn, and entrants are parties to conflicts over goods in infinitely many periods & Theorem 3.5 of Part IV \\
   167	Ax5$^{*}$ defection & Some rule in force has a share $p$ of agents tempted to violate it in the absence of any response that exceeds the violation rate $\theta$ the collective can tolerate, and members best-respond to the sanction regime in force (Lemma 3.3 of Part V) & Theorem 3.4 of Part V \\
   168	Ax6$^{*}$ maintenance & The collective and its institutions consume at least $k>0$ per period from a finite initial stock; inflows are produced by some agent's productive activity; and every practice of every pillar is performed by agents whose consumption is counted here, in a period only if that consumption is met & Lemma 3.3 of Part VI \\
   169	\bottomrule
   170	\end{tabularx}
   171	\end{table}
   172	
   173	The refined axioms are empirical claims about human collectives, not logical truths. Each can be false of some conceivable collective. A population that consumed nothing would violate Ax6$^{*}$; a population of agents who never wished to break a rule would violate Ax5$^{*}$; a collective whose members agreed about every collective choice would violate Ax2$^{*}$; a colony whose rules were fixed by development, as in social insects, would violate the non-innateness clause of Ax4$^{*}$. The hazard clauses of Ax1$^{*}$ and Ax3$^{*}$ are the most demanding, and the pillar Parts identified the cases that test them: collectives in which unsettled conflict is costless (Part I, Section 3) and collectives in which every residual dispute, including disputes among co-resident kin and over rights that follow the parties, can be escaped by free exit (Proposition 3.4 of Part III). Where a premise fails, the derivation of the corresponding function does not apply, and the presence of the function rests on the ethnographic record alone.
   174	
   175	Proposition A as the series states it therefore has two parts. The deductive part is a theorem: a collective that satisfies the refined axioms and persists implements every function. The empirical part is the bridge hypothesis that every functioning human collective satisfies the refined axioms. Part V states the bridge for its own axiom as an explicit assumption (Assumption 3.2 of Part V); the same structure holds for the other five. The honest content of a proof from minimal axioms is a valid derivation together with a list of the premises that could be false.
   176	
   177	\section{Structural necessity}
   178	\label{sec:necessity}
   179	
   180	\subsection{The forcing lemma}
   181	
   182	Two of the six pillar results share a single argument, which can be stated once. A recurring problem is forced if leaving an instance unsolved carries a bounded-below risk of ending the collective.
   183	
   184	\begin{lemma}[Forcing]
   185	\label{lem:formalized-state:forcing}
   186	Let a collective face a sequence of problem instances, indexed in order of disposition, each disposed of as solved or unsolved at a finite time. Suppose there is $\kappa\in(0,1]$ such that, conditional on the history up to the disposition of any instance and on that instance being unsolved, functioning ends at the disposition with probability at least $\kappa$. Let $N$ be the number of unsolved instances, with $N=\infty$ allowed. Then
   187	\begin{enumerate}[label=(\alph*)]
   188	\item $\Pr(\Pi\cap\{N\ge n\})\le(1-\kappa)^n$ for every $n\ge1$, so $N<\infty$ almost surely on $\Pi$;
   189	\item if infinitely many instances arise almost surely on $\Pi$, then almost surely on $\Pi$ infinitely many instances are solved, and the fraction of solved instances among the first $k$ tends to one as $k\to\infty$.
   190	\end{enumerate}
   191	\end{lemma}
   192	
   193	\begin{proof}
   194	(a) For $n\ge1$ let $S_n$ be the event that at least $n$ instances are left unsolved and the collective keeps functioning through the disposition of each of the first $n$. Conditional on $S_{n-1}$ and on the occurrence of an $n$-th unsolved instance, functioning survives that disposition with probability at most $1-\kappa$, so $\Pr(S_n)\le(1-\kappa)\Pr(S_{n-1})$, and induction from $\Pr(S_0)=1$ gives $\Pr(S_n)\le(1-\kappa)^n$. Since $\Pi\cap\{N\ge n\}\subseteq S_n$, the bound follows, and $\Pr(\Pi\cap\{N=\infty\})\le\inf_n(1-\kappa)^n=0$.
   195	
   196	(b) On $\Pi$, by (a), the number of unsolved instances among the first $k$ is eventually constant, while by hypothesis $k$ grows without bound. The number solved among the first $k$ is $k$ minus that constant, so it tends to infinity and its ratio to $k$ tends to one.
   197	\end{proof}
   198	
   199	Part III proved its necessity theorem by this argument, with residual disputes as instances and determination as solution (Theorem 3.3 of Part III). Part I proved a quantitative version with conflicts over goods as instances and settlement as solution (Proposition 3.3 of Part I). The lemma does not say that the solutions are good ones. A collective may settle conflicts by rules that favor a few, and determine disputes by biased procedures, and still satisfy it.
   200	
   201	\subsection{Three patterns of argument}
   202	
   203	The six pillar results rest on three kinds of argument, and the difference matters for what would refute them. Hazard forcing, \cref{lem:formalized-state:forcing}, gives the financial and judicial pillars; its empirical content is the hazard, and where unsolved instances are harmless, as with costless exit from a band, it gives nothing. Stock accounting gives the productive pillar: persistence requires a nonnegative stock $X_T=X_0+\sum_{t<T}(Y_t-K^{\mathrm{tot}}_t)$, so with consumption at least $k>0$ and a finite initial stock the inflows must average at least $k$, and the no-manna assumption makes every inflow someone's productive activity, possibly an outsider's (Lemmas 3.3 and 3.4 of Part VI). Constitutive arguments give the rest. A decision that binds everyone over alternatives on which members disagree is a selection among divergent preferences (Lemma 3.4 of Part II). Members who enter without knowing the rules acquire common knowledge of them only through practices that refine their information (Theorem 3.5 of Part IV, following \citealt{lewis1969} and \citealt{aumann1976}). And if more agents are tempted than the collective can tolerate, best responses keep violations within tolerance only if a positive deterrence margin shifts at least $p-\theta$ of probability mass to compliance (Theorem 3.4 of Part V, in the tradition of \citealt{becker1968}).
   204	
   205	\begin{lemma}[Pillar necessity]
   206	\label{lem:formalized-state:pillars}
   207	Let $G$ be a collective with $\Pr(\Pi)>0$. For each $k=1,\dots,6$, if $G$ satisfies Ax$k^{*}$ then $\Impl_{m_k}(G)$ holds, where $(m_1,\dots,m_6)=(\pF,\pP,\pJ,\pI,\pC,\pW)$.
   208	\end{lemma}
   209	
   210	\begin{proof}
   211	$\pF$: under Ax1$^{*}$, \cref{lem:formalized-state:forcing}(a) with $\kappa=q$ gives finitely many unsettled conflicts almost surely on $\Pi$. Part I's Proposition 3.3(b) gives $\Pr(\Pi\cap\{Y_T<pT/2\})\le e^{-pT/8}$ for the number $Y_T$ of periods with a conflict up to $T$. The bounds are summable in $T$, so by the Borel-Cantelli lemma, almost surely on $\Pi$ we have $Y_T\ge pT/2$ for all large $T$; conflicts therefore arise infinitely often on $\Pi$, and \cref{lem:formalized-state:forcing}(b) gives infinitely many settled conflicts. $\pP$: on $\Pi$ collective decisions are made, and Ax2$^{*}$ contains the hypotheses of Lemma 3.4 and Theorem 3.7 of Part II, which give sense (a) of Definition 2.2 of Part II at every decision. $\pJ$: \cref{lem:formalized-state:forcing}(b), applied to the subsequence of residual disputes that a move does not escape, which Ax3$^{*}$ makes infinite and subject to the hazard $\kappa$, with determination as solution, gives infinitely many determinations almost surely on $\Pi$, which is $\Impl_{\pJ}$; Theorem 3.3 of Part III is the case in which every residual dispute is inescapable. $\pI$: on $\Pi$ the collective functions at every date, so every window of length $L$ lies in an interval of functioning longer than $L$, and Theorem 3.5 of Part IV applies to each window. $\pC$: Ax5$^{*}$ is Assumption 3.1 of Part V for a rule in force under a best-response profile, and Theorem 3.4 of Part V gives the stated bound. $\pW$: on $\Pi$ the stock stays nonnegative at every date, which is persistence in the sense of Part VI, and Lemma 3.3 of Part VI applies.
   212	\end{proof}
   213	
   214	The lemma adds nothing to the six Parts except a common persistence event. That is its purpose. The Parts used different notions of persistence, from survival up to a horizon to functioning over a window, and a theorem about one collective needs one notion.
   215	
   216	\subsection{The structural necessity theorem}
   217	
   218	\begin{theorem}[Structural necessity]
   219	\label{thm:formalized-state:A}
   220	Let $G$ be a persistent collective that satisfies Ax1$^{*}$ to Ax6$^{*}$. Then, almost surely on the persistence event, all six functions are implemented: $\Impl_m(G)$ holds for every $m\in\Mset$. If every functioning human collective satisfies the refined axioms, this holds for every $G\in\mathcal{G}$. \Cref{cor:formalized-state:struct} adds the dependency relations $\Dzero$, which gives $\Struct(G)$, the first half of Proposition A.
   221	\end{theorem}
   222	
   223	Universality over real governance systems is the theorem together with the empirical bridge that every functioning collective satisfies Ax1$^{*}$ to Ax6$^{*}$, which historical observation supports.
   224	
   225	\begin{proof}
   226	By \cref{lem:formalized-state:pillars}, each $\Impl_m(G)$ holds, either deterministically on $\Pi$ or on an event of full conditional probability given $\Pi$. A finite intersection of events of full conditional probability has full conditional probability, so all six hold together almost surely on $\Pi$. The second sentence restates the first under the bridge hypothesis.
   227	\end{proof}
   228	
   229	The theorem does not use the integration statistic, the concentration indices, or any premise about who holds control. It also does not use strong connectivity of the dependency structure, which \cref{sec:dependency} derives from four further axioms. The second half of Proposition A, universal interdependence, is \cref{thm:formalized-state:interdependence}, and the two theorems together with the bridge hypothesis are Proposition A in the sense of the series.
   230	
   231	\subsection{Consistency and independence of the axioms}
   232	
   233	A theorem from axioms says little if the axioms have no model, and a necessity claim is empty if the conclusion holds whether or not the axioms do. The next proposition settles both points.
   234	
   235	\begin{proposition}[Consistency and independence]
   236	\label{prop:formalized-state:independence}
   237	\leavevmode
   238	\begin{enumerate}[label=(\alph*)]
   239	\item There is a collective that functions at every date with probability one, satisfies Ax1$^{*}$ to Ax6$^{*}$, and implements all six functions.
   240	\item For each $k$ there is a collective that functions at every date with probability one, satisfies Ax$j^{*}$ for every $j\neq k$, violates Ax$k^{*}$, and does not implement $m_k$.
   241	\end{enumerate}
   242	\end{proposition}
   243	
   244	\begin{proof}
   245	(a) Take three members at every date; the collective has no subgroups, so no residual dispute can be escaped by a move and every residual dispute is inescapable in the sense of Ax3$^{*}$. One member is replaced by an entrant every $L$ periods; the member replaced is always the longest-serving one, an entrant does not know the rule system at entry and no member forgets what it learns, and the plot is claimed in each period by the most recent entrant and one other member, so entrants are parties to conflicts over goods in every period. In each period: one plot of land is claimed by two members and is assigned by a known rotation rule, with hazard $q=1/2$ attached to an unsettled conflict; the members choose between two campsites, with members 1 and 2 preferring different sites, by majority vote; one residual dispute about the application of a rule arises between two members and is determined by a lot drawn by the third, whose result both accept because each places on the procedure a value $\ell$ at least as large as its gain from defiance, a value acquired at the initiation described next, where the lot is presented as the rightful procedure, with hazard $\kappa=1/2$ attached to any other disposition; an entrant takes part in a public initiation at which the rule system is recited to all members, which makes it common knowledge among those initiated; each member observes a temptation to breach a rule of camp chores, drawn from a distribution $G$ with $p=1-G(0)=1/2$, and a breach is met with a fine $d$ paid to the other members, with $d$ chosen so that $G(d)\ge3/4$, members best-respond to the fine, and the collective tolerates a violation rate $\theta=1/4$; and the members forage an output equal to their consumption $k$; each member forages alone, at any campsite. Every conflict is settled and every residual dispute determined, so no hazard is ever triggered and the collective functions at every date with probability one. Each refined axiom holds by construction, and each implementation predicate holds: settlement in every period, majority choice over divergent preferences, determination in every period, initiation in every window, a positive margin $d$ for every agent at every date, and foraging in every period.
   246	
   247	(b) Modify the model of (a) in one component. For $k=1$, set $q=0$ and assign the plot by contest each period, so conflicts are never settled and never harmful. For $k=2$, give all members the same preference over campsites, so no decision selects among divergent preferences. For $k=3$, abandon every residual dispute and set the hazard of abandonment to zero, which is the costless-exit case of Proposition 3.4 of Part III. For $k=4$, let entrants know the rule system at entry, drop the initiation, and attach the fine $d\ge g$ to defiance of a determination, so no practice of the legitimation class operates and determinations rest on sanction alone. For $k=5$, let temptations be nonpositive, so $p=0\le\theta$, and remove the fine, so every margin is zero and no violation occurs. For $k=6$, let an inflow of $k$ arrive in every period with no productive act by anyone. In each case the modified component triggers no hazard, the other components are unchanged, and the stated axiom and predicate fail.
   248	\end{proof}
   249	
   250	Part (b) is the formal answer to the charge that Proposition A is true by definition. In each modified collective the function is absent and the collective persists, so the class of persistent collectives does not contain the six functions by construction. What excludes such collectives from the real world is the failure of their premises: harmless unsettled conflict, unanimous preferences, free exit, innate rules, untempted members and unproduced inflows. Those are empirical claims, and the pillar Parts tested each against the ethnographic and historical record.
   251	
   252	\subsection{Minimal forms}
   253	
   254	The hard cases for Proposition A are societies described as having no state, no chiefs with power to command, or radical equality. The series predicts that each implements every function in an informal and dispersed form. The prediction has a formal core.
   255	
   256	\begin{lemma}[Minimal form]
   257	\label{lem:formalized-state:minimal}
   258	Let a collective of $n\ge2$ adults implement every function through practices without designated offices in which each adult holds an equal share of decision-relevant control, and let $Q_m\ge\bar q$ for every $m$. Then $H_m=1/n$ for every $m$ and $U_t\le(1-\bar q)/n$. If the coalition of all adults is admissible in the coalition list that defines $C_{mn}$ (\cref{def:formalized-state:overlap}), then $C_{mn}=1$ for every pair and $\Integ_t=1$. In either case the capture predicate of \cref{def:formalized-state:cap} fails for every threshold $u^{*}>(1-\bar q)/n$.
   259	\end{lemma}
   260	
   261	\begin{proof}
   262	Equal shares give $H_m=n\cdot(1/n)^2=1/n$. Then $U_t=\sum_m\omega_m(1/n)(1-Q_m)\le(1-\bar q)/n$. If the grand coalition $S=N$ is admissible, its control share in every pillar is one, so $\min\{\kappa_m(N),\kappa_n(N)\}=1$ for every pair. The capture predicate requires $U_t\ge u^{*}$, which fails when $u^{*}>(1-\bar q)/n$.
   263	\end{proof}
   264	
   265	The lemma resolves an apparent paradox in the ethnography. In egalitarian bands the same body judges, sanctions, decides and legitimates, so integration is at its maximum (Part III observed that $C_{\pJ\pC}$ is high there), yet the functions are held equally and open to challenge by anyone, so unaccountable concentration is near its minimum. This is the clearest reason why the source requires both indices to be high: integration of functions in the group as a whole is the opposite of capture.
   266	
   267	\Cref{tab:hardcases} collects the minimal forms that the pillar Parts documented for the Nuer \citep{evanspritchard1940}, the Ju/'hoansi \citep{marshall1976,lee1979,lee2013,wiessner2005}, mobile foragers with a reverse dominance hierarchy \citep{boehm1999}, Amazonian groups whose headmen speak but cannot command \citep{clastres1987}, and Ostrom's long-enduring commons \citep{ostrom1990,cox2010}. Woodburn's institutions of leveling show the same pattern from the side of sanctions: egalitarianism is produced and defended, not given \citep{woodburn1982}.
   268	
   269	\begin{table}[!htbp]
   270	\centering
   271	\small
   272	\caption{Minimal forms of the six functions in stateless and consensus societies, as documented in Parts I to VI. Each cell names the practice; no cell names an office with power to command.}
   273	\label{tab:hardcases}
   274	\footnotesize
   275	\setlength{\tabcolsep}{3pt}
   276	\begin{tabularx}{\textwidth}{@{}L{1.6cm}YYYYYY@{}}
   277	\toprule
   278	Case & $\pF$ & $\pP$ & $\pJ$ & $\pI$ & $\pC$ & $\pW$ \\
   279	\midrule
   280	Nuer & Cattle rights and bridewealth & Negotiation among lineages & Mediation by the leopard-skin chief & Lineage idiom and ritual & Threat of feud by kin & Herding and cultivation \\
   281	Ju/'hoansi & Meat shared by the arrow-owner rule & Camp talk and moving camp & Talking disputes out & Talk heard by all and the healing dance & Criticism, ridicule and avoidance & Foraging by both sexes \\
   282	Mobile foragers & Sharing enforced against hoarders & Group decision against would-be leaders & Group judgment of deviants & Shared moral talk & Ostracism, exile and execution & Foraging \\
   283	Amazonian groups & The headman's duty of generosity & Consensus with oratory as duty & Peacemaking by the headman & Myth and the headman's recitation & Abandonment of a commanding headman & Gardening and hunting \\
   284	Commons users & Appropriation and boundary rules & Users modify the rules & Low-cost local arenas & Rules known to users & Monitoring and graduated sanctions & Provision of maintenance labor \\
   285	\bottomrule
   286	\end{tabularx}
   287	\end{table}
   288	
   289	The table supports both halves of the series' thesis: every function operates where no office does, which is what Proposition A requires, and concentration varies with circumstance and choice, which is what makes Proposition B contingent. Some early societies moved seasonally between egalitarian and hierarchical arrangements, including temporary policing during collective hunts \citep{graeber2021}; upland groups in Southeast Asia kept their functions dispersed to avoid incorporation into lowland states \citep{scott2009}; and early grain states concentrated the resource and productive functions where taxable surpluses allowed \citep{scott2017}. Two cautions qualify the record without removing any function from it. The ethnographies describe groups in marginal environments and in contact with states and markets, and foraging societies vary widely \citep{kelly1995}. Equal formal shares understate actual concentration, because age, gender, skill and kinship give some speakers more weight (Part II, Section 3).
   290	
   291	The Ju/'hoansi are the hardest case for the judicial derivation, because moving to another camp resolves many disputes with no third party (Part III, Section 3). Under the unit of \cref{def:formalized-state:collective} the collective is the network of camps linked by kinship and exchange, within which a move is not exit. We code the Ju/'hoansi as satisfying the inescapable-dispute clause of Ax3$^{*}$: rights to territory and water are held through kin and follow a person from camp to camp, and disputes over sharing and marriage among kin recur and are talked out in public \citep{lee2013,wiessner2005}; Lee's records of homicide show that self-help between kin carried a real risk of feud \citep{lee1979}, which we read as a hazard to the functioning of the camp network in the sense of Ax3$^{*}$. The coding is an ethnographic reading of these sources, not a measurement of the hazard. With it and the codings of the other five axioms in Parts I to VI, the Ju/'hoansi are an instance of \cref{thm:formalized-state:A}, with a thin but present judicial function.
   292	
   293	\subsection{Falsifiers and counterexample attempts}
   294	
   295	Each pillar Part identified its strongest counterexample attempt and the observation that would refute its result. \Cref{tab:falsifiers} collects them. Every reply in the table narrows the claim in a stated direction or relocates the function; none rescues the claim by redefining the function after the fact.
   296	
   297	\begin{table}[!htbp]
   298	\centering
   299	\small
   300	\caption{The strongest counterexample attempt for each pillar, the reply given in the pillar Part, and the observation that would refute the pillar's necessity result.}
   301	\label{tab:falsifiers}
   302	\begin{tabularx}{\textwidth}{@{}L{0.7cm}YYY@{}}
   303	\toprule
   304	 & Counterexample attempt & Reply & Falsifier \\
   305	\midrule
   306	$\pF$ & Foragers' wants are easily met, so there is no scarcity \citep{sahlins1972b} & Scarcity concerns conflicting claims, and affluence lowers $p$ without making it zero & A persistent collective whose members hold conflicting claims and resolve them mostly without any settlement procedure \\
   307	$\pP$ & Custom evolves without legislators \citep{hayek1973,ellickson1991} & Distributed practices still select and change rules, with no office & A long-lived plural group whose rules never changed through environments that no single rule system could survive \\
   308	$\pJ$ & Free exit, or rules executed by code & Free exit thins the function (Proposition 3.4 of Part III), and code relocates interpretation to the encoding of cases (Proposition 3.5 of Part III) & A persistent collective in which disputes that a move does not escape recur and are always settled by force or left open \\
   309	$\pI$ & Force alone coordinates & Sanctions deter only those who know them, and elites must coordinate on expectations & A collective with turnover and locally variable rules whose entrants coordinate without any practice that informs them \\
   310	$\pC$ & Reciprocity and reputation enforce without coercion \citep{axelrod1984,greif1993} & Withdrawal of cooperation is a sanction & A rule whose measured temptation share exceeds its observed violation rate while violators fare no worse than matched compliers \\
   311	$\pW$ & Endowments, raiding, rents or automation & Production is relocated to donors, victims, extractors or the owners of machines (Lemma 3.4 of Part VI) & A system that persists indefinitely with no production anywhere and no replenishment of its stock \\
   312	\bottomrule
   313	\end{tabularx}
   314	\end{table}
   315	
   316	The coercion row needs one further safeguard. The replies to internalization and exit could be used to reclassify any compliant collective without sanctions as one in which few members are tempted, which would make the necessity claim immune to evidence. Part V therefore requires that the temptation share be measured independently of the sanction practices it is used to explain, for example by offering members an unobserved opportunity to break a rule, and it states the falsifier without the tolerance $\theta$, which would otherwise be an adjustable parameter. The same requirement applies to every hazard in \cref{tab:axioms} and to the legitimacy value and expected sanction in the compliance clause of Ax3$^{*}$: a premise measured only through the outcome it is meant to explain cannot test anything.
   317	
   318	\subsection{Hart's secondary rules}
   319	
   320	Hart argued that a regime of primary obligations alone suffers from uncertainty about which rules exist, a static character, and inefficiency in settling disputes, and that the remedies are a rule of recognition, rules of change and rules of adjudication \citep{hart1961}. The series assigns these to legitimation, rule making and interpretation (Definition 3.6 of Part II, Definition 2.2 of Part IV, Section 2 of Part III), and draws the boundary between $\pP$ and $\pJ$ by acts: making or changing a general rule belongs to $\pP$, applying a given rule to a case belongs to $\pJ$ (Definition 2.3 of Part II). A court that changes a rule by precedent performs both acts, and the role map records it in both layers. Under precedent, interpretation becomes an input to rule change and rule change produces the rules that interpretation applies, while recognition certifies both, since a new statute or precedent coordinates behavior only once it is common knowledge (Theorem 3.5 of Part IV). In \cref{sec:dependency}, Hart's triad appears as the arcs $\pI\to\pP$, $\pP\to\pJ$, $\pJ\to\pP$ and $\pP\to\pI$, which make the three secondary functions mutually reachable whenever rules change through both legislation and precedent.
   321	
   322	\subsection{Functional explanation}
   323	
   324	\Cref{thm:formalized-state:A} is a condition of persistence. It does not explain why any particular institution exists, and it asserts no feedback from the effects of an institution to its existence, which Elster required of functional explanation \citep{elster1979,elster1983}. It says nothing about why the Nuer had a leopard-skin chief or why Bourbon France sold judicial offices. Older lists of functional prerequisites drifted toward tautology because they defined prerequisites by what persisting societies happened to have (\cref{sec:literature}); the present derivation avoids the drift because each premise can be false and \cref{prop:formalized-state:independence} exhibits persistent collectives in which it is.
   325	
   326	\section{The dependency structure}
   327	\label{sec:dependency}
   328	
   329	\subsection{Dependency as a directed hypergraph}
   330	
   331	Proposition A speaks of the six functions ``together with the dependency relations among them''. The pillar Parts found two dependencies that a directed graph cannot express. An effective judicial determination needs either legitimacy or an expected sanction, and neither by itself (Proposition 3.6 of Part III). Large-scale sanctioning needs either material provisioning or legitimation, but only when sanctions are costly public goods (Proposition 3.6 and Corollary 3.7 of Part V). A dependency on one of several functions is a hyperarc. Directed hypergraphs of this kind, with reachability through hyperarcs whose whole tail has been reached, are standard in the study of AND/OR structures \citep{gallo1993}.
   332	
   333	\begin{definition}[Dependency hypergraph]
   334	\label{def:formalized-state:hypergraph}
   335	A \emph{hyperarc} is a pair $(T,m)$ with $m\in\Mset$ and $\emptyset\neq T\subseteq\Mset\setminus\{m\}$. The hyperarc $(T,m)$ belongs to the dependency structure $\mathcal{D}(G)$ of a collective if, almost surely on $\Pi$, infinitely many of the instances that the practices of $m$ solve are solved only with an output of at least one function in $T$: if every function in $T$ withheld its output, each of those instances would be left unsolved. The instances of each function are those of its implementation predicate: conflicts over goods for $\pF$, collective decisions for $\pP$, residual disputes for $\pJ$, entrants in a window for $\pI$, agent-periods under the rule for $\pC$, and periods of production for $\pW$. When $T=\{n\}$ the hyperarc is an \emph{arc}, written $n\to m$, with the provider on the left. A hyperarc with $|T|\ge2$ is a disjunction: $m$ needs some member of $T$, not all of them.
   336	\end{definition}
   337	
   338	\begin{definition}[Connectivity and cascade]
   339	\label{def:formalized-state:cascade}
   340	The \emph{underlying digraph} of $\mathcal{D}$ has an arc $t\to m$ for every $(T,m)\in\mathcal{D}$ and every $t\in T$. For $S\subseteq\Mset$ the \emph{cascade} $\cl_{\mathcal{D}}(S)$ is the smallest set that contains $S$ and contains $m$ whenever $(T,m)\in\mathcal{D}$ and $T\subseteq\cl_{\mathcal{D}}(S)$. $\mathcal{D}$ is \emph{strongly connected} if its underlying digraph is, and \emph{cascade-complete} if $\cl_{\mathcal{D}}(\{n\})=\Mset$ for every $n$. The \emph{interdependence predicate} $\Inter(G)$ holds if $\mathcal{D}(G)$ is strongly connected and cascade-complete.
   341	\end{definition}
   342	
   343	The cascade $\cl_{\mathcal{D}}(S)$ is the set of functions that fail when the functions in $S$ withhold their outputs, propagated through the instances of \cref{def:formalized-state:hypergraph}. Strong connectivity says that every function is linked to every other by a chain of dependencies. Cascade completeness says more: the failure of any single function brings down all the others. The two notions coincide for digraphs and come apart for hypergraphs, because a disjunctive hyperarc transmits failure only when its whole tail has failed.
   344	
   345	\begin{remark}[Dependency through persistence]
   346	\label{rem:formalized-state:persistence}
   347	If $n\to m$ were defined to mean that the collective stops persisting when $n$ is withheld, \cref{thm:formalized-state:A} would make every function depend on every other at no cost: withholding any function ends persistence, and every implementation predicate is defined on the persistence event. \Cref{def:formalized-state:hypergraph} excludes this by requiring that the instances of $m$ use an output of $T$ directly. Interdependence in the present sense is a claim about how the functions operate, and it does not follow from Proposition A.
   348	\end{remark}
   349	
   350	\subsection{Dependencies derived from the axioms}
   351	
   352	\begin{lemma}[Derived dependencies]
   353	\label{lem:formalized-state:D0}
   354	Under the hypotheses of \cref{thm:formalized-state:A}, $\mathcal{D}(G)$ contains
   355	\[
   356	\Dzero=\bigl\{\pW\to\pF,\ \pW\to\pP,\ \pW\to\pJ,\ \pW\to\pI,\ \pW\to\pC,\ (\{\pI,\pC\},\pJ),\ \pI\to\pF\bigr\}.
   357	\]
   358	It need not contain the arc $\pI\to\pJ$ or the arc $\pC\to\pJ$.
   359	\end{lemma}
   360	
   361	\begin{proof}
   362	\emph{Production.} By the last clause of Ax6$^{*}$, every practice is performed only when its performers' consumption is met. The initial stock is finite and consumption is at least $k>0$ per period, so without produced inflows the stock is exhausted after at most $X_0/k$ periods (Lemma 3.3 of Part VI). Every instance of every other function that falls after that date is solved only if productive activity, by members or by outsiders (Lemma 3.4 of Part VI), supplies the practitioners' consumption. On $\Pi$ each function solves infinitely many instances, so $\pW\to m$ for every $m\neq\pW$.
   363	
   364	\emph{Interpretation.} By the compliance clause of Ax3$^{*}$, which is the model of Proposition 3.6 of Part III, a losing party that gains $g>0$ by defiance complies if and only if $\ell+\sigma\ge g$, where $\ell$ is the value it places on the procedure's legitimacy and $\sigma$ the expected sanction. A party to a residual dispute strictly prefers its own verdict (Definition 2.2 of Part III), so $g>0$. If legitimation and sanction both withhold their outputs, then $\ell=\sigma=0$ by Ax3$^{*}$ and no determination is effective, so $\Impl_{\pJ}$ requires an output of legitimation or of sanction for each effective determination, and $(\{\pI,\pC\},\pJ)\in\mathcal{D}(G)$. In the collective of \cref{prop:formalized-state:independence}(a) with the fine $d\ge g$ also attached to defiance of a determination, each determination is effective with either output alone, so neither $\pI\to\pJ$ nor $\pC\to\pJ$ belongs to $\mathcal{D}(G)$.
   365	
   366	\emph{Allocation and recognition.} A conflict is settled only if members can anticipate the assignment from a description of the procedure (Definition 2.2(b) of Part I), which requires that they know the procedure. Settlement procedures belong to the rule system whose common knowledge Ax4$^{*}$ requires, and under Ax4$^{*}$ every window of length $L$ contains a member of the cooperating core who entered without knowing the rule system (Lemma 3.4 of Part IV) and came to know it only through practices of the legitimation function (Theorem 3.5 of Part IV). The conflicts that such members are party to after entry, which recur on $\Pi$ by the last clause of Ax4$^{*}$, are settled only with that output, so $\pI\to\pF$.
   367	\end{proof}
   368	
   369	\begin{corollary}[Structural necessity with dependencies]
   370	\label{cor:formalized-state:struct}
   371	Under the hypotheses of \cref{thm:formalized-state:A}, $\Struct(G)$ holds. If every functioning human collective satisfies the refined axioms, $\Struct(G)$ holds for every $G\in\mathcal{G}$.
   372	\end{corollary}
   373	
   374	\begin{proof}
   375	\Cref{thm:formalized-state:A} gives $\Impl_m(G)$ for every $m$ almost surely on $\Pi$, and \cref{lem:formalized-state:D0}, whose hypotheses are those of the theorem, gives $\Dzero\subseteq\mathcal{D}(G)$. The second sentence is the first under the bridge hypothesis.
   376	\end{proof}
   377	
   378	The structure $\Dzero$ is not strongly connected. No arc enters $\pW$, and $\pP$ and $\pJ$ have no outgoing arc, and $\pC$ has one only through the disjunctive hyperarc. Apart from the compliance clause of Ax3$^{*}$ and the settlement-procedure and entrant clauses of Ax4$^{*}$, the six axioms constrain each function separately. The next subsection adds the incidences on production, rule making, interpretation and coercion.
   379	
   380	\subsection{Incidence axioms}
   381	
   382	The six problems converge on one object in every collective that the pillar Parts examined: the rules that assign goods. A settlement procedure is a rule that must be changed when circumstances change, interpreted when its application is disputed, known to those it binds, enforced against those tempted to breach it, and applied to the inputs of production. Each of these is an incidence of one axiom on the financial pillar. They are stated as axioms because they are claims about collective life that the six axioms do not imply (\cref{prop:formalized-state:minimality}(a)), and each comes with a falsifier.
   383	
   384	\begin{assumption}[X1, contested inputs]
   385	\label{ass:formalized-state:X1}
   386	In infinitely many periods on $\Pi$, productive activity uses inputs, such as land, water, tools or equipment, that are goods under conflicting claims in the sense of Definition 2.1 of Part I, and an input is used productively only under an assignment that its user can anticipate.
   387	\end{assumption}
   388	
   389	\begin{assumption}[X2, changing environment]
   390	\label{ass:formalized-state:X2}
   391	On $\Pi$ the environment changes infinitely often in the sense of Assumption 3.2 of Part II, and each change creates conflicts over goods that no settlement procedure in force before the change can settle.
   392	\end{assumption}
   393	
   394	\begin{assumption}[X3, open-textured allocation]
   395	\label{ass:formalized-state:X3}
   396	Some settlement procedure in force has open texture in the sense of Definition 2.1 of Part III, and on $\Pi$ infinitely many residual disputes about its application arise that a move does not escape, subject to the hazard of Ax3$^{*}$.
   397	\end{assumption}
   398	
   399	\begin{assumption}[X5, tempting allocation]
   400	\label{ass:formalized-state:X5}
   401	Ax5$^{*}$ holds for some settlement procedure in force: the share of members who would gain from breaching its assignment in the absence of any response by others, net of every internal cost, exceeds the violation rate the collective can tolerate.
   402	\end{assumption}
   403	
   404	The incidence clauses of Ax4$^{*}$ fail for a collective whose entrants are never parties to conflicts over goods, or whose settlement procedures are run by specialists whose rules the parties need not know, although where such specialists belong to the cooperating core and parties anticipate assignments through them, as in complex polities with tax codes or credit rules, the clause holds; the compliance clause of Ax3$^{*}$ fails for a losing party that complies with no legitimating belief and no expected sanction. The falsifiers of the four incidence axioms are direct. X1 fails for a collective that sustains production on inputs nobody else claims, or on inputs whose use is decided each period by unregulated contest. X2 fails for a long-lived collective that meets new kinds of conflicting claims without ever changing its allocation rules. X3 fails for a collective whose allocation rules never produce a dispute that the parties cannot settle by bargaining. X5 fails for a collective in which the temptation to breach every allocation rule, measured independently of sanction practices, stays below a tolerance preregistered for that rule. The pillar Parts report evidence against each such collective. Foragers who own no land in the agrarian sense still hold kin-based rights to territory and water (Part I, Section 3). Ellickson's ranchers changed their norms when trespass and fencing conditions changed \citep{ellickson1991}. The Nuer settled homicide by cattle compensation through a mediator because the parties could not settle it alone \citep{evanspritchard1940}. And Wiessner's records of Ju/'hoansi camp talk show continual criticism of failures to share \citep{wiessner2005}, which is what X5 predicts and what a population of untempted members would not need.
   405	
   406	\begin{figure}[t]
   407	\centering
   408	\begin{tikzpicture}[>=stealth, every node/.style={font=\small},
   409	    fn/.style={circle,draw,minimum size=0.85cm,fill=white},
   410	    lab/.style={fill=white,inner sep=1.5pt,font=\footnotesize}]
   411	  \node[fn] (F) at (0,0) {$\pF$};
   412	  \node[fn] (W) at (0,-2.6) {$\pW$};
   413	  \node[fn] (P) at (-3.6,0.6) {$\pP$};
   414	  \node[fn] (J) at (3.6,0.6) {$\pJ$};
   415	  \node[fn] (I) at (-2.0,2.7) {$\pI$};
   416	  \node[fn] (C) at (2.0,2.7) {$\pC$};
   417	  \draw[->,gray] (W) to[bend left=28] (P);
   418	  \draw[->,gray] (W) to[bend right=28] (J);
   419	  \draw[->,gray] (W) to[bend left=45] (I);
   420	  \draw[->,gray] (W) to[bend right=45] (C);
   421	  \draw[->,gray] (W) to[bend right=25] (F);
   422	  \draw[->,thick] (F) to[bend right=25] node[lab] {X1} (W);
   423	  \draw[->,thick] (P) -- node[lab] {X2} (F);
   424	  \draw[->,thick] (J) -- node[lab] {X3} (F);
   425	  \draw[->,thick] (C) -- node[lab] {X5} (F);
   426	  \draw[->,thick] (I) -- node[lab] {Ax4} (F);
   427	  \coordinate (h) at (3.3,2.5);
   428	  \fill (h) circle (1.8pt);
   429	  \draw[thick,dashed] (I) .. controls (-0.8,3.9) and (2.6,3.7) .. (h);
   430	  \draw[thick,dashed] (C) -- (h);
   431	  \draw[->,thick,dashed] (h) -- (J);
   432	\end{tikzpicture}
   433	\caption{The dependency structure $\Dstar$ of \cref{thm:formalized-state:interdependence}. Gray arcs run from production to every other function. Solid labeled arcs enter allocation and production and carry the premise that yields them. The dashed hyperarc joins legitimation and coercion at a point before reaching interpretation, because interpretation needs one of the two and not both.}
   434	\label{fig:hypergraph}
   435	\end{figure}
   436	
   437	\subsection{Interdependence}
   438	
   439	\begin{theorem}[Interdependence]
   440	\label{thm:formalized-state:interdependence}
   441	Let $G$ satisfy the hypotheses of \cref{lem:formalized-state:D0} and Assumptions X1, X2, X3 and X5. Then $\mathcal{D}(G)$ contains
   442	\[
   443	\Dstar=\Dzero\cup\{\pF\to\pW,\ \pP\to\pF,\ \pJ\to\pF,\ \pC\to\pF\},
   444	\]
   445	$\Dstar$ is strongly connected and cascade-complete, and $\Inter(G)$ holds. If every functioning human collective satisfies the refined axioms and the four incidence axioms, then $\Struct(G)$ and $\Inter(G)$ hold for every $G\in\mathcal{G}$: every function reaches every other, and the failure of any one propagates to all six.
   446	\end{theorem}
   447	
   448	\begin{proof}
   449	\emph{The arcs.} $\Dzero\subseteq\mathcal{D}(G)$ by \cref{lem:formalized-state:D0}. For $\pF\to\pW$: under X1, the production that uses contested inputs takes place only under an anticipable assignment of those inputs, and on $\Pi$ such assignments are, in all but finitely many periods, the outputs of settlement (\cref{lem:formalized-state:pillars}); withholding settlement leaves that production undone. For $\pP\to\pF$: under X2, each change of environment creates conflicts that no procedure in force can settle, so they are settled only after the rule system has been replaced; by \cref{lem:formalized-state:pillars} all but finitely many of these conflicts are settled, so the rule system is replaced after all but finitely many changes, and the self-government clause of Ax2$^{*}$ makes each replacement a practice of the members, so the procedures that settle the new conflicts are outputs of rule making. For $\pJ\to\pF$: under X3, \cref{lem:formalized-state:forcing}(a), applied to the inescapable disputes about the open-textured procedure, gives, almost surely on $\Pi$, all but finitely many of them disposed of by determination; an assignment in the open set of the procedure becomes anticipable only once determined, so the conflicts at issue are settled only with the output of interpretation. For $\pC\to\pF$: under X5, Lemma 3.3 of Part V with a zero deterrence margin gives a violation probability of at least $p>\theta$ in every agent-period, so withholding sanctions leaves infinitely many assignments breached without anyone being held to them, and those conflicts are unsettled by Definition 2.2(c) of Part I.
   450	
   451	\emph{Strong connectivity.} Each of $\pP$, $\pJ$, $\pI$ and $\pC$ has an arc to $\pF$, $\pF$ has an arc to $\pW$, and $\pW$ has an arc to every other function. Every function therefore reaches $\pW$ within two steps and is reached from $\pW$ in one.
   452	
   453	\emph{Cascade completeness.} For $n\in\{\pP,\pJ,\pI,\pC\}$ the arc $n\to\pF$ puts $\pF$ in $\cl(\{n\})$; the arc $\pF\to\pW$ then puts $\pW$ in it, and the arcs from $\pW$ put every function in it. The same chain starts at $\pF$, and $\cl(\{\pW\})=\Mset$ directly.
   454	
   455	\emph{Monotonicity.} Adding hyperarcs adds arcs to the underlying digraph and can only enlarge each cascade, so both properties pass from $\Dstar$ to $\mathcal{D}(G)$. The last sentence restates the theorem under the bridge hypothesis.
   456	\end{proof}
   457	
   458	\Cref{fig:hypergraph} draws $\Dstar$. Allocation rules are the hub of the dependency structure because the six problems converge on them, not because resource controllers dominate. The hub of dependency and the hub of integration are different objects. A polity in which the allocation rules are made by a dispersed legislature, interpreted by independent courts, taught by a free press and enforced by accountable police has the same $\Dstar$ as one in which a single coalition does all four, and \cref{sec:capture} shows that the two differ in $U_t$ and $\Integ_t$.
   459	
   460	\begin{proposition}[Role of each premise]
   461	\label{prop:formalized-state:minimality}
   462	\leavevmode
   463	\begin{enumerate}[label=(\alph*)]
   464	\item The refined axioms do not imply interdependence: the collective of \cref{prop:formalized-state:independence}(a) satisfies Ax1$^{*}$ to Ax6$^{*}$ and $\Struct$, and no arc of its dependency structure enters $\pW$.
   465	\item Among the arcs of $\Dstar$ and the further arcs of \cref{rem:formalized-state:further}, the only arc into $\pW$ is $\pF\to\pW$; without X1 no structure built from them is strongly connected.
   466	\item Without X5, the structure $\Dstar\setminus\{\pC\to\pF\}$ is strongly connected but not cascade-complete: $\cl(\{\pC\})=\{\pC\}$.
   467	\item Without X3, replacing $\pJ\to\pF$ by the precedent arc $\pJ\to\pP$ of \cref{rem:formalized-state:further} keeps the structure strongly connected and cascade-complete.
   468	\item If the hyperarc $(\{\pI,\pC\},\pJ)$ is replaced by the two arcs $\pI\to\pJ$ and $\pC\to\pJ$, then the cascade of $\{\pC\}$ in $\Dstar\setminus\{\pC\to\pF\}$ becomes $\Mset$.
   469	\end{enumerate}
   470	\end{proposition}
   471	
   472	\begin{proof}
   473	(a) Foraging is individual, does not depend on the campsite chosen, uses no contested input and is not governed by the rule of camp chores, so no instance of $\pW$ uses an output of another function. (b) No other listed arc has head $\pW$, and a digraph with no arc into a vertex is not strongly connected. (c) The arcs of $\Dstar$ other than $\pC\to\pF$ still give every function a path to $\pW$, since $\pC$ reaches $\pJ$ in the underlying digraph and $\pJ\to\pF$. In the cascade, $\pC$ appears in the tail of only one hyperarc, $(\{\pI,\pC\},\pJ)$, which fires only if $\pI$ has also failed. (d) $\pJ\to\pP\to\pF$ replaces $\pJ\to\pF$ in both arguments of \cref{thm:formalized-state:interdependence}. (e) With the arc $\pC\to\pJ$, the chain $\pC\to\pJ\to\pF\to\pW$ fires and $\pW$ reaches every function.
   474	\end{proof}
   475	
   476	Part (e) is the reason to use hyperarcs. The arc representation would assert that a collapse of coercion disables interpretation. Part III showed the opposite: a determination that the parties regard as legitimate settles the dispute with no sanction behind it. Part (c) shows what X5 contributes. Without it, coercion is linked to the other functions but its failure stays local, because interpretation can rest on legitimacy alone and nothing else uses coercion directly.
   477	
   478	Part V's exception for bilateral exclusion does not touch the theorem. Corollary 3.7 of Part V concerns the motivation of sanctioners: when a cheated trader simply refuses to deal again with the cheat, the refusal costs nothing and needs neither provisioning nor legitimation, so the hyperarc $(\{\pF,\pI\},\pC)$ is absent. \Cref{thm:formalized-state:interdependence} uses no arc into coercion except $\pW\to\pC$, and that arc holds for bilateral exclusion too. The trader who withholds cooperation is an agent whose consumption is counted in Ax6$^{*}$, and the cooperation withheld is itself an exchange of produced goods; without production there is nothing to withhold and nobody to withhold it. The arc out of coercion that the theorem uses, $\pC\to\pF$, rests on X5 and on Lemma 3.3 of Part V, which say only that without any response to breach the breach rate exceeds tolerance. Bilateral exclusion is one such response. When it is the only one, coercion is exercised in its most dispersed form, and the arc is unaffected.
   479	
   480	A second route from legitimation to coercion exists, and it does not rest on reading equilibrium beliefs as legitimacy. Under Ax4$^{*}$, every window contains an entrant who did not know the rule system at entry (Lemma 3.4 of Part IV). A sanction rule deters such an entrant only once the entrant can tell which conduct the others will answer with exclusion, fines or force, and the practices that supply that information to entrants are the ones Theorem 3.5 of Part IV assigns to legitimation. The argument concerns the information of particular members who arrive uninformed, not the beliefs that sanctioners hold in equilibrium. It yields the arc $\pI\to\pC$ whenever sanction rules belong to the rule system whose common knowledge Ax4$^{*}$ requires. The theorem does not need this arc, and \cref{rem:formalized-state:further} lists it with the others.
   481	
   482	Every arc of $\Dstar$ appears in the minimal forms of \cref{tab:hardcases}, without offices. Among the Ju/'hoansi, foraging feeds the people who talk disputes out and criticize stinginess ($\pW\to m$); arrow-owner rules are learned in talk that everyone hears ($\pI\to\pF$); access to territory and water runs through rights held by kin ($\pF\to\pW$); disputes over sharing are talked out ($\pJ\to\pF$); and criticism of failures to share, recorded by Wiessner, holds people to the sharing rules ($\pC\to\pF$) \citep{lee2013,wiessner2005}. Among the Nuer, cattle rights govern herding ($\pF\to\pW$), compensation in cattle after a homicide is fixed through the leopard-skin chief ($\pJ\to\pF$), and the settlement holds because the parties value it and fear renewed feud, which is the disjunction of $(\{\pI,\pC\},\pJ)$ \citep{evanspritchard1940}. In Ostrom's commons, users modify their appropriation rules through collective-choice arrangements ($\pP\to\pF$), resolve conflicts over them in local arenas ($\pJ\to\pF$), monitor and sanction appropriators ($\pC\to\pF$), and draw provision labor from the users themselves under the same rules ($\pF\to\pW$) \citep{ostrom1990}. The dependency structure is the same in a band as in an empire. What differs is who sits at each node.
   483	
   484	\begin{remark}[Further arcs]
   485	\label{rem:formalized-state:further}
   486	Other incidences yield arcs that the theorem does not need. A replaced rule coordinates behavior only once it is common knowledge, so $\pI\to\pP$ whenever rules change (Part IV, Section 3). Under changes that alter the rules of adjudication and recognition, $\pP\to\pJ$ and $\pP\to\pI$. Where determinations bind later cases, interpretation changes rules, so $\pJ\to\pP$; with the arcs $\pI\to\pP$, $\pP\to\pJ$ and $\pP\to\pI$ this makes Hart's three secondary functions mutually reachable. Where sanctions are costly public goods delivered at large scale without higher-order sanctions, $(\{\pF,\pI\},\pC)$ by Corollary 3.7 of Part V, which gives a micro-foundation for the coupling of war making and extraction that \citet{tilly1990} described. When sanctions take the form of bilateral exclusion, Part V shows that sanctioners need no provisioning or legitimation, and the hyperarc is absent. Where sanction rules belong to the rule system whose common knowledge Ax4$^{*}$ requires, informing entrants of them yields $\pI\to\pC$, as argued above.
   487	\end{remark}
   488	
   489	\section{Capture}
   490	\label{sec:capture}
   491	
   492	\subsection{Integration}
   493	
   494	The source defines cross-pillar integration descriptively, and Part II proposed a formal candidate for pairs that include rule making (Section 6 of Part II, Equation 2). The series adopts it for all fifteen pairs.
   495	
   496	\begin{definition}[Coalition-overlap integration]
   497	\label{def:formalized-state:overlap}
   498	Let $\mathcal{S}$ be a preregistered list of coherent coalitions, groups such as parties, firms, dynasties or factions that can issue joint directives. For $S\in\mathcal{S}$ and a pillar $m$, let $\kappa_m(S)\in[0,1]$ be the share of decision-relevant control in $m$ that is exercised in accordance with the directives of $S$; for $m=\pP$ it is the bloc share of Part II. Then
   499	\[
   500	C^{\ov}_{mn}=\max_{S\in\mathcal{S}}\min\{\kappa_m(S),\kappa_n(S)\}.
   501	\]
   502	\end{definition}
   503	
   504	The measure lies in $[0,1]$, equals one exactly when some listed coalition commands all of both pillars, and equals zero exactly when no listed coalition has a positive share in both. Its value depends on the coalition list, which is why the list must be fixed before coding. Write $\deg_m=\sum_{n\neq m}C_{mn}$ for the integration degree of pillar $m$.
   505	
   506	\begin{lemma}[Degree, star and clique bounds]
   507	\label{lem:formalized-state:hub}
   508	For any symmetric $C$ with entries in $[0,1]$ and $M=6$:
   509	\begin{enumerate}[label=(\alph*)]
   510	\item $\Integ=\frac{1}{M(M-1)}\sum_{m}\deg_m=\frac{1}{30}\sum_m\deg_m$;
   511	\item if $C_{mn}=0$ whenever neither $m$ nor $n$ lies in a set $A$ of $k$ pillars, then $\Integ\le\bar c\,\bigl(k(M-k)+k(k-1)/2\bigr)/15$ with $\bar c=\max_{m<n}C_{mn}$; for a single hub, $k=1$, the bound is $\bar c/3$;
   512	\item under \cref{def:formalized-state:overlap}, if a coalition $S\in\mathcal{S}$ has $\kappa_m(S)\ge c$ for every $m$ in a set $A$ of $k$ pillars, then $C_{mn}\ge c$ for all distinct $m,n\in A$ and $\Integ\ge c\,k(k-1)/30$.
   513	\end{enumerate}
   514	\end{lemma}
   515	
   516	\begin{proof}
   517	(a) Each pair $\{m,n\}$ appears in $\deg_m$ and in $\deg_n$, so $\sum_m\deg_m=2\sum_{m<n}C_{mn}$, and $\Integ=\frac{2}{M(M-1)}\sum_{m<n}C_{mn}$. (b) The pairs with at least one member in $A$ number $k(M-k)+k(k-1)/2$; each contributes at most $\bar c$ and the others contribute zero; divide by fifteen. (c) For $m,n\in A$, $C^{\ov}_{mn}\ge\min\{\kappa_m(S),\kappa_n(S)\}\ge c$. The $k(k-1)/2$ such pairs contribute at least $c\,k(k-1)/2$ to the sum, and $\Integ$ is that sum divided by fifteen.
   518	\end{proof}
   519	
   520	The lemma separates two patterns that comparative accounts often run together. In a star, one pillar is coupled to the others by different coalitions, and the remaining pillars are not coupled to one another: with $k=1$, integration cannot exceed one third of the largest coupling. In a clique, one coalition commands several pillars, and the overlap measure forces every pair among them to be coupled: a coalition that commands a share $c$ of five pillars produces $\Integ\ge2c/3$. A threshold $i^{*}$ above one third therefore cannot be met by a pure star, whatever its couplings. The distinction is the formal content of the source's warning that strong organizations do not by themselves imply a strong coalition \citep{largo2026hbs}.
   521	
   522	\subsection{The capture predicate}
   523	
   524	\begin{definition}[Capture predicate]
   525	\label{def:formalized-state:cap}
   526	Fix preregistered thresholds $(u^{*},i^{*})\in(0,1]^2$ and weights $\omega$. Let $L_t$ be the set of capture links documented at $t$, each meeting the source's three conditions. Then $\Capt_{u^{*},i^{*}}(G,t)$ holds if $U_t\ge u^{*}$, $\Integ_t\ge i^{*}$ and $L_t\neq\emptyset$. Proposition B for a polity in a period is the statement that $\Capt$ holds.
   527	\end{definition}
   528	
   529	The source's stricter classification adds documented unaccountable concentration in at least two pillars, persistent restriction of effective contestation, and a materially consequential pattern linked to the concentrated coalition \citep{largo2026hbs}. These refine the predicate and do not change its logic. The predicate is defined only when each pillar has a control-share vector, so capture presupposes that the six functions are realized. The converse is the subject of this section.
   530	
   531	\begin{lemma}[Range of unaccountable concentration]
   532	\label{lem:formalized-state:U}
   533	(a) $0\le U_t\le1$. (b) $U_t=0$ if and only if $Q_m=1$ for every $m$ with $\omega_m>0$. (c) $\min_mH_m(1-Q_m)\le U_t\le\max_mH_m(1-Q_m)$, and both bounds are attained at vertices of the weight simplex.
   534	\end{lemma}
   535	
   536	\begin{proof}
   537	Each term $H_m(1-Q_m)$ lies in $[0,1]$, and $U_t$ is their convex combination, which gives (a) and (c); the bounds of (c) are attained by putting all weight on a minimizing or a maximizing pillar. For (b), a pillar with holders has $H_m\ge1/n_m>0$, so a term with positive weight vanishes only if $Q_m=1$.
   538	\end{proof}
   539	
   540	Part (c) bounds the effect of the weights: however they are chosen, $U_t$ stays in the interval spanned by the pillar terms, which is why the source requires them to be preregistered.
   541	
   542	\subsection{Non-implication}
   543	
   544	\begin{lemma}[Separation]
   545	\label{lem:formalized-state:separation}
   546	Describe a model of a collective as a pair $(\Gamma,\Lambda)$. $\Gamma$ consists of the processes of arrivals, dispositions, hazards, temptations and margins, information partitions, and stocks and flows. $\Lambda$ consists of the role map, the control shares, the coalition list with its control shares $\kappa$, the contestability components, and the record of evidence on capture links. Call $\Lambda$ admissible if every agent it assigns to a practice is a member, or an organization of members, whose consumption is counted in Ax6$^{*}$; no party to a residual dispute alone controls its determination; and the practices of rule making are the members' own. The refined axioms, the incidence axioms, the implementation predicates and the dependency structure are, for admissible $\Lambda$, functions of $\Gamma$ alone. $U_t$, $\Integ_t$ and $L_t$ are functions of $\Lambda$ alone.
   547	\end{lemma}
   548	
   549	\begin{proof}
   550	\Cref{tab:axioms}, \cref{def:formalized-state:implementation,def:formalized-state:hypergraph} and Assumptions X1, X2, X3 and X5 (\cref{ass:formalized-state:X1,ass:formalized-state:X2,ass:formalized-state:X3,ass:formalized-state:X5}) refer to whether conflicts are settled, decisions made, disputes determined, information refined, violations met and inflows produced, and to the hazards and temptations attached to these events. None refers to a share, to a coalition, to a contestability component or to evidence of privileged access. Admissibility fixes the only clauses that mention performers: the party-control clause of $\Impl_{\pJ}$, the self-government clause of Ax2$^{*}$ and the practice clause of Ax6$^{*}$. $U_t$ is computed from shares and contestability, $\Integ_t$ from the coalition list and $\kappa$, and $L_t$ from the evidentiary record.
   551	\end{proof}
   552	
   553	\begin{theorem}[Proposition A does not imply Proposition B]
   554	\label{thm:formalized-state:nonimplication}
   555	There are four collectives, each satisfying Ax1$^{*}$ to Ax6$^{*}$ and X1, X2, X3 and X5, and hence $\Struct$ and $\Inter$, whose pairs $(U_t,\Integ_t)$ are $(0,0)$, $(0,1)$, $(1,0)$ and $(1,1)$, and of which only the last has a documented capture link. Consequently, for every pair of thresholds $(u^{*},i^{*})\in(0,1]^2$, structural necessity and interdependence hold both in a collective where $\Capt$ holds and in collectives where it fails, and neither $U_t\ge u^{*}$ nor $\Integ_t\ge i^{*}$ implies $\Capt$.
   556	\end{theorem}
   557	
   558	\begin{proof}
   559	Extend the collective of \cref{prop:formalized-state:independence}(a) to at least twelve members and adjust four components so that the incidence axioms hold. The contested plot is the field the members cultivate, so production uses an input under an anticipable assignment (X1). The environment alternates between two states, and each change brings a new kind of claim that the old rotation rule does not cover, which the members settle by voting a new rule (X2). The residual disputes concern the application of the rotation rule to boundary cases (X3). Members are tempted to take the field out of turn with $p>\theta$, and a member who does so pays a fine and is made to return the field, so the conflict counts as settled (X5). Call the resulting processes $\Gamma$. By \cref{cor:formalized-state:struct,thm:formalized-state:interdependence}, $\Gamma$ yields $\Struct$ and $\Inter$, and by \cref{lem:formalized-state:separation} it does so under any admissible assignment $\Lambda$ of the practices to agents. Four assignments give the corners. In each corner the organizations consist of members, every determination is made by an organization that contains neither party (in $(0,1)$ by all members, so neither party controls it alone), and the procedures are those of $\Gamma$ with performers relabeled, so each assignment is admissible.
   560	
   561	$(0,0)$: each pillar's practices are performed by two organizations with equal shares, the twelve organizations are distinct, $\mathcal{S}$ lists only single organizations, and $Q_m=1$ for every $m$. Then $H_m=1/2$, $U_t=0$ by \cref{lem:formalized-state:U}(b), every $C_{mn}=0$, $\Integ_t=0$, and the record contains no capture link.
   562	
   563	$(0,1)$: every member takes an equal part in every practice by consensus, the coalition of all members is listed, and $Q_m=1$. Then $U_t=0$ and, by \cref{lem:formalized-state:minimal}, $\Integ_t=1$; the record contains no capture link.
   564	
   565	$(1,0)$: each pillar's practices are performed by a single organization, the six organizations are distinct, $\mathcal{S}$ lists only single organizations, and $Q_m=0$. Then $H_m=1$, $U_t=1$, every $C_{mn}=0$, $\Integ_t=0$, and the record contains no capture link.
   566	
   567	$(1,1)$: one organization performs every practice and $Q_m=0$. Then $H_m=1$, $U_t=1$, $\kappa_m=1$ for that organization in every pillar, $\Integ_t=1$, and the record documents one capture link: the organization's discretion over determinations removes review, and a record ties that discretion to an assignment of the field.
   568	
   569	For thresholds in $(0,1]^2$, the collective at $(1,1)$ satisfies $\Capt$, the one at $(0,0)$ does not, the one at $(1,0)$ fails $\Integ_t\ge i^{*}$ although $U_t\ge u^{*}$, and the one at $(0,1)$ fails $U_t\ge u^{*}$ although $\Integ_t\ge i^{*}$.
   570	\end{proof}
   571	
   572	The theorem formalizes three of the source's commitments. Differentiated functions do not establish a common hierarchy (source Proposition 1): the corner $(1,0)$ has six monopolies and no coalition among them. Integration of functions is not capture: the corner $(0,1)$ is the minimal form of the stateless societies. And the strong claim requires both indices and a documented link, because each index alone is compatible with its absence. Structural necessity fixes the support of the role map. Capture is a claim about its values.
   573	
   574	\section{Representation and minimality}
   575	\label{sec:representation}
   576	
   577	\subsection{The Formalized State as an abstraction}
   578	
   579	The results so far concern properties that every functioning collective has. This section states them as a single claim about an abstraction. The Formalized State is not a form of government. It is a class of mathematical structures, and the claim is that every governance system, whatever its period, ideology, institutions or degree of centralization, is represented by a member of the class. Historical regimes are instances. The name ``Beast System'' is the series' typological reading of the abstraction (\cref{sec:revelation}); it is not a conclusion of any theorem.
   580	
   581	\begin{definition}[Formalized State structure]
   582	\label{def:formalized-state:F}
   583	A \emph{Formalized State structure} is a tuple $F=(V,\rho,A,s,Q,\omega,\mathcal{S},\kappa,L,\mathcal{D})$ in which $V$ is a finite nonempty set of actors, $\rho:V\to2^{\Mset}$ is a role map, $A=(A^m)_{m\in\Mset}$ are layers with entries in $[0,1]$, $s=(s^m)_{m\in\Mset}$ are vectors on $V$, $Q\in[0,1]^{\Mset}$, $\omega$ is a weight vector on $\Mset$, $\mathcal{S}$ is a list of subsets of $V$ with control shares $\kappa_m(S)\in[0,1]$, $L$ is a finite set of capture links $(i\to j,m)$ with $i,j\in V$, and $\mathcal{D}$ is a set of hyperarcs on $\Mset$, subject to four conditions. Write $V_m=\{v\in V:m\in\rho(v)\}$.
   584	\begin{enumerate}[label=(F\arabic*)]
   585	\item Every function has a holder: $V_m\neq\emptyset$ for every $m\in\Mset$.
   586	\item Control lies with holders: each $s^m$ is a probability vector with $s^m_v>0$ only if $v\in V_m$, and $a^m_{ij}>0$ only if $i\in V_m$.
   587	\item The measurement components are in range: $\omega\ge0$ with $\sum_m\omega_m=1$.
   588	\item The dependency structure contains $\Dzero$ and is strongly connected and cascade-complete.
   589	\end{enumerate}
   590	The class of all such structures is $\mathcal{F}$. Each $F\in\mathcal{F}$ determines $H_m$, $U$, $C^{\ov}_{mn}$, $\Integ$ and the capture predicate by the formulas of \cref{sec:model,sec:capture}.
   591	\end{definition}
   592	
   593	The definition is purely mathematical. It does not mention any society, and checking whether a tuple belongs to $\mathcal{F}$ requires no knowledge of governance. Membership in $\mathcal{G}$, conversely, is checked without the pillars (\cref{def:formalized-state:collective}). The bridge between the two classes is a map that reads a structure off the coded record of a collective.
   594	
   595	\begin{definition}[Profile map]
   596	\label{def:formalized-state:profile}
   597	Let $G\in\mathcal{G}$ come with a coded record that lists, for each practice that recurs on $\Pi$, the actors who perform it and the actors it constrains, together with the contestability components, a preregistered coalition list with the share of each pillar's control that each coalition directs, the documented capture links, and preregistered weights. The \emph{profile} $\pi(G)=(V_G,\rho_G,A_G,s_G,Q_G,\omega,\mathcal{S}_G,\kappa_G,L_G,\mathcal{D}(G))$ is built in five steps.
   598	\begin{enumerate}[label=(\roman*)]
   599	\item $V_G$ is the set of actors who perform some practice.
   600	\item $m\in\rho_G(v)$ if and only if $\Impl_m(G)$ holds and $v$ performs a practice of the class that \cref{def:formalized-state:implementation} assigns to $m$. A function that is not implemented receives no holders.
   601	\item $s^m_G$ is computed by the share rule of the Part that owns $m$: the stake-weighted share of last words for $\pJ$ (Part III, Section 2), the power index of the decision procedure for $\pP$ (Part II, Section 2), deployment command for $\pC$ (Definition 2.2 of Part V), and the corresponding rules of Parts I, IV and VI. $A^m_G$ records the documented constraints.
   602	\item $Q_G$, $\omega$, $\mathcal{S}_G$, $\kappa_G$ and $L_G$ are copied from the record.
   603	\item $\mathcal{D}(G)$ is the dependency structure of \cref{def:formalized-state:hypergraph}.
   604	\end{enumerate}
   605	The record is well formed: each share rule returns a probability vector supported on the actors who perform practices of $m$, a constraint $(i,j,m)$ is recorded only if $i$ performs a practice of $m$, and the weights are nonnegative and sum to one. For $G\in\mathcal{G}$ and $F\in\mathcal{F}$, write $G\cong_AF$ if there is a bijection $\beta:V_G\to V_F$ that carries every component of $\pi(G)$ to the corresponding component of $F$. For $G,G'\in\mathcal{G}$ write $G\cong_AG'$ if a bijection $V_G\to V_{G'}$ carries $\pi(G)$ to $\pi(G')$.
   606	\end{definition}
   607	
   608	The profile is well defined on coded records. Steps (i), (ii), (iv) and (v) are determined by the record and the definitions, and step (iii) applies share rules that the pillar Parts fixed in advance; two codings of the same record differ at most by a relabeling of actors, which $\cong_A$ ignores. The relation $\cong_A$ is equivalence in the governance properties the abstraction keeps. It is not isomorphism of social detail, and the next lemma says exactly what is kept and what is not.
   609	
   610	\begin{lemma}[Preserved and forgotten properties]
   611	\label{lem:formalized-state:preserved}
   612	If $G\cong_AF$, then $G$ and $F$ have the same role map, control shares, concentrations $H_m$, contestability $Q_m$, unaccountable concentration $U$, couplings $C^{\ov}_{mn}$, integration $\Integ$, capture predicate for every threshold pair, dependency structure, and interdependence predicate, all up to the relabeling $\beta$. The relation $\cong_A$ does not preserve, and the abstraction does not represent, the content of the rules, the beliefs that legitimate them, the particular procedures that implement each function, the identities and histories of actors beyond their labels, the levels of capacity $x_t$, the quality or welfare consequences of decisions, or any moral evaluation of the system.
   613	\end{lemma}
   614	
   615	\begin{proof}
   616	Each preserved quantity is a function of the components that $\beta$ carries over: $H_m$ of $s^m$; $U$ of $s$, $Q$ and $\omega$; $C^{\ov}_{mn}$ and $\Integ$ of $\mathcal{S}$ and $\kappa$; the capture predicate of $U$, $\Integ$ and $L$; interdependence of $\mathcal{D}$. The forgotten items are not components of $\pi(G)$, so collectives that differ only in them have the same profile. Two examples show that the loss is real: a consensus band and a council of equals in a commons with the same number of members, the same contestability and the same dependency structure have the same image, and so do two monarchies that differ only in their official religion.
   617	\end{proof}
   618	
   619	\subsection{The representation theorem}
   620	
   621	\begin{theorem}[Representation]
   622	\label{thm:formalized-state:representation}
   623	Let $G\in\mathcal{G}$ come with a well-formed coded record.
   624	\begin{enumerate}[label=(\alph*)]
   625	\item $G\cong_AF$ for some $F\in\mathcal{F}$ if and only if $\Struct(G)$ and $\Inter(G)$ hold.
   626	\item If $G$ satisfies Ax1$^{*}$ to Ax6$^{*}$ and X1, X2, X3 and X5, then $F_G=\pi(G)$ belongs to $\mathcal{F}$ and $G\cong_AF_G$.
   627	\item If every functioning human collective satisfies the refined and incidence axioms, then for every $G\in\mathcal{G}$ there is $F_G\in\mathcal{F}$ with $G\cong_AF_G$.
   628	\end{enumerate}
   629	\end{theorem}
   630	
   631	\begin{proof}
   632	(a) Suppose $\Struct(G)$ and $\Inter(G)$. Each $\Impl_m(G)$ requires practices of $m$'s class that recur on $\Pi$, so step (ii) gives every function at least one holder, which is (F1). Since control in each pillar is exercised, the share rule of step (iii) yields a probability vector supported on the actors who exercise it, and documented constraints run only from holders, which is (F2). (F3) holds for preregistered weights. $\Struct(G)$ gives $\Dzero\subseteq\mathcal{D}(G)$ and $\Inter(G)$ gives strong connectivity and cascade completeness, which is (F4). So $\pi(G)\in\mathcal{F}$, and the identity map gives $G\cong_A\pi(G)$. Conversely, if $G\cong_AF$ with $F\in\mathcal{F}$, then by (F1) every function of $G$ has a holder, which by step (ii) happens only if $\Impl_m(G)$ holds for every $m$; by (F4) $\mathcal{D}(G)=\mathcal{D}_F$ contains $\Dzero$ and is strongly connected and cascade-complete, so $\Struct(G)$ and $\Inter(G)$ hold. (b) \Cref{cor:formalized-state:struct} and \cref{thm:formalized-state:interdependence} give $\Struct(G)$ and $\Inter(G)$, and (a) applies with $F_G=\pi(G)$. (c) is (b) under the bridge hypothesis.
   633	\end{proof}
   634	
   635	Universality over real governance systems is part (b) together with the empirical bridge that every functioning collective satisfies the refined and incidence axioms, which historical observation supports.
   636	
   637	Part (a) locates the content of the theorem. The profile map is defined for every collective, so the existence of a map is not the claim. The claim is that the image lands in $\mathcal{F}$: that every functioning collective has six nonempty layers with well-defined control shares and an interdependent dependency structure. That is exactly Proposition A, so the representation theorem is Proposition A stated as a property of an abstraction, and its proof runs through \cref{thm:formalized-state:A,thm:formalized-state:interdependence}. The representation can fail. The six collectives of \cref{prop:formalized-state:independence}(b) each have a function with no holders, so by (a) no structure in $\mathcal{F}$ represents them; the collective of \cref{prop:formalized-state:independence}(a) has all six functions but no arc into production (\cref{prop:formalized-state:minimality}(a)), so it fails (F4) and is not represented either. Whether a real collective is represented is therefore an empirical question, and the bridge hypothesis is the claim that the answer is always yes.
   638	
   639	Four results of the paper should be kept apart. Representation (\cref{thm:formalized-state:representation}) says that every governance system is an instance of the abstraction. Necessity (\cref{thm:formalized-state:A,thm:formalized-state:interdependence}) says why: the properties that membership requires follow from primitive axioms about collective life. Minimality (\cref{prop:formalized-state:minimality6}) says that no coarsening of the abstraction preserves the same properties. Uniqueness (\cref{thm:formalized-state:uniqueness,thm:formalized-state:six}) says that the abstraction is the coarsest one that does, up to a unique isomorphism, and that it has exactly six dimensions.
   640	
   641	\subsection{Minimality}
   642	
   643	Write $\mathcal{G}_*$ for the governance systems that satisfy Ax1$^{*}$ to Ax6$^{*}$, X1, X2, X3 and X5 and come with a well-formed coded record, and $P(G)$ for the isomorphism class of $\pi(G)$ under relabeling of actors. $P(G)$ is the \emph{preserved property set}: it determines the role map, the control shares, $H_m$, $Q_m$, $U$, $C^{\ov}_{mn}$, $\Integ$, the capture predicate and the dependency structure, and by \cref{def:formalized-state:profile} $G\cong_AG'$ if and only if $P(G)=P(G')$.
   644	
   645	An abstraction with fewer or other functional dimensions is obtained by a \emph{coarsening}. A coarsening is a map $c:\Mset\to K\cup\{\bot\}$ into a finite set $K$ whose image contains $K$, so that every block $c^{-1}(k)$ is nonempty, together with weights $\lambda_m>0$ that sum to one on each block $c^{-1}(k)$. It sends a structure to the structure indexed by $K$ in which block $k$ has holders $\bigcup_{m\in c^{-1}(k)}V_m$, shares $\sum_{m\in c^{-1}(k)}\lambda_ms^m$, layers, contestability and coalition shares formed with the same weights, and weight $\sum_{m\in c^{-1}(k)}\omega_m$; pillars with $c(m)=\bot$ are dropped, and the hyperarcs are the images under $c$ of the hyperarcs that contain no dropped pillar, with self-loops removed. Write $\Phi_c(G)$ for the coarsened image of $\pi(G)$, up to relabeling of actors. The identity coarsening gives $\Phi=\Phi_{\mathrm{id}}$, and $\Phi(G)=P(G)$. The source's five-function model is the coarsening that merges $\pP$ and $\pJ$ \citep{largo2026hbs}.
   646	
   647	\begin{proposition}[Minimality]
   648	\label{prop:formalized-state:minimality6}
   649	Let $(c,\lambda)$ be a coarsening that is not a bijection from $\Mset$ onto $K$. Then there are $G_1,G_2\in\mathcal{G}_*$ with $\Phi_c(G_1)=\Phi_c(G_2)$ and $P(G_1)\neq P(G_2)$. Explicitly:
   650	\begin{enumerate}[label=(\alph*)]
   651	\item if $c(m)=\bot$ for some $m$, $G_1$ and $G_2$ differ only in that $m$ is held by one organization $a$ in $G_1$, with $s^m=(1,0)$ on $(a,b)$, and by $a$ and $b$ equally in $G_2$, with $s^m=(1/2,1/2)$; then $H_m=1$ in $G_1$ and $H_m=1/2$ in $G_2$;
   652	\item if $c(m)=c(n)\neq\bot$ for some $m\neq n$, let $\mu=\lambda_m/(\lambda_m+\lambda_n)$; $G_1$ has $s^m=(1,0)$ and $s^n=(0,1)$ on $(a,b)$, and $G_2$ has $s^m=s^n=(\mu,1-\mu)$, with the same $Q_m=Q_n$ and with $\mathcal{S}$ listing single organizations; then $C^{\ov}_{mn}=0$ in $G_1$ and $\max\{\mu,1-\mu\}\ge1/2$ in $G_2$, so $\Integ$ differs by at least $1/30$, and $H_m=H_n=1$ in $G_1$ against $\mu^2+(1-\mu)^2<1$ in $G_2$.
   653	\end{enumerate}
   654	\end{proposition}
   655	
   656	\begin{proof}
   657	A coarsening whose restriction to the pillars not sent to $\bot$ is not a bijection onto $K$ either sends some pillar to $\bot$ or sends two pillars to the same element of $K$. In both cases start from the collective $\Gamma$ in the proof of \cref{thm:formalized-state:nonimplication}, let two organizations $a$ and $b$ perform the practices of the pillars named, code every other pillar identically in $G_1$ and $G_2$, and set the layers proportional to the shares, $a^{l}_{aj}=s^{l}_a$ and $a^{l}_{bj}=s^{l}_b$ for the pillars $l$ named and every other actor $j$. Since $a$ and $b$ are organizations of members that are parties to no residual dispute, both assignments are admissible, and by \cref{lem:formalized-state:separation} $G_1$ and $G_2$ satisfy every axiom, since they differ only in the assignment of control, so both lie in $\mathcal{G}_*$.
   658	
   659	(a) So that both collectives have the same actor set, let $a$ and $b$ also hold equal shares $(1/2,1/2)$ in one pillar $l_0\neq m$, with $c(l_0)\in K$ when $K\neq\emptyset$, identically in $G_1$ and $G_2$; in $G_1$ the organization $b$, which holds nothing in $m$, still performs practices of $l_0$. Dropping $m$ deletes its layer, shares, contestability and coalition shares, removes $m$ from every actor's roles, and deletes every hyperarc that contains $m$. What remains is identical in $G_1$ and $G_2$, so $\Phi_c(G_1)=\Phi_c(G_2)$; if $K=\emptyset$, both images consist of the actor set alone and coincide. The concentration $H_m=1^2=1$ in $G_1$ and $H_m=2\cdot(1/2)^2=1/2$ in $G_2$; a relabeling of actors does not change $H_m$, so $P(G_1)\neq P(G_2)$.
   660	
   661	(b) Here $a$ performs practices of $m$ and $b$ of $n$ in $G_1$, and both perform both in $G_2$, so the actor sets coincide; $a$ and $b$ perform no practice of any other pillar. In the block containing $m$ and $n$, the weighted shares of $m$ and $n$ contribute $\lambda_m(1,0)+\lambda_n(0,1)=(\lambda_m,\lambda_n)$ in $G_1$ and $(\lambda_m+\lambda_n)(\mu,1-\mu)=(\lambda_m,\lambda_n)$ in $G_2$. The coalition shares of the single organizations are $\kappa_l(\{a\})=s^l_a$ and $\kappa_l(\{b\})=s^l_b$, so they combine in the same way, as do the layers. Every other component is identical, so $\Phi_c(G_1)=\Phi_c(G_2)$. Before coarsening, $C^{\ov}_{mn}=\max\{\min(1,0),\min(0,1)\}=0$ in $G_1$ and $\max\{\min(\mu,\mu),\min(1-\mu,1-\mu)\}=\max\{\mu,1-\mu\}\ge1/2$ in $G_2$; the other fourteen couplings coincide, so $\Integ$ differs by at least $(1/2)/15=1/30$. The concentrations are $1$ against $\mu^2+(1-\mu)^2$, which is less than one for $\mu\in(0,1)$. These quantities are invariant under relabeling, so $P(G_1)\neq P(G_2)$.
   662	\end{proof}
   663	
   664	The independence of the axioms gives a stronger form of (a) on all of $\mathcal{G}$. The collectives of \cref{prop:formalized-state:independence}(a) and \cref{prop:formalized-state:independence}(b), coded with the same actors for the other five functions, have the same image after dropping $m_k$, although the first implements $m_k$ and the second does not. If one function were implied by the other five, dropping it would lose nothing. Part (b) shows what the source loses by merging rule making with interpretation: a polity whose legislature and courts are held by different organizations and one in which both share both functions in the same proportions have the same five-function image and different integration.
   665	
   666	\subsection{Uniqueness}
   667	
   668	\begin{definition}[Abstractions]
   669	\label{def:formalized-state:abstraction}
   670	Fix a countable universe of actor labels and dates, and let $\mathcal{G}_*$ consist of the governance systems in it whose coded records use those labels, so that $\mathcal{G}_*$ is a set. An \emph{abstraction} is a surjective map $\alpha:\mathcal{G}_*\to S_\alpha$ onto a set. It is \emph{$P$-preserving} if $P$ factors through it: $\alpha(G)=\alpha(G')$ implies $P(G)=P(G')$. A \emph{morphism} $\alpha\to\beta$ is a map $h:S_\alpha\to S_\beta$ with $h\circ\alpha=\beta$. Write $\mathbf{Abs}_P$ for the category of $P$-preserving abstractions and their morphisms. The \emph{Formalized State abstraction} is $\Phi:\mathcal{G}_*\to\mathcal{F}_*$, $\Phi(G)=[\pi(G)]$, where $\mathcal{F}_*$ is the set of isomorphism classes of structures in $\mathcal{F}$ that represent some $G\in\mathcal{G}_*$.
   671	\end{definition}
   672	
   673	Composition is composition of maps and the identity map is the identity morphism, so $\mathbf{Abs}_P$ is a category. Because abstractions are surjective, there is at most one morphism between two abstractions: $h$ is determined on $S_\alpha=\alpha(\mathcal{G}_*)$ by $h(\alpha(G))=\beta(G)$.
   674	
   675	\begin{theorem}[Uniqueness]
   676	\label{thm:formalized-state:uniqueness}
   677	Relative to the axioms Ax1$^{*}$ to Ax6$^{*}$, X1, X2, X3 and X5 and the preserved property set $P$:
   678	\begin{enumerate}[label=(\alph*)]
   679	\item $\Phi$ is an object of $\mathbf{Abs}_P$, and two systems have the same image under $\Phi$ if and only if $G\cong_AG'$;
   680	\item $\Phi$ is terminal in $\mathbf{Abs}_P$: for every $P$-preserving abstraction $\alpha$ there is exactly one morphism $\alpha\to\Phi$, so $\Phi$ is the coarsest $P$-preserving abstraction;
   681	\item every terminal object of $\mathbf{Abs}_P$ is isomorphic to $\Phi$ by a unique isomorphism;
   682	\item for each $G\in\mathcal{G}_*$, the representing structure $F_G$ is unique up to isomorphism: if $G\cong_AF$ and $G\cong_AF'$ with $F,F'\in\mathcal{F}$, then $F$ and $F'$ are isomorphic.
   683	\end{enumerate}
   684	\end{theorem}
   685	
   686	\begin{proof}
   687	(a) By \cref{thm:formalized-state:representation}(b), $\pi(G)\in\mathcal{F}$ for every $G\in\mathcal{G}_*$, so $\Phi$ is well defined, and it is surjective onto $\mathcal{F}_*$ by the definition of $\mathcal{F}_*$. $\Phi(G)=\Phi(G')$ means $[\pi(G)]=[\pi(G')]$, which is $P(G)=P(G')$, which is $G\cong_AG'$. In particular $\Phi(G)=\Phi(G')$ implies $P(G)=P(G')$, so $\Phi$ is $P$-preserving.
   688	
   689	(b) Let $\alpha$ be $P$-preserving. Define $h:S_\alpha\to\mathcal{F}_*$ by $h(\alpha(G))=\Phi(G)$. The definition does not depend on the choice of $G$: if $\alpha(G)=\alpha(G')$, then $P(G)=P(G')$ because $\alpha$ is $P$-preserving, and so $\Phi(G)=\Phi(G')$ by (a). Every point of $S_\alpha$ has the form $\alpha(G)$, so $h$ is defined on all of $S_\alpha$, and $h\circ\alpha=\Phi$ by construction. Any morphism $h':\alpha\to\Phi$ satisfies $h'(\alpha(G))=\Phi(G)=h(\alpha(G))$ for every $G$, so $h'=h$. The partition of $\mathcal{G}_*$ induced by $\alpha$ therefore refines the one induced by $\Phi$, which is the partition into $\cong_A$-classes; no $P$-preserving abstraction is coarser.
   690	
   691	(c) Let $\Psi$ be terminal in $\mathbf{Abs}_P$. Terminality of $\Phi$ gives a unique morphism $f:\Psi\to\Phi$, and terminality of $\Psi$ gives a unique morphism $g:\Phi\to\Psi$. Then $f\circ g$ is a morphism $\Phi\to\Phi$, and the identity is another; terminality of $\Phi$ allows only one, so $f\circ g=\mathrm{id}$. In the same way $g\circ f=\mathrm{id}$ on $\Psi$. So $f$ is an isomorphism, and it is the only morphism $\Psi\to\Phi$, hence the only isomorphism.
   692	
   693	(d) A relation $G\cong_AF$ is a bijection $\beta:V_G\to V_F$ carrying $\pi(G)$ to $F$, and $G\cong_AF'$ is a bijection $\beta'$ carrying $\pi(G)$ to $F'$. The bijection $\beta'\circ\beta^{-1}:V_F\to V_{F'}$ carries every component of $F$ to the corresponding component of $F'$, so $F$ and $F'$ are isomorphic.
   694	\end{proof}
   695	
   696	\begin{theorem}[Six dimensions]
   697	\label{thm:formalized-state:six}
   698	Relative to the same axioms and the same $P$, let $(c,\lambda)$ be a coarsening. The abstraction $\Phi_c$ is $P$-preserving if and only if $c$ is a bijection from $\Mset$ onto $K$. Every $P$-preserving coarsening $\Phi_c$ therefore has exactly $|K|=6$ dimensions, in a bijection with $\{\pF,\pP,\pJ,\pI,\pC,\pW\}$ that is unique up to relabeling of the dimensions, and it is isomorphic to $\Phi$ in $\mathbf{Abs}_P$.
   699	\end{theorem}
   700	
   701	\begin{proof}
   702	If $c$ is not a bijection onto $K$, \cref{prop:formalized-state:minimality6} gives $G_1,G_2$ with $\Phi_c(G_1)=\Phi_c(G_2)$ and $P(G_1)\neq P(G_2)$, so $\Phi_c$ is not $P$-preserving. If $c$ is a bijection, every block is a single pillar with weight one, so $\Phi_c(G)$ is $\pi(G)$ with its pillar labels renamed by $c$, up to relabeling of actors; $\Phi_c(G)=\Phi_c(G')$ holds exactly when $\Phi(G)=\Phi(G')$, so $\Phi_c$ is $P$-preserving, and the renaming is a bijection $h$ with $h\circ\Phi=\Phi_c$, an isomorphism in $\mathbf{Abs}_P$. A bijection from a six-element set onto $K$ forces $|K|=6$. Two such bijections $c,c'$ differ by the bijection $c'\circ c^{-1}$ of $K$, which is a relabeling of the dimensions.
   703	\end{proof}
   704	
   705	\begin{remark}[Scope of uniqueness]
   706	\label{rem:formalized-state:scope}
   707	Uniqueness is the universal property of \cref{thm:formalized-state:uniqueness} together with the count of \cref{thm:formalized-state:six}. Both are relative to the axioms and to the preserved property set $P$. A different choice of $P$, for instance one that also kept the content of legitimating beliefs, would yield a different abstraction, which would again be unique for its own $P$ by the same argument. \Cref{thm:formalized-state:six} concerns coarsenings, whose blocks aggregate pillar data with the weights $\lambda$; an abstraction that groups pillars but keeps each pillar's components separately is $\Phi$ relabeled and is not a coarsening; an abstraction that splits a class, such as coercion into policing and war making, is $P$-preserving and factors through $\Phi$ by \cref{thm:formalized-state:uniqueness}(b), so it is finer and not minimal.
   708	\end{remark}
   709	
   710	The universal property is close to the definition of $P$, and that is its point: once the properties to be preserved are fixed, the coarsest abstraction preserving them is determined up to unique isomorphism. The substantive content lies elsewhere. \Cref{thm:formalized-state:representation} shows that the coarsest abstraction lands in the class $\mathcal{F}$ of six-layer structures with an interdependent dependency hypergraph, which requires necessity, and \cref{thm:formalized-state:six} shows that its six dimensions cannot be reduced or merged, which requires the explicit witnesses of \cref{prop:formalized-state:minimality6}.
   711	
   712	\section{Capture tendencies and checks}
   713	\label{sec:tendencies}
   714	
   715	\subsection{Conditional capture axioms}
   716	
   717	Capture is contingent, but it is not random. Three mechanisms recur in the literature on oligarchy and rent seeking, and each can be stated as a conditional axiom.
   718	
   719	\begin{assumption}[T1, delegation]
   720	\label{ass:formalized-state:T1}
   721	In an organization that holds control in some pillar, a leadership extracts a rent, and members can monitor it only at private cost, as in Assumption 6.1 of Part II.
   722	\end{assumption}
   723	
   724	Under T1, Proposition 6.2 of Part II shows that monitoring by members vanishes once the organization is large enough, so the leadership is never replaced, while an organized opposition faction that monitors replaces it with a probability that does not depend on size. This is the mechanism behind Michels's iron law of oligarchy \citep{michels1915}, and its exceptions are the cases in which an organized opposition survived: the internal party system of the typographers' union that \citet{lipset1956} studied, and the revitalized unions in which \citet{voss2000} found the iron law broken. \Citet{cassinelli1953} had already argued that the law is a tendency with conditions rather than a law.
   725	
   726	\begin{assumption}[T2, organization asymmetry]
   727	\label{ass:formalized-state:T2}
   728	Coalitions with concentrated stakes organize at lower cost per member than coalitions with diffuse stakes, so their rate of converting control in one pillar into control in another is higher.
   729	\end{assumption}
   730	
   731	T2 is the logic of collective action of \citet{olson1965} applied across pillars, and the economic theory of regulation of \citet{stigler1971} applied to rule making. Mosca's observation that an organized minority prevails over an unorganized majority is an older statement of the same asymmetry \citep{mosca1939}.
   732	
   733	\begin{assumption}[T3, conversion against contestability]
   734	\label{ass:formalized-state:T3}
   735	A coalition's control in pillar $m$ converts into control in pillar $n$ at a rate $\eta_{nm}(1-Q_n)$ with $\eta_{nm}\ge0$, so contestability in the target pillar blocks conversion in proportion.
   736	\end{assumption}
   737	
   738	For $m=\pF$ the empirical counterpart of $\eta_{nm}$ is the conversion elasticity of Definition 6.1 of Part I. Walzer called the conversion of dominance in one sphere into dominance in another the defining mark of tyranny \citep{walzer1983}, and T3 states the condition under which conversion is checked: the source's second proposition, that independent review and voice interrupt transmission \citep{largo2026hbs}.
   739	
   740	\subsection{Conversion dynamics}
   741	
   742	\begin{definition}[Conversion dynamics]
   743	\label{def:formalized-state:conversion}
   744	Fix a coalition $S$ and let $y_t\in[0,1]^M$ collect its control shares $y_{m,t}=\kappa_m(S)$ at date $t$. Let $\delta\in[0,1]^M$ be the rates at which the coalition loses control in each pillar through replacement, turnover or exit, and let $K\ge0$ be an $M\times M$ matrix with zero diagonal, row sums at most one, and entries $K_{nm}=\eta_{nm}(1-Q_n)$. The coalition's shares follow
   745	\[
   746	y_{n,t+1}=(1-\delta_n)\,y_{n,t}+(1-y_{n,t})\,(Ky_t)_n .
   747	\]
   748	Write $A=\operatorname{diag}(1-\delta)+K$ and $\Integ(S)_t=\frac{1}{15}\sum_{m<n}\min\{y_{m,t},y_{n,t}\}$, the coalition's contribution to integration, which is a lower bound on $\Integ_t$ by \cref{def:formalized-state:overlap}.
   749	\end{definition}
   750	
   751	\begin{theorem}[Closure and reversibility]
   752	\label{thm:formalized-state:conversion}
   753	Under \cref{def:formalized-state:conversion}:
   754	\begin{enumerate}[label=(\alph*)]
   755	\item the dynamics map $[0,1]^M$ into itself, and $y_{t+1}\le Ay_t$ componentwise;
   756	\item if the spectral radius satisfies $\rho(A)<1$, then $y_t\to0$ and $\Integ(S)_t\to0$ geometrically from every initial state, so every foothold of the coalition is reversible;
   757	\item if $Q_n=1$ and $\delta_n>0$ for some pillar $n$, then $y_{n,t}=(1-\delta_n)^ty_{n,0}$, every pair containing $n$ contributes nothing in the limit, and $\limsup_t\Integ(S)_t\le10/15$;
   758	\item if $\delta_n=0$ for some pillar $n$, then $y_{n,t}$ is nondecreasing, so a foothold in $n$ never decays, and $\rho(A)\ge1$;
   759	\item $\rho(A)$ is nonincreasing in each $Q_n$;
   760	\item if $K$ is irreducible, $\max_n\delta_n<1$ and $\rho(A)>1$, let $v>0$ be the left Perron vector of $A$, $\bar\kappa$ the largest column sum of $K$, and $c=\bar\kappa\max_nv_n/(\min_nv_n)^2$. Then for every $y_0\neq0$ and every $t$,
   761	\[
   762	v^{\top}y_t\ \ge\ \min\Bigl\{v^{\top}y_0,\ (1-\max_n\delta_n)\frac{\rho(A)-1}{2c}\Bigr\}>0,
   763	\]
   764	so the coalition's foothold never vanishes.
   765	\end{enumerate}
   766	\end{theorem}
   767	
   768	\begin{proof}
   769	(a) If $y\in[0,1]^M$ then $(Ky)_n\in[0,1]$ because $K\ge0$ has row sums at most one. Hence $y_{n,t+1}\ge0$, and $y_{n,t+1}\le(1-\delta_n)y_{n,t}+1-y_{n,t}=1-\delta_ny_{n,t}\le1$. Since $1-y_{n,t}\le1$ and $(Ky_t)_n\ge0$, $y_{n,t+1}\le(1-\delta_n)y_{n,t}+(Ky_t)_n=(Ay_t)_n$.
   770	
   771	(b) $A\ge0$, so $z\le z'$ implies $Az\le Az'$, and induction on (a) gives $0\le y_t\le A^ty_0$. When $\rho(A)<1$, for any $r\in(\rho(A),1)$ there is a constant $b$ with $\|A^t\|\le br^t$ for all $t$, so $y_t\to0$ geometrically, and $\Integ(S)_t\le\max_my_{m,t}$ does too.
   772	
   773	(c) $Q_n=1$ makes row $n$ of $K$ zero, so $y_{n,t+1}=(1-\delta_n)y_{n,t}$. Each of the five pairs containing $n$ contributes at most $y_{n,t}\to0$, and the other ten contribute at most one each.
   774	
   775	(d) With $\delta_n=0$, $y_{n,t+1}-y_{n,t}=(1-y_{n,t})(Ky_t)_n\ge0$. Since $A\ge\operatorname{diag}(1-\delta)\ge0$ entrywise and the spectral radius is monotone on nonnegative matrices \citep{horn2012}, $\rho(A)\ge\max_n(1-\delta_n)=1$.
   776	
   777	(e) Raising $Q_n$ lowers or leaves unchanged every entry of row $n$ of $K$, hence of $A$, and monotonicity of the spectral radius applies.
   778	
   779	(f) By the Perron-Frobenius theorem for irreducible nonnegative matrices \citep{horn2012}, $\rho=\rho(A)$ has a left eigenvector $v$ with positive entries. Write $V_t=v^{\top}y_t$, which is positive when $y_t\neq0$. From the dynamics,
   780	\[
   781	V_{t+1}=v^{\top}Ay_t-\sum_nv_ny_{n,t}(Ky_t)_n=\rho V_t-\sum_nv_ny_{n,t}(Ky_t)_n .
   782	\]
   783	The subtracted sum is at most $\max_nv_n\cdot\max_ny_{n,t}\cdot\sum_n(Ky_t)_n\le\max_nv_n\cdot\|y_t\|_1\cdot\bar\kappa\|y_t\|_1$, and $\|y_t\|_1\le V_t/\min_nv_n$, so it is at most $cV_t^2$. Irreducibility with $M\ge2$ gives $K\neq0$, so $c>0$. Let $\varepsilon=(\rho-1)/(2c)$. If $V_t\le\varepsilon$ then $V_{t+1}\ge V_t(\rho-cV_t)\ge V_t(\rho+1)/2\ge V_t$. In every case $V_{t+1}\ge v^{\top}\operatorname{diag}(1-\delta)y_t\ge(1-\max_n\delta_n)V_t$, because the term $(1-y_t)\circ Ky_t$ is nonnegative. Let $\mu$ be the right side of the displayed bound and suppose $V_t\ge\mu$. If $V_t\le\varepsilon$ then $V_{t+1}\ge V_t\ge\mu$; if $V_t>\varepsilon$ then $V_{t+1}\ge(1-\max_n\delta_n)\varepsilon\ge\mu$. Since $V_0\ge\mu$, induction gives $V_t\ge\mu$ for all $t$.
   784	\end{proof}
   785	
   786	The theorem gives the source's vocabulary of closure and reversibility a precise meaning. Capture is reversible when the replacement rates outrun the conversion rates in the sense that $\rho(A)<1$, and closed when conversion along a strongly connected set of channels outruns replacement. Part (c) is a formal version of the source's second proposition: full contestability in one pillar with any positive replacement rate in it caps a coalition's integration at two thirds, whatever happens in the other five. Part (d) states the cost of entrenchment: a pillar in which the coalition cannot be replaced holds every foothold it gains.
   787	
   788	\begin{corollary}[Oligarchy and replacement]
   789	\label{cor:formalized-state:michels}
   790	Under T1, if the organization that holds the coalition's control in pillar $n$ is larger than the threshold of Proposition 6.2(a) of Part II and faces no organized opposition, then its leadership is never replaced, $\delta_n=0$ for the leadership's control, and by \cref{thm:formalized-state:conversion}(d) its foothold in $n$ never decays. An organized opposition faction that monitors, as in Proposition 6.2(b) of Part II, makes the replacement probability positive and independent of size. Reversibility in the sense of \cref{thm:formalized-state:conversion}(b) requires a positive replacement rate in every pillar.
   791	\end{corollary}
   792	
   793	\begin{proof}
   794	The first two statements are Proposition 6.2 of Part II read as statements about $\delta_n$. The last follows from \cref{thm:formalized-state:conversion}(d): if $\delta_n=0$ then $y_{n,t}\ge y_{n,0}$ for all $t$, so $y_t\not\to0$ from any initial state with $y_{n,0}>0$.
   795	\end{proof}
   796	
   797	The corollary connects the oldest theory of capture with the checks that interrupt it. Organized opposition, contested elections, term limits, judicial tenure that does not depend on the coalition, and the exit of members all raise replacement rates. Disclosure, independent review, open entry and protected speech raise contestability and lower conversion rates. The first family acts on the diagonal of $A$ and the second on its off-diagonal entries. Neither family alone guarantees reversibility, and by part (c) a single pillar that has both caps integration.
   798	
   799	\subsection{Pillar-capacity dynamics}
   800	
   801	The source's aggregate dynamics $x_{t+1}=B_tx_t+D_tz_t+\varepsilon_t$ describe capacities rather than coalition shares, and the source warns that stability cannot be read off positive links \citep{largo2026hbs}. Interdependence says something about the shape of the dominant mode, and nothing about its size.
   802	
   803	\begin{proposition}[Common mode under interdependence]
   804	\label{prop:formalized-state:perron}
   805	Let $B_t=B\ge0$ for all $t$, and suppose $B_{mn}>0$ whenever $n\to m$ is an arc of the underlying digraph of $\Dstar$. Under the hypotheses of \cref{thm:formalized-state:interdependence}, $B$ is irreducible, and $\rho(B)$ is a simple eigenvalue of $B$ with an eigenvector $u$ whose entries are all positive. If, in addition, some diagonal entry of $B$ is positive, then with $D_tz_t+\varepsilon_t=0$ and $w$ the positive left eigenvector normalized by $w^{\top}u=1$, $\rho(B)^{-t}x_t\to u\,w^{\top}x_0$ for every $x_0$.
   806	\end{proposition}
   807	
   808	\begin{proof}
   809	A nonnegative matrix is irreducible if and only if the digraph of its positive entries is strongly connected, and that digraph contains the underlying digraph of $\Dstar$, which is strongly connected by \cref{thm:formalized-state:interdependence}. The Perron-Frobenius theorem gives the simple eigenvalue and positive eigenvector. An irreducible nonnegative matrix with a positive diagonal entry is primitive, and for primitive matrices $(B/\rho(B))^t\to uw^{\top}$ \citep{horn2012}.
   810	\end{proof}
   811	
   812	Under interdependence and positive linear dependencies, no pillar's capacity can grow indefinitely faster than the others: all six share one long-run rate and one profile $u$. The proposition says nothing about whether that rate exceeds one, and its hypothesis of nonnegative dependencies is exactly what the source doubts.
   813	
   814	\begin{remark}[Positive links do not settle stability]
   815	\label{rem:formalized-state:sign}
   816	Matrices with the same positive entries can have spectral radii on opposite sides of one. The circulant matrices with first rows $(0.6,0.45,0)$ and $(0.6,0.45,-0.45)$ share their positive entries; their eigenvalues are $a+b\omega^k+c\omega^{2k}$ with $\omega=e^{2\pi i/3}$, which gives spectral radius $1.05$ for the first and $|0.6\pm0.45\,i\sqrt3|=\sqrt{0.9675}\approx0.984$ for the second. The negative entries are feedback of the kind the source lists, such as legitimacy lost through coercion, and a model that records only who depends on whom cannot tell a self-reinforcing hierarchy from a self-correcting one.
   817	\end{remark}
   818	
   819	\subsection{Testable implications}
   820	
   821	\Cref{tab:hypotheses} states the hypotheses at the level of this Part, each with the source hypothesis it refines and an observation that would refute it. The comparative evidence of Parts I to VI is qualitative and drawn from the historical record; each hypothesis states the quantitative test that would confirm or refute it. The hypotheses inherit the source's six, H1 to H6, and add two that only the series can state: that the role map is complete in every coded polity (A1, a test of the representation theorem) and that its completeness is unrelated to the indices of capture (A2).
   822	
   823	\begin{table}[!htbp]
   824	\centering
   825	\small
   826	\caption{Hypotheses at the level of the series, with the source hypothesis each refines and a falsifier. Codings must be preregistered and include negative cases.}
   827	\label{tab:hypotheses}
   828	\begin{tabularx}{\textwidth}{@{}L{0.6cm}YL{1.9cm}Y@{}}
   829	\toprule
   830	 & Hypothesis & Parent & Falsifier \\
   831	\midrule
   832	A1 & No persistent collective in the record lacks any of the six functions in some form & None & A documented persistent collective without one function \\
   833	A2 & The six functions are realized in every coded polity while $U_t$ and $\Integ_t$ vary widely & Proposition 1 & Indices that are collinear with features of the role map \\
   834	B1 & Preferential rules survive adverse disclosure longer where $\Integ_t$ is high & H2 & No difference in survival after disclosure \\
   835	B2 & Raising contestability in one pillar lowers transmission through it & H1, H4 & Staggered reforms with no change in transmission \\
   836	B3 & Dispersing control in one pillar without reducing cross-pillar overlap leaves preferential rules intact & H2 & Dispersal alone ends preferential rules \\
   837	B4 & Organizations without organized opposition keep their leaderships longer & H1 & Equal leadership turnover with and without opposition \\
   838	B5 & $U_t$ and service quality are not monotonically related & H6 & A monotone decline of service quality in $U_t$ \\
   839	\bottomrule
   840	\end{tabularx}
   841	\end{table}
   842	
   843	\section{Regime profiles}
   844	\label{sec:regimes}
   845	
   846	\subsection{The profile of a regime type}
   847	
   848	The six regime types are implementations of the Formalized State. Every one is represented by a structure in $\mathcal{F}$ (\cref{thm:formalized-state:representation}), so a comparison cannot ask whether a type has the structure; it asks how the structure is implemented. A \emph{regime profile} records the pattern of integration, either a star around a hub pillar or a clique commanded by one coalition (\cref{lem:formalized-state:hub}); the characteristic control path, the direction in which control is converted (source Proposition 3); the checks that raise replacement rates or contestability (\cref{thm:formalized-state:conversion}); and documented episodes of capture and of binding checks. The profiles synthesize the comparative sections of Parts I to VI. They are hypotheses about where a preregistered coding would find integration, not coded values.
   849	
   850	\subsection{Market capitalism}
   851	
   852	Private owners, banks and corporations hold the resource pillar alongside a public budget and a central bank (Part I, Section 5). The hypothesized pattern is a star around $\pF$: resources couple to rule making through donations and lobbying, to legitimation through media ownership and research sponsorship, to interpretation through repeat-player advantages, and to production because capital allocation and employment are held by the same actors (Parts I, II, III and VI, Section 5). The control path runs from wealth to rules \citep{largo2026hbs}. Competing firms and sectors make different coalitions on different spokes likely, the pluralist reading \citep{dahl1961}, and by \cref{lem:formalized-state:hub}(b) a pure star cannot raise $\Integ_t$ above one third of its largest coupling. Documented checks include competing interest groups, antitrust, disclosure and elections (Part II, Section 5), and a recusal ruling of the United States Supreme Court that addressed a capture risk created by campaign spending in a judicial election (Part III, Section 5).
   853	
   854	\subsection{Communist party-states}
   855	
   856	The ruling party appoints office holders in every pillar through nomenklatura lists, which the partisan \'emigr\'e account of \citet{voslensky1984} treated as the basis of a ruling class. Rule making is the hub, and the control path runs from appointment to allocation and enforcement, the reverse of the market path \citep{largo2026hbs}. Because one coalition appoints in five pillars, the pattern is a clique: Proposition 6.5 of Part II bounds each coupling below, and \cref{lem:formalized-state:hub}(c) bounds $\Integ_t$ below by two thirds of the party's smallest command share across the five pillars. The checks lie inside the coalition, in elite divisions \citep{lane1995} and bureaucratic bargaining \citep{hough1979}. Documented episodes include courts that followed campaign directives under Stalin and the terror of the late 1930s, and, as checks, party supremacy over the military and a later rise in legality in ordinary cases (Parts III and V, Section 5).
   857	
   858	\subsection{Social democracy and democratic socialism}
   859	
   860	The hypothesized pattern is a triangle of rule making, resources and production, joined by bargaining among the peak organizations of labor and capital and the state (Parts I, II and VI, Section 5). At least two coalitions, labor and capital, each command part of each pillar, so the overlap measure gives moderate couplings even where bargaining is encompassing. Contestability is high: governments alternate, unions give workers voice, and transparency norms are strong. The documented risk is closure to unorganized interests (Part II, Section 5). The \emph{Langborger} ruling held that labor courts whose lay members are nominated by interested organizations can fail the test of impartiality (Part III, Section 5), and official inquiries into political surveillance by security services led to standing parliamentary oversight (Part V, Section 5). The source's fourth proposition, that public benefit is compatible with hierarchy, applies here with particular force \citep{largo2026hbs}.
   861	
   862	\subsection{Islamic states}
   863	
   864	Islamic states derive legitimacy from religious law, and classical caliphates, the Ottoman empire, modern Iran and Saudi Arabia differ in almost every coupling (Parts II, III and IV, Section 5). In Hallaq's account of classical practice, rulers appointed qadis while jurists who were not state officials developed the law \citep{hallaq2009}, which kept much of $\pJ$ and $\pI$ outside the ruler's coalition. Why the Middle East fell behind Western Europe economically is disputed: \citet{kuran2011} points to features of Islamic law, and \citet{rubin2017} to the bargains through which religious authorities legitimated rulers. The Ottoman empire governed through brokerage among several coalitions \citep{barkey2008}. Modern Iran shows a clique around clerical authority: the Guardian Council screens legislation and candidates, and the revolutionary guards couple coercion to resources (Parts I, II and V, Section 5). Saudi Arabia couples rule making to legitimation through the alliance of the royal family and the religious establishment, and to resources through oil rents (Part I, Section 5; \citealt{ross2012}). The checks include juristic pluralism, endowed revenue, elections in Iran and brokered rule. Capture varies with the state and the period, not with the religion.
   865	
   866	\subsection{Historical Catholic monarchies}
   867	
   868	Habsburg Spain, Bourbon France and the Papal States intertwined royal authority with the Church, and their diversity matches that of the Islamic cases. The hypothesized pattern couples rule making to legitimation through royal influence over Church appointments, resources to interpretation through venal judicial office, and resources to coercion through the fiscal-military state (Parts I, II, III and V, Section 5; \citealt{tilly1990,ertman1997}). In the Papal States the fusion of rule making and legitimation was complete (Part IV, Section 5). Brokerage limited the crown: Beik describes absolutism in Languedoc as collaboration with provincial elites rather than command \citep{beik1985}. Checks included the estates and Cortes, competing jurisdictions and conflict between Church and crown. The chancellor Maupeou's suppression of the parlements in 1771 removed a check, and its reversal in 1774 restored it (Part III, Section 5). In the terms of \cref{thm:formalized-state:conversion}, venality raised the conversion rate from $\pF$ to $\pJ$, while the parlements' tenure kept the replacement rate in $\pJ$ out of the crown's hands.
   869	
   870	\subsection{Secular democracies}
   871	
   872	Authority is distributed among elected officials, courts and private institutions, and contestability is designed to be high on every component (Parts II and V, Section 5). Couplings are low overall, with two characteristic channels: appointments to courts, with constitutional review that can act as co-legislation \citep{hirschl2004}, and delegation to independent central banks, regulators and courts whose accountability runs through review rather than election (Parts I and III, Section 5). The documented risks are erosion of contestability by incumbents and capture of the bodies that review them: the enlargement of the Argentine Supreme Court in 1990 produced a court aligned with the government (Part III, Section 5), and surveillance of citizens exposed by the United States Senate inquiry of 1975 and 1976 was both a capture episode and a check (Part V, Section 5). Rival institutions, a free press and citizens' coordination against transgressions by the state, which \citet{weingast1997} identified as the foundation of self-enforcing limits on government, are the checks.
   873	
   874	\subsection{What the classification shows}
   875	
   876	\Cref{tab:regimes} summarizes the profiles. Every row satisfies $\Struct$ and $\Inter$ and has the same dependency structure, because that structure is a function of the problems a collective faces, not of who solves them (\cref{lem:formalized-state:separation}). The rows differ in the pattern of integration, and the star and clique bounds of \cref{lem:formalized-state:hub} explain why market and party-state profiles with similar maximal couplings can differ sharply in $\Integ_t$. Every row records both capture episodes and binding checks, so the regime type does not settle whether a polity is captured; that requires coding a polity in a period, with preregistered weights, thresholds and coalition lists.
   877	
   878	\begin{table}[!htbp]
   879	\centering
   880	\small
   881	\caption{Regime profiles. Patterns and paths are drawn from the comparative sections of Parts I to VI.}
   882	\label{tab:regimes}
   883	\begin{tabularx}{\textwidth}{@{}L{2.2cm}YYY@{}}
   884	\toprule
   885	Regime type & Hypothesized integration pattern & Characteristic control path & Principal checks \\
   886	\midrule
   887	Market capitalism & A star around resources, with different coalitions on different spokes & From wealth to rules, legitimation and interpretation & Competition among interests, antitrust, disclosure, elections and courts \\
   888	Communist party-state & A clique of five pillars under the ruling party & From appointment to allocation and enforcement & Elite divisions, bureaucratic bargaining and the loyalty limit on appointment \\
   889	Social democracy & A triangle of rule making, resources and production joined by bargaining & From organized bargaining to rules and terms of work & Elections, organized labor, ombudsmen and parliamentary oversight \\
   890	Islamic states & Plural in classical practice and a clique around clerical authority in modern Iran & From religious-legal authority to rules and adjudication, and from rents to rule & Juristic pluralism, endowed revenue, brokerage and elections in Iran \\
   891	Catholic monarchies & Couplings of crown and Church, of money and justice, and of money and force & From fiscal need to venal office and from Church patronage to legitimation & Parlements, estates and Cortes, competing jurisdictions and Church-crown conflict \\
   892	Secular democracies & Low couplings, with appointment to courts and delegation to technical bodies & From rule making to interpretation through appointment & Rival institutions, free press, review bodies and citizen coordination \\
   893	\bottomrule
   894	\end{tabularx}
   895	\end{table}
   896	
   897	\section{Predecessors and novelty}
   898	\label{sec:literature}
   899	
   900	\subsection{The canon}
   901	
   902	Earlier answers to the question of what every polity must contain are of three kinds: typologies of rulers and of legitimacy, lists of functions, and derivations from premises. The typologies classify polities along axes other than the six functions. Aristotle classified constitutions by whether one, a few or many rule and whether they rule for the common interest or their own, and distinguished the deliberative, magisterial and judicial elements of a constitution \citep{aristotle1996}. Weber classified domination by the belief in its legitimacy, traditional, charismatic or legal-rational, and by the administrative staff that executes it \citep{weber1978}.
   903	
   904	The lists of functions are the closest relatives. Parsons named four functional prerequisites of any social system, adaptation, goal attainment, integration and latent pattern maintenance \citep{parsons1951}, and \citet{aberle1950} gave a longer list. Easton described the political system as converting inputs of demands and supports into authoritative outputs \citep{easton1965}. Almond divided political functions into input functions, among them socialization, interest articulation, interest aggregation and communication, and output functions, rule making, rule application and rule adjudication \citep{almond1960}. Luhmann described modern society as differentiated into functional subsystems, among them the economy, politics, law, science, religion and the mass media \citep{luhmann1995}. Mann treated societies as overlapping networks of ideological, economic, military and political power, none of them primary \citep{mann1986,mann1993}. These lists were criticized for defining prerequisites by what persisting societies happen to have \citep{hempel1959,elster1983}.
   905	
   906	The derivations are the model for the method. Hobbes derived the sovereign from the premise that agreements without a power to enforce them do not hold \citep{hobbes1651}; Part V accepts the premise and derives a sanctioning function rather than a sovereign. Arrow's impossibility theorem derives a sharp result about collective decisions from short axioms \citep{arrow1951}; it concerns aggregation rather than the structure of governance, and the rule-making function of Part II begins where it leaves off, since a collective must choose some procedure although none satisfies every desirable condition.
   907	
   908	The lists differ from the six pillars at exactly the points the formal results test. Mann's economic source and Parsons's adaptation join the command of resources with the production of wealth, which the latent veto (Proposition 3.6 of Part VI) and relocation (Lemma 3.4 of Part VI) separate; Mann's political source joins rule making with adjudication, which the disjunctive dependency of Proposition 3.6 of Part III separates. Mann's distinction between the despotic power of elites and the infrastructural power of states \citep{mann1984} corresponds to the distinction between $U_t$ and the capacity vector $x_t$, and his historical account of how particular networks emerged is something no axiomatic treatment replaces.
   909	
   910	Two further literatures address the other side of the thesis. The theory of capture, from Michels \citep{michels1915} through Stigler \citep{stigler1971}, state capture \citep{hellman2000}, extractive institutions \citep{acemoglu2006,acemoglu2019} and limited-access orders \citep{nww2009}, explains when capture arises, which is Proposition B, and does not state what every polity must contain. Normative theory supplies readings of the indices: the separation of powers of Montesquieu and Madison covers two pillars and part of a third \citep{montesquieu1989,madison1788}, and Walzer's spheres and Pettit's non-domination give normative content to $C_{mn}$ and $Q_m$ \citep{walzer1983,pettit1997}.
   911	
   912	\subsection{Non-equivalence}
   913	
   914	Each predecessor can be encoded as an abstraction on $\mathcal{G}_*$, and the encodings can be compared with $\Phi$ in $\mathbf{Abs}_P$. Five are coarsenings in the sense of \cref{sec:representation}, with equal weights within each block. Parsons: adaptation $=\{\pF,\pW\}$, goal attainment $=\{\pP\}$, integration $=\{\pJ,\pC\}$, latent pattern maintenance $=\{\pI\}$ \citep{parsons1951}; whether coercion belongs to goal attainment or to integration is contestable, and the choice does not affect the argument. Mann: ideological $=\{\pI\}$, economic $=\{\pF,\pW\}$, military $=\{\pC\}$, political $=\{\pP,\pJ\}$ \citep{mann1986}. Easton: inputs $=\{\pI,\pW\}$, outputs $=\{\pF,\pP,\pJ,\pC\}$ \citep{easton1965}; the assignment of production to inputs, as the source of supports, is contestable. Almond: rule making $=\{\pP\}$, rule application $=\{\pC\}$, rule adjudication $=\{\pJ\}$, inputs $=\{\pI\}$, with $\pF$ and $\pW$ dropped because his functions are those of the political system \citep{almond1960}; placing administration with coercion is contestable. Luhmann: economy $=\{\pF,\pW\}$, politics $=\{\pP,\pC\}$, law $=\{\pJ\}$, and one block for the communicative subsystems $=\{\pI\}$ \citep{luhmann1995}; Luhmann splits that block further, which the argument does not need. These encodings are readings of the 1960 and 1995 partitions: Almond and Powell later added system capabilities, among them extractive, regulative and distributive ones, that touch $\pF$ \citep{almond1966}, and Luhmann's subsystems are codes of communication rather than layers of actors. The other two are typologies. Aristotle's encoding returns the number of rulers, one if a single actor has a positive share of rule making, few if between two and half the members do, many otherwise, and the aim, deviant if a capture link is documented and correct otherwise \citep{aristotle1996}; the thresholds are a choice. Weber's encoding returns the coded type of legitimation and whether an administrative staff exists \citep{weber1978}.
   915	
   916	\begin{proposition}[Witnesses]
   917	\label{prop:formalized-state:witnesses}
   918	For each encoding $\alpha_k$ above there are $G,G'\in\mathcal{G}_*$ with $\alpha_k(G)=\alpha_k(G')$ and $P(G)\neq P(G')$:
   919	\begin{enumerate}[label=(\alph*)]
   920	\item Parsons, Mann and Luhmann merge $\pF$ and $\pW$, and Mann and Easton merge $\pP$ and $\pJ$; the pair of \cref{prop:formalized-state:minimality6}(b) for the merged pair, with $\mu=1/2$, has $C^{\ov}$ equal to $0$ against $1/2$ and $H$ equal to $1$ against $1/2$ in each merged pillar;
   921	\item Almond drops $\pF$; the pair of \cref{prop:formalized-state:minimality6}(a) with $m=\pF$ and $l_0=\pP$ has $H_{\pF}=1$ against $1/2$;
   922	\item Aristotle: two collectives with the same rule-making layer and no capture link, in which interpretation is held by one organization ($s^{\pJ}=(1,0)$ on $(a,b)$, $H_{\pJ}=1$) or by two equally ($s^{\pJ}=(1/2,1/2)$, $H_{\pJ}=1/2$), with $a$ and $b$ holding equal shares in $\pI$ in both;
   923	\item Weber: two collectives coded as legal-rational with an administrative staff, in which coercion is held by one organization ($s^{\pC}=(1,0)$ on $(a,b)$, $H_{\pC}=1$) or by two equally ($H_{\pC}=1/2$), with $a$ and $b$ holding equal shares in $\pI$ in both.
   924	\end{enumerate}
   925	Hence no encoded predecessor is $P$-preserving, and none is isomorphic to $\Phi$ in $\mathbf{Abs}_P$.
   926	\end{proposition}
   927	
   928	\begin{proof}
   929	(a) and (b) are instances of \cref{prop:formalized-state:minimality6}, whose proof computes both $P$-values and shows the coarsened images equal for any weights. Easton's outputs block contains $\pF$, $\pC$ and the merged pair; the coarsened shares of the block are a weighted sum in which only the $\pP$ and $\pJ$ terms differ between the two collectives, and those terms sum to the same vector, as in the proof of \cref{prop:formalized-state:minimality6}(b). (c) The two collectives have the same actor set, since $b$ performs practices of $\pI$ in both. They have the same set of actors with positive rule-making share and the same empty set of capture links, so the encoding returns the same number of rulers and the same aim. Their $H_{\pJ}$ differ, and $H_{\pJ}$ is invariant under relabeling. Both assignments are admissible as in the proof of \cref{prop:formalized-state:minimality6}, so both lie in $\mathcal{G}_*$ by \cref{lem:formalized-state:separation}. (d) The actor sets coincide as in (c). The two collectives carry the same coded legitimation type and staff, so the encoding agrees; $H_{\pC}$ differs. For the last sentence: an abstraction isomorphic to $\Phi$ has the same partition of $\mathcal{G}_*$ as $\Phi$, which is the partition into $\cong_A$-classes, and is therefore $P$-preserving.
   930	\end{proof}
   931	
   932	The Weber encoding fails in the other direction too. Two collectives with the same profile can carry different legitimation types, since $P$ forgets the content of legitimating beliefs (\cref{lem:formalized-state:preserved}); so neither of Weber's typology and $\Phi$ factors through the other. Weber classifies what the Formalized State forgets, and the two are complements rather than rivals.
   933	
   934	\begin{theorem}[Novelty relative to the canon]
   935	\label{thm:formalized-state:novelty}
   936	For each of the encoded predecessors, Aristotle, Weber, Parsons, Easton, Almond, Luhmann and Mann, the encoding $\alpha_k$ is not isomorphic to $\Phi$ in $\mathbf{Abs}_P$, does not represent governance systems up to $\cong_A$, and is not the coarsest $P$-preserving abstraction. The Formalized State abstraction has all four properties: representation, necessity, minimality and uniqueness.
   937	\end{theorem}
   938	
   939	\begin{proof}
   940	By \cref{prop:formalized-state:witnesses}, each $\alpha_k$ identifies two systems that are not $\cong_A$-equivalent, so it does not represent systems up to $\cong_A$ and is not $P$-preserving. A terminal object of $\mathbf{Abs}_P$ is in particular an object of it, so $\alpha_k$ is neither terminal nor isomorphic to $\Phi$. The four properties of $\Phi$ are \cref{thm:formalized-state:representation}, \cref{thm:formalized-state:A,thm:formalized-state:interdependence}, \cref{prop:formalized-state:minimality6}, and \cref{thm:formalized-state:uniqueness,thm:formalized-state:six}.
   941	\end{proof}
   942	
   943	\begin{remark}[Scope of novelty]
   944	\label{rem:formalized-state:novelty-scope}
   945	The theorem covers the seven encoded predecessors and is relative to $P$: the predecessors were built to preserve other things, and failing to preserve $P$ is a difference, not a defect. For works outside the list, the novelty claim is that, to our knowledge, no prior work states and proves a representation theorem with derived necessity, minimality and uniqueness of this form.
   946	\end{remark}
   947	
   948	\Cref{tab:predecessors} summarizes the comparison. The columns record representation up to $\cong_A$ (R), necessity derived from premises that can be false (N), minimality among $P$-preserving coarsenings (M) and uniqueness as the coarsest $P$-preserving abstraction (U). For the predecessors the R, M and U entries follow from \cref{prop:formalized-state:witnesses}; the N entries record that none derives its list from stated axioms with falsifiers, which is a reading of the cited works rather than a theorem.
   949	
   950	\begin{table}[!htbp]
   951	\centering
   952	\small
   953	\caption{The Formalized State and the encoded predecessors. R, N, M and U are representation, derived necessity, minimality and uniqueness; the last column names the result that gives the pair of systems the encoding cannot tell apart.}
   954	\label{tab:predecessors}
   955	\footnotesize
   956	\setlength{\tabcolsep}{3.5pt}
   957	\begin{tabularx}{\textwidth}{@{}L{1.8cm}L{1.2cm}Ycccc L{2.7cm}@{}}
   958	\toprule
   959	Framework & Size & Encoding & R & N & M & U & Witness \\
   960	\midrule
   961	Formalized State & Six & The profile map & Yes & Yes & Yes & Yes & None \\
   962	Parsons & Four & Merges resources and production & No & No & No & No & \cref{prop:formalized-state:witnesses}(a) \\
   963	Mann & Four & Merges resources and production, and rule making and adjudication & No & No & No & No & \cref{prop:formalized-state:witnesses}(a) \\
   964	Easton & Two & Merges rule making and adjudication among outputs & No & No & No & No & \cref{prop:formalized-state:witnesses}(a) \\
   965	Almond & Seven & Drops resources and production & No & No & No & No & \cref{prop:formalized-state:witnesses}(b) \\
   966	Luhmann & Several & Merges resources and production in the economy & No & No & No & No & \cref{prop:formalized-state:witnesses}(a) \\
   967	Aristotle & Six types & Number of rulers and aim & No & No & No & No & \cref{prop:formalized-state:witnesses}(c) \\
   968	Weber & Three types & Legitimation type and staff & No & No & No & No & \cref{prop:formalized-state:witnesses}(d) \\
   969	\bottomrule
   970	\end{tabularx}
   971	\end{table}
   972	
   973	\section{Revelation 13 and 17 to 18}
   974	\label{sec:revelation}
   975	
   976	The series reads Revelation typologically. The beast is a recurring pattern of power that claims ultimate allegiance, and Babylon is the idolatrous city of every age. The reading does not identify any present-day government, party, institution, technology, payment system or person with the beast or its mark. Futurist identifications have a long record of failure \citep{mcginn1998,fuller1995,boyer1992}, and historicist identifications of the papacy or of any other institution with the beast belong to the history of polemic. The theological reading is the project's own and is offered as an interpretation, not as an exegetical result.
   977	
   978	The commentators agree that the beasts had a Roman referent, which the typological reading generalizes. Richard Bauckham reads Rome as the paradigm of the beast and the book's conflict as one between worship of the beast and faithful witness \citep{bauckham1993}, and he reads chapter 18 as an economic critique of Rome's trade \citep{bauckham1991}. Adela Yarbro Collins reads the book as a response to a crisis its audience perceived, working through catharsis \citep{collins1984}. Craig Koester's commentary places the beasts in the imperial politics and civic cults of Roman Asia \citep{koester2014}. J.\,Nelson Kraybill shows how participation in provincial commerce was bound up with the imperial cult \citep{kraybill1996}, and the archaeology of the imperial cult at Ephesus and the study of the cult as local civic practice give the image its setting \citep{friesen2001,price1984}.
   979	
   980	Read with the formal model, chapter 13 describes a single configuration in all six pillars. The dragon gives the first beast ``his power, and his seat, and great authority'' (Rev 13:2), and the onlookers ask ``Who is like unto the beast? who is able to make war with him?'' (Rev 13:4): rule and force held together. The second beast ``exerciseth all the power of the first beast before him, and causeth the earth and them which dwell therein to worship the first beast'' (Rev 13:12): legitimation in the service of rule. It gives life to an image that causes ``that as many as would not worship the image of the beast should be killed'' (Rev 13:15): sanction attached to allegiance, with no forum for those who refuse. And it causes all, ``both small and great, rich and poor, free and bond, to receive a mark in their right hand, or in their foreheads: And that no man might buy or sell, save he that had the mark'' (Rev 13:16 and 13:17) \citep{kjv}: participation in exchange and production made conditional on an allegiance test. In the vocabulary of \cref{sec:capture}, one coalition commands every pillar, contestability is zero, and integration is complete. The image is the corner $(1,1)$ of \cref{thm:formalized-state:nonimplication}, with every capture link documented in the text itself.
   981	
   982	Chapters 17 and 18 add the coalition and the market. The kings ``have one mind, and shall give their power and strength unto the beast'' (Rev 17:13), a coalition formed by delegation, which is the mechanism of T1. The waters on which the city sits ``are peoples, and multitudes, and nations, and tongues'' (Rev 17:15). The merchants ``are waxed rich through the abundance of her delicacies'' (Rev 18:3), they mourn because ``no man buyeth their merchandise any more'' (Rev 18:11), and the cargo list ends with ``slaves, and souls of men'' (Rev 18:13) \citep{kjv}. The text does not condemn commerce as such. It condemns a commerce whose merchants ``were the great men of the earth'' (Rev 18:23), an integration of resources and production with rule. Following the source, the series uses the language of bondage only in this disciplined and explicitly metaphorical sense, and distinguishes wage labor, taxation, serfdom and chattel slavery \citep{largo2026hbs}. The book's response is exit: ``Come out of her, my people'' (Rev 18:4). In \cref{thm:formalized-state:conversion}, exit is a replacement rate.
   983	
   984	The typology therefore fits the separation of the two propositions in a specific way. The text depicts the captured configuration, Proposition B at its limit, and it presupposes the functions of Proposition A: the book does not imagine a world without rule, judgment, worship, commerce or labor, but relocates them, as Part III observed of judgment. The series names the universal abstraction after the image of its worst instance. The name is the series' typological reading of the abstraction, not a conclusion of any theorem, and the normative warning attaches only to capture, which is a property of instances. The source makes the same distinction: the expression should be reserved for coercive and unaccountable coordination, and the theological image permits government that protects the vulnerable and expertise that corrects error \citep{largo2026hbs}. Walter Wink's reading of the biblical language of the powers as institutional structures that can become a domination system is a theological precedent for reading the image as a structure rather than a person \citep{wink1992}.
   985	
   986	\section{Objections and scope}
   987	\label{sec:objections}
   988	
   989	\emph{Proposition A is true by definition.} If the functions were defined so broadly that anything counts, the theorem would be empty. Each implementation predicate is a property of observable dispositions that can fail, and \cref{prop:formalized-state:independence}(b) exhibits persistent collectives in which each fails. The theorem excludes them from the real world only through its premises, and \cref{tab:falsifiers} states what observation would refute each premise.
   990	
   991	\emph{The argument is functionalist.} \Cref{thm:formalized-state:A} is a condition of persistence. It explains no institution by its effects, asserts no feedback from effects to causes, and allows any institution or none to perform a function. It is open to Hempel's objection only if read as an inference from a function to a particular institution, and it makes no such inference.
   992	
   993	\emph{The hazard premises are too strong.} Where unsettled conflict or abandoned disputes are harmless, the forcing argument gives nothing. The concession is real. Part III's exit proposition shows that adjudication can be thin where exit is free, and the immediate-return foragers that Woodburn described come closest to that condition \citep{woodburn1982}. The ethnographies of these societies still record talk-based mediation and leveling sanctions, so the functions are thin rather than absent, and the claim is narrowed to collectives in which some recurring class of residual disputes cannot be escaped by moving; a collective in which every residual dispute can be escaped at no cost falls outside the derivation, and Proposition 3.4 of Part III shows that such a collective can persist without determination.
   994	
   995	\emph{Interdependence rests on added premises.} It does, and \cref{prop:formalized-state:minimality}(a) shows that the six axioms alone do not yield it. Universal interdependence has the same logical status as the existence of the functions: a theorem from stated premises, made universal by the hypothesis that every functioning collective satisfies them. The premises can be refuted by observation. Universal interdependence would be falsified by a persistent collective in which production continued unchanged while every claim on its inputs went unsettled, which refutes X1 and removes the only arc into production; by one whose allocation rules survived a change of environment that created claims they could not settle, which refutes X2; by one whose allocation rules never produced a dispute the parties could not settle alone, which refutes X3; or by one whose allocation rules were kept, at a measured temptation above a preregistered tolerance, after every response to breach had ceased, which refutes X5. A single such collective would leave its dependency structure without a path from some function to production, or without a cascade from coercion, and would show that interdependence is common rather than universal. Universal interdependence is also not universal capture. It holds in every corner of \cref{thm:formalized-state:nonimplication}, including the stateless corner where no one holds more than an equal share of anything.
   996	
   997	\emph{There is no single apex.} The pluralist objection, that complex polities seldom have a unified center of command \citep{dahl1961}, is an objection to Proposition B, not to Proposition A, and the framework accommodates it. A polity whose couplings form a star built by different coalitions has bounded integration by \cref{lem:formalized-state:hub}(b), and the strong classification requires a documented coalition, mechanism, domain and duration \citep{largo2026hbs}.
   998	
   999	\emph{The indices cannot be measured.} The indices are defined for measurement, and what the paper proves about them is their range, the effect of the weights (\cref{lem:formalized-state:U}), and the bounds that link coalition structure to integration (\cref{lem:formalized-state:hub}). These results constrain measurement without performing it. The latent-variable and event-study designs of the source, together with a coding of the five conditions of a capture link, remain the agenda.
  1000	
  1001	\emph{The name condemns all governance.} Naming the universal structure after the beast could be read as a verdict that every polity is the beast of Revelation. The series rejects that reading. The name refers to a structure that every governance system has, and Proposition A carries no moral verdict; the warning attaches to Proposition B, and \cref{thm:formalized-state:nonimplication} shows that every regime type can satisfy A without B. Government that protects the vulnerable, courts that check power and expertise that corrects error are compatible with the structure and are among the checks that interrupt capture.
  1002	
  1003	\emph{The abstraction forgets too much.} The equivalence $\cong_A$ forgets the content of rules and beliefs, the procedures that implement each function, and the moral quality of outcomes (\cref{lem:formalized-state:preserved}). A medieval monarchy and a modern republic can have the same image if their control shares, contestability, couplings and dependencies coincide. This is the price of a representation that covers every governance system, and it is why the abstraction says nothing about justice. The properties it keeps are the ones that the capture predicate needs, and the properties it forgets are left to history, law and theology.
  1004	
  1005	\emph{Uniqueness is built into the definitions.} The universal property of \cref{thm:formalized-state:uniqueness} follows quickly once the preserved properties are fixed, and \cref{rem:formalized-state:scope} says so. The substantive content is that the coarsest abstraction is a class of six-layer structures with an interdependent dependency hypergraph, which needs necessity, and that no coarsening of it works, which needs the witness pairs. A reader who wants to preserve other properties obtains another abstraction, unique for those properties.
  1006	
  1007	\emph{Class relations are underdeveloped.} A Marxian reader may find that the six pillars dissolve class into functions. The productive pillar is the place where the objection is met. Part VI shows that producers hold a latent veto over every institution that cannot replace their output (Proposition 3.6 of Part VI), and the dependency structure makes every function depend on production. The framework is a middle-range theory of institutions, and it leaves the theory of class formation to others.
  1008	
  1009	\section{Conclusion}
  1010	\label{sec:conclusion}
  1011	
  1012	The six-pillar framework identifies an invariant structure of human governance, supported by historical observation and given precise expression through mathematics. Relative to six axioms about collective life, four incidence axioms and a stated set of preserved properties, the Formalized State has four properties. It represents every governance system that satisfies the axioms, preserving roles, control shares, concentration, contestability, integration and dependencies and forgetting content, ideology and procedure. Its components are necessary, because the axioms force each function and each dependency and each axiom can fail in a persistent model. It is minimal, because every way of dropping or merging pillars confuses two systems with different preserved properties. And it is unique, as the coarsest abstraction that preserves those properties, up to a unique isomorphism, with exactly six dimensions. Encodings of seven classical frameworks each confuse a pair of systems that it distinguishes.
  1013	
  1014	Capture belongs to instances. Structures that satisfy every axiom occupy every corner of the concentration and integration square, so the existence of the structure settles nothing about its capture, and the conversion model shows how replacement and contestability decide whether a coalition's foothold dies out. The open questions are empirical: whether every functioning collective satisfies the axioms, which has been tested against the ethnographic and historical record only qualitatively; and the quantitative scoring of real polities on indices whose ranges are proved here. The series calls the abstraction the Hierarchy of the Beast System. The structure is universal, its capture is contingent, and the difference between them is a matter of measurement.
  1015	
  1016	\appendix
  1017	
  1018	\section{Code evidence}
  1019	\label{app:code}
  1020	
  1021	The reference implementation is the Python package \texttt{beast\_system} in the directory \texttt{model/} of the project, with its tests in \texttt{model/tests/}. It encodes the formal objects of this paper and checks the results that admit a computational check on coded fixtures.
  1022	
  1023	%APPENDIX-CODE-EVIDENCE
  1024	
  1025	\begin{small}
  1026	\begin{thebibliography}{999}
  1027	
  1028	\bibitem[Aberle et al.(1950)]{aberle1950}
  1029	Aberle, D. F., A. K. Cohen, A. K. Davis, M. J. Levy Jr. and F. X. Sutton. 1950. ``The Functional Prerequisites of a Society.'' \emph{Ethics} 60(2): 100-111. \url{https://doi.org/10.1086/290705}.
  1030	
  1031	\bibitem[Acemoglu and Robinson(2006)]{acemoglu2006}
  1032	Acemoglu, Daron and James A. Robinson. 2006. \emph{Economic Origins of Dictatorship and Democracy}. Cambridge University Press. \url{https://doi.org/10.1017/CBO9780511510809}.
  1033	
  1034	\bibitem[Acemoglu and Robinson(2019)]{acemoglu2019}
  1035	Acemoglu, Daron and James A. Robinson. 2019. \emph{The Narrow Corridor: States, Societies, and the Fate of Liberty}. Penguin Press.
  1036	
  1037	\bibitem[Almond and Coleman(1960)]{almond1960}
  1038	Almond, Gabriel A. and James S. Coleman, eds. 1960. \emph{The Politics of the Developing Areas}. Princeton University Press. \url{https://doi.org/10.1515/9781400866977}.
  1039	
  1040	\bibitem[Almond and Powell(1966)]{almond1966}
  1041	Almond, Gabriel A. and G. Bingham Powell. 1966. \emph{Comparative Politics: A Developmental Approach}. Little, Brown. \url{https://openlibrary.org/works/OL2693586W}.
  1042	
  1043	\bibitem[Aristotle(1996)]{aristotle1996}
  1044	Aristotle. 1996. \emph{The Politics, and the Constitution of Athens}. Cambridge University Press. \url{https://openlibrary.org/works/OL14998298W}.
  1045	
  1046	\bibitem[Arrow(1951)]{arrow1951}
  1047	Arrow, Kenneth J. 1951. \emph{Social Choice and Individual Values}. Yale University Press edition. \url{https://doi.org/10.12987/9780300186987}.
  1048	
  1049	\bibitem[Aumann(1976)]{aumann1976}
  1050	Aumann, Robert J. 1976. ``Agreeing to Disagree.'' \emph{The Annals of Statistics} 4(6): 1236-1239. \url{https://doi.org/10.1214/aos/1176343654}.
  1051	
  1052	\bibitem[Axelrod(1984)]{axelrod1984}
  1053	Axelrod, Robert. 1984. \emph{The Evolution of Cooperation}. Basic Books.
  1054	
  1055	\bibitem[Barkey(2008)]{barkey2008}
  1056	Barkey, Karen. 2008. \emph{Empire of Difference: The Ottomans in Comparative Perspective}. Cambridge University Press. \url{https://doi.org/10.1017/cbo9780511790645}.
  1057	
  1058	\bibitem[Bauckham(1991)]{bauckham1991}
  1059	Bauckham, Richard. 1991. ``The Economic Critique of Rome in Revelation 18.'' In \emph{Images of Empire}, edited by Loveday Alexander, 47-90. Sheffield: JSOT Press.
  1060	
  1061	\bibitem[Bauckham(1993)]{bauckham1993}
  1062	Bauckham, Richard. 1993. \emph{The Theology of the Book of Revelation}. Cambridge University Press. \url{https://doi.org/10.1017/cbo9780511819858}.
  1063	
  1064	\bibitem[Becker(1968)]{becker1968}
  1065	Becker, Gary S. 1968. ``Crime and Punishment: An Economic Approach.'' \emph{Journal of Political Economy} 76(2): 169-217. \url{https://doi.org/10.1086/259394}.
  1066	
  1067	\bibitem[Beik(1985)]{beik1985}
  1068	Beik, William. 1985. \emph{Absolutism and Society in Seventeenth-Century France: State Power and Provincial Aristocracy in Languedoc}. Cambridge University Press. \url{https://doi.org/10.1017/cbo9780511583797}.
  1069	
  1070	\bibitem[Boehm(1999)]{boehm1999}
  1071	Boehm, Christopher. 1999. \emph{Hierarchy in the Forest: The Evolution of Egalitarian Behavior}. Harvard University Press. \url{https://doi.org/10.2307/j.ctvjf9xr4}.
  1072	
  1073	\bibitem[Boyer(1992)]{boyer1992}
  1074	Boyer, Paul. 1992. \emph{When Time Shall Be No More: Prophecy Belief in Modern American Culture}. Harvard University Press (Belknap). \url{https://doi.org/10.2307/jj.41480279}.
  1075	
  1076	\bibitem[Cassinelli(1953)]{cassinelli1953}
  1077	Cassinelli, C. W. 1953. ``The Law of Oligarchy.'' \emph{American Political Science Review} 47(3): 773-784. \url{https://doi.org/10.2307/1952904}.
  1078	
  1079	\bibitem[Clastres(1987)]{clastres1987}
  1080	Clastres, Pierre. 1987. \emph{Society against the State: Essays in Political Anthropology (1974), trans. Robert Hurley}. Zone Books. \url{https://doi.org/10.2307/j.ctv1595m3p}.
  1081	
  1082	\bibitem[Collins(1984)]{collins1984}
  1083	Collins, Adela Yarbro. 1984. \emph{Crisis and Catharsis: The Power of the Apocalypse}. Westminster Press.
  1084	
  1085	\bibitem[Cox et al.(2010)]{cox2010}
  1086	Cox, Michael, Gwen Arnold and Sergio Villamayor Tomas. 2010. ``A Review of Design Principles for Community-based Natural Resource Management.'' \emph{Ecology and Society} 15(4): 38. \url{https://doi.org/10.5751/ES-03704-150438}.
  1087	
  1088	\bibitem[Dahl(1961)]{dahl1961}
  1089	Dahl, Robert A. 1961. \emph{Who Governs? Democracy and Power in an American City}. Yale University Press.
  1090	
  1091	\bibitem[Easton(1965)]{easton1965}
  1092	Easton, David. 1965. \emph{A Systems Analysis of Political Life}. John Wiley \& Sons.
  1093	
  1094	\bibitem[Ellickson(1991)]{ellickson1991}
  1095	Ellickson, Robert C. 1991. \emph{Order without Law: How Neighbors Settle Disputes}. Harvard University Press. \url{https://doi.org/10.4159/9780674036437}.
  1096	
  1097	\bibitem[Elster(1979)]{elster1979}
  1098	Elster, Jon. 1979. \emph{Ulysses and the Sirens: Studies in Rationality and Irrationality}. Cambridge University Press.
  1099	
  1100	\bibitem[Elster(1983)]{elster1983}
  1101	Elster, Jon. 1983. \emph{Explaining Technical Change: A Case Study in the Philosophy of Science}. Cambridge University Press.
  1102	
  1103	\bibitem[Ertman(1997)]{ertman1997}
  1104	Ertman, Thomas. 1997. \emph{Birth of the Leviathan: Building States and Regimes in Medieval and Early Modern Europe}. Cambridge University Press. \url{https://doi.org/10.1017/cbo9780511529016}.
  1105	
  1106	\bibitem[Evans-Pritchard(1940)]{evanspritchard1940}
  1107	Evans-Pritchard, E. E. 1940. \emph{The Nuer: A Description of the Modes of Livelihood and Political Institutions of a Nilotic People}. Clarendon Press.
  1108	
  1109	\bibitem[Friesen(2001)]{friesen2001}
  1110	Friesen, Steven J. 2001. \emph{Imperial Cults and the Apocalypse of John: Reading Revelation in the Ruins}. Oxford University Press. \url{https://doi.org/10.1093/0195131533.001.0001}.
  1111	
  1112	\bibitem[Fuller(1995)]{fuller1995}
  1113	Fuller, Robert C. 1995. \emph{Naming the Antichrist: The History of an American Obsession}. Oxford University Press. \url{https://doi.org/10.1093/acprof:oso/9780195109795.001.0001}.
  1114	
  1115	\bibitem[Gallo et al.(1993)]{gallo1993}
  1116	Gallo, Giorgio, Giustino Longo, Stefano Pallottino and Sang Nguyen. 1993. ``Directed Hypergraphs and Applications.'' \emph{Discrete Applied Mathematics} 42(2-3): 177-201. \url{https://doi.org/10.1016/0166-218X(93)90045-P}.
  1117	
  1118	\bibitem[Graeber and Wengrow(2021)]{graeber2021}
  1119	Graeber, David and David Wengrow. 2021. \emph{The Dawn of Everything: A New History of Humanity}. Farrar, Straus and Giroux.
  1120	
  1121	\bibitem[Greif(1993)]{greif1993}
  1122	Greif, Avner. 1993. ``Contract Enforceability and Economic Institutions in Early Trade: The Maghribi Traders' Coalition.'' \emph{American Economic Review} 83(3): 525-548. \url{https://www.jstor.org/stable/2117532}.
  1123	
  1124	\bibitem[Hallaq(2009)]{hallaq2009}
  1125	Hallaq, Wael B. 2009. \emph{An Introduction to Islamic Law}. Cambridge University Press. \url{https://doi.org/10.1017/cbo9780511801044}.
  1126	
  1127	\bibitem[Hart(1961)]{hart1961}
  1128	Hart, H. L. A. 1961. \emph{The Concept of Law}. Clarendon Press (3rd ed. 2012, Oxford University Press). \url{https://doi.org/10.1093/he/9780199644704.001.0001}.
  1129	
  1130	\bibitem[Hayek(1973)]{hayek1973}
  1131	Hayek, Friedrich A. 1973. \emph{Law, Legislation and Liberty, Volume 1: Rules and Order}. University of Chicago Press. \url{https://doi.org/10.7208/chicago/9780226321233.001.0001}.
  1132	
  1133	\bibitem[Hellman et al.(2000)]{hellman2000}
  1134	Hellman, Joel S., Geraint Jones and Daniel Kaufmann. 2000. \emph{Seize the State, Seize the Day: State Capture, Corruption, and Influence in Transition}. World Bank Policy Research Working Paper 2444.
  1135	
  1136	\bibitem[Hempel(1959)]{hempel1959}
  1137	Hempel, Carl G. 1959. ``The Logic of Functional Analysis.'' In \emph{Symposium on Sociological Theory}, edited by Llewellyn Gross, 271-307. New York: Harper \& Row.
  1138	
  1139	\bibitem[Hirschl(2004)]{hirschl2004}
  1140	Hirschl, Ran. 2004. \emph{Towards Juristocracy: The Origins and Consequences of the New Constitutionalism}. Harvard University Press. \url{https://doi.org/10.2307/j.ctv15d81nb}.
  1141	
  1142	\bibitem[Hobbes(1996)]{hobbes1651}
  1143	Hobbes, Thomas. 1996. \emph{Leviathan} (1651), edited by Richard Tuck. Cambridge University Press. \url{https://doi.org/10.1017/CBO9780511808166}.
  1144	
  1145	\bibitem[Horn and Johnson(2012)]{horn2012}
  1146	Horn, Roger A. and Charles R. Johnson. 2012. \emph{Matrix Analysis}. Second edition. Cambridge University Press. \url{https://doi.org/10.1017/CBO9781139020411}.
  1147	
  1148	\bibitem[Hough and Fainsod(1979)]{hough1979}
  1149	Hough, Jerry F. and Merle Fainsod. 1979. \emph{How the Soviet Union Is Governed}. Harvard University Press.
  1150	
  1151	\bibitem[Kelly(1995)]{kelly1995}
  1152	Kelly, Robert L. 1995. \emph{The Foraging Spectrum: Diversity in Hunter-Gatherer Lifeways}. Smithsonian Institution Press. \url{https://doi.org/10.2307/j.ctv2sx9gc9}.
  1153	
  1154	\bibitem[{King James Bible}(1611)]{kjv}
  1155	\emph{The Holy Bible, King James Version}. 1611. Project Gutenberg eBook no.~10. \url{https://www.gutenberg.org/ebooks/10}.
  1156	
  1157	\bibitem[Kivela et al.(2014)]{kivela2014}
  1158	Kivela, Mikko, Alex Arenas, Marc Barthelemy, James P. Gleeson, Yamir Moreno and Mason A. Porter. 2014. ``Multilayer Networks.'' \emph{Journal of Complex Networks} 2(3): 203-271. \url{https://doi.org/10.1093/comnet/cnu016}.
  1159	
  1160	\bibitem[Koester(2014)]{koester2014}
  1161	Koester, Craig R. 2014. \emph{Revelation: A New Translation with Introduction and Commentary}. Yale University Press (Anchor Yale Bible 38A). \url{https://doi.org/10.12987/9780300211030}.
  1162	
  1163	\bibitem[Kraybill(1996)]{kraybill1996}
  1164	Kraybill, J. Nelson. 1996. \emph{Imperial Cult and Commerce in John's Apocalypse}. Sheffield Academic Press (JSNT Supplement 132).
  1165	
  1166	\bibitem[Kuran(2011)]{kuran2011}
  1167	Kuran, Timur. 2011. \emph{The Long Divergence: How Islamic Law Held Back the Middle East}. Princeton University Press. \url{https://doi.org/10.1515/9781400836017}.
  1168	
  1169	\bibitem[Lane and Ross(1995)]{lane1995}
  1170	Lane, David and Cameron Ross. 1995. ``The CPSU Ruling Elite 1981-1991: Commonalities and Divisions.'' \emph{Communist and Post-Communist Studies} 28(3): 339-360. \url{https://doi.org/10.1016/0967-067X(95)00020-U}.
  1171	
  1172	\bibitem[Largo(2026)]{largo2026hbs}
  1173	Largo, Mateo. 2026. ``The Hierarchy of the Beast System: Institutional Power, Elite Coordination, and Economic Dependency Across Political Regimes.'' Working paper, 14 October 2026.
  1174	
  1175	\bibitem[Lee(1979)]{lee1979}
  1176	Lee, Richard B. 1979. \emph{The !Kung San: Men, Women, and Work in a Foraging Society}. Cambridge University Press.
  1177	
  1178	\bibitem[Lee(2013)]{lee2013}
  1179	Lee, Richard B. 2013. \emph{The Dobe Ju/'hoansi (4th edition)}. Wadsworth/Cengage Learning.
  1180	
  1181	\bibitem[Lewis(1969)]{lewis1969}
  1182	Lewis, David K. 1969. \emph{Convention: A Philosophical Study}. Harvard University Press. \url{https://doi.org/10.1002/9780470693711}.
  1183	
  1184	\bibitem[Lipset et al.(1956)]{lipset1956}
  1185	Lipset, Seymour Martin, Martin A. Trow and James S. Coleman. 1956. \emph{Union Democracy: The Internal Politics of the International Typographical Union}. Free Press.
  1186	
  1187	\bibitem[Long(2026a)]{long2026coercive}
  1188	Long, Matthew. 2026a. ``Coercive Power and Enforcement.'' Part V of \emph{The Six Pillars of the Beast System}. Working paper, October 2026.
  1189	
  1190	\bibitem[Long(2026b)]{long2026financial}
  1191	Long, Matthew. 2026b. ``Financial Power and Resource Command.'' Part I of \emph{The Six Pillars of the Beast System}. Working paper, October 2026.
  1192	
  1193	\bibitem[Long(2026c)]{long2026ideological}
  1194	Long, Matthew. 2026c. ``Ideological Power and Legitimation.'' Part IV of \emph{The Six Pillars of the Beast System}. Working paper, October 2026.
  1195	
  1196	\bibitem[Long(2026d)]{long2026judicial}
  1197	Long, Matthew. 2026d. ``Judicial Power and Legal Interpretation.'' Part III of \emph{The Six Pillars of the Beast System}. Working paper, October 2026.
  1198	
  1199	\bibitem[Long(2026e)]{long2026political}
  1200	Long, Matthew. 2026e. ``Political Power and Rule Making.'' Part II of \emph{The Six Pillars of the Beast System}. Working paper, October 2026.
  1201	
  1202	\bibitem[Long(2026f)]{long2026productive}
  1203	Long, Matthew. 2026f. ``Productive Power and Social Reproduction.'' Part VI of \emph{The Six Pillars of the Beast System}. Working paper, October 2026.
  1204	
  1205	\bibitem[Luhmann(1995)]{luhmann1995}
  1206	Luhmann, Niklas. 1995. \emph{Social Systems}. Stanford University Press. \url{https://openlibrary.org/works/OL1652158W}.
  1207	
  1208	\bibitem[Madison(1788)]{madison1788}
  1209	Madison, James. 1788. \emph{The Federalist No. 51: The Structure of the Government Must Furnish the Proper Checks and Balances}. Independent Journal, 6 February 1788. \url{https://avalon.law.yale.edu/18th_century/fed51.asp}.
  1210	
  1211	\bibitem[Mann(1984)]{mann1984}
  1212	Mann, Michael. 1984. ``The Autonomous Power of the State: Its Origins, Mechanisms and Results.'' \emph{European Journal of Sociology} 25(2): 185-213. \url{https://doi.org/10.1017/S0003975600004239}.
  1213	
  1214	\bibitem[Mann(1986)]{mann1986}
  1215	Mann, Michael. 1986. \emph{The Sources of Social Power, Volume 1: A History of Power from the Beginning to A.D. 1760}. Cambridge University Press. \url{https://doi.org/10.1017/CBO9780511570896}.
  1216	
  1217	\bibitem[Mann(1993)]{mann1993}
  1218	Mann, Michael. 1993. \emph{The Sources of Social Power, Volume 2: The Rise of Classes and Nation-States, 1760-1914}. Cambridge University Press. \url{https://doi.org/10.1017/CBO9780511570902}.
  1219	
  1220	\bibitem[Marshall(1976)]{marshall1976}
  1221	Marshall, Lorna. 1976. \emph{The !Kung of Nyae Nyae}. Harvard University Press. \url{https://doi.org/10.4159/harvard.9780674180574}.
  1222	
  1223	\bibitem[McGinn(1998)]{mcginn1998}
  1224	McGinn, Bernard. 1998. \emph{Antichrist: Two Thousand Years of the Human Fascination with Evil}. Columbia University Press.
  1225	
  1226	\bibitem[Merton(1968)]{merton1968}
  1227	Merton, Robert K. 1968. \emph{Social Theory and Social Structure (enlarged edition)}. Free Press.
  1228	
  1229	\bibitem[Michels(1915)]{michels1915}
  1230	Michels, Robert. 1915. \emph{Political Parties: A Sociological Study of the Oligarchical Tendencies of Modern Democracy}. Hearst's International Library.
  1231	
  1232	\bibitem[Montesquieu(1989)]{montesquieu1989}
  1233	Montesquieu, Charles de Secondat. 1989. \emph{The Spirit of the Laws} (1748), edited by Anne M. Cohler, Basia Carolyn Miller and Harold Samuel Stone. Cambridge University Press.
  1234	
  1235	\bibitem[Mosca(1939)]{mosca1939}
  1236	Mosca, Gaetano. 1939. \emph{The Ruling Class (Elementi di scienza politica)}. McGraw-Hill.
  1237	
  1238	\bibitem[North et al.(2009)]{nww2009}
  1239	North, Douglass C., John Joseph Wallis and Barry R. Weingast. 2009. \emph{Violence and Social Orders: A Conceptual Framework for Interpreting Recorded Human History}. Cambridge University Press. \url{https://doi.org/10.1017/CBO9780511575839}.
  1240	
  1241	\bibitem[Olson(1965)]{olson1965}
  1242	Olson, Mancur. 1965. \emph{The Logic of Collective Action: Public Goods and the Theory of Groups}. Harvard University Press. \url{https://doi.org/10.4159/9780674041660}.
  1243	
  1244	\bibitem[Ostrom(1990)]{ostrom1990}
  1245	Ostrom, Elinor. 1990. \emph{Governing the Commons: The Evolution of Institutions for Collective Action}. Cambridge University Press. \url{https://doi.org/10.1017/CBO9780511807763}.
  1246	
  1247	\bibitem[Parsons(1951)]{parsons1951}
  1248	Parsons, Talcott. 1951. \emph{The Social System}. Free Press. \url{https://doi.org/10.4324/9780203992951}.
  1249	
  1250	\bibitem[Pettit(1997)]{pettit1997}
  1251	Pettit, Philip. 1997. \emph{Republicanism: A Theory of Freedom and Government}. Oxford University Press. \url{https://doi.org/10.1093/0198296428.001.0001}.
  1252	
  1253	\bibitem[Price(1984)]{price1984}
  1254	Price, S. R. F. 1984. \emph{Rituals and Power: The Roman Imperial Cult in Asia Minor}. Cambridge University Press.
  1255	
  1256	\bibitem[Ross(2012)]{ross2012}
  1257	Ross, Michael L. 2012. \emph{The Oil Curse: How Petroleum Wealth Shapes the Development of Nations}. Princeton University Press. \url{https://doi.org/10.1515/9781400841929}.
  1258	
  1259	\bibitem[Rubin(2017)]{rubin2017}
  1260	Rubin, Jared. 2017. \emph{Rulers, Religion, and Riches: Why the West Got Rich and the Middle East Did Not}. Cambridge University Press. \url{https://doi.org/10.1017/9781139568272}.
  1261	
  1262	\bibitem[Sahlins(1972)]{sahlins1972b}
  1263	Sahlins, Marshall. 1972. ``The Original Affluent Society.'' In \emph{Stone Age Economics}, 1-39. Chicago: Aldine-Atherton. \url{https://doi.org/10.4324/9781003058762-1}.
  1264	
  1265	\bibitem[Scott(2009)]{scott2009}
  1266	Scott, James C. 2009. \emph{The Art of Not Being Governed: An Anarchist History of Upland Southeast Asia}. Yale University Press. \url{https://doi.org/10.12987/9780300156522}.
  1267	
  1268	\bibitem[Scott(2017)]{scott2017}
  1269	Scott, James C. 2017. \emph{Against the Grain: A Deep History of the Earliest States}. Yale University Press. \url{https://doi.org/10.12987/9780300231687}.
  1270	
  1271	\bibitem[Stigler(1971)]{stigler1971}
  1272	Stigler, George J. 1971. ``The Theory of Economic Regulation.'' \emph{The Bell Journal of Economics and Management Science} 2(1): 3-21. \url{https://doi.org/10.2307/3003160}.
  1273	
  1274	\bibitem[Tilly(1990)]{tilly1990}
  1275	Tilly, Charles. 1990. \emph{Coercion, Capital, and European States, AD 990-1990}. Blackwell.
  1276	
  1277	\bibitem[Voslensky(1984)]{voslensky1984}
  1278	Voslensky, Michael. 1984. \emph{Nomenklatura: The Soviet Ruling Class}. Doubleday. \url{https://doi.org/10.1163/9789004635562_298}.
  1279	
  1280	\bibitem[Voss and Sherman(2000)]{voss2000}
  1281	Voss, Kim and Rachel Sherman. 2000. ``Breaking the Iron Law of Oligarchy: Union Revitalization in the American Labor Movement.'' \emph{American Journal of Sociology} 106(2): 303-349. \url{https://doi.org/10.1086/316963}.
  1282	
  1283	\bibitem[Walzer(1983)]{walzer1983}
  1284	Walzer, Michael. 1983. \emph{Spheres of Justice: A Defense of Pluralism and Equality}. Basic Books.
  1285	
  1286	\bibitem[Weber(1978)]{weber1978}
  1287	Weber, Max. 1978. \emph{Economy and Society: An Outline of Interpretive Sociology}. University of California Press. \url{https://doi.org/10.4159/9780674240827}.
  1288	
  1289	\bibitem[Weingast(1997)]{weingast1997}
  1290	Weingast, Barry R. 1997. ``The Political Foundations of Democracy and the Rule of Law.'' \emph{American Political Science Review} 91(2): 245-263. \url{https://doi.org/10.2307/2952354}.
  1291	
  1292	\bibitem[Wiessner(2005)]{wiessner2005}
  1293	Wiessner, Polly. 2005. ``Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity?'' \emph{Human Nature} 16(2): 115-145. \url{https://doi.org/10.1007/s12110-005-1000-9}.
  1294	
  1295	\bibitem[Wink(1992)]{wink1992}
  1296	Wink, Walter. 1992. \emph{Engaging the Powers: Discernment and Resistance in a World of Domination}. Fortress Press. \url{https://doi.org/10.2307/j.ctt1tm7j16}.
  1297	
  1298	\bibitem[Woodburn(1982)]{woodburn1982}
  1299	Woodburn, James. 1982. ``Egalitarian Societies.'' \emph{Man (N.S.)} 17(3): 431-451. \url{https://doi.org/10.2307/2801707}.
  1300	
  1301	\end{thebibliography}
  1302	\end{small}
  1303	
  1304	\end{document}
     1	This is pdfTeX, Version 3.141592653-2.6-1.40.29 (TeX Live 2026) (preloaded format=pdflatex 2026.3.22)  22 OCT 2026 14:04
     2	entering extended mode
     3	 restricted \write18 enabled.
     4	 %&-line parsing enabled.
     5	**formalized-state.tex
     6	(./formalized-state.tex
     7	LaTeX2e <2025-11-01>
     8	L3 programming layer <2026-01-19>
     9	(/usr/local/texlive/2026/texmf-dist/tex/latex/base/article.cls
    10	Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
    11	(/usr/local/texlive/2026/texmf-dist/tex/latex/base/size11.clo
    12	File: size11.clo 2025/01/22 v1.4n Standard LaTeX file (size option)
    13	)
    14	\c@part=\count275
    15	\c@section=\count276
    16	\c@subsection=\count277
    17	\c@subsubsection=\count278
    18	\c@paragraph=\count279
    19	\c@subparagraph=\count280
    20	\c@figure=\count281
    21	\c@table=\count282
    22	\abovecaptionskip=\skip49
    23	\belowcaptionskip=\skip50
    24	\bibindent=\dimen148
    25	)
    26	(/usr/local/texlive/2026/texmf-dist/tex/latex/base/fontenc.sty
    27	Package: fontenc 2025/07/18 v2.1d Standard LaTeX package
    28	)
    29	(/usr/local/texlive/2026/texmf-dist/tex/latex/lm/lmodern.sty
    30	Package: lmodern 2015/05/01 v1.6.1 Latin Modern Fonts
    31	LaTeX Font Info:    Overwriting symbol font `operators' in version `normal'
    32	(Font)                  OT1/cmr/m/n --> OT1/lmr/m/n on input line 22.
    33	LaTeX Font Info:    Overwriting symbol font `letters' in version `normal'
    34	(Font)                  OML/cmm/m/it --> OML/lmm/m/it on input line 23.
    35	LaTeX Font Info:    Overwriting symbol font `symbols' in version `normal'
    36	(Font)                  OMS/cmsy/m/n --> OMS/lmsy/m/n on input line 24.
    37	LaTeX Font Info:    Overwriting symbol font `largesymbols' in version `normal'
    38	(Font)                  OMX/cmex/m/n --> OMX/lmex/m/n on input line 25.
    39	LaTeX Font Info:    Overwriting symbol font `operators' in version `bold'
    40	(Font)                  OT1/cmr/bx/n --> OT1/lmr/bx/n on input line 26.
    41	LaTeX Font Info:    Overwriting symbol font `letters' in version `bold'
    42	(Font)                  OML/cmm/b/it --> OML/lmm/b/it on input line 27.
    43	LaTeX Font Info:    Overwriting symbol font `symbols' in version `bold'
    44	(Font)                  OMS/cmsy/b/n --> OMS/lmsy/b/n on input line 28.
    45	LaTeX Font Info:    Overwriting symbol font `largesymbols' in version `bold'
    46	(Font)                  OMX/cmex/m/n --> OMX/lmex/m/n on input line 29.
    47	LaTeX Font Info:    Overwriting math alphabet `\mathbf' in version `normal'
    48	(Font)                  OT1/cmr/bx/n --> OT1/lmr/bx/n on input line 31.
    49	LaTeX Font Info:    Overwriting math alphabet `\mathsf' in version `normal'
    50	(Font)                  OT1/cmss/m/n --> OT1/lmss/m/n on input line 32.
    51	LaTeX Font Info:    Overwriting math alphabet `\mathit' in version `normal'
    52	(Font)                  OT1/cmr/m/it --> OT1/lmr/m/it on input line 33.
    53	LaTeX Font Info:    Overwriting math alphabet `\mathtt' in version `normal'
    54	(Font)                  OT1/cmtt/m/n --> OT1/lmtt/m/n on input line 34.
    55	LaTeX Font Info:    Overwriting math alphabet `\mathbf' in version `bold'
    56	(Font)                  OT1/cmr/bx/n --> OT1/lmr/bx/n on input line 35.
    57	LaTeX Font Info:    Overwriting math alphabet `\mathsf' in version `bold'
    58	(Font)                  OT1/cmss/bx/n --> OT1/lmss/bx/n on input line 36.
    59	LaTeX Font Info:    Overwriting math alphabet `\mathit' in version `bold'
    60	(Font)                  OT1/cmr/bx/it --> OT1/lmr/bx/it on input line 37.
    61	LaTeX Font Info:    Overwriting math alphabet `\mathtt' in version `bold'
    62	(Font)                  OT1/cmtt/m/n --> OT1/lmtt/m/n on input line 38.
    63	)
    64	(/usr/local/texlive/2026/texmf-dist/tex/latex/microtype/microtype.sty
    65	Package: microtype 2026/03/01 v3.2d Micro-typographical refinements (RS)
    66	
    67	(/usr/local/texlive/2026/texmf-dist/tex/latex/graphics/keyval.sty
    68	Package: keyval 2022/05/29 v1.15 key=value parser (DPC)
    69	\KV@toks@=\toks17
    70	)
    71	(/usr/local/texlive/2026/texmf-dist/tex/latex/etoolbox/etoolbox.sty
    72	Package: etoolbox 2025/10/02 v2.5m e-TeX tools for LaTeX (JAW)
    73	\etb@tempcnta=\count283
    74	)
    75	\MT@toks=\toks18
    76	\MT@tempbox=\box53
    77	\MT@count=\count284
    78	LaTeX Info: Redefining \noprotrusionifhmode on input line 1084.
    79	LaTeX Info: Redefining \leftprotrusion on input line 1085.
    80	\MT@prot@toks=\toks19
    81	LaTeX Info: Redefining \rightprotrusion on input line 1104.
    82	LaTeX Info: Redefining \textls on input line 1449.
    83	\MT@outer@kern=\dimen149
    84	LaTeX Info: Redefining \microtypecontext on input line 2053.
    85	LaTeX Info: Redefining \textmicrotypecontext on input line 2070.
    86	\MT@listname@count=\count285
    87	
    88	(/usr/local/texlive/2026/texmf-dist/tex/latex/microtype/microtype-pdftex.def
    89	File: microtype-pdftex.def 2026/03/01 v3.2d Definitions specific to pdftex (RS)
    90	
    91	LaTeX Info: Redefining \lsstyle on input line 944.
    92	LaTeX Info: Redefining \lslig on input line 944.
    93	\MT@outer@space=\skip51
    94	)
    95	Package microtype Info: Loading configuration file microtype.cfg.
    96	
    97	(/usr/local/texlive/2026/texmf-dist/tex/latex/microtype/microtype.cfg
    98	File: microtype.cfg 2026/03/01 v3.2d microtype main configuration file (RS)
    99	)
   100	LaTeX Info: Redefining \microtypesetup on input line 3065.
   101	)
   102	(/usr/local/texlive/2026/texmf-dist/tex/latex/geometry/geometry.sty
   103	Package: geometry 2026/03/07 v6.0 Page Geometry
   104	
   105	(/usr/local/texlive/2026/texmf-dist/tex/generic/iftex/ifvtex.sty
   106	Package: ifvtex 2019/10/25 v1.7 ifvtex legacy package. Use iftex instead.
   107	
   108	(/usr/local/texlive/2026/texmf-dist/tex/generic/iftex/iftex.sty
   109	Package: iftex 2024/12/12 v1.0g TeX engine tests
   110	))
   111	\Gm@cnth=\count286
   112	\Gm@cntv=\count287
   113	\c@Gm@tempcnt=\count288
   114	\Gm@bindingoffset=\dimen150
   115	\Gm@wd@mp=\dimen151
   116	\Gm@odd@mp=\dimen152
   117	\Gm@even@mp=\dimen153
   118	\Gm@layoutwidth=\dimen154
   119	\Gm@layoutheight=\dimen155
   120	\Gm@layouthoffset=\dimen156
   121	\Gm@layoutvoffset=\dimen157
   122	\Gm@dimlist=\toks20
   123	)
   124	(/usr/local/texlive/2026/texmf-dist/tex/latex/amsmath/amsmath.sty
   125	Package: amsmath 2025/07/09 v2.17z AMS math features
   126	\@mathmargin=\skip52
   127	
   128	For additional information on amsmath, use the `?' option.
   129	(/usr/local/texlive/2026/texmf-dist/tex/latex/amsmath/amstext.sty
   130	Package: amstext 2024/11/17 v2.01 AMS text
   131	
   132	(/usr/local/texlive/2026/texmf-dist/tex/latex/amsmath/amsgen.sty
   133	File: amsgen.sty 1999/11/30 v2.0 generic functions
   134	\@emptytoks=\toks21
   135	\ex@=\dimen158
   136	))
   137	(/usr/local/texlive/2026/texmf-dist/tex/latex/amsmath/amsbsy.sty
   138	Package: amsbsy 1999/11/29 v1.2d Bold Symbols
   139	\pmbraise@=\dimen159
   140	)
   141	(/usr/local/texlive/2026/texmf-dist/tex/latex/amsmath/amsopn.sty
   142	Package: amsopn 2022/04/08 v2.04 operator names
   143	)
   144	\inf@bad=\count289
   145	LaTeX Info: Redefining \frac on input line 233.
   146	\uproot@=\count290
   147	\leftroot@=\count291
   148	LaTeX Info: Redefining \overline on input line 398.
   149	LaTeX Info: Redefining \colon on input line 409.
   150	\classnum@=\count292
   151	\DOTSCASE@=\count293
   152	LaTeX Info: Redefining \ldots on input line 495.
   153	LaTeX Info: Redefining \dots on input line 498.
   154	LaTeX Info: Redefining \cdots on input line 619.
   155	\Mathstrutbox@=\box54
   156	\strutbox@=\box55
   157	LaTeX Info: Redefining \big on input line 721.
   158	LaTeX Info: Redefining \Big on input line 722.
   159	LaTeX Info: Redefining \bigg on input line 723.
   160	LaTeX Info: Redefining \Bigg on input line 724.
   161	\big@size=\dimen160
   162	LaTeX Font Info:    Redeclaring font encoding OML on input line 742.
   163	LaTeX Font Info:    Redeclaring font encoding OMS on input line 743.
   164	\macc@depth=\count294
   165	LaTeX Info: Redefining \bmod on input line 904.
   166	LaTeX Info: Redefining \pmod on input line 909.
   167	LaTeX Info: Redefining \smash on input line 939.
   168	LaTeX Info: Redefining \relbar on input line 969.
   169	LaTeX Info: Redefining \Relbar on input line 970.
   170	\c@MaxMatrixCols=\count295
   171	\dotsspace@=\muskip17
   172	\c@parentequation=\count296
   173	\dspbrk@lvl=\count297
   174	\tag@help=\toks22
   175	\row@=\count298
   176	\column@=\count299
   177	\maxfields@=\count300
   178	\andhelp@=\toks23
   179	\eqnshift@=\dimen161
   180	\alignsep@=\dimen162
   181	\tagshift@=\dimen163
   182	\tagwidth@=\dimen164
   183	\totwidth@=\dimen165
   184	\lineht@=\dimen166
   185	\@envbody=\toks24
   186	\multlinegap=\skip53
   187	\multlinetaggap=\skip54
   188	\mathdisplay@stack=\toks25
   189	LaTeX Info: Redefining \[ on input line 2950.
   190	LaTeX Info: Redefining \] on input line 2951.
   191	)
   192	(/usr/local/texlive/2026/texmf-dist/tex/latex/amsfonts/amssymb.sty
   193	Package: amssymb 2013/01/14 v3.01 AMS font symbols
   194	
   195	(/usr/local/texlive/2026/texmf-dist/tex/latex/amsfonts/amsfonts.sty
   196	Package: amsfonts 2013/01/14 v3.01 Basic AMSFonts support
   197	\symAMSa=\mathgroup4
   198	\symAMSb=\mathgroup5
   199	LaTeX Font Info:    Redeclaring math symbol \hbar on input line 98.
   200	LaTeX Font Info:    Overwriting math alphabet `\mathfrak' in version `bold'
   201	(Font)                  U/euf/m/n --> U/euf/b/n on input line 106.
   202	))
   203	(/usr/local/texlive/2026/texmf-dist/tex/latex/amscls/amsthm.sty
   204	Package: amsthm 2020/05/29 v2.20.6
   205	\thm@style=\toks26
   206	\thm@bodyfont=\toks27
   207	\thm@headfont=\toks28
   208	\thm@notefont=\toks29
   209	\thm@headpunct=\toks30
   210	\thm@preskip=\skip55
   211	\thm@postskip=\skip56
   212	\thm@headsep=\skip57
   213	\dth@everypar=\toks31
   214	)
   215	(/usr/local/texlive/2026/texmf-dist/tex/latex/graphics/graphicx.sty
   216	Package: graphicx 2024/12/31 v1.2e Enhanced LaTeX Graphics (DPC,SPQR)
   217	
   218	(/usr/local/texlive/2026/texmf-dist/tex/latex/graphics/graphics.sty
   219	Package: graphics 2024/08/06 v1.4g Standard LaTeX Graphics (DPC,SPQR)
   220	
   221	(/usr/local/texlive/2026/texmf-dist/tex/latex/graphics/trig.sty
   222	Package: trig 2023/12/02 v1.11 sin cos tan (DPC)
   223	)
   224	(/usr/local/texlive/2026/texmf-dist/tex/latex/graphics-cfg/graphics.cfg
   225	File: graphics.cfg 2016/06/04 v1.11 sample graphics configuration
   226	)
   227	Package graphics Info: Driver file: pdftex.def on input line 106.
   228	
   229	(/usr/local/texlive/2026/texmf-dist/tex/latex/graphics-def/pdftex.def
   230	File: pdftex.def 2025/09/29 v1.2d Graphics/color driver for pdftex
   231	))
   232	\Gin@req@height=\dimen167
   233	\Gin@req@width=\dimen168
   234	)
   235	(/usr/local/texlive/2026/texmf-dist/tex/latex/xcolor/xcolor.sty
   236	Package: xcolor 2024/09/29 v3.02 LaTeX color extensions (UK)
   237	
   238	(/usr/local/texlive/2026/texmf-dist/tex/latex/graphics-cfg/color.cfg
   239	File: color.cfg 2016/01/02 v1.6 sample color configuration
   240	)
   241	Package xcolor Info: Driver file: pdftex.def on input line 274.
   242	
   243	(/usr/local/texlive/2026/texmf-dist/tex/latex/graphics/mathcolor.ltx)
   244	Package xcolor Info: Model `cmy' substituted by `cmy0' on input line 1349.
   245	Package xcolor Info: Model `hsb' substituted by `rgb' on input line 1353.
   246	Package xcolor Info: Model `RGB' extended on input line 1365.
   247	Package xcolor Info: Model `HTML' substituted by `rgb' on input line 1367.
   248	Package xcolor Info: Model `Hsb' substituted by `hsb' on input line 1368.
   249	Package xcolor Info: Model `tHsb' substituted by `hsb' on input line 1369.
   250	Package xcolor Info: Model `HSB' substituted by `hsb' on input line 1370.
   251	Package xcolor Info: Model `Gray' substituted by `gray' on input line 1371.
   252	Package xcolor Info: Model `wave' substituted by `hsb' on input line 1372.
   253	)
   254	(/usr/local/texlive/2026/texmf-dist/tex/latex/pgf/frontendlayer/tikz.sty
   255	(/usr/local/texlive/2026/texmf-dist/tex/latex/pgf/basiclayer/pgf.sty
   256	(/usr/local/texlive/2026/texmf-dist/tex/latex/pgf/utilities/pgfrcs.sty
   257	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/utilities/pgfutil-common.te
   258	x
   259	\pgfutil@everybye=\toks32
   260	\pgfutil@tempdima=\dimen169
   261	\pgfutil@tempdimb=\dimen170
   262	)
   263	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/utilities/pgfutil-latex.def
   264	\pgfutil@abb=\box56
   265	) (/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/utilities/pgfrcs.code.tex
   266	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/pgf.revision.tex)
   267	Package: pgfrcs 2025-08-29 v3.1.11a (3.1.11a)
   268	))
   269	Package: pgf 2025-08-29 v3.1.11a (3.1.11a)
   270	
   271	(/usr/local/texlive/2026/texmf-dist/tex/latex/pgf/basiclayer/pgfcore.sty
   272	(/usr/local/texlive/2026/texmf-dist/tex/latex/pgf/systemlayer/pgfsys.sty
   273	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/systemlayer/pgfsys.code.tex
   274	Package: pgfsys 2025-08-29 v3.1.11a (3.1.11a)
   275	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/utilities/pgfkeys.code.tex
   276	\pgfkeys@pathtoks=\toks33
   277	\pgfkeys@temptoks=\toks34
   278	
   279	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/utilities/pgfkeyslibraryfil
   280	tered.code.tex
   281	\pgfkeys@tmptoks=\toks35
   282	))
   283	\pgf@x=\dimen171
   284	\pgf@y=\dimen172
   285	\pgf@xa=\dimen173
   286	\pgf@ya=\dimen174
   287	\pgf@xb=\dimen175
   288	\pgf@yb=\dimen176
   289	\pgf@xc=\dimen177
   290	\pgf@yc=\dimen178
   291	\pgf@xd=\dimen179
   292	\pgf@yd=\dimen180
   293	\w@pgf@writea=\write3
   294	\r@pgf@reada=\read2
   295	\c@pgf@counta=\count301
   296	\c@pgf@countb=\count302
   297	\c@pgf@countc=\count303
   298	\c@pgf@countd=\count304
   299	\t@pgf@toka=\toks36
   300	\t@pgf@tokb=\toks37
   301	\t@pgf@tokc=\toks38
   302	\pgf@sys@id@count=\count305
   303	
   304	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/systemlayer/pgf.cfg
   305	File: pgf.cfg 2025-08-29 v3.1.11a (3.1.11a)
   306	)
   307	Driver file for pgf: pgfsys-pdftex.def
   308	
   309	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-pdftex.d
   310	ef
   311	File: pgfsys-pdftex.def 2025-08-29 v3.1.11a (3.1.11a)
   312	
   313	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-common-p
   314	df.def
   315	File: pgfsys-common-pdf.def 2025-08-29 v3.1.11a (3.1.11a)
   316	)))
   317	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/systemlayer/pgfsyssoftpath.
   318	code.tex
   319	File: pgfsyssoftpath.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   320	\pgfsyssoftpath@smallbuffer@items=\count306
   321	\pgfsyssoftpath@bigbuffer@items=\count307
   322	)
   323	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/systemlayer/pgfsysprotocol.
   324	code.tex
   325	File: pgfsysprotocol.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   326	))
   327	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/basiclayer/pgfcore.code.tex
   328	Package: pgfcore 2025-08-29 v3.1.11a (3.1.11a)
   329	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/math/pgfmath.code.tex
   330	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/math/pgfmathutil.code.tex)
   331	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/math/pgfmathparser.code.tex
   332	\pgfmath@dimen=\dimen181
   333	\pgfmath@count=\count308
   334	\pgfmath@box=\box57
   335	\pgfmath@toks=\toks39
   336	\pgfmath@stack@operand=\toks40
   337	\pgfmath@stack@operation=\toks41
   338	)
   339	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.code.
   340	tex)
   341	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.basic
   342	.code.tex)
   343	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.trigo
   344	nometric.code.tex)
   345	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.rando
   346	m.code.tex)
   347	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.compa
   348	rison.code.tex)
   349	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.base.
   350	code.tex)
   351	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.round
   352	.code.tex)
   353	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.misc.
   354	code.tex)
   355	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.integ
   356	erarithmetics.code.tex)
   357	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/math/pgfmathcalc.code.tex)
   358	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/math/pgfmathfloat.code.tex
   359	\c@pgfmathroundto@lastzeros=\count309
   360	)) (/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/math/pgfint.code.tex)
   361	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepoints.co
   362	de.tex
   363	File: pgfcorepoints.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   364	\pgf@picminx=\dimen182
   365	\pgf@picmaxx=\dimen183
   366	\pgf@picminy=\dimen184
   367	\pgf@picmaxy=\dimen185
   368	\pgf@pathminx=\dimen186
   369	\pgf@pathmaxx=\dimen187
   370	\pgf@pathminy=\dimen188
   371	\pgf@pathmaxy=\dimen189
   372	\pgf@xx=\dimen190
   373	\pgf@xy=\dimen191
   374	\pgf@yx=\dimen192
   375	\pgf@yy=\dimen193
   376	\pgf@zx=\dimen194
   377	\pgf@zy=\dimen195
   378	)
   379	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepathconst
   380	ruct.code.tex
   381	File: pgfcorepathconstruct.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   382	\pgf@path@lastx=\dimen196
   383	\pgf@path@lasty=\dimen197
   384	)
   385	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepathusage
   386	.code.tex
   387	File: pgfcorepathusage.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   388	\pgf@shorten@end@additional=\dimen198
   389	\pgf@shorten@start@additional=\dimen199
   390	)
   391	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/basiclayer/pgfcorescopes.co
   392	de.tex
   393	File: pgfcorescopes.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   394	\pgfpic=\box58
   395	\pgf@hbox=\box59
   396	\pgf@layerbox@main=\box60
   397	\pgf@picture@serial@count=\count310
   398	)
   399	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/basiclayer/pgfcoregraphicst
   400	ate.code.tex
   401	File: pgfcoregraphicstate.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   402	\pgflinewidth=\dimen256
   403	)
   404	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/basiclayer/pgfcoretransform
   405	ations.code.tex
   406	File: pgfcoretransformations.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   407	\pgf@pt@x=\dimen257
   408	\pgf@pt@y=\dimen258
   409	\pgf@pt@temp=\dimen259
   410	)
   411	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/basiclayer/pgfcorequick.cod
   412	e.tex
   413	File: pgfcorequick.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   414	)
   415	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreobjects.c
   416	ode.tex
   417	File: pgfcoreobjects.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   418	)
   419	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepathproce
   420	ssing.code.tex
   421	File: pgfcorepathprocessing.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   422	)
   423	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/basiclayer/pgfcorearrows.co
   424	de.tex
   425	File: pgfcorearrows.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   426	\pgfarrowsep=\dimen260
   427	)
   428	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreshade.cod
   429	e.tex
   430	File: pgfcoreshade.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   431	\pgf@max=\dimen261
   432	\pgf@sys@shading@range@num=\count311
   433	\pgf@shadingcount=\count312
   434	)
   435	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreimage.cod
   436	e.tex
   437	File: pgfcoreimage.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   438	)
   439	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreexternal.
   440	code.tex
   441	File: pgfcoreexternal.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   442	\pgfexternal@startupbox=\box61
   443	)
   444	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/basiclayer/pgfcorelayers.co
   445	de.tex
   446	File: pgfcorelayers.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   447	)
   448	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/basiclayer/pgfcoretranspare
   449	ncy.code.tex
   450	File: pgfcoretransparency.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   451	)
   452	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepatterns.
   453	code.tex
   454	File: pgfcorepatterns.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   455	)
   456	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/basiclayer/pgfcorerdf.code.
   457	tex
   458	File: pgfcorerdf.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   459	)))
   460	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/modules/pgfmoduleshapes.cod
   461	e.tex
   462	File: pgfmoduleshapes.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   463	\pgfnodeparttextbox=\box62
   464	)
   465	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/modules/pgfmoduleplot.code.
   466	tex
   467	File: pgfmoduleplot.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   468	)
   469	(/usr/local/texlive/2026/texmf-dist/tex/latex/pgf/compatibility/pgfcomp-version
   470	-0-65.sty
   471	Package: pgfcomp-version-0-65 2025-08-29 v3.1.11a (3.1.11a)
   472	\pgf@nodesepstart=\dimen262
   473	\pgf@nodesepend=\dimen263
   474	)
   475	(/usr/local/texlive/2026/texmf-dist/tex/latex/pgf/compatibility/pgfcomp-version
   476	-1-18.sty
   477	Package: pgfcomp-version-1-18 2025-08-29 v3.1.11a (3.1.11a)
   478	))
   479	(/usr/local/texlive/2026/texmf-dist/tex/latex/pgf/utilities/pgffor.sty
   480	(/usr/local/texlive/2026/texmf-dist/tex/latex/pgf/utilities/pgfkeys.sty
   481	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/utilities/pgfkeys.code.tex)
   482	) (/usr/local/texlive/2026/texmf-dist/tex/latex/pgf/math/pgfmath.sty
   483	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/math/pgfmath.code.tex))
   484	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/utilities/pgffor.code.tex
   485	Package: pgffor 2025-08-29 v3.1.11a (3.1.11a)
   486	\pgffor@iter=\dimen264
   487	\pgffor@skip=\dimen265
   488	\pgffor@stack=\toks42
   489	\pgffor@toks=\toks43
   490	))
   491	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/frontendlayer/tikz/tikz.cod
   492	e.tex
   493	Package: tikz 2025-08-29 v3.1.11a (3.1.11a)
   494	
   495	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/libraries/pgflibraryplothan
   496	dlers.code.tex
   497	File: pgflibraryplothandlers.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   498	\pgf@plot@mark@count=\count313
   499	\pgfplotmarksize=\dimen266
   500	)
   501	\tikz@lastx=\dimen267
   502	\tikz@lasty=\dimen268
   503	\tikz@lastxsaved=\dimen269
   504	\tikz@lastysaved=\dimen270
   505	\tikz@lastmovetox=\dimen271
   506	\tikz@lastmovetoy=\dimen272
   507	\tikzleveldistance=\dimen273
   508	\tikzsiblingdistance=\dimen274
   509	\tikz@figbox=\box63
   510	\tikz@figbox@bg=\box64
   511	\tikz@tempbox=\box65
   512	\tikz@tempbox@bg=\box66
   513	\tikztreelevel=\count314
   514	\tikznumberofchildren=\count315
   515	\tikznumberofcurrentchild=\count316
   516	\tikz@fig@count=\count317
   517	
   518	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/modules/pgfmodulematrix.cod
   519	e.tex
   520	File: pgfmodulematrix.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   521	\pgfmatrixcurrentrow=\count318
   522	\pgfmatrixcurrentcolumn=\count319
   523	\pgf@matrix@numberofcolumns=\count320
   524	)
   525	\tikz@expandcount=\count321
   526	
   527	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/frontendlayer/tikz/librarie
   528	s/tikzlibrarytopaths.code.tex
   529	File: tikzlibrarytopaths.code.tex 2025-08-29 v3.1.11a (3.1.11a)
   530	)))
   531	(/usr/local/texlive/2026/texmf-dist/tex/latex/booktabs/booktabs.sty
   532	Package: booktabs 2020/01/12 v1.61803398 Publication quality tables
   533	\heavyrulewidth=\dimen275
   534	\lightrulewidth=\dimen276
   535	\cmidrulewidth=\dimen277
   536	\belowrulesep=\dimen278
   537	\belowbottomsep=\dimen279
   538	\aboverulesep=\dimen280
   539	\abovetopsep=\dimen281
   540	\cmidrulesep=\dimen282
   541	\cmidrulekern=\dimen283
   542	\defaultaddspace=\dimen284
   543	\@cmidla=\count322
   544	\@cmidlb=\count323
   545	\@aboverulesep=\dimen285
   546	\@belowrulesep=\dimen286
   547	\@thisruleclass=\count324
   548	\@lastruleclass=\count325
   549	\@thisrulewidth=\dimen287
   550	)
   551	(/usr/local/texlive/2026/texmf-dist/tex/latex/tools/tabularx.sty
   552	Package: tabularx 2023/12/11 v2.12a `tabularx' package (DPC)
   553	
   554	(/usr/local/texlive/2026/texmf-dist/tex/latex/tools/array.sty
   555	Package: array 2025/09/25 v2.6n Tabular extension package (FMi)
   556	\col@sep=\dimen288
   557	\ar@mcellbox=\box67
   558	\extrarowheight=\dimen289
   559	\NC@list=\toks44
   560	\extratabsurround=\skip58
   561	\backup@length=\skip59
   562	\ar@cellbox=\box68
   563	)
   564	\TX@col@width=\dimen290
   565	\TX@old@table=\dimen291
   566	\TX@old@col=\dimen292
   567	\TX@target=\dimen293
   568	\TX@delta=\dimen294
   569	\TX@cols=\count326
   570	\TX@ftn=\toks45
   571	)
   572	(/usr/local/texlive/2026/texmf-dist/tex/latex/tools/longtable.sty
   573	Package: longtable 2025-10-13 v4.24 Multi-page Table package (DPC)
   574	\LTleft=\skip60
   575	\LTright=\skip61
   576	\LTpre=\skip62
   577	\LTpost=\skip63
   578	\LTchunksize=\count327
   579	\LTcapwidth=\dimen295
   580	\LT@head=\box69
   581	\LT@firsthead=\box70
   582	\LT@foot=\box71
   583	\LT@lastfoot=\box72
   584	\LT@gbox=\box73
   585	\LT@cols=\count328
   586	\LT@rows=\count329
   587	\c@LT@tables=\count330
   588	\c@LT@chunks=\count331
   589	\LT@p@ftn=\toks46
   590	)
   591	(/usr/local/texlive/2026/texmf-dist/tex/latex/listings/listings.sty
   592	\lst@mode=\count332
   593	\lst@gtempboxa=\box74
   594	\lst@token=\toks47
   595	\lst@length=\count333
   596	\lst@currlwidth=\dimen296
   597	\lst@column=\count334
   598	\lst@pos=\count335
   599	\lst@lostspace=\dimen297
   600	\lst@width=\dimen298
   601	\lst@newlines=\count336
   602	\lst@lineno=\count337
   603	\lst@maxwidth=\dimen299
   604	
   605	(/usr/local/texlive/2026/texmf-dist/tex/latex/listings/lstpatch.sty
   606	File: lstpatch.sty 2025/11/14 1.11b (Carsten Heinz)
   607	)
   608	(/usr/local/texlive/2026/texmf-dist/tex/latex/listings/lstmisc.sty
   609	File: lstmisc.sty 2025/11/14 1.11b (Carsten Heinz)
   610	\c@lstnumber=\count338
   611	\lst@skipnumbers=\count339
   612	\lst@framebox=\box75
   613	)
   614	(/usr/local/texlive/2026/texmf-dist/tex/latex/listings/listings.cfg
   615	File: listings.cfg 2025/11/14 1.11b listings configuration
   616	))
   617	Package: listings 2025/11/14 1.11b (Carsten Heinz)
   618	
   619	==> First Aid for listings.sty no longer applied!
   620	    Expected:
   621	        2024/09/23 1.10c (Carsten Heinz)
   622	    but found:
   623	        2025/11/14 1.11b (Carsten Heinz)
   624	    so I'm assuming it got fixed.
   625	(/usr/local/texlive/2026/texmf-dist/tex/latex/natbib/natbib.sty
   626	Package: natbib 2010/09/13 8.31b (PWD, AO)
   627	\bibhang=\skip64
   628	\bibsep=\skip65
   629	LaTeX Info: Redefining \cite on input line 694.
   630	\c@NAT@ctr=\count340
   631	)
   632	(/usr/local/texlive/2026/texmf-dist/tex/latex/enumitem/enumitem.sty
   633	Package: enumitem 2025/02/06 v3.11 Customized lists
   634	\labelindent=\skip66
   635	\enit@outerparindent=\dimen300
   636	\enit@toks=\toks48
   637	\enit@inbox=\box76
   638	\enit@count@id=\count341
   639	\enitdp@description=\count342
   640	)
   641	(/usr/local/texlive/2026/texmf-dist/tex/latex/hyperref/hyperref.sty
   642	Package: hyperref 2026-01-29 v7.01p Hypertext links for LaTeX
   643	
   644	(/usr/local/texlive/2026/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty
   645	Package: kvsetkeys 2022-10-05 v1.19 Key value parser (HO)
   646	)
   647	(/usr/local/texlive/2026/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty
   648	Package: kvdefinekeys 2019-12-19 v1.6 Define keys (HO)
   649	)
   650	(/usr/local/texlive/2026/texmf-dist/tex/generic/pdfescape/pdfescape.sty
   651	Package: pdfescape 2019/12/09 v1.15 Implements pdfTeX's escape features (HO)
   652	
   653	(/usr/local/texlive/2026/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty
   654	Package: ltxcmds 2023-12-04 v1.26 LaTeX kernel commands for general use (HO)
   655	)
   656	(/usr/local/texlive/2026/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty
   657	Package: pdftexcmds 2020-06-27 v0.33 Utility functions of pdfTeX for LuaTeX (HO
   658	)
   659	
   660	(/usr/local/texlive/2026/texmf-dist/tex/generic/infwarerr/infwarerr.sty
   661	Package: infwarerr 2019/12/03 v1.5 Providing info/warning/error messages (HO)
   662	)
   663	Package pdftexcmds Info: \pdf@primitive is available.
   664	Package pdftexcmds Info: \pdf@ifprimitive is available.
   665	Package pdftexcmds Info: \pdfdraftmode found.
   666	))
   667	(/usr/local/texlive/2026/texmf-dist/tex/latex/hycolor/hycolor.sty
   668	Package: hycolor 2020-01-27 v1.10 Color options for hyperref/bookmark (HO)
   669	)
   670	(/usr/local/texlive/2026/texmf-dist/tex/latex/hyperref/nameref.sty
   671	Package: nameref 2026-01-29 v2.58 Cross-referencing by name of section
   672	
   673	(/usr/local/texlive/2026/texmf-dist/tex/latex/refcount/refcount.sty
   674	Package: refcount 2019/12/15 v3.6 Data extraction from label references (HO)
   675	)
   676	(/usr/local/texlive/2026/texmf-dist/tex/generic/gettitlestring/gettitlestring.s
   677	ty
   678	Package: gettitlestring 2019/12/15 v1.6 Cleanup title references (HO)
   679	 (/usr/local/texlive/2026/texmf-dist/tex/latex/kvoptions/kvoptions.sty
   680	Package: kvoptions 2022-06-15 v3.15 Key value format for package options (HO)
   681	))
   682	\c@section@level=\count343
   683	)
   684	(/usr/local/texlive/2026/texmf-dist/tex/generic/stringenc/stringenc.sty
   685	Package: stringenc 2019/11/29 v1.12 Convert strings between diff. encodings (HO
   686	)
   687	)
   688	\@linkdim=\dimen301
   689	\Hy@linkcounter=\count344
   690	\Hy@pagecounter=\count345
   691	
   692	(/usr/local/texlive/2026/texmf-dist/tex/latex/hyperref/pd1enc.def
   693	File: pd1enc.def 2026-01-29 v7.01p Hyperref: PDFDocEncoding definition (HO)
   694	Now handling font encoding PD1 ...
   695	... no UTF-8 mapping file for font encoding PD1
   696	)
   697	(/usr/local/texlive/2026/texmf-dist/tex/generic/intcalc/intcalc.sty
   698	Package: intcalc 2019/12/15 v1.3 Expandable calculations with integers (HO)
   699	)
   700	\Hy@SavedSpaceFactor=\count346
   701	
   702	(/usr/local/texlive/2026/texmf-dist/tex/latex/hyperref/puenc.def
   703	File: puenc.def 2026-01-29 v7.01p Hyperref: PDF Unicode definition (HO)
   704	Now handling font encoding PU ...
   705	... no UTF-8 mapping file for font encoding PU
   706	)
   707	Package hyperref Info: Hyper figures OFF on input line 4201.
   708	Package hyperref Info: Link nesting OFF on input line 4206.
   709	Package hyperref Info: Hyper index ON on input line 4209.
   710	Package hyperref Info: Plain pages OFF on input line 4216.
   711	Package hyperref Info: Backreferencing OFF on input line 4221.
   712	Package hyperref Info: Implicit mode ON; LaTeX internals redefined.
   713	Package hyperref Info: Bookmarks ON on input line 4468.
   714	\c@Hy@tempcnt=\count347
   715	
   716	(/usr/local/texlive/2026/texmf-dist/tex/latex/url/url.sty
   717	\Urlmuskip=\muskip18
   718	Package: url 2013/09/16  ver 3.4  Verb mode for urls, etc.
   719	)
   720	LaTeX Info: Redefining \url on input line 4807.
   721	\XeTeXLinkMargin=\dimen302
   722	
   723	(/usr/local/texlive/2026/texmf-dist/tex/generic/bitset/bitset.sty
   724	Package: bitset 2019/12/09 v1.3 Handle bit-vector datatype (HO)
   725	
   726	(/usr/local/texlive/2026/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty
   727	Package: bigintcalc 2019/12/15 v1.5 Expandable calculations on big integers (HO
   728	)
   729	))
   730	\Fld@menulength=\count348
   731	\Field@Width=\dimen303
   732	\Fld@charsize=\dimen304
   733	Package hyperref Info: Hyper figures OFF on input line 6084.
   734	Package hyperref Info: Link nesting OFF on input line 6089.
   735	Package hyperref Info: Hyper index ON on input line 6092.
   736	Package hyperref Info: backreferencing OFF on input line 6099.
   737	Package hyperref Info: Link coloring OFF on input line 6104.
   738	Package hyperref Info: Link coloring with OCG OFF on input line 6109.
   739	Package hyperref Info: PDF/A mode OFF on input line 6114.
   740	\Hy@abspage=\count349
   741	\c@Item=\count350
   742	\c@Hfootnote=\count351
   743	)
   744	Package hyperref Info: Driver (autodetected): hpdftex.
   745	
   746	(/usr/local/texlive/2026/texmf-dist/tex/latex/hyperref/hpdftex.def
   747	File: hpdftex.def 2026-01-29 v7.01p Hyperref driver for pdfTeX
   748	\Fld@listcount=\count352
   749	\c@bookmark@seq@number=\count353
   750	
   751	(/usr/local/texlive/2026/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
   752	Package: rerunfilecheck 2025-06-21 v1.11 Rerun checks for auxiliary files (HO)
   753	
   754	(/usr/local/texlive/2026/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty
   755	Package: uniquecounter 2019/12/15 v1.4 Provide unlimited unique counter (HO)
   756	)
   757	Package uniquecounter Info: New unique counter `rerunfilecheck' on input line 2
   758	84.
   759	)
   760	\Hy@SectionHShift=\skip67
   761	) (/usr/local/texlive/2026/texmf-dist/tex/latex/cleveref/cleveref.sty
   762	Package: cleveref 2018/03/27 v0.21.4 Intelligent cross-referencing
   763	Package cleveref Info: `hyperref' support loaded on input line 2370.
   764	LaTeX Info: Redefining \cref on input line 2370.
   765	LaTeX Info: Redefining \Cref on input line 2370.
   766	LaTeX Info: Redefining \crefrange on input line 2370.
   767	LaTeX Info: Redefining \Crefrange on input line 2370.
   768	LaTeX Info: Redefining \cpageref on input line 2370.
   769	LaTeX Info: Redefining \Cpageref on input line 2370.
   770	LaTeX Info: Redefining \cpagerefrange on input line 2370.
   771	LaTeX Info: Redefining \Cpagerefrange on input line 2370.
   772	LaTeX Info: Redefining \labelcref on input line 2370.
   773	LaTeX Info: Redefining \labelcpageref on input line 2370.
   774	Package cleveref Info: `amsthm' support loaded on input line 3026.
   775	Package cleveref Info: `listings' support loaded on input line 3131.
   776	Package cleveref Info: always capitalise cross-reference names on input line 78
   777	25.
   778	Package cleveref Info: always capitalise cross-reference names on input line 78
   779	52.
   780	)
   781	==> First Aid for cleveref.sty applied!
   782	\c@theorem=\count354
   783	LaTeX Font Info:    Trying to load font information for T1+lmr on input line 79
   784	.
   785	(/usr/local/texlive/2026/texmf-dist/tex/latex/lm/t1lmr.fd
   786	File: t1lmr.fd 2015/05/01 v1.6.1 Font defs for Latin Modern
   787	)
   788	(/usr/local/texlive/2026/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def
   789	File: l3backend-pdftex.def 2025-10-09 L3 backend support: PDF output (pdfTeX)
   790	\l__color_backend_stack_int=\count355
   791	)
   792	(./formalized-state.aux)
   793	\openout1 = `formalized-state.aux'.
   794	
   795	LaTeX Font Info:    Checking defaults for OML/cmm/m/it on input line 79.
   796	LaTeX Font Info:    ... okay on input line 79.
   797	LaTeX Font Info:    Checking defaults for OMS/cmsy/m/n on input line 79.
   798	LaTeX Font Info:    ... okay on input line 79.
   799	LaTeX Font Info:    Checking defaults for OT1/cmr/m/n on input line 79.
   800	LaTeX Font Info:    ... okay on input line 79.
   801	LaTeX Font Info:    Checking defaults for T1/cmr/m/n on input line 79.
   802	LaTeX Font Info:    ... okay on input line 79.
   803	LaTeX Font Info:    Checking defaults for TS1/cmr/m/n on input line 79.
   804	LaTeX Font Info:    ... okay on input line 79.
   805	LaTeX Font Info:    Checking defaults for OMX/cmex/m/n on input line 79.
   806	LaTeX Font Info:    ... okay on input line 79.
   807	LaTeX Font Info:    Checking defaults for U/cmr/m/n on input line 79.
   808	LaTeX Font Info:    ... okay on input line 79.
   809	LaTeX Font Info:    Checking defaults for PD1/pdf/m/n on input line 79.
   810	LaTeX Font Info:    ... okay on input line 79.
   811	LaTeX Font Info:    Checking defaults for PU/pdf/m/n on input line 79.
   812	LaTeX Font Info:    ... okay on input line 79.
   813	LaTeX Info: Redefining \microtypecontext on input line 79.
   814	Package microtype Info: Applying patch `item' on input line 79.
   815	Package microtype Info: Applying patch `toc' on input line 79.
   816	Package microtype Info: Applying patch `eqnum' on input line 79.
   817	Package microtype Info: Applying patch `footnote' on input line 79.
   818	Package microtype Info: Applying patch `verbatim' on input line 79.
   819	LaTeX Info: Redefining \microtypesetup on input line 79.
   820	Package microtype Info: Generating PDF output.
   821	Package microtype Info: Character protrusion enabled (level 2).
   822	Package microtype Info: Using default protrusion set `alltext'.
   823	Package microtype Info: Automatic font expansion enabled (level 2),
   824	(microtype)             stretch: 20, shrink: 20, step: 1, non-selected.
   825	Package microtype Info: Using default expansion set `alltext-nott'.
   826	Package microtype Info: Patching command `\showhyphens'.
   827	Package microtype Info: No adjustment of tracking.
   828	Package microtype Info: No adjustment of interword spacing.
   829	Package microtype Info: No adjustment of character kerning.
   830	
   831	(/usr/local/texlive/2026/texmf-dist/tex/latex/microtype/mt-cmr.cfg
   832	File: mt-cmr.cfg 2013/05/19 v2.2 microtype config. file: Computer Modern Roman 
   833	(RS)
   834	)
   835	*geometry* driver: auto-detecting
   836	*geometry* detected driver: pdftex
   837	*geometry* verbose mode - [ preamble ] result:
   838	* driver: pdftex
   839	* paper: letterpaper
   840	* layout: <same size as paper>
   841	* layoutoffset:(h,v)=(0.0pt,0.0pt)
   842	* modes: 
   843	* h-part:(L,W,R)=(90.3375pt, 433.62001pt, 90.3375pt)
   844	* v-part:(T,H,B)=(72.26999pt, 650.43001pt, 72.26999pt)
   845	* \paperwidth=614.295pt
   846	* \paperheight=794.96999pt
   847	* \textwidth=433.62001pt
   848	* \textheight=650.43001pt
   849	* \oddsidemargin=18.0675pt
   850	* \evensidemargin=18.0675pt
   851	* \topmargin=-37.0pt
   852	* \headheight=12.0pt
   853	* \headsep=25.0pt
   854	* \topskip=11.0pt
   855	* \footskip=30.0pt
   856	* \marginparwidth=59.0pt
   857	* \marginparsep=10.0pt
   858	* \columnsep=10.0pt
   859	* \skip\footins=10.0pt plus 4.0pt minus 2.0pt
   860	* \hoffset=0.0pt
   861	* \voffset=0.0pt
   862	* \mag=1000
   863	* \@twocolumnfalse
   864	* \@twosidefalse
   865	* \@mparswitchfalse
   866	* \@reversemarginfalse
   867	* (1in=72.27pt=25.4mm, 1cm=28.453pt)
   868	
   869	(/usr/local/texlive/2026/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
   870	[Loading MPS to PDF converter (version 2006.09.02).]
   871	\scratchcounter=\count356
   872	\scratchdimen=\dimen305
   873	\scratchbox=\box77
   874	\nofMPsegments=\count357
   875	\nofMParguments=\count358
   876	\everyMPshowfont=\toks49
   877	\MPscratchCnt=\count359
   878	\MPscratchDim=\dimen306
   879	\MPnumerator=\count360
   880	\makeMPintoPDFobject=\count361
   881	\everyMPtoPDFconversion=\toks50
   882	) (/usr/local/texlive/2026/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
   883	Package: epstopdf-base 2020-01-24 v2.11 Base part for package epstopdf
   884	
   885	(/usr/local/texlive/2026/texmf-dist/tex/latex/grfext/grfext.sty
   886	Package: grfext 2019/12/03 v1.3 Manage graphics extensions (HO)
   887	)
   888	Package epstopdf-base Info: Redefining graphics rule for `.eps' on input line 4
   889	85.
   890	Package grfext Info: Graphics extension search list:
   891	(grfext)             [.pdf,.png,.jpg,.mps,.jpeg,.jbig2,.jb2,.PDF,.PNG,.JPG,.JPE
   892	G,.JBIG2,.JB2,.eps]
   893	(grfext)             \AppendGraphicsExtensions on input line 504.
   894	
   895	(/usr/local/texlive/2026/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg
   896	File: epstopdf-sys.cfg 2010/07/13 v1.3 Configuration of (r)epstopdf for TeX Liv
   897	e
   898	))
   899	\c@lstlisting=\count362
   900	Package hyperref Info: Link coloring OFF on input line 79.
   901	
   902	(./formalized-state.out) (./formalized-state.out)
   903	\@outlinefile=\write4
   904	\openout4 = `formalized-state.out'.
   905	
   906	LaTeX Font Info:    Trying to load font information for OT1+lmr on input line 8
   907	1.
   908	
   909	(/usr/local/texlive/2026/texmf-dist/tex/latex/lm/ot1lmr.fd
   910	File: ot1lmr.fd 2015/05/01 v1.6.1 Font defs for Latin Modern
   911	)
   912	LaTeX Font Info:    Trying to load font information for OML+lmm on input line 8
   913	1.
   914	
   915	(/usr/local/texlive/2026/texmf-dist/tex/latex/lm/omllmm.fd
   916	File: omllmm.fd 2015/05/01 v1.6.1 Font defs for Latin Modern
   917	)
   918	LaTeX Font Info:    Trying to load font information for OMS+lmsy on input line 
   919	81.
   920	
   921	(/usr/local/texlive/2026/texmf-dist/tex/latex/lm/omslmsy.fd
   922	File: omslmsy.fd 2015/05/01 v1.6.1 Font defs for Latin Modern
   923	)
   924	LaTeX Font Info:    Trying to load font information for OMX+lmex on input line 
   925	81.
   926	
   927	(/usr/local/texlive/2026/texmf-dist/tex/latex/lm/omxlmex.fd
   928	File: omxlmex.fd 2015/05/01 v1.6.1 Font defs for Latin Modern
   929	)
   930	LaTeX Font Info:    External font `lmex10' loaded for size
   931	(Font)              <12> on input line 81.
   932	LaTeX Font Info:    External font `lmex10' loaded for size
   933	(Font)              <8> on input line 81.
   934	LaTeX Font Info:    External font `lmex10' loaded for size
   935	(Font)              <6> on input line 81.
   936	LaTeX Font Info:    Trying to load font information for U+msa on input line 81.
   937	
   938	
   939	(/usr/local/texlive/2026/texmf-dist/tex/latex/amsfonts/umsa.fd
   940	File: umsa.fd 2013/01/14 v3.01 AMS symbols A
   941	)
   942	(/usr/local/texlive/2026/texmf-dist/tex/latex/microtype/mt-msa.cfg
   943	File: mt-msa.cfg 2006/02/04 v1.1 microtype config. file: AMS symbols (a) (RS)
   944	)
   945	LaTeX Font Info:    Trying to load font information for U+msb on input line 81.
   946	
   947	
   948	(/usr/local/texlive/2026/texmf-dist/tex/latex/amsfonts/umsb.fd
   949	File: umsb.fd 2013/01/14 v3.01 AMS symbols B
   950	)
   951	(/usr/local/texlive/2026/texmf-dist/tex/latex/microtype/mt-msb.cfg
   952	File: mt-msb.cfg 2005/06/01 v1.0 microtype config. file: AMS symbols (b) (RS)
   953	)
   954	LaTeX Font Info:    Trying to load font information for T1+lmtt on input line 8
   955	1.
   956	
   957	(/usr/local/texlive/2026/texmf-dist/tex/latex/lm/t1lmtt.fd
   958	File: t1lmtt.fd 2015/05/01 v1.6.1 Font defs for Latin Modern
   959	)
   960	Package microtype Info: Loading generic protrusion settings for font family
   961	(microtype)             `lmtt' (encoding: T1).
   962	(microtype)             For optimal results, create family-specific settings.
   963	(microtype)             See the microtype manual for details.
   964	LaTeX Font Info:    External font `lmex10' loaded for size
   965	(Font)              <10> on input line 81.
   966	LaTeX Font Info:    External font `lmex10' loaded for size
   967	(Font)              <7> on input line 81.
   968	LaTeX Font Info:    External font `lmex10' loaded for size
   969	(Font)              <5> on input line 81.
   970	LaTeX Font Info:    External font `lmex10' loaded for size
   971	(Font)              <10.95> on input line 91.
   972	LaTeX Font Info:    Trying to load font information for T1+lmss on input line 9
   973	2.
   974	
   975	(/usr/local/texlive/2026/texmf-dist/tex/latex/lm/t1lmss.fd
   976	File: t1lmss.fd 2015/05/01 v1.6.1 Font defs for Latin Modern
   977	)
   978	Package microtype Info: Loading generic protrusion settings for font family
   979	(microtype)             `lmss' (encoding: T1).
   980	(microtype)             For optimal results, create family-specific settings.
   981	(microtype)             See the microtype manual for details.
   982	 [1{/usr/local/texlive/2026/texmf-var/fonts/map/pdftex/updmap/pdftex.map}{/usr/
   983	local/texlive/2026/texmf-dist/fonts/enc/dvips/lm/lm-ec.enc}
   984	
   985	]
   986	LaTeX Font Info:    Trying to load font information for OT1+lmss on input line 
   987	93.
   988	
   989	(/usr/local/texlive/2026/texmf-dist/tex/latex/lm/ot1lmss.fd
   990	File: ot1lmss.fd 2015/05/01 v1.6.1 Font defs for Latin Modern
   991	)
   992	Package microtype Info: Loading generic protrusion settings for font family
   993	(microtype)             `lmss' (encoding: OT1).
   994	(microtype)             For optimal results, create family-specific settings.
   995	(microtype)             See the microtype manual for details.
   996	 [2{/usr/local/texlive/2026/texmf-dist/fonts/enc/dvips/lm/lm-mathsy.enc}{/usr/l
   997	ocal/texlive/2026/texmf-dist/fonts/enc/dvips/lm/lm-rm.enc}{/usr/local/texlive/2
   998	026/texmf-dist/fonts/enc/dvips/lm/lm-mathit.enc}] [3{/usr/local/texlive/2026/te
   999	xmf-dist/fonts/enc/dvips/lm/lm-mathex.enc}] [4] [5] [6] [7] [8] [9] [10] [11] [
  1000	12] [13] [14]
  1001	[15] [16] [17] [18] [19] [20] [21] [22] [23] [24] [25] [26] [27] [28] [29]
  1002	[30] [31] [32] [33] [34] [35] [36] [37] [38] [39] [40] [41] [42] [43] [44]
  1003	[45] (./formalized-state.aux)
  1004	 ***********
  1005	LaTeX2e <2025-11-01>
  1006	L3 programming layer <2026-01-19>
  1007	 ***********
  1008	Package rerunfilecheck Info: File `formalized-state.out' has not changed.
  1009	(rerunfilecheck)             Checksum: CAE907C95F1275C106CF738D3315890D;8210.
  1010	 ) 
  1011	Here is how much of TeX's memory you used:
  1012	 28656 strings out of 467525
  1013	 521668 string characters out of 5418982
  1014	 957469 words of memory out of 5000000
  1015	 56305 multiletter control sequences out of 15000+600000
  1016	 774235 words of font info for 379 fonts, out of 8000000 for 9000
  1017	 1141 hyphenation exceptions out of 8191
  1018	 84i,12n,94p,2300b,914s stack positions out of 10000i,1000n,20000p,200000b,200000s
  1019	</usr/local/texlive/2026/texmf-dist/fonts/type1/public/lm/lmbx10.pfb></usr/lo
  1020	cal/texlive/2026/texmf-dist/fonts/type1/public/lm/lmbx12.pfb></usr/local/texliv
  1021	e/2026/texmf-dist/fonts/type1/public/lm/lmex10.pfb></usr/local/texlive/2026/tex
  1022	mf-dist/fonts/type1/public/lm/lmmi10.pfb></usr/local/texlive/2026/texmf-dist/fo
  1023	nts/type1/public/lm/lmmi6.pfb></usr/local/texlive/2026/texmf-dist/fonts/type1/p
  1024	ublic/lm/lmmi7.pfb></usr/local/texlive/2026/texmf-dist/fonts/type1/public/lm/lm
  1025	mi8.pfb></usr/local/texlive/2026/texmf-dist/fonts/type1/public/lm/lmr10.pfb></u
  1026	sr/local/texlive/2026/texmf-dist/fonts/type1/public/lm/lmr12.pfb></usr/local/te
  1027	xlive/2026/texmf-dist/fonts/type1/public/lm/lmr17.pfb></usr/local/texlive/2026/
  1028	texmf-dist/fonts/type1/public/lm/lmr6.pfb></usr/local/texlive/2026/texmf-dist/f
  1029	onts/type1/public/lm/lmr8.pfb></usr/local/texlive/2026/texmf-dist/fonts/type1/p
  1030	ublic/lm/lmr9.pfb></usr/local/texlive/2026/texmf-dist/fonts/type1/public/lm/lmr
  1031	i10.pfb></usr/local/texlive/2026/texmf-dist/fonts/type1/public/lm/lmss10.pfb></
  1032	usr/local/texlive/2026/texmf-dist/fonts/type1/public/lm/lmss8.pfb></usr/local/t
  1033	exlive/2026/texmf-dist/fonts/type1/public/lm/lmss9.pfb></usr/local/texlive/2026
  1034	/texmf-dist/fonts/type1/public/lm/lmsy10.pfb></usr/local/texlive/2026/texmf-dis
  1035	t/fonts/type1/public/lm/lmsy6.pfb></usr/local/texlive/2026/texmf-dist/fonts/typ
  1036	e1/public/lm/lmsy7.pfb></usr/local/texlive/2026/texmf-dist/fonts/type1/public/l
  1037	m/lmsy8.pfb></usr/local/texlive/2026/texmf-dist/fonts/type1/public/lm/lmtt10.pf
  1038	b>
  1039	Output written on formalized-state.pdf (45 pages, 613967 bytes).
  1040	PDF statistics:
  1041	 1321 PDF objects out of 1440 (max. 8388607)
  1042	 1180 compressed objects within 12 object streams
  1043	 286 named destinations out of 1000 (max. 500000)
  1044	 77205 words of extra memory for PDF output out of 89155 (max. 10000000)
  1045	

2026-10-22T19:04:46.201302Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'rg -n "(''^!|LaTeX Error|Package .* Error|Undefined control sequence|Warning|Overfull|Underfull|undefined|multiply defined|Citation|Reference|No file|Emergency stop|Fatal error|Missing|not found|Rerun)" papers/latex/formalized-state.log' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
752:Package: rerunfilecheck 2025-06-21 v1.11 Rerun checks for auxiliary files (HO)

2026-10-22T19:04:50.154880Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
codex
The saved build is clean at the diagnostic level: it produced a 45-page PDF with no logged errors, warnings, undefined references/citations, or bad-box reports. I’m now checking the source itself for semantic cross-reference and layout/style problems that would not necessarily appear in the log.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '150,500p' papers/latex/formalized-state.tex | nl -ba -v150" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   150	\label{sec:axioms}
   151	
   152	The series works from six axioms about collective life. In their informal versions they are short: resources are finite and claims on them conflict (Ax1, scarcity); members' preferences diverge and collective choices are made (Ax2, plurality); rules are general, cases particular, and disputes arise (Ax3, generality); cooperation requires shared knowledge of the rules (Ax4, coordination); some members sometimes break rules (Ax5, defection); and the group and its institutions consume resources that someone produces (Ax6, maintenance). The informal versions are too weak to carry a proof, and each pillar Part supplied the auxiliary assumptions its derivation needed. The refined axiom $\mathrm{Ax}k^{*}$ is the bundle that the Part actually used. \Cref{tab:axioms} records the bundles.
   153	
   154	\begin{table}[!htbp]
   155	\centering
   156	\small
   157	\caption{The refined axioms. Each refined axiom is the set of assumptions under which the cited pillar result was proved; the right column names the result.}
   158	\label{tab:axioms}
   159	\begin{tabularx}{\textwidth}{@{}L{1.7cm}YL{2.6cm}@{}}
   160	\toprule
   161	Axiom & Refined content & Pillar result \\
   162	\midrule
   163	Ax1$^{*}$ scarcity & While the collective exists, a conflict over goods occurs in each period with conditional probability at least $p>0$, and an unsettled conflict ends functioning with conditional probability at least $q>0$ & Proposition 3.3 of Part I \\
   164	Ax2$^{*}$ plurality & Collective decisions recur, members' preferences diverge over every decision's alternatives, and decisions and rule changes are produced by the members' own practices & Theorem 3.7 of Part II \\
   165	Ax3$^{*}$ generality & On the persistence event infinitely many residual disputes arise that a move to another group of the collective does not escape (disputes among co-resident kin, or over rights to territory, water or sharing that follow the parties wherever they move); each reaches a disposition at a finite time; for these disputes a disposition by self-help, exit or abandonment ends functioning with conditional probability at least $\kappa>0$; and a losing party complies with a determination if and only if the value it places on the procedure's legitimacy plus the expected sanction is at least its gain from defiance, where the value is positive only if some practice of the legitimation class (Definition 2.1 of Part IV) has led the party to regard the procedure as rightful, and the expected sanction is positive only if some agent's practice answers defiance with a sanction & Theorem 3.3 and Proposition 3.6 of Part III \\
   166	Ax4$^{*}$ coordination & When the collective functions, its rule system, including its settlement procedures, is common knowledge among a cooperating core, members turn over within a bounded horizon $L$, entrants cannot infer the rules from innate endowment, members do not forget what they learn, and entrants are parties to conflicts over goods in infinitely many periods & Theorem 3.5 of Part IV \\
   167	Ax5$^{*}$ defection & Some rule in force has a share $p$ of agents tempted to violate it in the absence of any response that exceeds the violation rate $\theta$ the collective can tolerate, and members best-respond to the sanction regime in force (Lemma 3.3 of Part V) & Theorem 3.4 of Part V \\
   168	Ax6$^{*}$ maintenance & The collective and its institutions consume at least $k>0$ per period from a finite initial stock; inflows are produced by some agent's productive activity; and every practice of every pillar is performed by agents whose consumption is counted here, in a period only if that consumption is met & Lemma 3.3 of Part VI \\
   169	\bottomrule
   170	\end{tabularx}
   171	\end{table}
   172	
   173	The refined axioms are empirical claims about human collectives, not logical truths. Each can be false of some conceivable collective. A population that consumed nothing would violate Ax6$^{*}$; a population of agents who never wished to break a rule would violate Ax5$^{*}$; a collective whose members agreed about every collective choice would violate Ax2$^{*}$; a colony whose rules were fixed by development, as in social insects, would violate the non-innateness clause of Ax4$^{*}$. The hazard clauses of Ax1$^{*}$ and Ax3$^{*}$ are the most demanding, and the pillar Parts identified the cases that test them: collectives in which unsettled conflict is costless (Part I, Section 3) and collectives in which every residual dispute, including disputes among co-resident kin and over rights that follow the parties, can be escaped by free exit (Proposition 3.4 of Part III). Where a premise fails, the derivation of the corresponding function does not apply, and the presence of the function rests on the ethnographic record alone.
   174	
   175	Proposition A as the series states it therefore has two parts. The deductive part is a theorem: a collective that satisfies the refined axioms and persists implements every function. The empirical part is the bridge hypothesis that every functioning human collective satisfies the refined axioms. Part V states the bridge for its own axiom as an explicit assumption (Assumption 3.2 of Part V); the same structure holds for the other five. The honest content of a proof from minimal axioms is a valid derivation together with a list of the premises that could be false.
   176	
   177	\section{Structural necessity}
   178	\label{sec:necessity}
   179	
   180	\subsection{The forcing lemma}
   181	
   182	Two of the six pillar results share a single argument, which can be stated once. A recurring problem is forced if leaving an instance unsolved carries a bounded-below risk of ending the collective.
   183	
   184	\begin{lemma}[Forcing]
   185	\label{lem:formalized-state:forcing}
   186	Let a collective face a sequence of problem instances, indexed in order of disposition, each disposed of as solved or unsolved at a finite time. Suppose there is $\kappa\in(0,1]$ such that, conditional on the history up to the disposition of any instance and on that instance being unsolved, functioning ends at the disposition with probability at least $\kappa$. Let $N$ be the number of unsolved instances, with $N=\infty$ allowed. Then
   187	\begin{enumerate}[label=(\alph*)]
   188	\item $\Pr(\Pi\cap\{N\ge n\})\le(1-\kappa)^n$ for every $n\ge1$, so $N<\infty$ almost surely on $\Pi$;
   189	\item if infinitely many instances arise almost surely on $\Pi$, then almost surely on $\Pi$ infinitely many instances are solved, and the fraction of solved instances among the first $k$ tends to one as $k\to\infty$.
   190	\end{enumerate}
   191	\end{lemma}
   192	
   193	\begin{proof}
   194	(a) For $n\ge1$ let $S_n$ be the event that at least $n$ instances are left unsolved and the collective keeps functioning through the disposition of each of the first $n$. Conditional on $S_{n-1}$ and on the occurrence of an $n$-th unsolved instance, functioning survives that disposition with probability at most $1-\kappa$, so $\Pr(S_n)\le(1-\kappa)\Pr(S_{n-1})$, and induction from $\Pr(S_0)=1$ gives $\Pr(S_n)\le(1-\kappa)^n$. Since $\Pi\cap\{N\ge n\}\subseteq S_n$, the bound follows, and $\Pr(\Pi\cap\{N=\infty\})\le\inf_n(1-\kappa)^n=0$.
   195	
   196	(b) On $\Pi$, by (a), the number of unsolved instances among the first $k$ is eventually constant, while by hypothesis $k$ grows without bound. The number solved among the first $k$ is $k$ minus that constant, so it tends to infinity and its ratio to $k$ tends to one.
   197	\end{proof}
   198	
   199	Part III proved its necessity theorem by this argument, with residual disputes as instances and determination as solution (Theorem 3.3 of Part III). Part I proved a quantitative version with conflicts over goods as instances and settlement as solution (Proposition 3.3 of Part I). The lemma does not say that the solutions are good ones. A collective may settle conflicts by rules that favor a few, and determine disputes by biased procedures, and still satisfy it.
   200	
   201	\subsection{Three patterns of argument}
   202	
   203	The six pillar results rest on three kinds of argument, and the difference matters for what would refute them. Hazard forcing, \cref{lem:formalized-state:forcing}, gives the financial and judicial pillars; its empirical content is the hazard, and where unsolved instances are harmless, as with costless exit from a band, it gives nothing. Stock accounting gives the productive pillar: persistence requires a nonnegative stock $X_T=X_0+\sum_{t<T}(Y_t-K^{\mathrm{tot}}_t)$, so with consumption at least $k>0$ and a finite initial stock the inflows must average at least $k$, and the no-manna assumption makes every inflow someone's productive activity, possibly an outsider's (Lemmas 3.3 and 3.4 of Part VI). Constitutive arguments give the rest. A decision that binds everyone over alternatives on which members disagree is a selection among divergent preferences (Lemma 3.4 of Part II). Members who enter without knowing the rules acquire common knowledge of them only through practices that refine their information (Theorem 3.5 of Part IV, following \citealt{lewis1969} and \citealt{aumann1976}). And if more agents are tempted than the collective can tolerate, best responses keep violations within tolerance only if a positive deterrence margin shifts at least $p-\theta$ of probability mass to compliance (Theorem 3.4 of Part V, in the tradition of \citealt{becker1968}).
   204	
   205	\begin{lemma}[Pillar necessity]
   206	\label{lem:formalized-state:pillars}
   207	Let $G$ be a collective with $\Pr(\Pi)>0$. For each $k=1,\dots,6$, if $G$ satisfies Ax$k^{*}$ then $\Impl_{m_k}(G)$ holds, where $(m_1,\dots,m_6)=(\pF,\pP,\pJ,\pI,\pC,\pW)$.
   208	\end{lemma}
   209	
   210	\begin{proof}
   211	$\pF$: under Ax1$^{*}$, \cref{lem:formalized-state:forcing}(a) with $\kappa=q$ gives finitely many unsettled conflicts almost surely on $\Pi$. Part I's Proposition 3.3(b) gives $\Pr(\Pi\cap\{Y_T<pT/2\})\le e^{-pT/8}$ for the number $Y_T$ of periods with a conflict up to $T$. The bounds are summable in $T$, so by the Borel-Cantelli lemma, almost surely on $\Pi$ we have $Y_T\ge pT/2$ for all large $T$; conflicts therefore arise infinitely often on $\Pi$, and \cref{lem:formalized-state:forcing}(b) gives infinitely many settled conflicts. $\pP$: on $\Pi$ collective decisions are made, and Ax2$^{*}$ contains the hypotheses of Lemma 3.4 and Theorem 3.7 of Part II, which give sense (a) of Definition 2.2 of Part II at every decision. $\pJ$: \cref{lem:formalized-state:forcing}(b), applied to the subsequence of residual disputes that a move does not escape, which Ax3$^{*}$ makes infinite and subject to the hazard $\kappa$, with determination as solution, gives infinitely many determinations almost surely on $\Pi$, which is $\Impl_{\pJ}$; Theorem 3.3 of Part III is the case in which every residual dispute is inescapable. $\pI$: on $\Pi$ the collective functions at every date, so every window of length $L$ lies in an interval of functioning longer than $L$, and Theorem 3.5 of Part IV applies to each window. $\pC$: Ax5$^{*}$ is Assumption 3.1 of Part V for a rule in force under a best-response profile, and Theorem 3.4 of Part V gives the stated bound. $\pW$: on $\Pi$ the stock stays nonnegative at every date, which is persistence in the sense of Part VI, and Lemma 3.3 of Part VI applies.
   212	\end{proof}
   213	
   214	The lemma adds nothing to the six Parts except a common persistence event. That is its purpose. The Parts used different notions of persistence, from survival up to a horizon to functioning over a window, and a theorem about one collective needs one notion.
   215	
   216	\subsection{The structural necessity theorem}
   217	
   218	\begin{theorem}[Structural necessity]
   219	\label{thm:formalized-state:A}
   220	Let $G$ be a persistent collective that satisfies Ax1$^{*}$ to Ax6$^{*}$. Then, almost surely on the persistence event, all six functions are implemented: $\Impl_m(G)$ holds for every $m\in\Mset$. If every functioning human collective satisfies the refined axioms, this holds for every $G\in\mathcal{G}$. \Cref{cor:formalized-state:struct} adds the dependency relations $\Dzero$, which gives $\Struct(G)$, the first half of Proposition A.
   221	\end{theorem}
   222	
   223	Universality over real governance systems is the theorem together with the empirical bridge that every functioning collective satisfies Ax1$^{*}$ to Ax6$^{*}$, which historical observation supports.
   224	
   225	\begin{proof}
   226	By \cref{lem:formalized-state:pillars}, each $\Impl_m(G)$ holds, either deterministically on $\Pi$ or on an event of full conditional probability given $\Pi$. A finite intersection of events of full conditional probability has full conditional probability, so all six hold together almost surely on $\Pi$. The second sentence restates the first under the bridge hypothesis.
   227	\end{proof}
   228	
   229	The theorem does not use the integration statistic, the concentration indices, or any premise about who holds control. It also does not use strong connectivity of the dependency structure, which \cref{sec:dependency} derives from four further axioms. The second half of Proposition A, universal interdependence, is \cref{thm:formalized-state:interdependence}, and the two theorems together with the bridge hypothesis are Proposition A in the sense of the series.
   230	
   231	\subsection{Consistency and independence of the axioms}
   232	
   233	A theorem from axioms says little if the axioms have no model, and a necessity claim is empty if the conclusion holds whether or not the axioms do. The next proposition settles both points.
   234	
   235	\begin{proposition}[Consistency and independence]
   236	\label{prop:formalized-state:independence}
   237	\leavevmode
   238	\begin{enumerate}[label=(\alph*)]
   239	\item There is a collective that functions at every date with probability one, satisfies Ax1$^{*}$ to Ax6$^{*}$, and implements all six functions.
   240	\item For each $k$ there is a collective that functions at every date with probability one, satisfies Ax$j^{*}$ for every $j\neq k$, violates Ax$k^{*}$, and does not implement $m_k$.
   241	\end{enumerate}
   242	\end{proposition}
   243	
   244	\begin{proof}
   245	(a) Take three members at every date; the collective has no subgroups, so no residual dispute can be escaped by a move and every residual dispute is inescapable in the sense of Ax3$^{*}$. One member is replaced by an entrant every $L$ periods; the member replaced is always the longest-serving one, an entrant does not know the rule system at entry and no member forgets what it learns, and the plot is claimed in each period by the most recent entrant and one other member, so entrants are parties to conflicts over goods in every period. In each period: one plot of land is claimed by two members and is assigned by a known rotation rule, with hazard $q=1/2$ attached to an unsettled conflict; the members choose between two campsites, with members 1 and 2 preferring different sites, by majority vote; one residual dispute about the application of a rule arises between two members and is determined by a lot drawn by the third, whose result both accept because each places on the procedure a value $\ell$ at least as large as its gain from defiance, a value acquired at the initiation described next, where the lot is presented as the rightful procedure, with hazard $\kappa=1/2$ attached to any other disposition; an entrant takes part in a public initiation at which the rule system is recited to all members, which makes it common knowledge among those initiated; each member observes a temptation to breach a rule of camp chores, drawn from a distribution $G$ with $p=1-G(0)=1/2$, and a breach is met with a fine $d$ paid to the other members, with $d$ chosen so that $G(d)\ge3/4$, members best-respond to the fine, and the collective tolerates a violation rate $\theta=1/4$; and the members forage an output equal to their consumption $k$; each member forages alone, at any campsite. Every conflict is settled and every residual dispute determined, so no hazard is ever triggered and the collective functions at every date with probability one. Each refined axiom holds by construction, and each implementation predicate holds: settlement in every period, majority choice over divergent preferences, determination in every period, initiation in every window, a positive margin $d$ for every agent at every date, and foraging in every period.
   246	
   247	(b) Modify the model of (a) in one component. For $k=1$, set $q=0$ and assign the plot by contest each period, so conflicts are never settled and never harmful. For $k=2$, give all members the same preference over campsites, so no decision selects among divergent preferences. For $k=3$, abandon every residual dispute and set the hazard of abandonment to zero, which is the costless-exit case of Proposition 3.4 of Part III. For $k=4$, let entrants know the rule system at entry, drop the initiation, and attach the fine $d\ge g$ to defiance of a determination, so no practice of the legitimation class operates and determinations rest on sanction alone. For $k=5$, let temptations be nonpositive, so $p=0\le\theta$, and remove the fine, so every margin is zero and no violation occurs. For $k=6$, let an inflow of $k$ arrive in every period with no productive act by anyone. In each case the modified component triggers no hazard, the other components are unchanged, and the stated axiom and predicate fail.
   248	\end{proof}
   249	
   250	Part (b) is the formal answer to the charge that Proposition A is true by definition. In each modified collective the function is absent and the collective persists, so the class of persistent collectives does not contain the six functions by construction. What excludes such collectives from the real world is the failure of their premises: harmless unsettled conflict, unanimous preferences, free exit, innate rules, untempted members and unproduced inflows. Those are empirical claims, and the pillar Parts tested each against the ethnographic and historical record.
   251	
   252	\subsection{Minimal forms}
   253	
   254	The hard cases for Proposition A are societies described as having no state, no chiefs with power to command, or radical equality. The series predicts that each implements every function in an informal and dispersed form. The prediction has a formal core.
   255	
   256	\begin{lemma}[Minimal form]
   257	\label{lem:formalized-state:minimal}
   258	Let a collective of $n\ge2$ adults implement every function through practices without designated offices in which each adult holds an equal share of decision-relevant control, and let $Q_m\ge\bar q$ for every $m$. Then $H_m=1/n$ for every $m$ and $U_t\le(1-\bar q)/n$. If the coalition of all adults is admissible in the coalition list that defines $C_{mn}$ (\cref{def:formalized-state:overlap}), then $C_{mn}=1$ for every pair and $\Integ_t=1$. In either case the capture predicate of \cref{def:formalized-state:cap} fails for every threshold $u^{*}>(1-\bar q)/n$.
   259	\end{lemma}
   260	
   261	\begin{proof}
   262	Equal shares give $H_m=n\cdot(1/n)^2=1/n$. Then $U_t=\sum_m\omega_m(1/n)(1-Q_m)\le(1-\bar q)/n$. If the grand coalition $S=N$ is admissible, its control share in every pillar is one, so $\min\{\kappa_m(N),\kappa_n(N)\}=1$ for every pair. The capture predicate requires $U_t\ge u^{*}$, which fails when $u^{*}>(1-\bar q)/n$.
   263	\end{proof}
   264	
   265	The lemma resolves an apparent paradox in the ethnography. In egalitarian bands the same body judges, sanctions, decides and legitimates, so integration is at its maximum (Part III observed that $C_{\pJ\pC}$ is high there), yet the functions are held equally and open to challenge by anyone, so unaccountable concentration is near its minimum. This is the clearest reason why the source requires both indices to be high: integration of functions in the group as a whole is the opposite of capture.
   266	
   267	\Cref{tab:hardcases} collects the minimal forms that the pillar Parts documented for the Nuer \citep{evanspritchard1940}, the Ju/'hoansi \citep{marshall1976,lee1979,lee2013,wiessner2005}, mobile foragers with a reverse dominance hierarchy \citep{boehm1999}, Amazonian groups whose headmen speak but cannot command \citep{clastres1987}, and Ostrom's long-enduring commons \citep{ostrom1990,cox2010}. Woodburn's institutions of leveling show the same pattern from the side of sanctions: egalitarianism is produced and defended, not given \citep{woodburn1982}.
   268	
   269	\begin{table}[!htbp]
   270	\centering
   271	\small
   272	\caption{Minimal forms of the six functions in stateless and consensus societies, as documented in Parts I to VI. Each cell names the practice; no cell names an office with power to command.}
   273	\label{tab:hardcases}
   274	\footnotesize
   275	\setlength{\tabcolsep}{3pt}
   276	\begin{tabularx}{\textwidth}{@{}L{1.6cm}YYYYYY@{}}
   277	\toprule
   278	Case & $\pF$ & $\pP$ & $\pJ$ & $\pI$ & $\pC$ & $\pW$ \\
   279	\midrule
   280	Nuer & Cattle rights and bridewealth & Negotiation among lineages & Mediation by the leopard-skin chief & Lineage idiom and ritual & Threat of feud by kin & Herding and cultivation \\
   281	Ju/'hoansi & Meat shared by the arrow-owner rule & Camp talk and moving camp & Talking disputes out & Talk heard by all and the healing dance & Criticism, ridicule and avoidance & Foraging by both sexes \\
   282	Mobile foragers & Sharing enforced against hoarders & Group decision against would-be leaders & Group judgment of deviants & Shared moral talk & Ostracism, exile and execution & Foraging \\
   283	Amazonian groups & The headman's duty of generosity & Consensus with oratory as duty & Peacemaking by the headman & Myth and the headman's recitation & Abandonment of a commanding headman & Gardening and hunting \\
   284	Commons users & Appropriation and boundary rules & Users modify the rules & Low-cost local arenas & Rules known to users & Monitoring and graduated sanctions & Provision of maintenance labor \\
   285	\bottomrule
   286	\end{tabularx}
   287	\end{table}
   288	
   289	The table supports both halves of the series' thesis: every function operates where no office does, which is what Proposition A requires, and concentration varies with circumstance and choice, which is what makes Proposition B contingent. Some early societies moved seasonally between egalitarian and hierarchical arrangements, including temporary policing during collective hunts \citep{graeber2021}; upland groups in Southeast Asia kept their functions dispersed to avoid incorporation into lowland states \citep{scott2009}; and early grain states concentrated the resource and productive functions where taxable surpluses allowed \citep{scott2017}. Two cautions qualify the record without removing any function from it. The ethnographies describe groups in marginal environments and in contact with states and markets, and foraging societies vary widely \citep{kelly1995}. Equal formal shares understate actual concentration, because age, gender, skill and kinship give some speakers more weight (Part II, Section 3).
   290	
   291	The Ju/'hoansi are the hardest case for the judicial derivation, because moving to another camp resolves many disputes with no third party (Part III, Section 3). Under the unit of \cref{def:formalized-state:collective} the collective is the network of camps linked by kinship and exchange, within which a move is not exit. We code the Ju/'hoansi as satisfying the inescapable-dispute clause of Ax3$^{*}$: rights to territory and water are held through kin and follow a person from camp to camp, and disputes over sharing and marriage among kin recur and are talked out in public \citep{lee2013,wiessner2005}; Lee's records of homicide show that self-help between kin carried a real risk of feud \citep{lee1979}, which we read as a hazard to the functioning of the camp network in the sense of Ax3$^{*}$. The coding is an ethnographic reading of these sources, not a measurement of the hazard. With it and the codings of the other five axioms in Parts I to VI, the Ju/'hoansi are an instance of \cref{thm:formalized-state:A}, with a thin but present judicial function.
   292	
   293	\subsection{Falsifiers and counterexample attempts}
   294	
   295	Each pillar Part identified its strongest counterexample attempt and the observation that would refute its result. \Cref{tab:falsifiers} collects them. Every reply in the table narrows the claim in a stated direction or relocates the function; none rescues the claim by redefining the function after the fact.
   296	
   297	\begin{table}[!htbp]
   298	\centering
   299	\small
   300	\caption{The strongest counterexample attempt for each pillar, the reply given in the pillar Part, and the observation that would refute the pillar's necessity result.}
   301	\label{tab:falsifiers}
   302	\begin{tabularx}{\textwidth}{@{}L{0.7cm}YYY@{}}
   303	\toprule
   304	 & Counterexample attempt & Reply & Falsifier \\
   305	\midrule
   306	$\pF$ & Foragers' wants are easily met, so there is no scarcity \citep{sahlins1972b} & Scarcity concerns conflicting claims, and affluence lowers $p$ without making it zero & A persistent collective whose members hold conflicting claims and resolve them mostly without any settlement procedure \\
   307	$\pP$ & Custom evolves without legislators \citep{hayek1973,ellickson1991} & Distributed practices still select and change rules, with no office & A long-lived plural group whose rules never changed through environments that no single rule system could survive \\
   308	$\pJ$ & Free exit, or rules executed by code & Free exit thins the function (Proposition 3.4 of Part III), and code relocates interpretation to the encoding of cases (Proposition 3.5 of Part III) & A persistent collective in which disputes that a move does not escape recur and are always settled by force or left open \\
   309	$\pI$ & Force alone coordinates & Sanctions deter only those who know them, and elites must coordinate on expectations & A collective with turnover and locally variable rules whose entrants coordinate without any practice that informs them \\
   310	$\pC$ & Reciprocity and reputation enforce without coercion \citep{axelrod1984,greif1993} & Withdrawal of cooperation is a sanction & A rule whose measured temptation share exceeds its observed violation rate while violators fare no worse than matched compliers \\
   311	$\pW$ & Endowments, raiding, rents or automation & Production is relocated to donors, victims, extractors or the owners of machines (Lemma 3.4 of Part VI) & A system that persists indefinitely with no production anywhere and no replenishment of its stock \\
   312	\bottomrule
   313	\end{tabularx}
   314	\end{table}
   315	
   316	The coercion row needs one further safeguard. The replies to internalization and exit could be used to reclassify any compliant collective without sanctions as one in which few members are tempted, which would make the necessity claim immune to evidence. Part V therefore requires that the temptation share be measured independently of the sanction practices it is used to explain, for example by offering members an unobserved opportunity to break a rule, and it states the falsifier without the tolerance $\theta$, which would otherwise be an adjustable parameter. The same requirement applies to every hazard in \cref{tab:axioms} and to the legitimacy value and expected sanction in the compliance clause of Ax3$^{*}$: a premise measured only through the outcome it is meant to explain cannot test anything.
   317	
   318	\subsection{Hart's secondary rules}
   319	
   320	Hart argued that a regime of primary obligations alone suffers from uncertainty about which rules exist, a static character, and inefficiency in settling disputes, and that the remedies are a rule of recognition, rules of change and rules of adjudication \citep{hart1961}. The series assigns these to legitimation, rule making and interpretation (Definition 3.6 of Part II, Definition 2.2 of Part IV, Section 2 of Part III), and draws the boundary between $\pP$ and $\pJ$ by acts: making or changing a general rule belongs to $\pP$, applying a given rule to a case belongs to $\pJ$ (Definition 2.3 of Part II). A court that changes a rule by precedent performs both acts, and the role map records it in both layers. Under precedent, interpretation becomes an input to rule change and rule change produces the rules that interpretation applies, while recognition certifies both, since a new statute or precedent coordinates behavior only once it is common knowledge (Theorem 3.5 of Part IV). In \cref{sec:dependency}, Hart's triad appears as the arcs $\pI\to\pP$, $\pP\to\pJ$, $\pJ\to\pP$ and $\pP\to\pI$, which make the three secondary functions mutually reachable whenever rules change through both legislation and precedent.
   321	
   322	\subsection{Functional explanation}
   323	
   324	\Cref{thm:formalized-state:A} is a condition of persistence. It does not explain why any particular institution exists, and it asserts no feedback from the effects of an institution to its existence, which Elster required of functional explanation \citep{elster1979,elster1983}. It says nothing about why the Nuer had a leopard-skin chief or why Bourbon France sold judicial offices. Older lists of functional prerequisites drifted toward tautology because they defined prerequisites by what persisting societies happened to have (\cref{sec:literature}); the present derivation avoids the drift because each premise can be false and \cref{prop:formalized-state:independence} exhibits persistent collectives in which it is.
   325	
   326	\section{The dependency structure}
   327	\label{sec:dependency}
   328	
   329	\subsection{Dependency as a directed hypergraph}
   330	
   331	Proposition A speaks of the six functions ``together with the dependency relations among them''. The pillar Parts found two dependencies that a directed graph cannot express. An effective judicial determination needs either legitimacy or an expected sanction, and neither by itself (Proposition 3.6 of Part III). Large-scale sanctioning needs either material provisioning or legitimation, but only when sanctions are costly public goods (Proposition 3.6 and Corollary 3.7 of Part V). A dependency on one of several functions is a hyperarc. Directed hypergraphs of this kind, with reachability through hyperarcs whose whole tail has been reached, are standard in the study of AND/OR structures \citep{gallo1993}.
   332	
   333	\begin{definition}[Dependency hypergraph]
   334	\label{def:formalized-state:hypergraph}
   335	A \emph{hyperarc} is a pair $(T,m)$ with $m\in\Mset$ and $\emptyset\neq T\subseteq\Mset\setminus\{m\}$. The hyperarc $(T,m)$ belongs to the dependency structure $\mathcal{D}(G)$ of a collective if, almost surely on $\Pi$, infinitely many of the instances that the practices of $m$ solve are solved only with an output of at least one function in $T$: if every function in $T$ withheld its output, each of those instances would be left unsolved. The instances of each function are those of its implementation predicate: conflicts over goods for $\pF$, collective decisions for $\pP$, residual disputes for $\pJ$, entrants in a window for $\pI$, agent-periods under the rule for $\pC$, and periods of production for $\pW$. When $T=\{n\}$ the hyperarc is an \emph{arc}, written $n\to m$, with the provider on the left. A hyperarc with $|T|\ge2$ is a disjunction: $m$ needs some member of $T$, not all of them.
   336	\end{definition}
   337	
   338	\begin{definition}[Connectivity and cascade]
   339	\label{def:formalized-state:cascade}
   340	The \emph{underlying digraph} of $\mathcal{D}$ has an arc $t\to m$ for every $(T,m)\in\mathcal{D}$ and every $t\in T$. For $S\subseteq\Mset$ the \emph{cascade} $\cl_{\mathcal{D}}(S)$ is the smallest set that contains $S$ and contains $m$ whenever $(T,m)\in\mathcal{D}$ and $T\subseteq\cl_{\mathcal{D}}(S)$. $\mathcal{D}$ is \emph{strongly connected} if its underlying digraph is, and \emph{cascade-complete} if $\cl_{\mathcal{D}}(\{n\})=\Mset$ for every $n$. The \emph{interdependence predicate} $\Inter(G)$ holds if $\mathcal{D}(G)$ is strongly connected and cascade-complete.
   341	\end{definition}
   342	
   343	The cascade $\cl_{\mathcal{D}}(S)$ is the set of functions that fail when the functions in $S$ withhold their outputs, propagated through the instances of \cref{def:formalized-state:hypergraph}. Strong connectivity says that every function is linked to every other by a chain of dependencies. Cascade completeness says more: the failure of any single function brings down all the others. The two notions coincide for digraphs and come apart for hypergraphs, because a disjunctive hyperarc transmits failure only when its whole tail has failed.
   344	
   345	\begin{remark}[Dependency through persistence]
   346	\label{rem:formalized-state:persistence}
   347	If $n\to m$ were defined to mean that the collective stops persisting when $n$ is withheld, \cref{thm:formalized-state:A} would make every function depend on every other at no cost: withholding any function ends persistence, and every implementation predicate is defined on the persistence event. \Cref{def:formalized-state:hypergraph} excludes this by requiring that the instances of $m$ use an output of $T$ directly. Interdependence in the present sense is a claim about how the functions operate, and it does not follow from Proposition A.
   348	\end{remark}
   349	
   350	\subsection{Dependencies derived from the axioms}
   351	
   352	\begin{lemma}[Derived dependencies]
   353	\label{lem:formalized-state:D0}
   354	Under the hypotheses of \cref{thm:formalized-state:A}, $\mathcal{D}(G)$ contains
   355	\[
   356	\Dzero=\bigl\{\pW\to\pF,\ \pW\to\pP,\ \pW\to\pJ,\ \pW\to\pI,\ \pW\to\pC,\ (\{\pI,\pC\},\pJ),\ \pI\to\pF\bigr\}.
   357	\]
   358	It need not contain the arc $\pI\to\pJ$ or the arc $\pC\to\pJ$.
   359	\end{lemma}
   360	
   361	\begin{proof}
   362	\emph{Production.} By the last clause of Ax6$^{*}$, every practice is performed only when its performers' consumption is met. The initial stock is finite and consumption is at least $k>0$ per period, so without produced inflows the stock is exhausted after at most $X_0/k$ periods (Lemma 3.3 of Part VI). Every instance of every other function that falls after that date is solved only if productive activity, by members or by outsiders (Lemma 3.4 of Part VI), supplies the practitioners' consumption. On $\Pi$ each function solves infinitely many instances, so $\pW\to m$ for every $m\neq\pW$.
   363	
   364	\emph{Interpretation.} By the compliance clause of Ax3$^{*}$, which is the model of Proposition 3.6 of Part III, a losing party that gains $g>0$ by defiance complies if and only if $\ell+\sigma\ge g$, where $\ell$ is the value it places on the procedure's legitimacy and $\sigma$ the expected sanction. A party to a residual dispute strictly prefers its own verdict (Definition 2.2 of Part III), so $g>0$. If legitimation and sanction both withhold their outputs, then $\ell=\sigma=0$ by Ax3$^{*}$ and no determination is effective, so $\Impl_{\pJ}$ requires an output of legitimation or of sanction for each effective determination, and $(\{\pI,\pC\},\pJ)\in\mathcal{D}(G)$. In the collective of \cref{prop:formalized-state:independence}(a) with the fine $d\ge g$ also attached to defiance of a determination, each determination is effective with either output alone, so neither $\pI\to\pJ$ nor $\pC\to\pJ$ belongs to $\mathcal{D}(G)$.
   365	
   366	\emph{Allocation and recognition.} A conflict is settled only if members can anticipate the assignment from a description of the procedure (Definition 2.2(b) of Part I), which requires that they know the procedure. Settlement procedures belong to the rule system whose common knowledge Ax4$^{*}$ requires, and under Ax4$^{*}$ every window of length $L$ contains a member of the cooperating core who entered without knowing the rule system (Lemma 3.4 of Part IV) and came to know it only through practices of the legitimation function (Theorem 3.5 of Part IV). The conflicts that such members are party to after entry, which recur on $\Pi$ by the last clause of Ax4$^{*}$, are settled only with that output, so $\pI\to\pF$.
   367	\end{proof}
   368	
   369	\begin{corollary}[Structural necessity with dependencies]
   370	\label{cor:formalized-state:struct}
   371	Under the hypotheses of \cref{thm:formalized-state:A}, $\Struct(G)$ holds. If every functioning human collective satisfies the refined axioms, $\Struct(G)$ holds for every $G\in\mathcal{G}$.
   372	\end{corollary}
   373	
   374	\begin{proof}
   375	\Cref{thm:formalized-state:A} gives $\Impl_m(G)$ for every $m$ almost surely on $\Pi$, and \cref{lem:formalized-state:D0}, whose hypotheses are those of the theorem, gives $\Dzero\subseteq\mathcal{D}(G)$. The second sentence is the first under the bridge hypothesis.
   376	\end{proof}
   377	
   378	The structure $\Dzero$ is not strongly connected. No arc enters $\pW$, and $\pP$ and $\pJ$ have no outgoing arc, and $\pC$ has one only through the disjunctive hyperarc. Apart from the compliance clause of Ax3$^{*}$ and the settlement-procedure and entrant clauses of Ax4$^{*}$, the six axioms constrain each function separately. The next subsection adds the incidences on production, rule making, interpretation and coercion.
   379	
   380	\subsection{Incidence axioms}
   381	
   382	The six problems converge on one object in every collective that the pillar Parts examined: the rules that assign goods. A settlement procedure is a rule that must be changed when circumstances change, interpreted when its application is disputed, known to those it binds, enforced against those tempted to breach it, and applied to the inputs of production. Each of these is an incidence of one axiom on the financial pillar. They are stated as axioms because they are claims about collective life that the six axioms do not imply (\cref{prop:formalized-state:minimality}(a)), and each comes with a falsifier.
   383	
   384	\begin{assumption}[X1, contested inputs]
   385	\label{ass:formalized-state:X1}
   386	In infinitely many periods on $\Pi$, productive activity uses inputs, such as land, water, tools or equipment, that are goods under conflicting claims in the sense of Definition 2.1 of Part I, and an input is used productively only under an assignment that its user can anticipate.
   387	\end{assumption}
   388	
   389	\begin{assumption}[X2, changing environment]
   390	\label{ass:formalized-state:X2}
   391	On $\Pi$ the environment changes infinitely often in the sense of Assumption 3.2 of Part II, and each change creates conflicts over goods that no settlement procedure in force before the change can settle.
   392	\end{assumption}
   393	
   394	\begin{assumption}[X3, open-textured allocation]
   395	\label{ass:formalized-state:X3}
   396	Some settlement procedure in force has open texture in the sense of Definition 2.1 of Part III, and on $\Pi$ infinitely many residual disputes about its application arise that a move does not escape, subject to the hazard of Ax3$^{*}$.
   397	\end{assumption}
   398	
   399	\begin{assumption}[X5, tempting allocation]
   400	\label{ass:formalized-state:X5}
   401	Ax5$^{*}$ holds for some settlement procedure in force: the share of members who would gain from breaching its assignment in the absence of any response by others, net of every internal cost, exceeds the violation rate the collective can tolerate.
   402	\end{assumption}
   403	
   404	The incidence clauses of Ax4$^{*}$ fail for a collective whose entrants are never parties to conflicts over goods, or whose settlement procedures are run by specialists whose rules the parties need not know, although where such specialists belong to the cooperating core and parties anticipate assignments through them, as in complex polities with tax codes or credit rules, the clause holds; the compliance clause of Ax3$^{*}$ fails for a losing party that complies with no legitimating belief and no expected sanction. The falsifiers of the four incidence axioms are direct. X1 fails for a collective that sustains production on inputs nobody else claims, or on inputs whose use is decided each period by unregulated contest. X2 fails for a long-lived collective that meets new kinds of conflicting claims without ever changing its allocation rules. X3 fails for a collective whose allocation rules never produce a dispute that the parties cannot settle by bargaining. X5 fails for a collective in which the temptation to breach every allocation rule, measured independently of sanction practices, stays below a tolerance preregistered for that rule. The pillar Parts report evidence against each such collective. Foragers who own no land in the agrarian sense still hold kin-based rights to territory and water (Part I, Section 3). Ellickson's ranchers changed their norms when trespass and fencing conditions changed \citep{ellickson1991}. The Nuer settled homicide by cattle compensation through a mediator because the parties could not settle it alone \citep{evanspritchard1940}. And Wiessner's records of Ju/'hoansi camp talk show continual criticism of failures to share \citep{wiessner2005}, which is what X5 predicts and what a population of untempted members would not need.
   405	
   406	\begin{figure}[t]
   407	\centering
   408	\begin{tikzpicture}[>=stealth, every node/.style={font=\small},
   409	    fn/.style={circle,draw,minimum size=0.85cm,fill=white},
   410	    lab/.style={fill=white,inner sep=1.5pt,font=\footnotesize}]
   411	  \node[fn] (F) at (0,0) {$\pF$};
   412	  \node[fn] (W) at (0,-2.6) {$\pW$};
   413	  \node[fn] (P) at (-3.6,0.6) {$\pP$};
   414	  \node[fn] (J) at (3.6,0.6) {$\pJ$};
   415	  \node[fn] (I) at (-2.0,2.7) {$\pI$};
   416	  \node[fn] (C) at (2.0,2.7) {$\pC$};
   417	  \draw[->,gray] (W) to[bend left=28] (P);
   418	  \draw[->,gray] (W) to[bend right=28] (J);
   419	  \draw[->,gray] (W) to[bend left=45] (I);
   420	  \draw[->,gray] (W) to[bend right=45] (C);
   421	  \draw[->,gray] (W) to[bend right=25] (F);
   422	  \draw[->,thick] (F) to[bend right=25] node[lab] {X1} (W);
   423	  \draw[->,thick] (P) -- node[lab] {X2} (F);
   424	  \draw[->,thick] (J) -- node[lab] {X3} (F);
   425	  \draw[->,thick] (C) -- node[lab] {X5} (F);
   426	  \draw[->,thick] (I) -- node[lab] {Ax4} (F);
   427	  \coordinate (h) at (3.3,2.5);
   428	  \fill (h) circle (1.8pt);
   429	  \draw[thick,dashed] (I) .. controls (-0.8,3.9) and (2.6,3.7) .. (h);
   430	  \draw[thick,dashed] (C) -- (h);
   431	  \draw[->,thick,dashed] (h) -- (J);
   432	\end{tikzpicture}
   433	\caption{The dependency structure $\Dstar$ of \cref{thm:formalized-state:interdependence}. Gray arcs run from production to every other function. Solid labeled arcs enter allocation and production and carry the premise that yields them. The dashed hyperarc joins legitimation and coercion at a point before reaching interpretation, because interpretation needs one of the two and not both.}
   434	\label{fig:hypergraph}
   435	\end{figure}
   436	
   437	\subsection{Interdependence}
   438	
   439	\begin{theorem}[Interdependence]
   440	\label{thm:formalized-state:interdependence}
   441	Let $G$ satisfy the hypotheses of \cref{lem:formalized-state:D0} and Assumptions X1, X2, X3 and X5. Then $\mathcal{D}(G)$ contains
   442	\[
   443	\Dstar=\Dzero\cup\{\pF\to\pW,\ \pP\to\pF,\ \pJ\to\pF,\ \pC\to\pF\},
   444	\]
   445	$\Dstar$ is strongly connected and cascade-complete, and $\Inter(G)$ holds. If every functioning human collective satisfies the refined axioms and the four incidence axioms, then $\Struct(G)$ and $\Inter(G)$ hold for every $G\in\mathcal{G}$: every function reaches every other, and the failure of any one propagates to all six.
   446	\end{theorem}
   447	
   448	\begin{proof}
   449	\emph{The arcs.} $\Dzero\subseteq\mathcal{D}(G)$ by \cref{lem:formalized-state:D0}. For $\pF\to\pW$: under X1, the production that uses contested inputs takes place only under an anticipable assignment of those inputs, and on $\Pi$ such assignments are, in all but finitely many periods, the outputs of settlement (\cref{lem:formalized-state:pillars}); withholding settlement leaves that production undone. For $\pP\to\pF$: under X2, each change of environment creates conflicts that no procedure in force can settle, so they are settled only after the rule system has been replaced; by \cref{lem:formalized-state:pillars} all but finitely many of these conflicts are settled, so the rule system is replaced after all but finitely many changes, and the self-government clause of Ax2$^{*}$ makes each replacement a practice of the members, so the procedures that settle the new conflicts are outputs of rule making. For $\pJ\to\pF$: under X3, \cref{lem:formalized-state:forcing}(a), applied to the inescapable disputes about the open-textured procedure, gives, almost surely on $\Pi$, all but finitely many of them disposed of by determination; an assignment in the open set of the procedure becomes anticipable only once determined, so the conflicts at issue are settled only with the output of interpretation. For $\pC\to\pF$: under X5, Lemma 3.3 of Part V with a zero deterrence margin gives a violation probability of at least $p>\theta$ in every agent-period, so withholding sanctions leaves infinitely many assignments breached without anyone being held to them, and those conflicts are unsettled by Definition 2.2(c) of Part I.
   450	
   451	\emph{Strong connectivity.} Each of $\pP$, $\pJ$, $\pI$ and $\pC$ has an arc to $\pF$, $\pF$ has an arc to $\pW$, and $\pW$ has an arc to every other function. Every function therefore reaches $\pW$ within two steps and is reached from $\pW$ in one.
   452	
   453	\emph{Cascade completeness.} For $n\in\{\pP,\pJ,\pI,\pC\}$ the arc $n\to\pF$ puts $\pF$ in $\cl(\{n\})$; the arc $\pF\to\pW$ then puts $\pW$ in it, and the arcs from $\pW$ put every function in it. The same chain starts at $\pF$, and $\cl(\{\pW\})=\Mset$ directly.
   454	
   455	\emph{Monotonicity.} Adding hyperarcs adds arcs to the underlying digraph and can only enlarge each cascade, so both properties pass from $\Dstar$ to $\mathcal{D}(G)$. The last sentence restates the theorem under the bridge hypothesis.
   456	\end{proof}
   457	
   458	\Cref{fig:hypergraph} draws $\Dstar$. Allocation rules are the hub of the dependency structure because the six problems converge on them, not because resource controllers dominate. The hub of dependency and the hub of integration are different objects. A polity in which the allocation rules are made by a dispersed legislature, interpreted by independent courts, taught by a free press and enforced by accountable police has the same $\Dstar$ as one in which a single coalition does all four, and \cref{sec:capture} shows that the two differ in $U_t$ and $\Integ_t$.
   459	
   460	\begin{proposition}[Role of each premise]
   461	\label{prop:formalized-state:minimality}
   462	\leavevmode
   463	\begin{enumerate}[label=(\alph*)]
   464	\item The refined axioms do not imply interdependence: the collective of \cref{prop:formalized-state:independence}(a) satisfies Ax1$^{*}$ to Ax6$^{*}$ and $\Struct$, and no arc of its dependency structure enters $\pW$.
   465	\item Among the arcs of $\Dstar$ and the further arcs of \cref{rem:formalized-state:further}, the only arc into $\pW$ is $\pF\to\pW$; without X1 no structure built from them is strongly connected.
   466	\item Without X5, the structure $\Dstar\setminus\{\pC\to\pF\}$ is strongly connected but not cascade-complete: $\cl(\{\pC\})=\{\pC\}$.
   467	\item Without X3, replacing $\pJ\to\pF$ by the precedent arc $\pJ\to\pP$ of \cref{rem:formalized-state:further} keeps the structure strongly connected and cascade-complete.
   468	\item If the hyperarc $(\{\pI,\pC\},\pJ)$ is replaced by the two arcs $\pI\to\pJ$ and $\pC\to\pJ$, then the cascade of $\{\pC\}$ in $\Dstar\setminus\{\pC\to\pF\}$ becomes $\Mset$.
   469	\end{enumerate}
   470	\end{proposition}
   471	
   472	\begin{proof}
   473	(a) Foraging is individual, does not depend on the campsite chosen, uses no contested input and is not governed by the rule of camp chores, so no instance of $\pW$ uses an output of another function. (b) No other listed arc has head $\pW$, and a digraph with no arc into a vertex is not strongly connected. (c) The arcs of $\Dstar$ other than $\pC\to\pF$ still give every function a path to $\pW$, since $\pC$ reaches $\pJ$ in the underlying digraph and $\pJ\to\pF$. In the cascade, $\pC$ appears in the tail of only one hyperarc, $(\{\pI,\pC\},\pJ)$, which fires only if $\pI$ has also failed. (d) $\pJ\to\pP\to\pF$ replaces $\pJ\to\pF$ in both arguments of \cref{thm:formalized-state:interdependence}. (e) With the arc $\pC\to\pJ$, the chain $\pC\to\pJ\to\pF\to\pW$ fires and $\pW$ reaches every function.
   474	\end{proof}
   475	
   476	Part (e) is the reason to use hyperarcs. The arc representation would assert that a collapse of coercion disables interpretation. Part III showed the opposite: a determination that the parties regard as legitimate settles the dispute with no sanction behind it. Part (c) shows what X5 contributes. Without it, coercion is linked to the other functions but its failure stays local, because interpretation can rest on legitimacy alone and nothing else uses coercion directly.
   477	
   478	Part V's exception for bilateral exclusion does not touch the theorem. Corollary 3.7 of Part V concerns the motivation of sanctioners: when a cheated trader simply refuses to deal again with the cheat, the refusal costs nothing and needs neither provisioning nor legitimation, so the hyperarc $(\{\pF,\pI\},\pC)$ is absent. \Cref{thm:formalized-state:interdependence} uses no arc into coercion except $\pW\to\pC$, and that arc holds for bilateral exclusion too. The trader who withholds cooperation is an agent whose consumption is counted in Ax6$^{*}$, and the cooperation withheld is itself an exchange of produced goods; without production there is nothing to withhold and nobody to withhold it. The arc out of coercion that the theorem uses, $\pC\to\pF$, rests on X5 and on Lemma 3.3 of Part V, which say only that without any response to breach the breach rate exceeds tolerance. Bilateral exclusion is one such response. When it is the only one, coercion is exercised in its most dispersed form, and the arc is unaffected.
   479	
   480	A second route from legitimation to coercion exists, and it does not rest on reading equilibrium beliefs as legitimacy. Under Ax4$^{*}$, every window contains an entrant who did not know the rule system at entry (Lemma 3.4 of Part IV). A sanction rule deters such an entrant only once the entrant can tell which conduct the others will answer with exclusion, fines or force, and the practices that supply that information to entrants are the ones Theorem 3.5 of Part IV assigns to legitimation. The argument concerns the information of particular members who arrive uninformed, not the beliefs that sanctioners hold in equilibrium. It yields the arc $\pI\to\pC$ whenever sanction rules belong to the rule system whose common knowledge Ax4$^{*}$ requires. The theorem does not need this arc, and \cref{rem:formalized-state:further} lists it with the others.
   481	
   482	Every arc of $\Dstar$ appears in the minimal forms of \cref{tab:hardcases}, without offices. Among the Ju/'hoansi, foraging feeds the people who talk disputes out and criticize stinginess ($\pW\to m$); arrow-owner rules are learned in talk that everyone hears ($\pI\to\pF$); access to territory and water runs through rights held by kin ($\pF\to\pW$); disputes over sharing are talked out ($\pJ\to\pF$); and criticism of failures to share, recorded by Wiessner, holds people to the sharing rules ($\pC\to\pF$) \citep{lee2013,wiessner2005}. Among the Nuer, cattle rights govern herding ($\pF\to\pW$), compensation in cattle after a homicide is fixed through the leopard-skin chief ($\pJ\to\pF$), and the settlement holds because the parties value it and fear renewed feud, which is the disjunction of $(\{\pI,\pC\},\pJ)$ \citep{evanspritchard1940}. In Ostrom's commons, users modify their appropriation rules through collective-choice arrangements ($\pP\to\pF$), resolve conflicts over them in local arenas ($\pJ\to\pF$), monitor and sanction appropriators ($\pC\to\pF$), and draw provision labor from the users themselves under the same rules ($\pF\to\pW$) \citep{ostrom1990}. The dependency structure is the same in a band as in an empire. What differs is who sits at each node.
   483	
   484	\begin{remark}[Further arcs]
   485	\label{rem:formalized-state:further}
   486	Other incidences yield arcs that the theorem does not need. A replaced rule coordinates behavior only once it is common knowledge, so $\pI\to\pP$ whenever rules change (Part IV, Section 3). Under changes that alter the rules of adjudication and recognition, $\pP\to\pJ$ and $\pP\to\pI$. Where determinations bind later cases, interpretation changes rules, so $\pJ\to\pP$; with the arcs $\pI\to\pP$, $\pP\to\pJ$ and $\pP\to\pI$ this makes Hart's three secondary functions mutually reachable. Where sanctions are costly public goods delivered at large scale without higher-order sanctions, $(\{\pF,\pI\},\pC)$ by Corollary 3.7 of Part V, which gives a micro-foundation for the coupling of war making and extraction that \citet{tilly1990} described. When sanctions take the form of bilateral exclusion, Part V shows that sanctioners need no provisioning or legitimation, and the hyperarc is absent. Where sanction rules belong to the rule system whose common knowledge Ax4$^{*}$ requires, informing entrants of them yields $\pI\to\pC$, as argued above.
   487	\end{remark}
   488	
   489	\section{Capture}
   490	\label{sec:capture}
   491	
   492	\subsection{Integration}
   493	
   494	The source defines cross-pillar integration descriptively, and Part II proposed a formal candidate for pairs that include rule making (Section 6 of Part II, Equation 2). The series adopts it for all fifteen pairs.
   495	
   496	\begin{definition}[Coalition-overlap integration]
   497	\label{def:formalized-state:overlap}
   498	Let $\mathcal{S}$ be a preregistered list of coherent coalitions, groups such as parties, firms, dynasties or factions that can issue joint directives. For $S\in\mathcal{S}$ and a pillar $m$, let $\kappa_m(S)\in[0,1]$ be the share of decision-relevant control in $m$ that is exercised in accordance with the directives of $S$; for $m=\pP$ it is the bloc share of Part II. Then
   499	\[
   500	C^{\ov}_{mn}=\max_{S\in\mathcal{S}}\min\{\kappa_m(S),\kappa_n(S)\}.

2026-10-22T19:04:55.737271Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '250,400p' papers/latex/formalized-state.tex | nl -ba -v250" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   250	Part (b) is the formal answer to the charge that Proposition A is true by definition. In each modified collective the function is absent and the collective persists, so the class of persistent collectives does not contain the six functions by construction. What excludes such collectives from the real world is the failure of their premises: harmless unsettled conflict, unanimous preferences, free exit, innate rules, untempted members and unproduced inflows. Those are empirical claims, and the pillar Parts tested each against the ethnographic and historical record.
   251	
   252	\subsection{Minimal forms}
   253	
   254	The hard cases for Proposition A are societies described as having no state, no chiefs with power to command, or radical equality. The series predicts that each implements every function in an informal and dispersed form. The prediction has a formal core.
   255	
   256	\begin{lemma}[Minimal form]
   257	\label{lem:formalized-state:minimal}
   258	Let a collective of $n\ge2$ adults implement every function through practices without designated offices in which each adult holds an equal share of decision-relevant control, and let $Q_m\ge\bar q$ for every $m$. Then $H_m=1/n$ for every $m$ and $U_t\le(1-\bar q)/n$. If the coalition of all adults is admissible in the coalition list that defines $C_{mn}$ (\cref{def:formalized-state:overlap}), then $C_{mn}=1$ for every pair and $\Integ_t=1$. In either case the capture predicate of \cref{def:formalized-state:cap} fails for every threshold $u^{*}>(1-\bar q)/n$.
   259	\end{lemma}
   260	
   261	\begin{proof}
   262	Equal shares give $H_m=n\cdot(1/n)^2=1/n$. Then $U_t=\sum_m\omega_m(1/n)(1-Q_m)\le(1-\bar q)/n$. If the grand coalition $S=N$ is admissible, its control share in every pillar is one, so $\min\{\kappa_m(N),\kappa_n(N)\}=1$ for every pair. The capture predicate requires $U_t\ge u^{*}$, which fails when $u^{*}>(1-\bar q)/n$.
   263	\end{proof}
   264	
   265	The lemma resolves an apparent paradox in the ethnography. In egalitarian bands the same body judges, sanctions, decides and legitimates, so integration is at its maximum (Part III observed that $C_{\pJ\pC}$ is high there), yet the functions are held equally and open to challenge by anyone, so unaccountable concentration is near its minimum. This is the clearest reason why the source requires both indices to be high: integration of functions in the group as a whole is the opposite of capture.
   266	
   267	\Cref{tab:hardcases} collects the minimal forms that the pillar Parts documented for the Nuer \citep{evanspritchard1940}, the Ju/'hoansi \citep{marshall1976,lee1979,lee2013,wiessner2005}, mobile foragers with a reverse dominance hierarchy \citep{boehm1999}, Amazonian groups whose headmen speak but cannot command \citep{clastres1987}, and Ostrom's long-enduring commons \citep{ostrom1990,cox2010}. Woodburn's institutions of leveling show the same pattern from the side of sanctions: egalitarianism is produced and defended, not given \citep{woodburn1982}.
   268	
   269	\begin{table}[!htbp]
   270	\centering
   271	\small
   272	\caption{Minimal forms of the six functions in stateless and consensus societies, as documented in Parts I to VI. Each cell names the practice; no cell names an office with power to command.}
   273	\label{tab:hardcases}
   274	\footnotesize
   275	\setlength{\tabcolsep}{3pt}
   276	\begin{tabularx}{\textwidth}{@{}L{1.6cm}YYYYYY@{}}
   277	\toprule
   278	Case & $\pF$ & $\pP$ & $\pJ$ & $\pI$ & $\pC$ & $\pW$ \\
   279	\midrule
   280	Nuer & Cattle rights and bridewealth & Negotiation among lineages & Mediation by the leopard-skin chief & Lineage idiom and ritual & Threat of feud by kin & Herding and cultivation \\
   281	Ju/'hoansi & Meat shared by the arrow-owner rule & Camp talk and moving camp & Talking disputes out & Talk heard by all and the healing dance & Criticism, ridicule and avoidance & Foraging by both sexes \\
   282	Mobile foragers & Sharing enforced against hoarders & Group decision against would-be leaders & Group judgment of deviants & Shared moral talk & Ostracism, exile and execution & Foraging \\
   283	Amazonian groups & The headman's duty of generosity & Consensus with oratory as duty & Peacemaking by the headman & Myth and the headman's recitation & Abandonment of a commanding headman & Gardening and hunting \\
   284	Commons users & Appropriation and boundary rules & Users modify the rules & Low-cost local arenas & Rules known to users & Monitoring and graduated sanctions & Provision of maintenance labor \\
   285	\bottomrule
   286	\end{tabularx}
   287	\end{table}
   288	
   289	The table supports both halves of the series' thesis: every function operates where no office does, which is what Proposition A requires, and concentration varies with circumstance and choice, which is what makes Proposition B contingent. Some early societies moved seasonally between egalitarian and hierarchical arrangements, including temporary policing during collective hunts \citep{graeber2021}; upland groups in Southeast Asia kept their functions dispersed to avoid incorporation into lowland states \citep{scott2009}; and early grain states concentrated the resource and productive functions where taxable surpluses allowed \citep{scott2017}. Two cautions qualify the record without removing any function from it. The ethnographies describe groups in marginal environments and in contact with states and markets, and foraging societies vary widely \citep{kelly1995}. Equal formal shares understate actual concentration, because age, gender, skill and kinship give some speakers more weight (Part II, Section 3).
   290	
   291	The Ju/'hoansi are the hardest case for the judicial derivation, because moving to another camp resolves many disputes with no third party (Part III, Section 3). Under the unit of \cref{def:formalized-state:collective} the collective is the network of camps linked by kinship and exchange, within which a move is not exit. We code the Ju/'hoansi as satisfying the inescapable-dispute clause of Ax3$^{*}$: rights to territory and water are held through kin and follow a person from camp to camp, and disputes over sharing and marriage among kin recur and are talked out in public \citep{lee2013,wiessner2005}; Lee's records of homicide show that self-help between kin carried a real risk of feud \citep{lee1979}, which we read as a hazard to the functioning of the camp network in the sense of Ax3$^{*}$. The coding is an ethnographic reading of these sources, not a measurement of the hazard. With it and the codings of the other five axioms in Parts I to VI, the Ju/'hoansi are an instance of \cref{thm:formalized-state:A}, with a thin but present judicial function.
   292	
   293	\subsection{Falsifiers and counterexample attempts}
   294	
   295	Each pillar Part identified its strongest counterexample attempt and the observation that would refute its result. \Cref{tab:falsifiers} collects them. Every reply in the table narrows the claim in a stated direction or relocates the function; none rescues the claim by redefining the function after the fact.
   296	
   297	\begin{table}[!htbp]
   298	\centering
   299	\small
   300	\caption{The strongest counterexample attempt for each pillar, the reply given in the pillar Part, and the observation that would refute the pillar's necessity result.}
   301	\label{tab:falsifiers}
   302	\begin{tabularx}{\textwidth}{@{}L{0.7cm}YYY@{}}
   303	\toprule
   304	 & Counterexample attempt & Reply & Falsifier \\
   305	\midrule
   306	$\pF$ & Foragers' wants are easily met, so there is no scarcity \citep{sahlins1972b} & Scarcity concerns conflicting claims, and affluence lowers $p$ without making it zero & A persistent collective whose members hold conflicting claims and resolve them mostly without any settlement procedure \\
   307	$\pP$ & Custom evolves without legislators \citep{hayek1973,ellickson1991} & Distributed practices still select and change rules, with no office & A long-lived plural group whose rules never changed through environments that no single rule system could survive \\
   308	$\pJ$ & Free exit, or rules executed by code & Free exit thins the function (Proposition 3.4 of Part III), and code relocates interpretation to the encoding of cases (Proposition 3.5 of Part III) & A persistent collective in which disputes that a move does not escape recur and are always settled by force or left open \\
   309	$\pI$ & Force alone coordinates & Sanctions deter only those who know them, and elites must coordinate on expectations & A collective with turnover and locally variable rules whose entrants coordinate without any practice that informs them \\
   310	$\pC$ & Reciprocity and reputation enforce without coercion \citep{axelrod1984,greif1993} & Withdrawal of cooperation is a sanction & A rule whose measured temptation share exceeds its observed violation rate while violators fare no worse than matched compliers \\
   311	$\pW$ & Endowments, raiding, rents or automation & Production is relocated to donors, victims, extractors or the owners of machines (Lemma 3.4 of Part VI) & A system that persists indefinitely with no production anywhere and no replenishment of its stock \\
   312	\bottomrule
   313	\end{tabularx}
   314	\end{table}
   315	
   316	The coercion row needs one further safeguard. The replies to internalization and exit could be used to reclassify any compliant collective without sanctions as one in which few members are tempted, which would make the necessity claim immune to evidence. Part V therefore requires that the temptation share be measured independently of the sanction practices it is used to explain, for example by offering members an unobserved opportunity to break a rule, and it states the falsifier without the tolerance $\theta$, which would otherwise be an adjustable parameter. The same requirement applies to every hazard in \cref{tab:axioms} and to the legitimacy value and expected sanction in the compliance clause of Ax3$^{*}$: a premise measured only through the outcome it is meant to explain cannot test anything.
   317	
   318	\subsection{Hart's secondary rules}
   319	
   320	Hart argued that a regime of primary obligations alone suffers from uncertainty about which rules exist, a static character, and inefficiency in settling disputes, and that the remedies are a rule of recognition, rules of change and rules of adjudication \citep{hart1961}. The series assigns these to legitimation, rule making and interpretation (Definition 3.6 of Part II, Definition 2.2 of Part IV, Section 2 of Part III), and draws the boundary between $\pP$ and $\pJ$ by acts: making or changing a general rule belongs to $\pP$, applying a given rule to a case belongs to $\pJ$ (Definition 2.3 of Part II). A court that changes a rule by precedent performs both acts, and the role map records it in both layers. Under precedent, interpretation becomes an input to rule change and rule change produces the rules that interpretation applies, while recognition certifies both, since a new statute or precedent coordinates behavior only once it is common knowledge (Theorem 3.5 of Part IV). In \cref{sec:dependency}, Hart's triad appears as the arcs $\pI\to\pP$, $\pP\to\pJ$, $\pJ\to\pP$ and $\pP\to\pI$, which make the three secondary functions mutually reachable whenever rules change through both legislation and precedent.
   321	
   322	\subsection{Functional explanation}
   323	
   324	\Cref{thm:formalized-state:A} is a condition of persistence. It does not explain why any particular institution exists, and it asserts no feedback from the effects of an institution to its existence, which Elster required of functional explanation \citep{elster1979,elster1983}. It says nothing about why the Nuer had a leopard-skin chief or why Bourbon France sold judicial offices. Older lists of functional prerequisites drifted toward tautology because they defined prerequisites by what persisting societies happened to have (\cref{sec:literature}); the present derivation avoids the drift because each premise can be false and \cref{prop:formalized-state:independence} exhibits persistent collectives in which it is.
   325	
   326	\section{The dependency structure}
   327	\label{sec:dependency}
   328	
   329	\subsection{Dependency as a directed hypergraph}
   330	
   331	Proposition A speaks of the six functions ``together with the dependency relations among them''. The pillar Parts found two dependencies that a directed graph cannot express. An effective judicial determination needs either legitimacy or an expected sanction, and neither by itself (Proposition 3.6 of Part III). Large-scale sanctioning needs either material provisioning or legitimation, but only when sanctions are costly public goods (Proposition 3.6 and Corollary 3.7 of Part V). A dependency on one of several functions is a hyperarc. Directed hypergraphs of this kind, with reachability through hyperarcs whose whole tail has been reached, are standard in the study of AND/OR structures \citep{gallo1993}.
   332	
   333	\begin{definition}[Dependency hypergraph]
   334	\label{def:formalized-state:hypergraph}
   335	A \emph{hyperarc} is a pair $(T,m)$ with $m\in\Mset$ and $\emptyset\neq T\subseteq\Mset\setminus\{m\}$. The hyperarc $(T,m)$ belongs to the dependency structure $\mathcal{D}(G)$ of a collective if, almost surely on $\Pi$, infinitely many of the instances that the practices of $m$ solve are solved only with an output of at least one function in $T$: if every function in $T$ withheld its output, each of those instances would be left unsolved. The instances of each function are those of its implementation predicate: conflicts over goods for $\pF$, collective decisions for $\pP$, residual disputes for $\pJ$, entrants in a window for $\pI$, agent-periods under the rule for $\pC$, and periods of production for $\pW$. When $T=\{n\}$ the hyperarc is an \emph{arc}, written $n\to m$, with the provider on the left. A hyperarc with $|T|\ge2$ is a disjunction: $m$ needs some member of $T$, not all of them.
   336	\end{definition}
   337	
   338	\begin{definition}[Connectivity and cascade]
   339	\label{def:formalized-state:cascade}
   340	The \emph{underlying digraph} of $\mathcal{D}$ has an arc $t\to m$ for every $(T,m)\in\mathcal{D}$ and every $t\in T$. For $S\subseteq\Mset$ the \emph{cascade} $\cl_{\mathcal{D}}(S)$ is the smallest set that contains $S$ and contains $m$ whenever $(T,m)\in\mathcal{D}$ and $T\subseteq\cl_{\mathcal{D}}(S)$. $\mathcal{D}$ is \emph{strongly connected} if its underlying digraph is, and \emph{cascade-complete} if $\cl_{\mathcal{D}}(\{n\})=\Mset$ for every $n$. The \emph{interdependence predicate} $\Inter(G)$ holds if $\mathcal{D}(G)$ is strongly connected and cascade-complete.
   341	\end{definition}
   342	
   343	The cascade $\cl_{\mathcal{D}}(S)$ is the set of functions that fail when the functions in $S$ withhold their outputs, propagated through the instances of \cref{def:formalized-state:hypergraph}. Strong connectivity says that every function is linked to every other by a chain of dependencies. Cascade completeness says more: the failure of any single function brings down all the others. The two notions coincide for digraphs and come apart for hypergraphs, because a disjunctive hyperarc transmits failure only when its whole tail has failed.
   344	
   345	\begin{remark}[Dependency through persistence]
   346	\label{rem:formalized-state:persistence}
   347	If $n\to m$ were defined to mean that the collective stops persisting when $n$ is withheld, \cref{thm:formalized-state:A} would make every function depend on every other at no cost: withholding any function ends persistence, and every implementation predicate is defined on the persistence event. \Cref{def:formalized-state:hypergraph} excludes this by requiring that the instances of $m$ use an output of $T$ directly. Interdependence in the present sense is a claim about how the functions operate, and it does not follow from Proposition A.
   348	\end{remark}
   349	
   350	\subsection{Dependencies derived from the axioms}
   351	
   352	\begin{lemma}[Derived dependencies]
   353	\label{lem:formalized-state:D0}
   354	Under the hypotheses of \cref{thm:formalized-state:A}, $\mathcal{D}(G)$ contains
   355	\[
   356	\Dzero=\bigl\{\pW\to\pF,\ \pW\to\pP,\ \pW\to\pJ,\ \pW\to\pI,\ \pW\to\pC,\ (\{\pI,\pC\},\pJ),\ \pI\to\pF\bigr\}.
   357	\]
   358	It need not contain the arc $\pI\to\pJ$ or the arc $\pC\to\pJ$.
   359	\end{lemma}
   360	
   361	\begin{proof}
   362	\emph{Production.} By the last clause of Ax6$^{*}$, every practice is performed only when its performers' consumption is met. The initial stock is finite and consumption is at least $k>0$ per period, so without produced inflows the stock is exhausted after at most $X_0/k$ periods (Lemma 3.3 of Part VI). Every instance of every other function that falls after that date is solved only if productive activity, by members or by outsiders (Lemma 3.4 of Part VI), supplies the practitioners' consumption. On $\Pi$ each function solves infinitely many instances, so $\pW\to m$ for every $m\neq\pW$.
   363	
   364	\emph{Interpretation.} By the compliance clause of Ax3$^{*}$, which is the model of Proposition 3.6 of Part III, a losing party that gains $g>0$ by defiance complies if and only if $\ell+\sigma\ge g$, where $\ell$ is the value it places on the procedure's legitimacy and $\sigma$ the expected sanction. A party to a residual dispute strictly prefers its own verdict (Definition 2.2 of Part III), so $g>0$. If legitimation and sanction both withhold their outputs, then $\ell=\sigma=0$ by Ax3$^{*}$ and no determination is effective, so $\Impl_{\pJ}$ requires an output of legitimation or of sanction for each effective determination, and $(\{\pI,\pC\},\pJ)\in\mathcal{D}(G)$. In the collective of \cref{prop:formalized-state:independence}(a) with the fine $d\ge g$ also attached to defiance of a determination, each determination is effective with either output alone, so neither $\pI\to\pJ$ nor $\pC\to\pJ$ belongs to $\mathcal{D}(G)$.
   365	
   366	\emph{Allocation and recognition.} A conflict is settled only if members can anticipate the assignment from a description of the procedure (Definition 2.2(b) of Part I), which requires that they know the procedure. Settlement procedures belong to the rule system whose common knowledge Ax4$^{*}$ requires, and under Ax4$^{*}$ every window of length $L$ contains a member of the cooperating core who entered without knowing the rule system (Lemma 3.4 of Part IV) and came to know it only through practices of the legitimation function (Theorem 3.5 of Part IV). The conflicts that such members are party to after entry, which recur on $\Pi$ by the last clause of Ax4$^{*}$, are settled only with that output, so $\pI\to\pF$.
   367	\end{proof}
   368	
   369	\begin{corollary}[Structural necessity with dependencies]
   370	\label{cor:formalized-state:struct}
   371	Under the hypotheses of \cref{thm:formalized-state:A}, $\Struct(G)$ holds. If every functioning human collective satisfies the refined axioms, $\Struct(G)$ holds for every $G\in\mathcal{G}$.
   372	\end{corollary}
   373	
   374	\begin{proof}
   375	\Cref{thm:formalized-state:A} gives $\Impl_m(G)$ for every $m$ almost surely on $\Pi$, and \cref{lem:formalized-state:D0}, whose hypotheses are those of the theorem, gives $\Dzero\subseteq\mathcal{D}(G)$. The second sentence is the first under the bridge hypothesis.
   376	\end{proof}
   377	
   378	The structure $\Dzero$ is not strongly connected. No arc enters $\pW$, and $\pP$ and $\pJ$ have no outgoing arc, and $\pC$ has one only through the disjunctive hyperarc. Apart from the compliance clause of Ax3$^{*}$ and the settlement-procedure and entrant clauses of Ax4$^{*}$, the six axioms constrain each function separately. The next subsection adds the incidences on production, rule making, interpretation and coercion.
   379	
   380	\subsection{Incidence axioms}
   381	
   382	The six problems converge on one object in every collective that the pillar Parts examined: the rules that assign goods. A settlement procedure is a rule that must be changed when circumstances change, interpreted when its application is disputed, known to those it binds, enforced against those tempted to breach it, and applied to the inputs of production. Each of these is an incidence of one axiom on the financial pillar. They are stated as axioms because they are claims about collective life that the six axioms do not imply (\cref{prop:formalized-state:minimality}(a)), and each comes with a falsifier.
   383	
   384	\begin{assumption}[X1, contested inputs]
   385	\label{ass:formalized-state:X1}
   386	In infinitely many periods on $\Pi$, productive activity uses inputs, such as land, water, tools or equipment, that are goods under conflicting claims in the sense of Definition 2.1 of Part I, and an input is used productively only under an assignment that its user can anticipate.
   387	\end{assumption}
   388	
   389	\begin{assumption}[X2, changing environment]
   390	\label{ass:formalized-state:X2}
   391	On $\Pi$ the environment changes infinitely often in the sense of Assumption 3.2 of Part II, and each change creates conflicts over goods that no settlement procedure in force before the change can settle.
   392	\end{assumption}
   393	
   394	\begin{assumption}[X3, open-textured allocation]
   395	\label{ass:formalized-state:X3}
   396	Some settlement procedure in force has open texture in the sense of Definition 2.1 of Part III, and on $\Pi$ infinitely many residual disputes about its application arise that a move does not escape, subject to the hazard of Ax3$^{*}$.
   397	\end{assumption}
   398	
   399	\begin{assumption}[X5, tempting allocation]
   400	\label{ass:formalized-state:X5}

2026-10-22T19:04:58.973629Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '496,750p' papers/latex/formalized-state.tex | nl -ba -v496" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   496	\begin{definition}[Coalition-overlap integration]
   497	\label{def:formalized-state:overlap}
   498	Let $\mathcal{S}$ be a preregistered list of coherent coalitions, groups such as parties, firms, dynasties or factions that can issue joint directives. For $S\in\mathcal{S}$ and a pillar $m$, let $\kappa_m(S)\in[0,1]$ be the share of decision-relevant control in $m$ that is exercised in accordance with the directives of $S$; for $m=\pP$ it is the bloc share of Part II. Then
   499	\[
   500	C^{\ov}_{mn}=\max_{S\in\mathcal{S}}\min\{\kappa_m(S),\kappa_n(S)\}.
   501	\]
   502	\end{definition}
   503	
   504	The measure lies in $[0,1]$, equals one exactly when some listed coalition commands all of both pillars, and equals zero exactly when no listed coalition has a positive share in both. Its value depends on the coalition list, which is why the list must be fixed before coding. Write $\deg_m=\sum_{n\neq m}C_{mn}$ for the integration degree of pillar $m$.
   505	
   506	\begin{lemma}[Degree, star and clique bounds]
   507	\label{lem:formalized-state:hub}
   508	For any symmetric $C$ with entries in $[0,1]$ and $M=6$:
   509	\begin{enumerate}[label=(\alph*)]
   510	\item $\Integ=\frac{1}{M(M-1)}\sum_{m}\deg_m=\frac{1}{30}\sum_m\deg_m$;
   511	\item if $C_{mn}=0$ whenever neither $m$ nor $n$ lies in a set $A$ of $k$ pillars, then $\Integ\le\bar c\,\bigl(k(M-k)+k(k-1)/2\bigr)/15$ with $\bar c=\max_{m<n}C_{mn}$; for a single hub, $k=1$, the bound is $\bar c/3$;
   512	\item under \cref{def:formalized-state:overlap}, if a coalition $S\in\mathcal{S}$ has $\kappa_m(S)\ge c$ for every $m$ in a set $A$ of $k$ pillars, then $C_{mn}\ge c$ for all distinct $m,n\in A$ and $\Integ\ge c\,k(k-1)/30$.
   513	\end{enumerate}
   514	\end{lemma}
   515	
   516	\begin{proof}
   517	(a) Each pair $\{m,n\}$ appears in $\deg_m$ and in $\deg_n$, so $\sum_m\deg_m=2\sum_{m<n}C_{mn}$, and $\Integ=\frac{2}{M(M-1)}\sum_{m<n}C_{mn}$. (b) The pairs with at least one member in $A$ number $k(M-k)+k(k-1)/2$; each contributes at most $\bar c$ and the others contribute zero; divide by fifteen. (c) For $m,n\in A$, $C^{\ov}_{mn}\ge\min\{\kappa_m(S),\kappa_n(S)\}\ge c$. The $k(k-1)/2$ such pairs contribute at least $c\,k(k-1)/2$ to the sum, and $\Integ$ is that sum divided by fifteen.
   518	\end{proof}
   519	
   520	The lemma separates two patterns that comparative accounts often run together. In a star, one pillar is coupled to the others by different coalitions, and the remaining pillars are not coupled to one another: with $k=1$, integration cannot exceed one third of the largest coupling. In a clique, one coalition commands several pillars, and the overlap measure forces every pair among them to be coupled: a coalition that commands a share $c$ of five pillars produces $\Integ\ge2c/3$. A threshold $i^{*}$ above one third therefore cannot be met by a pure star, whatever its couplings. The distinction is the formal content of the source's warning that strong organizations do not by themselves imply a strong coalition \citep{largo2026hbs}.
   521	
   522	\subsection{The capture predicate}
   523	
   524	\begin{definition}[Capture predicate]
   525	\label{def:formalized-state:cap}
   526	Fix preregistered thresholds $(u^{*},i^{*})\in(0,1]^2$ and weights $\omega$. Let $L_t$ be the set of capture links documented at $t$, each meeting the source's three conditions. Then $\Capt_{u^{*},i^{*}}(G,t)$ holds if $U_t\ge u^{*}$, $\Integ_t\ge i^{*}$ and $L_t\neq\emptyset$. Proposition B for a polity in a period is the statement that $\Capt$ holds.
   527	\end{definition}
   528	
   529	The source's stricter classification adds documented unaccountable concentration in at least two pillars, persistent restriction of effective contestation, and a materially consequential pattern linked to the concentrated coalition \citep{largo2026hbs}. These refine the predicate and do not change its logic. The predicate is defined only when each pillar has a control-share vector, so capture presupposes that the six functions are realized. The converse is the subject of this section.
   530	
   531	\begin{lemma}[Range of unaccountable concentration]
   532	\label{lem:formalized-state:U}
   533	(a) $0\le U_t\le1$. (b) $U_t=0$ if and only if $Q_m=1$ for every $m$ with $\omega_m>0$. (c) $\min_mH_m(1-Q_m)\le U_t\le\max_mH_m(1-Q_m)$, and both bounds are attained at vertices of the weight simplex.
   534	\end{lemma}
   535	
   536	\begin{proof}
   537	Each term $H_m(1-Q_m)$ lies in $[0,1]$, and $U_t$ is their convex combination, which gives (a) and (c); the bounds of (c) are attained by putting all weight on a minimizing or a maximizing pillar. For (b), a pillar with holders has $H_m\ge1/n_m>0$, so a term with positive weight vanishes only if $Q_m=1$.
   538	\end{proof}
   539	
   540	Part (c) bounds the effect of the weights: however they are chosen, $U_t$ stays in the interval spanned by the pillar terms, which is why the source requires them to be preregistered.
   541	
   542	\subsection{Non-implication}
   543	
   544	\begin{lemma}[Separation]
   545	\label{lem:formalized-state:separation}
   546	Describe a model of a collective as a pair $(\Gamma,\Lambda)$. $\Gamma$ consists of the processes of arrivals, dispositions, hazards, temptations and margins, information partitions, and stocks and flows. $\Lambda$ consists of the role map, the control shares, the coalition list with its control shares $\kappa$, the contestability components, and the record of evidence on capture links. Call $\Lambda$ admissible if every agent it assigns to a practice is a member, or an organization of members, whose consumption is counted in Ax6$^{*}$; no party to a residual dispute alone controls its determination; and the practices of rule making are the members' own. The refined axioms, the incidence axioms, the implementation predicates and the dependency structure are, for admissible $\Lambda$, functions of $\Gamma$ alone. $U_t$, $\Integ_t$ and $L_t$ are functions of $\Lambda$ alone.
   547	\end{lemma}
   548	
   549	\begin{proof}
   550	\Cref{tab:axioms}, \cref{def:formalized-state:implementation,def:formalized-state:hypergraph} and Assumptions X1, X2, X3 and X5 (\cref{ass:formalized-state:X1,ass:formalized-state:X2,ass:formalized-state:X3,ass:formalized-state:X5}) refer to whether conflicts are settled, decisions made, disputes determined, information refined, violations met and inflows produced, and to the hazards and temptations attached to these events. None refers to a share, to a coalition, to a contestability component or to evidence of privileged access. Admissibility fixes the only clauses that mention performers: the party-control clause of $\Impl_{\pJ}$, the self-government clause of Ax2$^{*}$ and the practice clause of Ax6$^{*}$. $U_t$ is computed from shares and contestability, $\Integ_t$ from the coalition list and $\kappa$, and $L_t$ from the evidentiary record.
   551	\end{proof}
   552	
   553	\begin{theorem}[Proposition A does not imply Proposition B]
   554	\label{thm:formalized-state:nonimplication}
   555	There are four collectives, each satisfying Ax1$^{*}$ to Ax6$^{*}$ and X1, X2, X3 and X5, and hence $\Struct$ and $\Inter$, whose pairs $(U_t,\Integ_t)$ are $(0,0)$, $(0,1)$, $(1,0)$ and $(1,1)$, and of which only the last has a documented capture link. Consequently, for every pair of thresholds $(u^{*},i^{*})\in(0,1]^2$, structural necessity and interdependence hold both in a collective where $\Capt$ holds and in collectives where it fails, and neither $U_t\ge u^{*}$ nor $\Integ_t\ge i^{*}$ implies $\Capt$.
   556	\end{theorem}
   557	
   558	\begin{proof}
   559	Extend the collective of \cref{prop:formalized-state:independence}(a) to at least twelve members and adjust four components so that the incidence axioms hold. The contested plot is the field the members cultivate, so production uses an input under an anticipable assignment (X1). The environment alternates between two states, and each change brings a new kind of claim that the old rotation rule does not cover, which the members settle by voting a new rule (X2). The residual disputes concern the application of the rotation rule to boundary cases (X3). Members are tempted to take the field out of turn with $p>\theta$, and a member who does so pays a fine and is made to return the field, so the conflict counts as settled (X5). Call the resulting processes $\Gamma$. By \cref{cor:formalized-state:struct,thm:formalized-state:interdependence}, $\Gamma$ yields $\Struct$ and $\Inter$, and by \cref{lem:formalized-state:separation} it does so under any admissible assignment $\Lambda$ of the practices to agents. Four assignments give the corners. In each corner the organizations consist of members, every determination is made by an organization that contains neither party (in $(0,1)$ by all members, so neither party controls it alone), and the procedures are those of $\Gamma$ with performers relabeled, so each assignment is admissible.
   560	
   561	$(0,0)$: each pillar's practices are performed by two organizations with equal shares, the twelve organizations are distinct, $\mathcal{S}$ lists only single organizations, and $Q_m=1$ for every $m$. Then $H_m=1/2$, $U_t=0$ by \cref{lem:formalized-state:U}(b), every $C_{mn}=0$, $\Integ_t=0$, and the record contains no capture link.
   562	
   563	$(0,1)$: every member takes an equal part in every practice by consensus, the coalition of all members is listed, and $Q_m=1$. Then $U_t=0$ and, by \cref{lem:formalized-state:minimal}, $\Integ_t=1$; the record contains no capture link.
   564	
   565	$(1,0)$: each pillar's practices are performed by a single organization, the six organizations are distinct, $\mathcal{S}$ lists only single organizations, and $Q_m=0$. Then $H_m=1$, $U_t=1$, every $C_{mn}=0$, $\Integ_t=0$, and the record contains no capture link.
   566	
   567	$(1,1)$: one organization performs every practice and $Q_m=0$. Then $H_m=1$, $U_t=1$, $\kappa_m=1$ for that organization in every pillar, $\Integ_t=1$, and the record documents one capture link: the organization's discretion over determinations removes review, and a record ties that discretion to an assignment of the field.
   568	
   569	For thresholds in $(0,1]^2$, the collective at $(1,1)$ satisfies $\Capt$, the one at $(0,0)$ does not, the one at $(1,0)$ fails $\Integ_t\ge i^{*}$ although $U_t\ge u^{*}$, and the one at $(0,1)$ fails $U_t\ge u^{*}$ although $\Integ_t\ge i^{*}$.
   570	\end{proof}
   571	
   572	The theorem formalizes three of the source's commitments. Differentiated functions do not establish a common hierarchy (source Proposition 1): the corner $(1,0)$ has six monopolies and no coalition among them. Integration of functions is not capture: the corner $(0,1)$ is the minimal form of the stateless societies. And the strong claim requires both indices and a documented link, because each index alone is compatible with its absence. Structural necessity fixes the support of the role map. Capture is a claim about its values.
   573	
   574	\section{Representation and minimality}
   575	\label{sec:representation}
   576	
   577	\subsection{The Formalized State as an abstraction}
   578	
   579	The results so far concern properties that every functioning collective has. This section states them as a single claim about an abstraction. The Formalized State is not a form of government. It is a class of mathematical structures, and the claim is that every governance system, whatever its period, ideology, institutions or degree of centralization, is represented by a member of the class. Historical regimes are instances. The name ``Beast System'' is the series' typological reading of the abstraction (\cref{sec:revelation}); it is not a conclusion of any theorem.
   580	
   581	\begin{definition}[Formalized State structure]
   582	\label{def:formalized-state:F}
   583	A \emph{Formalized State structure} is a tuple $F=(V,\rho,A,s,Q,\omega,\mathcal{S},\kappa,L,\mathcal{D})$ in which $V$ is a finite nonempty set of actors, $\rho:V\to2^{\Mset}$ is a role map, $A=(A^m)_{m\in\Mset}$ are layers with entries in $[0,1]$, $s=(s^m)_{m\in\Mset}$ are vectors on $V$, $Q\in[0,1]^{\Mset}$, $\omega$ is a weight vector on $\Mset$, $\mathcal{S}$ is a list of subsets of $V$ with control shares $\kappa_m(S)\in[0,1]$, $L$ is a finite set of capture links $(i\to j,m)$ with $i,j\in V$, and $\mathcal{D}$ is a set of hyperarcs on $\Mset$, subject to four conditions. Write $V_m=\{v\in V:m\in\rho(v)\}$.
   584	\begin{enumerate}[label=(F\arabic*)]
   585	\item Every function has a holder: $V_m\neq\emptyset$ for every $m\in\Mset$.
   586	\item Control lies with holders: each $s^m$ is a probability vector with $s^m_v>0$ only if $v\in V_m$, and $a^m_{ij}>0$ only if $i\in V_m$.
   587	\item The measurement components are in range: $\omega\ge0$ with $\sum_m\omega_m=1$.
   588	\item The dependency structure contains $\Dzero$ and is strongly connected and cascade-complete.
   589	\end{enumerate}
   590	The class of all such structures is $\mathcal{F}$. Each $F\in\mathcal{F}$ determines $H_m$, $U$, $C^{\ov}_{mn}$, $\Integ$ and the capture predicate by the formulas of \cref{sec:model,sec:capture}.
   591	\end{definition}
   592	
   593	The definition is purely mathematical. It does not mention any society, and checking whether a tuple belongs to $\mathcal{F}$ requires no knowledge of governance. Membership in $\mathcal{G}$, conversely, is checked without the pillars (\cref{def:formalized-state:collective}). The bridge between the two classes is a map that reads a structure off the coded record of a collective.
   594	
   595	\begin{definition}[Profile map]
   596	\label{def:formalized-state:profile}
   597	Let $G\in\mathcal{G}$ come with a coded record that lists, for each practice that recurs on $\Pi$, the actors who perform it and the actors it constrains, together with the contestability components, a preregistered coalition list with the share of each pillar's control that each coalition directs, the documented capture links, and preregistered weights. The \emph{profile} $\pi(G)=(V_G,\rho_G,A_G,s_G,Q_G,\omega,\mathcal{S}_G,\kappa_G,L_G,\mathcal{D}(G))$ is built in five steps.
   598	\begin{enumerate}[label=(\roman*)]
   599	\item $V_G$ is the set of actors who perform some practice.
   600	\item $m\in\rho_G(v)$ if and only if $\Impl_m(G)$ holds and $v$ performs a practice of the class that \cref{def:formalized-state:implementation} assigns to $m$. A function that is not implemented receives no holders.
   601	\item $s^m_G$ is computed by the share rule of the Part that owns $m$: the stake-weighted share of last words for $\pJ$ (Part III, Section 2), the power index of the decision procedure for $\pP$ (Part II, Section 2), deployment command for $\pC$ (Definition 2.2 of Part V), and the corresponding rules of Parts I, IV and VI. $A^m_G$ records the documented constraints.
   602	\item $Q_G$, $\omega$, $\mathcal{S}_G$, $\kappa_G$ and $L_G$ are copied from the record.
   603	\item $\mathcal{D}(G)$ is the dependency structure of \cref{def:formalized-state:hypergraph}.
   604	\end{enumerate}
   605	The record is well formed: each share rule returns a probability vector supported on the actors who perform practices of $m$, a constraint $(i,j,m)$ is recorded only if $i$ performs a practice of $m$, and the weights are nonnegative and sum to one. For $G\in\mathcal{G}$ and $F\in\mathcal{F}$, write $G\cong_AF$ if there is a bijection $\beta:V_G\to V_F$ that carries every component of $\pi(G)$ to the corresponding component of $F$. For $G,G'\in\mathcal{G}$ write $G\cong_AG'$ if a bijection $V_G\to V_{G'}$ carries $\pi(G)$ to $\pi(G')$.
   606	\end{definition}
   607	
   608	The profile is well defined on coded records. Steps (i), (ii), (iv) and (v) are determined by the record and the definitions, and step (iii) applies share rules that the pillar Parts fixed in advance; two codings of the same record differ at most by a relabeling of actors, which $\cong_A$ ignores. The relation $\cong_A$ is equivalence in the governance properties the abstraction keeps. It is not isomorphism of social detail, and the next lemma says exactly what is kept and what is not.
   609	
   610	\begin{lemma}[Preserved and forgotten properties]
   611	\label{lem:formalized-state:preserved}
   612	If $G\cong_AF$, then $G$ and $F$ have the same role map, control shares, concentrations $H_m$, contestability $Q_m$, unaccountable concentration $U$, couplings $C^{\ov}_{mn}$, integration $\Integ$, capture predicate for every threshold pair, dependency structure, and interdependence predicate, all up to the relabeling $\beta$. The relation $\cong_A$ does not preserve, and the abstraction does not represent, the content of the rules, the beliefs that legitimate them, the particular procedures that implement each function, the identities and histories of actors beyond their labels, the levels of capacity $x_t$, the quality or welfare consequences of decisions, or any moral evaluation of the system.
   613	\end{lemma}
   614	
   615	\begin{proof}
   616	Each preserved quantity is a function of the components that $\beta$ carries over: $H_m$ of $s^m$; $U$ of $s$, $Q$ and $\omega$; $C^{\ov}_{mn}$ and $\Integ$ of $\mathcal{S}$ and $\kappa$; the capture predicate of $U$, $\Integ$ and $L$; interdependence of $\mathcal{D}$. The forgotten items are not components of $\pi(G)$, so collectives that differ only in them have the same profile. Two examples show that the loss is real: a consensus band and a council of equals in a commons with the same number of members, the same contestability and the same dependency structure have the same image, and so do two monarchies that differ only in their official religion.
   617	\end{proof}
   618	
   619	\subsection{The representation theorem}
   620	
   621	\begin{theorem}[Representation]
   622	\label{thm:formalized-state:representation}
   623	Let $G\in\mathcal{G}$ come with a well-formed coded record.
   624	\begin{enumerate}[label=(\alph*)]
   625	\item $G\cong_AF$ for some $F\in\mathcal{F}$ if and only if $\Struct(G)$ and $\Inter(G)$ hold.
   626	\item If $G$ satisfies Ax1$^{*}$ to Ax6$^{*}$ and X1, X2, X3 and X5, then $F_G=\pi(G)$ belongs to $\mathcal{F}$ and $G\cong_AF_G$.
   627	\item If every functioning human collective satisfies the refined and incidence axioms, then for every $G\in\mathcal{G}$ there is $F_G\in\mathcal{F}$ with $G\cong_AF_G$.
   628	\end{enumerate}
   629	\end{theorem}
   630	
   631	\begin{proof}
   632	(a) Suppose $\Struct(G)$ and $\Inter(G)$. Each $\Impl_m(G)$ requires practices of $m$'s class that recur on $\Pi$, so step (ii) gives every function at least one holder, which is (F1). Since control in each pillar is exercised, the share rule of step (iii) yields a probability vector supported on the actors who exercise it, and documented constraints run only from holders, which is (F2). (F3) holds for preregistered weights. $\Struct(G)$ gives $\Dzero\subseteq\mathcal{D}(G)$ and $\Inter(G)$ gives strong connectivity and cascade completeness, which is (F4). So $\pi(G)\in\mathcal{F}$, and the identity map gives $G\cong_A\pi(G)$. Conversely, if $G\cong_AF$ with $F\in\mathcal{F}$, then by (F1) every function of $G$ has a holder, which by step (ii) happens only if $\Impl_m(G)$ holds for every $m$; by (F4) $\mathcal{D}(G)=\mathcal{D}_F$ contains $\Dzero$ and is strongly connected and cascade-complete, so $\Struct(G)$ and $\Inter(G)$ hold. (b) \Cref{cor:formalized-state:struct} and \cref{thm:formalized-state:interdependence} give $\Struct(G)$ and $\Inter(G)$, and (a) applies with $F_G=\pi(G)$. (c) is (b) under the bridge hypothesis.
   633	\end{proof}
   634	
   635	Universality over real governance systems is part (b) together with the empirical bridge that every functioning collective satisfies the refined and incidence axioms, which historical observation supports.
   636	
   637	Part (a) locates the content of the theorem. The profile map is defined for every collective, so the existence of a map is not the claim. The claim is that the image lands in $\mathcal{F}$: that every functioning collective has six nonempty layers with well-defined control shares and an interdependent dependency structure. That is exactly Proposition A, so the representation theorem is Proposition A stated as a property of an abstraction, and its proof runs through \cref{thm:formalized-state:A,thm:formalized-state:interdependence}. The representation can fail. The six collectives of \cref{prop:formalized-state:independence}(b) each have a function with no holders, so by (a) no structure in $\mathcal{F}$ represents them; the collective of \cref{prop:formalized-state:independence}(a) has all six functions but no arc into production (\cref{prop:formalized-state:minimality}(a)), so it fails (F4) and is not represented either. Whether a real collective is represented is therefore an empirical question, and the bridge hypothesis is the claim that the answer is always yes.
   638	
   639	Four results of the paper should be kept apart. Representation (\cref{thm:formalized-state:representation}) says that every governance system is an instance of the abstraction. Necessity (\cref{thm:formalized-state:A,thm:formalized-state:interdependence}) says why: the properties that membership requires follow from primitive axioms about collective life. Minimality (\cref{prop:formalized-state:minimality6}) says that no coarsening of the abstraction preserves the same properties. Uniqueness (\cref{thm:formalized-state:uniqueness,thm:formalized-state:six}) says that the abstraction is the coarsest one that does, up to a unique isomorphism, and that it has exactly six dimensions.
   640	
   641	\subsection{Minimality}
   642	
   643	Write $\mathcal{G}_*$ for the governance systems that satisfy Ax1$^{*}$ to Ax6$^{*}$, X1, X2, X3 and X5 and come with a well-formed coded record, and $P(G)$ for the isomorphism class of $\pi(G)$ under relabeling of actors. $P(G)$ is the \emph{preserved property set}: it determines the role map, the control shares, $H_m$, $Q_m$, $U$, $C^{\ov}_{mn}$, $\Integ$, the capture predicate and the dependency structure, and by \cref{def:formalized-state:profile} $G\cong_AG'$ if and only if $P(G)=P(G')$.
   644	
   645	An abstraction with fewer or other functional dimensions is obtained by a \emph{coarsening}. A coarsening is a map $c:\Mset\to K\cup\{\bot\}$ into a finite set $K$ whose image contains $K$, so that every block $c^{-1}(k)$ is nonempty, together with weights $\lambda_m>0$ that sum to one on each block $c^{-1}(k)$. It sends a structure to the structure indexed by $K$ in which block $k$ has holders $\bigcup_{m\in c^{-1}(k)}V_m$, shares $\sum_{m\in c^{-1}(k)}\lambda_ms^m$, layers, contestability and coalition shares formed with the same weights, and weight $\sum_{m\in c^{-1}(k)}\omega_m$; pillars with $c(m)=\bot$ are dropped, and the hyperarcs are the images under $c$ of the hyperarcs that contain no dropped pillar, with self-loops removed. Write $\Phi_c(G)$ for the coarsened image of $\pi(G)$, up to relabeling of actors. The identity coarsening gives $\Phi=\Phi_{\mathrm{id}}$, and $\Phi(G)=P(G)$. The source's five-function model is the coarsening that merges $\pP$ and $\pJ$ \citep{largo2026hbs}.
   646	
   647	\begin{proposition}[Minimality]
   648	\label{prop:formalized-state:minimality6}
   649	Let $(c,\lambda)$ be a coarsening that is not a bijection from $\Mset$ onto $K$. Then there are $G_1,G_2\in\mathcal{G}_*$ with $\Phi_c(G_1)=\Phi_c(G_2)$ and $P(G_1)\neq P(G_2)$. Explicitly:
   650	\begin{enumerate}[label=(\alph*)]
   651	\item if $c(m)=\bot$ for some $m$, $G_1$ and $G_2$ differ only in that $m$ is held by one organization $a$ in $G_1$, with $s^m=(1,0)$ on $(a,b)$, and by $a$ and $b$ equally in $G_2$, with $s^m=(1/2,1/2)$; then $H_m=1$ in $G_1$ and $H_m=1/2$ in $G_2$;
   652	\item if $c(m)=c(n)\neq\bot$ for some $m\neq n$, let $\mu=\lambda_m/(\lambda_m+\lambda_n)$; $G_1$ has $s^m=(1,0)$ and $s^n=(0,1)$ on $(a,b)$, and $G_2$ has $s^m=s^n=(\mu,1-\mu)$, with the same $Q_m=Q_n$ and with $\mathcal{S}$ listing single organizations; then $C^{\ov}_{mn}=0$ in $G_1$ and $\max\{\mu,1-\mu\}\ge1/2$ in $G_2$, so $\Integ$ differs by at least $1/30$, and $H_m=H_n=1$ in $G_1$ against $\mu^2+(1-\mu)^2<1$ in $G_2$.
   653	\end{enumerate}
   654	\end{proposition}
   655	
   656	\begin{proof}
   657	A coarsening whose restriction to the pillars not sent to $\bot$ is not a bijection onto $K$ either sends some pillar to $\bot$ or sends two pillars to the same element of $K$. In both cases start from the collective $\Gamma$ in the proof of \cref{thm:formalized-state:nonimplication}, let two organizations $a$ and $b$ perform the practices of the pillars named, code every other pillar identically in $G_1$ and $G_2$, and set the layers proportional to the shares, $a^{l}_{aj}=s^{l}_a$ and $a^{l}_{bj}=s^{l}_b$ for the pillars $l$ named and every other actor $j$. Since $a$ and $b$ are organizations of members that are parties to no residual dispute, both assignments are admissible, and by \cref{lem:formalized-state:separation} $G_1$ and $G_2$ satisfy every axiom, since they differ only in the assignment of control, so both lie in $\mathcal{G}_*$.
   658	
   659	(a) So that both collectives have the same actor set, let $a$ and $b$ also hold equal shares $(1/2,1/2)$ in one pillar $l_0\neq m$, with $c(l_0)\in K$ when $K\neq\emptyset$, identically in $G_1$ and $G_2$; in $G_1$ the organization $b$, which holds nothing in $m$, still performs practices of $l_0$. Dropping $m$ deletes its layer, shares, contestability and coalition shares, removes $m$ from every actor's roles, and deletes every hyperarc that contains $m$. What remains is identical in $G_1$ and $G_2$, so $\Phi_c(G_1)=\Phi_c(G_2)$; if $K=\emptyset$, both images consist of the actor set alone and coincide. The concentration $H_m=1^2=1$ in $G_1$ and $H_m=2\cdot(1/2)^2=1/2$ in $G_2$; a relabeling of actors does not change $H_m$, so $P(G_1)\neq P(G_2)$.
   660	
   661	(b) Here $a$ performs practices of $m$ and $b$ of $n$ in $G_1$, and both perform both in $G_2$, so the actor sets coincide; $a$ and $b$ perform no practice of any other pillar. In the block containing $m$ and $n$, the weighted shares of $m$ and $n$ contribute $\lambda_m(1,0)+\lambda_n(0,1)=(\lambda_m,\lambda_n)$ in $G_1$ and $(\lambda_m+\lambda_n)(\mu,1-\mu)=(\lambda_m,\lambda_n)$ in $G_2$. The coalition shares of the single organizations are $\kappa_l(\{a\})=s^l_a$ and $\kappa_l(\{b\})=s^l_b$, so they combine in the same way, as do the layers. Every other component is identical, so $\Phi_c(G_1)=\Phi_c(G_2)$. Before coarsening, $C^{\ov}_{mn}=\max\{\min(1,0),\min(0,1)\}=0$ in $G_1$ and $\max\{\min(\mu,\mu),\min(1-\mu,1-\mu)\}=\max\{\mu,1-\mu\}\ge1/2$ in $G_2$; the other fourteen couplings coincide, so $\Integ$ differs by at least $(1/2)/15=1/30$. The concentrations are $1$ against $\mu^2+(1-\mu)^2$, which is less than one for $\mu\in(0,1)$. These quantities are invariant under relabeling, so $P(G_1)\neq P(G_2)$.
   662	\end{proof}
   663	
   664	The independence of the axioms gives a stronger form of (a) on all of $\mathcal{G}$. The collectives of \cref{prop:formalized-state:independence}(a) and \cref{prop:formalized-state:independence}(b), coded with the same actors for the other five functions, have the same image after dropping $m_k$, although the first implements $m_k$ and the second does not. If one function were implied by the other five, dropping it would lose nothing. Part (b) shows what the source loses by merging rule making with interpretation: a polity whose legislature and courts are held by different organizations and one in which both share both functions in the same proportions have the same five-function image and different integration.
   665	
   666	\subsection{Uniqueness}
   667	
   668	\begin{definition}[Abstractions]
   669	\label{def:formalized-state:abstraction}
   670	Fix a countable universe of actor labels and dates, and let $\mathcal{G}_*$ consist of the governance systems in it whose coded records use those labels, so that $\mathcal{G}_*$ is a set. An \emph{abstraction} is a surjective map $\alpha:\mathcal{G}_*\to S_\alpha$ onto a set. It is \emph{$P$-preserving} if $P$ factors through it: $\alpha(G)=\alpha(G')$ implies $P(G)=P(G')$. A \emph{morphism} $\alpha\to\beta$ is a map $h:S_\alpha\to S_\beta$ with $h\circ\alpha=\beta$. Write $\mathbf{Abs}_P$ for the category of $P$-preserving abstractions and their morphisms. The \emph{Formalized State abstraction} is $\Phi:\mathcal{G}_*\to\mathcal{F}_*$, $\Phi(G)=[\pi(G)]$, where $\mathcal{F}_*$ is the set of isomorphism classes of structures in $\mathcal{F}$ that represent some $G\in\mathcal{G}_*$.
   671	\end{definition}
   672	
   673	Composition is composition of maps and the identity map is the identity morphism, so $\mathbf{Abs}_P$ is a category. Because abstractions are surjective, there is at most one morphism between two abstractions: $h$ is determined on $S_\alpha=\alpha(\mathcal{G}_*)$ by $h(\alpha(G))=\beta(G)$.
   674	
   675	\begin{theorem}[Uniqueness]
   676	\label{thm:formalized-state:uniqueness}
   677	Relative to the axioms Ax1$^{*}$ to Ax6$^{*}$, X1, X2, X3 and X5 and the preserved property set $P$:
   678	\begin{enumerate}[label=(\alph*)]
   679	\item $\Phi$ is an object of $\mathbf{Abs}_P$, and two systems have the same image under $\Phi$ if and only if $G\cong_AG'$;
   680	\item $\Phi$ is terminal in $\mathbf{Abs}_P$: for every $P$-preserving abstraction $\alpha$ there is exactly one morphism $\alpha\to\Phi$, so $\Phi$ is the coarsest $P$-preserving abstraction;
   681	\item every terminal object of $\mathbf{Abs}_P$ is isomorphic to $\Phi$ by a unique isomorphism;
   682	\item for each $G\in\mathcal{G}_*$, the representing structure $F_G$ is unique up to isomorphism: if $G\cong_AF$ and $G\cong_AF'$ with $F,F'\in\mathcal{F}$, then $F$ and $F'$ are isomorphic.
   683	\end{enumerate}
   684	\end{theorem}
   685	
   686	\begin{proof}
   687	(a) By \cref{thm:formalized-state:representation}(b), $\pi(G)\in\mathcal{F}$ for every $G\in\mathcal{G}_*$, so $\Phi$ is well defined, and it is surjective onto $\mathcal{F}_*$ by the definition of $\mathcal{F}_*$. $\Phi(G)=\Phi(G')$ means $[\pi(G)]=[\pi(G')]$, which is $P(G)=P(G')$, which is $G\cong_AG'$. In particular $\Phi(G)=\Phi(G')$ implies $P(G)=P(G')$, so $\Phi$ is $P$-preserving.
   688	
   689	(b) Let $\alpha$ be $P$-preserving. Define $h:S_\alpha\to\mathcal{F}_*$ by $h(\alpha(G))=\Phi(G)$. The definition does not depend on the choice of $G$: if $\alpha(G)=\alpha(G')$, then $P(G)=P(G')$ because $\alpha$ is $P$-preserving, and so $\Phi(G)=\Phi(G')$ by (a). Every point of $S_\alpha$ has the form $\alpha(G)$, so $h$ is defined on all of $S_\alpha$, and $h\circ\alpha=\Phi$ by construction. Any morphism $h':\alpha\to\Phi$ satisfies $h'(\alpha(G))=\Phi(G)=h(\alpha(G))$ for every $G$, so $h'=h$. The partition of $\mathcal{G}_*$ induced by $\alpha$ therefore refines the one induced by $\Phi$, which is the partition into $\cong_A$-classes; no $P$-preserving abstraction is coarser.
   690	
   691	(c) Let $\Psi$ be terminal in $\mathbf{Abs}_P$. Terminality of $\Phi$ gives a unique morphism $f:\Psi\to\Phi$, and terminality of $\Psi$ gives a unique morphism $g:\Phi\to\Psi$. Then $f\circ g$ is a morphism $\Phi\to\Phi$, and the identity is another; terminality of $\Phi$ allows only one, so $f\circ g=\mathrm{id}$. In the same way $g\circ f=\mathrm{id}$ on $\Psi$. So $f$ is an isomorphism, and it is the only morphism $\Psi\to\Phi$, hence the only isomorphism.
   692	
   693	(d) A relation $G\cong_AF$ is a bijection $\beta:V_G\to V_F$ carrying $\pi(G)$ to $F$, and $G\cong_AF'$ is a bijection $\beta'$ carrying $\pi(G)$ to $F'$. The bijection $\beta'\circ\beta^{-1}:V_F\to V_{F'}$ carries every component of $F$ to the corresponding component of $F'$, so $F$ and $F'$ are isomorphic.
   694	\end{proof}
   695	
   696	\begin{theorem}[Six dimensions]
   697	\label{thm:formalized-state:six}
   698	Relative to the same axioms and the same $P$, let $(c,\lambda)$ be a coarsening. The abstraction $\Phi_c$ is $P$-preserving if and only if $c$ is a bijection from $\Mset$ onto $K$. Every $P$-preserving coarsening $\Phi_c$ therefore has exactly $|K|=6$ dimensions, in a bijection with $\{\pF,\pP,\pJ,\pI,\pC,\pW\}$ that is unique up to relabeling of the dimensions, and it is isomorphic to $\Phi$ in $\mathbf{Abs}_P$.
   699	\end{theorem}
   700	
   701	\begin{proof}
   702	If $c$ is not a bijection onto $K$, \cref{prop:formalized-state:minimality6} gives $G_1,G_2$ with $\Phi_c(G_1)=\Phi_c(G_2)$ and $P(G_1)\neq P(G_2)$, so $\Phi_c$ is not $P$-preserving. If $c$ is a bijection, every block is a single pillar with weight one, so $\Phi_c(G)$ is $\pi(G)$ with its pillar labels renamed by $c$, up to relabeling of actors; $\Phi_c(G)=\Phi_c(G')$ holds exactly when $\Phi(G)=\Phi(G')$, so $\Phi_c$ is $P$-preserving, and the renaming is a bijection $h$ with $h\circ\Phi=\Phi_c$, an isomorphism in $\mathbf{Abs}_P$. A bijection from a six-element set onto $K$ forces $|K|=6$. Two such bijections $c,c'$ differ by the bijection $c'\circ c^{-1}$ of $K$, which is a relabeling of the dimensions.
   703	\end{proof}
   704	
   705	\begin{remark}[Scope of uniqueness]
   706	\label{rem:formalized-state:scope}
   707	Uniqueness is the universal property of \cref{thm:formalized-state:uniqueness} together with the count of \cref{thm:formalized-state:six}. Both are relative to the axioms and to the preserved property set $P$. A different choice of $P$, for instance one that also kept the content of legitimating beliefs, would yield a different abstraction, which would again be unique for its own $P$ by the same argument. \Cref{thm:formalized-state:six} concerns coarsenings, whose blocks aggregate pillar data with the weights $\lambda$; an abstraction that groups pillars but keeps each pillar's components separately is $\Phi$ relabeled and is not a coarsening; an abstraction that splits a class, such as coercion into policing and war making, is $P$-preserving and factors through $\Phi$ by \cref{thm:formalized-state:uniqueness}(b), so it is finer and not minimal.
   708	\end{remark}
   709	
   710	The universal property is close to the definition of $P$, and that is its point: once the properties to be preserved are fixed, the coarsest abstraction preserving them is determined up to unique isomorphism. The substantive content lies elsewhere. \Cref{thm:formalized-state:representation} shows that the coarsest abstraction lands in the class $\mathcal{F}$ of six-layer structures with an interdependent dependency hypergraph, which requires necessity, and \cref{thm:formalized-state:six} shows that its six dimensions cannot be reduced or merged, which requires the explicit witnesses of \cref{prop:formalized-state:minimality6}.
   711	
   712	\section{Capture tendencies and checks}
   713	\label{sec:tendencies}
   714	
   715	\subsection{Conditional capture axioms}
   716	
   717	Capture is contingent, but it is not random. Three mechanisms recur in the literature on oligarchy and rent seeking, and each can be stated as a conditional axiom.
   718	
   719	\begin{assumption}[T1, delegation]
   720	\label{ass:formalized-state:T1}
   721	In an organization that holds control in some pillar, a leadership extracts a rent, and members can monitor it only at private cost, as in Assumption 6.1 of Part II.
   722	\end{assumption}
   723	
   724	Under T1, Proposition 6.2 of Part II shows that monitoring by members vanishes once the organization is large enough, so the leadership is never replaced, while an organized opposition faction that monitors replaces it with a probability that does not depend on size. This is the mechanism behind Michels's iron law of oligarchy \citep{michels1915}, and its exceptions are the cases in which an organized opposition survived: the internal party system of the typographers' union that \citet{lipset1956} studied, and the revitalized unions in which \citet{voss2000} found the iron law broken. \Citet{cassinelli1953} had already argued that the law is a tendency with conditions rather than a law.
   725	
   726	\begin{assumption}[T2, organization asymmetry]
   727	\label{ass:formalized-state:T2}
   728	Coalitions with concentrated stakes organize at lower cost per member than coalitions with diffuse stakes, so their rate of converting control in one pillar into control in another is higher.
   729	\end{assumption}
   730	
   731	T2 is the logic of collective action of \citet{olson1965} applied across pillars, and the economic theory of regulation of \citet{stigler1971} applied to rule making. Mosca's observation that an organized minority prevails over an unorganized majority is an older statement of the same asymmetry \citep{mosca1939}.
   732	
   733	\begin{assumption}[T3, conversion against contestability]
   734	\label{ass:formalized-state:T3}
   735	A coalition's control in pillar $m$ converts into control in pillar $n$ at a rate $\eta_{nm}(1-Q_n)$ with $\eta_{nm}\ge0$, so contestability in the target pillar blocks conversion in proportion.
   736	\end{assumption}
   737	
   738	For $m=\pF$ the empirical counterpart of $\eta_{nm}$ is the conversion elasticity of Definition 6.1 of Part I. Walzer called the conversion of dominance in one sphere into dominance in another the defining mark of tyranny \citep{walzer1983}, and T3 states the condition under which conversion is checked: the source's second proposition, that independent review and voice interrupt transmission \citep{largo2026hbs}.
   739	
   740	\subsection{Conversion dynamics}
   741	
   742	\begin{definition}[Conversion dynamics]
   743	\label{def:formalized-state:conversion}
   744	Fix a coalition $S$ and let $y_t\in[0,1]^M$ collect its control shares $y_{m,t}=\kappa_m(S)$ at date $t$. Let $\delta\in[0,1]^M$ be the rates at which the coalition loses control in each pillar through replacement, turnover or exit, and let $K\ge0$ be an $M\times M$ matrix with zero diagonal, row sums at most one, and entries $K_{nm}=\eta_{nm}(1-Q_n)$. The coalition's shares follow
   745	\[
   746	y_{n,t+1}=(1-\delta_n)\,y_{n,t}+(1-y_{n,t})\,(Ky_t)_n .
   747	\]
   748	Write $A=\operatorname{diag}(1-\delta)+K$ and $\Integ(S)_t=\frac{1}{15}\sum_{m<n}\min\{y_{m,t},y_{n,t}\}$, the coalition's contribution to integration, which is a lower bound on $\Integ_t$ by \cref{def:formalized-state:overlap}.
   749	\end{definition}
   750	

2026-10-22T19:05:03.423515Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '750,1000p' papers/latex/formalized-state.tex | nl -ba -v750" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   750	
   751	\begin{theorem}[Closure and reversibility]
   752	\label{thm:formalized-state:conversion}
   753	Under \cref{def:formalized-state:conversion}:
   754	\begin{enumerate}[label=(\alph*)]
   755	\item the dynamics map $[0,1]^M$ into itself, and $y_{t+1}\le Ay_t$ componentwise;
   756	\item if the spectral radius satisfies $\rho(A)<1$, then $y_t\to0$ and $\Integ(S)_t\to0$ geometrically from every initial state, so every foothold of the coalition is reversible;
   757	\item if $Q_n=1$ and $\delta_n>0$ for some pillar $n$, then $y_{n,t}=(1-\delta_n)^ty_{n,0}$, every pair containing $n$ contributes nothing in the limit, and $\limsup_t\Integ(S)_t\le10/15$;
   758	\item if $\delta_n=0$ for some pillar $n$, then $y_{n,t}$ is nondecreasing, so a foothold in $n$ never decays, and $\rho(A)\ge1$;
   759	\item $\rho(A)$ is nonincreasing in each $Q_n$;
   760	\item if $K$ is irreducible, $\max_n\delta_n<1$ and $\rho(A)>1$, let $v>0$ be the left Perron vector of $A$, $\bar\kappa$ the largest column sum of $K$, and $c=\bar\kappa\max_nv_n/(\min_nv_n)^2$. Then for every $y_0\neq0$ and every $t$,
   761	\[
   762	v^{\top}y_t\ \ge\ \min\Bigl\{v^{\top}y_0,\ (1-\max_n\delta_n)\frac{\rho(A)-1}{2c}\Bigr\}>0,
   763	\]
   764	so the coalition's foothold never vanishes.
   765	\end{enumerate}
   766	\end{theorem}
   767	
   768	\begin{proof}
   769	(a) If $y\in[0,1]^M$ then $(Ky)_n\in[0,1]$ because $K\ge0$ has row sums at most one. Hence $y_{n,t+1}\ge0$, and $y_{n,t+1}\le(1-\delta_n)y_{n,t}+1-y_{n,t}=1-\delta_ny_{n,t}\le1$. Since $1-y_{n,t}\le1$ and $(Ky_t)_n\ge0$, $y_{n,t+1}\le(1-\delta_n)y_{n,t}+(Ky_t)_n=(Ay_t)_n$.
   770	
   771	(b) $A\ge0$, so $z\le z'$ implies $Az\le Az'$, and induction on (a) gives $0\le y_t\le A^ty_0$. When $\rho(A)<1$, for any $r\in(\rho(A),1)$ there is a constant $b$ with $\|A^t\|\le br^t$ for all $t$, so $y_t\to0$ geometrically, and $\Integ(S)_t\le\max_my_{m,t}$ does too.
   772	
   773	(c) $Q_n=1$ makes row $n$ of $K$ zero, so $y_{n,t+1}=(1-\delta_n)y_{n,t}$. Each of the five pairs containing $n$ contributes at most $y_{n,t}\to0$, and the other ten contribute at most one each.
   774	
   775	(d) With $\delta_n=0$, $y_{n,t+1}-y_{n,t}=(1-y_{n,t})(Ky_t)_n\ge0$. Since $A\ge\operatorname{diag}(1-\delta)\ge0$ entrywise and the spectral radius is monotone on nonnegative matrices \citep{horn2012}, $\rho(A)\ge\max_n(1-\delta_n)=1$.
   776	
   777	(e) Raising $Q_n$ lowers or leaves unchanged every entry of row $n$ of $K$, hence of $A$, and monotonicity of the spectral radius applies.
   778	
   779	(f) By the Perron-Frobenius theorem for irreducible nonnegative matrices \citep{horn2012}, $\rho=\rho(A)$ has a left eigenvector $v$ with positive entries. Write $V_t=v^{\top}y_t$, which is positive when $y_t\neq0$. From the dynamics,
   780	\[
   781	V_{t+1}=v^{\top}Ay_t-\sum_nv_ny_{n,t}(Ky_t)_n=\rho V_t-\sum_nv_ny_{n,t}(Ky_t)_n .
   782	\]
   783	The subtracted sum is at most $\max_nv_n\cdot\max_ny_{n,t}\cdot\sum_n(Ky_t)_n\le\max_nv_n\cdot\|y_t\|_1\cdot\bar\kappa\|y_t\|_1$, and $\|y_t\|_1\le V_t/\min_nv_n$, so it is at most $cV_t^2$. Irreducibility with $M\ge2$ gives $K\neq0$, so $c>0$. Let $\varepsilon=(\rho-1)/(2c)$. If $V_t\le\varepsilon$ then $V_{t+1}\ge V_t(\rho-cV_t)\ge V_t(\rho+1)/2\ge V_t$. In every case $V_{t+1}\ge v^{\top}\operatorname{diag}(1-\delta)y_t\ge(1-\max_n\delta_n)V_t$, because the term $(1-y_t)\circ Ky_t$ is nonnegative. Let $\mu$ be the right side of the displayed bound and suppose $V_t\ge\mu$. If $V_t\le\varepsilon$ then $V_{t+1}\ge V_t\ge\mu$; if $V_t>\varepsilon$ then $V_{t+1}\ge(1-\max_n\delta_n)\varepsilon\ge\mu$. Since $V_0\ge\mu$, induction gives $V_t\ge\mu$ for all $t$.
   784	\end{proof}
   785	
   786	The theorem gives the source's vocabulary of closure and reversibility a precise meaning. Capture is reversible when the replacement rates outrun the conversion rates in the sense that $\rho(A)<1$, and closed when conversion along a strongly connected set of channels outruns replacement. Part (c) is a formal version of the source's second proposition: full contestability in one pillar with any positive replacement rate in it caps a coalition's integration at two thirds, whatever happens in the other five. Part (d) states the cost of entrenchment: a pillar in which the coalition cannot be replaced holds every foothold it gains.
   787	
   788	\begin{corollary}[Oligarchy and replacement]
   789	\label{cor:formalized-state:michels}
   790	Under T1, if the organization that holds the coalition's control in pillar $n$ is larger than the threshold of Proposition 6.2(a) of Part II and faces no organized opposition, then its leadership is never replaced, $\delta_n=0$ for the leadership's control, and by \cref{thm:formalized-state:conversion}(d) its foothold in $n$ never decays. An organized opposition faction that monitors, as in Proposition 6.2(b) of Part II, makes the replacement probability positive and independent of size. Reversibility in the sense of \cref{thm:formalized-state:conversion}(b) requires a positive replacement rate in every pillar.
   791	\end{corollary}
   792	
   793	\begin{proof}
   794	The first two statements are Proposition 6.2 of Part II read as statements about $\delta_n$. The last follows from \cref{thm:formalized-state:conversion}(d): if $\delta_n=0$ then $y_{n,t}\ge y_{n,0}$ for all $t$, so $y_t\not\to0$ from any initial state with $y_{n,0}>0$.
   795	\end{proof}
   796	
   797	The corollary connects the oldest theory of capture with the checks that interrupt it. Organized opposition, contested elections, term limits, judicial tenure that does not depend on the coalition, and the exit of members all raise replacement rates. Disclosure, independent review, open entry and protected speech raise contestability and lower conversion rates. The first family acts on the diagonal of $A$ and the second on its off-diagonal entries. Neither family alone guarantees reversibility, and by part (c) a single pillar that has both caps integration.
   798	
   799	\subsection{Pillar-capacity dynamics}
   800	
   801	The source's aggregate dynamics $x_{t+1}=B_tx_t+D_tz_t+\varepsilon_t$ describe capacities rather than coalition shares, and the source warns that stability cannot be read off positive links \citep{largo2026hbs}. Interdependence says something about the shape of the dominant mode, and nothing about its size.
   802	
   803	\begin{proposition}[Common mode under interdependence]
   804	\label{prop:formalized-state:perron}
   805	Let $B_t=B\ge0$ for all $t$, and suppose $B_{mn}>0$ whenever $n\to m$ is an arc of the underlying digraph of $\Dstar$. Under the hypotheses of \cref{thm:formalized-state:interdependence}, $B$ is irreducible, and $\rho(B)$ is a simple eigenvalue of $B$ with an eigenvector $u$ whose entries are all positive. If, in addition, some diagonal entry of $B$ is positive, then with $D_tz_t+\varepsilon_t=0$ and $w$ the positive left eigenvector normalized by $w^{\top}u=1$, $\rho(B)^{-t}x_t\to u\,w^{\top}x_0$ for every $x_0$.
   806	\end{proposition}
   807	
   808	\begin{proof}
   809	A nonnegative matrix is irreducible if and only if the digraph of its positive entries is strongly connected, and that digraph contains the underlying digraph of $\Dstar$, which is strongly connected by \cref{thm:formalized-state:interdependence}. The Perron-Frobenius theorem gives the simple eigenvalue and positive eigenvector. An irreducible nonnegative matrix with a positive diagonal entry is primitive, and for primitive matrices $(B/\rho(B))^t\to uw^{\top}$ \citep{horn2012}.
   810	\end{proof}
   811	
   812	Under interdependence and positive linear dependencies, no pillar's capacity can grow indefinitely faster than the others: all six share one long-run rate and one profile $u$. The proposition says nothing about whether that rate exceeds one, and its hypothesis of nonnegative dependencies is exactly what the source doubts.
   813	
   814	\begin{remark}[Positive links do not settle stability]
   815	\label{rem:formalized-state:sign}
   816	Matrices with the same positive entries can have spectral radii on opposite sides of one. The circulant matrices with first rows $(0.6,0.45,0)$ and $(0.6,0.45,-0.45)$ share their positive entries; their eigenvalues are $a+b\omega^k+c\omega^{2k}$ with $\omega=e^{2\pi i/3}$, which gives spectral radius $1.05$ for the first and $|0.6\pm0.45\,i\sqrt3|=\sqrt{0.9675}\approx0.984$ for the second. The negative entries are feedback of the kind the source lists, such as legitimacy lost through coercion, and a model that records only who depends on whom cannot tell a self-reinforcing hierarchy from a self-correcting one.
   817	\end{remark}
   818	
   819	\subsection{Testable implications}
   820	
   821	\Cref{tab:hypotheses} states the hypotheses at the level of this Part, each with the source hypothesis it refines and an observation that would refute it. The comparative evidence of Parts I to VI is qualitative and drawn from the historical record; each hypothesis states the quantitative test that would confirm or refute it. The hypotheses inherit the source's six, H1 to H6, and add two that only the series can state: that the role map is complete in every coded polity (A1, a test of the representation theorem) and that its completeness is unrelated to the indices of capture (A2).
   822	
   823	\begin{table}[!htbp]
   824	\centering
   825	\small
   826	\caption{Hypotheses at the level of the series, with the source hypothesis each refines and a falsifier. Codings must be preregistered and include negative cases.}
   827	\label{tab:hypotheses}
   828	\begin{tabularx}{\textwidth}{@{}L{0.6cm}YL{1.9cm}Y@{}}
   829	\toprule
   830	 & Hypothesis & Parent & Falsifier \\
   831	\midrule
   832	A1 & No persistent collective in the record lacks any of the six functions in some form & None & A documented persistent collective without one function \\
   833	A2 & The six functions are realized in every coded polity while $U_t$ and $\Integ_t$ vary widely & Proposition 1 & Indices that are collinear with features of the role map \\
   834	B1 & Preferential rules survive adverse disclosure longer where $\Integ_t$ is high & H2 & No difference in survival after disclosure \\
   835	B2 & Raising contestability in one pillar lowers transmission through it & H1, H4 & Staggered reforms with no change in transmission \\
   836	B3 & Dispersing control in one pillar without reducing cross-pillar overlap leaves preferential rules intact & H2 & Dispersal alone ends preferential rules \\
   837	B4 & Organizations without organized opposition keep their leaderships longer & H1 & Equal leadership turnover with and without opposition \\
   838	B5 & $U_t$ and service quality are not monotonically related & H6 & A monotone decline of service quality in $U_t$ \\
   839	\bottomrule
   840	\end{tabularx}
   841	\end{table}
   842	
   843	\section{Regime profiles}
   844	\label{sec:regimes}
   845	
   846	\subsection{The profile of a regime type}
   847	
   848	The six regime types are implementations of the Formalized State. Every one is represented by a structure in $\mathcal{F}$ (\cref{thm:formalized-state:representation}), so a comparison cannot ask whether a type has the structure; it asks how the structure is implemented. A \emph{regime profile} records the pattern of integration, either a star around a hub pillar or a clique commanded by one coalition (\cref{lem:formalized-state:hub}); the characteristic control path, the direction in which control is converted (source Proposition 3); the checks that raise replacement rates or contestability (\cref{thm:formalized-state:conversion}); and documented episodes of capture and of binding checks. The profiles synthesize the comparative sections of Parts I to VI. They are hypotheses about where a preregistered coding would find integration, not coded values.
   849	
   850	\subsection{Market capitalism}
   851	
   852	Private owners, banks and corporations hold the resource pillar alongside a public budget and a central bank (Part I, Section 5). The hypothesized pattern is a star around $\pF$: resources couple to rule making through donations and lobbying, to legitimation through media ownership and research sponsorship, to interpretation through repeat-player advantages, and to production because capital allocation and employment are held by the same actors (Parts I, II, III and VI, Section 5). The control path runs from wealth to rules \citep{largo2026hbs}. Competing firms and sectors make different coalitions on different spokes likely, the pluralist reading \citep{dahl1961}, and by \cref{lem:formalized-state:hub}(b) a pure star cannot raise $\Integ_t$ above one third of its largest coupling. Documented checks include competing interest groups, antitrust, disclosure and elections (Part II, Section 5), and a recusal ruling of the United States Supreme Court that addressed a capture risk created by campaign spending in a judicial election (Part III, Section 5).
   853	
   854	\subsection{Communist party-states}
   855	
   856	The ruling party appoints office holders in every pillar through nomenklatura lists, which the partisan \'emigr\'e account of \citet{voslensky1984} treated as the basis of a ruling class. Rule making is the hub, and the control path runs from appointment to allocation and enforcement, the reverse of the market path \citep{largo2026hbs}. Because one coalition appoints in five pillars, the pattern is a clique: Proposition 6.5 of Part II bounds each coupling below, and \cref{lem:formalized-state:hub}(c) bounds $\Integ_t$ below by two thirds of the party's smallest command share across the five pillars. The checks lie inside the coalition, in elite divisions \citep{lane1995} and bureaucratic bargaining \citep{hough1979}. Documented episodes include courts that followed campaign directives under Stalin and the terror of the late 1930s, and, as checks, party supremacy over the military and a later rise in legality in ordinary cases (Parts III and V, Section 5).
   857	
   858	\subsection{Social democracy and democratic socialism}
   859	
   860	The hypothesized pattern is a triangle of rule making, resources and production, joined by bargaining among the peak organizations of labor and capital and the state (Parts I, II and VI, Section 5). At least two coalitions, labor and capital, each command part of each pillar, so the overlap measure gives moderate couplings even where bargaining is encompassing. Contestability is high: governments alternate, unions give workers voice, and transparency norms are strong. The documented risk is closure to unorganized interests (Part II, Section 5). The \emph{Langborger} ruling held that labor courts whose lay members are nominated by interested organizations can fail the test of impartiality (Part III, Section 5), and official inquiries into political surveillance by security services led to standing parliamentary oversight (Part V, Section 5). The source's fourth proposition, that public benefit is compatible with hierarchy, applies here with particular force \citep{largo2026hbs}.
   861	
   862	\subsection{Islamic states}
   863	
   864	Islamic states derive legitimacy from religious law, and classical caliphates, the Ottoman empire, modern Iran and Saudi Arabia differ in almost every coupling (Parts II, III and IV, Section 5). In Hallaq's account of classical practice, rulers appointed qadis while jurists who were not state officials developed the law \citep{hallaq2009}, which kept much of $\pJ$ and $\pI$ outside the ruler's coalition. Why the Middle East fell behind Western Europe economically is disputed: \citet{kuran2011} points to features of Islamic law, and \citet{rubin2017} to the bargains through which religious authorities legitimated rulers. The Ottoman empire governed through brokerage among several coalitions \citep{barkey2008}. Modern Iran shows a clique around clerical authority: the Guardian Council screens legislation and candidates, and the revolutionary guards couple coercion to resources (Parts I, II and V, Section 5). Saudi Arabia couples rule making to legitimation through the alliance of the royal family and the religious establishment, and to resources through oil rents (Part I, Section 5; \citealt{ross2012}). The checks include juristic pluralism, endowed revenue, elections in Iran and brokered rule. Capture varies with the state and the period, not with the religion.
   865	
   866	\subsection{Historical Catholic monarchies}
   867	
   868	Habsburg Spain, Bourbon France and the Papal States intertwined royal authority with the Church, and their diversity matches that of the Islamic cases. The hypothesized pattern couples rule making to legitimation through royal influence over Church appointments, resources to interpretation through venal judicial office, and resources to coercion through the fiscal-military state (Parts I, II, III and V, Section 5; \citealt{tilly1990,ertman1997}). In the Papal States the fusion of rule making and legitimation was complete (Part IV, Section 5). Brokerage limited the crown: Beik describes absolutism in Languedoc as collaboration with provincial elites rather than command \citep{beik1985}. Checks included the estates and Cortes, competing jurisdictions and conflict between Church and crown. The chancellor Maupeou's suppression of the parlements in 1771 removed a check, and its reversal in 1774 restored it (Part III, Section 5). In the terms of \cref{thm:formalized-state:conversion}, venality raised the conversion rate from $\pF$ to $\pJ$, while the parlements' tenure kept the replacement rate in $\pJ$ out of the crown's hands.
   869	
   870	\subsection{Secular democracies}
   871	
   872	Authority is distributed among elected officials, courts and private institutions, and contestability is designed to be high on every component (Parts II and V, Section 5). Couplings are low overall, with two characteristic channels: appointments to courts, with constitutional review that can act as co-legislation \citep{hirschl2004}, and delegation to independent central banks, regulators and courts whose accountability runs through review rather than election (Parts I and III, Section 5). The documented risks are erosion of contestability by incumbents and capture of the bodies that review them: the enlargement of the Argentine Supreme Court in 1990 produced a court aligned with the government (Part III, Section 5), and surveillance of citizens exposed by the United States Senate inquiry of 1975 and 1976 was both a capture episode and a check (Part V, Section 5). Rival institutions, a free press and citizens' coordination against transgressions by the state, which \citet{weingast1997} identified as the foundation of self-enforcing limits on government, are the checks.
   873	
   874	\subsection{What the classification shows}
   875	
   876	\Cref{tab:regimes} summarizes the profiles. Every row satisfies $\Struct$ and $\Inter$ and has the same dependency structure, because that structure is a function of the problems a collective faces, not of who solves them (\cref{lem:formalized-state:separation}). The rows differ in the pattern of integration, and the star and clique bounds of \cref{lem:formalized-state:hub} explain why market and party-state profiles with similar maximal couplings can differ sharply in $\Integ_t$. Every row records both capture episodes and binding checks, so the regime type does not settle whether a polity is captured; that requires coding a polity in a period, with preregistered weights, thresholds and coalition lists.
   877	
   878	\begin{table}[!htbp]
   879	\centering
   880	\small
   881	\caption{Regime profiles. Patterns and paths are drawn from the comparative sections of Parts I to VI.}
   882	\label{tab:regimes}
   883	\begin{tabularx}{\textwidth}{@{}L{2.2cm}YYY@{}}
   884	\toprule
   885	Regime type & Hypothesized integration pattern & Characteristic control path & Principal checks \\
   886	\midrule
   887	Market capitalism & A star around resources, with different coalitions on different spokes & From wealth to rules, legitimation and interpretation & Competition among interests, antitrust, disclosure, elections and courts \\
   888	Communist party-state & A clique of five pillars under the ruling party & From appointment to allocation and enforcement & Elite divisions, bureaucratic bargaining and the loyalty limit on appointment \\
   889	Social democracy & A triangle of rule making, resources and production joined by bargaining & From organized bargaining to rules and terms of work & Elections, organized labor, ombudsmen and parliamentary oversight \\
   890	Islamic states & Plural in classical practice and a clique around clerical authority in modern Iran & From religious-legal authority to rules and adjudication, and from rents to rule & Juristic pluralism, endowed revenue, brokerage and elections in Iran \\
   891	Catholic monarchies & Couplings of crown and Church, of money and justice, and of money and force & From fiscal need to venal office and from Church patronage to legitimation & Parlements, estates and Cortes, competing jurisdictions and Church-crown conflict \\
   892	Secular democracies & Low couplings, with appointment to courts and delegation to technical bodies & From rule making to interpretation through appointment & Rival institutions, free press, review bodies and citizen coordination \\
   893	\bottomrule
   894	\end{tabularx}
   895	\end{table}
   896	
   897	\section{Predecessors and novelty}
   898	\label{sec:literature}
   899	
   900	\subsection{The canon}
   901	
   902	Earlier answers to the question of what every polity must contain are of three kinds: typologies of rulers and of legitimacy, lists of functions, and derivations from premises. The typologies classify polities along axes other than the six functions. Aristotle classified constitutions by whether one, a few or many rule and whether they rule for the common interest or their own, and distinguished the deliberative, magisterial and judicial elements of a constitution \citep{aristotle1996}. Weber classified domination by the belief in its legitimacy, traditional, charismatic or legal-rational, and by the administrative staff that executes it \citep{weber1978}.
   903	
   904	The lists of functions are the closest relatives. Parsons named four functional prerequisites of any social system, adaptation, goal attainment, integration and latent pattern maintenance \citep{parsons1951}, and \citet{aberle1950} gave a longer list. Easton described the political system as converting inputs of demands and supports into authoritative outputs \citep{easton1965}. Almond divided political functions into input functions, among them socialization, interest articulation, interest aggregation and communication, and output functions, rule making, rule application and rule adjudication \citep{almond1960}. Luhmann described modern society as differentiated into functional subsystems, among them the economy, politics, law, science, religion and the mass media \citep{luhmann1995}. Mann treated societies as overlapping networks of ideological, economic, military and political power, none of them primary \citep{mann1986,mann1993}. These lists were criticized for defining prerequisites by what persisting societies happen to have \citep{hempel1959,elster1983}.
   905	
   906	The derivations are the model for the method. Hobbes derived the sovereign from the premise that agreements without a power to enforce them do not hold \citep{hobbes1651}; Part V accepts the premise and derives a sanctioning function rather than a sovereign. Arrow's impossibility theorem derives a sharp result about collective decisions from short axioms \citep{arrow1951}; it concerns aggregation rather than the structure of governance, and the rule-making function of Part II begins where it leaves off, since a collective must choose some procedure although none satisfies every desirable condition.
   907	
   908	The lists differ from the six pillars at exactly the points the formal results test. Mann's economic source and Parsons's adaptation join the command of resources with the production of wealth, which the latent veto (Proposition 3.6 of Part VI) and relocation (Lemma 3.4 of Part VI) separate; Mann's political source joins rule making with adjudication, which the disjunctive dependency of Proposition 3.6 of Part III separates. Mann's distinction between the despotic power of elites and the infrastructural power of states \citep{mann1984} corresponds to the distinction between $U_t$ and the capacity vector $x_t$, and his historical account of how particular networks emerged is something no axiomatic treatment replaces.
   909	
   910	Two further literatures address the other side of the thesis. The theory of capture, from Michels \citep{michels1915} through Stigler \citep{stigler1971}, state capture \citep{hellman2000}, extractive institutions \citep{acemoglu2006,acemoglu2019} and limited-access orders \citep{nww2009}, explains when capture arises, which is Proposition B, and does not state what every polity must contain. Normative theory supplies readings of the indices: the separation of powers of Montesquieu and Madison covers two pillars and part of a third \citep{montesquieu1989,madison1788}, and Walzer's spheres and Pettit's non-domination give normative content to $C_{mn}$ and $Q_m$ \citep{walzer1983,pettit1997}.
   911	
   912	\subsection{Non-equivalence}
   913	
   914	Each predecessor can be encoded as an abstraction on $\mathcal{G}_*$, and the encodings can be compared with $\Phi$ in $\mathbf{Abs}_P$. Five are coarsenings in the sense of \cref{sec:representation}, with equal weights within each block. Parsons: adaptation $=\{\pF,\pW\}$, goal attainment $=\{\pP\}$, integration $=\{\pJ,\pC\}$, latent pattern maintenance $=\{\pI\}$ \citep{parsons1951}; whether coercion belongs to goal attainment or to integration is contestable, and the choice does not affect the argument. Mann: ideological $=\{\pI\}$, economic $=\{\pF,\pW\}$, military $=\{\pC\}$, political $=\{\pP,\pJ\}$ \citep{mann1986}. Easton: inputs $=\{\pI,\pW\}$, outputs $=\{\pF,\pP,\pJ,\pC\}$ \citep{easton1965}; the assignment of production to inputs, as the source of supports, is contestable. Almond: rule making $=\{\pP\}$, rule application $=\{\pC\}$, rule adjudication $=\{\pJ\}$, inputs $=\{\pI\}$, with $\pF$ and $\pW$ dropped because his functions are those of the political system \citep{almond1960}; placing administration with coercion is contestable. Luhmann: economy $=\{\pF,\pW\}$, politics $=\{\pP,\pC\}$, law $=\{\pJ\}$, and one block for the communicative subsystems $=\{\pI\}$ \citep{luhmann1995}; Luhmann splits that block further, which the argument does not need. These encodings are readings of the 1960 and 1995 partitions: Almond and Powell later added system capabilities, among them extractive, regulative and distributive ones, that touch $\pF$ \citep{almond1966}, and Luhmann's subsystems are codes of communication rather than layers of actors. The other two are typologies. Aristotle's encoding returns the number of rulers, one if a single actor has a positive share of rule making, few if between two and half the members do, many otherwise, and the aim, deviant if a capture link is documented and correct otherwise \citep{aristotle1996}; the thresholds are a choice. Weber's encoding returns the coded type of legitimation and whether an administrative staff exists \citep{weber1978}.
   915	
   916	\begin{proposition}[Witnesses]
   917	\label{prop:formalized-state:witnesses}
   918	For each encoding $\alpha_k$ above there are $G,G'\in\mathcal{G}_*$ with $\alpha_k(G)=\alpha_k(G')$ and $P(G)\neq P(G')$:
   919	\begin{enumerate}[label=(\alph*)]
   920	\item Parsons, Mann and Luhmann merge $\pF$ and $\pW$, and Mann and Easton merge $\pP$ and $\pJ$; the pair of \cref{prop:formalized-state:minimality6}(b) for the merged pair, with $\mu=1/2$, has $C^{\ov}$ equal to $0$ against $1/2$ and $H$ equal to $1$ against $1/2$ in each merged pillar;
   921	\item Almond drops $\pF$; the pair of \cref{prop:formalized-state:minimality6}(a) with $m=\pF$ and $l_0=\pP$ has $H_{\pF}=1$ against $1/2$;
   922	\item Aristotle: two collectives with the same rule-making layer and no capture link, in which interpretation is held by one organization ($s^{\pJ}=(1,0)$ on $(a,b)$, $H_{\pJ}=1$) or by two equally ($s^{\pJ}=(1/2,1/2)$, $H_{\pJ}=1/2$), with $a$ and $b$ holding equal shares in $\pI$ in both;
   923	\item Weber: two collectives coded as legal-rational with an administrative staff, in which coercion is held by one organization ($s^{\pC}=(1,0)$ on $(a,b)$, $H_{\pC}=1$) or by two equally ($H_{\pC}=1/2$), with $a$ and $b$ holding equal shares in $\pI$ in both.
   924	\end{enumerate}
   925	Hence no encoded predecessor is $P$-preserving, and none is isomorphic to $\Phi$ in $\mathbf{Abs}_P$.
   926	\end{proposition}
   927	
   928	\begin{proof}
   929	(a) and (b) are instances of \cref{prop:formalized-state:minimality6}, whose proof computes both $P$-values and shows the coarsened images equal for any weights. Easton's outputs block contains $\pF$, $\pC$ and the merged pair; the coarsened shares of the block are a weighted sum in which only the $\pP$ and $\pJ$ terms differ between the two collectives, and those terms sum to the same vector, as in the proof of \cref{prop:formalized-state:minimality6}(b). (c) The two collectives have the same actor set, since $b$ performs practices of $\pI$ in both. They have the same set of actors with positive rule-making share and the same empty set of capture links, so the encoding returns the same number of rulers and the same aim. Their $H_{\pJ}$ differ, and $H_{\pJ}$ is invariant under relabeling. Both assignments are admissible as in the proof of \cref{prop:formalized-state:minimality6}, so both lie in $\mathcal{G}_*$ by \cref{lem:formalized-state:separation}. (d) The actor sets coincide as in (c). The two collectives carry the same coded legitimation type and staff, so the encoding agrees; $H_{\pC}$ differs. For the last sentence: an abstraction isomorphic to $\Phi$ has the same partition of $\mathcal{G}_*$ as $\Phi$, which is the partition into $\cong_A$-classes, and is therefore $P$-preserving.
   930	\end{proof}
   931	
   932	The Weber encoding fails in the other direction too. Two collectives with the same profile can carry different legitimation types, since $P$ forgets the content of legitimating beliefs (\cref{lem:formalized-state:preserved}); so neither of Weber's typology and $\Phi$ factors through the other. Weber classifies what the Formalized State forgets, and the two are complements rather than rivals.
   933	
   934	\begin{theorem}[Novelty relative to the canon]
   935	\label{thm:formalized-state:novelty}
   936	For each of the encoded predecessors, Aristotle, Weber, Parsons, Easton, Almond, Luhmann and Mann, the encoding $\alpha_k$ is not isomorphic to $\Phi$ in $\mathbf{Abs}_P$, does not represent governance systems up to $\cong_A$, and is not the coarsest $P$-preserving abstraction. The Formalized State abstraction has all four properties: representation, necessity, minimality and uniqueness.
   937	\end{theorem}
   938	
   939	\begin{proof}
   940	By \cref{prop:formalized-state:witnesses}, each $\alpha_k$ identifies two systems that are not $\cong_A$-equivalent, so it does not represent systems up to $\cong_A$ and is not $P$-preserving. A terminal object of $\mathbf{Abs}_P$ is in particular an object of it, so $\alpha_k$ is neither terminal nor isomorphic to $\Phi$. The four properties of $\Phi$ are \cref{thm:formalized-state:representation}, \cref{thm:formalized-state:A,thm:formalized-state:interdependence}, \cref{prop:formalized-state:minimality6}, and \cref{thm:formalized-state:uniqueness,thm:formalized-state:six}.
   941	\end{proof}
   942	
   943	\begin{remark}[Scope of novelty]
   944	\label{rem:formalized-state:novelty-scope}
   945	The theorem covers the seven encoded predecessors and is relative to $P$: the predecessors were built to preserve other things, and failing to preserve $P$ is a difference, not a defect. For works outside the list, the novelty claim is that, to our knowledge, no prior work states and proves a representation theorem with derived necessity, minimality and uniqueness of this form.
   946	\end{remark}
   947	
   948	\Cref{tab:predecessors} summarizes the comparison. The columns record representation up to $\cong_A$ (R), necessity derived from premises that can be false (N), minimality among $P$-preserving coarsenings (M) and uniqueness as the coarsest $P$-preserving abstraction (U). For the predecessors the R, M and U entries follow from \cref{prop:formalized-state:witnesses}; the N entries record that none derives its list from stated axioms with falsifiers, which is a reading of the cited works rather than a theorem.
   949	
   950	\begin{table}[!htbp]
   951	\centering
   952	\small
   953	\caption{The Formalized State and the encoded predecessors. R, N, M and U are representation, derived necessity, minimality and uniqueness; the last column names the result that gives the pair of systems the encoding cannot tell apart.}
   954	\label{tab:predecessors}
   955	\footnotesize
   956	\setlength{\tabcolsep}{3.5pt}
   957	\begin{tabularx}{\textwidth}{@{}L{1.8cm}L{1.2cm}Ycccc L{2.7cm}@{}}
   958	\toprule
   959	Framework & Size & Encoding & R & N & M & U & Witness \\
   960	\midrule
   961	Formalized State & Six & The profile map & Yes & Yes & Yes & Yes & None \\
   962	Parsons & Four & Merges resources and production & No & No & No & No & \cref{prop:formalized-state:witnesses}(a) \\
   963	Mann & Four & Merges resources and production, and rule making and adjudication & No & No & No & No & \cref{prop:formalized-state:witnesses}(a) \\
   964	Easton & Two & Merges rule making and adjudication among outputs & No & No & No & No & \cref{prop:formalized-state:witnesses}(a) \\
   965	Almond & Seven & Drops resources and production & No & No & No & No & \cref{prop:formalized-state:witnesses}(b) \\
   966	Luhmann & Several & Merges resources and production in the economy & No & No & No & No & \cref{prop:formalized-state:witnesses}(a) \\
   967	Aristotle & Six types & Number of rulers and aim & No & No & No & No & \cref{prop:formalized-state:witnesses}(c) \\
   968	Weber & Three types & Legitimation type and staff & No & No & No & No & \cref{prop:formalized-state:witnesses}(d) \\
   969	\bottomrule
   970	\end{tabularx}
   971	\end{table}
   972	
   973	\section{Revelation 13 and 17 to 18}
   974	\label{sec:revelation}
   975	
   976	The series reads Revelation typologically. The beast is a recurring pattern of power that claims ultimate allegiance, and Babylon is the idolatrous city of every age. The reading does not identify any present-day government, party, institution, technology, payment system or person with the beast or its mark. Futurist identifications have a long record of failure \citep{mcginn1998,fuller1995,boyer1992}, and historicist identifications of the papacy or of any other institution with the beast belong to the history of polemic. The theological reading is the project's own and is offered as an interpretation, not as an exegetical result.
   977	
   978	The commentators agree that the beasts had a Roman referent, which the typological reading generalizes. Richard Bauckham reads Rome as the paradigm of the beast and the book's conflict as one between worship of the beast and faithful witness \citep{bauckham1993}, and he reads chapter 18 as an economic critique of Rome's trade \citep{bauckham1991}. Adela Yarbro Collins reads the book as a response to a crisis its audience perceived, working through catharsis \citep{collins1984}. Craig Koester's commentary places the beasts in the imperial politics and civic cults of Roman Asia \citep{koester2014}. J.\,Nelson Kraybill shows how participation in provincial commerce was bound up with the imperial cult \citep{kraybill1996}, and the archaeology of the imperial cult at Ephesus and the study of the cult as local civic practice give the image its setting \citep{friesen2001,price1984}.
   979	
   980	Read with the formal model, chapter 13 describes a single configuration in all six pillars. The dragon gives the first beast ``his power, and his seat, and great authority'' (Rev 13:2), and the onlookers ask ``Who is like unto the beast? who is able to make war with him?'' (Rev 13:4): rule and force held together. The second beast ``exerciseth all the power of the first beast before him, and causeth the earth and them which dwell therein to worship the first beast'' (Rev 13:12): legitimation in the service of rule. It gives life to an image that causes ``that as many as would not worship the image of the beast should be killed'' (Rev 13:15): sanction attached to allegiance, with no forum for those who refuse. And it causes all, ``both small and great, rich and poor, free and bond, to receive a mark in their right hand, or in their foreheads: And that no man might buy or sell, save he that had the mark'' (Rev 13:16 and 13:17) \citep{kjv}: participation in exchange and production made conditional on an allegiance test. In the vocabulary of \cref{sec:capture}, one coalition commands every pillar, contestability is zero, and integration is complete. The image is the corner $(1,1)$ of \cref{thm:formalized-state:nonimplication}, with every capture link documented in the text itself.
   981	
   982	Chapters 17 and 18 add the coalition and the market. The kings ``have one mind, and shall give their power and strength unto the beast'' (Rev 17:13), a coalition formed by delegation, which is the mechanism of T1. The waters on which the city sits ``are peoples, and multitudes, and nations, and tongues'' (Rev 17:15). The merchants ``are waxed rich through the abundance of her delicacies'' (Rev 18:3), they mourn because ``no man buyeth their merchandise any more'' (Rev 18:11), and the cargo list ends with ``slaves, and souls of men'' (Rev 18:13) \citep{kjv}. The text does not condemn commerce as such. It condemns a commerce whose merchants ``were the great men of the earth'' (Rev 18:23), an integration of resources and production with rule. Following the source, the series uses the language of bondage only in this disciplined and explicitly metaphorical sense, and distinguishes wage labor, taxation, serfdom and chattel slavery \citep{largo2026hbs}. The book's response is exit: ``Come out of her, my people'' (Rev 18:4). In \cref{thm:formalized-state:conversion}, exit is a replacement rate.
   983	
   984	The typology therefore fits the separation of the two propositions in a specific way. The text depicts the captured configuration, Proposition B at its limit, and it presupposes the functions of Proposition A: the book does not imagine a world without rule, judgment, worship, commerce or labor, but relocates them, as Part III observed of judgment. The series names the universal abstraction after the image of its worst instance. The name is the series' typological reading of the abstraction, not a conclusion of any theorem, and the normative warning attaches only to capture, which is a property of instances. The source makes the same distinction: the expression should be reserved for coercive and unaccountable coordination, and the theological image permits government that protects the vulnerable and expertise that corrects error \citep{largo2026hbs}. Walter Wink's reading of the biblical language of the powers as institutional structures that can become a domination system is a theological precedent for reading the image as a structure rather than a person \citep{wink1992}.
   985	
   986	\section{Objections and scope}
   987	\label{sec:objections}
   988	
   989	\emph{Proposition A is true by definition.} If the functions were defined so broadly that anything counts, the theorem would be empty. Each implementation predicate is a property of observable dispositions that can fail, and \cref{prop:formalized-state:independence}(b) exhibits persistent collectives in which each fails. The theorem excludes them from the real world only through its premises, and \cref{tab:falsifiers} states what observation would refute each premise.
   990	
   991	\emph{The argument is functionalist.} \Cref{thm:formalized-state:A} is a condition of persistence. It explains no institution by its effects, asserts no feedback from effects to causes, and allows any institution or none to perform a function. It is open to Hempel's objection only if read as an inference from a function to a particular institution, and it makes no such inference.
   992	
   993	\emph{The hazard premises are too strong.} Where unsettled conflict or abandoned disputes are harmless, the forcing argument gives nothing. The concession is real. Part III's exit proposition shows that adjudication can be thin where exit is free, and the immediate-return foragers that Woodburn described come closest to that condition \citep{woodburn1982}. The ethnographies of these societies still record talk-based mediation and leveling sanctions, so the functions are thin rather than absent, and the claim is narrowed to collectives in which some recurring class of residual disputes cannot be escaped by moving; a collective in which every residual dispute can be escaped at no cost falls outside the derivation, and Proposition 3.4 of Part III shows that such a collective can persist without determination.
   994	
   995	\emph{Interdependence rests on added premises.} It does, and \cref{prop:formalized-state:minimality}(a) shows that the six axioms alone do not yield it. Universal interdependence has the same logical status as the existence of the functions: a theorem from stated premises, made universal by the hypothesis that every functioning collective satisfies them. The premises can be refuted by observation. Universal interdependence would be falsified by a persistent collective in which production continued unchanged while every claim on its inputs went unsettled, which refutes X1 and removes the only arc into production; by one whose allocation rules survived a change of environment that created claims they could not settle, which refutes X2; by one whose allocation rules never produced a dispute the parties could not settle alone, which refutes X3; or by one whose allocation rules were kept, at a measured temptation above a preregistered tolerance, after every response to breach had ceased, which refutes X5. A single such collective would leave its dependency structure without a path from some function to production, or without a cascade from coercion, and would show that interdependence is common rather than universal. Universal interdependence is also not universal capture. It holds in every corner of \cref{thm:formalized-state:nonimplication}, including the stateless corner where no one holds more than an equal share of anything.
   996	
   997	\emph{There is no single apex.} The pluralist objection, that complex polities seldom have a unified center of command \citep{dahl1961}, is an objection to Proposition B, not to Proposition A, and the framework accommodates it. A polity whose couplings form a star built by different coalitions has bounded integration by \cref{lem:formalized-state:hub}(b), and the strong classification requires a documented coalition, mechanism, domain and duration \citep{largo2026hbs}.
   998	
   999	\emph{The indices cannot be measured.} The indices are defined for measurement, and what the paper proves about them is their range, the effect of the weights (\cref{lem:formalized-state:U}), and the bounds that link coalition structure to integration (\cref{lem:formalized-state:hub}). These results constrain measurement without performing it. The latent-variable and event-study designs of the source, together with a coding of the five conditions of a capture link, remain the agenda.
  1000	

2026-10-22T19:05:06.137685Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '878,940p' papers/latex/formalized-state.tex | nl -ba -v878 && sed -n '1000,1200p' papers/latex/formalized-state.tex | nl -ba -v1000" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   878	\begin{table}[!htbp]
   879	\centering
   880	\small
   881	\caption{Regime profiles. Patterns and paths are drawn from the comparative sections of Parts I to VI.}
   882	\label{tab:regimes}
   883	\begin{tabularx}{\textwidth}{@{}L{2.2cm}YYY@{}}
   884	\toprule
   885	Regime type & Hypothesized integration pattern & Characteristic control path & Principal checks \\
   886	\midrule
   887	Market capitalism & A star around resources, with different coalitions on different spokes & From wealth to rules, legitimation and interpretation & Competition among interests, antitrust, disclosure, elections and courts \\
   888	Communist party-state & A clique of five pillars under the ruling party & From appointment to allocation and enforcement & Elite divisions, bureaucratic bargaining and the loyalty limit on appointment \\
   889	Social democracy & A triangle of rule making, resources and production joined by bargaining & From organized bargaining to rules and terms of work & Elections, organized labor, ombudsmen and parliamentary oversight \\
   890	Islamic states & Plural in classical practice and a clique around clerical authority in modern Iran & From religious-legal authority to rules and adjudication, and from rents to rule & Juristic pluralism, endowed revenue, brokerage and elections in Iran \\
   891	Catholic monarchies & Couplings of crown and Church, of money and justice, and of money and force & From fiscal need to venal office and from Church patronage to legitimation & Parlements, estates and Cortes, competing jurisdictions and Church-crown conflict \\
   892	Secular democracies & Low couplings, with appointment to courts and delegation to technical bodies & From rule making to interpretation through appointment & Rival institutions, free press, review bodies and citizen coordination \\
   893	\bottomrule
   894	\end{tabularx}
   895	\end{table}
   896	
   897	\section{Predecessors and novelty}
   898	\label{sec:literature}
   899	
   900	\subsection{The canon}
   901	
   902	Earlier answers to the question of what every polity must contain are of three kinds: typologies of rulers and of legitimacy, lists of functions, and derivations from premises. The typologies classify polities along axes other than the six functions. Aristotle classified constitutions by whether one, a few or many rule and whether they rule for the common interest or their own, and distinguished the deliberative, magisterial and judicial elements of a constitution \citep{aristotle1996}. Weber classified domination by the belief in its legitimacy, traditional, charismatic or legal-rational, and by the administrative staff that executes it \citep{weber1978}.
   903	
   904	The lists of functions are the closest relatives. Parsons named four functional prerequisites of any social system, adaptation, goal attainment, integration and latent pattern maintenance \citep{parsons1951}, and \citet{aberle1950} gave a longer list. Easton described the political system as converting inputs of demands and supports into authoritative outputs \citep{easton1965}. Almond divided political functions into input functions, among them socialization, interest articulation, interest aggregation and communication, and output functions, rule making, rule application and rule adjudication \citep{almond1960}. Luhmann described modern society as differentiated into functional subsystems, among them the economy, politics, law, science, religion and the mass media \citep{luhmann1995}. Mann treated societies as overlapping networks of ideological, economic, military and political power, none of them primary \citep{mann1986,mann1993}. These lists were criticized for defining prerequisites by what persisting societies happen to have \citep{hempel1959,elster1983}.
   905	
   906	The derivations are the model for the method. Hobbes derived the sovereign from the premise that agreements without a power to enforce them do not hold \citep{hobbes1651}; Part V accepts the premise and derives a sanctioning function rather than a sovereign. Arrow's impossibility theorem derives a sharp result about collective decisions from short axioms \citep{arrow1951}; it concerns aggregation rather than the structure of governance, and the rule-making function of Part II begins where it leaves off, since a collective must choose some procedure although none satisfies every desirable condition.
   907	
   908	The lists differ from the six pillars at exactly the points the formal results test. Mann's economic source and Parsons's adaptation join the command of resources with the production of wealth, which the latent veto (Proposition 3.6 of Part VI) and relocation (Lemma 3.4 of Part VI) separate; Mann's political source joins rule making with adjudication, which the disjunctive dependency of Proposition 3.6 of Part III separates. Mann's distinction between the despotic power of elites and the infrastructural power of states \citep{mann1984} corresponds to the distinction between $U_t$ and the capacity vector $x_t$, and his historical account of how particular networks emerged is something no axiomatic treatment replaces.
   909	
   910	Two further literatures address the other side of the thesis. The theory of capture, from Michels \citep{michels1915} through Stigler \citep{stigler1971}, state capture \citep{hellman2000}, extractive institutions \citep{acemoglu2006,acemoglu2019} and limited-access orders \citep{nww2009}, explains when capture arises, which is Proposition B, and does not state what every polity must contain. Normative theory supplies readings of the indices: the separation of powers of Montesquieu and Madison covers two pillars and part of a third \citep{montesquieu1989,madison1788}, and Walzer's spheres and Pettit's non-domination give normative content to $C_{mn}$ and $Q_m$ \citep{walzer1983,pettit1997}.
   911	
   912	\subsection{Non-equivalence}
   913	
   914	Each predecessor can be encoded as an abstraction on $\mathcal{G}_*$, and the encodings can be compared with $\Phi$ in $\mathbf{Abs}_P$. Five are coarsenings in the sense of \cref{sec:representation}, with equal weights within each block. Parsons: adaptation $=\{\pF,\pW\}$, goal attainment $=\{\pP\}$, integration $=\{\pJ,\pC\}$, latent pattern maintenance $=\{\pI\}$ \citep{parsons1951}; whether coercion belongs to goal attainment or to integration is contestable, and the choice does not affect the argument. Mann: ideological $=\{\pI\}$, economic $=\{\pF,\pW\}$, military $=\{\pC\}$, political $=\{\pP,\pJ\}$ \citep{mann1986}. Easton: inputs $=\{\pI,\pW\}$, outputs $=\{\pF,\pP,\pJ,\pC\}$ \citep{easton1965}; the assignment of production to inputs, as the source of supports, is contestable. Almond: rule making $=\{\pP\}$, rule application $=\{\pC\}$, rule adjudication $=\{\pJ\}$, inputs $=\{\pI\}$, with $\pF$ and $\pW$ dropped because his functions are those of the political system \citep{almond1960}; placing administration with coercion is contestable. Luhmann: economy $=\{\pF,\pW\}$, politics $=\{\pP,\pC\}$, law $=\{\pJ\}$, and one block for the communicative subsystems $=\{\pI\}$ \citep{luhmann1995}; Luhmann splits that block further, which the argument does not need. These encodings are readings of the 1960 and 1995 partitions: Almond and Powell later added system capabilities, among them extractive, regulative and distributive ones, that touch $\pF$ \citep{almond1966}, and Luhmann's subsystems are codes of communication rather than layers of actors. The other two are typologies. Aristotle's encoding returns the number of rulers, one if a single actor has a positive share of rule making, few if between two and half the members do, many otherwise, and the aim, deviant if a capture link is documented and correct otherwise \citep{aristotle1996}; the thresholds are a choice. Weber's encoding returns the coded type of legitimation and whether an administrative staff exists \citep{weber1978}.
   915	
   916	\begin{proposition}[Witnesses]
   917	\label{prop:formalized-state:witnesses}
   918	For each encoding $\alpha_k$ above there are $G,G'\in\mathcal{G}_*$ with $\alpha_k(G)=\alpha_k(G')$ and $P(G)\neq P(G')$:
   919	\begin{enumerate}[label=(\alph*)]
   920	\item Parsons, Mann and Luhmann merge $\pF$ and $\pW$, and Mann and Easton merge $\pP$ and $\pJ$; the pair of \cref{prop:formalized-state:minimality6}(b) for the merged pair, with $\mu=1/2$, has $C^{\ov}$ equal to $0$ against $1/2$ and $H$ equal to $1$ against $1/2$ in each merged pillar;
   921	\item Almond drops $\pF$; the pair of \cref{prop:formalized-state:minimality6}(a) with $m=\pF$ and $l_0=\pP$ has $H_{\pF}=1$ against $1/2$;
   922	\item Aristotle: two collectives with the same rule-making layer and no capture link, in which interpretation is held by one organization ($s^{\pJ}=(1,0)$ on $(a,b)$, $H_{\pJ}=1$) or by two equally ($s^{\pJ}=(1/2,1/2)$, $H_{\pJ}=1/2$), with $a$ and $b$ holding equal shares in $\pI$ in both;
   923	\item Weber: two collectives coded as legal-rational with an administrative staff, in which coercion is held by one organization ($s^{\pC}=(1,0)$ on $(a,b)$, $H_{\pC}=1$) or by two equally ($H_{\pC}=1/2$), with $a$ and $b$ holding equal shares in $\pI$ in both.
   924	\end{enumerate}
   925	Hence no encoded predecessor is $P$-preserving, and none is isomorphic to $\Phi$ in $\mathbf{Abs}_P$.
   926	\end{proposition}
   927	
   928	\begin{proof}
   929	(a) and (b) are instances of \cref{prop:formalized-state:minimality6}, whose proof computes both $P$-values and shows the coarsened images equal for any weights. Easton's outputs block contains $\pF$, $\pC$ and the merged pair; the coarsened shares of the block are a weighted sum in which only the $\pP$ and $\pJ$ terms differ between the two collectives, and those terms sum to the same vector, as in the proof of \cref{prop:formalized-state:minimality6}(b). (c) The two collectives have the same actor set, since $b$ performs practices of $\pI$ in both. They have the same set of actors with positive rule-making share and the same empty set of capture links, so the encoding returns the same number of rulers and the same aim. Their $H_{\pJ}$ differ, and $H_{\pJ}$ is invariant under relabeling. Both assignments are admissible as in the proof of \cref{prop:formalized-state:minimality6}, so both lie in $\mathcal{G}_*$ by \cref{lem:formalized-state:separation}. (d) The actor sets coincide as in (c). The two collectives carry the same coded legitimation type and staff, so the encoding agrees; $H_{\pC}$ differs. For the last sentence: an abstraction isomorphic to $\Phi$ has the same partition of $\mathcal{G}_*$ as $\Phi$, which is the partition into $\cong_A$-classes, and is therefore $P$-preserving.
   930	\end{proof}
   931	
   932	The Weber encoding fails in the other direction too. Two collectives with the same profile can carry different legitimation types, since $P$ forgets the content of legitimating beliefs (\cref{lem:formalized-state:preserved}); so neither of Weber's typology and $\Phi$ factors through the other. Weber classifies what the Formalized State forgets, and the two are complements rather than rivals.
   933	
   934	\begin{theorem}[Novelty relative to the canon]
   935	\label{thm:formalized-state:novelty}
   936	For each of the encoded predecessors, Aristotle, Weber, Parsons, Easton, Almond, Luhmann and Mann, the encoding $\alpha_k$ is not isomorphic to $\Phi$ in $\mathbf{Abs}_P$, does not represent governance systems up to $\cong_A$, and is not the coarsest $P$-preserving abstraction. The Formalized State abstraction has all four properties: representation, necessity, minimality and uniqueness.
   937	\end{theorem}
   938	
   939	\begin{proof}
   940	By \cref{prop:formalized-state:witnesses}, each $\alpha_k$ identifies two systems that are not $\cong_A$-equivalent, so it does not represent systems up to $\cong_A$ and is not $P$-preserving. A terminal object of $\mathbf{Abs}_P$ is in particular an object of it, so $\alpha_k$ is neither terminal nor isomorphic to $\Phi$. The four properties of $\Phi$ are \cref{thm:formalized-state:representation}, \cref{thm:formalized-state:A,thm:formalized-state:interdependence}, \cref{prop:formalized-state:minimality6}, and \cref{thm:formalized-state:uniqueness,thm:formalized-state:six}.
  1000	
  1001	\emph{The name condemns all governance.} Naming the universal structure after the beast could be read as a verdict that every polity is the beast of Revelation. The series rejects that reading. The name refers to a structure that every governance system has, and Proposition A carries no moral verdict; the warning attaches to Proposition B, and \cref{thm:formalized-state:nonimplication} shows that every regime type can satisfy A without B. Government that protects the vulnerable, courts that check power and expertise that corrects error are compatible with the structure and are among the checks that interrupt capture.
  1002	
  1003	\emph{The abstraction forgets too much.} The equivalence $\cong_A$ forgets the content of rules and beliefs, the procedures that implement each function, and the moral quality of outcomes (\cref{lem:formalized-state:preserved}). A medieval monarchy and a modern republic can have the same image if their control shares, contestability, couplings and dependencies coincide. This is the price of a representation that covers every governance system, and it is why the abstraction says nothing about justice. The properties it keeps are the ones that the capture predicate needs, and the properties it forgets are left to history, law and theology.
  1004	
  1005	\emph{Uniqueness is built into the definitions.} The universal property of \cref{thm:formalized-state:uniqueness} follows quickly once the preserved properties are fixed, and \cref{rem:formalized-state:scope} says so. The substantive content is that the coarsest abstraction is a class of six-layer structures with an interdependent dependency hypergraph, which needs necessity, and that no coarsening of it works, which needs the witness pairs. A reader who wants to preserve other properties obtains another abstraction, unique for those properties.
  1006	
  1007	\emph{Class relations are underdeveloped.} A Marxian reader may find that the six pillars dissolve class into functions. The productive pillar is the place where the objection is met. Part VI shows that producers hold a latent veto over every institution that cannot replace their output (Proposition 3.6 of Part VI), and the dependency structure makes every function depend on production. The framework is a middle-range theory of institutions, and it leaves the theory of class formation to others.
  1008	
  1009	\section{Conclusion}
  1010	\label{sec:conclusion}
  1011	
  1012	The six-pillar framework identifies an invariant structure of human governance, supported by historical observation and given precise expression through mathematics. Relative to six axioms about collective life, four incidence axioms and a stated set of preserved properties, the Formalized State has four properties. It represents every governance system that satisfies the axioms, preserving roles, control shares, concentration, contestability, integration and dependencies and forgetting content, ideology and procedure. Its components are necessary, because the axioms force each function and each dependency and each axiom can fail in a persistent model. It is minimal, because every way of dropping or merging pillars confuses two systems with different preserved properties. And it is unique, as the coarsest abstraction that preserves those properties, up to a unique isomorphism, with exactly six dimensions. Encodings of seven classical frameworks each confuse a pair of systems that it distinguishes.
  1013	
  1014	Capture belongs to instances. Structures that satisfy every axiom occupy every corner of the concentration and integration square, so the existence of the structure settles nothing about its capture, and the conversion model shows how replacement and contestability decide whether a coalition's foothold dies out. The open questions are empirical: whether every functioning collective satisfies the axioms, which has been tested against the ethnographic and historical record only qualitatively; and the quantitative scoring of real polities on indices whose ranges are proved here. The series calls the abstraction the Hierarchy of the Beast System. The structure is universal, its capture is contingent, and the difference between them is a matter of measurement.
  1015	
  1016	\appendix
  1017	
  1018	\section{Code evidence}
  1019	\label{app:code}
  1020	
  1021	The reference implementation is the Python package \texttt{beast\_system} in the directory \texttt{model/} of the project, with its tests in \texttt{model/tests/}. It encodes the formal objects of this paper and checks the results that admit a computational check on coded fixtures.
  1022	
  1023	%APPENDIX-CODE-EVIDENCE
  1024	
  1025	\begin{small}
  1026	\begin{thebibliography}{999}
  1027	
  1028	\bibitem[Aberle et al.(1950)]{aberle1950}
  1029	Aberle, D. F., A. K. Cohen, A. K. Davis, M. J. Levy Jr. and F. X. Sutton. 1950. ``The Functional Prerequisites of a Society.'' \emph{Ethics} 60(2): 100-111. \url{https://doi.org/10.1086/290705}.
  1030	
  1031	\bibitem[Acemoglu and Robinson(2006)]{acemoglu2006}
  1032	Acemoglu, Daron and James A. Robinson. 2006. \emph{Economic Origins of Dictatorship and Democracy}. Cambridge University Press. \url{https://doi.org/10.1017/CBO9780511510809}.
  1033	
  1034	\bibitem[Acemoglu and Robinson(2019)]{acemoglu2019}
  1035	Acemoglu, Daron and James A. Robinson. 2019. \emph{The Narrow Corridor: States, Societies, and the Fate of Liberty}. Penguin Press.
  1036	
  1037	\bibitem[Almond and Coleman(1960)]{almond1960}
  1038	Almond, Gabriel A. and James S. Coleman, eds. 1960. \emph{The Politics of the Developing Areas}. Princeton University Press. \url{https://doi.org/10.1515/9781400866977}.
  1039	
  1040	\bibitem[Almond and Powell(1966)]{almond1966}
  1041	Almond, Gabriel A. and G. Bingham Powell. 1966. \emph{Comparative Politics: A Developmental Approach}. Little, Brown. \url{https://openlibrary.org/works/OL2693586W}.
  1042	
  1043	\bibitem[Aristotle(1996)]{aristotle1996}
  1044	Aristotle. 1996. \emph{The Politics, and the Constitution of Athens}. Cambridge University Press. \url{https://openlibrary.org/works/OL14998298W}.
  1045	
  1046	\bibitem[Arrow(1951)]{arrow1951}
  1047	Arrow, Kenneth J. 1951. \emph{Social Choice and Individual Values}. Yale University Press edition. \url{https://doi.org/10.12987/9780300186987}.
  1048	
  1049	\bibitem[Aumann(1976)]{aumann1976}
  1050	Aumann, Robert J. 1976. ``Agreeing to Disagree.'' \emph{The Annals of Statistics} 4(6): 1236-1239. \url{https://doi.org/10.1214/aos/1176343654}.
  1051	
  1052	\bibitem[Axelrod(1984)]{axelrod1984}
  1053	Axelrod, Robert. 1984. \emph{The Evolution of Cooperation}. Basic Books.
  1054	
  1055	\bibitem[Barkey(2008)]{barkey2008}
  1056	Barkey, Karen. 2008. \emph{Empire of Difference: The Ottomans in Comparative Perspective}. Cambridge University Press. \url{https://doi.org/10.1017/cbo9780511790645}.
  1057	
  1058	\bibitem[Bauckham(1991)]{bauckham1991}
  1059	Bauckham, Richard. 1991. ``The Economic Critique of Rome in Revelation 18.'' In \emph{Images of Empire}, edited by Loveday Alexander, 47-90. Sheffield: JSOT Press.
  1060	
  1061	\bibitem[Bauckham(1993)]{bauckham1993}
  1062	Bauckham, Richard. 1993. \emph{The Theology of the Book of Revelation}. Cambridge University Press. \url{https://doi.org/10.1017/cbo9780511819858}.
  1063	
  1064	\bibitem[Becker(1968)]{becker1968}
  1065	Becker, Gary S. 1968. ``Crime and Punishment: An Economic Approach.'' \emph{Journal of Political Economy} 76(2): 169-217. \url{https://doi.org/10.1086/259394}.
  1066	
  1067	\bibitem[Beik(1985)]{beik1985}
  1068	Beik, William. 1985. \emph{Absolutism and Society in Seventeenth-Century France: State Power and Provincial Aristocracy in Languedoc}. Cambridge University Press. \url{https://doi.org/10.1017/cbo9780511583797}.
  1069	
  1070	\bibitem[Boehm(1999)]{boehm1999}
  1071	Boehm, Christopher. 1999. \emph{Hierarchy in the Forest: The Evolution of Egalitarian Behavior}. Harvard University Press. \url{https://doi.org/10.2307/j.ctvjf9xr4}.
  1072	
  1073	\bibitem[Boyer(1992)]{boyer1992}
  1074	Boyer, Paul. 1992. \emph{When Time Shall Be No More: Prophecy Belief in Modern American Culture}. Harvard University Press (Belknap). \url{https://doi.org/10.2307/jj.41480279}.
  1075	
  1076	\bibitem[Cassinelli(1953)]{cassinelli1953}
  1077	Cassinelli, C. W. 1953. ``The Law of Oligarchy.'' \emph{American Political Science Review} 47(3): 773-784. \url{https://doi.org/10.2307/1952904}.
  1078	
  1079	\bibitem[Clastres(1987)]{clastres1987}
  1080	Clastres, Pierre. 1987. \emph{Society against the State: Essays in Political Anthropology (1974), trans. Robert Hurley}. Zone Books. \url{https://doi.org/10.2307/j.ctv1595m3p}.
  1081	
  1082	\bibitem[Collins(1984)]{collins1984}
  1083	Collins, Adela Yarbro. 1984. \emph{Crisis and Catharsis: The Power of the Apocalypse}. Westminster Press.
  1084	
  1085	\bibitem[Cox et al.(2010)]{cox2010}
  1086	Cox, Michael, Gwen Arnold and Sergio Villamayor Tomas. 2010. ``A Review of Design Principles for Community-based Natural Resource Management.'' \emph{Ecology and Society} 15(4): 38. \url{https://doi.org/10.5751/ES-03704-150438}.
  1087	
  1088	\bibitem[Dahl(1961)]{dahl1961}
  1089	Dahl, Robert A. 1961. \emph{Who Governs? Democracy and Power in an American City}. Yale University Press.
  1090	
  1091	\bibitem[Easton(1965)]{easton1965}
  1092	Easton, David. 1965. \emph{A Systems Analysis of Political Life}. John Wiley \& Sons.
  1093	
  1094	\bibitem[Ellickson(1991)]{ellickson1991}
  1095	Ellickson, Robert C. 1991. \emph{Order without Law: How Neighbors Settle Disputes}. Harvard University Press. \url{https://doi.org/10.4159/9780674036437}.
  1096	
  1097	\bibitem[Elster(1979)]{elster1979}
  1098	Elster, Jon. 1979. \emph{Ulysses and the Sirens: Studies in Rationality and Irrationality}. Cambridge University Press.
  1099	
  1100	\bibitem[Elster(1983)]{elster1983}
  1101	Elster, Jon. 1983. \emph{Explaining Technical Change: A Case Study in the Philosophy of Science}. Cambridge University Press.
  1102	
  1103	\bibitem[Ertman(1997)]{ertman1997}
  1104	Ertman, Thomas. 1997. \emph{Birth of the Leviathan: Building States and Regimes in Medieval and Early Modern Europe}. Cambridge University Press. \url{https://doi.org/10.1017/cbo9780511529016}.
  1105	
  1106	\bibitem[Evans-Pritchard(1940)]{evanspritchard1940}
  1107	Evans-Pritchard, E. E. 1940. \emph{The Nuer: A Description of the Modes of Livelihood and Political Institutions of a Nilotic People}. Clarendon Press.
  1108	
  1109	\bibitem[Friesen(2001)]{friesen2001}
  1110	Friesen, Steven J. 2001. \emph{Imperial Cults and the Apocalypse of John: Reading Revelation in the Ruins}. Oxford University Press. \url{https://doi.org/10.1093/0195131533.001.0001}.
  1111	
  1112	\bibitem[Fuller(1995)]{fuller1995}
  1113	Fuller, Robert C. 1995. \emph{Naming the Antichrist: The History of an American Obsession}. Oxford University Press. \url{https://doi.org/10.1093/acprof:oso/9780195109795.001.0001}.
  1114	
  1115	\bibitem[Gallo et al.(1993)]{gallo1993}
  1116	Gallo, Giorgio, Giustino Longo, Stefano Pallottino and Sang Nguyen. 1993. ``Directed Hypergraphs and Applications.'' \emph{Discrete Applied Mathematics} 42(2-3): 177-201. \url{https://doi.org/10.1016/0166-218X(93)90045-P}.
  1117	
  1118	\bibitem[Graeber and Wengrow(2021)]{graeber2021}
  1119	Graeber, David and David Wengrow. 2021. \emph{The Dawn of Everything: A New History of Humanity}. Farrar, Straus and Giroux.
  1120	
  1121	\bibitem[Greif(1993)]{greif1993}
  1122	Greif, Avner. 1993. ``Contract Enforceability and Economic Institutions in Early Trade: The Maghribi Traders' Coalition.'' \emph{American Economic Review} 83(3): 525-548. \url{https://www.jstor.org/stable/2117532}.
  1123	
  1124	\bibitem[Hallaq(2009)]{hallaq2009}
  1125	Hallaq, Wael B. 2009. \emph{An Introduction to Islamic Law}. Cambridge University Press. \url{https://doi.org/10.1017/cbo9780511801044}.
  1126	
  1127	\bibitem[Hart(1961)]{hart1961}
  1128	Hart, H. L. A. 1961. \emph{The Concept of Law}. Clarendon Press (3rd ed. 2012, Oxford University Press). \url{https://doi.org/10.1093/he/9780199644704.001.0001}.
  1129	
  1130	\bibitem[Hayek(1973)]{hayek1973}
  1131	Hayek, Friedrich A. 1973. \emph{Law, Legislation and Liberty, Volume 1: Rules and Order}. University of Chicago Press. \url{https://doi.org/10.7208/chicago/9780226321233.001.0001}.
  1132	
  1133	\bibitem[Hellman et al.(2000)]{hellman2000}
  1134	Hellman, Joel S., Geraint Jones and Daniel Kaufmann. 2000. \emph{Seize the State, Seize the Day: State Capture, Corruption, and Influence in Transition}. World Bank Policy Research Working Paper 2444.
  1135	
  1136	\bibitem[Hempel(1959)]{hempel1959}
  1137	Hempel, Carl G. 1959. ``The Logic of Functional Analysis.'' In \emph{Symposium on Sociological Theory}, edited by Llewellyn Gross, 271-307. New York: Harper \& Row.
  1138	
  1139	\bibitem[Hirschl(2004)]{hirschl2004}
  1140	Hirschl, Ran. 2004. \emph{Towards Juristocracy: The Origins and Consequences of the New Constitutionalism}. Harvard University Press. \url{https://doi.org/10.2307/j.ctv15d81nb}.
  1141	
  1142	\bibitem[Hobbes(1996)]{hobbes1651}
  1143	Hobbes, Thomas. 1996. \emph{Leviathan} (1651), edited by Richard Tuck. Cambridge University Press. \url{https://doi.org/10.1017/CBO9780511808166}.
  1144	
  1145	\bibitem[Horn and Johnson(2012)]{horn2012}
  1146	Horn, Roger A. and Charles R. Johnson. 2012. \emph{Matrix Analysis}. Second edition. Cambridge University Press. \url{https://doi.org/10.1017/CBO9781139020411}.
  1147	
  1148	\bibitem[Hough and Fainsod(1979)]{hough1979}
  1149	Hough, Jerry F. and Merle Fainsod. 1979. \emph{How the Soviet Union Is Governed}. Harvard University Press.
  1150	
  1151	\bibitem[Kelly(1995)]{kelly1995}
  1152	Kelly, Robert L. 1995. \emph{The Foraging Spectrum: Diversity in Hunter-Gatherer Lifeways}. Smithsonian Institution Press. \url{https://doi.org/10.2307/j.ctv2sx9gc9}.
  1153	
  1154	\bibitem[{King James Bible}(1611)]{kjv}
  1155	\emph{The Holy Bible, King James Version}. 1611. Project Gutenberg eBook no.~10. \url{https://www.gutenberg.org/ebooks/10}.
  1156	
  1157	\bibitem[Kivela et al.(2014)]{kivela2014}
  1158	Kivela, Mikko, Alex Arenas, Marc Barthelemy, James P. Gleeson, Yamir Moreno and Mason A. Porter. 2014. ``Multilayer Networks.'' \emph{Journal of Complex Networks} 2(3): 203-271. \url{https://doi.org/10.1093/comnet/cnu016}.
  1159	
  1160	\bibitem[Koester(2014)]{koester2014}
  1161	Koester, Craig R. 2014. \emph{Revelation: A New Translation with Introduction and Commentary}. Yale University Press (Anchor Yale Bible 38A). \url{https://doi.org/10.12987/9780300211030}.
  1162	
  1163	\bibitem[Kraybill(1996)]{kraybill1996}
  1164	Kraybill, J. Nelson. 1996. \emph{Imperial Cult and Commerce in John's Apocalypse}. Sheffield Academic Press (JSNT Supplement 132).
  1165	
  1166	\bibitem[Kuran(2011)]{kuran2011}
  1167	Kuran, Timur. 2011. \emph{The Long Divergence: How Islamic Law Held Back the Middle East}. Princeton University Press. \url{https://doi.org/10.1515/9781400836017}.
  1168	
  1169	\bibitem[Lane and Ross(1995)]{lane1995}
  1170	Lane, David and Cameron Ross. 1995. ``The CPSU Ruling Elite 1981-1991: Commonalities and Divisions.'' \emph{Communist and Post-Communist Studies} 28(3): 339-360. \url{https://doi.org/10.1016/0967-067X(95)00020-U}.
  1171	
  1172	\bibitem[Largo(2026)]{largo2026hbs}
  1173	Largo, Mateo. 2026. ``The Hierarchy of the Beast System: Institutional Power, Elite Coordination, and Economic Dependency Across Political Regimes.'' Working paper, 14 October 2026.
  1174	
  1175	\bibitem[Lee(1979)]{lee1979}
  1176	Lee, Richard B. 1979. \emph{The !Kung San: Men, Women, and Work in a Foraging Society}. Cambridge University Press.
  1177	
  1178	\bibitem[Lee(2013)]{lee2013}
  1179	Lee, Richard B. 2013. \emph{The Dobe Ju/'hoansi (4th edition)}. Wadsworth/Cengage Learning.
  1180	
  1181	\bibitem[Lewis(1969)]{lewis1969}
  1182	Lewis, David K. 1969. \emph{Convention: A Philosophical Study}. Harvard University Press. \url{https://doi.org/10.1002/9780470693711}.
  1183	
  1184	\bibitem[Lipset et al.(1956)]{lipset1956}
  1185	Lipset, Seymour Martin, Martin A. Trow and James S. Coleman. 1956. \emph{Union Democracy: The Internal Politics of the International Typographical Union}. Free Press.
  1186	
  1187	\bibitem[Long(2026a)]{long2026coercive}
  1188	Long, Matthew. 2026a. ``Coercive Power and Enforcement.'' Part V of \emph{The Six Pillars of the Beast System}. Working paper, October 2026.
  1189	
  1190	\bibitem[Long(2026b)]{long2026financial}
  1191	Long, Matthew. 2026b. ``Financial Power and Resource Command.'' Part I of \emph{The Six Pillars of the Beast System}. Working paper, October 2026.
  1192	
  1193	\bibitem[Long(2026c)]{long2026ideological}
  1194	Long, Matthew. 2026c. ``Ideological Power and Legitimation.'' Part IV of \emph{The Six Pillars of the Beast System}. Working paper, October 2026.
  1195	
  1196	\bibitem[Long(2026d)]{long2026judicial}
  1197	Long, Matthew. 2026d. ``Judicial Power and Legal Interpretation.'' Part III of \emph{The Six Pillars of the Beast System}. Working paper, October 2026.
  1198	
  1199	\bibitem[Long(2026e)]{long2026political}
  1200	Long, Matthew. 2026e. ``Political Power and Rule Making.'' Part II of \emph{The Six Pillars of the Beast System}. Working paper, October 2026.

2026-10-22T19:05:09.200864Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '1200,1304p' papers/latex/formalized-state.tex | nl -ba -v1200" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
  1200	Long, Matthew. 2026e. ``Political Power and Rule Making.'' Part II of \emph{The Six Pillars of the Beast System}. Working paper, October 2026.
  1201	
  1202	\bibitem[Long(2026f)]{long2026productive}
  1203	Long, Matthew. 2026f. ``Productive Power and Social Reproduction.'' Part VI of \emph{The Six Pillars of the Beast System}. Working paper, October 2026.
  1204	
  1205	\bibitem[Luhmann(1995)]{luhmann1995}
  1206	Luhmann, Niklas. 1995. \emph{Social Systems}. Stanford University Press. \url{https://openlibrary.org/works/OL1652158W}.
  1207	
  1208	\bibitem[Madison(1788)]{madison1788}
  1209	Madison, James. 1788. \emph{The Federalist No. 51: The Structure of the Government Must Furnish the Proper Checks and Balances}. Independent Journal, 6 February 1788. \url{https://avalon.law.yale.edu/18th_century/fed51.asp}.
  1210	
  1211	\bibitem[Mann(1984)]{mann1984}
  1212	Mann, Michael. 1984. ``The Autonomous Power of the State: Its Origins, Mechanisms and Results.'' \emph{European Journal of Sociology} 25(2): 185-213. \url{https://doi.org/10.1017/S0003975600004239}.
  1213	
  1214	\bibitem[Mann(1986)]{mann1986}
  1215	Mann, Michael. 1986. \emph{The Sources of Social Power, Volume 1: A History of Power from the Beginning to A.D. 1760}. Cambridge University Press. \url{https://doi.org/10.1017/CBO9780511570896}.
  1216	
  1217	\bibitem[Mann(1993)]{mann1993}
  1218	Mann, Michael. 1993. \emph{The Sources of Social Power, Volume 2: The Rise of Classes and Nation-States, 1760-1914}. Cambridge University Press. \url{https://doi.org/10.1017/CBO9780511570902}.
  1219	
  1220	\bibitem[Marshall(1976)]{marshall1976}
  1221	Marshall, Lorna. 1976. \emph{The !Kung of Nyae Nyae}. Harvard University Press. \url{https://doi.org/10.4159/harvard.9780674180574}.
  1222	
  1223	\bibitem[McGinn(1998)]{mcginn1998}
  1224	McGinn, Bernard. 1998. \emph{Antichrist: Two Thousand Years of the Human Fascination with Evil}. Columbia University Press.
  1225	
  1226	\bibitem[Merton(1968)]{merton1968}
  1227	Merton, Robert K. 1968. \emph{Social Theory and Social Structure (enlarged edition)}. Free Press.
  1228	
  1229	\bibitem[Michels(1915)]{michels1915}
  1230	Michels, Robert. 1915. \emph{Political Parties: A Sociological Study of the Oligarchical Tendencies of Modern Democracy}. Hearst's International Library.
  1231	
  1232	\bibitem[Montesquieu(1989)]{montesquieu1989}
  1233	Montesquieu, Charles de Secondat. 1989. \emph{The Spirit of the Laws} (1748), edited by Anne M. Cohler, Basia Carolyn Miller and Harold Samuel Stone. Cambridge University Press.
  1234	
  1235	\bibitem[Mosca(1939)]{mosca1939}
  1236	Mosca, Gaetano. 1939. \emph{The Ruling Class (Elementi di scienza politica)}. McGraw-Hill.
  1237	
  1238	\bibitem[North et al.(2009)]{nww2009}
  1239	North, Douglass C., John Joseph Wallis and Barry R. Weingast. 2009. \emph{Violence and Social Orders: A Conceptual Framework for Interpreting Recorded Human History}. Cambridge University Press. \url{https://doi.org/10.1017/CBO9780511575839}.
  1240	
  1241	\bibitem[Olson(1965)]{olson1965}
  1242	Olson, Mancur. 1965. \emph{The Logic of Collective Action: Public Goods and the Theory of Groups}. Harvard University Press. \url{https://doi.org/10.4159/9780674041660}.
  1243	
  1244	\bibitem[Ostrom(1990)]{ostrom1990}
  1245	Ostrom, Elinor. 1990. \emph{Governing the Commons: The Evolution of Institutions for Collective Action}. Cambridge University Press. \url{https://doi.org/10.1017/CBO9780511807763}.
  1246	
  1247	\bibitem[Parsons(1951)]{parsons1951}
  1248	Parsons, Talcott. 1951. \emph{The Social System}. Free Press. \url{https://doi.org/10.4324/9780203992951}.
  1249	
  1250	\bibitem[Pettit(1997)]{pettit1997}
  1251	Pettit, Philip. 1997. \emph{Republicanism: A Theory of Freedom and Government}. Oxford University Press. \url{https://doi.org/10.1093/0198296428.001.0001}.
  1252	
  1253	\bibitem[Price(1984)]{price1984}
  1254	Price, S. R. F. 1984. \emph{Rituals and Power: The Roman Imperial Cult in Asia Minor}. Cambridge University Press.
  1255	
  1256	\bibitem[Ross(2012)]{ross2012}
  1257	Ross, Michael L. 2012. \emph{The Oil Curse: How Petroleum Wealth Shapes the Development of Nations}. Princeton University Press. \url{https://doi.org/10.1515/9781400841929}.
  1258	
  1259	\bibitem[Rubin(2017)]{rubin2017}
  1260	Rubin, Jared. 2017. \emph{Rulers, Religion, and Riches: Why the West Got Rich and the Middle East Did Not}. Cambridge University Press. \url{https://doi.org/10.1017/9781139568272}.
  1261	
  1262	\bibitem[Sahlins(1972)]{sahlins1972b}
  1263	Sahlins, Marshall. 1972. ``The Original Affluent Society.'' In \emph{Stone Age Economics}, 1-39. Chicago: Aldine-Atherton. \url{https://doi.org/10.4324/9781003058762-1}.
  1264	
  1265	\bibitem[Scott(2009)]{scott2009}
  1266	Scott, James C. 2009. \emph{The Art of Not Being Governed: An Anarchist History of Upland Southeast Asia}. Yale University Press. \url{https://doi.org/10.12987/9780300156522}.
  1267	
  1268	\bibitem[Scott(2017)]{scott2017}
  1269	Scott, James C. 2017. \emph{Against the Grain: A Deep History of the Earliest States}. Yale University Press. \url{https://doi.org/10.12987/9780300231687}.
  1270	
  1271	\bibitem[Stigler(1971)]{stigler1971}
  1272	Stigler, George J. 1971. ``The Theory of Economic Regulation.'' \emph{The Bell Journal of Economics and Management Science} 2(1): 3-21. \url{https://doi.org/10.2307/3003160}.
  1273	
  1274	\bibitem[Tilly(1990)]{tilly1990}
  1275	Tilly, Charles. 1990. \emph{Coercion, Capital, and European States, AD 990-1990}. Blackwell.
  1276	
  1277	\bibitem[Voslensky(1984)]{voslensky1984}
  1278	Voslensky, Michael. 1984. \emph{Nomenklatura: The Soviet Ruling Class}. Doubleday. \url{https://doi.org/10.1163/9789004635562_298}.
  1279	
  1280	\bibitem[Voss and Sherman(2000)]{voss2000}
  1281	Voss, Kim and Rachel Sherman. 2000. ``Breaking the Iron Law of Oligarchy: Union Revitalization in the American Labor Movement.'' \emph{American Journal of Sociology} 106(2): 303-349. \url{https://doi.org/10.1086/316963}.
  1282	
  1283	\bibitem[Walzer(1983)]{walzer1983}
  1284	Walzer, Michael. 1983. \emph{Spheres of Justice: A Defense of Pluralism and Equality}. Basic Books.
  1285	
  1286	\bibitem[Weber(1978)]{weber1978}
  1287	Weber, Max. 1978. \emph{Economy and Society: An Outline of Interpretive Sociology}. University of California Press. \url{https://doi.org/10.4159/9780674240827}.
  1288	
  1289	\bibitem[Weingast(1997)]{weingast1997}
  1290	Weingast, Barry R. 1997. ``The Political Foundations of Democracy and the Rule of Law.'' \emph{American Political Science Review} 91(2): 245-263. \url{https://doi.org/10.2307/2952354}.
  1291	
  1292	\bibitem[Wiessner(2005)]{wiessner2005}
  1293	Wiessner, Polly. 2005. ``Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity?'' \emph{Human Nature} 16(2): 115-145. \url{https://doi.org/10.1007/s12110-005-1000-9}.
  1294	
  1295	\bibitem[Wink(1992)]{wink1992}
  1296	Wink, Walter. 1992. \emph{Engaging the Powers: Discernment and Resistance in a World of Domination}. Fortress Press. \url{https://doi.org/10.2307/j.ctt1tm7j16}.
  1297	
  1298	\bibitem[Woodburn(1982)]{woodburn1982}
  1299	Woodburn, James. 1982. ``Egalitarian Societies.'' \emph{Man (N.S.)} 17(3): 431-451. \url{https://doi.org/10.2307/2801707}.
  1300	
  1301	\end{thebibliography}
  1302	\end{small}
  1303	
  1304	\end{document}

2026-10-22T19:05:11.704986Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "perl -0777 -ne '
  my %labels; while (/\\\\label\\{(["'^}]+)'"\\}/g) {"'$labels{$1}++}
  my %refs; while (/'"\\\\[cC]ref(?:range)?\\{(["'^}]+)'"\\}/g) { "'$refs{$_}++ for split /,/, $1 }
  my %bib; while (/'"\\\\bibitem(?:\\[["'^'"\\]]*\\])?\\{(["'^}]+)'"\\}/g) {"'$bib{$1}++}
  my %cite; while (/'"\\\\cite(?:p|t|alt|alp|author|year|yearpar)?(?:\\[["'^'"\\]]*\\])?(?:\\[["'^'"\\]]*\\])?\\{(["'^}]+)'"\\}/g) { "'$cite{$_}++ for split /,/, $1 }
  print "Duplicate labels:'"\\n\"; print \""'$_ $labels{$_}'"\\n\" for grep {"'$labels{$_}>1} sort keys %labels;
  print "Missing ref targets:'"\\n\"; print \""'$_'"\\n\" for grep {"'!$labels{$_}} sort keys %refs;
  print "Duplicate bib keys:'"\\n\"; print \""'$_ $bib{$_}'"\\n\" for grep {"'$bib{$_}>1} sort keys %bib;
  print "Missing cite targets:'"\\n\"; print \""'$_'"\\n\" for grep {"'!$bib{$_}} sort keys %cite;
  print "Uncited bibitems:'"\\n\"; print \""'$_'"\\n\" for grep {"'!$cite{$_}} sort keys %bib;
'"' papers/latex/formalized-state.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
Duplicate labels:
Missing ref targets:
Duplicate bib keys:
Missing cite targets:
Uncited bibitems:
cassinelli1953

2026-10-22T19:05:27.202269Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "perl -0777 -ne '
  my %bib; while (/\\\\bibitem(?:\\[["'^'"\\]]*\\])?\\{(["'^}]+)'"\\}/g) {"'$bib{$1}++}
  my %cite; while (/'"\\\\[cC]ite(?:p|t|alt|alp|author|year|yearpar)?(?:\\[["'^'"\\]]*\\])?(?:\\[["'^'"\\]]*\\])?\\{(["'^}]+)'"\\}/g) { "'$cite{$_}++ for split /,/, $1 }
  print "Missing cite targets:'"\\n\"; print \""'$_'"\\n\" for grep {"'!$bib{$_}} sort keys %cite;
  print "Uncited bibitems:'"\\n\"; print \""'$_'"\\n\" for grep {"'!$cite{$_}} sort keys %bib;
'"' papers/latex/formalized-state.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
Missing cite targets:
Uncited bibitems:

2026-10-22T19:05:31.796153Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'rg -ni "warning|error|undefined|overfull|underfull|badness|multiply|duplicate|rerun to|get cross-references right|no file|not found|missing|ignored|deprecated" papers/latex/formalized-state.log' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
661:Package: infwarerr 2019/12/03 v1.5 Providing info/warning/error messages (HO)

2026-10-22T19:05:44.932543Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
codex
No actionable LaTeX formatting issues found. The log shows a successful 45-page build with no errors, warnings, unresolved citations or references, duplicate labels, overfull boxes, or underfull boxes. Tables, figure, bibliography, and citation keys are internally consistent.

VERDICT: PASS
hook: Stop
hook: Stop
hook: Stop Completed
hook: Stop Completed
tokens used
95,333
No actionable LaTeX formatting issues found. The log shows a successful 45-page build with no errors, warnings, unresolved citations or references, duplicate labels, overfull boxes, or underfull boxes. Tables, figure, bibliography, and citation keys are internally consistent.

VERDICT: PASS
