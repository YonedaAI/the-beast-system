---
reviewer: codex (OpenAI) gpt-5.6-sol
type: formatting
paper: political-power
round: 3
date: 2026-10-22T16:13:34Z
---
Reading additional input from stdin...
2026-10-22T16:40:05.706601Z ERROR codex_models_manager::cache: failed to load models cache: missing field `base_instructions` at line 139 column 5
OpenAI Codex v0.145.0
--------
workdir: /Users/mlong/Documents/Development/the-beast-system
model: gpt-5.6-sol
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a1647b-ef06-7bb2-bd85-e514d2aeba6c
--------
user
Read ONLY the file papers/latex/political-power.tex (do not explore other files or directories). Review it for LaTeX formatting issues: compilation errors, missing packages, broken references, inconsistent styling, overfull/underfull boxes, spacing problems. List all issues with line numbers and concrete fixes. End your response with a VERDICT line — exactly one of: VERDICT: PASS (no issues remain) or VERDICT: NEEDS_FIX (issues listed above must be fixed).
warning: Under-development features enabled: chronicle. Under-development features are incomplete and may behave unpredictably. To suppress this warning, set `suppress_unstable_features_warning = true` in /Users/mlong/.codex/config.toml.
warning: clamping SessionEnd hook timeout to 3s in /Users/mlong/.codex/plugins/cache/openai-codex/codex/1.0.6/hooks/hooks.json
2026-10-22T16:40:07.043103Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server linear: OAuth token refresh failed: Server returned error response: invalid_grant: Grant not found
2026-10-22T16:40:07.716718Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server resend: OAuth token refresh failed: Server returned error response: invalid_grant: Refresh token has been revoked
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
codex
I’ll inspect only the specified `.tex` file, using numbered output and static checks; I won’t open any other project files.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'nl -ba papers/latex/political-power.tex' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	\documentclass[11pt,letterpaper]{article}
     2	
     3	\usepackage[T1]{fontenc}
     4	\usepackage{lmodern}
     5	\usepackage{microtype}
     6	\usepackage[margin=1in,left=1.25in,right=1.25in]{geometry}
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
    20	\usepackage{enumitem}
    21	\usepackage[authoryear,round]{natbib}
    22	\usepackage{url}
    23	\usepackage[hidelinks]{hyperref}
    24	\usepackage{cleveref}
    25	
    26	\newtheorem{theorem}{Theorem}[section]
    27	\newtheorem{proposition}[theorem]{Proposition}
    28	\newtheorem{lemma}[theorem]{Lemma}
    29	\newtheorem{corollary}[theorem]{Corollary}
    30	\theoremstyle{definition}
    31	\newtheorem{definition}[theorem]{Definition}
    32	\newtheorem{assumption}[theorem]{Assumption}
    33	\theoremstyle{remark}
    34	\newtheorem{remark}[theorem]{Remark}
    35	
    36	\newcommand{\pF}{\mathsf{F}}
    37	\newcommand{\pP}{\mathsf{P}}
    38	\newcommand{\pJ}{\mathsf{J}}
    39	\newcommand{\pI}{\mathsf{I}}
    40	\newcommand{\pC}{\mathsf{C}}
    41	\newcommand{\pW}{\mathsf{W}}
    42	\newcommand{\Mset}{\mathcal{M}}
    43	\newcommand{\Int}{\mathcal{I}}
    44	\newcommand{\Rules}{\mathcal{R}}
    45	\newcommand{\Win}{\mathcal{W}}
    46	
    47	\title{Political Power and Rule Making\\[4pt]
    48	  {\normalsize Part II of \emph{The Six Pillars of the Beast System}}}
    49	\author{Matthew Long\\
    50	  \small The YonedaAI Collaboration, YonedaAI Research Collective\\
    51	  \small Chicago, IL\\
    52	  \small \texttt{matthew@yonedaai.com} \quad \url{https://yonedaai.com}}
    53	\date{October 2026}
    54	
    55	\begin{document}
    56	\maketitle
    57	
    58	\begin{abstract}
    59	Every governance system must settle who makes the rules. This paper treats rule making as one pillar of a six-function model of governance and separates two questions about it: whether the function is necessary, and how its control is distributed. From an axiom of plurality (members' preferences diverge, yet some choices bind everyone), together with environmental change and the persistence of the group, we prove that every persistent collective implements a rule-making function, though not any particular institution. In stateless and consensus societies the function appears as camp discussion, lineage moots, oratory without command, and fission. We measure the distribution of rule-making power with power indices over decision procedures and prove that necessity places no constraint on concentration: for a group of $n$ members and every $k$ from $1$ to $n$, some procedure satisfies the necessity lemma with concentration exactly $1/k$. Three conditional propositions describe how rule making can turn into capture: monitoring incentives that vanish as organizations grow, veto structures that protect preferential status quo rules, and appointment channels that couple rule making to courts, security services, and the economy. We compare market capitalism, communist party-states, social democracy, Islamic states, Catholic monarchies, and secular democracies on identical questions, state seven hypotheses with falsifiers, and read Revelation 13 and 17 typologically as an image of rule-making authority that admits no contest. The main limitation is that no regime is coded numerically; the comparative claims are qualitative and await preregistered measurement.
    60	\end{abstract}
    61	
    62	\section{Introduction}
    63	\label{sec:intro}
    64	
    65	Every polity answers the question of who makes the laws. A Ju/'hoansi camp answers it by talk around the fire and by the option of moving away. The Soviet Union answered it with a Politburo, a Central Committee apparatus, and a legislature that ratified what the party had decided. Bourbon France answered it with royal ordinances that the Parlements registered or remonstrated against. The Islamic Republic of Iran answers it with an elected assembly whose bills pass to a council of jurists for review. The answers differ in who holds the power, how many share it, and how it can be contested. They do not differ in whether the question must be answered.
    66	
    67	This observation is the rule-making instance of the thesis that organizes the series to which this paper belongs: the ideology changes, the institutional functions remain. The series distinguishes six functions that every governance system performs (control of resources, rule making, interpretation, legitimation, enforcement, and production) and calls the resulting structure the Hierarchy of the Beast System, after the image in Revelation 13 of authority, allegiance, and economic participation bound together \citep{largo2026hbs}. The name designates a universal structure. It is never a label for a religion, a people, a profession, a regime, or a person.
    68	
    69	Two claims must be kept apart. The first, which the series calls Proposition A, is that every functioning governance system contains the six functions and the dependencies among them. Part VII proves it in general from minimal axioms about collective life \citep{long2026formalized}. The second, Proposition B, is that the functions can become concentrated and coordinated so that independent accountability fails. Proposition B is contingent and measurable, and Proposition A does not imply it (Part VII). This paper supplies the rule-making piece of both arguments. It derives the necessity of the rule-making function from the axiom of plurality, and it studies the conditions under which rule making becomes an instrument of capture.
    70	
    71	The source framework \citep{largo2026hbs} placed legislation, regulation, adjudication, taxation, licensing, and administration in a single function of rule production. The series splits that function. Rule making, the subject here, covers the production and change of general rules and of decisions that bind the collective as a whole: legislation, executive decree, administrative rule making, party resolutions that have the force of law, and the appointment of the officials who do these things. Interpretation and adjudication of rules in particular cases belong to Part III, whose determination procedure \citep[Definition~2.3]{long2026judicial} is the interpretive counterpart of the rule-making procedure defined here. The split matters because the two activities have different failure modes. A captured legislature produces preferential rules; a captured court applies neutral rules selectively.
    72	
    73	The comparative literature on rule making is large but divided by regime. Elite and pluralist theory developed around Western democracies \citep{mosca1939,michels1915,dahl1961,mills1956}. Selectorate theory and the study of authoritarian institutions developed around autocracies \citep{bdm2003,svolik2012,gandhi2007}. Classical theories of the caliphate and of divine-right monarchy were written by participants in those orders \citep{mawardi1996,bodin1992,bossuet1990}. These literatures rarely share a metric. A reader can learn how the United States Congress responds to affluent constituents \citep{bartels2008,gilens2014} and how the Soviet nomenklatura filled posts \citep{hough1979,voslensky1984} without a common vocabulary in which to compare the two.
    74	
    75	A common vocabulary for rule making can be built from the source framework's multiplex network. Rule making becomes one layer of that network, with control shares in the layer measured by power indices over decision procedures and contestability split into five components specific to rule making. Most coupling between this layer and the others runs through an appointment channel, which this paper defines and which Parts III and V use for judges and security chiefs.
    76	
    77	The central result is a separation. From the plurality axiom, together with environmental change and the persistence of the group, every persistent collective implements a rule-making function (Section~\ref{sec:necessity}). Elementary results on power indices show that this necessity is compatible with every level of concentration from $1/n$ to $1$ (Section~\ref{sec:layer}), so the existence of rule makers says nothing about whether they can be contested. The stateless and consensus societies usually cited against the necessity claim display the function at its least concentrated, paired with cheap exit. Across six regime types the same function is held under very different sources of legitimacy, and its concentration and contestability vary independently of those sources (Section~\ref{sec:regimes}).
    78	
    79	Three mechanisms recur in that comparison: monitoring incentives that weaken as organizations grow, vetoes held by the beneficiaries of preferential rules, and appointment chains run by a single coalition. Section~\ref{sec:mechanisms} models each and identifies the check that interrupts it. Every one of those checks acts on contestability, not on the existence of rule makers.
    80	
    81	The paper does not code any regime numerically. The concentration and contestability measures for rule making are defined and the properties of the concentration measure are proved, but every comparative statement about a real polity is qualitative and rests on the cited historical and political-science literature. Numerical values for actual countries require the preregistered coding protocol of the source framework \citep{largo2026hbs}, which no Part of the series has yet carried out.
    82	
    83	\section{Rule making as a layer of the polity network}
    84	\label{sec:layer}
    85	
    86	\subsection{Shared objects}
    87	
    88	The objects in this subsection are defined in the source framework and are used here without modification \citep{largo2026hbs}. The polity at time $t$ is a directed multiplex network $G_t=(V_t,E_t)$ whose nodes are organizations or coherent actor groups. Each pillar $m\in\Mset=\{\pF,\pP,\pJ,\pI,\pC,\pW\}$, with $M=|\Mset|=6$, has an adjacency layer $A^m_t$ with edge weights $a^m_{ij,t}\in[0,1]$ that record the documented capacity of actor $i$ to constrain a feasible action of actor $j$ through mechanism $m$. A many-to-many role map assigns each actor the pillars in which it acts. Actor $i$ holds a normalized control share $s^m_{i,t}$ in pillar $m$, with $\sum_i s^m_{i,t}=1$. Concentration is the Herfindahl-Hirschman index $H_{m,t}=\sum_i (s^m_{i,t})^2$. Contestability $Q_{m,t}\in[0,1]$ summarizes transparency, appeal rights, independence, competition, and credible replacement. Unaccountable concentration is the illustrative index
    89	\begin{equation}
    90	U_t=\sum_{m\in\Mset}\omega_m H_{m,t}(1-Q_{m,t}),\qquad \omega_m\ge 0,\quad \sum_m\omega_m=1,
    91	\label{eq:U}
    92	\end{equation}
    93	with weights fixed in advance. Cross-pillar integration $C_{mn,t}\in[0,1]$ is the extent to which one coalition commands appointments, budgets, sanctions, or agenda in both $m$ and $n$, and the integration statistic is $\Int_t=\frac{2}{M(M-1)}\sum_{m<n}C_{mn,t}$, the mean over the fifteen pillar pairs. A capture link $(i\to j,m)$ requires privileged access or discretion, a resulting weakening of applicable accountability, and material evidence tying the asymmetry to an institutional output. A strong classification under the source's criterion requires both high $U_t$ and high $\Int_t$; differentiation alone never suffices \citep[Proposition~1]{largo2026hbs}. Pillar labels are written in sans-serif ($\pP$ for rule making) to keep them distinct from the integration statistic $\Int_t$ and from the role map. For the rule-making pillar the paper writes $s^{\pP}_i$, $H^{\pP}_t=H_{\pP,t}$, and $Q^{\pP}_t=Q_{\pP,t}$, dropping the time index when it plays no role. The letter $n$ is reserved below for the number of members of a collective, so a pillar other than $\pP$ is written $\ell$ and the couplings of rule making appear as $C_{\pP\ell}$.
    94	
    95	Three terms are kept apart. \emph{Unaccountable concentration} in rule making is the pillar's term $H^{\pP}(1-Q^{\pP})$ in $U_t$. A \emph{capture link} $(i\to j,\pP)$ is the dyadic relation defined above, with a general rule as its institutional output. \emph{Systemic capture} is the joint condition of high $U_t$, high $\Int_t$, and documented capture links that the series calls Proposition B. Capture, regulatory capture, and state capture as objects of the resource pillar are developed in Part I \citep[Sections~4 and~6]{long2026financial}.
    96	
    97	\subsection{The rule-making function}
    98	
    99	\begin{definition}[Rule system and collective decision]
   100	\label{def:political-power:rule-system}
   101	Let $N$ be the set of members of a collective, $|N|=n\ge 2$. A \emph{rule system} $R\in\Rules$ is a set of general prescriptions that apply to classes of persons and situations rather than to named individuals or single events. A \emph{collective decision} is a choice $x$ from a set $X$ of at least two alternatives such that the chosen alternative applies to all members at once (when to move camp, whether to go to war, which tax rate to levy). Each member $i$ ranks the alternatives by a strict linear order $\succ_i$ (complete and without indifference between distinct alternatives). Members' preferences \emph{diverge} over $X$ if no alternative is unanimously best: for every $x\in X$ some member $i$ and some $y\in X$ satisfy $y\succ_i x$. Write $R_t$ for the rule system in force at time $t$, where time runs over the integers.
   102	\end{definition}
   103	
   104	\begin{definition}[Rule-making function]
   105	\label{def:political-power:rule-making}
   106	Let $T$ be a window of consecutive periods. The rule-making function $\pP$ is \emph{implemented} in a collective over $T$ in sense (a) if some set of members or practices of the collective repeatedly selects collective decisions from sets of alternatives over which members' preferences diverge, and in sense (b) if such a practice replaces the rule system in force, $R_{t+1}\neq R_t$ for some $t$ with $t,t+1\in T$. The number of replacements in $T$ measures how often sense (b) is exercised. The selecting or replacing practice is the collective's \emph{rule-making procedure}. Its \emph{rule-making profile} records who may initiate a proposal, who must assent for it to take effect, who may block it, and who can be removed for its consequences.
   107	\end{definition}
   108	
   109	The definition locates the function in an activity, not an office. A legislature, a king in council, a party congress, a meeting of the whole camp, and a gradual change of custom under social pressure all count, provided the activity occurs. This choice is deliberate and follows the standard objection to functional analysis: the need for a function does not establish the existence of any particular institution that performs it \citep{hempel1959,merton1968}. The definition also fixes the boundary with the interpretive pillar.
   110	
   111	\begin{definition}[Boundary between rule making and interpretation]
   112	\label{def:political-power:boundary}
   113	An act belongs to $\pP$ if its output is a general rule or a collective decision, and to $\pJ$ if its output is the application of a given general rule to a particular case or dispute. Mixed institutions are split by act, not by organization.
   114	\end{definition}
   115	
   116	Table~\ref{tab:boundary} applies the boundary to cases that recur in the comparisons below. The role map of the source is many-to-many, so a single organization can act in both pillars. A constitutional court that annuls a statute applies a higher rule to a lower one and acts in $\pJ$; a legislature that responds with a constitutional amendment acts in $\pP$. Common-law courts that change a rule by precedent perform a rule-making act through an interpretive institution, and the role map records them in both pillars.
   117	
   118	\begin{table}[tbp]
   119	\centering
   120	\small
   121	\caption{Classification of mixed acts under Definition~\ref{def:political-power:boundary}. The organization appears in the first column and the act in the second.}
   122	\label{tab:boundary}
   123	\begin{tabularx}{\textwidth}{@{}L{3.6cm}Y L{1.6cm}@{}}
   124	\toprule
   125	Organization & Act & Pillar \\
   126	\midrule
   127	Bourbon Parlement & Registration of a royal edict, or remonstrance that delays it & $\pP$ (veto) \\
   128	Bourbon Parlement & Appellate judgment in a civil or criminal case & $\pJ$ \\
   129	Iranian Guardian Council & Review of a bill passed by the Majles for compatibility with Islam and the constitution & $\pP$ (veto) \\
   130	Iranian Guardian Council & Screening of candidates for elections it supervises & $\pP$ (veto over entry) \\
   131	Iranian Guardian Council & Interpretation of the constitution & $\pJ$ \\
   132	Ottoman sultan in council & Issue of a qanun regulation & $\pP$ \\
   133	Ottoman qadi court & Application of sharia or qanun to a case & $\pJ$ \\
   134	Common-law appellate court & Overruling a precedent & $\pP$ and $\pJ$ \\
   135	Communist party committee & Appointment of a judge or prosecutor & $\pP$ (appointment) \\
   136	\bottomrule
   137	\end{tabularx}
   138	\end{table}
   139	
   140	\subsection{Control shares from decision procedures}
   141	
   142	The source framework defines $s^m_{i,t}$ as a normalized share of decision-relevant control but leaves its measurement open. For rule making a natural baseline is available. A rule-making procedure is, at a minimum, a specification of which coalitions can enact a proposal against the status quo. The baseline below models each decision as such a binary vote. When a decision involves three or more alternatives, an agenda rule determines which proposals are put against the status quo and in what order; that rule is the object of agenda control (Definition~\ref{def:political-power:agenda-control}) and is measured separately. Power indices from cooperative game theory turn the specification of winning coalitions into shares that sum to one.
   143	
   144	\begin{definition}[Simple game and Shapley-Shubik shares]
   145	\label{def:political-power:shares}
   146	A \emph{simple game} on $N$ is a family $\Win$ of winning coalitions with $N\in\Win$, $\emptyset\notin\Win$, and $S\in\Win$, $S\subseteq S'$ implying $S'\in\Win$. The game is \emph{proper} if $S\in\Win$ implies $N\setminus S\notin\Win$, so that two disjoint coalitions cannot both enact incompatible decisions; a rule-making procedure is represented by a proper simple game. An ordering of $N$ is a bijection $\pi:\{1,\dots,n\}\to N$, and $B_\pi(i)=\{\pi(k):k<\pi^{-1}(i)\}$ is the set of members who precede $i$. Member $i$ is \emph{the pivot} in $\pi$ if $B_\pi(i)\notin\Win$ and $B_\pi(i)\cup\{i\}\in\Win$. The Shapley-Shubik share of $i$ is $\varphi_i=|\{\pi: i \text{ is the pivot in } \pi\}|/n!$ \citep{shapley1954}. Member $i$ is a \emph{veto player} if $i\in S$ for every $S\in\Win$, and a \emph{dictator} if $\{i\}\in\Win$ and every winning coalition contains $i$.
   147	\end{definition}
   148	
   149	The de jure baseline sets $s^{\pP}_i=\varphi_i$. Actual control can depart from the baseline when an agenda setter, an informal patron, or a donor shapes which proposals reach a vote, and the gap between de jure and de facto power is itself an object of study \citep{acemoglu2006}. The baseline is still useful, because it ties concentration to the written or customary procedure and so gives a reference point against which informal concentration can be measured.
   150	
   151	\begin{proposition}[Concentration under standard procedures]
   152	\label{prop:political-power:concentration}
   153	Let $\Win$ be a simple game on $N$ with $|N|=n$, and set $s^{\pP}_i=\varphi_i$ and $H^{\pP}=\sum_i\varphi_i^2$.
   154	\begin{enumerate}[label=(\alph*)]
   155	\item In every ordering exactly one member is the pivot, so $\sum_i\varphi_i=1$.
   156	\item $1/n\le H^{\pP}\le 1$, with $H^{\pP}=1/n$ if and only if $\varphi_i=1/n$ for every $i$.
   157	\item If $\Win$ is invariant under every permutation of $N$ (an anonymous procedure such as a quota rule with quota above $n/2$, or unanimity among all members), then $H^{\pP}=1/n$.
   158	\item If $\Win=\{S: K\subseteq S\}$ for a nonempty $K\subseteq N$ with $|K|=k$ (unanimity among the members of $K$), then $H^{\pP}=1/k$. A dictatorship is the case $k=1$.
   159	\item A veto player $i$ satisfies $\varphi_i\ge\varphi_j$ for every $j\in N$.
   160	\end{enumerate}
   161	\end{proposition}
   162	
   163	\begin{proof}
   164	(a) Fix $\pi$ and add members in the order $\pi$. The growing coalition starts at $\emptyset\notin\Win$ and ends at $N\in\Win$. By monotonicity, once the coalition is winning it remains winning, so it changes from losing to winning at exactly one step, and the member added at that step is the unique pivot. Summing over the $n!$ orderings gives $\sum_i\varphi_i=1$.
   165	
   166	(b) By the Cauchy-Schwarz inequality, $1=(\sum_i\varphi_i)^2\le n\sum_i\varphi_i^2$, with equality if and only if all $\varphi_i$ are equal. The upper bound holds because $\varphi_i\in[0,1]$ and $\sum_i\varphi_i=1$ imply $\sum_i\varphi_i^2\le\sum_i\varphi_i=1$.
   167	
   168	(c) If $\sigma$ is a permutation of $N$ and $\Win$ is invariant under $\sigma$, then $B_{\sigma\circ\pi}(\sigma(i))=\sigma(B_\pi(i))$, so $i$ is the pivot in $\pi$ if and only if $\sigma(i)$ is the pivot in $\sigma\circ\pi$. Composition with $\sigma$ is a bijection on orderings, so $\varphi_i=\varphi_{\sigma(i)}$. Every pair of members is exchanged by some permutation, so all shares are equal and (b) gives $H^{\pP}=1/n$.
   169	
   170	(d) A member outside $K$ is never the pivot, because adding a member outside $K$ cannot complete $K$. In any ordering the pivot is the last member of $K$ to appear. By symmetry among the members of $K$, each is last in a fraction $1/k$ of orderings. Hence $\varphi_i=1/k$ for $i\in K$, $\varphi_i=0$ otherwise, and $H^{\pP}=k\cdot(1/k)^2=1/k$.
   171	
   172	(e) Let $j\neq i$ and let $j$ be the pivot in $\pi$. Then $B_\pi(j)\cup\{j\}\in\Win$ contains the veto player $i$, and $i\neq j$, so $i\in B_\pi(j)$. Let $\pi'$ be $\pi$ with the positions of $i$ and $j$ exchanged. In $\pi'$ the set preceding $i$ is $B_\pi(j)\setminus\{i\}\cup\{j\}$, which does not contain $i$ and is therefore losing. Adding $i$ yields $B_\pi(j)\cup\{j\}$, which is winning. So $i$ is the pivot in $\pi'$. The exchange is a bijection on orderings, so the number of orderings in which $j$ is the pivot is at most the number in which $i$ is the pivot.
   173	\end{proof}
   174	
   175	Properness is not needed for the proofs, and every game used below is proper. Part (d) connects concentration to the veto-player tradition: when only the members of $K$ matter and each can block, concentration equals the reciprocal of the number of veto players \citep{tsebelis2002}. Part (c) shows that the anonymous procedures attributed to consensus societies produce the least concentrated rule making possible for their size. The next corollary records that the existence of a rule-making procedure says nothing about its concentration.
   176	
   177	\begin{corollary}[Necessity does not fix concentration]
   178	\label{cor:political-power:any-h}
   179	For every $n\ge2$ and every $k\in\{1,\dots,n\}$ there is a rule-making procedure on $n$ members with $H^{\pP}=1/k$.
   180	\end{corollary}
   181	
   182	\begin{proof}
   183	Take any $K\subseteq N$ with $|K|=k$ and the unanimity game on $K$ from Proposition~\ref{prop:political-power:concentration}(d), with the status quo as the default when no proposal wins and proposals put against the status quo one at a time by a fixed agenda rule. Each vote has a determinate outcome, so the procedure selects a collective decision in every case, and so implements $\pP$ in the sense of Definition~\ref{def:political-power:rule-making}, whatever the value of $k$.
   184	\end{proof}
   185	
   186	The corollary is the rule-making instance of the general non-implication proved in Part VII: the existence of the function (Proposition A) is compatible with any degree of concentration, so concentration (one ingredient of Proposition B) must be established by evidence about the particular polity.
   187	
   188	\subsection{Worked examples}
   189	
   190	The index can be computed for any procedure whose winning coalitions are known. Table~\ref{tab:examples} reports four stylized procedures, the last under two aggregations of actors, with organizations or parties treated as unitary actors. The first two show that the same chamber can produce opposite concentrations depending on the distribution of seats. If one party holds a majority in a chamber that is the only veto player and the party votes as a bloc, the party is a dictator and $H^{\pP}=1$. If three parties hold 40, 35, and 25 percent of the seats under majority rule, any two of them form a majority, the game is anonymous among the three parties, and $H^{\pP}=1/3$ by Proposition~\ref{prop:political-power:concentration}(c). Two chambers and an executive with an absolute veto form a unanimity game on three actors, so $H^{\pP}=1/3$ by part (d).
   191	
   192	The fourth procedure is modeled on the legislative articles of the constitution of the Islamic Republic of Iran \citep{iranconst}. A bill passed by the Majles ($M$) becomes law if the Guardian Council ($G$) approves it, or, if the Council rejects it and the Majles insists, if the Expediency Council ($E$) sides with the Majles. The winning coalitions are therefore $\{M,G\}$, $\{M,E\}$, and $\{M,G,E\}$, and the game is proper. Of the six orderings, $M$ is the pivot in four and $G$ and $E$ in one each, so $\varphi=(2/3,1/6,1/6)$ and $H^{\pP}=1/2$. The constitution also gives the Leader the selection of the six clerical members of the Guardian Council and the appointment of the members of the Expediency Council \citep{iranconst}. If $G$ and $E$ are treated as a single coalition through that appointment channel, the game becomes unanimity between the Majles and the coalition, and $\varphi=(1/2,1/2)$. Concentration is again $1/2$, but the share of the appointed bodies rises from $1/3$ to $1/2$. The example shows that $H^{\pP}$ depends on how actors are aggregated, which is why the actor list must be fixed before coding, and that the appointment channel can shift shares without changing the formal procedure. It omits the Leader's power to set general policy and the Council's screening of candidates for the Majles, both of which raise practical concentration above the de jure figure.
   193	
   194	Values of $H^{\pP}$ are comparable only at a declared level of aggregation. At the \emph{member level} the players are individuals, as in the consensus band of Proposition~\ref{prop:political-power:minimal-form}, where $H^{\pP}=1/n_a$. At the \emph{organ level} the players are chambers, councils, parties voting as blocs, or the electorate in a referendum, as in Table~\ref{tab:examples}. An organ-level figure of $1/3$ and a member-level figure of $1/40$ do not measure the same thing, and the comparisons in this paper are made within a level, never across levels. Where both levels matter, each organ's decision can itself be modeled as a game among its members, so that member-level shares are computed through the organ-level procedure; the paper does not pursue that construction.
   195	
   196	\begin{table}[tbp]
   197	\centering
   198	\small
   199	\caption{De jure Shapley-Shubik shares and concentration for four stylized rule-making procedures. Actors are treated as unitary; the figures illustrate the index and are not estimates for any polity.}
   200	\label{tab:examples}
   201	\begin{tabularx}{\textwidth}{@{}YL{3.6cm}L{1.4cm}@{}}
   202	\toprule
   203	Procedure & Shares & $H^{\pP}$ \\
   204	\midrule
   205	Single-party majority in the only veto chamber & $(1,0,\dots,0)$ & $1$ \\
   206	Three parties with 40, 35, and 25 percent of seats under majority rule & $(1/3,1/3,1/3)$ & $1/3$ \\
   207	Two chambers and an executive with an absolute veto & $(1/3,1/3,1/3)$ & $1/3$ \\
   208	Majles, Guardian Council, and Expediency Council as separate actors & $(2/3,1/6,1/6)$ & $1/2$ \\
   209	Majles and an appointed bloc of the two councils & $(1/2,1/2)$ & $1/2$ \\
   210	\bottomrule
   211	\end{tabularx}
   212	\end{table}
   213	
   214	\subsection{Contestability of rule making}
   215	
   216	The source's contestability index $Q_{m,t}$ is generic. For rule making five components can be distinguished and measured separately.
   217	
   218	\begin{definition}[Components of rule-making contestability]
   219	\label{def:political-power:qp}
   220	For a polity at time $t$, let $q_t=(q^{\mathrm{rep}},q^{\mathrm{ovs}},q^{\mathrm{ent}},q^{\mathrm{trn}},q^{\mathrm{ext}})\in[0,1]^5$ record, in order, the credibility of peaceful replacement of rule makers; the strength of oversight of rule makers by bodies they do not control; the freedom of entry into rule-making competition (forming parties, standing for office, petitioning); the transparency of rule making (publication of drafts, records of who proposed what); and the ease of exit from the jurisdiction or the group, so that cheap exit scores high. The rule-making contestability is $Q^{\pP}_t=g(q_t)$ for a preregistered aggregator $g:[0,1]^5\to[0,1]$ that is nondecreasing in each argument with $g(0,\dots,0)=0$ and $g(1,\dots,1)=1$.
   221	\end{definition}
   222	
   223	The exit component draws on the analysis of exit and voice that Part VI develops for the series \citep{long2026productive}. Two aggregators bracket the reasonable choices. The arithmetic mean treats the components as substitutes, so strong exit can compensate for absent elections. The geometric mean treats them as complements, so that any component at zero sets $Q^{\pP}$ to zero. The choice changes rankings in exactly the cases that interest the comparison. A foraging band has very cheap exit and open entry into discussion but no formal oversight body; a single-party state may publish drafts and permit petitions while ruling out replacement. Under the geometric mean both score low unless oversight in the band is coded to include direct observation of everyone by everyone. This is a concrete form of the measurement-invariance problem that the source framework raises for all its constructs \citep{largo2026hbs}, and it is why the aggregator must be fixed before coding begins.
   224	
   225	\subsection{Appointment channel and agenda control}
   226	
   227	Most coupling between rule making and the other pillars runs through two channels: the power to appoint the people who exercise the other functions, and the power to decide which questions reach a decision at all.
   228	
   229	\begin{definition}[Appointment channel]
   230	\label{def:political-power:appointment-channel}
   231	For a pillar $\ell\in\Mset$ (the letter $n$ is reserved for the size of a collective; see Section~\ref{sec:layer}), let $O_\ell$ be the set of offices that exercise decision-relevant control in $\ell$, with weights $w_o\ge0$ and $\sum_{o\in O_\ell}w_o=1$ equal to each office's control share. For a coalition $S$, the \emph{appointment share} of $S$ in $\ell$ is
   232	\[
   233	\alpha_{S,\ell}=\sum_{o\in O_\ell}w_o\,\mathbf{1}[S \text{ can unilaterally appoint or remove the holder of } o].
   234	\]
   235	The appointment channel from $\pP$ to $\ell$ is the map $S\mapsto\alpha_{S,\ell}$.
   236	\end{definition}
   237	
   238	The appointment channel is the instrument through which, in the source's account, party-state control paths run from central appointment to allocation and enforcement \citep[Proposition~3]{largo2026hbs}. Parts III and V use the same object for judges and for security chiefs. The word ``unilaterally'' matters. Where an appointment requires the consent of a second body, as in legislative confirmation, no single coalition's share includes that office unless it controls both bodies.
   239	
   240	\begin{definition}[Agenda control]
   241	\label{def:political-power:agenda-control}
   242	An actor exercises \emph{agenda control} in $\pP$ to the extent that it determines which proposals are considered by the rule-making procedure. A \emph{non-decision} is a proposal that some members want considered and that is kept from consideration by an actor with agenda control \citep{bachrach1962}.
   243	\end{definition}
   244	
   245	Agenda control is the second face of power in the classification of Bachrach and Baratz, and the third face, the shaping of preferences themselves, belongs to Part IV \citep{lukes2005}. Agenda control is invisible to the Shapley-Shubik baseline, which takes the set of proposals as given. This is one reason why the de jure shares of Definition~\ref{def:political-power:shares} are a lower bound on the concentration of actual rule-making power whenever agenda setting is itself concentrated.
   246	
   247	\subsection{Couplings to the other pillars}
   248	
   249	Under the series' allocation of the fifteen pillar pairs, this paper gives the primary treatment of four: rule making with interpretation ($C_{\pP\pJ}$), with legitimation ($C_{\pP\pI}$), with enforcement ($C_{\pP\pC}$), and with production ($C_{\pP\pW}$). The pair with resource control, $C_{\pF\pP}$, belongs to Part I \citep{long2026financial}. Each pair has a characteristic channel.
   250	
   251	Whoever appoints and removes judges couples rule making to interpretation, and so does the traffic between statute and precedent. Statutes give courts rules to apply, and judicial applications generate precedents and doctrines that legislatures then codify, override, or leave in place. A coalition that appoints judges without confirmation by another body and can remove them at will drives $\alpha_{S,\pJ}$ toward one.
   252	
   253	Legitimation enters rule making through the rule of recognition, which Part IV defines \citep[Definition~2.2]{long2026ideological}: rules count as law because officials and subjects accept criteria that identify them as law \citep{hart1961}. Rule makers seek legitimation through religious, ideological, and electoral claims, and they can also shape the information environment directly. Recent work argues that many contemporary autocrats rely more on the manipulation of information than on mass repression to sustain their hold on rule making \citep{guriev2019}.
   254	
   255	Civilian control of the coercive apparatus, the appointment of its commanders, and the rules that govern its use tie rule making to enforcement. Weber defined the state by its successful claim to a monopoly of legitimate force within a territory \citep{weber1946}, and the claim is made in rules. Part V analyzes the apparatus, including the coup-proofing strategies by which rulers divide it \citep[Proposition~6.3]{long2026coercive}. This paper treats the appointment of security chiefs as part of the appointment channel and leaves coup-proofing and the conduct of policing to Part V.
   256	
   257	The rules of work, taxation, and property, and the producers' organizations that help to make them, connect rule making to production. Labor law, tax codes, and the legal status of unions are outputs of $\pP$ that set the terms on which the productive population works. In corporatist systems, organized labor and employers take part in drafting the rules that govern them, which raises $C_{\pP\pW}$ by design and with the consent of the organized parties.
   258	
   259	\section{Necessity of the rule-making function}
   260	\label{sec:necessity}
   261	
   262	\subsection{Assumptions of the lemma}
   263	
   264	The working axiom for this pillar in the series is plurality: members' preferences diverge, yet collective choices are made. Part VII refines the full axiom set and proves the general theorem. Here the axiom is stated in the form needed for the rule-making lemma, together with two further assumptions that make its content explicit.
   265	
   266	\begin{assumption}[Plurality]
   267	\label{ass:political-power:plurality}
   268	The collective repeatedly faces collective decisions in the sense of Definition~\ref{def:political-power:rule-system}, and for each such decision the members' preferences diverge over the alternatives: for every alternative $x\in X$ some member strictly prefers another alternative $y\in X$ to $x$.
   269	\end{assumption}
   270	
   271	\begin{assumption}[Environmental change]
   272	\label{ass:political-power:change}
   273	The environment $e_t\in E$ of the collective varies over time. There is a viability correspondence $\mathcal{V}:E\to 2^{\Rules}$, where $\mathcal{V}(e)$ is the set of rule systems under which the collective survives a period in environment $e$, and the realized path contains periods $s_0<s_1<\dots<s_r$, with $r\ge1$, such that consecutive viability sets are disjoint: $\mathcal{V}(e_{s_{j-1}})\cap\mathcal{V}(e_{s_j})=\emptyset$ for $j=1,\dots,r$.
   274	\end{assumption}
   275	
   276	\begin{assumption}[Self-government and persistence]
   277	\label{ass:political-power:persistence}
   278	(i) The collective's decisions and changes in its rules are produced by practices of its members rather than imposed from outside. (ii) The collective persists over a window $T$ of consecutive periods that contains $s_0$ and $s_r$, so $R_t\in\mathcal{V}(e_t)$ for all $t\in T$.
   279	\end{assumption}
   280	
   281	The plurality assumption is empirical. It fails for a group whose members always agree on every collective choice, which no ethnography or history records for any group of more than a few people over any length of time. The change assumption formalizes the condition under which a regime of fixed rules becomes untenable. Hart called a regime of primary rules without a rule of change \emph{static} and listed this as one of its three defects \citep{hart1961}; the assumption states when the defect becomes fatal rather than merely costly. The self-government clause excludes a group whose rules are set entirely by an outside power. Such a group does not falsify the necessity of rule making; it shows that the rule maker lies outside the boundary drawn around the group, and the boundary should be redrawn to include it.
   282	
   283	\begin{lemma}[Collective choice requires a procedure]
   284	\label{lem:political-power:choice}
   285	Under Assumption~\ref{ass:political-power:plurality} and clause (i) of Assumption~\ref{ass:political-power:persistence}, every realized collective decision is ranked below some other alternative by at least one member. The practice that produces the realized decision therefore selects among divergent preferences, and the collective implements part (a) of Definition~\ref{def:political-power:rule-making}.
   286	\end{lemma}
   287	
   288	\begin{proof}
   289	Let $x^\ast$ be the alternative realized in a collective decision. By Assumption~\ref{ass:political-power:plurality} there is a member $i$ and an alternative $y$ with $y\succ_i x^\ast$. Because the decision applies to all members at once, $i$ cannot obtain $y$ while others obtain $x^\ast$. Some practice, whether a vote, a command, a discussion that ends when objectors fall silent, or a default to the status quo, determined that $x^\ast$ rather than $y$ would hold for everyone, and by clause (i) of Assumption~\ref{ass:political-power:persistence} that practice is the members' own. That practice selects among divergent preferences. Collective decisions recur by assumption, so such selections recur.
   290	\end{proof}
   291	
   292	\begin{lemma}[Change requires a rule of change]
   293	\label{lem:political-power:change}
   294	Under Assumptions~\ref{ass:political-power:change} and~\ref{ass:political-power:persistence}, the rule system is replaced at least $r$ times on $T$: for each $j=1,\dots,r$ there is $t$ with $s_{j-1}\le t<s_j$ and $R_{t+1}\neq R_t$. Each replacement is produced by a practice of the members.
   295	\end{lemma}
   296	
   297	\begin{proof}
   298	Fix $j$ and suppose $R_t=R_{t+1}$ for every $t$ with $s_{j-1}\le t<s_j$. Then $R_{s_{j-1}}=R_{s_j}=R$. Clause (ii) of Assumption~\ref{ass:political-power:persistence} gives $R\in\mathcal{V}(e_{s_{j-1}})$ and $R\in\mathcal{V}(e_{s_j})$, which contradicts the disjointness in Assumption~\ref{ass:political-power:change}. So some $t$ in $[s_{j-1},s_j)$ has $R_{t+1}\neq R_t$, and both $t$ and $t+1$ lie in $T$ because $T$ consists of consecutive periods containing $s_0$ and $s_r$. The intervals $[s_{j-1},s_j)$ are disjoint, so the $r$ replacements are distinct. By clause (i) of Assumption~\ref{ass:political-power:persistence} each is produced by the members' practices.
   299	\end{proof}
   300	
   301	Hart's term for the practice whose existence Lemma~\ref{lem:political-power:change} establishes is the rule of change. The series assigns this member of Hart's triad of secondary rules to the rule-making pillar; the rule of adjudication belongs to Part III and the rule of recognition to Part IV (Definition~2.2 of that Part).
   302	
   303	\begin{definition}[Rule of change]
   304	\label{def:political-power:rule-of-change}
   305	A \emph{rule of change} of a collective is a secondary rule, written or customary, that identifies who may introduce, alter, or repeal the collective's general rules and by what procedure \citep{hart1961}. It is the rule-making procedure of Definition~\ref{def:political-power:rule-making}(b) considered as a rule accepted by the members rather than as a regularity observed from outside.
   306	\end{definition}
   307	
   308	\begin{theorem}[Necessity of rule making]
   309	\label{thm:political-power:necessity}
   310	A collective that satisfies Assumption~\ref{ass:political-power:plurality} and clause (i) of Assumption~\ref{ass:political-power:persistence} implements the rule-making function in sense (a). If it also satisfies Assumptions~\ref{ass:political-power:change} and~\ref{ass:political-power:persistence}, it implements the function in sense (b), with at least $r$ replacements of the rule system on $T$. Whenever a replacement is chosen from the viable set $\mathcal{V}(e_{t+1})$ and members' preferences diverge over that set in the sense of Definition~\ref{def:political-power:rule-system}, the replacement is itself a selection among divergent preferences.
   311	\end{theorem}
   312	
   313	\begin{proof}
   314	The first statement is Lemma~\ref{lem:political-power:choice}. The second is Lemma~\ref{lem:political-power:change}. For the third, apply Lemma~\ref{lem:political-power:choice} to the choice of $R_{t+1}$ from $\mathcal{V}(e_{t+1})$, treating the choice of a rule system as a collective decision.
   315	\end{proof}
   316	
   317	The proofs are short because the work is done by the assumptions. This is the correct place for the work to be done. The theorem asserts that an activity must occur, not that an institution must exist. It would be false if a persistent collective could make its binding choices without any practice that selects among divergent preferences, or if it could survive incompatible environments without changing its rules. Each of these is an empirical possibility that the hard cases below test.
   318	
   319	\subsection{Scope of the lemma}
   320	
   321	The theorem makes $\pP$ a thin predicate, and a thin predicate invites the charge of vacuity. If anything that happens counts as rule making, the necessity claim is empty. Three things are excluded.
   322	
   323	A collective decision made by a fixed external rule (a lottery imposed by an outside authority, or a decision by the environment itself, such as a drought that forces a move) is excluded by the self-government clause. A rule change that is purely exogenous, such as the imposition of colonial law on a subject people, is excluded for the same reason and relocates the rule maker rather than eliminating it. Most importantly, the predicate excludes a group whose rules never change while the environment does. The falsifier of the theorem is therefore specific: a long-lived group, satisfying the plurality assumption, whose rules never changed and could not be changed by any of its members, through a sequence of environments that no single rule system could survive.
   324	
   325	The theorem says nothing about how rule making is distributed, how it is legitimated, or whether it is accountable. Corollary~\ref{cor:political-power:any-h} shows that the same function can be performed with concentration anywhere from $1/n$ to $1$.
   326	
   327	\subsection{Minimal form in stateless and consensus societies}
   328	
   329	The societies most often cited as lacking government are the test set for the theorem. If rule making is necessary, each should show it in some informal, distributed form. If any shows no rule-making activity at all, the theorem is in trouble.
   330	
   331	Among the Ju/'hoansi of the Kalahari, camp-level decisions about movement, sharing, and conflict are reached through extended public talk in which adults participate and no one has authority to command \citep{lee2013}. Wiessner's analysis of recorded conversations shows that much of this talk consists of criticism and joking directed at people who violate norms of sharing and modesty \citep{wiessner2005}. When disagreement cannot be resolved, people move to another camp. Fission is a rule-change practice of a particular kind: it does not change the rules of the existing group but creates a new group whose rules differ.
   332	
   333	Evans-Pritchard described the Nuer as an ``ordered anarchy'' with no government in the sense of a political authority able to command \citep{evanspritchard1940}. Their political order rested on the balanced opposition of lineage segments. Rules about bridewealth, compensation, and the use of grazing were maintained and adjusted through negotiation among kin groups, through the settlements of disputes, and through the influence of persons whose standing rested on persuasion rather than command. The leopard-skin chief who mediated in cases of homicide belongs to the interpretive pillar and is treated in Part III.
   334	
   335	Clastres argued from Amazonian ethnography that the chief in many lowland South American societies had no power to command, that his speech was an obligation rather than an instrument of rule, and that a chief who tried to give orders would be abandoned \citep{clastres1987}. Clastres's thesis is that such societies actively prevent political power from separating from the group. The thesis is consistent with the necessity theorem. Decisions are still made, by the group, and the chief's oratory is part of how they are made.
   336	
   337	Boehm's survey of foraging societies found a reverse dominance hierarchy: the adult members, acting as a coalition, suppress any individual who tries to dominate, using ridicule, disobedience, ostracism, and in extreme cases killing \citep{boehm1999}. Boehm emphasizes that egalitarianism of this kind is a political achievement. The group decides collectively and enforces the decision against would-be leaders. Woodburn reached a compatible conclusion for immediate-return societies such as the Hadza: their equality is produced by institutions of leveling that prevent the accumulation of power and property \citep{woodburn1982}.
   338	
   339	Ostrom's study of long-lived common-pool resource institutions supplies a different kind of case: small communities that govern a shared resource without a state and without private property \citep{ostrom1990}. Among the design principles she identified is that most individuals affected by the operational rules can participate in modifying them. The principle is a rule-making arrangement in the exact sense of Definition~\ref{def:political-power:rule-making}(b). Reviews of later case studies have found broad support for the principles \citep{cox2010}, and Ostrom's later work describes how such arrangements nest within larger polycentric systems \citep{ostromdesign2010}.
   340	
   341	\begin{proposition}[Minimal form of rule making]
   342	\label{prop:political-power:minimal-form}
   343	Let $N_a\subseteq N$ be the adult members of a group, $|N_a|=n_a\ge2$, and let the group make collective decisions by consensus, modeled as unanimity among the adults (a proposal wins exactly when every member of $N_a$ assents), with the status quo $q$ as default. Let each adult $i$ have a strict linear order $\succ_i$ over alternatives and assent to a proposal $x$ against $q$ if and only if $x\succ_i q$. Then:
   344	\begin{enumerate}[label=(\alph*)]
   345	\item the de jure concentration of rule making is $H^{\pP}=1/n_a$, the minimum possible for a procedure in which only adults' consent counts, and the minimum for the whole group when $N_a=N$;
   346	\item the set of alternatives that can replace $q$ is the set of strict Pareto improvements for the adults, $\{x: x\succ_i q \text{ for all } i\in N_a\}$, which is empty whenever $q$ is Pareto optimal among them;
   347	\item let the group be able to split, with each subgroup $N_1\subseteq N_a$ of at least two adults deciding by consensus for itself. A subgroup can replace $q$ if and only if all its members strictly prefer a common alternative $x$ to $q$, so some subgroup can do so if and only if at least two adults strictly prefer a common alternative to $q$. This condition can hold when $q$ is Pareto optimal among all adults.
   348	\end{enumerate}
   349	\end{proposition}
   350	
   351	\begin{proof}
   352	(a) The procedure is the unanimity game on $K=N_a$, so Proposition~\ref{prop:political-power:concentration}(d) gives $\varphi_i=1/n_a$ for adults, $\varphi_i=0$ for others, and $H^{\pP}=1/n_a$. Any procedure in which only adults can be the pivot has shares summing to one over $N_a$, so Proposition~\ref{prop:political-power:concentration}(b) applied to $N_a$ shows that $1/n_a$ is the minimum. (b) Under unanimity an alternative replaces $q$ only if every adult prefers it to $q$, which is the definition of a strict Pareto improvement among the adults. If $q$ is Pareto optimal among them, no alternative is strictly preferred to $q$ by every adult, so the set is empty. (c) Apply (b) to $N_1$: its consensus winset is $\{x: x\succ_i q\text{ for all }i\in N_1\}$, which is nonempty exactly when its members share an alternative they all prefer to $q$. If two adults $i,j$ both prefer some $x$ to $q$, the subgroup $\{i,j\}$ qualifies; conversely any qualifying subgroup contains two such adults. For the last claim, take three adults with $x\succ_1 q$, $x\succ_2 q$, and $q\succ_3 y$ for every $y\neq q$: then $q$ is Pareto optimal among all three, yet $\{1,2\}$ can adopt $x$.
   353	\end{proof}
   354	
   355	The proposition gives a formal reason for an ethnographic regularity. Consensus produces the least concentrated rule making possible, and it also produces the most status-quo-biased rule making possible, because every adult is a veto player. A consensus society facing a changing environment therefore needs another way to change its rules when no change is a Pareto improvement. Fission supplies it. The pairing of consensus decision making with cheap exit, documented among the Ju/'hoansi and in Woodburn's immediate-return societies, is what Proposition~\ref{prop:political-power:minimal-form} predicts. In the vocabulary of Definition~\ref{def:political-power:qp}, such groups combine minimal concentration with very high exit and entry components of contestability.
   356	
   357	Formal consensus sets only a lower bound on the concentration of rule making in these societies. Even where every adult can block a decision, differences in age, gender, skill, and kinship give some speakers more weight in discussion than others, so actual concentration exceeds the de jure figure $1/n_a$. The equal-share coding describes the procedure, not the distribution of influence within it.
   358	
   359	Across the ethnographic and historical record, collective decisions are made and rules change, while the concentration of rule making varies. Graeber and Wengrow argue that prehistoric societies moved deliberately between egalitarian and hierarchical arrangements, sometimes by season \citep{graeber2021}. Scott describes upland peoples of Southeast Asia who kept rule making dispersed to avoid incorporation by lowland states \citep{scott2009}, and early states in which it became concentrated \citep{scott2017}. Both readings are disputed, and the record itself overrepresents groups observed in the nineteenth and twentieth centuries, many in marginal environments and in contact with states, among foragers who vary widely \citep{kelly1995}. None of these qualifications touches the pattern that matters here: what varies is who makes the rules, not whether they are made.
   360	
   361	\subsection{Custom without legislators}
   362	
   363	The strongest objection to the theorem is not a stateless society but an argument about how rules come into being. Hayek distinguished law that grows out of practice, discovered and articulated rather than made, from legislation deliberately enacted by an authority, and he argued that much of the order of a society rests on the former \citep{hayek1973}. Ellickson's study of cattle ranchers in Shasta County, California, showed that neighbors settled trespass disputes by informal norms that diverged from the formal law and that the norms adjusted over time without recourse to it \citep{ellickson1991}. If rules can evolve without anyone making them, the rule-making function may be unnecessary.
   364	
   365	The objection narrows the theorem but does not defeat it. The theorem requires a practice that selects collective decisions and replaces rules, not a legislator. Evolved custom changes through practices: some members deviate, others imitate or sanction the deviation, and social pressure settles on a new regularity. Ellickson's ranchers are rule makers in this distributed sense. The norms change because particular neighbors propose, test, and enforce new expectations through gossip, reciprocity, and occasional self-help. The function is performed; the office is absent.
   366	
   367	The objection still shows something important. Under customary rule change, the rule-making profile of Definition~\ref{def:political-power:rule-making} is diffuse and difficult to observe, and control shares cannot be read from a written procedure. The power-index baseline does not apply, and concentration must be estimated from who in fact initiates and enforces changes. This is a measurement limitation of the paper's framework, not a counterexample to the theorem.
   368	
   369	\subsection{Functional explanation and its limits}
   370	
   371	The theorem is a statement about the conditions under which a collective persists. It is not a functional explanation of why any particular rule-making institution exists. Hempel showed that an inference from the need for a function to the presence of a particular institution commits the fallacy of affirming the consequent, because functional equivalents can meet the same need \citep{hempel1959}. Elster argued that explaining an institution by its beneficial consequences requires a feedback mechanism through which the consequences maintain the institution \citep{elster1983}. The theorem respects both constraints. It claims the necessity of an activity, it allows any institution or none to perform it, and it does not explain the existence of the Parlement of Paris, the Politburo, or the Majles by their contribution to the persistence of their polities. Those institutions have histories, and the comparative section treats them as historical products whose relation to the function is a matter of evidence.
   372	
   373	\section{Literature on rule-making power}
   374	\label{sec:literature}
   375	
   376	\subsection{Elite, pluralist and structural theories}
   377	
   378	The oldest question about rule making is whether a minority always makes the rules. Mosca held that in every society an organized minority rules an unorganized majority, and that the minority's advantage lies in its organization rather than in its numbers \citep{mosca1939}. Michels drew the same conclusion from the internal life of the German Social Democratic Party: organization requires delegation, delegation creates leaders with expertise and control of communication, and leaders entrench themselves even in organizations committed to democracy \citep{michels1915}. Mills extended the elite argument to the postwar United States, describing an interlocking set of corporate, military, and political leaders \citep{mills1956}.
   379	
   380	Pluralists denied that the elite claim had been demonstrated. Dahl's study of New Haven found that different actors prevailed in different issue areas and that no single group controlled decisions across them \citep{dahl1961}. His later account of polyarchy defined democracy by two dimensions, the inclusiveness of participation and the extent of public contestation \citep{dahl1971}. These two dimensions anticipate the separation in this paper between the distribution of rule-making shares and the contestability of rule making.
   381	
   382	A third position holds that rule makers need not be controlled by a class to serve it. Lindblom argued that business occupies a privileged position in market societies because governments depend on business investment for economic performance, so that rule makers anticipate business reactions without being directed \citep{lindblom1977}. Winters defined oligarchy as the political use of concentrated wealth for wealth defense and showed that oligarchs can coexist with electoral democracy \citep{winters2011}. Structural arguments of this kind imply that integration between resource control and rule making, $C_{\pF\pP}$, can be high even when no capture link in the source's sense can be documented. They therefore pose a measurement problem for the framework that Part I examines in detail.
   383	
   384	The empirical debate has moved to policy responsiveness. Gilens and Page estimated, on a dataset of 1,779 policy questions, that the preferences of economic elites and organized business groups have substantial independent associations with policy outcomes in the United States while the preferences of average citizens have little \citep{gilens2014}. Bartels found that senators' votes were more responsive to affluent constituents than to poor ones \citep{bartels2008}. Branham, Soroka, and Wlezien found that the preferences of the affluent and the middle class usually coincide and that, when they diverge, the affluent prevail only modestly more often \citep{branham2017}. Elkjaer and Klitgaard review the comparative evidence on unequal responsiveness and its methods \citep{elkjaer2024}. The disagreement concerns the size and the generality of a bias, not its direction in the American case.
   385	
   386	\subsection{Faces of power and agenda control}
   387	
   388	Bachrach and Baratz argued that the pluralist method of studying observable decisions misses the power exercised by keeping issues off the agenda \citep{bachrach1962}. Lukes added a third dimension, the shaping of preferences so that conflicts of interest never surface as grievances \citep{lukes2005}. For rule making the second face is central and measurable in principle: a non-decision leaves traces in proposals that were drafted and never scheduled, in petitions that went unanswered, and in committee chairs who declined to act. The third face shades into the legitimation pillar and is left to Part IV.
   389	
   390	Culpepper's study of corporate control in Europe and Japan gives the agenda argument an empirical form. Business influence over the rules of corporate governance was greatest on issues of low public salience, where legislators relied on managers' expertise and the press paid little attention \citep{culpepper2010}. Hall and Deardorff model lobbying as a subsidy of information and labor given to legislators who already agree with the lobbyist \citep{hall2006}. On this view, organized interests shape rules mainly by shaping what allied legislators can do with limited time, not by changing their votes.
   391	
   392	\subsection{Rule making in autocracies}
   393	
   394	Theories of autocracy explain the survival of rulers by how they share rule-making power with a narrow group of insiders. In selectorate theory, leaders must retain a winning coalition drawn from a larger selectorate, and when that coalition is small they survive by supplying private goods to its members rather than public goods to all \citep{bdm2003}. Svolik locates the main threat to dictators among the elites who share power with them and shows how parties, legislatures, and rules of succession make that sharing credible \citep{svolik2012}. Gandhi and Przeworski and Magaloni reach compatible conclusions: nominally democratic institutions and ruling parties co-opt potential rivals and are associated with longer rule \citep{gandhi2007,magaloni2008}. Gerschewski adds legitimation and repression to co-optation as the supports of autocratic stability \citep{gerschewski2013}, which in the series' vocabulary brings the legitimation and enforcement pillars to the aid of rule makers. The regime classification of Geddes, Wright, and Frantz makes these claims testable across party, personalist, military, and monarchic autocracies \citep{geddes2014}.
   395	
   396	Hale describes post-Soviet politics as patronal: power runs through networks of personal reward and punishment, organized either as a single pyramid around one patron or as competing pyramids \citep{hale2014}. Levitsky and Way identify competitive authoritarian regimes in which elections are real but the field is uneven \citep{levitsky2010}. These categories matter for measurement because they describe regimes whose formal rule-making procedures are pluralistic and whose actual concentration is high.
   397	
   398	\subsection{Separation of powers and veto players}
   399	
   400	Montesquieu argued that liberty requires that the power to make law, the power to execute it, and the power to judge not be united in the same hands \citep{montesquieu1989}. Madison's defense of the proposed American constitution relied on the same idea in a different form: ``Ambition must be made to counteract ambition'' \citep{madison1788}. The constitutional design he defended gave each branch the means and the motive to resist encroachment by the others.
   401	
   402	Tsebelis generalized the idea. A veto player is an individual or collective actor whose agreement is required for a change of the status quo, and the set of policies that can replace the status quo shrinks as veto players are added or as their positions diverge \citep{tsebelis2002}. Lijphart contrasts majoritarian democracies, which concentrate rule making in the cabinet of a single-party majority, with consensus democracies that disperse it among coalition partners, two legislative chambers, federal units, and courts \citep{lijphart1999}. Linz argued that presidential systems, which give the executive and the legislature separate mandates, make conflicts between them harder to resolve \citep{linz1990}. Weingast showed that constitutional limits on rule makers are self-enforcing only when citizens can coordinate their reactions to transgressions \citep{weingast1997}.
   403	
   404	\subsection{Sources of rule-making authority}
   405	
   406	Weber classified legitimate domination as traditional, charismatic, or rational-legal according to the grounds on which subjects accept commands \citep{weber1978}. Each regime type in the comparison below claims rule-making authority on a different ground: divine right and dynastic tradition in the Catholic monarchies \citep{figgis1914,kantorowicz1957}, divine law administered by rulers and jurists in the Islamic states \citep{crone2004,lambton1981}, the historical mission of a vanguard party in the communist states \citep{kornai1992}, and popular sovereignty expressed in elections in the democracies \citep{dahl1971}. Bodin made the power to give law to all without the consent of others the first mark of sovereignty \citep{bodin1992}. Al-Mawardi set out the conditions under which an imam is validly appointed and the powers he may delegate to viziers, governors, and judges \citep{mawardi1996}. These are theories written from inside regimes, and they describe what rule makers claimed, not necessarily what they could do.
   407	
   408	\subsection{Relation to prior work}
   409	
   410	Three gaps in this literature motivate the present paper. The theories of democratic and autocratic rule making use different concepts, so comparisons across regime types tend to be either impressionistic or confined to a single dimension such as regime survival. The functional-prerequisite tradition in sociology asserted that every society must make collective decisions \citep{aberle1950,parsons1951} but did not separate the necessity of the function from the distribution of its control, and it was criticized for that reason. The source framework of the series \citep{largo2026hbs} supplies a common network vocabulary but merges rule making with adjudication and leaves the measurement of control shares open. This paper separates rule making from adjudication, gives control shares a de jure baseline in power indices, proves that necessity and concentration are logically independent for this pillar, and uses one set of questions for all six regime types.
   411	
   412	\section{Rule making across six regime types}
   413	\label{sec:regimes}
   414	
   415	\subsection{Comparative method}
   416	
   417	Each regime type is examined for the same five features: the institutions that hold the rule-making function, the concentration of control in the sense of $H^{\pP}$ and its contestability in the components of Definition~\ref{def:political-power:qp}, the strength of its coupling to the other five pillars, the arrangements that preserve accountability, and the documented capture episodes and effective checks. The answers are qualitative. Terms such as ``high'' or ``low'' concentration refer to the ordering implied by Proposition~\ref{prop:political-power:concentration} applied to the described procedure, adjusted for documented informal concentration, and they are not estimates of $H^{\pP}$ for any polity.
   418	
   419	The six types are analytical lenses, not mutually exclusive categories. A single country can be a market-capitalist society and a secular democracy at once, and the two lenses ask different questions of it. The market-capitalist lens examines how private economic resources reach rule making. The secular-democratic lens examines how rule making is distributed among elected officials, courts, independent bodies, and private institutions under a constitution. Islamic states and Catholic monarchies are treated as polities in which religious law or religious institutions supplied a source of political legitimacy, in particular historical states with large internal differences. Neither religion is treated as an essence, and no regime type is ranked above another.
   420	
   421	\subsection{Market-capitalist societies}
   422	
   423	In market-capitalist societies with electoral institutions, general rules are made by elected legislatures, by executives through decrees and regulations, and by administrative agencies under delegated authority. The United States, the most studied case, divides rule making among two legislative chambers, a president with a veto, federal agencies that issue regulations, and fifty states. The formal procedure has several veto players, so the de jure concentration of rule making is moderate, and its formal contestability is high on all five components of Definition~\ref{def:political-power:qp}.
   424	
   425	The question this lens asks is how private economic resources enter that procedure. The source framework describes a path from unequal private resources through advocacy and access to the specialized development of policy and the distribution of legal benefits \citep[Section~8]{largo2026hbs}. Several links in that path are documented. A randomized field experiment found that when a political organization revealed that attendees at requested meetings were campaign donors, congressional offices were more likely to arrange meetings with senior staff or the member \citep{kalla2016}. Lobbyists who had worked for a senator saw their lobbying revenue fall when that senator left office, which indicates that part of what they sold was access to a particular rule maker \citep{blanes2012}. Lobbyists also follow the legislators to whom they are connected when those legislators change committee assignments \citep{bertrand2014}. These findings concern access. They show privileged access, the first condition of a capture link, but they do not by themselves show that the access changed a rule.
   426	
   427	Evidence that access changes rules is weaker than the evidence of access itself, and it is contested. Gilens and Page's estimates \citep{gilens2014} are disputed by work that finds the preferences of affluent and middle-income citizens usually coincide \citep{branham2017}. A large study of lobbying on ninety-eight issues found that the status quo usually prevailed and that the resources of a side were a poor predictor of its success \citep{baumgartner2009}. Ansolabehere, de Figueiredo, and Snyder observed that campaign contributions are small relative to the value of the policies at stake, which is hard to reconcile with a market in which rules are bought \citep{ansolabehere2003}. The theory of economic regulation predicted that concentrated interests would capture the rules that govern them \citep{stigler1971}, and Peltzman generalized it to a regulator who balances the support of several groups \citep{peltzman1976}; Part I develops the capture literature \citep{long2026financial}.
   428	
   429	Rule making in this regime type is coupled most strongly to resource control. The coupling runs through the wealth-to-rules path described above and through the structural dependence of rule makers on investment that Lindblom described \citep{lindblom1977}. Hacker and Pierson argue that organized interests used this path to shift tax and regulatory rules toward the very wealthy over several decades \citep{hackerpierson2010}, and Culpepper's comparison of Europe and Japan shows that business influence is greatest when issues are technical and receive little public attention \citep{culpepper2010}. Coupling to interpretation is weaker by design: federal judges are appointed by the president with Senate confirmation, so no single coalition controls the appointment channel unless it holds both bodies.
   430	
   431	Elections, opposition rights, judicial review, disclosure rules, and competition among organized interests, which frequently lobby on opposite sides of the same question \citep{baumgartner2009}, keep this rule making contestable. The regime type thus combines moderate de jure concentration and high formal contestability with unequal practical access, and the open question is how much that access changes rules.
   432	
   433	\subsection{Communist party-states}
   434	
   435	In communist party-states, the ruling party makes the rules that matter and the state legislature ratifies them. In the Soviet Union the Politburo of the Central Committee decided major questions, the Central Committee apparatus prepared and supervised policy, party congresses ratified the line, and the Supreme Soviet enacted laws whose content had been determined elsewhere \citep{fainsod1953,hough1979}. Kornai treats the undivided power of the communist party as the defining feature of the classical socialist system, from which its economic institutions follow \citep{kornai1992}. The de jure concentration of rule making is high, and every component of contestability except transparency of some rule texts is low for actors outside the party.
   436	
   437	The appointment channel is the defining instrument. Party committees at each level held lists of posts, the nomenklatura, whose holders they appointed or approved, covering the leadership of ministries, enterprises, courts, newspapers, universities, and the armed forces \citep{hough1979}. In the notation of Definition~\ref{def:political-power:appointment-channel}, the party's appointment share $\alpha_{S,\ell}$ approached one in every pillar. Voslensky, a former Soviet official writing in emigration, described the nomenklatura as a ruling class \citep{voslensky1984}, and Djilas, a Yugoslav dissident, called the party bureaucracy a new class that held collective ownership through political control \citep{djilas1957}. Both accounts come from authors with strong political commitments and should be read alongside the institutional scholarship. Hough and Fainsod described a system of bureaucratic bargaining among ministries and regions, and Lane and Ross found significant divisions within the Soviet ruling elite of 1981 to 1991 \citep{lane1995}. These findings bear on the loyalty of appointees, a parameter formalized in Section~\ref{sec:mechanisms} (Proposition~\ref{prop:political-power:appointment-bound}): appointment by a single party does not guarantee that appointees act as one coalition.
   438	
   439	The People's Republic of China retains the Leninist structure with important changes. Shirk described the relation between the party's top leaders and the Central Committee as reciprocal accountability: leaders appoint the members of the committee that formally selects them \citep{shirk1993}. Landry showed how the party's control of the appointment and evaluation of local cadres allowed it to decentralize economic decisions without losing political control \citep{landry2008}. Minzner documented a turn after the early 2000s away from legal professionalization and toward mediation and political direction of the courts \citep{minzner2011}, which raises the coupling $C_{\pP\pJ}$.
   440	
   441	Coupling to the other pillars is high by design in all four pairs treated here: party direction of courts, of propaganda and education, of the security services, and of official trade unions organized under party leadership \citep{kornai1992}. Accountability operates mainly within the party, through collective leadership, factional bargaining, and rules of succession, which Svolik identifies as the institutions that make power sharing among elites credible \citep{svolik2012}. The documented checks are intra-elite. In 1964 the Soviet party leadership removed Khrushchev as first secretary through the Presidium and the Central Committee, a replacement of the top rule maker carried out entirely inside the party \citep{hough1979}. Svolik's cross-national evidence points the same way: most authoritarian leaders who lose office by nonconstitutional means are removed by regime insiders rather than by popular uprisings \citep{svolik2012}. The Soviet case also shows the limits of high integration: the party's control of every pillar did not prevent the divisions that Lane and Ross document or the collapse of the system at the end of the period they study.
   442	
   443	\subsection{Social democracy and democratic socialism}
   444	
   445	In social democracies, rules are made by parliaments in which strong programmatic parties compete, and many economic and social rules are negotiated with organized labor and employers before they reach parliament. Sweden is the standard case. The Social Democratic Workers' Party governed for most of the twentieth century, and its close tie to the national trade union confederation gave organized labor direct access to rule making \citep{esping1985}. Korpi's power-resources theory treats the strength of labor's organization as the main determinant of the redistributive content of rules in capitalist democracies \citep{korpi1983}. De jure concentration of rule making is moderate, because rule making requires parliamentary majorities and coalition partners, and contestability is high on every component.
   446	
   447	Corporatist bargaining is the first feature that distinguishes this regime type in the rule-making layer. Peak organizations of labor and capital take part in drafting rules about wages, working conditions, and social insurance, which raises the coupling $C_{\pP\pW}$ by design. Within the domains it covers, a tripartite bargain among the government, the labor confederation, and the employers' confederation is a unanimity procedure among three organs, so by Proposition~\ref{prop:political-power:concentration}(d) the organ-level concentration of rule making in those domains is $1/3$. The same arrangement creates a risk of closure: interests that are not organized into the peak associations, such as the unemployed or new categories of workers, may be excluded from rule making that formally includes all producers.
   448	
   449	The long tenure of a single party is the second feature. Prolonged dominance of rule making by one party in a competitive system is concentration over time, which the static index $H^{\pP}$ does not capture.
   450	
   451	Przeworski described the strategic dilemma of electoral socialism: to win majorities, workers' parties must appeal beyond the working class, and to govern a market economy they depend on the investment decisions of private owners \citep{przeworski1985}. Pontusson's study of investment politics in Sweden showed that proposals to extend collective control over investment met strong resistance from business and were scaled back \citep{pontusson1992}. In the series' vocabulary, the structural dependence of rule makers on capital constrained the rules that social-democratic majorities could make. Kitschelt traced how European social-democratic parties changed their programs as their electorates changed \citep{kitschelt1994}, and Berman argued that the social-democratic movement was defined by a belief in the primacy of political choice over market outcomes \citep{berman2006}.
   452	
   453	Accountability rests on competitive elections, which did remove social-democratic governments, on an independent civil service, and on the formal openness of the corporatist channels. Rothstein's study of Swedish labor-market and school policy argues that the bureaucratic design of implementation, not only legislative majorities, determined whether social-democratic reforms achieved their goals \citep{rothstein1996}. Huber and Stephens show that long periods of social-democratic government were associated with the expansion of welfare states and that the effects persisted after the parties lost office \citep{huber2001}. The documented check on concentration in this regime type is alternation in government combined with corporatist channels that remain open to opposing organized interests, and the documented risk is closure of rule making to the unorganized.
   454	
   455	\subsection{Islamic states}
   456	
   457	In polities that derived political legitimacy from Islamic law, the question of who makes the rules has had an answer that differs from the European cases in one structural respect. Much of the general law, the fiqh developed from the Quran and the Sunna, was elaborated by jurists who were not officials of the ruler. Crone and Hinds argue that the early caliphs claimed religious authority in their own right and that this authority passed over the first centuries of Islam to the scholars, the ulama \citep{crone1986}. Rulers continued to make rules in the domains of administration, taxation, and public order, but they did not control the content of the law in the way that Bodin attributed to the sovereign. Hallaq argues that the modern state, with its claim to a monopoly of legislation, cannot reproduce this moral and legal order \citep{hallaq2013}. The argument is contested; the difference in the distribution of rule-making shares that it identifies is not.
   458	
   459	Classical theory placed the imam, or caliph, at the head of the community. Al-Mawardi's treatise sets out the qualifications of the imam, the ways in which he is validly appointed, including selection by qualified electors, and the powers he may delegate \citep{mawardi1996}. Lambton and Crone describe a long gap between this theory and practice, in which military rulers held effective power while caliphs conferred legitimacy and jurists accommodated the arrangement \citep{lambton1981,crone2004}. The Ottoman Empire added a body of sultanic regulation, the qanun, alongside sharia. Imber's study of the sixteenth-century chief mufti Ebussuud shows a senior jurist harmonizing sultanic law with Hanafi jurisprudence, which places a religious official inside the rule-making process of the empire \citep{imber1997}. Barkey describes Ottoman rule as the brokered management of diverse intermediaries rather than direct command \citep{barkey2008}.
   460	
   461	Two modern states show how differently the legitimating source can be institutionalized. The constitution of the Islamic Republic of Iran, adopted in 1979 and revised in 1989, vests leadership of the community in a just and pious jurist in the absence of the Twelfth Imam, following Khomeini's doctrine of the guardianship of the jurist \citep{iranconst,khomeini1981}. The Leader is selected by an elected Assembly of Experts and sets the general policies of the state. Legislation passed by the elected Majles must be sent to the Guardian Council, whose jurists judge its compatibility with Islam, and disputes between the two bodies go to the Expediency Council \citep{iranconst,schirazi1997}. Rule making in Iran therefore combines electoral and appointed components, and its de jure concentration is moderate to high depending on how the Leader's appointment power is weighted. Factions and parallel institutions compete within this structure \citep{brumberg2001,buchta2000}.
   462	
   463	Saudi rule making is concentrated in form and fragmented in practice. The Basic Law of Governance of 1992 declares the system of government monarchical, states that the regime derives its power from the Quran and the Sunna, provides that laws are issued and amended by royal decree, and gives the King the power to dissolve and re-form the consultative council \citep{saudibasic}. The state rests on the alliance between the Al Saud and the religious establishment descended from the eighteenth-century Wahhabi movement \citep{commins2006,alrasheed2002}. Yet Hertog shows that rule making in the oil era was divided among princes, brokers, and bureaucratic fiefdoms rather than centralized \citep{hertog2010}.
   464	
   465	In both modern cases rule making is closely coupled to legitimation and interpretation, and each case has one further strong coupling. In Iran the coupling to enforcement runs through the Revolutionary Guards, whose economic and political role is debated \citep{alfoneh2013}. In Saudi Arabia the coupling to resource control runs through the allocation of oil rents \citep{gause1994}; whether oil revenue itself weakens accountability is disputed \citep{ross2001}.
   466	
   467	Whether religious jurists raised or lowered the contestability of rule making is the question on which the scholarship divides. Jurists with authority independent of rulers raised the oversight component, while jurists co-opted by rulers could lower the entry component by excluding rival law makers. Kuran attributes the economic divergence of the Middle East to particular institutions of Islamic law, and Kuru attributes authoritarianism and underdevelopment in Muslim-majority states to an alliance between the ulama and the state \citep{kuran2011,kuru2019}; Rubin explains the divergence instead by the terms on which rulers bargained with religious authorities for legitimacy \citep{rubin2017}. Doctrine permits both arrangements. Shia jurists have held positions ranging from political quietism to the activism of Khomeini's doctrine \citep{arjomand1988}, and Sunni theory accommodated military rulers alongside autonomous jurists \citep{lambton1981}.
   468	
   469	Checks on rule makers are documented throughout the type. In the classical period the jurists' authority over much of the law limited what rulers could legislate, Ottoman and Saudi rule rested on negotiation with intermediaries, and Iranian elections remain contested within the limits set by candidate screening. Religious legitimation also constrains the rulers who depend on it: militant challenges to the Saudi state show that religious actors can turn the ruler's own ground of legitimacy against the ruler \citep{hegghammer2010}.
   470	
   471	\subsection{Catholic monarchies}
   472	
   473	In the Catholic monarchies of early modern Europe, the king was in theory the source of law. Bodin made the power to legislate without the consent of others the mark of sovereignty \citep{bodin1992}, and Bossuet grounded royal authority in Scripture \citep{bossuet1990}. Kantorowicz traced the medieval idea that the king had a mortal natural body and an undying political body \citep{kantorowicz1957}, and Figgis described the theory of divine right as it developed in early modern Europe \citep{figgis1914}. In formal terms, rule making was concentrated in one person, close to the dictatorship case of Proposition~\ref{prop:political-power:concentration}(d).
   474	
   475	In practice, Catholic monarchs shared rule making with councils, estates, and courts that could delay or block royal decrees. Habsburg Spain was a composite monarchy whose kingdoms kept their own laws and representative assemblies, and royal government worked through separate councils for kingdoms and functions \citep{elliott1963}. When Olivares tried in the 1620s and 1630s to make the kingdoms share the costs of the monarchy's wars, the resistance contributed to the revolts of Catalonia and Portugal in 1640 \citep{elliott1963,elliott1984}, a documented check on what the crown could impose. In Bourbon France the Estates-General did not meet between 1614 and 1789, yet royal ordinances still had to be registered by the Parlements, which could remonstrate and delay unless the king overrode them in a formal session in person. Beik's study of Languedoc shows absolutism working through collaboration with provincial elites who shared in its revenues \citep{beik1985}, and Collins presents the French state as a negotiated structure with real limits \citep{collins1995}. The crown's reach was nonetheless real: Root shows royal rules on village finances reshaping relations between peasants and lords in Burgundy \citep{root1987}.
   476	
   477	The Papal States combined spiritual and temporal rule making in one office. The pope was elected by the cardinals, so the Papal States were an elective monarchy, and Prodi describes the early modern papacy as a single body with two souls, the head of the universal Church and the prince of a territorial state \citep{prodi1987}. Rule making in the Papal States was concentrated in the pope and the curial congregations, and the coupling between rule making and legitimation was complete by construction.
   478	
   479	Rule making in these monarchies was coupled to the other pillars through the Church and through office. Crowns controlled appointments to high Church office in their territories, which raised $C_{\pP\pI}$; the Gallican tradition in France asserted royal and episcopal liberties against Rome, and Van Kley traces how disputes over Jansenism drew the Parlements into conflict with both crown and papacy \citep{vankley1996}. Venality of judicial and financial offices coupled rule making to resource control and to interpretation, because offices were property that the crown sold and whose holders could resist the crown. Ertman classifies France and Spain as patrimonial absolutist states, in which office holding and fiscal administration were tied to private interests \citep{ertman1997}.
   480	
   481	Accountability did not take the form of replacement of rule makers, which the dynastic principle excluded, but of the corporate privileges of estates, towns, Parlements, and the Church, of the Church's autonomous canon law, and, in extreme cases, of revolt. The de jure concentration was high, and practical concentration was lower because of brokerage; contestability was low in replacement and entry and intermittently significant in oversight through the Parlements and estates.
   482	
   483	\subsection{Secular democracies}
   484	
   485	In secular democracies, the authority to make rules is derived from popular sovereignty and distributed by a constitution among elected legislatures, executives, courts with powers of review, independent agencies, subnational governments, and in some cases the voters directly. The distribution varies widely. Lijphart's comparison of thirty-six democracies distinguishes majoritarian systems, in which a single-party cabinet controls rule making between elections, from consensus systems that disperse it \citep{lijphart1999}. Federal systems add a territorial division, giving subnational governments rule-making authority that the national legislature cannot revoke by ordinary statute. Presidential systems add a division between an executive and a legislature with separate electoral mandates and fixed terms, which Linz argued makes conflicts between them harder to resolve \citep{linz1990}. Where constitutions provide for referendums and popular initiatives, the electorate itself becomes a veto player or an agenda setter in the rule-making procedure \citep{lijphart1999}. In the vocabulary of this paper, majoritarian systems have higher de jure concentration and fewer veto players; consensus systems have lower concentration and more veto players, and the trade-off between them is the subject of Proposition~\ref{prop:political-power:veto} in Section~\ref{sec:mechanisms}.
   486	
   487	Contestability is the defining property of this regime type. Dahl's polyarchy requires both inclusive participation and public contestation \citep{dahl1971}. Przeworski characterized democracy as a system in which parties can lose elections and accept the loss, so that outcomes are uncertain in advance \citep{przeworski1991}. The replacement component $q^{\mathrm{rep}}$ is therefore the component that distinguishes democracies from the other regime types most sharply. Data projects such as V-Dem measure it alongside legislative and judicial constraints on the executive and the freedom to form parties \citep{coppedge2011}, and the Regimes of the World classification uses these measures to separate liberal and electoral democracies from electoral and closed autocracies \citep{luhrmann2018}.
   488	
   489	Secular democracies have relocated part of rule making away from elected bodies. Constitutional courts in Europe shape legislation by reviewing it, and Stone Sweet shows that legislators anticipate review and draft accordingly \citep{stonesweet2000}. Hirschl argues that the transfer of power to courts in several democracies served elites who expected to lose control of legislatures \citep{hirschl2004}. Independent agencies and central banks make rules under delegated authority. Each of these relocations lowers the concentration of rule making in elected bodies and raises its concentration in bodies that are not removable by voters, and whether the result is more or less accountable depends on the oversight component, not on the relocation itself.
   490	
   491	The documented capture risk in this regime type is the erosion of contestability by elected rule makers. Levitsky and Way describe regimes that hold real elections while incumbents abuse state resources, media access, and legal harassment to tilt the field \citep{levitsky2010}. In such regimes the formal rule-making procedure is unchanged while the replacement and entry components of contestability fall. The documented checks are the ones Madison anticipated, rival institutions with the means and motive to resist \citep{madison1788}, together with the coordination of citizens against transgressions that Weingast identifies as the condition for constitutional limits to hold \citep{weingast1997}. Pettit's republican account treats the contestability of rule making by those subject to it as the core of freedom from domination \citep{pettit1997}, which supplies a normative ground for the measurement emphasis of Definition~\ref{def:political-power:qp}.
   492	
   493	\subsection{Comparative summary}
   494	
   495	Tables~\ref{tab:regimes-holders} and~\ref{tab:regimes-coupling} summarize the configuration of the rule-making pillar under each regime type and the coupling that the cited literature documents. Every regime type performs the function, which is what Theorem~\ref{thm:political-power:necessity} requires. Concentration and contestability vary independently of the source of legitimacy: rule making in Habsburg Spain was less concentrated in practice than its theory claimed, and rule making in some electoral regimes is more concentrated than their procedures suggest. The main channel of coupling differs by regime type, from wealth to rules in market economies to appointment in party-states and religious legitimation in the Islamic states and Catholic monarchies, which is the rule-making form of the source's proposition that control paths differ by regime \citep[Proposition~3]{largo2026hbs}.
   496	
   497	\begin{table}[tbp]
   498	\centering
   499	\small
   500	\caption{Holders, concentration, and contestability of rule making by regime type. Concentration and contestability are qualitative descriptions based on the cited literature, not coded values.}
   501	\label{tab:regimes-holders}
   502	\begin{tabularx}{\textwidth}{@{}L{2.5cm}YYY@{}}
   503	\toprule
   504	Regime type & Principal rule makers & Concentration of rule making & Contestability of rule making \\
   505	\midrule
   506	Market-capitalist & Elected legislatures, executives, and regulatory agencies, with organized interests shaping drafts & Moderate, with several veto players in the formal procedure & High in form, with unequal practical access by economic resources \\
   507	Communist party-state & Party leadership and apparatus, with the legislature ratifying & High, through the party's control of appointments in every pillar & Low outside the party and partial within it \\
   508	Social democracy & Parliamentary majorities negotiating with peak organizations of labor and capital & Moderate, with long tenure of a dominant party in some cases & High, with a risk of closure to unorganized interests \\
   509	Islamic states & Rulers and councils, with jurists holding authority over much of the law & Varies from dispersed classical arrangements to concentrated modern ones & Varies from contested elections in Iran to none in Saudi Arabia \\
   510	Catholic monarchies & Crown in council, with Parlements, Cortes, and estates able to delay or refuse & High in theory and lower in practice because of brokerage & Low for replacement and intermittent for oversight \\
   511	Secular democracies & Legislatures and executives under a constitution, with courts and agencies holding delegated parts & Low to moderate, depending on majoritarian or consensus design & High, and falling where incumbents tilt the electoral field \\
   512	\bottomrule
   513	\end{tabularx}
   514	\end{table}
   515	
   516	\begin{table}[tbp]
   517	\centering
   518	\small
   519	\caption{Coupling of rule making to other pillars, documented capture risks, and documented checks by regime type.}
   520	\label{tab:regimes-coupling}
   521	\begin{tabularx}{\textwidth}{@{}L{2.5cm}YYY@{}}
   522	\toprule
   523	Regime type & Strongest documented coupling & Documented capture risk & Documented check \\
   524	\midrule
   525	Market-capitalist & Resource control to rule making through donations, lobbying, and investment dependence & Privileged access of donors and connected lobbyists & Competing interest groups, elections, and the advantage of the status quo \\
   526	Communist party-state & Rule making to every other pillar through appointment lists & Integration of all pillars under one coalition & Factional bargaining and divisions within the elite \\
   527	Social democracy & Rule making to production through corporatist bargaining & Exclusion of unorganized groups from negotiated rules & Electoral alternation and open corporatist channels \\
   528	Islamic states & Rule making to legitimation and interpretation through religious-legal authority & Clerical vetting of legislation and candidates, and rent allocation & Independent juristic authority, elections in Iran, and brokered rule \\
   529	Catholic monarchies & Rule making to legitimation through royal control of Church appointments & Venality of office and dynastic exclusion of replacement & Corporate privileges, registration by Parlements, and revolt \\
   530	Secular democracies & Rule making to interpretation through appointments and constitutional review & Erosion of contestability by elected incumbents & Rival institutions and citizen coordination against transgression \\
   531	\bottomrule
   532	\end{tabularx}
   533	\end{table}
   534	
   535	\section{Mechanisms, failure modes and checks}
   536	\label{sec:mechanisms}
   537	
   538	The necessity theorem says that rule making occurs; Proposition B concerns the conditions under which it becomes concentrated, coupled to other pillars, and unaccountable. Each mechanism below is a comparative static under explicit assumptions, not a law of history, and each identifies the check that interrupts it, in line with the source's proposition that checks can interrupt the transmission of concentrated power \citep[Proposition~2]{largo2026hbs}.
   539	
   540	\subsection{Delegation and oligarchy}
   541	
   542	Michels argued that the leaders of large organizations escape the control of members because members lack the time, expertise, and information to monitor them \citep{michels1915}. Olson's analysis of collective action explains why: the benefit of monitoring is shared by all members, while its cost falls on the one who monitors \citep{olson1965}. A simple model makes the conditional character of the argument precise.
   543	
   544	\begin{assumption}[Monitoring game]
   545	\label{ass:political-power:monitoring}
   546	An organization has $n\ge2$ members and a leadership that extracts a rent $\rho>0$ from the organization in each period, at a cost of $\rho/n$ to each member. Each member chooses simultaneously whether to monitor the leadership at private cost $c>0$. Each monitor independently detects the extraction with probability $\delta\in(0,1]$, and detection leads to the replacement of the leadership. After replacement the rent is returned to the members, so each member recovers $\rho/n$. A member's payoff is the expected rent recovered by that member minus the member's own monitoring cost.
   547	\end{assumption}
   548	
   549	\begin{proposition}[Monitoring vanishes in large organizations]
   550	\label{prop:political-power:michels}
   551	Under Assumption~\ref{ass:political-power:monitoring}:
   552	\begin{enumerate}[label=(\alph*)]
   553	\item if $n>\rho\delta/c$, the unique Nash equilibrium is that no member monitors, and the leadership retains the rent with probability one;
   554	\item suppose instead that an organized opposition faction, distinct from the members, chooses simultaneously with them whether to monitor at cost $c$, detects the extraction independently with probability $\delta$ if it monitors, and takes office whenever the leadership is replaced, whoever detected the extraction. In office the faction keeps a share $\beta\in(0,1]$ of the rent, so each member recovers only $(1-\beta)\rho/n$, and the faction's payoff is $\beta\rho$ times the probability of replacement minus $c$ if it monitors. If $n>(1-\beta)\rho\delta/c$ and $\beta\rho\delta>c$, the unique Nash equilibrium is that no member monitors and the faction monitors, so the leadership is detected and replaced with probability $\delta$ whatever the value of $n$.
   555	\end{enumerate}
   556	\end{proposition}
   557	
   558	\begin{proof}
   559	(a) If $k$ other members monitor, the probability that none of them detects the extraction is $(1-\delta)^k$. A member who adds monitoring raises the detection probability by $\delta(1-\delta)^k$ and so gains $(\rho/n)\delta(1-\delta)^k$ in expected recovered rent. This gain is at most $(\rho/n)\delta$, which is less than $c$ when $n>\rho\delta/c$. Monitoring is therefore strictly dominated for every member, whatever the others do, and the unique equilibrium has no monitoring.
   560	
   561	(b) A member's gain from monitoring is now at most $(1-\beta)(\rho/n)\delta$, which is less than $c$ when $n>(1-\beta)\rho\delta/c$, so monitoring is strictly dominated for every member as in (a). In any equilibrium no member monitors, and the faction's gain from monitoring is then $\beta\rho\delta$, which exceeds $c$ and does not depend on $n$. The faction therefore monitors, and the equilibrium is unique because the members' choice is dominant.
   562	\end{proof}
   563	
   564	The threshold $n^\ast=\rho\delta/c$ rises with the size of the rent and the effectiveness of monitoring and falls with its cost. Part (a) is Michels's tendency stated as a conditional result. Part (b) identifies the check. An organized opposition with a private stake in winning office converts the public good of oversight into a private incentive, and it does so even though it lowers the members' own incentive to monitor. Lipset, Trow, and Coleman's study of the International Typographical Union found exactly such an arrangement, a durable two-party system inside a union, and it is the classic exception to Michels's law \citep{lipset1956}. Voss and Sherman documented later cases in which American union locals reversed oligarchic tendencies \citep{voss2000}, and Cassinelli offered an early analytic critique of the law \citep{cassinelli1953}. Schumpeter's competitive theory of democracy rests on the same mechanism at the scale of a polity: rival teams of leaders compete for the vote and monitor one another \citep{schumpeter1942}.
   565	
   566	The model omits much. Leaders can raise the cost of monitoring by controlling information, which is Michels's own emphasis, and members may value leaders for reasons other than rent. The proposition shows only that oligarchy follows from size under one set of conditions and that a specific institutional change reverses it. That is enough to treat oligarchization as a conditional tendency, which is the role the series assigns it in the argument for Proposition B (Part VII), rather than as a necessity.
   567	
   568	\subsection{Veto players and the status quo}
   569	
   570	Adding veto players is the standard constitutional remedy for concentrated rule making. It has a cost that the comparison of majoritarian and consensus democracies brings out, and a simple result shows why the cost is unavoidable.
   571	
   572	\begin{definition}[Winset]
   573	\label{def:political-power:veto-players}
   574	Let $X$ be a set of alternatives, $q\in X$ the status quo, and $K$ a nonempty set of veto players, each with strict preferences $\succ_i$ on $X$. The \emph{winset} of $q$ is $W_K(q)=\{x\in X: x\succ_i q\text{ for all }i\in K\}$, the set of alternatives that every veto player prefers to the status quo \citep{tsebelis2002}. A \emph{pure veto-player procedure} enacts $x$ against $q$ exactly when $x\in W_K(q)$; it is the unanimity game on $K$ of Proposition~\ref{prop:political-power:concentration}(d). In a general simple game membership in $W_K(q)$ is necessary for replacing $q$ but not sufficient.
   575	\end{definition}
   576	
   577	\begin{proposition}[Veto players protect the status quo]
   578	\label{prop:political-power:veto}
   579	\leavevmode
   580	\begin{enumerate}[label=(\alph*)]
   581	\item If $K\subseteq K'$, then $W_{K'}(q)\subseteq W_K(q)$.
   582	\item If some $i\in K$ prefers $q$ to every other alternative, then $W_K(q)=\emptyset$.
   583	\item Let $q$ be a preferential rule, one that every member of a group $B$ prefers to every other alternative, and let $x\neq q$ be a reform that every member of $K\setminus B$ prefers to $q$. Under a pure veto-player procedure, $x$ can replace $q$ if and only if $K\cap B=\emptyset$.
   584	\end{enumerate}
   585	\end{proposition}
   586	
   587	\begin{proof}
   588	(a) An alternative in $W_{K'}(q)$ is preferred to $q$ by every member of $K'$, and so by every member of $K$. (b) If $i\in K$ prefers $q$ to every $x\neq q$, no $x$ is preferred to $q$ by $i$, so no $x$ lies in $W_K(q)$. (c) If $K\cap B=\emptyset$, every member of $K$ prefers $x$ to $q$, so $x\in W_K(q)$. If some $i\in K\cap B$, then $i$ prefers $q$ to $x$, so $x\notin W_K(q)$.
   589	\end{proof}
   590	
   591	Part (c) contains the trade-off. A preferential rule survives any reform whenever one of its beneficiaries holds a veto. Adding veto players protects the polity against new preferential rules, because a new rule must pass every veto player, and it protects existing preferential rules, because their repeal must also pass every veto player. Part (a) states the general form: the set of possible changes can only shrink as veto players are added. This is why the hypothesis HP7 in Section~\ref{sec:measurement} predicts that the number of effective veto players is associated both with the persistence of preferential rules and with low responsiveness. The same logic explains the status-quo bias of consensus societies in Proposition~\ref{prop:political-power:minimal-form}, where every adult holds a veto.
   592	
   593	The check implied by the proposition is not more veto players but the control of who holds them. A veto held by an independent body with no stake in a preferential rule, such as a court reviewing a statute against a general constitutional standard, constrains new preferential rules without protecting old ones, provided the body cannot itself be captured. That condition is the subject of Part III.
   594	
   595	\subsection{The appointment channel}
   596	
   597	The source framework defines cross-pillar integration $C_{mn}$ only descriptively, as the extent to which one coalition commands appointments, budgets, sanctions, or agenda in two pillars \citep{largo2026hbs}, and Part VII fixes a formal definition for the series. The appointment channel acquires testable content under one explicit candidate, the coalition-overlap measure. Let $\mathcal{S}$ be a preregistered list of coherent coalitions, groups such as parties, factions, or dynasties that can issue joint directives. For $S\in\mathcal{S}$ let $s^{\pP}(S)$ be the Shapley-Shubik share of the bloc player $p_S$ in the quotient game on $N_S=(N\setminus S)\cup\{p_S\}$, whose winning coalitions are defined for $T\subseteq N\setminus S$ by $T\in\Win_S$ if and only if $T\in\Win$, and $T\cup\{p_S\}\in\Win_S$ if and only if $T\cup S\in\Win$. This bloc share is not in general the sum of the members' separate shares; in the Iranian example of Table~\ref{tab:examples} the two councils hold $1/6+1/6$ separately and $1/2$ as a bloc. Let $\kappa_\ell(S)\in[0,1]$ be the share of decision-relevant control in pillar $\ell$ that is exercised in accordance with the directives of $S$, and set
   598	\begin{equation}
   599	C^{\mathrm{ov}}_{\pP\ell}=\max_{S\in\mathcal{S}}\min\{s^{\pP}(S),\kappa_\ell(S)\}.
   600	\label{eq:overlap}
   601	\end{equation}
   602	The candidate lies in $[0,1]$, equals one when a single coalition holds all rule-making control and commands all of pillar $\ell$, and equals zero when no listed coalition has a positive share in both.
   603	
   604	\begin{proposition}[Appointment bounds on integration]
   605	\label{prop:political-power:appointment-bound}
   606	For a coalition $S$ and an office $o$ let $f_{S,o}\in[0,1]$ be the share of the holder's decisions that follow the directives of $S$. For $S\in\mathcal{S}$ with $\alpha_{S,\ell}>0$ define the loyalty of its appointees as the conditional average
   607	\[
   608	\lambda_S=\frac{1}{\alpha_{S,\ell}}\sum_{o\in O_\ell}w_o f_{S,o}\,\mathbf{1}[S\text{ can unilaterally appoint or remove the holder of }o],
   609	\]
   610	and set $\lambda_S=0$ when $\alpha_{S,\ell}=0$. Suppose that command in pillar $\ell$ decomposes as $\kappa_\ell(S)=\lambda_S\alpha_{S,\ell}+\gamma_S$, where $\gamma_S\in[0,1-\lambda_S\alpha_{S,\ell}]$ is command exercised through channels other than appointment, such as budgets, sanctions, and informal patronage. Then:
   611	\begin{enumerate}[label=(\alph*)]
   612	\item for every $S\in\mathcal{S}$, $C^{\mathrm{ov}}_{\pP\ell}\ge\min\{s^{\pP}(S),\lambda_S\alpha_{S,\ell}\}$;
   613	\item if command runs only through appointment ($\gamma_S=0$ for all $S$) and loyalty is at most $\bar\lambda$ ($\lambda_S\le\bar\lambda$ for all $S$), then $C^{\mathrm{ov}}_{\pP\ell}\le\bar\lambda\max_{S\in\mathcal{S}}\alpha_{S,\ell}$;
   614	\item if command runs only through appointment and no listed coalition can unilaterally appoint or remove the holder of any office in $O_\ell$, for example because both appointment and removal require the consent of two bodies controlled by different coalitions, then $C^{\mathrm{ov}}_{\pP\ell}=0$.
   615	\end{enumerate}
   616	\end{proposition}
   617	
   618	\begin{proof}
   619	(a) By Equation~\eqref{eq:overlap}, $C^{\mathrm{ov}}_{\pP\ell}\ge\min\{s^{\pP}(S),\kappa_\ell(S)\}$. Since $\gamma_S\ge0$, $\kappa_\ell(S)\ge\lambda_S\alpha_{S,\ell}$, and the minimum is nondecreasing in each argument. (b) For every $S$, $\min\{s^{\pP}(S),\kappa_\ell(S)\}\le\kappa_\ell(S)=\lambda_S\alpha_{S,\ell}\le\bar\lambda\max_{S'}\alpha_{S',\ell}$; take the maximum over $S$. (c) The hypothesis gives $\alpha_{S,\ell}=0$ for every $S\in\mathcal{S}$ by Definition~\ref{def:political-power:appointment-channel}, and (b) gives $C^{\mathrm{ov}}_{\pP\ell}\le0$.
   620	\end{proof}
   621	
   622	The proposition separates three quantities that comparative accounts often run together. The rule-making share $s^{\pP}(S)$ says how much of rule making the coalition controls. The appointment share $\alpha_{S,\ell}$ says how many posts in another pillar it fills. The loyalty parameter $\lambda_S$ says how far the people it appoints do what it wants. Nomenklatura systems maximize the first two, and part (a) then makes integration high unless loyalty is low. The Soviet evidence of elite divisions \citep{lane1995} and of bureaucratic bargaining \citep{hough1979} concerns loyalty, and so it limits the integration that appointment alone can produce. Parts (b) and (c) identify the check. Requiring the consent of a second body for both appointment and removal closes the appointment channel to any single coalition, and security of tenure lowers loyalty after appointment by removing the threat of dismissal. Under plural appointment any remaining integration must run through budgets, sanctions, or patronage ($\gamma_S$), which tells an investigator where to look.
   623	
   624	\subsection{Agenda control and quiet politics}
   625	
   626	The three propositions concern visible procedures. A fourth mechanism operates through what never reaches a procedure. An actor with agenda control can keep a reform off the agenda without casting a vote, and no power index computed from the formal procedure will register the effect (Definition~\ref{def:political-power:agenda-control}). The evidence for this mechanism comes from studies of low-salience rule making, where business influence over the rules of corporate governance was greatest when issues were technical and public attention was low \citep{culpepper2010}, and from accounts of lobbying as a subsidy that extends the capacity of allied legislators \citep{hall2006}.
   627	
   628	Agenda control fails as a mechanism of capture when the transparency and entry components of contestability are high. Publication of drafts and of the record of who proposed what makes non-decisions visible, and free entry into rule-making competition allows excluded interests to place their proposals on the agenda through other actors. The source framework's redesign proposals include lobbying registers and the disclosure of contacts between rule makers and interested parties for this reason \citep[Section~11]{largo2026hbs}.
   629	
   630	\subsection{Checks}
   631	
   632	The four mechanisms share a structure. In each, rule making drifts toward capture when one component of contestability is weak: oversight in the monitoring game, the identity of veto holders in the veto game, independence of appointees in the appointment channel, and transparency in agenda control. The corresponding checks are organized opposition, vetoes held by actors without a stake in the rule, plural appointment and security of tenure, and publicity. None of these checks removes the rule-making function, and none requires that it be dispersed to the point of the consensus society, whose own status-quo bias Proposition~\ref{prop:political-power:minimal-form} describes. The checks act on contestability, not on the existence of rule makers, which is the rule-making form of the series' central distinction between Proposition A and Proposition B.
   633	
   634	\section{Measurement and hypotheses}
   635	\label{sec:measurement}
   636	
   637	\subsection{Indicators}
   638	
   639	Table~\ref{tab:indicators} lists indicators for the constructs of this paper. Each indicator can be coded from documentary sources, and each has a known weakness. The table follows the source framework's requirement that measurement precede accusation and that the population of coded events include ordinary rule making, not only scandals \citep[Appendix~B]{largo2026hbs}.
   640	
   641	\begin{table}[tbp]
   642	\centering
   643	\small
   644	\caption{Indicators for the constructs of the rule-making layer, with the main weakness of each.}
   645	\label{tab:indicators}
   646	\begin{tabularx}{\textwidth}{@{}L{2.6cm}YY@{}}
   647	\toprule
   648	Construct & Indicator & Main weakness \\
   649	\midrule
   650	De jure control shares & Shapley-Shubik shares computed from the written or customary decision procedure & Ignores agenda setting and informal influence \\
   651	De facto control shares & Shares of contested decisions in which each actor's position prevails, and survival of each actor's provisions through amendment and veto bargaining & Success can reflect anticipation of others' positions rather than control \\
   652	Agenda origin & Shares of enacted rules by originating actor, from legislative records and decree registers & Initiation is a different power from enactment \\
   653	Concentration $H^{\pP}$ & Sum of squared shares from either of the two indicators above & Sensitive to the definition of actors as individuals or groups \\
   654	Replacement $q^{\mathrm{rep}}$ & Frequency of peaceful turnover of rule makers through elections or regular succession & Turnover can occur within a closed coalition \\
   655	Oversight $q^{\mathrm{ovs}}$ & Indices of legislative and judicial constraints on the executive & Formal powers may not be used \\
   656	Entry $q^{\mathrm{ent}}$ & Legal and practical freedom to form parties, stand for office, and petition & Practical barriers are hard to code \\
   657	Transparency $q^{\mathrm{trn}}$ & Publication of drafts, consultation records, and lobbying registers & Disclosure can be formal and incomplete \\
   658	Exit $q^{\mathrm{ext}}$ & Legal and economic cost of leaving the jurisdiction or the group & Exit can substitute for voice and weaken reform \\
   659	Appointment share $\alpha_{S,\ell}$ & Share of weighted posts in pillar $\ell$ that a coalition fills without the consent of another body & Requires a list of posts and weights fixed in advance \\
   660	Veto players & Number of actors whose consent is required to change a statute & Partisan alignment can merge formally separate veto players \\
   661	\bottomrule
   662	\end{tabularx}
   663	\end{table}
   664	
   665	\subsection{Hypotheses with falsifiers}
   666	
   667	Each hypothesis below refines one of three general hypotheses in the source framework \citep[Section~9]{largo2026hbs}: that benefits concentrated among connected actors go with weaker chances of challenge (H1), that groups controlling appointments, funds, and sanctions across several domains keep preferential rules after exposure (H2), and that appointment chains explain allocation in one-party sectors better than private capital does (H3). Each names its parent and the observation that would count against it.
   668	
   669	\begin{description}[font=\normalfont\itshape, leftmargin=1.5em, style=nextline]
   670	\item[HP1, appointment channel.] In party-state regimes, the share of key economic, judicial, media, and security posts filled from party appointment lists predicts the integration of rule making with those pillars. In secular democracies, where appointment to such posts requires confirmation by a second body or is governed by civil-service rules, the same pairwise integrations are lower. Parent: H3. Falsifier: equal integration across regimes with different appointment rules, after controlling for the loyalty of appointees.
   671	\item[HP2, institutionalized power sharing.] Autocracies with functioning ruling parties or legislatures that share rule making have longer-lived leaders \citep{gandhi2007,magaloni2008}. Parent: H2. Falsifier: no difference in leader survival once resource rents are controlled.
   672	\item[HP3, conditional oligarchy.] Leadership turnover in membership organizations is lower where monitoring is costly, and higher where an organized internal opposition exists, as Proposition~\ref{prop:political-power:michels} predicts. Parent: H1. Falsifier: turnover unrelated to measured monitoring costs or to the presence of an organized opposition.
   673	\item[HP4, selectorate.] Smaller winning coalitions relative to the selectorate predict a higher share of private goods in public spending \citep{bdm2003}. Parent: H1. Falsifier: no association, or the reverse association.
   674	\item[HP5, religious-political bargaining.] Where rulers depend on religious legitimation, they grant religious authorities autonomy in law and education in return for support. Rubin and Kuru predict different consequences of this bargain \citep{rubin2017,kuru2019}, and both predictions should be tested. Parent: H2. Falsifier: religious autonomy that does not vary with rulers' dependence on religious legitimation.
   675	\item[HP6, brokered absolutism.] Royal rule making in the Catholic monarchies depended on negotiated intermediaries, so royal legislative success varied with the survival of provincial estates and corporate bodies \citep{beik1985}. Parent: H1. Falsifier: royal legislative success unrelated to the survival of intermediaries.
   676	\item[HP7, veto trade-off.] The number of effective veto players is positively associated with the persistence of preferential rules and negatively associated with responsiveness to changes in majority preference, as Proposition~\ref{prop:political-power:veto} predicts. Parent: H2. Falsifier: no association with the persistence of preferential rules.
   677	\end{description}
   678	
   679	HP1 and HP7 test the propositions of Section~\ref{sec:mechanisms} directly, and HP3 tests the role of organized opposition. HP2 and HP4 import established theories of autocracy into the framework, and their value here lies in coding the same variables across all six regime types. HP5 and HP6 apply to particular historical regime types and require archival coding. Identification is difficult for all seven. Appointment rules, veto structures, and legitimation strategies are chosen by rule makers, so cross-sectional associations confound the effects of these institutions with the reasons they were adopted. The source framework's event-study design, which compares outcomes before and after reforms of oversight in matched jurisdictions, is the appropriate design where such reforms occurred \citep[Section~9]{largo2026hbs}.
   680	
   681	\section{Revelation 13 and the rule-making pillar}
   682	\label{sec:revelation}
   683	
   684	The series reads Revelation typologically: the beast is a recurring pattern of power that claims ultimate loyalty, with the Roman Empire of the first century as its historical anchor \citep{bauckham1993,koester2014}. The reading identifies no present-day government, party, institution, or person with the beast, and it declines the futurist practice of doing so, whose long record of failed identifications is documented in the history of its reception \citep{fuller1995,mcginn1998}. The mapping from the text to the six pillars is an interpretive claim of the series, not a result of exegesis.
   685	
   686	Revelation 13 opens with a beast rising from the sea to whom ``the dragon gave him his power, and his seat, and great authority'' (Rev.\ 13:2, \citealp{kjv}). The rule-making authority of the beast is derived; it comes from a source outside itself and is then exercised over others. In Weber's terms the passage poses the question of legitimacy, the ground on which a claim to rule is accepted \citep{weber1978}. The text then records the response of those ruled: ``Who is like unto the beast? who is able to make war with him?'' (Rev.\ 13:4). The question describes authority that admits no contest. In the vocabulary of this paper it is an image of contestability near zero and concentration near one, the condition under which the pillar's term $H^{\pP}(1-Q^{\pP})$ in unaccountable concentration is at its maximum. The beast's reach extends ``over all kindreds, and tongues, and nations'' (Rev.\ 13:7), so a single authority governs a population whose plurality the necessity theorem takes as its starting point.
   687	
   688	Two features of the text qualify this image. The authority is repeatedly described as given, and given for a limited time: ``power was given unto him to continue forty and two months'' (Rev.\ 13:5). Within the text the beast's rule is bounded by a sovereignty it does not control. The second beast, from the earth, ``exerciseth all the power of the first beast before him'' and causes the inhabitants of the earth to worship the first (Rev.\ 13:12). Read typologically, it represents the legitimation of political authority by a second institution, a coupling of rule making with the ideological pillar that Part IV examines. Kraybill and Friesen locate the historical referent in the imperial cult of the cities of Asia Minor and its ties to commerce and civic life \citep{kraybill1996,friesen2001}, and Collins reads the book as a response to a crisis perceived by its audience \citep{collins1984}.
   689	
   690	Revelation 17 gives the clearest image of the rule-making pillar itself. The ten horns ``are ten kings, which have received no kingdom as yet; but receive power as kings one hour with the beast. These have one mind, and shall give their power and strength unto the beast'' (Rev.\ 17:12 to 13). Ten rulers who could have acted as separate veto players surrender their authority to a single center. In the terms of Proposition~\ref{prop:political-power:concentration}, the image is a move from a dispersed set of rule makers toward the dictatorship case, accomplished by delegation rather than conquest. The text then has the same kings turn on the city they served (Rev.\ 17:16), an image of the instability of coalitions that rest on delegated power. Svolik's account of authoritarian power sharing, in which the ruler's allies are also the most likely source of the ruler's removal, describes the same instability in the vocabulary of political science \citep{svolik2012}. The parallel is an interpretive analogy and makes no claim about the authorial intention of the text.
   691	
   692	Bauckham reads Revelation as a critique of Rome's claim to absolute loyalty, set against the alternative of faithful witness \citep{bauckham1993}. On this reading the object of the critique is not the existence of political authority. Paul's letter to the Romans tells its readers, ``Let every soul be subject unto the higher powers'' (Rom.\ 13:1), and Christian political ethics has long read Romans 13 and Revelation 13 together \citep{yoder1972}. The typological reading adopted here locates the warning of Revelation 13 at the point where rule making becomes unanswerable, not at the existence of rule makers. This is the theological counterpart of the distinction between Proposition A and Proposition B. Every polity has rule makers. The image of the beast applies when the rule makers can no longer be contested.
   693	
   694	\section{Objections and scope conditions}
   695	\label{sec:objections}
   696	
   697	The necessity theorem is not vacuous, because both of its substantive assumptions can fail. A group whose members always agreed would need no procedure for selecting among divergent preferences, and a group in an unchanging environment could persist without changing its rules. The predicate ``implements rule making'' is thin, but Section~\ref{sec:necessity} states what it excludes: decisions and rule changes imposed from outside, and rules that never change through environments that no single rule system could survive. A thin predicate that can fail differs from one that holds by definition.
   698	
   699	The boundary between rule making and interpretation is analytical, and it is drawn by act rather than by institution. Common-law courts make rules, constitutional courts shape legislation, and administrative agencies both make and apply regulations. Definition~\ref{def:political-power:boundary} classifies each such act, and the many-to-many role map of the source framework records an institution that does both in both pillars, with the coupling $C_{\pP\pJ}$ measuring how far one coalition controls the two. Part III applies the same classification of mixed acts from the interpretive side.
   700	
   701	Power indices measure formal power and nothing more. The Shapley-Shubik share assumes that all orderings of members are equally likely and ignores the content of proposals, the identity of agenda setters, and informal influence. The paper therefore uses the index only as a de jure baseline and pairs it with outcome-based indicators of de facto control in Table~\ref{tab:indicators}, recording the origin of proposals separately because initiation and enactment are different powers. A large gap between the two, as in brokered absolutism or patronal regimes, is itself evidence about where rule-making power lies.
   702	
   703	The comparison of regime types from different centuries is valid because it asks the same questions of each, not because the answers are commensurable in every respect. A medieval caliphate and a twenty-first century democracy face different problems with different technologies of rule. The six types are lenses, as Section~\ref{sec:regimes} states, and the comparative claims concern the distribution of a function that the necessity theorem shows all of them must perform.
   704	
   705	The theological reading is separable from the analysis. Nothing in Sections~\ref{sec:layer}, \ref{sec:necessity}, \ref{sec:mechanisms}, and~\ref{sec:measurement} depends on it, and the reading is offered as an interpretation of a text that has shaped the political imagination of many societies, with its interpretive status stated.
   706	
   707	The mechanisms are modeled in their simplest forms. Richer models of oligarchy, veto bargaining, and appointment would move the thresholds and could qualify some conclusions, so the propositions are offered as conditional mechanisms, not as complete theories.
   708	
   709	The sources for some regime types are themselves contested. For the Islamic states and the Catholic monarchies in particular, the paper relies on specialists whose interpretations are debated, and it reports their positions without adjudicating among them.
   710	
   711	\section{Conclusion}
   712	\label{sec:conclusion}
   713	
   714	Every persistent collective whose members disagree about binding choices, and whose environment changes, makes rules. The theorem of Section~\ref{sec:necessity} establishes this from explicit assumptions, and the stateless and consensus societies that seem to refute it display the function in distributed form: talk, oratory without command, collective suppression of would-be dominants, and fission. The same function is performed by parliaments, party committees, kings in council, and assemblies of jurists.
   715	
   716	The existence of the function places no constraint on its concentration. For a group of any size, procedures that satisfy the necessity theorem range from equal shares to dictatorship. Concentration, contestability, and coupling to other pillars therefore have to be measured, and the comparative evidence shows that they vary independently of the source of legitimacy that a regime claims. The conditional mechanisms of Section~\ref{sec:mechanisms} describe how rule making can drift toward capture through diffuse monitoring incentives, protected vetoes, appointment chains, and agenda control. Each mechanism has a check that acts on contestability, and none of the checks removes the need for rule makers.
   717	
   718	What remains uncertain is quantitative: how concentrated and how contestable rule making is in particular polities, and how strongly it is coupled to the other pillars. Answering these questions requires the preregistered coding that the framework specifies. The conclusion that the paper can defend is structural. The question of who makes the laws has always had an answer; whether the answer can be contested is the question on which accountability depends.
   719	
   720	\begin{thebibliography}{200}
   721	\small
   722	\setlength{\itemsep}{0pt}
   723	\bibitem[Aberle et al.(1950)]{aberle1950}
   724	Aberle, D. F., A. K. Cohen, A. K. Davis, M. J. Levy Jr., and F. X. Sutton. 1950. ``The Functional Prerequisites of a Society.'' \emph{Ethics} 60(2): 100-111. doi:10.1086/290705.
   725	
   726	\bibitem[Acemoglu and Robinson(2006)]{acemoglu2006}
   727	Acemoglu, Daron and James A. Robinson. 2006. \emph{Economic Origins of Dictatorship and Democracy}. Cambridge University Press. doi:10.1017/CBO9780511510809.
   728	
   729	\bibitem[Alfoneh(2013)]{alfoneh2013}
   730	Alfoneh, Ali. 2013. \emph{Iran Unveiled: How the Revolutionary Guards Is Transforming Iran from Theocracy into Military Dictatorship}. AEI Press.
   731	
   732	\bibitem[Ansolabehere et al.(2003)]{ansolabehere2003}
   733	Ansolabehere, Stephen, John M. de Figueiredo, and James M. Snyder. 2003. ``Why Is There So Little Money in U.S. Politics?'' \emph{Journal of Economic Perspectives} 17(1): 105-130. doi:10.1257/089533003321164976.
   734	
   735	\bibitem[Arjomand(1988)]{arjomand1988}
   736	Arjomand, Said Amir. 1988. \emph{The Turban for the Crown: The Islamic Revolution in Iran}. Oxford University Press.
   737	
   738	\bibitem[Bachrach and Baratz(1962)]{bachrach1962}
   739	Bachrach, Peter and Morton S. Baratz. 1962. ``Two Faces of Power.'' \emph{American Political Science Review} 56(4): 947-952. doi:10.2307/1952796.
   740	
   741	\bibitem[Barkey(2008)]{barkey2008}
   742	Barkey, Karen. 2008. \emph{Empire of Difference: The Ottomans in Comparative Perspective}. Cambridge University Press. doi:10.1017/cbo9780511790645.
   743	
   744	\bibitem[Bartels(2008)]{bartels2008}
   745	Bartels, Larry M. 2008. \emph{Unequal Democracy: The Political Economy of the New Gilded Age}. Princeton University Press. doi:10.1515/9781400883363.
   746	
   747	\bibitem[Bauckham(1993)]{bauckham1993}
   748	Bauckham, Richard. 1993. \emph{The Theology of the Book of Revelation}. Cambridge University Press. doi:10.1017/cbo9780511819858.
   749	
   750	\bibitem[Baumgartner et al.(2009)]{baumgartner2009}
   751	Baumgartner, Frank R., Jeffrey M. Berry, Marie Hojnacki, David C. Kimball, and Beth L. Leech. 2009. \emph{Lobbying and Policy Change: Who Wins, Who Loses, and Why}. University of Chicago Press. doi:10.7208/chicago/9780226039466.001.0001.
   752	
   753	\bibitem[Beik(1985)]{beik1985}
   754	Beik, William. 1985. \emph{Absolutism and Society in Seventeenth-Century France: State Power and Provincial Aristocracy in Languedoc}. Cambridge University Press. doi:10.1017/cbo9780511583797.
   755	
   756	\bibitem[Berman(2006)]{berman2006}
   757	Berman, Sheri. 2006. \emph{The Primacy of Politics: Social Democracy and the Making of Europe's Twentieth Century}. Cambridge University Press. doi:10.1017/cbo9780511791109.
   758	
   759	\bibitem[Bertrand et al.(2014)]{bertrand2014}
   760	Bertrand, Marianne, Matilde Bombardini, and Francesco Trebbi. 2014. ``Is It Whom You Know or What You Know? An Empirical Assessment of the Lobbying Process.'' \emph{American Economic Review} 104(12): 3885-3920. doi:10.1257/aer.104.12.3885.
   761	
   762	\bibitem[Blanes i Vidal et al.(2012)]{blanes2012}
   763	Blanes i Vidal, Jordi, Mirko Draca, and Christian Fons-Rosen. 2012. ``Revolving Door Lobbyists.'' \emph{American Economic Review} 102(7): 3731-3748. doi:10.1257/aer.102.7.3731.
   764	
   765	\bibitem[Bodin(1992)]{bodin1992}
   766	Bodin, Jean. 1992. \emph{On Sovereignty: Four Chapters from The Six Books of the Commonwealth (1576)}. Cambridge University Press (ed.~Franklin).
   767	
   768	\bibitem[Boehm(1999)]{boehm1999}
   769	Boehm, Christopher. 1999. \emph{Hierarchy in the Forest: The Evolution of Egalitarian Behavior}. Harvard University Press. doi:10.2307/j.ctvjf9xr4.
   770	
   771	\bibitem[Bossuet(1990)]{bossuet1990}
   772	Bossuet, Jacques-B\'enigne. 1990. \emph{Politics Drawn from the Very Words of Holy Scripture (1709)}. Cambridge University Press (ed.~Riley).
   773	
   774	\bibitem[Branham et al.(2017)]{branham2017}
   775	Branham, J. Alexander, Stuart N. Soroka, and Christopher Wlezien. 2017. ``When Do the Rich Win?'' \emph{Political Science Quarterly} 132(1): 43-62. doi:10.1002/polq.12577.
   776	
   777	\bibitem[Brumberg(2001)]{brumberg2001}
   778	Brumberg, Daniel. 2001. \emph{Reinventing Khomeini: The Struggle for Reform in Iran}. University of Chicago Press.
   779	
   780	\bibitem[Buchta(2000)]{buchta2000}
   781	Buchta, Wilfried. 2000. \emph{Who Rules Iran? The Structure of Power in the Islamic Republic}. Washington Institute for Near East Policy and Konrad Adenauer Stiftung.
   782	
   783	\bibitem[Bueno de Mesquita et al.(2003)]{bdm2003}
   784	Bueno de Mesquita, Bruce, Alastair Smith, Randolph M. Siverson, and James D. Morrow. 2003. \emph{The Logic of Political Survival}. MIT Press. doi:10.7551/mitpress/4292.001.0001.
   785	
   786	\bibitem[Cassinelli(1953)]{cassinelli1953}
   787	Cassinelli, C. W. 1953. ``The Law of Oligarchy.'' \emph{American Political Science Review} 47(3): 773-784. doi:10.2307/1952904.
   788	
   789	\bibitem[Clastres(1987)]{clastres1987}
   790	Clastres, Pierre. 1987. \emph{Society against the State: Essays in Political Anthropology (1974)}, trans.~Robert Hurley. Zone Books. doi:10.2307/j.ctv1595m3p.
   791	
   792	\bibitem[Collins(1984)]{collins1984}
   793	Collins, Adela Yarbro. 1984. \emph{Crisis and Catharsis: The Power of the Apocalypse}. Westminster Press.
   794	
   795	\bibitem[Collins(1995)]{collins1995}
   796	Collins, James B. 1995. \emph{The State in Early Modern France}. Cambridge University Press. doi:10.1017/cbo9781139170147.
   797	
   798	\bibitem[Commins(2006)]{commins2006}
   799	Commins, David. 2006. \emph{The Wahhabi Mission and Saudi Arabia}. I. B. Tauris. doi:10.5040/9780755609444.
   800	
   801	\bibitem[Coppedge et al.(2011)]{coppedge2011}
   802	Coppedge, Michael, John Gerring, David Altman, Michael Bernhard, Steven Fish, Allen Hicken, Matthew Kroenig, Staffan I. Lindberg, Kelly McMann, Pamela Paxton, Holli A. Semetko, Svend-Erik Skaaning, Jeffrey Staton, and Jan Teorell. 2011. ``Conceptualizing and Measuring Democracy: A New Approach.'' \emph{Perspectives on Politics} 9(2): 247-267. doi:10.1017/S1537592711000880.
   803	
   804	\bibitem[Cox et al.(2010)]{cox2010}
   805	Cox, Michael, Gwen Arnold, and Sergio Villamayor Tomas. 2010. ``A Review of Design Principles for Community-based Natural Resource Management.'' \emph{Ecology and Society} 15(4): 38. doi:10.5751/ES-03704-150438.
   806	
   807	\bibitem[Crone and Hinds(1986)]{crone1986}
   808	Crone, Patricia and Martin Hinds. 1986. \emph{God's Caliph: Religious Authority in the First Centuries of Islam}. Cambridge University Press.
   809	
   810	\bibitem[Crone(2004)]{crone2004}
   811	Crone, Patricia. 2004. \emph{God's Rule: Government and Islam: Six Centuries of Medieval Islamic Political Thought}. Columbia University Press.
   812	
   813	\bibitem[Culpepper(2010)]{culpepper2010}
   814	Culpepper, Pepper D. 2010. \emph{Quiet Politics and Business Power: Corporate Control in Europe and Japan}. Cambridge University Press. doi:10.1017/cbo9780511760716.
   815	
   816	\bibitem[Dahl(1961)]{dahl1961}
   817	Dahl, Robert A. 1961. \emph{Who Governs? Democracy and Power in an American City}. Yale University Press.
   818	
   819	\bibitem[Dahl(1971)]{dahl1971}
   820	Dahl, Robert A. 1971. \emph{Polyarchy: Participation and Opposition}. Yale University Press.
   821	
   822	\bibitem[Djilas(1957)]{djilas1957}
   823	Djilas, Milovan. 1957. \emph{The New Class: An Analysis of the Communist System}. Praeger.
   824	
   825	\bibitem[Elkjaer and Klitgaard(2024)]{elkjaer2024}
   826	Elkjaer, Mads Andreas and Michael Baggesen Klitgaard. 2024. ``Economic Inequality and Political Responsiveness: A Systematic Review.'' \emph{Perspectives on Politics} 22(2): 318-337. doi:10.1017/S1537592721002188.
   827	
   828	\bibitem[Ellickson(1991)]{ellickson1991}
   829	Ellickson, Robert C. 1991. \emph{Order without Law: How Neighbors Settle Disputes}. Harvard University Press. doi:10.4159/9780674036437.
   830	
   831	\bibitem[Elliott(1963)]{elliott1963}
   832	Elliott, J. H. 1963. \emph{Imperial Spain 1469-1716}. Edward Arnold.
   833	
   834	\bibitem[Elliott(1984)]{elliott1984}
   835	Elliott, J. H. 1984. \emph{Richelieu and Olivares}. Cambridge University Press.
   836	
   837	\bibitem[Elster(1983)]{elster1983}
   838	Elster, Jon. 1983. \emph{Explaining Technical Change: A Case Study in the Philosophy of Science}. Cambridge University Press.
   839	
   840	\bibitem[Ertman(1997)]{ertman1997}
   841	Ertman, Thomas. 1997. \emph{Birth of the Leviathan: Building States and Regimes in Medieval and Early Modern Europe}. Cambridge University Press. doi:10.1017/cbo9780511529016.
   842	
   843	\bibitem[Esping-Andersen(1985)]{esping1985}
   844	Esping-Andersen, G{\o}sta. 1985. \emph{Politics against Markets: The Social Democratic Road to Power}. Princeton University Press. doi:10.1515/9781400886203.
   845	
   846	\bibitem[Evans-Pritchard(1940)]{evanspritchard1940}
   847	Evans-Pritchard, E. E. 1940. \emph{The Nuer: A Description of the Modes of Livelihood and Political Institutions of a Nilotic People}. Clarendon Press.
   848	
   849	\bibitem[Fainsod(1953)]{fainsod1953}
   850	Fainsod, Merle. 1953. \emph{How Russia Is Ruled}. Harvard University Press. doi:10.4159/harvard.9780674189188.
   851	
   852	\bibitem[Figgis(1914)]{figgis1914}
   853	Figgis, John Neville. 1914. \emph{The Divine Right of Kings}. Cambridge University Press.
   854	
   855	\bibitem[Friesen(2001)]{friesen2001}
   856	Friesen, Steven J. 2001. \emph{Imperial Cults and the Apocalypse of John: Reading Revelation in the Ruins}. Oxford University Press. doi:10.1093/0195131533.001.0001.
   857	
   858	\bibitem[Fuller(1995)]{fuller1995}
   859	Fuller, Robert C. 1995. \emph{Naming the Antichrist: The History of an American Obsession}. Oxford University Press. doi:10.1093/acprof:oso/9780195109795.001.0001.
   860	
   861	\bibitem[Gandhi and Przeworski(2007)]{gandhi2007}
   862	Gandhi, Jennifer and Adam Przeworski. 2007. ``Authoritarian Institutions and the Survival of Autocrats.'' \emph{Comparative Political Studies} 40(11): 1279-1301. doi:10.1177/0010414007305817.
   863	
   864	\bibitem[Gause(1994)]{gause1994}
   865	Gause, F. Gregory III. 1994. \emph{Oil Monarchies: Domestic and Security Challenges in the Arab Gulf States}. Council on Foreign Relations Press.
   866	
   867	\bibitem[Geddes et al.(2014)]{geddes2014}
   868	Geddes, Barbara, Joseph Wright, and Erica Frantz. 2014. ``Autocratic Breakdown and Regime Transitions: A New Data Set.'' \emph{Perspectives on Politics} 12(2): 313-331. doi:10.1017/S1537592714000851.
   869	
   870	\bibitem[Gerschewski(2013)]{gerschewski2013}
   871	Gerschewski, Johannes. 2013. ``The Three Pillars of Stability: Legitimation, Repression, and Co-optation in Autocratic Regimes.'' \emph{Democratization} 20(1): 13-38. doi:10.1080/13510347.2013.738860.
   872	
   873	\bibitem[Gilens and Page(2014)]{gilens2014}
   874	Gilens, Martin and Benjamin I. Page. 2014. ``Testing Theories of American Politics: Elites, Interest Groups, and Average Citizens.'' \emph{Perspectives on Politics} 12(3): 564-581. doi:10.1017/S1537592714001595.
   875	
   876	\bibitem[Graeber and Wengrow(2021)]{graeber2021}
   877	Graeber, David and David Wengrow. 2021. \emph{The Dawn of Everything: A New History of Humanity}. Farrar, Straus and Giroux.
   878	
   879	\bibitem[Guriev and Treisman(2019)]{guriev2019}
   880	Guriev, Sergei and Daniel Treisman. 2019. ``Informational Autocrats.'' \emph{Journal of Economic Perspectives} 33(4): 100-127. doi:10.1257/jep.33.4.100.
   881	
   882	\bibitem[Hacker and Pierson(2010)]{hackerpierson2010}
   883	Hacker, Jacob S. and Paul Pierson. 2010. \emph{Winner-Take-All Politics: How Washington Made the Rich Richer and Turned Its Back on the Middle Class}. Simon \& Schuster.
   884	
   885	\bibitem[Hale(2014)]{hale2014}
   886	Hale, Henry E. 2014. \emph{Patronal Politics: Eurasian Regime Dynamics in Comparative Perspective}. Cambridge University Press. doi:10.1017/CBO9781139683524.
   887	
   888	\bibitem[Hall and Deardorff(2006)]{hall2006}
   889	Hall, Richard L. and Alan V. Deardorff. 2006. ``Lobbying as Legislative Subsidy.'' \emph{American Political Science Review} 100(1): 69-84. doi:10.1017/s0003055406062010.
   890	
   891	\bibitem[Hallaq(2013)]{hallaq2013}
   892	Hallaq, Wael B. 2013. \emph{The Impossible State: Islam, Politics, and Modernity's Moral Predicament}. Columbia University Press.
   893	
   894	\bibitem[Hart(1961)]{hart1961}
   895	Hart, H. L. A. 1961. \emph{The Concept of Law}. Clarendon Press (3rd ed.~2012, Oxford University Press). doi:10.1093/he/9780199644704.001.0001.
   896	
   897	\bibitem[Hayek(1973)]{hayek1973}
   898	Hayek, Friedrich A. 1973. \emph{Law, Legislation and Liberty, Volume 1: Rules and Order}. University of Chicago Press. doi:10.7208/chicago/9780226321233.001.0001.
   899	
   900	\bibitem[Hegghammer(2010)]{hegghammer2010}
   901	Hegghammer, Thomas. 2010. \emph{Jihad in Saudi Arabia: Violence and Pan-Islamism since 1979}. Cambridge University Press. doi:10.1017/cbo9780511809439.
   902	
   903	\bibitem[Hempel(1959)]{hempel1959}
   904	Hempel, Carl G. 1959. ``The Logic of Functional Analysis.'' In \emph{Symposium on Sociological Theory}, ed.~Llewellyn Gross, Harper \& Row, pp.~271-307.
   905	
   906	\bibitem[Hertog(2010)]{hertog2010}
   907	Hertog, Steffen. 2010. \emph{Princes, Brokers, and Bureaucrats: Oil and the State in Saudi Arabia}. Cornell University Press. doi:10.7591/9780801458774.
   908	
   909	\bibitem[Hirschl(2004)]{hirschl2004}
   910	Hirschl, Ran. 2004. \emph{Towards Juristocracy: The Origins and Consequences of the New Constitutionalism}. Harvard University Press. doi:10.2307/j.ctv15d81nb.
   911	
   912	\bibitem[Hough and Fainsod(1979)]{hough1979}
   913	Hough, Jerry F. and Merle Fainsod. 1979. \emph{How the Soviet Union Is Governed}. Harvard University Press.
   914	
   915	\bibitem[Huber and Stephens(2001)]{huber2001}
   916	Huber, Evelyne and John D. Stephens. 2001. \emph{Development and Crisis of the Welfare State: Parties and Policies in Global Markets}. University of Chicago Press. doi:10.7208/chicago/9780226356495.001.0001.
   917	
   918	\bibitem[Imber(1997)]{imber1997}
   919	Imber, Colin. 1997. \emph{Ebu's-su'ud: The Islamic Legal Tradition}. Stanford University Press.
   920	
   921	\bibitem[Islamic Republic of Iran(1989)]{iranconst}
   922	Islamic Republic of Iran. 1989. \emph{Constitution of the Islamic Republic of Iran (1979, revised 1989)}. English translation, Constitute Project. \url{https://www.constituteproject.org/constitution/Iran_1989}.
   923	
   924	\bibitem[Kalla and Broockman(2016)]{kalla2016}
   925	Kalla, Joshua L. and David E. Broockman. 2016. ``Campaign Contributions Facilitate Access to Congressional Officials: A Randomized Field Experiment.'' \emph{American Journal of Political Science} 60(3): 545-558. doi:10.1111/ajps.12180.
   926	
   927	\bibitem[Kantorowicz(1957)]{kantorowicz1957}
   928	Kantorowicz, Ernst H. 1957. \emph{The King's Two Bodies: A Study in Mediaeval Political Theology}. Princeton University Press. doi:10.1515/9781400880782.
   929	
   930	\bibitem[Kelly(1995)]{kelly1995}
   931	Kelly, Robert L. 1995. \emph{The Foraging Spectrum: Diversity in Hunter-Gatherer Lifeways}. Smithsonian Institution Press. doi:10.2307/j.ctv2sx9gc9.
   932	
   933	\bibitem[Khomeini(1981)]{khomeini1981}
   934	Khomeini, Ruhollah. 1981. \emph{Islam and Revolution: Writings and Declarations of Imam Khomeini (incl.~Islamic Government, 1970)}, trans.~Hamid Algar. Mizan Press.
   935	
   936	\bibitem[King James Version(1611)]{kjv}
   937	King James Version. 1611. \emph{The Holy Bible, Authorized King James Version}. Project Gutenberg eBook 10. \url{https://www.gutenberg.org/ebooks/10}.
   938	
   939	\bibitem[Kingdom of Saudi Arabia(1992)]{saudibasic}
   940	Kingdom of Saudi Arabia. 1992. \emph{Basic Law of Governance (1992, revised 2013)}. English translation, Constitute Project. \url{https://www.constituteproject.org/constitution/Saudi_Arabia_2013}.
   941	
   942	\bibitem[Kitschelt(1994)]{kitschelt1994}
   943	Kitschelt, Herbert. 1994. \emph{The Transformation of European Social Democracy}. Cambridge University Press. doi:10.1017/CBO9780511622014.
   944	
   945	\bibitem[Koester(2014)]{koester2014}
   946	Koester, Craig R. 2014. \emph{Revelation: A New Translation with Introduction and Commentary}. Yale University Press (Anchor Yale Bible 38A). doi:10.12987/9780300211030.
   947	
   948	\bibitem[Kornai(1992)]{kornai1992}
   949	Kornai, J\'anos. 1992. \emph{The Socialist System: The Political Economy of Communism}. Princeton University Press. doi:10.2307/j.ctv1ddczdr.
   950	
   951	\bibitem[Korpi(1983)]{korpi1983}
   952	Korpi, Walter. 1983. \emph{The Democratic Class Struggle}. Routledge \& Kegan Paul.
   953	
   954	\bibitem[Kraybill(1996)]{kraybill1996}
   955	Kraybill, J. Nelson. 1996. \emph{Imperial Cult and Commerce in John's Apocalypse}. Sheffield Academic Press (JSNT Supplement 132).
   956	
   957	\bibitem[Kuran(2011)]{kuran2011}
   958	Kuran, Timur. 2011. \emph{The Long Divergence: How Islamic Law Held Back the Middle East}. Princeton University Press. doi:10.1515/9781400836017.
   959	
   960	\bibitem[Kuru(2019)]{kuru2019}
   961	Kuru, Ahmet T. 2019. \emph{Islam, Authoritarianism, and Underdevelopment: A Global and Historical Comparison}. Cambridge University Press. doi:10.1017/9781108296892.
   962	
   963	\bibitem[Lambton(1981)]{lambton1981}
   964	Lambton, Ann K. S. 1981. \emph{State and Government in Medieval Islam}. Oxford University Press. doi:10.4324/9780203385463.
   965	
   966	\bibitem[Landry(2008)]{landry2008}
   967	Landry, Pierre F. 2008. \emph{Decentralized Authoritarianism in China: The Communist Party's Control of Local Elites in the Post-Mao Era}. Cambridge University Press. doi:10.1017/CBO9780511510243.
   968	
   969	\bibitem[Lane and Ross(1995)]{lane1995}
   970	Lane, David and Cameron Ross. 1995. ``The CPSU Ruling Elite 1981-1991: Commonalities and Divisions.'' \emph{Communist and Post-Communist Studies} 28(3): 339-360. doi:10.1016/0967-067X(95)00020-U.
   971	
   972	\bibitem[Largo(2026)]{largo2026hbs}
   973	Largo, Mateo. 2026. \emph{The Hierarchy of the Beast System: Institutional Power, Elite Coordination, and Economic Dependency Across Political Regimes}. Working paper, 14 October 2026.
   974	
   975	\bibitem[Lee(2013)]{lee2013}
   976	Lee, Richard B. 2013. \emph{The Dobe Ju/'hoansi (4th edition)}. Wadsworth/Cengage Learning.
   977	
   978	\bibitem[Levitsky and Way(2010)]{levitsky2010}
   979	Levitsky, Steven and Lucan A. Way. 2010. \emph{Competitive Authoritarianism: Hybrid Regimes after the Cold War}. Cambridge University Press. doi:10.1017/CBO9780511781353.
   980	
   981	\bibitem[Lijphart(1999)]{lijphart1999}
   982	Lijphart, Arend. 1999. \emph{Patterns of Democracy: Government Forms and Performance in Thirty-Six Countries}. Yale University Press. doi:10.12987/9780300189124.
   983	
   984	\bibitem[Lindblom(1977)]{lindblom1977}
   985	Lindblom, Charles E. 1977. \emph{Politics and Markets: The World's Political-Economic Systems}. Basic Books.
   986	
   987	\bibitem[Linz(1990)]{linz1990}
   988	Linz, Juan J. 1990. ``The Perils of Presidentialism.'' \emph{Journal of Democracy} 1(1): 51-69. doi:10.1353/jod.2005.0026.
   989	
   990	\bibitem[Lipset et al.(1956)]{lipset1956}
   991	Lipset, Seymour Martin, Martin A. Trow, and James S. Coleman. 1956. \emph{Union Democracy: The Internal Politics of the International Typographical Union}. Free Press.
   992	
   993	\bibitem[Long(2026a)]{long2026coercive}
   994	Long, Matthew. 2026a. \emph{Coercive Power and Enforcement}. Part V of The Six Pillars of the Beast System. Working paper, October 2026.
   995	
   996	\bibitem[Long(2026b)]{long2026financial}
   997	Long, Matthew. 2026b. \emph{Financial Power and Resource Command}. Part I of The Six Pillars of the Beast System. Working paper, October 2026.
   998	
   999	\bibitem[Long(2026c)]{long2026formalized}
  1000	Long, Matthew. 2026c. \emph{The Formalized State: The Hierarchy of the Beast System}. Part VII of The Six Pillars of the Beast System. Working paper, in preparation.
  1001	
  1002	\bibitem[Long(2026d)]{long2026ideological}
  1003	Long, Matthew. 2026d. \emph{Ideological Power and Legitimation}. Part IV of The Six Pillars of the Beast System. Working paper, October 2026.
  1004	
  1005	\bibitem[Long(2026e)]{long2026judicial}
  1006	Long, Matthew. 2026e. \emph{Judicial Power and Legal Interpretation}. Part III of The Six Pillars of the Beast System. Working paper, October 2026.
  1007	
  1008	\bibitem[Long(2026f)]{long2026productive}
  1009	Long, Matthew. 2026f. \emph{Productive Power and Social Reproduction}. Part VI of The Six Pillars of the Beast System. Working paper, October 2026.
  1010	
  1011	\bibitem[L\"uhrmann et al.(2018)]{luhrmann2018}
  1012	L\"uhrmann, Anna, Marcus Tannenberg, and Staffan I. Lindberg. 2018. ``Regimes of the World (RoW): Opening New Avenues for the Comparative Study of Political Regimes.'' \emph{Politics and Governance} 6(1): 60-77. doi:10.17645/pag.v6i1.1214.
  1013	
  1014	\bibitem[Lukes(2005)]{lukes2005}
  1015	Lukes, Steven. 2005. \emph{Power: A Radical View}. Palgrave Macmillan. doi:10.1007/978-0-230-80257-5.
  1016	
  1017	\bibitem[Madison(1788)]{madison1788}
  1018	Madison, James. 1788. \emph{The Federalist No.~51: The Structure of the Government Must Furnish the Proper Checks and Balances}. Independent Journal, 6 February 1788. \url{https://avalon.law.yale.edu/18th_century/fed51.asp}.
  1019	
  1020	\bibitem[Magaloni(2008)]{magaloni2008}
  1021	Magaloni, Beatriz. 2008. ``Credible Power-Sharing and the Longevity of Authoritarian Rule.'' \emph{Comparative Political Studies} 41(4-5): 715-741. doi:10.1177/0010414007313124.
  1022	
  1023	\bibitem[al-Mawardi(1996)]{mawardi1996}
  1024	al-Mawardi, Abu al-Hasan. 1996. \emph{The Ordinances of Government (al-Ahkam al-Sultaniyya, c.~1058)}, trans.~Wafaa H. Wahba. Garnet Publishing.
  1025	
  1026	\bibitem[McGinn(1998)]{mcginn1998}
  1027	McGinn, Bernard. 1998. \emph{Antichrist: Two Thousand Years of the Human Fascination with Evil}. Columbia University Press.
  1028	
  1029	\bibitem[Merton(1968)]{merton1968}
  1030	Merton, Robert K. 1968. \emph{Social Theory and Social Structure (enlarged edition)}. Free Press.
  1031	
  1032	\bibitem[Michels(1915)]{michels1915}
  1033	Michels, Robert. 1915. \emph{Political Parties: A Sociological Study of the Oligarchical Tendencies of Modern Democracy}. Hearst's International Library.
  1034	
  1035	\bibitem[Mills(1956)]{mills1956}
  1036	Mills, C. Wright. 1956. \emph{The Power Elite}. Oxford University Press.
  1037	
  1038	\bibitem[Minzner(2011)]{minzner2011}
  1039	Minzner, Carl F. 2011. ``China's Turn against Law.'' \emph{American Journal of Comparative Law} 59(4): 935-984. doi:10.5131/ajcl.2011.0006.
  1040	
  1041	\bibitem[Montesquieu(1989)]{montesquieu1989}
  1042	Montesquieu, Charles de Secondat. 1989. \emph{The Spirit of the Laws (1748)}, ed.~Cohler, Miller, Stone. Cambridge University Press.
  1043	
  1044	\bibitem[Mosca(1939)]{mosca1939}
  1045	Mosca, Gaetano. 1939. \emph{The Ruling Class (Elementi di scienza politica)}. McGraw-Hill.
  1046	
  1047	\bibitem[Olson(1965)]{olson1965}
  1048	Olson, Mancur. 1965. \emph{The Logic of Collective Action: Public Goods and the Theory of Groups}. Harvard University Press. doi:10.4159/9780674041660.
  1049	
  1050	\bibitem[Ostrom(1990)]{ostrom1990}
  1051	Ostrom, Elinor. 1990. \emph{Governing the Commons: The Evolution of Institutions for Collective Action}. Cambridge University Press. doi:10.1017/CBO9780511807763.
  1052	
  1053	\bibitem[Ostrom(2010)]{ostromdesign2010}
  1054	Ostrom, Elinor. 2010. ``Beyond Markets and States: Polycentric Governance of Complex Economic Systems.'' \emph{American Economic Review} 100(3): 641-672. doi:10.1257/aer.100.3.641.
  1055	
  1056	\bibitem[Parsons(1951)]{parsons1951}
  1057	Parsons, Talcott. 1951. \emph{The Social System}. Free Press. doi:10.4324/9780203992951.
  1058	
  1059	\bibitem[Peltzman(1976)]{peltzman1976}
  1060	Peltzman, Sam. 1976. ``Toward a More General Theory of Regulation.'' \emph{The Journal of Law and Economics} 19(2): 211-240. doi:10.1086/466865.
  1061	
  1062	\bibitem[Pettit(1997)]{pettit1997}
  1063	Pettit, Philip. 1997. \emph{Republicanism: A Theory of Freedom and Government}. Oxford University Press. doi:10.1093/0198296428.001.0001.
  1064	
  1065	\bibitem[Pontusson(1992)]{pontusson1992}
  1066	Pontusson, Jonas. 1992. \emph{The Limits of Social Democracy: Investment Politics in Sweden}. Cornell University Press. doi:10.7591/9781501737541.
  1067	
  1068	\bibitem[Prodi(1987)]{prodi1987}
  1069	Prodi, Paolo. 1987. \emph{The Papal Prince: One Body and Two Souls: The Papal Monarchy in Early Modern Europe}. Cambridge University Press.
  1070	
  1071	\bibitem[Przeworski(1985)]{przeworski1985}
  1072	Przeworski, Adam. 1985. \emph{Capitalism and Social Democracy}. Cambridge University Press. doi:10.1017/cbo9781139171830.
  1073	
  1074	\bibitem[Przeworski(1991)]{przeworski1991}
  1075	Przeworski, Adam. 1991. \emph{Democracy and the Market: Political and Economic Reforms in Eastern Europe and Latin America}. Cambridge University Press. doi:10.1017/CBO9781139172493.
  1076	
  1077	\bibitem[Al-Rasheed(2002)]{alrasheed2002}
  1078	Al-Rasheed, Madawi. 2002. \emph{A History of Saudi Arabia}. Cambridge University Press. doi:10.1017/cbo9780511993510.
  1079	
  1080	\bibitem[Root(1987)]{root1987}
  1081	Root, Hilton L. 1987. \emph{Peasants and King in Burgundy: Agrarian Foundations of French Absolutism}. University of California Press. doi:10.1525/9780520913349.
  1082	
  1083	\bibitem[Ross(2001)]{ross2001}
  1084	Ross, Michael L. 2001. ``Does Oil Hinder Democracy?'' \emph{World Politics} 53(3): 325-361. doi:10.1353/wp.2001.0011.
  1085	
  1086	\bibitem[Rothstein(1996)]{rothstein1996}
  1087	Rothstein, Bo. 1996. \emph{The Social Democratic State: The Swedish Model and the Bureaucratic Problem of Social Reforms}. University of Pittsburgh Press. doi:10.2307/jj.13110785.
  1088	
  1089	\bibitem[Rubin(2017)]{rubin2017}
  1090	Rubin, Jared. 2017. \emph{Rulers, Religion, and Riches: Why the West Got Rich and the Middle East Did Not}. Cambridge University Press. doi:10.1017/9781139568272.
  1091	
  1092	\bibitem[Schirazi(1997)]{schirazi1997}
  1093	Schirazi, Asghar. 1997. \emph{The Constitution of Iran: Politics and the State in the Islamic Republic}. I. B. Tauris.
  1094	
  1095	\bibitem[Schumpeter(1942)]{schumpeter1942}
  1096	Schumpeter, Joseph A. 1942. \emph{Capitalism, Socialism and Democracy}. Harper \& Brothers. doi:10.4324/9780203857090.
  1097	
  1098	\bibitem[Scott(2009)]{scott2009}
  1099	Scott, James C. 2009. \emph{The Art of Not Being Governed: An Anarchist History of Upland Southeast Asia}. Yale University Press. doi:10.12987/9780300156522.
  1100	
  1101	\bibitem[Scott(2017)]{scott2017}
  1102	Scott, James C. 2017. \emph{Against the Grain: A Deep History of the Earliest States}. Yale University Press. doi:10.12987/9780300231687.
  1103	
  1104	\bibitem[Shapley and Shubik(1954)]{shapley1954}
  1105	Shapley, L. S. and Martin Shubik. 1954. ``A Method for Evaluating the Distribution of Power in a Committee System.'' \emph{American Political Science Review} 48(3): 787-792. doi:10.2307/1951053.
  1106	
  1107	\bibitem[Shirk(1993)]{shirk1993}
  1108	Shirk, Susan L. 1993. \emph{The Political Logic of Economic Reform in China}. University of California Press. doi:10.1525/9780520912212.
  1109	
  1110	\bibitem[Stigler(1971)]{stigler1971}
  1111	Stigler, George J. 1971. ``The Theory of Economic Regulation.'' \emph{The Bell Journal of Economics and Management Science} 2(1): 3-21. doi:10.2307/3003160.
  1112	
  1113	\bibitem[Stone Sweet(2000)]{stonesweet2000}
  1114	Stone Sweet, Alec. 2000. \emph{Governing with Judges: Constitutional Politics in Europe}. Oxford University Press. doi:10.1093/0198297718.001.0001.
  1115	
  1116	\bibitem[Svolik(2012)]{svolik2012}
  1117	Svolik, Milan W. 2012. \emph{The Politics of Authoritarian Rule}. Cambridge University Press. doi:10.1017/CBO9781139176040.
  1118	
  1119	\bibitem[Tsebelis(2002)]{tsebelis2002}
  1120	Tsebelis, George. 2002. \emph{Veto Players: How Political Institutions Work}. Princeton University Press. doi:10.1515/9781400831456.
  1121	
  1122	\bibitem[Van Kley(1996)]{vankley1996}
  1123	Van Kley, Dale K. 1996. \emph{The Religious Origins of the French Revolution: From Calvin to the Civil Constitution, 1560-1791}. Yale University Press.
  1124	
  1125	\bibitem[Voslensky(1984)]{voslensky1984}
  1126	Voslensky, Michael. 1984. \emph{Nomenklatura: The Soviet Ruling Class}. Doubleday.
  1127	
  1128	\bibitem[Voss and Sherman(2000)]{voss2000}
  1129	Voss, Kim and Rachel Sherman. 2000. ``Breaking the Iron Law of Oligarchy: Union Revitalization in the American Labor Movement.'' \emph{American Journal of Sociology} 106(2): 303-349. doi:10.1086/316963.
  1130	
  1131	\bibitem[Weber(1946)]{weber1946}
  1132	Weber, Max. 1946. ``Politics as a Vocation.'' In \emph{From Max Weber: Essays in Sociology}, ed.~Gerth and Mills, Oxford University Press, pp.~77-128.
  1133	
  1134	\bibitem[Weber(1978)]{weber1978}
  1135	Weber, Max. 1978. \emph{Economy and Society: An Outline of Interpretive Sociology}. University of California Press. doi:10.4159/9780674240827.
  1136	
  1137	\bibitem[Weingast(1997)]{weingast1997}
  1138	Weingast, Barry R. 1997. ``The Political Foundations of Democracy and the Rule of Law.'' \emph{American Political Science Review} 91(2): 245-263. doi:10.2307/2952354.
  1139	
  1140	\bibitem[Wiessner(2005)]{wiessner2005}
  1141	Wiessner, Polly. 2005. ``Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity?'' \emph{Human Nature} 16(2): 115-145. doi:10.1007/s12110-005-1000-9.
  1142	
  1143	\bibitem[Winters(2011)]{winters2011}
  1144	Winters, Jeffrey A. 2011. \emph{Oligarchy}. Cambridge University Press. doi:10.1017/cbo9780511793806.
  1145	
  1146	\bibitem[Woodburn(1982)]{woodburn1982}
  1147	Woodburn, James. 1982. ``Egalitarian Societies.'' \emph{Man (N.S.)} 17(3): 431-451. doi:10.2307/2801707.
  1148	
  1149	\bibitem[Yoder(1972)]{yoder1972}
  1150	Yoder, John Howard. 1972. \emph{The Politics of Jesus}. Eerdmans.
  1151	
  1152	\end{thebibliography}
  1153	\end{document}

codex
The first read was truncated by output limits, so I’m continuing with bounded line ranges from the same file only. I’ll distinguish definite source issues from warnings that require an actual TeX log to confirm.
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '581,800p' papers/latex/political-power.tex | nl -ba -v 581" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   581	\item If $K\subseteq K'$, then $W_{K'}(q)\subseteq W_K(q)$.
   582	\item If some $i\in K$ prefers $q$ to every other alternative, then $W_K(q)=\emptyset$.
   583	\item Let $q$ be a preferential rule, one that every member of a group $B$ prefers to every other alternative, and let $x\neq q$ be a reform that every member of $K\setminus B$ prefers to $q$. Under a pure veto-player procedure, $x$ can replace $q$ if and only if $K\cap B=\emptyset$.
   584	\end{enumerate}
   585	\end{proposition}
   586	
   587	\begin{proof}
   588	(a) An alternative in $W_{K'}(q)$ is preferred to $q$ by every member of $K'$, and so by every member of $K$. (b) If $i\in K$ prefers $q$ to every $x\neq q$, no $x$ is preferred to $q$ by $i$, so no $x$ lies in $W_K(q)$. (c) If $K\cap B=\emptyset$, every member of $K$ prefers $x$ to $q$, so $x\in W_K(q)$. If some $i\in K\cap B$, then $i$ prefers $q$ to $x$, so $x\notin W_K(q)$.
   589	\end{proof}
   590	
   591	Part (c) contains the trade-off. A preferential rule survives any reform whenever one of its beneficiaries holds a veto. Adding veto players protects the polity against new preferential rules, because a new rule must pass every veto player, and it protects existing preferential rules, because their repeal must also pass every veto player. Part (a) states the general form: the set of possible changes can only shrink as veto players are added. This is why the hypothesis HP7 in Section~\ref{sec:measurement} predicts that the number of effective veto players is associated both with the persistence of preferential rules and with low responsiveness. The same logic explains the status-quo bias of consensus societies in Proposition~\ref{prop:political-power:minimal-form}, where every adult holds a veto.
   592	
   593	The check implied by the proposition is not more veto players but the control of who holds them. A veto held by an independent body with no stake in a preferential rule, such as a court reviewing a statute against a general constitutional standard, constrains new preferential rules without protecting old ones, provided the body cannot itself be captured. That condition is the subject of Part III.
   594	
   595	\subsection{The appointment channel}
   596	
   597	The source framework defines cross-pillar integration $C_{mn}$ only descriptively, as the extent to which one coalition commands appointments, budgets, sanctions, or agenda in two pillars \citep{largo2026hbs}, and Part VII fixes a formal definition for the series. The appointment channel acquires testable content under one explicit candidate, the coalition-overlap measure. Let $\mathcal{S}$ be a preregistered list of coherent coalitions, groups such as parties, factions, or dynasties that can issue joint directives. For $S\in\mathcal{S}$ let $s^{\pP}(S)$ be the Shapley-Shubik share of the bloc player $p_S$ in the quotient game on $N_S=(N\setminus S)\cup\{p_S\}$, whose winning coalitions are defined for $T\subseteq N\setminus S$ by $T\in\Win_S$ if and only if $T\in\Win$, and $T\cup\{p_S\}\in\Win_S$ if and only if $T\cup S\in\Win$. This bloc share is not in general the sum of the members' separate shares; in the Iranian example of Table~\ref{tab:examples} the two councils hold $1/6+1/6$ separately and $1/2$ as a bloc. Let $\kappa_\ell(S)\in[0,1]$ be the share of decision-relevant control in pillar $\ell$ that is exercised in accordance with the directives of $S$, and set
   598	\begin{equation}
   599	C^{\mathrm{ov}}_{\pP\ell}=\max_{S\in\mathcal{S}}\min\{s^{\pP}(S),\kappa_\ell(S)\}.
   600	\label{eq:overlap}
   601	\end{equation}
   602	The candidate lies in $[0,1]$, equals one when a single coalition holds all rule-making control and commands all of pillar $\ell$, and equals zero when no listed coalition has a positive share in both.
   603	
   604	\begin{proposition}[Appointment bounds on integration]
   605	\label{prop:political-power:appointment-bound}
   606	For a coalition $S$ and an office $o$ let $f_{S,o}\in[0,1]$ be the share of the holder's decisions that follow the directives of $S$. For $S\in\mathcal{S}$ with $\alpha_{S,\ell}>0$ define the loyalty of its appointees as the conditional average
   607	\[
   608	\lambda_S=\frac{1}{\alpha_{S,\ell}}\sum_{o\in O_\ell}w_o f_{S,o}\,\mathbf{1}[S\text{ can unilaterally appoint or remove the holder of }o],
   609	\]
   610	and set $\lambda_S=0$ when $\alpha_{S,\ell}=0$. Suppose that command in pillar $\ell$ decomposes as $\kappa_\ell(S)=\lambda_S\alpha_{S,\ell}+\gamma_S$, where $\gamma_S\in[0,1-\lambda_S\alpha_{S,\ell}]$ is command exercised through channels other than appointment, such as budgets, sanctions, and informal patronage. Then:
   611	\begin{enumerate}[label=(\alph*)]
   612	\item for every $S\in\mathcal{S}$, $C^{\mathrm{ov}}_{\pP\ell}\ge\min\{s^{\pP}(S),\lambda_S\alpha_{S,\ell}\}$;
   613	\item if command runs only through appointment ($\gamma_S=0$ for all $S$) and loyalty is at most $\bar\lambda$ ($\lambda_S\le\bar\lambda$ for all $S$), then $C^{\mathrm{ov}}_{\pP\ell}\le\bar\lambda\max_{S\in\mathcal{S}}\alpha_{S,\ell}$;
   614	\item if command runs only through appointment and no listed coalition can unilaterally appoint or remove the holder of any office in $O_\ell$, for example because both appointment and removal require the consent of two bodies controlled by different coalitions, then $C^{\mathrm{ov}}_{\pP\ell}=0$.
   615	\end{enumerate}
   616	\end{proposition}
   617	
   618	\begin{proof}
   619	(a) By Equation~\eqref{eq:overlap}, $C^{\mathrm{ov}}_{\pP\ell}\ge\min\{s^{\pP}(S),\kappa_\ell(S)\}$. Since $\gamma_S\ge0$, $\kappa_\ell(S)\ge\lambda_S\alpha_{S,\ell}$, and the minimum is nondecreasing in each argument. (b) For every $S$, $\min\{s^{\pP}(S),\kappa_\ell(S)\}\le\kappa_\ell(S)=\lambda_S\alpha_{S,\ell}\le\bar\lambda\max_{S'}\alpha_{S',\ell}$; take the maximum over $S$. (c) The hypothesis gives $\alpha_{S,\ell}=0$ for every $S\in\mathcal{S}$ by Definition~\ref{def:political-power:appointment-channel}, and (b) gives $C^{\mathrm{ov}}_{\pP\ell}\le0$.
   620	\end{proof}
   621	
   622	The proposition separates three quantities that comparative accounts often run together. The rule-making share $s^{\pP}(S)$ says how much of rule making the coalition controls. The appointment share $\alpha_{S,\ell}$ says how many posts in another pillar it fills. The loyalty parameter $\lambda_S$ says how far the people it appoints do what it wants. Nomenklatura systems maximize the first two, and part (a) then makes integration high unless loyalty is low. The Soviet evidence of elite divisions \citep{lane1995} and of bureaucratic bargaining \citep{hough1979} concerns loyalty, and so it limits the integration that appointment alone can produce. Parts (b) and (c) identify the check. Requiring the consent of a second body for both appointment and removal closes the appointment channel to any single coalition, and security of tenure lowers loyalty after appointment by removing the threat of dismissal. Under plural appointment any remaining integration must run through budgets, sanctions, or patronage ($\gamma_S$), which tells an investigator where to look.
   623	
   624	\subsection{Agenda control and quiet politics}
   625	
   626	The three propositions concern visible procedures. A fourth mechanism operates through what never reaches a procedure. An actor with agenda control can keep a reform off the agenda without casting a vote, and no power index computed from the formal procedure will register the effect (Definition~\ref{def:political-power:agenda-control}). The evidence for this mechanism comes from studies of low-salience rule making, where business influence over the rules of corporate governance was greatest when issues were technical and public attention was low \citep{culpepper2010}, and from accounts of lobbying as a subsidy that extends the capacity of allied legislators \citep{hall2006}.
   627	
   628	Agenda control fails as a mechanism of capture when the transparency and entry components of contestability are high. Publication of drafts and of the record of who proposed what makes non-decisions visible, and free entry into rule-making competition allows excluded interests to place their proposals on the agenda through other actors. The source framework's redesign proposals include lobbying registers and the disclosure of contacts between rule makers and interested parties for this reason \citep[Section~11]{largo2026hbs}.
   629	
   630	\subsection{Checks}
   631	
   632	The four mechanisms share a structure. In each, rule making drifts toward capture when one component of contestability is weak: oversight in the monitoring game, the identity of veto holders in the veto game, independence of appointees in the appointment channel, and transparency in agenda control. The corresponding checks are organized opposition, vetoes held by actors without a stake in the rule, plural appointment and security of tenure, and publicity. None of these checks removes the rule-making function, and none requires that it be dispersed to the point of the consensus society, whose own status-quo bias Proposition~\ref{prop:political-power:minimal-form} describes. The checks act on contestability, not on the existence of rule makers, which is the rule-making form of the series' central distinction between Proposition A and Proposition B.
   633	
   634	\section{Measurement and hypotheses}
   635	\label{sec:measurement}
   636	
   637	\subsection{Indicators}
   638	
   639	Table~\ref{tab:indicators} lists indicators for the constructs of this paper. Each indicator can be coded from documentary sources, and each has a known weakness. The table follows the source framework's requirement that measurement precede accusation and that the population of coded events include ordinary rule making, not only scandals \citep[Appendix~B]{largo2026hbs}.
   640	
   641	\begin{table}[tbp]
   642	\centering
   643	\small
   644	\caption{Indicators for the constructs of the rule-making layer, with the main weakness of each.}
   645	\label{tab:indicators}
   646	\begin{tabularx}{\textwidth}{@{}L{2.6cm}YY@{}}
   647	\toprule
   648	Construct & Indicator & Main weakness \\
   649	\midrule
   650	De jure control shares & Shapley-Shubik shares computed from the written or customary decision procedure & Ignores agenda setting and informal influence \\
   651	De facto control shares & Shares of contested decisions in which each actor's position prevails, and survival of each actor's provisions through amendment and veto bargaining & Success can reflect anticipation of others' positions rather than control \\
   652	Agenda origin & Shares of enacted rules by originating actor, from legislative records and decree registers & Initiation is a different power from enactment \\
   653	Concentration $H^{\pP}$ & Sum of squared shares from either of the two indicators above & Sensitive to the definition of actors as individuals or groups \\
   654	Replacement $q^{\mathrm{rep}}$ & Frequency of peaceful turnover of rule makers through elections or regular succession & Turnover can occur within a closed coalition \\
   655	Oversight $q^{\mathrm{ovs}}$ & Indices of legislative and judicial constraints on the executive & Formal powers may not be used \\
   656	Entry $q^{\mathrm{ent}}$ & Legal and practical freedom to form parties, stand for office, and petition & Practical barriers are hard to code \\
   657	Transparency $q^{\mathrm{trn}}$ & Publication of drafts, consultation records, and lobbying registers & Disclosure can be formal and incomplete \\
   658	Exit $q^{\mathrm{ext}}$ & Legal and economic cost of leaving the jurisdiction or the group & Exit can substitute for voice and weaken reform \\
   659	Appointment share $\alpha_{S,\ell}$ & Share of weighted posts in pillar $\ell$ that a coalition fills without the consent of another body & Requires a list of posts and weights fixed in advance \\
   660	Veto players & Number of actors whose consent is required to change a statute & Partisan alignment can merge formally separate veto players \\
   661	\bottomrule
   662	\end{tabularx}
   663	\end{table}
   664	
   665	\subsection{Hypotheses with falsifiers}
   666	
   667	Each hypothesis below refines one of three general hypotheses in the source framework \citep[Section~9]{largo2026hbs}: that benefits concentrated among connected actors go with weaker chances of challenge (H1), that groups controlling appointments, funds, and sanctions across several domains keep preferential rules after exposure (H2), and that appointment chains explain allocation in one-party sectors better than private capital does (H3). Each names its parent and the observation that would count against it.
   668	
   669	\begin{description}[font=\normalfont\itshape, leftmargin=1.5em, style=nextline]
   670	\item[HP1, appointment channel.] In party-state regimes, the share of key economic, judicial, media, and security posts filled from party appointment lists predicts the integration of rule making with those pillars. In secular democracies, where appointment to such posts requires confirmation by a second body or is governed by civil-service rules, the same pairwise integrations are lower. Parent: H3. Falsifier: equal integration across regimes with different appointment rules, after controlling for the loyalty of appointees.
   671	\item[HP2, institutionalized power sharing.] Autocracies with functioning ruling parties or legislatures that share rule making have longer-lived leaders \citep{gandhi2007,magaloni2008}. Parent: H2. Falsifier: no difference in leader survival once resource rents are controlled.
   672	\item[HP3, conditional oligarchy.] Leadership turnover in membership organizations is lower where monitoring is costly, and higher where an organized internal opposition exists, as Proposition~\ref{prop:political-power:michels} predicts. Parent: H1. Falsifier: turnover unrelated to measured monitoring costs or to the presence of an organized opposition.
   673	\item[HP4, selectorate.] Smaller winning coalitions relative to the selectorate predict a higher share of private goods in public spending \citep{bdm2003}. Parent: H1. Falsifier: no association, or the reverse association.
   674	\item[HP5, religious-political bargaining.] Where rulers depend on religious legitimation, they grant religious authorities autonomy in law and education in return for support. Rubin and Kuru predict different consequences of this bargain \citep{rubin2017,kuru2019}, and both predictions should be tested. Parent: H2. Falsifier: religious autonomy that does not vary with rulers' dependence on religious legitimation.
   675	\item[HP6, brokered absolutism.] Royal rule making in the Catholic monarchies depended on negotiated intermediaries, so royal legislative success varied with the survival of provincial estates and corporate bodies \citep{beik1985}. Parent: H1. Falsifier: royal legislative success unrelated to the survival of intermediaries.
   676	\item[HP7, veto trade-off.] The number of effective veto players is positively associated with the persistence of preferential rules and negatively associated with responsiveness to changes in majority preference, as Proposition~\ref{prop:political-power:veto} predicts. Parent: H2. Falsifier: no association with the persistence of preferential rules.
   677	\end{description}
   678	
   679	HP1 and HP7 test the propositions of Section~\ref{sec:mechanisms} directly, and HP3 tests the role of organized opposition. HP2 and HP4 import established theories of autocracy into the framework, and their value here lies in coding the same variables across all six regime types. HP5 and HP6 apply to particular historical regime types and require archival coding. Identification is difficult for all seven. Appointment rules, veto structures, and legitimation strategies are chosen by rule makers, so cross-sectional associations confound the effects of these institutions with the reasons they were adopted. The source framework's event-study design, which compares outcomes before and after reforms of oversight in matched jurisdictions, is the appropriate design where such reforms occurred \citep[Section~9]{largo2026hbs}.
   680	
   681	\section{Revelation 13 and the rule-making pillar}
   682	\label{sec:revelation}
   683	
   684	The series reads Revelation typologically: the beast is a recurring pattern of power that claims ultimate loyalty, with the Roman Empire of the first century as its historical anchor \citep{bauckham1993,koester2014}. The reading identifies no present-day government, party, institution, or person with the beast, and it declines the futurist practice of doing so, whose long record of failed identifications is documented in the history of its reception \citep{fuller1995,mcginn1998}. The mapping from the text to the six pillars is an interpretive claim of the series, not a result of exegesis.
   685	
   686	Revelation 13 opens with a beast rising from the sea to whom ``the dragon gave him his power, and his seat, and great authority'' (Rev.\ 13:2, \citealp{kjv}). The rule-making authority of the beast is derived; it comes from a source outside itself and is then exercised over others. In Weber's terms the passage poses the question of legitimacy, the ground on which a claim to rule is accepted \citep{weber1978}. The text then records the response of those ruled: ``Who is like unto the beast? who is able to make war with him?'' (Rev.\ 13:4). The question describes authority that admits no contest. In the vocabulary of this paper it is an image of contestability near zero and concentration near one, the condition under which the pillar's term $H^{\pP}(1-Q^{\pP})$ in unaccountable concentration is at its maximum. The beast's reach extends ``over all kindreds, and tongues, and nations'' (Rev.\ 13:7), so a single authority governs a population whose plurality the necessity theorem takes as its starting point.
   687	
   688	Two features of the text qualify this image. The authority is repeatedly described as given, and given for a limited time: ``power was given unto him to continue forty and two months'' (Rev.\ 13:5). Within the text the beast's rule is bounded by a sovereignty it does not control. The second beast, from the earth, ``exerciseth all the power of the first beast before him'' and causes the inhabitants of the earth to worship the first (Rev.\ 13:12). Read typologically, it represents the legitimation of political authority by a second institution, a coupling of rule making with the ideological pillar that Part IV examines. Kraybill and Friesen locate the historical referent in the imperial cult of the cities of Asia Minor and its ties to commerce and civic life \citep{kraybill1996,friesen2001}, and Collins reads the book as a response to a crisis perceived by its audience \citep{collins1984}.
   689	
   690	Revelation 17 gives the clearest image of the rule-making pillar itself. The ten horns ``are ten kings, which have received no kingdom as yet; but receive power as kings one hour with the beast. These have one mind, and shall give their power and strength unto the beast'' (Rev.\ 17:12 to 13). Ten rulers who could have acted as separate veto players surrender their authority to a single center. In the terms of Proposition~\ref{prop:political-power:concentration}, the image is a move from a dispersed set of rule makers toward the dictatorship case, accomplished by delegation rather than conquest. The text then has the same kings turn on the city they served (Rev.\ 17:16), an image of the instability of coalitions that rest on delegated power. Svolik's account of authoritarian power sharing, in which the ruler's allies are also the most likely source of the ruler's removal, describes the same instability in the vocabulary of political science \citep{svolik2012}. The parallel is an interpretive analogy and makes no claim about the authorial intention of the text.
   691	
   692	Bauckham reads Revelation as a critique of Rome's claim to absolute loyalty, set against the alternative of faithful witness \citep{bauckham1993}. On this reading the object of the critique is not the existence of political authority. Paul's letter to the Romans tells its readers, ``Let every soul be subject unto the higher powers'' (Rom.\ 13:1), and Christian political ethics has long read Romans 13 and Revelation 13 together \citep{yoder1972}. The typological reading adopted here locates the warning of Revelation 13 at the point where rule making becomes unanswerable, not at the existence of rule makers. This is the theological counterpart of the distinction between Proposition A and Proposition B. Every polity has rule makers. The image of the beast applies when the rule makers can no longer be contested.
   693	
   694	\section{Objections and scope conditions}
   695	\label{sec:objections}
   696	
   697	The necessity theorem is not vacuous, because both of its substantive assumptions can fail. A group whose members always agreed would need no procedure for selecting among divergent preferences, and a group in an unchanging environment could persist without changing its rules. The predicate ``implements rule making'' is thin, but Section~\ref{sec:necessity} states what it excludes: decisions and rule changes imposed from outside, and rules that never change through environments that no single rule system could survive. A thin predicate that can fail differs from one that holds by definition.
   698	
   699	The boundary between rule making and interpretation is analytical, and it is drawn by act rather than by institution. Common-law courts make rules, constitutional courts shape legislation, and administrative agencies both make and apply regulations. Definition~\ref{def:political-power:boundary} classifies each such act, and the many-to-many role map of the source framework records an institution that does both in both pillars, with the coupling $C_{\pP\pJ}$ measuring how far one coalition controls the two. Part III applies the same classification of mixed acts from the interpretive side.
   700	
   701	Power indices measure formal power and nothing more. The Shapley-Shubik share assumes that all orderings of members are equally likely and ignores the content of proposals, the identity of agenda setters, and informal influence. The paper therefore uses the index only as a de jure baseline and pairs it with outcome-based indicators of de facto control in Table~\ref{tab:indicators}, recording the origin of proposals separately because initiation and enactment are different powers. A large gap between the two, as in brokered absolutism or patronal regimes, is itself evidence about where rule-making power lies.
   702	
   703	The comparison of regime types from different centuries is valid because it asks the same questions of each, not because the answers are commensurable in every respect. A medieval caliphate and a twenty-first century democracy face different problems with different technologies of rule. The six types are lenses, as Section~\ref{sec:regimes} states, and the comparative claims concern the distribution of a function that the necessity theorem shows all of them must perform.
   704	
   705	The theological reading is separable from the analysis. Nothing in Sections~\ref{sec:layer}, \ref{sec:necessity}, \ref{sec:mechanisms}, and~\ref{sec:measurement} depends on it, and the reading is offered as an interpretation of a text that has shaped the political imagination of many societies, with its interpretive status stated.
   706	
   707	The mechanisms are modeled in their simplest forms. Richer models of oligarchy, veto bargaining, and appointment would move the thresholds and could qualify some conclusions, so the propositions are offered as conditional mechanisms, not as complete theories.
   708	
   709	The sources for some regime types are themselves contested. For the Islamic states and the Catholic monarchies in particular, the paper relies on specialists whose interpretations are debated, and it reports their positions without adjudicating among them.
   710	
   711	\section{Conclusion}
   712	\label{sec:conclusion}
   713	
   714	Every persistent collective whose members disagree about binding choices, and whose environment changes, makes rules. The theorem of Section~\ref{sec:necessity} establishes this from explicit assumptions, and the stateless and consensus societies that seem to refute it display the function in distributed form: talk, oratory without command, collective suppression of would-be dominants, and fission. The same function is performed by parliaments, party committees, kings in council, and assemblies of jurists.
   715	
   716	The existence of the function places no constraint on its concentration. For a group of any size, procedures that satisfy the necessity theorem range from equal shares to dictatorship. Concentration, contestability, and coupling to other pillars therefore have to be measured, and the comparative evidence shows that they vary independently of the source of legitimacy that a regime claims. The conditional mechanisms of Section~\ref{sec:mechanisms} describe how rule making can drift toward capture through diffuse monitoring incentives, protected vetoes, appointment chains, and agenda control. Each mechanism has a check that acts on contestability, and none of the checks removes the need for rule makers.
   717	
   718	What remains uncertain is quantitative: how concentrated and how contestable rule making is in particular polities, and how strongly it is coupled to the other pillars. Answering these questions requires the preregistered coding that the framework specifies. The conclusion that the paper can defend is structural. The question of who makes the laws has always had an answer; whether the answer can be contested is the question on which accountability depends.
   719	
   720	\begin{thebibliography}{200}
   721	\small
   722	\setlength{\itemsep}{0pt}
   723	\bibitem[Aberle et al.(1950)]{aberle1950}
   724	Aberle, D. F., A. K. Cohen, A. K. Davis, M. J. Levy Jr., and F. X. Sutton. 1950. ``The Functional Prerequisites of a Society.'' \emph{Ethics} 60(2): 100-111. doi:10.1086/290705.
   725	
   726	\bibitem[Acemoglu and Robinson(2006)]{acemoglu2006}
   727	Acemoglu, Daron and James A. Robinson. 2006. \emph{Economic Origins of Dictatorship and Democracy}. Cambridge University Press. doi:10.1017/CBO9780511510809.
   728	
   729	\bibitem[Alfoneh(2013)]{alfoneh2013}
   730	Alfoneh, Ali. 2013. \emph{Iran Unveiled: How the Revolutionary Guards Is Transforming Iran from Theocracy into Military Dictatorship}. AEI Press.
   731	
   732	\bibitem[Ansolabehere et al.(2003)]{ansolabehere2003}
   733	Ansolabehere, Stephen, John M. de Figueiredo, and James M. Snyder. 2003. ``Why Is There So Little Money in U.S. Politics?'' \emph{Journal of Economic Perspectives} 17(1): 105-130. doi:10.1257/089533003321164976.
   734	
   735	\bibitem[Arjomand(1988)]{arjomand1988}
   736	Arjomand, Said Amir. 1988. \emph{The Turban for the Crown: The Islamic Revolution in Iran}. Oxford University Press.
   737	
   738	\bibitem[Bachrach and Baratz(1962)]{bachrach1962}
   739	Bachrach, Peter and Morton S. Baratz. 1962. ``Two Faces of Power.'' \emph{American Political Science Review} 56(4): 947-952. doi:10.2307/1952796.
   740	
   741	\bibitem[Barkey(2008)]{barkey2008}
   742	Barkey, Karen. 2008. \emph{Empire of Difference: The Ottomans in Comparative Perspective}. Cambridge University Press. doi:10.1017/cbo9780511790645.
   743	
   744	\bibitem[Bartels(2008)]{bartels2008}
   745	Bartels, Larry M. 2008. \emph{Unequal Democracy: The Political Economy of the New Gilded Age}. Princeton University Press. doi:10.1515/9781400883363.
   746	
   747	\bibitem[Bauckham(1993)]{bauckham1993}
   748	Bauckham, Richard. 1993. \emph{The Theology of the Book of Revelation}. Cambridge University Press. doi:10.1017/cbo9780511819858.
   749	
   750	\bibitem[Baumgartner et al.(2009)]{baumgartner2009}
   751	Baumgartner, Frank R., Jeffrey M. Berry, Marie Hojnacki, David C. Kimball, and Beth L. Leech. 2009. \emph{Lobbying and Policy Change: Who Wins, Who Loses, and Why}. University of Chicago Press. doi:10.7208/chicago/9780226039466.001.0001.
   752	
   753	\bibitem[Beik(1985)]{beik1985}
   754	Beik, William. 1985. \emph{Absolutism and Society in Seventeenth-Century France: State Power and Provincial Aristocracy in Languedoc}. Cambridge University Press. doi:10.1017/cbo9780511583797.
   755	
   756	\bibitem[Berman(2006)]{berman2006}
   757	Berman, Sheri. 2006. \emph{The Primacy of Politics: Social Democracy and the Making of Europe's Twentieth Century}. Cambridge University Press. doi:10.1017/cbo9780511791109.
   758	
   759	\bibitem[Bertrand et al.(2014)]{bertrand2014}
   760	Bertrand, Marianne, Matilde Bombardini, and Francesco Trebbi. 2014. ``Is It Whom You Know or What You Know? An Empirical Assessment of the Lobbying Process.'' \emph{American Economic Review} 104(12): 3885-3920. doi:10.1257/aer.104.12.3885.
   761	
   762	\bibitem[Blanes i Vidal et al.(2012)]{blanes2012}
   763	Blanes i Vidal, Jordi, Mirko Draca, and Christian Fons-Rosen. 2012. ``Revolving Door Lobbyists.'' \emph{American Economic Review} 102(7): 3731-3748. doi:10.1257/aer.102.7.3731.
   764	
   765	\bibitem[Bodin(1992)]{bodin1992}
   766	Bodin, Jean. 1992. \emph{On Sovereignty: Four Chapters from The Six Books of the Commonwealth (1576)}. Cambridge University Press (ed.~Franklin).
   767	
   768	\bibitem[Boehm(1999)]{boehm1999}
   769	Boehm, Christopher. 1999. \emph{Hierarchy in the Forest: The Evolution of Egalitarian Behavior}. Harvard University Press. doi:10.2307/j.ctvjf9xr4.
   770	
   771	\bibitem[Bossuet(1990)]{bossuet1990}
   772	Bossuet, Jacques-B\'enigne. 1990. \emph{Politics Drawn from the Very Words of Holy Scripture (1709)}. Cambridge University Press (ed.~Riley).
   773	
   774	\bibitem[Branham et al.(2017)]{branham2017}
   775	Branham, J. Alexander, Stuart N. Soroka, and Christopher Wlezien. 2017. ``When Do the Rich Win?'' \emph{Political Science Quarterly} 132(1): 43-62. doi:10.1002/polq.12577.
   776	
   777	\bibitem[Brumberg(2001)]{brumberg2001}
   778	Brumberg, Daniel. 2001. \emph{Reinventing Khomeini: The Struggle for Reform in Iran}. University of Chicago Press.
   779	
   780	\bibitem[Buchta(2000)]{buchta2000}
   781	Buchta, Wilfried. 2000. \emph{Who Rules Iran? The Structure of Power in the Islamic Republic}. Washington Institute for Near East Policy and Konrad Adenauer Stiftung.
   782	
   783	\bibitem[Bueno de Mesquita et al.(2003)]{bdm2003}
   784	Bueno de Mesquita, Bruce, Alastair Smith, Randolph M. Siverson, and James D. Morrow. 2003. \emph{The Logic of Political Survival}. MIT Press. doi:10.7551/mitpress/4292.001.0001.
   785	
   786	\bibitem[Cassinelli(1953)]{cassinelli1953}
   787	Cassinelli, C. W. 1953. ``The Law of Oligarchy.'' \emph{American Political Science Review} 47(3): 773-784. doi:10.2307/1952904.
   788	
   789	\bibitem[Clastres(1987)]{clastres1987}
   790	Clastres, Pierre. 1987. \emph{Society against the State: Essays in Political Anthropology (1974)}, trans.~Robert Hurley. Zone Books. doi:10.2307/j.ctv1595m3p.
   791	
   792	\bibitem[Collins(1984)]{collins1984}
   793	Collins, Adela Yarbro. 1984. \emph{Crisis and Catharsis: The Power of the Apocalypse}. Westminster Press.
   794	
   795	\bibitem[Collins(1995)]{collins1995}
   796	Collins, James B. 1995. \emph{The State in Early Modern France}. Cambridge University Press. doi:10.1017/cbo9781139170147.
   797	
   798	\bibitem[Commins(2006)]{commins2006}
   799	Commins, David. 2006. \emph{The Wahhabi Mission and Saudi Arabia}. I. B. Tauris. doi:10.5040/9780755609444.
   800	

exec
/usr/local/bin/zsh -lc "sed -n '140,360p' papers/latex/political-power.tex | nl -ba -v 140" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   140	\subsection{Control shares from decision procedures}
   141	
   142	The source framework defines $s^m_{i,t}$ as a normalized share of decision-relevant control but leaves its measurement open. For rule making a natural baseline is available. A rule-making procedure is, at a minimum, a specification of which coalitions can enact a proposal against the status quo. The baseline below models each decision as such a binary vote. When a decision involves three or more alternatives, an agenda rule determines which proposals are put against the status quo and in what order; that rule is the object of agenda control (Definition~\ref{def:political-power:agenda-control}) and is measured separately. Power indices from cooperative game theory turn the specification of winning coalitions into shares that sum to one.
   143	
   144	\begin{definition}[Simple game and Shapley-Shubik shares]
   145	\label{def:political-power:shares}
   146	A \emph{simple game} on $N$ is a family $\Win$ of winning coalitions with $N\in\Win$, $\emptyset\notin\Win$, and $S\in\Win$, $S\subseteq S'$ implying $S'\in\Win$. The game is \emph{proper} if $S\in\Win$ implies $N\setminus S\notin\Win$, so that two disjoint coalitions cannot both enact incompatible decisions; a rule-making procedure is represented by a proper simple game. An ordering of $N$ is a bijection $\pi:\{1,\dots,n\}\to N$, and $B_\pi(i)=\{\pi(k):k<\pi^{-1}(i)\}$ is the set of members who precede $i$. Member $i$ is \emph{the pivot} in $\pi$ if $B_\pi(i)\notin\Win$ and $B_\pi(i)\cup\{i\}\in\Win$. The Shapley-Shubik share of $i$ is $\varphi_i=|\{\pi: i \text{ is the pivot in } \pi\}|/n!$ \citep{shapley1954}. Member $i$ is a \emph{veto player} if $i\in S$ for every $S\in\Win$, and a \emph{dictator} if $\{i\}\in\Win$ and every winning coalition contains $i$.
   147	\end{definition}
   148	
   149	The de jure baseline sets $s^{\pP}_i=\varphi_i$. Actual control can depart from the baseline when an agenda setter, an informal patron, or a donor shapes which proposals reach a vote, and the gap between de jure and de facto power is itself an object of study \citep{acemoglu2006}. The baseline is still useful, because it ties concentration to the written or customary procedure and so gives a reference point against which informal concentration can be measured.
   150	
   151	\begin{proposition}[Concentration under standard procedures]
   152	\label{prop:political-power:concentration}
   153	Let $\Win$ be a simple game on $N$ with $|N|=n$, and set $s^{\pP}_i=\varphi_i$ and $H^{\pP}=\sum_i\varphi_i^2$.
   154	\begin{enumerate}[label=(\alph*)]
   155	\item In every ordering exactly one member is the pivot, so $\sum_i\varphi_i=1$.
   156	\item $1/n\le H^{\pP}\le 1$, with $H^{\pP}=1/n$ if and only if $\varphi_i=1/n$ for every $i$.
   157	\item If $\Win$ is invariant under every permutation of $N$ (an anonymous procedure such as a quota rule with quota above $n/2$, or unanimity among all members), then $H^{\pP}=1/n$.
   158	\item If $\Win=\{S: K\subseteq S\}$ for a nonempty $K\subseteq N$ with $|K|=k$ (unanimity among the members of $K$), then $H^{\pP}=1/k$. A dictatorship is the case $k=1$.
   159	\item A veto player $i$ satisfies $\varphi_i\ge\varphi_j$ for every $j\in N$.
   160	\end{enumerate}
   161	\end{proposition}
   162	
   163	\begin{proof}
   164	(a) Fix $\pi$ and add members in the order $\pi$. The growing coalition starts at $\emptyset\notin\Win$ and ends at $N\in\Win$. By monotonicity, once the coalition is winning it remains winning, so it changes from losing to winning at exactly one step, and the member added at that step is the unique pivot. Summing over the $n!$ orderings gives $\sum_i\varphi_i=1$.
   165	
   166	(b) By the Cauchy-Schwarz inequality, $1=(\sum_i\varphi_i)^2\le n\sum_i\varphi_i^2$, with equality if and only if all $\varphi_i$ are equal. The upper bound holds because $\varphi_i\in[0,1]$ and $\sum_i\varphi_i=1$ imply $\sum_i\varphi_i^2\le\sum_i\varphi_i=1$.
   167	
   168	(c) If $\sigma$ is a permutation of $N$ and $\Win$ is invariant under $\sigma$, then $B_{\sigma\circ\pi}(\sigma(i))=\sigma(B_\pi(i))$, so $i$ is the pivot in $\pi$ if and only if $\sigma(i)$ is the pivot in $\sigma\circ\pi$. Composition with $\sigma$ is a bijection on orderings, so $\varphi_i=\varphi_{\sigma(i)}$. Every pair of members is exchanged by some permutation, so all shares are equal and (b) gives $H^{\pP}=1/n$.
   169	
   170	(d) A member outside $K$ is never the pivot, because adding a member outside $K$ cannot complete $K$. In any ordering the pivot is the last member of $K$ to appear. By symmetry among the members of $K$, each is last in a fraction $1/k$ of orderings. Hence $\varphi_i=1/k$ for $i\in K$, $\varphi_i=0$ otherwise, and $H^{\pP}=k\cdot(1/k)^2=1/k$.
   171	
   172	(e) Let $j\neq i$ and let $j$ be the pivot in $\pi$. Then $B_\pi(j)\cup\{j\}\in\Win$ contains the veto player $i$, and $i\neq j$, so $i\in B_\pi(j)$. Let $\pi'$ be $\pi$ with the positions of $i$ and $j$ exchanged. In $\pi'$ the set preceding $i$ is $B_\pi(j)\setminus\{i\}\cup\{j\}$, which does not contain $i$ and is therefore losing. Adding $i$ yields $B_\pi(j)\cup\{j\}$, which is winning. So $i$ is the pivot in $\pi'$. The exchange is a bijection on orderings, so the number of orderings in which $j$ is the pivot is at most the number in which $i$ is the pivot.
   173	\end{proof}
   174	
   175	Properness is not needed for the proofs, and every game used below is proper. Part (d) connects concentration to the veto-player tradition: when only the members of $K$ matter and each can block, concentration equals the reciprocal of the number of veto players \citep{tsebelis2002}. Part (c) shows that the anonymous procedures attributed to consensus societies produce the least concentrated rule making possible for their size. The next corollary records that the existence of a rule-making procedure says nothing about its concentration.
   176	
   177	\begin{corollary}[Necessity does not fix concentration]
   178	\label{cor:political-power:any-h}
   179	For every $n\ge2$ and every $k\in\{1,\dots,n\}$ there is a rule-making procedure on $n$ members with $H^{\pP}=1/k$.
   180	\end{corollary}
   181	
   182	\begin{proof}
   183	Take any $K\subseteq N$ with $|K|=k$ and the unanimity game on $K$ from Proposition~\ref{prop:political-power:concentration}(d), with the status quo as the default when no proposal wins and proposals put against the status quo one at a time by a fixed agenda rule. Each vote has a determinate outcome, so the procedure selects a collective decision in every case, and so implements $\pP$ in the sense of Definition~\ref{def:political-power:rule-making}, whatever the value of $k$.
   184	\end{proof}
   185	
   186	The corollary is the rule-making instance of the general non-implication proved in Part VII: the existence of the function (Proposition A) is compatible with any degree of concentration, so concentration (one ingredient of Proposition B) must be established by evidence about the particular polity.
   187	
   188	\subsection{Worked examples}
   189	
   190	The index can be computed for any procedure whose winning coalitions are known. Table~\ref{tab:examples} reports four stylized procedures, the last under two aggregations of actors, with organizations or parties treated as unitary actors. The first two show that the same chamber can produce opposite concentrations depending on the distribution of seats. If one party holds a majority in a chamber that is the only veto player and the party votes as a bloc, the party is a dictator and $H^{\pP}=1$. If three parties hold 40, 35, and 25 percent of the seats under majority rule, any two of them form a majority, the game is anonymous among the three parties, and $H^{\pP}=1/3$ by Proposition~\ref{prop:political-power:concentration}(c). Two chambers and an executive with an absolute veto form a unanimity game on three actors, so $H^{\pP}=1/3$ by part (d).
   191	
   192	The fourth procedure is modeled on the legislative articles of the constitution of the Islamic Republic of Iran \citep{iranconst}. A bill passed by the Majles ($M$) becomes law if the Guardian Council ($G$) approves it, or, if the Council rejects it and the Majles insists, if the Expediency Council ($E$) sides with the Majles. The winning coalitions are therefore $\{M,G\}$, $\{M,E\}$, and $\{M,G,E\}$, and the game is proper. Of the six orderings, $M$ is the pivot in four and $G$ and $E$ in one each, so $\varphi=(2/3,1/6,1/6)$ and $H^{\pP}=1/2$. The constitution also gives the Leader the selection of the six clerical members of the Guardian Council and the appointment of the members of the Expediency Council \citep{iranconst}. If $G$ and $E$ are treated as a single coalition through that appointment channel, the game becomes unanimity between the Majles and the coalition, and $\varphi=(1/2,1/2)$. Concentration is again $1/2$, but the share of the appointed bodies rises from $1/3$ to $1/2$. The example shows that $H^{\pP}$ depends on how actors are aggregated, which is why the actor list must be fixed before coding, and that the appointment channel can shift shares without changing the formal procedure. It omits the Leader's power to set general policy and the Council's screening of candidates for the Majles, both of which raise practical concentration above the de jure figure.
   193	
   194	Values of $H^{\pP}$ are comparable only at a declared level of aggregation. At the \emph{member level} the players are individuals, as in the consensus band of Proposition~\ref{prop:political-power:minimal-form}, where $H^{\pP}=1/n_a$. At the \emph{organ level} the players are chambers, councils, parties voting as blocs, or the electorate in a referendum, as in Table~\ref{tab:examples}. An organ-level figure of $1/3$ and a member-level figure of $1/40$ do not measure the same thing, and the comparisons in this paper are made within a level, never across levels. Where both levels matter, each organ's decision can itself be modeled as a game among its members, so that member-level shares are computed through the organ-level procedure; the paper does not pursue that construction.
   195	
   196	\begin{table}[tbp]
   197	\centering
   198	\small
   199	\caption{De jure Shapley-Shubik shares and concentration for four stylized rule-making procedures. Actors are treated as unitary; the figures illustrate the index and are not estimates for any polity.}
   200	\label{tab:examples}
   201	\begin{tabularx}{\textwidth}{@{}YL{3.6cm}L{1.4cm}@{}}
   202	\toprule
   203	Procedure & Shares & $H^{\pP}$ \\
   204	\midrule
   205	Single-party majority in the only veto chamber & $(1,0,\dots,0)$ & $1$ \\
   206	Three parties with 40, 35, and 25 percent of seats under majority rule & $(1/3,1/3,1/3)$ & $1/3$ \\
   207	Two chambers and an executive with an absolute veto & $(1/3,1/3,1/3)$ & $1/3$ \\
   208	Majles, Guardian Council, and Expediency Council as separate actors & $(2/3,1/6,1/6)$ & $1/2$ \\
   209	Majles and an appointed bloc of the two councils & $(1/2,1/2)$ & $1/2$ \\
   210	\bottomrule
   211	\end{tabularx}
   212	\end{table}
   213	
   214	\subsection{Contestability of rule making}
   215	
   216	The source's contestability index $Q_{m,t}$ is generic. For rule making five components can be distinguished and measured separately.
   217	
   218	\begin{definition}[Components of rule-making contestability]
   219	\label{def:political-power:qp}
   220	For a polity at time $t$, let $q_t=(q^{\mathrm{rep}},q^{\mathrm{ovs}},q^{\mathrm{ent}},q^{\mathrm{trn}},q^{\mathrm{ext}})\in[0,1]^5$ record, in order, the credibility of peaceful replacement of rule makers; the strength of oversight of rule makers by bodies they do not control; the freedom of entry into rule-making competition (forming parties, standing for office, petitioning); the transparency of rule making (publication of drafts, records of who proposed what); and the ease of exit from the jurisdiction or the group, so that cheap exit scores high. The rule-making contestability is $Q^{\pP}_t=g(q_t)$ for a preregistered aggregator $g:[0,1]^5\to[0,1]$ that is nondecreasing in each argument with $g(0,\dots,0)=0$ and $g(1,\dots,1)=1$.
   221	\end{definition}
   222	
   223	The exit component draws on the analysis of exit and voice that Part VI develops for the series \citep{long2026productive}. Two aggregators bracket the reasonable choices. The arithmetic mean treats the components as substitutes, so strong exit can compensate for absent elections. The geometric mean treats them as complements, so that any component at zero sets $Q^{\pP}$ to zero. The choice changes rankings in exactly the cases that interest the comparison. A foraging band has very cheap exit and open entry into discussion but no formal oversight body; a single-party state may publish drafts and permit petitions while ruling out replacement. Under the geometric mean both score low unless oversight in the band is coded to include direct observation of everyone by everyone. This is a concrete form of the measurement-invariance problem that the source framework raises for all its constructs \citep{largo2026hbs}, and it is why the aggregator must be fixed before coding begins.
   224	
   225	\subsection{Appointment channel and agenda control}
   226	
   227	Most coupling between rule making and the other pillars runs through two channels: the power to appoint the people who exercise the other functions, and the power to decide which questions reach a decision at all.
   228	
   229	\begin{definition}[Appointment channel]
   230	\label{def:political-power:appointment-channel}
   231	For a pillar $\ell\in\Mset$ (the letter $n$ is reserved for the size of a collective; see Section~\ref{sec:layer}), let $O_\ell$ be the set of offices that exercise decision-relevant control in $\ell$, with weights $w_o\ge0$ and $\sum_{o\in O_\ell}w_o=1$ equal to each office's control share. For a coalition $S$, the \emph{appointment share} of $S$ in $\ell$ is
   232	\[
   233	\alpha_{S,\ell}=\sum_{o\in O_\ell}w_o\,\mathbf{1}[S \text{ can unilaterally appoint or remove the holder of } o].
   234	\]
   235	The appointment channel from $\pP$ to $\ell$ is the map $S\mapsto\alpha_{S,\ell}$.
   236	\end{definition}
   237	
   238	The appointment channel is the instrument through which, in the source's account, party-state control paths run from central appointment to allocation and enforcement \citep[Proposition~3]{largo2026hbs}. Parts III and V use the same object for judges and for security chiefs. The word ``unilaterally'' matters. Where an appointment requires the consent of a second body, as in legislative confirmation, no single coalition's share includes that office unless it controls both bodies.
   239	
   240	\begin{definition}[Agenda control]
   241	\label{def:political-power:agenda-control}
   242	An actor exercises \emph{agenda control} in $\pP$ to the extent that it determines which proposals are considered by the rule-making procedure. A \emph{non-decision} is a proposal that some members want considered and that is kept from consideration by an actor with agenda control \citep{bachrach1962}.
   243	\end{definition}
   244	
   245	Agenda control is the second face of power in the classification of Bachrach and Baratz, and the third face, the shaping of preferences themselves, belongs to Part IV \citep{lukes2005}. Agenda control is invisible to the Shapley-Shubik baseline, which takes the set of proposals as given. This is one reason why the de jure shares of Definition~\ref{def:political-power:shares} are a lower bound on the concentration of actual rule-making power whenever agenda setting is itself concentrated.
   246	
   247	\subsection{Couplings to the other pillars}
   248	
   249	Under the series' allocation of the fifteen pillar pairs, this paper gives the primary treatment of four: rule making with interpretation ($C_{\pP\pJ}$), with legitimation ($C_{\pP\pI}$), with enforcement ($C_{\pP\pC}$), and with production ($C_{\pP\pW}$). The pair with resource control, $C_{\pF\pP}$, belongs to Part I \citep{long2026financial}. Each pair has a characteristic channel.
   250	
   251	Whoever appoints and removes judges couples rule making to interpretation, and so does the traffic between statute and precedent. Statutes give courts rules to apply, and judicial applications generate precedents and doctrines that legislatures then codify, override, or leave in place. A coalition that appoints judges without confirmation by another body and can remove them at will drives $\alpha_{S,\pJ}$ toward one.
   252	
   253	Legitimation enters rule making through the rule of recognition, which Part IV defines \citep[Definition~2.2]{long2026ideological}: rules count as law because officials and subjects accept criteria that identify them as law \citep{hart1961}. Rule makers seek legitimation through religious, ideological, and electoral claims, and they can also shape the information environment directly. Recent work argues that many contemporary autocrats rely more on the manipulation of information than on mass repression to sustain their hold on rule making \citep{guriev2019}.
   254	
   255	Civilian control of the coercive apparatus, the appointment of its commanders, and the rules that govern its use tie rule making to enforcement. Weber defined the state by its successful claim to a monopoly of legitimate force within a territory \citep{weber1946}, and the claim is made in rules. Part V analyzes the apparatus, including the coup-proofing strategies by which rulers divide it \citep[Proposition~6.3]{long2026coercive}. This paper treats the appointment of security chiefs as part of the appointment channel and leaves coup-proofing and the conduct of policing to Part V.
   256	
   257	The rules of work, taxation, and property, and the producers' organizations that help to make them, connect rule making to production. Labor law, tax codes, and the legal status of unions are outputs of $\pP$ that set the terms on which the productive population works. In corporatist systems, organized labor and employers take part in drafting the rules that govern them, which raises $C_{\pP\pW}$ by design and with the consent of the organized parties.
   258	
   259	\section{Necessity of the rule-making function}
   260	\label{sec:necessity}
   261	
   262	\subsection{Assumptions of the lemma}
   263	
   264	The working axiom for this pillar in the series is plurality: members' preferences diverge, yet collective choices are made. Part VII refines the full axiom set and proves the general theorem. Here the axiom is stated in the form needed for the rule-making lemma, together with two further assumptions that make its content explicit.
   265	
   266	\begin{assumption}[Plurality]
   267	\label{ass:political-power:plurality}
   268	The collective repeatedly faces collective decisions in the sense of Definition~\ref{def:political-power:rule-system}, and for each such decision the members' preferences diverge over the alternatives: for every alternative $x\in X$ some member strictly prefers another alternative $y\in X$ to $x$.
   269	\end{assumption}
   270	
   271	\begin{assumption}[Environmental change]
   272	\label{ass:political-power:change}
   273	The environment $e_t\in E$ of the collective varies over time. There is a viability correspondence $\mathcal{V}:E\to 2^{\Rules}$, where $\mathcal{V}(e)$ is the set of rule systems under which the collective survives a period in environment $e$, and the realized path contains periods $s_0<s_1<\dots<s_r$, with $r\ge1$, such that consecutive viability sets are disjoint: $\mathcal{V}(e_{s_{j-1}})\cap\mathcal{V}(e_{s_j})=\emptyset$ for $j=1,\dots,r$.
   274	\end{assumption}
   275	
   276	\begin{assumption}[Self-government and persistence]
   277	\label{ass:political-power:persistence}
   278	(i) The collective's decisions and changes in its rules are produced by practices of its members rather than imposed from outside. (ii) The collective persists over a window $T$ of consecutive periods that contains $s_0$ and $s_r$, so $R_t\in\mathcal{V}(e_t)$ for all $t\in T$.
   279	\end{assumption}
   280	
   281	The plurality assumption is empirical. It fails for a group whose members always agree on every collective choice, which no ethnography or history records for any group of more than a few people over any length of time. The change assumption formalizes the condition under which a regime of fixed rules becomes untenable. Hart called a regime of primary rules without a rule of change \emph{static} and listed this as one of its three defects \citep{hart1961}; the assumption states when the defect becomes fatal rather than merely costly. The self-government clause excludes a group whose rules are set entirely by an outside power. Such a group does not falsify the necessity of rule making; it shows that the rule maker lies outside the boundary drawn around the group, and the boundary should be redrawn to include it.
   282	
   283	\begin{lemma}[Collective choice requires a procedure]
   284	\label{lem:political-power:choice}
   285	Under Assumption~\ref{ass:political-power:plurality} and clause (i) of Assumption~\ref{ass:political-power:persistence}, every realized collective decision is ranked below some other alternative by at least one member. The practice that produces the realized decision therefore selects among divergent preferences, and the collective implements part (a) of Definition~\ref{def:political-power:rule-making}.
   286	\end{lemma}
   287	
   288	\begin{proof}
   289	Let $x^\ast$ be the alternative realized in a collective decision. By Assumption~\ref{ass:political-power:plurality} there is a member $i$ and an alternative $y$ with $y\succ_i x^\ast$. Because the decision applies to all members at once, $i$ cannot obtain $y$ while others obtain $x^\ast$. Some practice, whether a vote, a command, a discussion that ends when objectors fall silent, or a default to the status quo, determined that $x^\ast$ rather than $y$ would hold for everyone, and by clause (i) of Assumption~\ref{ass:political-power:persistence} that practice is the members' own. That practice selects among divergent preferences. Collective decisions recur by assumption, so such selections recur.
   290	\end{proof}
   291	
   292	\begin{lemma}[Change requires a rule of change]
   293	\label{lem:political-power:change}
   294	Under Assumptions~\ref{ass:political-power:change} and~\ref{ass:political-power:persistence}, the rule system is replaced at least $r$ times on $T$: for each $j=1,\dots,r$ there is $t$ with $s_{j-1}\le t<s_j$ and $R_{t+1}\neq R_t$. Each replacement is produced by a practice of the members.
   295	\end{lemma}
   296	
   297	\begin{proof}
   298	Fix $j$ and suppose $R_t=R_{t+1}$ for every $t$ with $s_{j-1}\le t<s_j$. Then $R_{s_{j-1}}=R_{s_j}=R$. Clause (ii) of Assumption~\ref{ass:political-power:persistence} gives $R\in\mathcal{V}(e_{s_{j-1}})$ and $R\in\mathcal{V}(e_{s_j})$, which contradicts the disjointness in Assumption~\ref{ass:political-power:change}. So some $t$ in $[s_{j-1},s_j)$ has $R_{t+1}\neq R_t$, and both $t$ and $t+1$ lie in $T$ because $T$ consists of consecutive periods containing $s_0$ and $s_r$. The intervals $[s_{j-1},s_j)$ are disjoint, so the $r$ replacements are distinct. By clause (i) of Assumption~\ref{ass:political-power:persistence} each is produced by the members' practices.
   299	\end{proof}
   300	
   301	Hart's term for the practice whose existence Lemma~\ref{lem:political-power:change} establishes is the rule of change. The series assigns this member of Hart's triad of secondary rules to the rule-making pillar; the rule of adjudication belongs to Part III and the rule of recognition to Part IV (Definition~2.2 of that Part).
   302	
   303	\begin{definition}[Rule of change]
   304	\label{def:political-power:rule-of-change}
   305	A \emph{rule of change} of a collective is a secondary rule, written or customary, that identifies who may introduce, alter, or repeal the collective's general rules and by what procedure \citep{hart1961}. It is the rule-making procedure of Definition~\ref{def:political-power:rule-making}(b) considered as a rule accepted by the members rather than as a regularity observed from outside.
   306	\end{definition}
   307	
   308	\begin{theorem}[Necessity of rule making]
   309	\label{thm:political-power:necessity}
   310	A collective that satisfies Assumption~\ref{ass:political-power:plurality} and clause (i) of Assumption~\ref{ass:political-power:persistence} implements the rule-making function in sense (a). If it also satisfies Assumptions~\ref{ass:political-power:change} and~\ref{ass:political-power:persistence}, it implements the function in sense (b), with at least $r$ replacements of the rule system on $T$. Whenever a replacement is chosen from the viable set $\mathcal{V}(e_{t+1})$ and members' preferences diverge over that set in the sense of Definition~\ref{def:political-power:rule-system}, the replacement is itself a selection among divergent preferences.
   311	\end{theorem}
   312	
   313	\begin{proof}
   314	The first statement is Lemma~\ref{lem:political-power:choice}. The second is Lemma~\ref{lem:political-power:change}. For the third, apply Lemma~\ref{lem:political-power:choice} to the choice of $R_{t+1}$ from $\mathcal{V}(e_{t+1})$, treating the choice of a rule system as a collective decision.
   315	\end{proof}
   316	
   317	The proofs are short because the work is done by the assumptions. This is the correct place for the work to be done. The theorem asserts that an activity must occur, not that an institution must exist. It would be false if a persistent collective could make its binding choices without any practice that selects among divergent preferences, or if it could survive incompatible environments without changing its rules. Each of these is an empirical possibility that the hard cases below test.
   318	
   319	\subsection{Scope of the lemma}
   320	
   321	The theorem makes $\pP$ a thin predicate, and a thin predicate invites the charge of vacuity. If anything that happens counts as rule making, the necessity claim is empty. Three things are excluded.
   322	
   323	A collective decision made by a fixed external rule (a lottery imposed by an outside authority, or a decision by the environment itself, such as a drought that forces a move) is excluded by the self-government clause. A rule change that is purely exogenous, such as the imposition of colonial law on a subject people, is excluded for the same reason and relocates the rule maker rather than eliminating it. Most importantly, the predicate excludes a group whose rules never change while the environment does. The falsifier of the theorem is therefore specific: a long-lived group, satisfying the plurality assumption, whose rules never changed and could not be changed by any of its members, through a sequence of environments that no single rule system could survive.
   324	
   325	The theorem says nothing about how rule making is distributed, how it is legitimated, or whether it is accountable. Corollary~\ref{cor:political-power:any-h} shows that the same function can be performed with concentration anywhere from $1/n$ to $1$.
   326	
   327	\subsection{Minimal form in stateless and consensus societies}
   328	
   329	The societies most often cited as lacking government are the test set for the theorem. If rule making is necessary, each should show it in some informal, distributed form. If any shows no rule-making activity at all, the theorem is in trouble.
   330	
   331	Among the Ju/'hoansi of the Kalahari, camp-level decisions about movement, sharing, and conflict are reached through extended public talk in which adults participate and no one has authority to command \citep{lee2013}. Wiessner's analysis of recorded conversations shows that much of this talk consists of criticism and joking directed at people who violate norms of sharing and modesty \citep{wiessner2005}. When disagreement cannot be resolved, people move to another camp. Fission is a rule-change practice of a particular kind: it does not change the rules of the existing group but creates a new group whose rules differ.
   332	
   333	Evans-Pritchard described the Nuer as an ``ordered anarchy'' with no government in the sense of a political authority able to command \citep{evanspritchard1940}. Their political order rested on the balanced opposition of lineage segments. Rules about bridewealth, compensation, and the use of grazing were maintained and adjusted through negotiation among kin groups, through the settlements of disputes, and through the influence of persons whose standing rested on persuasion rather than command. The leopard-skin chief who mediated in cases of homicide belongs to the interpretive pillar and is treated in Part III.
   334	
   335	Clastres argued from Amazonian ethnography that the chief in many lowland South American societies had no power to command, that his speech was an obligation rather than an instrument of rule, and that a chief who tried to give orders would be abandoned \citep{clastres1987}. Clastres's thesis is that such societies actively prevent political power from separating from the group. The thesis is consistent with the necessity theorem. Decisions are still made, by the group, and the chief's oratory is part of how they are made.
   336	
   337	Boehm's survey of foraging societies found a reverse dominance hierarchy: the adult members, acting as a coalition, suppress any individual who tries to dominate, using ridicule, disobedience, ostracism, and in extreme cases killing \citep{boehm1999}. Boehm emphasizes that egalitarianism of this kind is a political achievement. The group decides collectively and enforces the decision against would-be leaders. Woodburn reached a compatible conclusion for immediate-return societies such as the Hadza: their equality is produced by institutions of leveling that prevent the accumulation of power and property \citep{woodburn1982}.
   338	
   339	Ostrom's study of long-lived common-pool resource institutions supplies a different kind of case: small communities that govern a shared resource without a state and without private property \citep{ostrom1990}. Among the design principles she identified is that most individuals affected by the operational rules can participate in modifying them. The principle is a rule-making arrangement in the exact sense of Definition~\ref{def:political-power:rule-making}(b). Reviews of later case studies have found broad support for the principles \citep{cox2010}, and Ostrom's later work describes how such arrangements nest within larger polycentric systems \citep{ostromdesign2010}.
   340	
   341	\begin{proposition}[Minimal form of rule making]
   342	\label{prop:political-power:minimal-form}
   343	Let $N_a\subseteq N$ be the adult members of a group, $|N_a|=n_a\ge2$, and let the group make collective decisions by consensus, modeled as unanimity among the adults (a proposal wins exactly when every member of $N_a$ assents), with the status quo $q$ as default. Let each adult $i$ have a strict linear order $\succ_i$ over alternatives and assent to a proposal $x$ against $q$ if and only if $x\succ_i q$. Then:
   344	\begin{enumerate}[label=(\alph*)]
   345	\item the de jure concentration of rule making is $H^{\pP}=1/n_a$, the minimum possible for a procedure in which only adults' consent counts, and the minimum for the whole group when $N_a=N$;
   346	\item the set of alternatives that can replace $q$ is the set of strict Pareto improvements for the adults, $\{x: x\succ_i q \text{ for all } i\in N_a\}$, which is empty whenever $q$ is Pareto optimal among them;
   347	\item let the group be able to split, with each subgroup $N_1\subseteq N_a$ of at least two adults deciding by consensus for itself. A subgroup can replace $q$ if and only if all its members strictly prefer a common alternative $x$ to $q$, so some subgroup can do so if and only if at least two adults strictly prefer a common alternative to $q$. This condition can hold when $q$ is Pareto optimal among all adults.
   348	\end{enumerate}
   349	\end{proposition}
   350	
   351	\begin{proof}
   352	(a) The procedure is the unanimity game on $K=N_a$, so Proposition~\ref{prop:political-power:concentration}(d) gives $\varphi_i=1/n_a$ for adults, $\varphi_i=0$ for others, and $H^{\pP}=1/n_a$. Any procedure in which only adults can be the pivot has shares summing to one over $N_a$, so Proposition~\ref{prop:political-power:concentration}(b) applied to $N_a$ shows that $1/n_a$ is the minimum. (b) Under unanimity an alternative replaces $q$ only if every adult prefers it to $q$, which is the definition of a strict Pareto improvement among the adults. If $q$ is Pareto optimal among them, no alternative is strictly preferred to $q$ by every adult, so the set is empty. (c) Apply (b) to $N_1$: its consensus winset is $\{x: x\succ_i q\text{ for all }i\in N_1\}$, which is nonempty exactly when its members share an alternative they all prefer to $q$. If two adults $i,j$ both prefer some $x$ to $q$, the subgroup $\{i,j\}$ qualifies; conversely any qualifying subgroup contains two such adults. For the last claim, take three adults with $x\succ_1 q$, $x\succ_2 q$, and $q\succ_3 y$ for every $y\neq q$: then $q$ is Pareto optimal among all three, yet $\{1,2\}$ can adopt $x$.
   353	\end{proof}
   354	
   355	The proposition gives a formal reason for an ethnographic regularity. Consensus produces the least concentrated rule making possible, and it also produces the most status-quo-biased rule making possible, because every adult is a veto player. A consensus society facing a changing environment therefore needs another way to change its rules when no change is a Pareto improvement. Fission supplies it. The pairing of consensus decision making with cheap exit, documented among the Ju/'hoansi and in Woodburn's immediate-return societies, is what Proposition~\ref{prop:political-power:minimal-form} predicts. In the vocabulary of Definition~\ref{def:political-power:qp}, such groups combine minimal concentration with very high exit and entry components of contestability.
   356	
   357	Formal consensus sets only a lower bound on the concentration of rule making in these societies. Even where every adult can block a decision, differences in age, gender, skill, and kinship give some speakers more weight in discussion than others, so actual concentration exceeds the de jure figure $1/n_a$. The equal-share coding describes the procedure, not the distribution of influence within it.
   358	
   359	Across the ethnographic and historical record, collective decisions are made and rules change, while the concentration of rule making varies. Graeber and Wengrow argue that prehistoric societies moved deliberately between egalitarian and hierarchical arrangements, sometimes by season \citep{graeber2021}. Scott describes upland peoples of Southeast Asia who kept rule making dispersed to avoid incorporation by lowland states \citep{scott2009}, and early states in which it became concentrated \citep{scott2017}. Both readings are disputed, and the record itself overrepresents groups observed in the nineteenth and twentieth centuries, many in marginal environments and in contact with states, among foragers who vary widely \citep{kelly1995}. None of these qualifications touches the pattern that matters here: what varies is who makes the rules, not whether they are made.
   360	

exec
/usr/local/bin/zsh -lc "sed -n '361,580p' papers/latex/political-power.tex | nl -ba -v 361" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   361	\subsection{Custom without legislators}
   362	
   363	The strongest objection to the theorem is not a stateless society but an argument about how rules come into being. Hayek distinguished law that grows out of practice, discovered and articulated rather than made, from legislation deliberately enacted by an authority, and he argued that much of the order of a society rests on the former \citep{hayek1973}. Ellickson's study of cattle ranchers in Shasta County, California, showed that neighbors settled trespass disputes by informal norms that diverged from the formal law and that the norms adjusted over time without recourse to it \citep{ellickson1991}. If rules can evolve without anyone making them, the rule-making function may be unnecessary.
   364	
   365	The objection narrows the theorem but does not defeat it. The theorem requires a practice that selects collective decisions and replaces rules, not a legislator. Evolved custom changes through practices: some members deviate, others imitate or sanction the deviation, and social pressure settles on a new regularity. Ellickson's ranchers are rule makers in this distributed sense. The norms change because particular neighbors propose, test, and enforce new expectations through gossip, reciprocity, and occasional self-help. The function is performed; the office is absent.
   366	
   367	The objection still shows something important. Under customary rule change, the rule-making profile of Definition~\ref{def:political-power:rule-making} is diffuse and difficult to observe, and control shares cannot be read from a written procedure. The power-index baseline does not apply, and concentration must be estimated from who in fact initiates and enforces changes. This is a measurement limitation of the paper's framework, not a counterexample to the theorem.
   368	
   369	\subsection{Functional explanation and its limits}
   370	
   371	The theorem is a statement about the conditions under which a collective persists. It is not a functional explanation of why any particular rule-making institution exists. Hempel showed that an inference from the need for a function to the presence of a particular institution commits the fallacy of affirming the consequent, because functional equivalents can meet the same need \citep{hempel1959}. Elster argued that explaining an institution by its beneficial consequences requires a feedback mechanism through which the consequences maintain the institution \citep{elster1983}. The theorem respects both constraints. It claims the necessity of an activity, it allows any institution or none to perform it, and it does not explain the existence of the Parlement of Paris, the Politburo, or the Majles by their contribution to the persistence of their polities. Those institutions have histories, and the comparative section treats them as historical products whose relation to the function is a matter of evidence.
   372	
   373	\section{Literature on rule-making power}
   374	\label{sec:literature}
   375	
   376	\subsection{Elite, pluralist and structural theories}
   377	
   378	The oldest question about rule making is whether a minority always makes the rules. Mosca held that in every society an organized minority rules an unorganized majority, and that the minority's advantage lies in its organization rather than in its numbers \citep{mosca1939}. Michels drew the same conclusion from the internal life of the German Social Democratic Party: organization requires delegation, delegation creates leaders with expertise and control of communication, and leaders entrench themselves even in organizations committed to democracy \citep{michels1915}. Mills extended the elite argument to the postwar United States, describing an interlocking set of corporate, military, and political leaders \citep{mills1956}.
   379	
   380	Pluralists denied that the elite claim had been demonstrated. Dahl's study of New Haven found that different actors prevailed in different issue areas and that no single group controlled decisions across them \citep{dahl1961}. His later account of polyarchy defined democracy by two dimensions, the inclusiveness of participation and the extent of public contestation \citep{dahl1971}. These two dimensions anticipate the separation in this paper between the distribution of rule-making shares and the contestability of rule making.
   381	
   382	A third position holds that rule makers need not be controlled by a class to serve it. Lindblom argued that business occupies a privileged position in market societies because governments depend on business investment for economic performance, so that rule makers anticipate business reactions without being directed \citep{lindblom1977}. Winters defined oligarchy as the political use of concentrated wealth for wealth defense and showed that oligarchs can coexist with electoral democracy \citep{winters2011}. Structural arguments of this kind imply that integration between resource control and rule making, $C_{\pF\pP}$, can be high even when no capture link in the source's sense can be documented. They therefore pose a measurement problem for the framework that Part I examines in detail.
   383	
   384	The empirical debate has moved to policy responsiveness. Gilens and Page estimated, on a dataset of 1,779 policy questions, that the preferences of economic elites and organized business groups have substantial independent associations with policy outcomes in the United States while the preferences of average citizens have little \citep{gilens2014}. Bartels found that senators' votes were more responsive to affluent constituents than to poor ones \citep{bartels2008}. Branham, Soroka, and Wlezien found that the preferences of the affluent and the middle class usually coincide and that, when they diverge, the affluent prevail only modestly more often \citep{branham2017}. Elkjaer and Klitgaard review the comparative evidence on unequal responsiveness and its methods \citep{elkjaer2024}. The disagreement concerns the size and the generality of a bias, not its direction in the American case.
   385	
   386	\subsection{Faces of power and agenda control}
   387	
   388	Bachrach and Baratz argued that the pluralist method of studying observable decisions misses the power exercised by keeping issues off the agenda \citep{bachrach1962}. Lukes added a third dimension, the shaping of preferences so that conflicts of interest never surface as grievances \citep{lukes2005}. For rule making the second face is central and measurable in principle: a non-decision leaves traces in proposals that were drafted and never scheduled, in petitions that went unanswered, and in committee chairs who declined to act. The third face shades into the legitimation pillar and is left to Part IV.
   389	
   390	Culpepper's study of corporate control in Europe and Japan gives the agenda argument an empirical form. Business influence over the rules of corporate governance was greatest on issues of low public salience, where legislators relied on managers' expertise and the press paid little attention \citep{culpepper2010}. Hall and Deardorff model lobbying as a subsidy of information and labor given to legislators who already agree with the lobbyist \citep{hall2006}. On this view, organized interests shape rules mainly by shaping what allied legislators can do with limited time, not by changing their votes.
   391	
   392	\subsection{Rule making in autocracies}
   393	
   394	Theories of autocracy explain the survival of rulers by how they share rule-making power with a narrow group of insiders. In selectorate theory, leaders must retain a winning coalition drawn from a larger selectorate, and when that coalition is small they survive by supplying private goods to its members rather than public goods to all \citep{bdm2003}. Svolik locates the main threat to dictators among the elites who share power with them and shows how parties, legislatures, and rules of succession make that sharing credible \citep{svolik2012}. Gandhi and Przeworski and Magaloni reach compatible conclusions: nominally democratic institutions and ruling parties co-opt potential rivals and are associated with longer rule \citep{gandhi2007,magaloni2008}. Gerschewski adds legitimation and repression to co-optation as the supports of autocratic stability \citep{gerschewski2013}, which in the series' vocabulary brings the legitimation and enforcement pillars to the aid of rule makers. The regime classification of Geddes, Wright, and Frantz makes these claims testable across party, personalist, military, and monarchic autocracies \citep{geddes2014}.
   395	
   396	Hale describes post-Soviet politics as patronal: power runs through networks of personal reward and punishment, organized either as a single pyramid around one patron or as competing pyramids \citep{hale2014}. Levitsky and Way identify competitive authoritarian regimes in which elections are real but the field is uneven \citep{levitsky2010}. These categories matter for measurement because they describe regimes whose formal rule-making procedures are pluralistic and whose actual concentration is high.
   397	
   398	\subsection{Separation of powers and veto players}
   399	
   400	Montesquieu argued that liberty requires that the power to make law, the power to execute it, and the power to judge not be united in the same hands \citep{montesquieu1989}. Madison's defense of the proposed American constitution relied on the same idea in a different form: ``Ambition must be made to counteract ambition'' \citep{madison1788}. The constitutional design he defended gave each branch the means and the motive to resist encroachment by the others.
   401	
   402	Tsebelis generalized the idea. A veto player is an individual or collective actor whose agreement is required for a change of the status quo, and the set of policies that can replace the status quo shrinks as veto players are added or as their positions diverge \citep{tsebelis2002}. Lijphart contrasts majoritarian democracies, which concentrate rule making in the cabinet of a single-party majority, with consensus democracies that disperse it among coalition partners, two legislative chambers, federal units, and courts \citep{lijphart1999}. Linz argued that presidential systems, which give the executive and the legislature separate mandates, make conflicts between them harder to resolve \citep{linz1990}. Weingast showed that constitutional limits on rule makers are self-enforcing only when citizens can coordinate their reactions to transgressions \citep{weingast1997}.
   403	
   404	\subsection{Sources of rule-making authority}
   405	
   406	Weber classified legitimate domination as traditional, charismatic, or rational-legal according to the grounds on which subjects accept commands \citep{weber1978}. Each regime type in the comparison below claims rule-making authority on a different ground: divine right and dynastic tradition in the Catholic monarchies \citep{figgis1914,kantorowicz1957}, divine law administered by rulers and jurists in the Islamic states \citep{crone2004,lambton1981}, the historical mission of a vanguard party in the communist states \citep{kornai1992}, and popular sovereignty expressed in elections in the democracies \citep{dahl1971}. Bodin made the power to give law to all without the consent of others the first mark of sovereignty \citep{bodin1992}. Al-Mawardi set out the conditions under which an imam is validly appointed and the powers he may delegate to viziers, governors, and judges \citep{mawardi1996}. These are theories written from inside regimes, and they describe what rule makers claimed, not necessarily what they could do.
   407	
   408	\subsection{Relation to prior work}
   409	
   410	Three gaps in this literature motivate the present paper. The theories of democratic and autocratic rule making use different concepts, so comparisons across regime types tend to be either impressionistic or confined to a single dimension such as regime survival. The functional-prerequisite tradition in sociology asserted that every society must make collective decisions \citep{aberle1950,parsons1951} but did not separate the necessity of the function from the distribution of its control, and it was criticized for that reason. The source framework of the series \citep{largo2026hbs} supplies a common network vocabulary but merges rule making with adjudication and leaves the measurement of control shares open. This paper separates rule making from adjudication, gives control shares a de jure baseline in power indices, proves that necessity and concentration are logically independent for this pillar, and uses one set of questions for all six regime types.
   411	
   412	\section{Rule making across six regime types}
   413	\label{sec:regimes}
   414	
   415	\subsection{Comparative method}
   416	
   417	Each regime type is examined for the same five features: the institutions that hold the rule-making function, the concentration of control in the sense of $H^{\pP}$ and its contestability in the components of Definition~\ref{def:political-power:qp}, the strength of its coupling to the other five pillars, the arrangements that preserve accountability, and the documented capture episodes and effective checks. The answers are qualitative. Terms such as ``high'' or ``low'' concentration refer to the ordering implied by Proposition~\ref{prop:political-power:concentration} applied to the described procedure, adjusted for documented informal concentration, and they are not estimates of $H^{\pP}$ for any polity.
   418	
   419	The six types are analytical lenses, not mutually exclusive categories. A single country can be a market-capitalist society and a secular democracy at once, and the two lenses ask different questions of it. The market-capitalist lens examines how private economic resources reach rule making. The secular-democratic lens examines how rule making is distributed among elected officials, courts, independent bodies, and private institutions under a constitution. Islamic states and Catholic monarchies are treated as polities in which religious law or religious institutions supplied a source of political legitimacy, in particular historical states with large internal differences. Neither religion is treated as an essence, and no regime type is ranked above another.
   420	
   421	\subsection{Market-capitalist societies}
   422	
   423	In market-capitalist societies with electoral institutions, general rules are made by elected legislatures, by executives through decrees and regulations, and by administrative agencies under delegated authority. The United States, the most studied case, divides rule making among two legislative chambers, a president with a veto, federal agencies that issue regulations, and fifty states. The formal procedure has several veto players, so the de jure concentration of rule making is moderate, and its formal contestability is high on all five components of Definition~\ref{def:political-power:qp}.
   424	
   425	The question this lens asks is how private economic resources enter that procedure. The source framework describes a path from unequal private resources through advocacy and access to the specialized development of policy and the distribution of legal benefits \citep[Section~8]{largo2026hbs}. Several links in that path are documented. A randomized field experiment found that when a political organization revealed that attendees at requested meetings were campaign donors, congressional offices were more likely to arrange meetings with senior staff or the member \citep{kalla2016}. Lobbyists who had worked for a senator saw their lobbying revenue fall when that senator left office, which indicates that part of what they sold was access to a particular rule maker \citep{blanes2012}. Lobbyists also follow the legislators to whom they are connected when those legislators change committee assignments \citep{bertrand2014}. These findings concern access. They show privileged access, the first condition of a capture link, but they do not by themselves show that the access changed a rule.
   426	
   427	Evidence that access changes rules is weaker than the evidence of access itself, and it is contested. Gilens and Page's estimates \citep{gilens2014} are disputed by work that finds the preferences of affluent and middle-income citizens usually coincide \citep{branham2017}. A large study of lobbying on ninety-eight issues found that the status quo usually prevailed and that the resources of a side were a poor predictor of its success \citep{baumgartner2009}. Ansolabehere, de Figueiredo, and Snyder observed that campaign contributions are small relative to the value of the policies at stake, which is hard to reconcile with a market in which rules are bought \citep{ansolabehere2003}. The theory of economic regulation predicted that concentrated interests would capture the rules that govern them \citep{stigler1971}, and Peltzman generalized it to a regulator who balances the support of several groups \citep{peltzman1976}; Part I develops the capture literature \citep{long2026financial}.
   428	
   429	Rule making in this regime type is coupled most strongly to resource control. The coupling runs through the wealth-to-rules path described above and through the structural dependence of rule makers on investment that Lindblom described \citep{lindblom1977}. Hacker and Pierson argue that organized interests used this path to shift tax and regulatory rules toward the very wealthy over several decades \citep{hackerpierson2010}, and Culpepper's comparison of Europe and Japan shows that business influence is greatest when issues are technical and receive little public attention \citep{culpepper2010}. Coupling to interpretation is weaker by design: federal judges are appointed by the president with Senate confirmation, so no single coalition controls the appointment channel unless it holds both bodies.
   430	
   431	Elections, opposition rights, judicial review, disclosure rules, and competition among organized interests, which frequently lobby on opposite sides of the same question \citep{baumgartner2009}, keep this rule making contestable. The regime type thus combines moderate de jure concentration and high formal contestability with unequal practical access, and the open question is how much that access changes rules.
   432	
   433	\subsection{Communist party-states}
   434	
   435	In communist party-states, the ruling party makes the rules that matter and the state legislature ratifies them. In the Soviet Union the Politburo of the Central Committee decided major questions, the Central Committee apparatus prepared and supervised policy, party congresses ratified the line, and the Supreme Soviet enacted laws whose content had been determined elsewhere \citep{fainsod1953,hough1979}. Kornai treats the undivided power of the communist party as the defining feature of the classical socialist system, from which its economic institutions follow \citep{kornai1992}. The de jure concentration of rule making is high, and every component of contestability except transparency of some rule texts is low for actors outside the party.
   436	
   437	The appointment channel is the defining instrument. Party committees at each level held lists of posts, the nomenklatura, whose holders they appointed or approved, covering the leadership of ministries, enterprises, courts, newspapers, universities, and the armed forces \citep{hough1979}. In the notation of Definition~\ref{def:political-power:appointment-channel}, the party's appointment share $\alpha_{S,\ell}$ approached one in every pillar. Voslensky, a former Soviet official writing in emigration, described the nomenklatura as a ruling class \citep{voslensky1984}, and Djilas, a Yugoslav dissident, called the party bureaucracy a new class that held collective ownership through political control \citep{djilas1957}. Both accounts come from authors with strong political commitments and should be read alongside the institutional scholarship. Hough and Fainsod described a system of bureaucratic bargaining among ministries and regions, and Lane and Ross found significant divisions within the Soviet ruling elite of 1981 to 1991 \citep{lane1995}. These findings bear on the loyalty of appointees, a parameter formalized in Section~\ref{sec:mechanisms} (Proposition~\ref{prop:political-power:appointment-bound}): appointment by a single party does not guarantee that appointees act as one coalition.
   438	
   439	The People's Republic of China retains the Leninist structure with important changes. Shirk described the relation between the party's top leaders and the Central Committee as reciprocal accountability: leaders appoint the members of the committee that formally selects them \citep{shirk1993}. Landry showed how the party's control of the appointment and evaluation of local cadres allowed it to decentralize economic decisions without losing political control \citep{landry2008}. Minzner documented a turn after the early 2000s away from legal professionalization and toward mediation and political direction of the courts \citep{minzner2011}, which raises the coupling $C_{\pP\pJ}$.
   440	
   441	Coupling to the other pillars is high by design in all four pairs treated here: party direction of courts, of propaganda and education, of the security services, and of official trade unions organized under party leadership \citep{kornai1992}. Accountability operates mainly within the party, through collective leadership, factional bargaining, and rules of succession, which Svolik identifies as the institutions that make power sharing among elites credible \citep{svolik2012}. The documented checks are intra-elite. In 1964 the Soviet party leadership removed Khrushchev as first secretary through the Presidium and the Central Committee, a replacement of the top rule maker carried out entirely inside the party \citep{hough1979}. Svolik's cross-national evidence points the same way: most authoritarian leaders who lose office by nonconstitutional means are removed by regime insiders rather than by popular uprisings \citep{svolik2012}. The Soviet case also shows the limits of high integration: the party's control of every pillar did not prevent the divisions that Lane and Ross document or the collapse of the system at the end of the period they study.
   442	
   443	\subsection{Social democracy and democratic socialism}
   444	
   445	In social democracies, rules are made by parliaments in which strong programmatic parties compete, and many economic and social rules are negotiated with organized labor and employers before they reach parliament. Sweden is the standard case. The Social Democratic Workers' Party governed for most of the twentieth century, and its close tie to the national trade union confederation gave organized labor direct access to rule making \citep{esping1985}. Korpi's power-resources theory treats the strength of labor's organization as the main determinant of the redistributive content of rules in capitalist democracies \citep{korpi1983}. De jure concentration of rule making is moderate, because rule making requires parliamentary majorities and coalition partners, and contestability is high on every component.
   446	
   447	Corporatist bargaining is the first feature that distinguishes this regime type in the rule-making layer. Peak organizations of labor and capital take part in drafting rules about wages, working conditions, and social insurance, which raises the coupling $C_{\pP\pW}$ by design. Within the domains it covers, a tripartite bargain among the government, the labor confederation, and the employers' confederation is a unanimity procedure among three organs, so by Proposition~\ref{prop:political-power:concentration}(d) the organ-level concentration of rule making in those domains is $1/3$. The same arrangement creates a risk of closure: interests that are not organized into the peak associations, such as the unemployed or new categories of workers, may be excluded from rule making that formally includes all producers.
   448	
   449	The long tenure of a single party is the second feature. Prolonged dominance of rule making by one party in a competitive system is concentration over time, which the static index $H^{\pP}$ does not capture.
   450	
   451	Przeworski described the strategic dilemma of electoral socialism: to win majorities, workers' parties must appeal beyond the working class, and to govern a market economy they depend on the investment decisions of private owners \citep{przeworski1985}. Pontusson's study of investment politics in Sweden showed that proposals to extend collective control over investment met strong resistance from business and were scaled back \citep{pontusson1992}. In the series' vocabulary, the structural dependence of rule makers on capital constrained the rules that social-democratic majorities could make. Kitschelt traced how European social-democratic parties changed their programs as their electorates changed \citep{kitschelt1994}, and Berman argued that the social-democratic movement was defined by a belief in the primacy of political choice over market outcomes \citep{berman2006}.
   452	
   453	Accountability rests on competitive elections, which did remove social-democratic governments, on an independent civil service, and on the formal openness of the corporatist channels. Rothstein's study of Swedish labor-market and school policy argues that the bureaucratic design of implementation, not only legislative majorities, determined whether social-democratic reforms achieved their goals \citep{rothstein1996}. Huber and Stephens show that long periods of social-democratic government were associated with the expansion of welfare states and that the effects persisted after the parties lost office \citep{huber2001}. The documented check on concentration in this regime type is alternation in government combined with corporatist channels that remain open to opposing organized interests, and the documented risk is closure of rule making to the unorganized.
   454	
   455	\subsection{Islamic states}
   456	
   457	In polities that derived political legitimacy from Islamic law, the question of who makes the rules has had an answer that differs from the European cases in one structural respect. Much of the general law, the fiqh developed from the Quran and the Sunna, was elaborated by jurists who were not officials of the ruler. Crone and Hinds argue that the early caliphs claimed religious authority in their own right and that this authority passed over the first centuries of Islam to the scholars, the ulama \citep{crone1986}. Rulers continued to make rules in the domains of administration, taxation, and public order, but they did not control the content of the law in the way that Bodin attributed to the sovereign. Hallaq argues that the modern state, with its claim to a monopoly of legislation, cannot reproduce this moral and legal order \citep{hallaq2013}. The argument is contested; the difference in the distribution of rule-making shares that it identifies is not.
   458	
   459	Classical theory placed the imam, or caliph, at the head of the community. Al-Mawardi's treatise sets out the qualifications of the imam, the ways in which he is validly appointed, including selection by qualified electors, and the powers he may delegate \citep{mawardi1996}. Lambton and Crone describe a long gap between this theory and practice, in which military rulers held effective power while caliphs conferred legitimacy and jurists accommodated the arrangement \citep{lambton1981,crone2004}. The Ottoman Empire added a body of sultanic regulation, the qanun, alongside sharia. Imber's study of the sixteenth-century chief mufti Ebussuud shows a senior jurist harmonizing sultanic law with Hanafi jurisprudence, which places a religious official inside the rule-making process of the empire \citep{imber1997}. Barkey describes Ottoman rule as the brokered management of diverse intermediaries rather than direct command \citep{barkey2008}.
   460	
   461	Two modern states show how differently the legitimating source can be institutionalized. The constitution of the Islamic Republic of Iran, adopted in 1979 and revised in 1989, vests leadership of the community in a just and pious jurist in the absence of the Twelfth Imam, following Khomeini's doctrine of the guardianship of the jurist \citep{iranconst,khomeini1981}. The Leader is selected by an elected Assembly of Experts and sets the general policies of the state. Legislation passed by the elected Majles must be sent to the Guardian Council, whose jurists judge its compatibility with Islam, and disputes between the two bodies go to the Expediency Council \citep{iranconst,schirazi1997}. Rule making in Iran therefore combines electoral and appointed components, and its de jure concentration is moderate to high depending on how the Leader's appointment power is weighted. Factions and parallel institutions compete within this structure \citep{brumberg2001,buchta2000}.
   462	
   463	Saudi rule making is concentrated in form and fragmented in practice. The Basic Law of Governance of 1992 declares the system of government monarchical, states that the regime derives its power from the Quran and the Sunna, provides that laws are issued and amended by royal decree, and gives the King the power to dissolve and re-form the consultative council \citep{saudibasic}. The state rests on the alliance between the Al Saud and the religious establishment descended from the eighteenth-century Wahhabi movement \citep{commins2006,alrasheed2002}. Yet Hertog shows that rule making in the oil era was divided among princes, brokers, and bureaucratic fiefdoms rather than centralized \citep{hertog2010}.
   464	
   465	In both modern cases rule making is closely coupled to legitimation and interpretation, and each case has one further strong coupling. In Iran the coupling to enforcement runs through the Revolutionary Guards, whose economic and political role is debated \citep{alfoneh2013}. In Saudi Arabia the coupling to resource control runs through the allocation of oil rents \citep{gause1994}; whether oil revenue itself weakens accountability is disputed \citep{ross2001}.
   466	
   467	Whether religious jurists raised or lowered the contestability of rule making is the question on which the scholarship divides. Jurists with authority independent of rulers raised the oversight component, while jurists co-opted by rulers could lower the entry component by excluding rival law makers. Kuran attributes the economic divergence of the Middle East to particular institutions of Islamic law, and Kuru attributes authoritarianism and underdevelopment in Muslim-majority states to an alliance between the ulama and the state \citep{kuran2011,kuru2019}; Rubin explains the divergence instead by the terms on which rulers bargained with religious authorities for legitimacy \citep{rubin2017}. Doctrine permits both arrangements. Shia jurists have held positions ranging from political quietism to the activism of Khomeini's doctrine \citep{arjomand1988}, and Sunni theory accommodated military rulers alongside autonomous jurists \citep{lambton1981}.
   468	
   469	Checks on rule makers are documented throughout the type. In the classical period the jurists' authority over much of the law limited what rulers could legislate, Ottoman and Saudi rule rested on negotiation with intermediaries, and Iranian elections remain contested within the limits set by candidate screening. Religious legitimation also constrains the rulers who depend on it: militant challenges to the Saudi state show that religious actors can turn the ruler's own ground of legitimacy against the ruler \citep{hegghammer2010}.
   470	
   471	\subsection{Catholic monarchies}
   472	
   473	In the Catholic monarchies of early modern Europe, the king was in theory the source of law. Bodin made the power to legislate without the consent of others the mark of sovereignty \citep{bodin1992}, and Bossuet grounded royal authority in Scripture \citep{bossuet1990}. Kantorowicz traced the medieval idea that the king had a mortal natural body and an undying political body \citep{kantorowicz1957}, and Figgis described the theory of divine right as it developed in early modern Europe \citep{figgis1914}. In formal terms, rule making was concentrated in one person, close to the dictatorship case of Proposition~\ref{prop:political-power:concentration}(d).
   474	
   475	In practice, Catholic monarchs shared rule making with councils, estates, and courts that could delay or block royal decrees. Habsburg Spain was a composite monarchy whose kingdoms kept their own laws and representative assemblies, and royal government worked through separate councils for kingdoms and functions \citep{elliott1963}. When Olivares tried in the 1620s and 1630s to make the kingdoms share the costs of the monarchy's wars, the resistance contributed to the revolts of Catalonia and Portugal in 1640 \citep{elliott1963,elliott1984}, a documented check on what the crown could impose. In Bourbon France the Estates-General did not meet between 1614 and 1789, yet royal ordinances still had to be registered by the Parlements, which could remonstrate and delay unless the king overrode them in a formal session in person. Beik's study of Languedoc shows absolutism working through collaboration with provincial elites who shared in its revenues \citep{beik1985}, and Collins presents the French state as a negotiated structure with real limits \citep{collins1995}. The crown's reach was nonetheless real: Root shows royal rules on village finances reshaping relations between peasants and lords in Burgundy \citep{root1987}.
   476	
   477	The Papal States combined spiritual and temporal rule making in one office. The pope was elected by the cardinals, so the Papal States were an elective monarchy, and Prodi describes the early modern papacy as a single body with two souls, the head of the universal Church and the prince of a territorial state \citep{prodi1987}. Rule making in the Papal States was concentrated in the pope and the curial congregations, and the coupling between rule making and legitimation was complete by construction.
   478	
   479	Rule making in these monarchies was coupled to the other pillars through the Church and through office. Crowns controlled appointments to high Church office in their territories, which raised $C_{\pP\pI}$; the Gallican tradition in France asserted royal and episcopal liberties against Rome, and Van Kley traces how disputes over Jansenism drew the Parlements into conflict with both crown and papacy \citep{vankley1996}. Venality of judicial and financial offices coupled rule making to resource control and to interpretation, because offices were property that the crown sold and whose holders could resist the crown. Ertman classifies France and Spain as patrimonial absolutist states, in which office holding and fiscal administration were tied to private interests \citep{ertman1997}.
   480	
   481	Accountability did not take the form of replacement of rule makers, which the dynastic principle excluded, but of the corporate privileges of estates, towns, Parlements, and the Church, of the Church's autonomous canon law, and, in extreme cases, of revolt. The de jure concentration was high, and practical concentration was lower because of brokerage; contestability was low in replacement and entry and intermittently significant in oversight through the Parlements and estates.
   482	
   483	\subsection{Secular democracies}
   484	
   485	In secular democracies, the authority to make rules is derived from popular sovereignty and distributed by a constitution among elected legislatures, executives, courts with powers of review, independent agencies, subnational governments, and in some cases the voters directly. The distribution varies widely. Lijphart's comparison of thirty-six democracies distinguishes majoritarian systems, in which a single-party cabinet controls rule making between elections, from consensus systems that disperse it \citep{lijphart1999}. Federal systems add a territorial division, giving subnational governments rule-making authority that the national legislature cannot revoke by ordinary statute. Presidential systems add a division between an executive and a legislature with separate electoral mandates and fixed terms, which Linz argued makes conflicts between them harder to resolve \citep{linz1990}. Where constitutions provide for referendums and popular initiatives, the electorate itself becomes a veto player or an agenda setter in the rule-making procedure \citep{lijphart1999}. In the vocabulary of this paper, majoritarian systems have higher de jure concentration and fewer veto players; consensus systems have lower concentration and more veto players, and the trade-off between them is the subject of Proposition~\ref{prop:political-power:veto} in Section~\ref{sec:mechanisms}.
   486	
   487	Contestability is the defining property of this regime type. Dahl's polyarchy requires both inclusive participation and public contestation \citep{dahl1971}. Przeworski characterized democracy as a system in which parties can lose elections and accept the loss, so that outcomes are uncertain in advance \citep{przeworski1991}. The replacement component $q^{\mathrm{rep}}$ is therefore the component that distinguishes democracies from the other regime types most sharply. Data projects such as V-Dem measure it alongside legislative and judicial constraints on the executive and the freedom to form parties \citep{coppedge2011}, and the Regimes of the World classification uses these measures to separate liberal and electoral democracies from electoral and closed autocracies \citep{luhrmann2018}.
   488	
   489	Secular democracies have relocated part of rule making away from elected bodies. Constitutional courts in Europe shape legislation by reviewing it, and Stone Sweet shows that legislators anticipate review and draft accordingly \citep{stonesweet2000}. Hirschl argues that the transfer of power to courts in several democracies served elites who expected to lose control of legislatures \citep{hirschl2004}. Independent agencies and central banks make rules under delegated authority. Each of these relocations lowers the concentration of rule making in elected bodies and raises its concentration in bodies that are not removable by voters, and whether the result is more or less accountable depends on the oversight component, not on the relocation itself.
   490	
   491	The documented capture risk in this regime type is the erosion of contestability by elected rule makers. Levitsky and Way describe regimes that hold real elections while incumbents abuse state resources, media access, and legal harassment to tilt the field \citep{levitsky2010}. In such regimes the formal rule-making procedure is unchanged while the replacement and entry components of contestability fall. The documented checks are the ones Madison anticipated, rival institutions with the means and motive to resist \citep{madison1788}, together with the coordination of citizens against transgressions that Weingast identifies as the condition for constitutional limits to hold \citep{weingast1997}. Pettit's republican account treats the contestability of rule making by those subject to it as the core of freedom from domination \citep{pettit1997}, which supplies a normative ground for the measurement emphasis of Definition~\ref{def:political-power:qp}.
   492	
   493	\subsection{Comparative summary}
   494	
   495	Tables~\ref{tab:regimes-holders} and~\ref{tab:regimes-coupling} summarize the configuration of the rule-making pillar under each regime type and the coupling that the cited literature documents. Every regime type performs the function, which is what Theorem~\ref{thm:political-power:necessity} requires. Concentration and contestability vary independently of the source of legitimacy: rule making in Habsburg Spain was less concentrated in practice than its theory claimed, and rule making in some electoral regimes is more concentrated than their procedures suggest. The main channel of coupling differs by regime type, from wealth to rules in market economies to appointment in party-states and religious legitimation in the Islamic states and Catholic monarchies, which is the rule-making form of the source's proposition that control paths differ by regime \citep[Proposition~3]{largo2026hbs}.
   496	
   497	\begin{table}[tbp]
   498	\centering
   499	\small
   500	\caption{Holders, concentration, and contestability of rule making by regime type. Concentration and contestability are qualitative descriptions based on the cited literature, not coded values.}
   501	\label{tab:regimes-holders}
   502	\begin{tabularx}{\textwidth}{@{}L{2.5cm}YYY@{}}
   503	\toprule
   504	Regime type & Principal rule makers & Concentration of rule making & Contestability of rule making \\
   505	\midrule
   506	Market-capitalist & Elected legislatures, executives, and regulatory agencies, with organized interests shaping drafts & Moderate, with several veto players in the formal procedure & High in form, with unequal practical access by economic resources \\
   507	Communist party-state & Party leadership and apparatus, with the legislature ratifying & High, through the party's control of appointments in every pillar & Low outside the party and partial within it \\
   508	Social democracy & Parliamentary majorities negotiating with peak organizations of labor and capital & Moderate, with long tenure of a dominant party in some cases & High, with a risk of closure to unorganized interests \\
   509	Islamic states & Rulers and councils, with jurists holding authority over much of the law & Varies from dispersed classical arrangements to concentrated modern ones & Varies from contested elections in Iran to none in Saudi Arabia \\
   510	Catholic monarchies & Crown in council, with Parlements, Cortes, and estates able to delay or refuse & High in theory and lower in practice because of brokerage & Low for replacement and intermittent for oversight \\
   511	Secular democracies & Legislatures and executives under a constitution, with courts and agencies holding delegated parts & Low to moderate, depending on majoritarian or consensus design & High, and falling where incumbents tilt the electoral field \\
   512	\bottomrule
   513	\end{tabularx}
   514	\end{table}
   515	
   516	\begin{table}[tbp]
   517	\centering
   518	\small
   519	\caption{Coupling of rule making to other pillars, documented capture risks, and documented checks by regime type.}
   520	\label{tab:regimes-coupling}
   521	\begin{tabularx}{\textwidth}{@{}L{2.5cm}YYY@{}}
   522	\toprule
   523	Regime type & Strongest documented coupling & Documented capture risk & Documented check \\
   524	\midrule
   525	Market-capitalist & Resource control to rule making through donations, lobbying, and investment dependence & Privileged access of donors and connected lobbyists & Competing interest groups, elections, and the advantage of the status quo \\
   526	Communist party-state & Rule making to every other pillar through appointment lists & Integration of all pillars under one coalition & Factional bargaining and divisions within the elite \\
   527	Social democracy & Rule making to production through corporatist bargaining & Exclusion of unorganized groups from negotiated rules & Electoral alternation and open corporatist channels \\
   528	Islamic states & Rule making to legitimation and interpretation through religious-legal authority & Clerical vetting of legislation and candidates, and rent allocation & Independent juristic authority, elections in Iran, and brokered rule \\
   529	Catholic monarchies & Rule making to legitimation through royal control of Church appointments & Venality of office and dynastic exclusion of replacement & Corporate privileges, registration by Parlements, and revolt \\
   530	Secular democracies & Rule making to interpretation through appointments and constitutional review & Erosion of contestability by elected incumbents & Rival institutions and citizen coordination against transgression \\
   531	\bottomrule
   532	\end{tabularx}
   533	\end{table}
   534	
   535	\section{Mechanisms, failure modes and checks}
   536	\label{sec:mechanisms}
   537	
   538	The necessity theorem says that rule making occurs; Proposition B concerns the conditions under which it becomes concentrated, coupled to other pillars, and unaccountable. Each mechanism below is a comparative static under explicit assumptions, not a law of history, and each identifies the check that interrupts it, in line with the source's proposition that checks can interrupt the transmission of concentrated power \citep[Proposition~2]{largo2026hbs}.
   539	
   540	\subsection{Delegation and oligarchy}
   541	
   542	Michels argued that the leaders of large organizations escape the control of members because members lack the time, expertise, and information to monitor them \citep{michels1915}. Olson's analysis of collective action explains why: the benefit of monitoring is shared by all members, while its cost falls on the one who monitors \citep{olson1965}. A simple model makes the conditional character of the argument precise.
   543	
   544	\begin{assumption}[Monitoring game]
   545	\label{ass:political-power:monitoring}
   546	An organization has $n\ge2$ members and a leadership that extracts a rent $\rho>0$ from the organization in each period, at a cost of $\rho/n$ to each member. Each member chooses simultaneously whether to monitor the leadership at private cost $c>0$. Each monitor independently detects the extraction with probability $\delta\in(0,1]$, and detection leads to the replacement of the leadership. After replacement the rent is returned to the members, so each member recovers $\rho/n$. A member's payoff is the expected rent recovered by that member minus the member's own monitoring cost.
   547	\end{assumption}
   548	
   549	\begin{proposition}[Monitoring vanishes in large organizations]
   550	\label{prop:political-power:michels}
   551	Under Assumption~\ref{ass:political-power:monitoring}:
   552	\begin{enumerate}[label=(\alph*)]
   553	\item if $n>\rho\delta/c$, the unique Nash equilibrium is that no member monitors, and the leadership retains the rent with probability one;
   554	\item suppose instead that an organized opposition faction, distinct from the members, chooses simultaneously with them whether to monitor at cost $c$, detects the extraction independently with probability $\delta$ if it monitors, and takes office whenever the leadership is replaced, whoever detected the extraction. In office the faction keeps a share $\beta\in(0,1]$ of the rent, so each member recovers only $(1-\beta)\rho/n$, and the faction's payoff is $\beta\rho$ times the probability of replacement minus $c$ if it monitors. If $n>(1-\beta)\rho\delta/c$ and $\beta\rho\delta>c$, the unique Nash equilibrium is that no member monitors and the faction monitors, so the leadership is detected and replaced with probability $\delta$ whatever the value of $n$.
   555	\end{enumerate}
   556	\end{proposition}
   557	
   558	\begin{proof}
   559	(a) If $k$ other members monitor, the probability that none of them detects the extraction is $(1-\delta)^k$. A member who adds monitoring raises the detection probability by $\delta(1-\delta)^k$ and so gains $(\rho/n)\delta(1-\delta)^k$ in expected recovered rent. This gain is at most $(\rho/n)\delta$, which is less than $c$ when $n>\rho\delta/c$. Monitoring is therefore strictly dominated for every member, whatever the others do, and the unique equilibrium has no monitoring.
   560	
   561	(b) A member's gain from monitoring is now at most $(1-\beta)(\rho/n)\delta$, which is less than $c$ when $n>(1-\beta)\rho\delta/c$, so monitoring is strictly dominated for every member as in (a). In any equilibrium no member monitors, and the faction's gain from monitoring is then $\beta\rho\delta$, which exceeds $c$ and does not depend on $n$. The faction therefore monitors, and the equilibrium is unique because the members' choice is dominant.
   562	\end{proof}
   563	
   564	The threshold $n^\ast=\rho\delta/c$ rises with the size of the rent and the effectiveness of monitoring and falls with its cost. Part (a) is Michels's tendency stated as a conditional result. Part (b) identifies the check. An organized opposition with a private stake in winning office converts the public good of oversight into a private incentive, and it does so even though it lowers the members' own incentive to monitor. Lipset, Trow, and Coleman's study of the International Typographical Union found exactly such an arrangement, a durable two-party system inside a union, and it is the classic exception to Michels's law \citep{lipset1956}. Voss and Sherman documented later cases in which American union locals reversed oligarchic tendencies \citep{voss2000}, and Cassinelli offered an early analytic critique of the law \citep{cassinelli1953}. Schumpeter's competitive theory of democracy rests on the same mechanism at the scale of a polity: rival teams of leaders compete for the vote and monitor one another \citep{schumpeter1942}.
   565	
   566	The model omits much. Leaders can raise the cost of monitoring by controlling information, which is Michels's own emphasis, and members may value leaders for reasons other than rent. The proposition shows only that oligarchy follows from size under one set of conditions and that a specific institutional change reverses it. That is enough to treat oligarchization as a conditional tendency, which is the role the series assigns it in the argument for Proposition B (Part VII), rather than as a necessity.
   567	
   568	\subsection{Veto players and the status quo}
   569	
   570	Adding veto players is the standard constitutional remedy for concentrated rule making. It has a cost that the comparison of majoritarian and consensus democracies brings out, and a simple result shows why the cost is unavoidable.
   571	
   572	\begin{definition}[Winset]
   573	\label{def:political-power:veto-players}
   574	Let $X$ be a set of alternatives, $q\in X$ the status quo, and $K$ a nonempty set of veto players, each with strict preferences $\succ_i$ on $X$. The \emph{winset} of $q$ is $W_K(q)=\{x\in X: x\succ_i q\text{ for all }i\in K\}$, the set of alternatives that every veto player prefers to the status quo \citep{tsebelis2002}. A \emph{pure veto-player procedure} enacts $x$ against $q$ exactly when $x\in W_K(q)$; it is the unanimity game on $K$ of Proposition~\ref{prop:political-power:concentration}(d). In a general simple game membership in $W_K(q)$ is necessary for replacing $q$ but not sufficient.
   575	\end{definition}
   576	
   577	\begin{proposition}[Veto players protect the status quo]
   578	\label{prop:political-power:veto}
   579	\leavevmode
   580	\begin{enumerate}[label=(\alph*)]

exec
/usr/local/bin/zsh -lc "sed -n '801,985p' papers/latex/political-power.tex | nl -ba -v 801" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   801	\bibitem[Coppedge et al.(2011)]{coppedge2011}
   802	Coppedge, Michael, John Gerring, David Altman, Michael Bernhard, Steven Fish, Allen Hicken, Matthew Kroenig, Staffan I. Lindberg, Kelly McMann, Pamela Paxton, Holli A. Semetko, Svend-Erik Skaaning, Jeffrey Staton, and Jan Teorell. 2011. ``Conceptualizing and Measuring Democracy: A New Approach.'' \emph{Perspectives on Politics} 9(2): 247-267. doi:10.1017/S1537592711000880.
   803	
   804	\bibitem[Cox et al.(2010)]{cox2010}
   805	Cox, Michael, Gwen Arnold, and Sergio Villamayor Tomas. 2010. ``A Review of Design Principles for Community-based Natural Resource Management.'' \emph{Ecology and Society} 15(4): 38. doi:10.5751/ES-03704-150438.
   806	
   807	\bibitem[Crone and Hinds(1986)]{crone1986}
   808	Crone, Patricia and Martin Hinds. 1986. \emph{God's Caliph: Religious Authority in the First Centuries of Islam}. Cambridge University Press.
   809	
   810	\bibitem[Crone(2004)]{crone2004}
   811	Crone, Patricia. 2004. \emph{God's Rule: Government and Islam: Six Centuries of Medieval Islamic Political Thought}. Columbia University Press.
   812	
   813	\bibitem[Culpepper(2010)]{culpepper2010}
   814	Culpepper, Pepper D. 2010. \emph{Quiet Politics and Business Power: Corporate Control in Europe and Japan}. Cambridge University Press. doi:10.1017/cbo9780511760716.
   815	
   816	\bibitem[Dahl(1961)]{dahl1961}
   817	Dahl, Robert A. 1961. \emph{Who Governs? Democracy and Power in an American City}. Yale University Press.
   818	
   819	\bibitem[Dahl(1971)]{dahl1971}
   820	Dahl, Robert A. 1971. \emph{Polyarchy: Participation and Opposition}. Yale University Press.
   821	
   822	\bibitem[Djilas(1957)]{djilas1957}
   823	Djilas, Milovan. 1957. \emph{The New Class: An Analysis of the Communist System}. Praeger.
   824	
   825	\bibitem[Elkjaer and Klitgaard(2024)]{elkjaer2024}
   826	Elkjaer, Mads Andreas and Michael Baggesen Klitgaard. 2024. ``Economic Inequality and Political Responsiveness: A Systematic Review.'' \emph{Perspectives on Politics} 22(2): 318-337. doi:10.1017/S1537592721002188.
   827	
   828	\bibitem[Ellickson(1991)]{ellickson1991}
   829	Ellickson, Robert C. 1991. \emph{Order without Law: How Neighbors Settle Disputes}. Harvard University Press. doi:10.4159/9780674036437.
   830	
   831	\bibitem[Elliott(1963)]{elliott1963}
   832	Elliott, J. H. 1963. \emph{Imperial Spain 1469-1716}. Edward Arnold.
   833	
   834	\bibitem[Elliott(1984)]{elliott1984}
   835	Elliott, J. H. 1984. \emph{Richelieu and Olivares}. Cambridge University Press.
   836	
   837	\bibitem[Elster(1983)]{elster1983}
   838	Elster, Jon. 1983. \emph{Explaining Technical Change: A Case Study in the Philosophy of Science}. Cambridge University Press.
   839	
   840	\bibitem[Ertman(1997)]{ertman1997}
   841	Ertman, Thomas. 1997. \emph{Birth of the Leviathan: Building States and Regimes in Medieval and Early Modern Europe}. Cambridge University Press. doi:10.1017/cbo9780511529016.
   842	
   843	\bibitem[Esping-Andersen(1985)]{esping1985}
   844	Esping-Andersen, G{\o}sta. 1985. \emph{Politics against Markets: The Social Democratic Road to Power}. Princeton University Press. doi:10.1515/9781400886203.
   845	
   846	\bibitem[Evans-Pritchard(1940)]{evanspritchard1940}
   847	Evans-Pritchard, E. E. 1940. \emph{The Nuer: A Description of the Modes of Livelihood and Political Institutions of a Nilotic People}. Clarendon Press.
   848	
   849	\bibitem[Fainsod(1953)]{fainsod1953}
   850	Fainsod, Merle. 1953. \emph{How Russia Is Ruled}. Harvard University Press. doi:10.4159/harvard.9780674189188.
   851	
   852	\bibitem[Figgis(1914)]{figgis1914}
   853	Figgis, John Neville. 1914. \emph{The Divine Right of Kings}. Cambridge University Press.
   854	
   855	\bibitem[Friesen(2001)]{friesen2001}
   856	Friesen, Steven J. 2001. \emph{Imperial Cults and the Apocalypse of John: Reading Revelation in the Ruins}. Oxford University Press. doi:10.1093/0195131533.001.0001.
   857	
   858	\bibitem[Fuller(1995)]{fuller1995}
   859	Fuller, Robert C. 1995. \emph{Naming the Antichrist: The History of an American Obsession}. Oxford University Press. doi:10.1093/acprof:oso/9780195109795.001.0001.
   860	
   861	\bibitem[Gandhi and Przeworski(2007)]{gandhi2007}
   862	Gandhi, Jennifer and Adam Przeworski. 2007. ``Authoritarian Institutions and the Survival of Autocrats.'' \emph{Comparative Political Studies} 40(11): 1279-1301. doi:10.1177/0010414007305817.
   863	
   864	\bibitem[Gause(1994)]{gause1994}
   865	Gause, F. Gregory III. 1994. \emph{Oil Monarchies: Domestic and Security Challenges in the Arab Gulf States}. Council on Foreign Relations Press.
   866	
   867	\bibitem[Geddes et al.(2014)]{geddes2014}
   868	Geddes, Barbara, Joseph Wright, and Erica Frantz. 2014. ``Autocratic Breakdown and Regime Transitions: A New Data Set.'' \emph{Perspectives on Politics} 12(2): 313-331. doi:10.1017/S1537592714000851.
   869	
   870	\bibitem[Gerschewski(2013)]{gerschewski2013}
   871	Gerschewski, Johannes. 2013. ``The Three Pillars of Stability: Legitimation, Repression, and Co-optation in Autocratic Regimes.'' \emph{Democratization} 20(1): 13-38. doi:10.1080/13510347.2013.738860.
   872	
   873	\bibitem[Gilens and Page(2014)]{gilens2014}
   874	Gilens, Martin and Benjamin I. Page. 2014. ``Testing Theories of American Politics: Elites, Interest Groups, and Average Citizens.'' \emph{Perspectives on Politics} 12(3): 564-581. doi:10.1017/S1537592714001595.
   875	
   876	\bibitem[Graeber and Wengrow(2021)]{graeber2021}
   877	Graeber, David and David Wengrow. 2021. \emph{The Dawn of Everything: A New History of Humanity}. Farrar, Straus and Giroux.
   878	
   879	\bibitem[Guriev and Treisman(2019)]{guriev2019}
   880	Guriev, Sergei and Daniel Treisman. 2019. ``Informational Autocrats.'' \emph{Journal of Economic Perspectives} 33(4): 100-127. doi:10.1257/jep.33.4.100.
   881	
   882	\bibitem[Hacker and Pierson(2010)]{hackerpierson2010}
   883	Hacker, Jacob S. and Paul Pierson. 2010. \emph{Winner-Take-All Politics: How Washington Made the Rich Richer and Turned Its Back on the Middle Class}. Simon \& Schuster.
   884	
   885	\bibitem[Hale(2014)]{hale2014}
   886	Hale, Henry E. 2014. \emph{Patronal Politics: Eurasian Regime Dynamics in Comparative Perspective}. Cambridge University Press. doi:10.1017/CBO9781139683524.
   887	
   888	\bibitem[Hall and Deardorff(2006)]{hall2006}
   889	Hall, Richard L. and Alan V. Deardorff. 2006. ``Lobbying as Legislative Subsidy.'' \emph{American Political Science Review} 100(1): 69-84. doi:10.1017/s0003055406062010.
   890	
   891	\bibitem[Hallaq(2013)]{hallaq2013}
   892	Hallaq, Wael B. 2013. \emph{The Impossible State: Islam, Politics, and Modernity's Moral Predicament}. Columbia University Press.
   893	
   894	\bibitem[Hart(1961)]{hart1961}
   895	Hart, H. L. A. 1961. \emph{The Concept of Law}. Clarendon Press (3rd ed.~2012, Oxford University Press). doi:10.1093/he/9780199644704.001.0001.
   896	
   897	\bibitem[Hayek(1973)]{hayek1973}
   898	Hayek, Friedrich A. 1973. \emph{Law, Legislation and Liberty, Volume 1: Rules and Order}. University of Chicago Press. doi:10.7208/chicago/9780226321233.001.0001.
   899	
   900	\bibitem[Hegghammer(2010)]{hegghammer2010}
   901	Hegghammer, Thomas. 2010. \emph{Jihad in Saudi Arabia: Violence and Pan-Islamism since 1979}. Cambridge University Press. doi:10.1017/cbo9780511809439.
   902	
   903	\bibitem[Hempel(1959)]{hempel1959}
   904	Hempel, Carl G. 1959. ``The Logic of Functional Analysis.'' In \emph{Symposium on Sociological Theory}, ed.~Llewellyn Gross, Harper \& Row, pp.~271-307.
   905	
   906	\bibitem[Hertog(2010)]{hertog2010}
   907	Hertog, Steffen. 2010. \emph{Princes, Brokers, and Bureaucrats: Oil and the State in Saudi Arabia}. Cornell University Press. doi:10.7591/9780801458774.
   908	
   909	\bibitem[Hirschl(2004)]{hirschl2004}
   910	Hirschl, Ran. 2004. \emph{Towards Juristocracy: The Origins and Consequences of the New Constitutionalism}. Harvard University Press. doi:10.2307/j.ctv15d81nb.
   911	
   912	\bibitem[Hough and Fainsod(1979)]{hough1979}
   913	Hough, Jerry F. and Merle Fainsod. 1979. \emph{How the Soviet Union Is Governed}. Harvard University Press.
   914	
   915	\bibitem[Huber and Stephens(2001)]{huber2001}
   916	Huber, Evelyne and John D. Stephens. 2001. \emph{Development and Crisis of the Welfare State: Parties and Policies in Global Markets}. University of Chicago Press. doi:10.7208/chicago/9780226356495.001.0001.
   917	
   918	\bibitem[Imber(1997)]{imber1997}
   919	Imber, Colin. 1997. \emph{Ebu's-su'ud: The Islamic Legal Tradition}. Stanford University Press.
   920	
   921	\bibitem[Islamic Republic of Iran(1989)]{iranconst}
   922	Islamic Republic of Iran. 1989. \emph{Constitution of the Islamic Republic of Iran (1979, revised 1989)}. English translation, Constitute Project. \url{https://www.constituteproject.org/constitution/Iran_1989}.
   923	
   924	\bibitem[Kalla and Broockman(2016)]{kalla2016}
   925	Kalla, Joshua L. and David E. Broockman. 2016. ``Campaign Contributions Facilitate Access to Congressional Officials: A Randomized Field Experiment.'' \emph{American Journal of Political Science} 60(3): 545-558. doi:10.1111/ajps.12180.
   926	
   927	\bibitem[Kantorowicz(1957)]{kantorowicz1957}
   928	Kantorowicz, Ernst H. 1957. \emph{The King's Two Bodies: A Study in Mediaeval Political Theology}. Princeton University Press. doi:10.1515/9781400880782.
   929	
   930	\bibitem[Kelly(1995)]{kelly1995}
   931	Kelly, Robert L. 1995. \emph{The Foraging Spectrum: Diversity in Hunter-Gatherer Lifeways}. Smithsonian Institution Press. doi:10.2307/j.ctv2sx9gc9.
   932	
   933	\bibitem[Khomeini(1981)]{khomeini1981}
   934	Khomeini, Ruhollah. 1981. \emph{Islam and Revolution: Writings and Declarations of Imam Khomeini (incl.~Islamic Government, 1970)}, trans.~Hamid Algar. Mizan Press.
   935	
   936	\bibitem[King James Version(1611)]{kjv}
   937	King James Version. 1611. \emph{The Holy Bible, Authorized King James Version}. Project Gutenberg eBook 10. \url{https://www.gutenberg.org/ebooks/10}.
   938	
   939	\bibitem[Kingdom of Saudi Arabia(1992)]{saudibasic}
   940	Kingdom of Saudi Arabia. 1992. \emph{Basic Law of Governance (1992, revised 2013)}. English translation, Constitute Project. \url{https://www.constituteproject.org/constitution/Saudi_Arabia_2013}.
   941	
   942	\bibitem[Kitschelt(1994)]{kitschelt1994}
   943	Kitschelt, Herbert. 1994. \emph{The Transformation of European Social Democracy}. Cambridge University Press. doi:10.1017/CBO9780511622014.
   944	
   945	\bibitem[Koester(2014)]{koester2014}
   946	Koester, Craig R. 2014. \emph{Revelation: A New Translation with Introduction and Commentary}. Yale University Press (Anchor Yale Bible 38A). doi:10.12987/9780300211030.
   947	
   948	\bibitem[Kornai(1992)]{kornai1992}
   949	Kornai, J\'anos. 1992. \emph{The Socialist System: The Political Economy of Communism}. Princeton University Press. doi:10.2307/j.ctv1ddczdr.
   950	
   951	\bibitem[Korpi(1983)]{korpi1983}
   952	Korpi, Walter. 1983. \emph{The Democratic Class Struggle}. Routledge \& Kegan Paul.
   953	
   954	\bibitem[Kraybill(1996)]{kraybill1996}
   955	Kraybill, J. Nelson. 1996. \emph{Imperial Cult and Commerce in John's Apocalypse}. Sheffield Academic Press (JSNT Supplement 132).
   956	
   957	\bibitem[Kuran(2011)]{kuran2011}
   958	Kuran, Timur. 2011. \emph{The Long Divergence: How Islamic Law Held Back the Middle East}. Princeton University Press. doi:10.1515/9781400836017.
   959	
   960	\bibitem[Kuru(2019)]{kuru2019}
   961	Kuru, Ahmet T. 2019. \emph{Islam, Authoritarianism, and Underdevelopment: A Global and Historical Comparison}. Cambridge University Press. doi:10.1017/9781108296892.
   962	
   963	\bibitem[Lambton(1981)]{lambton1981}
   964	Lambton, Ann K. S. 1981. \emph{State and Government in Medieval Islam}. Oxford University Press. doi:10.4324/9780203385463.
   965	
   966	\bibitem[Landry(2008)]{landry2008}
   967	Landry, Pierre F. 2008. \emph{Decentralized Authoritarianism in China: The Communist Party's Control of Local Elites in the Post-Mao Era}. Cambridge University Press. doi:10.1017/CBO9780511510243.
   968	
   969	\bibitem[Lane and Ross(1995)]{lane1995}
   970	Lane, David and Cameron Ross. 1995. ``The CPSU Ruling Elite 1981-1991: Commonalities and Divisions.'' \emph{Communist and Post-Communist Studies} 28(3): 339-360. doi:10.1016/0967-067X(95)00020-U.
   971	
   972	\bibitem[Largo(2026)]{largo2026hbs}
   973	Largo, Mateo. 2026. \emph{The Hierarchy of the Beast System: Institutional Power, Elite Coordination, and Economic Dependency Across Political Regimes}. Working paper, 14 October 2026.
   974	
   975	\bibitem[Lee(2013)]{lee2013}
   976	Lee, Richard B. 2013. \emph{The Dobe Ju/'hoansi (4th edition)}. Wadsworth/Cengage Learning.
   977	
   978	\bibitem[Levitsky and Way(2010)]{levitsky2010}
   979	Levitsky, Steven and Lucan A. Way. 2010. \emph{Competitive Authoritarianism: Hybrid Regimes after the Cold War}. Cambridge University Press. doi:10.1017/CBO9780511781353.
   980	
   981	\bibitem[Lijphart(1999)]{lijphart1999}
   982	Lijphart, Arend. 1999. \emph{Patterns of Democracy: Government Forms and Performance in Thirty-Six Countries}. Yale University Press. doi:10.12987/9780300189124.
   983	
   984	\bibitem[Lindblom(1977)]{lindblom1977}
   985	Lindblom, Charles E. 1977. \emph{Politics and Markets: The World's Political-Economic Systems}. Basic Books.

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '260,480p' papers/latex/political-power.tex | nl -ba -v 260" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   260	\label{sec:necessity}
   261	
   262	\subsection{Assumptions of the lemma}
   263	
   264	The working axiom for this pillar in the series is plurality: members' preferences diverge, yet collective choices are made. Part VII refines the full axiom set and proves the general theorem. Here the axiom is stated in the form needed for the rule-making lemma, together with two further assumptions that make its content explicit.
   265	
   266	\begin{assumption}[Plurality]
   267	\label{ass:political-power:plurality}
   268	The collective repeatedly faces collective decisions in the sense of Definition~\ref{def:political-power:rule-system}, and for each such decision the members' preferences diverge over the alternatives: for every alternative $x\in X$ some member strictly prefers another alternative $y\in X$ to $x$.
   269	\end{assumption}
   270	
   271	\begin{assumption}[Environmental change]
   272	\label{ass:political-power:change}
   273	The environment $e_t\in E$ of the collective varies over time. There is a viability correspondence $\mathcal{V}:E\to 2^{\Rules}$, where $\mathcal{V}(e)$ is the set of rule systems under which the collective survives a period in environment $e$, and the realized path contains periods $s_0<s_1<\dots<s_r$, with $r\ge1$, such that consecutive viability sets are disjoint: $\mathcal{V}(e_{s_{j-1}})\cap\mathcal{V}(e_{s_j})=\emptyset$ for $j=1,\dots,r$.
   274	\end{assumption}
   275	
   276	\begin{assumption}[Self-government and persistence]
   277	\label{ass:political-power:persistence}
   278	(i) The collective's decisions and changes in its rules are produced by practices of its members rather than imposed from outside. (ii) The collective persists over a window $T$ of consecutive periods that contains $s_0$ and $s_r$, so $R_t\in\mathcal{V}(e_t)$ for all $t\in T$.
   279	\end{assumption}
   280	
   281	The plurality assumption is empirical. It fails for a group whose members always agree on every collective choice, which no ethnography or history records for any group of more than a few people over any length of time. The change assumption formalizes the condition under which a regime of fixed rules becomes untenable. Hart called a regime of primary rules without a rule of change \emph{static} and listed this as one of its three defects \citep{hart1961}; the assumption states when the defect becomes fatal rather than merely costly. The self-government clause excludes a group whose rules are set entirely by an outside power. Such a group does not falsify the necessity of rule making; it shows that the rule maker lies outside the boundary drawn around the group, and the boundary should be redrawn to include it.
   282	
   283	\begin{lemma}[Collective choice requires a procedure]
   284	\label{lem:political-power:choice}
   285	Under Assumption~\ref{ass:political-power:plurality} and clause (i) of Assumption~\ref{ass:political-power:persistence}, every realized collective decision is ranked below some other alternative by at least one member. The practice that produces the realized decision therefore selects among divergent preferences, and the collective implements part (a) of Definition~\ref{def:political-power:rule-making}.
   286	\end{lemma}
   287	
   288	\begin{proof}
   289	Let $x^\ast$ be the alternative realized in a collective decision. By Assumption~\ref{ass:political-power:plurality} there is a member $i$ and an alternative $y$ with $y\succ_i x^\ast$. Because the decision applies to all members at once, $i$ cannot obtain $y$ while others obtain $x^\ast$. Some practice, whether a vote, a command, a discussion that ends when objectors fall silent, or a default to the status quo, determined that $x^\ast$ rather than $y$ would hold for everyone, and by clause (i) of Assumption~\ref{ass:political-power:persistence} that practice is the members' own. That practice selects among divergent preferences. Collective decisions recur by assumption, so such selections recur.
   290	\end{proof}
   291	
   292	\begin{lemma}[Change requires a rule of change]
   293	\label{lem:political-power:change}
   294	Under Assumptions~\ref{ass:political-power:change} and~\ref{ass:political-power:persistence}, the rule system is replaced at least $r$ times on $T$: for each $j=1,\dots,r$ there is $t$ with $s_{j-1}\le t<s_j$ and $R_{t+1}\neq R_t$. Each replacement is produced by a practice of the members.
   295	\end{lemma}
   296	
   297	\begin{proof}
   298	Fix $j$ and suppose $R_t=R_{t+1}$ for every $t$ with $s_{j-1}\le t<s_j$. Then $R_{s_{j-1}}=R_{s_j}=R$. Clause (ii) of Assumption~\ref{ass:political-power:persistence} gives $R\in\mathcal{V}(e_{s_{j-1}})$ and $R\in\mathcal{V}(e_{s_j})$, which contradicts the disjointness in Assumption~\ref{ass:political-power:change}. So some $t$ in $[s_{j-1},s_j)$ has $R_{t+1}\neq R_t$, and both $t$ and $t+1$ lie in $T$ because $T$ consists of consecutive periods containing $s_0$ and $s_r$. The intervals $[s_{j-1},s_j)$ are disjoint, so the $r$ replacements are distinct. By clause (i) of Assumption~\ref{ass:political-power:persistence} each is produced by the members' practices.
   299	\end{proof}
   300	
   301	Hart's term for the practice whose existence Lemma~\ref{lem:political-power:change} establishes is the rule of change. The series assigns this member of Hart's triad of secondary rules to the rule-making pillar; the rule of adjudication belongs to Part III and the rule of recognition to Part IV (Definition~2.2 of that Part).
   302	
   303	\begin{definition}[Rule of change]
   304	\label{def:political-power:rule-of-change}
   305	A \emph{rule of change} of a collective is a secondary rule, written or customary, that identifies who may introduce, alter, or repeal the collective's general rules and by what procedure \citep{hart1961}. It is the rule-making procedure of Definition~\ref{def:political-power:rule-making}(b) considered as a rule accepted by the members rather than as a regularity observed from outside.
   306	\end{definition}
   307	
   308	\begin{theorem}[Necessity of rule making]
   309	\label{thm:political-power:necessity}
   310	A collective that satisfies Assumption~\ref{ass:political-power:plurality} and clause (i) of Assumption~\ref{ass:political-power:persistence} implements the rule-making function in sense (a). If it also satisfies Assumptions~\ref{ass:political-power:change} and~\ref{ass:political-power:persistence}, it implements the function in sense (b), with at least $r$ replacements of the rule system on $T$. Whenever a replacement is chosen from the viable set $\mathcal{V}(e_{t+1})$ and members' preferences diverge over that set in the sense of Definition~\ref{def:political-power:rule-system}, the replacement is itself a selection among divergent preferences.
   311	\end{theorem}
   312	
   313	\begin{proof}
   314	The first statement is Lemma~\ref{lem:political-power:choice}. The second is Lemma~\ref{lem:political-power:change}. For the third, apply Lemma~\ref{lem:political-power:choice} to the choice of $R_{t+1}$ from $\mathcal{V}(e_{t+1})$, treating the choice of a rule system as a collective decision.
   315	\end{proof}
   316	
   317	The proofs are short because the work is done by the assumptions. This is the correct place for the work to be done. The theorem asserts that an activity must occur, not that an institution must exist. It would be false if a persistent collective could make its binding choices without any practice that selects among divergent preferences, or if it could survive incompatible environments without changing its rules. Each of these is an empirical possibility that the hard cases below test.
   318	
   319	\subsection{Scope of the lemma}
   320	
   321	The theorem makes $\pP$ a thin predicate, and a thin predicate invites the charge of vacuity. If anything that happens counts as rule making, the necessity claim is empty. Three things are excluded.
   322	
   323	A collective decision made by a fixed external rule (a lottery imposed by an outside authority, or a decision by the environment itself, such as a drought that forces a move) is excluded by the self-government clause. A rule change that is purely exogenous, such as the imposition of colonial law on a subject people, is excluded for the same reason and relocates the rule maker rather than eliminating it. Most importantly, the predicate excludes a group whose rules never change while the environment does. The falsifier of the theorem is therefore specific: a long-lived group, satisfying the plurality assumption, whose rules never changed and could not be changed by any of its members, through a sequence of environments that no single rule system could survive.
   324	
   325	The theorem says nothing about how rule making is distributed, how it is legitimated, or whether it is accountable. Corollary~\ref{cor:political-power:any-h} shows that the same function can be performed with concentration anywhere from $1/n$ to $1$.
   326	
   327	\subsection{Minimal form in stateless and consensus societies}
   328	
   329	The societies most often cited as lacking government are the test set for the theorem. If rule making is necessary, each should show it in some informal, distributed form. If any shows no rule-making activity at all, the theorem is in trouble.
   330	
   331	Among the Ju/'hoansi of the Kalahari, camp-level decisions about movement, sharing, and conflict are reached through extended public talk in which adults participate and no one has authority to command \citep{lee2013}. Wiessner's analysis of recorded conversations shows that much of this talk consists of criticism and joking directed at people who violate norms of sharing and modesty \citep{wiessner2005}. When disagreement cannot be resolved, people move to another camp. Fission is a rule-change practice of a particular kind: it does not change the rules of the existing group but creates a new group whose rules differ.
   332	
   333	Evans-Pritchard described the Nuer as an ``ordered anarchy'' with no government in the sense of a political authority able to command \citep{evanspritchard1940}. Their political order rested on the balanced opposition of lineage segments. Rules about bridewealth, compensation, and the use of grazing were maintained and adjusted through negotiation among kin groups, through the settlements of disputes, and through the influence of persons whose standing rested on persuasion rather than command. The leopard-skin chief who mediated in cases of homicide belongs to the interpretive pillar and is treated in Part III.
   334	
   335	Clastres argued from Amazonian ethnography that the chief in many lowland South American societies had no power to command, that his speech was an obligation rather than an instrument of rule, and that a chief who tried to give orders would be abandoned \citep{clastres1987}. Clastres's thesis is that such societies actively prevent political power from separating from the group. The thesis is consistent with the necessity theorem. Decisions are still made, by the group, and the chief's oratory is part of how they are made.
   336	
   337	Boehm's survey of foraging societies found a reverse dominance hierarchy: the adult members, acting as a coalition, suppress any individual who tries to dominate, using ridicule, disobedience, ostracism, and in extreme cases killing \citep{boehm1999}. Boehm emphasizes that egalitarianism of this kind is a political achievement. The group decides collectively and enforces the decision against would-be leaders. Woodburn reached a compatible conclusion for immediate-return societies such as the Hadza: their equality is produced by institutions of leveling that prevent the accumulation of power and property \citep{woodburn1982}.
   338	
   339	Ostrom's study of long-lived common-pool resource institutions supplies a different kind of case: small communities that govern a shared resource without a state and without private property \citep{ostrom1990}. Among the design principles she identified is that most individuals affected by the operational rules can participate in modifying them. The principle is a rule-making arrangement in the exact sense of Definition~\ref{def:political-power:rule-making}(b). Reviews of later case studies have found broad support for the principles \citep{cox2010}, and Ostrom's later work describes how such arrangements nest within larger polycentric systems \citep{ostromdesign2010}.
   340	
   341	\begin{proposition}[Minimal form of rule making]
   342	\label{prop:political-power:minimal-form}
   343	Let $N_a\subseteq N$ be the adult members of a group, $|N_a|=n_a\ge2$, and let the group make collective decisions by consensus, modeled as unanimity among the adults (a proposal wins exactly when every member of $N_a$ assents), with the status quo $q$ as default. Let each adult $i$ have a strict linear order $\succ_i$ over alternatives and assent to a proposal $x$ against $q$ if and only if $x\succ_i q$. Then:
   344	\begin{enumerate}[label=(\alph*)]
   345	\item the de jure concentration of rule making is $H^{\pP}=1/n_a$, the minimum possible for a procedure in which only adults' consent counts, and the minimum for the whole group when $N_a=N$;
   346	\item the set of alternatives that can replace $q$ is the set of strict Pareto improvements for the adults, $\{x: x\succ_i q \text{ for all } i\in N_a\}$, which is empty whenever $q$ is Pareto optimal among them;
   347	\item let the group be able to split, with each subgroup $N_1\subseteq N_a$ of at least two adults deciding by consensus for itself. A subgroup can replace $q$ if and only if all its members strictly prefer a common alternative $x$ to $q$, so some subgroup can do so if and only if at least two adults strictly prefer a common alternative to $q$. This condition can hold when $q$ is Pareto optimal among all adults.
   348	\end{enumerate}
   349	\end{proposition}
   350	
   351	\begin{proof}
   352	(a) The procedure is the unanimity game on $K=N_a$, so Proposition~\ref{prop:political-power:concentration}(d) gives $\varphi_i=1/n_a$ for adults, $\varphi_i=0$ for others, and $H^{\pP}=1/n_a$. Any procedure in which only adults can be the pivot has shares summing to one over $N_a$, so Proposition~\ref{prop:political-power:concentration}(b) applied to $N_a$ shows that $1/n_a$ is the minimum. (b) Under unanimity an alternative replaces $q$ only if every adult prefers it to $q$, which is the definition of a strict Pareto improvement among the adults. If $q$ is Pareto optimal among them, no alternative is strictly preferred to $q$ by every adult, so the set is empty. (c) Apply (b) to $N_1$: its consensus winset is $\{x: x\succ_i q\text{ for all }i\in N_1\}$, which is nonempty exactly when its members share an alternative they all prefer to $q$. If two adults $i,j$ both prefer some $x$ to $q$, the subgroup $\{i,j\}$ qualifies; conversely any qualifying subgroup contains two such adults. For the last claim, take three adults with $x\succ_1 q$, $x\succ_2 q$, and $q\succ_3 y$ for every $y\neq q$: then $q$ is Pareto optimal among all three, yet $\{1,2\}$ can adopt $x$.
   353	\end{proof}
   354	
   355	The proposition gives a formal reason for an ethnographic regularity. Consensus produces the least concentrated rule making possible, and it also produces the most status-quo-biased rule making possible, because every adult is a veto player. A consensus society facing a changing environment therefore needs another way to change its rules when no change is a Pareto improvement. Fission supplies it. The pairing of consensus decision making with cheap exit, documented among the Ju/'hoansi and in Woodburn's immediate-return societies, is what Proposition~\ref{prop:political-power:minimal-form} predicts. In the vocabulary of Definition~\ref{def:political-power:qp}, such groups combine minimal concentration with very high exit and entry components of contestability.
   356	
   357	Formal consensus sets only a lower bound on the concentration of rule making in these societies. Even where every adult can block a decision, differences in age, gender, skill, and kinship give some speakers more weight in discussion than others, so actual concentration exceeds the de jure figure $1/n_a$. The equal-share coding describes the procedure, not the distribution of influence within it.
   358	
   359	Across the ethnographic and historical record, collective decisions are made and rules change, while the concentration of rule making varies. Graeber and Wengrow argue that prehistoric societies moved deliberately between egalitarian and hierarchical arrangements, sometimes by season \citep{graeber2021}. Scott describes upland peoples of Southeast Asia who kept rule making dispersed to avoid incorporation by lowland states \citep{scott2009}, and early states in which it became concentrated \citep{scott2017}. Both readings are disputed, and the record itself overrepresents groups observed in the nineteenth and twentieth centuries, many in marginal environments and in contact with states, among foragers who vary widely \citep{kelly1995}. None of these qualifications touches the pattern that matters here: what varies is who makes the rules, not whether they are made.
   360	
   361	\subsection{Custom without legislators}
   362	
   363	The strongest objection to the theorem is not a stateless society but an argument about how rules come into being. Hayek distinguished law that grows out of practice, discovered and articulated rather than made, from legislation deliberately enacted by an authority, and he argued that much of the order of a society rests on the former \citep{hayek1973}. Ellickson's study of cattle ranchers in Shasta County, California, showed that neighbors settled trespass disputes by informal norms that diverged from the formal law and that the norms adjusted over time without recourse to it \citep{ellickson1991}. If rules can evolve without anyone making them, the rule-making function may be unnecessary.
   364	
   365	The objection narrows the theorem but does not defeat it. The theorem requires a practice that selects collective decisions and replaces rules, not a legislator. Evolved custom changes through practices: some members deviate, others imitate or sanction the deviation, and social pressure settles on a new regularity. Ellickson's ranchers are rule makers in this distributed sense. The norms change because particular neighbors propose, test, and enforce new expectations through gossip, reciprocity, and occasional self-help. The function is performed; the office is absent.
   366	
   367	The objection still shows something important. Under customary rule change, the rule-making profile of Definition~\ref{def:political-power:rule-making} is diffuse and difficult to observe, and control shares cannot be read from a written procedure. The power-index baseline does not apply, and concentration must be estimated from who in fact initiates and enforces changes. This is a measurement limitation of the paper's framework, not a counterexample to the theorem.
   368	
   369	\subsection{Functional explanation and its limits}
   370	
   371	The theorem is a statement about the conditions under which a collective persists. It is not a functional explanation of why any particular rule-making institution exists. Hempel showed that an inference from the need for a function to the presence of a particular institution commits the fallacy of affirming the consequent, because functional equivalents can meet the same need \citep{hempel1959}. Elster argued that explaining an institution by its beneficial consequences requires a feedback mechanism through which the consequences maintain the institution \citep{elster1983}. The theorem respects both constraints. It claims the necessity of an activity, it allows any institution or none to perform it, and it does not explain the existence of the Parlement of Paris, the Politburo, or the Majles by their contribution to the persistence of their polities. Those institutions have histories, and the comparative section treats them as historical products whose relation to the function is a matter of evidence.
   372	
   373	\section{Literature on rule-making power}
   374	\label{sec:literature}
   375	
   376	\subsection{Elite, pluralist and structural theories}
   377	
   378	The oldest question about rule making is whether a minority always makes the rules. Mosca held that in every society an organized minority rules an unorganized majority, and that the minority's advantage lies in its organization rather than in its numbers \citep{mosca1939}. Michels drew the same conclusion from the internal life of the German Social Democratic Party: organization requires delegation, delegation creates leaders with expertise and control of communication, and leaders entrench themselves even in organizations committed to democracy \citep{michels1915}. Mills extended the elite argument to the postwar United States, describing an interlocking set of corporate, military, and political leaders \citep{mills1956}.
   379	
   380	Pluralists denied that the elite claim had been demonstrated. Dahl's study of New Haven found that different actors prevailed in different issue areas and that no single group controlled decisions across them \citep{dahl1961}. His later account of polyarchy defined democracy by two dimensions, the inclusiveness of participation and the extent of public contestation \citep{dahl1971}. These two dimensions anticipate the separation in this paper between the distribution of rule-making shares and the contestability of rule making.
   381	
   382	A third position holds that rule makers need not be controlled by a class to serve it. Lindblom argued that business occupies a privileged position in market societies because governments depend on business investment for economic performance, so that rule makers anticipate business reactions without being directed \citep{lindblom1977}. Winters defined oligarchy as the political use of concentrated wealth for wealth defense and showed that oligarchs can coexist with electoral democracy \citep{winters2011}. Structural arguments of this kind imply that integration between resource control and rule making, $C_{\pF\pP}$, can be high even when no capture link in the source's sense can be documented. They therefore pose a measurement problem for the framework that Part I examines in detail.
   383	
   384	The empirical debate has moved to policy responsiveness. Gilens and Page estimated, on a dataset of 1,779 policy questions, that the preferences of economic elites and organized business groups have substantial independent associations with policy outcomes in the United States while the preferences of average citizens have little \citep{gilens2014}. Bartels found that senators' votes were more responsive to affluent constituents than to poor ones \citep{bartels2008}. Branham, Soroka, and Wlezien found that the preferences of the affluent and the middle class usually coincide and that, when they diverge, the affluent prevail only modestly more often \citep{branham2017}. Elkjaer and Klitgaard review the comparative evidence on unequal responsiveness and its methods \citep{elkjaer2024}. The disagreement concerns the size and the generality of a bias, not its direction in the American case.
   385	
   386	\subsection{Faces of power and agenda control}
   387	
   388	Bachrach and Baratz argued that the pluralist method of studying observable decisions misses the power exercised by keeping issues off the agenda \citep{bachrach1962}. Lukes added a third dimension, the shaping of preferences so that conflicts of interest never surface as grievances \citep{lukes2005}. For rule making the second face is central and measurable in principle: a non-decision leaves traces in proposals that were drafted and never scheduled, in petitions that went unanswered, and in committee chairs who declined to act. The third face shades into the legitimation pillar and is left to Part IV.
   389	
   390	Culpepper's study of corporate control in Europe and Japan gives the agenda argument an empirical form. Business influence over the rules of corporate governance was greatest on issues of low public salience, where legislators relied on managers' expertise and the press paid little attention \citep{culpepper2010}. Hall and Deardorff model lobbying as a subsidy of information and labor given to legislators who already agree with the lobbyist \citep{hall2006}. On this view, organized interests shape rules mainly by shaping what allied legislators can do with limited time, not by changing their votes.
   391	
   392	\subsection{Rule making in autocracies}
   393	
   394	Theories of autocracy explain the survival of rulers by how they share rule-making power with a narrow group of insiders. In selectorate theory, leaders must retain a winning coalition drawn from a larger selectorate, and when that coalition is small they survive by supplying private goods to its members rather than public goods to all \citep{bdm2003}. Svolik locates the main threat to dictators among the elites who share power with them and shows how parties, legislatures, and rules of succession make that sharing credible \citep{svolik2012}. Gandhi and Przeworski and Magaloni reach compatible conclusions: nominally democratic institutions and ruling parties co-opt potential rivals and are associated with longer rule \citep{gandhi2007,magaloni2008}. Gerschewski adds legitimation and repression to co-optation as the supports of autocratic stability \citep{gerschewski2013}, which in the series' vocabulary brings the legitimation and enforcement pillars to the aid of rule makers. The regime classification of Geddes, Wright, and Frantz makes these claims testable across party, personalist, military, and monarchic autocracies \citep{geddes2014}.
   395	
   396	Hale describes post-Soviet politics as patronal: power runs through networks of personal reward and punishment, organized either as a single pyramid around one patron or as competing pyramids \citep{hale2014}. Levitsky and Way identify competitive authoritarian regimes in which elections are real but the field is uneven \citep{levitsky2010}. These categories matter for measurement because they describe regimes whose formal rule-making procedures are pluralistic and whose actual concentration is high.
   397	
   398	\subsection{Separation of powers and veto players}
   399	
   400	Montesquieu argued that liberty requires that the power to make law, the power to execute it, and the power to judge not be united in the same hands \citep{montesquieu1989}. Madison's defense of the proposed American constitution relied on the same idea in a different form: ``Ambition must be made to counteract ambition'' \citep{madison1788}. The constitutional design he defended gave each branch the means and the motive to resist encroachment by the others.
   401	
   402	Tsebelis generalized the idea. A veto player is an individual or collective actor whose agreement is required for a change of the status quo, and the set of policies that can replace the status quo shrinks as veto players are added or as their positions diverge \citep{tsebelis2002}. Lijphart contrasts majoritarian democracies, which concentrate rule making in the cabinet of a single-party majority, with consensus democracies that disperse it among coalition partners, two legislative chambers, federal units, and courts \citep{lijphart1999}. Linz argued that presidential systems, which give the executive and the legislature separate mandates, make conflicts between them harder to resolve \citep{linz1990}. Weingast showed that constitutional limits on rule makers are self-enforcing only when citizens can coordinate their reactions to transgressions \citep{weingast1997}.
   403	
   404	\subsection{Sources of rule-making authority}
   405	
   406	Weber classified legitimate domination as traditional, charismatic, or rational-legal according to the grounds on which subjects accept commands \citep{weber1978}. Each regime type in the comparison below claims rule-making authority on a different ground: divine right and dynastic tradition in the Catholic monarchies \citep{figgis1914,kantorowicz1957}, divine law administered by rulers and jurists in the Islamic states \citep{crone2004,lambton1981}, the historical mission of a vanguard party in the communist states \citep{kornai1992}, and popular sovereignty expressed in elections in the democracies \citep{dahl1971}. Bodin made the power to give law to all without the consent of others the first mark of sovereignty \citep{bodin1992}. Al-Mawardi set out the conditions under which an imam is validly appointed and the powers he may delegate to viziers, governors, and judges \citep{mawardi1996}. These are theories written from inside regimes, and they describe what rule makers claimed, not necessarily what they could do.
   407	
   408	\subsection{Relation to prior work}
   409	
   410	Three gaps in this literature motivate the present paper. The theories of democratic and autocratic rule making use different concepts, so comparisons across regime types tend to be either impressionistic or confined to a single dimension such as regime survival. The functional-prerequisite tradition in sociology asserted that every society must make collective decisions \citep{aberle1950,parsons1951} but did not separate the necessity of the function from the distribution of its control, and it was criticized for that reason. The source framework of the series \citep{largo2026hbs} supplies a common network vocabulary but merges rule making with adjudication and leaves the measurement of control shares open. This paper separates rule making from adjudication, gives control shares a de jure baseline in power indices, proves that necessity and concentration are logically independent for this pillar, and uses one set of questions for all six regime types.
   411	
   412	\section{Rule making across six regime types}
   413	\label{sec:regimes}
   414	
   415	\subsection{Comparative method}
   416	
   417	Each regime type is examined for the same five features: the institutions that hold the rule-making function, the concentration of control in the sense of $H^{\pP}$ and its contestability in the components of Definition~\ref{def:political-power:qp}, the strength of its coupling to the other five pillars, the arrangements that preserve accountability, and the documented capture episodes and effective checks. The answers are qualitative. Terms such as ``high'' or ``low'' concentration refer to the ordering implied by Proposition~\ref{prop:political-power:concentration} applied to the described procedure, adjusted for documented informal concentration, and they are not estimates of $H^{\pP}$ for any polity.
   418	
   419	The six types are analytical lenses, not mutually exclusive categories. A single country can be a market-capitalist society and a secular democracy at once, and the two lenses ask different questions of it. The market-capitalist lens examines how private economic resources reach rule making. The secular-democratic lens examines how rule making is distributed among elected officials, courts, independent bodies, and private institutions under a constitution. Islamic states and Catholic monarchies are treated as polities in which religious law or religious institutions supplied a source of political legitimacy, in particular historical states with large internal differences. Neither religion is treated as an essence, and no regime type is ranked above another.
   420	
   421	\subsection{Market-capitalist societies}
   422	
   423	In market-capitalist societies with electoral institutions, general rules are made by elected legislatures, by executives through decrees and regulations, and by administrative agencies under delegated authority. The United States, the most studied case, divides rule making among two legislative chambers, a president with a veto, federal agencies that issue regulations, and fifty states. The formal procedure has several veto players, so the de jure concentration of rule making is moderate, and its formal contestability is high on all five components of Definition~\ref{def:political-power:qp}.
   424	
   425	The question this lens asks is how private economic resources enter that procedure. The source framework describes a path from unequal private resources through advocacy and access to the specialized development of policy and the distribution of legal benefits \citep[Section~8]{largo2026hbs}. Several links in that path are documented. A randomized field experiment found that when a political organization revealed that attendees at requested meetings were campaign donors, congressional offices were more likely to arrange meetings with senior staff or the member \citep{kalla2016}. Lobbyists who had worked for a senator saw their lobbying revenue fall when that senator left office, which indicates that part of what they sold was access to a particular rule maker \citep{blanes2012}. Lobbyists also follow the legislators to whom they are connected when those legislators change committee assignments \citep{bertrand2014}. These findings concern access. They show privileged access, the first condition of a capture link, but they do not by themselves show that the access changed a rule.
   426	
   427	Evidence that access changes rules is weaker than the evidence of access itself, and it is contested. Gilens and Page's estimates \citep{gilens2014} are disputed by work that finds the preferences of affluent and middle-income citizens usually coincide \citep{branham2017}. A large study of lobbying on ninety-eight issues found that the status quo usually prevailed and that the resources of a side were a poor predictor of its success \citep{baumgartner2009}. Ansolabehere, de Figueiredo, and Snyder observed that campaign contributions are small relative to the value of the policies at stake, which is hard to reconcile with a market in which rules are bought \citep{ansolabehere2003}. The theory of economic regulation predicted that concentrated interests would capture the rules that govern them \citep{stigler1971}, and Peltzman generalized it to a regulator who balances the support of several groups \citep{peltzman1976}; Part I develops the capture literature \citep{long2026financial}.
   428	
   429	Rule making in this regime type is coupled most strongly to resource control. The coupling runs through the wealth-to-rules path described above and through the structural dependence of rule makers on investment that Lindblom described \citep{lindblom1977}. Hacker and Pierson argue that organized interests used this path to shift tax and regulatory rules toward the very wealthy over several decades \citep{hackerpierson2010}, and Culpepper's comparison of Europe and Japan shows that business influence is greatest when issues are technical and receive little public attention \citep{culpepper2010}. Coupling to interpretation is weaker by design: federal judges are appointed by the president with Senate confirmation, so no single coalition controls the appointment channel unless it holds both bodies.
   430	
   431	Elections, opposition rights, judicial review, disclosure rules, and competition among organized interests, which frequently lobby on opposite sides of the same question \citep{baumgartner2009}, keep this rule making contestable. The regime type thus combines moderate de jure concentration and high formal contestability with unequal practical access, and the open question is how much that access changes rules.
   432	
   433	\subsection{Communist party-states}
   434	
   435	In communist party-states, the ruling party makes the rules that matter and the state legislature ratifies them. In the Soviet Union the Politburo of the Central Committee decided major questions, the Central Committee apparatus prepared and supervised policy, party congresses ratified the line, and the Supreme Soviet enacted laws whose content had been determined elsewhere \citep{fainsod1953,hough1979}. Kornai treats the undivided power of the communist party as the defining feature of the classical socialist system, from which its economic institutions follow \citep{kornai1992}. The de jure concentration of rule making is high, and every component of contestability except transparency of some rule texts is low for actors outside the party.
   436	
   437	The appointment channel is the defining instrument. Party committees at each level held lists of posts, the nomenklatura, whose holders they appointed or approved, covering the leadership of ministries, enterprises, courts, newspapers, universities, and the armed forces \citep{hough1979}. In the notation of Definition~\ref{def:political-power:appointment-channel}, the party's appointment share $\alpha_{S,\ell}$ approached one in every pillar. Voslensky, a former Soviet official writing in emigration, described the nomenklatura as a ruling class \citep{voslensky1984}, and Djilas, a Yugoslav dissident, called the party bureaucracy a new class that held collective ownership through political control \citep{djilas1957}. Both accounts come from authors with strong political commitments and should be read alongside the institutional scholarship. Hough and Fainsod described a system of bureaucratic bargaining among ministries and regions, and Lane and Ross found significant divisions within the Soviet ruling elite of 1981 to 1991 \citep{lane1995}. These findings bear on the loyalty of appointees, a parameter formalized in Section~\ref{sec:mechanisms} (Proposition~\ref{prop:political-power:appointment-bound}): appointment by a single party does not guarantee that appointees act as one coalition.
   438	
   439	The People's Republic of China retains the Leninist structure with important changes. Shirk described the relation between the party's top leaders and the Central Committee as reciprocal accountability: leaders appoint the members of the committee that formally selects them \citep{shirk1993}. Landry showed how the party's control of the appointment and evaluation of local cadres allowed it to decentralize economic decisions without losing political control \citep{landry2008}. Minzner documented a turn after the early 2000s away from legal professionalization and toward mediation and political direction of the courts \citep{minzner2011}, which raises the coupling $C_{\pP\pJ}$.
   440	
   441	Coupling to the other pillars is high by design in all four pairs treated here: party direction of courts, of propaganda and education, of the security services, and of official trade unions organized under party leadership \citep{kornai1992}. Accountability operates mainly within the party, through collective leadership, factional bargaining, and rules of succession, which Svolik identifies as the institutions that make power sharing among elites credible \citep{svolik2012}. The documented checks are intra-elite. In 1964 the Soviet party leadership removed Khrushchev as first secretary through the Presidium and the Central Committee, a replacement of the top rule maker carried out entirely inside the party \citep{hough1979}. Svolik's cross-national evidence points the same way: most authoritarian leaders who lose office by nonconstitutional means are removed by regime insiders rather than by popular uprisings \citep{svolik2012}. The Soviet case also shows the limits of high integration: the party's control of every pillar did not prevent the divisions that Lane and Ross document or the collapse of the system at the end of the period they study.
   442	
   443	\subsection{Social democracy and democratic socialism}
   444	
   445	In social democracies, rules are made by parliaments in which strong programmatic parties compete, and many economic and social rules are negotiated with organized labor and employers before they reach parliament. Sweden is the standard case. The Social Democratic Workers' Party governed for most of the twentieth century, and its close tie to the national trade union confederation gave organized labor direct access to rule making \citep{esping1985}. Korpi's power-resources theory treats the strength of labor's organization as the main determinant of the redistributive content of rules in capitalist democracies \citep{korpi1983}. De jure concentration of rule making is moderate, because rule making requires parliamentary majorities and coalition partners, and contestability is high on every component.
   446	
   447	Corporatist bargaining is the first feature that distinguishes this regime type in the rule-making layer. Peak organizations of labor and capital take part in drafting rules about wages, working conditions, and social insurance, which raises the coupling $C_{\pP\pW}$ by design. Within the domains it covers, a tripartite bargain among the government, the labor confederation, and the employers' confederation is a unanimity procedure among three organs, so by Proposition~\ref{prop:political-power:concentration}(d) the organ-level concentration of rule making in those domains is $1/3$. The same arrangement creates a risk of closure: interests that are not organized into the peak associations, such as the unemployed or new categories of workers, may be excluded from rule making that formally includes all producers.
   448	
   449	The long tenure of a single party is the second feature. Prolonged dominance of rule making by one party in a competitive system is concentration over time, which the static index $H^{\pP}$ does not capture.
   450	
   451	Przeworski described the strategic dilemma of electoral socialism: to win majorities, workers' parties must appeal beyond the working class, and to govern a market economy they depend on the investment decisions of private owners \citep{przeworski1985}. Pontusson's study of investment politics in Sweden showed that proposals to extend collective control over investment met strong resistance from business and were scaled back \citep{pontusson1992}. In the series' vocabulary, the structural dependence of rule makers on capital constrained the rules that social-democratic majorities could make. Kitschelt traced how European social-democratic parties changed their programs as their electorates changed \citep{kitschelt1994}, and Berman argued that the social-democratic movement was defined by a belief in the primacy of political choice over market outcomes \citep{berman2006}.
   452	
   453	Accountability rests on competitive elections, which did remove social-democratic governments, on an independent civil service, and on the formal openness of the corporatist channels. Rothstein's study of Swedish labor-market and school policy argues that the bureaucratic design of implementation, not only legislative majorities, determined whether social-democratic reforms achieved their goals \citep{rothstein1996}. Huber and Stephens show that long periods of social-democratic government were associated with the expansion of welfare states and that the effects persisted after the parties lost office \citep{huber2001}. The documented check on concentration in this regime type is alternation in government combined with corporatist channels that remain open to opposing organized interests, and the documented risk is closure of rule making to the unorganized.
   454	
   455	\subsection{Islamic states}
   456	
   457	In polities that derived political legitimacy from Islamic law, the question of who makes the rules has had an answer that differs from the European cases in one structural respect. Much of the general law, the fiqh developed from the Quran and the Sunna, was elaborated by jurists who were not officials of the ruler. Crone and Hinds argue that the early caliphs claimed religious authority in their own right and that this authority passed over the first centuries of Islam to the scholars, the ulama \citep{crone1986}. Rulers continued to make rules in the domains of administration, taxation, and public order, but they did not control the content of the law in the way that Bodin attributed to the sovereign. Hallaq argues that the modern state, with its claim to a monopoly of legislation, cannot reproduce this moral and legal order \citep{hallaq2013}. The argument is contested; the difference in the distribution of rule-making shares that it identifies is not.
   458	
   459	Classical theory placed the imam, or caliph, at the head of the community. Al-Mawardi's treatise sets out the qualifications of the imam, the ways in which he is validly appointed, including selection by qualified electors, and the powers he may delegate \citep{mawardi1996}. Lambton and Crone describe a long gap between this theory and practice, in which military rulers held effective power while caliphs conferred legitimacy and jurists accommodated the arrangement \citep{lambton1981,crone2004}. The Ottoman Empire added a body of sultanic regulation, the qanun, alongside sharia. Imber's study of the sixteenth-century chief mufti Ebussuud shows a senior jurist harmonizing sultanic law with Hanafi jurisprudence, which places a religious official inside the rule-making process of the empire \citep{imber1997}. Barkey describes Ottoman rule as the brokered management of diverse intermediaries rather than direct command \citep{barkey2008}.
   460	
   461	Two modern states show how differently the legitimating source can be institutionalized. The constitution of the Islamic Republic of Iran, adopted in 1979 and revised in 1989, vests leadership of the community in a just and pious jurist in the absence of the Twelfth Imam, following Khomeini's doctrine of the guardianship of the jurist \citep{iranconst,khomeini1981}. The Leader is selected by an elected Assembly of Experts and sets the general policies of the state. Legislation passed by the elected Majles must be sent to the Guardian Council, whose jurists judge its compatibility with Islam, and disputes between the two bodies go to the Expediency Council \citep{iranconst,schirazi1997}. Rule making in Iran therefore combines electoral and appointed components, and its de jure concentration is moderate to high depending on how the Leader's appointment power is weighted. Factions and parallel institutions compete within this structure \citep{brumberg2001,buchta2000}.
   462	
   463	Saudi rule making is concentrated in form and fragmented in practice. The Basic Law of Governance of 1992 declares the system of government monarchical, states that the regime derives its power from the Quran and the Sunna, provides that laws are issued and amended by royal decree, and gives the King the power to dissolve and re-form the consultative council \citep{saudibasic}. The state rests on the alliance between the Al Saud and the religious establishment descended from the eighteenth-century Wahhabi movement \citep{commins2006,alrasheed2002}. Yet Hertog shows that rule making in the oil era was divided among princes, brokers, and bureaucratic fiefdoms rather than centralized \citep{hertog2010}.
   464	
   465	In both modern cases rule making is closely coupled to legitimation and interpretation, and each case has one further strong coupling. In Iran the coupling to enforcement runs through the Revolutionary Guards, whose economic and political role is debated \citep{alfoneh2013}. In Saudi Arabia the coupling to resource control runs through the allocation of oil rents \citep{gause1994}; whether oil revenue itself weakens accountability is disputed \citep{ross2001}.
   466	
   467	Whether religious jurists raised or lowered the contestability of rule making is the question on which the scholarship divides. Jurists with authority independent of rulers raised the oversight component, while jurists co-opted by rulers could lower the entry component by excluding rival law makers. Kuran attributes the economic divergence of the Middle East to particular institutions of Islamic law, and Kuru attributes authoritarianism and underdevelopment in Muslim-majority states to an alliance between the ulama and the state \citep{kuran2011,kuru2019}; Rubin explains the divergence instead by the terms on which rulers bargained with religious authorities for legitimacy \citep{rubin2017}. Doctrine permits both arrangements. Shia jurists have held positions ranging from political quietism to the activism of Khomeini's doctrine \citep{arjomand1988}, and Sunni theory accommodated military rulers alongside autonomous jurists \citep{lambton1981}.
   468	
   469	Checks on rule makers are documented throughout the type. In the classical period the jurists' authority over much of the law limited what rulers could legislate, Ottoman and Saudi rule rested on negotiation with intermediaries, and Iranian elections remain contested within the limits set by candidate screening. Religious legitimation also constrains the rulers who depend on it: militant challenges to the Saudi state show that religious actors can turn the ruler's own ground of legitimacy against the ruler \citep{hegghammer2010}.
   470	
   471	\subsection{Catholic monarchies}
   472	
   473	In the Catholic monarchies of early modern Europe, the king was in theory the source of law. Bodin made the power to legislate without the consent of others the mark of sovereignty \citep{bodin1992}, and Bossuet grounded royal authority in Scripture \citep{bossuet1990}. Kantorowicz traced the medieval idea that the king had a mortal natural body and an undying political body \citep{kantorowicz1957}, and Figgis described the theory of divine right as it developed in early modern Europe \citep{figgis1914}. In formal terms, rule making was concentrated in one person, close to the dictatorship case of Proposition~\ref{prop:political-power:concentration}(d).
   474	
   475	In practice, Catholic monarchs shared rule making with councils, estates, and courts that could delay or block royal decrees. Habsburg Spain was a composite monarchy whose kingdoms kept their own laws and representative assemblies, and royal government worked through separate councils for kingdoms and functions \citep{elliott1963}. When Olivares tried in the 1620s and 1630s to make the kingdoms share the costs of the monarchy's wars, the resistance contributed to the revolts of Catalonia and Portugal in 1640 \citep{elliott1963,elliott1984}, a documented check on what the crown could impose. In Bourbon France the Estates-General did not meet between 1614 and 1789, yet royal ordinances still had to be registered by the Parlements, which could remonstrate and delay unless the king overrode them in a formal session in person. Beik's study of Languedoc shows absolutism working through collaboration with provincial elites who shared in its revenues \citep{beik1985}, and Collins presents the French state as a negotiated structure with real limits \citep{collins1995}. The crown's reach was nonetheless real: Root shows royal rules on village finances reshaping relations between peasants and lords in Burgundy \citep{root1987}.
   476	
   477	The Papal States combined spiritual and temporal rule making in one office. The pope was elected by the cardinals, so the Papal States were an elective monarchy, and Prodi describes the early modern papacy as a single body with two souls, the head of the universal Church and the prince of a territorial state \citep{prodi1987}. Rule making in the Papal States was concentrated in the pope and the curial congregations, and the coupling between rule making and legitimation was complete by construction.
   478	
   479	Rule making in these monarchies was coupled to the other pillars through the Church and through office. Crowns controlled appointments to high Church office in their territories, which raised $C_{\pP\pI}$; the Gallican tradition in France asserted royal and episcopal liberties against Rome, and Van Kley traces how disputes over Jansenism drew the Parlements into conflict with both crown and papacy \citep{vankley1996}. Venality of judicial and financial offices coupled rule making to resource control and to interpretation, because offices were property that the crown sold and whose holders could resist the crown. Ertman classifies France and Spain as patrimonial absolutist states, in which office holding and fiscal administration were tied to private interests \citep{ertman1997}.
   480	

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '370,430p' papers/latex/political-power.tex | nl -ba -v 370" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   370	
   371	The theorem is a statement about the conditions under which a collective persists. It is not a functional explanation of why any particular rule-making institution exists. Hempel showed that an inference from the need for a function to the presence of a particular institution commits the fallacy of affirming the consequent, because functional equivalents can meet the same need \citep{hempel1959}. Elster argued that explaining an institution by its beneficial consequences requires a feedback mechanism through which the consequences maintain the institution \citep{elster1983}. The theorem respects both constraints. It claims the necessity of an activity, it allows any institution or none to perform it, and it does not explain the existence of the Parlement of Paris, the Politburo, or the Majles by their contribution to the persistence of their polities. Those institutions have histories, and the comparative section treats them as historical products whose relation to the function is a matter of evidence.
   372	
   373	\section{Literature on rule-making power}
   374	\label{sec:literature}
   375	
   376	\subsection{Elite, pluralist and structural theories}
   377	
   378	The oldest question about rule making is whether a minority always makes the rules. Mosca held that in every society an organized minority rules an unorganized majority, and that the minority's advantage lies in its organization rather than in its numbers \citep{mosca1939}. Michels drew the same conclusion from the internal life of the German Social Democratic Party: organization requires delegation, delegation creates leaders with expertise and control of communication, and leaders entrench themselves even in organizations committed to democracy \citep{michels1915}. Mills extended the elite argument to the postwar United States, describing an interlocking set of corporate, military, and political leaders \citep{mills1956}.
   379	
   380	Pluralists denied that the elite claim had been demonstrated. Dahl's study of New Haven found that different actors prevailed in different issue areas and that no single group controlled decisions across them \citep{dahl1961}. His later account of polyarchy defined democracy by two dimensions, the inclusiveness of participation and the extent of public contestation \citep{dahl1971}. These two dimensions anticipate the separation in this paper between the distribution of rule-making shares and the contestability of rule making.
   381	
   382	A third position holds that rule makers need not be controlled by a class to serve it. Lindblom argued that business occupies a privileged position in market societies because governments depend on business investment for economic performance, so that rule makers anticipate business reactions without being directed \citep{lindblom1977}. Winters defined oligarchy as the political use of concentrated wealth for wealth defense and showed that oligarchs can coexist with electoral democracy \citep{winters2011}. Structural arguments of this kind imply that integration between resource control and rule making, $C_{\pF\pP}$, can be high even when no capture link in the source's sense can be documented. They therefore pose a measurement problem for the framework that Part I examines in detail.
   383	
   384	The empirical debate has moved to policy responsiveness. Gilens and Page estimated, on a dataset of 1,779 policy questions, that the preferences of economic elites and organized business groups have substantial independent associations with policy outcomes in the United States while the preferences of average citizens have little \citep{gilens2014}. Bartels found that senators' votes were more responsive to affluent constituents than to poor ones \citep{bartels2008}. Branham, Soroka, and Wlezien found that the preferences of the affluent and the middle class usually coincide and that, when they diverge, the affluent prevail only modestly more often \citep{branham2017}. Elkjaer and Klitgaard review the comparative evidence on unequal responsiveness and its methods \citep{elkjaer2024}. The disagreement concerns the size and the generality of a bias, not its direction in the American case.
   385	
   386	\subsection{Faces of power and agenda control}
   387	
   388	Bachrach and Baratz argued that the pluralist method of studying observable decisions misses the power exercised by keeping issues off the agenda \citep{bachrach1962}. Lukes added a third dimension, the shaping of preferences so that conflicts of interest never surface as grievances \citep{lukes2005}. For rule making the second face is central and measurable in principle: a non-decision leaves traces in proposals that were drafted and never scheduled, in petitions that went unanswered, and in committee chairs who declined to act. The third face shades into the legitimation pillar and is left to Part IV.
   389	
   390	Culpepper's study of corporate control in Europe and Japan gives the agenda argument an empirical form. Business influence over the rules of corporate governance was greatest on issues of low public salience, where legislators relied on managers' expertise and the press paid little attention \citep{culpepper2010}. Hall and Deardorff model lobbying as a subsidy of information and labor given to legislators who already agree with the lobbyist \citep{hall2006}. On this view, organized interests shape rules mainly by shaping what allied legislators can do with limited time, not by changing their votes.
   391	
   392	\subsection{Rule making in autocracies}
   393	
   394	Theories of autocracy explain the survival of rulers by how they share rule-making power with a narrow group of insiders. In selectorate theory, leaders must retain a winning coalition drawn from a larger selectorate, and when that coalition is small they survive by supplying private goods to its members rather than public goods to all \citep{bdm2003}. Svolik locates the main threat to dictators among the elites who share power with them and shows how parties, legislatures, and rules of succession make that sharing credible \citep{svolik2012}. Gandhi and Przeworski and Magaloni reach compatible conclusions: nominally democratic institutions and ruling parties co-opt potential rivals and are associated with longer rule \citep{gandhi2007,magaloni2008}. Gerschewski adds legitimation and repression to co-optation as the supports of autocratic stability \citep{gerschewski2013}, which in the series' vocabulary brings the legitimation and enforcement pillars to the aid of rule makers. The regime classification of Geddes, Wright, and Frantz makes these claims testable across party, personalist, military, and monarchic autocracies \citep{geddes2014}.
   395	
   396	Hale describes post-Soviet politics as patronal: power runs through networks of personal reward and punishment, organized either as a single pyramid around one patron or as competing pyramids \citep{hale2014}. Levitsky and Way identify competitive authoritarian regimes in which elections are real but the field is uneven \citep{levitsky2010}. These categories matter for measurement because they describe regimes whose formal rule-making procedures are pluralistic and whose actual concentration is high.
   397	
   398	\subsection{Separation of powers and veto players}
   399	
   400	Montesquieu argued that liberty requires that the power to make law, the power to execute it, and the power to judge not be united in the same hands \citep{montesquieu1989}. Madison's defense of the proposed American constitution relied on the same idea in a different form: ``Ambition must be made to counteract ambition'' \citep{madison1788}. The constitutional design he defended gave each branch the means and the motive to resist encroachment by the others.
   401	
   402	Tsebelis generalized the idea. A veto player is an individual or collective actor whose agreement is required for a change of the status quo, and the set of policies that can replace the status quo shrinks as veto players are added or as their positions diverge \citep{tsebelis2002}. Lijphart contrasts majoritarian democracies, which concentrate rule making in the cabinet of a single-party majority, with consensus democracies that disperse it among coalition partners, two legislative chambers, federal units, and courts \citep{lijphart1999}. Linz argued that presidential systems, which give the executive and the legislature separate mandates, make conflicts between them harder to resolve \citep{linz1990}. Weingast showed that constitutional limits on rule makers are self-enforcing only when citizens can coordinate their reactions to transgressions \citep{weingast1997}.
   403	
   404	\subsection{Sources of rule-making authority}
   405	
   406	Weber classified legitimate domination as traditional, charismatic, or rational-legal according to the grounds on which subjects accept commands \citep{weber1978}. Each regime type in the comparison below claims rule-making authority on a different ground: divine right and dynastic tradition in the Catholic monarchies \citep{figgis1914,kantorowicz1957}, divine law administered by rulers and jurists in the Islamic states \citep{crone2004,lambton1981}, the historical mission of a vanguard party in the communist states \citep{kornai1992}, and popular sovereignty expressed in elections in the democracies \citep{dahl1971}. Bodin made the power to give law to all without the consent of others the first mark of sovereignty \citep{bodin1992}. Al-Mawardi set out the conditions under which an imam is validly appointed and the powers he may delegate to viziers, governors, and judges \citep{mawardi1996}. These are theories written from inside regimes, and they describe what rule makers claimed, not necessarily what they could do.
   407	
   408	\subsection{Relation to prior work}
   409	
   410	Three gaps in this literature motivate the present paper. The theories of democratic and autocratic rule making use different concepts, so comparisons across regime types tend to be either impressionistic or confined to a single dimension such as regime survival. The functional-prerequisite tradition in sociology asserted that every society must make collective decisions \citep{aberle1950,parsons1951} but did not separate the necessity of the function from the distribution of its control, and it was criticized for that reason. The source framework of the series \citep{largo2026hbs} supplies a common network vocabulary but merges rule making with adjudication and leaves the measurement of control shares open. This paper separates rule making from adjudication, gives control shares a de jure baseline in power indices, proves that necessity and concentration are logically independent for this pillar, and uses one set of questions for all six regime types.
   411	
   412	\section{Rule making across six regime types}
   413	\label{sec:regimes}
   414	
   415	\subsection{Comparative method}
   416	
   417	Each regime type is examined for the same five features: the institutions that hold the rule-making function, the concentration of control in the sense of $H^{\pP}$ and its contestability in the components of Definition~\ref{def:political-power:qp}, the strength of its coupling to the other five pillars, the arrangements that preserve accountability, and the documented capture episodes and effective checks. The answers are qualitative. Terms such as ``high'' or ``low'' concentration refer to the ordering implied by Proposition~\ref{prop:political-power:concentration} applied to the described procedure, adjusted for documented informal concentration, and they are not estimates of $H^{\pP}$ for any polity.
   418	
   419	The six types are analytical lenses, not mutually exclusive categories. A single country can be a market-capitalist society and a secular democracy at once, and the two lenses ask different questions of it. The market-capitalist lens examines how private economic resources reach rule making. The secular-democratic lens examines how rule making is distributed among elected officials, courts, independent bodies, and private institutions under a constitution. Islamic states and Catholic monarchies are treated as polities in which religious law or religious institutions supplied a source of political legitimacy, in particular historical states with large internal differences. Neither religion is treated as an essence, and no regime type is ranked above another.
   420	
   421	\subsection{Market-capitalist societies}
   422	
   423	In market-capitalist societies with electoral institutions, general rules are made by elected legislatures, by executives through decrees and regulations, and by administrative agencies under delegated authority. The United States, the most studied case, divides rule making among two legislative chambers, a president with a veto, federal agencies that issue regulations, and fifty states. The formal procedure has several veto players, so the de jure concentration of rule making is moderate, and its formal contestability is high on all five components of Definition~\ref{def:political-power:qp}.
   424	
   425	The question this lens asks is how private economic resources enter that procedure. The source framework describes a path from unequal private resources through advocacy and access to the specialized development of policy and the distribution of legal benefits \citep[Section~8]{largo2026hbs}. Several links in that path are documented. A randomized field experiment found that when a political organization revealed that attendees at requested meetings were campaign donors, congressional offices were more likely to arrange meetings with senior staff or the member \citep{kalla2016}. Lobbyists who had worked for a senator saw their lobbying revenue fall when that senator left office, which indicates that part of what they sold was access to a particular rule maker \citep{blanes2012}. Lobbyists also follow the legislators to whom they are connected when those legislators change committee assignments \citep{bertrand2014}. These findings concern access. They show privileged access, the first condition of a capture link, but they do not by themselves show that the access changed a rule.
   426	
   427	Evidence that access changes rules is weaker than the evidence of access itself, and it is contested. Gilens and Page's estimates \citep{gilens2014} are disputed by work that finds the preferences of affluent and middle-income citizens usually coincide \citep{branham2017}. A large study of lobbying on ninety-eight issues found that the status quo usually prevailed and that the resources of a side were a poor predictor of its success \citep{baumgartner2009}. Ansolabehere, de Figueiredo, and Snyder observed that campaign contributions are small relative to the value of the policies at stake, which is hard to reconcile with a market in which rules are bought \citep{ansolabehere2003}. The theory of economic regulation predicted that concentrated interests would capture the rules that govern them \citep{stigler1971}, and Peltzman generalized it to a regulator who balances the support of several groups \citep{peltzman1976}; Part I develops the capture literature \citep{long2026financial}.
   428	
   429	Rule making in this regime type is coupled most strongly to resource control. The coupling runs through the wealth-to-rules path described above and through the structural dependence of rule makers on investment that Lindblom described \citep{lindblom1977}. Hacker and Pierson argue that organized interests used this path to shift tax and regulatory rules toward the very wealthy over several decades \citep{hackerpierson2010}, and Culpepper's comparison of Europe and Japan shows that business influence is greatest when issues are technical and receive little public attention \citep{culpepper2010}. Coupling to interpretation is weaker by design: federal judges are appointed by the president with Senate confirmation, so no single coalition controls the appointment channel unless it holds both bodies.
   430	

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '481,720p' papers/latex/political-power.tex | nl -ba -v 481" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   481	Accountability did not take the form of replacement of rule makers, which the dynastic principle excluded, but of the corporate privileges of estates, towns, Parlements, and the Church, of the Church's autonomous canon law, and, in extreme cases, of revolt. The de jure concentration was high, and practical concentration was lower because of brokerage; contestability was low in replacement and entry and intermittently significant in oversight through the Parlements and estates.
   482	
   483	\subsection{Secular democracies}
   484	
   485	In secular democracies, the authority to make rules is derived from popular sovereignty and distributed by a constitution among elected legislatures, executives, courts with powers of review, independent agencies, subnational governments, and in some cases the voters directly. The distribution varies widely. Lijphart's comparison of thirty-six democracies distinguishes majoritarian systems, in which a single-party cabinet controls rule making between elections, from consensus systems that disperse it \citep{lijphart1999}. Federal systems add a territorial division, giving subnational governments rule-making authority that the national legislature cannot revoke by ordinary statute. Presidential systems add a division between an executive and a legislature with separate electoral mandates and fixed terms, which Linz argued makes conflicts between them harder to resolve \citep{linz1990}. Where constitutions provide for referendums and popular initiatives, the electorate itself becomes a veto player or an agenda setter in the rule-making procedure \citep{lijphart1999}. In the vocabulary of this paper, majoritarian systems have higher de jure concentration and fewer veto players; consensus systems have lower concentration and more veto players, and the trade-off between them is the subject of Proposition~\ref{prop:political-power:veto} in Section~\ref{sec:mechanisms}.
   486	
   487	Contestability is the defining property of this regime type. Dahl's polyarchy requires both inclusive participation and public contestation \citep{dahl1971}. Przeworski characterized democracy as a system in which parties can lose elections and accept the loss, so that outcomes are uncertain in advance \citep{przeworski1991}. The replacement component $q^{\mathrm{rep}}$ is therefore the component that distinguishes democracies from the other regime types most sharply. Data projects such as V-Dem measure it alongside legislative and judicial constraints on the executive and the freedom to form parties \citep{coppedge2011}, and the Regimes of the World classification uses these measures to separate liberal and electoral democracies from electoral and closed autocracies \citep{luhrmann2018}.
   488	
   489	Secular democracies have relocated part of rule making away from elected bodies. Constitutional courts in Europe shape legislation by reviewing it, and Stone Sweet shows that legislators anticipate review and draft accordingly \citep{stonesweet2000}. Hirschl argues that the transfer of power to courts in several democracies served elites who expected to lose control of legislatures \citep{hirschl2004}. Independent agencies and central banks make rules under delegated authority. Each of these relocations lowers the concentration of rule making in elected bodies and raises its concentration in bodies that are not removable by voters, and whether the result is more or less accountable depends on the oversight component, not on the relocation itself.
   490	
   491	The documented capture risk in this regime type is the erosion of contestability by elected rule makers. Levitsky and Way describe regimes that hold real elections while incumbents abuse state resources, media access, and legal harassment to tilt the field \citep{levitsky2010}. In such regimes the formal rule-making procedure is unchanged while the replacement and entry components of contestability fall. The documented checks are the ones Madison anticipated, rival institutions with the means and motive to resist \citep{madison1788}, together with the coordination of citizens against transgressions that Weingast identifies as the condition for constitutional limits to hold \citep{weingast1997}. Pettit's republican account treats the contestability of rule making by those subject to it as the core of freedom from domination \citep{pettit1997}, which supplies a normative ground for the measurement emphasis of Definition~\ref{def:political-power:qp}.
   492	
   493	\subsection{Comparative summary}
   494	
   495	Tables~\ref{tab:regimes-holders} and~\ref{tab:regimes-coupling} summarize the configuration of the rule-making pillar under each regime type and the coupling that the cited literature documents. Every regime type performs the function, which is what Theorem~\ref{thm:political-power:necessity} requires. Concentration and contestability vary independently of the source of legitimacy: rule making in Habsburg Spain was less concentrated in practice than its theory claimed, and rule making in some electoral regimes is more concentrated than their procedures suggest. The main channel of coupling differs by regime type, from wealth to rules in market economies to appointment in party-states and religious legitimation in the Islamic states and Catholic monarchies, which is the rule-making form of the source's proposition that control paths differ by regime \citep[Proposition~3]{largo2026hbs}.
   496	
   497	\begin{table}[tbp]
   498	\centering
   499	\small
   500	\caption{Holders, concentration, and contestability of rule making by regime type. Concentration and contestability are qualitative descriptions based on the cited literature, not coded values.}
   501	\label{tab:regimes-holders}
   502	\begin{tabularx}{\textwidth}{@{}L{2.5cm}YYY@{}}
   503	\toprule
   504	Regime type & Principal rule makers & Concentration of rule making & Contestability of rule making \\
   505	\midrule
   506	Market-capitalist & Elected legislatures, executives, and regulatory agencies, with organized interests shaping drafts & Moderate, with several veto players in the formal procedure & High in form, with unequal practical access by economic resources \\
   507	Communist party-state & Party leadership and apparatus, with the legislature ratifying & High, through the party's control of appointments in every pillar & Low outside the party and partial within it \\
   508	Social democracy & Parliamentary majorities negotiating with peak organizations of labor and capital & Moderate, with long tenure of a dominant party in some cases & High, with a risk of closure to unorganized interests \\
   509	Islamic states & Rulers and councils, with jurists holding authority over much of the law & Varies from dispersed classical arrangements to concentrated modern ones & Varies from contested elections in Iran to none in Saudi Arabia \\
   510	Catholic monarchies & Crown in council, with Parlements, Cortes, and estates able to delay or refuse & High in theory and lower in practice because of brokerage & Low for replacement and intermittent for oversight \\
   511	Secular democracies & Legislatures and executives under a constitution, with courts and agencies holding delegated parts & Low to moderate, depending on majoritarian or consensus design & High, and falling where incumbents tilt the electoral field \\
   512	\bottomrule
   513	\end{tabularx}
   514	\end{table}
   515	
   516	\begin{table}[tbp]
   517	\centering
   518	\small
   519	\caption{Coupling of rule making to other pillars, documented capture risks, and documented checks by regime type.}
   520	\label{tab:regimes-coupling}
   521	\begin{tabularx}{\textwidth}{@{}L{2.5cm}YYY@{}}
   522	\toprule
   523	Regime type & Strongest documented coupling & Documented capture risk & Documented check \\
   524	\midrule
   525	Market-capitalist & Resource control to rule making through donations, lobbying, and investment dependence & Privileged access of donors and connected lobbyists & Competing interest groups, elections, and the advantage of the status quo \\
   526	Communist party-state & Rule making to every other pillar through appointment lists & Integration of all pillars under one coalition & Factional bargaining and divisions within the elite \\
   527	Social democracy & Rule making to production through corporatist bargaining & Exclusion of unorganized groups from negotiated rules & Electoral alternation and open corporatist channels \\
   528	Islamic states & Rule making to legitimation and interpretation through religious-legal authority & Clerical vetting of legislation and candidates, and rent allocation & Independent juristic authority, elections in Iran, and brokered rule \\
   529	Catholic monarchies & Rule making to legitimation through royal control of Church appointments & Venality of office and dynastic exclusion of replacement & Corporate privileges, registration by Parlements, and revolt \\
   530	Secular democracies & Rule making to interpretation through appointments and constitutional review & Erosion of contestability by elected incumbents & Rival institutions and citizen coordination against transgression \\
   531	\bottomrule
   532	\end{tabularx}
   533	\end{table}
   534	
   535	\section{Mechanisms, failure modes and checks}
   536	\label{sec:mechanisms}
   537	
   538	The necessity theorem says that rule making occurs; Proposition B concerns the conditions under which it becomes concentrated, coupled to other pillars, and unaccountable. Each mechanism below is a comparative static under explicit assumptions, not a law of history, and each identifies the check that interrupts it, in line with the source's proposition that checks can interrupt the transmission of concentrated power \citep[Proposition~2]{largo2026hbs}.
   539	
   540	\subsection{Delegation and oligarchy}
   541	
   542	Michels argued that the leaders of large organizations escape the control of members because members lack the time, expertise, and information to monitor them \citep{michels1915}. Olson's analysis of collective action explains why: the benefit of monitoring is shared by all members, while its cost falls on the one who monitors \citep{olson1965}. A simple model makes the conditional character of the argument precise.
   543	
   544	\begin{assumption}[Monitoring game]
   545	\label{ass:political-power:monitoring}
   546	An organization has $n\ge2$ members and a leadership that extracts a rent $\rho>0$ from the organization in each period, at a cost of $\rho/n$ to each member. Each member chooses simultaneously whether to monitor the leadership at private cost $c>0$. Each monitor independently detects the extraction with probability $\delta\in(0,1]$, and detection leads to the replacement of the leadership. After replacement the rent is returned to the members, so each member recovers $\rho/n$. A member's payoff is the expected rent recovered by that member minus the member's own monitoring cost.
   547	\end{assumption}
   548	
   549	\begin{proposition}[Monitoring vanishes in large organizations]
   550	\label{prop:political-power:michels}
   551	Under Assumption~\ref{ass:political-power:monitoring}:
   552	\begin{enumerate}[label=(\alph*)]
   553	\item if $n>\rho\delta/c$, the unique Nash equilibrium is that no member monitors, and the leadership retains the rent with probability one;
   554	\item suppose instead that an organized opposition faction, distinct from the members, chooses simultaneously with them whether to monitor at cost $c$, detects the extraction independently with probability $\delta$ if it monitors, and takes office whenever the leadership is replaced, whoever detected the extraction. In office the faction keeps a share $\beta\in(0,1]$ of the rent, so each member recovers only $(1-\beta)\rho/n$, and the faction's payoff is $\beta\rho$ times the probability of replacement minus $c$ if it monitors. If $n>(1-\beta)\rho\delta/c$ and $\beta\rho\delta>c$, the unique Nash equilibrium is that no member monitors and the faction monitors, so the leadership is detected and replaced with probability $\delta$ whatever the value of $n$.
   555	\end{enumerate}
   556	\end{proposition}
   557	
   558	\begin{proof}
   559	(a) If $k$ other members monitor, the probability that none of them detects the extraction is $(1-\delta)^k$. A member who adds monitoring raises the detection probability by $\delta(1-\delta)^k$ and so gains $(\rho/n)\delta(1-\delta)^k$ in expected recovered rent. This gain is at most $(\rho/n)\delta$, which is less than $c$ when $n>\rho\delta/c$. Monitoring is therefore strictly dominated for every member, whatever the others do, and the unique equilibrium has no monitoring.
   560	
   561	(b) A member's gain from monitoring is now at most $(1-\beta)(\rho/n)\delta$, which is less than $c$ when $n>(1-\beta)\rho\delta/c$, so monitoring is strictly dominated for every member as in (a). In any equilibrium no member monitors, and the faction's gain from monitoring is then $\beta\rho\delta$, which exceeds $c$ and does not depend on $n$. The faction therefore monitors, and the equilibrium is unique because the members' choice is dominant.
   562	\end{proof}
   563	
   564	The threshold $n^\ast=\rho\delta/c$ rises with the size of the rent and the effectiveness of monitoring and falls with its cost. Part (a) is Michels's tendency stated as a conditional result. Part (b) identifies the check. An organized opposition with a private stake in winning office converts the public good of oversight into a private incentive, and it does so even though it lowers the members' own incentive to monitor. Lipset, Trow, and Coleman's study of the International Typographical Union found exactly such an arrangement, a durable two-party system inside a union, and it is the classic exception to Michels's law \citep{lipset1956}. Voss and Sherman documented later cases in which American union locals reversed oligarchic tendencies \citep{voss2000}, and Cassinelli offered an early analytic critique of the law \citep{cassinelli1953}. Schumpeter's competitive theory of democracy rests on the same mechanism at the scale of a polity: rival teams of leaders compete for the vote and monitor one another \citep{schumpeter1942}.
   565	
   566	The model omits much. Leaders can raise the cost of monitoring by controlling information, which is Michels's own emphasis, and members may value leaders for reasons other than rent. The proposition shows only that oligarchy follows from size under one set of conditions and that a specific institutional change reverses it. That is enough to treat oligarchization as a conditional tendency, which is the role the series assigns it in the argument for Proposition B (Part VII), rather than as a necessity.
   567	
   568	\subsection{Veto players and the status quo}
   569	
   570	Adding veto players is the standard constitutional remedy for concentrated rule making. It has a cost that the comparison of majoritarian and consensus democracies brings out, and a simple result shows why the cost is unavoidable.
   571	
   572	\begin{definition}[Winset]
   573	\label{def:political-power:veto-players}
   574	Let $X$ be a set of alternatives, $q\in X$ the status quo, and $K$ a nonempty set of veto players, each with strict preferences $\succ_i$ on $X$. The \emph{winset} of $q$ is $W_K(q)=\{x\in X: x\succ_i q\text{ for all }i\in K\}$, the set of alternatives that every veto player prefers to the status quo \citep{tsebelis2002}. A \emph{pure veto-player procedure} enacts $x$ against $q$ exactly when $x\in W_K(q)$; it is the unanimity game on $K$ of Proposition~\ref{prop:political-power:concentration}(d). In a general simple game membership in $W_K(q)$ is necessary for replacing $q$ but not sufficient.
   575	\end{definition}
   576	
   577	\begin{proposition}[Veto players protect the status quo]
   578	\label{prop:political-power:veto}
   579	\leavevmode
   580	\begin{enumerate}[label=(\alph*)]
   581	\item If $K\subseteq K'$, then $W_{K'}(q)\subseteq W_K(q)$.
   582	\item If some $i\in K$ prefers $q$ to every other alternative, then $W_K(q)=\emptyset$.
   583	\item Let $q$ be a preferential rule, one that every member of a group $B$ prefers to every other alternative, and let $x\neq q$ be a reform that every member of $K\setminus B$ prefers to $q$. Under a pure veto-player procedure, $x$ can replace $q$ if and only if $K\cap B=\emptyset$.
   584	\end{enumerate}
   585	\end{proposition}
   586	
   587	\begin{proof}
   588	(a) An alternative in $W_{K'}(q)$ is preferred to $q$ by every member of $K'$, and so by every member of $K$. (b) If $i\in K$ prefers $q$ to every $x\neq q$, no $x$ is preferred to $q$ by $i$, so no $x$ lies in $W_K(q)$. (c) If $K\cap B=\emptyset$, every member of $K$ prefers $x$ to $q$, so $x\in W_K(q)$. If some $i\in K\cap B$, then $i$ prefers $q$ to $x$, so $x\notin W_K(q)$.
   589	\end{proof}
   590	
   591	Part (c) contains the trade-off. A preferential rule survives any reform whenever one of its beneficiaries holds a veto. Adding veto players protects the polity against new preferential rules, because a new rule must pass every veto player, and it protects existing preferential rules, because their repeal must also pass every veto player. Part (a) states the general form: the set of possible changes can only shrink as veto players are added. This is why the hypothesis HP7 in Section~\ref{sec:measurement} predicts that the number of effective veto players is associated both with the persistence of preferential rules and with low responsiveness. The same logic explains the status-quo bias of consensus societies in Proposition~\ref{prop:political-power:minimal-form}, where every adult holds a veto.
   592	
   593	The check implied by the proposition is not more veto players but the control of who holds them. A veto held by an independent body with no stake in a preferential rule, such as a court reviewing a statute against a general constitutional standard, constrains new preferential rules without protecting old ones, provided the body cannot itself be captured. That condition is the subject of Part III.
   594	
   595	\subsection{The appointment channel}
   596	
   597	The source framework defines cross-pillar integration $C_{mn}$ only descriptively, as the extent to which one coalition commands appointments, budgets, sanctions, or agenda in two pillars \citep{largo2026hbs}, and Part VII fixes a formal definition for the series. The appointment channel acquires testable content under one explicit candidate, the coalition-overlap measure. Let $\mathcal{S}$ be a preregistered list of coherent coalitions, groups such as parties, factions, or dynasties that can issue joint directives. For $S\in\mathcal{S}$ let $s^{\pP}(S)$ be the Shapley-Shubik share of the bloc player $p_S$ in the quotient game on $N_S=(N\setminus S)\cup\{p_S\}$, whose winning coalitions are defined for $T\subseteq N\setminus S$ by $T\in\Win_S$ if and only if $T\in\Win$, and $T\cup\{p_S\}\in\Win_S$ if and only if $T\cup S\in\Win$. This bloc share is not in general the sum of the members' separate shares; in the Iranian example of Table~\ref{tab:examples} the two councils hold $1/6+1/6$ separately and $1/2$ as a bloc. Let $\kappa_\ell(S)\in[0,1]$ be the share of decision-relevant control in pillar $\ell$ that is exercised in accordance with the directives of $S$, and set
   598	\begin{equation}
   599	C^{\mathrm{ov}}_{\pP\ell}=\max_{S\in\mathcal{S}}\min\{s^{\pP}(S),\kappa_\ell(S)\}.
   600	\label{eq:overlap}
   601	\end{equation}
   602	The candidate lies in $[0,1]$, equals one when a single coalition holds all rule-making control and commands all of pillar $\ell$, and equals zero when no listed coalition has a positive share in both.
   603	
   604	\begin{proposition}[Appointment bounds on integration]
   605	\label{prop:political-power:appointment-bound}
   606	For a coalition $S$ and an office $o$ let $f_{S,o}\in[0,1]$ be the share of the holder's decisions that follow the directives of $S$. For $S\in\mathcal{S}$ with $\alpha_{S,\ell}>0$ define the loyalty of its appointees as the conditional average
   607	\[
   608	\lambda_S=\frac{1}{\alpha_{S,\ell}}\sum_{o\in O_\ell}w_o f_{S,o}\,\mathbf{1}[S\text{ can unilaterally appoint or remove the holder of }o],
   609	\]
   610	and set $\lambda_S=0$ when $\alpha_{S,\ell}=0$. Suppose that command in pillar $\ell$ decomposes as $\kappa_\ell(S)=\lambda_S\alpha_{S,\ell}+\gamma_S$, where $\gamma_S\in[0,1-\lambda_S\alpha_{S,\ell}]$ is command exercised through channels other than appointment, such as budgets, sanctions, and informal patronage. Then:
   611	\begin{enumerate}[label=(\alph*)]
   612	\item for every $S\in\mathcal{S}$, $C^{\mathrm{ov}}_{\pP\ell}\ge\min\{s^{\pP}(S),\lambda_S\alpha_{S,\ell}\}$;
   613	\item if command runs only through appointment ($\gamma_S=0$ for all $S$) and loyalty is at most $\bar\lambda$ ($\lambda_S\le\bar\lambda$ for all $S$), then $C^{\mathrm{ov}}_{\pP\ell}\le\bar\lambda\max_{S\in\mathcal{S}}\alpha_{S,\ell}$;
   614	\item if command runs only through appointment and no listed coalition can unilaterally appoint or remove the holder of any office in $O_\ell$, for example because both appointment and removal require the consent of two bodies controlled by different coalitions, then $C^{\mathrm{ov}}_{\pP\ell}=0$.
   615	\end{enumerate}
   616	\end{proposition}
   617	
   618	\begin{proof}
   619	(a) By Equation~\eqref{eq:overlap}, $C^{\mathrm{ov}}_{\pP\ell}\ge\min\{s^{\pP}(S),\kappa_\ell(S)\}$. Since $\gamma_S\ge0$, $\kappa_\ell(S)\ge\lambda_S\alpha_{S,\ell}$, and the minimum is nondecreasing in each argument. (b) For every $S$, $\min\{s^{\pP}(S),\kappa_\ell(S)\}\le\kappa_\ell(S)=\lambda_S\alpha_{S,\ell}\le\bar\lambda\max_{S'}\alpha_{S',\ell}$; take the maximum over $S$. (c) The hypothesis gives $\alpha_{S,\ell}=0$ for every $S\in\mathcal{S}$ by Definition~\ref{def:political-power:appointment-channel}, and (b) gives $C^{\mathrm{ov}}_{\pP\ell}\le0$.
   620	\end{proof}
   621	
   622	The proposition separates three quantities that comparative accounts often run together. The rule-making share $s^{\pP}(S)$ says how much of rule making the coalition controls. The appointment share $\alpha_{S,\ell}$ says how many posts in another pillar it fills. The loyalty parameter $\lambda_S$ says how far the people it appoints do what it wants. Nomenklatura systems maximize the first two, and part (a) then makes integration high unless loyalty is low. The Soviet evidence of elite divisions \citep{lane1995} and of bureaucratic bargaining \citep{hough1979} concerns loyalty, and so it limits the integration that appointment alone can produce. Parts (b) and (c) identify the check. Requiring the consent of a second body for both appointment and removal closes the appointment channel to any single coalition, and security of tenure lowers loyalty after appointment by removing the threat of dismissal. Under plural appointment any remaining integration must run through budgets, sanctions, or patronage ($\gamma_S$), which tells an investigator where to look.
   623	
   624	\subsection{Agenda control and quiet politics}
   625	
   626	The three propositions concern visible procedures. A fourth mechanism operates through what never reaches a procedure. An actor with agenda control can keep a reform off the agenda without casting a vote, and no power index computed from the formal procedure will register the effect (Definition~\ref{def:political-power:agenda-control}). The evidence for this mechanism comes from studies of low-salience rule making, where business influence over the rules of corporate governance was greatest when issues were technical and public attention was low \citep{culpepper2010}, and from accounts of lobbying as a subsidy that extends the capacity of allied legislators \citep{hall2006}.
   627	
   628	Agenda control fails as a mechanism of capture when the transparency and entry components of contestability are high. Publication of drafts and of the record of who proposed what makes non-decisions visible, and free entry into rule-making competition allows excluded interests to place their proposals on the agenda through other actors. The source framework's redesign proposals include lobbying registers and the disclosure of contacts between rule makers and interested parties for this reason \citep[Section~11]{largo2026hbs}.
   629	
   630	\subsection{Checks}
   631	
   632	The four mechanisms share a structure. In each, rule making drifts toward capture when one component of contestability is weak: oversight in the monitoring game, the identity of veto holders in the veto game, independence of appointees in the appointment channel, and transparency in agenda control. The corresponding checks are organized opposition, vetoes held by actors without a stake in the rule, plural appointment and security of tenure, and publicity. None of these checks removes the rule-making function, and none requires that it be dispersed to the point of the consensus society, whose own status-quo bias Proposition~\ref{prop:political-power:minimal-form} describes. The checks act on contestability, not on the existence of rule makers, which is the rule-making form of the series' central distinction between Proposition A and Proposition B.
   633	
   634	\section{Measurement and hypotheses}
   635	\label{sec:measurement}
   636	
   637	\subsection{Indicators}
   638	
   639	Table~\ref{tab:indicators} lists indicators for the constructs of this paper. Each indicator can be coded from documentary sources, and each has a known weakness. The table follows the source framework's requirement that measurement precede accusation and that the population of coded events include ordinary rule making, not only scandals \citep[Appendix~B]{largo2026hbs}.
   640	
   641	\begin{table}[tbp]
   642	\centering
   643	\small
   644	\caption{Indicators for the constructs of the rule-making layer, with the main weakness of each.}
   645	\label{tab:indicators}
   646	\begin{tabularx}{\textwidth}{@{}L{2.6cm}YY@{}}
   647	\toprule
   648	Construct & Indicator & Main weakness \\
   649	\midrule
   650	De jure control shares & Shapley-Shubik shares computed from the written or customary decision procedure & Ignores agenda setting and informal influence \\
   651	De facto control shares & Shares of contested decisions in which each actor's position prevails, and survival of each actor's provisions through amendment and veto bargaining & Success can reflect anticipation of others' positions rather than control \\
   652	Agenda origin & Shares of enacted rules by originating actor, from legislative records and decree registers & Initiation is a different power from enactment \\
   653	Concentration $H^{\pP}$ & Sum of squared shares from either of the two indicators above & Sensitive to the definition of actors as individuals or groups \\
   654	Replacement $q^{\mathrm{rep}}$ & Frequency of peaceful turnover of rule makers through elections or regular succession & Turnover can occur within a closed coalition \\
   655	Oversight $q^{\mathrm{ovs}}$ & Indices of legislative and judicial constraints on the executive & Formal powers may not be used \\
   656	Entry $q^{\mathrm{ent}}$ & Legal and practical freedom to form parties, stand for office, and petition & Practical barriers are hard to code \\
   657	Transparency $q^{\mathrm{trn}}$ & Publication of drafts, consultation records, and lobbying registers & Disclosure can be formal and incomplete \\
   658	Exit $q^{\mathrm{ext}}$ & Legal and economic cost of leaving the jurisdiction or the group & Exit can substitute for voice and weaken reform \\
   659	Appointment share $\alpha_{S,\ell}$ & Share of weighted posts in pillar $\ell$ that a coalition fills without the consent of another body & Requires a list of posts and weights fixed in advance \\
   660	Veto players & Number of actors whose consent is required to change a statute & Partisan alignment can merge formally separate veto players \\
   661	\bottomrule
   662	\end{tabularx}
   663	\end{table}
   664	
   665	\subsection{Hypotheses with falsifiers}
   666	
   667	Each hypothesis below refines one of three general hypotheses in the source framework \citep[Section~9]{largo2026hbs}: that benefits concentrated among connected actors go with weaker chances of challenge (H1), that groups controlling appointments, funds, and sanctions across several domains keep preferential rules after exposure (H2), and that appointment chains explain allocation in one-party sectors better than private capital does (H3). Each names its parent and the observation that would count against it.
   668	
   669	\begin{description}[font=\normalfont\itshape, leftmargin=1.5em, style=nextline]
   670	\item[HP1, appointment channel.] In party-state regimes, the share of key economic, judicial, media, and security posts filled from party appointment lists predicts the integration of rule making with those pillars. In secular democracies, where appointment to such posts requires confirmation by a second body or is governed by civil-service rules, the same pairwise integrations are lower. Parent: H3. Falsifier: equal integration across regimes with different appointment rules, after controlling for the loyalty of appointees.
   671	\item[HP2, institutionalized power sharing.] Autocracies with functioning ruling parties or legislatures that share rule making have longer-lived leaders \citep{gandhi2007,magaloni2008}. Parent: H2. Falsifier: no difference in leader survival once resource rents are controlled.
   672	\item[HP3, conditional oligarchy.] Leadership turnover in membership organizations is lower where monitoring is costly, and higher where an organized internal opposition exists, as Proposition~\ref{prop:political-power:michels} predicts. Parent: H1. Falsifier: turnover unrelated to measured monitoring costs or to the presence of an organized opposition.
   673	\item[HP4, selectorate.] Smaller winning coalitions relative to the selectorate predict a higher share of private goods in public spending \citep{bdm2003}. Parent: H1. Falsifier: no association, or the reverse association.
   674	\item[HP5, religious-political bargaining.] Where rulers depend on religious legitimation, they grant religious authorities autonomy in law and education in return for support. Rubin and Kuru predict different consequences of this bargain \citep{rubin2017,kuru2019}, and both predictions should be tested. Parent: H2. Falsifier: religious autonomy that does not vary with rulers' dependence on religious legitimation.
   675	\item[HP6, brokered absolutism.] Royal rule making in the Catholic monarchies depended on negotiated intermediaries, so royal legislative success varied with the survival of provincial estates and corporate bodies \citep{beik1985}. Parent: H1. Falsifier: royal legislative success unrelated to the survival of intermediaries.
   676	\item[HP7, veto trade-off.] The number of effective veto players is positively associated with the persistence of preferential rules and negatively associated with responsiveness to changes in majority preference, as Proposition~\ref{prop:political-power:veto} predicts. Parent: H2. Falsifier: no association with the persistence of preferential rules.
   677	\end{description}
   678	
   679	HP1 and HP7 test the propositions of Section~\ref{sec:mechanisms} directly, and HP3 tests the role of organized opposition. HP2 and HP4 import established theories of autocracy into the framework, and their value here lies in coding the same variables across all six regime types. HP5 and HP6 apply to particular historical regime types and require archival coding. Identification is difficult for all seven. Appointment rules, veto structures, and legitimation strategies are chosen by rule makers, so cross-sectional associations confound the effects of these institutions with the reasons they were adopted. The source framework's event-study design, which compares outcomes before and after reforms of oversight in matched jurisdictions, is the appropriate design where such reforms occurred \citep[Section~9]{largo2026hbs}.
   680	
   681	\section{Revelation 13 and the rule-making pillar}
   682	\label{sec:revelation}
   683	
   684	The series reads Revelation typologically: the beast is a recurring pattern of power that claims ultimate loyalty, with the Roman Empire of the first century as its historical anchor \citep{bauckham1993,koester2014}. The reading identifies no present-day government, party, institution, or person with the beast, and it declines the futurist practice of doing so, whose long record of failed identifications is documented in the history of its reception \citep{fuller1995,mcginn1998}. The mapping from the text to the six pillars is an interpretive claim of the series, not a result of exegesis.
   685	
   686	Revelation 13 opens with a beast rising from the sea to whom ``the dragon gave him his power, and his seat, and great authority'' (Rev.\ 13:2, \citealp{kjv}). The rule-making authority of the beast is derived; it comes from a source outside itself and is then exercised over others. In Weber's terms the passage poses the question of legitimacy, the ground on which a claim to rule is accepted \citep{weber1978}. The text then records the response of those ruled: ``Who is like unto the beast? who is able to make war with him?'' (Rev.\ 13:4). The question describes authority that admits no contest. In the vocabulary of this paper it is an image of contestability near zero and concentration near one, the condition under which the pillar's term $H^{\pP}(1-Q^{\pP})$ in unaccountable concentration is at its maximum. The beast's reach extends ``over all kindreds, and tongues, and nations'' (Rev.\ 13:7), so a single authority governs a population whose plurality the necessity theorem takes as its starting point.
   687	
   688	Two features of the text qualify this image. The authority is repeatedly described as given, and given for a limited time: ``power was given unto him to continue forty and two months'' (Rev.\ 13:5). Within the text the beast's rule is bounded by a sovereignty it does not control. The second beast, from the earth, ``exerciseth all the power of the first beast before him'' and causes the inhabitants of the earth to worship the first (Rev.\ 13:12). Read typologically, it represents the legitimation of political authority by a second institution, a coupling of rule making with the ideological pillar that Part IV examines. Kraybill and Friesen locate the historical referent in the imperial cult of the cities of Asia Minor and its ties to commerce and civic life \citep{kraybill1996,friesen2001}, and Collins reads the book as a response to a crisis perceived by its audience \citep{collins1984}.
   689	
   690	Revelation 17 gives the clearest image of the rule-making pillar itself. The ten horns ``are ten kings, which have received no kingdom as yet; but receive power as kings one hour with the beast. These have one mind, and shall give their power and strength unto the beast'' (Rev.\ 17:12 to 13). Ten rulers who could have acted as separate veto players surrender their authority to a single center. In the terms of Proposition~\ref{prop:political-power:concentration}, the image is a move from a dispersed set of rule makers toward the dictatorship case, accomplished by delegation rather than conquest. The text then has the same kings turn on the city they served (Rev.\ 17:16), an image of the instability of coalitions that rest on delegated power. Svolik's account of authoritarian power sharing, in which the ruler's allies are also the most likely source of the ruler's removal, describes the same instability in the vocabulary of political science \citep{svolik2012}. The parallel is an interpretive analogy and makes no claim about the authorial intention of the text.
   691	
   692	Bauckham reads Revelation as a critique of Rome's claim to absolute loyalty, set against the alternative of faithful witness \citep{bauckham1993}. On this reading the object of the critique is not the existence of political authority. Paul's letter to the Romans tells its readers, ``Let every soul be subject unto the higher powers'' (Rom.\ 13:1), and Christian political ethics has long read Romans 13 and Revelation 13 together \citep{yoder1972}. The typological reading adopted here locates the warning of Revelation 13 at the point where rule making becomes unanswerable, not at the existence of rule makers. This is the theological counterpart of the distinction between Proposition A and Proposition B. Every polity has rule makers. The image of the beast applies when the rule makers can no longer be contested.
   693	
   694	\section{Objections and scope conditions}
   695	\label{sec:objections}
   696	
   697	The necessity theorem is not vacuous, because both of its substantive assumptions can fail. A group whose members always agreed would need no procedure for selecting among divergent preferences, and a group in an unchanging environment could persist without changing its rules. The predicate ``implements rule making'' is thin, but Section~\ref{sec:necessity} states what it excludes: decisions and rule changes imposed from outside, and rules that never change through environments that no single rule system could survive. A thin predicate that can fail differs from one that holds by definition.
   698	
   699	The boundary between rule making and interpretation is analytical, and it is drawn by act rather than by institution. Common-law courts make rules, constitutional courts shape legislation, and administrative agencies both make and apply regulations. Definition~\ref{def:political-power:boundary} classifies each such act, and the many-to-many role map of the source framework records an institution that does both in both pillars, with the coupling $C_{\pP\pJ}$ measuring how far one coalition controls the two. Part III applies the same classification of mixed acts from the interpretive side.
   700	
   701	Power indices measure formal power and nothing more. The Shapley-Shubik share assumes that all orderings of members are equally likely and ignores the content of proposals, the identity of agenda setters, and informal influence. The paper therefore uses the index only as a de jure baseline and pairs it with outcome-based indicators of de facto control in Table~\ref{tab:indicators}, recording the origin of proposals separately because initiation and enactment are different powers. A large gap between the two, as in brokered absolutism or patronal regimes, is itself evidence about where rule-making power lies.
   702	
   703	The comparison of regime types from different centuries is valid because it asks the same questions of each, not because the answers are commensurable in every respect. A medieval caliphate and a twenty-first century democracy face different problems with different technologies of rule. The six types are lenses, as Section~\ref{sec:regimes} states, and the comparative claims concern the distribution of a function that the necessity theorem shows all of them must perform.
   704	
   705	The theological reading is separable from the analysis. Nothing in Sections~\ref{sec:layer}, \ref{sec:necessity}, \ref{sec:mechanisms}, and~\ref{sec:measurement} depends on it, and the reading is offered as an interpretation of a text that has shaped the political imagination of many societies, with its interpretive status stated.
   706	
   707	The mechanisms are modeled in their simplest forms. Richer models of oligarchy, veto bargaining, and appointment would move the thresholds and could qualify some conclusions, so the propositions are offered as conditional mechanisms, not as complete theories.
   708	
   709	The sources for some regime types are themselves contested. For the Islamic states and the Catholic monarchies in particular, the paper relies on specialists whose interpretations are debated, and it reports their positions without adjudicating among them.
   710	
   711	\section{Conclusion}
   712	\label{sec:conclusion}
   713	
   714	Every persistent collective whose members disagree about binding choices, and whose environment changes, makes rules. The theorem of Section~\ref{sec:necessity} establishes this from explicit assumptions, and the stateless and consensus societies that seem to refute it display the function in distributed form: talk, oratory without command, collective suppression of would-be dominants, and fission. The same function is performed by parliaments, party committees, kings in council, and assemblies of jurists.
   715	
   716	The existence of the function places no constraint on its concentration. For a group of any size, procedures that satisfy the necessity theorem range from equal shares to dictatorship. Concentration, contestability, and coupling to other pillars therefore have to be measured, and the comparative evidence shows that they vary independently of the source of legitimacy that a regime claims. The conditional mechanisms of Section~\ref{sec:mechanisms} describe how rule making can drift toward capture through diffuse monitoring incentives, protected vetoes, appointment chains, and agenda control. Each mechanism has a check that acts on contestability, and none of the checks removes the need for rule makers.
   717	
   718	What remains uncertain is quantitative: how concentrated and how contestable rule making is in particular polities, and how strongly it is coupled to the other pillars. Answering these questions requires the preregistered coding that the framework specifies. The conclusion that the paper can defend is structural. The question of who makes the laws has always had an answer; whether the answer can be contested is the question on which accountability depends.
   719	
   720	\begin{thebibliography}{200}

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '595,625p' papers/latex/political-power.tex | nl -ba -v 595" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   595	\subsection{The appointment channel}
   596	
   597	The source framework defines cross-pillar integration $C_{mn}$ only descriptively, as the extent to which one coalition commands appointments, budgets, sanctions, or agenda in two pillars \citep{largo2026hbs}, and Part VII fixes a formal definition for the series. The appointment channel acquires testable content under one explicit candidate, the coalition-overlap measure. Let $\mathcal{S}$ be a preregistered list of coherent coalitions, groups such as parties, factions, or dynasties that can issue joint directives. For $S\in\mathcal{S}$ let $s^{\pP}(S)$ be the Shapley-Shubik share of the bloc player $p_S$ in the quotient game on $N_S=(N\setminus S)\cup\{p_S\}$, whose winning coalitions are defined for $T\subseteq N\setminus S$ by $T\in\Win_S$ if and only if $T\in\Win$, and $T\cup\{p_S\}\in\Win_S$ if and only if $T\cup S\in\Win$. This bloc share is not in general the sum of the members' separate shares; in the Iranian example of Table~\ref{tab:examples} the two councils hold $1/6+1/6$ separately and $1/2$ as a bloc. Let $\kappa_\ell(S)\in[0,1]$ be the share of decision-relevant control in pillar $\ell$ that is exercised in accordance with the directives of $S$, and set
   598	\begin{equation}
   599	C^{\mathrm{ov}}_{\pP\ell}=\max_{S\in\mathcal{S}}\min\{s^{\pP}(S),\kappa_\ell(S)\}.
   600	\label{eq:overlap}
   601	\end{equation}
   602	The candidate lies in $[0,1]$, equals one when a single coalition holds all rule-making control and commands all of pillar $\ell$, and equals zero when no listed coalition has a positive share in both.
   603	
   604	\begin{proposition}[Appointment bounds on integration]
   605	\label{prop:political-power:appointment-bound}
   606	For a coalition $S$ and an office $o$ let $f_{S,o}\in[0,1]$ be the share of the holder's decisions that follow the directives of $S$. For $S\in\mathcal{S}$ with $\alpha_{S,\ell}>0$ define the loyalty of its appointees as the conditional average
   607	\[
   608	\lambda_S=\frac{1}{\alpha_{S,\ell}}\sum_{o\in O_\ell}w_o f_{S,o}\,\mathbf{1}[S\text{ can unilaterally appoint or remove the holder of }o],
   609	\]
   610	and set $\lambda_S=0$ when $\alpha_{S,\ell}=0$. Suppose that command in pillar $\ell$ decomposes as $\kappa_\ell(S)=\lambda_S\alpha_{S,\ell}+\gamma_S$, where $\gamma_S\in[0,1-\lambda_S\alpha_{S,\ell}]$ is command exercised through channels other than appointment, such as budgets, sanctions, and informal patronage. Then:
   611	\begin{enumerate}[label=(\alph*)]
   612	\item for every $S\in\mathcal{S}$, $C^{\mathrm{ov}}_{\pP\ell}\ge\min\{s^{\pP}(S),\lambda_S\alpha_{S,\ell}\}$;
   613	\item if command runs only through appointment ($\gamma_S=0$ for all $S$) and loyalty is at most $\bar\lambda$ ($\lambda_S\le\bar\lambda$ for all $S$), then $C^{\mathrm{ov}}_{\pP\ell}\le\bar\lambda\max_{S\in\mathcal{S}}\alpha_{S,\ell}$;
   614	\item if command runs only through appointment and no listed coalition can unilaterally appoint or remove the holder of any office in $O_\ell$, for example because both appointment and removal require the consent of two bodies controlled by different coalitions, then $C^{\mathrm{ov}}_{\pP\ell}=0$.
   615	\end{enumerate}
   616	\end{proposition}
   617	
   618	\begin{proof}
   619	(a) By Equation~\eqref{eq:overlap}, $C^{\mathrm{ov}}_{\pP\ell}\ge\min\{s^{\pP}(S),\kappa_\ell(S)\}$. Since $\gamma_S\ge0$, $\kappa_\ell(S)\ge\lambda_S\alpha_{S,\ell}$, and the minimum is nondecreasing in each argument. (b) For every $S$, $\min\{s^{\pP}(S),\kappa_\ell(S)\}\le\kappa_\ell(S)=\lambda_S\alpha_{S,\ell}\le\bar\lambda\max_{S'}\alpha_{S',\ell}$; take the maximum over $S$. (c) The hypothesis gives $\alpha_{S,\ell}=0$ for every $S\in\mathcal{S}$ by Definition~\ref{def:political-power:appointment-channel}, and (b) gives $C^{\mathrm{ov}}_{\pP\ell}\le0$.
   620	\end{proof}
   621	
   622	The proposition separates three quantities that comparative accounts often run together. The rule-making share $s^{\pP}(S)$ says how much of rule making the coalition controls. The appointment share $\alpha_{S,\ell}$ says how many posts in another pillar it fills. The loyalty parameter $\lambda_S$ says how far the people it appoints do what it wants. Nomenklatura systems maximize the first two, and part (a) then makes integration high unless loyalty is low. The Soviet evidence of elite divisions \citep{lane1995} and of bureaucratic bargaining \citep{hough1979} concerns loyalty, and so it limits the integration that appointment alone can produce. Parts (b) and (c) identify the check. Requiring the consent of a second body for both appointment and removal closes the appointment channel to any single coalition, and security of tenure lowers loyalty after appointment by removing the threat of dismissal. Under plural appointment any remaining integration must run through budgets, sanctions, or patronage ($\gamma_S$), which tells an investigator where to look.
   623	
   624	\subsection{Agenda control and quiet politics}
   625	

codex
I’ve completed the full source read. I’m now checking label/citation/environment consistency within that file; I won’t compile it because TeX would read package/class files beyond the user-authorized file and generate auxiliary files.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "perl -0777 -ne 'while(/\\\\label\\{(["'^}]+)'"\\}/g){"'$L{$1}++;$Ll{$1}.=($.||q{})} while(/'"\\\\(?:ref|eqref|cref|Cref)\\{(["'^}]+)'"\\}/g){for(split /,/, "'$1){$R{$_}++}} while(/'"\\\\cite(?:p|t|alp|alt|author|year|yearpar)?(?:\\[["'^'"\\]]*\\])?(?:\\[["'^'"\\]]*\\])?\\{(["'^}]+)'"\\}/g){for(split /,/, "'$1){s/''^'"\\s+|\\s+"'$//g;$C{$_}++}} while(/'"\\\\bibitem(?:\\[["'^'"\\]]*\\])?\\{(["'^}]+)'"\\}/g){"'$B{$1}++} while(/'"\\\\begin\\{(["'^}]+)'"\\}/g){"'$E{$1}++} while(/'"\\\\end\\{(["'^}]+)'"\\}/g){"'$F{$1}++} print qq{Undefined refs:'"\\n}; print qq{"'$_'"\\n} for grep {"'!$L{$_}} sort keys %R; print qq{Duplicate labels:'"\\n}; print qq{"'$_ ($L{$_})'"\\n} for grep {"'$L{$_}>1} sort keys %L; print qq{Missing bibitems:'"\\n}; print qq{"'$_'"\\n} for grep {"'!$B{$_}} sort keys %C; print qq{Duplicate bibitems:'"\\n}; print qq{"'$_ ($B{$_})'"\\n} for grep {"'$B{$_}>1} sort keys %B; print qq{Environment count mismatches:'"\\n}; print qq{"'$_ begin=$E{$_} end=$F{$_}'"\\n} for grep {("'$E{$_}//0)!=($F{$_}//0)} sort(keys(%E),keys(%F));'"' papers/latex/political-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
Undefined refs:
Duplicate labels:
Missing bibitems:
Duplicate bibitems:
Environment count mismatches:

2026-10-22T16:41:19.463238Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "LC_ALL=C grep -n '["'^ -~]'"' papers/latex/political-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 exited 1 in 0ms:
2026-10-22T16:41:22.798579Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "grep -nE '\\\\\\[|\\\\\\]|begin\\{equation\\}|end\\{equation\\}|begin\\{align|end\\{align' papers/latex/political-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
47:\title{Political Power and Rule Making\\[4pt]
89:\begin{equation}
92:\end{equation}
232:\[
234:\]
598:\begin{equation}
601:\end{equation}
607:\[
609:\]

2026-10-22T16:41:30.339792Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "grep -nE '[0-9]-[0-9]' papers/latex/political-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
724:Aberle, D. F., A. K. Cohen, A. K. Davis, M. J. Levy Jr., and F. X. Sutton. 1950. ``The Functional Prerequisites of a Society.'' \emph{Ethics} 60(2): 100-111. doi:10.1086/290705.
733:Ansolabehere, Stephen, John M. de Figueiredo, and James M. Snyder. 2003. ``Why Is There So Little Money in U.S. Politics?'' \emph{Journal of Economic Perspectives} 17(1): 105-130. doi:10.1257/089533003321164976.
739:Bachrach, Peter and Morton S. Baratz. 1962. ``Two Faces of Power.'' \emph{American Political Science Review} 56(4): 947-952. doi:10.2307/1952796.
760:Bertrand, Marianne, Matilde Bombardini, and Francesco Trebbi. 2014. ``Is It Whom You Know or What You Know? An Empirical Assessment of the Lobbying Process.'' \emph{American Economic Review} 104(12): 3885-3920. doi:10.1257/aer.104.12.3885.
763:Blanes i Vidal, Jordi, Mirko Draca, and Christian Fons-Rosen. 2012. ``Revolving Door Lobbyists.'' \emph{American Economic Review} 102(7): 3731-3748. doi:10.1257/aer.102.7.3731.
775:Branham, J. Alexander, Stuart N. Soroka, and Christopher Wlezien. 2017. ``When Do the Rich Win?'' \emph{Political Science Quarterly} 132(1): 43-62. doi:10.1002/polq.12577.
787:Cassinelli, C. W. 1953. ``The Law of Oligarchy.'' \emph{American Political Science Review} 47(3): 773-784. doi:10.2307/1952904.
802:Coppedge, Michael, John Gerring, David Altman, Michael Bernhard, Steven Fish, Allen Hicken, Matthew Kroenig, Staffan I. Lindberg, Kelly McMann, Pamela Paxton, Holli A. Semetko, Svend-Erik Skaaning, Jeffrey Staton, and Jan Teorell. 2011. ``Conceptualizing and Measuring Democracy: A New Approach.'' \emph{Perspectives on Politics} 9(2): 247-267. doi:10.1017/S1537592711000880.
805:Cox, Michael, Gwen Arnold, and Sergio Villamayor Tomas. 2010. ``A Review of Design Principles for Community-based Natural Resource Management.'' \emph{Ecology and Society} 15(4): 38. doi:10.5751/ES-03704-150438.
826:Elkjaer, Mads Andreas and Michael Baggesen Klitgaard. 2024. ``Economic Inequality and Political Responsiveness: A Systematic Review.'' \emph{Perspectives on Politics} 22(2): 318-337. doi:10.1017/S1537592721002188.
832:Elliott, J. H. 1963. \emph{Imperial Spain 1469-1716}. Edward Arnold.
862:Gandhi, Jennifer and Adam Przeworski. 2007. ``Authoritarian Institutions and the Survival of Autocrats.'' \emph{Comparative Political Studies} 40(11): 1279-1301. doi:10.1177/0010414007305817.
868:Geddes, Barbara, Joseph Wright, and Erica Frantz. 2014. ``Autocratic Breakdown and Regime Transitions: A New Data Set.'' \emph{Perspectives on Politics} 12(2): 313-331. doi:10.1017/S1537592714000851.
871:Gerschewski, Johannes. 2013. ``The Three Pillars of Stability: Legitimation, Repression, and Co-optation in Autocratic Regimes.'' \emph{Democratization} 20(1): 13-38. doi:10.1080/13510347.2013.738860.
874:Gilens, Martin and Benjamin I. Page. 2014. ``Testing Theories of American Politics: Elites, Interest Groups, and Average Citizens.'' \emph{Perspectives on Politics} 12(3): 564-581. doi:10.1017/S1537592714001595.
880:Guriev, Sergei and Daniel Treisman. 2019. ``Informational Autocrats.'' \emph{Journal of Economic Perspectives} 33(4): 100-127. doi:10.1257/jep.33.4.100.
889:Hall, Richard L. and Alan V. Deardorff. 2006. ``Lobbying as Legislative Subsidy.'' \emph{American Political Science Review} 100(1): 69-84. doi:10.1017/s0003055406062010.
904:Hempel, Carl G. 1959. ``The Logic of Functional Analysis.'' In \emph{Symposium on Sociological Theory}, ed.~Llewellyn Gross, Harper \& Row, pp.~271-307.
925:Kalla, Joshua L. and David E. Broockman. 2016. ``Campaign Contributions Facilitate Access to Congressional Officials: A Randomized Field Experiment.'' \emph{American Journal of Political Science} 60(3): 545-558. doi:10.1111/ajps.12180.
970:Lane, David and Cameron Ross. 1995. ``The CPSU Ruling Elite 1981-1991: Commonalities and Divisions.'' \emph{Communist and Post-Communist Studies} 28(3): 339-360. doi:10.1016/0967-067X(95)00020-U.
988:Linz, Juan J. 1990. ``The Perils of Presidentialism.'' \emph{Journal of Democracy} 1(1): 51-69. doi:10.1353/jod.2005.0026.
1012:L\"uhrmann, Anna, Marcus Tannenberg, and Staffan I. Lindberg. 2018. ``Regimes of the World (RoW): Opening New Avenues for the Comparative Study of Political Regimes.'' \emph{Politics and Governance} 6(1): 60-77. doi:10.17645/pag.v6i1.1214.
1015:Lukes, Steven. 2005. \emph{Power: A Radical View}. Palgrave Macmillan. doi:10.1007/978-0-230-80257-5.
1021:Magaloni, Beatriz. 2008. ``Credible Power-Sharing and the Longevity of Authoritarian Rule.'' \emph{Comparative Political Studies} 41(4-5): 715-741. doi:10.1177/0010414007313124.
1039:Minzner, Carl F. 2011. ``China's Turn against Law.'' \emph{American Journal of Comparative Law} 59(4): 935-984. doi:10.5131/ajcl.2011.0006.
1054:Ostrom, Elinor. 2010. ``Beyond Markets and States: Polycentric Governance of Complex Economic Systems.'' \emph{American Economic Review} 100(3): 641-672. doi:10.1257/aer.100.3.641.
1060:Peltzman, Sam. 1976. ``Toward a More General Theory of Regulation.'' \emph{The Journal of Law and Economics} 19(2): 211-240. doi:10.1086/466865.
1084:Ross, Michael L. 2001. ``Does Oil Hinder Democracy?'' \emph{World Politics} 53(3): 325-361. doi:10.1353/wp.2001.0011.
1105:Shapley, L. S. and Martin Shubik. 1954. ``A Method for Evaluating the Distribution of Power in a Committee System.'' \emph{American Political Science Review} 48(3): 787-792. doi:10.2307/1951053.
1111:Stigler, George J. 1971. ``The Theory of Economic Regulation.'' \emph{The Bell Journal of Economics and Management Science} 2(1): 3-21. doi:10.2307/3003160.
1123:Van Kley, Dale K. 1996. \emph{The Religious Origins of the French Revolution: From Calvin to the Civil Constitution, 1560-1791}. Yale University Press.
1129:Voss, Kim and Rachel Sherman. 2000. ``Breaking the Iron Law of Oligarchy: Union Revitalization in the American Labor Movement.'' \emph{American Journal of Sociology} 106(2): 303-349. doi:10.1086/316963.
1132:Weber, Max. 1946. ``Politics as a Vocation.'' In \emph{From Max Weber: Essays in Sociology}, ed.~Gerth and Mills, Oxford University Press, pp.~77-128.
1138:Weingast, Barry R. 1997. ``The Political Foundations of Democracy and the Rule of Law.'' \emph{American Political Science Review} 91(2): 245-263. doi:10.2307/2952354.
1141:Wiessner, Polly. 2005. ``Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity?'' \emph{Human Nature} 16(2): 115-145. doi:10.1007/s12110-005-1000-9.
1147:Woodburn, James. 1982. ``Egalitarian Societies.'' \emph{Man (N.S.)} 17(3): 431-451. doi:10.2307/2801707.

2026-10-22T16:41:40.604353Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "grep -n 'doi:' papers/latex/political-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
724:Aberle, D. F., A. K. Cohen, A. K. Davis, M. J. Levy Jr., and F. X. Sutton. 1950. ``The Functional Prerequisites of a Society.'' \emph{Ethics} 60(2): 100-111. doi:10.1086/290705.
727:Acemoglu, Daron and James A. Robinson. 2006. \emph{Economic Origins of Dictatorship and Democracy}. Cambridge University Press. doi:10.1017/CBO9780511510809.
733:Ansolabehere, Stephen, John M. de Figueiredo, and James M. Snyder. 2003. ``Why Is There So Little Money in U.S. Politics?'' \emph{Journal of Economic Perspectives} 17(1): 105-130. doi:10.1257/089533003321164976.
739:Bachrach, Peter and Morton S. Baratz. 1962. ``Two Faces of Power.'' \emph{American Political Science Review} 56(4): 947-952. doi:10.2307/1952796.
742:Barkey, Karen. 2008. \emph{Empire of Difference: The Ottomans in Comparative Perspective}. Cambridge University Press. doi:10.1017/cbo9780511790645.
745:Bartels, Larry M. 2008. \emph{Unequal Democracy: The Political Economy of the New Gilded Age}. Princeton University Press. doi:10.1515/9781400883363.
748:Bauckham, Richard. 1993. \emph{The Theology of the Book of Revelation}. Cambridge University Press. doi:10.1017/cbo9780511819858.
751:Baumgartner, Frank R., Jeffrey M. Berry, Marie Hojnacki, David C. Kimball, and Beth L. Leech. 2009. \emph{Lobbying and Policy Change: Who Wins, Who Loses, and Why}. University of Chicago Press. doi:10.7208/chicago/9780226039466.001.0001.
754:Beik, William. 1985. \emph{Absolutism and Society in Seventeenth-Century France: State Power and Provincial Aristocracy in Languedoc}. Cambridge University Press. doi:10.1017/cbo9780511583797.
757:Berman, Sheri. 2006. \emph{The Primacy of Politics: Social Democracy and the Making of Europe's Twentieth Century}. Cambridge University Press. doi:10.1017/cbo9780511791109.
760:Bertrand, Marianne, Matilde Bombardini, and Francesco Trebbi. 2014. ``Is It Whom You Know or What You Know? An Empirical Assessment of the Lobbying Process.'' \emph{American Economic Review} 104(12): 3885-3920. doi:10.1257/aer.104.12.3885.
763:Blanes i Vidal, Jordi, Mirko Draca, and Christian Fons-Rosen. 2012. ``Revolving Door Lobbyists.'' \emph{American Economic Review} 102(7): 3731-3748. doi:10.1257/aer.102.7.3731.
769:Boehm, Christopher. 1999. \emph{Hierarchy in the Forest: The Evolution of Egalitarian Behavior}. Harvard University Press. doi:10.2307/j.ctvjf9xr4.
775:Branham, J. Alexander, Stuart N. Soroka, and Christopher Wlezien. 2017. ``When Do the Rich Win?'' \emph{Political Science Quarterly} 132(1): 43-62. doi:10.1002/polq.12577.
784:Bueno de Mesquita, Bruce, Alastair Smith, Randolph M. Siverson, and James D. Morrow. 2003. \emph{The Logic of Political Survival}. MIT Press. doi:10.7551/mitpress/4292.001.0001.
787:Cassinelli, C. W. 1953. ``The Law of Oligarchy.'' \emph{American Political Science Review} 47(3): 773-784. doi:10.2307/1952904.
790:Clastres, Pierre. 1987. \emph{Society against the State: Essays in Political Anthropology (1974)}, trans.~Robert Hurley. Zone Books. doi:10.2307/j.ctv1595m3p.
796:Collins, James B. 1995. \emph{The State in Early Modern France}. Cambridge University Press. doi:10.1017/cbo9781139170147.
799:Commins, David. 2006. \emph{The Wahhabi Mission and Saudi Arabia}. I. B. Tauris. doi:10.5040/9780755609444.
802:Coppedge, Michael, John Gerring, David Altman, Michael Bernhard, Steven Fish, Allen Hicken, Matthew Kroenig, Staffan I. Lindberg, Kelly McMann, Pamela Paxton, Holli A. Semetko, Svend-Erik Skaaning, Jeffrey Staton, and Jan Teorell. 2011. ``Conceptualizing and Measuring Democracy: A New Approach.'' \emph{Perspectives on Politics} 9(2): 247-267. doi:10.1017/S1537592711000880.
805:Cox, Michael, Gwen Arnold, and Sergio Villamayor Tomas. 2010. ``A Review of Design Principles for Community-based Natural Resource Management.'' \emph{Ecology and Society} 15(4): 38. doi:10.5751/ES-03704-150438.
814:Culpepper, Pepper D. 2010. \emph{Quiet Politics and Business Power: Corporate Control in Europe and Japan}. Cambridge University Press. doi:10.1017/cbo9780511760716.
826:Elkjaer, Mads Andreas and Michael Baggesen Klitgaard. 2024. ``Economic Inequality and Political Responsiveness: A Systematic Review.'' \emph{Perspectives on Politics} 22(2): 318-337. doi:10.1017/S1537592721002188.
829:Ellickson, Robert C. 1991. \emph{Order without Law: How Neighbors Settle Disputes}. Harvard University Press. doi:10.4159/9780674036437.
841:Ertman, Thomas. 1997. \emph{Birth of the Leviathan: Building States and Regimes in Medieval and Early Modern Europe}. Cambridge University Press. doi:10.1017/cbo9780511529016.
844:Esping-Andersen, G{\o}sta. 1985. \emph{Politics against Markets: The Social Democratic Road to Power}. Princeton University Press. doi:10.1515/9781400886203.
850:Fainsod, Merle. 1953. \emph{How Russia Is Ruled}. Harvard University Press. doi:10.4159/harvard.9780674189188.
856:Friesen, Steven J. 2001. \emph{Imperial Cults and the Apocalypse of John: Reading Revelation in the Ruins}. Oxford University Press. doi:10.1093/0195131533.001.0001.
859:Fuller, Robert C. 1995. \emph{Naming the Antichrist: The History of an American Obsession}. Oxford University Press. doi:10.1093/acprof:oso/9780195109795.001.0001.
862:Gandhi, Jennifer and Adam Przeworski. 2007. ``Authoritarian Institutions and the Survival of Autocrats.'' \emph{Comparative Political Studies} 40(11): 1279-1301. doi:10.1177/0010414007305817.
868:Geddes, Barbara, Joseph Wright, and Erica Frantz. 2014. ``Autocratic Breakdown and Regime Transitions: A New Data Set.'' \emph{Perspectives on Politics} 12(2): 313-331. doi:10.1017/S1537592714000851.
871:Gerschewski, Johannes. 2013. ``The Three Pillars of Stability: Legitimation, Repression, and Co-optation in Autocratic Regimes.'' \emph{Democratization} 20(1): 13-38. doi:10.1080/13510347.2013.738860.
874:Gilens, Martin and Benjamin I. Page. 2014. ``Testing Theories of American Politics: Elites, Interest Groups, and Average Citizens.'' \emph{Perspectives on Politics} 12(3): 564-581. doi:10.1017/S1537592714001595.
880:Guriev, Sergei and Daniel Treisman. 2019. ``Informational Autocrats.'' \emph{Journal of Economic Perspectives} 33(4): 100-127. doi:10.1257/jep.33.4.100.
886:Hale, Henry E. 2014. \emph{Patronal Politics: Eurasian Regime Dynamics in Comparative Perspective}. Cambridge University Press. doi:10.1017/CBO9781139683524.
889:Hall, Richard L. and Alan V. Deardorff. 2006. ``Lobbying as Legislative Subsidy.'' \emph{American Political Science Review} 100(1): 69-84. doi:10.1017/s0003055406062010.
895:Hart, H. L. A. 1961. \emph{The Concept of Law}. Clarendon Press (3rd ed.~2012, Oxford University Press). doi:10.1093/he/9780199644704.001.0001.
898:Hayek, Friedrich A. 1973. \emph{Law, Legislation and Liberty, Volume 1: Rules and Order}. University of Chicago Press. doi:10.7208/chicago/9780226321233.001.0001.
901:Hegghammer, Thomas. 2010. \emph{Jihad in Saudi Arabia: Violence and Pan-Islamism since 1979}. Cambridge University Press. doi:10.1017/cbo9780511809439.
907:Hertog, Steffen. 2010. \emph{Princes, Brokers, and Bureaucrats: Oil and the State in Saudi Arabia}. Cornell University Press. doi:10.7591/9780801458774.
910:Hirschl, Ran. 2004. \emph{Towards Juristocracy: The Origins and Consequences of the New Constitutionalism}. Harvard University Press. doi:10.2307/j.ctv15d81nb.
916:Huber, Evelyne and John D. Stephens. 2001. \emph{Development and Crisis of the Welfare State: Parties and Policies in Global Markets}. University of Chicago Press. doi:10.7208/chicago/9780226356495.001.0001.
925:Kalla, Joshua L. and David E. Broockman. 2016. ``Campaign Contributions Facilitate Access to Congressional Officials: A Randomized Field Experiment.'' \emph{American Journal of Political Science} 60(3): 545-558. doi:10.1111/ajps.12180.
928:Kantorowicz, Ernst H. 1957. \emph{The King's Two Bodies: A Study in Mediaeval Political Theology}. Princeton University Press. doi:10.1515/9781400880782.
931:Kelly, Robert L. 1995. \emph{The Foraging Spectrum: Diversity in Hunter-Gatherer Lifeways}. Smithsonian Institution Press. doi:10.2307/j.ctv2sx9gc9.
943:Kitschelt, Herbert. 1994. \emph{The Transformation of European Social Democracy}. Cambridge University Press. doi:10.1017/CBO9780511622014.
946:Koester, Craig R. 2014. \emph{Revelation: A New Translation with Introduction and Commentary}. Yale University Press (Anchor Yale Bible 38A). doi:10.12987/9780300211030.
949:Kornai, J\'anos. 1992. \emph{The Socialist System: The Political Economy of Communism}. Princeton University Press. doi:10.2307/j.ctv1ddczdr.
958:Kuran, Timur. 2011. \emph{The Long Divergence: How Islamic Law Held Back the Middle East}. Princeton University Press. doi:10.1515/9781400836017.
961:Kuru, Ahmet T. 2019. \emph{Islam, Authoritarianism, and Underdevelopment: A Global and Historical Comparison}. Cambridge University Press. doi:10.1017/9781108296892.
964:Lambton, Ann K. S. 1981. \emph{State and Government in Medieval Islam}. Oxford University Press. doi:10.4324/9780203385463.
967:Landry, Pierre F. 2008. \emph{Decentralized Authoritarianism in China: The Communist Party's Control of Local Elites in the Post-Mao Era}. Cambridge University Press. doi:10.1017/CBO9780511510243.
970:Lane, David and Cameron Ross. 1995. ``The CPSU Ruling Elite 1981-1991: Commonalities and Divisions.'' \emph{Communist and Post-Communist Studies} 28(3): 339-360. doi:10.1016/0967-067X(95)00020-U.
979:Levitsky, Steven and Lucan A. Way. 2010. \emph{Competitive Authoritarianism: Hybrid Regimes after the Cold War}. Cambridge University Press. doi:10.1017/CBO9780511781353.
982:Lijphart, Arend. 1999. \emph{Patterns of Democracy: Government Forms and Performance in Thirty-Six Countries}. Yale University Press. doi:10.12987/9780300189124.
988:Linz, Juan J. 1990. ``The Perils of Presidentialism.'' \emph{Journal of Democracy} 1(1): 51-69. doi:10.1353/jod.2005.0026.
1012:L\"uhrmann, Anna, Marcus Tannenberg, and Staffan I. Lindberg. 2018. ``Regimes of the World (RoW): Opening New Avenues for the Comparative Study of Political Regimes.'' \emph{Politics and Governance} 6(1): 60-77. doi:10.17645/pag.v6i1.1214.
1015:Lukes, Steven. 2005. \emph{Power: A Radical View}. Palgrave Macmillan. doi:10.1007/978-0-230-80257-5.
1021:Magaloni, Beatriz. 2008. ``Credible Power-Sharing and the Longevity of Authoritarian Rule.'' \emph{Comparative Political Studies} 41(4-5): 715-741. doi:10.1177/0010414007313124.
1039:Minzner, Carl F. 2011. ``China's Turn against Law.'' \emph{American Journal of Comparative Law} 59(4): 935-984. doi:10.5131/ajcl.2011.0006.
1048:Olson, Mancur. 1965. \emph{The Logic of Collective Action: Public Goods and the Theory of Groups}. Harvard University Press. doi:10.4159/9780674041660.
1051:Ostrom, Elinor. 1990. \emph{Governing the Commons: The Evolution of Institutions for Collective Action}. Cambridge University Press. doi:10.1017/CBO9780511807763.
1054:Ostrom, Elinor. 2010. ``Beyond Markets and States: Polycentric Governance of Complex Economic Systems.'' \emph{American Economic Review} 100(3): 641-672. doi:10.1257/aer.100.3.641.
1057:Parsons, Talcott. 1951. \emph{The Social System}. Free Press. doi:10.4324/9780203992951.
1060:Peltzman, Sam. 1976. ``Toward a More General Theory of Regulation.'' \emph{The Journal of Law and Economics} 19(2): 211-240. doi:10.1086/466865.
1063:Pettit, Philip. 1997. \emph{Republicanism: A Theory of Freedom and Government}. Oxford University Press. doi:10.1093/0198296428.001.0001.
1066:Pontusson, Jonas. 1992. \emph{The Limits of Social Democracy: Investment Politics in Sweden}. Cornell University Press. doi:10.7591/9781501737541.
1072:Przeworski, Adam. 1985. \emph{Capitalism and Social Democracy}. Cambridge University Press. doi:10.1017/cbo9781139171830.
1075:Przeworski, Adam. 1991. \emph{Democracy and the Market: Political and Economic Reforms in Eastern Europe and Latin America}. Cambridge University Press. doi:10.1017/CBO9781139172493.
1078:Al-Rasheed, Madawi. 2002. \emph{A History of Saudi Arabia}. Cambridge University Press. doi:10.1017/cbo9780511993510.
1081:Root, Hilton L. 1987. \emph{Peasants and King in Burgundy: Agrarian Foundations of French Absolutism}. University of California Press. doi:10.1525/9780520913349.
1084:Ross, Michael L. 2001. ``Does Oil Hinder Democracy?'' \emph{World Politics} 53(3): 325-361. doi:10.1353/wp.2001.0011.
1087:Rothstein, Bo. 1996. \emph{The Social Democratic State: The Swedish Model and the Bureaucratic Problem of Social Reforms}. University of Pittsburgh Press. doi:10.2307/jj.13110785.
1090:Rubin, Jared. 2017. \emph{Rulers, Religion, and Riches: Why the West Got Rich and the Middle East Did Not}. Cambridge University Press. doi:10.1017/9781139568272.
1096:Schumpeter, Joseph A. 1942. \emph{Capitalism, Socialism and Democracy}. Harper \& Brothers. doi:10.4324/9780203857090.
1099:Scott, James C. 2009. \emph{The Art of Not Being Governed: An Anarchist History of Upland Southeast Asia}. Yale University Press. doi:10.12987/9780300156522.
1102:Scott, James C. 2017. \emph{Against the Grain: A Deep History of the Earliest States}. Yale University Press. doi:10.12987/9780300231687.
1105:Shapley, L. S. and Martin Shubik. 1954. ``A Method for Evaluating the Distribution of Power in a Committee System.'' \emph{American Political Science Review} 48(3): 787-792. doi:10.2307/1951053.
1108:Shirk, Susan L. 1993. \emph{The Political Logic of Economic Reform in China}. University of California Press. doi:10.1525/9780520912212.
1111:Stigler, George J. 1971. ``The Theory of Economic Regulation.'' \emph{The Bell Journal of Economics and Management Science} 2(1): 3-21. doi:10.2307/3003160.
1114:Stone Sweet, Alec. 2000. \emph{Governing with Judges: Constitutional Politics in Europe}. Oxford University Press. doi:10.1093/0198297718.001.0001.
1117:Svolik, Milan W. 2012. \emph{The Politics of Authoritarian Rule}. Cambridge University Press. doi:10.1017/CBO9781139176040.
1120:Tsebelis, George. 2002. \emph{Veto Players: How Political Institutions Work}. Princeton University Press. doi:10.1515/9781400831456.
1129:Voss, Kim and Rachel Sherman. 2000. ``Breaking the Iron Law of Oligarchy: Union Revitalization in the American Labor Movement.'' \emph{American Journal of Sociology} 106(2): 303-349. doi:10.1086/316963.
1135:Weber, Max. 1978. \emph{Economy and Society: An Outline of Interpretive Sociology}. University of California Press. doi:10.4159/9780674240827.
1138:Weingast, Barry R. 1997. ``The Political Foundations of Democracy and the Rule of Law.'' \emph{American Political Science Review} 91(2): 245-263. doi:10.2307/2952354.
1141:Wiessner, Polly. 2005. ``Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity?'' \emph{Human Nature} 16(2): 115-145. doi:10.1007/s12110-005-1000-9.
1144:Winters, Jeffrey A. 2011. \emph{Oligarchy}. Cambridge University Press. doi:10.1017/cbo9780511793806.
1147:Woodburn, James. 1982. ``Egalitarian Societies.'' \emph{Man (N.S.)} 17(3): 431-451. doi:10.2307/2801707.

2026-10-22T16:41:47.667655Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "grep -nE '("'^|[''^'"\\\\])[%&#_]' papers/latex/political-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
16:\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
88:The objects in this subsection are defined in the source framework and are used here without modification \citep{largo2026hbs}. The polity at time $t$ is a directed multiplex network $G_t=(V_t,E_t)$ whose nodes are organizations or coherent actor groups. Each pillar $m\in\Mset=\{\pF,\pP,\pJ,\pI,\pC,\pW\}$, with $M=|\Mset|=6$, has an adjacency layer $A^m_t$ with edge weights $a^m_{ij,t}\in[0,1]$ that record the documented capacity of actor $i$ to constrain a feasible action of actor $j$ through mechanism $m$. A many-to-many role map assigns each actor the pillars in which it acts. Actor $i$ holds a normalized control share $s^m_{i,t}$ in pillar $m$, with $\sum_i s^m_{i,t}=1$. Concentration is the Herfindahl-Hirschman index $H_{m,t}=\sum_i (s^m_{i,t})^2$. Contestability $Q_{m,t}\in[0,1]$ summarizes transparency, appeal rights, independence, competition, and credible replacement. Unaccountable concentration is the illustrative index
90:U_t=\sum_{m\in\Mset}\omega_m H_{m,t}(1-Q_{m,t}),\qquad \omega_m\ge 0,\quad \sum_m\omega_m=1,
93:with weights fixed in advance. Cross-pillar integration $C_{mn,t}\in[0,1]$ is the extent to which one coalition commands appointments, budgets, sanctions, or agenda in both $m$ and $n$, and the integration statistic is $\Int_t=\frac{2}{M(M-1)}\sum_{m<n}C_{mn,t}$, the mean over the fifteen pillar pairs. A capture link $(i\to j,m)$ requires privileged access or discretion, a resulting weakening of applicable accountability, and material evidence tying the asymmetry to an institutional output. A strong classification under the source's criterion requires both high $U_t$ and high $\Int_t$; differentiation alone never suffices \citep[Proposition~1]{largo2026hbs}. Pillar labels are written in sans-serif ($\pP$ for rule making) to keep them distinct from the integration statistic $\Int_t$ and from the role map. For the rule-making pillar the paper writes $s^{\pP}_i$, $H^{\pP}_t=H_{\pP,t}$, and $Q^{\pP}_t=Q_{\pP,t}$, dropping the time index when it plays no role. The letter $n$ is reserved below for the number of members of a collective, so a pillar other than $\pP$ is written $\ell$ and the couplings of rule making appear as $C_{\pP\ell}$.
95:Three terms are kept apart. \emph{Unaccountable concentration} in rule making is the pillar's term $H^{\pP}(1-Q^{\pP})$ in $U_t$. A \emph{capture link} $(i\to j,\pP)$ is the dyadic relation defined above, with a general rule as its institutional output. \emph{Systemic capture} is the joint condition of high $U_t$, high $\Int_t$, and documented capture links that the series calls Proposition B. Capture, regulatory capture, and state capture as objects of the resource pillar are developed in Part I \citep[Sections~4 and~6]{long2026financial}.
101:Let $N$ be the set of members of a collective, $|N|=n\ge 2$. A \emph{rule system} $R\in\Rules$ is a set of general prescriptions that apply to classes of persons and situations rather than to named individuals or single events. A \emph{collective decision} is a choice $x$ from a set $X$ of at least two alternatives such that the chosen alternative applies to all members at once (when to move camp, whether to go to war, which tax rate to levy). Each member $i$ ranks the alternatives by a strict linear order $\succ_i$ (complete and without indifference between distinct alternatives). Members' preferences \emph{diverge} over $X$ if no alternative is unanimously best: for every $x\in X$ some member $i$ and some $y\in X$ satisfy $y\succ_i x$. Write $R_t$ for the rule system in force at time $t$, where time runs over the integers.
106:Let $T$ be a window of consecutive periods. The rule-making function $\pP$ is \emph{implemented} in a collective over $T$ in sense (a) if some set of members or practices of the collective repeatedly selects collective decisions from sets of alternatives over which members' preferences diverge, and in sense (b) if such a practice replaces the rule system in force, $R_{t+1}\neq R_t$ for some $t$ with $t,t+1\in T$. The number of replacements in $T$ measures how often sense (b) is exercised. The selecting or replacing practice is the collective's \emph{rule-making procedure}. Its \emph{rule-making profile} records who may initiate a proposal, who must assent for it to take effect, who may block it, and who can be removed for its consequences.
125:Organization & Act & Pillar \\
127:Bourbon Parlement & Registration of a royal edict, or remonstrance that delays it & $\pP$ (veto) \\
128:Bourbon Parlement & Appellate judgment in a civil or criminal case & $\pJ$ \\
129:Iranian Guardian Council & Review of a bill passed by the Majles for compatibility with Islam and the constitution & $\pP$ (veto) \\
130:Iranian Guardian Council & Screening of candidates for elections it supervises & $\pP$ (veto over entry) \\
131:Iranian Guardian Council & Interpretation of the constitution & $\pJ$ \\
132:Ottoman sultan in council & Issue of a qanun regulation & $\pP$ \\
133:Ottoman qadi court & Application of sharia or qanun to a case & $\pJ$ \\
134:Common-law appellate court & Overruling a precedent & $\pP$ and $\pJ$ \\
135:Communist party committee & Appointment of a judge or prosecutor & $\pP$ (appointment) \\
142:The source framework defines $s^m_{i,t}$ as a normalized share of decision-relevant control but leaves its measurement open. For rule making a natural baseline is available. A rule-making procedure is, at a minimum, a specification of which coalitions can enact a proposal against the status quo. The baseline below models each decision as such a binary vote. When a decision involves three or more alternatives, an agenda rule determines which proposals are put against the status quo and in what order; that rule is the object of agenda control (Definition~\ref{def:political-power:agenda-control}) and is measured separately. Power indices from cooperative game theory turn the specification of winning coalitions into shares that sum to one.
146:A \emph{simple game} on $N$ is a family $\Win$ of winning coalitions with $N\in\Win$, $\emptyset\notin\Win$, and $S\in\Win$, $S\subseteq S'$ implying $S'\in\Win$. The game is \emph{proper} if $S\in\Win$ implies $N\setminus S\notin\Win$, so that two disjoint coalitions cannot both enact incompatible decisions; a rule-making procedure is represented by a proper simple game. An ordering of $N$ is a bijection $\pi:\{1,\dots,n\}\to N$, and $B_\pi(i)=\{\pi(k):k<\pi^{-1}(i)\}$ is the set of members who precede $i$. Member $i$ is \emph{the pivot} in $\pi$ if $B_\pi(i)\notin\Win$ and $B_\pi(i)\cup\{i\}\in\Win$. The Shapley-Shubik share of $i$ is $\varphi_i=|\{\pi: i \text{ is the pivot in } \pi\}|/n!$ \citep{shapley1954}. Member $i$ is a \emph{veto player} if $i\in S$ for every $S\in\Win$, and a \emph{dictator} if $\{i\}\in\Win$ and every winning coalition contains $i$.
149:The de jure baseline sets $s^{\pP}_i=\varphi_i$. Actual control can depart from the baseline when an agenda setter, an informal patron, or a donor shapes which proposals reach a vote, and the gap between de jure and de facto power is itself an object of study \citep{acemoglu2006}. The baseline is still useful, because it ties concentration to the written or customary procedure and so gives a reference point against which informal concentration can be measured.
153:Let $\Win$ be a simple game on $N$ with $|N|=n$, and set $s^{\pP}_i=\varphi_i$ and $H^{\pP}=\sum_i\varphi_i^2$.
155:\item In every ordering exactly one member is the pivot, so $\sum_i\varphi_i=1$.
156:\item $1/n\le H^{\pP}\le 1$, with $H^{\pP}=1/n$ if and only if $\varphi_i=1/n$ for every $i$.
159:\item A veto player $i$ satisfies $\varphi_i\ge\varphi_j$ for every $j\in N$.
164:(a) Fix $\pi$ and add members in the order $\pi$. The growing coalition starts at $\emptyset\notin\Win$ and ends at $N\in\Win$. By monotonicity, once the coalition is winning it remains winning, so it changes from losing to winning at exactly one step, and the member added at that step is the unique pivot. Summing over the $n!$ orderings gives $\sum_i\varphi_i=1$.
166:(b) By the Cauchy-Schwarz inequality, $1=(\sum_i\varphi_i)^2\le n\sum_i\varphi_i^2$, with equality if and only if all $\varphi_i$ are equal. The upper bound holds because $\varphi_i\in[0,1]$ and $\sum_i\varphi_i=1$ imply $\sum_i\varphi_i^2\le\sum_i\varphi_i=1$.
168:(c) If $\sigma$ is a permutation of $N$ and $\Win$ is invariant under $\sigma$, then $B_{\sigma\circ\pi}(\sigma(i))=\sigma(B_\pi(i))$, so $i$ is the pivot in $\pi$ if and only if $\sigma(i)$ is the pivot in $\sigma\circ\pi$. Composition with $\sigma$ is a bijection on orderings, so $\varphi_i=\varphi_{\sigma(i)}$. Every pair of members is exchanged by some permutation, so all shares are equal and (b) gives $H^{\pP}=1/n$.
170:(d) A member outside $K$ is never the pivot, because adding a member outside $K$ cannot complete $K$. In any ordering the pivot is the last member of $K$ to appear. By symmetry among the members of $K$, each is last in a fraction $1/k$ of orderings. Hence $\varphi_i=1/k$ for $i\in K$, $\varphi_i=0$ otherwise, and $H^{\pP}=k\cdot(1/k)^2=1/k$.
172:(e) Let $j\neq i$ and let $j$ be the pivot in $\pi$. Then $B_\pi(j)\cup\{j\}\in\Win$ contains the veto player $i$, and $i\neq j$, so $i\in B_\pi(j)$. Let $\pi'$ be $\pi$ with the positions of $i$ and $j$ exchanged. In $\pi'$ the set preceding $i$ is $B_\pi(j)\setminus\{i\}\cup\{j\}$, which does not contain $i$ and is therefore losing. Adding $i$ yields $B_\pi(j)\cup\{j\}$, which is winning. So $i$ is the pivot in $\pi'$. The exchange is a bijection on orderings, so the number of orderings in which $j$ is the pivot is at most the number in which $i$ is the pivot.
194:Values of $H^{\pP}$ are comparable only at a declared level of aggregation. At the \emph{member level} the players are individuals, as in the consensus band of Proposition~\ref{prop:political-power:minimal-form}, where $H^{\pP}=1/n_a$. At the \emph{organ level} the players are chambers, councils, parties voting as blocs, or the electorate in a referendum, as in Table~\ref{tab:examples}. An organ-level figure of $1/3$ and a member-level figure of $1/40$ do not measure the same thing, and the comparisons in this paper are made within a level, never across levels. Where both levels matter, each organ's decision can itself be modeled as a game among its members, so that member-level shares are computed through the organ-level procedure; the paper does not pursue that construction.
203:Procedure & Shares & $H^{\pP}$ \\
205:Single-party majority in the only veto chamber & $(1,0,\dots,0)$ & $1$ \\
206:Three parties with 40, 35, and 25 percent of seats under majority rule & $(1/3,1/3,1/3)$ & $1/3$ \\
207:Two chambers and an executive with an absolute veto & $(1/3,1/3,1/3)$ & $1/3$ \\
208:Majles, Guardian Council, and Expediency Council as separate actors & $(2/3,1/6,1/6)$ & $1/2$ \\
209:Majles and an appointed bloc of the two councils & $(1/2,1/2)$ & $1/2$ \\
216:The source's contestability index $Q_{m,t}$ is generic. For rule making five components can be distinguished and measured separately.
220:For a polity at time $t$, let $q_t=(q^{\mathrm{rep}},q^{\mathrm{ovs}},q^{\mathrm{ent}},q^{\mathrm{trn}},q^{\mathrm{ext}})\in[0,1]^5$ record, in order, the credibility of peaceful replacement of rule makers; the strength of oversight of rule makers by bodies they do not control; the freedom of entry into rule-making competition (forming parties, standing for office, petitioning); the transparency of rule making (publication of drafts, records of who proposed what); and the ease of exit from the jurisdiction or the group, so that cheap exit scores high. The rule-making contestability is $Q^{\pP}_t=g(q_t)$ for a preregistered aggregator $g:[0,1]^5\to[0,1]$ that is nondecreasing in each argument with $g(0,\dots,0)=0$ and $g(1,\dots,1)=1$.
231:For a pillar $\ell\in\Mset$ (the letter $n$ is reserved for the size of a collective; see Section~\ref{sec:layer}), let $O_\ell$ be the set of offices that exercise decision-relevant control in $\ell$, with weights $w_o\ge0$ and $\sum_{o\in O_\ell}w_o=1$ equal to each office's control share. For a coalition $S$, the \emph{appointment share} of $S$ in $\ell$ is
233:\alpha_{S,\ell}=\sum_{o\in O_\ell}w_o\,\mathbf{1}[S \text{ can unilaterally appoint or remove the holder of } o].
235:The appointment channel from $\pP$ to $\ell$ is the map $S\mapsto\alpha_{S,\ell}$.
249:Under the series' allocation of the fifteen pillar pairs, this paper gives the primary treatment of four: rule making with interpretation ($C_{\pP\pJ}$), with legitimation ($C_{\pP\pI}$), with enforcement ($C_{\pP\pC}$), and with production ($C_{\pP\pW}$). The pair with resource control, $C_{\pF\pP}$, belongs to Part I \citep{long2026financial}. Each pair has a characteristic channel.
251:Whoever appoints and removes judges couples rule making to interpretation, and so does the traffic between statute and precedent. Statutes give courts rules to apply, and judicial applications generate precedents and doctrines that legislatures then codify, override, or leave in place. A coalition that appoints judges without confirmation by another body and can remove them at will drives $\alpha_{S,\pJ}$ toward one.
257:The rules of work, taxation, and property, and the producers' organizations that help to make them, connect rule making to production. Labor law, tax codes, and the legal status of unions are outputs of $\pP$ that set the terms on which the productive population works. In corporatist systems, organized labor and employers take part in drafting the rules that govern them, which raises $C_{\pP\pW}$ by design and with the consent of the organized parties.
273:The environment $e_t\in E$ of the collective varies over time. There is a viability correspondence $\mathcal{V}:E\to 2^{\Rules}$, where $\mathcal{V}(e)$ is the set of rule systems under which the collective survives a period in environment $e$, and the realized path contains periods $s_0<s_1<\dots<s_r$, with $r\ge1$, such that consecutive viability sets are disjoint: $\mathcal{V}(e_{s_{j-1}})\cap\mathcal{V}(e_{s_j})=\emptyset$ for $j=1,\dots,r$.
278:(i) The collective's decisions and changes in its rules are produced by practices of its members rather than imposed from outside. (ii) The collective persists over a window $T$ of consecutive periods that contains $s_0$ and $s_r$, so $R_t\in\mathcal{V}(e_t)$ for all $t\in T$.
289:Let $x^\ast$ be the alternative realized in a collective decision. By Assumption~\ref{ass:political-power:plurality} there is a member $i$ and an alternative $y$ with $y\succ_i x^\ast$. Because the decision applies to all members at once, $i$ cannot obtain $y$ while others obtain $x^\ast$. Some practice, whether a vote, a command, a discussion that ends when objectors fall silent, or a default to the status quo, determined that $x^\ast$ rather than $y$ would hold for everyone, and by clause (i) of Assumption~\ref{ass:political-power:persistence} that practice is the members' own. That practice selects among divergent preferences. Collective decisions recur by assumption, so such selections recur.
294:Under Assumptions~\ref{ass:political-power:change} and~\ref{ass:political-power:persistence}, the rule system is replaced at least $r$ times on $T$: for each $j=1,\dots,r$ there is $t$ with $s_{j-1}\le t<s_j$ and $R_{t+1}\neq R_t$. Each replacement is produced by a practice of the members.
298:Fix $j$ and suppose $R_t=R_{t+1}$ for every $t$ with $s_{j-1}\le t<s_j$. Then $R_{s_{j-1}}=R_{s_j}=R$. Clause (ii) of Assumption~\ref{ass:political-power:persistence} gives $R\in\mathcal{V}(e_{s_{j-1}})$ and $R\in\mathcal{V}(e_{s_j})$, which contradicts the disjointness in Assumption~\ref{ass:political-power:change}. So some $t$ in $[s_{j-1},s_j)$ has $R_{t+1}\neq R_t$, and both $t$ and $t+1$ lie in $T$ because $T$ consists of consecutive periods containing $s_0$ and $s_r$. The intervals $[s_{j-1},s_j)$ are disjoint, so the $r$ replacements are distinct. By clause (i) of Assumption~\ref{ass:political-power:persistence} each is produced by the members' practices.
310:A collective that satisfies Assumption~\ref{ass:political-power:plurality} and clause (i) of Assumption~\ref{ass:political-power:persistence} implements the rule-making function in sense (a). If it also satisfies Assumptions~\ref{ass:political-power:change} and~\ref{ass:political-power:persistence}, it implements the function in sense (b), with at least $r$ replacements of the rule system on $T$. Whenever a replacement is chosen from the viable set $\mathcal{V}(e_{t+1})$ and members' preferences diverge over that set in the sense of Definition~\ref{def:political-power:rule-system}, the replacement is itself a selection among divergent preferences.
314:The first statement is Lemma~\ref{lem:political-power:choice}. The second is Lemma~\ref{lem:political-power:change}. For the third, apply Lemma~\ref{lem:political-power:choice} to the choice of $R_{t+1}$ from $\mathcal{V}(e_{t+1})$, treating the choice of a rule system as a collective decision.
343:Let $N_a\subseteq N$ be the adult members of a group, $|N_a|=n_a\ge2$, and let the group make collective decisions by consensus, modeled as unanimity among the adults (a proposal wins exactly when every member of $N_a$ assents), with the status quo $q$ as default. Let each adult $i$ have a strict linear order $\succ_i$ over alternatives and assent to a proposal $x$ against $q$ if and only if $x\succ_i q$. Then:
345:\item the de jure concentration of rule making is $H^{\pP}=1/n_a$, the minimum possible for a procedure in which only adults' consent counts, and the minimum for the whole group when $N_a=N$;
346:\item the set of alternatives that can replace $q$ is the set of strict Pareto improvements for the adults, $\{x: x\succ_i q \text{ for all } i\in N_a\}$, which is empty whenever $q$ is Pareto optimal among them;
347:\item let the group be able to split, with each subgroup $N_1\subseteq N_a$ of at least two adults deciding by consensus for itself. A subgroup can replace $q$ if and only if all its members strictly prefer a common alternative $x$ to $q$, so some subgroup can do so if and only if at least two adults strictly prefer a common alternative to $q$. This condition can hold when $q$ is Pareto optimal among all adults.
352:(a) The procedure is the unanimity game on $K=N_a$, so Proposition~\ref{prop:political-power:concentration}(d) gives $\varphi_i=1/n_a$ for adults, $\varphi_i=0$ for others, and $H^{\pP}=1/n_a$. Any procedure in which only adults can be the pivot has shares summing to one over $N_a$, so Proposition~\ref{prop:political-power:concentration}(b) applied to $N_a$ shows that $1/n_a$ is the minimum. (b) Under unanimity an alternative replaces $q$ only if every adult prefers it to $q$, which is the definition of a strict Pareto improvement among the adults. If $q$ is Pareto optimal among them, no alternative is strictly preferred to $q$ by every adult, so the set is empty. (c) Apply (b) to $N_1$: its consensus winset is $\{x: x\succ_i q\text{ for all }i\in N_1\}$, which is nonempty exactly when its members share an alternative they all prefer to $q$. If two adults $i,j$ both prefer some $x$ to $q$, the subgroup $\{i,j\}$ qualifies; conversely any qualifying subgroup contains two such adults. For the last claim, take three adults with $x\succ_1 q$, $x\succ_2 q$, and $q\succ_3 y$ for every $y\neq q$: then $q$ is Pareto optimal among all three, yet $\{1,2\}$ can adopt $x$.
357:Formal consensus sets only a lower bound on the concentration of rule making in these societies. Even where every adult can block a decision, differences in age, gender, skill, and kinship give some speakers more weight in discussion than others, so actual concentration exceeds the de jure figure $1/n_a$. The equal-share coding describes the procedure, not the distribution of influence within it.
382:A third position holds that rule makers need not be controlled by a class to serve it. Lindblom argued that business occupies a privileged position in market societies because governments depend on business investment for economic performance, so that rule makers anticipate business reactions without being directed \citep{lindblom1977}. Winters defined oligarchy as the political use of concentrated wealth for wealth defense and showed that oligarchs can coexist with electoral democracy \citep{winters2011}. Structural arguments of this kind imply that integration between resource control and rule making, $C_{\pF\pP}$, can be high even when no capture link in the source's sense can be documented. They therefore pose a measurement problem for the framework that Part I examines in detail.
437:The appointment channel is the defining instrument. Party committees at each level held lists of posts, the nomenklatura, whose holders they appointed or approved, covering the leadership of ministries, enterprises, courts, newspapers, universities, and the armed forces \citep{hough1979}. In the notation of Definition~\ref{def:political-power:appointment-channel}, the party's appointment share $\alpha_{S,\ell}$ approached one in every pillar. Voslensky, a former Soviet official writing in emigration, described the nomenklatura as a ruling class \citep{voslensky1984}, and Djilas, a Yugoslav dissident, called the party bureaucracy a new class that held collective ownership through political control \citep{djilas1957}. Both accounts come from authors with strong political commitments and should be read alongside the institutional scholarship. Hough and Fainsod described a system of bureaucratic bargaining among ministries and regions, and Lane and Ross found significant divisions within the Soviet ruling elite of 1981 to 1991 \citep{lane1995}. These findings bear on the loyalty of appointees, a parameter formalized in Section~\ref{sec:mechanisms} (Proposition~\ref{prop:political-power:appointment-bound}): appointment by a single party does not guarantee that appointees act as one coalition.
439:The People's Republic of China retains the Leninist structure with important changes. Shirk described the relation between the party's top leaders and the Central Committee as reciprocal accountability: leaders appoint the members of the committee that formally selects them \citep{shirk1993}. Landry showed how the party's control of the appointment and evaluation of local cadres allowed it to decentralize economic decisions without losing political control \citep{landry2008}. Minzner documented a turn after the early 2000s away from legal professionalization and toward mediation and political direction of the courts \citep{minzner2011}, which raises the coupling $C_{\pP\pJ}$.
447:Corporatist bargaining is the first feature that distinguishes this regime type in the rule-making layer. Peak organizations of labor and capital take part in drafting rules about wages, working conditions, and social insurance, which raises the coupling $C_{\pP\pW}$ by design. Within the domains it covers, a tripartite bargain among the government, the labor confederation, and the employers' confederation is a unanimity procedure among three organs, so by Proposition~\ref{prop:political-power:concentration}(d) the organ-level concentration of rule making in those domains is $1/3$. The same arrangement creates a risk of closure: interests that are not organized into the peak associations, such as the unemployed or new categories of workers, may be excluded from rule making that formally includes all producers.
479:Rule making in these monarchies was coupled to the other pillars through the Church and through office. Crowns controlled appointments to high Church office in their territories, which raised $C_{\pP\pI}$; the Gallican tradition in France asserted royal and episcopal liberties against Rome, and Van Kley traces how disputes over Jansenism drew the Parlements into conflict with both crown and papacy \citep{vankley1996}. Venality of judicial and financial offices coupled rule making to resource control and to interpretation, because offices were property that the crown sold and whose holders could resist the crown. Ertman classifies France and Spain as patrimonial absolutist states, in which office holding and fiscal administration were tied to private interests \citep{ertman1997}.
504:Regime type & Principal rule makers & Concentration of rule making & Contestability of rule making \\
506:Market-capitalist & Elected legislatures, executives, and regulatory agencies, with organized interests shaping drafts & Moderate, with several veto players in the formal procedure & High in form, with unequal practical access by economic resources \\
507:Communist party-state & Party leadership and apparatus, with the legislature ratifying & High, through the party's control of appointments in every pillar & Low outside the party and partial within it \\
508:Social democracy & Parliamentary majorities negotiating with peak organizations of labor and capital & Moderate, with long tenure of a dominant party in some cases & High, with a risk of closure to unorganized interests \\
509:Islamic states & Rulers and councils, with jurists holding authority over much of the law & Varies from dispersed classical arrangements to concentrated modern ones & Varies from contested elections in Iran to none in Saudi Arabia \\
510:Catholic monarchies & Crown in council, with Parlements, Cortes, and estates able to delay or refuse & High in theory and lower in practice because of brokerage & Low for replacement and intermittent for oversight \\
511:Secular democracies & Legislatures and executives under a constitution, with courts and agencies holding delegated parts & Low to moderate, depending on majoritarian or consensus design & High, and falling where incumbents tilt the electoral field \\
523:Regime type & Strongest documented coupling & Documented capture risk & Documented check \\
525:Market-capitalist & Resource control to rule making through donations, lobbying, and investment dependence & Privileged access of donors and connected lobbyists & Competing interest groups, elections, and the advantage of the status quo \\
526:Communist party-state & Rule making to every other pillar through appointment lists & Integration of all pillars under one coalition & Factional bargaining and divisions within the elite \\
527:Social democracy & Rule making to production through corporatist bargaining & Exclusion of unorganized groups from negotiated rules & Electoral alternation and open corporatist channels \\
528:Islamic states & Rule making to legitimation and interpretation through religious-legal authority & Clerical vetting of legislation and candidates, and rent allocation & Independent juristic authority, elections in Iran, and brokered rule \\
529:Catholic monarchies & Rule making to legitimation through royal control of Church appointments & Venality of office and dynastic exclusion of replacement & Corporate privileges, registration by Parlements, and revolt \\
530:Secular democracies & Rule making to interpretation through appointments and constitutional review & Erosion of contestability by elected incumbents & Rival institutions and citizen coordination against transgression \\
574:Let $X$ be a set of alternatives, $q\in X$ the status quo, and $K$ a nonempty set of veto players, each with strict preferences $\succ_i$ on $X$. The \emph{winset} of $q$ is $W_K(q)=\{x\in X: x\succ_i q\text{ for all }i\in K\}$, the set of alternatives that every veto player prefers to the status quo \citep{tsebelis2002}. A \emph{pure veto-player procedure} enacts $x$ against $q$ exactly when $x\in W_K(q)$; it is the unanimity game on $K$ of Proposition~\ref{prop:political-power:concentration}(d). In a general simple game membership in $W_K(q)$ is necessary for replacing $q$ but not sufficient.
581:\item If $K\subseteq K'$, then $W_{K'}(q)\subseteq W_K(q)$.
582:\item If some $i\in K$ prefers $q$ to every other alternative, then $W_K(q)=\emptyset$.
588:(a) An alternative in $W_{K'}(q)$ is preferred to $q$ by every member of $K'$, and so by every member of $K$. (b) If $i\in K$ prefers $q$ to every $x\neq q$, no $x$ is preferred to $q$ by $i$, so no $x$ lies in $W_K(q)$. (c) If $K\cap B=\emptyset$, every member of $K$ prefers $x$ to $q$, so $x\in W_K(q)$. If some $i\in K\cap B$, then $i$ prefers $q$ to $x$, so $x\notin W_K(q)$.
597:The source framework defines cross-pillar integration $C_{mn}$ only descriptively, as the extent to which one coalition commands appointments, budgets, sanctions, or agenda in two pillars \citep{largo2026hbs}, and Part VII fixes a formal definition for the series. The appointment channel acquires testable content under one explicit candidate, the coalition-overlap measure. Let $\mathcal{S}$ be a preregistered list of coherent coalitions, groups such as parties, factions, or dynasties that can issue joint directives. For $S\in\mathcal{S}$ let $s^{\pP}(S)$ be the Shapley-Shubik share of the bloc player $p_S$ in the quotient game on $N_S=(N\setminus S)\cup\{p_S\}$, whose winning coalitions are defined for $T\subseteq N\setminus S$ by $T\in\Win_S$ if and only if $T\in\Win$, and $T\cup\{p_S\}\in\Win_S$ if and only if $T\cup S\in\Win$. This bloc share is not in general the sum of the members' separate shares; in the Iranian example of Table~\ref{tab:examples} the two councils hold $1/6+1/6$ separately and $1/2$ as a bloc. Let $\kappa_\ell(S)\in[0,1]$ be the share of decision-relevant control in pillar $\ell$ that is exercised in accordance with the directives of $S$, and set
599:C^{\mathrm{ov}}_{\pP\ell}=\max_{S\in\mathcal{S}}\min\{s^{\pP}(S),\kappa_\ell(S)\}.
606:For a coalition $S$ and an office $o$ let $f_{S,o}\in[0,1]$ be the share of the holder's decisions that follow the directives of $S$. For $S\in\mathcal{S}$ with $\alpha_{S,\ell}>0$ define the loyalty of its appointees as the conditional average
608:\lambda_S=\frac{1}{\alpha_{S,\ell}}\sum_{o\in O_\ell}w_o f_{S,o}\,\mathbf{1}[S\text{ can unilaterally appoint or remove the holder of }o],
610:and set $\lambda_S=0$ when $\alpha_{S,\ell}=0$. Suppose that command in pillar $\ell$ decomposes as $\kappa_\ell(S)=\lambda_S\alpha_{S,\ell}+\gamma_S$, where $\gamma_S\in[0,1-\lambda_S\alpha_{S,\ell}]$ is command exercised through channels other than appointment, such as budgets, sanctions, and informal patronage. Then:
612:\item for every $S\in\mathcal{S}$, $C^{\mathrm{ov}}_{\pP\ell}\ge\min\{s^{\pP}(S),\lambda_S\alpha_{S,\ell}\}$;
613:\item if command runs only through appointment ($\gamma_S=0$ for all $S$) and loyalty is at most $\bar\lambda$ ($\lambda_S\le\bar\lambda$ for all $S$), then $C^{\mathrm{ov}}_{\pP\ell}\le\bar\lambda\max_{S\in\mathcal{S}}\alpha_{S,\ell}$;
614:\item if command runs only through appointment and no listed coalition can unilaterally appoint or remove the holder of any office in $O_\ell$, for example because both appointment and removal require the consent of two bodies controlled by different coalitions, then $C^{\mathrm{ov}}_{\pP\ell}=0$.
619:(a) By Equation~\eqref{eq:overlap}, $C^{\mathrm{ov}}_{\pP\ell}\ge\min\{s^{\pP}(S),\kappa_\ell(S)\}$. Since $\gamma_S\ge0$, $\kappa_\ell(S)\ge\lambda_S\alpha_{S,\ell}$, and the minimum is nondecreasing in each argument. (b) For every $S$, $\min\{s^{\pP}(S),\kappa_\ell(S)\}\le\kappa_\ell(S)=\lambda_S\alpha_{S,\ell}\le\bar\lambda\max_{S'}\alpha_{S',\ell}$; take the maximum over $S$. (c) The hypothesis gives $\alpha_{S,\ell}=0$ for every $S\in\mathcal{S}$ by Definition~\ref{def:political-power:appointment-channel}, and (b) gives $C^{\mathrm{ov}}_{\pP\ell}\le0$.
622:The proposition separates three quantities that comparative accounts often run together. The rule-making share $s^{\pP}(S)$ says how much of rule making the coalition controls. The appointment share $\alpha_{S,\ell}$ says how many posts in another pillar it fills. The loyalty parameter $\lambda_S$ says how far the people it appoints do what it wants. Nomenklatura systems maximize the first two, and part (a) then makes integration high unless loyalty is low. The Soviet evidence of elite divisions \citep{lane1995} and of bureaucratic bargaining \citep{hough1979} concerns loyalty, and so it limits the integration that appointment alone can produce. Parts (b) and (c) identify the check. Requiring the consent of a second body for both appointment and removal closes the appointment channel to any single coalition, and security of tenure lowers loyalty after appointment by removing the threat of dismissal. Under plural appointment any remaining integration must run through budgets, sanctions, or patronage ($\gamma_S$), which tells an investigator where to look.
648:Construct & Indicator & Main weakness \\
650:De jure control shares & Shapley-Shubik shares computed from the written or customary decision procedure & Ignores agenda setting and informal influence \\
651:De facto control shares & Shares of contested decisions in which each actor's position prevails, and survival of each actor's provisions through amendment and veto bargaining & Success can reflect anticipation of others' positions rather than control \\
652:Agenda origin & Shares of enacted rules by originating actor, from legislative records and decree registers & Initiation is a different power from enactment \\
653:Concentration $H^{\pP}$ & Sum of squared shares from either of the two indicators above & Sensitive to the definition of actors as individuals or groups \\
654:Replacement $q^{\mathrm{rep}}$ & Frequency of peaceful turnover of rule makers through elections or regular succession & Turnover can occur within a closed coalition \\
655:Oversight $q^{\mathrm{ovs}}$ & Indices of legislative and judicial constraints on the executive & Formal powers may not be used \\
656:Entry $q^{\mathrm{ent}}$ & Legal and practical freedom to form parties, stand for office, and petition & Practical barriers are hard to code \\
657:Transparency $q^{\mathrm{trn}}$ & Publication of drafts, consultation records, and lobbying registers & Disclosure can be formal and incomplete \\
658:Exit $q^{\mathrm{ext}}$ & Legal and economic cost of leaving the jurisdiction or the group & Exit can substitute for voice and weaken reform \\
659:Appointment share $\alpha_{S,\ell}$ & Share of weighted posts in pillar $\ell$ that a coalition fills without the consent of another body & Requires a list of posts and weights fixed in advance \\
660:Veto players & Number of actors whose consent is required to change a statute & Partisan alignment can merge formally separate veto players \\
699:The boundary between rule making and interpretation is analytical, and it is drawn by act rather than by institution. Common-law courts make rules, constitutional courts shape legislation, and administrative agencies both make and apply regulations. Definition~\ref{def:political-power:boundary} classifies each such act, and the many-to-many role map of the source framework records an institution that does both in both pillars, with the coupling $C_{\pP\pJ}$ measuring how far one coalition controls the two. Part III applies the same classification of mixed acts from the interpretive side.
922:Islamic Republic of Iran. 1989. \emph{Constitution of the Islamic Republic of Iran (1979, revised 1989)}. English translation, Constitute Project. \url{https://www.constituteproject.org/constitution/Iran_1989}.
940:Kingdom of Saudi Arabia. 1992. \emph{Basic Law of Governance (1992, revised 2013)}. English translation, Constitute Project. \url{https://www.constituteproject.org/constitution/Saudi_Arabia_2013}.
1018:Madison, James. 1788. \emph{The Federalist No.~51: The Structure of the Government Must Furnish the Proper Checks and Balances}. Independent Journal, 6 February 1788. \url{https://avalon.law.yale.edu/18th_century/fed51.asp}.

2026-10-22T16:41:54.123941Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "perl -ne '"'$line=$.; $s=$_; $s=~s/'"\\\\[{}"'$%&#_]//g; for(split //,$s){if($_ eq q{{}){push @st,$line} elsif($_ eq q{}}){if(@st){pop @st}else{print qq{extra closing brace at $line'"\\n}}}} "'$d+=tr/$/$/; END{print qq{unclosed opening braces at lines: },join(q{,},@st),qq{'"\\n}; print qq{dollar delimiters: "'$d },($d%2?q{ODD}:q{even}),qq{'"\\n}}' papers/latex/political-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
unclosed opening braces at lines: 
dollar delimiters: 1020 even

2026-10-22T16:42:15.332043Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
codex
Static review found no unmatched environments/braces, missing packages, duplicate labels, undefined references, or missing citation keys. Issues found:

1. **Lines 232–234 and 607–609 — likely overfull display equations.** The textual indicator conditions are too long for the 6-inch text width. Define a short indicator such as `a_{S,o}` in prose, then use:
   ```latex
   \alpha_{S,\ell}=\sum_{o\in O_\ell} w_o a_{S,o}
   ```
   and
   ```latex
   \lambda_S=
   \frac{1}{\alpha_{S,\ell}}
   \sum_{o\in O_\ell} w_o f_{S,o}a_{S,o}.
   ```

2. **Line 690 — inconsistent biblical range formatting.** Change `Rev.\ 17:12 to 13` to `Rev.\ 17:12--13`.

3. **Lines 724, 733, 739, 760, 763, 775, 787, 802, 826, 832, 862, 868, 871, 874, 880, 889, 904, 925, 970, 988, 1012, 1021, 1039, 1054, 1060, 1084, 1105, 1111, 1123, 1129, 1132, 1138, 1141, and 1147 — numeric ranges use hyphens instead of en dashes.** Replace range hyphens with LaTeX double hyphens, e.g. `100--111`, `1981--1991`, and `41(4--5)`. Do not alter hyphens inside DOI strings or compound words.

4. **Lines 724–1147, all bibliography entries containing literal `doi:` — DOI text is non-linking and has poor line-breaking behavior.** Format each DOI using the already-loaded `hyperref`/`url` support, for example:
   ```latex
   \href{https://doi.org/10.1086/290705}
        {\nolinkurl{doi:10.1086/290705}}
   ```
   This also reduces the risk of overfull bibliography lines.

No actual TeX compilation was performed because that would read files beyond the one authorized, so log-dependent underfull/overfull warnings cannot be exhaustively confirmed.

VERDICT: NEEDS_FIX
hook: Stop
hook: Stop
hook: Stop Completed
hook: Stop Completed
tokens used
93,208
Static review found no unmatched environments/braces, missing packages, duplicate labels, undefined references, or missing citation keys. Issues found:

1. **Lines 232–234 and 607–609 — likely overfull display equations.** The textual indicator conditions are too long for the 6-inch text width. Define a short indicator such as `a_{S,o}` in prose, then use:
   ```latex
   \alpha_{S,\ell}=\sum_{o\in O_\ell} w_o a_{S,o}
   ```
   and
   ```latex
   \lambda_S=
   \frac{1}{\alpha_{S,\ell}}
   \sum_{o\in O_\ell} w_o f_{S,o}a_{S,o}.
   ```

2. **Line 690 — inconsistent biblical range formatting.** Change `Rev.\ 17:12 to 13` to `Rev.\ 17:12--13`.

3. **Lines 724, 733, 739, 760, 763, 775, 787, 802, 826, 832, 862, 868, 871, 874, 880, 889, 904, 925, 970, 988, 1012, 1021, 1039, 1054, 1060, 1084, 1105, 1111, 1123, 1129, 1132, 1138, 1141, and 1147 — numeric ranges use hyphens instead of en dashes.** Replace range hyphens with LaTeX double hyphens, e.g. `100--111`, `1981--1991`, and `41(4--5)`. Do not alter hyphens inside DOI strings or compound words.

4. **Lines 724–1147, all bibliography entries containing literal `doi:` — DOI text is non-linking and has poor line-breaking behavior.** Format each DOI using the already-loaded `hyperref`/`url` support, for example:
   ```latex
   \href{https://doi.org/10.1086/290705}
        {\nolinkurl{doi:10.1086/290705}}
   ```
   This also reduces the risk of overfull bibliography lines.

No actual TeX compilation was performed because that would read files beyond the one authorized, so log-dependent underfull/overfull warnings cannot be exhaustively confirmed.

VERDICT: NEEDS_FIX
