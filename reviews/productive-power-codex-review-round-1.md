---
reviewer: codex (OpenAI) gpt-5.6-sol
type: formatting
paper: productive-power
round: 1
date: 2026-10-22T16:18:51Z
---
Reading additional input from stdin...
2026-10-22T16:28:22.973724Z ERROR codex_models_manager::cache: failed to load models cache: missing field `base_instructions` at line 139 column 5
OpenAI Codex v0.145.0
--------
workdir: /Users/mlong/Documents/Development/the-beast-system
model: gpt-5.6-sol
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a16471-3607-7552-923f-db7f9dfba4ed
--------
user
Read ONLY the file papers/latex/productive-power.tex (do not explore other files or directories). Review it for LaTeX formatting issues: compilation errors, missing packages, broken references, inconsistent styling, overfull/underfull boxes, spacing problems. List all issues with line numbers and concrete fixes. End your response with a VERDICT line — exactly one of: VERDICT: PASS (no issues remain) or VERDICT: NEEDS_FIX (issues listed above must be fixed).
warning: Under-development features enabled: chronicle. Under-development features are incomplete and may behave unpredictably. To suppress this warning, set `suppress_unstable_features_warning = true` in /Users/mlong/.codex/config.toml.
warning: clamping SessionEnd hook timeout to 3s in /Users/mlong/.codex/plugins/cache/openai-codex/codex/1.0.6/hooks/hooks.json
2026-10-22T16:28:24.455127Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server linear: OAuth token refresh failed: Server returned error response: invalid_grant: Grant not found
2026-10-22T16:28:26.178624Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server resend: OAuth token refresh failed: Server returned error response: invalid_grant: Refresh token has been revoked
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
I’ll inspect only `papers/latex/productive-power.tex`, with numbered lines, and keep the review limited to LaTeX formatting and likely compilation/layout issues.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'nl -ba papers/latex/productive-power.tex' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	\documentclass[11pt,letterpaper]{article}
     2	
     3	\usepackage[T1]{fontenc}
     4	\usepackage{lmodern}
     5	\usepackage{microtype}
     6	\usepackage[margin=1in]{geometry}      % one-inch margins, as the writing standard specifies
     7	\linespread{1.0}
     8	\setlength{\parskip}{0pt}          % conventional article: indent, no vertical gap
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
    33	
    34	\crefname{assumption}{Assumption}{Assumptions}
    35	
    36	% Pillar labels (sans-serif, series convention) and shared objects
    37	\newcommand{\pF}{\mathsf{F}}
    38	\newcommand{\pP}{\mathsf{P}}
    39	\newcommand{\pJ}{\mathsf{J}}
    40	\newcommand{\pI}{\mathsf{I}}
    41	\newcommand{\pC}{\mathsf{C}}
    42	\newcommand{\pW}{\mathsf{W}}
    43	\newcommand{\Pill}{\mathcal{M}}
    44	\newcommand{\Integ}{\mathcal{I}}
    45	\newcommand{\QW}{Q^{\pW}}
    46	\newcommand{\HW}{H_{\pW}}
    47	
    48	\title{Productive Power and Social Reproduction\\[4pt]
    49	  {\normalsize Part VI of \emph{The Six Pillars of the Beast System}}}
    50	\author{Matthew Long\\
    51	  \small The YonedaAI Collaboration, YonedaAI Research Collective\\
    52	  \small Chicago, IL\\
    53	  \small \texttt{matthew@yonedaai.com} \quad \url{https://yonedaai.com}}
    54	\date{October 2026}
    55	
    56	\begin{document}
    57	\maketitle
    58	
    59	\begin{abstract}
    60	Every governance system consumes resources that someone must produce. This paper treats production, payment and social reproduction as the sixth pillar of a comparative framework in which six functions (resource allocation, rule-making, adjudication, legitimation, sanction and production) are present in every functioning polity. From a maintenance axiom we prove that a persistent collective must produce at a positive average rate and must reproduce its producers through care labor, and that rents, tribute, migration or automation relocate production rather than remove it. The same dependence gives producers a latent veto: when outside revenue falls short of the institutions' maintenance requirement, a collective withdrawal of labor, taxes or trade threatens their persistence. A bargaining model makes the channels exact. Producers' terms rise with their outside option and organized bargaining weight, fall linearly with the concentration of control over productive participation, and lose their withdrawal premium once rents cover the maintenance requirement. Restricting mobility pays only when the value of free exit exceeds the cost of enforcement, a condition that nests Domar's land-labor hypothesis and Brenner's emphasis on class organization. Every instrument that depresses producers' terms is held in another pillar, so the capture of production never originates inside it. A comparison of six regime types finds the function everywhere and its capture only under specific couplings. Read typologically, Revelation 13:16-17 depicts the limiting case in which exchange is conditioned on allegiance. The parameters are not estimated here; nine hypotheses state what would falsify the model.
    61	\end{abstract}
    62	
    63	\section{Introduction}
    64	\label{sec:intro}
    65	
    66	This paper asks who produces the wealth that sustains everything. The question is older than political economy, but it is usually asked in one of two narrow forms. Economists ask how output is divided among wages, profits, rents and taxes. Political scientists ask when those who pay taxes obtain representation. Both forms take for granted something this paper makes explicit: that every governance system, whatever its ideology, runs on a flow of goods and services that its rulers do not themselves produce in sufficient quantity, and that the people who do produce it therefore hold a form of power that no ruler can abolish, only channel, divide or suppress.
    67	
    68	The paper is Part VI of a seven-part series on the six functions that every governance system must perform. The series follows \citet{largo2026hbs}, who proposed a multiplex network model of five institutional functions under the name ``Hierarchy of the Beast System.'' The series splits Largo's rule function into rule-making and adjudication, giving six pillars: financial power $\pF$ (who controls the resources), political power $\pP$ (who makes the laws), judicial power $\pJ$ (who interprets the laws), ideological power $\pI$ (who shapes the beliefs), coercive power $\pC$ (who enforces the rules) and productive power $\pW$ (who produces the wealth that sustains everything). The thesis of the series is that the ideology changes and the institutional functions remain. ``Beast System'' names that universal six-function structure. It is never a label for a religion, a people, a profession, a regime or a person.
    69	
    70	Two propositions organize the series and must be kept apart. Proposition A, proved in general in Part VII \citep{long2026formalized}, states that every functioning governance system contains all six functions together with dependency relations among them. Proposition B describes capture: the functions become concentrated or coordinated so that independent accountability fails. Proposition B is contingent and measurable, and Part VII proves that A does not imply B. Each pillar paper derives its own pillar from one axiom, shows the pillar's minimal form in stateless and consensus societies, compares how the function is distributed across six regime types, and states when coordination in the pillar becomes capture.
    71	
    72	For production the derivation is short and the consequences are not. The maintenance axiom says that the group and its institutions consume resources that someone produces. From it we prove that a persistent collective must implement production at a positive average rate (Lemma~\ref{thm:productive-power:necessity}), that it must reproduce its producers through care labor or import producers raised elsewhere (Lemma~\ref{lem:productive-power:reproduction}), that systems apparently freed from their producers by rents, tribute or machines have relocated production rather than escaped it (Lemma~\ref{lem:productive-power:relocation}), and that dependence on production gives producers a latent veto over the system's persistence whenever outside revenue falls short of the maintenance requirement (Proposition~\ref{prop:productive-power:latent-veto}). The dependence is mutual. Producers depend on access to land, tools, employers, markets and protection; rulers depend on the flow those producers generate. Largo insists that the working population is active rather than passive and that taxation is not automatically extraction \citep{largo2026hbs}. The latent veto is the formal content of that insistence.
    73	
    74	Whether the latent veto becomes effective bargaining power depends on a small number of quantities that differ sharply across regimes. A bargaining model in Section~\ref{sec:mechanisms} identifies them: the producers' outside option, their organized bargaining weight, the concentration of control over productive participation, the share of the ruling coalition's revenue that comes from outside production, and whether access to exchange is conditioned on allegiance. The model yields five main results with proofs. Mean outside options fall linearly with the Herfindahl concentration of employers (Lemma~\ref{lem:productive-power:concentration}). Restricting producers' mobility pays exactly when the value of free exit exceeds the cost of enforcement, which unifies Domar's land-labor hypothesis with Brenner's class-organization critique (Proposition~\ref{prop:productive-power:domar}). Organized producers obtain a share above their exit floor and a premium from the threat of withdrawal (Proposition~\ref{prop:productive-power:voice}). Non-tax revenue removes that premium only up to the point where it covers the maintenance requirement (Proposition~\ref{prop:productive-power:rentier}). A participation gate drives unorganized producers toward their autarky value (Proposition~\ref{prop:productive-power:gate}).
    75	
    76	The model also locates capture. Every instrument that depresses producers' terms (mobility restriction, concentration of productive means, suppression of organization, control of exchange, command over rents) is exercised in a pillar other than $\pW$. The capture of production is therefore never a fact about production alone. It requires coupling between $\pW$ and at least one of $\pC$, $\pF$, $\pP$ or $\pI$ (Corollary~\ref{cor:productive-power:coupling}), which is why Largo's strong classification demands high cross-pillar integration as well as concentration \citep{largo2026hbs}.
    77	
    78	The comparative analysis in Section~\ref{sec:comparison} applies the same questions to market-capitalist societies, communist party-states, social democracies, Islamic states, historical Catholic monarchies and secular democracies. Each has the productive function. The regimes differ in who sets the terms of participation, how concentrated that control is, which other pillars it is coupled to, and which channels of exit and voice remain open. Documented episodes of capture appear in several regime types, and so do documented checks. Neither list tracks ideology.
    79	
    80	The paper closes with a typological reading of Revelation 13 and 18. The image of a mark without which ``no man might buy or sell'' (Rev 13:17) is a precise picture of the limiting case of the gate proposition: access to exchange conditioned on allegiance, with exit closed. The reading identifies no present-day government, technology or person with the image, and it is presented as an interpretive claim of the project rather than as exegesis.
    81	
    82	The contributions are four. The paper derives the productive pillar from the maintenance axiom and states the falsifier of that derivation. It gives a bargaining model whose comparative statics connect labor economics, fiscal sociology, rentier-state theory and the history of unfree labor in one notation. It compares the six regime types on equal terms. And it states nine hypotheses, each with the observation that would refute it.
    83	
    84	\section{The productive layer}
    85	\label{sec:layer}
    86	
    87	\subsection{Shared notation}
    88	
    89	The objects in this subsection are defined by \citet{largo2026hbs} and used throughout the series without redefinition. The polity at time $t$ is a directed multiplex network $G_t=(V_t,E_t)$ whose vertices are organizations or coherent actor groups. Each pillar $m$ in the index set $\Pill=\{\pF,\pP,\pJ,\pI,\pC,\pW\}$, with $M=|\Pill|=6$, contributes a layer with adjacency $A^m_t$ and edge weights $a^m_{ij,t}\in[0,1]$ that record the documented capacity of actor $i$ to constrain a feasible action of actor $j$ through mechanism $m$. The role map assigns each vertex a set of pillars, many to many. In pillar $m$, actor $i$ holds a control share $s^m_{i,t}$ with $\sum_i s^m_{i,t}=1$; concentration is the Herfindahl index $H_{m,t}=\sum_i (s^m_{i,t})^2$ and contestability is $Q_{m,t}\in[0,1]$. The illustrative unaccountable-concentration index is $U_t=\sum_m \omega_m H_{m,t}(1-Q_{m,t})$ with preregistered weights $\omega_m\ge 0$ summing to one. Cross-pillar integration $C_{mn,t}\in[0,1]$ measures the extent to which one coalition commands appointments, budgets, sanctions or agenda in both $m$ and $n$, and the integration statistic is $\Integ_t=\frac{2}{M(M-1)}\sum_{m<n}C_{mn,t}$ over fifteen pairs. A capture link $(i\to j,m)$ is an influence that gives privileged access or discretion, weakens otherwise applicable accountability or contestability, and is tied by material evidence to an institutional output. The state vector $x_t=(F_t,P_t,J_t,I^{\mathrm{cap}}_t,C_t,W_t)$ collects aggregate pillar capacities, with dynamics $x_{t+1}=B_tx_t+D_tz_t+\epsilon_t$.
    90	
    91	Two conventions avoid clashes. Pillar labels are sans-serif, so $\pI$ is the ideological pillar and $\Integ_t$ is the integration statistic. No symbol for the wage is introduced; $W_t$ is the productive entry of the state vector and $\pW$ is the pillar label.
    92	
    93	\subsection{Pillar-specific definitions}
    94	
    95	\begin{definition}[Maintenance function]
    96	\label{def:productive-power:maintenance}
    97	The \emph{maintenance function} of a collective is the set of activities that produce, pay for and reproduce the material means on which the collective and its institutions run. It includes paid and unpaid labor, cultivation and herding, craft and manufacture, extraction, trade that moves goods to where they are consumed, enterprise, the payment of taxes, tithes, tribute and dues, consumption that sustains producers and their enterprises, and the household work of care and child-rearing that reproduces the producers themselves. The productive pillar $\pW$ is the layer of $G_t$ in which these activities and the claims on them are organized.
    98	\end{definition}
    99	
   100	The definition is deliberately wide. Largo's fifth function already includes households, workers, taxpayers, small businesses, consumers and caregivers \citep{largo2026hbs}. The household is included because a collective that persists over generations must reproduce its members, and historians of social reproduction have documented how much of that work is unpaid and gendered \citep{laslett1989}. Large holders of capital appear in $\pW$ in their capacity as organizers of production and in $\pF$ in their capacity as allocators of resources; the role map is many to many and does not force a choice.
   101	
   102	\begin{definition}[Maintenance requirement and persistence]
   103	\label{def:productive-power:persistence}
   104	Let $K_t$ be the \emph{institutional maintenance requirement}: the resources consumed in period $t$ by the institutions that realize the six functions, including the subsistence of their full-time personnel. Let $Z_t$ be the subsistence of all other members, and $K^{\mathrm{tot}}_t=Z_t+K_t$ the collective's total consumption. Let $X_t\ge 0$ be the stock of usable resources held by the collective at the start of period $t$ and $Y_t\ge 0$ the inflow of usable resources during $t$; the stock evolves as $X_{t+1}=X_t+Y_t-K^{\mathrm{tot}}_t$. The collective \emph{persists} on a horizon $\{0,\dots,T\}$ if $X_t\ge 0$ for every $t$ in the horizon, and persists indefinitely if this holds for every $T$. Within the stock, the institutions hold a part $X^S_t\ge 0$ (a treasury, granary or endowment) that receives the transfers $T_t$ from producers and any non-producer revenue $R_t$ and evolves as $X^S_{t+1}=X^S_t+T_t+R_t-K_t$; the institutions persist while $X^S_t\ge 0$.
   105	\end{definition}
   106	
   107	\begin{definition}[Producers, extraction and non-producer revenue]
   108	\label{def:productive-power:surplus}
   109	A \emph{producer} is an agent whose activity in period $t$ contributes to $Y_t$, together with any agent who owns, operates or maintains equipment that does. In the stationary model of Section~\ref{sec:mechanisms} there are $n$ producers, each producing $y>0$ per period. A governing coalition $S$ receives a fraction $\chi$ of output (taxes, rents, dues, profits or procurement deliveries, net of services returned) and the producer retains $(1-\chi)y$. The coalition also receives \emph{non-producer revenue} $R_t\ge 0$ that does not come from its own producers: rents from resources sold abroad, tribute, foreign aid or remittances. In the stationary model the producers' transfer is $T_t=\chi ny$, and the coalition's \emph{producer dependence} is $\xi_t=T_t/(T_t+R_t)$.
   110	\end{definition}
   111	
   112	The extraction share $\chi$ is net of services returned. A tax that finances schooling or roads which producers value is not extraction in the sense used here, and the model treats such services as part of what producers receive. This follows Largo's warning that taxation is not automatically extraction and that incidence must be established before a flow is called extractive \citep{largo2026hbs}.
   113	
   114	The series uses the word slavery only in Largo's disciplined, explicitly metaphorical sense, and the comparisons below depend on keeping forms of labor apart. Table~\ref{tab:bondage} defines the forms that recur in the comparative analysis by four criteria: whether the producer may lawfully leave, whether the obligation rests on contract or on sanction, whether the producer's person is owned, and whether the producer keeps the remainder of output after the obligation is met.
   115	
   116	\begin{definition}[Bondage spectrum]
   117	\label{def:productive-power:bondage}
   118	A form of productive obligation is classified by the four criteria of Table~\ref{tab:bondage}. \emph{Wage labor} and \emph{taxation} leave lawful mobility and personal ownership with the producer. \emph{Serfdom} ties the producer to land or lord and compels dues or labor. \emph{Compelled state labor} (corv\'ee, labor drafts, penal labor) is compelled by sanction for a term. \emph{Chattel slavery} makes the person property. The word ``bondage'' is reserved for forms that legally restrict mobility and compel labor; wage labor and taxation are not called slavery in this paper.
   119	\end{definition}
   120	
   121	\begin{table}[t]
   122	\centering
   123	\small
   124	\caption{The bondage spectrum. Each row is a form of productive obligation classified by four criteria; the comparative analysis uses these terms and no others.}
   125	\label{tab:bondage}
   126	\begin{tabularx}{\textwidth}{@{}L{2.6cm}YYYY@{}}
   127	\toprule
   128	Form & May the producer lawfully leave? & Basis of the obligation & Is the person owned? & Who keeps the remainder? \\
   129	\midrule
   130	Wage labor & Yes, subject to notice and contract & Contract, under law & No & The worker keeps the wage \\
   131	Taxation & Yes, subject to emigration rules & Law, enforced by sanction & No & The taxpayer keeps income after tax \\
   132	Serfdom & No, the producer is tied to land or lord & Custom and law, enforced by the lord and the state & No, though some regimes allowed sale with or without land & The household keeps output after dues and labor service \\
   133	Compelled state labor & No, for the term of the draft or sentence & Sanction by the state & No & Little or nothing during the term \\
   134	Chattel slavery & No & Ownership, enforced by the state & Yes & The owner \\
   135	\bottomrule
   136	\end{tabularx}
   137	\end{table}
   138	
   139	Hirschman's distinction between exit and voice is the standard vocabulary for the options of members facing a declining organization \citep{hirschman1970}. Largo adopts it for the productive function \citep{largo2026hbs}, and this Part owns its use in the series.
   140	
   141	\begin{definition}[Exit, voice and loyalty in the productive layer]
   142	\label{def:productive-power:evl}
   143	A producer's \emph{outside option} $o$ is the per-period value available if the producer stops participating on the current terms: another employer, free land, migration, a subsistence plot, or a cooperative. \emph{Exit} is the exercise of that option. \emph{Voice} is collective or individual action to change the terms without leaving (petitions, lawsuits, strikes, tax refusal, boycotts, votes); its effectiveness in the model is the \emph{organized bargaining weight} $\eta\in[0,1]$, with $\eta=0$ for atomized producers. \emph{Loyalty} is attachment that raises the threshold at which a producer exits, which can make voice possible by keeping members inside long enough to use it \citep{hirschman1970}.
   144	\end{definition}
   145	
   146	\begin{definition}[Productive contestability]
   147	\label{def:productive-power:qw}
   148	The contestability of the productive pillar, $\QW_t:=Q_{\pW,t}$, is a preregistered aggregate of five components in $[0,1]$: bargaining coverage $q^{\mathrm{bar}}$ (the share of producers whose terms are set or reviewed collectively), mobility $q^{\mathrm{mob}}$ (lawful and practical ability to change employer, residence or occupation, including portability of benefits), legal access $q^{\mathrm{leg}}$ (access to independent adjudication of disputes over terms), income protection $q^{\mathrm{inc}}$ (replacement of income during unemployment, illness and old age), and voice $q^{\mathrm{voi}}$ (lawful ability to organize, strike, petition and vote over the terms of taxation).
   149	\end{definition}
   150	
   151	The five components follow Largo's list for the productive function: bargaining, legal protection, mobility, representation and income protection \citep{largo2026hbs}. They are separate because they fail separately. A worker can have the vote and no union, a union and no portable pension, or a labor court and no means to reach it. Legal access belongs to the judicial pillar as well. Part III \citep{long2026judicial} owns the analysis of legal mobilization (its Proposition 6.4) and the components of judicial contestability (its Definition 2.4): disclosure of a defective decision, access to a challenge, independence of the reviewing forum, and compliance with its ruling.
   152	
   153	The concentration $H_{\pW,t}$ is computed on shares of decision-relevant control over the terms of productive participation. In a labor market the natural proxy is the employment or vacancy share of each employer, which is how \citet{azar2022} measure labor-market concentration. Where the state is the dominant employer or the sole purchaser of farm output, its share approaches one. Where every household controls its own labor and land is open, shares are close to $1/n_h$ for $n_h$ households.
   154	
   155	\subsection{The production game}
   156	
   157	The mechanisms of Section~\ref{sec:mechanisms} and the comparisons of Section~\ref{sec:comparison} use one stationary model, defined here and analyzed in Section~\ref{sec:mechanisms}.
   158	
   159	\begin{definition}[Production game]
   160	\label{def:productive-power:game}
   161	In each period a coalition $S$ governs $n$ identical producers. A participating producer produces $y>0$. The coalition and the producers agree on terms $u$, the per-producer value the producer retains (consumption plus the money value of services and concessions received); the extraction share is $\chi=1-u/y$, which is negative when producers receive net transfers. The coalition's revenue is $n(y-u)+R$, where $R\ge 0$ is non-producer revenue, and it must meet the institutional maintenance requirement $K>0$ of Definition~\ref{def:productive-power:persistence}. Producers' own subsistence is covered by $u$, so $K$ contains only the cost of the institutions. A producer who does not participate obtains the outside option $o$, with $y_0\le o\le y$, where $y_0$ is the autarky value of a producer cut off from exchange.
   162	\end{definition}
   163	
   164	The coalition objective of \citet{largo2026hbs}, $\Pi=B(p)+\rho(c)-\kappa(g)-\phi(\cdot)$, is the general form of which the coalition's payoff here is a special case. The net revenue $n(y-u)$ is a component of the material benefit $B$, and the mobility restriction $g$ defined next is an instance of the source's coercive measures with cost $\kappa(g)$.
   165	
   166	\begin{definition}[Instruments on the outside option]
   167	\label{def:productive-power:gate}
   168	A \emph{mobility restriction} $g\in[0,1]$ is the probability that a producer who tries to leave is prevented: tying peasants to land, internal passports, residence permits tied to an employer. A \emph{participation gate} $\gamma\in[0,1]$ is the probability that a producer who withholds allegiance from the coalition retains access to exchange (buying inputs, selling output, credit, being hired); otherwise the producer falls to the autarky value $y_0$. Employment shares $s_j=s^{\pW}_j$ of employers $j=1,\dots,J$ define the concentration $\HW=\sum_j s_j^2$.
   169	\end{definition}
   170	
   171	\begin{definition}[Composite outside option]
   172	\label{def:productive-power:outside}
   173	Let $o_1>y_0$ be the value of an offer from a competing employer. The outside option of a producer at employer $j$ is
   174	\[
   175	o_j=y_0+\gamma\,(1-g)\,(1-s_j)\,(o_1-y_0),
   176	\]
   177	and the employment-weighted mean outside option is $\bar o=\sum_j s_jo_j=y_0+\gamma(1-g)(1-\HW)(o_1-y_0)$.
   178	\end{definition}
   179	
   180	Each factor of the composite form is a probability that the producer's exit succeeds: the producer is not blocked from leaving ($1-g$), keeps access to exchange ($\gamma$), and finds a different employer ($1-s_j$, justified in Lemma~\ref{lem:productive-power:concentration}). When an exit fails the producer receives the fallback $y_0$. Unrestricted producers facing many small employers obtain nearly $o_1$; a closed gate, a complete restriction or a single employer each holds them at $y_0$.
   181	
   182	\section{Necessity of the pillar}
   183	\label{sec:necessity}
   184	
   185	\subsection{The maintenance axiom}
   186	
   187	Part VII owns the axiom set from which the series derives Proposition A. The sixth axiom concerns this pillar.
   188	
   189	\begin{assumption}[Ax6, maintenance]
   190	\label{ass:productive-power:ax6}
   191	There are constants $k\ge k_S>0$ with $K^{\mathrm{tot}}_t\ge k$ and $K_t\ge k_S$ for every $t$: the group and its institutions consume resources in every period. The initial stocks $X_0$ and $X^S_0$ are finite.
   192	\end{assumption}
   193	
   194	The axiom is empirical, not logical. A population that consumed nothing would not need production, and the derivation below would fail for it. No human collective satisfies that description, since members eat and institutions occupy time that could otherwise produce food. The finite initial stock excludes inexhaustible inheritances.
   195	
   196	\begin{assumption}[No manna]
   197	\label{ass:productive-power:nomanna}
   198	Inflows are produced: $Y_t>0$ only if some agent, inside or outside the collective, performs productive activity in period $t$ or owns, operates or maintains equipment that does.
   199	\end{assumption}
   200	
   201	The no-manna assumption converts the accounting identity of Definition~\ref{def:productive-power:persistence} into a claim about activity. Wild foods require gathering, oil requires extraction, and a gift requires a giver who produced or acquired what is given. The assumption fails only for resources that arrive with no human act at any point in the chain, and the scarcity axiom of the series (Ax1, which states that resources are finite and that claims on them conflict) makes any such free stock finite.
   202	
   203	\subsection{Necessity and relocation}
   204	
   205	\begin{lemma}[Necessity of the maintenance function]
   206	\label{thm:productive-power:necessity}
   207	Under Assumptions~\ref{ass:productive-power:ax6} and~\ref{ass:productive-power:nomanna}, if a collective persists indefinitely then for every $T\ge 1$
   208	\[
   209	\frac{1}{T}\sum_{t=0}^{T-1}Y_t\;\ge\;k-\frac{X_0}{T},
   210	\]
   211	so the long-run average inflow is at least $k>0$, and productive activity occurs in infinitely many periods.
   212	\end{lemma}
   213	
   214	\begin{proof}
   215	Iterating the stock equation gives $X_T=X_0+\sum_{t<T}(Y_t-K^{\mathrm{tot}}_t)$. Persistence requires $X_T\ge 0$, hence $\sum_{t<T}Y_t\ge\sum_{t<T}K^{\mathrm{tot}}_t-X_0\ge Tk-X_0$. Dividing by $T$ gives the displayed bound, and its right side tends to $k$ as $T\to\infty$. If productive activity occurred in only finitely many periods, Assumption~\ref{ass:productive-power:nomanna} would make $Y_t=0$ from some period on, so $\sum_{t<T}Y_t$ would be bounded while $Tk-X_0$ grows without bound, a contradiction.
   216	\end{proof}
   217	
   218	The lemma establishes the existence of the activity, not of any institution that organizes it. Wage labor, serfdom, the household farm, the kolkhoz and the cooperative are alternative ways of implementing the same function. This is the distinction \citet{hempel1959} required of functional analysis: a functional requirement does not entail any particular institution, because functional equivalents may satisfy it. Nor does the lemma explain why a given regime has the productive institutions it has. \citet{elster1983} showed that explanation by beneficial consequences needs a feedback mechanism from the effect to the trait. The lemma is a condition of persistence, and it makes no causal claim about the origin of institutions.
   219	
   220	A collective can persist while its own members produce little or nothing. The next lemma shows what such persistence requires.
   221	
   222	\begin{lemma}[Relocation]
   223	\label{lem:productive-power:relocation}
   224	Split the inflow as $Y_t=Y^{\mathrm{in}}_t+Y^{\mathrm{out}}_t$, where $Y^{\mathrm{in}}_t$ is produced by members and $Y^{\mathrm{out}}_t$ by non-members and transferred to the collective. Under Assumptions~\ref{ass:productive-power:ax6} and~\ref{ass:productive-power:nomanna}, if a collective persists indefinitely and $Y^{\mathrm{in}}_t=0$ for all $t\ge t_0$, then non-members produce for the collective in infinitely many periods, and for every $T>t_0$ the transferred output satisfies $\sum_{t_0\le t<T}Y^{\mathrm{out}}_t\ge (T-t_0)k-X_{t_0}$.
   225	\end{lemma}
   226	
   227	\begin{proof}
   228	Apply Lemma~\ref{thm:productive-power:necessity} to the collective from period $t_0$ with initial stock $X_{t_0}$, which is finite because each $X_t$ is finite. From $t_0$ on, $Y_t=Y^{\mathrm{out}}_t$, so the bound becomes the displayed inequality, and productive activity by non-members occurs in infinitely many periods.
   229	\end{proof}
   230	
   231	The transfer in Lemma~\ref{lem:productive-power:relocation} is an edge of the productive layer between the collective and producers outside its membership. It can take the form of tribute extracted by force, rents paid by foreign buyers for oil extracted by migrant workers, alms and endowments given to a religious community, or foreign aid financed by taxpayers elsewhere. Each moves the producers out of the membership and usually out of the polity's channels of voice. None removes them.
   232	
   233	Automation is the hardest version of the relocation argument. If equipment performs all productive activity, Definition~\ref{def:productive-power:surplus} still assigns the producer role to whoever owns, operates or maintains the equipment. Control over the productive layer then coincides with ownership of equipment, a relation that also belongs to $\pF$, and $\HW$ tracks the concentration of that ownership. The function survives full automation. The bargaining power of human labor, analyzed below, does not survive it automatically: it depends on human activity remaining necessary somewhere in the chain. That dependence is an empirical condition of present technology, not a consequence of the axiom, and the paper's claims about labor are narrowed accordingly.
   234	
   235	The producers must themselves be produced. A collective that persists beyond the working lives of its present members depends on the care and child-rearing that \citet{laslett1989} call social reproduction, most of it unpaid. The next lemma states the dependence.
   236	
   237	\begin{lemma}[Reproduction]
   238	\label{lem:productive-power:reproduction}
   239	Let the number of producers evolve as $n_{t+1}=(1-d)n_t+bh_t+m_t$, where $d\in(0,1]$ is the rate at which producers leave work through death, age or illness, $h_t\ge 0$ is care labor performed in period $t$, $b>0$ is the number of future producers sustained per unit of care, and $m_t\ge 0$ is the net arrival of producers raised elsewhere. If $h_t=m_t=0$ for all $t\ge t_0$, then $n_{t_0+j}=(1-d)^jn_{t_0}$, and members' output $n_ty$ falls below any fixed $k>0$ after finitely many periods. A collective that persists indefinitely on members' production therefore requires care labor, or the arrival of producers raised elsewhere, in infinitely many periods.
   240	\end{lemma}
   241	
   242	\begin{proof}
   243	With $h_t=m_t=0$ the recursion is $n_{t+1}=(1-d)n_t$, whose solution is $(1-d)^jn_{t_0}$; this tends to zero because $0\le 1-d<1$, so $n_ty<k$ for all large $t$. If care and arrivals were zero from some period on, members' production would fall below $k$ from some period on, and Lemma~\ref{thm:productive-power:necessity} would require inflows produced by non-members, contradicting persistence on members' production.
   244	\end{proof}
   245	
   246	The lemma puts unpaid household work inside the maintenance function on the same footing as paid work. It also shows a second form of relocation. A labor regime that imports adult migrants ($m_t>0$) draws on care performed in the migrants' places of origin, so the cost of reproducing its producers is borne outside the polity, as the cost of producing its rents is in Lemma~\ref{lem:productive-power:relocation}.
   247	
   248	\subsection{The latent veto}
   249	
   250	Dependence on production runs in both directions. Producers depend on land, tools, employers, buyers and protection. The coalition that governs depends on the flow that producers generate. The next proposition states the second dependence as a bound.
   251	
   252	\begin{proposition}[Latent veto]
   253	\label{prop:productive-power:latent-veto}
   254	Suppose Assumption~\ref{ass:productive-power:ax6} holds, the institutions' non-producer revenue satisfies $R_t\le\bar r$ for all $t$ with $\bar r<k_S$, and from period $t_0$ on the producers withdraw completely, so that their transfers are $T_t=0$. Then the institutions fail to persist no later than period $t_0+\lfloor X^S_{t_0}/(k_S-\bar r)\rfloor+1$.
   255	\end{proposition}
   256	
   257	\begin{proof}
   258	For $t\ge t_0$ the institutional stock of Definition~\ref{def:productive-power:persistence} satisfies $X^S_{t+1}=X^S_t+R_t-K_t\le X^S_t-(k_S-\bar r)$. After $j$ periods of withdrawal, $X^S_{t_0+j}\le X^S_{t_0}-j(k_S-\bar r)$, which is negative for the smallest integer $j$ exceeding $X^S_{t_0}/(k_S-\bar r)$, that is, for $j=\lfloor X^S_{t_0}/(k_S-\bar r)\rfloor+1$.
   259	\end{proof}
   260	
   261	The proposition is elementary, and its content lies in what it rules out. No governance system whose non-producer revenue stays below its institutional maintenance requirement can survive the complete and permanent withdrawal of its producers. The producers therefore hold, collectively, a veto over persistence. The veto is latent because exercising it requires coordination that atomized producers lack \citep{olson1965}, because the coalition may meet withdrawal with coercion, and because the producers bear their own costs of withdrawal. Section~\ref{sec:mechanisms} prices these obstacles. When $R_t\ge K_t$ the bound fails, and the veto passes to whoever produces the rents (Lemma~\ref{lem:productive-power:relocation}).
   262	
   263	Largo states the same mutual dependence in prose: the working population is active, dependency is not powerlessness, and concentration elsewhere translates into material dependency only where workers lack bargaining, legal protection, mobility and representation \citep{largo2026hbs}. Proposition~\ref{prop:productive-power:latent-veto} supplies the reason the population is active. It is part of the structure on which everything else rests.
   264	
   265	\subsection{Minimal form in stateless and consensus societies}
   266	
   267	Proposition A predicts that each function exists in societies with no state, no chiefs with coercive power and strong egalitarian norms. For production the prediction is easy to confirm and the interesting question is different: why does production in these societies so rarely support a class that extracts from producers? The formal part of the answer is an exit argument.
   268	
   269	\begin{proposition}[Minimal form]
   270	\label{prop:productive-power:minimal-form}
   271	Consider a band in which every household controls its own labor, any household can leave the camp and obtain the same output $y$ elsewhere on open land, and leaving costs nothing. Then (a) the maintenance function is implemented by the households themselves, and (b) no member or coalition can sustain a positive extraction share $\chi>0$ from any household that is free to leave.
   272	\end{proposition}
   273	
   274	\begin{proof}
   275	Part (a) is Lemma~\ref{thm:productive-power:necessity} applied to the band, with producers identified as household members. For (b), a household asked to surrender $\chi y>0$ obtains $(1-\chi)y$ by staying and $y$ by leaving, so leaving is strictly better. A demand for $\chi>0$ is therefore not met by any household that is free to leave.
   276	\end{proof}
   277	
   278	The ethnography supplies the premises and shows where they fail. Table~\ref{tab:hardcases} summarizes the cases the series uses.
   279	
   280	\begin{table}[t]
   281	\centering
   282	\small
   283	\caption{Minimal form of the productive function in the hard cases. The right column records the strongest reading on which the function, or its accountability, might be absent.}
   284	\label{tab:hardcases}
   285	\begin{tabularx}{\textwidth}{@{}L{2.5cm}YY@{}}
   286	\toprule
   287	Case & Who produces and on what terms & Strongest counter-reading and reply \\
   288	\midrule
   289	Ju/'hoansi \citep{lee1979,marshall1976} & Men and women forage, sharing rules distribute meat, and gift exchange links camps & No one commands labor. Reply: production is universal and its terms are policed by leveling talk \citep{wiessner2005} \\
   290	Immediate-return foragers \citep{woodburn1982} & Food is consumed soon after it is obtained and accumulation is discouraged & Egalitarianism looks like the absence of power. Reply: it is produced by institutions of leveling \\
   291	Nuer \citep{evanspritchard1940} & Herding, horticulture and fishing are organized by households and kin & Evans-Pritchard stressed the absence of government. Reply: cattle rights and exchange organize production without an office \\
   292	Amazonian chiefs \citep{clastres1987} & Households garden and hunt, and the chief must give and work more & The flow runs from chief to group. Reply: this is a negative extraction share, not an absent function \\
   293	Upland Southeast Asia \citep{scott2009} & Swidden farmers choose crops that are hard to tax & Producers evade the state. Reply: they produce and govern their own terms \\
   294	Commons \citep{ostrom1990} & Users provide labor to maintain irrigation and other common resources & No state allocates labor. Reply: provision rules assign maintenance labor and are monitored \\
   295	\bottomrule
   296	\end{tabularx}
   297	\end{table}
   298	
   299	Among the Ju/'hoansi, production by both sexes is the basis of daily life, and the terms on which its results circulate are governed by sharing rules, gift partnerships and talk \citep{lee1979,lee2013,marshall1976}. \citet{wiessner2005} documented how the Ju/'hoansi enforce such norms, largely through criticism and talk rather than physical punishment. In the vocabulary of this paper, open access and costless fission keep $o$ close to $y$, and leveling sanctions keep it there. \citet{woodburn1982} generalized the point: in immediate-return societies equality is an achievement of institutions that prevent accumulation, not a default. \citet{boehm1999} called the same pattern a reverse dominance hierarchy, in which the group as a coalition dominates would-be dominants.
   300	
   301	Clastres's Amazonian chiefs are the most striking case for this pillar. The chief has no power to command, is expected to be generous, and works harder than others to supply what he gives away \citep{clastres1987}. In the model's terms, the leader's extraction share is negative. Clastres read this as a society actively preventing power from separating from it. That reading supports the distinction between Propositions A and B. The productive function is present, and its capture is prevented.
   302	
   303	Ostrom's commons supply the cleanest institutional image of the maintenance function at small scale. Her design principles require congruence between appropriation rules and provision rules, so that those who draw on an irrigation system or a fishery also contribute the labor that maintains it, under monitoring by the users themselves \citep{ostrom1990,ostromdesign2010}. A review of later studies found broad, though not uniform, support for the principles \citep{cox2010}. Provision rules are the productive pillar in miniature.
   304	
   305	The ethnographic record has limits that bear on the claim. Contact-era ethnographies describe groups living in marginal environments, often already in contact with states and markets, and foraging societies vary widely \citep{kelly1995}. Sahlins's argument that hunter-gatherers met their needs with modest labor \citep{sahlins1972} corrects any picture of constant struggle, but it does not remove production; it lowers its hours. The minimal-form proposition needs only that someone produces and that, where exit is open and costless, no one can take a share.
   306	
   307	\subsection{Counterexample attempts}
   308	
   309	The falsifier of Lemma~\ref{thm:productive-power:necessity} is a governance system that persists indefinitely while supported by no production and no replenishment of its stock. Six candidates come close and fail.
   310	
   311	A community living from an endowment consumes a finite stock unless the endowment earns a return, and a return is someone's production. Monasteries and mendicant orders that live by alms relocate production to donors. A raiding or tributary state relocates it to the raided and the tributary, as Lemma~\ref{lem:productive-power:relocation} predicts; the Spanish colonial labor draft discussed in Section~\ref{sec:comparison} is a documented instance in which the producers were outside the ruling community and inside its coercive reach \citep{dell2010}. A rentier state relocates production to the workers who extract the resource and the foreign buyers who pay for it; in the Gulf monarchies much of the extracting and building labor is done by migrants without citizenship \citep{hanieh2011,kapiszewski2001}. Full automation, as argued above, relocates the producer role to owners and maintainers of equipment. The original affluent society lowers labor hours without eliminating them \citep{sahlins1972}.
   312	
   313	The strongest attempt is the last of these taken to its limit: a society of self-maintaining machines serving a population that does nothing. The function would then be performed by equipment owned by someone, and the claim survives in its functional form. What would not survive is any claim that human labor holds a latent veto. The paper's claims about producer power are therefore conditional on human activity remaining necessary in production. That narrowing is the honest result of the counterexample.
   314	
   315	\section{Literature}
   316	\label{sec:literature}
   317	
   318	Four bodies of work bear on the productive pillar, and they rarely cite one another. Each answers part of the guiding question, and each leaves a gap that the framework of this series is meant to fill.
   319	
   320	The first asks who creates value and how it is divided. For \citet{marx1976}, labor applied to means of production owned by others yields a surplus appropriated as profit, and the compulsion that keeps wage workers at work is economic rather than legal. Polanyi's account of the nineteenth-century market society adds that labor, land and money are fictitious commodities, not produced for sale, and that treating them as commodities provoked a protective countermovement \citep{polanyi1944}. Both accounts locate power in production, but neither supplies a comparative instrument that applies equally to market and command economies. Recent distributional accounting measures who receives national income without asking how the terms were bargained \citep{piketty2018}. Work on social reproduction widens the category of producers to include unpaid household labor \citep{laslett1989}.
   321	
   322	The second body of work locates producers' power in their options and their organization. Hirschman's exit, voice and loyalty frame the options of members of any organization in decline \citep{hirschman1970}. \citet{freeman1984} applied the frame to trade unions, which have a monopoly face that raises wages and a collective-voice face that lets workers change conditions without quitting. \citet{wright2000} distinguished associational power, which comes from organization in unions and parties, from structural power, which comes from workers' position in tight labor markets or strategic sectors. \citet{silver2003} used the distinction to trace labor unrest across a century of relocating industries.
   323	
   324	Power resources theory explains welfare-state variation by the organization of wage earners and their parties \citep{korpi1983,esping1985}. The employer side of the same relation is monopsony: when workers cannot move costlessly between employers, firms set wages below the competitive level \citep{manning2003}, and local labor markets are often concentrated enough for this to matter \citep{azar2022}. These studies measure producer power well within capitalist democracies and say little about serfs, kolkhoz members or migrant workers under sponsorship.
   325	
   326	The third body of work is fiscal sociology, which treats the tax relation as the core of state formation \citep{campbell1993,martin2009}. \citet{levi1988} modeled rulers as revenue maximizers constrained by their bargaining power relative to constituents, by transaction costs and by their discount rates, and showed that compliance is quasi-voluntary: taxpayers comply when they believe others do and the ruler keeps bargains. \citet{bates1985} argued that owners of mobile assets can extract representative concessions. \citet{ross2004} tested the claim that taxation leads to representation and found that the relevant variable is taxation relative to the services government provides, and \citet{timmons2005} found that governments trade services for revenue with the groups that pay.
   327	
   328	Rentier-state theory supplies the converse: revenue that does not come from domestic taxpayers frees rulers from bargaining with them \citep{mahdavy1970,beblawiluciani1987,ross2001}. The converse is contested. \citet{habermenaldo2011} find no evidence that resource reliance promotes authoritarianism over time within countries. Part I \citep{long2026financial} treats rents (its Section 5) on the allocation side; this Part treats them as a change in producers' bargaining position.
   329	
   330	The fourth body of work explains when producers are bound. \citet{domar1970} proposed that serfdom or slavery arises where land is abundant relative to labor, because free peasants could otherwise leave to farm free land, and that free land, free peasants and non-working landowners cannot coexist. \citet{brenner1976} answered that the outcomes of the late-medieval demographic crisis differed across Europe with the same land-labor ratios, and that the balance of organized class power decided them. \citet{dell2010} showed that the Spanish colonial mining draft in Peru left lower household consumption and worse child health in the districts subject to it, centuries after its abolition. \citet{scott1976,scott1985} showed that peasants who cannot exit or speak openly resist through foot-dragging, evasion and gossip, and that they judge extraction against a subsistence ethic.
   331	
   332	The gap is a common instrument. Labor economics, fiscal sociology, rentier theory and the history of bondage each study one or two of the quantities that set producers' terms, in one or two regime types. The model in Section~\ref{sec:mechanisms} places the outside option, organization, employer concentration, non-producer revenue and conditional access to exchange in one notation that applies to a band, a kolkhoz, a Gulf labor camp and a unionized factory. It does not replace the specialized literatures. It shows where they meet.
   333	
   334	\section{Comparative analysis}
   335	\label{sec:comparison}
   336	
   337	Producers' terms were worst, in every regime type that produced such cases, where concentrated control over production was coupled to coercion and to control of exchange; ideology did not decide where this happened. The evidence comes from asking the same questions of each regime type: who produces and pays, who sets the terms of participation, how concentrated that control is, which other pillars it is coupled to, and which channels of exit and voice remain open.
   338	
   339	Two conventions govern the comparison. Where market-capitalist and secular-democratic institutions coexist in one country, the first type is read through the organization of the economy (private capital, labor markets, the structural power of business) and the second through the political organization of the fiscal relation (citizen taxpayers, universal suffrage, social insurance law). Judgments of concentration are qualitative, because no country has been coded under a preregistered scheme, and no value of $U_t$ or $\Integ_t$ is reported.
   340	
   341	\subsection{Market-capitalist societies}
   342	
   343	In market-capitalist societies most producers are wage earners, the self-employed and small businesses, and the terms of production are set mainly by employers in labor markets and by the state through tax and labor law. Consumers sustain enterprises by their purchases and pay a large share of indirect taxes. The holders of the pillar are therefore many, but control over terms is not evenly spread. \citet{azar2022} found that a large share of local labor markets in the United States are highly concentrated by the standard used in antitrust, and that concentration is associated with lower posted wages. Monopsony theory explains why: when moving between employers is costly, employers set wages below the competitive level \citep{manning2003}. In the notation of this paper, $\HW$ varies across local markets and is high in many of them.
   344	
   345	The structural power of business is the distinctive coupling of this regime type. \citet{lindblom1977} argued that because investment decisions are private and governments depend on growth, business holds a privileged position that requires no organization: governments anticipate the reaction of investors. \citet{przeworski1985} drew the consequence for labor parties, which must sustain profits to sustain employment. This is the exit option of mobile capital, and \citet{bates1985} predicted that the owners of mobile assets obtain concessions. The coupling $C_{\pF\pW}$ is high wherever those who allocate capital also set the terms of employment. Part I gives the primary treatment of that pair in its Section 5.
   346	
   347	Accountability in the pillar has rested on three channels: collective bargaining, labor mobility and the vote. Their strength has varied over time. \citet{farber2021} assembled survey data across the twentieth century and found that unions compressed the income distribution when they were strong. \citet{western2011} attributed a substantial part of the rise in American wage inequality after the 1970s to the decline of unions, including through the erosion of norms of fair pay in non-union firms. \citet{piketty2018} documented the same period's shift of pre-tax income toward the top of the distribution. These are documented changes in $q^{\mathrm{bar}}$ and $q^{\mathrm{voi}}$, not evidence of capture by themselves. A decline in bargaining coverage can follow from changes in industry composition and trade as well as from employer action and law.
   348	
   349	Documented checks are visible in the same record. Union contracts, minimum-wage laws, antitrust enforcement in labor markets and the expansion of social insurance in the twentieth century all raised producers' terms through voice. \citet{polanyi1944} treated the protective legislation of the nineteenth century as the countermovement of a society defending itself against the commodification of labor. Documented capture is harder to establish than decline. The source's capture-link criterion requires material evidence linking privileged access to an output \citep{largo2026hbs}. Accounts of how organized business reshaped American labor and tax policy from the 1970s \citep{hackerpierson2010} supply candidate links, and they remain contested in the way Part II \citep{long2026political} describes in its Section 5.2 for the wider literature on unequal political responsiveness.
   350	
   351	\subsection{Communist party-states}
   352	
   353	In the Soviet Union after collectivization and in China under the planned economy, the party-state was the dominant employer, the sole legal purchaser of most farm output and the owner of nearly all productive assets. Its share of control over the terms of productive participation approached one, so $\HW$ was near its maximum. The coupling of $\pW$ to the other pillars was also high, because the same apparatus set prices and procurement quotas ($\pF$), wrote labor law ($\pP$), staffed the courts ($\pJ$), ran the official unions and the press ($\pI$), and policed mobility ($\pC$).
   354	
   355	Collectivization is the most fully documented case in which every instrument of Definitions~\ref{def:productive-power:gate} and~\ref{def:productive-power:outside} was used at once: a single purchaser, restricted mobility, and access to exchange conditioned on membership of the collective farm. Peasants resisted it in 1930 by slaughtering livestock, petitioning and open revolt \citep{viola1996}. After collectivization, the kolkhoz delivered grain at state-set prices, and procurement in the years 1931 to 1933 continued in regions where famine was spreading \citep{davies2004}. Mobility was restricted, and peasants adapted with strategies of evasion and survival that \citet{fitzpatrick1994} documented in detail. Forced labor in the Gulag formed a further tier of compelled state labor \citep{applebaum2003}, and economic historians have argued that it was expensive to run and less productive than free labor \citep{gregory2003}. In the terms of Table~\ref{tab:bondage}, collective farmers were tied to the farm for long periods and Gulag prisoners were compelled state laborers. Neither group was chattel property.
   356	
   357	Soviet industrial workers held more power than the formal structure suggests, because labor was scarce. Chronic labor shortage, the soft budget constraint of enterprises \citep{kornai1986,kornai1992} and managers' need to meet plans gave workers an informal bargaining position. Workers in the 1930s used it through high turnover, absenteeism and control over the pace of work, despite harsh labor-discipline laws \citep{filtzer1986}. Even the Stakhanovite campaign of record-setting provoked conflict on the shop floor as well as productivity gains \citep{siegelbaum1988}.
   358	
   359	Chinese workers under the planned economy faced a more complete dependence on the enterprise. Housing, rations and welfare came through the work unit and through personal ties to superiors, which made the unit a site of dependence rather than of bargaining \citep{walder1986}. The household registration system closed the main exit, tying rural people to their place of birth and restricting their access to urban employment and services \citep{cheng1994}.
   360	
   361	The reform era changed the instruments without removing them. Migration from the countryside expanded producers' outside options, and labor protest grew. \citet{lee2007} compared the protests of laid-off state-sector workers in the northeastern rustbelt with those of migrant workers in the southern export zones, who used the courts and labor law as well as street protest. The official union federation remains tied to the party, which limits voice outside party channels \citep{friedman2010}. Documented checks in this regime type are therefore mainly informal: evasion, turnover, petitioning, and the regime's own fear of unrest. That they existed matters for the comparison. Even under the most integrated arrangement in the record, the latent veto of Proposition~\ref{prop:productive-power:latent-veto} operated through everyday resistance.
   362	
   363	\subsection{Social democracy and market socialism}
   364	
   365	In the Nordic social democracies, producers are wage earners and the self-employed in market economies, but their terms are set to an unusual degree by collective bargaining at the national and sectoral level and by universal social insurance. Union density and bargaining coverage have been high by international standards for most of the postwar period. Power resources theory explains the arrangement as the result of the organization of wage earners in unions and their alliance with social democratic parties \citep{korpi1983,esping1985}. \citet{esping1990} measured its consequence as decommodification, the degree to which people can maintain a livelihood without relying on the labor market. \citet{huber2001} traced the development of the welfare state to partisan government over decades.
   366	
   367	The distinctive coupling here is between $\pW$ and $\pP$, through corporatist bargaining in which unions, employers and the state set wages and social policy together. By the source's own standard this coupling is not capture \citep{largo2026hbs}. It is a coalition commanding agenda in two pillars, and in this case its effect was to raise producers' contestability rather than to lower it. Corollary~\ref{cor:productive-power:coupling} formalizes the asymmetry: capture requires instruments that lower producers' terms, and corporatist coupling has mainly strengthened voice. Universalism also has a fiscal logic. \citet{korpi1998} found that universal programs redistribute more than targeted ones, because they build coalitions of support that enlarge the budget. \citet{rothstein1996} showed how the Swedish administrative model made universal programs implementable.
   368	
   369	The limits of the model are documented as well. \citet{przeworski1985} argued that social democratic parties remain structurally dependent on private investment, and \citet{pontusson1992} traced the failure of Swedish wage-earner funds, the most ambitious attempt to transfer ownership to labor. \citet{rueda2005} argued that social democratic parties have incentives to protect labor-market insiders rather than outsiders in temporary or precarious employment. That cleavage is a candidate failure mode inside the pillar: high $\QW$ for insiders can coexist with low $\QW$ for outsiders.
   370	
   371	Market socialism and workers' self-management are the variants of this regime type in which producers formally own the enterprise. \citet{kornai1992} argued that reform socialism in Hungary and Yugoslavia retained soft budget constraints and party control of appointments, which limited the autonomy of self-managed firms. Worker cooperatives in market economies are the small-scale analogue. \citet{dow2003} surveyed the theory and evidence on labor-managed firms, and \citet{craig1993} studied the objectives of worker cooperatives in the plywood industry of the Pacific Northwest. In the model, a cooperative raises producers' outside option, since it is an employer that the producers themselves control, and it removes extraction within the firm while leaving taxation to the state.
   372	
   373	\subsection{Islamic states}
   374	
   375	Islamic states share a source of political legitimacy, the claim to govern according to religious law, and differ in nearly every other respect. The comparison here covers the Ottoman Empire, modern Iran and Saudi Arabia, and the productive arrangements in each are not derived from Islamic law alone. Some instruments are legal categories of the tradition, such as alms taxes and land taxes. Others, such as tax farming or migrant sponsorship, are fiscal and labor-market institutions that belong to particular states and periods.
   376	
   377	In the Ottoman Empire, organized crafts gave producers a channel of voice. The taxpaying subjects were mainly peasants, artisans and merchants, and urban crafts were organized in guilds that regulated entry, prices and quality while also serving the state as administrative and fiscal intermediaries \citep{baer1970}. The guild was thus a site of coupling between $\pW$ and $\pP$: guilds petitioned authorities and brought disputes to the courts. Studies of Ottoman and early Republican workers document strikes and labor organization in the nineteenth and early twentieth centuries \citep{quataert1995}.
   378	
   379	Control over Ottoman producers' terms was dispersed among intermediaries. \citet{karaman2010} compared Ottoman state finances with those of European states and found that Ottoman revenue per capita remained low and collection decentralized, with heavy reliance on tax farming. \citet{barkey2008} described Ottoman rule as brokerage with intermediaries rather than direct command. In the vocabulary of this paper, control over the terms of production was dispersed among intermediaries, so $\HW$ was moderate. Ibn Khaldun had already observed that dynasties begin with low tax rates that yield large revenues and end with high rates that yield little, as producers withdraw effort \citep{khaldun1958}. The observation states the latent veto in fourteenth-century terms.
   380	
   381	Islamic legal categories of taxation and charity, including the alms tax and endowments, shaped the fiscal relation and the provision of welfare. \citet{singer2008} surveyed charity in Islamic societies, including endowed public kitchens in the Ottoman Empire. The economic consequences of Islamic commercial law are debated. \citet{kuran2011} argued that rules of partnership, inheritance and endowment held back the formation of durable private enterprises in the Middle East; \citet{rubin2017} attributed divergence instead to the way rulers relied on religious authorities for legitimacy, and \citet{pamuk2000} offered a monetary and fiscal history that does not reduce Ottoman outcomes to law.
   382	
   383	Modern Iran shows producers' power at both extremes. Oil workers' strikes were central to the revolution of 1978 to 1979, and workers' councils briefly took over the management of factories before the new regime absorbed or suppressed them \citep{bayat1987}. In the following decades the urban poor pursued what \citet{bayat1997} called the quiet encroachment of the ordinary: unorganized, cumulative claims on land, services and public space. \citet{mahdavy1970} coined the concept of the rentier state using the Iranian case: oil revenue reduces the state's need to tax, and with it the bargaining weight of taxpayers.
   384	
   385	Saudi Arabia is the clearest rentier case. Oil rent finances the state, citizens receive public employment and transfers, and much of the private-sector labor force consists of migrants without citizenship \citep{chaudhry1997,hertog2010}. The migrant labor system ties a worker's legal residence to a sponsoring employer, which restricts the worker's ability to change employer or leave \citep{hanieh2011,kapiszewski2001}. On Table~\ref{tab:bondage} this is a restriction on mobility within wage labor, not chattel slavery; in the model it is a mobility restriction $g>0$ applied to a group with high outside options, exactly the case in which Proposition~\ref{prop:productive-power:domar} predicts that restriction pays. The early oil industry also produced organized protest: \citet{vitalis2007} documented the segregated labor hierarchy of the oil camps and the strikes it provoked. For citizens, the rentier bargain lowers producer dependence $\xi$, and Proposition~\ref{prop:productive-power:rentier} predicts that their withdrawal premium is small.
   386	
   387	\subsection{Catholic monarchies}
   388	
   389	In Habsburg Spain, Bourbon France and the Papal States, producers were mainly peasants owing seigneurial dues, the tithe and royal taxes, together with urban artisans and merchants. The privileged estates, clergy and nobility, were exempt from important direct taxes. The Church was simultaneously a landholder, a tithe receiver and a source of the monarch's legitimacy, so its coupling to $\pW$ was material as well as ideological. The tithe had a long history as an ecclesiastical claim on agricultural output \citep{constable1964}, and \citet{ekelund1996} analyzed the medieval Church as an economic organization that collected revenue for services.
   390	
   391	In Bourbon France, privilege sorted the fiscal burden. The heaviest direct tax fell on commoners, so the distribution of the burden was itself an output of political privilege; when the eighteenth-century monarchy tried to tax the privileged through new direct taxes, the resulting conflicts politicized taxation \citep{kwass2000}. In Languedoc the revenue drawn from producers was shared between the crown and provincial elites, whose collaboration made absolutism work \citep{beik1985}.
   392	
   393	The same fiscal interest produced a documented check. The monarchy strengthened village communities in Burgundy in order to tax them, and those communities then used royal courts to contest seigneurial dues \citep{root1987}. The crown's need for revenue thus raised the peasants' organized weight $\eta$ against their lords.
   394	
   395	In Castile, communal lands and municipal institutions mattered to peasant livelihoods \citep{vassberg1984}, and ordinary people litigated in large numbers in the royal courts \citep{kagan1981}. The Cortes bargained with the crown over new taxes, and the taxes paid by Castilian producers sustained the crown's borrowing \citep{drelichman2014}. In the Americas the same monarchy organized compelled state labor. The Potos\'i mining draft required indigenous communities in designated districts to send a share of their men to the mines, and \citet{dell2010} found persistent lower consumption and child growth in those districts today. In the Papal States, the pope was both temporal sovereign and head of the Church, which made the coupling of $\pI$ with fiscal administration direct \citep{prodi1987}.
   396	
   397	\citet{brenner1976} supplies the comparative lesson for this regime type. Seigneurial power, village organization and the fiscal needs of the crown interacted differently in France, England and eastern Europe, with different outcomes for peasant tenure. Productivity followed politics as much as technique: French agricultural output grew in some periods and regions and stagnated in others, and war, taxation and access to markets mattered more than peasant conservatism \citep{hoffman1996}. Catholic legitimation was common to several of these cases and did not determine the outcome. Village communities, royal courts, the Cortes and periodic revolt were the producers' channels of voice; flight to towns and colonies was their exit.
   398	
   399	\subsection{Secular democracies}
   400	
   401	In secular democracies, the citizen is a taxpayer and a voter at once, and the fiscal relation is the most general channel through which producers affect the state. The fiscal contract argument holds that states which depend on taxes must bargain with taxpayers, and that the bargain produces representation and services \citep{bates1985,moore2004,timmons2005}. Evidence for the link is conditional. \citet{ross2004} found that it is the cost of government relative to the services provided, rather than the level of taxation alone, that predicts democratization. \citet{levi1988} found that compliance in established democracies is quasi-voluntary: it depends on taxpayers' belief that others pay and that the government keeps its side of the bargain.
   402	
   403	The modern tax state depends on fiscal capacity, the ability to tax incomes broadly, which \citet{besley2011,besley2013} treat as an investment that states make when they expect common-interest spending such as defense. \citet{scheve2016} found that steeply progressive taxation in the twentieth century followed wars of mass mobilization, in which arguments that the wealthy should compensate for the sacrifices of conscripts proved persuasive, rather than following the extension of the franchise alone. This is the latent veto at work in a democratic register: those who supplied the soldiers and the war production obtained fiscal concessions.
   404	
   405	The working class appears in the comparative-historical literature as a force for democratization. \citet{rueschemeyer1992} argued that organized workers were the most consistent supporters of full democracy, against landlords and often against the bourgeoisie. Voice in secular democracies therefore includes the franchise, unions and the courts, and \citet{chenoweth2011} found that, in their data on twentieth-century campaigns, nonviolent campaigns relying on mass non-cooperation, including strikes and boycotts, succeeded more often than violent ones. Welfare regimes differ within this regime type. \citet{esping1990} classified liberal, conservative and social democratic regimes, and the liberal regime offers the weakest income protection.
   406	
   407	Capture episodes in secular democracies take the form of privileged access to tax and labor policy. Their documentation is subject to the source's three-part test, and the main empirical claims about unequal responsiveness are contested (Part II, Section 5.2). Documented checks include tax administration under judicial review, labor law enforced in independent courts, and the electoral reversal of fiscal policies. Part III treats the courts, including the contest between repeat players and occasional litigants (its Proposition 6.4).
   408	
   409	\subsection{Social reproduction across regimes}
   410	
   411	Every regime type relied on unpaid care to reproduce its producers, and the regimes differed mainly in how far the state or the market took over part of that work. In market economies the cost of raising children falls largely on parents, and disproportionately on mothers, even though the next generation of workers and taxpayers benefits everyone \citep{folbre1994}. Social democracies socialized more of the cost through public care services and policies that supported women's paid employment, which \citet{esping1990} and \citet{huber2001} treat as part of the social democratic welfare state. The Soviet Union drew women into paid work on a large scale while leaving most domestic work to them, a combination documented by \citet{lapidus1978}.
   412	
   413	The household's internal terms followed the same logic as the producers' terms elsewhere. \citet{kandiyoti1988} compared the household systems of sub-Saharan Africa with those she called classic patriarchy, found in a belt running from North Africa through the Middle East to South and East Asia, and showed that women bargained within each system according to its constraints. Her comparison concerns kinship and property systems, not religious doctrine, and it cuts across the regime types of this paper. \citet{laslett1989} trace the historical variation in how families, markets and states divided the work of reproduction. In the model's terms, these are differences in carers' fallback $o_h$ and standing $\eta_h$, set by property and family law in $\pP$ and $\pJ$ and by norms in $\pI$.
   414	
   415	\subsection{Summary across regimes}
   416	
   417	The comparison yields one regularity and one negative finding. The regularity is that producers' terms were worst where control over production was concentrated and coupled to coercion and to control of exchange: collectivization, the colonial mining draft, Gulag labor and the sponsorship of migrants. The negative finding is that this pattern does not follow ideology. It appears under a communist party, a Catholic monarchy and a modern monarchy legitimated by Islam, and its opposite, producers with strong voice, appears under social democracy, in Ottoman guilds and among Burgundian villagers. Tables~\ref{tab:regimes} and~\ref{tab:regimes2} record the dominant pattern in each regime type; the internal diversity is in the text.
   418	
   419	\begin{table}[p]
   420	\centering
   421	\small
   422	\caption{Who holds the productive pillar in each regime type, and how concentrated control over the terms of production is. Concentration is a qualitative judgment from the cited literature, not a coded value.}
   423	\label{tab:regimes}
   424	\begin{tabularx}{\textwidth}{@{}L{2.6cm}YYL{2.6cm}@{}}
   425	\toprule
   426	Regime type & Main producers and payers & Who sets the terms of participation & Concentration of control \\
   427	\midrule
   428	Market-capitalist & Wage earners, small firms, consumers and taxpayers & Employers in labor markets and the state through tax and labor law & Varies by local market and is high in many \\
   429	Communist party-state & State employees, collective farmers and, in the reform era, migrant workers & The party-state as employer, purchaser and owner & Near the maximum before reform \\
   430	Social democracy and market socialism & Wage earners and the self-employed under encompassing bargaining & Unions, employers' associations and the state jointly & Moderate, with power shared by peak organizations \\
   431	Islamic states & Ottoman peasants and guild artisans, Iranian workers, Gulf citizens and migrants & Intermediaries and guilds in the Ottoman case, the rentier state and sponsors in the Gulf & Moderate in the Ottoman case and high for Gulf migrants \\
   432	Catholic monarchies & Peasants, artisans and colonial indigenous communities & Lords, the Church as landholder and tithe receiver, and the crown & High locally, shared among privileged estates \\
   433	Secular democracies & Citizen taxpayers and wage earners & Legislatures, tax administrations and labor markets & Varies with the economic regime \\
   434	\bottomrule
   435	\end{tabularx}
   436	\end{table}
   437	
   438	\begin{table}[p]
   439	\centering
   440	\small
   441	\caption{Coupling of the productive pillar to other pillars, channels of exit and voice, and documented checks. Each documented check is cited in the corresponding subsection.}
   442	\label{tab:regimes2}
   443	\begin{tabularx}{\textwidth}{@{}L{2.6cm}YYY@{}}
   444	\toprule
   445	Regime type & Principal couplings & Exit and voice & A documented check \\
   446	\midrule
   447	Market-capitalist & Capital allocation and employment are held by the same actors & Job mobility, unions and the vote & Union wage compression in the mid-twentieth century \\
   448	Communist party-state & One apparatus prices output, writes labor law, runs unions and polices mobility & Turnover, evasion, petitions and migration after reform & Shop-floor control of the pace of work by Soviet workers \\
   449	Social democracy and market socialism & Corporatist bargaining joins producers and the legislature & Encompassing unions, elections and universal benefits & Universal programs that enlarged redistribution \\
   450	Islamic states & Guilds joined crafts to administration, and rents join citizens to the state & Guild petitions, courts, strikes and quiet encroachment & Oil workers' strikes in the Iranian revolution \\
   451	Catholic monarchies & The Church joined land, tithe and legitimation, and the crown joined tax and justice & Village litigation, the Cortes, flight and revolt & Burgundian villages contesting dues in royal courts \\
   452	Secular democracies & Taxpayers and the franchise are joined in the same citizens & Elections, courts, unions and mass non-cooperation & Progressive taxation after wars of mass mobilization \\
   453	\bottomrule
   454	\end{tabularx}
   455	\end{table}
   456	
   457	Section~\ref{sec:mechanisms} derives the mechanism behind the regularity: each instrument that worsened producers' terms in these cases lowers the outside option or organized weight in the production game, and each is held outside the productive pillar.
   458	
   459	\section{Mechanisms, failure modes and checks}
   460	\label{sec:mechanisms}
   461	
   462	Producers' terms in the production game of Definition~\ref{def:productive-power:game} are set by five quantities: what producers can obtain by leaving, how well they are organized, how concentrated control over their participation is, how much of the coalition's revenue comes from elsewhere, and whether access to exchange is conditioned on allegiance. Each is a parameter of the game, and the results below give their comparative statics. The model is deliberately simple so that the mechanisms stay separate, and its parameters are not estimated here.
   463	
   464	\subsection{Exit and concentration}
   465	
   466	\begin{lemma}[Exit floor]
   467	\label{lem:productive-power:exit-floor}
   468	If producers are atomized, so that each decides alone whether to participate and the coalition sets $u$, the coalition's optimal terms are $u^*=o$ and the extraction share is $\chi^*=1-o/y$.
   469	\end{lemma}
   470	
   471	\begin{proof}
   472	A producer participates if and only if $u\ge o$. The coalition's revenue $n(y-u)+R$ is decreasing in $u$, so it chooses the smallest $u$ at which producers participate, which is $u=o$.
   473	\end{proof}
   474	
   475	The exit floor is the whole of atomized producers' power. It is zero extraction when $o=y$, as in the band of Proposition~\ref{prop:productive-power:minimal-form}, and maximal extraction when $o=y_0$.
   476	
   477	\begin{lemma}[Concentration lowers the outside option]
   478	\label{lem:productive-power:concentration}
   479	Suppose a producer who leaves employer $j$, and is neither blocked nor gated, receives one new offer, from employer $k$ with probability $s_k$; an offer from a different employer is worth $o_1$ and an offer from the employer just left is worth no more than the fallback $y_0<o_1$. Then the outside option at employer $j$ is the composite $o_j$ of Definition~\ref{def:productive-power:outside}, and the employment-weighted mean is $\bar o=y_0+\gamma(1-g)(1-\HW)(o_1-y_0)$. Under the exit floor, the employment-weighted mean extraction share is
   480	\[
   481	\bar\chi=1-\frac{y_0+\gamma(1-g)(1-\HW)(o_1-y_0)}{y},
   482	\]
   483	which increases linearly in $\HW$.
   484	\end{lemma}
   485	
   486	\begin{proof}
   487	An exit succeeds with probability $\gamma(1-g)$; given success, the offer comes from a different employer with probability $1-s_j$. The expected value is $y_0+\gamma(1-g)(1-s_j)(o_1-y_0)=o_j$. Then $\sum_js_jo_j=y_0+\gamma(1-g)(o_1-y_0)\sum_j s_j(1-s_j)=y_0+\gamma(1-g)(1-\HW)(o_1-y_0)$, since $\sum_js_j=1$. Each employer sets $u_j=o_j$ by Lemma~\ref{lem:productive-power:exit-floor}, so $\chi_j=1-o_j/y$ and the weighted mean is $1-\bar o/y$.
   488	\end{proof}
   489	
   490	The lemma gives the source's concentration index a mechanical role in this pillar. Under its assumptions, average extraction rises linearly with $\HW$, at a rate equal to the value of a competing offer relative to output. A single employer, $\HW=1$, holds every producer at the fallback; this is the company town, and in the limit it is the party-state as sole employer before reform. Many small employers, $\HW\to 0$, give unrestricted producers the competing value $o_1$. The association between labor-market concentration and lower wages found by \citet{azar2022} is consistent with the lemma, though random rematching simplifies search in real labor markets \citep{manning2003}.
   491	
   492	\subsection{Voice and the withdrawal premium}
   493	
   494	Organized producers do not accept the exit floor. They bargain collectively, and their threat is withdrawal: a strike, a tax refusal, a boycott, a delivery strike by farmers, or mass flight. If the coalition's non-producer revenue does not cover its maintenance requirement, withdrawal imposes a cost beyond lost revenue, because the institutions cannot be paid. Let $\psi\ge 0$ be the cost per unit of that shortfall, so that at total revenue $T+R$ the coalition's payoff is
   495	\[
   496	V_S(T)=T+R-K-\psi\,(K-T-R)^+,\qquad (x)^+=\max(x,0).
   497	\]
   498	
   499	\begin{assumption}[Agreement covers maintenance]
   500	\label{ass:productive-power:feasible}
   501	The parameters satisfy $n(1-\eta)(y-o)\ge(1+\eta\psi)(K-R)^+$.
   502	\end{assumption}
   503	
   504	The assumption says that the surplus over producers' exit floor is large enough for an agreement to pay for the institutions. It holds automatically when $R\ge K$. When $R<K$ it fails for $\eta$ close to one, so fully organized producers facing a coalition without outside revenue lie outside the scope of the next result.
   505	
   506	\begin{proposition}[Voice share]
   507	\label{prop:productive-power:voice}
   508	Let producers bargain collectively with the coalition by the asymmetric Nash bargaining solution with producer weight $\eta\in[0,1]$, where disagreement gives producers $no$ and the coalition $V_S(0)=R-K-\psi(K-R)^+$. Under Assumption~\ref{ass:productive-power:feasible}, the agreed terms are
   509	\[
   510	u^*=o+\eta(y-o)+\Omega,\qquad \Omega=\frac{\eta\,\psi\,(K-R)^+}{n},
   511	\]
   512	and the agreement leaves no maintenance shortfall: $n(y-u^*)+R\ge K$.
   513	\end{proposition}
   514	
   515	\begin{proof}
   516	Write $\Psi=\psi(K-R)^+$ and $u_K=y-(K-R)^+/n$, the largest terms at which the coalition's revenue still covers $K$. For $u\le u_K$ the coalition's payoff is $V_S=n(y-u)+R-K$, which is linear; for $u>u_K$ it is lower by $\psi(K-n(y-u)-R)>0$. Consider first the linear problem, which maximizes $N(u)=(n(u-o))^{\eta}(n(y-u)+\Psi)^{1-\eta}$, the product of the gains $n(u-o)$ and $n(y-u)+R-K-V_S(0)=n(y-u)+\Psi$. For $0<\eta<1$ the logarithm of $N$ is strictly concave, and the first-order condition $\eta\,(n(y-u)+\Psi)=(1-\eta)\,n(u-o)$ gives $nu^*=\eta ny+(1-\eta)no+\eta\Psi$, the stated formula; for $\eta=0$ and $\eta=1$ the solution gives the whole gain to the coalition or to the producers, which the formula also covers. At $u^*$, $n(y-u^*)+R-K=n(1-\eta)(y-o)-\eta\Psi-(K-R)$, which is non-negative when $R\ge K$ (then $\Psi=0$) and, when $R<K$, equals $n(1-\eta)(y-o)-(1+\eta\psi)(K-R)\ge 0$ by Assumption~\ref{ass:productive-power:feasible}. So $u^*\le u_K$. The true Nash product with the payoff $V_S$ is never larger than $N(u)$ and equals it for $u\le u_K$. Hence $u^*$, which maximizes $N$ and lies where the two coincide, also maximizes the true Nash product.
   517	\end{proof}
   518	
   519	The terms have three parts. The exit floor $o$ is what producers obtain without organization. The bargained share $\eta(y-o)$ is what organization adds by splitting the surplus over the floor. The withdrawal premium $\Omega$ is what organization adds because the coalition cannot afford a withdrawal; it is the price of the latent veto of Proposition~\ref{prop:productive-power:latent-veto}. Organization is necessary for both of the latter parts. An individual producer's withdrawal costs the coalition only that producer's contribution $y-u$, which in a large population is too small to threaten the maintenance requirement. That is why the latent veto stays latent without collective action \citep{olson1965}. Unions, guilds, village communities, peasant assemblies, tax revolts and cooperatives are the institutions that raise $\eta$ above zero.
   520	
   521	\begin{corollary}[Organization flattens the concentration gradient]
   522	\label{cor:productive-power:gradient}
   523	Suppose each employer $j$ bargains with its own workers as in Proposition~\ref{prop:productive-power:voice}, with common weight $\eta$, common premium $\Omega$ and outside option $o_j$ from Definition~\ref{def:productive-power:outside}. Then the employment-weighted mean terms are $\bar u=\bar o+\eta(y-\bar o)+\Omega$, and
   524	\[
   525	\frac{\partial\bar u}{\partial\HW}=-(1-\eta)\,\gamma\,(1-g)\,(o_1-y_0)\le 0 .
   526	\]
   527	\end{corollary}
   528	
   529	\begin{proof}
   530	Averaging $u_j=o_j+\eta(y-o_j)+\Omega$ with weights $s_j$ gives $\bar u=(1-\eta)\bar o+\eta y+\Omega$. By Lemma~\ref{lem:productive-power:concentration}, $\partial\bar o/\partial\HW=-\gamma(1-g)(o_1-y_0)$, and the stated derivative follows.
   531	\end{proof}
   532	
   533	Hirschman's loyalty has an ambiguous place in the model. Loyalty that raises the threshold for exit lowers the effective outside option and with it the floor; loyalty that keeps members inside while they organize raises $\eta$ \citep{hirschman1970}. Which effect dominates depends on whether the loyal can speak.
   534	
   535	The same bargaining logic applies inside the household, where most care labor is done. \citet{agarwal1997} argued that a household member's bargaining power depends on the fallback position available outside the household: property, paid employment, access to common resources, and support from kin, community or state. In the notation of the model, a carer's terms are $o_h+\eta_h(y_h-o_h)$, where $o_h$ is that fallback and $\eta_h$ the carer's organized or normative standing. Property rights, divorce law, public childcare and access to paid work all act on $o_h$. The paper does not develop the household game further, but the instruments that set $o_h$ are, like those in Assumption~\ref{ass:productive-power:instruments} below, held largely in $\pP$, $\pJ$ and $\pI$.
   536	
   537	\subsection{The bondage condition}
   538	
   539	A coalition can lower the outside option directly by restricting mobility. Write $o(g)=y_0+(1-g)(o_0-y_0)$, where $o_0$ is the outside option at $g=0$ given by Definition~\ref{def:productive-power:outside}. Enforcement costs the coalition $\kappa(g)$ per producer, with $\kappa(0)=0$ and $\kappa$ increasing and convex.
   540	
   541	\begin{proposition}[Domar-Brenner condition]
   542	\label{prop:productive-power:domar}
   543	Suppose the coalition chooses $g$ and then sets terms, with producers bargaining with weight $\eta\in[0,1)$ as in Proposition~\ref{prop:productive-power:voice} (the atomized case is $\eta=0$), and Assumption~\ref{ass:productive-power:feasible} holds at every $g$. Then the coalition's payoff, net of terms that do not depend on $g$, is $n[(1-\eta)g(o_0-y_0)-\kappa(g)]$.
   544	\begin{enumerate}
   545	\item[(a)] If $\kappa(g)=\kappa g$ is linear, restriction is chosen ($g^*=1$) when $(1-\eta)(o_0-y_0)>\kappa$ and not chosen ($g^*=0$) when $(1-\eta)(o_0-y_0)<\kappa$.
   546	\item[(b)] If $\kappa$ is differentiable and strictly convex with $\kappa'(0)<(1-\eta)(o_0-y_0)<\kappa'(1)$, then $g^*\in(0,1)$ is the unique solution of $\kappa'(g^*)=(1-\eta)(o_0-y_0)$, and $g^*$ is increasing in $o_0-y_0$ and decreasing in $\eta$.
   547	\end{enumerate}
   548	\end{proposition}
   549	
   550	\begin{proof}
   551	By Proposition~\ref{prop:productive-power:voice}, the producers' terms at outside option $o$ are $u^*=o+\eta(y-o)+\Omega$, where $\Omega$ does not depend on $o$, and the agreement leaves no shortfall, so the coalition's payoff from producers is $n(y-u^*)=n[(1-\eta)(y-o)-\Omega]$. Substituting $o(g)=o_0-g(o_0-y_0)$ gives $n[(1-\eta)(y-o_0)-\Omega]+n(1-\eta)g(o_0-y_0)$, and subtracting enforcement cost $n\kappa(g)$ leaves the stated $g$-dependent part. In case (a) the payoff is linear in $g$ with slope $n[(1-\eta)(o_0-y_0)-\kappa]$, so the optimum is at $g=1$ when the slope is positive and at $g=0$ when it is negative. In case (b) the payoff is strictly concave, its derivative is positive at $g=0$ and negative at $g=1$, so the unique maximizer satisfies the first-order condition. Because $\kappa'$ is strictly increasing, a larger right side $(1-\eta)(o_0-y_0)$ requires a larger $g^*$; the right side increases in $o_0-y_0$ and decreases in $\eta$.
   552	\end{proof}
   553	
   554	The proposition places two classic explanations of bondage in one inequality. Domar's land-labor hypothesis concerns $o_0$: where land is abundant, a free peasant can leave and farm independently, so $o_0$ is high and binding the peasant pays \citep{domar1970}. Where land is scarce and labor abundant, $o_0$ is already close to $y_0$, the wage market holds producers near the floor, and restriction adds little. Brenner's objection concerns $\kappa$ and $\eta$: organized peasant communities raise the cost of enforcing restriction and bargain over terms, so the same land-labor ratio produced serfdom in one region and free tenure in another \citep{brenner1976}. The two accounts are not rivals in this form. They name different terms of the same condition, and the empirical question is which term varied more across the cases at issue.
   555	
   556	Organization also lowers the return to restriction, since a coalition facing organized producers captures only the fraction $1-\eta$ of any reduction in their outside option. That gives a reason for coercive suppression of organization to accompany mobility restriction, a joint pattern visible in collectivization and in the sponsorship system for migrants, where workers' organization was also restricted. Part V \citep{long2026coercive} gives the primary treatment of this pair in its Section 6.5, including the allegiance margin of sanctions (its Definition 2.5) on which coercive enforcement of a gate depends.
   557	
   558	\subsection{Rents}
   559	
   560	\begin{proposition}[Rentier comparative static]
   561	\label{prop:productive-power:rentier}
   562	In Proposition~\ref{prop:productive-power:voice}, the withdrawal premium $\Omega$ is non-increasing in non-producer revenue $R$. It falls at rate $\eta\psi/n$ while $R<K$ and is zero for all $R\ge K$. The exit floor and the bargained share do not depend on $R$.
   563	\end{proposition}
   564	
   565	\begin{proof}
   566	$\Omega=\eta\psi(K-R)^+/n$. For $R<K$ its derivative in $R$ is $-\eta\psi/n\le 0$; for $R\ge K$ it is identically zero. The other two terms, $o$ and $\eta(y-o)$, contain no $R$. Raising $R$ relaxes Assumption~\ref{ass:productive-power:feasible}, so the result stays within its scope.
   567	\end{proof}
   568	
   569	The proposition refines the rentier-state argument. Rents do not lower producers' terms by making producers less productive or less organized. They remove the part of producers' bargaining power that rested on the coalition's need for their contribution, and they remove it only up to the point where rents cover the maintenance requirement. Beyond that point additional rent changes nothing in this model. Within a country, the effect of rents on concessions to producers should therefore be concentrated near the threshold at which rents cover the cost of running the state, and small far above or below it. Across countries, a null average effect such as that reported by \citet{habermenaldo2011} is consistent with the model if most variation lies away from the threshold. Measuring the maintenance requirement is difficult, and Section~\ref{sec:measurement} proposes a proxy.
   570	
   571	For the citizens of a rentier state, the premium is near zero and their terms are set by the coalition's choice to distribute rent, not by their capacity to withhold. The producers of the rent are elsewhere, and Lemma~\ref{lem:productive-power:relocation} says where: in the extraction workforce, which in the Gulf monarchies is largely foreign, and among foreign buyers.
   572	
   573	\subsection{The participation gate}
   574	
   575	A coalition can lower producers' outside options without restricting their movement, by conditioning access to exchange. A producer who cannot buy inputs, sell output, obtain credit or be hired has nowhere to go even if free to walk away.
   576	
   577	\begin{proposition}[Gate]
   578	\label{prop:productive-power:gate}
   579	Let $o$ denote the outside option at $\gamma=1$, so that under the gate of Definition~\ref{def:productive-power:gate} it is $o_\gamma=y_0+\gamma(o-y_0)$. Under Assumption~\ref{ass:productive-power:feasible}, the agreed terms are $u^*(\gamma)=o_\gamma+\eta(y-o_\gamma)+\Omega$, and
   580	\[
   581	\frac{\partial u^*}{\partial\gamma}=(1-\eta)(o-y_0)\ge 0 .
   582	\]
   583	If the gate is closed ($\gamma=0$), producers are atomized ($\eta=0$) and rents cover the maintenance requirement ($R\ge K$), producers are held at the autarky value, $u^*=y_0$, and the coalition takes $n(y-y_0)$.
   584	\end{proposition}
   585	
   586	\begin{proof}
   587	Substitute $o_\gamma$ for $o$ in Proposition~\ref{prop:productive-power:voice}. Since $do_\gamma/d\gamma=o-y_0$ and $u^*$ depends on the outside option through $(1-\eta)o_\gamma$, the derivative follows. With $\gamma=0$, $o_\gamma=y_0$; with $\eta=0$, $\Omega=0$ and $u^*=o_\gamma=y_0$, and the coalition's revenue from producers is $n(y-y_0)$.
   588	\end{proof}
   589	
   590	The closed gate with atomized producers is the most complete form of producer dependence in the model. Nothing about it requires the producers to be owned, bound to land, or imprisoned. It requires only that access to exchange pass through a checkpoint controlled by the coalition and that the checkpoint test allegiance. The coalition needs control over exchange (markets, credit, licenses, employment) to build the checkpoint, a criterion of allegiance to apply at it, and enforcement to keep producers from trading around it. Part IV (Section 6.5) treats the coupling of belief and production from the side of belief, including the quasi-voluntary compliance of taxpayers. Section~\ref{sec:revelation} returns to this configuration.
   591	
   592	\subsection{Capture of the productive pillar}
   593	
   594	\begin{definition}[Capture of the productive pillar]
   595	\label{def:productive-power:w-capture}
   596	A \emph{productive capture link} is a capture link $(S\to j,\pW)$ in the sense of \citet{largo2026hbs} in which the privileged discretion held by $S$ is control over one of the parameters through which the production game sets producers' terms: their exit (through $g$ or the concentration $\HW$), their organization (through $\eta$), their access to exchange (through $\gamma$), or the coalition's exposure to their withdrawal (through non-producer revenue $R$ or the shortfall cost $\psi$). Material evidence must tie the exercise of that control to the terms $u$ or the extraction share $\chi$. The productive pillar is \emph{captured} at $t$ when productive capture links persist and the pillar's term $H_{\pW,t}(1-\QW_t)$ in $U_t$ is high.
   597	\end{definition}
   598	
   599	The definition inherits the source's three conditions, including the requirement of material evidence. Low wages, high taxes or concentrated employment do not by themselves establish capture. They may reflect low productivity, the cost of public goods that producers value, or economies of scale. Capture requires a documented instrument and a documented link from the instrument to the terms.
   600	
   601	\begin{assumption}[Assignment of instruments]
   602	\label{ass:productive-power:instruments}
   603	The instruments that change the parameters of the production game are exercised in the following pillars. Mobility restriction $g$ requires enforcement in $\pC$. Concentration of control over productive means, which raises $\HW$, is an allocation of resources in $\pF$. Lowering producers' organized weight $\eta$ requires prohibition in $\pP$, enforcement in $\pC$ or delegitimation in $\pI$. Closing the gate requires control of exchange in $\pF$, an allegiance criterion supplied in $\pI$ (the legitimation function of Part IV, Definition 2.1, the practices that produce and validate the beliefs about rules and authority on which members' coordination depends \citep{long2026ideological}), and enforcement in $\pC$. Raising non-producer revenue $R$ is an allocation in $\pF$. Lowering the shortfall cost $\psi$ requires reserves accumulated in $\pF$ or the lawful hiring of replacement producers, whose permission is set in $\pP$.
   604	\end{assumption}
   605	
   606	\begin{corollary}[Capture requires coupling]
   607	\label{cor:productive-power:coupling}
   608	Under Assumption~\ref{ass:productive-power:instruments}, any action by a coalition $S$ that lowers producers' terms $u^*$ below their value at the baseline parameters $(\HW^0,g=0,\eta_0,\gamma=1,R_0,\psi_0)$ is taken in at least one pillar $n\ne\pW$. Hence a captured productive pillar implies $C_{n\pW,t}>0$ for some $n\in\{\pF,\pP,\pI,\pC\}$, with $S$ the coalition in question.
   609	\end{corollary}
   610	
   611	\begin{proof}
   612	By Proposition~\ref{prop:productive-power:voice}, Proposition~\ref{prop:productive-power:gate} and Lemma~\ref{lem:productive-power:concentration}, $u^*$ is non-decreasing in $o$, $\eta$, $\gamma$ and $\psi$ and non-increasing in $R$, with $o$ non-increasing in $g$ and $\HW$ by Definition~\ref{def:productive-power:outside}. Holding output $y$ and the maintenance requirement $K$ fixed, a reduction of $u^*$ therefore requires raising $g$ or $\HW$, lowering $\eta$, $\gamma$ or $\psi$, or raising $R$. By Assumption~\ref{ass:productive-power:instruments} each of these is exercised in a pillar other than $\pW$. If $S$ exercises it and also holds the terms of production, $S$ commands decisions in both $\pW$ and that pillar, which is $C_{n\pW,t}>0$.
   613	\end{proof}
   614	
   615	The corollary depends on the assignment, which is a modeling claim rather than a theorem. The hardest case for it is the hiring of replacement workers during a strike, which happens in the labor market itself; the assignment places it in $\pP$ because whether replacement is lawful is decided there. The assignment is defensible because each instrument in the comparative record was in fact exercised outside the productive layer: passports and residence permits by police and ministries, procurement prices by planners, union prohibitions by legislatures and courts, and allegiance tests by the authorities that define loyalty. Its consequence is that capture of production is never a fact about production alone. A society in which producers work long hours for low pay under many competing employers, free to organize and to leave, has a poor productive pillar but not a captured one. This is the pillar-level form of Largo's requirement that a strong classification show both concentration and cross-pillar integration \citep{largo2026hbs}, and of Part VII's result that Proposition A does not imply Proposition B. The function is implemented at every parameter value of the production game. Capture is a region of the parameter space.
   616	
   617	\subsection{Failure modes and checks}
   618	
   619	Each instrument in the production game defines a failure mode, and each failure mode has a check that interrupts it.
   620	
   621	Concentration of employment or purchase lowers the outside option (Lemma~\ref{lem:productive-power:concentration}). Antitrust enforcement in labor markets, the entry of new employers and public employment of last resort raise $o$. Cooperatives add an employer that producers themselves control \citep{dow2003}.
   622	
   623	Mobility restriction lowers the outside option directly (Proposition~\ref{prop:productive-power:domar}). Portability of benefits, abolition of tied residence and the right to change employer interrupt it. The condition in Proposition~\ref{prop:productive-power:domar} also shows when the check is under most pressure: when producers' free outside options are high, the coalition gains most from restriction.
   624	
   625	Suppression of organization lowers $\eta$ and with it both the bargained share and the withdrawal premium (Proposition~\ref{prop:productive-power:voice}). Legal protection of association and strikes, independent courts that enforce it (Part III, Section 6), and union democracy interrupt it. Michels's argument that organizations develop oligarchic leaderships applies to unions as well \citep{michels1915}, and Part II states it as a conditional tendency (its Proposition 6.2) rather than a law. The International Typographical Union studied by \citet{lipset1956} is the classic documented exception, a union that kept a two-party internal democracy.
   626	
   627	Rents remove the withdrawal premium (Proposition~\ref{prop:productive-power:rentier}). Fiscal rules that route rents into funds outside the coalition's discretion, and taxation that keeps the state dependent on domestic producers, are the checks the model suggests. Their effectiveness is an empirical question this paper does not settle.
   628	
   629	The gate lowers outside options through control of exchange (Proposition~\ref{prop:productive-power:gate}). Open markets, multiple sources of credit and employment, and the legal separation of economic access from political allegiance keep $\gamma$ close to one. The check is a separation of pillars: the actors who test allegiance must not control exchange.
   630	
   631	\begin{figure}[t]
   632	\centering
   633	\begin{tikzpicture}[x=1cm,y=1cm,>=stealth]
   634	  \node[draw,rounded corners,minimum width=2.6cm,minimum height=1.2cm,align=center] (W) at (0,0) {Producers\\ $\pW$};
   635	  \node[draw,rounded corners,minimum width=2.6cm,minimum height=1.2cm,align=center] (S) at (7,0) {Coalition $S$\\ maintenance $K$};
   636	  \node[align=center,font=\small] (F) at (0,2.6) {$\pF$: concentration $\HW$,\\ rents $R$, control of exchange};
   637	  \node[align=center,font=\small] (C) at (0,-2.6) {$\pC$: mobility restriction $g$,\\ enforcement of the gate};
   638	  \node[align=center,font=\small,anchor=east] (PI) at (-2.6,0) {$\pP$, $\pI$: organization $\eta$,\\ allegiance test};
   639	  \draw[->,thick] ([yshift=3mm]W.east) -- node[above,font=\small]{output $n(y-u)$} ([yshift=3mm]S.west);
   640	  \draw[->,thick,dashed] ([yshift=-3mm]W.east) -- node[below,font=\small]{withdrawal threat $\Omega$} ([yshift=-3mm]S.west);
   641	  \draw[->] (F) -- (W);
   642	  \draw[->] (C) -- (W);
   643	  \draw[->] (PI) -- (W);
   644	\end{tikzpicture}
   645	\caption{Instruments of the production game. Producers supply output to the coalition and hold a withdrawal threat whose value depends on the coalition's maintenance shortfall; every instrument that lowers producers' terms is held in another pillar.}
   646	\label{fig:instruments}
   647	\end{figure}
   648	
   649	\section{Measurement}
   650	\label{sec:measurement}
   651	
   652	The model's parameters correspond to observable quantities, though several can be measured only by proxy. Table~\ref{tab:indicators} lists an indicator for each. The list follows the source's rule that weights and codings be preregistered and that no aggregate index be reported for a real country without a documented coding \citep{largo2026hbs}. Largo also warns that measurement invariance across regimes must be tested before indicators are compared \citep{largo2026hbs}. Union density means something different under a party-controlled federation than under independent unions, and the indicators below are meant to be coded with that difference recorded.
   653	
   654	\begin{table}[t]
   655	\centering
   656	\small
   657	\caption{Indicators for the parameters of the production game and the components of productive contestability. Each indicator requires a preregistered coding rule before use.}
   658	\label{tab:indicators}
   659	\begin{tabularx}{\textwidth}{@{}L{3.6cm}Y@{}}
   660	\toprule
   661	Quantity & Indicator \\
   662	\midrule
   663	Concentration $\HW$ & Herfindahl index of employment or vacancy shares in local labor markets, the state's share of employment, and the share of farm output sold to a single purchaser \\
   664	Outside option $o$ & Rates of job-to-job transition, wage changes on switching employer, and the legal ability to change employer or residence \\
   665	Mobility restriction $g$ & Statutes and practice on internal passports, residence permits tied to an employer, and debt or land ties \\
   666	Organized weight $\eta$ & Union density, bargaining coverage, legality of strikes, and the independence of unions from the ruling party or employer \\
   667	Rents and maintenance, $R$ and $K$ & Non-tax revenue relative to recurrent spending on administration, courts, security and public information \\
   668	Producer dependence $\xi$ & Share of government revenue raised from domestic taxes and contributions \\
   669	Participation gate $\gamma$ & Rules that condition employment, licenses, credit or market access on political or religious criteria, coded from statute and documented practice \\
   670	Legal access $q^{\mathrm{leg}}$ & Availability, cost and independence of labor and tax adjudication, coded with the components of Part III, Definition 2.4 \\
   671	Income protection $q^{\mathrm{inc}}$ & Replacement rates of unemployment, sickness and old-age insurance \\
   672	Care labor $h$ and carers' fallback $o_h$ & Time-use surveys of unpaid care by sex, coverage of public childcare and paid leave, and women's property and divorce rights \\
   673	\bottomrule
   674	\end{tabularx}
   675	\end{table}
   676	
   677	The maintenance requirement $K$ is the hardest quantity to measure. A workable proxy is recurrent spending on the core functions of the other five pillars, excluding transfers and investment, since those are the outlays that cannot be postponed without loss of function. The proxy is imperfect because some transfers are themselves maintenance (pensions to soldiers, stipends to clergy) and because the shortfall cost $\psi$ depends on reserves and borrowing capacity. A preregistered study would fix the proxy and test sensitivity to alternatives.
   678	
   679	The model and the comparison yield nine testable hypotheses, listed with their falsifiers in Table~\ref{tab:hypotheses}. Several refine the source's hypotheses H5 and H6 \citep{largo2026hbs}.
   680	
   681	\begin{table}[t]
   682	\centering
   683	\small
   684	\caption{Hypotheses for the productive pillar. Each prediction follows from the result named in the second column; the falsifier is the observation that would refute it.}
   685	\label{tab:hypotheses}
   686	\begin{tabularx}{\textwidth}{@{}L{1.0cm}L{2.4cm}YY@{}}
   687	\toprule
   688	 & Basis & Prediction & Falsifier \\
   689	\midrule
   690	HW1 & Source H5, Lemma~\ref{lem:productive-power:concentration} & Higher bargaining coverage weakens the association between employer concentration and lower pay & The concentration gradient is the same at high and low coverage \\
   691	HW2 & Fiscal contract & Governments concede more services and representation where domestic taxes supply more revenue & No relation after conditioning on income, as some tests find \\
   692	HW3 & Proposition~\ref{prop:productive-power:rentier} & The effect of rents on concessions to producers is largest where rents are close to the cost of running the state & The effect is uniform in the ratio of rents to maintenance or largest far from one \\
   693	HW4 & Proposition~\ref{prop:productive-power:domar} & Bondage is more frequent where free exit is valuable and enforcement is cheap & Its incidence is unrelated to both across regions under comparable states \\
   694	HW5 & Everyday resistance & Covert non-compliance rises where open voice is suppressed & Evasion and turnover are unrelated to repression of organization \\
   695	HW6 & Insiders and outsiders & Contestability differs between permanent and precarious workers in encompassing welfare states & No difference in bargaining coverage or income protection between the groups \\
   696	HW7 & Persistence & Compelled labor drafts leave lower consumption in affected districts long after abolition & Comparable drafts show no persistent effect at their boundaries \\
   697	HW8 & Source H6 & Higher tax revenue with accountable provision goes with lower worker vulnerability & Vulnerability rises with provision \\
   698	HW9 & Lemma~\ref{lem:productive-power:reproduction} and household bargaining & Unpaid care is shared more evenly where carers' fallback positions are stronger & The division of unpaid care is unrelated to property rights, paid employment and public care \\
   699	\bottomrule
   700	\end{tabularx}
   701	\end{table}
   702	
   703	The exit hypotheses, HW1, HW4 and HW7, test how outside options set terms. HW1 is Corollary~\ref{cor:productive-power:gradient}: organization scales the concentration gradient by $1-\eta$, so it should be flatter where bargaining coverage is high. HW4 is the Domar-Brenner condition, and its test requires regional comparisons within one state, so that enforcement institutions are held roughly constant while land-labor ratios and peasant organization vary. HW7 generalizes \citet{dell2010}, whose regression-discontinuity design at the boundary of the draft area is the template.
   704	
   705	The fiscal hypotheses, HW2, HW3 and HW8, test the coalition's dependence on producers. HW2 carries the condition that \citet{ross2004} found necessary: the relevant variable is the price of government services, not taxation alone. HW3 is the paper's sharpest new prediction. If most observed variation in rents lies far from the threshold at which rents cover the cost of the state, it reconciles the rentier literature with null findings such as those of \citet{habermenaldo2011}. HW8 is the source's public-goods rival stated for producers: if it holds, high taxation is not evidence of extraction.
   706	
   707	The voice hypotheses, HW5, HW6 and HW9, test what happens to producers whose organized weight is low. HW5 follows \citet{scott1985} and the Soviet evidence of \citet{fitzpatrick1994} and \citet{filtzer1986}, and its difficulty is that covert resistance is hard to observe by design. HW6 tests the insider-outsider cleavage that \citet{rueda2005} identified. HW9 applies the household version of the bargaining model, with the fallback positions emphasized by \citet{agarwal1997}.
   708	
   709	Two identification problems apply to all nine. Organization is endogenous to the terms it is supposed to explain, since producers organize more where they expect gains. Rents, concentration and gates are chosen by coalitions that anticipate producers' responses. Event studies around reforms that change one instrument at a time, of the kind Largo proposes for oversight reforms \citep{largo2026hbs}, are the most direct remedy. Examples include the abolition of tied residence, the legalization of independent unions and the creation of a sovereign fund that removes rents from current budgets.
   710	
   711	\section{The Revelation reading}
   712	\label{sec:revelation}
   713	
   714	The series reads Revelation 13 and 17 to 18 typologically: the beast is a recurring pattern of power that claims ultimate loyalty, and Babylon is the idolatrous city of every age \citep{bauckham1993,beale1999}. The reading is anchored in the text's first-century setting, the Roman province of Asia, where the imperial cult was a civic institution woven into local life \citep{price1984,friesen2001}. Futurist readings that identify the beast or the mark with a coming government, person, product, technology or payment system are excluded. Their reception history is a record of failed identifications \citep{boyer1992,fuller1995,mcginn1998}. Historicist readings that identified the beast with a particular church or ruler belong to the history of polemic and are excluded for the same reason. The mapping of images to pillars below is a heuristic that aids comparison. It is an interpretive claim of this project, not a settled exegetical result.
   715	
   716	The passage most directly relevant to this pillar is Revelation 13:16-17 (KJV): ``And he causeth all, both small and great, rich and poor, free and bond, to receive a mark in their right hand, or in their foreheads: And that no man might buy or sell, save he that had the mark, or the name of the beast, or the number of his name.'' The verse does not describe a form of labor. It describes a condition on participation in exchange. Its scope runs across every category of the social order, ``free and bond'' included, so the condition is not the bondage of a class but the gating of everyone's access to buying and selling by a sign of allegiance.
   717	
   718	In the terms of Section~\ref{sec:mechanisms}, the verse depicts a closed participation gate, $\gamma=0$, applied to all who withhold allegiance. Proposition~\ref{prop:productive-power:gate} says what such a gate requires and what it yields. It requires control over exchange, a criterion of allegiance and enforcement. In the vision these are distributed across figures: the first beast holds authority and makes war (13:2, 13:4, 13:7); the second beast speaks, performs signs and causes the image of the first to be worshipped (13:12-15); and the restriction on buying and selling is its economic instrument. The series' heuristic maps these to $\pP$ and $\pC$, to $\pI$, and to the coupling of $\pF$ with $\pW$. The gate also yields a precise result: producers without organization or exit are held to their autarky value. The vision's image of economic exclusion as the sanction for refused allegiance is the limiting case of the model, and it is a limiting case of capture (Proposition B), not of the productive function itself.
   719	
   720	The preterist anchor gives the image economic content. \citet{kraybill1996} argued that participation in the maritime trade and trade guilds of Asia Minor entangled Christians in the imperial cult, and that John's vision calls them to withdraw from commerce on those terms. \citet{bauckham1991} read the lament over Babylon in Revelation 18 as an economic critique of Rome. The cargo list of 18:11-13 runs through luxury goods and ends with ``slaves, and souls of men,'' an indictment of a trade that included human beings. This is literal chattel slavery in the Roman economy. It is the extreme of Table~\ref{tab:bondage} and must not be read as a metaphor for wage labor or taxation. The list also illustrates the relocation lemma: the goods that sustained the imperial center were produced across the provinces and beyond them, and the kings, merchants and shipmasters who lament Babylon's fall (18:9-19) are those whose wealth depended on that flow.
   721	
   722	The text's response to the gate has the shape of Hirschman's triad, though it was written for different purposes. The imperative ``Come out of her, my people'' (18:4) is a call to exit. Faithful witness (11:3-13) and the ``patience and the faith of the saints'' (13:10) are a form of voice that refuses the demanded loyalty. Loyalty itself is the contested object: the vision depicts a demand for worship, and the faithful are those who give their allegiance elsewhere. \citet{rossing1999} read the contrast between Babylon and the New Jerusalem as a choice between two cities, with an economic critique of imperial Rome at its center. \citet{wink1992} generalized the beast into a domination system present in institutions of every age, a reading congenial to the series' claim that the structure is universal.
   723	
   724	The analogy has limits that must be stated. Revelation is apocalyptic literature, and its resolution is divine judgment, not producers' bargaining. \citet{collins1984} argued that the book addresses a crisis that was partly perceived, written to produce catharsis in its readers, and \citet{thompson1990} questioned the extent of persecution under Domitian. The verses supply an image of the limiting case of capture in this pillar, and the model supplies the conditions under which that limit is approached. Neither depends on the other. The analytic claims of this paper stand without the theological reading, and the reading identifies no present institution with the beast.
   725	
   726	\section{Objections and scope conditions}
   727	\label{sec:objections}
   728	
   729	A Marxian reader will object that production is not one pillar among six but the base on which the others rest, and that the framework flattens class relations into a network. The paper's own results partly concede the point. The latent veto gives production a status that no other pillar has: every other function consumes what this one supplies. But Proposition A asserts only that all six functions exist and depend on one another, not that they carry equal causal weight. Whether production determines the other pillars is a claim about the dependency matrix $B_t$, and it is an empirical question. Largo describes the framework as mid-range institutional theory that treats producers as active rather than as a passive base \citep{largo2026hbs}. The functional-explanation debate in Marxism \citep{cohen1978,elster1985} is a reminder that claims of determination need mechanisms, which is what the production game attempts to supply.
   730	
   731	A liberal reader will object that the extraction share mislabels returns to capital and payments for public services, and that market exchange is voluntary. The model accommodates the objection rather than rejecting it. The extraction share is net of services returned. Under competitive conditions, with many employers and free mobility, Lemma~\ref{lem:productive-power:concentration} gives producers the competitive value of their labor, and the liberal benchmark is the case $\HW\to 0$. Capture requires a documented instrument and a documented link to terms. What the model denies is only that voluntariness is a property of exchange as such. It depends on the outside option, and the outside option is shaped by concentration, restriction and gates.
   732	
   733	A functionalist objection runs the other way: the paper may have explained the existence of production by its usefulness. It has not. Lemma~\ref{thm:productive-power:necessity} is a condition of persistence. It says that persistent collectives produce, not that their productive institutions exist because they help the collective persist. This is the standard of \citet{hempel1959} and \citet{elster1983}, and the series adopts it throughout. \citet{merton1968} supplies the further point that functional alternatives exist: the same function is met by foraging bands, serf villages, kolkhozes and labor markets.
   734	
   735	Unpaid household labor enters the formal results in two places only: the reproduction lemma, which makes care a condition of persistence, and the household application of the bargaining model. The production game itself treats its $n$ producers as identical and sets their terms with the coalition, so it does not derive how care is divided within households or how that division interacts with the terms of paid work. A full treatment would solve the household game jointly with the production game, with each member's fallback set by property, divorce law and access to paid work. This paper states the household game's structure and one hypothesis (HW9) but does not solve it jointly.
   736	
   737	The comparative statics are monotone in the parameters, and that monotonicity, not the functional forms, carries the paper's qualitative claims. The functional forms are simple. The production game is stationary, its producers are identical within a group, and the asymmetric Nash solution summarizes rather than models the process of strikes and concessions. Real coalitions face heterogeneous producers, such as citizens and migrants or capital and labor, so the model must be applied group by group.
   738	
   739	Two simplifications bear directly on the size of the effects. Reserves and borrowing let coalitions survive withdrawal longer than the stationary shortfall cost suggests, which shrinks the withdrawal premium. The concentration lemma assumes random rematching in proportion to employment shares, which fixes the linear form of the concentration gradient. Relaxations that preserve monotonicity leave the signs of the results intact; their magnitudes require estimation.
   740	
   741	The claims about producer power are conditional on human activity remaining necessary for production. Lemma~\ref{lem:productive-power:relocation} keeps the function in place under full automation, but it moves the producer role to the owners and maintainers of equipment, and the latent veto of labor goes with it.
   742	
   743	\section{Conclusion}
   744	\label{sec:conclusion}
   745	
   746	Production is the one function every other function consumes. From the maintenance axiom, a persistent collective must produce at a positive average rate, and rents, tribute and machines relocate production without removing it. Producers therefore hold a latent veto over any governance system whose outside revenue falls short of its maintenance requirement. The production game prices that veto. Producers' terms rise with their outside option and their organization, fall linearly with the concentration of control over their participation, and lose their withdrawal premium once rents cover the cost of running the state. Restriction of mobility pays exactly when free exit is valuable and enforcement cheap.
   747	
   748	Every instrument that lowers producers' terms is exercised in another pillar. The capture of production is therefore always a coupling of production with coercion, allocation, rule-making or legitimation, and never a property of production alone. The comparison of six regime types found the productive function in all of them and its worst forms where control over production was concentrated and coupled to coercion and to control of exchange: under a communist party, a Catholic monarchy and a modern monarchy legitimated by Islam alike. Producers' voice was strongest under social democracy, in some Ottoman guilds and among Burgundian villagers using royal courts. Ideology did not sort the cases. The instruments did.
   749	
   750	What remains uncertain is quantitative. None of the model's parameters has been estimated here, and the sharpest prediction, that rents matter most where they nearly cover the cost of the state, awaits a test. The structural claim does not wait on that test. Every governance system in the record depends on those who produce for it, and the image of a world in which no one may buy or sell without the mark describes the condition in which that dependence has been turned entirely against them.
   751	
   752	\begin{thebibliography}{131}
   753	\small
   754	\setlength{\itemsep}{2pt}
   755	\bibitem[{Agarwal}(1997)]{agarwal1997}
   756	Agarwal, Bina. 1997. ``Bargaining'' and Gender Relations: Within and Beyond the Household. \emph{Feminist Economics} 3(1): 1-51. doi:10.1080/135457097338799.
   757	
   758	\bibitem[{Applebaum}(2003)]{applebaum2003}
   759	Applebaum, Anne. 2003. \emph{Gulag: A History}. Doubleday.
   760	
   761	\bibitem[{Azar et~al.}(2022)]{azar2022}
   762	Azar, Jos\'e, Ioana Marinescu, and Marshall Steinbaum. 2022. Labor Market Concentration. \emph{Journal of Human Resources} 57(S): S167-S199. doi:10.3368/jhr.monopsony.1218-9914R1.
   763	
   764	\bibitem[{Baer}(1970)]{baer1970}
   765	Baer, Gabriel. 1970. The Administrative, Economic and Social Functions of Turkish Guilds. \emph{International Journal of Middle East Studies} 1(1): 28-50. doi:10.1017/s0020743800023898.
   766	
   767	\bibitem[{Barkey}(2008)]{barkey2008}
   768	Barkey, Karen. 2008. \emph{Empire of Difference: The Ottomans in Comparative Perspective}. Cambridge University Press. doi:10.1017/cbo9780511790645.
   769	
   770	\bibitem[{Bates and Lien}(1985)]{bates1985}
   771	Bates, Robert H. and Da-Hsiang Donald Lien. 1985. A Note on Taxation, Development, and Representative Government. \emph{Politics \& Society} 14(1): 53-70. doi:10.1177/003232928501400102.
   772	
   773	\bibitem[{Bauckham}(1991)]{bauckham1991}
   774	Bauckham, Richard. 1991. The Economic Critique of Rome in Revelation 18. In \emph{Images of Empire}, ed. Loveday Alexander, JSOT Press (JSOTSup 122), pp. 47-90.
   775	
   776	\bibitem[{Bauckham}(1993)]{bauckham1993}
   777	Bauckham, Richard. 1993. \emph{The Theology of the Book of Revelation}. Cambridge University Press. doi:10.1017/cbo9780511819858.
   778	
   779	\bibitem[{Bayat}(1987)]{bayat1987}
   780	Bayat, Assef. 1987. \emph{Workers and Revolution in Iran: A Third World Experience of Workers' Control}. Zed Books.
   781	
   782	\bibitem[{Bayat}(1997)]{bayat1997}
   783	Bayat, Asef. 1997. \emph{Street Politics: Poor People's Movements in Iran}. Columbia University Press.
   784	
   785	\bibitem[{Beale}(1999)]{beale1999}
   786	Beale, G. K. 1999. \emph{The Book of Revelation: A Commentary on the Greek Text}. Eerdmans (NIGTC).
   787	
   788	\bibitem[{Beblawi and Luciani}(1987)]{beblawiluciani1987}
   789	Beblawi, Hazem and Giacomo Luciani (eds.). 1987. \emph{The Rentier State}. Croom Helm. doi:10.4324/9781315684864.
   790	
   791	\bibitem[{Beik}(1985)]{beik1985}
   792	Beik, William. 1985. \emph{Absolutism and Society in Seventeenth-Century France: State Power and Provincial Aristocracy in Languedoc}. Cambridge University Press. doi:10.1017/cbo9780511583797.
   793	
   794	\bibitem[{Besley and Persson}(2011)]{besley2011}
   795	Besley, Timothy and Torsten Persson. 2011. \emph{Pillars of Prosperity: The Political Economics of Development Clusters}. Princeton University Press. doi:10.23943/princeton/9780691152684.001.0001.
   796	
   797	\bibitem[{Besley and Persson}(2013)]{besley2013}
   798	Besley, Timothy and Torsten Persson. 2013. Taxation and Development. In \emph{Handbook of Public Economics}, vol. 5, Elsevier, pp. 51-110. doi:10.1016/B978-0-444-53759-1.00002-9.
   799	
   800	\bibitem[{Boehm}(1999)]{boehm1999}
   801	Boehm, Christopher. 1999. \emph{Hierarchy in the Forest: The Evolution of Egalitarian Behavior}. Harvard University Press. doi:10.2307/j.ctvjf9xr4.
   802	
   803	\bibitem[{Boyer}(1992)]{boyer1992}
   804	Boyer, Paul. 1992. \emph{When Time Shall Be No More: Prophecy Belief in Modern American Culture}. Harvard University Press (Belknap). doi:10.2307/jj.41480279.
   805	
   806	\bibitem[{Brenner}(1976)]{brenner1976}
   807	Brenner, Robert. 1976. Agrarian Class Structure and Economic Development in Pre-Industrial Europe. \emph{Past \& Present} 70: 30-75. doi:10.1093/past/70.1.30.
   808	
   809	\bibitem[{Campbell}(1993)]{campbell1993}
   810	Campbell, John L. 1993. The State and Fiscal Sociology. \emph{Annual Review of Sociology} 19: 163-185. doi:10.1146/annurev.so.19.080193.001115.
   811	
   812	\bibitem[{Chaudhry}(1997)]{chaudhry1997}
   813	Chaudhry, Kiren Aziz. 1997. \emph{The Price of Wealth: Economies and Institutions in the Middle East}. Cornell University Press. doi:10.7591/9781501700347.
   814	
   815	\bibitem[{Cheng and Selden}(1994)]{cheng1994}
   816	Cheng, Tiejun and Mark Selden. 1994. The Origins and Social Consequences of China's Hukou System. \emph{The China Quarterly} 139: 644-668. doi:10.1017/S0305741000043083.
   817	
   818	\bibitem[{Chenoweth and Stephan}(2011)]{chenoweth2011}
   819	Chenoweth, Erica and Maria J. Stephan. 2011. \emph{Why Civil Resistance Works: The Strategic Logic of Nonviolent Conflict}. Columbia University Press.
   820	
   821	\bibitem[{Clastres}(1987)]{clastres1987}
   822	Clastres, Pierre. 1987. \emph{Society against the State: Essays in Political Anthropology (1974), trans. Robert Hurley}. Zone Books. doi:10.2307/j.ctv1595m3p.
   823	
   824	\bibitem[{Cohen}(1978)]{cohen1978}
   825	Cohen, G. A. 1978. \emph{Karl Marx's Theory of History: A Defence}. Princeton University Press. doi:10.1515/9780691213002.
   826	
   827	\bibitem[{Collins}(1984)]{collins1984}
   828	Collins, Adela Yarbro. 1984. \emph{Crisis and Catharsis: The Power of the Apocalypse}. Westminster Press.
   829	
   830	\bibitem[{Constable}(1964)]{constable1964}
   831	Constable, Giles. 1964. \emph{Monastic Tithes from Their Origins to the Twelfth Century}. Cambridge University Press.
   832	
   833	\bibitem[{Cox et~al.}(2010)]{cox2010}
   834	Cox, Michael, Gwen Arnold, and Sergio Villamayor Tomas. 2010. A Review of Design Principles for Community-based Natural Resource Management. \emph{Ecology and Society} 15(4): 38.
   835	
   836	\bibitem[{Craig and Pencavel}(1993)]{craig1993}
   837	Craig, Ben and John Pencavel. 1993. The Objectives of Worker Cooperatives. \emph{Journal of Comparative Economics} 17(2): 288-308. doi:10.1006/jcec.1993.1027.
   838	
   839	\bibitem[{Davies and Wheatcroft}(2004)]{davies2004}
   840	Davies, R. W. and Stephen G. Wheatcroft. 2004. \emph{The Years of Hunger: Soviet Agriculture, 1931-1933}. Palgrave Macmillan.
   841	
   842	\bibitem[{Dell}(2010)]{dell2010}
   843	Dell, Melissa. 2010. The Persistent Effects of Peru's Mining Mita. \emph{Econometrica} 78(6): 1863-1903. doi:10.3982/ECTA8121.
   844	
   845	\bibitem[{Domar}(1970)]{domar1970}
   846	Domar, Evsey D. 1970. The Causes of Slavery or Serfdom: A Hypothesis. \emph{The Journal of Economic History} 30(1): 18-32. doi:10.1017/S0022050700078566.
   847	
   848	\bibitem[{Dow}(2003)]{dow2003}
   849	Dow, Gregory K. 2003. \emph{Governing the Firm: Workers' Control in Theory and Practice}. Cambridge University Press. doi:10.1017/CBO9780511615849.
   850	
   851	\bibitem[{Drelichman and Voth}(2014)]{drelichman2014}
   852	Drelichman, Mauricio and Hans-Joachim Voth. 2014. \emph{Lending to the Borrower from Hell: Debt, Taxes, and Default in the Age of Philip II}. Princeton University Press.
   853	
   854	\bibitem[{Ekelund et~al.}(1996)]{ekelund1996}
   855	Ekelund, Robert B., Robert F. Hebert, Robert D. Tollison, Gary M. Anderson, and Audrey B. Davidson. 1996. \emph{Sacred Trust: The Medieval Church as an Economic Firm}. Oxford University Press.
   856	
   857	\bibitem[{Elster}(1983)]{elster1983}
   858	Elster, Jon. 1983. \emph{Explaining Technical Change: A Case Study in the Philosophy of Science}. Cambridge University Press.
   859	
   860	\bibitem[{Elster}(1985)]{elster1985}
   861	Elster, Jon. 1985. \emph{Making Sense of Marx}. Cambridge University Press.
   862	
   863	\bibitem[{Esping-Andersen}(1985)]{esping1985}
   864	Esping-Andersen, G\"osta. 1985. \emph{Politics against Markets: The Social Democratic Road to Power}. Princeton University Press. doi:10.1515/9781400886203.
   865	
   866	\bibitem[{Esping-Andersen}(1990)]{esping1990}
   867	Esping-Andersen, G\"osta. 1990. \emph{The Three Worlds of Welfare Capitalism}. Princeton University Press.
   868	
   869	\bibitem[{Evans-Pritchard}(1940)]{evanspritchard1940}
   870	Evans-Pritchard, E. E. 1940. \emph{The Nuer: A Description of the Modes of Livelihood and Political Institutions of a Nilotic People}. Clarendon Press.
   871	
   872	\bibitem[{Farber et~al.}(2021)]{farber2021}
   873	Farber, Henry S., Daniel Herbst, Ilyana Kuziemko, and Suresh Naidu. 2021. Unions and Inequality over the Twentieth Century: New Evidence from Survey Data. \emph{The Quarterly Journal of Economics} 136(3): 1325-1385. doi:10.1093/qje/qjab012.
   874	
   875	\bibitem[{Filtzer}(1986)]{filtzer1986}
   876	Filtzer, Donald. 1986. \emph{Soviet Workers and Stalinist Industrialization: The Formation of Modern Soviet Production Relations, 1928-1941}. Pluto Press.
   877	
   878	\bibitem[{Fitzpatrick}(1994)]{fitzpatrick1994}
   879	Fitzpatrick, Sheila. 1994. \emph{Stalin's Peasants: Resistance and Survival in the Russian Village after Collectivization}. Oxford University Press. doi:10.1093/oso/9780195069822.001.0001.
   880	
   881	\bibitem[{Folbre}(1994)]{folbre1994}
   882	Folbre, Nancy. 1994. \emph{Who Pays for the Kids? Gender and the Structures of Constraint}. Routledge. doi:10.4324/9780203168295.
   883	
   884	\bibitem[{Freeman and Medoff}(1984)]{freeman1984}
   885	Freeman, Richard B. and James L. Medoff. 1984. \emph{What Do Unions Do?} Basic Books.
   886	
   887	\bibitem[{Friedman and Lee}(2010)]{friedman2010}
   888	Friedman, Eli and Ching Kwan Lee. 2010. Remaking the World of Chinese Labour: A 30-Year Retrospective. \emph{British Journal of Industrial Relations} 48(3): 507-533. doi:10.1111/j.1467-8543.2010.00814.x.
   889	
   890	\bibitem[{Friesen}(2001)]{friesen2001}
   891	Friesen, Steven J. 2001. \emph{Imperial Cults and the Apocalypse of John: Reading Revelation in the Ruins}. Oxford University Press. doi:10.1093/0195131533.001.0001.
   892	
   893	\bibitem[{Fuller}(1995)]{fuller1995}
   894	Fuller, Robert C. 1995. \emph{Naming the Antichrist: The History of an American Obsession}. Oxford University Press. doi:10.1093/acprof:oso/9780195109795.001.0001.
   895	
   896	\bibitem[{Gregory and Lazarev}(2003)]{gregory2003}
   897	Gregory, Paul R. and Valery Lazarev (eds.). 2003. \emph{The Economics of Forced Labor: The Soviet Gulag}. Hoover Institution Press.
   898	
   899	\bibitem[{Haber and Menaldo}(2011)]{habermenaldo2011}
   900	Haber, Stephen and Victor Menaldo. 2011. Do Natural Resources Fuel Authoritarianism? A Reappraisal of the Resource Curse. \emph{American Political Science Review} 105(1): 1-26. doi:10.1017/S0003055410000584.
   901	
   902	\bibitem[{Hacker and Pierson}(2010)]{hackerpierson2010}
   903	Hacker, Jacob S. and Paul Pierson. 2010. \emph{Winner-Take-All Politics: How Washington Made the Rich Richer and Turned Its Back on the Middle Class}. Simon \& Schuster.
   904	
   905	\bibitem[{Hanieh}(2011)]{hanieh2011}
   906	Hanieh, Adam. 2011. \emph{Capitalism and Class in the Gulf Arab States}. Palgrave Macmillan. doi:10.1057/9781137495105.
   907	
   908	\bibitem[{Hempel}(1959)]{hempel1959}
   909	Hempel, Carl G. 1959. The Logic of Functional Analysis. In \emph{Symposium on Sociological Theory}, ed. Llewellyn Gross, Harper \& Row, pp. 271-307.
   910	
   911	\bibitem[{Hertog}(2010)]{hertog2010}
   912	Hertog, Steffen. 2010. \emph{Princes, Brokers, and Bureaucrats: Oil and the State in Saudi Arabia}. Cornell University Press. doi:10.7591/9780801458774.
   913	
   914	\bibitem[{Hirschman}(1970)]{hirschman1970}
   915	Hirschman, Albert O. 1970. \emph{Exit, Voice, and Loyalty: Responses to Decline in Firms, Organizations, and States}. Harvard University Press.
   916	
   917	\bibitem[{Hoffman}(1996)]{hoffman1996}
   918	Hoffman, Philip T. 1996. \emph{Growth in a Traditional Society: The French Countryside, 1450-1815}. Princeton University Press. doi:10.1515/9780691187204.
   919	
   920	\bibitem[{Huber and Stephens}(2001)]{huber2001}
   921	Huber, Evelyne and John D. Stephens. 2001. \emph{Development and Crisis of the Welfare State: Parties and Policies in Global Markets}. University of Chicago Press. doi:10.7208/chicago/9780226356495.001.0001.
   922	
   923	\bibitem[{Ibn Khaldun}(1958)]{khaldun1958}
   924	Ibn Khaldun. 1958. \emph{The Muqaddimah: An Introduction to History (1377), trans. Franz Rosenthal}. Pantheon Books / Princeton University Press.
   925	
   926	\bibitem[{Kagan}(1981)]{kagan1981}
   927	Kagan, Richard L. 1981. \emph{Lawsuits and Litigants in Castile, 1500-1700}. University of North Carolina Press.
   928	
   929	\bibitem[{Kandiyoti}(1988)]{kandiyoti1988}
   930	Kandiyoti, Deniz. 1988. Bargaining with Patriarchy. \emph{Gender \& Society} 2(3): 274-290. doi:10.1177/089124388002003004.
   931	
   932	\bibitem[{Kapiszewski}(2001)]{kapiszewski2001}
   933	Kapiszewski, Andrzej. 2001. \emph{Nationals and Expatriates: Population and Labour Dilemmas of the Gulf Cooperation Council States}. Ithaca Press.
   934	
   935	\bibitem[{Karaman and Pamuk}(2010)]{karaman2010}
   936	Karaman, K. K{\i}van\c{c} and \c{S}evket Pamuk. 2010. Ottoman State Finances in European Perspective, 1500-1914. \emph{The Journal of Economic History} 70(3): 593-629. doi:10.1017/s0022050710000550.
   937	
   938	\bibitem[{Kelly}(1995)]{kelly1995}
   939	Kelly, Robert L. 1995. \emph{The Foraging Spectrum: Diversity in Hunter-Gatherer Lifeways}. Smithsonian Institution Press. doi:10.2307/j.ctv2sx9gc9.
   940	
   941	\bibitem[{Kornai}(1986)]{kornai1986}
   942	Kornai, J\'anos. 1986. The Soft Budget Constraint. \emph{Kyklos} 39(1): 3-30. doi:10.1111/j.1467-6435.1986.tb01252.x.
   943	
   944	\bibitem[{Kornai}(1992)]{kornai1992}
   945	Kornai, J\'anos. 1992. \emph{The Socialist System: The Political Economy of Communism}. Princeton University Press. doi:10.2307/j.ctv1ddczdr.
   946	
   947	\bibitem[{Korpi}(1983)]{korpi1983}
   948	Korpi, Walter. 1983. \emph{The Democratic Class Struggle}. Routledge \& Kegan Paul.
   949	
   950	\bibitem[{Korpi and Palme}(1998)]{korpi1998}
   951	Korpi, Walter and Joakim Palme. 1998. The Paradox of Redistribution and Strategies of Equality: Welfare State Institutions, Inequality, and Poverty in the Western Countries. \emph{American Sociological Review} 63(5): 661-687. doi:10.2307/2657333.
   952	
   953	\bibitem[{Kraybill}(1996)]{kraybill1996}
   954	Kraybill, J. Nelson. 1996. \emph{Imperial Cult and Commerce in John's Apocalypse}. Sheffield Academic Press (JSNT Supplement 132).
   955	
   956	\bibitem[{Kuran}(2011)]{kuran2011}
   957	Kuran, Timur. 2011. \emph{The Long Divergence: How Islamic Law Held Back the Middle East}. Princeton University Press. doi:10.1515/9781400836017.
   958	
   959	\bibitem[{Kwass}(2000)]{kwass2000}
   960	Kwass, Michael. 2000. \emph{Privilege and the Politics of Taxation in Eighteenth-Century France}. Cambridge University Press.
   961	
   962	\bibitem[{Lapidus}(1978)]{lapidus1978}
   963	Lapidus, Gail Warshofsky. 1978. \emph{Women in Soviet Society: Equality, Development, and Social Change}. University of California Press.
   964	
   965	\bibitem[{Largo}(2026)]{largo2026hbs}
   966	Largo, Mateo. 2026. \emph{The Hierarchy of the Beast System: Institutional Power, Elite Coordination, and Economic Dependency Across Political Regimes}. Working paper, 14 October 2026.
   967	
   968	\bibitem[{Laslett and Brenner}(1989)]{laslett1989}
   969	Laslett, Barbara and Johanna Brenner. 1989. Gender and Social Reproduction: Historical Perspectives. \emph{Annual Review of Sociology} 15: 381-404. doi:10.1146/annurev.so.15.080189.002121.
   970	
   971	\bibitem[{Lee}(1979)]{lee1979}
   972	Lee, Richard B. 1979. \emph{The !Kung San: Men, Women, and Work in a Foraging Society}. Cambridge University Press.
   973	
   974	\bibitem[{Lee}(2007)]{lee2007}
   975	Lee, Ching Kwan. 2007. \emph{Against the Law: Labor Protests in China's Rustbelt and Sunbelt}. University of California Press. doi:10.1525/9780520940642.
   976	
   977	\bibitem[{Lee}(2013)]{lee2013}
   978	Lee, Richard B. 2013. \emph{The Dobe Ju/'hoansi (4th edition)}. Wadsworth/Cengage Learning.
   979	
   980	\bibitem[{Levi}(1988)]{levi1988}
   981	Levi, Margaret. 1988. \emph{Of Rule and Revenue}. University of California Press. doi:10.1525/9780520909540.
   982	
   983	\bibitem[{Lindblom}(1977)]{lindblom1977}
   984	Lindblom, Charles E. 1977. \emph{Politics and Markets: The World's Political-Economic Systems}. Basic Books.
   985	
   986	\bibitem[{Lipset et~al.}(1956)]{lipset1956}
   987	Lipset, Seymour Martin, Martin A. Trow, and James S. Coleman. 1956. \emph{Union Democracy: The Internal Politics of the International Typographical Union}. Free Press.
   988	
   989	\bibitem[{Long}(2026a)]{long2026coercive}
   990	Long, Matthew. 2026a. \emph{Coercive Power and Enforcement}. Part V of The Six Pillars of the Beast System. Working paper, October 2026.
   991	
   992	\bibitem[{Long}(2026b)]{long2026financial}
   993	Long, Matthew. 2026b. \emph{Financial Power and Resource Command}. Part I of The Six Pillars of the Beast System. Working paper, October 2026.
   994	
   995	\bibitem[{Long}(2026c)]{long2026formalized}
   996	Long, Matthew. 2026c. \emph{The Formalized State: The Hierarchy of the Beast System}. Part VII of The Six Pillars of the Beast System. Working paper, October 2026.
   997	
   998	\bibitem[{Long}(2026d)]{long2026ideological}
   999	Long, Matthew. 2026d. \emph{Ideological Power and Legitimation}. Part IV of The Six Pillars of the Beast System. Working paper, October 2026.
  1000	
  1001	\bibitem[{Long}(2026e)]{long2026judicial}
  1002	Long, Matthew. 2026e. \emph{Judicial Power and Legal Interpretation}. Part III of The Six Pillars of the Beast System. Working paper, October 2026.
  1003	
  1004	\bibitem[{Long}(2026f)]{long2026political}
  1005	Long, Matthew. 2026f. \emph{Political Power and Rule Making}. Part II of The Six Pillars of the Beast System. Working paper, October 2026.
  1006	
  1007	\bibitem[{Mahdavy}(1970)]{mahdavy1970}
  1008	Mahdavy, Hossein. 1970. The Patterns and Problems of Economic Development in Rentier States: The Case of Iran. In \emph{Studies in the Economic History of the Middle East}, ed. M. A. Cook, Oxford University Press, pp. 428-467.
  1009	
  1010	\bibitem[{Manning}(2003)]{manning2003}
  1011	Manning, Alan. 2003. \emph{Monopsony in Motion: Imperfect Competition in Labor Markets}. Princeton University Press. doi:10.1515/9781400850679.
  1012	
  1013	\bibitem[{Marshall}(1976)]{marshall1976}
  1014	Marshall, Lorna. 1976. \emph{The !Kung of Nyae Nyae}. Harvard University Press. doi:10.4159/harvard.9780674180574.
  1015	
  1016	\bibitem[{Martin et~al.}(2009)]{martin2009}
  1017	Martin, Isaac William, Ajay K. Mehrotra, and Monica Prasad (eds.). 2009. \emph{The New Fiscal Sociology: Taxation in Comparative and Historical Perspective}. Cambridge University Press. doi:10.1017/CBO9780511627071.
  1018	
  1019	\bibitem[{Marx}(1976)]{marx1976}
  1020	Marx, Karl. 1976. \emph{Capital: A Critique of Political Economy, Volume 1 (1867), trans. Ben Fowkes}. Penguin.
  1021	
  1022	\bibitem[{McGinn}(1998)]{mcginn1998}
  1023	McGinn, Bernard. 1998. \emph{Antichrist: Two Thousand Years of the Human Fascination with Evil}. Columbia University Press.
  1024	
  1025	\bibitem[{Merton}(1968)]{merton1968}
  1026	Merton, Robert K. 1968. \emph{Social Theory and Social Structure (enlarged edition)}. Free Press.
  1027	
  1028	\bibitem[{Michels}(1915)]{michels1915}
  1029	Michels, Robert. 1915. \emph{Political Parties: A Sociological Study of the Oligarchical Tendencies of Modern Democracy}. Hearst's International Library.
  1030	
  1031	\bibitem[{Moore}(2004)]{moore2004}
  1032	Moore, Mick. 2004. Revenues, State Formation, and the Quality of Governance in Developing Countries. \emph{International Political Science Review} 25(3): 297-319. doi:10.1177/0192512104043018.
  1033	
  1034	\bibitem[{Olson}(1965)]{olson1965}
  1035	Olson, Mancur. 1965. \emph{The Logic of Collective Action: Public Goods and the Theory of Groups}. Harvard University Press. doi:10.4159/9780674041660.
  1036	
  1037	\bibitem[{Ostrom}(1990)]{ostrom1990}
  1038	Ostrom, Elinor. 1990. \emph{Governing the Commons: The Evolution of Institutions for Collective Action}. Cambridge University Press. doi:10.1017/CBO9780511807763.
  1039	
  1040	\bibitem[{Ostrom}(2010)]{ostromdesign2010}
  1041	Ostrom, Elinor. 2010. Beyond Markets and States: Polycentric Governance of Complex Economic Systems. \emph{American Economic Review} 100(3): 641-672. doi:10.1257/aer.100.3.641.
  1042	
  1043	\bibitem[{Pamuk}(2000)]{pamuk2000}
  1044	Pamuk, \c{S}evket. 2000. \emph{A Monetary History of the Ottoman Empire}. Cambridge University Press.
  1045	
  1046	\bibitem[{Piketty et~al.}(2018)]{piketty2018}
  1047	Piketty, Thomas, Emmanuel Saez, and Gabriel Zucman. 2018. Distributional National Accounts: Methods and Estimates for the United States. \emph{The Quarterly Journal of Economics} 133(2): 553-609. doi:10.1093/qje/qjx043.
  1048	
  1049	\bibitem[{Polanyi}(1944)]{polanyi1944}
  1050	Polanyi, Karl. 1944. \emph{The Great Transformation: The Political and Economic Origins of Our Time}. Farrar \& Rinehart.
  1051	
  1052	\bibitem[{Pontusson}(1992)]{pontusson1992}
  1053	Pontusson, Jonas. 1992. \emph{The Limits of Social Democracy: Investment Politics in Sweden}. Cornell University Press. doi:10.7591/9781501737541.
  1054	
  1055	\bibitem[{Price}(1984)]{price1984}
  1056	Price, S. R. F. 1984. \emph{Rituals and Power: The Roman Imperial Cult in Asia Minor}. Cambridge University Press.
  1057	
  1058	\bibitem[{Prodi}(1987)]{prodi1987}
  1059	Prodi, Paolo. 1987. \emph{The Papal Prince: One Body and Two Souls: The Papal Monarchy in Early Modern Europe}. Cambridge University Press.
  1060	
  1061	\bibitem[{Przeworski}(1985)]{przeworski1985}
  1062	Przeworski, Adam. 1985. \emph{Capitalism and Social Democracy}. Cambridge University Press. doi:10.1017/cbo9781139171830.
  1063	
  1064	\bibitem[{Quataert and Z\"urcher}(1995)]{quataert1995}
  1065	Quataert, Donald and Erik Jan Z\"urcher (eds.). 1995. \emph{Workers and the Working Class in the Ottoman Empire and the Turkish Republic, 1839-1950}. I. B. Tauris.
  1066	
  1067	\bibitem[{Root}(1987)]{root1987}
  1068	Root, Hilton L. 1987. \emph{Peasants and King in Burgundy: Agrarian Foundations of French Absolutism}. University of California Press. doi:10.1525/9780520913349.
  1069	
  1070	\bibitem[{Ross}(2001)]{ross2001}
  1071	Ross, Michael L. 2001. Does Oil Hinder Democracy? \emph{World Politics} 53(3): 325-361. doi:10.1353/wp.2001.0011.
  1072	
  1073	\bibitem[{Ross}(2004)]{ross2004}
  1074	Ross, Michael L. 2004. Does Taxation Lead to Representation? \emph{British Journal of Political Science} 34(2): 229-249. doi:10.1017/S0007123404000031.
  1075	
  1076	\bibitem[{Rossing}(1999)]{rossing1999}
  1077	Rossing, Barbara R. 1999. \emph{The Choice between Two Cities: Whore, Bride, and Empire in the Apocalypse}. Trinity Press International (Harvard Theological Studies 48).
  1078	
  1079	\bibitem[{Rothstein}(1996)]{rothstein1996}
  1080	Rothstein, Bo. 1996. \emph{The Social Democratic State: The Swedish Model and the Bureaucratic Problem of Social Reforms}. University of Pittsburgh Press. doi:10.2307/jj.13110785.
  1081	
  1082	\bibitem[{Rubin}(2017)]{rubin2017}
  1083	Rubin, Jared. 2017. \emph{Rulers, Religion, and Riches: Why the West Got Rich and the Middle East Did Not}. Cambridge University Press. doi:10.1017/9781139568272.
  1084	
  1085	\bibitem[{Rueda}(2005)]{rueda2005}
  1086	Rueda, David. 2005. Insider-Outsider Politics in Industrialized Democracies: The Challenge to Social Democratic Parties. \emph{American Political Science Review} 99(1): 61-74. doi:10.1017/S000305540505149X.
  1087	
  1088	\bibitem[{Rueschemeyer et~al.}(1992)]{rueschemeyer1992}
  1089	Rueschemeyer, Dietrich, Evelyne Huber Stephens, and John D. Stephens. 1992. \emph{Capitalist Development and Democracy}. University of Chicago Press.
  1090	
  1091	\bibitem[{Sahlins}(1972)]{sahlins1972}
  1092	Sahlins, Marshall. 1972. \emph{Stone Age Economics}. Aldine-Atherton. doi:10.4324/9780203037416.
  1093	
  1094	\bibitem[{Scheve and Stasavage}(2016)]{scheve2016}
  1095	Scheve, Kenneth and David Stasavage. 2016. \emph{Taxing the Rich: A History of Fiscal Fairness in the United States and Europe}. Princeton University Press. doi:10.1515/9781400880379.
  1096	
  1097	\bibitem[{Scott}(1976)]{scott1976}
  1098	Scott, James C. 1976. \emph{The Moral Economy of the Peasant: Rebellion and Subsistence in Southeast Asia}. Yale University Press. doi:10.12987/9780300185553.
  1099	
  1100	\bibitem[{Scott}(1985)]{scott1985}
  1101	Scott, James C. 1985. \emph{Weapons of the Weak: Everyday Forms of Peasant Resistance}. Yale University Press. doi:10.12987/9780300153620.
  1102	
  1103	\bibitem[{Scott}(2009)]{scott2009}
  1104	Scott, James C. 2009. \emph{The Art of Not Being Governed: An Anarchist History of Upland Southeast Asia}. Yale University Press. doi:10.12987/9780300156522.
  1105	
  1106	\bibitem[{Siegelbaum}(1988)]{siegelbaum1988}
  1107	Siegelbaum, Lewis H. 1988. \emph{Stakhanovism and the Politics of Productivity in the USSR, 1935-1941}. Cambridge University Press.
  1108	
  1109	\bibitem[{Silver}(2003)]{silver2003}
  1110	Silver, Beverly J. 2003. \emph{Forces of Labor: Workers' Movements and Globalization since 1870}. Cambridge University Press. doi:10.1017/CBO9780511615702.
  1111	
  1112	\bibitem[{Singer}(2008)]{singer2008}
  1113	Singer, Amy. 2008. \emph{Charity in Islamic Societies}. Cambridge University Press.
  1114	
  1115	\bibitem[{Thompson}(1990)]{thompson1990}
  1116	Thompson, Leonard L. 1990. \emph{The Book of Revelation: Apocalypse and Empire}. Oxford University Press. doi:10.1093/oso/9780195055511.001.0001.
  1117	
  1118	\bibitem[{Timmons}(2005)]{timmons2005}
  1119	Timmons, Jeffrey F. 2005. The Fiscal Contract: States, Taxes, and Public Services. \emph{World Politics} 57(4): 530-567. doi:10.1353/wp.2006.0015.
  1120	
  1121	\bibitem[{Vassberg}(1984)]{vassberg1984}
  1122	Vassberg, David E. 1984. \emph{Land and Society in Golden Age Castile}. Cambridge University Press.
  1123	
  1124	\bibitem[{Viola}(1996)]{viola1996}
  1125	Viola, Lynne. 1996. \emph{Peasant Rebels under Stalin: Collectivization and the Culture of Peasant Resistance}. Oxford University Press. doi:10.1093/oso/9780195101973.001.0001.
  1126	
  1127	\bibitem[{Vitalis}(2007)]{vitalis2007}
  1128	Vitalis, Robert. 2007. \emph{America's Kingdom: Mythmaking on the Saudi Oil Frontier}. Stanford University Press. doi:10.1515/9781503626119.
  1129	
  1130	\bibitem[{Walder}(1986)]{walder1986}
  1131	Walder, Andrew G. 1986. \emph{Communist Neo-Traditionalism: Work and Authority in Chinese Industry}. University of California Press. doi:10.1525/9780520909007.
  1132	
  1133	\bibitem[{Western and Rosenfeld}(2011)]{western2011}
  1134	Western, Bruce and Jake Rosenfeld. 2011. Unions, Norms, and the Rise in U.S. Wage Inequality. \emph{American Sociological Review} 76(4): 513-537. doi:10.1177/0003122411414817.
  1135	
  1136	\bibitem[{Wiessner}(2005)]{wiessner2005}
  1137	Wiessner, Polly. 2005. Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity? \emph{Human Nature} 16(2): 115-145.
  1138	
  1139	\bibitem[{Wink}(1992)]{wink1992}
  1140	Wink, Walter. 1992. \emph{Engaging the Powers: Discernment and Resistance in a World of Domination}. Fortress Press. doi:10.2307/j.ctt1tm7j16.
  1141	
  1142	\bibitem[{Woodburn}(1982)]{woodburn1982}
  1143	Woodburn, James. 1982. Egalitarian Societies. \emph{Man (N.S.)} 17(3): 431-451. doi:10.2307/2801707.
  1144	
  1145	\bibitem[{Wright}(2000)]{wright2000}
  1146	Wright, Erik Olin. 2000. Working-Class Power, Capitalist-Class Interests, and Class Compromise. \emph{American Journal of Sociology} 105(4): 957-1002. doi:10.1086/210397.
  1147	\end{thebibliography}
  1148	
  1149	\end{document}

codex
The first read was truncated, so I’m continuing by reading bounded line ranges from the same file only. I won’t compile it, because compilation could follow external inputs beyond the one-file constraint; I’ll verify syntax, package use, labels/references, and likely box/spacing risks statically.
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '421,710p' papers/latex/productive-power.tex | nl -ba -v421" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   421	\small
   422	\caption{Who holds the productive pillar in each regime type, and how concentrated control over the terms of production is. Concentration is a qualitative judgment from the cited literature, not a coded value.}
   423	\label{tab:regimes}
   424	\begin{tabularx}{\textwidth}{@{}L{2.6cm}YYL{2.6cm}@{}}
   425	\toprule
   426	Regime type & Main producers and payers & Who sets the terms of participation & Concentration of control \\
   427	\midrule
   428	Market-capitalist & Wage earners, small firms, consumers and taxpayers & Employers in labor markets and the state through tax and labor law & Varies by local market and is high in many \\
   429	Communist party-state & State employees, collective farmers and, in the reform era, migrant workers & The party-state as employer, purchaser and owner & Near the maximum before reform \\
   430	Social democracy and market socialism & Wage earners and the self-employed under encompassing bargaining & Unions, employers' associations and the state jointly & Moderate, with power shared by peak organizations \\
   431	Islamic states & Ottoman peasants and guild artisans, Iranian workers, Gulf citizens and migrants & Intermediaries and guilds in the Ottoman case, the rentier state and sponsors in the Gulf & Moderate in the Ottoman case and high for Gulf migrants \\
   432	Catholic monarchies & Peasants, artisans and colonial indigenous communities & Lords, the Church as landholder and tithe receiver, and the crown & High locally, shared among privileged estates \\
   433	Secular democracies & Citizen taxpayers and wage earners & Legislatures, tax administrations and labor markets & Varies with the economic regime \\
   434	\bottomrule
   435	\end{tabularx}
   436	\end{table}
   437	
   438	\begin{table}[p]
   439	\centering
   440	\small
   441	\caption{Coupling of the productive pillar to other pillars, channels of exit and voice, and documented checks. Each documented check is cited in the corresponding subsection.}
   442	\label{tab:regimes2}
   443	\begin{tabularx}{\textwidth}{@{}L{2.6cm}YYY@{}}
   444	\toprule
   445	Regime type & Principal couplings & Exit and voice & A documented check \\
   446	\midrule
   447	Market-capitalist & Capital allocation and employment are held by the same actors & Job mobility, unions and the vote & Union wage compression in the mid-twentieth century \\
   448	Communist party-state & One apparatus prices output, writes labor law, runs unions and polices mobility & Turnover, evasion, petitions and migration after reform & Shop-floor control of the pace of work by Soviet workers \\
   449	Social democracy and market socialism & Corporatist bargaining joins producers and the legislature & Encompassing unions, elections and universal benefits & Universal programs that enlarged redistribution \\
   450	Islamic states & Guilds joined crafts to administration, and rents join citizens to the state & Guild petitions, courts, strikes and quiet encroachment & Oil workers' strikes in the Iranian revolution \\
   451	Catholic monarchies & The Church joined land, tithe and legitimation, and the crown joined tax and justice & Village litigation, the Cortes, flight and revolt & Burgundian villages contesting dues in royal courts \\
   452	Secular democracies & Taxpayers and the franchise are joined in the same citizens & Elections, courts, unions and mass non-cooperation & Progressive taxation after wars of mass mobilization \\
   453	\bottomrule
   454	\end{tabularx}
   455	\end{table}
   456	
   457	Section~\ref{sec:mechanisms} derives the mechanism behind the regularity: each instrument that worsened producers' terms in these cases lowers the outside option or organized weight in the production game, and each is held outside the productive pillar.
   458	
   459	\section{Mechanisms, failure modes and checks}
   460	\label{sec:mechanisms}
   461	
   462	Producers' terms in the production game of Definition~\ref{def:productive-power:game} are set by five quantities: what producers can obtain by leaving, how well they are organized, how concentrated control over their participation is, how much of the coalition's revenue comes from elsewhere, and whether access to exchange is conditioned on allegiance. Each is a parameter of the game, and the results below give their comparative statics. The model is deliberately simple so that the mechanisms stay separate, and its parameters are not estimated here.
   463	
   464	\subsection{Exit and concentration}
   465	
   466	\begin{lemma}[Exit floor]
   467	\label{lem:productive-power:exit-floor}
   468	If producers are atomized, so that each decides alone whether to participate and the coalition sets $u$, the coalition's optimal terms are $u^*=o$ and the extraction share is $\chi^*=1-o/y$.
   469	\end{lemma}
   470	
   471	\begin{proof}
   472	A producer participates if and only if $u\ge o$. The coalition's revenue $n(y-u)+R$ is decreasing in $u$, so it chooses the smallest $u$ at which producers participate, which is $u=o$.
   473	\end{proof}
   474	
   475	The exit floor is the whole of atomized producers' power. It is zero extraction when $o=y$, as in the band of Proposition~\ref{prop:productive-power:minimal-form}, and maximal extraction when $o=y_0$.
   476	
   477	\begin{lemma}[Concentration lowers the outside option]
   478	\label{lem:productive-power:concentration}
   479	Suppose a producer who leaves employer $j$, and is neither blocked nor gated, receives one new offer, from employer $k$ with probability $s_k$; an offer from a different employer is worth $o_1$ and an offer from the employer just left is worth no more than the fallback $y_0<o_1$. Then the outside option at employer $j$ is the composite $o_j$ of Definition~\ref{def:productive-power:outside}, and the employment-weighted mean is $\bar o=y_0+\gamma(1-g)(1-\HW)(o_1-y_0)$. Under the exit floor, the employment-weighted mean extraction share is
   480	\[
   481	\bar\chi=1-\frac{y_0+\gamma(1-g)(1-\HW)(o_1-y_0)}{y},
   482	\]
   483	which increases linearly in $\HW$.
   484	\end{lemma}
   485	
   486	\begin{proof}
   487	An exit succeeds with probability $\gamma(1-g)$; given success, the offer comes from a different employer with probability $1-s_j$. The expected value is $y_0+\gamma(1-g)(1-s_j)(o_1-y_0)=o_j$. Then $\sum_js_jo_j=y_0+\gamma(1-g)(o_1-y_0)\sum_j s_j(1-s_j)=y_0+\gamma(1-g)(1-\HW)(o_1-y_0)$, since $\sum_js_j=1$. Each employer sets $u_j=o_j$ by Lemma~\ref{lem:productive-power:exit-floor}, so $\chi_j=1-o_j/y$ and the weighted mean is $1-\bar o/y$.
   488	\end{proof}
   489	
   490	The lemma gives the source's concentration index a mechanical role in this pillar. Under its assumptions, average extraction rises linearly with $\HW$, at a rate equal to the value of a competing offer relative to output. A single employer, $\HW=1$, holds every producer at the fallback; this is the company town, and in the limit it is the party-state as sole employer before reform. Many small employers, $\HW\to 0$, give unrestricted producers the competing value $o_1$. The association between labor-market concentration and lower wages found by \citet{azar2022} is consistent with the lemma, though random rematching simplifies search in real labor markets \citep{manning2003}.
   491	
   492	\subsection{Voice and the withdrawal premium}
   493	
   494	Organized producers do not accept the exit floor. They bargain collectively, and their threat is withdrawal: a strike, a tax refusal, a boycott, a delivery strike by farmers, or mass flight. If the coalition's non-producer revenue does not cover its maintenance requirement, withdrawal imposes a cost beyond lost revenue, because the institutions cannot be paid. Let $\psi\ge 0$ be the cost per unit of that shortfall, so that at total revenue $T+R$ the coalition's payoff is
   495	\[
   496	V_S(T)=T+R-K-\psi\,(K-T-R)^+,\qquad (x)^+=\max(x,0).
   497	\]
   498	
   499	\begin{assumption}[Agreement covers maintenance]
   500	\label{ass:productive-power:feasible}
   501	The parameters satisfy $n(1-\eta)(y-o)\ge(1+\eta\psi)(K-R)^+$.
   502	\end{assumption}
   503	
   504	The assumption says that the surplus over producers' exit floor is large enough for an agreement to pay for the institutions. It holds automatically when $R\ge K$. When $R<K$ it fails for $\eta$ close to one, so fully organized producers facing a coalition without outside revenue lie outside the scope of the next result.
   505	
   506	\begin{proposition}[Voice share]
   507	\label{prop:productive-power:voice}
   508	Let producers bargain collectively with the coalition by the asymmetric Nash bargaining solution with producer weight $\eta\in[0,1]$, where disagreement gives producers $no$ and the coalition $V_S(0)=R-K-\psi(K-R)^+$. Under Assumption~\ref{ass:productive-power:feasible}, the agreed terms are
   509	\[
   510	u^*=o+\eta(y-o)+\Omega,\qquad \Omega=\frac{\eta\,\psi\,(K-R)^+}{n},
   511	\]
   512	and the agreement leaves no maintenance shortfall: $n(y-u^*)+R\ge K$.
   513	\end{proposition}
   514	
   515	\begin{proof}
   516	Write $\Psi=\psi(K-R)^+$ and $u_K=y-(K-R)^+/n$, the largest terms at which the coalition's revenue still covers $K$. For $u\le u_K$ the coalition's payoff is $V_S=n(y-u)+R-K$, which is linear; for $u>u_K$ it is lower by $\psi(K-n(y-u)-R)>0$. Consider first the linear problem, which maximizes $N(u)=(n(u-o))^{\eta}(n(y-u)+\Psi)^{1-\eta}$, the product of the gains $n(u-o)$ and $n(y-u)+R-K-V_S(0)=n(y-u)+\Psi$. For $0<\eta<1$ the logarithm of $N$ is strictly concave, and the first-order condition $\eta\,(n(y-u)+\Psi)=(1-\eta)\,n(u-o)$ gives $nu^*=\eta ny+(1-\eta)no+\eta\Psi$, the stated formula; for $\eta=0$ and $\eta=1$ the solution gives the whole gain to the coalition or to the producers, which the formula also covers. At $u^*$, $n(y-u^*)+R-K=n(1-\eta)(y-o)-\eta\Psi-(K-R)$, which is non-negative when $R\ge K$ (then $\Psi=0$) and, when $R<K$, equals $n(1-\eta)(y-o)-(1+\eta\psi)(K-R)\ge 0$ by Assumption~\ref{ass:productive-power:feasible}. So $u^*\le u_K$. The true Nash product with the payoff $V_S$ is never larger than $N(u)$ and equals it for $u\le u_K$. Hence $u^*$, which maximizes $N$ and lies where the two coincide, also maximizes the true Nash product.
   517	\end{proof}
   518	
   519	The terms have three parts. The exit floor $o$ is what producers obtain without organization. The bargained share $\eta(y-o)$ is what organization adds by splitting the surplus over the floor. The withdrawal premium $\Omega$ is what organization adds because the coalition cannot afford a withdrawal; it is the price of the latent veto of Proposition~\ref{prop:productive-power:latent-veto}. Organization is necessary for both of the latter parts. An individual producer's withdrawal costs the coalition only that producer's contribution $y-u$, which in a large population is too small to threaten the maintenance requirement. That is why the latent veto stays latent without collective action \citep{olson1965}. Unions, guilds, village communities, peasant assemblies, tax revolts and cooperatives are the institutions that raise $\eta$ above zero.
   520	
   521	\begin{corollary}[Organization flattens the concentration gradient]
   522	\label{cor:productive-power:gradient}
   523	Suppose each employer $j$ bargains with its own workers as in Proposition~\ref{prop:productive-power:voice}, with common weight $\eta$, common premium $\Omega$ and outside option $o_j$ from Definition~\ref{def:productive-power:outside}. Then the employment-weighted mean terms are $\bar u=\bar o+\eta(y-\bar o)+\Omega$, and
   524	\[
   525	\frac{\partial\bar u}{\partial\HW}=-(1-\eta)\,\gamma\,(1-g)\,(o_1-y_0)\le 0 .
   526	\]
   527	\end{corollary}
   528	
   529	\begin{proof}
   530	Averaging $u_j=o_j+\eta(y-o_j)+\Omega$ with weights $s_j$ gives $\bar u=(1-\eta)\bar o+\eta y+\Omega$. By Lemma~\ref{lem:productive-power:concentration}, $\partial\bar o/\partial\HW=-\gamma(1-g)(o_1-y_0)$, and the stated derivative follows.
   531	\end{proof}
   532	
   533	Hirschman's loyalty has an ambiguous place in the model. Loyalty that raises the threshold for exit lowers the effective outside option and with it the floor; loyalty that keeps members inside while they organize raises $\eta$ \citep{hirschman1970}. Which effect dominates depends on whether the loyal can speak.
   534	
   535	The same bargaining logic applies inside the household, where most care labor is done. \citet{agarwal1997} argued that a household member's bargaining power depends on the fallback position available outside the household: property, paid employment, access to common resources, and support from kin, community or state. In the notation of the model, a carer's terms are $o_h+\eta_h(y_h-o_h)$, where $o_h$ is that fallback and $\eta_h$ the carer's organized or normative standing. Property rights, divorce law, public childcare and access to paid work all act on $o_h$. The paper does not develop the household game further, but the instruments that set $o_h$ are, like those in Assumption~\ref{ass:productive-power:instruments} below, held largely in $\pP$, $\pJ$ and $\pI$.
   536	
   537	\subsection{The bondage condition}
   538	
   539	A coalition can lower the outside option directly by restricting mobility. Write $o(g)=y_0+(1-g)(o_0-y_0)$, where $o_0$ is the outside option at $g=0$ given by Definition~\ref{def:productive-power:outside}. Enforcement costs the coalition $\kappa(g)$ per producer, with $\kappa(0)=0$ and $\kappa$ increasing and convex.
   540	
   541	\begin{proposition}[Domar-Brenner condition]
   542	\label{prop:productive-power:domar}
   543	Suppose the coalition chooses $g$ and then sets terms, with producers bargaining with weight $\eta\in[0,1)$ as in Proposition~\ref{prop:productive-power:voice} (the atomized case is $\eta=0$), and Assumption~\ref{ass:productive-power:feasible} holds at every $g$. Then the coalition's payoff, net of terms that do not depend on $g$, is $n[(1-\eta)g(o_0-y_0)-\kappa(g)]$.
   544	\begin{enumerate}
   545	\item[(a)] If $\kappa(g)=\kappa g$ is linear, restriction is chosen ($g^*=1$) when $(1-\eta)(o_0-y_0)>\kappa$ and not chosen ($g^*=0$) when $(1-\eta)(o_0-y_0)<\kappa$.
   546	\item[(b)] If $\kappa$ is differentiable and strictly convex with $\kappa'(0)<(1-\eta)(o_0-y_0)<\kappa'(1)$, then $g^*\in(0,1)$ is the unique solution of $\kappa'(g^*)=(1-\eta)(o_0-y_0)$, and $g^*$ is increasing in $o_0-y_0$ and decreasing in $\eta$.
   547	\end{enumerate}
   548	\end{proposition}
   549	
   550	\begin{proof}
   551	By Proposition~\ref{prop:productive-power:voice}, the producers' terms at outside option $o$ are $u^*=o+\eta(y-o)+\Omega$, where $\Omega$ does not depend on $o$, and the agreement leaves no shortfall, so the coalition's payoff from producers is $n(y-u^*)=n[(1-\eta)(y-o)-\Omega]$. Substituting $o(g)=o_0-g(o_0-y_0)$ gives $n[(1-\eta)(y-o_0)-\Omega]+n(1-\eta)g(o_0-y_0)$, and subtracting enforcement cost $n\kappa(g)$ leaves the stated $g$-dependent part. In case (a) the payoff is linear in $g$ with slope $n[(1-\eta)(o_0-y_0)-\kappa]$, so the optimum is at $g=1$ when the slope is positive and at $g=0$ when it is negative. In case (b) the payoff is strictly concave, its derivative is positive at $g=0$ and negative at $g=1$, so the unique maximizer satisfies the first-order condition. Because $\kappa'$ is strictly increasing, a larger right side $(1-\eta)(o_0-y_0)$ requires a larger $g^*$; the right side increases in $o_0-y_0$ and decreases in $\eta$.
   552	\end{proof}
   553	
   554	The proposition places two classic explanations of bondage in one inequality. Domar's land-labor hypothesis concerns $o_0$: where land is abundant, a free peasant can leave and farm independently, so $o_0$ is high and binding the peasant pays \citep{domar1970}. Where land is scarce and labor abundant, $o_0$ is already close to $y_0$, the wage market holds producers near the floor, and restriction adds little. Brenner's objection concerns $\kappa$ and $\eta$: organized peasant communities raise the cost of enforcing restriction and bargain over terms, so the same land-labor ratio produced serfdom in one region and free tenure in another \citep{brenner1976}. The two accounts are not rivals in this form. They name different terms of the same condition, and the empirical question is which term varied more across the cases at issue.
   555	
   556	Organization also lowers the return to restriction, since a coalition facing organized producers captures only the fraction $1-\eta$ of any reduction in their outside option. That gives a reason for coercive suppression of organization to accompany mobility restriction, a joint pattern visible in collectivization and in the sponsorship system for migrants, where workers' organization was also restricted. Part V \citep{long2026coercive} gives the primary treatment of this pair in its Section 6.5, including the allegiance margin of sanctions (its Definition 2.5) on which coercive enforcement of a gate depends.
   557	
   558	\subsection{Rents}
   559	
   560	\begin{proposition}[Rentier comparative static]
   561	\label{prop:productive-power:rentier}
   562	In Proposition~\ref{prop:productive-power:voice}, the withdrawal premium $\Omega$ is non-increasing in non-producer revenue $R$. It falls at rate $\eta\psi/n$ while $R<K$ and is zero for all $R\ge K$. The exit floor and the bargained share do not depend on $R$.
   563	\end{proposition}
   564	
   565	\begin{proof}
   566	$\Omega=\eta\psi(K-R)^+/n$. For $R<K$ its derivative in $R$ is $-\eta\psi/n\le 0$; for $R\ge K$ it is identically zero. The other two terms, $o$ and $\eta(y-o)$, contain no $R$. Raising $R$ relaxes Assumption~\ref{ass:productive-power:feasible}, so the result stays within its scope.
   567	\end{proof}
   568	
   569	The proposition refines the rentier-state argument. Rents do not lower producers' terms by making producers less productive or less organized. They remove the part of producers' bargaining power that rested on the coalition's need for their contribution, and they remove it only up to the point where rents cover the maintenance requirement. Beyond that point additional rent changes nothing in this model. Within a country, the effect of rents on concessions to producers should therefore be concentrated near the threshold at which rents cover the cost of running the state, and small far above or below it. Across countries, a null average effect such as that reported by \citet{habermenaldo2011} is consistent with the model if most variation lies away from the threshold. Measuring the maintenance requirement is difficult, and Section~\ref{sec:measurement} proposes a proxy.
   570	
   571	For the citizens of a rentier state, the premium is near zero and their terms are set by the coalition's choice to distribute rent, not by their capacity to withhold. The producers of the rent are elsewhere, and Lemma~\ref{lem:productive-power:relocation} says where: in the extraction workforce, which in the Gulf monarchies is largely foreign, and among foreign buyers.
   572	
   573	\subsection{The participation gate}
   574	
   575	A coalition can lower producers' outside options without restricting their movement, by conditioning access to exchange. A producer who cannot buy inputs, sell output, obtain credit or be hired has nowhere to go even if free to walk away.
   576	
   577	\begin{proposition}[Gate]
   578	\label{prop:productive-power:gate}
   579	Let $o$ denote the outside option at $\gamma=1$, so that under the gate of Definition~\ref{def:productive-power:gate} it is $o_\gamma=y_0+\gamma(o-y_0)$. Under Assumption~\ref{ass:productive-power:feasible}, the agreed terms are $u^*(\gamma)=o_\gamma+\eta(y-o_\gamma)+\Omega$, and
   580	\[
   581	\frac{\partial u^*}{\partial\gamma}=(1-\eta)(o-y_0)\ge 0 .
   582	\]
   583	If the gate is closed ($\gamma=0$), producers are atomized ($\eta=0$) and rents cover the maintenance requirement ($R\ge K$), producers are held at the autarky value, $u^*=y_0$, and the coalition takes $n(y-y_0)$.
   584	\end{proposition}
   585	
   586	\begin{proof}
   587	Substitute $o_\gamma$ for $o$ in Proposition~\ref{prop:productive-power:voice}. Since $do_\gamma/d\gamma=o-y_0$ and $u^*$ depends on the outside option through $(1-\eta)o_\gamma$, the derivative follows. With $\gamma=0$, $o_\gamma=y_0$; with $\eta=0$, $\Omega=0$ and $u^*=o_\gamma=y_0$, and the coalition's revenue from producers is $n(y-y_0)$.
   588	\end{proof}
   589	
   590	The closed gate with atomized producers is the most complete form of producer dependence in the model. Nothing about it requires the producers to be owned, bound to land, or imprisoned. It requires only that access to exchange pass through a checkpoint controlled by the coalition and that the checkpoint test allegiance. The coalition needs control over exchange (markets, credit, licenses, employment) to build the checkpoint, a criterion of allegiance to apply at it, and enforcement to keep producers from trading around it. Part IV (Section 6.5) treats the coupling of belief and production from the side of belief, including the quasi-voluntary compliance of taxpayers. Section~\ref{sec:revelation} returns to this configuration.
   591	
   592	\subsection{Capture of the productive pillar}
   593	
   594	\begin{definition}[Capture of the productive pillar]
   595	\label{def:productive-power:w-capture}
   596	A \emph{productive capture link} is a capture link $(S\to j,\pW)$ in the sense of \citet{largo2026hbs} in which the privileged discretion held by $S$ is control over one of the parameters through which the production game sets producers' terms: their exit (through $g$ or the concentration $\HW$), their organization (through $\eta$), their access to exchange (through $\gamma$), or the coalition's exposure to their withdrawal (through non-producer revenue $R$ or the shortfall cost $\psi$). Material evidence must tie the exercise of that control to the terms $u$ or the extraction share $\chi$. The productive pillar is \emph{captured} at $t$ when productive capture links persist and the pillar's term $H_{\pW,t}(1-\QW_t)$ in $U_t$ is high.
   597	\end{definition}
   598	
   599	The definition inherits the source's three conditions, including the requirement of material evidence. Low wages, high taxes or concentrated employment do not by themselves establish capture. They may reflect low productivity, the cost of public goods that producers value, or economies of scale. Capture requires a documented instrument and a documented link from the instrument to the terms.
   600	
   601	\begin{assumption}[Assignment of instruments]
   602	\label{ass:productive-power:instruments}
   603	The instruments that change the parameters of the production game are exercised in the following pillars. Mobility restriction $g$ requires enforcement in $\pC$. Concentration of control over productive means, which raises $\HW$, is an allocation of resources in $\pF$. Lowering producers' organized weight $\eta$ requires prohibition in $\pP$, enforcement in $\pC$ or delegitimation in $\pI$. Closing the gate requires control of exchange in $\pF$, an allegiance criterion supplied in $\pI$ (the legitimation function of Part IV, Definition 2.1, the practices that produce and validate the beliefs about rules and authority on which members' coordination depends \citep{long2026ideological}), and enforcement in $\pC$. Raising non-producer revenue $R$ is an allocation in $\pF$. Lowering the shortfall cost $\psi$ requires reserves accumulated in $\pF$ or the lawful hiring of replacement producers, whose permission is set in $\pP$.
   604	\end{assumption}
   605	
   606	\begin{corollary}[Capture requires coupling]
   607	\label{cor:productive-power:coupling}
   608	Under Assumption~\ref{ass:productive-power:instruments}, any action by a coalition $S$ that lowers producers' terms $u^*$ below their value at the baseline parameters $(\HW^0,g=0,\eta_0,\gamma=1,R_0,\psi_0)$ is taken in at least one pillar $n\ne\pW$. Hence a captured productive pillar implies $C_{n\pW,t}>0$ for some $n\in\{\pF,\pP,\pI,\pC\}$, with $S$ the coalition in question.
   609	\end{corollary}
   610	
   611	\begin{proof}
   612	By Proposition~\ref{prop:productive-power:voice}, Proposition~\ref{prop:productive-power:gate} and Lemma~\ref{lem:productive-power:concentration}, $u^*$ is non-decreasing in $o$, $\eta$, $\gamma$ and $\psi$ and non-increasing in $R$, with $o$ non-increasing in $g$ and $\HW$ by Definition~\ref{def:productive-power:outside}. Holding output $y$ and the maintenance requirement $K$ fixed, a reduction of $u^*$ therefore requires raising $g$ or $\HW$, lowering $\eta$, $\gamma$ or $\psi$, or raising $R$. By Assumption~\ref{ass:productive-power:instruments} each of these is exercised in a pillar other than $\pW$. If $S$ exercises it and also holds the terms of production, $S$ commands decisions in both $\pW$ and that pillar, which is $C_{n\pW,t}>0$.
   613	\end{proof}
   614	
   615	The corollary depends on the assignment, which is a modeling claim rather than a theorem. The hardest case for it is the hiring of replacement workers during a strike, which happens in the labor market itself; the assignment places it in $\pP$ because whether replacement is lawful is decided there. The assignment is defensible because each instrument in the comparative record was in fact exercised outside the productive layer: passports and residence permits by police and ministries, procurement prices by planners, union prohibitions by legislatures and courts, and allegiance tests by the authorities that define loyalty. Its consequence is that capture of production is never a fact about production alone. A society in which producers work long hours for low pay under many competing employers, free to organize and to leave, has a poor productive pillar but not a captured one. This is the pillar-level form of Largo's requirement that a strong classification show both concentration and cross-pillar integration \citep{largo2026hbs}, and of Part VII's result that Proposition A does not imply Proposition B. The function is implemented at every parameter value of the production game. Capture is a region of the parameter space.
   616	
   617	\subsection{Failure modes and checks}
   618	
   619	Each instrument in the production game defines a failure mode, and each failure mode has a check that interrupts it.
   620	
   621	Concentration of employment or purchase lowers the outside option (Lemma~\ref{lem:productive-power:concentration}). Antitrust enforcement in labor markets, the entry of new employers and public employment of last resort raise $o$. Cooperatives add an employer that producers themselves control \citep{dow2003}.
   622	
   623	Mobility restriction lowers the outside option directly (Proposition~\ref{prop:productive-power:domar}). Portability of benefits, abolition of tied residence and the right to change employer interrupt it. The condition in Proposition~\ref{prop:productive-power:domar} also shows when the check is under most pressure: when producers' free outside options are high, the coalition gains most from restriction.
   624	
   625	Suppression of organization lowers $\eta$ and with it both the bargained share and the withdrawal premium (Proposition~\ref{prop:productive-power:voice}). Legal protection of association and strikes, independent courts that enforce it (Part III, Section 6), and union democracy interrupt it. Michels's argument that organizations develop oligarchic leaderships applies to unions as well \citep{michels1915}, and Part II states it as a conditional tendency (its Proposition 6.2) rather than a law. The International Typographical Union studied by \citet{lipset1956} is the classic documented exception, a union that kept a two-party internal democracy.
   626	
   627	Rents remove the withdrawal premium (Proposition~\ref{prop:productive-power:rentier}). Fiscal rules that route rents into funds outside the coalition's discretion, and taxation that keeps the state dependent on domestic producers, are the checks the model suggests. Their effectiveness is an empirical question this paper does not settle.
   628	
   629	The gate lowers outside options through control of exchange (Proposition~\ref{prop:productive-power:gate}). Open markets, multiple sources of credit and employment, and the legal separation of economic access from political allegiance keep $\gamma$ close to one. The check is a separation of pillars: the actors who test allegiance must not control exchange.
   630	
   631	\begin{figure}[t]
   632	\centering
   633	\begin{tikzpicture}[x=1cm,y=1cm,>=stealth]
   634	  \node[draw,rounded corners,minimum width=2.6cm,minimum height=1.2cm,align=center] (W) at (0,0) {Producers\\ $\pW$};
   635	  \node[draw,rounded corners,minimum width=2.6cm,minimum height=1.2cm,align=center] (S) at (7,0) {Coalition $S$\\ maintenance $K$};
   636	  \node[align=center,font=\small] (F) at (0,2.6) {$\pF$: concentration $\HW$,\\ rents $R$, control of exchange};
   637	  \node[align=center,font=\small] (C) at (0,-2.6) {$\pC$: mobility restriction $g$,\\ enforcement of the gate};
   638	  \node[align=center,font=\small,anchor=east] (PI) at (-2.6,0) {$\pP$, $\pI$: organization $\eta$,\\ allegiance test};
   639	  \draw[->,thick] ([yshift=3mm]W.east) -- node[above,font=\small]{output $n(y-u)$} ([yshift=3mm]S.west);
   640	  \draw[->,thick,dashed] ([yshift=-3mm]W.east) -- node[below,font=\small]{withdrawal threat $\Omega$} ([yshift=-3mm]S.west);
   641	  \draw[->] (F) -- (W);
   642	  \draw[->] (C) -- (W);
   643	  \draw[->] (PI) -- (W);
   644	\end{tikzpicture}
   645	\caption{Instruments of the production game. Producers supply output to the coalition and hold a withdrawal threat whose value depends on the coalition's maintenance shortfall; every instrument that lowers producers' terms is held in another pillar.}
   646	\label{fig:instruments}
   647	\end{figure}
   648	
   649	\section{Measurement}
   650	\label{sec:measurement}
   651	
   652	The model's parameters correspond to observable quantities, though several can be measured only by proxy. Table~\ref{tab:indicators} lists an indicator for each. The list follows the source's rule that weights and codings be preregistered and that no aggregate index be reported for a real country without a documented coding \citep{largo2026hbs}. Largo also warns that measurement invariance across regimes must be tested before indicators are compared \citep{largo2026hbs}. Union density means something different under a party-controlled federation than under independent unions, and the indicators below are meant to be coded with that difference recorded.
   653	
   654	\begin{table}[t]
   655	\centering
   656	\small
   657	\caption{Indicators for the parameters of the production game and the components of productive contestability. Each indicator requires a preregistered coding rule before use.}
   658	\label{tab:indicators}
   659	\begin{tabularx}{\textwidth}{@{}L{3.6cm}Y@{}}
   660	\toprule
   661	Quantity & Indicator \\
   662	\midrule
   663	Concentration $\HW$ & Herfindahl index of employment or vacancy shares in local labor markets, the state's share of employment, and the share of farm output sold to a single purchaser \\
   664	Outside option $o$ & Rates of job-to-job transition, wage changes on switching employer, and the legal ability to change employer or residence \\
   665	Mobility restriction $g$ & Statutes and practice on internal passports, residence permits tied to an employer, and debt or land ties \\
   666	Organized weight $\eta$ & Union density, bargaining coverage, legality of strikes, and the independence of unions from the ruling party or employer \\
   667	Rents and maintenance, $R$ and $K$ & Non-tax revenue relative to recurrent spending on administration, courts, security and public information \\
   668	Producer dependence $\xi$ & Share of government revenue raised from domestic taxes and contributions \\
   669	Participation gate $\gamma$ & Rules that condition employment, licenses, credit or market access on political or religious criteria, coded from statute and documented practice \\
   670	Legal access $q^{\mathrm{leg}}$ & Availability, cost and independence of labor and tax adjudication, coded with the components of Part III, Definition 2.4 \\
   671	Income protection $q^{\mathrm{inc}}$ & Replacement rates of unemployment, sickness and old-age insurance \\
   672	Care labor $h$ and carers' fallback $o_h$ & Time-use surveys of unpaid care by sex, coverage of public childcare and paid leave, and women's property and divorce rights \\
   673	\bottomrule
   674	\end{tabularx}
   675	\end{table}
   676	
   677	The maintenance requirement $K$ is the hardest quantity to measure. A workable proxy is recurrent spending on the core functions of the other five pillars, excluding transfers and investment, since those are the outlays that cannot be postponed without loss of function. The proxy is imperfect because some transfers are themselves maintenance (pensions to soldiers, stipends to clergy) and because the shortfall cost $\psi$ depends on reserves and borrowing capacity. A preregistered study would fix the proxy and test sensitivity to alternatives.
   678	
   679	The model and the comparison yield nine testable hypotheses, listed with their falsifiers in Table~\ref{tab:hypotheses}. Several refine the source's hypotheses H5 and H6 \citep{largo2026hbs}.
   680	
   681	\begin{table}[t]
   682	\centering
   683	\small
   684	\caption{Hypotheses for the productive pillar. Each prediction follows from the result named in the second column; the falsifier is the observation that would refute it.}
   685	\label{tab:hypotheses}
   686	\begin{tabularx}{\textwidth}{@{}L{1.0cm}L{2.4cm}YY@{}}
   687	\toprule
   688	 & Basis & Prediction & Falsifier \\
   689	\midrule
   690	HW1 & Source H5, Lemma~\ref{lem:productive-power:concentration} & Higher bargaining coverage weakens the association between employer concentration and lower pay & The concentration gradient is the same at high and low coverage \\
   691	HW2 & Fiscal contract & Governments concede more services and representation where domestic taxes supply more revenue & No relation after conditioning on income, as some tests find \\
   692	HW3 & Proposition~\ref{prop:productive-power:rentier} & The effect of rents on concessions to producers is largest where rents are close to the cost of running the state & The effect is uniform in the ratio of rents to maintenance or largest far from one \\
   693	HW4 & Proposition~\ref{prop:productive-power:domar} & Bondage is more frequent where free exit is valuable and enforcement is cheap & Its incidence is unrelated to both across regions under comparable states \\
   694	HW5 & Everyday resistance & Covert non-compliance rises where open voice is suppressed & Evasion and turnover are unrelated to repression of organization \\
   695	HW6 & Insiders and outsiders & Contestability differs between permanent and precarious workers in encompassing welfare states & No difference in bargaining coverage or income protection between the groups \\
   696	HW7 & Persistence & Compelled labor drafts leave lower consumption in affected districts long after abolition & Comparable drafts show no persistent effect at their boundaries \\
   697	HW8 & Source H6 & Higher tax revenue with accountable provision goes with lower worker vulnerability & Vulnerability rises with provision \\
   698	HW9 & Lemma~\ref{lem:productive-power:reproduction} and household bargaining & Unpaid care is shared more evenly where carers' fallback positions are stronger & The division of unpaid care is unrelated to property rights, paid employment and public care \\
   699	\bottomrule
   700	\end{tabularx}
   701	\end{table}
   702	
   703	The exit hypotheses, HW1, HW4 and HW7, test how outside options set terms. HW1 is Corollary~\ref{cor:productive-power:gradient}: organization scales the concentration gradient by $1-\eta$, so it should be flatter where bargaining coverage is high. HW4 is the Domar-Brenner condition, and its test requires regional comparisons within one state, so that enforcement institutions are held roughly constant while land-labor ratios and peasant organization vary. HW7 generalizes \citet{dell2010}, whose regression-discontinuity design at the boundary of the draft area is the template.
   704	
   705	The fiscal hypotheses, HW2, HW3 and HW8, test the coalition's dependence on producers. HW2 carries the condition that \citet{ross2004} found necessary: the relevant variable is the price of government services, not taxation alone. HW3 is the paper's sharpest new prediction. If most observed variation in rents lies far from the threshold at which rents cover the cost of the state, it reconciles the rentier literature with null findings such as those of \citet{habermenaldo2011}. HW8 is the source's public-goods rival stated for producers: if it holds, high taxation is not evidence of extraction.
   706	
   707	The voice hypotheses, HW5, HW6 and HW9, test what happens to producers whose organized weight is low. HW5 follows \citet{scott1985} and the Soviet evidence of \citet{fitzpatrick1994} and \citet{filtzer1986}, and its difficulty is that covert resistance is hard to observe by design. HW6 tests the insider-outsider cleavage that \citet{rueda2005} identified. HW9 applies the household version of the bargaining model, with the fallback positions emphasized by \citet{agarwal1997}.
   708	
   709	Two identification problems apply to all nine. Organization is endogenous to the terms it is supposed to explain, since producers organize more where they expect gains. Rents, concentration and gates are chosen by coalitions that anticipate producers' responses. Event studies around reforms that change one instrument at a time, of the kind Largo proposes for oversight reforms \citep{largo2026hbs}, are the most direct remedy. Examples include the abolition of tied residence, the legalization of independent unions and the creation of a sovereign fund that removes rents from current budgets.
   710	

exec
/usr/local/bin/zsh -lc "sed -n '711,865p' papers/latex/productive-power.tex | nl -ba -v711" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   711	\section{The Revelation reading}
   712	\label{sec:revelation}
   713	
   714	The series reads Revelation 13 and 17 to 18 typologically: the beast is a recurring pattern of power that claims ultimate loyalty, and Babylon is the idolatrous city of every age \citep{bauckham1993,beale1999}. The reading is anchored in the text's first-century setting, the Roman province of Asia, where the imperial cult was a civic institution woven into local life \citep{price1984,friesen2001}. Futurist readings that identify the beast or the mark with a coming government, person, product, technology or payment system are excluded. Their reception history is a record of failed identifications \citep{boyer1992,fuller1995,mcginn1998}. Historicist readings that identified the beast with a particular church or ruler belong to the history of polemic and are excluded for the same reason. The mapping of images to pillars below is a heuristic that aids comparison. It is an interpretive claim of this project, not a settled exegetical result.
   715	
   716	The passage most directly relevant to this pillar is Revelation 13:16-17 (KJV): ``And he causeth all, both small and great, rich and poor, free and bond, to receive a mark in their right hand, or in their foreheads: And that no man might buy or sell, save he that had the mark, or the name of the beast, or the number of his name.'' The verse does not describe a form of labor. It describes a condition on participation in exchange. Its scope runs across every category of the social order, ``free and bond'' included, so the condition is not the bondage of a class but the gating of everyone's access to buying and selling by a sign of allegiance.
   717	
   718	In the terms of Section~\ref{sec:mechanisms}, the verse depicts a closed participation gate, $\gamma=0$, applied to all who withhold allegiance. Proposition~\ref{prop:productive-power:gate} says what such a gate requires and what it yields. It requires control over exchange, a criterion of allegiance and enforcement. In the vision these are distributed across figures: the first beast holds authority and makes war (13:2, 13:4, 13:7); the second beast speaks, performs signs and causes the image of the first to be worshipped (13:12-15); and the restriction on buying and selling is its economic instrument. The series' heuristic maps these to $\pP$ and $\pC$, to $\pI$, and to the coupling of $\pF$ with $\pW$. The gate also yields a precise result: producers without organization or exit are held to their autarky value. The vision's image of economic exclusion as the sanction for refused allegiance is the limiting case of the model, and it is a limiting case of capture (Proposition B), not of the productive function itself.
   719	
   720	The preterist anchor gives the image economic content. \citet{kraybill1996} argued that participation in the maritime trade and trade guilds of Asia Minor entangled Christians in the imperial cult, and that John's vision calls them to withdraw from commerce on those terms. \citet{bauckham1991} read the lament over Babylon in Revelation 18 as an economic critique of Rome. The cargo list of 18:11-13 runs through luxury goods and ends with ``slaves, and souls of men,'' an indictment of a trade that included human beings. This is literal chattel slavery in the Roman economy. It is the extreme of Table~\ref{tab:bondage} and must not be read as a metaphor for wage labor or taxation. The list also illustrates the relocation lemma: the goods that sustained the imperial center were produced across the provinces and beyond them, and the kings, merchants and shipmasters who lament Babylon's fall (18:9-19) are those whose wealth depended on that flow.
   721	
   722	The text's response to the gate has the shape of Hirschman's triad, though it was written for different purposes. The imperative ``Come out of her, my people'' (18:4) is a call to exit. Faithful witness (11:3-13) and the ``patience and the faith of the saints'' (13:10) are a form of voice that refuses the demanded loyalty. Loyalty itself is the contested object: the vision depicts a demand for worship, and the faithful are those who give their allegiance elsewhere. \citet{rossing1999} read the contrast between Babylon and the New Jerusalem as a choice between two cities, with an economic critique of imperial Rome at its center. \citet{wink1992} generalized the beast into a domination system present in institutions of every age, a reading congenial to the series' claim that the structure is universal.
   723	
   724	The analogy has limits that must be stated. Revelation is apocalyptic literature, and its resolution is divine judgment, not producers' bargaining. \citet{collins1984} argued that the book addresses a crisis that was partly perceived, written to produce catharsis in its readers, and \citet{thompson1990} questioned the extent of persecution under Domitian. The verses supply an image of the limiting case of capture in this pillar, and the model supplies the conditions under which that limit is approached. Neither depends on the other. The analytic claims of this paper stand without the theological reading, and the reading identifies no present institution with the beast.
   725	
   726	\section{Objections and scope conditions}
   727	\label{sec:objections}
   728	
   729	A Marxian reader will object that production is not one pillar among six but the base on which the others rest, and that the framework flattens class relations into a network. The paper's own results partly concede the point. The latent veto gives production a status that no other pillar has: every other function consumes what this one supplies. But Proposition A asserts only that all six functions exist and depend on one another, not that they carry equal causal weight. Whether production determines the other pillars is a claim about the dependency matrix $B_t$, and it is an empirical question. Largo describes the framework as mid-range institutional theory that treats producers as active rather than as a passive base \citep{largo2026hbs}. The functional-explanation debate in Marxism \citep{cohen1978,elster1985} is a reminder that claims of determination need mechanisms, which is what the production game attempts to supply.
   730	
   731	A liberal reader will object that the extraction share mislabels returns to capital and payments for public services, and that market exchange is voluntary. The model accommodates the objection rather than rejecting it. The extraction share is net of services returned. Under competitive conditions, with many employers and free mobility, Lemma~\ref{lem:productive-power:concentration} gives producers the competitive value of their labor, and the liberal benchmark is the case $\HW\to 0$. Capture requires a documented instrument and a documented link to terms. What the model denies is only that voluntariness is a property of exchange as such. It depends on the outside option, and the outside option is shaped by concentration, restriction and gates.
   732	
   733	A functionalist objection runs the other way: the paper may have explained the existence of production by its usefulness. It has not. Lemma~\ref{thm:productive-power:necessity} is a condition of persistence. It says that persistent collectives produce, not that their productive institutions exist because they help the collective persist. This is the standard of \citet{hempel1959} and \citet{elster1983}, and the series adopts it throughout. \citet{merton1968} supplies the further point that functional alternatives exist: the same function is met by foraging bands, serf villages, kolkhozes and labor markets.
   734	
   735	Unpaid household labor enters the formal results in two places only: the reproduction lemma, which makes care a condition of persistence, and the household application of the bargaining model. The production game itself treats its $n$ producers as identical and sets their terms with the coalition, so it does not derive how care is divided within households or how that division interacts with the terms of paid work. A full treatment would solve the household game jointly with the production game, with each member's fallback set by property, divorce law and access to paid work. This paper states the household game's structure and one hypothesis (HW9) but does not solve it jointly.
   736	
   737	The comparative statics are monotone in the parameters, and that monotonicity, not the functional forms, carries the paper's qualitative claims. The functional forms are simple. The production game is stationary, its producers are identical within a group, and the asymmetric Nash solution summarizes rather than models the process of strikes and concessions. Real coalitions face heterogeneous producers, such as citizens and migrants or capital and labor, so the model must be applied group by group.
   738	
   739	Two simplifications bear directly on the size of the effects. Reserves and borrowing let coalitions survive withdrawal longer than the stationary shortfall cost suggests, which shrinks the withdrawal premium. The concentration lemma assumes random rematching in proportion to employment shares, which fixes the linear form of the concentration gradient. Relaxations that preserve monotonicity leave the signs of the results intact; their magnitudes require estimation.
   740	
   741	The claims about producer power are conditional on human activity remaining necessary for production. Lemma~\ref{lem:productive-power:relocation} keeps the function in place under full automation, but it moves the producer role to the owners and maintainers of equipment, and the latent veto of labor goes with it.
   742	
   743	\section{Conclusion}
   744	\label{sec:conclusion}
   745	
   746	Production is the one function every other function consumes. From the maintenance axiom, a persistent collective must produce at a positive average rate, and rents, tribute and machines relocate production without removing it. Producers therefore hold a latent veto over any governance system whose outside revenue falls short of its maintenance requirement. The production game prices that veto. Producers' terms rise with their outside option and their organization, fall linearly with the concentration of control over their participation, and lose their withdrawal premium once rents cover the cost of running the state. Restriction of mobility pays exactly when free exit is valuable and enforcement cheap.
   747	
   748	Every instrument that lowers producers' terms is exercised in another pillar. The capture of production is therefore always a coupling of production with coercion, allocation, rule-making or legitimation, and never a property of production alone. The comparison of six regime types found the productive function in all of them and its worst forms where control over production was concentrated and coupled to coercion and to control of exchange: under a communist party, a Catholic monarchy and a modern monarchy legitimated by Islam alike. Producers' voice was strongest under social democracy, in some Ottoman guilds and among Burgundian villagers using royal courts. Ideology did not sort the cases. The instruments did.
   749	
   750	What remains uncertain is quantitative. None of the model's parameters has been estimated here, and the sharpest prediction, that rents matter most where they nearly cover the cost of the state, awaits a test. The structural claim does not wait on that test. Every governance system in the record depends on those who produce for it, and the image of a world in which no one may buy or sell without the mark describes the condition in which that dependence has been turned entirely against them.
   751	
   752	\begin{thebibliography}{131}
   753	\small
   754	\setlength{\itemsep}{2pt}
   755	\bibitem[{Agarwal}(1997)]{agarwal1997}
   756	Agarwal, Bina. 1997. ``Bargaining'' and Gender Relations: Within and Beyond the Household. \emph{Feminist Economics} 3(1): 1-51. doi:10.1080/135457097338799.
   757	
   758	\bibitem[{Applebaum}(2003)]{applebaum2003}
   759	Applebaum, Anne. 2003. \emph{Gulag: A History}. Doubleday.
   760	
   761	\bibitem[{Azar et~al.}(2022)]{azar2022}
   762	Azar, Jos\'e, Ioana Marinescu, and Marshall Steinbaum. 2022. Labor Market Concentration. \emph{Journal of Human Resources} 57(S): S167-S199. doi:10.3368/jhr.monopsony.1218-9914R1.
   763	
   764	\bibitem[{Baer}(1970)]{baer1970}
   765	Baer, Gabriel. 1970. The Administrative, Economic and Social Functions of Turkish Guilds. \emph{International Journal of Middle East Studies} 1(1): 28-50. doi:10.1017/s0020743800023898.
   766	
   767	\bibitem[{Barkey}(2008)]{barkey2008}
   768	Barkey, Karen. 2008. \emph{Empire of Difference: The Ottomans in Comparative Perspective}. Cambridge University Press. doi:10.1017/cbo9780511790645.
   769	
   770	\bibitem[{Bates and Lien}(1985)]{bates1985}
   771	Bates, Robert H. and Da-Hsiang Donald Lien. 1985. A Note on Taxation, Development, and Representative Government. \emph{Politics \& Society} 14(1): 53-70. doi:10.1177/003232928501400102.
   772	
   773	\bibitem[{Bauckham}(1991)]{bauckham1991}
   774	Bauckham, Richard. 1991. The Economic Critique of Rome in Revelation 18. In \emph{Images of Empire}, ed. Loveday Alexander, JSOT Press (JSOTSup 122), pp. 47-90.
   775	
   776	\bibitem[{Bauckham}(1993)]{bauckham1993}
   777	Bauckham, Richard. 1993. \emph{The Theology of the Book of Revelation}. Cambridge University Press. doi:10.1017/cbo9780511819858.
   778	
   779	\bibitem[{Bayat}(1987)]{bayat1987}
   780	Bayat, Assef. 1987. \emph{Workers and Revolution in Iran: A Third World Experience of Workers' Control}. Zed Books.
   781	
   782	\bibitem[{Bayat}(1997)]{bayat1997}
   783	Bayat, Asef. 1997. \emph{Street Politics: Poor People's Movements in Iran}. Columbia University Press.
   784	
   785	\bibitem[{Beale}(1999)]{beale1999}
   786	Beale, G. K. 1999. \emph{The Book of Revelation: A Commentary on the Greek Text}. Eerdmans (NIGTC).
   787	
   788	\bibitem[{Beblawi and Luciani}(1987)]{beblawiluciani1987}
   789	Beblawi, Hazem and Giacomo Luciani (eds.). 1987. \emph{The Rentier State}. Croom Helm. doi:10.4324/9781315684864.
   790	
   791	\bibitem[{Beik}(1985)]{beik1985}
   792	Beik, William. 1985. \emph{Absolutism and Society in Seventeenth-Century France: State Power and Provincial Aristocracy in Languedoc}. Cambridge University Press. doi:10.1017/cbo9780511583797.
   793	
   794	\bibitem[{Besley and Persson}(2011)]{besley2011}
   795	Besley, Timothy and Torsten Persson. 2011. \emph{Pillars of Prosperity: The Political Economics of Development Clusters}. Princeton University Press. doi:10.23943/princeton/9780691152684.001.0001.
   796	
   797	\bibitem[{Besley and Persson}(2013)]{besley2013}
   798	Besley, Timothy and Torsten Persson. 2013. Taxation and Development. In \emph{Handbook of Public Economics}, vol. 5, Elsevier, pp. 51-110. doi:10.1016/B978-0-444-53759-1.00002-9.
   799	
   800	\bibitem[{Boehm}(1999)]{boehm1999}
   801	Boehm, Christopher. 1999. \emph{Hierarchy in the Forest: The Evolution of Egalitarian Behavior}. Harvard University Press. doi:10.2307/j.ctvjf9xr4.
   802	
   803	\bibitem[{Boyer}(1992)]{boyer1992}
   804	Boyer, Paul. 1992. \emph{When Time Shall Be No More: Prophecy Belief in Modern American Culture}. Harvard University Press (Belknap). doi:10.2307/jj.41480279.
   805	
   806	\bibitem[{Brenner}(1976)]{brenner1976}
   807	Brenner, Robert. 1976. Agrarian Class Structure and Economic Development in Pre-Industrial Europe. \emph{Past \& Present} 70: 30-75. doi:10.1093/past/70.1.30.
   808	
   809	\bibitem[{Campbell}(1993)]{campbell1993}
   810	Campbell, John L. 1993. The State and Fiscal Sociology. \emph{Annual Review of Sociology} 19: 163-185. doi:10.1146/annurev.so.19.080193.001115.
   811	
   812	\bibitem[{Chaudhry}(1997)]{chaudhry1997}
   813	Chaudhry, Kiren Aziz. 1997. \emph{The Price of Wealth: Economies and Institutions in the Middle East}. Cornell University Press. doi:10.7591/9781501700347.
   814	
   815	\bibitem[{Cheng and Selden}(1994)]{cheng1994}
   816	Cheng, Tiejun and Mark Selden. 1994. The Origins and Social Consequences of China's Hukou System. \emph{The China Quarterly} 139: 644-668. doi:10.1017/S0305741000043083.
   817	
   818	\bibitem[{Chenoweth and Stephan}(2011)]{chenoweth2011}
   819	Chenoweth, Erica and Maria J. Stephan. 2011. \emph{Why Civil Resistance Works: The Strategic Logic of Nonviolent Conflict}. Columbia University Press.
   820	
   821	\bibitem[{Clastres}(1987)]{clastres1987}
   822	Clastres, Pierre. 1987. \emph{Society against the State: Essays in Political Anthropology (1974), trans. Robert Hurley}. Zone Books. doi:10.2307/j.ctv1595m3p.
   823	
   824	\bibitem[{Cohen}(1978)]{cohen1978}
   825	Cohen, G. A. 1978. \emph{Karl Marx's Theory of History: A Defence}. Princeton University Press. doi:10.1515/9780691213002.
   826	
   827	\bibitem[{Collins}(1984)]{collins1984}
   828	Collins, Adela Yarbro. 1984. \emph{Crisis and Catharsis: The Power of the Apocalypse}. Westminster Press.
   829	
   830	\bibitem[{Constable}(1964)]{constable1964}
   831	Constable, Giles. 1964. \emph{Monastic Tithes from Their Origins to the Twelfth Century}. Cambridge University Press.
   832	
   833	\bibitem[{Cox et~al.}(2010)]{cox2010}
   834	Cox, Michael, Gwen Arnold, and Sergio Villamayor Tomas. 2010. A Review of Design Principles for Community-based Natural Resource Management. \emph{Ecology and Society} 15(4): 38.
   835	
   836	\bibitem[{Craig and Pencavel}(1993)]{craig1993}
   837	Craig, Ben and John Pencavel. 1993. The Objectives of Worker Cooperatives. \emph{Journal of Comparative Economics} 17(2): 288-308. doi:10.1006/jcec.1993.1027.
   838	
   839	\bibitem[{Davies and Wheatcroft}(2004)]{davies2004}
   840	Davies, R. W. and Stephen G. Wheatcroft. 2004. \emph{The Years of Hunger: Soviet Agriculture, 1931-1933}. Palgrave Macmillan.
   841	
   842	\bibitem[{Dell}(2010)]{dell2010}
   843	Dell, Melissa. 2010. The Persistent Effects of Peru's Mining Mita. \emph{Econometrica} 78(6): 1863-1903. doi:10.3982/ECTA8121.
   844	
   845	\bibitem[{Domar}(1970)]{domar1970}
   846	Domar, Evsey D. 1970. The Causes of Slavery or Serfdom: A Hypothesis. \emph{The Journal of Economic History} 30(1): 18-32. doi:10.1017/S0022050700078566.
   847	
   848	\bibitem[{Dow}(2003)]{dow2003}
   849	Dow, Gregory K. 2003. \emph{Governing the Firm: Workers' Control in Theory and Practice}. Cambridge University Press. doi:10.1017/CBO9780511615849.
   850	
   851	\bibitem[{Drelichman and Voth}(2014)]{drelichman2014}
   852	Drelichman, Mauricio and Hans-Joachim Voth. 2014. \emph{Lending to the Borrower from Hell: Debt, Taxes, and Default in the Age of Philip II}. Princeton University Press.
   853	
   854	\bibitem[{Ekelund et~al.}(1996)]{ekelund1996}
   855	Ekelund, Robert B., Robert F. Hebert, Robert D. Tollison, Gary M. Anderson, and Audrey B. Davidson. 1996. \emph{Sacred Trust: The Medieval Church as an Economic Firm}. Oxford University Press.
   856	
   857	\bibitem[{Elster}(1983)]{elster1983}
   858	Elster, Jon. 1983. \emph{Explaining Technical Change: A Case Study in the Philosophy of Science}. Cambridge University Press.
   859	
   860	\bibitem[{Elster}(1985)]{elster1985}
   861	Elster, Jon. 1985. \emph{Making Sense of Marx}. Cambridge University Press.
   862	
   863	\bibitem[{Esping-Andersen}(1985)]{esping1985}
   864	Esping-Andersen, G\"osta. 1985. \emph{Politics against Markets: The Social Democratic Road to Power}. Princeton University Press. doi:10.1515/9781400886203.
   865	

exec
/usr/local/bin/zsh -lc "sed -n '130,420p' papers/latex/productive-power.tex | nl -ba -v130" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   130	Wage labor & Yes, subject to notice and contract & Contract, under law & No & The worker keeps the wage \\
   131	Taxation & Yes, subject to emigration rules & Law, enforced by sanction & No & The taxpayer keeps income after tax \\
   132	Serfdom & No, the producer is tied to land or lord & Custom and law, enforced by the lord and the state & No, though some regimes allowed sale with or without land & The household keeps output after dues and labor service \\
   133	Compelled state labor & No, for the term of the draft or sentence & Sanction by the state & No & Little or nothing during the term \\
   134	Chattel slavery & No & Ownership, enforced by the state & Yes & The owner \\
   135	\bottomrule
   136	\end{tabularx}
   137	\end{table}
   138	
   139	Hirschman's distinction between exit and voice is the standard vocabulary for the options of members facing a declining organization \citep{hirschman1970}. Largo adopts it for the productive function \citep{largo2026hbs}, and this Part owns its use in the series.
   140	
   141	\begin{definition}[Exit, voice and loyalty in the productive layer]
   142	\label{def:productive-power:evl}
   143	A producer's \emph{outside option} $o$ is the per-period value available if the producer stops participating on the current terms: another employer, free land, migration, a subsistence plot, or a cooperative. \emph{Exit} is the exercise of that option. \emph{Voice} is collective or individual action to change the terms without leaving (petitions, lawsuits, strikes, tax refusal, boycotts, votes); its effectiveness in the model is the \emph{organized bargaining weight} $\eta\in[0,1]$, with $\eta=0$ for atomized producers. \emph{Loyalty} is attachment that raises the threshold at which a producer exits, which can make voice possible by keeping members inside long enough to use it \citep{hirschman1970}.
   144	\end{definition}
   145	
   146	\begin{definition}[Productive contestability]
   147	\label{def:productive-power:qw}
   148	The contestability of the productive pillar, $\QW_t:=Q_{\pW,t}$, is a preregistered aggregate of five components in $[0,1]$: bargaining coverage $q^{\mathrm{bar}}$ (the share of producers whose terms are set or reviewed collectively), mobility $q^{\mathrm{mob}}$ (lawful and practical ability to change employer, residence or occupation, including portability of benefits), legal access $q^{\mathrm{leg}}$ (access to independent adjudication of disputes over terms), income protection $q^{\mathrm{inc}}$ (replacement of income during unemployment, illness and old age), and voice $q^{\mathrm{voi}}$ (lawful ability to organize, strike, petition and vote over the terms of taxation).
   149	\end{definition}
   150	
   151	The five components follow Largo's list for the productive function: bargaining, legal protection, mobility, representation and income protection \citep{largo2026hbs}. They are separate because they fail separately. A worker can have the vote and no union, a union and no portable pension, or a labor court and no means to reach it. Legal access belongs to the judicial pillar as well. Part III \citep{long2026judicial} owns the analysis of legal mobilization (its Proposition 6.4) and the components of judicial contestability (its Definition 2.4): disclosure of a defective decision, access to a challenge, independence of the reviewing forum, and compliance with its ruling.
   152	
   153	The concentration $H_{\pW,t}$ is computed on shares of decision-relevant control over the terms of productive participation. In a labor market the natural proxy is the employment or vacancy share of each employer, which is how \citet{azar2022} measure labor-market concentration. Where the state is the dominant employer or the sole purchaser of farm output, its share approaches one. Where every household controls its own labor and land is open, shares are close to $1/n_h$ for $n_h$ households.
   154	
   155	\subsection{The production game}
   156	
   157	The mechanisms of Section~\ref{sec:mechanisms} and the comparisons of Section~\ref{sec:comparison} use one stationary model, defined here and analyzed in Section~\ref{sec:mechanisms}.
   158	
   159	\begin{definition}[Production game]
   160	\label{def:productive-power:game}
   161	In each period a coalition $S$ governs $n$ identical producers. A participating producer produces $y>0$. The coalition and the producers agree on terms $u$, the per-producer value the producer retains (consumption plus the money value of services and concessions received); the extraction share is $\chi=1-u/y$, which is negative when producers receive net transfers. The coalition's revenue is $n(y-u)+R$, where $R\ge 0$ is non-producer revenue, and it must meet the institutional maintenance requirement $K>0$ of Definition~\ref{def:productive-power:persistence}. Producers' own subsistence is covered by $u$, so $K$ contains only the cost of the institutions. A producer who does not participate obtains the outside option $o$, with $y_0\le o\le y$, where $y_0$ is the autarky value of a producer cut off from exchange.
   162	\end{definition}
   163	
   164	The coalition objective of \citet{largo2026hbs}, $\Pi=B(p)+\rho(c)-\kappa(g)-\phi(\cdot)$, is the general form of which the coalition's payoff here is a special case. The net revenue $n(y-u)$ is a component of the material benefit $B$, and the mobility restriction $g$ defined next is an instance of the source's coercive measures with cost $\kappa(g)$.
   165	
   166	\begin{definition}[Instruments on the outside option]
   167	\label{def:productive-power:gate}
   168	A \emph{mobility restriction} $g\in[0,1]$ is the probability that a producer who tries to leave is prevented: tying peasants to land, internal passports, residence permits tied to an employer. A \emph{participation gate} $\gamma\in[0,1]$ is the probability that a producer who withholds allegiance from the coalition retains access to exchange (buying inputs, selling output, credit, being hired); otherwise the producer falls to the autarky value $y_0$. Employment shares $s_j=s^{\pW}_j$ of employers $j=1,\dots,J$ define the concentration $\HW=\sum_j s_j^2$.
   169	\end{definition}
   170	
   171	\begin{definition}[Composite outside option]
   172	\label{def:productive-power:outside}
   173	Let $o_1>y_0$ be the value of an offer from a competing employer. The outside option of a producer at employer $j$ is
   174	\[
   175	o_j=y_0+\gamma\,(1-g)\,(1-s_j)\,(o_1-y_0),
   176	\]
   177	and the employment-weighted mean outside option is $\bar o=\sum_j s_jo_j=y_0+\gamma(1-g)(1-\HW)(o_1-y_0)$.
   178	\end{definition}
   179	
   180	Each factor of the composite form is a probability that the producer's exit succeeds: the producer is not blocked from leaving ($1-g$), keeps access to exchange ($\gamma$), and finds a different employer ($1-s_j$, justified in Lemma~\ref{lem:productive-power:concentration}). When an exit fails the producer receives the fallback $y_0$. Unrestricted producers facing many small employers obtain nearly $o_1$; a closed gate, a complete restriction or a single employer each holds them at $y_0$.
   181	
   182	\section{Necessity of the pillar}
   183	\label{sec:necessity}
   184	
   185	\subsection{The maintenance axiom}
   186	
   187	Part VII owns the axiom set from which the series derives Proposition A. The sixth axiom concerns this pillar.
   188	
   189	\begin{assumption}[Ax6, maintenance]
   190	\label{ass:productive-power:ax6}
   191	There are constants $k\ge k_S>0$ with $K^{\mathrm{tot}}_t\ge k$ and $K_t\ge k_S$ for every $t$: the group and its institutions consume resources in every period. The initial stocks $X_0$ and $X^S_0$ are finite.
   192	\end{assumption}
   193	
   194	The axiom is empirical, not logical. A population that consumed nothing would not need production, and the derivation below would fail for it. No human collective satisfies that description, since members eat and institutions occupy time that could otherwise produce food. The finite initial stock excludes inexhaustible inheritances.
   195	
   196	\begin{assumption}[No manna]
   197	\label{ass:productive-power:nomanna}
   198	Inflows are produced: $Y_t>0$ only if some agent, inside or outside the collective, performs productive activity in period $t$ or owns, operates or maintains equipment that does.
   199	\end{assumption}
   200	
   201	The no-manna assumption converts the accounting identity of Definition~\ref{def:productive-power:persistence} into a claim about activity. Wild foods require gathering, oil requires extraction, and a gift requires a giver who produced or acquired what is given. The assumption fails only for resources that arrive with no human act at any point in the chain, and the scarcity axiom of the series (Ax1, which states that resources are finite and that claims on them conflict) makes any such free stock finite.
   202	
   203	\subsection{Necessity and relocation}
   204	
   205	\begin{lemma}[Necessity of the maintenance function]
   206	\label{thm:productive-power:necessity}
   207	Under Assumptions~\ref{ass:productive-power:ax6} and~\ref{ass:productive-power:nomanna}, if a collective persists indefinitely then for every $T\ge 1$
   208	\[
   209	\frac{1}{T}\sum_{t=0}^{T-1}Y_t\;\ge\;k-\frac{X_0}{T},
   210	\]
   211	so the long-run average inflow is at least $k>0$, and productive activity occurs in infinitely many periods.
   212	\end{lemma}
   213	
   214	\begin{proof}
   215	Iterating the stock equation gives $X_T=X_0+\sum_{t<T}(Y_t-K^{\mathrm{tot}}_t)$. Persistence requires $X_T\ge 0$, hence $\sum_{t<T}Y_t\ge\sum_{t<T}K^{\mathrm{tot}}_t-X_0\ge Tk-X_0$. Dividing by $T$ gives the displayed bound, and its right side tends to $k$ as $T\to\infty$. If productive activity occurred in only finitely many periods, Assumption~\ref{ass:productive-power:nomanna} would make $Y_t=0$ from some period on, so $\sum_{t<T}Y_t$ would be bounded while $Tk-X_0$ grows without bound, a contradiction.
   216	\end{proof}
   217	
   218	The lemma establishes the existence of the activity, not of any institution that organizes it. Wage labor, serfdom, the household farm, the kolkhoz and the cooperative are alternative ways of implementing the same function. This is the distinction \citet{hempel1959} required of functional analysis: a functional requirement does not entail any particular institution, because functional equivalents may satisfy it. Nor does the lemma explain why a given regime has the productive institutions it has. \citet{elster1983} showed that explanation by beneficial consequences needs a feedback mechanism from the effect to the trait. The lemma is a condition of persistence, and it makes no causal claim about the origin of institutions.
   219	
   220	A collective can persist while its own members produce little or nothing. The next lemma shows what such persistence requires.
   221	
   222	\begin{lemma}[Relocation]
   223	\label{lem:productive-power:relocation}
   224	Split the inflow as $Y_t=Y^{\mathrm{in}}_t+Y^{\mathrm{out}}_t$, where $Y^{\mathrm{in}}_t$ is produced by members and $Y^{\mathrm{out}}_t$ by non-members and transferred to the collective. Under Assumptions~\ref{ass:productive-power:ax6} and~\ref{ass:productive-power:nomanna}, if a collective persists indefinitely and $Y^{\mathrm{in}}_t=0$ for all $t\ge t_0$, then non-members produce for the collective in infinitely many periods, and for every $T>t_0$ the transferred output satisfies $\sum_{t_0\le t<T}Y^{\mathrm{out}}_t\ge (T-t_0)k-X_{t_0}$.
   225	\end{lemma}
   226	
   227	\begin{proof}
   228	Apply Lemma~\ref{thm:productive-power:necessity} to the collective from period $t_0$ with initial stock $X_{t_0}$, which is finite because each $X_t$ is finite. From $t_0$ on, $Y_t=Y^{\mathrm{out}}_t$, so the bound becomes the displayed inequality, and productive activity by non-members occurs in infinitely many periods.
   229	\end{proof}
   230	
   231	The transfer in Lemma~\ref{lem:productive-power:relocation} is an edge of the productive layer between the collective and producers outside its membership. It can take the form of tribute extracted by force, rents paid by foreign buyers for oil extracted by migrant workers, alms and endowments given to a religious community, or foreign aid financed by taxpayers elsewhere. Each moves the producers out of the membership and usually out of the polity's channels of voice. None removes them.
   232	
   233	Automation is the hardest version of the relocation argument. If equipment performs all productive activity, Definition~\ref{def:productive-power:surplus} still assigns the producer role to whoever owns, operates or maintains the equipment. Control over the productive layer then coincides with ownership of equipment, a relation that also belongs to $\pF$, and $\HW$ tracks the concentration of that ownership. The function survives full automation. The bargaining power of human labor, analyzed below, does not survive it automatically: it depends on human activity remaining necessary somewhere in the chain. That dependence is an empirical condition of present technology, not a consequence of the axiom, and the paper's claims about labor are narrowed accordingly.
   234	
   235	The producers must themselves be produced. A collective that persists beyond the working lives of its present members depends on the care and child-rearing that \citet{laslett1989} call social reproduction, most of it unpaid. The next lemma states the dependence.
   236	
   237	\begin{lemma}[Reproduction]
   238	\label{lem:productive-power:reproduction}
   239	Let the number of producers evolve as $n_{t+1}=(1-d)n_t+bh_t+m_t$, where $d\in(0,1]$ is the rate at which producers leave work through death, age or illness, $h_t\ge 0$ is care labor performed in period $t$, $b>0$ is the number of future producers sustained per unit of care, and $m_t\ge 0$ is the net arrival of producers raised elsewhere. If $h_t=m_t=0$ for all $t\ge t_0$, then $n_{t_0+j}=(1-d)^jn_{t_0}$, and members' output $n_ty$ falls below any fixed $k>0$ after finitely many periods. A collective that persists indefinitely on members' production therefore requires care labor, or the arrival of producers raised elsewhere, in infinitely many periods.
   240	\end{lemma}
   241	
   242	\begin{proof}
   243	With $h_t=m_t=0$ the recursion is $n_{t+1}=(1-d)n_t$, whose solution is $(1-d)^jn_{t_0}$; this tends to zero because $0\le 1-d<1$, so $n_ty<k$ for all large $t$. If care and arrivals were zero from some period on, members' production would fall below $k$ from some period on, and Lemma~\ref{thm:productive-power:necessity} would require inflows produced by non-members, contradicting persistence on members' production.
   244	\end{proof}
   245	
   246	The lemma puts unpaid household work inside the maintenance function on the same footing as paid work. It also shows a second form of relocation. A labor regime that imports adult migrants ($m_t>0$) draws on care performed in the migrants' places of origin, so the cost of reproducing its producers is borne outside the polity, as the cost of producing its rents is in Lemma~\ref{lem:productive-power:relocation}.
   247	
   248	\subsection{The latent veto}
   249	
   250	Dependence on production runs in both directions. Producers depend on land, tools, employers, buyers and protection. The coalition that governs depends on the flow that producers generate. The next proposition states the second dependence as a bound.
   251	
   252	\begin{proposition}[Latent veto]
   253	\label{prop:productive-power:latent-veto}
   254	Suppose Assumption~\ref{ass:productive-power:ax6} holds, the institutions' non-producer revenue satisfies $R_t\le\bar r$ for all $t$ with $\bar r<k_S$, and from period $t_0$ on the producers withdraw completely, so that their transfers are $T_t=0$. Then the institutions fail to persist no later than period $t_0+\lfloor X^S_{t_0}/(k_S-\bar r)\rfloor+1$.
   255	\end{proposition}
   256	
   257	\begin{proof}
   258	For $t\ge t_0$ the institutional stock of Definition~\ref{def:productive-power:persistence} satisfies $X^S_{t+1}=X^S_t+R_t-K_t\le X^S_t-(k_S-\bar r)$. After $j$ periods of withdrawal, $X^S_{t_0+j}\le X^S_{t_0}-j(k_S-\bar r)$, which is negative for the smallest integer $j$ exceeding $X^S_{t_0}/(k_S-\bar r)$, that is, for $j=\lfloor X^S_{t_0}/(k_S-\bar r)\rfloor+1$.
   259	\end{proof}
   260	
   261	The proposition is elementary, and its content lies in what it rules out. No governance system whose non-producer revenue stays below its institutional maintenance requirement can survive the complete and permanent withdrawal of its producers. The producers therefore hold, collectively, a veto over persistence. The veto is latent because exercising it requires coordination that atomized producers lack \citep{olson1965}, because the coalition may meet withdrawal with coercion, and because the producers bear their own costs of withdrawal. Section~\ref{sec:mechanisms} prices these obstacles. When $R_t\ge K_t$ the bound fails, and the veto passes to whoever produces the rents (Lemma~\ref{lem:productive-power:relocation}).
   262	
   263	Largo states the same mutual dependence in prose: the working population is active, dependency is not powerlessness, and concentration elsewhere translates into material dependency only where workers lack bargaining, legal protection, mobility and representation \citep{largo2026hbs}. Proposition~\ref{prop:productive-power:latent-veto} supplies the reason the population is active. It is part of the structure on which everything else rests.
   264	
   265	\subsection{Minimal form in stateless and consensus societies}
   266	
   267	Proposition A predicts that each function exists in societies with no state, no chiefs with coercive power and strong egalitarian norms. For production the prediction is easy to confirm and the interesting question is different: why does production in these societies so rarely support a class that extracts from producers? The formal part of the answer is an exit argument.
   268	
   269	\begin{proposition}[Minimal form]
   270	\label{prop:productive-power:minimal-form}
   271	Consider a band in which every household controls its own labor, any household can leave the camp and obtain the same output $y$ elsewhere on open land, and leaving costs nothing. Then (a) the maintenance function is implemented by the households themselves, and (b) no member or coalition can sustain a positive extraction share $\chi>0$ from any household that is free to leave.
   272	\end{proposition}
   273	
   274	\begin{proof}
   275	Part (a) is Lemma~\ref{thm:productive-power:necessity} applied to the band, with producers identified as household members. For (b), a household asked to surrender $\chi y>0$ obtains $(1-\chi)y$ by staying and $y$ by leaving, so leaving is strictly better. A demand for $\chi>0$ is therefore not met by any household that is free to leave.
   276	\end{proof}
   277	
   278	The ethnography supplies the premises and shows where they fail. Table~\ref{tab:hardcases} summarizes the cases the series uses.
   279	
   280	\begin{table}[t]
   281	\centering
   282	\small
   283	\caption{Minimal form of the productive function in the hard cases. The right column records the strongest reading on which the function, or its accountability, might be absent.}
   284	\label{tab:hardcases}
   285	\begin{tabularx}{\textwidth}{@{}L{2.5cm}YY@{}}
   286	\toprule
   287	Case & Who produces and on what terms & Strongest counter-reading and reply \\
   288	\midrule
   289	Ju/'hoansi \citep{lee1979,marshall1976} & Men and women forage, sharing rules distribute meat, and gift exchange links camps & No one commands labor. Reply: production is universal and its terms are policed by leveling talk \citep{wiessner2005} \\
   290	Immediate-return foragers \citep{woodburn1982} & Food is consumed soon after it is obtained and accumulation is discouraged & Egalitarianism looks like the absence of power. Reply: it is produced by institutions of leveling \\
   291	Nuer \citep{evanspritchard1940} & Herding, horticulture and fishing are organized by households and kin & Evans-Pritchard stressed the absence of government. Reply: cattle rights and exchange organize production without an office \\
   292	Amazonian chiefs \citep{clastres1987} & Households garden and hunt, and the chief must give and work more & The flow runs from chief to group. Reply: this is a negative extraction share, not an absent function \\
   293	Upland Southeast Asia \citep{scott2009} & Swidden farmers choose crops that are hard to tax & Producers evade the state. Reply: they produce and govern their own terms \\
   294	Commons \citep{ostrom1990} & Users provide labor to maintain irrigation and other common resources & No state allocates labor. Reply: provision rules assign maintenance labor and are monitored \\
   295	\bottomrule
   296	\end{tabularx}
   297	\end{table}
   298	
   299	Among the Ju/'hoansi, production by both sexes is the basis of daily life, and the terms on which its results circulate are governed by sharing rules, gift partnerships and talk \citep{lee1979,lee2013,marshall1976}. \citet{wiessner2005} documented how the Ju/'hoansi enforce such norms, largely through criticism and talk rather than physical punishment. In the vocabulary of this paper, open access and costless fission keep $o$ close to $y$, and leveling sanctions keep it there. \citet{woodburn1982} generalized the point: in immediate-return societies equality is an achievement of institutions that prevent accumulation, not a default. \citet{boehm1999} called the same pattern a reverse dominance hierarchy, in which the group as a coalition dominates would-be dominants.
   300	
   301	Clastres's Amazonian chiefs are the most striking case for this pillar. The chief has no power to command, is expected to be generous, and works harder than others to supply what he gives away \citep{clastres1987}. In the model's terms, the leader's extraction share is negative. Clastres read this as a society actively preventing power from separating from it. That reading supports the distinction between Propositions A and B. The productive function is present, and its capture is prevented.
   302	
   303	Ostrom's commons supply the cleanest institutional image of the maintenance function at small scale. Her design principles require congruence between appropriation rules and provision rules, so that those who draw on an irrigation system or a fishery also contribute the labor that maintains it, under monitoring by the users themselves \citep{ostrom1990,ostromdesign2010}. A review of later studies found broad, though not uniform, support for the principles \citep{cox2010}. Provision rules are the productive pillar in miniature.
   304	
   305	The ethnographic record has limits that bear on the claim. Contact-era ethnographies describe groups living in marginal environments, often already in contact with states and markets, and foraging societies vary widely \citep{kelly1995}. Sahlins's argument that hunter-gatherers met their needs with modest labor \citep{sahlins1972} corrects any picture of constant struggle, but it does not remove production; it lowers its hours. The minimal-form proposition needs only that someone produces and that, where exit is open and costless, no one can take a share.
   306	
   307	\subsection{Counterexample attempts}
   308	
   309	The falsifier of Lemma~\ref{thm:productive-power:necessity} is a governance system that persists indefinitely while supported by no production and no replenishment of its stock. Six candidates come close and fail.
   310	
   311	A community living from an endowment consumes a finite stock unless the endowment earns a return, and a return is someone's production. Monasteries and mendicant orders that live by alms relocate production to donors. A raiding or tributary state relocates it to the raided and the tributary, as Lemma~\ref{lem:productive-power:relocation} predicts; the Spanish colonial labor draft discussed in Section~\ref{sec:comparison} is a documented instance in which the producers were outside the ruling community and inside its coercive reach \citep{dell2010}. A rentier state relocates production to the workers who extract the resource and the foreign buyers who pay for it; in the Gulf monarchies much of the extracting and building labor is done by migrants without citizenship \citep{hanieh2011,kapiszewski2001}. Full automation, as argued above, relocates the producer role to owners and maintainers of equipment. The original affluent society lowers labor hours without eliminating them \citep{sahlins1972}.
   312	
   313	The strongest attempt is the last of these taken to its limit: a society of self-maintaining machines serving a population that does nothing. The function would then be performed by equipment owned by someone, and the claim survives in its functional form. What would not survive is any claim that human labor holds a latent veto. The paper's claims about producer power are therefore conditional on human activity remaining necessary in production. That narrowing is the honest result of the counterexample.
   314	
   315	\section{Literature}
   316	\label{sec:literature}
   317	
   318	Four bodies of work bear on the productive pillar, and they rarely cite one another. Each answers part of the guiding question, and each leaves a gap that the framework of this series is meant to fill.
   319	
   320	The first asks who creates value and how it is divided. For \citet{marx1976}, labor applied to means of production owned by others yields a surplus appropriated as profit, and the compulsion that keeps wage workers at work is economic rather than legal. Polanyi's account of the nineteenth-century market society adds that labor, land and money are fictitious commodities, not produced for sale, and that treating them as commodities provoked a protective countermovement \citep{polanyi1944}. Both accounts locate power in production, but neither supplies a comparative instrument that applies equally to market and command economies. Recent distributional accounting measures who receives national income without asking how the terms were bargained \citep{piketty2018}. Work on social reproduction widens the category of producers to include unpaid household labor \citep{laslett1989}.
   321	
   322	The second body of work locates producers' power in their options and their organization. Hirschman's exit, voice and loyalty frame the options of members of any organization in decline \citep{hirschman1970}. \citet{freeman1984} applied the frame to trade unions, which have a monopoly face that raises wages and a collective-voice face that lets workers change conditions without quitting. \citet{wright2000} distinguished associational power, which comes from organization in unions and parties, from structural power, which comes from workers' position in tight labor markets or strategic sectors. \citet{silver2003} used the distinction to trace labor unrest across a century of relocating industries.
   323	
   324	Power resources theory explains welfare-state variation by the organization of wage earners and their parties \citep{korpi1983,esping1985}. The employer side of the same relation is monopsony: when workers cannot move costlessly between employers, firms set wages below the competitive level \citep{manning2003}, and local labor markets are often concentrated enough for this to matter \citep{azar2022}. These studies measure producer power well within capitalist democracies and say little about serfs, kolkhoz members or migrant workers under sponsorship.
   325	
   326	The third body of work is fiscal sociology, which treats the tax relation as the core of state formation \citep{campbell1993,martin2009}. \citet{levi1988} modeled rulers as revenue maximizers constrained by their bargaining power relative to constituents, by transaction costs and by their discount rates, and showed that compliance is quasi-voluntary: taxpayers comply when they believe others do and the ruler keeps bargains. \citet{bates1985} argued that owners of mobile assets can extract representative concessions. \citet{ross2004} tested the claim that taxation leads to representation and found that the relevant variable is taxation relative to the services government provides, and \citet{timmons2005} found that governments trade services for revenue with the groups that pay.
   327	
   328	Rentier-state theory supplies the converse: revenue that does not come from domestic taxpayers frees rulers from bargaining with them \citep{mahdavy1970,beblawiluciani1987,ross2001}. The converse is contested. \citet{habermenaldo2011} find no evidence that resource reliance promotes authoritarianism over time within countries. Part I \citep{long2026financial} treats rents (its Section 5) on the allocation side; this Part treats them as a change in producers' bargaining position.
   329	
   330	The fourth body of work explains when producers are bound. \citet{domar1970} proposed that serfdom or slavery arises where land is abundant relative to labor, because free peasants could otherwise leave to farm free land, and that free land, free peasants and non-working landowners cannot coexist. \citet{brenner1976} answered that the outcomes of the late-medieval demographic crisis differed across Europe with the same land-labor ratios, and that the balance of organized class power decided them. \citet{dell2010} showed that the Spanish colonial mining draft in Peru left lower household consumption and worse child health in the districts subject to it, centuries after its abolition. \citet{scott1976,scott1985} showed that peasants who cannot exit or speak openly resist through foot-dragging, evasion and gossip, and that they judge extraction against a subsistence ethic.
   331	
   332	The gap is a common instrument. Labor economics, fiscal sociology, rentier theory and the history of bondage each study one or two of the quantities that set producers' terms, in one or two regime types. The model in Section~\ref{sec:mechanisms} places the outside option, organization, employer concentration, non-producer revenue and conditional access to exchange in one notation that applies to a band, a kolkhoz, a Gulf labor camp and a unionized factory. It does not replace the specialized literatures. It shows where they meet.
   333	
   334	\section{Comparative analysis}
   335	\label{sec:comparison}
   336	
   337	Producers' terms were worst, in every regime type that produced such cases, where concentrated control over production was coupled to coercion and to control of exchange; ideology did not decide where this happened. The evidence comes from asking the same questions of each regime type: who produces and pays, who sets the terms of participation, how concentrated that control is, which other pillars it is coupled to, and which channels of exit and voice remain open.
   338	
   339	Two conventions govern the comparison. Where market-capitalist and secular-democratic institutions coexist in one country, the first type is read through the organization of the economy (private capital, labor markets, the structural power of business) and the second through the political organization of the fiscal relation (citizen taxpayers, universal suffrage, social insurance law). Judgments of concentration are qualitative, because no country has been coded under a preregistered scheme, and no value of $U_t$ or $\Integ_t$ is reported.
   340	
   341	\subsection{Market-capitalist societies}
   342	
   343	In market-capitalist societies most producers are wage earners, the self-employed and small businesses, and the terms of production are set mainly by employers in labor markets and by the state through tax and labor law. Consumers sustain enterprises by their purchases and pay a large share of indirect taxes. The holders of the pillar are therefore many, but control over terms is not evenly spread. \citet{azar2022} found that a large share of local labor markets in the United States are highly concentrated by the standard used in antitrust, and that concentration is associated with lower posted wages. Monopsony theory explains why: when moving between employers is costly, employers set wages below the competitive level \citep{manning2003}. In the notation of this paper, $\HW$ varies across local markets and is high in many of them.
   344	
   345	The structural power of business is the distinctive coupling of this regime type. \citet{lindblom1977} argued that because investment decisions are private and governments depend on growth, business holds a privileged position that requires no organization: governments anticipate the reaction of investors. \citet{przeworski1985} drew the consequence for labor parties, which must sustain profits to sustain employment. This is the exit option of mobile capital, and \citet{bates1985} predicted that the owners of mobile assets obtain concessions. The coupling $C_{\pF\pW}$ is high wherever those who allocate capital also set the terms of employment. Part I gives the primary treatment of that pair in its Section 5.
   346	
   347	Accountability in the pillar has rested on three channels: collective bargaining, labor mobility and the vote. Their strength has varied over time. \citet{farber2021} assembled survey data across the twentieth century and found that unions compressed the income distribution when they were strong. \citet{western2011} attributed a substantial part of the rise in American wage inequality after the 1970s to the decline of unions, including through the erosion of norms of fair pay in non-union firms. \citet{piketty2018} documented the same period's shift of pre-tax income toward the top of the distribution. These are documented changes in $q^{\mathrm{bar}}$ and $q^{\mathrm{voi}}$, not evidence of capture by themselves. A decline in bargaining coverage can follow from changes in industry composition and trade as well as from employer action and law.
   348	
   349	Documented checks are visible in the same record. Union contracts, minimum-wage laws, antitrust enforcement in labor markets and the expansion of social insurance in the twentieth century all raised producers' terms through voice. \citet{polanyi1944} treated the protective legislation of the nineteenth century as the countermovement of a society defending itself against the commodification of labor. Documented capture is harder to establish than decline. The source's capture-link criterion requires material evidence linking privileged access to an output \citep{largo2026hbs}. Accounts of how organized business reshaped American labor and tax policy from the 1970s \citep{hackerpierson2010} supply candidate links, and they remain contested in the way Part II \citep{long2026political} describes in its Section 5.2 for the wider literature on unequal political responsiveness.
   350	
   351	\subsection{Communist party-states}
   352	
   353	In the Soviet Union after collectivization and in China under the planned economy, the party-state was the dominant employer, the sole legal purchaser of most farm output and the owner of nearly all productive assets. Its share of control over the terms of productive participation approached one, so $\HW$ was near its maximum. The coupling of $\pW$ to the other pillars was also high, because the same apparatus set prices and procurement quotas ($\pF$), wrote labor law ($\pP$), staffed the courts ($\pJ$), ran the official unions and the press ($\pI$), and policed mobility ($\pC$).
   354	
   355	Collectivization is the most fully documented case in which every instrument of Definitions~\ref{def:productive-power:gate} and~\ref{def:productive-power:outside} was used at once: a single purchaser, restricted mobility, and access to exchange conditioned on membership of the collective farm. Peasants resisted it in 1930 by slaughtering livestock, petitioning and open revolt \citep{viola1996}. After collectivization, the kolkhoz delivered grain at state-set prices, and procurement in the years 1931 to 1933 continued in regions where famine was spreading \citep{davies2004}. Mobility was restricted, and peasants adapted with strategies of evasion and survival that \citet{fitzpatrick1994} documented in detail. Forced labor in the Gulag formed a further tier of compelled state labor \citep{applebaum2003}, and economic historians have argued that it was expensive to run and less productive than free labor \citep{gregory2003}. In the terms of Table~\ref{tab:bondage}, collective farmers were tied to the farm for long periods and Gulag prisoners were compelled state laborers. Neither group was chattel property.
   356	
   357	Soviet industrial workers held more power than the formal structure suggests, because labor was scarce. Chronic labor shortage, the soft budget constraint of enterprises \citep{kornai1986,kornai1992} and managers' need to meet plans gave workers an informal bargaining position. Workers in the 1930s used it through high turnover, absenteeism and control over the pace of work, despite harsh labor-discipline laws \citep{filtzer1986}. Even the Stakhanovite campaign of record-setting provoked conflict on the shop floor as well as productivity gains \citep{siegelbaum1988}.
   358	
   359	Chinese workers under the planned economy faced a more complete dependence on the enterprise. Housing, rations and welfare came through the work unit and through personal ties to superiors, which made the unit a site of dependence rather than of bargaining \citep{walder1986}. The household registration system closed the main exit, tying rural people to their place of birth and restricting their access to urban employment and services \citep{cheng1994}.
   360	
   361	The reform era changed the instruments without removing them. Migration from the countryside expanded producers' outside options, and labor protest grew. \citet{lee2007} compared the protests of laid-off state-sector workers in the northeastern rustbelt with those of migrant workers in the southern export zones, who used the courts and labor law as well as street protest. The official union federation remains tied to the party, which limits voice outside party channels \citep{friedman2010}. Documented checks in this regime type are therefore mainly informal: evasion, turnover, petitioning, and the regime's own fear of unrest. That they existed matters for the comparison. Even under the most integrated arrangement in the record, the latent veto of Proposition~\ref{prop:productive-power:latent-veto} operated through everyday resistance.
   362	
   363	\subsection{Social democracy and market socialism}
   364	
   365	In the Nordic social democracies, producers are wage earners and the self-employed in market economies, but their terms are set to an unusual degree by collective bargaining at the national and sectoral level and by universal social insurance. Union density and bargaining coverage have been high by international standards for most of the postwar period. Power resources theory explains the arrangement as the result of the organization of wage earners in unions and their alliance with social democratic parties \citep{korpi1983,esping1985}. \citet{esping1990} measured its consequence as decommodification, the degree to which people can maintain a livelihood without relying on the labor market. \citet{huber2001} traced the development of the welfare state to partisan government over decades.
   366	
   367	The distinctive coupling here is between $\pW$ and $\pP$, through corporatist bargaining in which unions, employers and the state set wages and social policy together. By the source's own standard this coupling is not capture \citep{largo2026hbs}. It is a coalition commanding agenda in two pillars, and in this case its effect was to raise producers' contestability rather than to lower it. Corollary~\ref{cor:productive-power:coupling} formalizes the asymmetry: capture requires instruments that lower producers' terms, and corporatist coupling has mainly strengthened voice. Universalism also has a fiscal logic. \citet{korpi1998} found that universal programs redistribute more than targeted ones, because they build coalitions of support that enlarge the budget. \citet{rothstein1996} showed how the Swedish administrative model made universal programs implementable.
   368	
   369	The limits of the model are documented as well. \citet{przeworski1985} argued that social democratic parties remain structurally dependent on private investment, and \citet{pontusson1992} traced the failure of Swedish wage-earner funds, the most ambitious attempt to transfer ownership to labor. \citet{rueda2005} argued that social democratic parties have incentives to protect labor-market insiders rather than outsiders in temporary or precarious employment. That cleavage is a candidate failure mode inside the pillar: high $\QW$ for insiders can coexist with low $\QW$ for outsiders.
   370	
   371	Market socialism and workers' self-management are the variants of this regime type in which producers formally own the enterprise. \citet{kornai1992} argued that reform socialism in Hungary and Yugoslavia retained soft budget constraints and party control of appointments, which limited the autonomy of self-managed firms. Worker cooperatives in market economies are the small-scale analogue. \citet{dow2003} surveyed the theory and evidence on labor-managed firms, and \citet{craig1993} studied the objectives of worker cooperatives in the plywood industry of the Pacific Northwest. In the model, a cooperative raises producers' outside option, since it is an employer that the producers themselves control, and it removes extraction within the firm while leaving taxation to the state.
   372	
   373	\subsection{Islamic states}
   374	
   375	Islamic states share a source of political legitimacy, the claim to govern according to religious law, and differ in nearly every other respect. The comparison here covers the Ottoman Empire, modern Iran and Saudi Arabia, and the productive arrangements in each are not derived from Islamic law alone. Some instruments are legal categories of the tradition, such as alms taxes and land taxes. Others, such as tax farming or migrant sponsorship, are fiscal and labor-market institutions that belong to particular states and periods.
   376	
   377	In the Ottoman Empire, organized crafts gave producers a channel of voice. The taxpaying subjects were mainly peasants, artisans and merchants, and urban crafts were organized in guilds that regulated entry, prices and quality while also serving the state as administrative and fiscal intermediaries \citep{baer1970}. The guild was thus a site of coupling between $\pW$ and $\pP$: guilds petitioned authorities and brought disputes to the courts. Studies of Ottoman and early Republican workers document strikes and labor organization in the nineteenth and early twentieth centuries \citep{quataert1995}.
   378	
   379	Control over Ottoman producers' terms was dispersed among intermediaries. \citet{karaman2010} compared Ottoman state finances with those of European states and found that Ottoman revenue per capita remained low and collection decentralized, with heavy reliance on tax farming. \citet{barkey2008} described Ottoman rule as brokerage with intermediaries rather than direct command. In the vocabulary of this paper, control over the terms of production was dispersed among intermediaries, so $\HW$ was moderate. Ibn Khaldun had already observed that dynasties begin with low tax rates that yield large revenues and end with high rates that yield little, as producers withdraw effort \citep{khaldun1958}. The observation states the latent veto in fourteenth-century terms.
   380	
   381	Islamic legal categories of taxation and charity, including the alms tax and endowments, shaped the fiscal relation and the provision of welfare. \citet{singer2008} surveyed charity in Islamic societies, including endowed public kitchens in the Ottoman Empire. The economic consequences of Islamic commercial law are debated. \citet{kuran2011} argued that rules of partnership, inheritance and endowment held back the formation of durable private enterprises in the Middle East; \citet{rubin2017} attributed divergence instead to the way rulers relied on religious authorities for legitimacy, and \citet{pamuk2000} offered a monetary and fiscal history that does not reduce Ottoman outcomes to law.
   382	
   383	Modern Iran shows producers' power at both extremes. Oil workers' strikes were central to the revolution of 1978 to 1979, and workers' councils briefly took over the management of factories before the new regime absorbed or suppressed them \citep{bayat1987}. In the following decades the urban poor pursued what \citet{bayat1997} called the quiet encroachment of the ordinary: unorganized, cumulative claims on land, services and public space. \citet{mahdavy1970} coined the concept of the rentier state using the Iranian case: oil revenue reduces the state's need to tax, and with it the bargaining weight of taxpayers.
   384	
   385	Saudi Arabia is the clearest rentier case. Oil rent finances the state, citizens receive public employment and transfers, and much of the private-sector labor force consists of migrants without citizenship \citep{chaudhry1997,hertog2010}. The migrant labor system ties a worker's legal residence to a sponsoring employer, which restricts the worker's ability to change employer or leave \citep{hanieh2011,kapiszewski2001}. On Table~\ref{tab:bondage} this is a restriction on mobility within wage labor, not chattel slavery; in the model it is a mobility restriction $g>0$ applied to a group with high outside options, exactly the case in which Proposition~\ref{prop:productive-power:domar} predicts that restriction pays. The early oil industry also produced organized protest: \citet{vitalis2007} documented the segregated labor hierarchy of the oil camps and the strikes it provoked. For citizens, the rentier bargain lowers producer dependence $\xi$, and Proposition~\ref{prop:productive-power:rentier} predicts that their withdrawal premium is small.
   386	
   387	\subsection{Catholic monarchies}
   388	
   389	In Habsburg Spain, Bourbon France and the Papal States, producers were mainly peasants owing seigneurial dues, the tithe and royal taxes, together with urban artisans and merchants. The privileged estates, clergy and nobility, were exempt from important direct taxes. The Church was simultaneously a landholder, a tithe receiver and a source of the monarch's legitimacy, so its coupling to $\pW$ was material as well as ideological. The tithe had a long history as an ecclesiastical claim on agricultural output \citep{constable1964}, and \citet{ekelund1996} analyzed the medieval Church as an economic organization that collected revenue for services.
   390	
   391	In Bourbon France, privilege sorted the fiscal burden. The heaviest direct tax fell on commoners, so the distribution of the burden was itself an output of political privilege; when the eighteenth-century monarchy tried to tax the privileged through new direct taxes, the resulting conflicts politicized taxation \citep{kwass2000}. In Languedoc the revenue drawn from producers was shared between the crown and provincial elites, whose collaboration made absolutism work \citep{beik1985}.
   392	
   393	The same fiscal interest produced a documented check. The monarchy strengthened village communities in Burgundy in order to tax them, and those communities then used royal courts to contest seigneurial dues \citep{root1987}. The crown's need for revenue thus raised the peasants' organized weight $\eta$ against their lords.
   394	
   395	In Castile, communal lands and municipal institutions mattered to peasant livelihoods \citep{vassberg1984}, and ordinary people litigated in large numbers in the royal courts \citep{kagan1981}. The Cortes bargained with the crown over new taxes, and the taxes paid by Castilian producers sustained the crown's borrowing \citep{drelichman2014}. In the Americas the same monarchy organized compelled state labor. The Potos\'i mining draft required indigenous communities in designated districts to send a share of their men to the mines, and \citet{dell2010} found persistent lower consumption and child growth in those districts today. In the Papal States, the pope was both temporal sovereign and head of the Church, which made the coupling of $\pI$ with fiscal administration direct \citep{prodi1987}.
   396	
   397	\citet{brenner1976} supplies the comparative lesson for this regime type. Seigneurial power, village organization and the fiscal needs of the crown interacted differently in France, England and eastern Europe, with different outcomes for peasant tenure. Productivity followed politics as much as technique: French agricultural output grew in some periods and regions and stagnated in others, and war, taxation and access to markets mattered more than peasant conservatism \citep{hoffman1996}. Catholic legitimation was common to several of these cases and did not determine the outcome. Village communities, royal courts, the Cortes and periodic revolt were the producers' channels of voice; flight to towns and colonies was their exit.
   398	
   399	\subsection{Secular democracies}
   400	
   401	In secular democracies, the citizen is a taxpayer and a voter at once, and the fiscal relation is the most general channel through which producers affect the state. The fiscal contract argument holds that states which depend on taxes must bargain with taxpayers, and that the bargain produces representation and services \citep{bates1985,moore2004,timmons2005}. Evidence for the link is conditional. \citet{ross2004} found that it is the cost of government relative to the services provided, rather than the level of taxation alone, that predicts democratization. \citet{levi1988} found that compliance in established democracies is quasi-voluntary: it depends on taxpayers' belief that others pay and that the government keeps its side of the bargain.
   402	
   403	The modern tax state depends on fiscal capacity, the ability to tax incomes broadly, which \citet{besley2011,besley2013} treat as an investment that states make when they expect common-interest spending such as defense. \citet{scheve2016} found that steeply progressive taxation in the twentieth century followed wars of mass mobilization, in which arguments that the wealthy should compensate for the sacrifices of conscripts proved persuasive, rather than following the extension of the franchise alone. This is the latent veto at work in a democratic register: those who supplied the soldiers and the war production obtained fiscal concessions.
   404	
   405	The working class appears in the comparative-historical literature as a force for democratization. \citet{rueschemeyer1992} argued that organized workers were the most consistent supporters of full democracy, against landlords and often against the bourgeoisie. Voice in secular democracies therefore includes the franchise, unions and the courts, and \citet{chenoweth2011} found that, in their data on twentieth-century campaigns, nonviolent campaigns relying on mass non-cooperation, including strikes and boycotts, succeeded more often than violent ones. Welfare regimes differ within this regime type. \citet{esping1990} classified liberal, conservative and social democratic regimes, and the liberal regime offers the weakest income protection.
   406	
   407	Capture episodes in secular democracies take the form of privileged access to tax and labor policy. Their documentation is subject to the source's three-part test, and the main empirical claims about unequal responsiveness are contested (Part II, Section 5.2). Documented checks include tax administration under judicial review, labor law enforced in independent courts, and the electoral reversal of fiscal policies. Part III treats the courts, including the contest between repeat players and occasional litigants (its Proposition 6.4).
   408	
   409	\subsection{Social reproduction across regimes}
   410	
   411	Every regime type relied on unpaid care to reproduce its producers, and the regimes differed mainly in how far the state or the market took over part of that work. In market economies the cost of raising children falls largely on parents, and disproportionately on mothers, even though the next generation of workers and taxpayers benefits everyone \citep{folbre1994}. Social democracies socialized more of the cost through public care services and policies that supported women's paid employment, which \citet{esping1990} and \citet{huber2001} treat as part of the social democratic welfare state. The Soviet Union drew women into paid work on a large scale while leaving most domestic work to them, a combination documented by \citet{lapidus1978}.
   412	
   413	The household's internal terms followed the same logic as the producers' terms elsewhere. \citet{kandiyoti1988} compared the household systems of sub-Saharan Africa with those she called classic patriarchy, found in a belt running from North Africa through the Middle East to South and East Asia, and showed that women bargained within each system according to its constraints. Her comparison concerns kinship and property systems, not religious doctrine, and it cuts across the regime types of this paper. \citet{laslett1989} trace the historical variation in how families, markets and states divided the work of reproduction. In the model's terms, these are differences in carers' fallback $o_h$ and standing $\eta_h$, set by property and family law in $\pP$ and $\pJ$ and by norms in $\pI$.
   414	
   415	\subsection{Summary across regimes}
   416	
   417	The comparison yields one regularity and one negative finding. The regularity is that producers' terms were worst where control over production was concentrated and coupled to coercion and to control of exchange: collectivization, the colonial mining draft, Gulag labor and the sponsorship of migrants. The negative finding is that this pattern does not follow ideology. It appears under a communist party, a Catholic monarchy and a modern monarchy legitimated by Islam, and its opposite, producers with strong voice, appears under social democracy, in Ottoman guilds and among Burgundian villagers. Tables~\ref{tab:regimes} and~\ref{tab:regimes2} record the dominant pattern in each regime type; the internal diversity is in the text.
   418	
   419	\begin{table}[p]
   420	\centering

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '280,500p' papers/latex/productive-power.tex | nl -ba -v280" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   280	\begin{table}[t]
   281	\centering
   282	\small
   283	\caption{Minimal form of the productive function in the hard cases. The right column records the strongest reading on which the function, or its accountability, might be absent.}
   284	\label{tab:hardcases}
   285	\begin{tabularx}{\textwidth}{@{}L{2.5cm}YY@{}}
   286	\toprule
   287	Case & Who produces and on what terms & Strongest counter-reading and reply \\
   288	\midrule
   289	Ju/'hoansi \citep{lee1979,marshall1976} & Men and women forage, sharing rules distribute meat, and gift exchange links camps & No one commands labor. Reply: production is universal and its terms are policed by leveling talk \citep{wiessner2005} \\
   290	Immediate-return foragers \citep{woodburn1982} & Food is consumed soon after it is obtained and accumulation is discouraged & Egalitarianism looks like the absence of power. Reply: it is produced by institutions of leveling \\
   291	Nuer \citep{evanspritchard1940} & Herding, horticulture and fishing are organized by households and kin & Evans-Pritchard stressed the absence of government. Reply: cattle rights and exchange organize production without an office \\
   292	Amazonian chiefs \citep{clastres1987} & Households garden and hunt, and the chief must give and work more & The flow runs from chief to group. Reply: this is a negative extraction share, not an absent function \\
   293	Upland Southeast Asia \citep{scott2009} & Swidden farmers choose crops that are hard to tax & Producers evade the state. Reply: they produce and govern their own terms \\
   294	Commons \citep{ostrom1990} & Users provide labor to maintain irrigation and other common resources & No state allocates labor. Reply: provision rules assign maintenance labor and are monitored \\
   295	\bottomrule
   296	\end{tabularx}
   297	\end{table}
   298	
   299	Among the Ju/'hoansi, production by both sexes is the basis of daily life, and the terms on which its results circulate are governed by sharing rules, gift partnerships and talk \citep{lee1979,lee2013,marshall1976}. \citet{wiessner2005} documented how the Ju/'hoansi enforce such norms, largely through criticism and talk rather than physical punishment. In the vocabulary of this paper, open access and costless fission keep $o$ close to $y$, and leveling sanctions keep it there. \citet{woodburn1982} generalized the point: in immediate-return societies equality is an achievement of institutions that prevent accumulation, not a default. \citet{boehm1999} called the same pattern a reverse dominance hierarchy, in which the group as a coalition dominates would-be dominants.
   300	
   301	Clastres's Amazonian chiefs are the most striking case for this pillar. The chief has no power to command, is expected to be generous, and works harder than others to supply what he gives away \citep{clastres1987}. In the model's terms, the leader's extraction share is negative. Clastres read this as a society actively preventing power from separating from it. That reading supports the distinction between Propositions A and B. The productive function is present, and its capture is prevented.
   302	
   303	Ostrom's commons supply the cleanest institutional image of the maintenance function at small scale. Her design principles require congruence between appropriation rules and provision rules, so that those who draw on an irrigation system or a fishery also contribute the labor that maintains it, under monitoring by the users themselves \citep{ostrom1990,ostromdesign2010}. A review of later studies found broad, though not uniform, support for the principles \citep{cox2010}. Provision rules are the productive pillar in miniature.
   304	
   305	The ethnographic record has limits that bear on the claim. Contact-era ethnographies describe groups living in marginal environments, often already in contact with states and markets, and foraging societies vary widely \citep{kelly1995}. Sahlins's argument that hunter-gatherers met their needs with modest labor \citep{sahlins1972} corrects any picture of constant struggle, but it does not remove production; it lowers its hours. The minimal-form proposition needs only that someone produces and that, where exit is open and costless, no one can take a share.
   306	
   307	\subsection{Counterexample attempts}
   308	
   309	The falsifier of Lemma~\ref{thm:productive-power:necessity} is a governance system that persists indefinitely while supported by no production and no replenishment of its stock. Six candidates come close and fail.
   310	
   311	A community living from an endowment consumes a finite stock unless the endowment earns a return, and a return is someone's production. Monasteries and mendicant orders that live by alms relocate production to donors. A raiding or tributary state relocates it to the raided and the tributary, as Lemma~\ref{lem:productive-power:relocation} predicts; the Spanish colonial labor draft discussed in Section~\ref{sec:comparison} is a documented instance in which the producers were outside the ruling community and inside its coercive reach \citep{dell2010}. A rentier state relocates production to the workers who extract the resource and the foreign buyers who pay for it; in the Gulf monarchies much of the extracting and building labor is done by migrants without citizenship \citep{hanieh2011,kapiszewski2001}. Full automation, as argued above, relocates the producer role to owners and maintainers of equipment. The original affluent society lowers labor hours without eliminating them \citep{sahlins1972}.
   312	
   313	The strongest attempt is the last of these taken to its limit: a society of self-maintaining machines serving a population that does nothing. The function would then be performed by equipment owned by someone, and the claim survives in its functional form. What would not survive is any claim that human labor holds a latent veto. The paper's claims about producer power are therefore conditional on human activity remaining necessary in production. That narrowing is the honest result of the counterexample.
   314	
   315	\section{Literature}
   316	\label{sec:literature}
   317	
   318	Four bodies of work bear on the productive pillar, and they rarely cite one another. Each answers part of the guiding question, and each leaves a gap that the framework of this series is meant to fill.
   319	
   320	The first asks who creates value and how it is divided. For \citet{marx1976}, labor applied to means of production owned by others yields a surplus appropriated as profit, and the compulsion that keeps wage workers at work is economic rather than legal. Polanyi's account of the nineteenth-century market society adds that labor, land and money are fictitious commodities, not produced for sale, and that treating them as commodities provoked a protective countermovement \citep{polanyi1944}. Both accounts locate power in production, but neither supplies a comparative instrument that applies equally to market and command economies. Recent distributional accounting measures who receives national income without asking how the terms were bargained \citep{piketty2018}. Work on social reproduction widens the category of producers to include unpaid household labor \citep{laslett1989}.
   321	
   322	The second body of work locates producers' power in their options and their organization. Hirschman's exit, voice and loyalty frame the options of members of any organization in decline \citep{hirschman1970}. \citet{freeman1984} applied the frame to trade unions, which have a monopoly face that raises wages and a collective-voice face that lets workers change conditions without quitting. \citet{wright2000} distinguished associational power, which comes from organization in unions and parties, from structural power, which comes from workers' position in tight labor markets or strategic sectors. \citet{silver2003} used the distinction to trace labor unrest across a century of relocating industries.
   323	
   324	Power resources theory explains welfare-state variation by the organization of wage earners and their parties \citep{korpi1983,esping1985}. The employer side of the same relation is monopsony: when workers cannot move costlessly between employers, firms set wages below the competitive level \citep{manning2003}, and local labor markets are often concentrated enough for this to matter \citep{azar2022}. These studies measure producer power well within capitalist democracies and say little about serfs, kolkhoz members or migrant workers under sponsorship.
   325	
   326	The third body of work is fiscal sociology, which treats the tax relation as the core of state formation \citep{campbell1993,martin2009}. \citet{levi1988} modeled rulers as revenue maximizers constrained by their bargaining power relative to constituents, by transaction costs and by their discount rates, and showed that compliance is quasi-voluntary: taxpayers comply when they believe others do and the ruler keeps bargains. \citet{bates1985} argued that owners of mobile assets can extract representative concessions. \citet{ross2004} tested the claim that taxation leads to representation and found that the relevant variable is taxation relative to the services government provides, and \citet{timmons2005} found that governments trade services for revenue with the groups that pay.
   327	
   328	Rentier-state theory supplies the converse: revenue that does not come from domestic taxpayers frees rulers from bargaining with them \citep{mahdavy1970,beblawiluciani1987,ross2001}. The converse is contested. \citet{habermenaldo2011} find no evidence that resource reliance promotes authoritarianism over time within countries. Part I \citep{long2026financial} treats rents (its Section 5) on the allocation side; this Part treats them as a change in producers' bargaining position.
   329	
   330	The fourth body of work explains when producers are bound. \citet{domar1970} proposed that serfdom or slavery arises where land is abundant relative to labor, because free peasants could otherwise leave to farm free land, and that free land, free peasants and non-working landowners cannot coexist. \citet{brenner1976} answered that the outcomes of the late-medieval demographic crisis differed across Europe with the same land-labor ratios, and that the balance of organized class power decided them. \citet{dell2010} showed that the Spanish colonial mining draft in Peru left lower household consumption and worse child health in the districts subject to it, centuries after its abolition. \citet{scott1976,scott1985} showed that peasants who cannot exit or speak openly resist through foot-dragging, evasion and gossip, and that they judge extraction against a subsistence ethic.
   331	
   332	The gap is a common instrument. Labor economics, fiscal sociology, rentier theory and the history of bondage each study one or two of the quantities that set producers' terms, in one or two regime types. The model in Section~\ref{sec:mechanisms} places the outside option, organization, employer concentration, non-producer revenue and conditional access to exchange in one notation that applies to a band, a kolkhoz, a Gulf labor camp and a unionized factory. It does not replace the specialized literatures. It shows where they meet.
   333	
   334	\section{Comparative analysis}
   335	\label{sec:comparison}
   336	
   337	Producers' terms were worst, in every regime type that produced such cases, where concentrated control over production was coupled to coercion and to control of exchange; ideology did not decide where this happened. The evidence comes from asking the same questions of each regime type: who produces and pays, who sets the terms of participation, how concentrated that control is, which other pillars it is coupled to, and which channels of exit and voice remain open.
   338	
   339	Two conventions govern the comparison. Where market-capitalist and secular-democratic institutions coexist in one country, the first type is read through the organization of the economy (private capital, labor markets, the structural power of business) and the second through the political organization of the fiscal relation (citizen taxpayers, universal suffrage, social insurance law). Judgments of concentration are qualitative, because no country has been coded under a preregistered scheme, and no value of $U_t$ or $\Integ_t$ is reported.
   340	
   341	\subsection{Market-capitalist societies}
   342	
   343	In market-capitalist societies most producers are wage earners, the self-employed and small businesses, and the terms of production are set mainly by employers in labor markets and by the state through tax and labor law. Consumers sustain enterprises by their purchases and pay a large share of indirect taxes. The holders of the pillar are therefore many, but control over terms is not evenly spread. \citet{azar2022} found that a large share of local labor markets in the United States are highly concentrated by the standard used in antitrust, and that concentration is associated with lower posted wages. Monopsony theory explains why: when moving between employers is costly, employers set wages below the competitive level \citep{manning2003}. In the notation of this paper, $\HW$ varies across local markets and is high in many of them.
   344	
   345	The structural power of business is the distinctive coupling of this regime type. \citet{lindblom1977} argued that because investment decisions are private and governments depend on growth, business holds a privileged position that requires no organization: governments anticipate the reaction of investors. \citet{przeworski1985} drew the consequence for labor parties, which must sustain profits to sustain employment. This is the exit option of mobile capital, and \citet{bates1985} predicted that the owners of mobile assets obtain concessions. The coupling $C_{\pF\pW}$ is high wherever those who allocate capital also set the terms of employment. Part I gives the primary treatment of that pair in its Section 5.
   346	
   347	Accountability in the pillar has rested on three channels: collective bargaining, labor mobility and the vote. Their strength has varied over time. \citet{farber2021} assembled survey data across the twentieth century and found that unions compressed the income distribution when they were strong. \citet{western2011} attributed a substantial part of the rise in American wage inequality after the 1970s to the decline of unions, including through the erosion of norms of fair pay in non-union firms. \citet{piketty2018} documented the same period's shift of pre-tax income toward the top of the distribution. These are documented changes in $q^{\mathrm{bar}}$ and $q^{\mathrm{voi}}$, not evidence of capture by themselves. A decline in bargaining coverage can follow from changes in industry composition and trade as well as from employer action and law.
   348	
   349	Documented checks are visible in the same record. Union contracts, minimum-wage laws, antitrust enforcement in labor markets and the expansion of social insurance in the twentieth century all raised producers' terms through voice. \citet{polanyi1944} treated the protective legislation of the nineteenth century as the countermovement of a society defending itself against the commodification of labor. Documented capture is harder to establish than decline. The source's capture-link criterion requires material evidence linking privileged access to an output \citep{largo2026hbs}. Accounts of how organized business reshaped American labor and tax policy from the 1970s \citep{hackerpierson2010} supply candidate links, and they remain contested in the way Part II \citep{long2026political} describes in its Section 5.2 for the wider literature on unequal political responsiveness.
   350	
   351	\subsection{Communist party-states}
   352	
   353	In the Soviet Union after collectivization and in China under the planned economy, the party-state was the dominant employer, the sole legal purchaser of most farm output and the owner of nearly all productive assets. Its share of control over the terms of productive participation approached one, so $\HW$ was near its maximum. The coupling of $\pW$ to the other pillars was also high, because the same apparatus set prices and procurement quotas ($\pF$), wrote labor law ($\pP$), staffed the courts ($\pJ$), ran the official unions and the press ($\pI$), and policed mobility ($\pC$).
   354	
   355	Collectivization is the most fully documented case in which every instrument of Definitions~\ref{def:productive-power:gate} and~\ref{def:productive-power:outside} was used at once: a single purchaser, restricted mobility, and access to exchange conditioned on membership of the collective farm. Peasants resisted it in 1930 by slaughtering livestock, petitioning and open revolt \citep{viola1996}. After collectivization, the kolkhoz delivered grain at state-set prices, and procurement in the years 1931 to 1933 continued in regions where famine was spreading \citep{davies2004}. Mobility was restricted, and peasants adapted with strategies of evasion and survival that \citet{fitzpatrick1994} documented in detail. Forced labor in the Gulag formed a further tier of compelled state labor \citep{applebaum2003}, and economic historians have argued that it was expensive to run and less productive than free labor \citep{gregory2003}. In the terms of Table~\ref{tab:bondage}, collective farmers were tied to the farm for long periods and Gulag prisoners were compelled state laborers. Neither group was chattel property.
   356	
   357	Soviet industrial workers held more power than the formal structure suggests, because labor was scarce. Chronic labor shortage, the soft budget constraint of enterprises \citep{kornai1986,kornai1992} and managers' need to meet plans gave workers an informal bargaining position. Workers in the 1930s used it through high turnover, absenteeism and control over the pace of work, despite harsh labor-discipline laws \citep{filtzer1986}. Even the Stakhanovite campaign of record-setting provoked conflict on the shop floor as well as productivity gains \citep{siegelbaum1988}.
   358	
   359	Chinese workers under the planned economy faced a more complete dependence on the enterprise. Housing, rations and welfare came through the work unit and through personal ties to superiors, which made the unit a site of dependence rather than of bargaining \citep{walder1986}. The household registration system closed the main exit, tying rural people to their place of birth and restricting their access to urban employment and services \citep{cheng1994}.
   360	
   361	The reform era changed the instruments without removing them. Migration from the countryside expanded producers' outside options, and labor protest grew. \citet{lee2007} compared the protests of laid-off state-sector workers in the northeastern rustbelt with those of migrant workers in the southern export zones, who used the courts and labor law as well as street protest. The official union federation remains tied to the party, which limits voice outside party channels \citep{friedman2010}. Documented checks in this regime type are therefore mainly informal: evasion, turnover, petitioning, and the regime's own fear of unrest. That they existed matters for the comparison. Even under the most integrated arrangement in the record, the latent veto of Proposition~\ref{prop:productive-power:latent-veto} operated through everyday resistance.
   362	
   363	\subsection{Social democracy and market socialism}
   364	
   365	In the Nordic social democracies, producers are wage earners and the self-employed in market economies, but their terms are set to an unusual degree by collective bargaining at the national and sectoral level and by universal social insurance. Union density and bargaining coverage have been high by international standards for most of the postwar period. Power resources theory explains the arrangement as the result of the organization of wage earners in unions and their alliance with social democratic parties \citep{korpi1983,esping1985}. \citet{esping1990} measured its consequence as decommodification, the degree to which people can maintain a livelihood without relying on the labor market. \citet{huber2001} traced the development of the welfare state to partisan government over decades.
   366	
   367	The distinctive coupling here is between $\pW$ and $\pP$, through corporatist bargaining in which unions, employers and the state set wages and social policy together. By the source's own standard this coupling is not capture \citep{largo2026hbs}. It is a coalition commanding agenda in two pillars, and in this case its effect was to raise producers' contestability rather than to lower it. Corollary~\ref{cor:productive-power:coupling} formalizes the asymmetry: capture requires instruments that lower producers' terms, and corporatist coupling has mainly strengthened voice. Universalism also has a fiscal logic. \citet{korpi1998} found that universal programs redistribute more than targeted ones, because they build coalitions of support that enlarge the budget. \citet{rothstein1996} showed how the Swedish administrative model made universal programs implementable.
   368	
   369	The limits of the model are documented as well. \citet{przeworski1985} argued that social democratic parties remain structurally dependent on private investment, and \citet{pontusson1992} traced the failure of Swedish wage-earner funds, the most ambitious attempt to transfer ownership to labor. \citet{rueda2005} argued that social democratic parties have incentives to protect labor-market insiders rather than outsiders in temporary or precarious employment. That cleavage is a candidate failure mode inside the pillar: high $\QW$ for insiders can coexist with low $\QW$ for outsiders.
   370	
   371	Market socialism and workers' self-management are the variants of this regime type in which producers formally own the enterprise. \citet{kornai1992} argued that reform socialism in Hungary and Yugoslavia retained soft budget constraints and party control of appointments, which limited the autonomy of self-managed firms. Worker cooperatives in market economies are the small-scale analogue. \citet{dow2003} surveyed the theory and evidence on labor-managed firms, and \citet{craig1993} studied the objectives of worker cooperatives in the plywood industry of the Pacific Northwest. In the model, a cooperative raises producers' outside option, since it is an employer that the producers themselves control, and it removes extraction within the firm while leaving taxation to the state.
   372	
   373	\subsection{Islamic states}
   374	
   375	Islamic states share a source of political legitimacy, the claim to govern according to religious law, and differ in nearly every other respect. The comparison here covers the Ottoman Empire, modern Iran and Saudi Arabia, and the productive arrangements in each are not derived from Islamic law alone. Some instruments are legal categories of the tradition, such as alms taxes and land taxes. Others, such as tax farming or migrant sponsorship, are fiscal and labor-market institutions that belong to particular states and periods.
   376	
   377	In the Ottoman Empire, organized crafts gave producers a channel of voice. The taxpaying subjects were mainly peasants, artisans and merchants, and urban crafts were organized in guilds that regulated entry, prices and quality while also serving the state as administrative and fiscal intermediaries \citep{baer1970}. The guild was thus a site of coupling between $\pW$ and $\pP$: guilds petitioned authorities and brought disputes to the courts. Studies of Ottoman and early Republican workers document strikes and labor organization in the nineteenth and early twentieth centuries \citep{quataert1995}.
   378	
   379	Control over Ottoman producers' terms was dispersed among intermediaries. \citet{karaman2010} compared Ottoman state finances with those of European states and found that Ottoman revenue per capita remained low and collection decentralized, with heavy reliance on tax farming. \citet{barkey2008} described Ottoman rule as brokerage with intermediaries rather than direct command. In the vocabulary of this paper, control over the terms of production was dispersed among intermediaries, so $\HW$ was moderate. Ibn Khaldun had already observed that dynasties begin with low tax rates that yield large revenues and end with high rates that yield little, as producers withdraw effort \citep{khaldun1958}. The observation states the latent veto in fourteenth-century terms.
   380	
   381	Islamic legal categories of taxation and charity, including the alms tax and endowments, shaped the fiscal relation and the provision of welfare. \citet{singer2008} surveyed charity in Islamic societies, including endowed public kitchens in the Ottoman Empire. The economic consequences of Islamic commercial law are debated. \citet{kuran2011} argued that rules of partnership, inheritance and endowment held back the formation of durable private enterprises in the Middle East; \citet{rubin2017} attributed divergence instead to the way rulers relied on religious authorities for legitimacy, and \citet{pamuk2000} offered a monetary and fiscal history that does not reduce Ottoman outcomes to law.
   382	
   383	Modern Iran shows producers' power at both extremes. Oil workers' strikes were central to the revolution of 1978 to 1979, and workers' councils briefly took over the management of factories before the new regime absorbed or suppressed them \citep{bayat1987}. In the following decades the urban poor pursued what \citet{bayat1997} called the quiet encroachment of the ordinary: unorganized, cumulative claims on land, services and public space. \citet{mahdavy1970} coined the concept of the rentier state using the Iranian case: oil revenue reduces the state's need to tax, and with it the bargaining weight of taxpayers.
   384	
   385	Saudi Arabia is the clearest rentier case. Oil rent finances the state, citizens receive public employment and transfers, and much of the private-sector labor force consists of migrants without citizenship \citep{chaudhry1997,hertog2010}. The migrant labor system ties a worker's legal residence to a sponsoring employer, which restricts the worker's ability to change employer or leave \citep{hanieh2011,kapiszewski2001}. On Table~\ref{tab:bondage} this is a restriction on mobility within wage labor, not chattel slavery; in the model it is a mobility restriction $g>0$ applied to a group with high outside options, exactly the case in which Proposition~\ref{prop:productive-power:domar} predicts that restriction pays. The early oil industry also produced organized protest: \citet{vitalis2007} documented the segregated labor hierarchy of the oil camps and the strikes it provoked. For citizens, the rentier bargain lowers producer dependence $\xi$, and Proposition~\ref{prop:productive-power:rentier} predicts that their withdrawal premium is small.
   386	
   387	\subsection{Catholic monarchies}
   388	
   389	In Habsburg Spain, Bourbon France and the Papal States, producers were mainly peasants owing seigneurial dues, the tithe and royal taxes, together with urban artisans and merchants. The privileged estates, clergy and nobility, were exempt from important direct taxes. The Church was simultaneously a landholder, a tithe receiver and a source of the monarch's legitimacy, so its coupling to $\pW$ was material as well as ideological. The tithe had a long history as an ecclesiastical claim on agricultural output \citep{constable1964}, and \citet{ekelund1996} analyzed the medieval Church as an economic organization that collected revenue for services.
   390	
   391	In Bourbon France, privilege sorted the fiscal burden. The heaviest direct tax fell on commoners, so the distribution of the burden was itself an output of political privilege; when the eighteenth-century monarchy tried to tax the privileged through new direct taxes, the resulting conflicts politicized taxation \citep{kwass2000}. In Languedoc the revenue drawn from producers was shared between the crown and provincial elites, whose collaboration made absolutism work \citep{beik1985}.
   392	
   393	The same fiscal interest produced a documented check. The monarchy strengthened village communities in Burgundy in order to tax them, and those communities then used royal courts to contest seigneurial dues \citep{root1987}. The crown's need for revenue thus raised the peasants' organized weight $\eta$ against their lords.
   394	
   395	In Castile, communal lands and municipal institutions mattered to peasant livelihoods \citep{vassberg1984}, and ordinary people litigated in large numbers in the royal courts \citep{kagan1981}. The Cortes bargained with the crown over new taxes, and the taxes paid by Castilian producers sustained the crown's borrowing \citep{drelichman2014}. In the Americas the same monarchy organized compelled state labor. The Potos\'i mining draft required indigenous communities in designated districts to send a share of their men to the mines, and \citet{dell2010} found persistent lower consumption and child growth in those districts today. In the Papal States, the pope was both temporal sovereign and head of the Church, which made the coupling of $\pI$ with fiscal administration direct \citep{prodi1987}.
   396	
   397	\citet{brenner1976} supplies the comparative lesson for this regime type. Seigneurial power, village organization and the fiscal needs of the crown interacted differently in France, England and eastern Europe, with different outcomes for peasant tenure. Productivity followed politics as much as technique: French agricultural output grew in some periods and regions and stagnated in others, and war, taxation and access to markets mattered more than peasant conservatism \citep{hoffman1996}. Catholic legitimation was common to several of these cases and did not determine the outcome. Village communities, royal courts, the Cortes and periodic revolt were the producers' channels of voice; flight to towns and colonies was their exit.
   398	
   399	\subsection{Secular democracies}
   400	
   401	In secular democracies, the citizen is a taxpayer and a voter at once, and the fiscal relation is the most general channel through which producers affect the state. The fiscal contract argument holds that states which depend on taxes must bargain with taxpayers, and that the bargain produces representation and services \citep{bates1985,moore2004,timmons2005}. Evidence for the link is conditional. \citet{ross2004} found that it is the cost of government relative to the services provided, rather than the level of taxation alone, that predicts democratization. \citet{levi1988} found that compliance in established democracies is quasi-voluntary: it depends on taxpayers' belief that others pay and that the government keeps its side of the bargain.
   402	
   403	The modern tax state depends on fiscal capacity, the ability to tax incomes broadly, which \citet{besley2011,besley2013} treat as an investment that states make when they expect common-interest spending such as defense. \citet{scheve2016} found that steeply progressive taxation in the twentieth century followed wars of mass mobilization, in which arguments that the wealthy should compensate for the sacrifices of conscripts proved persuasive, rather than following the extension of the franchise alone. This is the latent veto at work in a democratic register: those who supplied the soldiers and the war production obtained fiscal concessions.
   404	
   405	The working class appears in the comparative-historical literature as a force for democratization. \citet{rueschemeyer1992} argued that organized workers were the most consistent supporters of full democracy, against landlords and often against the bourgeoisie. Voice in secular democracies therefore includes the franchise, unions and the courts, and \citet{chenoweth2011} found that, in their data on twentieth-century campaigns, nonviolent campaigns relying on mass non-cooperation, including strikes and boycotts, succeeded more often than violent ones. Welfare regimes differ within this regime type. \citet{esping1990} classified liberal, conservative and social democratic regimes, and the liberal regime offers the weakest income protection.
   406	
   407	Capture episodes in secular democracies take the form of privileged access to tax and labor policy. Their documentation is subject to the source's three-part test, and the main empirical claims about unequal responsiveness are contested (Part II, Section 5.2). Documented checks include tax administration under judicial review, labor law enforced in independent courts, and the electoral reversal of fiscal policies. Part III treats the courts, including the contest between repeat players and occasional litigants (its Proposition 6.4).
   408	
   409	\subsection{Social reproduction across regimes}
   410	
   411	Every regime type relied on unpaid care to reproduce its producers, and the regimes differed mainly in how far the state or the market took over part of that work. In market economies the cost of raising children falls largely on parents, and disproportionately on mothers, even though the next generation of workers and taxpayers benefits everyone \citep{folbre1994}. Social democracies socialized more of the cost through public care services and policies that supported women's paid employment, which \citet{esping1990} and \citet{huber2001} treat as part of the social democratic welfare state. The Soviet Union drew women into paid work on a large scale while leaving most domestic work to them, a combination documented by \citet{lapidus1978}.
   412	
   413	The household's internal terms followed the same logic as the producers' terms elsewhere. \citet{kandiyoti1988} compared the household systems of sub-Saharan Africa with those she called classic patriarchy, found in a belt running from North Africa through the Middle East to South and East Asia, and showed that women bargained within each system according to its constraints. Her comparison concerns kinship and property systems, not religious doctrine, and it cuts across the regime types of this paper. \citet{laslett1989} trace the historical variation in how families, markets and states divided the work of reproduction. In the model's terms, these are differences in carers' fallback $o_h$ and standing $\eta_h$, set by property and family law in $\pP$ and $\pJ$ and by norms in $\pI$.
   414	
   415	\subsection{Summary across regimes}
   416	
   417	The comparison yields one regularity and one negative finding. The regularity is that producers' terms were worst where control over production was concentrated and coupled to coercion and to control of exchange: collectivization, the colonial mining draft, Gulag labor and the sponsorship of migrants. The negative finding is that this pattern does not follow ideology. It appears under a communist party, a Catholic monarchy and a modern monarchy legitimated by Islam, and its opposite, producers with strong voice, appears under social democracy, in Ottoman guilds and among Burgundian villagers. Tables~\ref{tab:regimes} and~\ref{tab:regimes2} record the dominant pattern in each regime type; the internal diversity is in the text.
   418	
   419	\begin{table}[p]
   420	\centering
   421	\small
   422	\caption{Who holds the productive pillar in each regime type, and how concentrated control over the terms of production is. Concentration is a qualitative judgment from the cited literature, not a coded value.}
   423	\label{tab:regimes}
   424	\begin{tabularx}{\textwidth}{@{}L{2.6cm}YYL{2.6cm}@{}}
   425	\toprule
   426	Regime type & Main producers and payers & Who sets the terms of participation & Concentration of control \\
   427	\midrule
   428	Market-capitalist & Wage earners, small firms, consumers and taxpayers & Employers in labor markets and the state through tax and labor law & Varies by local market and is high in many \\
   429	Communist party-state & State employees, collective farmers and, in the reform era, migrant workers & The party-state as employer, purchaser and owner & Near the maximum before reform \\
   430	Social democracy and market socialism & Wage earners and the self-employed under encompassing bargaining & Unions, employers' associations and the state jointly & Moderate, with power shared by peak organizations \\
   431	Islamic states & Ottoman peasants and guild artisans, Iranian workers, Gulf citizens and migrants & Intermediaries and guilds in the Ottoman case, the rentier state and sponsors in the Gulf & Moderate in the Ottoman case and high for Gulf migrants \\
   432	Catholic monarchies & Peasants, artisans and colonial indigenous communities & Lords, the Church as landholder and tithe receiver, and the crown & High locally, shared among privileged estates \\
   433	Secular democracies & Citizen taxpayers and wage earners & Legislatures, tax administrations and labor markets & Varies with the economic regime \\
   434	\bottomrule
   435	\end{tabularx}
   436	\end{table}
   437	
   438	\begin{table}[p]
   439	\centering
   440	\small
   441	\caption{Coupling of the productive pillar to other pillars, channels of exit and voice, and documented checks. Each documented check is cited in the corresponding subsection.}
   442	\label{tab:regimes2}
   443	\begin{tabularx}{\textwidth}{@{}L{2.6cm}YYY@{}}
   444	\toprule
   445	Regime type & Principal couplings & Exit and voice & A documented check \\
   446	\midrule
   447	Market-capitalist & Capital allocation and employment are held by the same actors & Job mobility, unions and the vote & Union wage compression in the mid-twentieth century \\
   448	Communist party-state & One apparatus prices output, writes labor law, runs unions and polices mobility & Turnover, evasion, petitions and migration after reform & Shop-floor control of the pace of work by Soviet workers \\
   449	Social democracy and market socialism & Corporatist bargaining joins producers and the legislature & Encompassing unions, elections and universal benefits & Universal programs that enlarged redistribution \\
   450	Islamic states & Guilds joined crafts to administration, and rents join citizens to the state & Guild petitions, courts, strikes and quiet encroachment & Oil workers' strikes in the Iranian revolution \\
   451	Catholic monarchies & The Church joined land, tithe and legitimation, and the crown joined tax and justice & Village litigation, the Cortes, flight and revolt & Burgundian villages contesting dues in royal courts \\
   452	Secular democracies & Taxpayers and the franchise are joined in the same citizens & Elections, courts, unions and mass non-cooperation & Progressive taxation after wars of mass mobilization \\
   453	\bottomrule
   454	\end{tabularx}
   455	\end{table}
   456	
   457	Section~\ref{sec:mechanisms} derives the mechanism behind the regularity: each instrument that worsened producers' terms in these cases lowers the outside option or organized weight in the production game, and each is held outside the productive pillar.
   458	
   459	\section{Mechanisms, failure modes and checks}
   460	\label{sec:mechanisms}
   461	
   462	Producers' terms in the production game of Definition~\ref{def:productive-power:game} are set by five quantities: what producers can obtain by leaving, how well they are organized, how concentrated control over their participation is, how much of the coalition's revenue comes from elsewhere, and whether access to exchange is conditioned on allegiance. Each is a parameter of the game, and the results below give their comparative statics. The model is deliberately simple so that the mechanisms stay separate, and its parameters are not estimated here.
   463	
   464	\subsection{Exit and concentration}
   465	
   466	\begin{lemma}[Exit floor]
   467	\label{lem:productive-power:exit-floor}
   468	If producers are atomized, so that each decides alone whether to participate and the coalition sets $u$, the coalition's optimal terms are $u^*=o$ and the extraction share is $\chi^*=1-o/y$.
   469	\end{lemma}
   470	
   471	\begin{proof}
   472	A producer participates if and only if $u\ge o$. The coalition's revenue $n(y-u)+R$ is decreasing in $u$, so it chooses the smallest $u$ at which producers participate, which is $u=o$.
   473	\end{proof}
   474	
   475	The exit floor is the whole of atomized producers' power. It is zero extraction when $o=y$, as in the band of Proposition~\ref{prop:productive-power:minimal-form}, and maximal extraction when $o=y_0$.
   476	
   477	\begin{lemma}[Concentration lowers the outside option]
   478	\label{lem:productive-power:concentration}
   479	Suppose a producer who leaves employer $j$, and is neither blocked nor gated, receives one new offer, from employer $k$ with probability $s_k$; an offer from a different employer is worth $o_1$ and an offer from the employer just left is worth no more than the fallback $y_0<o_1$. Then the outside option at employer $j$ is the composite $o_j$ of Definition~\ref{def:productive-power:outside}, and the employment-weighted mean is $\bar o=y_0+\gamma(1-g)(1-\HW)(o_1-y_0)$. Under the exit floor, the employment-weighted mean extraction share is
   480	\[
   481	\bar\chi=1-\frac{y_0+\gamma(1-g)(1-\HW)(o_1-y_0)}{y},
   482	\]
   483	which increases linearly in $\HW$.
   484	\end{lemma}
   485	
   486	\begin{proof}
   487	An exit succeeds with probability $\gamma(1-g)$; given success, the offer comes from a different employer with probability $1-s_j$. The expected value is $y_0+\gamma(1-g)(1-s_j)(o_1-y_0)=o_j$. Then $\sum_js_jo_j=y_0+\gamma(1-g)(o_1-y_0)\sum_j s_j(1-s_j)=y_0+\gamma(1-g)(1-\HW)(o_1-y_0)$, since $\sum_js_j=1$. Each employer sets $u_j=o_j$ by Lemma~\ref{lem:productive-power:exit-floor}, so $\chi_j=1-o_j/y$ and the weighted mean is $1-\bar o/y$.
   488	\end{proof}
   489	
   490	The lemma gives the source's concentration index a mechanical role in this pillar. Under its assumptions, average extraction rises linearly with $\HW$, at a rate equal to the value of a competing offer relative to output. A single employer, $\HW=1$, holds every producer at the fallback; this is the company town, and in the limit it is the party-state as sole employer before reform. Many small employers, $\HW\to 0$, give unrestricted producers the competing value $o_1$. The association between labor-market concentration and lower wages found by \citet{azar2022} is consistent with the lemma, though random rematching simplifies search in real labor markets \citep{manning2003}.
   491	
   492	\subsection{Voice and the withdrawal premium}
   493	
   494	Organized producers do not accept the exit floor. They bargain collectively, and their threat is withdrawal: a strike, a tax refusal, a boycott, a delivery strike by farmers, or mass flight. If the coalition's non-producer revenue does not cover its maintenance requirement, withdrawal imposes a cost beyond lost revenue, because the institutions cannot be paid. Let $\psi\ge 0$ be the cost per unit of that shortfall, so that at total revenue $T+R$ the coalition's payoff is
   495	\[
   496	V_S(T)=T+R-K-\psi\,(K-T-R)^+,\qquad (x)^+=\max(x,0).
   497	\]
   498	
   499	\begin{assumption}[Agreement covers maintenance]
   500	\label{ass:productive-power:feasible}

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '500,710p' papers/latex/productive-power.tex | nl -ba -v500" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   500	\label{ass:productive-power:feasible}
   501	The parameters satisfy $n(1-\eta)(y-o)\ge(1+\eta\psi)(K-R)^+$.
   502	\end{assumption}
   503	
   504	The assumption says that the surplus over producers' exit floor is large enough for an agreement to pay for the institutions. It holds automatically when $R\ge K$. When $R<K$ it fails for $\eta$ close to one, so fully organized producers facing a coalition without outside revenue lie outside the scope of the next result.
   505	
   506	\begin{proposition}[Voice share]
   507	\label{prop:productive-power:voice}
   508	Let producers bargain collectively with the coalition by the asymmetric Nash bargaining solution with producer weight $\eta\in[0,1]$, where disagreement gives producers $no$ and the coalition $V_S(0)=R-K-\psi(K-R)^+$. Under Assumption~\ref{ass:productive-power:feasible}, the agreed terms are
   509	\[
   510	u^*=o+\eta(y-o)+\Omega,\qquad \Omega=\frac{\eta\,\psi\,(K-R)^+}{n},
   511	\]
   512	and the agreement leaves no maintenance shortfall: $n(y-u^*)+R\ge K$.
   513	\end{proposition}
   514	
   515	\begin{proof}
   516	Write $\Psi=\psi(K-R)^+$ and $u_K=y-(K-R)^+/n$, the largest terms at which the coalition's revenue still covers $K$. For $u\le u_K$ the coalition's payoff is $V_S=n(y-u)+R-K$, which is linear; for $u>u_K$ it is lower by $\psi(K-n(y-u)-R)>0$. Consider first the linear problem, which maximizes $N(u)=(n(u-o))^{\eta}(n(y-u)+\Psi)^{1-\eta}$, the product of the gains $n(u-o)$ and $n(y-u)+R-K-V_S(0)=n(y-u)+\Psi$. For $0<\eta<1$ the logarithm of $N$ is strictly concave, and the first-order condition $\eta\,(n(y-u)+\Psi)=(1-\eta)\,n(u-o)$ gives $nu^*=\eta ny+(1-\eta)no+\eta\Psi$, the stated formula; for $\eta=0$ and $\eta=1$ the solution gives the whole gain to the coalition or to the producers, which the formula also covers. At $u^*$, $n(y-u^*)+R-K=n(1-\eta)(y-o)-\eta\Psi-(K-R)$, which is non-negative when $R\ge K$ (then $\Psi=0$) and, when $R<K$, equals $n(1-\eta)(y-o)-(1+\eta\psi)(K-R)\ge 0$ by Assumption~\ref{ass:productive-power:feasible}. So $u^*\le u_K$. The true Nash product with the payoff $V_S$ is never larger than $N(u)$ and equals it for $u\le u_K$. Hence $u^*$, which maximizes $N$ and lies where the two coincide, also maximizes the true Nash product.
   517	\end{proof}
   518	
   519	The terms have three parts. The exit floor $o$ is what producers obtain without organization. The bargained share $\eta(y-o)$ is what organization adds by splitting the surplus over the floor. The withdrawal premium $\Omega$ is what organization adds because the coalition cannot afford a withdrawal; it is the price of the latent veto of Proposition~\ref{prop:productive-power:latent-veto}. Organization is necessary for both of the latter parts. An individual producer's withdrawal costs the coalition only that producer's contribution $y-u$, which in a large population is too small to threaten the maintenance requirement. That is why the latent veto stays latent without collective action \citep{olson1965}. Unions, guilds, village communities, peasant assemblies, tax revolts and cooperatives are the institutions that raise $\eta$ above zero.
   520	
   521	\begin{corollary}[Organization flattens the concentration gradient]
   522	\label{cor:productive-power:gradient}
   523	Suppose each employer $j$ bargains with its own workers as in Proposition~\ref{prop:productive-power:voice}, with common weight $\eta$, common premium $\Omega$ and outside option $o_j$ from Definition~\ref{def:productive-power:outside}. Then the employment-weighted mean terms are $\bar u=\bar o+\eta(y-\bar o)+\Omega$, and
   524	\[
   525	\frac{\partial\bar u}{\partial\HW}=-(1-\eta)\,\gamma\,(1-g)\,(o_1-y_0)\le 0 .
   526	\]
   527	\end{corollary}
   528	
   529	\begin{proof}
   530	Averaging $u_j=o_j+\eta(y-o_j)+\Omega$ with weights $s_j$ gives $\bar u=(1-\eta)\bar o+\eta y+\Omega$. By Lemma~\ref{lem:productive-power:concentration}, $\partial\bar o/\partial\HW=-\gamma(1-g)(o_1-y_0)$, and the stated derivative follows.
   531	\end{proof}
   532	
   533	Hirschman's loyalty has an ambiguous place in the model. Loyalty that raises the threshold for exit lowers the effective outside option and with it the floor; loyalty that keeps members inside while they organize raises $\eta$ \citep{hirschman1970}. Which effect dominates depends on whether the loyal can speak.
   534	
   535	The same bargaining logic applies inside the household, where most care labor is done. \citet{agarwal1997} argued that a household member's bargaining power depends on the fallback position available outside the household: property, paid employment, access to common resources, and support from kin, community or state. In the notation of the model, a carer's terms are $o_h+\eta_h(y_h-o_h)$, where $o_h$ is that fallback and $\eta_h$ the carer's organized or normative standing. Property rights, divorce law, public childcare and access to paid work all act on $o_h$. The paper does not develop the household game further, but the instruments that set $o_h$ are, like those in Assumption~\ref{ass:productive-power:instruments} below, held largely in $\pP$, $\pJ$ and $\pI$.
   536	
   537	\subsection{The bondage condition}
   538	
   539	A coalition can lower the outside option directly by restricting mobility. Write $o(g)=y_0+(1-g)(o_0-y_0)$, where $o_0$ is the outside option at $g=0$ given by Definition~\ref{def:productive-power:outside}. Enforcement costs the coalition $\kappa(g)$ per producer, with $\kappa(0)=0$ and $\kappa$ increasing and convex.
   540	
   541	\begin{proposition}[Domar-Brenner condition]
   542	\label{prop:productive-power:domar}
   543	Suppose the coalition chooses $g$ and then sets terms, with producers bargaining with weight $\eta\in[0,1)$ as in Proposition~\ref{prop:productive-power:voice} (the atomized case is $\eta=0$), and Assumption~\ref{ass:productive-power:feasible} holds at every $g$. Then the coalition's payoff, net of terms that do not depend on $g$, is $n[(1-\eta)g(o_0-y_0)-\kappa(g)]$.
   544	\begin{enumerate}
   545	\item[(a)] If $\kappa(g)=\kappa g$ is linear, restriction is chosen ($g^*=1$) when $(1-\eta)(o_0-y_0)>\kappa$ and not chosen ($g^*=0$) when $(1-\eta)(o_0-y_0)<\kappa$.
   546	\item[(b)] If $\kappa$ is differentiable and strictly convex with $\kappa'(0)<(1-\eta)(o_0-y_0)<\kappa'(1)$, then $g^*\in(0,1)$ is the unique solution of $\kappa'(g^*)=(1-\eta)(o_0-y_0)$, and $g^*$ is increasing in $o_0-y_0$ and decreasing in $\eta$.
   547	\end{enumerate}
   548	\end{proposition}
   549	
   550	\begin{proof}
   551	By Proposition~\ref{prop:productive-power:voice}, the producers' terms at outside option $o$ are $u^*=o+\eta(y-o)+\Omega$, where $\Omega$ does not depend on $o$, and the agreement leaves no shortfall, so the coalition's payoff from producers is $n(y-u^*)=n[(1-\eta)(y-o)-\Omega]$. Substituting $o(g)=o_0-g(o_0-y_0)$ gives $n[(1-\eta)(y-o_0)-\Omega]+n(1-\eta)g(o_0-y_0)$, and subtracting enforcement cost $n\kappa(g)$ leaves the stated $g$-dependent part. In case (a) the payoff is linear in $g$ with slope $n[(1-\eta)(o_0-y_0)-\kappa]$, so the optimum is at $g=1$ when the slope is positive and at $g=0$ when it is negative. In case (b) the payoff is strictly concave, its derivative is positive at $g=0$ and negative at $g=1$, so the unique maximizer satisfies the first-order condition. Because $\kappa'$ is strictly increasing, a larger right side $(1-\eta)(o_0-y_0)$ requires a larger $g^*$; the right side increases in $o_0-y_0$ and decreases in $\eta$.
   552	\end{proof}
   553	
   554	The proposition places two classic explanations of bondage in one inequality. Domar's land-labor hypothesis concerns $o_0$: where land is abundant, a free peasant can leave and farm independently, so $o_0$ is high and binding the peasant pays \citep{domar1970}. Where land is scarce and labor abundant, $o_0$ is already close to $y_0$, the wage market holds producers near the floor, and restriction adds little. Brenner's objection concerns $\kappa$ and $\eta$: organized peasant communities raise the cost of enforcing restriction and bargain over terms, so the same land-labor ratio produced serfdom in one region and free tenure in another \citep{brenner1976}. The two accounts are not rivals in this form. They name different terms of the same condition, and the empirical question is which term varied more across the cases at issue.
   555	
   556	Organization also lowers the return to restriction, since a coalition facing organized producers captures only the fraction $1-\eta$ of any reduction in their outside option. That gives a reason for coercive suppression of organization to accompany mobility restriction, a joint pattern visible in collectivization and in the sponsorship system for migrants, where workers' organization was also restricted. Part V \citep{long2026coercive} gives the primary treatment of this pair in its Section 6.5, including the allegiance margin of sanctions (its Definition 2.5) on which coercive enforcement of a gate depends.
   557	
   558	\subsection{Rents}
   559	
   560	\begin{proposition}[Rentier comparative static]
   561	\label{prop:productive-power:rentier}
   562	In Proposition~\ref{prop:productive-power:voice}, the withdrawal premium $\Omega$ is non-increasing in non-producer revenue $R$. It falls at rate $\eta\psi/n$ while $R<K$ and is zero for all $R\ge K$. The exit floor and the bargained share do not depend on $R$.
   563	\end{proposition}
   564	
   565	\begin{proof}
   566	$\Omega=\eta\psi(K-R)^+/n$. For $R<K$ its derivative in $R$ is $-\eta\psi/n\le 0$; for $R\ge K$ it is identically zero. The other two terms, $o$ and $\eta(y-o)$, contain no $R$. Raising $R$ relaxes Assumption~\ref{ass:productive-power:feasible}, so the result stays within its scope.
   567	\end{proof}
   568	
   569	The proposition refines the rentier-state argument. Rents do not lower producers' terms by making producers less productive or less organized. They remove the part of producers' bargaining power that rested on the coalition's need for their contribution, and they remove it only up to the point where rents cover the maintenance requirement. Beyond that point additional rent changes nothing in this model. Within a country, the effect of rents on concessions to producers should therefore be concentrated near the threshold at which rents cover the cost of running the state, and small far above or below it. Across countries, a null average effect such as that reported by \citet{habermenaldo2011} is consistent with the model if most variation lies away from the threshold. Measuring the maintenance requirement is difficult, and Section~\ref{sec:measurement} proposes a proxy.
   570	
   571	For the citizens of a rentier state, the premium is near zero and their terms are set by the coalition's choice to distribute rent, not by their capacity to withhold. The producers of the rent are elsewhere, and Lemma~\ref{lem:productive-power:relocation} says where: in the extraction workforce, which in the Gulf monarchies is largely foreign, and among foreign buyers.
   572	
   573	\subsection{The participation gate}
   574	
   575	A coalition can lower producers' outside options without restricting their movement, by conditioning access to exchange. A producer who cannot buy inputs, sell output, obtain credit or be hired has nowhere to go even if free to walk away.
   576	
   577	\begin{proposition}[Gate]
   578	\label{prop:productive-power:gate}
   579	Let $o$ denote the outside option at $\gamma=1$, so that under the gate of Definition~\ref{def:productive-power:gate} it is $o_\gamma=y_0+\gamma(o-y_0)$. Under Assumption~\ref{ass:productive-power:feasible}, the agreed terms are $u^*(\gamma)=o_\gamma+\eta(y-o_\gamma)+\Omega$, and
   580	\[
   581	\frac{\partial u^*}{\partial\gamma}=(1-\eta)(o-y_0)\ge 0 .
   582	\]
   583	If the gate is closed ($\gamma=0$), producers are atomized ($\eta=0$) and rents cover the maintenance requirement ($R\ge K$), producers are held at the autarky value, $u^*=y_0$, and the coalition takes $n(y-y_0)$.
   584	\end{proposition}
   585	
   586	\begin{proof}
   587	Substitute $o_\gamma$ for $o$ in Proposition~\ref{prop:productive-power:voice}. Since $do_\gamma/d\gamma=o-y_0$ and $u^*$ depends on the outside option through $(1-\eta)o_\gamma$, the derivative follows. With $\gamma=0$, $o_\gamma=y_0$; with $\eta=0$, $\Omega=0$ and $u^*=o_\gamma=y_0$, and the coalition's revenue from producers is $n(y-y_0)$.
   588	\end{proof}
   589	
   590	The closed gate with atomized producers is the most complete form of producer dependence in the model. Nothing about it requires the producers to be owned, bound to land, or imprisoned. It requires only that access to exchange pass through a checkpoint controlled by the coalition and that the checkpoint test allegiance. The coalition needs control over exchange (markets, credit, licenses, employment) to build the checkpoint, a criterion of allegiance to apply at it, and enforcement to keep producers from trading around it. Part IV (Section 6.5) treats the coupling of belief and production from the side of belief, including the quasi-voluntary compliance of taxpayers. Section~\ref{sec:revelation} returns to this configuration.
   591	
   592	\subsection{Capture of the productive pillar}
   593	
   594	\begin{definition}[Capture of the productive pillar]
   595	\label{def:productive-power:w-capture}
   596	A \emph{productive capture link} is a capture link $(S\to j,\pW)$ in the sense of \citet{largo2026hbs} in which the privileged discretion held by $S$ is control over one of the parameters through which the production game sets producers' terms: their exit (through $g$ or the concentration $\HW$), their organization (through $\eta$), their access to exchange (through $\gamma$), or the coalition's exposure to their withdrawal (through non-producer revenue $R$ or the shortfall cost $\psi$). Material evidence must tie the exercise of that control to the terms $u$ or the extraction share $\chi$. The productive pillar is \emph{captured} at $t$ when productive capture links persist and the pillar's term $H_{\pW,t}(1-\QW_t)$ in $U_t$ is high.
   597	\end{definition}
   598	
   599	The definition inherits the source's three conditions, including the requirement of material evidence. Low wages, high taxes or concentrated employment do not by themselves establish capture. They may reflect low productivity, the cost of public goods that producers value, or economies of scale. Capture requires a documented instrument and a documented link from the instrument to the terms.
   600	
   601	\begin{assumption}[Assignment of instruments]
   602	\label{ass:productive-power:instruments}
   603	The instruments that change the parameters of the production game are exercised in the following pillars. Mobility restriction $g$ requires enforcement in $\pC$. Concentration of control over productive means, which raises $\HW$, is an allocation of resources in $\pF$. Lowering producers' organized weight $\eta$ requires prohibition in $\pP$, enforcement in $\pC$ or delegitimation in $\pI$. Closing the gate requires control of exchange in $\pF$, an allegiance criterion supplied in $\pI$ (the legitimation function of Part IV, Definition 2.1, the practices that produce and validate the beliefs about rules and authority on which members' coordination depends \citep{long2026ideological}), and enforcement in $\pC$. Raising non-producer revenue $R$ is an allocation in $\pF$. Lowering the shortfall cost $\psi$ requires reserves accumulated in $\pF$ or the lawful hiring of replacement producers, whose permission is set in $\pP$.
   604	\end{assumption}
   605	
   606	\begin{corollary}[Capture requires coupling]
   607	\label{cor:productive-power:coupling}
   608	Under Assumption~\ref{ass:productive-power:instruments}, any action by a coalition $S$ that lowers producers' terms $u^*$ below their value at the baseline parameters $(\HW^0,g=0,\eta_0,\gamma=1,R_0,\psi_0)$ is taken in at least one pillar $n\ne\pW$. Hence a captured productive pillar implies $C_{n\pW,t}>0$ for some $n\in\{\pF,\pP,\pI,\pC\}$, with $S$ the coalition in question.
   609	\end{corollary}
   610	
   611	\begin{proof}
   612	By Proposition~\ref{prop:productive-power:voice}, Proposition~\ref{prop:productive-power:gate} and Lemma~\ref{lem:productive-power:concentration}, $u^*$ is non-decreasing in $o$, $\eta$, $\gamma$ and $\psi$ and non-increasing in $R$, with $o$ non-increasing in $g$ and $\HW$ by Definition~\ref{def:productive-power:outside}. Holding output $y$ and the maintenance requirement $K$ fixed, a reduction of $u^*$ therefore requires raising $g$ or $\HW$, lowering $\eta$, $\gamma$ or $\psi$, or raising $R$. By Assumption~\ref{ass:productive-power:instruments} each of these is exercised in a pillar other than $\pW$. If $S$ exercises it and also holds the terms of production, $S$ commands decisions in both $\pW$ and that pillar, which is $C_{n\pW,t}>0$.
   613	\end{proof}
   614	
   615	The corollary depends on the assignment, which is a modeling claim rather than a theorem. The hardest case for it is the hiring of replacement workers during a strike, which happens in the labor market itself; the assignment places it in $\pP$ because whether replacement is lawful is decided there. The assignment is defensible because each instrument in the comparative record was in fact exercised outside the productive layer: passports and residence permits by police and ministries, procurement prices by planners, union prohibitions by legislatures and courts, and allegiance tests by the authorities that define loyalty. Its consequence is that capture of production is never a fact about production alone. A society in which producers work long hours for low pay under many competing employers, free to organize and to leave, has a poor productive pillar but not a captured one. This is the pillar-level form of Largo's requirement that a strong classification show both concentration and cross-pillar integration \citep{largo2026hbs}, and of Part VII's result that Proposition A does not imply Proposition B. The function is implemented at every parameter value of the production game. Capture is a region of the parameter space.
   616	
   617	\subsection{Failure modes and checks}
   618	
   619	Each instrument in the production game defines a failure mode, and each failure mode has a check that interrupts it.
   620	
   621	Concentration of employment or purchase lowers the outside option (Lemma~\ref{lem:productive-power:concentration}). Antitrust enforcement in labor markets, the entry of new employers and public employment of last resort raise $o$. Cooperatives add an employer that producers themselves control \citep{dow2003}.
   622	
   623	Mobility restriction lowers the outside option directly (Proposition~\ref{prop:productive-power:domar}). Portability of benefits, abolition of tied residence and the right to change employer interrupt it. The condition in Proposition~\ref{prop:productive-power:domar} also shows when the check is under most pressure: when producers' free outside options are high, the coalition gains most from restriction.
   624	
   625	Suppression of organization lowers $\eta$ and with it both the bargained share and the withdrawal premium (Proposition~\ref{prop:productive-power:voice}). Legal protection of association and strikes, independent courts that enforce it (Part III, Section 6), and union democracy interrupt it. Michels's argument that organizations develop oligarchic leaderships applies to unions as well \citep{michels1915}, and Part II states it as a conditional tendency (its Proposition 6.2) rather than a law. The International Typographical Union studied by \citet{lipset1956} is the classic documented exception, a union that kept a two-party internal democracy.
   626	
   627	Rents remove the withdrawal premium (Proposition~\ref{prop:productive-power:rentier}). Fiscal rules that route rents into funds outside the coalition's discretion, and taxation that keeps the state dependent on domestic producers, are the checks the model suggests. Their effectiveness is an empirical question this paper does not settle.
   628	
   629	The gate lowers outside options through control of exchange (Proposition~\ref{prop:productive-power:gate}). Open markets, multiple sources of credit and employment, and the legal separation of economic access from political allegiance keep $\gamma$ close to one. The check is a separation of pillars: the actors who test allegiance must not control exchange.
   630	
   631	\begin{figure}[t]
   632	\centering
   633	\begin{tikzpicture}[x=1cm,y=1cm,>=stealth]
   634	  \node[draw,rounded corners,minimum width=2.6cm,minimum height=1.2cm,align=center] (W) at (0,0) {Producers\\ $\pW$};
   635	  \node[draw,rounded corners,minimum width=2.6cm,minimum height=1.2cm,align=center] (S) at (7,0) {Coalition $S$\\ maintenance $K$};
   636	  \node[align=center,font=\small] (F) at (0,2.6) {$\pF$: concentration $\HW$,\\ rents $R$, control of exchange};
   637	  \node[align=center,font=\small] (C) at (0,-2.6) {$\pC$: mobility restriction $g$,\\ enforcement of the gate};
   638	  \node[align=center,font=\small,anchor=east] (PI) at (-2.6,0) {$\pP$, $\pI$: organization $\eta$,\\ allegiance test};
   639	  \draw[->,thick] ([yshift=3mm]W.east) -- node[above,font=\small]{output $n(y-u)$} ([yshift=3mm]S.west);
   640	  \draw[->,thick,dashed] ([yshift=-3mm]W.east) -- node[below,font=\small]{withdrawal threat $\Omega$} ([yshift=-3mm]S.west);
   641	  \draw[->] (F) -- (W);
   642	  \draw[->] (C) -- (W);
   643	  \draw[->] (PI) -- (W);
   644	\end{tikzpicture}
   645	\caption{Instruments of the production game. Producers supply output to the coalition and hold a withdrawal threat whose value depends on the coalition's maintenance shortfall; every instrument that lowers producers' terms is held in another pillar.}
   646	\label{fig:instruments}
   647	\end{figure}
   648	
   649	\section{Measurement}
   650	\label{sec:measurement}
   651	
   652	The model's parameters correspond to observable quantities, though several can be measured only by proxy. Table~\ref{tab:indicators} lists an indicator for each. The list follows the source's rule that weights and codings be preregistered and that no aggregate index be reported for a real country without a documented coding \citep{largo2026hbs}. Largo also warns that measurement invariance across regimes must be tested before indicators are compared \citep{largo2026hbs}. Union density means something different under a party-controlled federation than under independent unions, and the indicators below are meant to be coded with that difference recorded.
   653	
   654	\begin{table}[t]
   655	\centering
   656	\small
   657	\caption{Indicators for the parameters of the production game and the components of productive contestability. Each indicator requires a preregistered coding rule before use.}
   658	\label{tab:indicators}
   659	\begin{tabularx}{\textwidth}{@{}L{3.6cm}Y@{}}
   660	\toprule
   661	Quantity & Indicator \\
   662	\midrule
   663	Concentration $\HW$ & Herfindahl index of employment or vacancy shares in local labor markets, the state's share of employment, and the share of farm output sold to a single purchaser \\
   664	Outside option $o$ & Rates of job-to-job transition, wage changes on switching employer, and the legal ability to change employer or residence \\
   665	Mobility restriction $g$ & Statutes and practice on internal passports, residence permits tied to an employer, and debt or land ties \\
   666	Organized weight $\eta$ & Union density, bargaining coverage, legality of strikes, and the independence of unions from the ruling party or employer \\
   667	Rents and maintenance, $R$ and $K$ & Non-tax revenue relative to recurrent spending on administration, courts, security and public information \\
   668	Producer dependence $\xi$ & Share of government revenue raised from domestic taxes and contributions \\
   669	Participation gate $\gamma$ & Rules that condition employment, licenses, credit or market access on political or religious criteria, coded from statute and documented practice \\
   670	Legal access $q^{\mathrm{leg}}$ & Availability, cost and independence of labor and tax adjudication, coded with the components of Part III, Definition 2.4 \\
   671	Income protection $q^{\mathrm{inc}}$ & Replacement rates of unemployment, sickness and old-age insurance \\
   672	Care labor $h$ and carers' fallback $o_h$ & Time-use surveys of unpaid care by sex, coverage of public childcare and paid leave, and women's property and divorce rights \\
   673	\bottomrule
   674	\end{tabularx}
   675	\end{table}
   676	
   677	The maintenance requirement $K$ is the hardest quantity to measure. A workable proxy is recurrent spending on the core functions of the other five pillars, excluding transfers and investment, since those are the outlays that cannot be postponed without loss of function. The proxy is imperfect because some transfers are themselves maintenance (pensions to soldiers, stipends to clergy) and because the shortfall cost $\psi$ depends on reserves and borrowing capacity. A preregistered study would fix the proxy and test sensitivity to alternatives.
   678	
   679	The model and the comparison yield nine testable hypotheses, listed with their falsifiers in Table~\ref{tab:hypotheses}. Several refine the source's hypotheses H5 and H6 \citep{largo2026hbs}.
   680	
   681	\begin{table}[t]
   682	\centering
   683	\small
   684	\caption{Hypotheses for the productive pillar. Each prediction follows from the result named in the second column; the falsifier is the observation that would refute it.}
   685	\label{tab:hypotheses}
   686	\begin{tabularx}{\textwidth}{@{}L{1.0cm}L{2.4cm}YY@{}}
   687	\toprule
   688	 & Basis & Prediction & Falsifier \\
   689	\midrule
   690	HW1 & Source H5, Lemma~\ref{lem:productive-power:concentration} & Higher bargaining coverage weakens the association between employer concentration and lower pay & The concentration gradient is the same at high and low coverage \\
   691	HW2 & Fiscal contract & Governments concede more services and representation where domestic taxes supply more revenue & No relation after conditioning on income, as some tests find \\
   692	HW3 & Proposition~\ref{prop:productive-power:rentier} & The effect of rents on concessions to producers is largest where rents are close to the cost of running the state & The effect is uniform in the ratio of rents to maintenance or largest far from one \\
   693	HW4 & Proposition~\ref{prop:productive-power:domar} & Bondage is more frequent where free exit is valuable and enforcement is cheap & Its incidence is unrelated to both across regions under comparable states \\
   694	HW5 & Everyday resistance & Covert non-compliance rises where open voice is suppressed & Evasion and turnover are unrelated to repression of organization \\
   695	HW6 & Insiders and outsiders & Contestability differs between permanent and precarious workers in encompassing welfare states & No difference in bargaining coverage or income protection between the groups \\
   696	HW7 & Persistence & Compelled labor drafts leave lower consumption in affected districts long after abolition & Comparable drafts show no persistent effect at their boundaries \\
   697	HW8 & Source H6 & Higher tax revenue with accountable provision goes with lower worker vulnerability & Vulnerability rises with provision \\
   698	HW9 & Lemma~\ref{lem:productive-power:reproduction} and household bargaining & Unpaid care is shared more evenly where carers' fallback positions are stronger & The division of unpaid care is unrelated to property rights, paid employment and public care \\
   699	\bottomrule
   700	\end{tabularx}
   701	\end{table}
   702	
   703	The exit hypotheses, HW1, HW4 and HW7, test how outside options set terms. HW1 is Corollary~\ref{cor:productive-power:gradient}: organization scales the concentration gradient by $1-\eta$, so it should be flatter where bargaining coverage is high. HW4 is the Domar-Brenner condition, and its test requires regional comparisons within one state, so that enforcement institutions are held roughly constant while land-labor ratios and peasant organization vary. HW7 generalizes \citet{dell2010}, whose regression-discontinuity design at the boundary of the draft area is the template.
   704	
   705	The fiscal hypotheses, HW2, HW3 and HW8, test the coalition's dependence on producers. HW2 carries the condition that \citet{ross2004} found necessary: the relevant variable is the price of government services, not taxation alone. HW3 is the paper's sharpest new prediction. If most observed variation in rents lies far from the threshold at which rents cover the cost of the state, it reconciles the rentier literature with null findings such as those of \citet{habermenaldo2011}. HW8 is the source's public-goods rival stated for producers: if it holds, high taxation is not evidence of extraction.
   706	
   707	The voice hypotheses, HW5, HW6 and HW9, test what happens to producers whose organized weight is low. HW5 follows \citet{scott1985} and the Soviet evidence of \citet{fitzpatrick1994} and \citet{filtzer1986}, and its difficulty is that covert resistance is hard to observe by design. HW6 tests the insider-outsider cleavage that \citet{rueda2005} identified. HW9 applies the household version of the bargaining model, with the fallback positions emphasized by \citet{agarwal1997}.
   708	
   709	Two identification problems apply to all nine. Organization is endogenous to the terms it is supposed to explain, since producers organize more where they expect gains. Rents, concentration and gates are chosen by coalitions that anticipate producers' responses. Event studies around reforms that change one instrument at a time, of the kind Largo proposes for oversight reforms \citep{largo2026hbs}, are the most direct remedy. Examples include the abolition of tied residence, the legalization of independent unions and the creation of a sovereign fund that removes rents from current budgets.
   710	

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "perl -ne 'while(/\\\\label\\{(["'^}]+)'"\\}/g){"'$l{$1}.="$.:"} while(/'"\\\\(?:ref|cref|Cref)\\{(["'^}]+)'"\\}/g){for "'$x(split /,/,$1){$r{$x}.="$.:"}} while(/'"\\\\cite(?:t|p|alp|author|year)?\\{(["'^}]+)'"\\}/g){for "'$x(split /,/,$1){$c{$x}.="$.:"}} while(/'"\\\\bibitem(?:\\[["'^]]*'"\\])?\\{(["'^}]+)'"\\}/g){"'$b{$1}.="$.:"} END{for(sort keys %r){print "UNDEFINED_REF $_ used $r{$_}'"\\n\" unless "'$l{$_}} for(sort keys %l){print "DUP_LABEL $_ at $l{$_}'"\\n\" if "'$l{$_}=~/:.*:/} for(sort keys %c){print "UNDEFINED_CITE $_ used $c{$_}'"\\n\" unless "'$b{$_}} for(sort keys %b){print "DUP_BIB $_ at $b{$_}'"\\n\" if "'$b{$_}=~/:.*:/}}'"' papers/latex/productive-power.tex
perl -ne 'while(/\\\\begin\\{(["'^}]+)'"\\}/g){push @s,["'$1,$.]}; while(/'"\\\\end\\{(["'^}]+)'"\\}/g){"'$x=pop @s; if(!$x||$x->[0] ne $1){print "ENV_MISMATCH line $. end=$1 open=".($x?$x->[0]:"NONE")."'"\\n\"}} END{for(@s){print \"UNCLOSED_ENV "'$_->[0] line $_->[1]'"\\n\"}}' papers/latex/productive-power.tex
perl -ne '"'$x=$_; $x=~s/'"\\\\[{}%&#_"'$]//g; $x=~s/%.*//; $o=()=$x=~/'"\\{/g; "'$c=()=$x=~/'"\\}/g; "'$bal+=$o-$c; print "NEG_BRACE line $.'"\\n\" if "'$bal<0; END{print "FINAL_BRACE_BALANCE $bal'"\\n\"}' papers/latex/productive-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 exited 25 in 0ms:
Unmatched [ in regex; marked by <-- HERE in m/\\[ <-- HERE {}%&#_5.044000/ at -e line 1, <> line 1.
FINAL_BRACE_BALANCE 

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "perl -ne '"'$x=$_; $x=~s/'"\\\\[{}%&#_\\"'$]//g; $x=~s/%.*//; $o=()=$x=~/'"\\{/g; "'$c=()=$x=~/'"\\}/g; "'$bal+=$o-$c; print "NEG_BRACE line $.'"\\n\" if "'$bal<0; END{print "FINAL_BRACE_BALANCE $bal'"\\n\"}' papers/latex/productive-power.tex
rg -n '(?<"'!'"\\\\)[#%&]' papers/latex/productive-power.tex
rg -n '(?<"'!'"\\\\)_' papers/latex/productive-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 exited 2 in 0ms:
FINAL_BRACE_BALANCE 0
rg: regex parse error:
    (?:(?<!\\)[#%&])
       ^^^^
error: look-around, including look-ahead and look-behind, is not supported

Consider enabling PCRE2 with the --pcre2 flag, which can handle backreferences
and look-around.
rg: regex parse error:
    (?:(?<!\\)_)
       ^^^^
error: look-around, including look-ahead and look-behind, is not supported

Consider enabling PCRE2 with the --pcre2 flag, which can handle backreferences
and look-around.

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "rg --pcre2 -n '(?<"'!'"\\\\)[#%&]' papers/latex/productive-power.tex
rg --pcre2 -n '(?<"'!'"\\\\)_' papers/latex/productive-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
6:\usepackage[margin=1in]{geometry}      % one-inch margins, as the writing standard specifies
8:\setlength{\parskip}{0pt}          % conventional article: indent, no vertical gap
16:\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
36:% Pillar labels (sans-serif, series convention) and shared objects
128:Form & May the producer lawfully leave? & Basis of the obligation & Is the person owned? & Who keeps the remainder? \\
130:Wage labor & Yes, subject to notice and contract & Contract, under law & No & The worker keeps the wage \\
131:Taxation & Yes, subject to emigration rules & Law, enforced by sanction & No & The taxpayer keeps income after tax \\
132:Serfdom & No, the producer is tied to land or lord & Custom and law, enforced by the lord and the state & No, though some regimes allowed sale with or without land & The household keeps output after dues and labor service \\
133:Compelled state labor & No, for the term of the draft or sentence & Sanction by the state & No & Little or nothing during the term \\
134:Chattel slavery & No & Ownership, enforced by the state & Yes & The owner \\
287:Case & Who produces and on what terms & Strongest counter-reading and reply \\
289:Ju/'hoansi \citep{lee1979,marshall1976} & Men and women forage, sharing rules distribute meat, and gift exchange links camps & No one commands labor. Reply: production is universal and its terms are policed by leveling talk \citep{wiessner2005} \\
290:Immediate-return foragers \citep{woodburn1982} & Food is consumed soon after it is obtained and accumulation is discouraged & Egalitarianism looks like the absence of power. Reply: it is produced by institutions of leveling \\
291:Nuer \citep{evanspritchard1940} & Herding, horticulture and fishing are organized by households and kin & Evans-Pritchard stressed the absence of government. Reply: cattle rights and exchange organize production without an office \\
292:Amazonian chiefs \citep{clastres1987} & Households garden and hunt, and the chief must give and work more & The flow runs from chief to group. Reply: this is a negative extraction share, not an absent function \\
293:Upland Southeast Asia \citep{scott2009} & Swidden farmers choose crops that are hard to tax & Producers evade the state. Reply: they produce and govern their own terms \\
294:Commons \citep{ostrom1990} & Users provide labor to maintain irrigation and other common resources & No state allocates labor. Reply: provision rules assign maintenance labor and are monitored \\
426:Regime type & Main producers and payers & Who sets the terms of participation & Concentration of control \\
428:Market-capitalist & Wage earners, small firms, consumers and taxpayers & Employers in labor markets and the state through tax and labor law & Varies by local market and is high in many \\
429:Communist party-state & State employees, collective farmers and, in the reform era, migrant workers & The party-state as employer, purchaser and owner & Near the maximum before reform \\
430:Social democracy and market socialism & Wage earners and the self-employed under encompassing bargaining & Unions, employers' associations and the state jointly & Moderate, with power shared by peak organizations \\
431:Islamic states & Ottoman peasants and guild artisans, Iranian workers, Gulf citizens and migrants & Intermediaries and guilds in the Ottoman case, the rentier state and sponsors in the Gulf & Moderate in the Ottoman case and high for Gulf migrants \\
432:Catholic monarchies & Peasants, artisans and colonial indigenous communities & Lords, the Church as landholder and tithe receiver, and the crown & High locally, shared among privileged estates \\
433:Secular democracies & Citizen taxpayers and wage earners & Legislatures, tax administrations and labor markets & Varies with the economic regime \\
445:Regime type & Principal couplings & Exit and voice & A documented check \\
447:Market-capitalist & Capital allocation and employment are held by the same actors & Job mobility, unions and the vote & Union wage compression in the mid-twentieth century \\
448:Communist party-state & One apparatus prices output, writes labor law, runs unions and polices mobility & Turnover, evasion, petitions and migration after reform & Shop-floor control of the pace of work by Soviet workers \\
449:Social democracy and market socialism & Corporatist bargaining joins producers and the legislature & Encompassing unions, elections and universal benefits & Universal programs that enlarged redistribution \\
450:Islamic states & Guilds joined crafts to administration, and rents join citizens to the state & Guild petitions, courts, strikes and quiet encroachment & Oil workers' strikes in the Iranian revolution \\
451:Catholic monarchies & The Church joined land, tithe and legitimation, and the crown joined tax and justice & Village litigation, the Cortes, flight and revolt & Burgundian villages contesting dues in royal courts \\
452:Secular democracies & Taxpayers and the franchise are joined in the same citizens & Elections, courts, unions and mass non-cooperation & Progressive taxation after wars of mass mobilization \\
661:Quantity & Indicator \\
663:Concentration $\HW$ & Herfindahl index of employment or vacancy shares in local labor markets, the state's share of employment, and the share of farm output sold to a single purchaser \\
664:Outside option $o$ & Rates of job-to-job transition, wage changes on switching employer, and the legal ability to change employer or residence \\
665:Mobility restriction $g$ & Statutes and practice on internal passports, residence permits tied to an employer, and debt or land ties \\
666:Organized weight $\eta$ & Union density, bargaining coverage, legality of strikes, and the independence of unions from the ruling party or employer \\
667:Rents and maintenance, $R$ and $K$ & Non-tax revenue relative to recurrent spending on administration, courts, security and public information \\
668:Producer dependence $\xi$ & Share of government revenue raised from domestic taxes and contributions \\
669:Participation gate $\gamma$ & Rules that condition employment, licenses, credit or market access on political or religious criteria, coded from statute and documented practice \\
670:Legal access $q^{\mathrm{leg}}$ & Availability, cost and independence of labor and tax adjudication, coded with the components of Part III, Definition 2.4 \\
671:Income protection $q^{\mathrm{inc}}$ & Replacement rates of unemployment, sickness and old-age insurance \\
672:Care labor $h$ and carers' fallback $o_h$ & Time-use surveys of unpaid care by sex, coverage of public childcare and paid leave, and women's property and divorce rights \\
688: & Basis & Prediction & Falsifier \\
690:HW1 & Source H5, Lemma~\ref{lem:productive-power:concentration} & Higher bargaining coverage weakens the association between employer concentration and lower pay & The concentration gradient is the same at high and low coverage \\
691:HW2 & Fiscal contract & Governments concede more services and representation where domestic taxes supply more revenue & No relation after conditioning on income, as some tests find \\
692:HW3 & Proposition~\ref{prop:productive-power:rentier} & The effect of rents on concessions to producers is largest where rents are close to the cost of running the state & The effect is uniform in the ratio of rents to maintenance or largest far from one \\
693:HW4 & Proposition~\ref{prop:productive-power:domar} & Bondage is more frequent where free exit is valuable and enforcement is cheap & Its incidence is unrelated to both across regions under comparable states \\
694:HW5 & Everyday resistance & Covert non-compliance rises where open voice is suppressed & Evasion and turnover are unrelated to repression of organization \\
695:HW6 & Insiders and outsiders & Contestability differs between permanent and precarious workers in encompassing welfare states & No difference in bargaining coverage or income protection between the groups \\
696:HW7 & Persistence & Compelled labor drafts leave lower consumption in affected districts long after abolition & Comparable drafts show no persistent effect at their boundaries \\
697:HW8 & Source H6 & Higher tax revenue with accountable provision goes with lower worker vulnerability & Vulnerability rises with provision \\
698:HW9 & Lemma~\ref{lem:productive-power:reproduction} and household bargaining & Unpaid care is shared more evenly where carers' fallback positions are stronger & The division of unpaid care is unrelated to property rights, paid employment and public care \\
46:\newcommand{\HW}{H_{\pW}}
89:The objects in this subsection are defined by \citet{largo2026hbs} and used throughout the series without redefinition. The polity at time $t$ is a directed multiplex network $G_t=(V_t,E_t)$ whose vertices are organizations or coherent actor groups. Each pillar $m$ in the index set $\Pill=\{\pF,\pP,\pJ,\pI,\pC,\pW\}$, with $M=|\Pill|=6$, contributes a layer with adjacency $A^m_t$ and edge weights $a^m_{ij,t}\in[0,1]$ that record the documented capacity of actor $i$ to constrain a feasible action of actor $j$ through mechanism $m$. The role map assigns each vertex a set of pillars, many to many. In pillar $m$, actor $i$ holds a control share $s^m_{i,t}$ with $\sum_i s^m_{i,t}=1$; concentration is the Herfindahl index $H_{m,t}=\sum_i (s^m_{i,t})^2$ and contestability is $Q_{m,t}\in[0,1]$. The illustrative unaccountable-concentration index is $U_t=\sum_m \omega_m H_{m,t}(1-Q_{m,t})$ with preregistered weights $\omega_m\ge 0$ summing to one. Cross-pillar integration $C_{mn,t}\in[0,1]$ measures the extent to which one coalition commands appointments, budgets, sanctions or agenda in both $m$ and $n$, and the integration statistic is $\Integ_t=\frac{2}{M(M-1)}\sum_{m<n}C_{mn,t}$ over fifteen pairs. A capture link $(i\to j,m)$ is an influence that gives privileged access or discretion, weakens otherwise applicable accountability or contestability, and is tied by material evidence to an institutional output. The state vector $x_t=(F_t,P_t,J_t,I^{\mathrm{cap}}_t,C_t,W_t)$ collects aggregate pillar capacities, with dynamics $x_{t+1}=B_tx_t+D_tz_t+\epsilon_t$.
91:Two conventions avoid clashes. Pillar labels are sans-serif, so $\pI$ is the ideological pillar and $\Integ_t$ is the integration statistic. No symbol for the wage is introduced; $W_t$ is the productive entry of the state vector and $\pW$ is the pillar label.
97:The \emph{maintenance function} of a collective is the set of activities that produce, pay for and reproduce the material means on which the collective and its institutions run. It includes paid and unpaid labor, cultivation and herding, craft and manufacture, extraction, trade that moves goods to where they are consumed, enterprise, the payment of taxes, tithes, tribute and dues, consumption that sustains producers and their enterprises, and the household work of care and child-rearing that reproduces the producers themselves. The productive pillar $\pW$ is the layer of $G_t$ in which these activities and the claims on them are organized.
104:Let $K_t$ be the \emph{institutional maintenance requirement}: the resources consumed in period $t$ by the institutions that realize the six functions, including the subsistence of their full-time personnel. Let $Z_t$ be the subsistence of all other members, and $K^{\mathrm{tot}}_t=Z_t+K_t$ the collective's total consumption. Let $X_t\ge 0$ be the stock of usable resources held by the collective at the start of period $t$ and $Y_t\ge 0$ the inflow of usable resources during $t$; the stock evolves as $X_{t+1}=X_t+Y_t-K^{\mathrm{tot}}_t$. The collective \emph{persists} on a horizon $\{0,\dots,T\}$ if $X_t\ge 0$ for every $t$ in the horizon, and persists indefinitely if this holds for every $T$. Within the stock, the institutions hold a part $X^S_t\ge 0$ (a treasury, granary or endowment) that receives the transfers $T_t$ from producers and any non-producer revenue $R_t$ and evolves as $X^S_{t+1}=X^S_t+T_t+R_t-K_t$; the institutions persist while $X^S_t\ge 0$.
109:A \emph{producer} is an agent whose activity in period $t$ contributes to $Y_t$, together with any agent who owns, operates or maintains equipment that does. In the stationary model of Section~\ref{sec:mechanisms} there are $n$ producers, each producing $y>0$ per period. A governing coalition $S$ receives a fraction $\chi$ of output (taxes, rents, dues, profits or procurement deliveries, net of services returned) and the producer retains $(1-\chi)y$. The coalition also receives \emph{non-producer revenue} $R_t\ge 0$ that does not come from its own producers: rents from resources sold abroad, tribute, foreign aid or remittances. In the stationary model the producers' transfer is $T_t=\chi ny$, and the coalition's \emph{producer dependence} is $\xi_t=T_t/(T_t+R_t)$.
148:The contestability of the productive pillar, $\QW_t:=Q_{\pW,t}$, is a preregistered aggregate of five components in $[0,1]$: bargaining coverage $q^{\mathrm{bar}}$ (the share of producers whose terms are set or reviewed collectively), mobility $q^{\mathrm{mob}}$ (lawful and practical ability to change employer, residence or occupation, including portability of benefits), legal access $q^{\mathrm{leg}}$ (access to independent adjudication of disputes over terms), income protection $q^{\mathrm{inc}}$ (replacement of income during unemployment, illness and old age), and voice $q^{\mathrm{voi}}$ (lawful ability to organize, strike, petition and vote over the terms of taxation).
153:The concentration $H_{\pW,t}$ is computed on shares of decision-relevant control over the terms of productive participation. In a labor market the natural proxy is the employment or vacancy share of each employer, which is how \citet{azar2022} measure labor-market concentration. Where the state is the dominant employer or the sole purchaser of farm output, its share approaches one. Where every household controls its own labor and land is open, shares are close to $1/n_h$ for $n_h$ households.
161:In each period a coalition $S$ governs $n$ identical producers. A participating producer produces $y>0$. The coalition and the producers agree on terms $u$, the per-producer value the producer retains (consumption plus the money value of services and concessions received); the extraction share is $\chi=1-u/y$, which is negative when producers receive net transfers. The coalition's revenue is $n(y-u)+R$, where $R\ge 0$ is non-producer revenue, and it must meet the institutional maintenance requirement $K>0$ of Definition~\ref{def:productive-power:persistence}. Producers' own subsistence is covered by $u$, so $K$ contains only the cost of the institutions. A producer who does not participate obtains the outside option $o$, with $y_0\le o\le y$, where $y_0$ is the autarky value of a producer cut off from exchange.
168:A \emph{mobility restriction} $g\in[0,1]$ is the probability that a producer who tries to leave is prevented: tying peasants to land, internal passports, residence permits tied to an employer. A \emph{participation gate} $\gamma\in[0,1]$ is the probability that a producer who withholds allegiance from the coalition retains access to exchange (buying inputs, selling output, credit, being hired); otherwise the producer falls to the autarky value $y_0$. Employment shares $s_j=s^{\pW}_j$ of employers $j=1,\dots,J$ define the concentration $\HW=\sum_j s_j^2$.
173:Let $o_1>y_0$ be the value of an offer from a competing employer. The outside option of a producer at employer $j$ is
175:o_j=y_0+\gamma\,(1-g)\,(1-s_j)\,(o_1-y_0),
177:and the employment-weighted mean outside option is $\bar o=\sum_j s_jo_j=y_0+\gamma(1-g)(1-\HW)(o_1-y_0)$.
180:Each factor of the composite form is a probability that the producer's exit succeeds: the producer is not blocked from leaving ($1-g$), keeps access to exchange ($\gamma$), and finds a different employer ($1-s_j$, justified in Lemma~\ref{lem:productive-power:concentration}). When an exit fails the producer receives the fallback $y_0$. Unrestricted producers facing many small employers obtain nearly $o_1$; a closed gate, a complete restriction or a single employer each holds them at $y_0$.
191:There are constants $k\ge k_S>0$ with $K^{\mathrm{tot}}_t\ge k$ and $K_t\ge k_S$ for every $t$: the group and its institutions consume resources in every period. The initial stocks $X_0$ and $X^S_0$ are finite.
198:Inflows are produced: $Y_t>0$ only if some agent, inside or outside the collective, performs productive activity in period $t$ or owns, operates or maintains equipment that does.
209:\frac{1}{T}\sum_{t=0}^{T-1}Y_t\;\ge\;k-\frac{X_0}{T},
215:Iterating the stock equation gives $X_T=X_0+\sum_{t<T}(Y_t-K^{\mathrm{tot}}_t)$. Persistence requires $X_T\ge 0$, hence $\sum_{t<T}Y_t\ge\sum_{t<T}K^{\mathrm{tot}}_t-X_0\ge Tk-X_0$. Dividing by $T$ gives the displayed bound, and its right side tends to $k$ as $T\to\infty$. If productive activity occurred in only finitely many periods, Assumption~\ref{ass:productive-power:nomanna} would make $Y_t=0$ from some period on, so $\sum_{t<T}Y_t$ would be bounded while $Tk-X_0$ grows without bound, a contradiction.
224:Split the inflow as $Y_t=Y^{\mathrm{in}}_t+Y^{\mathrm{out}}_t$, where $Y^{\mathrm{in}}_t$ is produced by members and $Y^{\mathrm{out}}_t$ by non-members and transferred to the collective. Under Assumptions~\ref{ass:productive-power:ax6} and~\ref{ass:productive-power:nomanna}, if a collective persists indefinitely and $Y^{\mathrm{in}}_t=0$ for all $t\ge t_0$, then non-members produce for the collective in infinitely many periods, and for every $T>t_0$ the transferred output satisfies $\sum_{t_0\le t<T}Y^{\mathrm{out}}_t\ge (T-t_0)k-X_{t_0}$.
228:Apply Lemma~\ref{thm:productive-power:necessity} to the collective from period $t_0$ with initial stock $X_{t_0}$, which is finite because each $X_t$ is finite. From $t_0$ on, $Y_t=Y^{\mathrm{out}}_t$, so the bound becomes the displayed inequality, and productive activity by non-members occurs in infinitely many periods.
239:Let the number of producers evolve as $n_{t+1}=(1-d)n_t+bh_t+m_t$, where $d\in(0,1]$ is the rate at which producers leave work through death, age or illness, $h_t\ge 0$ is care labor performed in period $t$, $b>0$ is the number of future producers sustained per unit of care, and $m_t\ge 0$ is the net arrival of producers raised elsewhere. If $h_t=m_t=0$ for all $t\ge t_0$, then $n_{t_0+j}=(1-d)^jn_{t_0}$, and members' output $n_ty$ falls below any fixed $k>0$ after finitely many periods. A collective that persists indefinitely on members' production therefore requires care labor, or the arrival of producers raised elsewhere, in infinitely many periods.
243:With $h_t=m_t=0$ the recursion is $n_{t+1}=(1-d)n_t$, whose solution is $(1-d)^jn_{t_0}$; this tends to zero because $0\le 1-d<1$, so $n_ty<k$ for all large $t$. If care and arrivals were zero from some period on, members' production would fall below $k$ from some period on, and Lemma~\ref{thm:productive-power:necessity} would require inflows produced by non-members, contradicting persistence on members' production.
246:The lemma puts unpaid household work inside the maintenance function on the same footing as paid work. It also shows a second form of relocation. A labor regime that imports adult migrants ($m_t>0$) draws on care performed in the migrants' places of origin, so the cost of reproducing its producers is borne outside the polity, as the cost of producing its rents is in Lemma~\ref{lem:productive-power:relocation}.
254:Suppose Assumption~\ref{ass:productive-power:ax6} holds, the institutions' non-producer revenue satisfies $R_t\le\bar r$ for all $t$ with $\bar r<k_S$, and from period $t_0$ on the producers withdraw completely, so that their transfers are $T_t=0$. Then the institutions fail to persist no later than period $t_0+\lfloor X^S_{t_0}/(k_S-\bar r)\rfloor+1$.
258:For $t\ge t_0$ the institutional stock of Definition~\ref{def:productive-power:persistence} satisfies $X^S_{t+1}=X^S_t+R_t-K_t\le X^S_t-(k_S-\bar r)$. After $j$ periods of withdrawal, $X^S_{t_0+j}\le X^S_{t_0}-j(k_S-\bar r)$, which is negative for the smallest integer $j$ exceeding $X^S_{t_0}/(k_S-\bar r)$, that is, for $j=\lfloor X^S_{t_0}/(k_S-\bar r)\rfloor+1$.
261:The proposition is elementary, and its content lies in what it rules out. No governance system whose non-producer revenue stays below its institutional maintenance requirement can survive the complete and permanent withdrawal of its producers. The producers therefore hold, collectively, a veto over persistence. The veto is latent because exercising it requires coordination that atomized producers lack \citep{olson1965}, because the coalition may meet withdrawal with coercion, and because the producers bear their own costs of withdrawal. Section~\ref{sec:mechanisms} prices these obstacles. When $R_t\ge K_t$ the bound fails, and the veto passes to whoever produces the rents (Lemma~\ref{lem:productive-power:relocation}).
339:Two conventions govern the comparison. Where market-capitalist and secular-democratic institutions coexist in one country, the first type is read through the organization of the economy (private capital, labor markets, the structural power of business) and the second through the political organization of the fiscal relation (citizen taxpayers, universal suffrage, social insurance law). Judgments of concentration are qualitative, because no country has been coded under a preregistered scheme, and no value of $U_t$ or $\Integ_t$ is reported.
345:The structural power of business is the distinctive coupling of this regime type. \citet{lindblom1977} argued that because investment decisions are private and governments depend on growth, business holds a privileged position that requires no organization: governments anticipate the reaction of investors. \citet{przeworski1985} drew the consequence for labor parties, which must sustain profits to sustain employment. This is the exit option of mobile capital, and \citet{bates1985} predicted that the owners of mobile assets obtain concessions. The coupling $C_{\pF\pW}$ is high wherever those who allocate capital also set the terms of employment. Part I gives the primary treatment of that pair in its Section 5.
413:The household's internal terms followed the same logic as the producers' terms elsewhere. \citet{kandiyoti1988} compared the household systems of sub-Saharan Africa with those she called classic patriarchy, found in a belt running from North Africa through the Middle East to South and East Asia, and showed that women bargained within each system according to its constraints. Her comparison concerns kinship and property systems, not religious doctrine, and it cuts across the regime types of this paper. \citet{laslett1989} trace the historical variation in how families, markets and states divided the work of reproduction. In the model's terms, these are differences in carers' fallback $o_h$ and standing $\eta_h$, set by property and family law in $\pP$ and $\pJ$ and by norms in $\pI$.
475:The exit floor is the whole of atomized producers' power. It is zero extraction when $o=y$, as in the band of Proposition~\ref{prop:productive-power:minimal-form}, and maximal extraction when $o=y_0$.
479:Suppose a producer who leaves employer $j$, and is neither blocked nor gated, receives one new offer, from employer $k$ with probability $s_k$; an offer from a different employer is worth $o_1$ and an offer from the employer just left is worth no more than the fallback $y_0<o_1$. Then the outside option at employer $j$ is the composite $o_j$ of Definition~\ref{def:productive-power:outside}, and the employment-weighted mean is $\bar o=y_0+\gamma(1-g)(1-\HW)(o_1-y_0)$. Under the exit floor, the employment-weighted mean extraction share is
481:\bar\chi=1-\frac{y_0+\gamma(1-g)(1-\HW)(o_1-y_0)}{y},
487:An exit succeeds with probability $\gamma(1-g)$; given success, the offer comes from a different employer with probability $1-s_j$. The expected value is $y_0+\gamma(1-g)(1-s_j)(o_1-y_0)=o_j$. Then $\sum_js_jo_j=y_0+\gamma(1-g)(o_1-y_0)\sum_j s_j(1-s_j)=y_0+\gamma(1-g)(1-\HW)(o_1-y_0)$, since $\sum_js_j=1$. Each employer sets $u_j=o_j$ by Lemma~\ref{lem:productive-power:exit-floor}, so $\chi_j=1-o_j/y$ and the weighted mean is $1-\bar o/y$.
490:The lemma gives the source's concentration index a mechanical role in this pillar. Under its assumptions, average extraction rises linearly with $\HW$, at a rate equal to the value of a competing offer relative to output. A single employer, $\HW=1$, holds every producer at the fallback; this is the company town, and in the limit it is the party-state as sole employer before reform. Many small employers, $\HW\to 0$, give unrestricted producers the competing value $o_1$. The association between labor-market concentration and lower wages found by \citet{azar2022} is consistent with the lemma, though random rematching simplifies search in real labor markets \citep{manning2003}.
496:V_S(T)=T+R-K-\psi\,(K-T-R)^+,\qquad (x)^+=\max(x,0).
508:Let producers bargain collectively with the coalition by the asymmetric Nash bargaining solution with producer weight $\eta\in[0,1]$, where disagreement gives producers $no$ and the coalition $V_S(0)=R-K-\psi(K-R)^+$. Under Assumption~\ref{ass:productive-power:feasible}, the agreed terms are
516:Write $\Psi=\psi(K-R)^+$ and $u_K=y-(K-R)^+/n$, the largest terms at which the coalition's revenue still covers $K$. For $u\le u_K$ the coalition's payoff is $V_S=n(y-u)+R-K$, which is linear; for $u>u_K$ it is lower by $\psi(K-n(y-u)-R)>0$. Consider first the linear problem, which maximizes $N(u)=(n(u-o))^{\eta}(n(y-u)+\Psi)^{1-\eta}$, the product of the gains $n(u-o)$ and $n(y-u)+R-K-V_S(0)=n(y-u)+\Psi$. For $0<\eta<1$ the logarithm of $N$ is strictly concave, and the first-order condition $\eta\,(n(y-u)+\Psi)=(1-\eta)\,n(u-o)$ gives $nu^*=\eta ny+(1-\eta)no+\eta\Psi$, the stated formula; for $\eta=0$ and $\eta=1$ the solution gives the whole gain to the coalition or to the producers, which the formula also covers. At $u^*$, $n(y-u^*)+R-K=n(1-\eta)(y-o)-\eta\Psi-(K-R)$, which is non-negative when $R\ge K$ (then $\Psi=0$) and, when $R<K$, equals $n(1-\eta)(y-o)-(1+\eta\psi)(K-R)\ge 0$ by Assumption~\ref{ass:productive-power:feasible}. So $u^*\le u_K$. The true Nash product with the payoff $V_S$ is never larger than $N(u)$ and equals it for $u\le u_K$. Hence $u^*$, which maximizes $N$ and lies where the two coincide, also maximizes the true Nash product.
523:Suppose each employer $j$ bargains with its own workers as in Proposition~\ref{prop:productive-power:voice}, with common weight $\eta$, common premium $\Omega$ and outside option $o_j$ from Definition~\ref{def:productive-power:outside}. Then the employment-weighted mean terms are $\bar u=\bar o+\eta(y-\bar o)+\Omega$, and
525:\frac{\partial\bar u}{\partial\HW}=-(1-\eta)\,\gamma\,(1-g)\,(o_1-y_0)\le 0 .
530:Averaging $u_j=o_j+\eta(y-o_j)+\Omega$ with weights $s_j$ gives $\bar u=(1-\eta)\bar o+\eta y+\Omega$. By Lemma~\ref{lem:productive-power:concentration}, $\partial\bar o/\partial\HW=-\gamma(1-g)(o_1-y_0)$, and the stated derivative follows.
535:The same bargaining logic applies inside the household, where most care labor is done. \citet{agarwal1997} argued that a household member's bargaining power depends on the fallback position available outside the household: property, paid employment, access to common resources, and support from kin, community or state. In the notation of the model, a carer's terms are $o_h+\eta_h(y_h-o_h)$, where $o_h$ is that fallback and $\eta_h$ the carer's organized or normative standing. Property rights, divorce law, public childcare and access to paid work all act on $o_h$. The paper does not develop the household game further, but the instruments that set $o_h$ are, like those in Assumption~\ref{ass:productive-power:instruments} below, held largely in $\pP$, $\pJ$ and $\pI$.
539:A coalition can lower the outside option directly by restricting mobility. Write $o(g)=y_0+(1-g)(o_0-y_0)$, where $o_0$ is the outside option at $g=0$ given by Definition~\ref{def:productive-power:outside}. Enforcement costs the coalition $\kappa(g)$ per producer, with $\kappa(0)=0$ and $\kappa$ increasing and convex.
543:Suppose the coalition chooses $g$ and then sets terms, with producers bargaining with weight $\eta\in[0,1)$ as in Proposition~\ref{prop:productive-power:voice} (the atomized case is $\eta=0$), and Assumption~\ref{ass:productive-power:feasible} holds at every $g$. Then the coalition's payoff, net of terms that do not depend on $g$, is $n[(1-\eta)g(o_0-y_0)-\kappa(g)]$.
545:\item[(a)] If $\kappa(g)=\kappa g$ is linear, restriction is chosen ($g^*=1$) when $(1-\eta)(o_0-y_0)>\kappa$ and not chosen ($g^*=0$) when $(1-\eta)(o_0-y_0)<\kappa$.
546:\item[(b)] If $\kappa$ is differentiable and strictly convex with $\kappa'(0)<(1-\eta)(o_0-y_0)<\kappa'(1)$, then $g^*\in(0,1)$ is the unique solution of $\kappa'(g^*)=(1-\eta)(o_0-y_0)$, and $g^*$ is increasing in $o_0-y_0$ and decreasing in $\eta$.
551:By Proposition~\ref{prop:productive-power:voice}, the producers' terms at outside option $o$ are $u^*=o+\eta(y-o)+\Omega$, where $\Omega$ does not depend on $o$, and the agreement leaves no shortfall, so the coalition's payoff from producers is $n(y-u^*)=n[(1-\eta)(y-o)-\Omega]$. Substituting $o(g)=o_0-g(o_0-y_0)$ gives $n[(1-\eta)(y-o_0)-\Omega]+n(1-\eta)g(o_0-y_0)$, and subtracting enforcement cost $n\kappa(g)$ leaves the stated $g$-dependent part. In case (a) the payoff is linear in $g$ with slope $n[(1-\eta)(o_0-y_0)-\kappa]$, so the optimum is at $g=1$ when the slope is positive and at $g=0$ when it is negative. In case (b) the payoff is strictly concave, its derivative is positive at $g=0$ and negative at $g=1$, so the unique maximizer satisfies the first-order condition. Because $\kappa'$ is strictly increasing, a larger right side $(1-\eta)(o_0-y_0)$ requires a larger $g^*$; the right side increases in $o_0-y_0$ and decreases in $\eta$.
554:The proposition places two classic explanations of bondage in one inequality. Domar's land-labor hypothesis concerns $o_0$: where land is abundant, a free peasant can leave and farm independently, so $o_0$ is high and binding the peasant pays \citep{domar1970}. Where land is scarce and labor abundant, $o_0$ is already close to $y_0$, the wage market holds producers near the floor, and restriction adds little. Brenner's objection concerns $\kappa$ and $\eta$: organized peasant communities raise the cost of enforcing restriction and bargain over terms, so the same land-labor ratio produced serfdom in one region and free tenure in another \citep{brenner1976}. The two accounts are not rivals in this form. They name different terms of the same condition, and the empirical question is which term varied more across the cases at issue.
579:Let $o$ denote the outside option at $\gamma=1$, so that under the gate of Definition~\ref{def:productive-power:gate} it is $o_\gamma=y_0+\gamma(o-y_0)$. Under Assumption~\ref{ass:productive-power:feasible}, the agreed terms are $u^*(\gamma)=o_\gamma+\eta(y-o_\gamma)+\Omega$, and
581:\frac{\partial u^*}{\partial\gamma}=(1-\eta)(o-y_0)\ge 0 .
583:If the gate is closed ($\gamma=0$), producers are atomized ($\eta=0$) and rents cover the maintenance requirement ($R\ge K$), producers are held at the autarky value, $u^*=y_0$, and the coalition takes $n(y-y_0)$.
587:Substitute $o_\gamma$ for $o$ in Proposition~\ref{prop:productive-power:voice}. Since $do_\gamma/d\gamma=o-y_0$ and $u^*$ depends on the outside option through $(1-\eta)o_\gamma$, the derivative follows. With $\gamma=0$, $o_\gamma=y_0$; with $\eta=0$, $\Omega=0$ and $u^*=o_\gamma=y_0$, and the coalition's revenue from producers is $n(y-y_0)$.
596:A \emph{productive capture link} is a capture link $(S\to j,\pW)$ in the sense of \citet{largo2026hbs} in which the privileged discretion held by $S$ is control over one of the parameters through which the production game sets producers' terms: their exit (through $g$ or the concentration $\HW$), their organization (through $\eta$), their access to exchange (through $\gamma$), or the coalition's exposure to their withdrawal (through non-producer revenue $R$ or the shortfall cost $\psi$). Material evidence must tie the exercise of that control to the terms $u$ or the extraction share $\chi$. The productive pillar is \emph{captured} at $t$ when productive capture links persist and the pillar's term $H_{\pW,t}(1-\QW_t)$ in $U_t$ is high.
608:Under Assumption~\ref{ass:productive-power:instruments}, any action by a coalition $S$ that lowers producers' terms $u^*$ below their value at the baseline parameters $(\HW^0,g=0,\eta_0,\gamma=1,R_0,\psi_0)$ is taken in at least one pillar $n\ne\pW$. Hence a captured productive pillar implies $C_{n\pW,t}>0$ for some $n\in\{\pF,\pP,\pI,\pC\}$, with $S$ the coalition in question.
612:By Proposition~\ref{prop:productive-power:voice}, Proposition~\ref{prop:productive-power:gate} and Lemma~\ref{lem:productive-power:concentration}, $u^*$ is non-decreasing in $o$, $\eta$, $\gamma$ and $\psi$ and non-increasing in $R$, with $o$ non-increasing in $g$ and $\HW$ by Definition~\ref{def:productive-power:outside}. Holding output $y$ and the maintenance requirement $K$ fixed, a reduction of $u^*$ therefore requires raising $g$ or $\HW$, lowering $\eta$, $\gamma$ or $\psi$, or raising $R$. By Assumption~\ref{ass:productive-power:instruments} each of these is exercised in a pillar other than $\pW$. If $S$ exercises it and also holds the terms of production, $S$ commands decisions in both $\pW$ and that pillar, which is $C_{n\pW,t}>0$.
672:Care labor $h$ and carers' fallback $o_h$ & Time-use surveys of unpaid care by sex, coverage of public childcare and paid leave, and women's property and divorce rights \\
729:A Marxian reader will object that production is not one pillar among six but the base on which the others rest, and that the framework flattens class relations into a network. The paper's own results partly concede the point. The latent veto gives production a status that no other pillar has: every other function consumes what this one supplies. But Proposition A asserts only that all six functions exist and depend on one another, not that they carry equal causal weight. Whether production determines the other pillars is a claim about the dependency matrix $B_t$, and it is an empirical question. Largo describes the framework as mid-range institutional theory that treats producers as active rather than as a passive base \citep{largo2026hbs}. The functional-explanation debate in Marxism \citep{cohen1978,elster1985} is a reminder that claims of determination need mechanisms, which is what the production game attempts to supply.

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '360,380p' papers/latex/productive-power.tex | nl -ba -v360" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   360	
   361	The reform era changed the instruments without removing them. Migration from the countryside expanded producers' outside options, and labor protest grew. \citet{lee2007} compared the protests of laid-off state-sector workers in the northeastern rustbelt with those of migrant workers in the southern export zones, who used the courts and labor law as well as street protest. The official union federation remains tied to the party, which limits voice outside party channels \citep{friedman2010}. Documented checks in this regime type are therefore mainly informal: evasion, turnover, petitioning, and the regime's own fear of unrest. That they existed matters for the comparison. Even under the most integrated arrangement in the record, the latent veto of Proposition~\ref{prop:productive-power:latent-veto} operated through everyday resistance.
   362	
   363	\subsection{Social democracy and market socialism}
   364	
   365	In the Nordic social democracies, producers are wage earners and the self-employed in market economies, but their terms are set to an unusual degree by collective bargaining at the national and sectoral level and by universal social insurance. Union density and bargaining coverage have been high by international standards for most of the postwar period. Power resources theory explains the arrangement as the result of the organization of wage earners in unions and their alliance with social democratic parties \citep{korpi1983,esping1985}. \citet{esping1990} measured its consequence as decommodification, the degree to which people can maintain a livelihood without relying on the labor market. \citet{huber2001} traced the development of the welfare state to partisan government over decades.
   366	
   367	The distinctive coupling here is between $\pW$ and $\pP$, through corporatist bargaining in which unions, employers and the state set wages and social policy together. By the source's own standard this coupling is not capture \citep{largo2026hbs}. It is a coalition commanding agenda in two pillars, and in this case its effect was to raise producers' contestability rather than to lower it. Corollary~\ref{cor:productive-power:coupling} formalizes the asymmetry: capture requires instruments that lower producers' terms, and corporatist coupling has mainly strengthened voice. Universalism also has a fiscal logic. \citet{korpi1998} found that universal programs redistribute more than targeted ones, because they build coalitions of support that enlarge the budget. \citet{rothstein1996} showed how the Swedish administrative model made universal programs implementable.
   368	
   369	The limits of the model are documented as well. \citet{przeworski1985} argued that social democratic parties remain structurally dependent on private investment, and \citet{pontusson1992} traced the failure of Swedish wage-earner funds, the most ambitious attempt to transfer ownership to labor. \citet{rueda2005} argued that social democratic parties have incentives to protect labor-market insiders rather than outsiders in temporary or precarious employment. That cleavage is a candidate failure mode inside the pillar: high $\QW$ for insiders can coexist with low $\QW$ for outsiders.
   370	
   371	Market socialism and workers' self-management are the variants of this regime type in which producers formally own the enterprise. \citet{kornai1992} argued that reform socialism in Hungary and Yugoslavia retained soft budget constraints and party control of appointments, which limited the autonomy of self-managed firms. Worker cooperatives in market economies are the small-scale analogue. \citet{dow2003} surveyed the theory and evidence on labor-managed firms, and \citet{craig1993} studied the objectives of worker cooperatives in the plywood industry of the Pacific Northwest. In the model, a cooperative raises producers' outside option, since it is an employer that the producers themselves control, and it removes extraction within the firm while leaving taxation to the state.
   372	
   373	\subsection{Islamic states}
   374	
   375	Islamic states share a source of political legitimacy, the claim to govern according to religious law, and differ in nearly every other respect. The comparison here covers the Ottoman Empire, modern Iran and Saudi Arabia, and the productive arrangements in each are not derived from Islamic law alone. Some instruments are legal categories of the tradition, such as alms taxes and land taxes. Others, such as tax farming or migrant sponsorship, are fiscal and labor-market institutions that belong to particular states and periods.
   376	
   377	In the Ottoman Empire, organized crafts gave producers a channel of voice. The taxpaying subjects were mainly peasants, artisans and merchants, and urban crafts were organized in guilds that regulated entry, prices and quality while also serving the state as administrative and fiscal intermediaries \citep{baer1970}. The guild was thus a site of coupling between $\pW$ and $\pP$: guilds petitioned authorities and brought disputes to the courts. Studies of Ottoman and early Republican workers document strikes and labor organization in the nineteenth and early twentieth centuries \citep{quataert1995}.
   378	
   379	Control over Ottoman producers' terms was dispersed among intermediaries. \citet{karaman2010} compared Ottoman state finances with those of European states and found that Ottoman revenue per capita remained low and collection decentralized, with heavy reliance on tax farming. \citet{barkey2008} described Ottoman rule as brokerage with intermediaries rather than direct command. In the vocabulary of this paper, control over the terms of production was dispersed among intermediaries, so $\HW$ was moderate. Ibn Khaldun had already observed that dynasties begin with low tax rates that yield large revenues and end with high rates that yield little, as producers withdraw effort \citep{khaldun1958}. The observation states the latent veto in fourteenth-century terms.
   380	

codex
Static checks found balanced braces/environments and no undefined internal labels or bibliography keys. To assess actual box warnings without reading any other project source, I’m checking whether an isolated LaTeX engine is available; if so, I’ll run it only against this file with outputs redirected outside the workspace.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'command -v pdflatex || true' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
/Library/TeX/texbin/pdflatex

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'review_tmp=$(mktemp -d /tmp/productive-power-review.XXXXXX)
cd "$review_tmp"
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error /Users/mlong/Documents/Development/the-beast-system/papers/latex/productive-power.tex >/dev/null
first_status=$?
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error /Users/mlong/Documents/Development/the-beast-system/papers/latex/productive-power.tex >/dev/null
second_status=$?
printf '"'PASSES %s %s\\n' \""'$first_status" "$second_status"
rg -n '"'("'^!|LaTeX Warning|Package .* Warning|Overfull|Underfull|Undefined control sequence|Fatal error)'"' \""'$review_tmp/productive-power.log" || true' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 190ms:
PASSES 1 1
rg: /productive-power.log: IO error for operation on /productive-power.log: No such file or directory (os error 2)

codex
The sandbox is fully read-only, so the isolated compile could not create even temporary `.aux`/`.log` files and did not run. I’m finishing with read-only linting and source-level layout checks; any box findings will be identified as risks rather than falsely presented as compiler-confirmed warnings.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "if command -v chktex >/dev/null 2>&1; then chktex -q -n1 -n8 -n13 -n24 -n36 papers/latex/productive-power.tex; else printf 'chktex unavailable\\n'; fi" in /Users/mlong/Documents/Development/the-beast-system
 exited 2 in 0ms:
Warning 38 in papers/latex/productive-power.tex line 68: You should not use punctuation in front of quotes.
The paper is Part VI of a seven-part series on the six functions that every governance system must perform. The series follows \citet{largo2026hbs}, who proposed a multiplex network model of five institutional functions under the name ``Hierarchy of the Beast System.'' The series splits Largo's rule function into rule-making and adjudication, giving six pillars: financial power $\pF$ (who controls the resources), political power $\pP$ (who makes the laws), judicial power $\pJ$ (who interprets the laws), ideological power $\pI$ (who shapes the beliefs), coercive power $\pC$ (who enforces the rules) and productive power $\pW$ (who produces the wealth that sustains everything). The thesis of the series is that the ideology changes and the institutional functions remain. ``Beast System'' names that universal six-function structure. It is never a label for a religion, a people, a profession, a regime or a person.  
                                                                                                                                                                                                                                                                          ^
Warning 3 in papers/latex/productive-power.tex line 89: You should enclose the previous parenthesis with `{}'.
The objects in this subsection are defined by \citet{largo2026hbs} and used throughout the series without redefinition. The polity at time $t$ is a directed multiplex network $G_t=(V_t,E_t)$ whose vertices are organizations or coherent actor groups. Each pillar $m$ in the index set $\Pill=\{\pF,\pP,\pJ,\pI,\pC,\pW\}$, with $M=|\Pill|=6$, contributes a layer with adjacency $A^m_t$ and edge weights $a^m_{ij,t}\in[0,1]$ that record the documented capacity of actor $i$ to constrain a feasible action of actor $j$ through mechanism $m$. The role map assigns each vertex a set of pillars, many to many. In pillar $m$, actor $i$ holds a control share $s^m_{i,t}$ with $\sum_i s^m_{i,t}=1$; concentration is the Herfindahl index $H_{m,t}=\sum_i (s^m_{i,t})^2$ and contestability is $Q_{m,t}\in[0,1]$. The illustrative unaccountable-concentration index is $U_t=\sum_m \omega_m H_{m,t}(1-Q_{m,t})$ with preregistered weights $\omega_m\ge 0$ summing to one. Cross-pillar integration $C_{mn,t}\in[0,1]$ measures the extent to which one coalition commands appointments, budgets, sanctions or agenda in both $m$ and $n$, and the integration statistic is $\Integ_t=\frac{2}{M(M-1)}\sum_{m<n}C_{mn,t}$ over fifteen pairs. A capture link $(i\to j,m)$ is an influence that gives privileged access or discretion, weakens otherwise applicable accountability or contestability, and is tied by material evidence to an institutional output. The state vector $x_t=(F_t,P_t,J_t,I^{\mathrm{cap}}_t,C_t,W_t)$ collects aggregate pillar capacities, with dynamics $x_{t+1}=B_tx_t+D_tz_t+\epsilon_t$.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ^
Warning 25 in papers/latex/productive-power.tex line 89: You might wish to put this between a pair of `{}'
The objects in this subsection are defined by \citet{largo2026hbs} and used throughout the series without redefinition. The polity at time $t$ is a directed multiplex network $G_t=(V_t,E_t)$ whose vertices are organizations or coherent actor groups. Each pillar $m$ in the index set $\Pill=\{\pF,\pP,\pJ,\pI,\pC,\pW\}$, with $M=|\Pill|=6$, contributes a layer with adjacency $A^m_t$ and edge weights $a^m_{ij,t}\in[0,1]$ that record the documented capacity of actor $i$ to constrain a feasible action of actor $j$ through mechanism $m$. The role map assigns each vertex a set of pillars, many to many. In pillar $m$, actor $i$ holds a control share $s^m_{i,t}$ with $\sum_i s^m_{i,t}=1$; concentration is the Herfindahl index $H_{m,t}=\sum_i (s^m_{i,t})^2$ and contestability is $Q_{m,t}\in[0,1]$. The illustrative unaccountable-concentration index is $U_t=\sum_m \omega_m H_{m,t}(1-Q_{m,t})$ with preregistered weights $\omega_m\ge 0$ summing to one. Cross-pillar integration $C_{mn,t}\in[0,1]$ measures the extent to which one coalition commands appointments, budgets, sanctions or agenda in both $m$ and $n$, and the integration statistic is $\Integ_t=\frac{2}{M(M-1)}\sum_{m<n}C_{mn,t}$ over fifteen pairs. A capture link $(i\to j,m)$ is an influence that gives privileged access or discretion, weakens otherwise applicable accountability or contestability, and is tied by material evidence to an institutional output. The state vector $x_t=(F_t,P_t,J_t,I^{\mathrm{cap}}_t,C_t,W_t)$ collects aggregate pillar capacities, with dynamics $x_{t+1}=B_tx_t+D_tz_t+\epsilon_t$.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ^^
Warning 25 in papers/latex/productive-power.tex line 89: You might wish to put this between a pair of `{}'
The objects in this subsection are defined by \citet{largo2026hbs} and used throughout the series without redefinition. The polity at time $t$ is a directed multiplex network $G_t=(V_t,E_t)$ whose vertices are organizations or coherent actor groups. Each pillar $m$ in the index set $\Pill=\{\pF,\pP,\pJ,\pI,\pC,\pW\}$, with $M=|\Pill|=6$, contributes a layer with adjacency $A^m_t$ and edge weights $a^m_{ij,t}\in[0,1]$ that record the documented capacity of actor $i$ to constrain a feasible action of actor $j$ through mechanism $m$. The role map assigns each vertex a set of pillars, many to many. In pillar $m$, actor $i$ holds a control share $s^m_{i,t}$ with $\sum_i s^m_{i,t}=1$; concentration is the Herfindahl index $H_{m,t}=\sum_i (s^m_{i,t})^2$ and contestability is $Q_{m,t}\in[0,1]$. The illustrative unaccountable-concentration index is $U_t=\sum_m \omega_m H_{m,t}(1-Q_{m,t})$ with preregistered weights $\omega_m\ge 0$ summing to one. Cross-pillar integration $C_{mn,t}\in[0,1]$ measures the extent to which one coalition commands appointments, budgets, sanctions or agenda in both $m$ and $n$, and the integration statistic is $\Integ_t=\frac{2}{M(M-1)}\sum_{m<n}C_{mn,t}$ over fifteen pairs. A capture link $(i\to j,m)$ is an influence that gives privileged access or discretion, weakens otherwise applicable accountability or contestability, and is tied by material evidence to an institutional output. The state vector $x_t=(F_t,P_t,J_t,I^{\mathrm{cap}}_t,C_t,W_t)$ collects aggregate pillar capacities, with dynamics $x_{t+1}=B_tx_t+D_tz_t+\epsilon_t$.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ^^
Warning 12 in papers/latex/productive-power.tex line 118: Interword spacing (`\ ') should perhaps be used.
A form of productive obligation is classified by the four criteria of Table~\ref{tab:bondage}. \emph{Wage labor} and \emph{taxation} leave lawful mobility and personal ownership with the producer. \emph{Serfdom} ties the producer to land or lord and compels dues or labor. \emph{Compelled state labor} (corv\'ee, labor drafts, penal labor) is compelled by sanction for a term. \emph{Chattel slavery} makes the person property. The word ``bondage'' is reserved for forms that legally restrict mobility and compel labor; wage labor and taxation are not called slavery in this paper.  
                                                                                              ^
Warning 12 in papers/latex/productive-power.tex line 118: Interword spacing (`\ ') should perhaps be used.
A form of productive obligation is classified by the four criteria of Table~\ref{tab:bondage}. \emph{Wage labor} and \emph{taxation} leave lawful mobility and personal ownership with the producer. \emph{Serfdom} ties the producer to land or lord and compels dues or labor. \emph{Compelled state labor} (corv\'ee, labor drafts, penal labor) is compelled by sanction for a term. \emph{Chattel slavery} makes the person property. The word ``bondage'' is reserved for forms that legally restrict mobility and compel labor; wage labor and taxation are not called slavery in this paper.  
                                                                                                                                                                                                    ^
Warning 12 in papers/latex/productive-power.tex line 118: Interword spacing (`\ ') should perhaps be used.
A form of productive obligation is classified by the four criteria of Table~\ref{tab:bondage}. \emph{Wage labor} and \emph{taxation} leave lawful mobility and personal ownership with the producer. \emph{Serfdom} ties the producer to land or lord and compels dues or labor. \emph{Compelled state labor} (corv\'ee, labor drafts, penal labor) is compelled by sanction for a term. \emph{Chattel slavery} makes the person property. The word ``bondage'' is reserved for forms that legally restrict mobility and compel labor; wage labor and taxation are not called slavery in this paper.  
                                                                                                                                                                                                                                                                                ^
Warning 12 in papers/latex/productive-power.tex line 118: Interword spacing (`\ ') should perhaps be used.
A form of productive obligation is classified by the four criteria of Table~\ref{tab:bondage}. \emph{Wage labor} and \emph{taxation} leave lawful mobility and personal ownership with the producer. \emph{Serfdom} ties the producer to land or lord and compels dues or labor. \emph{Compelled state labor} (corv\'ee, labor drafts, penal labor) is compelled by sanction for a term. \emph{Chattel slavery} makes the person property. The word ``bondage'' is reserved for forms that legally restrict mobility and compel labor; wage labor and taxation are not called slavery in this paper.  
                                                                                                                                                                                                                                                                                                                                                                                        ^
Warning 12 in papers/latex/productive-power.tex line 143: Interword spacing (`\ ') should perhaps be used.
A producer's \emph{outside option} $o$ is the per-period value available if the producer stops participating on the current terms: another employer, free land, migration, a subsistence plot, or a cooperative. \emph{Exit} is the exercise of that option. \emph{Voice} is collective or individual action to change the terms without leaving (petitions, lawsuits, strikes, tax refusal, boycotts, votes); its effectiveness in the model is the \emph{organized bargaining weight} $\eta\in[0,1]$, with $\eta=0$ for atomized producers. \emph{Loyalty} is attachment that raises the threshold at which a producer exits, which can make voice possible by keeping members inside long enough to use it \citep{hirschman1970}.  
                                                                                                                                                                                                                ^
Warning 12 in papers/latex/productive-power.tex line 143: Interword spacing (`\ ') should perhaps be used.
A producer's \emph{outside option} $o$ is the per-period value available if the producer stops participating on the current terms: another employer, free land, migration, a subsistence plot, or a cooperative. \emph{Exit} is the exercise of that option. \emph{Voice} is collective or individual action to change the terms without leaving (petitions, lawsuits, strikes, tax refusal, boycotts, votes); its effectiveness in the model is the \emph{organized bargaining weight} $\eta\in[0,1]$, with $\eta=0$ for atomized producers. \emph{Loyalty} is attachment that raises the threshold at which a producer exits, which can make voice possible by keeping members inside long enough to use it \citep{hirschman1970}.  
                                                                                                                                                                                                                                                            ^
Warning 12 in papers/latex/productive-power.tex line 143: Interword spacing (`\ ') should perhaps be used.
A producer's \emph{outside option} $o$ is the per-period value available if the producer stops participating on the current terms: another employer, free land, migration, a subsistence plot, or a cooperative. \emph{Exit} is the exercise of that option. \emph{Voice} is collective or individual action to change the terms without leaving (petitions, lawsuits, strikes, tax refusal, boycotts, votes); its effectiveness in the model is the \emph{organized bargaining weight} $\eta\in[0,1]$, with $\eta=0$ for atomized producers. \emph{Loyalty} is attachment that raises the threshold at which a producer exits, which can make voice possible by keeping members inside long enough to use it \citep{hirschman1970}.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             ^
Warning 25 in papers/latex/productive-power.tex line 177: You might wish to put this between a pair of `{}'
and the employment-weighted mean outside option is $\bar o=\sum_j s_jo_j=y_0+\gamma(1-g)(1-\HW)(o_1-y_0)$.  
                                                                    ^^
Warning 12 in papers/latex/productive-power.tex line 218: Interword spacing (`\ ') should perhaps be used.
The lemma establishes the existence of the activity, not of any institution that organizes it. Wage labor, serfdom, the household farm, the kolkhoz and the cooperative are alternative ways of implementing the same function. This is the distinction \citet{hempel1959} required of functional analysis: a functional requirement does not entail any particular institution, because functional equivalents may satisfy it. Nor does the lemma explain why a given regime has the productive institutions it has. \citet{elster1983} showed that explanation by beneficial consequences needs a feedback mechanism from the effect to the trait. The lemma is a condition of persistence, and it makes no causal claim about the origin of institutions.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ^
Warning 9 in papers/latex/productive-power.tex line 239: `)' expected, found `]'.
Let the number of producers evolve as $n_{t+1}=(1-d)n_t+bh_t+m_t$, where $d\in(0,1]$ is the rate at which producers leave work through death, age or illness, $h_t\ge 0$ is care labor performed in period $t$, $b>0$ is the number of future producers sustained per unit of care, and $m_t\ge 0$ is the net arrival of producers raised elsewhere. If $h_t=m_t=0$ for all $t\ge t_0$, then $n_{t_0+j}=(1-d)^jn_{t_0}$, and members' output $n_ty$ falls below any fixed $k>0$ after finitely many periods. A collective that persists indefinitely on members' production therefore requires care labor, or the arrival of producers raised elsewhere, in infinitely many periods.  
                                                                                  ^
Warning 3 in papers/latex/productive-power.tex line 239: You should enclose the previous parenthesis with `{}'.
Let the number of producers evolve as $n_{t+1}=(1-d)n_t+bh_t+m_t$, where $d\in(0,1]$ is the rate at which producers leave work through death, age or illness, $h_t\ge 0$ is care labor performed in period $t$, $b>0$ is the number of future producers sustained per unit of care, and $m_t\ge 0$ is the net arrival of producers raised elsewhere. If $h_t=m_t=0$ for all $t\ge t_0$, then $n_{t_0+j}=(1-d)^jn_{t_0}$, and members' output $n_ty$ falls below any fixed $k>0$ after finitely many periods. A collective that persists indefinitely on members' production therefore requires care labor, or the arrival of producers raised elsewhere, in infinitely many periods.  
                                                                                                                                                                                                                                                                                                                                                                                                            ^
Warning 25 in papers/latex/productive-power.tex line 239: You might wish to put this between a pair of `{}'
Let the number of producers evolve as $n_{t+1}=(1-d)n_t+bh_t+m_t$, where $d\in(0,1]$ is the rate at which producers leave work through death, age or illness, $h_t\ge 0$ is care labor performed in period $t$, $b>0$ is the number of future producers sustained per unit of care, and $m_t\ge 0$ is the net arrival of producers raised elsewhere. If $h_t=m_t=0$ for all $t\ge t_0$, then $n_{t_0+j}=(1-d)^jn_{t_0}$, and members' output $n_ty$ falls below any fixed $k>0$ after finitely many periods. A collective that persists indefinitely on members' production therefore requires care labor, or the arrival of producers raised elsewhere, in infinitely many periods.  
                                                                                                                                                                                                                                                                                                                                                                                                              ^^
Warning 25 in papers/latex/productive-power.tex line 239: You might wish to put this between a pair of `{}'
Let the number of producers evolve as $n_{t+1}=(1-d)n_t+bh_t+m_t$, where $d\in(0,1]$ is the rate at which producers leave work through death, age or illness, $h_t\ge 0$ is care labor performed in period $t$, $b>0$ is the number of future producers sustained per unit of care, and $m_t\ge 0$ is the net arrival of producers raised elsewhere. If $h_t=m_t=0$ for all $t\ge t_0$, then $n_{t_0+j}=(1-d)^jn_{t_0}$, and members' output $n_ty$ falls below any fixed $k>0$ after finitely many periods. A collective that persists indefinitely on members' production therefore requires care labor, or the arrival of producers raised elsewhere, in infinitely many periods.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                ^^
Warning 3 in papers/latex/productive-power.tex line 243: You should enclose the previous parenthesis with `{}'.
With $h_t=m_t=0$ the recursion is $n_{t+1}=(1-d)n_t$, whose solution is $(1-d)^jn_{t_0}$; this tends to zero because $0\le 1-d<1$, so $n_ty<k$ for all large $t$. If care and arrivals were zero from some period on, members' production would fall below $k$ from some period on, and Lemma~\ref{thm:productive-power:necessity} would require inflows produced by non-members, contradicting persistence on members' production.  
                                                                             ^
Warning 25 in papers/latex/productive-power.tex line 243: You might wish to put this between a pair of `{}'
With $h_t=m_t=0$ the recursion is $n_{t+1}=(1-d)n_t$, whose solution is $(1-d)^jn_{t_0}$; this tends to zero because $0\le 1-d<1$, so $n_ty<k$ for all large $t$. If care and arrivals were zero from some period on, members' production would fall below $k$ from some period on, and Lemma~\ref{thm:productive-power:necessity} would require inflows produced by non-members, contradicting persistence on members' production.  
                                                                               ^^
Warning 25 in papers/latex/productive-power.tex line 243: You might wish to put this between a pair of `{}'
With $h_t=m_t=0$ the recursion is $n_{t+1}=(1-d)n_t$, whose solution is $(1-d)^jn_{t_0}$; this tends to zero because $0\le 1-d<1$, so $n_ty<k$ for all large $t$. If care and arrivals were zero from some period on, members' production would fall below $k$ from some period on, and Lemma~\ref{thm:productive-power:necessity} would require inflows produced by non-members, contradicting persistence on members' production.  
                                                                                                                                         ^^
Warning 12 in papers/latex/productive-power.tex line 299: Interword spacing (`\ ') should perhaps be used.
Among the Ju/'hoansi, production by both sexes is the basis of daily life, and the terms on which its results circulate are governed by sharing rules, gift partnerships and talk \citep{lee1979,lee2013,marshall1976}. \citet{wiessner2005} documented how the Ju/'hoansi enforce such norms, largely through criticism and talk rather than physical punishment. In the vocabulary of this paper, open access and costless fission keep $o$ close to $y$, and leveling sanctions keep it there. \citet{woodburn1982} generalized the point: in immediate-return societies equality is an achievement of institutions that prevent accumulation, not a default. \citet{boehm1999} called the same pattern a reverse dominance hierarchy, in which the group as a coalition dominates would-be dominants.  
                                                                                                                                                                                                                       ^
Warning 12 in papers/latex/productive-power.tex line 299: Interword spacing (`\ ') should perhaps be used.
Among the Ju/'hoansi, production by both sexes is the basis of daily life, and the terms on which its results circulate are governed by sharing rules, gift partnerships and talk \citep{lee1979,lee2013,marshall1976}. \citet{wiessner2005} documented how the Ju/'hoansi enforce such norms, largely through criticism and talk rather than physical punishment. In the vocabulary of this paper, open access and costless fission keep $o$ close to $y$, and leveling sanctions keep it there. \citet{woodburn1982} generalized the point: in immediate-return societies equality is an achievement of institutions that prevent accumulation, not a default. \citet{boehm1999} called the same pattern a reverse dominance hierarchy, in which the group as a coalition dominates would-be dominants.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ^
Warning 12 in papers/latex/productive-power.tex line 299: Interword spacing (`\ ') should perhaps be used.
Among the Ju/'hoansi, production by both sexes is the basis of daily life, and the terms on which its results circulate are governed by sharing rules, gift partnerships and talk \citep{lee1979,lee2013,marshall1976}. \citet{wiessner2005} documented how the Ju/'hoansi enforce such norms, largely through criticism and talk rather than physical punishment. In the vocabulary of this paper, open access and costless fission keep $o$ close to $y$, and leveling sanctions keep it there. \citet{woodburn1982} generalized the point: in immediate-return societies equality is an achievement of institutions that prevent accumulation, not a default. \citet{boehm1999} called the same pattern a reverse dominance hierarchy, in which the group as a coalition dominates would-be dominants.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ^
Warning 12 in papers/latex/productive-power.tex line 322: Interword spacing (`\ ') should perhaps be used.
The second body of work locates producers' power in their options and their organization. Hirschman's exit, voice and loyalty frame the options of members of any organization in decline \citep{hirschman1970}. \citet{freeman1984} applied the frame to trade unions, which have a monopoly face that raises wages and a collective-voice face that lets workers change conditions without quitting. \citet{wright2000} distinguished associational power, which comes from organization in unions and parties, from structural power, which comes from workers' position in tight labor markets or strategic sectors. \citet{silver2003} used the distinction to trace labor unrest across a century of relocating industries.  
                                                                                                                                                                                                                ^
Warning 12 in papers/latex/productive-power.tex line 322: Interword spacing (`\ ') should perhaps be used.
The second body of work locates producers' power in their options and their organization. Hirschman's exit, voice and loyalty frame the options of members of any organization in decline \citep{hirschman1970}. \citet{freeman1984} applied the frame to trade unions, which have a monopoly face that raises wages and a collective-voice face that lets workers change conditions without quitting. \citet{wright2000} distinguished associational power, which comes from organization in unions and parties, from structural power, which comes from workers' position in tight labor markets or strategic sectors. \citet{silver2003} used the distinction to trace labor unrest across a century of relocating industries.  
                                                                                                                                                                                                                                                                                                                                                                                                      ^
Warning 12 in papers/latex/productive-power.tex line 322: Interword spacing (`\ ') should perhaps be used.
The second body of work locates producers' power in their options and their organization. Hirschman's exit, voice and loyalty frame the options of members of any organization in decline \citep{hirschman1970}. \citet{freeman1984} applied the frame to trade unions, which have a monopoly face that raises wages and a collective-voice face that lets workers change conditions without quitting. \citet{wright2000} distinguished associational power, which comes from organization in unions and parties, from structural power, which comes from workers' position in tight labor markets or strategic sectors. \citet{silver2003} used the distinction to trace labor unrest across a century of relocating industries.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ^
Warning 12 in papers/latex/productive-power.tex line 326: Interword spacing (`\ ') should perhaps be used.
The third body of work is fiscal sociology, which treats the tax relation as the core of state formation \citep{campbell1993,martin2009}. \citet{levi1988} modeled rulers as revenue maximizers constrained by their bargaining power relative to constituents, by transaction costs and by their discount rates, and showed that compliance is quasi-voluntary: taxpayers comply when they believe others do and the ruler keeps bargains. \citet{bates1985} argued that owners of mobile assets can extract representative concessions. \citet{ross2004} tested the claim that taxation leads to representation and found that the relevant variable is taxation relative to the services government provides, and \citet{timmons2005} found that governments trade services for revenue with the groups that pay.  
                                                                                                                                         ^
Warning 12 in papers/latex/productive-power.tex line 326: Interword spacing (`\ ') should perhaps be used.
The third body of work is fiscal sociology, which treats the tax relation as the core of state formation \citep{campbell1993,martin2009}. \citet{levi1988} modeled rulers as revenue maximizers constrained by their bargaining power relative to constituents, by transaction costs and by their discount rates, and showed that compliance is quasi-voluntary: taxpayers comply when they believe others do and the ruler keeps bargains. \citet{bates1985} argued that owners of mobile assets can extract representative concessions. \citet{ross2004} tested the claim that taxation leads to representation and found that the relevant variable is taxation relative to the services government provides, and \citet{timmons2005} found that governments trade services for revenue with the groups that pay.  
                                                                                                                                                                                                                                                                                                                                                                                                                                           ^
Warning 12 in papers/latex/productive-power.tex line 326: Interword spacing (`\ ') should perhaps be used.
The third body of work is fiscal sociology, which treats the tax relation as the core of state formation \citep{campbell1993,martin2009}. \citet{levi1988} modeled rulers as revenue maximizers constrained by their bargaining power relative to constituents, by transaction costs and by their discount rates, and showed that compliance is quasi-voluntary: taxpayers comply when they believe others do and the ruler keeps bargains. \citet{bates1985} argued that owners of mobile assets can extract representative concessions. \citet{ross2004} tested the claim that taxation leads to representation and found that the relevant variable is taxation relative to the services government provides, and \citet{timmons2005} found that governments trade services for revenue with the groups that pay.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ^
Warning 12 in papers/latex/productive-power.tex line 328: Interword spacing (`\ ') should perhaps be used.
Rentier-state theory supplies the converse: revenue that does not come from domestic taxpayers frees rulers from bargaining with them \citep{mahdavy1970,beblawiluciani1987,ross2001}. The converse is contested. \citet{habermenaldo2011} find no evidence that resource reliance promotes authoritarianism over time within countries. Part I \citep{long2026financial} treats rents (its Section 5) on the allocation side; this Part treats them as a change in producers' bargaining position.  
                                                                                                                                                                                                                 ^
Warning 12 in papers/latex/productive-power.tex line 330: Interword spacing (`\ ') should perhaps be used.
The fourth body of work explains when producers are bound. \citet{domar1970} proposed that serfdom or slavery arises where land is abundant relative to labor, because free peasants could otherwise leave to farm free land, and that free land, free peasants and non-working landowners cannot coexist. \citet{brenner1976} answered that the outcomes of the late-medieval demographic crisis differed across Europe with the same land-labor ratios, and that the balance of organized class power decided them. \citet{dell2010} showed that the Spanish colonial mining draft in Peru left lower household consumption and worse child health in the districts subject to it, centuries after its abolition. \citet{scott1976,scott1985} showed that peasants who cannot exit or speak openly resist through foot-dragging, evasion and gossip, and that they judge extraction against a subsistence ethic.  
                                                          ^
Warning 12 in papers/latex/productive-power.tex line 330: Interword spacing (`\ ') should perhaps be used.
The fourth body of work explains when producers are bound. \citet{domar1970} proposed that serfdom or slavery arises where land is abundant relative to labor, because free peasants could otherwise leave to farm free land, and that free land, free peasants and non-working landowners cannot coexist. \citet{brenner1976} answered that the outcomes of the late-medieval demographic crisis differed across Europe with the same land-labor ratios, and that the balance of organized class power decided them. \citet{dell2010} showed that the Spanish colonial mining draft in Peru left lower household consumption and worse child health in the districts subject to it, centuries after its abolition. \citet{scott1976,scott1985} showed that peasants who cannot exit or speak openly resist through foot-dragging, evasion and gossip, and that they judge extraction against a subsistence ethic.  
                                                                                                                                                                                                                                                                                                          ^
Warning 12 in papers/latex/productive-power.tex line 330: Interword spacing (`\ ') should perhaps be used.
The fourth body of work explains when producers are bound. \citet{domar1970} proposed that serfdom or slavery arises where land is abundant relative to labor, because free peasants could otherwise leave to farm free land, and that free land, free peasants and non-working landowners cannot coexist. \citet{brenner1976} answered that the outcomes of the late-medieval demographic crisis differed across Europe with the same land-labor ratios, and that the balance of organized class power decided them. \citet{dell2010} showed that the Spanish colonial mining draft in Peru left lower household consumption and worse child health in the districts subject to it, centuries after its abolition. \citet{scott1976,scott1985} showed that peasants who cannot exit or speak openly resist through foot-dragging, evasion and gossip, and that they judge extraction against a subsistence ethic.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ^
Warning 12 in papers/latex/productive-power.tex line 330: Interword spacing (`\ ') should perhaps be used.
The fourth body of work explains when producers are bound. \citet{domar1970} proposed that serfdom or slavery arises where land is abundant relative to labor, because free peasants could otherwise leave to farm free land, and that free land, free peasants and non-working landowners cannot coexist. \citet{brenner1976} answered that the outcomes of the late-medieval demographic crisis differed across Europe with the same land-labor ratios, and that the balance of organized class power decided them. \citet{dell2010} showed that the Spanish colonial mining draft in Peru left lower household consumption and worse child health in the districts subject to it, centuries after its abolition. \citet{scott1976,scott1985} showed that peasants who cannot exit or speak openly resist through foot-dragging, evasion and gossip, and that they judge extraction against a subsistence ethic.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ^
Warning 12 in papers/latex/productive-power.tex line 343: Interword spacing (`\ ') should perhaps be used.
In market-capitalist societies most producers are wage earners, the self-employed and small businesses, and the terms of production are set mainly by employers in labor markets and by the state through tax and labor law. Consumers sustain enterprises by their purchases and pay a large share of indirect taxes. The holders of the pillar are therefore many, but control over terms is not evenly spread. \citet{azar2022} found that a large share of local labor markets in the United States are highly concentrated by the standard used in antitrust, and that concentration is associated with lower posted wages. Monopsony theory explains why: when moving between employers is costly, employers set wages below the competitive level \citep{manning2003}. In the notation of this paper, $\HW$ varies across local markets and is high in many of them.  
                                                                                                                                                                                                                                                                                                                                                                                                                 ^
Warning 12 in papers/latex/productive-power.tex line 345: Interword spacing (`\ ') should perhaps be used.
The structural power of business is the distinctive coupling of this regime type. \citet{lindblom1977} argued that because investment decisions are private and governments depend on growth, business holds a privileged position that requires no organization: governments anticipate the reaction of investors. \citet{przeworski1985} drew the consequence for labor parties, which must sustain profits to sustain employment. This is the exit option of mobile capital, and \citet{bates1985} predicted that the owners of mobile assets obtain concessions. The coupling $C_{\pF\pW}$ is high wherever those who allocate capital also set the terms of employment. Part I gives the primary treatment of that pair in its Section 5.  
                                                                                 ^
Warning 12 in papers/latex/productive-power.tex line 345: Interword spacing (`\ ') should perhaps be used.
The structural power of business is the distinctive coupling of this regime type. \citet{lindblom1977} argued that because investment decisions are private and governments depend on growth, business holds a privileged position that requires no organization: governments anticipate the reaction of investors. \citet{przeworski1985} drew the consequence for labor parties, which must sustain profits to sustain employment. This is the exit option of mobile capital, and \citet{bates1985} predicted that the owners of mobile assets obtain concessions. The coupling $C_{\pF\pW}$ is high wherever those who allocate capital also set the terms of employment. Part I gives the primary treatment of that pair in its Section 5.  
                                                                                                                                                                                                                                                                                                                   ^
Warning 12 in papers/latex/productive-power.tex line 347: Interword spacing (`\ ') should perhaps be used.
Accountability in the pillar has rested on three channels: collective bargaining, labor mobility and the vote. Their strength has varied over time. \citet{farber2021} assembled survey data across the twentieth century and found that unions compressed the income distribution when they were strong. \citet{western2011} attributed a substantial part of the rise in American wage inequality after the 1970s to the decline of unions, including through the erosion of norms of fair pay in non-union firms. \citet{piketty2018} documented the same period's shift of pre-tax income toward the top of the distribution. These are documented changes in $q^{\mathrm{bar}}$ and $q^{\mathrm{voi}}$, not evidence of capture by themselves. A decline in bargaining coverage can follow from changes in industry composition and trade as well as from employer action and law.  
                                                                                                                                                   ^
Warning 12 in papers/latex/productive-power.tex line 347: Interword spacing (`\ ') should perhaps be used.
Accountability in the pillar has rested on three channels: collective bargaining, labor mobility and the vote. Their strength has varied over time. \citet{farber2021} assembled survey data across the twentieth century and found that unions compressed the income distribution when they were strong. \citet{western2011} attributed a substantial part of the rise in American wage inequality after the 1970s to the decline of unions, including through the erosion of norms of fair pay in non-union firms. \citet{piketty2018} documented the same period's shift of pre-tax income toward the top of the distribution. These are documented changes in $q^{\mathrm{bar}}$ and $q^{\mathrm{voi}}$, not evidence of capture by themselves. A decline in bargaining coverage can follow from changes in industry composition and trade as well as from employer action and law.  
                                                                                                                                                                                                                                                                                                         ^
Warning 12 in papers/latex/productive-power.tex line 347: Interword spacing (`\ ') should perhaps be used.
Accountability in the pillar has rested on three channels: collective bargaining, labor mobility and the vote. Their strength has varied over time. \citet{farber2021} assembled survey data across the twentieth century and found that unions compressed the income distribution when they were strong. \citet{western2011} attributed a substantial part of the rise in American wage inequality after the 1970s to the decline of unions, including through the erosion of norms of fair pay in non-union firms. \citet{piketty2018} documented the same period's shift of pre-tax income toward the top of the distribution. These are documented changes in $q^{\mathrm{bar}}$ and $q^{\mathrm{voi}}$, not evidence of capture by themselves. A decline in bargaining coverage can follow from changes in industry composition and trade as well as from employer action and law.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ^
Warning 12 in papers/latex/productive-power.tex line 349: Interword spacing (`\ ') should perhaps be used.
Documented checks are visible in the same record. Union contracts, minimum-wage laws, antitrust enforcement in labor markets and the expansion of social insurance in the twentieth century all raised producers' terms through voice. \citet{polanyi1944} treated the protective legislation of the nineteenth century as the countermovement of a society defending itself against the commodification of labor. Documented capture is harder to establish than decline. The source's capture-link criterion requires material evidence linking privileged access to an output \citep{largo2026hbs}. Accounts of how organized business reshaped American labor and tax policy from the 1970s \citep{hackerpierson2010} supply candidate links, and they remain contested in the way Part II \citep{long2026political} describes in its Section 5.2 for the wider literature on unequal political responsiveness.  
                                                                                                                                                                                                                                      ^
Warning 12 in papers/latex/productive-power.tex line 361: Interword spacing (`\ ') should perhaps be used.
The reform era changed the instruments without removing them. Migration from the countryside expanded producers' outside options, and labor protest grew. \citet{lee2007} compared the protests of laid-off state-sector workers in the northeastern rustbelt with those of migrant workers in the southern export zones, who used the courts and labor law as well as street protest. The official union federation remains tied to the party, which limits voice outside party channels \citep{friedman2010}. Documented checks in this regime type are therefore mainly informal: evasion, turnover, petitioning, and the regime's own fear of unrest. That they existed matters for the comparison. Even under the most integrated arrangement in the record, the latent veto of Proposition~\ref{prop:productive-power:latent-veto} operated through everyday resistance.  
                                                                                                                                                         ^
Warning 12 in papers/latex/productive-power.tex line 365: Interword spacing (`\ ') should perhaps be used.
In the Nordic social democracies, producers are wage earners and the self-employed in market economies, but their terms are set to an unusual degree by collective bargaining at the national and sectoral level and by universal social insurance. Union density and bargaining coverage have been high by international standards for most of the postwar period. Power resources theory explains the arrangement as the result of the organization of wage earners in unions and their alliance with social democratic parties \citep{korpi1983,esping1985}. \citet{esping1990} measured its consequence as decommodification, the degree to which people can maintain a livelihood without relying on the labor market. \citet{huber2001} traced the development of the welfare state to partisan government over decades.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ^
Warning 12 in papers/latex/productive-power.tex line 365: Interword spacing (`\ ') should perhaps be used.
In the Nordic social democracies, producers are wage earners and the self-employed in market economies, but their terms are set to an unusual degree by collective bargaining at the national and sectoral level and by universal social insurance. Union density and bargaining coverage have been high by international standards for most of the postwar period. Power resources theory explains the arrangement as the result of the organization of wage earners in unions and their alliance with social democratic parties \citep{korpi1983,esping1985}. \citet{esping1990} measured its consequence as decommodification, the degree to which people can maintain a livelihood without relying on the labor market. \citet{huber2001} traced the development of the welfare state to partisan government over decades.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ^
Warning 12 in papers/latex/productive-power.tex line 367: Interword spacing (`\ ') should perhaps be used.
The distinctive coupling here is between $\pW$ and $\pP$, through corporatist bargaining in which unions, employers and the state set wages and social policy together. By the source's own standard this coupling is not capture \citep{largo2026hbs}. It is a coalition commanding agenda in two pillars, and in this case its effect was to raise producers' contestability rather than to lower it. Corollary~\ref{cor:productive-power:coupling} formalizes the asymmetry: capture requires instruments that lower producers' terms, and corporatist coupling has mainly strengthened voice. Universalism also has a fiscal logic. \citet{korpi1998} found that universal programs redistribute more than targeted ones, because they build coalitions of support that enlarge the budget. \citet{rothstein1996} showed how the Swedish administrative model made universal programs implementable.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ^
Warning 12 in papers/latex/productive-power.tex line 367: Interword spacing (`\ ') should perhaps be used.
The distinctive coupling here is between $\pW$ and $\pP$, through corporatist bargaining in which unions, employers and the state set wages and social policy together. By the source's own standard this coupling is not capture \citep{largo2026hbs}. It is a coalition commanding agenda in two pillars, and in this case its effect was to raise producers' contestability rather than to lower it. Corollary~\ref{cor:productive-power:coupling} formalizes the asymmetry: capture requires instruments that lower producers' terms, and corporatist coupling has mainly strengthened voice. Universalism also has a fiscal logic. \citet{korpi1998} found that universal programs redistribute more than targeted ones, because they build coalitions of support that enlarge the budget. \citet{rothstein1996} showed how the Swedish administrative model made universal programs implementable.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ^
Warning 12 in papers/latex/productive-power.tex line 369: Interword spacing (`\ ') should perhaps be used.
The limits of the model are documented as well. \citet{przeworski1985} argued that social democratic parties remain structurally dependent on private investment, and \citet{pontusson1992} traced the failure of Swedish wage-earner funds, the most ambitious attempt to transfer ownership to labor. \citet{rueda2005} argued that social democratic parties have incentives to protect labor-market insiders rather than outsiders in temporary or precarious employment. That cleavage is a candidate failure mode inside the pillar: high $\QW$ for insiders can coexist with low $\QW$ for outsiders.  
                                               ^
Warning 12 in papers/latex/productive-power.tex line 369: Interword spacing (`\ ') should perhaps be used.
The limits of the model are documented as well. \citet{przeworski1985} argued that social democratic parties remain structurally dependent on private investment, and \citet{pontusson1992} traced the failure of Swedish wage-earner funds, the most ambitious attempt to transfer ownership to labor. \citet{rueda2005} argued that social democratic parties have incentives to protect labor-market insiders rather than outsiders in temporary or precarious employment. That cleavage is a candidate failure mode inside the pillar: high $\QW$ for insiders can coexist with low $\QW$ for outsiders.  
                                                                                                                                                                                                                                                                                                       ^
Warning 12 in papers/latex/productive-power.tex line 371: Interword spacing (`\ ') should perhaps be used.
Market socialism and workers' self-management are the variants of this regime type in which producers formally own the enterprise. \citet{kornai1992} argued that reform socialism in Hungary and Yugoslavia retained soft budget constraints and party control of appointments, which limited the autonomy of self-managed firms. Worker cooperatives in market economies are the small-scale analogue. \citet{dow2003} surveyed the theory and evidence on labor-managed firms, and \citet{craig1993} studied the objectives of worker cooperatives in the plywood industry of the Pacific Northwest. In the model, a cooperative raises producers' outside option, since it is an employer that the producers themselves control, and it removes extraction within the firm while leaving taxation to the state.  
                                                                                                                                  ^
Warning 12 in papers/latex/productive-power.tex line 371: Interword spacing (`\ ') should perhaps be used.
Market socialism and workers' self-management are the variants of this regime type in which producers formally own the enterprise. \citet{kornai1992} argued that reform socialism in Hungary and Yugoslavia retained soft budget constraints and party control of appointments, which limited the autonomy of self-managed firms. Worker cooperatives in market economies are the small-scale analogue. \citet{dow2003} surveyed the theory and evidence on labor-managed firms, and \citet{craig1993} studied the objectives of worker cooperatives in the plywood industry of the Pacific Northwest. In the model, a cooperative raises producers' outside option, since it is an employer that the producers themselves control, and it removes extraction within the firm while leaving taxation to the state.  
                                                                                                                                                                                                                                                                                                                                                                                                        ^
Warning 12 in papers/latex/productive-power.tex line 379: Interword spacing (`\ ') should perhaps be used.
Control over Ottoman producers' terms was dispersed among intermediaries. \citet{karaman2010} compared Ottoman state finances with those of European states and found that Ottoman revenue per capita remained low and collection decentralized, with heavy reliance on tax farming. \citet{barkey2008} described Ottoman rule as brokerage with intermediaries rather than direct command. In the vocabulary of this paper, control over the terms of production was dispersed among intermediaries, so $\HW$ was moderate. Ibn Khaldun had already observed that dynasties begin with low tax rates that yield large revenues and end with high rates that yield little, as producers withdraw effort \citep{khaldun1958}. The observation states the latent veto in fourteenth-century terms.  
                                                                         ^
Warning 12 in papers/latex/productive-power.tex line 379: Interword spacing (`\ ') should perhaps be used.
Control over Ottoman producers' terms was dispersed among intermediaries. \citet{karaman2010} compared Ottoman state finances with those of European states and found that Ottoman revenue per capita remained low and collection decentralized, with heavy reliance on tax farming. \citet{barkey2008} described Ottoman rule as brokerage with intermediaries rather than direct command. In the vocabulary of this paper, control over the terms of production was dispersed among intermediaries, so $\HW$ was moderate. Ibn Khaldun had already observed that dynasties begin with low tax rates that yield large revenues and end with high rates that yield little, as producers withdraw effort \citep{khaldun1958}. The observation states the latent veto in fourteenth-century terms.  
                                                                                                                                                                                                                                                                                    ^
Warning 12 in papers/latex/productive-power.tex line 381: Interword spacing (`\ ') should perhaps be used.
Islamic legal categories of taxation and charity, including the alms tax and endowments, shaped the fiscal relation and the provision of welfare. \citet{singer2008} surveyed charity in Islamic societies, including endowed public kitchens in the Ottoman Empire. The economic consequences of Islamic commercial law are debated. \citet{kuran2011} argued that rules of partnership, inheritance and endowment held back the formation of durable private enterprises in the Middle East; \citet{rubin2017} attributed divergence instead to the way rulers relied on religious authorities for legitimacy, and \citet{pamuk2000} offered a monetary and fiscal history that does not reduce Ottoman outcomes to law.  
                                                                                                                                                 ^
Warning 12 in papers/latex/productive-power.tex line 381: Interword spacing (`\ ') should perhaps be used.
Islamic legal categories of taxation and charity, including the alms tax and endowments, shaped the fiscal relation and the provision of welfare. \citet{singer2008} surveyed charity in Islamic societies, including endowed public kitchens in the Ottoman Empire. The economic consequences of Islamic commercial law are debated. \citet{kuran2011} argued that rules of partnership, inheritance and endowment held back the formation of durable private enterprises in the Middle East; \citet{rubin2017} attributed divergence instead to the way rulers relied on religious authorities for legitimacy, and \citet{pamuk2000} offered a monetary and fiscal history that does not reduce Ottoman outcomes to law.  
                                                                                                                                                                                                                                                                                                                                     ^
Warning 12 in papers/latex/productive-power.tex line 383: Interword spacing (`\ ') should perhaps be used.
Modern Iran shows producers' power at both extremes. Oil workers' strikes were central to the revolution of 1978 to 1979, and workers' councils briefly took over the management of factories before the new regime absorbed or suppressed them \citep{bayat1987}. In the following decades the urban poor pursued what \citet{bayat1997} called the quiet encroachment of the ordinary: unorganized, cumulative claims on land, services and public space. \citet{mahdavy1970} coined the concept of the rentier state using the Iranian case: oil revenue reduces the state's need to tax, and with it the bargaining weight of taxpayers.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                           ^
Warning 7 in papers/latex/productive-power.tex line 395: Accent command `\'' needs use of `\i'.
In Castile, communal lands and municipal institutions mattered to peasant livelihoods \citep{vassberg1984}, and ordinary people litigated in large numbers in the royal courts \citep{kagan1981}. The Cortes bargained with the crown over new taxes, and the taxes paid by Castilian producers sustained the crown's borrowing \citep{drelichman2014}. In the Americas the same monarchy organized compelled state labor. The Potos\'i mining draft required indigenous communities in designated districts to send a share of their men to the mines, and \citet{dell2010} found persistent lower consumption and child growth in those districts today. In the Papal States, the pope was both temporal sovereign and head of the Church, which made the coupling of $\pI$ with fiscal administration direct \citep{prodi1987}.  
                                                                                                                                                                                                                                                                                                                                                                                                                                    ^^
Warning 12 in papers/latex/productive-power.tex line 401: Interword spacing (`\ ') should perhaps be used.
In secular democracies, the citizen is a taxpayer and a voter at once, and the fiscal relation is the most general channel through which producers affect the state. The fiscal contract argument holds that states which depend on taxes must bargain with taxpayers, and that the bargain produces representation and services \citep{bates1985,moore2004,timmons2005}. Evidence for the link is conditional. \citet{ross2004} found that it is the cost of government relative to the services provided, rather than the level of taxation alone, that predicts democratization. \citet{levi1988} found that compliance in established democracies is quasi-voluntary: it depends on taxpayers' belief that others pay and that the government keeps its side of the bargain.  
                                                                                                                                                                                                                                                                                                                                                                                                               ^
Warning 12 in papers/latex/productive-power.tex line 401: Interword spacing (`\ ') should perhaps be used.
In secular democracies, the citizen is a taxpayer and a voter at once, and the fiscal relation is the most general channel through which producers affect the state. The fiscal contract argument holds that states which depend on taxes must bargain with taxpayers, and that the bargain produces representation and services \citep{bates1985,moore2004,timmons2005}. Evidence for the link is conditional. \citet{ross2004} found that it is the cost of government relative to the services provided, rather than the level of taxation alone, that predicts democratization. \citet{levi1988} found that compliance in established democracies is quasi-voluntary: it depends on taxpayers' belief that others pay and that the government keeps its side of the bargain.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ^
Warning 12 in papers/latex/productive-power.tex line 403: Interword spacing (`\ ') should perhaps be used.
The modern tax state depends on fiscal capacity, the ability to tax incomes broadly, which \citet{besley2011,besley2013} treat as an investment that states make when they expect common-interest spending such as defense. \citet{scheve2016} found that steeply progressive taxation in the twentieth century followed wars of mass mobilization, in which arguments that the wealthy should compensate for the sacrifices of conscripts proved persuasive, rather than following the extension of the franchise alone. This is the latent veto at work in a democratic register: those who supplied the soldiers and the war production obtained fiscal concessions.  
                                                                                                                                                                                                                           ^
Warning 12 in papers/latex/productive-power.tex line 405: Interword spacing (`\ ') should perhaps be used.
The working class appears in the comparative-historical literature as a force for democratization. \citet{rueschemeyer1992} argued that organized workers were the most consistent supporters of full democracy, against landlords and often against the bourgeoisie. Voice in secular democracies therefore includes the franchise, unions and the courts, and \citet{chenoweth2011} found that, in their data on twentieth-century campaigns, nonviolent campaigns relying on mass non-cooperation, including strikes and boycotts, succeeded more often than violent ones. Welfare regimes differ within this regime type. \citet{esping1990} classified liberal, conservative and social democratic regimes, and the liberal regime offers the weakest income protection.  
                                                                                                  ^
Warning 12 in papers/latex/productive-power.tex line 405: Interword spacing (`\ ') should perhaps be used.
The working class appears in the comparative-historical literature as a force for democratization. \citet{rueschemeyer1992} argued that organized workers were the most consistent supporters of full democracy, against landlords and often against the bourgeoisie. Voice in secular democracies therefore includes the franchise, unions and the courts, and \citet{chenoweth2011} found that, in their data on twentieth-century campaigns, nonviolent campaigns relying on mass non-cooperation, including strikes and boycotts, succeeded more often than violent ones. Welfare regimes differ within this regime type. \citet{esping1990} classified liberal, conservative and social democratic regimes, and the liberal regime offers the weakest income protection.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             ^
Warning 12 in papers/latex/productive-power.tex line 413: Interword spacing (`\ ') should perhaps be used.
The household's internal terms followed the same logic as the producers' terms elsewhere. \citet{kandiyoti1988} compared the household systems of sub-Saharan Africa with those she called classic patriarchy, found in a belt running from North Africa through the Middle East to South and East Asia, and showed that women bargained within each system according to its constraints. Her comparison concerns kinship and property systems, not religious doctrine, and it cuts across the regime types of this paper. \citet{laslett1989} trace the historical variation in how families, markets and states divided the work of reproduction. In the model's terms, these are differences in carers' fallback $o_h$ and standing $\eta_h$, set by property and family law in $\pP$ and $\pJ$ and by norms in $\pI$.  
                                                                                         ^
Warning 12 in papers/latex/productive-power.tex line 413: Interword spacing (`\ ') should perhaps be used.
The household's internal terms followed the same logic as the producers' terms elsewhere. \citet{kandiyoti1988} compared the household systems of sub-Saharan Africa with those she called classic patriarchy, found in a belt running from North Africa through the Middle East to South and East Asia, and showed that women bargained within each system according to its constraints. Her comparison concerns kinship and property systems, not religious doctrine, and it cuts across the regime types of this paper. \citet{laslett1989} trace the historical variation in how families, markets and states divided the work of reproduction. In the model's terms, these are differences in carers' fallback $o_h$ and standing $\eta_h$, set by property and family law in $\pP$ and $\pJ$ and by norms in $\pI$.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ^
Warning 25 in papers/latex/productive-power.tex line 487: You might wish to put this between a pair of `{}'
An exit succeeds with probability $\gamma(1-g)$; given success, the offer comes from a different employer with probability $1-s_j$. The expected value is $y_0+\gamma(1-g)(1-s_j)(o_1-y_0)=o_j$. Then $\sum_js_jo_j=y_0+\gamma(1-g)(o_1-y_0)\sum_j s_j(1-s_j)=y_0+\gamma(1-g)(1-\HW)(o_1-y_0)$, since $\sum_js_j=1$. Each employer sets $u_j=o_j$ by Lemma~\ref{lem:productive-power:exit-floor}, so $\chi_j=1-o_j/y$ and the weighted mean is $1-\bar o/y$.  
                                                                                                                                                                                                            ^^
Warning 25 in papers/latex/productive-power.tex line 487: You might wish to put this between a pair of `{}'
An exit succeeds with probability $\gamma(1-g)$; given success, the offer comes from a different employer with probability $1-s_j$. The expected value is $y_0+\gamma(1-g)(1-s_j)(o_1-y_0)=o_j$. Then $\sum_js_jo_j=y_0+\gamma(1-g)(o_1-y_0)\sum_j s_j(1-s_j)=y_0+\gamma(1-g)(1-\HW)(o_1-y_0)$, since $\sum_js_j=1$. Each employer sets $u_j=o_j$ by Lemma~\ref{lem:productive-power:exit-floor}, so $\chi_j=1-o_j/y$ and the weighted mean is $1-\bar o/y$.  
                                                                                                                                                                                                               ^^
Warning 25 in papers/latex/productive-power.tex line 487: You might wish to put this between a pair of `{}'
An exit succeeds with probability $\gamma(1-g)$; given success, the offer comes from a different employer with probability $1-s_j$. The expected value is $y_0+\gamma(1-g)(1-s_j)(o_1-y_0)=o_j$. Then $\sum_js_jo_j=y_0+\gamma(1-g)(o_1-y_0)\sum_j s_j(1-s_j)=y_0+\gamma(1-g)(1-\HW)(o_1-y_0)$, since $\sum_js_j=1$. Each employer sets $u_j=o_j$ by Lemma~\ref{lem:productive-power:exit-floor}, so $\chi_j=1-o_j/y$ and the weighted mean is $1-\bar o/y$.  
                                                                                                                                                                                                                                                                                                            ^^
Warning 3 in papers/latex/productive-power.tex line 496: You should enclose the previous parenthesis with `{}'.
V_S(T)=T+R-K-\psi\,(K-T-R)^+,\qquad (x)^+=\max(x,0).  
                         ^
Warning 3 in papers/latex/productive-power.tex line 496: You should enclose the previous parenthesis with `{}'.
V_S(T)=T+R-K-\psi\,(K-T-R)^+,\qquad (x)^+=\max(x,0).  
                                      ^
Warning 3 in papers/latex/productive-power.tex line 501: You should enclose the previous parenthesis with `{}'.
The parameters satisfy $n(1-\eta)(y-o)\ge(1+\eta\psi)(K-R)^+$.  
                                                         ^
Warning 3 in papers/latex/productive-power.tex line 508: You should enclose the previous parenthesis with `{}'.
Let producers bargain collectively with the coalition by the asymmetric Nash bargaining solution with producer weight $\eta\in[0,1]$, where disagreement gives producers $no$ and the coalition $V_S(0)=R-K-\psi(K-R)^+$. Under Assumption~\ref{ass:productive-power:feasible}, the agreed terms are  
                                                                                                                                                                                                                    ^
Warning 3 in papers/latex/productive-power.tex line 510: You should enclose the previous parenthesis with `{}'.
u^*=o+\eta(y-o)+\Omega,\qquad \Omega=\frac{\eta\,\psi\,(K-R)^+}{n},  
                                                           ^
Warning 3 in papers/latex/productive-power.tex line 516: You should enclose the previous parenthesis with `{}'.
Write $\Psi=\psi(K-R)^+$ and $u_K=y-(K-R)^+/n$, the largest terms at which the coalition's revenue still covers $K$. For $u\le u_K$ the coalition's payoff is $V_S=n(y-u)+R-K$, which is linear; for $u>u_K$ it is lower by $\psi(K-n(y-u)-R)>0$. Consider first the linear problem, which maximizes $N(u)=(n(u-o))^{\eta}(n(y-u)+\Psi)^{1-\eta}$, the product of the gains $n(u-o)$ and $n(y-u)+R-K-V_S(0)=n(y-u)+\Psi$. For $0<\eta<1$ the logarithm of $N$ is strictly concave, and the first-order condition $\eta\,(n(y-u)+\Psi)=(1-\eta)\,n(u-o)$ gives $nu^*=\eta ny+(1-\eta)no+\eta\Psi$, the stated formula; for $\eta=0$ and $\eta=1$ the solution gives the whole gain to the coalition or to the producers, which the formula also covers. At $u^*$, $n(y-u^*)+R-K=n(1-\eta)(y-o)-\eta\Psi-(K-R)$, which is non-negative when $R\ge K$ (then $\Psi=0$) and, when $R<K$, equals $n(1-\eta)(y-o)-(1+\eta\psi)(K-R)\ge 0$ by Assumption~\ref{ass:productive-power:feasible}. So $u^*\le u_K$. The true Nash product with the payoff $V_S$ is never larger than $N(u)$ and equals it for $u\le u_K$. Hence $u^*$, which maximizes $N$ and lies where the two coincide, also maximizes the true Nash product.  
                    ^
Warning 3 in papers/latex/productive-power.tex line 516: You should enclose the previous parenthesis with `{}'.
Write $\Psi=\psi(K-R)^+$ and $u_K=y-(K-R)^+/n$, the largest terms at which the coalition's revenue still covers $K$. For $u\le u_K$ the coalition's payoff is $V_S=n(y-u)+R-K$, which is linear; for $u>u_K$ it is lower by $\psi(K-n(y-u)-R)>0$. Consider first the linear problem, which maximizes $N(u)=(n(u-o))^{\eta}(n(y-u)+\Psi)^{1-\eta}$, the product of the gains $n(u-o)$ and $n(y-u)+R-K-V_S(0)=n(y-u)+\Psi$. For $0<\eta<1$ the logarithm of $N$ is strictly concave, and the first-order condition $\eta\,(n(y-u)+\Psi)=(1-\eta)\,n(u-o)$ gives $nu^*=\eta ny+(1-\eta)no+\eta\Psi$, the stated formula; for $\eta=0$ and $\eta=1$ the solution gives the whole gain to the coalition or to the producers, which the formula also covers. At $u^*$, $n(y-u^*)+R-K=n(1-\eta)(y-o)-\eta\Psi-(K-R)$, which is non-negative when $R\ge K$ (then $\Psi=0$) and, when $R<K$, equals $n(1-\eta)(y-o)-(1+\eta\psi)(K-R)\ge 0$ by Assumption~\ref{ass:productive-power:feasible}. So $u^*\le u_K$. The true Nash product with the payoff $V_S$ is never larger than $N(u)$ and equals it for $u\le u_K$. Hence $u^*$, which maximizes $N$ and lies where the two coincide, also maximizes the true Nash product.  
                                        ^
Warning 3 in papers/latex/productive-power.tex line 516: You should enclose the previous parenthesis with `{}'.
Write $\Psi=\psi(K-R)^+$ and $u_K=y-(K-R)^+/n$, the largest terms at which the coalition's revenue still covers $K$. For $u\le u_K$ the coalition's payoff is $V_S=n(y-u)+R-K$, which is linear; for $u>u_K$ it is lower by $\psi(K-n(y-u)-R)>0$. Consider first the linear problem, which maximizes $N(u)=(n(u-o))^{\eta}(n(y-u)+\Psi)^{1-\eta}$, the product of the gains $n(u-o)$ and $n(y-u)+R-K-V_S(0)=n(y-u)+\Psi$. For $0<\eta<1$ the logarithm of $N$ is strictly concave, and the first-order condition $\eta\,(n(y-u)+\Psi)=(1-\eta)\,n(u-o)$ gives $nu^*=\eta ny+(1-\eta)no+\eta\Psi$, the stated formula; for $\eta=0$ and $\eta=1$ the solution gives the whole gain to the coalition or to the producers, which the formula also covers. At $u^*$, $n(y-u^*)+R-K=n(1-\eta)(y-o)-\eta\Psi-(K-R)$, which is non-negative when $R\ge K$ (then $\Psi=0$) and, when $R<K$, equals $n(1-\eta)(y-o)-(1+\eta\psi)(K-R)\ge 0$ by Assumption~\ref{ass:productive-power:feasible}. So $u^*\le u_K$. The true Nash product with the payoff $V_S$ is never larger than $N(u)$ and equals it for $u\le u_K$. Hence $u^*$, which maximizes $N$ and lies where the two coincide, also maximizes the true Nash product.  
                                                                                                                                                                                                                                                                                                                  ^
Warning 3 in papers/latex/productive-power.tex line 516: You should enclose the previous parenthesis with `{}'.
Write $\Psi=\psi(K-R)^+$ and $u_K=y-(K-R)^+/n$, the largest terms at which the coalition's revenue still covers $K$. For $u\le u_K$ the coalition's payoff is $V_S=n(y-u)+R-K$, which is linear; for $u>u_K$ it is lower by $\psi(K-n(y-u)-R)>0$. Consider first the linear problem, which maximizes $N(u)=(n(u-o))^{\eta}(n(y-u)+\Psi)^{1-\eta}$, the product of the gains $n(u-o)$ and $n(y-u)+R-K-V_S(0)=n(y-u)+\Psi$. For $0<\eta<1$ the logarithm of $N$ is strictly concave, and the first-order condition $\eta\,(n(y-u)+\Psi)=(1-\eta)\,n(u-o)$ gives $nu^*=\eta ny+(1-\eta)no+\eta\Psi$, the stated formula; for $\eta=0$ and $\eta=1$ the solution gives the whole gain to the coalition or to the producers, which the formula also covers. At $u^*$, $n(y-u^*)+R-K=n(1-\eta)(y-o)-\eta\Psi-(K-R)$, which is non-negative when $R\ge K$ (then $\Psi=0$) and, when $R<K$, equals $n(1-\eta)(y-o)-(1+\eta\psi)(K-R)\ge 0$ by Assumption~\ref{ass:productive-power:feasible}. So $u^*\le u_K$. The true Nash product with the payoff $V_S$ is never larger than $N(u)$ and equals it for $u\le u_K$. Hence $u^*$, which maximizes $N$ and lies where the two coincide, also maximizes the true Nash product.  
                                                                                                                                                                                                                                                                                                                                      ^
Warning 12 in papers/latex/productive-power.tex line 535: Interword spacing (`\ ') should perhaps be used.
The same bargaining logic applies inside the household, where most care labor is done. \citet{agarwal1997} argued that a household member's bargaining power depends on the fallback position available outside the household: property, paid employment, access to common resources, and support from kin, community or state. In the notation of the model, a carer's terms are $o_h+\eta_h(y_h-o_h)$, where $o_h$ is that fallback and $\eta_h$ the carer's organized or normative standing. Property rights, divorce law, public childcare and access to paid work all act on $o_h$. The paper does not develop the household game further, but the instruments that set $o_h$ are, like those in Assumption~\ref{ass:productive-power:instruments} below, held largely in $\pP$, $\pJ$ and $\pI$.  
                                                                                      ^
Warning 9 in papers/latex/productive-power.tex line 543: `]' expected, found `)'.
Suppose the coalition chooses $g$ and then sets terms, with producers bargaining with weight $\eta\in[0,1)$ as in Proposition~\ref{prop:productive-power:voice} (the atomized case is $\eta=0$), and Assumption~\ref{ass:productive-power:feasible} holds at every $g$. Then the coalition's payoff, net of terms that do not depend on $g$, is $n[(1-\eta)g(o_0-y_0)-\kappa(g)]$.  
                                                                                                         ^
Warning 3 in papers/latex/productive-power.tex line 566: You should enclose the previous parenthesis with `{}'.
$\Omega=\eta\psi(K-R)^+/n$. For $R<K$ its derivative in $R$ is $-\eta\psi/n\le 0$; for $R\ge K$ it is identically zero. The other two terms, $o$ and $\eta(y-o)$, contain no $R$. Raising $R$ relaxes Assumption~\ref{ass:productive-power:feasible}, so the result stays within its scope.  
                    ^
Warning 38 in papers/latex/productive-power.tex line 716: You should not use punctuation in front of quotes.
The passage most directly relevant to this pillar is Revelation 13:16-17 (KJV): ``And he causeth all, both small and great, rich and poor, free and bond, to receive a mark in their right hand, or in their foreheads: And that no man might buy or sell, save he that had the mark, or the name of the beast, or the number of his name.'' The verse does not describe a form of labor. It describes a condition on participation in exchange. Its scope runs across every category of the social order, ``free and bond'' included, so the condition is not the bondage of a class but the gating of everyone's access to buying and selling by a sign of allegiance.  
                                                                                                                                                                                                                                                                                                                                         ^
Warning 12 in papers/latex/productive-power.tex line 720: Interword spacing (`\ ') should perhaps be used.
The preterist anchor gives the image economic content. \citet{kraybill1996} argued that participation in the maritime trade and trade guilds of Asia Minor entangled Christians in the imperial cult, and that John's vision calls them to withdraw from commerce on those terms. \citet{bauckham1991} read the lament over Babylon in Revelation 18 as an economic critique of Rome. The cargo list of 18:11-13 runs through luxury goods and ends with ``slaves, and souls of men,'' an indictment of a trade that included human beings. This is literal chattel slavery in the Roman economy. It is the extreme of Table~\ref{tab:bondage} and must not be read as a metaphor for wage labor or taxation. The list also illustrates the relocation lemma: the goods that sustained the imperial center were produced across the provinces and beyond them, and the kings, merchants and shipmasters who lament Babylon's fall (18:9-19) are those whose wealth depended on that flow.  
                                                      ^
Warning 12 in papers/latex/productive-power.tex line 720: Interword spacing (`\ ') should perhaps be used.
The preterist anchor gives the image economic content. \citet{kraybill1996} argued that participation in the maritime trade and trade guilds of Asia Minor entangled Christians in the imperial cult, and that John's vision calls them to withdraw from commerce on those terms. \citet{bauckham1991} read the lament over Babylon in Revelation 18 as an economic critique of Rome. The cargo list of 18:11-13 runs through luxury goods and ends with ``slaves, and souls of men,'' an indictment of a trade that included human beings. This is literal chattel slavery in the Roman economy. It is the extreme of Table~\ref{tab:bondage} and must not be read as a metaphor for wage labor or taxation. The list also illustrates the relocation lemma: the goods that sustained the imperial center were produced across the provinces and beyond them, and the kings, merchants and shipmasters who lament Babylon's fall (18:9-19) are those whose wealth depended on that flow.  
                                                                                                                                                                                                                                                                                 ^
Warning 38 in papers/latex/productive-power.tex line 720: You should not use punctuation in front of quotes.
The preterist anchor gives the image economic content. \citet{kraybill1996} argued that participation in the maritime trade and trade guilds of Asia Minor entangled Christians in the imperial cult, and that John's vision calls them to withdraw from commerce on those terms. \citet{bauckham1991} read the lament over Babylon in Revelation 18 as an economic critique of Rome. The cargo list of 18:11-13 runs through luxury goods and ends with ``slaves, and souls of men,'' an indictment of a trade that included human beings. This is literal chattel slavery in the Roman economy. It is the extreme of Table~\ref{tab:bondage} and must not be read as a metaphor for wage labor or taxation. The list also illustrates the relocation lemma: the goods that sustained the imperial center were produced across the provinces and beyond them, and the kings, merchants and shipmasters who lament Babylon's fall (18:9-19) are those whose wealth depended on that flow.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ^
Warning 12 in papers/latex/productive-power.tex line 722: Interword spacing (`\ ') should perhaps be used.
The text's response to the gate has the shape of Hirschman's triad, though it was written for different purposes. The imperative ``Come out of her, my people'' (18:4) is a call to exit. Faithful witness (11:3-13) and the ``patience and the faith of the saints'' (13:10) are a form of voice that refuses the demanded loyalty. Loyalty itself is the contested object: the vision depicts a demand for worship, and the faithful are those who give their allegiance elsewhere. \citet{rossing1999} read the contrast between Babylon and the New Jerusalem as a choice between two cities, with an economic critique of imperial Rome at its center. \citet{wink1992} generalized the beast into a domination system present in institutions of every age, a reading congenial to the series' claim that the structure is universal.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ^
Warning 12 in papers/latex/productive-power.tex line 722: Interword spacing (`\ ') should perhaps be used.
The text's response to the gate has the shape of Hirschman's triad, though it was written for different purposes. The imperative ``Come out of her, my people'' (18:4) is a call to exit. Faithful witness (11:3-13) and the ``patience and the faith of the saints'' (13:10) are a form of voice that refuses the demanded loyalty. Loyalty itself is the contested object: the vision depicts a demand for worship, and the faithful are those who give their allegiance elsewhere. \citet{rossing1999} read the contrast between Babylon and the New Jerusalem as a choice between two cities, with an economic critique of imperial Rome at its center. \citet{wink1992} generalized the beast into a domination system present in institutions of every age, a reading congenial to the series' claim that the structure is universal.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ^
Warning 12 in papers/latex/productive-power.tex line 724: Interword spacing (`\ ') should perhaps be used.
The analogy has limits that must be stated. Revelation is apocalyptic literature, and its resolution is divine judgment, not producers' bargaining. \citet{collins1984} argued that the book addresses a crisis that was partly perceived, written to produce catharsis in its readers, and \citet{thompson1990} questioned the extent of persecution under Domitian. The verses supply an image of the limiting case of capture in this pillar, and the model supplies the conditions under which that limit is approached. Neither depends on the other. The analytic claims of this paper stand without the theological reading, and the reading identifies no present institution with the beast.  
                                                                                                                                                   ^
Warning 12 in papers/latex/productive-power.tex line 733: Interword spacing (`\ ') should perhaps be used.
A functionalist objection runs the other way: the paper may have explained the existence of production by its usefulness. It has not. Lemma~\ref{thm:productive-power:necessity} is a condition of persistence. It says that persistent collectives produce, not that their productive institutions exist because they help the collective persist. This is the standard of \citet{hempel1959} and \citet{elster1983}, and the series adopts it throughout. \citet{merton1968} supplies the further point that functional alternatives exist: the same function is met by foraging bands, serf villages, kolkhozes and labor markets.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                           ^
Warning 12 in papers/latex/productive-power.tex line 756: Interword spacing (`\ ') should perhaps be used.
Agarwal, Bina. 1997. ``Bargaining'' and Gender Relations: Within and Beyond the Household. \emph{Feminist Economics} 3(1): 1-51. doi:10.1080/135457097338799.  
                                                                                          ^
Warning 12 in papers/latex/productive-power.tex line 756: Interword spacing (`\ ') should perhaps be used.
Agarwal, Bina. 1997. ``Bargaining'' and Gender Relations: Within and Beyond the Household. \emph{Feminist Economics} 3(1): 1-51. doi:10.1080/135457097338799.  
                                                                                                                                ^
Warning 12 in papers/latex/productive-power.tex line 759: Interword spacing (`\ ') should perhaps be used.
Applebaum, Anne. 2003. \emph{Gulag: A History}. Doubleday.  
                      ^
Warning 12 in papers/latex/productive-power.tex line 762: Interword spacing (`\ ') should perhaps be used.
Azar, Jos\'e, Ioana Marinescu, and Marshall Steinbaum. 2022. Labor Market Concentration. \emph{Journal of Human Resources} 57(S): S167-S199. doi:10.3368/jhr.monopsony.1218-9914R1.  
                                                                                        ^
Warning 12 in papers/latex/productive-power.tex line 762: Interword spacing (`\ ') should perhaps be used.
Azar, Jos\'e, Ioana Marinescu, and Marshall Steinbaum. 2022. Labor Market Concentration. \emph{Journal of Human Resources} 57(S): S167-S199. doi:10.3368/jhr.monopsony.1218-9914R1.  
                                                                                                                                            ^
Warning 12 in papers/latex/productive-power.tex line 765: Interword spacing (`\ ') should perhaps be used.
Baer, Gabriel. 1970. The Administrative, Economic and Social Functions of Turkish Guilds. \emph{International Journal of Middle East Studies} 1(1): 28-50. doi:10.1017/s0020743800023898.  
                                                                                         ^
Warning 12 in papers/latex/productive-power.tex line 765: Interword spacing (`\ ') should perhaps be used.
Baer, Gabriel. 1970. The Administrative, Economic and Social Functions of Turkish Guilds. \emph{International Journal of Middle East Studies} 1(1): 28-50. doi:10.1017/s0020743800023898.  
                                                                                                                                                          ^
Warning 12 in papers/latex/productive-power.tex line 768: Interword spacing (`\ ') should perhaps be used.
Barkey, Karen. 2008. \emph{Empire of Difference: The Ottomans in Comparative Perspective}. Cambridge University Press. doi:10.1017/cbo9780511790645.  
                    ^
Warning 12 in papers/latex/productive-power.tex line 768: Interword spacing (`\ ') should perhaps be used.
Barkey, Karen. 2008. \emph{Empire of Difference: The Ottomans in Comparative Perspective}. Cambridge University Press. doi:10.1017/cbo9780511790645.  
                                                                                                                      ^
Warning 12 in papers/latex/productive-power.tex line 771: Interword spacing (`\ ') should perhaps be used.
Bates, Robert H. and Da-Hsiang Donald Lien. 1985. A Note on Taxation, Development, and Representative Government. \emph{Politics \& Society} 14(1): 53-70. doi:10.1177/003232928501400102.  
                                                                                                                 ^
Warning 12 in papers/latex/productive-power.tex line 771: Interword spacing (`\ ') should perhaps be used.
Bates, Robert H. and Da-Hsiang Donald Lien. 1985. A Note on Taxation, Development, and Representative Government. \emph{Politics \& Society} 14(1): 53-70. doi:10.1177/003232928501400102.  
                                                                                                                                                          ^
Warning 12 in papers/latex/productive-power.tex line 777: Interword spacing (`\ ') should perhaps be used.
Bauckham, Richard. 1993. \emph{The Theology of the Book of Revelation}. Cambridge University Press. doi:10.1017/cbo9780511819858.  
                        ^
Warning 12 in papers/latex/productive-power.tex line 777: Interword spacing (`\ ') should perhaps be used.
Bauckham, Richard. 1993. \emph{The Theology of the Book of Revelation}. Cambridge University Press. doi:10.1017/cbo9780511819858.  
                                                                                                   ^
Warning 12 in papers/latex/productive-power.tex line 780: Interword spacing (`\ ') should perhaps be used.
Bayat, Assef. 1987. \emph{Workers and Revolution in Iran: A Third World Experience of Workers' Control}. Zed Books.  
                   ^
Warning 12 in papers/latex/productive-power.tex line 783: Interword spacing (`\ ') should perhaps be used.
Bayat, Asef. 1997. \emph{Street Politics: Poor People's Movements in Iran}. Columbia University Press.  
                  ^
Warning 12 in papers/latex/productive-power.tex line 786: Interword spacing (`\ ') should perhaps be used.
Beale, G. K. 1999. \emph{The Book of Revelation: A Commentary on the Greek Text}. Eerdmans (NIGTC).  
                  ^
Warning 12 in papers/latex/productive-power.tex line 789: Interword spacing (`\ ') should perhaps be used.
Beblawi, Hazem and Giacomo Luciani (eds.). 1987. \emph{The Rentier State}. Croom Helm. doi:10.4324/9781315684864.  
                                                ^
Warning 12 in papers/latex/productive-power.tex line 789: Interword spacing (`\ ') should perhaps be used.
Beblawi, Hazem and Giacomo Luciani (eds.). 1987. \emph{The Rentier State}. Croom Helm. doi:10.4324/9781315684864.  
                                                                                      ^
Warning 12 in papers/latex/productive-power.tex line 792: Interword spacing (`\ ') should perhaps be used.
Beik, William. 1985. \emph{Absolutism and Society in Seventeenth-Century France: State Power and Provincial Aristocracy in Languedoc}. Cambridge University Press. doi:10.1017/cbo9780511583797.  
                    ^
Warning 12 in papers/latex/productive-power.tex line 792: Interword spacing (`\ ') should perhaps be used.
Beik, William. 1985. \emph{Absolutism and Society in Seventeenth-Century France: State Power and Provincial Aristocracy in Languedoc}. Cambridge University Press. doi:10.1017/cbo9780511583797.  
                                                                                                                                                                  ^
Warning 12 in papers/latex/productive-power.tex line 795: Interword spacing (`\ ') should perhaps be used.
Besley, Timothy and Torsten Persson. 2011. \emph{Pillars of Prosperity: The Political Economics of Development Clusters}. Princeton University Press. doi:10.23943/princeton/9780691152684.001.0001.  
                                          ^
Warning 12 in papers/latex/productive-power.tex line 795: Interword spacing (`\ ') should perhaps be used.
Besley, Timothy and Torsten Persson. 2011. \emph{Pillars of Prosperity: The Political Economics of Development Clusters}. Princeton University Press. doi:10.23943/princeton/9780691152684.001.0001.  
                                                                                                                                                     ^
Warning 12 in papers/latex/productive-power.tex line 798: Interword spacing (`\ ') should perhaps be used.
Besley, Timothy and Torsten Persson. 2013. Taxation and Development. In \emph{Handbook of Public Economics}, vol. 5, Elsevier, pp. 51-110. doi:10.1016/B978-0-444-53759-1.00002-9.  
                                                                                                                                          ^
Warning 12 in papers/latex/productive-power.tex line 801: Interword spacing (`\ ') should perhaps be used.
Boehm, Christopher. 1999. \emph{Hierarchy in the Forest: The Evolution of Egalitarian Behavior}. Harvard University Press. doi:10.2307/j.ctvjf9xr4.  
                         ^
Warning 12 in papers/latex/productive-power.tex line 801: Interword spacing (`\ ') should perhaps be used.
Boehm, Christopher. 1999. \emph{Hierarchy in the Forest: The Evolution of Egalitarian Behavior}. Harvard University Press. doi:10.2307/j.ctvjf9xr4.  
                                                                                                                          ^
Warning 12 in papers/latex/productive-power.tex line 804: Interword spacing (`\ ') should perhaps be used.
Boyer, Paul. 1992. \emph{When Time Shall Be No More: Prophecy Belief in Modern American Culture}. Harvard University Press (Belknap). doi:10.2307/jj.41480279.  
                  ^
Warning 12 in papers/latex/productive-power.tex line 804: Interword spacing (`\ ') should perhaps be used.
Boyer, Paul. 1992. \emph{When Time Shall Be No More: Prophecy Belief in Modern American Culture}. Harvard University Press (Belknap). doi:10.2307/jj.41480279.  
                                                                                                                                     ^
Warning 12 in papers/latex/productive-power.tex line 807: Interword spacing (`\ ') should perhaps be used.
Brenner, Robert. 1976. Agrarian Class Structure and Economic Development in Pre-Industrial Europe. \emph{Past \& Present} 70: 30-75. doi:10.1093/past/70.1.30.  
                                                                                                  ^
Warning 12 in papers/latex/productive-power.tex line 807: Interword spacing (`\ ') should perhaps be used.
Brenner, Robert. 1976. Agrarian Class Structure and Economic Development in Pre-Industrial Europe. \emph{Past \& Present} 70: 30-75. doi:10.1093/past/70.1.30.  
                                                                                                                                    ^
Warning 12 in papers/latex/productive-power.tex line 810: Interword spacing (`\ ') should perhaps be used.
Campbell, John L. 1993. The State and Fiscal Sociology. \emph{Annual Review of Sociology} 19: 163-185. doi:10.1146/annurev.so.19.080193.001115.  
                                                       ^
Warning 12 in papers/latex/productive-power.tex line 810: Interword spacing (`\ ') should perhaps be used.
Campbell, John L. 1993. The State and Fiscal Sociology. \emph{Annual Review of Sociology} 19: 163-185. doi:10.1146/annurev.so.19.080193.001115.  
                                                                                                      ^
Warning 12 in papers/latex/productive-power.tex line 813: Interword spacing (`\ ') should perhaps be used.
Chaudhry, Kiren Aziz. 1997. \emph{The Price of Wealth: Economies and Institutions in the Middle East}. Cornell University Press. doi:10.7591/9781501700347.  
                           ^
Warning 12 in papers/latex/productive-power.tex line 813: Interword spacing (`\ ') should perhaps be used.
Chaudhry, Kiren Aziz. 1997. \emph{The Price of Wealth: Economies and Institutions in the Middle East}. Cornell University Press. doi:10.7591/9781501700347.  
                                                                                                                                ^
Warning 12 in papers/latex/productive-power.tex line 816: Interword spacing (`\ ') should perhaps be used.
Cheng, Tiejun and Mark Selden. 1994. The Origins and Social Consequences of China's Hukou System. \emph{The China Quarterly} 139: 644-668. doi:10.1017/S0305741000043083.  
                                                                                                 ^
Warning 12 in papers/latex/productive-power.tex line 816: Interword spacing (`\ ') should perhaps be used.
Cheng, Tiejun and Mark Selden. 1994. The Origins and Social Consequences of China's Hukou System. \emph{The China Quarterly} 139: 644-668. doi:10.1017/S0305741000043083.  
                                                                                                                                          ^
Warning 12 in papers/latex/productive-power.tex line 819: Interword spacing (`\ ') should perhaps be used.
Chenoweth, Erica and Maria J. Stephan. 2011. \emph{Why Civil Resistance Works: The Strategic Logic of Nonviolent Conflict}. Columbia University Press.  
                                            ^
Warning 12 in papers/latex/productive-power.tex line 822: Interword spacing (`\ ') should perhaps be used.
Clastres, Pierre. 1987. \emph{Society against the State: Essays in Political Anthropology (1974), trans. Robert Hurley}. Zone Books. doi:10.2307/j.ctv1595m3p.  
                       ^
Warning 12 in papers/latex/productive-power.tex line 822: Interword spacing (`\ ') should perhaps be used.
Clastres, Pierre. 1987. \emph{Society against the State: Essays in Political Anthropology (1974), trans. Robert Hurley}. Zone Books. doi:10.2307/j.ctv1595m3p.  
                                                                                                                                    ^
Warning 12 in papers/latex/productive-power.tex line 825: Interword spacing (`\ ') should perhaps be used.
Cohen, G. A. 1978. \emph{Karl Marx's Theory of History: A Defence}. Princeton University Press. doi:10.1515/9780691213002.  
                  ^
Warning 12 in papers/latex/productive-power.tex line 825: Interword spacing (`\ ') should perhaps be used.
Cohen, G. A. 1978. \emph{Karl Marx's Theory of History: A Defence}. Princeton University Press. doi:10.1515/9780691213002.  
                                                                                               ^
Warning 12 in papers/latex/productive-power.tex line 828: Interword spacing (`\ ') should perhaps be used.
Collins, Adela Yarbro. 1984. \emph{Crisis and Catharsis: The Power of the Apocalypse}. Westminster Press.  
                            ^
Warning 12 in papers/latex/productive-power.tex line 831: Interword spacing (`\ ') should perhaps be used.
Constable, Giles. 1964. \emph{Monastic Tithes from Their Origins to the Twelfth Century}. Cambridge University Press.  
                       ^
Warning 12 in papers/latex/productive-power.tex line 834: Interword spacing (`\ ') should perhaps be used.
Cox, Michael, Gwen Arnold, and Sergio Villamayor Tomas. 2010. A Review of Design Principles for Community-based Natural Resource Management. \emph{Ecology and Society} 15(4): 38.  
                                                                                                                                            ^
Warning 12 in papers/latex/productive-power.tex line 837: Interword spacing (`\ ') should perhaps be used.
Craig, Ben and John Pencavel. 1993. The Objectives of Worker Cooperatives. \emph{Journal of Comparative Economics} 17(2): 288-308. doi:10.1006/jcec.1993.1027.  
                                                                          ^
Warning 12 in papers/latex/productive-power.tex line 837: Interword spacing (`\ ') should perhaps be used.
Craig, Ben and John Pencavel. 1993. The Objectives of Worker Cooperatives. \emph{Journal of Comparative Economics} 17(2): 288-308. doi:10.1006/jcec.1993.1027.  
                                                                                                                                  ^
Warning 12 in papers/latex/productive-power.tex line 840: Interword spacing (`\ ') should perhaps be used.
Davies, R. W. and Stephen G. Wheatcroft. 2004. \emph{The Years of Hunger: Soviet Agriculture, 1931-1933}. Palgrave Macmillan.  
                                              ^
Warning 12 in papers/latex/productive-power.tex line 843: Interword spacing (`\ ') should perhaps be used.
Dell, Melissa. 2010. The Persistent Effects of Peru's Mining Mita. \emph{Econometrica} 78(6): 1863-1903. doi:10.3982/ECTA8121.  
                                                                  ^
Warning 12 in papers/latex/productive-power.tex line 843: Interword spacing (`\ ') should perhaps be used.
Dell, Melissa. 2010. The Persistent Effects of Peru's Mining Mita. \emph{Econometrica} 78(6): 1863-1903. doi:10.3982/ECTA8121.  
                                                                                                        ^
Warning 12 in papers/latex/productive-power.tex line 846: Interword spacing (`\ ') should perhaps be used.
Domar, Evsey D. 1970. The Causes of Slavery or Serfdom: A Hypothesis. \emph{The Journal of Economic History} 30(1): 18-32. doi:10.1017/S0022050700078566.  
                                                                     ^
Warning 12 in papers/latex/productive-power.tex line 846: Interword spacing (`\ ') should perhaps be used.
Domar, Evsey D. 1970. The Causes of Slavery or Serfdom: A Hypothesis. \emph{The Journal of Economic History} 30(1): 18-32. doi:10.1017/S0022050700078566.  
                                                                                                                          ^
Warning 12 in papers/latex/productive-power.tex line 849: Interword spacing (`\ ') should perhaps be used.
Dow, Gregory K. 2003. \emph{Governing the Firm: Workers' Control in Theory and Practice}. Cambridge University Press. doi:10.1017/CBO9780511615849.  
                     ^
Warning 12 in papers/latex/productive-power.tex line 849: Interword spacing (`\ ') should perhaps be used.
Dow, Gregory K. 2003. \emph{Governing the Firm: Workers' Control in Theory and Practice}. Cambridge University Press. doi:10.1017/CBO9780511615849.  
                                                                                                                     ^
Warning 12 in papers/latex/productive-power.tex line 852: Interword spacing (`\ ') should perhaps be used.
Drelichman, Mauricio and Hans-Joachim Voth. 2014. \emph{Lending to the Borrower from Hell: Debt, Taxes, and Default in the Age of Philip II}. Princeton University Press.  
                                                 ^
Warning 12 in papers/latex/productive-power.tex line 855: Interword spacing (`\ ') should perhaps be used.
Ekelund, Robert B., Robert F. Hebert, Robert D. Tollison, Gary M. Anderson, and Audrey B. Davidson. 1996. \emph{Sacred Trust: The Medieval Church as an Economic Firm}. Oxford University Press.  
                                                                                                         ^
Warning 12 in papers/latex/productive-power.tex line 858: Interword spacing (`\ ') should perhaps be used.
Elster, Jon. 1983. \emph{Explaining Technical Change: A Case Study in the Philosophy of Science}. Cambridge University Press.  
                  ^
Warning 12 in papers/latex/productive-power.tex line 861: Interword spacing (`\ ') should perhaps be used.
Elster, Jon. 1985. \emph{Making Sense of Marx}. Cambridge University Press.  
                  ^
Warning 12 in papers/latex/productive-power.tex line 864: Interword spacing (`\ ') should perhaps be used.
Esping-Andersen, G\"osta. 1985. \emph{Politics against Markets: The Social Democratic Road to Power}. Princeton University Press. doi:10.1515/9781400886203.  
                               ^
Warning 12 in papers/latex/productive-power.tex line 864: Interword spacing (`\ ') should perhaps be used.
Esping-Andersen, G\"osta. 1985. \emph{Politics against Markets: The Social Democratic Road to Power}. Princeton University Press. doi:10.1515/9781400886203.  
                                                                                                                                 ^
Warning 12 in papers/latex/productive-power.tex line 867: Interword spacing (`\ ') should perhaps be used.
Esping-Andersen, G\"osta. 1990. \emph{The Three Worlds of Welfare Capitalism}. Princeton University Press.  
                               ^
Warning 12 in papers/latex/productive-power.tex line 870: Interword spacing (`\ ') should perhaps be used.
Evans-Pritchard, E. E. 1940. \emph{The Nuer: A Description of the Modes of Livelihood and Political Institutions of a Nilotic People}. Clarendon Press.  
                            ^
Warning 12 in papers/latex/productive-power.tex line 873: Interword spacing (`\ ') should perhaps be used.
Farber, Henry S., Daniel Herbst, Ilyana Kuziemko, and Suresh Naidu. 2021. Unions and Inequality over the Twentieth Century: New Evidence from Survey Data. \emph{The Quarterly Journal of Economics} 136(3): 1325-1385. doi:10.1093/qje/qjab012.  
                                                                                                                                                          ^
Warning 12 in papers/latex/productive-power.tex line 873: Interword spacing (`\ ') should perhaps be used.
Farber, Henry S., Daniel Herbst, Ilyana Kuziemko, and Suresh Naidu. 2021. Unions and Inequality over the Twentieth Century: New Evidence from Survey Data. \emph{The Quarterly Journal of Economics} 136(3): 1325-1385. doi:10.1093/qje/qjab012.  
                                                                                                                                                                                                                       ^
Warning 12 in papers/latex/productive-power.tex line 876: Interword spacing (`\ ') should perhaps be used.
Filtzer, Donald. 1986. \emph{Soviet Workers and Stalinist Industrialization: The Formation of Modern Soviet Production Relations, 1928-1941}. Pluto Press.  
                      ^
Warning 12 in papers/latex/productive-power.tex line 879: Interword spacing (`\ ') should perhaps be used.
Fitzpatrick, Sheila. 1994. \emph{Stalin's Peasants: Resistance and Survival in the Russian Village after Collectivization}. Oxford University Press. doi:10.1093/oso/9780195069822.001.0001.  
                          ^
Warning 12 in papers/latex/productive-power.tex line 879: Interword spacing (`\ ') should perhaps be used.
Fitzpatrick, Sheila. 1994. \emph{Stalin's Peasants: Resistance and Survival in the Russian Village after Collectivization}. Oxford University Press. doi:10.1093/oso/9780195069822.001.0001.  
                                                                                                                                                    ^
Warning 12 in papers/latex/productive-power.tex line 882: Interword spacing (`\ ') should perhaps be used.
Folbre, Nancy. 1994. \emph{Who Pays for the Kids? Gender and the Structures of Constraint}. Routledge. doi:10.4324/9780203168295.  
                    ^
Warning 12 in papers/latex/productive-power.tex line 882: Interword spacing (`\ ') should perhaps be used.
Folbre, Nancy. 1994. \emph{Who Pays for the Kids? Gender and the Structures of Constraint}. Routledge. doi:10.4324/9780203168295.  
                                                                                                      ^
Warning 12 in papers/latex/productive-power.tex line 885: Interword spacing (`\ ') should perhaps be used.
Freeman, Richard B. and James L. Medoff. 1984. \emph{What Do Unions Do?} Basic Books.  
                                              ^
Warning 12 in papers/latex/productive-power.tex line 888: Interword spacing (`\ ') should perhaps be used.
Friedman, Eli and Ching Kwan Lee. 2010. Remaking the World of Chinese Labour: A 30-Year Retrospective. \emph{British Journal of Industrial Relations} 48(3): 507-533. doi:10.1111/j.1467-8543.2010.00814.x.  
                                                                                                      ^
Warning 12 in papers/latex/productive-power.tex line 888: Interword spacing (`\ ') should perhaps be used.
Friedman, Eli and Ching Kwan Lee. 2010. Remaking the World of Chinese Labour: A 30-Year Retrospective. \emph{British Journal of Industrial Relations} 48(3): 507-533. doi:10.1111/j.1467-8543.2010.00814.x.  
                                                                                                                                                                     ^
Warning 12 in papers/latex/productive-power.tex line 891: Interword spacing (`\ ') should perhaps be used.
Friesen, Steven J. 2001. \emph{Imperial Cults and the Apocalypse of John: Reading Revelation in the Ruins}. Oxford University Press. doi:10.1093/0195131533.001.0001.  
                        ^
Warning 12 in papers/latex/productive-power.tex line 891: Interword spacing (`\ ') should perhaps be used.
Friesen, Steven J. 2001. \emph{Imperial Cults and the Apocalypse of John: Reading Revelation in the Ruins}. Oxford University Press. doi:10.1093/0195131533.001.0001.  
                                                                                                                                    ^
Warning 12 in papers/latex/productive-power.tex line 894: Interword spacing (`\ ') should perhaps be used.
Fuller, Robert C. 1995. \emph{Naming the Antichrist: The History of an American Obsession}. Oxford University Press. doi:10.1093/acprof:oso/9780195109795.001.0001.  
                       ^
Warning 12 in papers/latex/productive-power.tex line 894: Interword spacing (`\ ') should perhaps be used.
Fuller, Robert C. 1995. \emph{Naming the Antichrist: The History of an American Obsession}. Oxford University Press. doi:10.1093/acprof:oso/9780195109795.001.0001.  
                                                                                                                    ^
Warning 12 in papers/latex/productive-power.tex line 897: Interword spacing (`\ ') should perhaps be used.
Gregory, Paul R. and Valery Lazarev (eds.). 2003. \emph{The Economics of Forced Labor: The Soviet Gulag}. Hoover Institution Press.  
                                                 ^
Warning 12 in papers/latex/productive-power.tex line 900: Interword spacing (`\ ') should perhaps be used.
Haber, Stephen and Victor Menaldo. 2011. Do Natural Resources Fuel Authoritarianism? A Reappraisal of the Resource Curse. \emph{American Political Science Review} 105(1): 1-26. doi:10.1017/S0003055410000584.  
                                                                                                                         ^
Warning 12 in papers/latex/productive-power.tex line 900: Interword spacing (`\ ') should perhaps be used.
Haber, Stephen and Victor Menaldo. 2011. Do Natural Resources Fuel Authoritarianism? A Reappraisal of the Resource Curse. \emph{American Political Science Review} 105(1): 1-26. doi:10.1017/S0003055410000584.  
                                                                                                                                                                                ^
Warning 12 in papers/latex/productive-power.tex line 903: Interword spacing (`\ ') should perhaps be used.
Hacker, Jacob S. and Paul Pierson. 2010. \emph{Winner-Take-All Politics: How Washington Made the Rich Richer and Turned Its Back on the Middle Class}. Simon \& Schuster.  
                                        ^
Warning 12 in papers/latex/productive-power.tex line 906: Interword spacing (`\ ') should perhaps be used.
Hanieh, Adam. 2011. \emph{Capitalism and Class in the Gulf Arab States}. Palgrave Macmillan. doi:10.1057/9781137495105.  
                   ^
Warning 12 in papers/latex/productive-power.tex line 906: Interword spacing (`\ ') should perhaps be used.
Hanieh, Adam. 2011. \emph{Capitalism and Class in the Gulf Arab States}. Palgrave Macmillan. doi:10.1057/9781137495105.  
                                                                                            ^
Warning 12 in papers/latex/productive-power.tex line 912: Interword spacing (`\ ') should perhaps be used.
Hertog, Steffen. 2010. \emph{Princes, Brokers, and Bureaucrats: Oil and the State in Saudi Arabia}. Cornell University Press. doi:10.7591/9780801458774.  
                      ^
Warning 12 in papers/latex/productive-power.tex line 912: Interword spacing (`\ ') should perhaps be used.
Hertog, Steffen. 2010. \emph{Princes, Brokers, and Bureaucrats: Oil and the State in Saudi Arabia}. Cornell University Press. doi:10.7591/9780801458774.  
                                                                                                                             ^
Warning 12 in papers/latex/productive-power.tex line 915: Interword spacing (`\ ') should perhaps be used.
Hirschman, Albert O. 1970. \emph{Exit, Voice, and Loyalty: Responses to Decline in Firms, Organizations, and States}. Harvard University Press.  
                          ^
Warning 12 in papers/latex/productive-power.tex line 918: Interword spacing (`\ ') should perhaps be used.
Hoffman, Philip T. 1996. \emph{Growth in a Traditional Society: The French Countryside, 1450-1815}. Princeton University Press. doi:10.1515/9780691187204.  
                        ^
Warning 12 in papers/latex/productive-power.tex line 918: Interword spacing (`\ ') should perhaps be used.
Hoffman, Philip T. 1996. \emph{Growth in a Traditional Society: The French Countryside, 1450-1815}. Princeton University Press. doi:10.1515/9780691187204.  
                                                                                                                               ^
Warning 12 in papers/latex/productive-power.tex line 921: Interword spacing (`\ ') should perhaps be used.
Huber, Evelyne and John D. Stephens. 2001. \emph{Development and Crisis of the Welfare State: Parties and Policies in Global Markets}. University of Chicago Press. doi:10.7208/chicago/9780226356495.001.0001.  
                                          ^
Warning 12 in papers/latex/productive-power.tex line 921: Interword spacing (`\ ') should perhaps be used.
Huber, Evelyne and John D. Stephens. 2001. \emph{Development and Crisis of the Welfare State: Parties and Policies in Global Markets}. University of Chicago Press. doi:10.7208/chicago/9780226356495.001.0001.  
                                                                                                                                                                   ^
Warning 12 in papers/latex/productive-power.tex line 924: Interword spacing (`\ ') should perhaps be used.
Ibn Khaldun. 1958. \emph{The Muqaddimah: An Introduction to History (1377), trans. Franz Rosenthal}. Pantheon Books / Princeton University Press.  
                  ^
Warning 12 in papers/latex/productive-power.tex line 927: Interword spacing (`\ ') should perhaps be used.
Kagan, Richard L. 1981. \emph{Lawsuits and Litigants in Castile, 1500-1700}. University of North Carolina Press.  
                       ^
Warning 12 in papers/latex/productive-power.tex line 930: Interword spacing (`\ ') should perhaps be used.
Kandiyoti, Deniz. 1988. Bargaining with Patriarchy. \emph{Gender \& Society} 2(3): 274-290. doi:10.1177/089124388002003004.  
                                                   ^
Warning 12 in papers/latex/productive-power.tex line 930: Interword spacing (`\ ') should perhaps be used.
Kandiyoti, Deniz. 1988. Bargaining with Patriarchy. \emph{Gender \& Society} 2(3): 274-290. doi:10.1177/089124388002003004.  
                                                                                           ^
Warning 12 in papers/latex/productive-power.tex line 933: Interword spacing (`\ ') should perhaps be used.
Kapiszewski, Andrzej. 2001. \emph{Nationals and Expatriates: Population and Labour Dilemmas of the Gulf Cooperation Council States}. Ithaca Press.  
                           ^
Warning 12 in papers/latex/productive-power.tex line 936: Interword spacing (`\ ') should perhaps be used.
Karaman, K. K{\i}van\c{c} and \c{S}evket Pamuk. 2010. Ottoman State Finances in European Perspective, 1500-1914. \emph{The Journal of Economic History} 70(3): 593-629. doi:10.1017/s0022050710000550.  
                                                                                                                ^
Warning 12 in papers/latex/productive-power.tex line 936: Interword spacing (`\ ') should perhaps be used.
Karaman, K. K{\i}van\c{c} and \c{S}evket Pamuk. 2010. Ottoman State Finances in European Perspective, 1500-1914. \emph{The Journal of Economic History} 70(3): 593-629. doi:10.1017/s0022050710000550.  
                                                                                                                                                                       ^
Warning 12 in papers/latex/productive-power.tex line 939: Interword spacing (`\ ') should perhaps be used.
Kelly, Robert L. 1995. \emph{The Foraging Spectrum: Diversity in Hunter-Gatherer Lifeways}. Smithsonian Institution Press. doi:10.2307/j.ctv2sx9gc9.  
                      ^
Warning 12 in papers/latex/productive-power.tex line 939: Interword spacing (`\ ') should perhaps be used.
Kelly, Robert L. 1995. \emph{The Foraging Spectrum: Diversity in Hunter-Gatherer Lifeways}. Smithsonian Institution Press. doi:10.2307/j.ctv2sx9gc9.  
                                                                                                                          ^
Warning 12 in papers/latex/productive-power.tex line 942: Interword spacing (`\ ') should perhaps be used.
Kornai, J\'anos. 1986. The Soft Budget Constraint. \emph{Kyklos} 39(1): 3-30. doi:10.1111/j.1467-6435.1986.tb01252.x.  
                                                  ^
Warning 12 in papers/latex/productive-power.tex line 942: Interword spacing (`\ ') should perhaps be used.
Kornai, J\'anos. 1986. The Soft Budget Constraint. \emph{Kyklos} 39(1): 3-30. doi:10.1111/j.1467-6435.1986.tb01252.x.  
                                                                             ^
Warning 12 in papers/latex/productive-power.tex line 945: Interword spacing (`\ ') should perhaps be used.
Kornai, J\'anos. 1992. \emph{The Socialist System: The Political Economy of Communism}. Princeton University Press. doi:10.2307/j.ctv1ddczdr.  
                      ^
Warning 12 in papers/latex/productive-power.tex line 945: Interword spacing (`\ ') should perhaps be used.
Kornai, J\'anos. 1992. \emph{The Socialist System: The Political Economy of Communism}. Princeton University Press. doi:10.2307/j.ctv1ddczdr.  
                                                                                                                   ^
Warning 12 in papers/latex/productive-power.tex line 948: Interword spacing (`\ ') should perhaps be used.
Korpi, Walter. 1983. \emph{The Democratic Class Struggle}. Routledge \& Kegan Paul.  
                    ^
Warning 12 in papers/latex/productive-power.tex line 951: Interword spacing (`\ ') should perhaps be used.
Korpi, Walter and Joakim Palme. 1998. The Paradox of Redistribution and Strategies of Equality: Welfare State Institutions, Inequality, and Poverty in the Western Countries. \emph{American Sociological Review} 63(5): 661-687. doi:10.2307/2657333.  
                                                                                                                                                                             ^
Warning 12 in papers/latex/productive-power.tex line 951: Interword spacing (`\ ') should perhaps be used.
Korpi, Walter and Joakim Palme. 1998. The Paradox of Redistribution and Strategies of Equality: Welfare State Institutions, Inequality, and Poverty in the Western Countries. \emph{American Sociological Review} 63(5): 661-687. doi:10.2307/2657333.  
                                                                                                                                                                                                                                 ^
Warning 12 in papers/latex/productive-power.tex line 954: Interword spacing (`\ ') should perhaps be used.
Kraybill, J. Nelson. 1996. \emph{Imperial Cult and Commerce in John's Apocalypse}. Sheffield Academic Press (JSNT Supplement 132).  
                          ^
Warning 12 in papers/latex/productive-power.tex line 957: Interword spacing (`\ ') should perhaps be used.
Kuran, Timur. 2011. \emph{The Long Divergence: How Islamic Law Held Back the Middle East}. Princeton University Press. doi:10.1515/9781400836017.  
                   ^
Warning 12 in papers/latex/productive-power.tex line 957: Interword spacing (`\ ') should perhaps be used.
Kuran, Timur. 2011. \emph{The Long Divergence: How Islamic Law Held Back the Middle East}. Princeton University Press. doi:10.1515/9781400836017.  
                                                                                                                      ^
Warning 12 in papers/latex/productive-power.tex line 960: Interword spacing (`\ ') should perhaps be used.
Kwass, Michael. 2000. \emph{Privilege and the Politics of Taxation in Eighteenth-Century France}. Cambridge University Press.  
                     ^
Warning 12 in papers/latex/productive-power.tex line 963: Interword spacing (`\ ') should perhaps be used.
Lapidus, Gail Warshofsky. 1978. \emph{Women in Soviet Society: Equality, Development, and Social Change}. University of California Press.  
                               ^
Warning 12 in papers/latex/productive-power.tex line 966: Interword spacing (`\ ') should perhaps be used.
Largo, Mateo. 2026. \emph{The Hierarchy of the Beast System: Institutional Power, Elite Coordination, and Economic Dependency Across Political Regimes}. Working paper, 14 October 2026.  
                   ^
Warning 12 in papers/latex/productive-power.tex line 969: Interword spacing (`\ ') should perhaps be used.
Laslett, Barbara and Johanna Brenner. 1989. Gender and Social Reproduction: Historical Perspectives. \emph{Annual Review of Sociology} 15: 381-404. doi:10.1146/annurev.so.15.080189.002121.  
                                                                                                    ^
Warning 12 in papers/latex/productive-power.tex line 969: Interword spacing (`\ ') should perhaps be used.
Laslett, Barbara and Johanna Brenner. 1989. Gender and Social Reproduction: Historical Perspectives. \emph{Annual Review of Sociology} 15: 381-404. doi:10.1146/annurev.so.15.080189.002121.  
                                                                                                                                                   ^
Warning 12 in papers/latex/productive-power.tex line 972: Interword spacing (`\ ') should perhaps be used.
Lee, Richard B. 1979. \emph{The !Kung San: Men, Women, and Work in a Foraging Society}. Cambridge University Press.  
                     ^
Warning 26 in papers/latex/productive-power.tex line 972: You ought to remove spaces in front of punctuation.
Lee, Richard B. 1979. \emph{The !Kung San: Men, Women, and Work in a Foraging Society}. Cambridge University Press.  
                               ^
Warning 12 in papers/latex/productive-power.tex line 975: Interword spacing (`\ ') should perhaps be used.
Lee, Ching Kwan. 2007. \emph{Against the Law: Labor Protests in China's Rustbelt and Sunbelt}. University of California Press. doi:10.1525/9780520940642.  
                      ^
Warning 12 in papers/latex/productive-power.tex line 975: Interword spacing (`\ ') should perhaps be used.
Lee, Ching Kwan. 2007. \emph{Against the Law: Labor Protests in China's Rustbelt and Sunbelt}. University of California Press. doi:10.1525/9780520940642.  
                                                                                                                              ^
Warning 12 in papers/latex/productive-power.tex line 978: Interword spacing (`\ ') should perhaps be used.
Lee, Richard B. 2013. \emph{The Dobe Ju/'hoansi (4th edition)}. Wadsworth/Cengage Learning.  
                     ^
Warning 12 in papers/latex/productive-power.tex line 981: Interword spacing (`\ ') should perhaps be used.
Levi, Margaret. 1988. \emph{Of Rule and Revenue}. University of California Press. doi:10.1525/9780520909540.  
                     ^
Warning 12 in papers/latex/productive-power.tex line 981: Interword spacing (`\ ') should perhaps be used.
Levi, Margaret. 1988. \emph{Of Rule and Revenue}. University of California Press. doi:10.1525/9780520909540.  
                                                                                 ^
Warning 12 in papers/latex/productive-power.tex line 984: Interword spacing (`\ ') should perhaps be used.
Lindblom, Charles E. 1977. \emph{Politics and Markets: The World's Political-Economic Systems}. Basic Books.  
                          ^
Warning 12 in papers/latex/productive-power.tex line 987: Interword spacing (`\ ') should perhaps be used.
Lipset, Seymour Martin, Martin A. Trow, and James S. Coleman. 1956. \emph{Union Democracy: The Internal Politics of the International Typographical Union}. Free Press.  
                                                                   ^
Warning 12 in papers/latex/productive-power.tex line 990: Interword spacing (`\ ') should perhaps be used.
Long, Matthew. 2026a. \emph{Coercive Power and Enforcement}. Part V of The Six Pillars of the Beast System. Working paper, October 2026.  
                     ^
Warning 12 in papers/latex/productive-power.tex line 993: Interword spacing (`\ ') should perhaps be used.
Long, Matthew. 2026b. \emph{Financial Power and Resource Command}. Part I of The Six Pillars of the Beast System. Working paper, October 2026.  
                     ^
Warning 12 in papers/latex/productive-power.tex line 996: Interword spacing (`\ ') should perhaps be used.
Long, Matthew. 2026c. \emph{The Formalized State: The Hierarchy of the Beast System}. Part VII of The Six Pillars of the Beast System. Working paper, October 2026.  
                     ^
Warning 12 in papers/latex/productive-power.tex line 999: Interword spacing (`\ ') should perhaps be used.
Long, Matthew. 2026d. \emph{Ideological Power and Legitimation}. Part IV of The Six Pillars of the Beast System. Working paper, October 2026.  
                     ^
Warning 12 in papers/latex/productive-power.tex line 1002: Interword spacing (`\ ') should perhaps be used.
Long, Matthew. 2026e. \emph{Judicial Power and Legal Interpretation}. Part III of The Six Pillars of the Beast System. Working paper, October 2026.  
                     ^
Warning 12 in papers/latex/productive-power.tex line 1005: Interword spacing (`\ ') should perhaps be used.
Long, Matthew. 2026f. \emph{Political Power and Rule Making}. Part II of The Six Pillars of the Beast System. Working paper, October 2026.  
                     ^
Warning 12 in papers/latex/productive-power.tex line 1011: Interword spacing (`\ ') should perhaps be used.
Manning, Alan. 2003. \emph{Monopsony in Motion: Imperfect Competition in Labor Markets}. Princeton University Press. doi:10.1515/9781400850679.  
                    ^
Warning 12 in papers/latex/productive-power.tex line 1011: Interword spacing (`\ ') should perhaps be used.
Manning, Alan. 2003. \emph{Monopsony in Motion: Imperfect Competition in Labor Markets}. Princeton University Press. doi:10.1515/9781400850679.  
                                                                                                                    ^
Warning 12 in papers/latex/productive-power.tex line 1014: Interword spacing (`\ ') should perhaps be used.
Marshall, Lorna. 1976. \emph{The !Kung of Nyae Nyae}. Harvard University Press. doi:10.4159/harvard.9780674180574.  
                      ^
Warning 26 in papers/latex/productive-power.tex line 1014: You ought to remove spaces in front of punctuation.
Marshall, Lorna. 1976. \emph{The !Kung of Nyae Nyae}. Harvard University Press. doi:10.4159/harvard.9780674180574.  
                                ^
Warning 12 in papers/latex/productive-power.tex line 1014: Interword spacing (`\ ') should perhaps be used.
Marshall, Lorna. 1976. \emph{The !Kung of Nyae Nyae}. Harvard University Press. doi:10.4159/harvard.9780674180574.  
                                                                               ^
Warning 12 in papers/latex/productive-power.tex line 1017: Interword spacing (`\ ') should perhaps be used.
Martin, Isaac William, Ajay K. Mehrotra, and Monica Prasad (eds.). 2009. \emph{The New Fiscal Sociology: Taxation in Comparative and Historical Perspective}. Cambridge University Press. doi:10.1017/CBO9780511627071.  
                                                                        ^
Warning 12 in papers/latex/productive-power.tex line 1017: Interword spacing (`\ ') should perhaps be used.
Martin, Isaac William, Ajay K. Mehrotra, and Monica Prasad (eds.). 2009. \emph{The New Fiscal Sociology: Taxation in Comparative and Historical Perspective}. Cambridge University Press. doi:10.1017/CBO9780511627071.  
                                                                                                                                                                                         ^
Warning 12 in papers/latex/productive-power.tex line 1020: Interword spacing (`\ ') should perhaps be used.
Marx, Karl. 1976. \emph{Capital: A Critique of Political Economy, Volume 1 (1867), trans. Ben Fowkes}. Penguin.  
                 ^
Warning 12 in papers/latex/productive-power.tex line 1023: Interword spacing (`\ ') should perhaps be used.
McGinn, Bernard. 1998. \emph{Antichrist: Two Thousand Years of the Human Fascination with Evil}. Columbia University Press.  
                      ^
Warning 12 in papers/latex/productive-power.tex line 1026: Interword spacing (`\ ') should perhaps be used.
Merton, Robert K. 1968. \emph{Social Theory and Social Structure (enlarged edition)}. Free Press.  
                       ^
Warning 12 in papers/latex/productive-power.tex line 1029: Interword spacing (`\ ') should perhaps be used.
Michels, Robert. 1915. \emph{Political Parties: A Sociological Study of the Oligarchical Tendencies of Modern Democracy}. Hearst's International Library.  
                      ^
Warning 12 in papers/latex/productive-power.tex line 1032: Interword spacing (`\ ') should perhaps be used.
Moore, Mick. 2004. Revenues, State Formation, and the Quality of Governance in Developing Countries. \emph{International Political Science Review} 25(3): 297-319. doi:10.1177/0192512104043018.  
                                                                                                    ^
Warning 12 in papers/latex/productive-power.tex line 1032: Interword spacing (`\ ') should perhaps be used.
Moore, Mick. 2004. Revenues, State Formation, and the Quality of Governance in Developing Countries. \emph{International Political Science Review} 25(3): 297-319. doi:10.1177/0192512104043018.  
                                                                                                                                                                  ^
Warning 12 in papers/latex/productive-power.tex line 1035: Interword spacing (`\ ') should perhaps be used.
Olson, Mancur. 1965. \emph{The Logic of Collective Action: Public Goods and the Theory of Groups}. Harvard University Press. doi:10.4159/9780674041660.  
                    ^
Warning 12 in papers/latex/productive-power.tex line 1035: Interword spacing (`\ ') should perhaps be used.
Olson, Mancur. 1965. \emph{The Logic of Collective Action: Public Goods and the Theory of Groups}. Harvard University Press. doi:10.4159/9780674041660.  
                                                                                                                            ^
Warning 12 in papers/latex/productive-power.tex line 1038: Interword spacing (`\ ') should perhaps be used.
Ostrom, Elinor. 1990. \emph{Governing the Commons: The Evolution of Institutions for Collective Action}. Cambridge University Press. doi:10.1017/CBO9780511807763.  
                     ^
Warning 12 in papers/latex/productive-power.tex line 1038: Interword spacing (`\ ') should perhaps be used.
Ostrom, Elinor. 1990. \emph{Governing the Commons: The Evolution of Institutions for Collective Action}. Cambridge University Press. doi:10.1017/CBO9780511807763.  
                                                                                                                                    ^
Warning 12 in papers/latex/productive-power.tex line 1041: Interword spacing (`\ ') should perhaps be used.
Ostrom, Elinor. 2010. Beyond Markets and States: Polycentric Governance of Complex Economic Systems. \emph{American Economic Review} 100(3): 641-672. doi:10.1257/aer.100.3.641.  
                                                                                                    ^
Warning 12 in papers/latex/productive-power.tex line 1041: Interword spacing (`\ ') should perhaps be used.
Ostrom, Elinor. 2010. Beyond Markets and States: Polycentric Governance of Complex Economic Systems. \emph{American Economic Review} 100(3): 641-672. doi:10.1257/aer.100.3.641.  
                                                                                                                                                     ^
Warning 12 in papers/latex/productive-power.tex line 1044: Interword spacing (`\ ') should perhaps be used.
Pamuk, \c{S}evket. 2000. \emph{A Monetary History of the Ottoman Empire}. Cambridge University Press.  
                        ^
Warning 12 in papers/latex/productive-power.tex line 1047: Interword spacing (`\ ') should perhaps be used.
Piketty, Thomas, Emmanuel Saez, and Gabriel Zucman. 2018. Distributional National Accounts: Methods and Estimates for the United States. \emph{The Quarterly Journal of Economics} 133(2): 553-609. doi:10.1093/qje/qjx043.  
                                                                                                                                        ^
Warning 12 in papers/latex/productive-power.tex line 1047: Interword spacing (`\ ') should perhaps be used.
Piketty, Thomas, Emmanuel Saez, and Gabriel Zucman. 2018. Distributional National Accounts: Methods and Estimates for the United States. \emph{The Quarterly Journal of Economics} 133(2): 553-609. doi:10.1093/qje/qjx043.  
                                                                                                                                                                                                   ^
Warning 12 in papers/latex/productive-power.tex line 1050: Interword spacing (`\ ') should perhaps be used.
Polanyi, Karl. 1944. \emph{The Great Transformation: The Political and Economic Origins of Our Time}. Farrar \& Rinehart.  
                    ^
Warning 12 in papers/latex/productive-power.tex line 1053: Interword spacing (`\ ') should perhaps be used.
Pontusson, Jonas. 1992. \emph{The Limits of Social Democracy: Investment Politics in Sweden}. Cornell University Press. doi:10.7591/9781501737541.  
                       ^
Warning 12 in papers/latex/productive-power.tex line 1053: Interword spacing (`\ ') should perhaps be used.
Pontusson, Jonas. 1992. \emph{The Limits of Social Democracy: Investment Politics in Sweden}. Cornell University Press. doi:10.7591/9781501737541.  
                                                                                                                       ^
Warning 12 in papers/latex/productive-power.tex line 1056: Interword spacing (`\ ') should perhaps be used.
Price, S. R. F. 1984. \emph{Rituals and Power: The Roman Imperial Cult in Asia Minor}. Cambridge University Press.  
                     ^
Warning 12 in papers/latex/productive-power.tex line 1059: Interword spacing (`\ ') should perhaps be used.
Prodi, Paolo. 1987. \emph{The Papal Prince: One Body and Two Souls: The Papal Monarchy in Early Modern Europe}. Cambridge University Press.  
                   ^
Warning 12 in papers/latex/productive-power.tex line 1062: Interword spacing (`\ ') should perhaps be used.
Przeworski, Adam. 1985. \emph{Capitalism and Social Democracy}. Cambridge University Press. doi:10.1017/cbo9781139171830.  
                       ^
Warning 12 in papers/latex/productive-power.tex line 1062: Interword spacing (`\ ') should perhaps be used.
Przeworski, Adam. 1985. \emph{Capitalism and Social Democracy}. Cambridge University Press. doi:10.1017/cbo9781139171830.  
                                                                                           ^
Warning 12 in papers/latex/productive-power.tex line 1065: Interword spacing (`\ ') should perhaps be used.
Quataert, Donald and Erik Jan Z\"urcher (eds.). 1995. \emph{Workers and the Working Class in the Ottoman Empire and the Turkish Republic, 1839-1950}. I. B. Tauris.  
                                                     ^
Warning 12 in papers/latex/productive-power.tex line 1068: Interword spacing (`\ ') should perhaps be used.
Root, Hilton L. 1987. \emph{Peasants and King in Burgundy: Agrarian Foundations of French Absolutism}. University of California Press. doi:10.1525/9780520913349.  
                     ^
Warning 12 in papers/latex/productive-power.tex line 1068: Interword spacing (`\ ') should perhaps be used.
Root, Hilton L. 1987. \emph{Peasants and King in Burgundy: Agrarian Foundations of French Absolutism}. University of California Press. doi:10.1525/9780520913349.  
                                                                                                                                      ^
Warning 12 in papers/latex/productive-power.tex line 1071: Interword spacing (`\ ') should perhaps be used.
Ross, Michael L. 2001. Does Oil Hinder Democracy? \emph{World Politics} 53(3): 325-361. doi:10.1353/wp.2001.0011.  
                                                                                       ^
Warning 12 in papers/latex/productive-power.tex line 1074: Interword spacing (`\ ') should perhaps be used.
Ross, Michael L. 2004. Does Taxation Lead to Representation? \emph{British Journal of Political Science} 34(2): 229-249. doi:10.1017/S0007123404000031.  
                                                                                                                        ^
Warning 12 in papers/latex/productive-power.tex line 1077: Interword spacing (`\ ') should perhaps be used.
Rossing, Barbara R. 1999. \emph{The Choice between Two Cities: Whore, Bride, and Empire in the Apocalypse}. Trinity Press International (Harvard Theological Studies 48).  
                         ^
Warning 12 in papers/latex/productive-power.tex line 1080: Interword spacing (`\ ') should perhaps be used.
Rothstein, Bo. 1996. \emph{The Social Democratic State: The Swedish Model and the Bureaucratic Problem of Social Reforms}. University of Pittsburgh Press. doi:10.2307/jj.13110785.  
                    ^
Warning 12 in papers/latex/productive-power.tex line 1080: Interword spacing (`\ ') should perhaps be used.
Rothstein, Bo. 1996. \emph{The Social Democratic State: The Swedish Model and the Bureaucratic Problem of Social Reforms}. University of Pittsburgh Press. doi:10.2307/jj.13110785.  
                                                                                                                                                          ^
Warning 12 in papers/latex/productive-power.tex line 1083: Interword spacing (`\ ') should perhaps be used.
Rubin, Jared. 2017. \emph{Rulers, Religion, and Riches: Why the West Got Rich and the Middle East Did Not}. Cambridge University Press. doi:10.1017/9781139568272.  
                   ^
Warning 12 in papers/latex/productive-power.tex line 1083: Interword spacing (`\ ') should perhaps be used.
Rubin, Jared. 2017. \emph{Rulers, Religion, and Riches: Why the West Got Rich and the Middle East Did Not}. Cambridge University Press. doi:10.1017/9781139568272.  
                                                                                                                                       ^
Warning 12 in papers/latex/productive-power.tex line 1086: Interword spacing (`\ ') should perhaps be used.
Rueda, David. 2005. Insider-Outsider Politics in Industrialized Democracies: The Challenge to Social Democratic Parties. \emph{American Political Science Review} 99(1): 61-74. doi:10.1017/S000305540505149X.  
                                                                                                                        ^
Warning 12 in papers/latex/productive-power.tex line 1086: Interword spacing (`\ ') should perhaps be used.
Rueda, David. 2005. Insider-Outsider Politics in Industrialized Democracies: The Challenge to Social Democratic Parties. \emph{American Political Science Review} 99(1): 61-74. doi:10.1017/S000305540505149X.  
                                                                                                                                                                               ^
Warning 12 in papers/latex/productive-power.tex line 1089: Interword spacing (`\ ') should perhaps be used.
Rueschemeyer, Dietrich, Evelyne Huber Stephens, and John D. Stephens. 1992. \emph{Capitalist Development and Democracy}. University of Chicago Press.  
                                                                           ^
Warning 12 in papers/latex/productive-power.tex line 1092: Interword spacing (`\ ') should perhaps be used.
Sahlins, Marshall. 1972. \emph{Stone Age Economics}. Aldine-Atherton. doi:10.4324/9780203037416.  
                        ^
Warning 12 in papers/latex/productive-power.tex line 1092: Interword spacing (`\ ') should perhaps be used.
Sahlins, Marshall. 1972. \emph{Stone Age Economics}. Aldine-Atherton. doi:10.4324/9780203037416.  
                                                                     ^
Warning 12 in papers/latex/productive-power.tex line 1095: Interword spacing (`\ ') should perhaps be used.
Scheve, Kenneth and David Stasavage. 2016. \emph{Taxing the Rich: A History of Fiscal Fairness in the United States and Europe}. Princeton University Press. doi:10.1515/9781400880379.  
                                          ^
Warning 12 in papers/latex/productive-power.tex line 1095: Interword spacing (`\ ') should perhaps be used.
Scheve, Kenneth and David Stasavage. 2016. \emph{Taxing the Rich: A History of Fiscal Fairness in the United States and Europe}. Princeton University Press. doi:10.1515/9781400880379.  
                                                                                                                                                            ^
Warning 12 in papers/latex/productive-power.tex line 1098: Interword spacing (`\ ') should perhaps be used.
Scott, James C. 1976. \emph{The Moral Economy of the Peasant: Rebellion and Subsistence in Southeast Asia}. Yale University Press. doi:10.12987/9780300185553.  
                     ^
Warning 12 in papers/latex/productive-power.tex line 1098: Interword spacing (`\ ') should perhaps be used.
Scott, James C. 1976. \emph{The Moral Economy of the Peasant: Rebellion and Subsistence in Southeast Asia}. Yale University Press. doi:10.12987/9780300185553.  
                                                                                                                                  ^
Warning 12 in papers/latex/productive-power.tex line 1101: Interword spacing (`\ ') should perhaps be used.
Scott, James C. 1985. \emph{Weapons of the Weak: Everyday Forms of Peasant Resistance}. Yale University Press. doi:10.12987/9780300153620.  
                     ^
Warning 12 in papers/latex/productive-power.tex line 1101: Interword spacing (`\ ') should perhaps be used.
Scott, James C. 1985. \emph{Weapons of the Weak: Everyday Forms of Peasant Resistance}. Yale University Press. doi:10.12987/9780300153620.  
                                                                                                              ^
Warning 12 in papers/latex/productive-power.tex line 1104: Interword spacing (`\ ') should perhaps be used.
Scott, James C. 2009. \emph{The Art of Not Being Governed: An Anarchist History of Upland Southeast Asia}. Yale University Press. doi:10.12987/9780300156522.  
                     ^
Warning 12 in papers/latex/productive-power.tex line 1104: Interword spacing (`\ ') should perhaps be used.
Scott, James C. 2009. \emph{The Art of Not Being Governed: An Anarchist History of Upland Southeast Asia}. Yale University Press. doi:10.12987/9780300156522.  
                                                                                                                                 ^
Warning 12 in papers/latex/productive-power.tex line 1107: Interword spacing (`\ ') should perhaps be used.
Siegelbaum, Lewis H. 1988. \emph{Stakhanovism and the Politics of Productivity in the USSR, 1935-1941}. Cambridge University Press.  
                          ^
Warning 12 in papers/latex/productive-power.tex line 1110: Interword spacing (`\ ') should perhaps be used.
Silver, Beverly J. 2003. \emph{Forces of Labor: Workers' Movements and Globalization since 1870}. Cambridge University Press. doi:10.1017/CBO9780511615702.  
                        ^
Warning 12 in papers/latex/productive-power.tex line 1110: Interword spacing (`\ ') should perhaps be used.
Silver, Beverly J. 2003. \emph{Forces of Labor: Workers' Movements and Globalization since 1870}. Cambridge University Press. doi:10.1017/CBO9780511615702.  
                                                                                                                             ^
Warning 12 in papers/latex/productive-power.tex line 1113: Interword spacing (`\ ') should perhaps be used.
Singer, Amy. 2008. \emph{Charity in Islamic Societies}. Cambridge University Press.  
                  ^
Warning 12 in papers/latex/productive-power.tex line 1116: Interword spacing (`\ ') should perhaps be used.
Thompson, Leonard L. 1990. \emph{The Book of Revelation: Apocalypse and Empire}. Oxford University Press. doi:10.1093/oso/9780195055511.001.0001.  
                          ^
Warning 12 in papers/latex/productive-power.tex line 1116: Interword spacing (`\ ') should perhaps be used.
Thompson, Leonard L. 1990. \emph{The Book of Revelation: Apocalypse and Empire}. Oxford University Press. doi:10.1093/oso/9780195055511.001.0001.  
                                                                                                         ^
Warning 12 in papers/latex/productive-power.tex line 1119: Interword spacing (`\ ') should perhaps be used.
Timmons, Jeffrey F. 2005. The Fiscal Contract: States, Taxes, and Public Services. \emph{World Politics} 57(4): 530-567. doi:10.1353/wp.2006.0015.  
                                                                                  ^
Warning 12 in papers/latex/productive-power.tex line 1119: Interword spacing (`\ ') should perhaps be used.
Timmons, Jeffrey F. 2005. The Fiscal Contract: States, Taxes, and Public Services. \emph{World Politics} 57(4): 530-567. doi:10.1353/wp.2006.0015.  
                                                                                                                        ^
Warning 12 in papers/latex/productive-power.tex line 1122: Interword spacing (`\ ') should perhaps be used.
Vassberg, David E. 1984. \emph{Land and Society in Golden Age Castile}. Cambridge University Press.  
                        ^
Warning 12 in papers/latex/productive-power.tex line 1125: Interword spacing (`\ ') should perhaps be used.
Viola, Lynne. 1996. \emph{Peasant Rebels under Stalin: Collectivization and the Culture of Peasant Resistance}. Oxford University Press. doi:10.1093/oso/9780195101973.001.0001.  
                   ^
Warning 12 in papers/latex/productive-power.tex line 1125: Interword spacing (`\ ') should perhaps be used.
Viola, Lynne. 1996. \emph{Peasant Rebels under Stalin: Collectivization and the Culture of Peasant Resistance}. Oxford University Press. doi:10.1093/oso/9780195101973.001.0001.  
                                                                                                                                        ^
Warning 12 in papers/latex/productive-power.tex line 1128: Interword spacing (`\ ') should perhaps be used.
Vitalis, Robert. 2007. \emph{America's Kingdom: Mythmaking on the Saudi Oil Frontier}. Stanford University Press. doi:10.1515/9781503626119.  
                      ^
Warning 12 in papers/latex/productive-power.tex line 1128: Interword spacing (`\ ') should perhaps be used.
Vitalis, Robert. 2007. \emph{America's Kingdom: Mythmaking on the Saudi Oil Frontier}. Stanford University Press. doi:10.1515/9781503626119.  
                                                                                                                 ^
Warning 12 in papers/latex/productive-power.tex line 1131: Interword spacing (`\ ') should perhaps be used.
Walder, Andrew G. 1986. \emph{Communist Neo-Traditionalism: Work and Authority in Chinese Industry}. University of California Press. doi:10.1525/9780520909007.  
                       ^
Warning 12 in papers/latex/productive-power.tex line 1131: Interword spacing (`\ ') should perhaps be used.
Walder, Andrew G. 1986. \emph{Communist Neo-Traditionalism: Work and Authority in Chinese Industry}. University of California Press. doi:10.1525/9780520909007.  
                                                                                                                                    ^
Warning 12 in papers/latex/productive-power.tex line 1134: Interword spacing (`\ ') should perhaps be used.
Western, Bruce and Jake Rosenfeld. 2011. Unions, Norms, and the Rise in U.S. Wage Inequality. \emph{American Sociological Review} 76(4): 513-537. doi:10.1177/0003122411414817.  
                                                                                             ^
Warning 12 in papers/latex/productive-power.tex line 1134: Interword spacing (`\ ') should perhaps be used.
Western, Bruce and Jake Rosenfeld. 2011. Unions, Norms, and the Rise in U.S. Wage Inequality. \emph{American Sociological Review} 76(4): 513-537. doi:10.1177/0003122411414817.  
                                                                                                                                                 ^
Warning 12 in papers/latex/productive-power.tex line 1140: Interword spacing (`\ ') should perhaps be used.
Wink, Walter. 1992. \emph{Engaging the Powers: Discernment and Resistance in a World of Domination}. Fortress Press. doi:10.2307/j.ctt1tm7j16.  
                   ^
Warning 12 in papers/latex/productive-power.tex line 1140: Interword spacing (`\ ') should perhaps be used.
Wink, Walter. 1992. \emph{Engaging the Powers: Discernment and Resistance in a World of Domination}. Fortress Press. doi:10.2307/j.ctt1tm7j16.  
                                                                                                                    ^
Warning 12 in papers/latex/productive-power.tex line 1143: Interword spacing (`\ ') should perhaps be used.
Woodburn, James. 1982. Egalitarian Societies. \emph{Man (N.S.)} 17(3): 431-451. doi:10.2307/2801707.  
                                             ^
Warning 12 in papers/latex/productive-power.tex line 1143: Interword spacing (`\ ') should perhaps be used.
Woodburn, James. 1982. Egalitarian Societies. \emph{Man (N.S.)} 17(3): 431-451. doi:10.2307/2801707.  
                                                                               ^
Warning 12 in papers/latex/productive-power.tex line 1146: Interword spacing (`\ ') should perhaps be used.
Wright, Erik Olin. 2000. Working-Class Power, Capitalist-Class Interests, and Class Compromise. \emph{American Journal of Sociology} 105(4): 957-1002. doi:10.1086/210397.  
                                                                                               ^
Warning 12 in papers/latex/productive-power.tex line 1146: Interword spacing (`\ ') should perhaps be used.
Wright, Erik Olin. 2000. Working-Class Power, Capitalist-Class Interests, and Class Compromise. \emph{American Journal of Sociology} 105(4): 957-1002. doi:10.1086/210397.  
                                                                                                                                                      ^

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'chktex -q -n1 -n3 -n8 -n9 -n12 -n13 -n24 -n25 -n36 -n38 papers/latex/productive-power.tex' in /Users/mlong/Documents/Development/the-beast-system
 exited 2 in 0ms:
Warning 7 in papers/latex/productive-power.tex line 395: Accent command `\'' needs use of `\i'.
In Castile, communal lands and municipal institutions mattered to peasant livelihoods \citep{vassberg1984}, and ordinary people litigated in large numbers in the royal courts \citep{kagan1981}. The Cortes bargained with the crown over new taxes, and the taxes paid by Castilian producers sustained the crown's borrowing \citep{drelichman2014}. In the Americas the same monarchy organized compelled state labor. The Potos\'i mining draft required indigenous communities in designated districts to send a share of their men to the mines, and \citet{dell2010} found persistent lower consumption and child growth in those districts today. In the Papal States, the pope was both temporal sovereign and head of the Church, which made the coupling of $\pI$ with fiscal administration direct \citep{prodi1987}.  
                                                                                                                                                                                                                                                                                                                                                                                                                                    ^^
Warning 26 in papers/latex/productive-power.tex line 972: You ought to remove spaces in front of punctuation.
Lee, Richard B. 1979. \emph{The !Kung San: Men, Women, and Work in a Foraging Society}. Cambridge University Press.  
                               ^
Warning 26 in papers/latex/productive-power.tex line 1014: You ought to remove spaces in front of punctuation.
Marshall, Lorna. 1976. \emph{The !Kung of Nyae Nyae}. Harvard University Press. doi:10.4159/harvard.9780674180574.  
                                ^

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "rg -n '[0-9]-[0-9]' papers/latex/productive-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
60:Every governance system consumes resources that someone must produce. This paper treats production, payment and social reproduction as the sixth pillar of a comparative framework in which six functions (resource allocation, rule-making, adjudication, legitimation, sanction and production) are present in every functioning polity. From a maintenance axiom we prove that a persistent collective must produce at a positive average rate and must reproduce its producers through care labor, and that rents, tribute, migration or automation relocate production rather than remove it. The same dependence gives producers a latent veto: when outside revenue falls short of the institutions' maintenance requirement, a collective withdrawal of labor, taxes or trade threatens their persistence. A bargaining model makes the channels exact. Producers' terms rise with their outside option and organized bargaining weight, fall linearly with the concentration of control over productive participation, and lose their withdrawal premium once rents cover the maintenance requirement. Restricting mobility pays only when the value of free exit exceeds the cost of enforcement, a condition that nests Domar's land-labor hypothesis and Brenner's emphasis on class organization. Every instrument that depresses producers' terms is held in another pillar, so the capture of production never originates inside it. A comparison of six regime types finds the function everywhere and its capture only under specific couplings. Read typologically, Revelation 13:16-17 depicts the limiting case in which exchange is conditioned on allegiance. The parameters are not estimated here; nine hypotheses state what would falsify the model.
716:The passage most directly relevant to this pillar is Revelation 13:16-17 (KJV): ``And he causeth all, both small and great, rich and poor, free and bond, to receive a mark in their right hand, or in their foreheads: And that no man might buy or sell, save he that had the mark, or the name of the beast, or the number of his name.'' The verse does not describe a form of labor. It describes a condition on participation in exchange. Its scope runs across every category of the social order, ``free and bond'' included, so the condition is not the bondage of a class but the gating of everyone's access to buying and selling by a sign of allegiance.
718:In the terms of Section~\ref{sec:mechanisms}, the verse depicts a closed participation gate, $\gamma=0$, applied to all who withhold allegiance. Proposition~\ref{prop:productive-power:gate} says what such a gate requires and what it yields. It requires control over exchange, a criterion of allegiance and enforcement. In the vision these are distributed across figures: the first beast holds authority and makes war (13:2, 13:4, 13:7); the second beast speaks, performs signs and causes the image of the first to be worshipped (13:12-15); and the restriction on buying and selling is its economic instrument. The series' heuristic maps these to $\pP$ and $\pC$, to $\pI$, and to the coupling of $\pF$ with $\pW$. The gate also yields a precise result: producers without organization or exit are held to their autarky value. The vision's image of economic exclusion as the sanction for refused allegiance is the limiting case of the model, and it is a limiting case of capture (Proposition B), not of the productive function itself.
720:The preterist anchor gives the image economic content. \citet{kraybill1996} argued that participation in the maritime trade and trade guilds of Asia Minor entangled Christians in the imperial cult, and that John's vision calls them to withdraw from commerce on those terms. \citet{bauckham1991} read the lament over Babylon in Revelation 18 as an economic critique of Rome. The cargo list of 18:11-13 runs through luxury goods and ends with ``slaves, and souls of men,'' an indictment of a trade that included human beings. This is literal chattel slavery in the Roman economy. It is the extreme of Table~\ref{tab:bondage} and must not be read as a metaphor for wage labor or taxation. The list also illustrates the relocation lemma: the goods that sustained the imperial center were produced across the provinces and beyond them, and the kings, merchants and shipmasters who lament Babylon's fall (18:9-19) are those whose wealth depended on that flow.
722:The text's response to the gate has the shape of Hirschman's triad, though it was written for different purposes. The imperative ``Come out of her, my people'' (18:4) is a call to exit. Faithful witness (11:3-13) and the ``patience and the faith of the saints'' (13:10) are a form of voice that refuses the demanded loyalty. Loyalty itself is the contested object: the vision depicts a demand for worship, and the faithful are those who give their allegiance elsewhere. \citet{rossing1999} read the contrast between Babylon and the New Jerusalem as a choice between two cities, with an economic critique of imperial Rome at its center. \citet{wink1992} generalized the beast into a domination system present in institutions of every age, a reading congenial to the series' claim that the structure is universal.
756:Agarwal, Bina. 1997. ``Bargaining'' and Gender Relations: Within and Beyond the Household. \emph{Feminist Economics} 3(1): 1-51. doi:10.1080/135457097338799.
762:Azar, Jos\'e, Ioana Marinescu, and Marshall Steinbaum. 2022. Labor Market Concentration. \emph{Journal of Human Resources} 57(S): S167-S199. doi:10.3368/jhr.monopsony.1218-9914R1.
765:Baer, Gabriel. 1970. The Administrative, Economic and Social Functions of Turkish Guilds. \emph{International Journal of Middle East Studies} 1(1): 28-50. doi:10.1017/s0020743800023898.
771:Bates, Robert H. and Da-Hsiang Donald Lien. 1985. A Note on Taxation, Development, and Representative Government. \emph{Politics \& Society} 14(1): 53-70. doi:10.1177/003232928501400102.
774:Bauckham, Richard. 1991. The Economic Critique of Rome in Revelation 18. In \emph{Images of Empire}, ed. Loveday Alexander, JSOT Press (JSOTSup 122), pp. 47-90.
798:Besley, Timothy and Torsten Persson. 2013. Taxation and Development. In \emph{Handbook of Public Economics}, vol. 5, Elsevier, pp. 51-110. doi:10.1016/B978-0-444-53759-1.00002-9.
807:Brenner, Robert. 1976. Agrarian Class Structure and Economic Development in Pre-Industrial Europe. \emph{Past \& Present} 70: 30-75. doi:10.1093/past/70.1.30.
810:Campbell, John L. 1993. The State and Fiscal Sociology. \emph{Annual Review of Sociology} 19: 163-185. doi:10.1146/annurev.so.19.080193.001115.
816:Cheng, Tiejun and Mark Selden. 1994. The Origins and Social Consequences of China's Hukou System. \emph{The China Quarterly} 139: 644-668. doi:10.1017/S0305741000043083.
837:Craig, Ben and John Pencavel. 1993. The Objectives of Worker Cooperatives. \emph{Journal of Comparative Economics} 17(2): 288-308. doi:10.1006/jcec.1993.1027.
840:Davies, R. W. and Stephen G. Wheatcroft. 2004. \emph{The Years of Hunger: Soviet Agriculture, 1931-1933}. Palgrave Macmillan.
843:Dell, Melissa. 2010. The Persistent Effects of Peru's Mining Mita. \emph{Econometrica} 78(6): 1863-1903. doi:10.3982/ECTA8121.
846:Domar, Evsey D. 1970. The Causes of Slavery or Serfdom: A Hypothesis. \emph{The Journal of Economic History} 30(1): 18-32. doi:10.1017/S0022050700078566.
873:Farber, Henry S., Daniel Herbst, Ilyana Kuziemko, and Suresh Naidu. 2021. Unions and Inequality over the Twentieth Century: New Evidence from Survey Data. \emph{The Quarterly Journal of Economics} 136(3): 1325-1385. doi:10.1093/qje/qjab012.
876:Filtzer, Donald. 1986. \emph{Soviet Workers and Stalinist Industrialization: The Formation of Modern Soviet Production Relations, 1928-1941}. Pluto Press.
888:Friedman, Eli and Ching Kwan Lee. 2010. Remaking the World of Chinese Labour: A 30-Year Retrospective. \emph{British Journal of Industrial Relations} 48(3): 507-533. doi:10.1111/j.1467-8543.2010.00814.x.
900:Haber, Stephen and Victor Menaldo. 2011. Do Natural Resources Fuel Authoritarianism? A Reappraisal of the Resource Curse. \emph{American Political Science Review} 105(1): 1-26. doi:10.1017/S0003055410000584.
909:Hempel, Carl G. 1959. The Logic of Functional Analysis. In \emph{Symposium on Sociological Theory}, ed. Llewellyn Gross, Harper \& Row, pp. 271-307.
918:Hoffman, Philip T. 1996. \emph{Growth in a Traditional Society: The French Countryside, 1450-1815}. Princeton University Press. doi:10.1515/9780691187204.
927:Kagan, Richard L. 1981. \emph{Lawsuits and Litigants in Castile, 1500-1700}. University of North Carolina Press.
930:Kandiyoti, Deniz. 1988. Bargaining with Patriarchy. \emph{Gender \& Society} 2(3): 274-290. doi:10.1177/089124388002003004.
936:Karaman, K. K{\i}van\c{c} and \c{S}evket Pamuk. 2010. Ottoman State Finances in European Perspective, 1500-1914. \emph{The Journal of Economic History} 70(3): 593-629. doi:10.1017/s0022050710000550.
942:Kornai, J\'anos. 1986. The Soft Budget Constraint. \emph{Kyklos} 39(1): 3-30. doi:10.1111/j.1467-6435.1986.tb01252.x.
951:Korpi, Walter and Joakim Palme. 1998. The Paradox of Redistribution and Strategies of Equality: Welfare State Institutions, Inequality, and Poverty in the Western Countries. \emph{American Sociological Review} 63(5): 661-687. doi:10.2307/2657333.
969:Laslett, Barbara and Johanna Brenner. 1989. Gender and Social Reproduction: Historical Perspectives. \emph{Annual Review of Sociology} 15: 381-404. doi:10.1146/annurev.so.15.080189.002121.
1008:Mahdavy, Hossein. 1970. The Patterns and Problems of Economic Development in Rentier States: The Case of Iran. In \emph{Studies in the Economic History of the Middle East}, ed. M. A. Cook, Oxford University Press, pp. 428-467.
1032:Moore, Mick. 2004. Revenues, State Formation, and the Quality of Governance in Developing Countries. \emph{International Political Science Review} 25(3): 297-319. doi:10.1177/0192512104043018.
1041:Ostrom, Elinor. 2010. Beyond Markets and States: Polycentric Governance of Complex Economic Systems. \emph{American Economic Review} 100(3): 641-672. doi:10.1257/aer.100.3.641.
1047:Piketty, Thomas, Emmanuel Saez, and Gabriel Zucman. 2018. Distributional National Accounts: Methods and Estimates for the United States. \emph{The Quarterly Journal of Economics} 133(2): 553-609. doi:10.1093/qje/qjx043.
1065:Quataert, Donald and Erik Jan Z\"urcher (eds.). 1995. \emph{Workers and the Working Class in the Ottoman Empire and the Turkish Republic, 1839-1950}. I. B. Tauris.
1071:Ross, Michael L. 2001. Does Oil Hinder Democracy? \emph{World Politics} 53(3): 325-361. doi:10.1353/wp.2001.0011.
1074:Ross, Michael L. 2004. Does Taxation Lead to Representation? \emph{British Journal of Political Science} 34(2): 229-249. doi:10.1017/S0007123404000031.
1086:Rueda, David. 2005. Insider-Outsider Politics in Industrialized Democracies: The Challenge to Social Democratic Parties. \emph{American Political Science Review} 99(1): 61-74. doi:10.1017/S000305540505149X.
1107:Siegelbaum, Lewis H. 1988. \emph{Stakhanovism and the Politics of Productivity in the USSR, 1935-1941}. Cambridge University Press.
1119:Timmons, Jeffrey F. 2005. The Fiscal Contract: States, Taxes, and Public Services. \emph{World Politics} 57(4): 530-567. doi:10.1353/wp.2006.0015.
1134:Western, Bruce and Jake Rosenfeld. 2011. Unions, Norms, and the Rise in U.S. Wage Inequality. \emph{American Sociological Review} 76(4): 513-537. doi:10.1177/0003122411414817.
1137:Wiessner, Polly. 2005. Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity? \emph{Human Nature} 16(2): 115-145.
1143:Woodburn, James. 1982. Egalitarian Societies. \emph{Man (N.S.)} 17(3): 431-451. doi:10.2307/2801707.
1146:Wright, Erik Olin. 2000. Working-Class Power, Capitalist-Class Interests, and Class Compromise. \emph{American Journal of Sociology} 105(4): 957-1002. doi:10.1086/210397.

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "rg -n \"\\\\\\\\'i|\\\\\\\\'\\{i\\}\" papers/latex/productive-power.tex
rg -n '\\\\emph\\{["'^}]*[0-9]+-[0-9]+'"' papers/latex/productive-power.tex
rg -n '(pp?\\. |\\): )[A-Z]?[0-9]+-[A-Z]?[0-9]+' papers/latex/productive-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
395:In Castile, communal lands and municipal institutions mattered to peasant livelihoods \citep{vassberg1984}, and ordinary people litigated in large numbers in the royal courts \citep{kagan1981}. The Cortes bargained with the crown over new taxes, and the taxes paid by Castilian producers sustained the crown's borrowing \citep{drelichman2014}. In the Americas the same monarchy organized compelled state labor. The Potos\'i mining draft required indigenous communities in designated districts to send a share of their men to the mines, and \citet{dell2010} found persistent lower consumption and child growth in those districts today. In the Papal States, the pope was both temporal sovereign and head of the Church, which made the coupling of $\pI$ with fiscal administration direct \citep{prodi1987}.
840:Davies, R. W. and Stephen G. Wheatcroft. 2004. \emph{The Years of Hunger: Soviet Agriculture, 1931-1933}. Palgrave Macmillan.
876:Filtzer, Donald. 1986. \emph{Soviet Workers and Stalinist Industrialization: The Formation of Modern Soviet Production Relations, 1928-1941}. Pluto Press.
918:Hoffman, Philip T. 1996. \emph{Growth in a Traditional Society: The French Countryside, 1450-1815}. Princeton University Press. doi:10.1515/9780691187204.
927:Kagan, Richard L. 1981. \emph{Lawsuits and Litigants in Castile, 1500-1700}. University of North Carolina Press.
1065:Quataert, Donald and Erik Jan Z\"urcher (eds.). 1995. \emph{Workers and the Working Class in the Ottoman Empire and the Turkish Republic, 1839-1950}. I. B. Tauris.
1107:Siegelbaum, Lewis H. 1988. \emph{Stakhanovism and the Politics of Productivity in the USSR, 1935-1941}. Cambridge University Press.
756:Agarwal, Bina. 1997. ``Bargaining'' and Gender Relations: Within and Beyond the Household. \emph{Feminist Economics} 3(1): 1-51. doi:10.1080/135457097338799.
762:Azar, Jos\'e, Ioana Marinescu, and Marshall Steinbaum. 2022. Labor Market Concentration. \emph{Journal of Human Resources} 57(S): S167-S199. doi:10.3368/jhr.monopsony.1218-9914R1.
765:Baer, Gabriel. 1970. The Administrative, Economic and Social Functions of Turkish Guilds. \emph{International Journal of Middle East Studies} 1(1): 28-50. doi:10.1017/s0020743800023898.
771:Bates, Robert H. and Da-Hsiang Donald Lien. 1985. A Note on Taxation, Development, and Representative Government. \emph{Politics \& Society} 14(1): 53-70. doi:10.1177/003232928501400102.
774:Bauckham, Richard. 1991. The Economic Critique of Rome in Revelation 18. In \emph{Images of Empire}, ed. Loveday Alexander, JSOT Press (JSOTSup 122), pp. 47-90.
798:Besley, Timothy and Torsten Persson. 2013. Taxation and Development. In \emph{Handbook of Public Economics}, vol. 5, Elsevier, pp. 51-110. doi:10.1016/B978-0-444-53759-1.00002-9.
837:Craig, Ben and John Pencavel. 1993. The Objectives of Worker Cooperatives. \emph{Journal of Comparative Economics} 17(2): 288-308. doi:10.1006/jcec.1993.1027.
843:Dell, Melissa. 2010. The Persistent Effects of Peru's Mining Mita. \emph{Econometrica} 78(6): 1863-1903. doi:10.3982/ECTA8121.
846:Domar, Evsey D. 1970. The Causes of Slavery or Serfdom: A Hypothesis. \emph{The Journal of Economic History} 30(1): 18-32. doi:10.1017/S0022050700078566.
873:Farber, Henry S., Daniel Herbst, Ilyana Kuziemko, and Suresh Naidu. 2021. Unions and Inequality over the Twentieth Century: New Evidence from Survey Data. \emph{The Quarterly Journal of Economics} 136(3): 1325-1385. doi:10.1093/qje/qjab012.
888:Friedman, Eli and Ching Kwan Lee. 2010. Remaking the World of Chinese Labour: A 30-Year Retrospective. \emph{British Journal of Industrial Relations} 48(3): 507-533. doi:10.1111/j.1467-8543.2010.00814.x.
900:Haber, Stephen and Victor Menaldo. 2011. Do Natural Resources Fuel Authoritarianism? A Reappraisal of the Resource Curse. \emph{American Political Science Review} 105(1): 1-26. doi:10.1017/S0003055410000584.
909:Hempel, Carl G. 1959. The Logic of Functional Analysis. In \emph{Symposium on Sociological Theory}, ed. Llewellyn Gross, Harper \& Row, pp. 271-307.
930:Kandiyoti, Deniz. 1988. Bargaining with Patriarchy. \emph{Gender \& Society} 2(3): 274-290. doi:10.1177/089124388002003004.
936:Karaman, K. K{\i}van\c{c} and \c{S}evket Pamuk. 2010. Ottoman State Finances in European Perspective, 1500-1914. \emph{The Journal of Economic History} 70(3): 593-629. doi:10.1017/s0022050710000550.
942:Kornai, J\'anos. 1986. The Soft Budget Constraint. \emph{Kyklos} 39(1): 3-30. doi:10.1111/j.1467-6435.1986.tb01252.x.
951:Korpi, Walter and Joakim Palme. 1998. The Paradox of Redistribution and Strategies of Equality: Welfare State Institutions, Inequality, and Poverty in the Western Countries. \emph{American Sociological Review} 63(5): 661-687. doi:10.2307/2657333.
1008:Mahdavy, Hossein. 1970. The Patterns and Problems of Economic Development in Rentier States: The Case of Iran. In \emph{Studies in the Economic History of the Middle East}, ed. M. A. Cook, Oxford University Press, pp. 428-467.
1032:Moore, Mick. 2004. Revenues, State Formation, and the Quality of Governance in Developing Countries. \emph{International Political Science Review} 25(3): 297-319. doi:10.1177/0192512104043018.
1041:Ostrom, Elinor. 2010. Beyond Markets and States: Polycentric Governance of Complex Economic Systems. \emph{American Economic Review} 100(3): 641-672. doi:10.1257/aer.100.3.641.
1047:Piketty, Thomas, Emmanuel Saez, and Gabriel Zucman. 2018. Distributional National Accounts: Methods and Estimates for the United States. \emph{The Quarterly Journal of Economics} 133(2): 553-609. doi:10.1093/qje/qjx043.
1071:Ross, Michael L. 2001. Does Oil Hinder Democracy? \emph{World Politics} 53(3): 325-361. doi:10.1353/wp.2001.0011.
1074:Ross, Michael L. 2004. Does Taxation Lead to Representation? \emph{British Journal of Political Science} 34(2): 229-249. doi:10.1017/S0007123404000031.
1086:Rueda, David. 2005. Insider-Outsider Politics in Industrialized Democracies: The Challenge to Social Democratic Parties. \emph{American Political Science Review} 99(1): 61-74. doi:10.1017/S000305540505149X.
1119:Timmons, Jeffrey F. 2005. The Fiscal Contract: States, Taxes, and Public Services. \emph{World Politics} 57(4): 530-567. doi:10.1353/wp.2006.0015.
1134:Western, Bruce and Jake Rosenfeld. 2011. Unions, Norms, and the Rise in U.S. Wage Inequality. \emph{American Sociological Review} 76(4): 513-537. doi:10.1177/0003122411414817.
1137:Wiessner, Polly. 2005. Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity? \emph{Human Nature} 16(2): 115-145.
1143:Woodburn, James. 1982. Egalitarian Societies. \emph{Man (N.S.)} 17(3): 431-451. doi:10.2307/2801707.
1146:Wright, Erik Olin. 2000. Working-Class Power, Capitalist-Class Interests, and Class Compromise. \emph{American Journal of Sociology} 105(4): 957-1002. doi:10.1086/210397.

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "rg -c '"'^'"\\\\bibitem' papers/latex/productive-power.tex
rg -n '"'^'"\\\\bibitem' papers/latex/productive-power.tex | tail -1" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
131
1145:\bibitem[{Wright}(2000)]{wright2000}

codex
- Line 395: `Potos\'i` accents a dotted `i`, which can render incorrectly. Use `Potos\'{\i}` or UTF-8 `Potosí`.

- Lines 60, 716, 718, 720, 722: numeric verse ranges use hyphens instead of en dashes. Replace, for example, `13:16-17` with `13:16--17`.

- Lines 756, 762, 765, 771, 774, 798, 807, 810, 816, 837, 840, 843, 846, 873, 876, 888, 900, 909, 918, 927, 930, 936, 942, 951, 969, 1008, 1032, 1041, 1047, 1065, 1071, 1074, 1086, 1107, 1119, 1134, 1137, 1143, 1146: page and year ranges incorrectly use hyphens. Replace range separators with `--`, such as `1325--1385` and `1928--1941`. Preserve hyphens in compound words and DOI identifiers.

No missing packages, unmatched environments/braces, duplicate labels, undefined references, or undefined citation keys were found. Actual box warnings could not be compiler-confirmed because the read-only environment prevented LaTeX from creating temporary `.aux` and `.log` files; static inspection found no definite overfull/underfull-box source beyond the issues above.

VERDICT: NEEDS_FIX
hook: Stop
hook: Stop
hook: Stop Completed
hook: Stop Completed
tokens used
95,166
- Line 395: `Potos\'i` accents a dotted `i`, which can render incorrectly. Use `Potos\'{\i}` or UTF-8 `Potosí`.

- Lines 60, 716, 718, 720, 722: numeric verse ranges use hyphens instead of en dashes. Replace, for example, `13:16-17` with `13:16--17`.

- Lines 756, 762, 765, 771, 774, 798, 807, 810, 816, 837, 840, 843, 846, 873, 876, 888, 900, 909, 918, 927, 930, 936, 942, 951, 969, 1008, 1032, 1041, 1047, 1065, 1071, 1074, 1086, 1107, 1119, 1134, 1137, 1143, 1146: page and year ranges incorrectly use hyphens. Replace range separators with `--`, such as `1325--1385` and `1928--1941`. Preserve hyphens in compound words and DOI identifiers.

No missing packages, unmatched environments/braces, duplicate labels, undefined references, or undefined citation keys were found. Actual box warnings could not be compiler-confirmed because the read-only environment prevented LaTeX from creating temporary `.aux` and `.log` files; static inspection found no definite overfull/underfull-box source beyond the issues above.

VERDICT: NEEDS_FIX
