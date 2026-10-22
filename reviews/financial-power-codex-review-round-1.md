---
reviewer: codex (OpenAI) gpt-5.6-sol
type: formatting
paper: financial-power
round: 1
date: 2026-10-22T16:57:01Z
---
Reading additional input from stdin...
2026-10-22T16:57:01.769816Z ERROR codex_models_manager::cache: failed to load models cache: missing field `base_instructions` at line 139 column 5
OpenAI Codex v0.145.0
--------
workdir: /Users/mlong/Documents/Development/the-beast-system
model: gpt-5.6-sol
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a1648b-7119-7f11-96c6-27f566d5c2bb
--------
user
Read ONLY the file papers/latex/financial-power.tex (do not explore other files or directories). Review it for LaTeX formatting issues: compilation errors, missing packages, broken references, inconsistent styling, overfull/underfull boxes, spacing problems. List all issues with line numbers and concrete fixes. End your response with a VERDICT line — exactly one of: VERDICT: PASS (no issues remain) or VERDICT: NEEDS_FIX (issues listed above must be fixed).
warning: Under-development features enabled: chronicle. Under-development features are incomplete and may behave unpredictably. To suppress this warning, set `suppress_unstable_features_warning = true` in /Users/mlong/.codex/config.toml.
warning: clamping SessionEnd hook timeout to 3s in /Users/mlong/.codex/plugins/cache/openai-codex/codex/1.0.6/hooks/hooks.json
2026-10-22T16:57:03.495139Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server linear: OAuth token refresh failed: Server returned error response: invalid_grant: Grant not found
2026-10-22T16:57:04.412418Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server resend: OAuth token refresh failed: Server returned error response: invalid_grant: Refresh token has been revoked
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
I’ll inspect only `papers/latex/financial-power.tex`, with numbered lines, and report formatting/compilation risks without reading anything else.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'nl -ba papers/latex/financial-power.tex' in /Users/mlong/Documents/Development/the-beast-system
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
    20	\usepackage[authoryear,round]{natbib}
    21	\usepackage[hidelinks]{hyperref}
    22	\usepackage{cleveref}
    23	
    24	\newtheorem{theorem}{Theorem}[section]
    25	\newtheorem{proposition}[theorem]{Proposition}
    26	\newtheorem{lemma}[theorem]{Lemma}
    27	\newtheorem{corollary}[theorem]{Corollary}
    28	\newtheorem{assumption}[theorem]{Assumption}
    29	\theoremstyle{definition}
    30	\newtheorem{definition}[theorem]{Definition}
    31	\newtheorem{example}[theorem]{Example}
    32	\theoremstyle{remark}
    33	\newtheorem{remark}[theorem]{Remark}
    34	
    35	\AddToHook{env/proposition/begin}{\crefalias{theorem}{proposition}}
    36	\AddToHook{env/lemma/begin}{\crefalias{theorem}{lemma}}
    37	\AddToHook{env/corollary/begin}{\crefalias{theorem}{corollary}}
    38	\AddToHook{env/definition/begin}{\crefalias{theorem}{definition}}
    39	\AddToHook{env/assumption/begin}{\crefalias{theorem}{assumption}}
    40	\AddToHook{env/example/begin}{\crefalias{theorem}{example}}
    41	\AddToHook{env/remark/begin}{\crefalias{theorem}{remark}}
    42	\crefname{assumption}{assumption}{assumptions}
    43	\Crefname{assumption}{Assumption}{Assumptions}
    44	
    45	% Pillar labels (sans-serif, per the series notation) and shared objects
    46	\newcommand{\pF}{\mathsf{F}}
    47	\newcommand{\pP}{\mathsf{P}}
    48	\newcommand{\pJ}{\mathsf{J}}
    49	\newcommand{\pI}{\mathsf{I}}
    50	\newcommand{\pC}{\mathsf{C}}
    51	\newcommand{\pW}{\mathsf{W}}
    52	\newcommand{\Pillars}{\mathcal{M}}
    53	\newcommand{\Integ}{\mathcal{I}}
    54	\newcommand{\Prob}{\mathbb{P}}
    55	\newcommand{\E}{\mathbb{E}}
    56	
    57	\title{Financial Power and Resource Command\\[4pt]
    58	  {\normalsize Part I of \emph{The Six Pillars of the Beast System}}}
    59	\author{Matthew Long\\
    60	  \small The YonedaAI Collaboration, YonedaAI Research Collective\\
    61	  \small Chicago, IL\\
    62	  \small \texttt{matthew@yonedaai.com} \quad \url{https://yonedaai.com}}
    63	\date{October 2026}
    64	
    65	\begin{document}
    66	
    67	\maketitle
    68	
    69	\begin{abstract}
    70	Every governance system must settle conflicting claims on finite resources. This paper treats that settlement as the financial pillar of a six-function model of governance and asks who controls resources across regime types. From a scarcity axiom and an explicit assumption that unsettled conflicts carry a positive hazard of dissolution, we prove that a collective with no recognized allocation regularity cannot persist with probability bounded away from zero, and that in any collective that does persist the share of conflicts settled by such a regularity tends to one. The result concerns a function, not an institution: in foraging bands the regularity is a sharing norm, and control is dispersed close to the minimum concentration the index allows. We then prove that the necessity of the pillar places no restriction on its concentration or contestability, show that aggregating subdomains understates concentration by exactly the cross-domain variance of control shares, and derive conditional comparative statics under which resource holders convert wealth into influence over rules. A comparison of market-capitalist societies, communist party-states, social democracies, Islamic states, Catholic monarchies and secular democracies finds the same function held by different institutions, with documented capture episodes and documented checks in every type. Seven hypotheses with stated falsifiers make the capture claim testable. Revelation 13 and 18 are read typologically as images of economic participation conditioned on allegiance. The main limitation is that no coded cross-regime dataset yet exists, so the comparative claims remain qualitative.
    71	\end{abstract}
    72	
    73	\section{Introduction}
    74	\label{sec:intro}
    75	
    76	Every polity decides who controls its resources, whether or not it has a treasury, a bank, or a word for property. A foraging camp decides who carves the meat and who receives which portion. A pastoral lineage decides whose cattle pay a bridewealth or a blood debt. A medieval caliphate assigns revenues to a treasury and endowments to trustees, an early modern monarchy pledges future taxes to its bankers, a Soviet ministry allocates steel by plan, and a modern democracy delegates the supply of money to an independent central bank. The institutions differ almost completely. The problem they solve does not.
    77	
    78	This paper is the first of seven Parts of a series whose thesis is that the ideology of governance changes while its institutional functions remain. The series follows the framework of \citet{largo2026hbs}, which models a polity as a directed multiplex network whose layers record distinct mechanisms of constraint, and which asks when concentration and coordination across those layers turn into unaccountable domination. The series uses six pillars: financial power~$\pF$ (who controls the resources), political power~$\pP$ (who makes the laws), judicial power~$\pJ$ (who interprets them), ideological power~$\pI$ (who shapes beliefs), coercive power~$\pC$ (who enforces the rules), and productive power~$\pW$ (who produces the wealth that sustains everything). Part VII \citep{long2026formalized} proves the general claim, called Proposition~A, that every functioning governance system contains all six functions and the dependencies among them, and it proves that this structural necessity does not imply Proposition~B, the contingent and measurable claim that the functions have been captured by a coalition that escapes independent accountability.
    79	
    80	The financial pillar is the one most easily misread. Popular usage equates control of resources with capitalists, bankers, or a single class, and so treats the existence of the pillar as an accusation. The argument here runs the other way. Resource command exists in a hunter-gatherer camp, where it is held by everyone at once through sharing norms; what varies across polities is how concentrated it is, how contestable it is, and how tightly it is coupled to rule-making, adjudication, belief, coercion, and work. A theory that cannot separate the existence of the function from its concentration will find domination everywhere and therefore explain nothing.
    81	
    82	The necessity of the function and the contingency of its concentration can both be proved. From the scarcity axiom of the series and an explicit assumption that unsettled conflict risks dissolution, a collective with no recognized way of settling claims loses its chance of survival geometrically over time, and in a collective that survives almost every conflict is settled by such a procedure (\cref{prop:financial-power:necessity}). The same necessity places no restriction on how concentrated or contestable control is (\cref{prop:financial-power:nonimplication}); this is the pillar-level case of the non-implication that Part VII proves for all six pillars.
    83	
    84	Three further results make the comparison measurable. Aggregate concentration understates the concentration of subdomains such as credit, land, and the public budget by exactly the cross-domain variance of control shares (\cref{prop:financial-power:aggregation-gap}). A resource holder's investment in influence over other pillars rises with its share and falls with the contestability of the receiving pillar (\cref{prop:financial-power:influence}). And lenders to a sovereign are protected by the threat of exclusion from future credit, not by control of legislation, whenever the ruler's future need for credit is large enough (\cref{prop:financial-power:sovereign-credit}). The six regime types of the series are then compared with the same questions and the same standard of evidence, and seven hypotheses are stated together with the observations that would falsify them.
    85	
    86	Two scope commitments govern everything that follows. The phrase ``Beast System'' names the universal six-function structure that Part VII proves present in every governance system; it is never a label for a religion, a people, a profession, a regime, or a person. And the comparison asks how the universal function is distributed in each regime type, not whether a civilization ``has'' it. Because every type has it, the comparison is even-handed by construction, and the evidentiary burden falls entirely on claims of capture.
    87	
    88	\section{The financial pillar in the multiplex network}
    89	\label{sec:pillar}
    90	
    91	\subsection{Shared notation}
    92	
    93	The series inherits its formal objects from \citet{largo2026hbs} and does not redefine them. A polity at time~$t$ is a directed multiplex network $G_t=(V_t,E_t)$ whose nodes are organizations or coherent actor groups. Each pillar $m$ in the index set $\Pillars=\{\pF,\pP,\pJ,\pI,\pC,\pW\}$, with $M=|\Pillars|=6$, contributes a layer with adjacency $A^m_t$ and edge weights $a^m_{ij,t}\in[0,1]$ that record the documented capacity of actor~$i$ to constrain a feasible action of actor~$j$ through mechanism~$m$. A many-to-many role map assigns actors to pillars. Actor~$i$ holds a normalized share $s^m_{i,t}$ of decision-relevant control in pillar~$m$, with $\sum_i s^m_{i,t}=1$; concentration is the Herfindahl-Hirschman index $H_{m,t}=\sum_i (s^m_{i,t})^2$ \citep{hirschman1964}; contestability $Q_{m,t}\in[0,1]$ scores transparency, appeal rights, independence, competition, and credible replacement of decision makers. The illustrative index of unaccountable concentration is $U_t=\sum_m \omega_m H_{m,t}(1-Q_{m,t})$ with preregistered weights $\omega_m\geq 0$ summing to one.
    94	
    95	The remaining objects concern relations between pillars. Cross-pillar integration $C_{mn,t}\in[0,1]$ is the extent to which one coalition commands appointments, budgets, sanctions, or agenda in both $m$ and $n$, and the integration statistic is $\Integ_t=\tfrac{2}{M(M-1)}\sum_{m<n}C_{mn,t}$, the mean over the fifteen pillar pairs. A capture link $(i\to j,m)$ requires privileged access or discretion, a resulting weakening of applicable accountability or contestability, and material evidence tying the asymmetry to an institutional output. All of these objects are due to \citet{largo2026hbs}; the six-pillar version with fifteen pairs follows the series convention.
    96	
    97	The financial pillar corresponds to the source's resource function $R$: command over capital, land, credit, investment, infrastructure, public budgets, and strategic means of production. The source cautions that ownership, scale, or the administration of public goods is not by itself evidence of domination, and that in a party-state the resource function can sit under political authority \citep{largo2026hbs}. The label $\pF$ is written in sans-serif throughout so that it is never confused with the role map.
    98	
    99	\subsection{The allocation problem}
   100	
   101	\begin{definition}[Allocation problem]
   102	\label{def:financial-power:allocation-problem}
   103	Let $N$ be a collective of $n\geq 2$ members and $\mathcal{K}$ a finite set of goods, with available stock $\omega\in\mathbb{R}^{\mathcal{K}}_{+}$ at a given date. Each member $i$ holds a claim $c_i\in\mathbb{R}^{\mathcal{K}}_{+}$ on the stock. A \emph{conflict} occurs when the claims on some good $k$ are jointly infeasible, $\sum_{i\in N}c_{ik}>\omega_k$. An \emph{allocation problem} is the task of determining, for each conflict, which feasible assignment $x=(x_i)_{i\in N}$ with $\sum_i x_i\leq\omega$ prevails, together with the related decisions of who may use a good, who may store it, and what is held in reserve.
   104	\end{definition}
   105	
   106	Scarcity in this sense is relative to claims, not absolute. A group can be materially comfortable and still face conflicts, because the meat of one animal, the best grazing in a dry season, or the revenue of one year is claimed by more people, or for more purposes, than it can satisfy. This is the scarcity axiom of the series (Ax1: resources are finite and claims on them conflict), whose general statement and refinement belong to Part VII.
   107	
   108	\begin{definition}[Settlement]
   109	\label{def:financial-power:settlement}
   110	A conflict is \emph{settled} when it is resolved by a procedure that belongs to the collective's repertoire, meaning that (a) the procedure applies to a class of situations rather than to a single instance, (b) members can anticipate the resulting assignment from a description of the procedure and of the situation, and (c) members comply with the assignment or are held to it by others. A conflict resolved without such a procedure, by unregulated contest whose outcome depends on whoever prevails in the moment, is \emph{unsettled}. The \emph{financial pillar} of a collective is the set of procedures that settle its conflicts, together with the actors who operate them.
   111	\end{definition}
   112	
   113	The definition is deliberately broad on the side of form and narrow on the side of function. A sharing norm, an ownership rule with voluntary exchange, a plan target, a waqf deed, a credit contract, a lottery, and a ritualized contest with known rules all settle conflicts. A brawl over a carcass does not, unless brawls themselves follow rules that the parties recognize. The broad side guards against the error of identifying the function with one institution; the narrow side keeps the definition from being satisfied by anything whatever.
   114	
   115	\begin{definition}[Settlement modes]
   116	\label{def:financial-power:settlement-modes}
   117	A settlement procedure is classified by the source of the assignment it produces: a \emph{sharing norm} assigns goods by a rule of distribution binding on the holder; \emph{property and exchange} assigns goods by prior entitlement and voluntary transfer at agreed terms; \emph{command allocation} assigns goods by the decision of an office; an \emph{endowment} assigns the yield of a dedicated asset to stated purposes under a trustee; \emph{credit} assigns present goods against a promise of future repayment. Real procedures combine modes.
   118	\end{definition}
   119	
   120	The modes are a coding device, not a typology of societies. A Ju/'hoansi camp uses sharing norms and also recognizes ownership of arrows; a market economy uses property and exchange and also command allocation through public budgets; an Ottoman province combined command allocation, endowments, and tax farms that were a form of credit to the treasury.
   121	
   122	\begin{definition}[Allocation regime]
   123	\label{def:financial-power:allocation-regime}
   124	The \emph{allocation regime} of a polity at time $t$ is the tuple consisting of its settlement modes, the actors who hold control shares $s^{\pF}_{i,t}$ in them, the concentration $H_{\pF,t}$, the contestability $Q_{\pF,t}$, and the five couplings $C_{\pF n,t}$ for $n\in\{\pP,\pJ,\pI,\pC,\pW\}$.
   125	\end{definition}
   126	
   127	The control share $s^{\pF}_{i,t}$ is meant to be measured from documents rather than inferred from outcomes. Its observable components include asset shares, shares of bank credit, shares of output produced by state-owned enterprises, shares of the public budget under discretionary control, shares of procurement awards, and rights to collect rent or tribute. Contestability $Q_{\pF,t}$ is scored from open entry, competitive tendering, beneficial-ownership disclosure, independent audit, bankruptcy that actually binds, antitrust enforcement, and the independence of the monetary authority.
   128	
   129	\subsection{Concentration and its normalization}
   130	
   131	The index $H_{\pF,t}$ lies in $[1/n,1]$ for a polity of $n$ actors, with the lower bound attained only at equal shares. Comparisons across polities of different size therefore require normalization. We use
   132	\begin{equation}
   133	\label{eq:hstar}
   134	H^{*}_{\pF,t}=\frac{H_{\pF,t}-1/n}{1-1/n}\in[0,1],\qquad n\geq 2,
   135	\end{equation}
   136	which is zero at equal shares and one when a single actor holds everything. The financial term of the unaccountable-concentration index is $u_{\pF,t}=H_{\pF,t}(1-Q_{\pF,t})$, so that $U_t=\sum_m\omega_m u_{m,t}$ in the notation of \citet{largo2026hbs}. The term is small when control is dispersed or when concentrated control is open to effective challenge, and it approaches one only when one actor holds the resources and nobody can contest how they are used.
   137	
   138	\subsection{Subdomains and the aggregation gap}
   139	
   140	Financial control is not one thing. A polity's credit market, its land, its public budget, and its procurement system may each be held by different actors. Aggregating the subdomains into one share vector loses information in a precise way.
   141	
   142	\begin{proposition}[Aggregation gap]
   143	\label{prop:financial-power:aggregation-gap}
   144	Let the financial pillar consist of subdomains $k=1,\dots,K$ with weights $\beta_k\geq 0$, $\sum_k\beta_k=1$, and control-share vectors $s^{k}=(s^{k}_i)_{i\in N}$, each summing to one. Define the aggregate share $\bar s_i=\sum_k\beta_k s^{k}_i$. Then
   145	\begin{equation}
   146	\label{eq:aggregation-gap}
   147	\sum_{k=1}^{K}\beta_k H(s^{k})-H(\bar s)=\sum_{i\in N}\operatorname{Var}_\beta\bigl(s^{\cdot}_i\bigr)\geq 0,
   148	\end{equation}
   149	where $\operatorname{Var}_\beta(s^{\cdot}_i)=\sum_k\beta_k(s^{k}_i-\bar s_i)^2$ is the $\beta$-weighted variance of actor $i$'s share across subdomains. Equality holds if and only if every actor holds the same share in every subdomain of positive weight.
   150	\end{proposition}
   151	
   152	\begin{proof}
   153	The aggregate shares sum to one, since $\sum_i\bar s_i=\sum_k\beta_k\sum_i s^k_i=\sum_k\beta_k=1$, so $H(\bar s)$ is a valid concentration index. For a fixed actor $i$, the identity $\sum_k\beta_k(s^k_i)^2-\bigl(\sum_k\beta_k s^k_i\bigr)^2=\sum_k\beta_k(s^k_i-\bar s_i)^2$ is the usual decomposition of a second moment into a squared mean and a variance; it uses only $\sum_k\beta_k=1$. Summing over $i$ gives
   154	\[
   155	\sum_k\beta_k\sum_i(s^k_i)^2-\sum_i\bar s_i^{\,2}=\sum_i\operatorname{Var}_\beta(s^{\cdot}_i),
   156	\]
   157	which is \eqref{eq:aggregation-gap}. Each variance is nonnegative and vanishes exactly when $s^k_i=\bar s_i$ for every $k$ with $\beta_k>0$.
   158	\end{proof}
   159	
   160	\begin{example}[Separated and fused holdings]
   161	\label{ex:aggregation}
   162	Consider three actors and three equally weighted subdomains: land, credit, and the public budget. In a \emph{separated} configuration actor $k$ holds all of subdomain $k$. Each subdomain then has $H=1$, so the weighted mean of subdomain concentrations is $1$, while aggregate shares are $(1/3,1/3,1/3)$ and $H(\bar s)=1/3$. The gap is $2/3$. In a \emph{fused} configuration one actor holds all three subdomains, every index equals $1$, and the gap is $0$. The numbers are hypothetical; the point is that the aggregate index rates the separated polity as dispersed even though every subdomain is a monopoly.
   163	\end{example}
   164	
   165	The gap measures within-pillar specialization: it is large when different actors dominate different subdomains and zero when the same actors hold the same shares everywhere. It is therefore a within-pillar analogue of the cross-pillar integration that \citet{largo2026hbs} records with $C_{mn,t}$, but it is not that object, and Part VII owns the formal treatment of integration. The practical lesson is that a polity should be coded subdomain by subdomain, with the aggregate reported alongside the gap, since a low aggregate index can conceal monopolies that do not overlap.
   166	
   167	\section{Necessity of the financial pillar}
   168	\label{sec:necessity}
   169	
   170	\subsection{The derivation}
   171	
   172	The scarcity axiom alone does not imply that a collective must have a financial pillar. A group could in principle resolve every conflict by unregulated contest. The derivation therefore needs a second assumption that says what unsettled conflict costs, and it is better to state that assumption openly than to hide it inside the word ``persistence''.
   173	
   174	\begin{assumption}[Scarcity, pillar form]
   175	\label{ass:scarcity}
   176	Time is discrete, $t=1,2,\dots$, and $\mathcal{F}_{t-1}$ denotes the history up to the end of period $t-1$. On the event that the collective exists at the start of period $t$, a conflict in the sense of \cref{def:financial-power:allocation-problem} occurs in period $t$ with conditional probability at least $p>0$ given $\mathcal{F}_{t-1}$.
   177	\end{assumption}
   178	
   179	\begin{assumption}[Dissolution hazard]
   180	\label{ass:hazard}
   181	On the event that a conflict in period $t$ is unsettled, the collective dissolves in period $t$ with conditional probability at least $q>0$ given $\mathcal{F}_{t-1}$ and on the conflict being unsettled. Dissolution means that the collective ceases to make and enforce collective decisions as one body: it breaks into groups that no longer coordinate, or it suffers violence that ends cooperation.
   182	\end{assumption}
   183	
   184	At most one conflict is indexed per period; a period with several conflicts counts once, and \cref{ass:hazard} applies to any period that contains an unsettled conflict. Write $Y_T$ for the number of periods in $1,\dots,T$ with a conflict, $Z_T$ for the number of periods with an unsettled conflict, with the convention $Z_T/Y_T:=0$ when $Y_T=0$, and $S_T$ for the event that the collective survives through period $T$.
   185	
   186	\begin{proposition}[Necessity of the financial pillar]
   187	\label{prop:financial-power:necessity}
   188	Under \cref{ass:scarcity,ass:hazard}, for every horizon $T$ and every integer $k\geq 0$:
   189	\begin{enumerate}
   190	\item[(a)] $\Prob(S_T\cap\{Z_T\geq k\})\leq(1-q)^k$;
   191	\item[(b)] $\Prob(S_T\cap\{Y_T<pT/2\})\leq e^{-pT/8}$;
   192	\item[(c)] if the collective has no settlement procedure at all, so that $Z_T=Y_T$, then $\Prob(S_T)\leq(1-q)^{\lceil pT/2\rceil}+e^{-pT/8}$;
   193	\item[(d)] if $\Prob(S_T)\geq\nu>0$, then
   194	\[
   195	\Prob\Bigl(\frac{Z_T}{Y_T}\geq\frac{2k}{pT}\,\Big|\,S_T\Bigr)\leq\frac{(1-q)^k+e^{-pT/8}}{\nu}.
   196	\]
   197	\end{enumerate}
   198	In particular, a collective without a financial pillar cannot survive with probability bounded away from zero as the horizon grows, and in a collective that does survive with probability at least $\nu$ for every horizon, the share of conflicts settled by a recognized procedure converges to one in conditional probability.
   199	\end{proposition}
   200	
   201	\begin{proof}
   202	(a) Let $\tau_j$ be the period of the $j$-th unsettled conflict, with $\tau_j=\infty$ if there is none, and let $A_j$ be the event that $\tau_j\leq T$ and the collective survives period $\tau_j$. Set $A_0$ to be the sure event. A $j$-th unsettled conflict can occur only if the collective survived the $(j-1)$-th, so $A_j\subseteq A_{j-1}$. Conditional on the history before $\tau_j$ and on the conflict being unsettled, \cref{ass:hazard} gives survival probability at most $1-q$. Hence $\Prob(A_j)\leq(1-q)\Prob(\tau_j\leq T,\ \text{alive at }\tau_j)\leq(1-q)\Prob(A_{j-1})$, and by induction $\Prob(A_k)\leq(1-q)^k$. If the collective survives through $T$ and $Z_T\geq k$, then the $k$-th unsettled conflict occurred by $T$ and was survived, so $S_T\cap\{Z_T\geq k\}\subseteq A_k$.
   203	
   204	(b) Enlarge the probability space with independent uniform variables $U_1,U_2,\dots$ on $[0,1]$. By \cref{ass:scarcity}, the conflict indicator in period $t$ can be represented as $\mathbf{1}\{U_t\leq p_t\}$ for an $\mathcal{F}_{t-1}$-measurable $p_t\geq p$ while the collective exists; after dissolution, define the indicator as $\mathbf{1}\{U_t\leq p\}$. The extended count then satisfies $\tilde Y_T\geq B_T=\sum_{t\leq T}\mathbf{1}\{U_t\leq p\}$, which is binomial with mean $pT$, and $\tilde Y_T=Y_T$ on $S_T$. The multiplicative Chernoff bound for the lower tail of a binomial variable, $\Prob(B_T\leq(1-\delta)pT)\leq\exp(-\delta^2pT/2)$, with $\delta=1/2$ gives $\Prob(S_T\cap\{Y_T<pT/2\})\leq\Prob(B_T<pT/2)\leq e^{-pT/8}$.
   205	
   206	(c) If every conflict is unsettled, then on $S_T\cap\{Y_T\geq pT/2\}$ we have $Z_T\geq\lceil pT/2\rceil$, so by (a) that event has probability at most $(1-q)^{\lceil pT/2\rceil}$. Adding the bound in (b) for the complementary part of $S_T$ gives the claim.
   207	
   208	(d) On $S_T\cap\{Z_T<k\}\cap\{Y_T\geq pT/2\}$ we have $Z_T/Y_T<2k/(pT)$. The event in the numerator of the conditional probability is therefore contained in $(S_T\cap\{Z_T\geq k\})\cup(S_T\cap\{Y_T<pT/2\})$, whose probability is bounded by (a) and (b). Dividing by $\Prob(S_T)\geq\nu$ gives the inequality. Taking $k=\lceil\sqrt T\,\rceil$, the threshold $2k/(pT)$ and the bound both tend to zero as $T\to\infty$, which proves the final statement.
   209	\end{proof}
   210	
   211	The proposition is a conditions-of-persistence result. It says that collectives without a financial pillar do not last; it does not say that any particular collective acquired its pillar because the pillar helps it last. Elster's objection to functional explanation applies with full force here: an account of why an institution exists by reference to its beneficial effects requires a feedback mechanism from effect to cause, and none is asserted \citep{elster1983}. Hempel's objection also applies: from the need for a function nothing follows about which institution supplies it, since many functional equivalents can satisfy the same need \citep{hempel1959,merton1968}. The proposition is accordingly stated about the class of settlement procedures, not about property, markets, treasuries, or banks.
   212	
   213	\begin{example}[Survival without settlement]
   214	\label{ex:survival}
   215	Suppose, purely for illustration, that a band of foragers meets a conflict over some good in at least one week in ten ($p=0.1$), and that each unsettled conflict carries a five percent chance of permanent fission or lethal violence ($q=0.05$). If the band had no settlement procedure at all, \cref{prop:financial-power:necessity}(c) bounds its probability of surviving ten years ($T=520$ weeks) by $0.95^{26}+e^{-6.5}\approx 0.265$, and of surviving fifty years ($T=2600$) by $0.95^{130}+e^{-32.5}\approx 0.0013$. The parameters are invented; the geometric decay is not.
   216	\end{example}
   217	
   218	\subsection{Scope of the assumptions}
   219	
   220	The derivation rests on \cref{ass:hazard}, and its weak point is there. If unsettled conflicts were costless, so that $q=0$, a collective could persist while every carcass went to whoever seized it first, and the proposition would fail. Two replies narrow rather than remove this possibility. A practice in which the first taker keeps the good, known in advance and accepted by the others, is a settlement procedure in the sense of \cref{def:financial-power:settlement}: it applies to a class of situations, its outcome can be anticipated, and members comply with it. The case that escapes the proposition is therefore a collective whose members fight over goods without any shared expectation of the outcome and suffer no risk of dissolution from doing so. We know of no ethnographic description of such a collective, and the hard cases below suggest the opposite: the societies most often cited as lacking authority spend considerable effort settling claims on goods.
   221	
   222	The second weak point is the meaning of dissolution. Among mobile foragers, a camp can split and its members can join other camps without the wider society ending. If every split counted as dissolution, bands would dissolve constantly and the proposition would say little. The relevant collective is the unit that makes collective decisions, which for the Ju/'hoansi is a network of camps linked by kinship and exchange, not a single camp. A split that follows recognized lines of access, with people moving to places where they hold rights through kin, is itself a settlement procedure, since it assigns people to resources by a rule they anticipate. Fission along such lines is exit, and exit is part of the financial pillar when it reassigns access to land and water. For the same reason the proposition says nothing about transient aggregates such as crowds or short-lived coalitions, which make no collective decisions to sustain. Part VI owns the general treatment of exit and voice (Definition 2.5 of \citealt{long2026productive}).
   223	
   224	\subsection{Minimal forms in stateless and consensus societies}
   225	
   226	The societies that anthropology describes as egalitarian, acephalous, or organized against the state are the natural test set. Each exhibits the financial pillar in a form with no office, no treasury, and dispersed control, and none exhibits its absence.
   227	
   228	Among the Ju/'hoansi of the Kalahari, meat from a large animal is distributed according to rules that assign the role of distributor to the owner of the arrow that killed it, and arrows circulate as gifts, so that the distributor is often not the hunter \citep{marshall1976,lee1979}. Distribution follows kinship and camp membership, and a successful hunter who boasts is met with ritualized deprecation of the kill, which Lee describes as ``insulting the meat'' \citep{lee2013}. Wiessner's records of everyday talk show that criticism and complaint about failures to share are frequent and that they bring offenders back into line \citep{wiessner2005}. Each element meets \cref{def:financial-power:settlement}: the rules apply to every kill, their outcome can be anticipated, and compliance is enforced by others. Control shares are close to equal, so $H_{\pF}$ is close to $1/n$ and $H^{*}_{\pF}$ close to zero.
   229	
   230	Woodburn's comparison of immediate-return societies, including the Hadza, Mbuti, !Kung, and Batek, generalizes the point. These societies avoid storage and accumulation, make sharing obligatory, and maintain what Woodburn calls leveling mechanisms that prevent any member from converting a temporary advantage into lasting control \citep{woodburn1982}. The equality of these societies is an outcome that institutions produce and defend, not the absence of institutions. Boehm reaches the same conclusion from a broader comparative sample of foragers: egalitarian bands sustain equality through a reverse dominance hierarchy in which the group collectively sanctions would-be dominants, and enforcement of meat-sharing against hoarders is one of its recurring targets \citep{boehm1999}.
   231	
   232	The Nuer, whom Evans-Pritchard described as living in ordered anarchy without government, allocate cattle through kinship, bridewealth, and compensation for homicide \citep{evanspritchard1940}. The so-called leopard-skin chief has no coercive authority; he mediates feuds and helps arrange compensation in cattle, which the parties accept under the shadow of renewed feud. Here the financial pillar settles not only access to grazing and milk but also the price of peace between lineages, and it does so through a mediator without power to command. In the Amazonian societies that Clastres described, the obligation of the headman runs in the opposite direction from tribute: he is expected to be generous with his goods, and a headman who tries to command loses his followers \citep{clastres1987}. Clastres's thesis is that these societies actively prevent political power from separating from the group. That thesis is consistent with the necessity of the financial pillar and incompatible with any claim that its concentration is inevitable.
   233	
   234	Ostrom's studies of long-enduring common-pool resource institutions give the most direct evidence on how small groups settle conflicting claims without either a state or private property in the usual sense \citep{ostrom1990}. The design principles she identified include clearly defined boundaries of the resource and of its users, appropriation rules matched to local conditions, collective-choice arrangements in which those affected can modify the rules, monitoring, graduated sanctions, accessible conflict-resolution mechanisms, recognition of the users' right to organize, and nesting of small units within larger ones. A later review of empirical studies found the principles well supported, with some refinements \citep{cox2010}. In the vocabulary of this paper, a well-designed commons is an allocation regime with dispersed control and high contestability: users appropriate according to known rules, and those rules are themselves open to collective revision. Ellickson's study of ranchers in Shasta County shows a modern variant, in which neighbors settle damage from straying cattle by informal norms rather than by the formal law that nominally applies \citep{ellickson1991}.
   235	
   236	\begin{table}[t]
   237	\centering
   238	\small
   239	\caption{Minimal forms of the financial pillar in societies without a state. Each row reports the settlement procedure, the actors who hold control, and the strongest reading on which the function is absent.}
   240	\label{tab:minimal}
   241	\begin{tabularx}{\linewidth}{@{}L{2.3cm}YYY@{}}
   242	\toprule
   243	Case & Settlement procedure & Holders of control & Strongest counter-reading \\
   244	\midrule
   245	Ju/'hoansi & Arrow-owner rule for meat, gift exchange, demand sharing & All adults, with distributors rotating as arrows circulate & No office allocates anything, but the rules allocate every kill \\
   246	Immediate-return foragers & Obligatory sharing and avoidance of storage & The camp as a whole through leveling sanctions & Little is stored, but what is acquired is still shared by rule \\
   247	Nuer & Cattle rights, bridewealth, and homicide compensation & Lineages, with a mediator who cannot command & No government exists, yet compensation in cattle settles feuds \\
   248	Amazonian groups & The headman's obligatory generosity & The group, which withholds support from a commanding headman & Power is prevented from separating, not allocation from occurring \\
   249	Ostrom commons & Boundaries, appropriation rules, monitoring, and graduated sanctions & Users acting through collective-choice arrangements & No owner or state controls the resource, but the users' rules do \\
   250	\bottomrule
   251	\end{tabularx}
   252	\end{table}
   253	
   254	\Cref{tab:minimal} summarizes the cases. In every row the function is present and its holders are many. The cases thus support the necessity claim and, at the same time, the claim that concentration is contingent. Two cautions apply. Ethnographies of foragers describe groups observed in marginal environments and under the influence of neighbors and states, and foraging societies differ widely among themselves \citep{kelly1995}. Graeber and Wengrow argue further that many early societies moved between hierarchical and egalitarian arrangements, sometimes seasonally, and deliberately chose among political forms \citep{graeber2021}. Neither caution weakens the necessity claim, which requires only that some settlement procedure exist; both strengthen the claim that its concentration is a matter of choice and circumstance.
   255	
   256	\subsection{Counterexample attempts}
   257	
   258	The strongest is Sahlins's ``original affluent society'' \citep{sahlins1972b}. If foragers' wants are limited and easily satisfied, the argument runs, there is no scarcity and so no allocation problem. The reply is that \cref{ass:scarcity} concerns conflicting claims, not shortage. Foragers who spend few hours obtaining food still divide each large kill among claimants who cannot all receive the best portions, and the elaborate sharing rules recorded by Marshall and Lee exist precisely because claims on particular goods conflict \citep{marshall1976,lee1979}. Sahlins's argument, if accepted, lowers $p$; it does not make it zero.
   259	
   260	A second attempt appeals to markets. In a pure market economy, on this view, nobody allocates: prices do. But prices settle conflicts only against a background of property rules that say who may sell what, and those rules are made, interpreted, and enforced by other pillars. Allocation by price is a settlement procedure of the property-and-exchange mode, and control shares in it are given by the distribution of endowments. The market answer to the guiding question is ``whoever owns,'' which is an answer, not a dissolution of the question.
   261	
   262	A third attempt imagines post-scarcity abundance through automation. It fails twice: no existing governance system satisfies it, and even a society with abundant manufactured goods would allocate land, energy, computation, and attention, which remain finite and contested.
   263	
   264	The case that narrows the claim is the one already identified: a collective in which unsettled conflicts carry no risk of dissolution. The falsifier for the financial pillar's necessity is therefore precise. It is a persistent collective whose members hold conflicting claims on some good and resolve them predominantly without any procedure in the sense of \cref{def:financial-power:settlement}. We found no documented case in the sources reviewed (cutoff October 2026).
   265	
   266	\subsection{Necessity without concentration}
   267	
   268	The necessity of the financial pillar implies nothing about how its control is distributed or how open it is to challenge. The next result makes this exact at the level of the pillar; Part VII proves the corresponding non-implication for all six pillars together.
   269	
   270	\begin{proposition}[Pillar-level non-implication]
   271	\label{prop:financial-power:nonimplication}
   272	Fix $n\geq 2$. For every $h\in[1/n,1]$ there is a control-share vector $s$ on $n$ actors with $H(s)=h$. Consequently, for every $h\in[1/n,1]$ and every $c\in[0,1]$ there is an allocation regime in which the financial pillar exists, $H_{\pF}=h$, and $Q_{\pF}=c$, and the financial term $u_{\pF}=H_{\pF}(1-Q_{\pF})$ takes every value in $[0,1]$.
   273	\end{proposition}
   274	
   275	\begin{proof}
   276	For $a\in[1/n,1]$ let $s(a)$ give share $a$ to one actor and $(1-a)/(n-1)$ to each of the others. Then $H(s(a))=a^2+(1-a)^2/(n-1)$, which is continuous in $a$, equals $1/n$ at $a=1/n$, and equals $1$ at $a=1$. By the intermediate value theorem every $h\in[1/n,1]$ is attained. Contestability is scored from features (disclosure, audit, entry, appeal) that the share vector does not determine, so any $c\in[0,1]$ can be paired with any $h$; existence of the pillar requires only that some settlement procedure operate, which it does under any share vector. Finally $u_{\pF}=h(1-c)$ equals $0$ at $c=1$ and equals $h$ at $c=0$, so taking $h=1$ and letting $c$ range over $[0,1]$ attains every value in $[0,1]$.
   277	\end{proof}
   278	
   279	The proposition is elementary, and its role is to block a common inference. That every polity has someone who controls resources is a structural fact. That some polity's resource control is concentrated and unaccountable is an empirical claim about $H_{\pF}$, $Q_{\pF}$, and the couplings $C_{\pF n}$, which requires evidence of the kind \citet{largo2026hbs} specifies for capture links. The rest of this paper is about that evidence.
   280	
   281	\section{Literature on financial power}
   282	\label{sec:literature}
   283	
   284	Research on resource command and political power has developed along four lines that rarely meet. Each supplies a mechanism the financial pillar needs, and each has a rival literature that limits it.
   285	
   286	The economic theory of regulation asks how resource holders shape the rules that govern them. Stigler's theory of economic regulation treats regulation as a good demanded by industries and supplied by the state, so that regulatory agencies tend to serve the regulated \citep{stigler1971}. Peltzman generalized the model: a regulator balances producer and consumer pressure, so outcomes fall between pure capture and pure public interest \citep{peltzman1976}. Becker showed that competition among pressure groups limits the transfers any one group can extract, because deadweight losses grow with the size of the transfer and mobilize the losers \citep{becker1983}. Laffont and Tirole recast capture as a principal-supervisor-agent problem in which the danger of collusion between the supervisor and the regulated firm shapes the optimal design of incentives \citep{laffont1991}. Grossman and Helpman modeled trade protection as the outcome of contribution schedules offered to an incumbent government \citep{grossman1994}. Dal B\'o surveys the theory and evidence \citep{dalbo2006}, and Carpenter and Moss insist on a demanding definition: capture requires showing that regulation was directed away from the public interest and toward the regulated industry by the industry's own intent and action, not merely that the industry benefited \citep{carpentermoss2014}. That standard is the same one the capture link of \citet{largo2026hbs} encodes.
   287	
   288	Rent-seeking theory measures the costs of the contest itself. Tullock observed that resources spent to obtain or defend monopolies and tariffs are a social cost beyond the usual deadweight triangle \citep{tullock1967}; Krueger named the activity rent seeking and estimated its scale in licensing regimes \citep{krueger1974}; Posner argued that competition for rents can dissipate them entirely \citep{posner1975}. Olson supplied the organizational asymmetry that makes such contests one-sided: small groups with concentrated stakes organize more readily than large groups with diffuse ones \citep{olson1965}. These works explain why concentrated resource control tends to seek conversion into rule-making power. They do not show that the conversion succeeds, and direct studies of influence suggest that it often does not.
   289	
   290	Those studies concern democracies, and they divide sharply. Lindblom argued that business holds a privileged position because governments depend on private investment for the prosperity on which they are judged \citep{lindblom1977}. Przeworski stated the same dependence as a dilemma for electoral socialism: a party that threatens profits risks the investment its program needs \citep{przeworski1985}. Mills described an interlocking economic, political, and military elite in the postwar United States \citep{mills1956}, and Winters defines oligarchy by the political work of wealth defense, which he traces from Athens and Rome to the modern United States \citep{winters2011}. Against these accounts, Ansolabehere, de Figueiredo, and Snyder find that campaign money in the United States is small relative to the value of government policy and behaves more like consumption than investment \citep{ansolabehere2003}, and Baumgartner and colleagues find, in a large sample of issues, that the side with more resources often fails to win \citep{baumgartner2009}. Mizruchi documents the fragmentation of the American corporate elite after the 1970s, which cuts against claims of a unified business class \citep{mizruchi2013}. Gilens and Page's finding that economic elites and organized business interests have substantial independent influence on policy while average citizens have little \citep{gilens2014} is disputed by Branham, Soroka, and Wlezien, who show that the preferences of the affluent and the middle class differ on relatively few issues and that the affluent win only modestly more often when they do differ \citep{branham2017}. Culpepper offers a reconciliation: business power is strongest in quiet politics, on technical issues of low public salience \citep{culpepper2010}.
   291	
   292	Political economists of the state study the relation between rulers and the resources they command. Kornai's soft budget constraint describes a paternalistic state that rescues loss-making enterprises, so that the enterprises' expectations of rescue erode the discipline of the budget \citep{kornai1986,kornai1992}. North, Wallis, and Weingast describe limited-access orders in which the dominant coalition creates rents for its members and so binds them to keep the peace, and open-access orders in which entry into economic and political organization is impersonal \citep{nww2009}. The rentier-state literature, originating with Mahdavy's study of Iran and developed by Beblawi and Luciani, holds that states living on external rents need not bargain with taxpayers \citep{mahdavy1970,beblawiluciani1987}; Ross tests the claim cross-nationally \citep{ross2001,ross2012}, and Haber and Menaldo find that the association between resource wealth and authoritarianism does not survive within-country analysis over long time series \citep{habermenaldo2011}. Levi models rulers as revenue maximizers constrained by their bargaining power, transaction costs, and discount rates, and argues that compliance is quasi-voluntary when taxpayers believe others also pay and the ruler keeps its bargains \citep{levi1988}. Tilly traces European state formation along capital-intensive and coercion-intensive paths, in which rulers obtained the means of war either from merchants and cities or by direct extraction from the land \citep{tilly1990}. This paper owns the financing side of that fiscal-military account; Part V treats its coercive side \citep{long2026coercive}.
   293	
   294	Two normative and sociological works connect these lines to the cross-pillar question. Walzer defines tyranny as the conversion of dominance in one sphere of distribution into dominance in another, as when wealth buys office or office buys wealth \citep{walzer1983}. Bourdieu treats economic, cultural, social, and symbolic capital as convertible into one another at rates that are themselves objects of struggle \citep{bourdieu1989}. Both supply a vocabulary for what the multiplex model measures with the couplings $C_{\pF n}$: the degree to which control of resources carries control of rules, rulings, beliefs, sanctions, and work. Mann's model of ideological, economic, military, and political networks of power is the nearest precedent for a pluralist decomposition of social power \citep{mann1986}; Part IV presents it in full and compares it with the six-pillar scheme \citep[Section 4]{long2026ideological}.
   295	
   296	The capture literature tests resource-to-rule conversion mostly in one regime type, the market democracy, and the literatures on party-states, rentier states, and early modern fiscal states each describe resource command within one regime family. None places the universal allocation function, its necessity, and its regime-specific distribution in a single frame with common measures. That frame is what the six-pillar model provides, and the comparison below applies it.
   297	
   298	\section{Comparative analysis across six regime types}
   299	\label{sec:comparative}
   300	
   301	The six regime types of the series span two institutional dimensions rather than six exclusive categories. Market capitalism and social democracy describe how an economy organizes ownership, bargaining, and allocation; secular democracy describes how a constitution separates, delegates, and reviews authority over resources. Communist party-states, Islamic states, and the Catholic monarchies of early modern Europe combine a position on each dimension with a distinctive source of legitimacy. A single polity can therefore be coded on both dimensions, and most contemporary market-capitalist and social-democratic polities are also secular democracies. Each subsection below examines which institutions hold the financial pillar, how concentrated and contestable control is, how the pillar is coupled to the other five, what preserves accountability, and which capture episodes and checks are documented.
   302	
   303	No polity has yet been coded under a preregistered protocol, so no numerical value of $H_{\pF}$, $Q_{\pF}$, $U_t$, or $\Integ_t$ is reported for any real case. Statements that a value is high or low are hypotheses about what such coding would find.
   304	
   305	\subsection{Market-capitalist societies}
   306	
   307	In market-capitalist societies the financial pillar is held mainly by private owners of capital, by banks and other financial intermediaries, by corporations, and by institutional investors, with a central bank controlling the supply of money and a state controlling a public budget. The dominant settlement mode is property and exchange, supplemented by command allocation through taxation and public spending. Control shares within subdomains can be highly concentrated: Piketty documents long periods in which the return on capital exceeded the growth rate and wealth concentration rose \citep{piketty2014}. Aggregate concentration across all actors is lower than within subdomains, which is the aggregation gap of \cref{prop:financial-power:aggregation-gap} at work.
   308	
   309	The characteristic coupling is $C_{\pF\pP}$, the conversion of resources into influence over rule-making, which \citet{largo2026hbs} calls the wealth-to-rules pathway. Evidence that the pathway operates is substantial. Igan, Mishra, and Tressel find that lenders who lobbied more intensively before the 2008 crisis made riskier loans and performed worse in the crisis \citep{igan2012}. Mian, Sufi, and Trebbi find that campaign contributions from the financial industry predicted congressional votes on the major housing and financial legislation of 2008, alongside constituents' mortgage distress \citep{mian2010}. Kalla and Broockman show experimentally that disclosing a constituent's status as a donor increased access to senior congressional officials \citep{kalla2016}. Bertrand, Bombardini, and Trebbi, and Blanes i Vidal, Draca, and Fons-Rosen, show that lobbyists' value depends heavily on their personal connections to officeholders, a revolving-door effect \citep{bertrand2014,blanes2012}. Faccio finds politically connected firms in many countries, more often where corruption is higher \citep{faccio2006}. Hacker and Pierson attribute the rise of top incomes in the United States to organized political combat over taxation and regulation \citep{hackerpierson2010}, and Bartels finds senators more responsive to affluent constituents \citep{bartels2008}.
   310	
   311	The counter-evidence is as substantial. Access is not outcome: Hall and Deardorff model lobbying as a subsidy of information and labor to legislators who already agree with the lobbyist \citep{hall2006}, which implies influence over agenda and detail more than over direction. The findings of Ansolabehere and colleagues, of Baumgartner and colleagues, and of Branham, Soroka, and Wlezien cited in \cref{sec:literature} show that money is small relative to stakes, that resource advantages often lose, and that the rich win mainly when their preferences coincide with those of the middle class. Mizruchi's account of elite fragmentation suggests that $\Integ_t$ for the American business community has declined rather than risen \citep{mizruchi2013}.
   312	
   313	Accountability in this regime type rests on open entry, antitrust law, disclosure of contributions and lobbying, competitive procurement, judicial review of regulation, a free press, and elections. Contestability is therefore high on paper, and the open empirical question is how much of it binds in quiet, technical domains, where Culpepper finds business power strongest \citep{culpepper2010}. Capture and its checks are both documented. The best documented capture episode in the sources reviewed is pre-crisis financial regulation, where both the lobbying evidence and the outcome evidence point in the same direction. The best documented checks are the frequent defeats of well-funded interests and the electoral reversals of policy that the pluralist literature records.
   314	
   315	The couplings $C_{\pF\pI}$, through sponsorship of research and ownership of media, and $C_{\pF\pJ}$, through the resources that let repeat players litigate, are plausible but less systematically measured. Part III analyzes the contest between repeat players and occasional litigants (Proposition 4.3 of \citealt{long2026judicial}), and Part IV shows that endorsements from captured authorities carry no information (Proposition 2.9 of \citealt{long2026ideological}).
   316	
   317	\subsection{Communist party-states}
   318	
   319	In the communist party-state the financial pillar is held by planners and ministries, by state banks, and by managers of state enterprises appointed through the party's personnel system. The dominant settlement mode is command allocation, with property and exchange confined to permitted margins. Formal concentration is extreme, since the state owns the principal means of production and the party controls appointments to the posts that allocate them. Kornai's account of the classical socialist system makes the party's monopoly of power the defining feature from which the economic features follow \citep{kornai1992}. In the terms of \citet{largo2026hbs}, the control path runs from appointment to allocation rather than from wealth to rules, and the coupling $C_{\pP\pF}$ is near its maximum by design. Part II owns the appointment channel (Definition 2.8 of \citealt{long2026political}); here we record its financial consequences.
   320	
   321	Formal concentration overstates effective concentration. Gregory's study of the Soviet archives shows that the top leadership could not allocate everything and bargained constantly with ministries and enterprises that held better information about their own capacities \citep{gregory2004}. Berliner's interviews with former Soviet managers documented the informal procurement agents who obtained scarce inputs outside the plan, and the networks of favors through which managers met targets \citep{berliner1957}; Ledeneva reconstructed the economy of favors, known as blat, that ran alongside the formal allocation of goods in the late Soviet period \citep{ledeneva1998}. These informal channels lowered effective concentration while also lowering contestability, since favors were by nature unrecorded and unreviewable. Kornai's soft budget constraint completes the picture: enterprises expected rescue from their administrative superiors, so loss did not lead to exit, and the allocation of credit followed bargaining power rather than performance \citep{kornai1986}.
   322	
   323	The reform-era People's Republic of China shows that the regime type admits wide variation. A large private sector emerged and came to produce much of output and employment \citep{lardy2014,naughton2007}. The banking system nevertheless remained dominated by state-owned banks whose senior executives are appointed through the party's personnel system, and Walter and Howie describe the resulting financial structure as serving party priorities \citep{walterhowie2011}. Allen, Qian, and Qian observe that China grew rapidly despite a formal legal and financial system weaker than standard theory would predict, and attribute much of the growth to firms financed through informal and alternative channels \citep{allen2005}. Milhaupt and Zheng argue that ownership is a poor guide to control, because large private firms are also tied to the party-state through their founders' political memberships and their dependence on state support \citep{milhaupt2015}. Cross-nationally, La Porta, L\'opez-de-Silanes, and Shleifer associate government ownership of banks with slower subsequent financial development \citep{laporta2002}, and Shleifer and Vishny model politicians' use of state firms to deliver employment and patronage \citep{shleifer1994}.
   324	
   325	Accountability in the classical system ran through the party's own control organs, so contestability against the party itself was low. Documented capture episodes include the bargaining and soft budgets that Kornai describes, which transferred resources to enterprises and officials with bargaining power. The transition from communism produced the clearest cases of reciprocal capture in the comparative record. Hellman found that early winners from partial reform blocked further reform that would have dissipated their rents \citep{hellman1998}; Hellman, Jones, and Kaufmann defined state capture as firms shaping the basic rules of the game through private payments to officials \citep{hellman2000}; Black, Kraakman, and Tarassova describe insider privatization in Russia \citep{black2000}; and Guriev and Rachinsky document the concentration of Russian industrial ownership among a small number of owners \citep{guriev2005}. Treisman argues that the conventional account of the loans-for-shares auctions overstates their role in that concentration \citep{treisman2010}, a reminder that even the canonical episode is contested. The documented checks within the regime type are the hard budget constraints that reform introduced in some sectors and the competition from non-state firms that limited the rents of state incumbents.
   326	
   327	\subsection{Social democracy and market socialism}
   328	
   329	In social democracies the financial pillar is mixed. Private capital owns most productive assets, but high taxation, a large public budget, public pension funds, and corporatist bargaining among employers, unions, and the state give organized labor and the state substantial shares of decision-relevant control. Korpi's power-resources theory explains the configuration as the product of labor's organizational strength, which allowed it to win through democratic politics what it could not win through ownership \citep{korpi1983}. Esping-Andersen traces how social democratic parties used state power to reduce workers' dependence on the market \citep{esping1985}, and Berman locates the movement's origin in a commitment to the primacy of politics over markets \citep{berman2006}. Hall and Soskice classify the economies that developed from these settlements as coordinated market economies, in which firms solve problems of training, finance, and wage setting through non-market institutions \citep{hallsoskice2001}.
   330	
   331	Social democracy combined high taxation with remarkably concentrated private ownership. H\"ogfeldt shows that Swedish corporate control was held through pyramids and dual-class shares by a few families and foundations, of which the Wallenberg sphere was the largest, and argues that social democratic governments tolerated this concentration as a stable partner for investment and employment \citep{hogfeldt2005}. Subdomain concentration in the ownership of large firms was therefore high, while the public budget, pensions, and wage setting were held by other actors. That is the separated configuration of \cref{ex:aggregation}, with a large aggregation gap.
   332	
   333	The most direct attempt to change who held the financial pillar was the Swedish proposal for wage-earner funds, which would have transferred a growing share of corporate equity to funds controlled by the labor movement. Pontusson's account shows how employers mobilized against the proposal, how the enacted version was diluted, and how the episode revealed the limits of social democratic power over investment \citep{pontusson1992}. Przeworski's dilemma predicts exactly this limit: a democratic government that threatens the returns to capital faces the possibility that investment falls \citep{przeworski1985}. Streeck argues that later decades shifted power from citizens to creditors as states financed themselves through debt \citep{streeck2014}.
   334	
   335	The couplings characteristic of this type are $C_{\pF\pW}$ and $C_{\pF\pP}$, but they take a bargained rather than a captured form: organized capital and organized labor both hold seats in the arenas where wages, pensions, and investment rules are set. Accountability rests on electoral competition, on the countervailing power of unions, and on transparency norms. Scheve and Stasavage show that the high progressive taxation of the twentieth century followed mass mobilization for war and arguments for fair compensation rather than democracy as such \citep{scheve2016}. We found fewer documented capture episodes for this type in the sources reviewed (cutoff October 2026). The main candidate is the entrenchment of concentrated family control that H\"ogfeldt describes, which social democratic governments accepted in exchange for investment \citep{hogfeldt2005}. The documented check is that labor's organized power repeatedly reversed advantages that capital held, which is one of the four findings that \citet{largo2026hbs} lists as undermining a strong capture thesis.
   336	
   337	\subsection{Islamic states}
   338	
   339	Islamic states are polities whose rulers derived legitimacy in substantial part from religious law, and they differ widely among themselves: the early caliphates, the Ottoman Empire, the Safavid and later Iranian states, and modern Saudi Arabia and the Islamic Republic of Iran organized resource command in very different ways. Islam here is a source of political legitimacy in specific historical states, not an essence that determines their economic institutions.
   340	
   341	Classical Islamic law supplied several settlement modes at once. The treasury, the bayt al-m\=al, held public revenues under the ruler's control. The obligatory alms tax, zak\=at, assigned a share of certain kinds of wealth to specified categories of recipients. The waqf, a perpetual endowment, dedicated the yield of an asset to purposes fixed by its founder under a trustee, and the qadi courts supervised its administration. Partnership forms, especially the commenda contract known as qir\=ad or mu\d{d}\=araba, organized long-distance trade \citep{udovitch1970,cizakca1996}. Singer describes how endowments financed mosques, schools, hospitals, and public kitchens across Ottoman and wider Islamic societies \citep{singer2008}. Kuran argues that the waqf provided public goods while protecting wealth from expropriation by rulers, and that its rigidity, together with features of Islamic partnership and inheritance law, limited the development of durable commercial organizations \citep{kuran2001,kuran2004,kuran2011}. The thesis is contested. Rubin attributes the divergence between Western Europe and the Middle East less to the content of Islamic law than to the role of religious authorities in legitimating rulers \citep{rubin2017}, and Kuru locates the cause in an alliance between the ulama and the state that took shape in the eleventh century \citep{kuru2019}. These accounts disagree about causes; they agree that the distribution of the financial pillar among rulers, jurists, endowments, and merchants shaped later development.
   342	
   343	The Ottoman Empire illustrates a fiscal regime built on command allocation and credit. Karaman and Pamuk show that Ottoman central revenues per capita fell behind those of the leading European states in the seventeenth and eighteenth centuries and that the state relied increasingly on tax farming, including life-term tax farms, which converted future revenues into present credit from local and provincial elites \citep{karaman2010}. In a comparative study they relate the different paths of European and Ottoman fiscal development to the interaction of warfare, economic structure, and political regime \citep{karaman2013}. Pamuk's monetary history records the use of debasement as a revenue source in fiscal crises \citep{pamuk2000}. Tax farming dispersed the collection of revenue among many holders, lowering $H_{\pF}$, while coupling it tightly to local political and coercive power.
   344	
   345	Modern Islamic states are mostly rentier states, and their allocation regimes are shaped by oil more than by religious law. Hertog describes the Saudi state as a set of fiefdoms and brokerage networks built around royal patrons, alongside islands of efficient bureaucracy such as the national oil company \citep{hertog2010}. Chaudhry contrasts the institutional erosion that oil wealth produced in Saudi Arabia with the different path of labor-exporting Yemen \citep{chaudhry1997}, and Vitalis reconstructs the corporate and political entanglements of the American oil company in the early Saudi state \citep{vitalis2007}. In the Islamic Republic of Iran, revolutionary foundations known as bonyads control large economic assets outside the ordinary budget, and the Revolutionary Guards developed substantial business interests, including construction and engineering firms \citep{maloney2015,wehrey2009}. That fusion of financial and coercive control is the coupling $C_{\pF\pC}$ in its most direct form; Part V treats the coercive side. El-Gamal argues that much of modern Islamic finance replicates conventional instruments in legally permissible form, so that its religious label says little about how control is distributed \citep{elgamal2006}.
   346	
   347	Accountability varied with the type of state. Qadi supervision of endowments, the jurists' claim to interpret the law independently of rulers, and the commercial courts all provided checks in classical and Ottoman settings, although Kuran records that rulers did at times confiscate endowments \citep{kuran2001}. In modern rentier states the rentier argument predicts weak fiscal bargaining because the state does not depend on taxpayers \citep{beblawiluciani1987,ross2001}, but the within-country evidence of Haber and Menaldo cautions against treating oil as a sufficient cause \citep{habermenaldo2011}. Documented capture episodes include the off-budget concentration of assets in Iran's foundations and security forces; documented checks include the juristic independence that endowment supervision required and the variation across Islamic polities that rules out any single Islamic allocation regime.
   348	
   349	\subsection{Catholic monarchies of early modern Europe}
   350	
   351	In the Catholic monarchies of early modern Europe, royal authority was intertwined with the Church, and the financial pillar was distributed among the crown's fiscal apparatus, private bankers who lent to the crown, the Church with its lands and tithes, and officeholders who had bought their posts. Habsburg Spain, Bourbon France, and the Papal States organized these elements differently, and Gallican and ultramontane traditions disagreed about the Church's relation to royal finance. Catholicism here, like Islam in the preceding subsection, is a source of political legitimacy in specific states, not a determinant of their institutions.
   352	
   353	Habsburg Spain under Philip II is the best studied case of sovereign credit in the period. The crown borrowed heavily from Genoese and other bankers through short-term contracts called asientos and long-term bonds called juros, and it suspended payments on several occasions. Drelichman and Voth show that lending nevertheless continued, that the bankers earned positive returns overall, and that the payment stops are better read as excusable defaults in bad fiscal states, followed by negotiated settlements, than as predation \citep{drelichman2011,drelichman2014}. Conklin models the relationship as a repeated game in which the bankers' capacity to act together disciplined the crown \citep{conklin1998}. The coupling $C_{\pF\pC}$ was strong, since the debt financed war, while $C_{\pF\pP}$ ran through the Cortes of Castile, whose consent was needed for important taxes and which therefore constrained the crown's capacity to pledge revenue. \Cref{prop:financial-power:sovereign-credit} in \cref{sec:mechanisms} gives the formal condition.
   354	
   355	Bourbon France combined a royal fiscal system with extensive sale of offices and tax farming. Doyle describes venality as the sale of offices that became the heritable property of their holders, so that judges and financial officials owned their posts \citep{doyle1996}. Kwass shows how privilege sorted subjects for taxation and how new direct taxes provoked eighteenth-century disputes over liberty and equality \citep{kwass2000}. Velde and Weir analyze the crown's borrowing through life annuities and other instruments before 1789 \citep{velde1992}, and Hoffman, Postel-Vinay, and Rosenthal reconstruct a large private credit market organized by Parisian notaries \citep{hoffman2000}. The essays collected by Hoffman and Norberg compare how fiscal crises interacted with representative institutions across European states \citep{hoffmannorberg1994}. Venality made the financial pillar less concentrated and less contestable at once: offices were dispersed across many holders, but holders could not be removed except by reimbursement, and the coupling between $\pF$ and $\pJ$ was direct because judicial offices were purchased.
   356	
   357	The Papal States and the finances of the papacy give the case of fusion between financial and spiritual authority. Prodi describes the pope as both head of the Church and territorial prince, with a fiscal and administrative apparatus that anticipated features of other early modern states \citep{prodi1987}. De Roover's history of the Medici bank documents its role as depository of the papal Camera \citep{deroover1963}, and Padgett and Ansell show how the Medici built power in Florence through overlapping networks of marriage, business, and patronage \citep{padgett1993}, which is a historical multiplex in exactly the sense of \citet{largo2026hbs}. Ekelund and colleagues interpret the medieval Church as an economic firm that sought rents \citep{ekelund1996}; the interpretation is contested, and we cite it as one reading of the evidence rather than as an established result.
   358	
   359	Accountability in these monarchies rested on representative bodies such as the Cortes and the Parlements, on the repeated-game discipline that lenders imposed, on ecclesiastical immunities that sometimes protected Church wealth from the crown and sometimes protected the crown's allies, and on conflict between crown and Church. Documented capture episodes include the conversion of financial office into judicial office through venality. Documented checks include the Cortes' control over new taxes in Castile and the bankers' capacity to withhold further credit.
   360	
   361	\subsection{Secular democracies}
   362	
   363	Secular democracies distribute authority among elected officials, courts, independent agencies, and private institutions, and justify it without reference to religious law. The financial pillar in such polities includes private holders, as in the first and third types, together with public institutions designed to be insulated from the elected government: an independent central bank, a supreme audit institution, competition authorities, and procurement and disclosure regimes. The distinctive feature of the type is constitutional: it separates the holders of different financial subdomains and places some of them beyond the direct reach of elected officials.
   364	
   365	Central bank independence is the clearest example of delegated financial authority. Alesina and Summers found that more independent central banks were associated with lower and more stable inflation, without a corresponding cost in real growth \citep{alesina1993}. Goodhart traces the evolution of central banks from government bankers to institutions charged with monetary stability and the supervision of banks \citep{goodhart1988}. Delegation raises contestability against elected officials, who can no longer finance spending by printing money, but it concentrates control of the monetary subdomain in a small technocratic body. Whether delegation reduces unaccountable concentration or relocates it is therefore an empirical question about the review that independent agencies themselves face, through legislative oversight, published reasoning, and judicial review.
   366	
   367	Secular democracies also build disclosure and review into the coupling $C_{\pF\pP}$. Lobbying registers, contribution limits, beneficial-ownership registers, and competitive procurement aim to make the wealth-to-rules pathway visible and contestable; \citet{largo2026hbs} lists them among redesign measures. The revolving-door evidence cited above shows that personal connections still carry value \citep{blanes2012,bertrand2014}, and Carpenter and Moss collect designs intended to prevent capture, including procedural requirements, external review, and the deliberate building of countervailing expertise \citep{carpentermoss2014}. Rajan and Zingales show that financial development in many countries reversed between the early twentieth century and the postwar decades, and argue that incumbent firms and financiers oppose financial development when it would admit competitors \citep{rajan2003}. Their result implies that constitutional separation does not by itself prevent incumbents from using political influence to close entry.
   368	
   369	Accountability in this type is the highest on paper, because the review of financial decisions is spread across courts, legislatures, auditors, and the press. The documented capture episodes are those of the first type, since most secular democracies are also market economies, and their characteristic form is quiet influence on technical rules. The documented checks are the binding constraints that independent agencies, courts, and elections impose, including judicial invalidation of regulations and the electoral replacement of governments that have favored concentrated interests. Scheve and Stasavage show that democracies do not automatically tax the rich more heavily \citep{scheve2016}, which is a reminder that constitutional design shapes the distribution of financial control without determining it.
   370	
   371	\subsection{Summary of the comparison}
   372	
   373	\Cref{tab:regimes} collects the comparison. Every row has a financial pillar, which is the necessity claim; the rows differ in who holds it, how it is coupled, and what checks it, which is where the contingent capture claim must be tested.
   374	
   375	\begin{table}[t]
   376	\centering
   377	\small
   378	\caption{The financial pillar across the six regime types. Coupling entries are hypotheses about which pairs a preregistered coding would find strongest, not measured values.}
   379	\label{tab:regimes}
   380	\begin{tabularx}{\linewidth}{@{}L{2.2cm}YL{2.1cm}Y@{}}
   381	\toprule
   382	Regime type & Typical holders of control & Strongest couplings & Main sources of accountability \\
   383	\midrule
   384	Market capitalism & Private owners, banks, corporations, and a central bank & $C_{\pF\pP}$, $C_{\pF\pI}$, $C_{\pF\pJ}$ & Open entry, antitrust, disclosure, courts, and elections \\
   385	Communist party-state & Planners, state banks, and managers appointed by the party & $C_{\pP\pF}$ and $C_{\pF\pC}$ & Mainly the party's own control organs, with informal bargaining \\
   386	Social democracy & Private owners alongside unions, public funds, and the state budget & $C_{\pF\pW}$ and $C_{\pF\pP}$ & Elections, organized labor, and transparency norms \\
   387	Islamic states & Treasuries, endowment trustees, merchants, tax farmers, and rentier states & $C_{\pF\pC}$ and $C_{\pF\pI}$ & Qadi supervision and juristic independence, varying widely by state \\
   388	Catholic monarchies & The crown, its bankers, the Church, and owners of venal offices & $C_{\pF\pC}$ and $C_{\pF\pJ}$ & Representative assemblies, lenders' discipline, and Church-crown conflict \\
   389	Secular democracies & Private holders with independent central banks, auditors, and regulators & $C_{\pF\pP}$ in quiet, technical domains & Delegated review, courts, legislatures, and the press \\
   390	\bottomrule
   391	\end{tabularx}
   392	\end{table}
   393	
   394	Three results of the comparison bear on the series' thesis. The financial pillar is present in every type and in every case examined, held by institutions that have almost nothing else in common. The control path differs by regime as \citet{largo2026hbs} predicts: wealth to rules in market societies, appointment to allocation in party-states, bargaining between organized interests in social democracies, ruler to rent in rentier states, and lender to ruler in early modern fiscal states. And every type has both documented capture episodes and documented checks, so the type alone does not settle whether a polity's financial pillar is captured. That question requires coding a particular polity in a particular period.
   395	
   396	\section{Mechanisms, failure modes and checks}
   397	\label{sec:mechanisms}
   398	
   399	Coordination in the financial pillar becomes capture when three conditions of the capture link hold together \citep{largo2026hbs}: an actor obtains privileged access or discretion over allocation, the privilege weakens the accountability or contestability that would otherwise apply, and material evidence ties the asymmetry to an output such as a rule, a credit decision, a contract, or an exemption. Large holdings, profitable lending, and political donations are not capture by themselves.
   400	
   401	\subsection{Conversion of resources into influence}
   402	
   403	The central mechanism is conversion: the use of control in the financial pillar to obtain favorable outputs in another pillar. Walzer's tyranny and Bourdieu's convertibility of capital name the same phenomenon \citep{walzer1983,bourdieu1989}.
   404	
   405	\begin{definition}[Conversion elasticity]
   406	\label{def:financial-power:conversion}
   407	Let $y^{n}_i$ be a measure of outputs of pillar $n\neq\pF$ that favor actor $i$: rules adopted, rulings won, coverage obtained, sanctions avoided, or labor terms secured. The \emph{conversion elasticity} from the financial pillar to pillar $n$ is
   408	\[
   409	\varepsilon_{\pF\to n}=\frac{\partial\ln\E[y^{n}_i\mid s^{\pF}_i,X_i]}{\partial\ln s^{\pF}_i},
   410	\]
   411	where $X_i$ collects the controls under which the comparison is made, including the actor's preferences and the public salience of the issue. The elasticity is defined where $s^{\pF}_i>0$, the conditional expectation is positive, and it is differentiable in $s^{\pF}_i$.
   412	\end{definition}
   413	
   414	Conversion elasticity and the coupling $C_{\pF n}$ measure different things. The coupling records whether one coalition commands appointments, budgets, sanctions, or agenda in both pillars \citep{largo2026hbs}; the elasticity records whether resource shares buy favorable outputs from actors who may be entirely independent. A wealthy firm lobbying an independent legislature produces positive $\varepsilon_{\pF\to\pP}$ with $C_{\pF\pP}$ near zero. A party-state in which appointment determines credit has high $C_{\pP\pF}$, but the relevant elasticity runs the other way, from appointment rank to allocation, which is the object of hypothesis HF2 in \cref{sec:measurement}. Which direction dominates is the regime-specific control path of \citet{largo2026hbs}.
   415	
   416	A deliberately simple decision model gives conditions under which a resource holder invests in conversion.
   417	
   418	\begin{proposition}[Influence investment]
   419	\label{prop:financial-power:influence}
   420	An actor with financial share $s\in(0,1]$ faces a rule whose adoption is worth $sV$ to it, where $V>0$ is the value of the rule to the whole resource base. By spending $e\geq 0$ the actor makes adoption occur with probability $\pi(e,Q)$, where $Q\in[0,1)$ is the contestability of the receiving pillar and $\pi$ is twice continuously differentiable on $[0,\infty)\times[0,1)$ with $\pi_e>0$, $\pi_{ee}<0$, and $\pi_{eQ}<0$. At $Q=1$ influence has no return and the actor spends nothing. The actor maximizes $sV\pi(e,Q)-e$. If the maximizer $e^*$ is interior, then
   421	\[
   422	\frac{\partial e^*}{\partial s}=-\frac{\pi_e}{s\,\pi_{ee}}>0,\qquad
   423	\frac{\partial e^*}{\partial V}=-\frac{\pi_e}{V\,\pi_{ee}}>0,\qquad
   424	\frac{\partial e^*}{\partial Q}=-\frac{\pi_{eQ}}{\pi_{ee}}<0.
   425	\]
   426	\end{proposition}
   427	
   428	\begin{proof}
   429	An interior maximizer satisfies the first-order condition $sV\pi_e(e^*,Q)=1$, and the second-order condition holds because $sV\pi_{ee}<0$. Write $\Phi(e,s,V,Q)=sV\pi_e(e,Q)-1$. Since $\partial\Phi/\partial e=sV\pi_{ee}\neq 0$, the implicit function theorem gives $e^*$ as a differentiable function of $(s,V,Q)$ near any interior solution, with $\partial e^*/\partial z=-(\partial\Phi/\partial z)/(\partial\Phi/\partial e)$ for each parameter $z$. Here $\partial\Phi/\partial s=V\pi_e$, $\partial\Phi/\partial V=s\pi_e$, and $\partial\Phi/\partial Q=sV\pi_{eQ}$. Substituting gives the three expressions. Their signs follow from $\pi_e>0$, $\pi_{ee}<0$, and $\pi_{eQ}<0$.
   430	\end{proof}
   431	
   432	\begin{example}[A participation threshold]
   433	\label{ex:threshold}
   434	Let $\pi(e,Q)=(1-Q)(1-e^{-e})$, which satisfies the conditions of \cref{prop:financial-power:influence} for $Q<1$. The objective $sV(1-Q)(1-e^{-e})-e$ is concave in $e$ with derivative $sV(1-Q)e^{-e}-1$, so the optimum is $e^*=\ln\bigl(sV(1-Q)\bigr)$ when $sV(1-Q)>1$ and $e^*=0$ otherwise. Actors with shares below the threshold $\bar s=1/\bigl(V(1-Q)\bigr)$ do not invest at all. Take ten actors and $V=10$. At $Q=0.5$ and equal shares of $0.1$, every actor has $sV(1-Q)=0.5<1$ and total investment is zero. If one actor's share rises to $0.55$ and the other nine hold $0.05$ each, that actor invests $\ln 2.75\approx 1.01$ and the others still invest nothing. If contestability then rises to $Q=0.9$, the large holder's product falls to $0.55$ and its investment returns to zero.
   435	\end{example}
   436	
   437	The example states three things in miniature. Concentration activates conversion, because only holders above a threshold find influence worth buying; this is Olson's asymmetry between concentrated and diffuse interests \citep{olson1965}. Contestability shuts conversion off by lowering its marginal return, which is the financial form of the source's Proposition 2 that checks can interrupt transmission \citep{largo2026hbs}. And the threshold depends on the stake $V$, so conversion concentrates in domains where rules are worth much to few, which is consistent with Culpepper's finding that business power is strongest in quiet, technical politics \citep{culpepper2010}.
   438	
   439	The model has clear limits. It is a single-actor decision problem: other actors' spending does not enter $\pi$, so the competition among groups that Becker emphasizes, and the countermobilization that large transfers provoke, are absent \citep{becker1983}. The sign condition $\pi_{eQ}<0$ is an assumption about how contestability works, not a finding, and it would fail if contestability raised the value of expert lobbying by making the process more procedural. The proposition is therefore a conditional comparative static of the kind \citet{largo2026hbs} uses throughout, and its empirical counterpart is hypothesis HF1.
   440	
   441	\subsection{Credit and the discipline of lenders}
   442	
   443	Sovereign borrowing is the oldest form of coupling between private finance and political power. It can be read as capture, with lenders controlling the state, or as a bargain, with lenders disciplined by their need for repayment and the ruler by its need for future credit. A standard repeated-game condition separates the two readings.
   444	
   445	\begin{proposition}[Sovereign credit]
   446	\label{prop:financial-power:sovereign-credit}
   447	A ruler with discount factor $\delta\in(0,1)$ owes a payment $D>0$ in the current period. Continued access to credit yields a net surplus $g>0$ in every future period. Lenders act together, so that a default not excused by an agreed contingency ends all future lending. Then repayment is the ruler's best response if and only if
   448	\[
   449	D\leq\frac{\delta g}{1-\delta}.
   450	\]
   451	\end{proposition}
   452	
   453	\begin{proof}
   454	Repaying costs $D$ now and preserves the surplus stream, whose present value is $\sum_{t\geq 1}\delta^t g=\delta g/(1-\delta)$. Defaulting saves $D$ and ends the stream. Repayment is a best response exactly when $-D+\delta g/(1-\delta)\geq 0$.
   455	\end{proof}
   456	
   457	The condition explains how early modern lenders protected themselves without controlling legislation. Their security came from the ruler's need for future credit, measured by $g$, and from their own capacity to act together, which made exclusion credible. When a fiscal shock raised $D$ above the bound, a payment stop followed, and a negotiated settlement restored the relationship. Drelichman and Voth read the defaults of Philip II in this way, and Conklin attributes the discipline to the Genoese bankers' ability to coordinate \citep{drelichman2011,conklin1998}. If lenders cannot coordinate, because many small lenders compete to replace any lender who is excluded, the threat of exclusion weakens and the bound no longer protects them. The proposition thus identifies when lending is a bargain rather than capture: lenders receive repayment, not legal privileges unrelated to their loans. That is hypothesis HF3.
   458	
   459	North and Weingast argued that the constitutional settlement in seventeenth-century England improved the crown's capacity to borrow by making its commitments credible \citep{northweingast1989}. In the terms of the proposition, a representative assembly that controls taxation can raise the credibility of repayment by shifting authority over $D$ away from the ruler alone. The same logic connects the Cortes of Castile to the Habsburg debt.
   460	
   461	\subsection{Soft budgets, rents and fusion}
   462	
   463	Three further mechanisms move a financial pillar toward capture. The soft budget constraint arises whenever an allocating authority cannot commit to let loss-making units fail \citep{kornai1986}. Kornai developed the concept for socialist enterprises, where the paternalistic state rescued firms as a matter of course. The analogy with private banks considered too large to fail is plausible, but it extends the concept beyond the evidence that Kornai and \citet{largo2026hbs} cite, and we treat it as a hypothesis rather than a finding. Wherever it holds, rescue expectations transfer resources to units with bargaining power, and the transfer is unreviewable when the rescuing authority is not itself accountable.
   464	
   465	Rentier revenue changes the coupling between the financial pillar and the productive pillar. A state that lives on external rents does not depend on taxpayers and therefore need not bargain with them \citep{mahdavy1970,beblawiluciani1987}. Levi's account of quasi-voluntary compliance identifies what is lost: the reciprocal bargain in which rulers provide services and keep promises in exchange for compliance \citep{levi1988}. The rentier mechanism lowers $Q_{\pF}$ by weakening the fiscal voice of producers. Part VI derives the producers' side of the same mechanism (Proposition 6.6 of \citealt{long2026productive}); the allocation side belongs here. The evidence that the mechanism operates is mixed, as \cref{sec:literature} records.
   466	
   467	Fusion of the financial and coercive pillars in one organization is the most direct route to high $C_{\pF\pC}$. Part V shows that in large collectives sanctioners must be paid or provisioned, or else rewarded by belief (Proposition 3.5 of \citealt{long2026coercive}), which derives the dependency of coercion on resource allocation; fusion places both ends of that dependency in one organization. Business arms of security forces, whether the Revolutionary Guards' firms in Iran \citep{wehrey2009} or the military enterprise of early modern monarchies, give one organization both resources and the means of sanction. The rival explanation is public-goods provision: the same organizations build infrastructure and conduct reconstruction, and their size may reflect capacity rather than capture. Distinguishing the two requires evidence on procurement, competition, and review, not on size.
   468	
   469	\subsection{Checks}
   470	
   471	The checks that interrupt these mechanisms are specific. Open entry, enforced by antitrust and by competitive procurement, raises the number of actors who can contest a holder's position; Rajan and Zingales show that incumbents oppose it for that reason \citep{rajan2003}. A hard budget constraint, under which failing units actually exit, removes the rents of rescue. Disclosure of contributions, lobbying, and beneficial ownership makes the conversion pathway visible, which is a precondition of contesting it. Independent audit and independent central banking separate the review of financial decisions from those who make them, although independence relocates concentration into the reviewing body. And coordinated lenders, organized labor, and representative assemblies supply countervailing power from within the financial pillar itself. Each check raises $Q_{\pF}$ or lowers a coupling; none lowers the necessity of the pillar, which no check can or should remove.
   472	
   473	\section{Measurement and testable hypotheses}
   474	\label{sec:measurement}
   475	
   476	\subsection{Indicators}
   477	
   478	Measurement of the financial pillar should proceed subdomain by subdomain, as \cref{prop:financial-power:aggregation-gap} recommends, and should code contestability separately from concentration. \Cref{tab:indicators} lists indicators drawn from sources that already exist. Cross-national governance indicators, such as the Worldwide Governance Indicators and the V-Dem data, supply partial measures of contestability \citep{kaufmann2010,coppedge2011}; they do not measure control shares and should not be used as proxies for them.
   479	
   480	\begin{table}[t]
   481	\centering
   482	\small
   483	\caption{Indicators for the financial pillar. Concentration indicators enter $H_{\pF}$ by subdomain; contestability indicators enter $Q_{\pF}$.}
   484	\label{tab:indicators}
   485	\begin{tabularx}{\linewidth}{@{}L{2.6cm}YY@{}}
   486	\toprule
   487	Construct & Indicators & Main pitfall \\
   488	\midrule
   489	Ownership concentration & Asset shares, ownership pyramids, and dual-class control & Ownership understates control where party or family ties matter \\
   490	Credit concentration & Bank credit shares by lender and by borrower & State and private banks may follow different rules \\
   491	Budget discretion & Share of spending allocated without formula or tender & Discretion can serve legitimate emergencies \\
   492	Procurement & Concentration of awards by recipient, and the share awarded without competition & Specialized markets have few qualified suppliers \\
   493	Contestability & Entry barriers, audit independence, bankruptcy enforcement, and disclosure regimes & Laws on paper may not bind in practice \\
   494	Conversion & Connected-firm returns, connected lending, and lobbying linked to outcomes & Large firms become connected because they are large \\
   495	\bottomrule
   496	\end{tabularx}
   497	\end{table}
   498	
   499	The capture-link coding of \citet{largo2026hbs} supplies the unit of evidence. A coded link records the actor, the mechanism, the evidence of privileged access, the review that applied, the decision, and the material effect, together with counterevidence. The population of coded events should include all decisions in a preregistered sector, not only scandals, since a sample of scandals selects on the outcome.
   500	
   501	\subsection{Hypotheses}
   502	
   503	\Cref{tab:hypotheses} states seven hypotheses specific to the financial pillar, each refining one of the source hypotheses H1 to H6 and each with a stated falsifier.
   504	
   505	\begin{table}[t]
   506	\centering
   507	\small
   508	\caption{Hypotheses for the financial pillar, each paired with an observation that would falsify it.}
   509	\label{tab:hypotheses}
   510	\begin{tabularx}{\linewidth}{@{}L{1.1cm}YY@{}}
   511	\toprule
   512	Label & Hypothesis & Falsifier \\
   513	\midrule
   514	HF1 & The conversion elasticity $\varepsilon_{\pF\to\pP}$ is higher on technical issues of low salience than on salient ones & Equal or higher elasticity on salient issues, or no elasticity once preferences shared across income groups are controlled \\
   515	HF2 & In party-state command sectors, the appointment rank of an enterprise head predicts credit and inputs after controlling for profitability and plan targets & Profitability predicts allocation better than rank \\
   516	HF3 & Where a ruler needs repeated credit, lenders secure repayment without obtaining legal privileges unrelated to their loans & Lenders obtain legal advantages that do not secure repayment \\
   517	HF4 & Liberalizing entry reduces the rents of connected incumbents & Rents of connected firms persist after entry reform \\
   518	HF5 & A higher share of non-tax revenue lowers fiscal bargaining with taxpayers and raises discretionary allocation & A null effect in within-country panels \\
   519	HF6 & Where one organization holds financial and coercive control, financial contestability falls & Fused organizations face the same procurement competition and audit as others \\
   520	HF7 & Credible bankruptcy of large failing units is associated with lower rents & Rescues are followed by lower, not higher, subsequent rents \\
   521	\bottomrule
   522	\end{tabularx}
   523	\end{table}
   524	
   525	HF1 refines source hypothesis H1 and follows from \cref{prop:financial-power:influence} together with Culpepper's account of quiet politics \citep{culpepper2010}; the alternative falsifier comes from Branham, Soroka, and Wlezien \citep{branham2017}. HF2 specializes source hypothesis H3. HF3 follows from \cref{prop:financial-power:sovereign-credit} and the Habsburg evidence \citep{drelichman2011}. HF4 tests the argument of Rajan and Zingales \citep{rajan2003} and the evidence on connected lending: Khwaja and Mian find that politically connected firms in Pakistan obtained more credit from government banks and defaulted more often \citep{khwaja2005}, and Fisman finds that the market value of firms connected to Suharto fell when rumors of his ill health spread \citep{fisman2001}. HF5 tests the rentier mechanism against the within-country null of Haber and Menaldo \citep{habermenaldo2011}. HF6 states the fusion mechanism with its public-goods rival. HF7 tests the soft budget constraint.
   526	
   527	\subsection{Rival explanations and identification}
   528	
   529	Each hypothesis faces four rival explanations that coding must address. Economies of scale and natural monopoly can produce high concentration without any political cause. Public-goods provision can justify discretion and concentration, which is the source's Proposition 4 and hypothesis H6 \citep{largo2026hbs}. Survivorship can reverse the causal arrow, since firms that grow large for economic reasons attract political connections. And preference alignment can make the wealthy appear influential when they merely agree with the majority \citep{branham2017}. The event-study and latent-variable designs specified by \citet{largo2026hbs} address some of these threats, but each requires assumptions, such as parallel trends before a reform and measurement invariance across regimes, that must be tested rather than assumed. Measurement invariance is the most demanding: a control share in a Soviet ministry and a control share in a private bank may not be the same construct, and if invariance fails the comparison must use regime-specific models.
   530	
   531	\section{The Revelation reading}
   532	\label{sec:revelation}
   533	
   534	The series takes its name from Revelation 13, and its theological vocabulary is typological. The beast of Revelation 13 and the city of Babylon in chapters 17 and 18 are read as images of a recurring configuration of power that claims ultimate loyalty, not as predictions of a particular future state, person, or technology. This is one of several interpretive traditions. Preterist readings locate the text in its first-century setting and read the beast as Roman imperial power and the imperial cult of the province of Asia \citep{collins1984,kraybill1996}. Typological or idealist readings see Rome as a paradigm of a pattern that recurs \citep{bauckham1993}. Futurist readings identify the beast with a coming ruler or system; the history of such identifications is a history of failures, as McGinn and Fuller document \citep{mcginn1998,fuller1995}, and the series excludes them.
   535	
   536	Two passages bear on the financial pillar. The first is Revelation 13:16-17: ``And he causeth all, both small and great, rich and poor, free and bond, to receive a mark in their right hand, or in their foreheads: And that no man might buy or sell, save he that had the mark, or the name of the beast, or the number of his name.'' The image is economic participation conditioned on allegiance. In the vocabulary of this paper, it describes a financial pillar whose settlement procedure for exchange is gated by a test of loyalty administered by the ideological pillar: the coupling $C_{\pF\pI}$ is complete, and contestability for those who fail the test is zero. Part VI formalizes the same condition from the producers' side as a participation gate, access to exchange conditional on allegiance, and treats the passage as its limiting case (Definition 6.7 and Proposition 6.8 of \citealt{long2026productive}). Kraybill reads the passage against the participation of Asian merchants and artisans in trade guilds whose life was bound up with the imperial cult, so that commerce required at least tacit participation in worship \citep{kraybill1996}.
   537	
   538	The second is the lament over Babylon in Revelation 18. The merchants of the earth ``are waxed rich through the abundance of her delicacies'' (18:3), they weep ``for no man buyeth their merchandise any more'' (18:11), and the chapter's list of cargoes ends with ``slaves, and souls of men'' (18:13). Bauckham reads the chapter as an economic critique of Rome's trade empire, in which the wealth of the city depends on the extraction of goods from the provinces and the trade in persons is the last item of the list \citep{bauckham1991}. Koester and Aune give the philological and historical commentary \citep{koester2014,aune1998c}, and Rossing reads the chapter as a choice between two cities, Babylon and the new Jerusalem \citep{rossing1999}. The trade in slaves in 18:13 is literal: it refers to the Roman slave trade, and nothing in this reading equates it with wage labor, taxation, or other forms of economic dependence, which the series distinguishes from chattel slavery.
   539	
   540	The typological reading names the condition under which the series' structural claim acquires moral weight. The text does not condemn the existence of buying and selling; it condemns a configuration in which access to exchange depends on allegiance and the city's wealth depends on extraction and the trade in persons. That configuration is Proposition~B, the contingent capture of the financial pillar by a coalition that has also captured belief and coercion, not Proposition~A, the existence of an allocation function. The call of Revelation 18:4, ``Come out of her, my people,'' is in this reading an image of exit, one of the checks that Part VI treats. Wink's theology of the powers draws the same distinction: institutions are necessary to human life, become a system of domination when organized around it, and remain open to transformation \citep{wink1992}. The mapping from text to model is an interpretive claim of this series, offered as an aid to comparison; it is not a settled exegetical result. Collins's argument that Revelation responds to a crisis perceived by its author and audience, rather than to an empirically general persecution \citep{collins1984}, is a reminder that the text's images express a judgment about an order, which a comparative political economy cannot simply import as evidence.
   541	
   542	\section{Objections and scope conditions}
   543	\label{sec:objections}
   544	
   545	A pluralist will object that resource control in democracies has no apex: many holders compete, coalitions shift by issue, and resources often lose. The objection is correct about the evidence it cites \citep{baumgartner2009,ansolabehere2003} and does not touch the necessity claim, which concerns the existence of the function, not its concentration. It does bear on the capture claim, which is why that claim is stated as a set of hypotheses with falsifiers rather than as a description.
   546	
   547	A Marxian critic will object from the other side that the financial pillar abstracts from class: control of the means of production is a social relation, not a share in an index. The model accommodates the relation, since control shares can be computed over the means of production and the coupling $C_{\pF\pW}$ records employer power over workers, but it does not presuppose that one class holds the pillar in every regime. The party-state cases, where control follows appointment rather than ownership, show why that presupposition would mislead.
   548	
   549	A market liberal will object that in a market nobody allocates. The reply in \cref{sec:necessity} applies: allocation by price is a settlement procedure whose control shares follow the distribution of endowments, and property rules are themselves outputs of other pillars. The objection has force against a different claim, that markets concentrate control more than other modes, and that claim is not made here.
   550	
   551	A philosopher of science will object that the necessity claim is true by definition. It is not, for two reasons. \Cref{def:financial-power:settlement} excludes unregulated contest, so a collective that resolves conflicts by fighting without shared expectations would lack the pillar; and \cref{ass:hazard} is an empirical assumption that could fail. The falsifier stated in \cref{sec:necessity} is a possible observation. What the claim does not do is explain why any particular institution exists, and \cref{sec:necessity} disclaims that explanation explicitly \citep{elster1983,hempel1959}.
   552	
   553	A reader concerned with even-handedness may object that Islamic and Catholic polities appear as types at all. They appear because their rulers drew legitimacy from religious law and religious institutions, which shaped how the financial pillar was organized, and the comparison records the internal diversity of each: the waqf and the tax farm, the Ottoman and the Saudi state, the Habsburg debt and the papal Camera. No claim is made that either religion determines an allocation regime, and the evidence reviewed contradicts any such claim.
   554	
   555	The comparative claims carry less weight than the formal ones. They rest on secondary scholarship, none of the six types has been coded under a preregistered protocol, and the coupling entries in \cref{tab:regimes} are hypotheses about what such coding would find.
   556	
   557	\section{Conclusion}
   558	\label{sec:conclusion}
   559	
   560	The financial pillar is necessary in a precise and limited sense. Given that claims on finite resources conflict and that unsettled conflict risks dissolution, a collective without a recognized procedure for settling those claims cannot persist, and in any collective that does persist almost all conflicts are settled by such a procedure. The procedure can be a sharing norm in a foraging camp, a cattle payment arranged by a mediator, a waqf deed, a crown loan, a plan target, or a market price. Its necessity implies nothing about who holds it: control can be as dispersed as the index allows or held by one actor, and it can be fully contestable or not contestable at all.
   561	
   562	The comparison of six regime types shows the same function held by institutions that differ almost entirely, with control paths that run from wealth to rules, from appointment to allocation, from rents to rulers, and from lenders to kings. Each type has documented capture episodes and documented checks. Whether a particular financial pillar has been captured is therefore an empirical question about concentration, contestability, and coupling in a given polity and period, and the hypotheses stated here make it answerable. What remains uncertain is the measurement itself: until control shares and couplings are coded under a common protocol, the comparative claims of this paper are well-grounded hypotheses rather than estimates. The ideology that justifies resource command changes from one order to the next. The question of who controls the resources remains, and every order must answer it.
   563	
   564	\begin{thebibliography}{99}
   565	\small
   566	\raggedright
   567	
   568	\bibitem[Alesina and Summers(1993)]{alesina1993}
   569	Alberto Alesina and Lawrence H. Summers (1993). Central Bank Independence and Macroeconomic Performance: Some Comparative Evidence. \emph{Journal of Money, Credit and Banking} 25(2). doi:10.2307/2077833.
   570	
   571	\bibitem[Allen et al.(2005)]{allen2005}
   572	Franklin Allen, Jun Qian, and Meijun Qian (2005). Law, Finance, and Economic Growth in China. \emph{Journal of Financial Economics} 77(1). doi:10.1016/j.jfineco.2004.06.010.
   573	
   574	\bibitem[Ansolabehere et al.(2003)]{ansolabehere2003}
   575	Stephen Ansolabehere, John M. de Figueiredo, and James M. Snyder (2003). Why Is There So Little Money in U.S. Politics? \emph{Journal of Economic Perspectives} 17(1). doi:10.1257/089533003321164976.
   576	
   577	\bibitem[Aune(1998)]{aune1998c}
   578	David E. Aune (1998). \emph{Revelation 17-22}. Word Biblical Commentary 52C, Thomas Nelson.
   579	
   580	\bibitem[Bartels(2008)]{bartels2008}
   581	Larry M. Bartels (2008). \emph{Unequal Democracy: The Political Economy of the New Gilded Age}. Princeton University Press. doi:10.1515/9781400883363.
   582	
   583	\bibitem[Bauckham(1991)]{bauckham1991}
   584	Richard Bauckham (1991). The Economic Critique of Rome in Revelation 18. In \emph{Images of Empire}, edited by Loveday Alexander, JSOT Press (JSOTSup 122).
   585	
   586	\bibitem[Bauckham(1993)]{bauckham1993}
   587	Richard Bauckham (1993). \emph{The Theology of the Book of Revelation}. Cambridge University Press. doi:10.1017/cbo9780511819858.
   588	
   589	\bibitem[Baumgartner et al.(2009)]{baumgartner2009}
   590	Frank R. Baumgartner, Jeffrey M. Berry, Marie Hojnacki, David C. Kimball, and Beth L. Leech (2009). \emph{Lobbying and Policy Change: Who Wins, Who Loses, and Why}. University of Chicago Press. doi:10.7208/chicago/9780226039466.001.0001.
   591	
   592	\bibitem[Beblawi and Luciani(1987)]{beblawiluciani1987}
   593	Hazem Beblawi and Giacomo Luciani (eds.) (1987). \emph{The Rentier State}. Croom Helm. doi:10.4324/9781315684864.
   594	
   595	\bibitem[Becker(1983)]{becker1983}
   596	Gary S. Becker (1983). A Theory of Competition among Pressure Groups for Political Influence. \emph{The Quarterly Journal of Economics} 98(3). doi:10.2307/1886017.
   597	
   598	\bibitem[Berliner(1957)]{berliner1957}
   599	Joseph S. Berliner (1957). \emph{Factory and Manager in the USSR}. Harvard University Press. doi:10.4159/harvard.9780674188273.
   600	
   601	\bibitem[Berman(2006)]{berman2006}
   602	Sheri Berman (2006). \emph{The Primacy of Politics: Social Democracy and the Making of Europe's Twentieth Century}. Cambridge University Press. doi:10.1017/cbo9780511791109.
   603	
   604	\bibitem[Bertrand et al.(2014)]{bertrand2014}
   605	Marianne Bertrand, Matilde Bombardini, and Francesco Trebbi (2014). Is It Whom You Know or What You Know? An Empirical Assessment of the Lobbying Process. \emph{American Economic Review} 104(12). doi:10.1257/aer.104.12.3885.
   606	
   607	\bibitem[Black et al.(2000)]{black2000}
   608	Bernard Black, Reinier Kraakman, and Anna Tarassova (2000). Russian Privatization and Corporate Governance: What Went Wrong? \emph{Stanford Law Review} 52(6). doi:10.2307/1229501.
   609	
   610	\bibitem[Blanes i Vidal et al.(2012)]{blanes2012}
   611	Jordi Blanes i Vidal, Mirko Draca, and Christian Fons-Rosen (2012). Revolving Door Lobbyists. \emph{American Economic Review} 102(7). doi:10.1257/aer.102.7.3731.
   612	
   613	\bibitem[Boehm(1999)]{boehm1999}
   614	Christopher Boehm (1999). \emph{Hierarchy in the Forest: The Evolution of Egalitarian Behavior}. Harvard University Press. doi:10.2307/j.ctvjf9xr4.
   615	
   616	\bibitem[Bourdieu(1989)]{bourdieu1989}
   617	Pierre Bourdieu (1989). Social Space and Symbolic Power. \emph{Sociological Theory} 7(1). doi:10.2307/202060.
   618	
   619	\bibitem[Branham et al.(2017)]{branham2017}
   620	J. Alexander Branham, Stuart N. Soroka, and Christopher Wlezien (2017). When Do the Rich Win? \emph{Political Science Quarterly} 132(1). doi:10.1002/polq.12577.
   621	
   622	\bibitem[Carpenter and Moss(2014)]{carpentermoss2014}
   623	Daniel Carpenter and David A. Moss (eds.) (2014). \emph{Preventing Regulatory Capture: Special Interest Influence and How to Limit It}. Cambridge University Press. doi:10.1017/CBO9781139565875.
   624	
   625	\bibitem[Chaudhry(1997)]{chaudhry1997}
   626	Kiren Aziz Chaudhry (1997). \emph{The Price of Wealth: Economies and Institutions in the Middle East}. Cornell University Press. doi:10.7591/9781501700347.
   627	
   628	\bibitem[\c{C}izak\c{c}a(1996)]{cizakca1996}
   629	Murat \c{C}izak\c{c}a (1996). \emph{A Comparative Evolution of Business Partnerships: The Islamic World and Europe, with Specific Reference to the Ottoman Archives}. Brill.
   630	
   631	\bibitem[Clastres(1987)]{clastres1987}
   632	Pierre Clastres (1987). \emph{Society against the State: Essays in Political Anthropology (1974), trans. Robert Hurley}. Zone Books. doi:10.2307/j.ctv1595m3p.
   633	
   634	\bibitem[Collins(1984)]{collins1984}
   635	Adela Yarbro Collins (1984). \emph{Crisis and Catharsis: The Power of the Apocalypse}. Westminster Press.
   636	
   637	\bibitem[Conklin(1998)]{conklin1998}
   638	James Conklin (1998). The Theory of Sovereign Debt and Spain under Philip II. \emph{Journal of Political Economy} 106(3). doi:10.1086/250019.
   639	
   640	\bibitem[Coppedge et al.(2011)]{coppedge2011}
   641	Michael Coppedge, John Gerring, David Altman, Michael Bernhard, Steven Fish, Allen Hicken, Matthew Kroenig, Staffan I. Lindberg, Kelly McMann, Pamela Paxton, Holli A. Semetko, Svend-Erik Skaaning, Jeffrey Staton, and Jan Teorell (2011). Conceptualizing and Measuring Democracy: A New Approach. \emph{Perspectives on Politics} 9(2). doi:10.1017/S1537592711000880.
   642	
   643	\bibitem[Cox et al.(2010)]{cox2010}
   644	Michael Cox, Gwen Arnold, and Sergio Villamayor Tomas (2010). A Review of Design Principles for Community-based Natural Resource Management. \emph{Ecology and Society} 15(4). doi:10.5751/ES-03704-150438.
   645	
   646	\bibitem[Culpepper(2010)]{culpepper2010}
   647	Pepper D. Culpepper (2010). \emph{Quiet Politics and Business Power: Corporate Control in Europe and Japan}. Cambridge University Press. doi:10.1017/cbo9780511760716.
   648	
   649	\bibitem[Dal B\'o(2006)]{dalbo2006}
   650	Ernesto Dal B\'o (2006). Regulatory Capture: A Review. \emph{Oxford Review of Economic Policy} 22(2). doi:10.1093/oxrep/grj013.
   651	
   652	\bibitem[de Roover(1963)]{deroover1963}
   653	Raymond de Roover (1963). \emph{The Rise and Decline of the Medici Bank, 1397-1494}. Harvard University Press.
   654	
   655	\bibitem[Doyle(1996)]{doyle1996}
   656	William Doyle (1996). \emph{Venality: The Sale of Offices in Eighteenth-Century France}. Oxford University Press. doi:10.1093/acprof:oso/9780198205364.001.0001.
   657	
   658	\bibitem[Drelichman and Voth(2011)]{drelichman2011}
   659	Mauricio Drelichman and Hans-Joachim Voth (2011). Lending to the Borrower from Hell: Debt and Default in the Age of Philip II. \emph{The Economic Journal} 121(557). doi:10.1111/j.1468-0297.2011.02442.x.
   660	
   661	\bibitem[Drelichman and Voth(2014)]{drelichman2014}
   662	Mauricio Drelichman and Hans-Joachim Voth (2014). \emph{Lending to the Borrower from Hell: Debt, Taxes, and Default in the Age of Philip II}. Princeton University Press.
   663	
   664	\bibitem[Ekelund et al.(1996)]{ekelund1996}
   665	Robert B. Ekelund, Robert F. Hebert, Robert D. Tollison, Gary M. Anderson, and Audrey B. Davidson (1996). \emph{Sacred Trust: The Medieval Church as an Economic Firm}. Oxford University Press.
   666	
   667	\bibitem[El-Gamal(2006)]{elgamal2006}
   668	Mahmoud A. El-Gamal (2006). \emph{Islamic Finance: Law, Economics, and Practice}. Cambridge University Press. doi:10.1017/CBO9780511753756.
   669	
   670	\bibitem[Ellickson(1991)]{ellickson1991}
   671	Robert C. Ellickson (1991). \emph{Order without Law: How Neighbors Settle Disputes}. Harvard University Press. doi:10.4159/9780674036437.
   672	
   673	\bibitem[Elster(1983)]{elster1983}
   674	Jon Elster (1983). \emph{Explaining Technical Change: A Case Study in the Philosophy of Science}. Cambridge University Press.
   675	
   676	\bibitem[Esping-Andersen(1985)]{esping1985}
   677	G\"osta Esping-Andersen (1985). \emph{Politics against Markets: The Social Democratic Road to Power}. Princeton University Press. doi:10.1515/9781400886203.
   678	
   679	\bibitem[Evans-Pritchard(1940)]{evanspritchard1940}
   680	E. E. Evans-Pritchard (1940). \emph{The Nuer: A Description of the Modes of Livelihood and Political Institutions of a Nilotic People}. Clarendon Press.
   681	
   682	\bibitem[Faccio(2006)]{faccio2006}
   683	Mara Faccio (2006). Politically Connected Firms. \emph{American Economic Review} 96(1). doi:10.1257/000282806776157704.
   684	
   685	\bibitem[Fisman(2001)]{fisman2001}
   686	Raymond Fisman (2001). Estimating the Value of Political Connections. \emph{American Economic Review} 91(4). doi:10.1257/aer.91.4.1095.
   687	
   688	\bibitem[Fuller(1995)]{fuller1995}
   689	Robert C. Fuller (1995). \emph{Naming the Antichrist: The History of an American Obsession}. Oxford University Press. doi:10.1093/acprof:oso/9780195109795.001.0001.
   690	
   691	\bibitem[Gilens and Page(2014)]{gilens2014}
   692	Martin Gilens and Benjamin I. Page (2014). Testing Theories of American Politics: Elites, Interest Groups, and Average Citizens. \emph{Perspectives on Politics} 12(3). doi:10.1017/S1537592714001595.
   693	
   694	\bibitem[Goodhart(1988)]{goodhart1988}
   695	Charles A. E. Goodhart (1988). \emph{The Evolution of Central Banks}. MIT Press.
   696	
   697	\bibitem[Graeber and Wengrow(2021)]{graeber2021}
   698	David Graeber and David Wengrow (2021). \emph{The Dawn of Everything: A New History of Humanity}. Farrar, Straus and Giroux.
   699	
   700	\bibitem[Gregory(2004)]{gregory2004}
   701	Paul R. Gregory (2004). \emph{The Political Economy of Stalinism: Evidence from the Soviet Secret Archives}. Cambridge University Press. doi:10.1017/cbo9780511615856.
   702	
   703	\bibitem[Grossman and Helpman(1994)]{grossman1994}
   704	Gene M. Grossman and Elhanan Helpman (1994). Protection for Sale. \emph{American Economic Review} 84(4).
   705	
   706	\bibitem[Guriev and Rachinsky(2005)]{guriev2005}
   707	Sergei Guriev and Andrei Rachinsky (2005). The Role of Oligarchs in Russian Capitalism. \emph{Journal of Economic Perspectives} 19(1). doi:10.1257/0895330053147994.
   708	
   709	\bibitem[Haber and Menaldo(2011)]{habermenaldo2011}
   710	Stephen Haber and Victor Menaldo (2011). Do Natural Resources Fuel Authoritarianism? A Reappraisal of the Resource Curse. \emph{American Political Science Review} 105(1). doi:10.1017/S0003055410000584.
   711	
   712	\bibitem[Hacker and Pierson(2010)]{hackerpierson2010}
   713	Jacob S. Hacker and Paul Pierson (2010). \emph{Winner-Take-All Politics: How Washington Made the Rich Richer and Turned Its Back on the Middle Class}. Simon \& Schuster.
   714	
   715	\bibitem[Hall and Deardorff(2006)]{hall2006}
   716	Richard L. Hall and Alan V. Deardorff (2006). Lobbying as Legislative Subsidy. \emph{American Political Science Review} 100(1). doi:10.1017/s0003055406062010.
   717	
   718	\bibitem[Hall and Soskice(2001)]{hallsoskice2001}
   719	Peter A. Hall and David Soskice (eds.) (2001). \emph{Varieties of Capitalism: The Institutional Foundations of Comparative Advantage}. Oxford University Press. doi:10.1093/0199247757.001.0001.
   720	
   721	\bibitem[Hellman(1998)]{hellman1998}
   722	Joel S. Hellman (1998). Winners Take All: The Politics of Partial Reform in Postcommunist Transitions. \emph{World Politics} 50(2). doi:10.1017/s0043887100008091.
   723	
   724	\bibitem[Hellman et al.(2000)]{hellman2000}
   725	Joel S. Hellman, Geraint Jones, and Daniel Kaufmann (2000). Seize the State, Seize the Day: State Capture, Corruption, and Influence in Transition. World Bank Policy Research Working Paper 2444.
   726	
   727	\bibitem[Hempel(1959)]{hempel1959}
   728	Carl G. Hempel (1959). The Logic of Functional Analysis. In \emph{Symposium on Sociological Theory}, edited by Llewellyn Gross, Harper \& Row.
   729	
   730	\bibitem[Hertog(2010)]{hertog2010}
   731	Steffen Hertog (2010). \emph{Princes, Brokers, and Bureaucrats: Oil and the State in Saudi Arabia}. Cornell University Press. doi:10.7591/9780801458774.
   732	
   733	\bibitem[Hirschman(1964)]{hirschman1964}
   734	Albert O. Hirschman (1964). The Paternity of an Index. \emph{American Economic Review} 54(5).
   735	
   736	\bibitem[Hoffman and Norberg(1994)]{hoffmannorberg1994}
   737	Philip T. Hoffman and Kathryn Norberg (eds.) (1994). \emph{Fiscal Crises, Liberty, and Representative Government, 1450-1789}. Stanford University Press. doi:10.1515/9781503619500.
   738	
   739	\bibitem[Hoffman et al.(2000)]{hoffman2000}
   740	Philip T. Hoffman, Gilles Postel-Vinay, and Jean-Laurent Rosenthal (2000). \emph{Priceless Markets: The Political Economy of Credit in Paris, 1660-1870}. University of Chicago Press.
   741	
   742	\bibitem[H\"ogfeldt(2005)]{hogfeldt2005}
   743	Peter H\"ogfeldt (2005). The History and Politics of Corporate Ownership in Sweden. In \emph{A History of Corporate Governance around the World}, edited by Randall K. Morck, University of Chicago Press / NBER.
   744	
   745	\bibitem[Igan et al.(2012)]{igan2012}
   746	Deniz Igan, Prachi Mishra, and Thierry Tressel (2012). A Fistful of Dollars: Lobbying and the Financial Crisis. \emph{NBER Macroeconomics Annual} 26.
   747	
   748	\bibitem[Kalla and Broockman(2016)]{kalla2016}
   749	Joshua L. Kalla and David E. Broockman (2016). Campaign Contributions Facilitate Access to Congressional Officials: A Randomized Field Experiment. \emph{American Journal of Political Science} 60(3). doi:10.1111/ajps.12180.
   750	
   751	\bibitem[Karaman and Pamuk(2010)]{karaman2010}
   752	K. K{\i}van\c{c} Karaman and \c{S}evket Pamuk (2010). Ottoman State Finances in European Perspective, 1500-1914. \emph{The Journal of Economic History} 70(3). doi:10.1017/s0022050710000550.
   753	
   754	\bibitem[Karaman and Pamuk(2013)]{karaman2013}
   755	K. K{\i}van\c{c} Karaman and \c{S}evket Pamuk (2013). Different Paths to the Modern State in Europe: The Interaction between Warfare, Economic Structure, and Political Regime. \emph{American Political Science Review} 107(3). doi:10.1017/S0003055413000312.
   756	
   757	\bibitem[Kaufmann et al.(2010)]{kaufmann2010}
   758	Daniel Kaufmann, Aart Kraay, and Massimo Mastruzzi (2010). The Worldwide Governance Indicators: Methodology and Analytical Issues. \emph{Hague Journal on the Rule of Law} 3(2). doi:10.1017/S1876404511200046.
   759	
   760	\bibitem[Kelly(1995)]{kelly1995}
   761	Robert L. Kelly (1995). \emph{The Foraging Spectrum: Diversity in Hunter-Gatherer Lifeways}. Smithsonian Institution Press. doi:10.2307/j.ctv2sx9gc9.
   762	
   763	\bibitem[Khwaja and Mian(2005)]{khwaja2005}
   764	Asim Ijaz Khwaja and Atif Mian (2005). Do Lenders Favor Politically Connected Firms? Rent Provision in an Emerging Financial Market. \emph{Quarterly Journal of Economics} 120(4). doi:10.1162/003355305775097524.
   765	
   766	\bibitem[Koester(2014)]{koester2014}
   767	Craig R. Koester (2014). \emph{Revelation: A New Translation with Introduction and Commentary}. Yale University Press (Anchor Yale Bible 38A). doi:10.12987/9780300211030.
   768	
   769	\bibitem[Kornai(1986)]{kornai1986}
   770	J\'anos Kornai (1986). The Soft Budget Constraint. \emph{Kyklos} 39(1). doi:10.1111/j.1467-6435.1986.tb01252.x.
   771	
   772	\bibitem[Kornai(1992)]{kornai1992}
   773	J\'anos Kornai (1992). \emph{The Socialist System: The Political Economy of Communism}. Princeton University Press. doi:10.2307/j.ctv1ddczdr.
   774	
   775	\bibitem[Korpi(1983)]{korpi1983}
   776	Walter Korpi (1983). \emph{The Democratic Class Struggle}. Routledge \& Kegan Paul.
   777	
   778	\bibitem[Kraybill(1996)]{kraybill1996}
   779	J. Nelson Kraybill (1996). \emph{Imperial Cult and Commerce in John's Apocalypse}. Sheffield Academic Press (JSNT Supplement 132).
   780	
   781	\bibitem[Krueger(1974)]{krueger1974}
   782	Anne O. Krueger (1974). The Political Economy of the Rent-Seeking Society. \emph{American Economic Review} 64(3).
   783	
   784	\bibitem[Kuran(2001)]{kuran2001}
   785	Timur Kuran (2001). The Provision of Public Goods under Islamic Law: Origins, Impact, and Limitations of the Waqf System. \emph{Law \& Society Review} 35(4). doi:10.2307/3185418.
   786	
   787	\bibitem[Kuran(2004)]{kuran2004}
   788	Timur Kuran (2004). Why the Middle East Is Economically Underdeveloped: Historical Mechanisms of Institutional Stagnation. \emph{Journal of Economic Perspectives} 18(3). doi:10.1257/0895330042162421.
   789	
   790	\bibitem[Kuran(2011)]{kuran2011}
   791	Timur Kuran (2011). \emph{The Long Divergence: How Islamic Law Held Back the Middle East}. Princeton University Press. doi:10.1515/9781400836017.
   792	
   793	\bibitem[Kuru(2019)]{kuru2019}
   794	Ahmet T. Kuru (2019). \emph{Islam, Authoritarianism, and Underdevelopment: A Global and Historical Comparison}. Cambridge University Press. doi:10.1017/9781108296892.
   795	
   796	\bibitem[Kwass(2000)]{kwass2000}
   797	Michael Kwass (2000). \emph{Privilege and the Politics of Taxation in Eighteenth-Century France}. Cambridge University Press.
   798	
   799	\bibitem[La Porta et al.(2002)]{laporta2002}
   800	Rafael La Porta, Florencio L\'opez-de-Silanes, and Andrei Shleifer (2002). Government Ownership of Banks. \emph{The Journal of Finance} 57(1). doi:10.1111/1540-6261.00422.
   801	
   802	\bibitem[Laffont and Tirole(1991)]{laffont1991}
   803	Jean-Jacques Laffont and Jean Tirole (1991). The Politics of Government Decision-Making: A Theory of Regulatory Capture. \emph{The Quarterly Journal of Economics} 106(4). doi:10.2307/2937958.
   804	
   805	\bibitem[Lardy(2014)]{lardy2014}
   806	Nicholas R. Lardy (2014). \emph{Markets over Mao: The Rise of Private Business in China}. Peterson Institute for International Economics.
   807	
   808	\bibitem[Largo(2026)]{largo2026hbs}
   809	Mateo Largo (2026). The Hierarchy of the Beast System: Institutional Power, Elite Coordination, and Economic Dependency Across Political Regimes. Working paper, 14 October 2026.
   810	
   811	\bibitem[Ledeneva(1998)]{ledeneva1998}
   812	Alena V. Ledeneva (1998). \emph{Russia's Economy of Favours: Blat, Networking and Informal Exchange}. Cambridge University Press.
   813	
   814	\bibitem[Lee(1979)]{lee1979}
   815	Richard B. Lee (1979). \emph{The !Kung San: Men, Women, and Work in a Foraging Society}. Cambridge University Press.
   816	
   817	\bibitem[Lee(2013)]{lee2013}
   818	Richard B. Lee (2013). \emph{The Dobe Ju/'hoansi (4th edition)}. Wadsworth/Cengage Learning.
   819	
   820	\bibitem[Levi(1988)]{levi1988}
   821	Margaret Levi (1988). \emph{Of Rule and Revenue}. University of California Press. doi:10.1525/9780520909540.
   822	
   823	\bibitem[Lindblom(1977)]{lindblom1977}
   824	Charles E. Lindblom (1977). \emph{Politics and Markets: The World's Political-Economic Systems}. Basic Books.
   825	
   826	\bibitem[Long(2026a)]{long2026coercive}
   827	Matthew Long (2026a). Coercive Power and Enforcement. Part V of \emph{The Six Pillars of the Beast System}. Working paper, October 2026.
   828	
   829	\bibitem[Long(2026b)]{long2026formalized}
   830	Matthew Long (2026b). The Formalized State: The Hierarchy of the Beast System. Part VII of \emph{The Six Pillars of the Beast System}. Working paper, in preparation.
   831	
   832	\bibitem[Long(2026c)]{long2026ideological}
   833	Matthew Long (2026c). Ideological Power and Legitimation. Part IV of \emph{The Six Pillars of the Beast System}. Working paper, October 2026.
   834	
   835	\bibitem[Long(2026d)]{long2026judicial}
   836	Matthew Long (2026d). Judicial Power and Legal Interpretation. Part III of \emph{The Six Pillars of the Beast System}. Working paper, October 2026.
   837	
   838	\bibitem[Long(2026e)]{long2026political}
   839	Matthew Long (2026e). Political Power and Rule Making. Part II of \emph{The Six Pillars of the Beast System}. Working paper, October 2026.
   840	
   841	\bibitem[Long(2026f)]{long2026productive}
   842	Matthew Long (2026f). Productive Power and Social Reproduction. Part VI of \emph{The Six Pillars of the Beast System}. Working paper, October 2026.
   843	
   844	\bibitem[Mahdavy(1970)]{mahdavy1970}
   845	Hossein Mahdavy (1970). The Patterns and Problems of Economic Development in Rentier States: The Case of Iran. In \emph{Studies in the Economic History of the Middle East}, edited by M. A. Cook, Oxford University Press.
   846	
   847	\bibitem[Maloney(2015)]{maloney2015}
   848	Suzanne Maloney (2015). \emph{Iran's Political Economy since the Revolution}. Cambridge University Press. doi:10.1017/cbo9781139023276.
   849	
   850	\bibitem[Mann(1986)]{mann1986}
   851	Michael Mann (1986). \emph{The Sources of Social Power, Volume 1: A History of Power from the Beginning to A.D. 1760}. Cambridge University Press. doi:10.1017/CBO9780511570896.
   852	
   853	\bibitem[Marshall(1976)]{marshall1976}
   854	Lorna Marshall (1976). \emph{The !Kung of Nyae Nyae}. Harvard University Press. doi:10.4159/harvard.9780674180574.
   855	
   856	\bibitem[McGinn(1998)]{mcginn1998}
   857	Bernard McGinn (1998). \emph{Antichrist: Two Thousand Years of the Human Fascination with Evil}. Columbia University Press.
   858	
   859	\bibitem[Merton(1968)]{merton1968}
   860	Robert K. Merton (1968). \emph{Social Theory and Social Structure (enlarged edition)}. Free Press.
   861	
   862	\bibitem[Mian et al.(2010)]{mian2010}
   863	Atif Mian, Amir Sufi, and Francesco Trebbi (2010). The Political Economy of the US Mortgage Default Crisis. \emph{American Economic Review} 100(5). doi:10.1257/aer.100.5.1967.
   864	
   865	\bibitem[Milhaupt and Zheng(2015)]{milhaupt2015}
   866	Curtis J. Milhaupt and Wentong Zheng (2015). Beyond Ownership: State Capitalism and the Chinese Firm. \emph{Georgetown Law Journal} 103(3).
   867	
   868	\bibitem[Mills(1956)]{mills1956}
   869	C. Wright Mills (1956). \emph{The Power Elite}. Oxford University Press.
   870	
   871	\bibitem[Mizruchi(2013)]{mizruchi2013}
   872	Mark S. Mizruchi (2013). \emph{The Fracturing of the American Corporate Elite}. Harvard University Press. doi:10.4159/harvard.9780674075368.
   873	
   874	\bibitem[Naughton(2007)]{naughton2007}
   875	Barry Naughton (2007). \emph{The Chinese Economy: Transitions and Growth}. MIT Press.
   876	
   877	\bibitem[North and Weingast(1989)]{northweingast1989}
   878	Douglass C. North and Barry R. Weingast (1989). Constitutions and Commitment: The Evolution of Institutions Governing Public Choice in Seventeenth-Century England. \emph{The Journal of Economic History} 49(4). doi:10.1017/S0022050700009451.
   879	
   880	\bibitem[North et al.(2009)]{nww2009}
   881	Douglass C. North, John Joseph Wallis, and Barry R. Weingast (2009). \emph{Violence and Social Orders: A Conceptual Framework for Interpreting Recorded Human History}. Cambridge University Press. doi:10.1017/CBO9780511575839.
   882	
   883	\bibitem[Olson(1965)]{olson1965}
   884	Mancur Olson (1965). \emph{The Logic of Collective Action: Public Goods and the Theory of Groups}. Harvard University Press. doi:10.4159/9780674041660.
   885	
   886	\bibitem[Ostrom(1990)]{ostrom1990}
   887	Elinor Ostrom (1990). \emph{Governing the Commons: The Evolution of Institutions for Collective Action}. Cambridge University Press. doi:10.1017/CBO9780511807763.
   888	
   889	\bibitem[Padgett and Ansell(1993)]{padgett1993}
   890	John F. Padgett and Christopher K. Ansell (1993). Robust Action and the Rise of the Medici, 1400-1434. \emph{American Journal of Sociology} 98(6). doi:10.1086/230190.
   891	
   892	\bibitem[Pamuk(2000)]{pamuk2000}
   893	\c{S}evket Pamuk (2000). \emph{A Monetary History of the Ottoman Empire}. Cambridge University Press.
   894	
   895	\bibitem[Peltzman(1976)]{peltzman1976}
   896	Sam Peltzman (1976). Toward a More General Theory of Regulation. \emph{The Journal of Law and Economics} 19(2). doi:10.1086/466865.
   897	
   898	\bibitem[Piketty(2014)]{piketty2014}
   899	Thomas Piketty (2014). \emph{Capital in the Twenty-First Century}. Harvard University Press (Belknap). doi:10.4159/9780674982918.
   900	
   901	\bibitem[Pontusson(1992)]{pontusson1992}
   902	Jonas Pontusson (1992). \emph{The Limits of Social Democracy: Investment Politics in Sweden}. Cornell University Press. doi:10.7591/9781501737541.
   903	
   904	\bibitem[Posner(1975)]{posner1975}
   905	Richard A. Posner (1975). The Social Costs of Monopoly and Regulation. \emph{Journal of Political Economy} 83(4). doi:10.1086/260357.
   906	
   907	\bibitem[Prodi(1987)]{prodi1987}
   908	Paolo Prodi (1987). \emph{The Papal Prince: One Body and Two Souls: The Papal Monarchy in Early Modern Europe}. Cambridge University Press.
   909	
   910	\bibitem[Przeworski(1985)]{przeworski1985}
   911	Adam Przeworski (1985). \emph{Capitalism and Social Democracy}. Cambridge University Press. doi:10.1017/cbo9781139171830.
   912	
   913	\bibitem[Rajan and Zingales(2003)]{rajan2003}
   914	Raghuram G. Rajan and Luigi Zingales (2003). The Great Reversals: The Politics of Financial Development in the Twentieth Century. \emph{Journal of Financial Economics} 69(1). doi:10.1016/S0304-405X(03)00125-9.
   915	
   916	\bibitem[Ross(2001)]{ross2001}
   917	Michael L. Ross (2001). Does Oil Hinder Democracy? \emph{World Politics} 53(3). doi:10.1353/wp.2001.0011.
   918	
   919	\bibitem[Ross(2012)]{ross2012}
   920	Michael L. Ross (2012). \emph{The Oil Curse: How Petroleum Wealth Shapes the Development of Nations}. Princeton University Press. doi:10.1515/9781400841929.
   921	
   922	\bibitem[Rossing(1999)]{rossing1999}
   923	Barbara R. Rossing (1999). \emph{The Choice between Two Cities: Whore, Bride, and Empire in the Apocalypse}. Trinity Press International (Harvard Theological Studies 48).
   924	
   925	\bibitem[Rubin(2017)]{rubin2017}
   926	Jared Rubin (2017). \emph{Rulers, Religion, and Riches: Why the West Got Rich and the Middle East Did Not}. Cambridge University Press. doi:10.1017/9781139568272.
   927	
   928	\bibitem[Sahlins(1972)]{sahlins1972b}
   929	Marshall Sahlins (1972). The Original Affluent Society. In \emph{Stone Age Economics}, Aldine-Atherton.
   930	
   931	\bibitem[Scheve and Stasavage(2016)]{scheve2016}
   932	Kenneth Scheve and David Stasavage (2016). \emph{Taxing the Rich: A History of Fiscal Fairness in the United States and Europe}. Princeton University Press. doi:10.1515/9781400880379.
   933	
   934	\bibitem[Shleifer and Vishny(1994)]{shleifer1994}
   935	Andrei Shleifer and Robert W. Vishny (1994). Politicians and Firms. \emph{The Quarterly Journal of Economics} 109(4). doi:10.2307/2118354.
   936	
   937	\bibitem[Singer(2008)]{singer2008}
   938	Amy Singer (2008). \emph{Charity in Islamic Societies}. Cambridge University Press.
   939	
   940	\bibitem[Stigler(1971)]{stigler1971}
   941	George J. Stigler (1971). The Theory of Economic Regulation. \emph{The Bell Journal of Economics and Management Science} 2(1). doi:10.2307/3003160.
   942	
   943	\bibitem[Streeck(2014)]{streeck2014}
   944	Wolfgang Streeck (2014). \emph{Buying Time: The Delayed Crisis of Democratic Capitalism}. Verso.
   945	
   946	\bibitem[Tilly(1990)]{tilly1990}
   947	Charles Tilly (1990). \emph{Coercion, Capital, and European States, AD 990-1990}. Blackwell.
   948	
   949	\bibitem[Treisman(2010)]{treisman2010}
   950	Daniel Treisman (2010). 'Loans for Shares' Revisited. \emph{Post-Soviet Affairs} 26(3). doi:10.2747/1060-586X.26.3.207.
   951	
   952	\bibitem[Tullock(1967)]{tullock1967}
   953	Gordon Tullock (1967). The Welfare Costs of Tariffs, Monopolies, and Theft. \emph{Western Economic Journal} 5(3). doi:10.1111/j.1465-7295.1967.tb01923.x.
   954	
   955	\bibitem[Udovitch(1970)]{udovitch1970}
   956	Abraham L. Udovitch (1970). \emph{Partnership and Profit in Medieval Islam}. Princeton University Press. doi:10.1515/9781400820474.
   957	
   958	\bibitem[Velde and Weir(1992)]{velde1992}
   959	Fran\c{c}ois R. Velde and David R. Weir (1992). The Financial Market and Government Debt Policy in France, 1746-1793. \emph{The Journal of Economic History} 52(1). doi:10.1017/s002205070001024x.
   960	
   961	\bibitem[Vitalis(2007)]{vitalis2007}
   962	Robert Vitalis (2007). \emph{America's Kingdom: Mythmaking on the Saudi Oil Frontier}. Stanford University Press. doi:10.1515/9781503626119.
   963	
   964	\bibitem[Walter and Howie(2011)]{walterhowie2011}
   965	Carl E. Walter and Fraser J. T. Howie (2011). \emph{Red Capitalism: The Fragile Financial Foundation of China's Extraordinary Rise}. Wiley. doi:10.1002/9781119199083.
   966	
   967	\bibitem[Walzer(1983)]{walzer1983}
   968	Michael Walzer (1983). \emph{Spheres of Justice: A Defense of Pluralism and Equality}. Basic Books.
   969	
   970	\bibitem[Wehrey et al.(2009)]{wehrey2009}
   971	Frederic Wehrey, Jerrold D. Green, Brian Nichiporuk, Alireza Nader, Lydia Hansell, Rasool Nafisi, and S. R. Bohandy (2009). The Rise of the Pasdaran: Assessing the Domestic Roles of Iran's Islamic Revolutionary Guards Corps. RAND Corporation, MG-821-OSD.
   972	
   973	\bibitem[Wiessner(2005)]{wiessner2005}
   974	Polly Wiessner (2005). Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity? \emph{Human Nature} 16(2). doi:10.1007/s12110-005-1000-9.
   975	
   976	\bibitem[Wink(1992)]{wink1992}
   977	Walter Wink (1992). \emph{Engaging the Powers: Discernment and Resistance in a World of Domination}. Fortress Press. doi:10.2307/j.ctt1tm7j16.
   978	
   979	\bibitem[Winters(2011)]{winters2011}
   980	Jeffrey A. Winters (2011). \emph{Oligarchy}. Cambridge University Press. doi:10.1017/cbo9780511793806.
   981	
   982	\bibitem[Woodburn(1982)]{woodburn1982}
   983	James Woodburn (1982). Egalitarian Societies. \emph{Man (N.S.)} 17(3). doi:10.2307/2801707.
   984	
   985	\end{thebibliography}
   986	
   987	\end{document}

hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '431,702p' papers/latex/financial-power.tex | nl -ba -v431" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   431	
   432	\begin{example}[A participation threshold]
   433	\label{ex:threshold}
   434	Let $\pi(e,Q)=(1-Q)(1-e^{-e})$, which satisfies the conditions of \cref{prop:financial-power:influence} for $Q<1$. The objective $sV(1-Q)(1-e^{-e})-e$ is concave in $e$ with derivative $sV(1-Q)e^{-e}-1$, so the optimum is $e^*=\ln\bigl(sV(1-Q)\bigr)$ when $sV(1-Q)>1$ and $e^*=0$ otherwise. Actors with shares below the threshold $\bar s=1/\bigl(V(1-Q)\bigr)$ do not invest at all. Take ten actors and $V=10$. At $Q=0.5$ and equal shares of $0.1$, every actor has $sV(1-Q)=0.5<1$ and total investment is zero. If one actor's share rises to $0.55$ and the other nine hold $0.05$ each, that actor invests $\ln 2.75\approx 1.01$ and the others still invest nothing. If contestability then rises to $Q=0.9$, the large holder's product falls to $0.55$ and its investment returns to zero.
   435	\end{example}
   436	
   437	The example states three things in miniature. Concentration activates conversion, because only holders above a threshold find influence worth buying; this is Olson's asymmetry between concentrated and diffuse interests \citep{olson1965}. Contestability shuts conversion off by lowering its marginal return, which is the financial form of the source's Proposition 2 that checks can interrupt transmission \citep{largo2026hbs}. And the threshold depends on the stake $V$, so conversion concentrates in domains where rules are worth much to few, which is consistent with Culpepper's finding that business power is strongest in quiet, technical politics \citep{culpepper2010}.
   438	
   439	The model has clear limits. It is a single-actor decision problem: other actors' spending does not enter $\pi$, so the competition among groups that Becker emphasizes, and the countermobilization that large transfers provoke, are absent \citep{becker1983}. The sign condition $\pi_{eQ}<0$ is an assumption about how contestability works, not a finding, and it would fail if contestability raised the value of expert lobbying by making the process more procedural. The proposition is therefore a conditional comparative static of the kind \citet{largo2026hbs} uses throughout, and its empirical counterpart is hypothesis HF1.
   440	
   441	\subsection{Credit and the discipline of lenders}
   442	
   443	Sovereign borrowing is the oldest form of coupling between private finance and political power. It can be read as capture, with lenders controlling the state, or as a bargain, with lenders disciplined by their need for repayment and the ruler by its need for future credit. A standard repeated-game condition separates the two readings.
   444	
   445	\begin{proposition}[Sovereign credit]
   446	\label{prop:financial-power:sovereign-credit}
   447	A ruler with discount factor $\delta\in(0,1)$ owes a payment $D>0$ in the current period. Continued access to credit yields a net surplus $g>0$ in every future period. Lenders act together, so that a default not excused by an agreed contingency ends all future lending. Then repayment is the ruler's best response if and only if
   448	\[
   449	D\leq\frac{\delta g}{1-\delta}.
   450	\]
   451	\end{proposition}
   452	
   453	\begin{proof}
   454	Repaying costs $D$ now and preserves the surplus stream, whose present value is $\sum_{t\geq 1}\delta^t g=\delta g/(1-\delta)$. Defaulting saves $D$ and ends the stream. Repayment is a best response exactly when $-D+\delta g/(1-\delta)\geq 0$.
   455	\end{proof}
   456	
   457	The condition explains how early modern lenders protected themselves without controlling legislation. Their security came from the ruler's need for future credit, measured by $g$, and from their own capacity to act together, which made exclusion credible. When a fiscal shock raised $D$ above the bound, a payment stop followed, and a negotiated settlement restored the relationship. Drelichman and Voth read the defaults of Philip II in this way, and Conklin attributes the discipline to the Genoese bankers' ability to coordinate \citep{drelichman2011,conklin1998}. If lenders cannot coordinate, because many small lenders compete to replace any lender who is excluded, the threat of exclusion weakens and the bound no longer protects them. The proposition thus identifies when lending is a bargain rather than capture: lenders receive repayment, not legal privileges unrelated to their loans. That is hypothesis HF3.
   458	
   459	North and Weingast argued that the constitutional settlement in seventeenth-century England improved the crown's capacity to borrow by making its commitments credible \citep{northweingast1989}. In the terms of the proposition, a representative assembly that controls taxation can raise the credibility of repayment by shifting authority over $D$ away from the ruler alone. The same logic connects the Cortes of Castile to the Habsburg debt.
   460	
   461	\subsection{Soft budgets, rents and fusion}
   462	
   463	Three further mechanisms move a financial pillar toward capture. The soft budget constraint arises whenever an allocating authority cannot commit to let loss-making units fail \citep{kornai1986}. Kornai developed the concept for socialist enterprises, where the paternalistic state rescued firms as a matter of course. The analogy with private banks considered too large to fail is plausible, but it extends the concept beyond the evidence that Kornai and \citet{largo2026hbs} cite, and we treat it as a hypothesis rather than a finding. Wherever it holds, rescue expectations transfer resources to units with bargaining power, and the transfer is unreviewable when the rescuing authority is not itself accountable.
   464	
   465	Rentier revenue changes the coupling between the financial pillar and the productive pillar. A state that lives on external rents does not depend on taxpayers and therefore need not bargain with them \citep{mahdavy1970,beblawiluciani1987}. Levi's account of quasi-voluntary compliance identifies what is lost: the reciprocal bargain in which rulers provide services and keep promises in exchange for compliance \citep{levi1988}. The rentier mechanism lowers $Q_{\pF}$ by weakening the fiscal voice of producers. Part VI derives the producers' side of the same mechanism (Proposition 6.6 of \citealt{long2026productive}); the allocation side belongs here. The evidence that the mechanism operates is mixed, as \cref{sec:literature} records.
   466	
   467	Fusion of the financial and coercive pillars in one organization is the most direct route to high $C_{\pF\pC}$. Part V shows that in large collectives sanctioners must be paid or provisioned, or else rewarded by belief (Proposition 3.5 of \citealt{long2026coercive}), which derives the dependency of coercion on resource allocation; fusion places both ends of that dependency in one organization. Business arms of security forces, whether the Revolutionary Guards' firms in Iran \citep{wehrey2009} or the military enterprise of early modern monarchies, give one organization both resources and the means of sanction. The rival explanation is public-goods provision: the same organizations build infrastructure and conduct reconstruction, and their size may reflect capacity rather than capture. Distinguishing the two requires evidence on procurement, competition, and review, not on size.
   468	
   469	\subsection{Checks}
   470	
   471	The checks that interrupt these mechanisms are specific. Open entry, enforced by antitrust and by competitive procurement, raises the number of actors who can contest a holder's position; Rajan and Zingales show that incumbents oppose it for that reason \citep{rajan2003}. A hard budget constraint, under which failing units actually exit, removes the rents of rescue. Disclosure of contributions, lobbying, and beneficial ownership makes the conversion pathway visible, which is a precondition of contesting it. Independent audit and independent central banking separate the review of financial decisions from those who make them, although independence relocates concentration into the reviewing body. And coordinated lenders, organized labor, and representative assemblies supply countervailing power from within the financial pillar itself. Each check raises $Q_{\pF}$ or lowers a coupling; none lowers the necessity of the pillar, which no check can or should remove.
   472	
   473	\section{Measurement and testable hypotheses}
   474	\label{sec:measurement}
   475	
   476	\subsection{Indicators}
   477	
   478	Measurement of the financial pillar should proceed subdomain by subdomain, as \cref{prop:financial-power:aggregation-gap} recommends, and should code contestability separately from concentration. \Cref{tab:indicators} lists indicators drawn from sources that already exist. Cross-national governance indicators, such as the Worldwide Governance Indicators and the V-Dem data, supply partial measures of contestability \citep{kaufmann2010,coppedge2011}; they do not measure control shares and should not be used as proxies for them.
   479	
   480	\begin{table}[t]
   481	\centering
   482	\small
   483	\caption{Indicators for the financial pillar. Concentration indicators enter $H_{\pF}$ by subdomain; contestability indicators enter $Q_{\pF}$.}
   484	\label{tab:indicators}
   485	\begin{tabularx}{\linewidth}{@{}L{2.6cm}YY@{}}
   486	\toprule
   487	Construct & Indicators & Main pitfall \\
   488	\midrule
   489	Ownership concentration & Asset shares, ownership pyramids, and dual-class control & Ownership understates control where party or family ties matter \\
   490	Credit concentration & Bank credit shares by lender and by borrower & State and private banks may follow different rules \\
   491	Budget discretion & Share of spending allocated without formula or tender & Discretion can serve legitimate emergencies \\
   492	Procurement & Concentration of awards by recipient, and the share awarded without competition & Specialized markets have few qualified suppliers \\
   493	Contestability & Entry barriers, audit independence, bankruptcy enforcement, and disclosure regimes & Laws on paper may not bind in practice \\
   494	Conversion & Connected-firm returns, connected lending, and lobbying linked to outcomes & Large firms become connected because they are large \\
   495	\bottomrule
   496	\end{tabularx}
   497	\end{table}
   498	
   499	The capture-link coding of \citet{largo2026hbs} supplies the unit of evidence. A coded link records the actor, the mechanism, the evidence of privileged access, the review that applied, the decision, and the material effect, together with counterevidence. The population of coded events should include all decisions in a preregistered sector, not only scandals, since a sample of scandals selects on the outcome.
   500	
   501	\subsection{Hypotheses}
   502	
   503	\Cref{tab:hypotheses} states seven hypotheses specific to the financial pillar, each refining one of the source hypotheses H1 to H6 and each with a stated falsifier.
   504	
   505	\begin{table}[t]
   506	\centering
   507	\small
   508	\caption{Hypotheses for the financial pillar, each paired with an observation that would falsify it.}
   509	\label{tab:hypotheses}
   510	\begin{tabularx}{\linewidth}{@{}L{1.1cm}YY@{}}
   511	\toprule
   512	Label & Hypothesis & Falsifier \\
   513	\midrule
   514	HF1 & The conversion elasticity $\varepsilon_{\pF\to\pP}$ is higher on technical issues of low salience than on salient ones & Equal or higher elasticity on salient issues, or no elasticity once preferences shared across income groups are controlled \\
   515	HF2 & In party-state command sectors, the appointment rank of an enterprise head predicts credit and inputs after controlling for profitability and plan targets & Profitability predicts allocation better than rank \\
   516	HF3 & Where a ruler needs repeated credit, lenders secure repayment without obtaining legal privileges unrelated to their loans & Lenders obtain legal advantages that do not secure repayment \\
   517	HF4 & Liberalizing entry reduces the rents of connected incumbents & Rents of connected firms persist after entry reform \\
   518	HF5 & A higher share of non-tax revenue lowers fiscal bargaining with taxpayers and raises discretionary allocation & A null effect in within-country panels \\
   519	HF6 & Where one organization holds financial and coercive control, financial contestability falls & Fused organizations face the same procurement competition and audit as others \\
   520	HF7 & Credible bankruptcy of large failing units is associated with lower rents & Rescues are followed by lower, not higher, subsequent rents \\
   521	\bottomrule
   522	\end{tabularx}
   523	\end{table}
   524	
   525	HF1 refines source hypothesis H1 and follows from \cref{prop:financial-power:influence} together with Culpepper's account of quiet politics \citep{culpepper2010}; the alternative falsifier comes from Branham, Soroka, and Wlezien \citep{branham2017}. HF2 specializes source hypothesis H3. HF3 follows from \cref{prop:financial-power:sovereign-credit} and the Habsburg evidence \citep{drelichman2011}. HF4 tests the argument of Rajan and Zingales \citep{rajan2003} and the evidence on connected lending: Khwaja and Mian find that politically connected firms in Pakistan obtained more credit from government banks and defaulted more often \citep{khwaja2005}, and Fisman finds that the market value of firms connected to Suharto fell when rumors of his ill health spread \citep{fisman2001}. HF5 tests the rentier mechanism against the within-country null of Haber and Menaldo \citep{habermenaldo2011}. HF6 states the fusion mechanism with its public-goods rival. HF7 tests the soft budget constraint.
   526	
   527	\subsection{Rival explanations and identification}
   528	
   529	Each hypothesis faces four rival explanations that coding must address. Economies of scale and natural monopoly can produce high concentration without any political cause. Public-goods provision can justify discretion and concentration, which is the source's Proposition 4 and hypothesis H6 \citep{largo2026hbs}. Survivorship can reverse the causal arrow, since firms that grow large for economic reasons attract political connections. And preference alignment can make the wealthy appear influential when they merely agree with the majority \citep{branham2017}. The event-study and latent-variable designs specified by \citet{largo2026hbs} address some of these threats, but each requires assumptions, such as parallel trends before a reform and measurement invariance across regimes, that must be tested rather than assumed. Measurement invariance is the most demanding: a control share in a Soviet ministry and a control share in a private bank may not be the same construct, and if invariance fails the comparison must use regime-specific models.
   530	
   531	\section{The Revelation reading}
   532	\label{sec:revelation}
   533	
   534	The series takes its name from Revelation 13, and its theological vocabulary is typological. The beast of Revelation 13 and the city of Babylon in chapters 17 and 18 are read as images of a recurring configuration of power that claims ultimate loyalty, not as predictions of a particular future state, person, or technology. This is one of several interpretive traditions. Preterist readings locate the text in its first-century setting and read the beast as Roman imperial power and the imperial cult of the province of Asia \citep{collins1984,kraybill1996}. Typological or idealist readings see Rome as a paradigm of a pattern that recurs \citep{bauckham1993}. Futurist readings identify the beast with a coming ruler or system; the history of such identifications is a history of failures, as McGinn and Fuller document \citep{mcginn1998,fuller1995}, and the series excludes them.
   535	
   536	Two passages bear on the financial pillar. The first is Revelation 13:16-17: ``And he causeth all, both small and great, rich and poor, free and bond, to receive a mark in their right hand, or in their foreheads: And that no man might buy or sell, save he that had the mark, or the name of the beast, or the number of his name.'' The image is economic participation conditioned on allegiance. In the vocabulary of this paper, it describes a financial pillar whose settlement procedure for exchange is gated by a test of loyalty administered by the ideological pillar: the coupling $C_{\pF\pI}$ is complete, and contestability for those who fail the test is zero. Part VI formalizes the same condition from the producers' side as a participation gate, access to exchange conditional on allegiance, and treats the passage as its limiting case (Definition 6.7 and Proposition 6.8 of \citealt{long2026productive}). Kraybill reads the passage against the participation of Asian merchants and artisans in trade guilds whose life was bound up with the imperial cult, so that commerce required at least tacit participation in worship \citep{kraybill1996}.
   537	
   538	The second is the lament over Babylon in Revelation 18. The merchants of the earth ``are waxed rich through the abundance of her delicacies'' (18:3), they weep ``for no man buyeth their merchandise any more'' (18:11), and the chapter's list of cargoes ends with ``slaves, and souls of men'' (18:13). Bauckham reads the chapter as an economic critique of Rome's trade empire, in which the wealth of the city depends on the extraction of goods from the provinces and the trade in persons is the last item of the list \citep{bauckham1991}. Koester and Aune give the philological and historical commentary \citep{koester2014,aune1998c}, and Rossing reads the chapter as a choice between two cities, Babylon and the new Jerusalem \citep{rossing1999}. The trade in slaves in 18:13 is literal: it refers to the Roman slave trade, and nothing in this reading equates it with wage labor, taxation, or other forms of economic dependence, which the series distinguishes from chattel slavery.
   539	
   540	The typological reading names the condition under which the series' structural claim acquires moral weight. The text does not condemn the existence of buying and selling; it condemns a configuration in which access to exchange depends on allegiance and the city's wealth depends on extraction and the trade in persons. That configuration is Proposition~B, the contingent capture of the financial pillar by a coalition that has also captured belief and coercion, not Proposition~A, the existence of an allocation function. The call of Revelation 18:4, ``Come out of her, my people,'' is in this reading an image of exit, one of the checks that Part VI treats. Wink's theology of the powers draws the same distinction: institutions are necessary to human life, become a system of domination when organized around it, and remain open to transformation \citep{wink1992}. The mapping from text to model is an interpretive claim of this series, offered as an aid to comparison; it is not a settled exegetical result. Collins's argument that Revelation responds to a crisis perceived by its author and audience, rather than to an empirically general persecution \citep{collins1984}, is a reminder that the text's images express a judgment about an order, which a comparative political economy cannot simply import as evidence.
   541	
   542	\section{Objections and scope conditions}
   543	\label{sec:objections}
   544	
   545	A pluralist will object that resource control in democracies has no apex: many holders compete, coalitions shift by issue, and resources often lose. The objection is correct about the evidence it cites \citep{baumgartner2009,ansolabehere2003} and does not touch the necessity claim, which concerns the existence of the function, not its concentration. It does bear on the capture claim, which is why that claim is stated as a set of hypotheses with falsifiers rather than as a description.
   546	
   547	A Marxian critic will object from the other side that the financial pillar abstracts from class: control of the means of production is a social relation, not a share in an index. The model accommodates the relation, since control shares can be computed over the means of production and the coupling $C_{\pF\pW}$ records employer power over workers, but it does not presuppose that one class holds the pillar in every regime. The party-state cases, where control follows appointment rather than ownership, show why that presupposition would mislead.
   548	
   549	A market liberal will object that in a market nobody allocates. The reply in \cref{sec:necessity} applies: allocation by price is a settlement procedure whose control shares follow the distribution of endowments, and property rules are themselves outputs of other pillars. The objection has force against a different claim, that markets concentrate control more than other modes, and that claim is not made here.
   550	
   551	A philosopher of science will object that the necessity claim is true by definition. It is not, for two reasons. \Cref{def:financial-power:settlement} excludes unregulated contest, so a collective that resolves conflicts by fighting without shared expectations would lack the pillar; and \cref{ass:hazard} is an empirical assumption that could fail. The falsifier stated in \cref{sec:necessity} is a possible observation. What the claim does not do is explain why any particular institution exists, and \cref{sec:necessity} disclaims that explanation explicitly \citep{elster1983,hempel1959}.
   552	
   553	A reader concerned with even-handedness may object that Islamic and Catholic polities appear as types at all. They appear because their rulers drew legitimacy from religious law and religious institutions, which shaped how the financial pillar was organized, and the comparison records the internal diversity of each: the waqf and the tax farm, the Ottoman and the Saudi state, the Habsburg debt and the papal Camera. No claim is made that either religion determines an allocation regime, and the evidence reviewed contradicts any such claim.
   554	
   555	The comparative claims carry less weight than the formal ones. They rest on secondary scholarship, none of the six types has been coded under a preregistered protocol, and the coupling entries in \cref{tab:regimes} are hypotheses about what such coding would find.
   556	
   557	\section{Conclusion}
   558	\label{sec:conclusion}
   559	
   560	The financial pillar is necessary in a precise and limited sense. Given that claims on finite resources conflict and that unsettled conflict risks dissolution, a collective without a recognized procedure for settling those claims cannot persist, and in any collective that does persist almost all conflicts are settled by such a procedure. The procedure can be a sharing norm in a foraging camp, a cattle payment arranged by a mediator, a waqf deed, a crown loan, a plan target, or a market price. Its necessity implies nothing about who holds it: control can be as dispersed as the index allows or held by one actor, and it can be fully contestable or not contestable at all.
   561	
   562	The comparison of six regime types shows the same function held by institutions that differ almost entirely, with control paths that run from wealth to rules, from appointment to allocation, from rents to rulers, and from lenders to kings. Each type has documented capture episodes and documented checks. Whether a particular financial pillar has been captured is therefore an empirical question about concentration, contestability, and coupling in a given polity and period, and the hypotheses stated here make it answerable. What remains uncertain is the measurement itself: until control shares and couplings are coded under a common protocol, the comparative claims of this paper are well-grounded hypotheses rather than estimates. The ideology that justifies resource command changes from one order to the next. The question of who controls the resources remains, and every order must answer it.
   563	
   564	\begin{thebibliography}{99}
   565	\small
   566	\raggedright
   567	
   568	\bibitem[Alesina and Summers(1993)]{alesina1993}
   569	Alberto Alesina and Lawrence H. Summers (1993). Central Bank Independence and Macroeconomic Performance: Some Comparative Evidence. \emph{Journal of Money, Credit and Banking} 25(2). doi:10.2307/2077833.
   570	
   571	\bibitem[Allen et al.(2005)]{allen2005}
   572	Franklin Allen, Jun Qian, and Meijun Qian (2005). Law, Finance, and Economic Growth in China. \emph{Journal of Financial Economics} 77(1). doi:10.1016/j.jfineco.2004.06.010.
   573	
   574	\bibitem[Ansolabehere et al.(2003)]{ansolabehere2003}
   575	Stephen Ansolabehere, John M. de Figueiredo, and James M. Snyder (2003). Why Is There So Little Money in U.S. Politics? \emph{Journal of Economic Perspectives} 17(1). doi:10.1257/089533003321164976.
   576	
   577	\bibitem[Aune(1998)]{aune1998c}
   578	David E. Aune (1998). \emph{Revelation 17-22}. Word Biblical Commentary 52C, Thomas Nelson.
   579	
   580	\bibitem[Bartels(2008)]{bartels2008}
   581	Larry M. Bartels (2008). \emph{Unequal Democracy: The Political Economy of the New Gilded Age}. Princeton University Press. doi:10.1515/9781400883363.
   582	
   583	\bibitem[Bauckham(1991)]{bauckham1991}
   584	Richard Bauckham (1991). The Economic Critique of Rome in Revelation 18. In \emph{Images of Empire}, edited by Loveday Alexander, JSOT Press (JSOTSup 122).
   585	
   586	\bibitem[Bauckham(1993)]{bauckham1993}
   587	Richard Bauckham (1993). \emph{The Theology of the Book of Revelation}. Cambridge University Press. doi:10.1017/cbo9780511819858.
   588	
   589	\bibitem[Baumgartner et al.(2009)]{baumgartner2009}
   590	Frank R. Baumgartner, Jeffrey M. Berry, Marie Hojnacki, David C. Kimball, and Beth L. Leech (2009). \emph{Lobbying and Policy Change: Who Wins, Who Loses, and Why}. University of Chicago Press. doi:10.7208/chicago/9780226039466.001.0001.
   591	
   592	\bibitem[Beblawi and Luciani(1987)]{beblawiluciani1987}
   593	Hazem Beblawi and Giacomo Luciani (eds.) (1987). \emph{The Rentier State}. Croom Helm. doi:10.4324/9781315684864.
   594	
   595	\bibitem[Becker(1983)]{becker1983}
   596	Gary S. Becker (1983). A Theory of Competition among Pressure Groups for Political Influence. \emph{The Quarterly Journal of Economics} 98(3). doi:10.2307/1886017.
   597	
   598	\bibitem[Berliner(1957)]{berliner1957}
   599	Joseph S. Berliner (1957). \emph{Factory and Manager in the USSR}. Harvard University Press. doi:10.4159/harvard.9780674188273.
   600	
   601	\bibitem[Berman(2006)]{berman2006}
   602	Sheri Berman (2006). \emph{The Primacy of Politics: Social Democracy and the Making of Europe's Twentieth Century}. Cambridge University Press. doi:10.1017/cbo9780511791109.
   603	
   604	\bibitem[Bertrand et al.(2014)]{bertrand2014}
   605	Marianne Bertrand, Matilde Bombardini, and Francesco Trebbi (2014). Is It Whom You Know or What You Know? An Empirical Assessment of the Lobbying Process. \emph{American Economic Review} 104(12). doi:10.1257/aer.104.12.3885.
   606	
   607	\bibitem[Black et al.(2000)]{black2000}
   608	Bernard Black, Reinier Kraakman, and Anna Tarassova (2000). Russian Privatization and Corporate Governance: What Went Wrong? \emph{Stanford Law Review} 52(6). doi:10.2307/1229501.
   609	
   610	\bibitem[Blanes i Vidal et al.(2012)]{blanes2012}
   611	Jordi Blanes i Vidal, Mirko Draca, and Christian Fons-Rosen (2012). Revolving Door Lobbyists. \emph{American Economic Review} 102(7). doi:10.1257/aer.102.7.3731.
   612	
   613	\bibitem[Boehm(1999)]{boehm1999}
   614	Christopher Boehm (1999). \emph{Hierarchy in the Forest: The Evolution of Egalitarian Behavior}. Harvard University Press. doi:10.2307/j.ctvjf9xr4.
   615	
   616	\bibitem[Bourdieu(1989)]{bourdieu1989}
   617	Pierre Bourdieu (1989). Social Space and Symbolic Power. \emph{Sociological Theory} 7(1). doi:10.2307/202060.
   618	
   619	\bibitem[Branham et al.(2017)]{branham2017}
   620	J. Alexander Branham, Stuart N. Soroka, and Christopher Wlezien (2017). When Do the Rich Win? \emph{Political Science Quarterly} 132(1). doi:10.1002/polq.12577.
   621	
   622	\bibitem[Carpenter and Moss(2014)]{carpentermoss2014}
   623	Daniel Carpenter and David A. Moss (eds.) (2014). \emph{Preventing Regulatory Capture: Special Interest Influence and How to Limit It}. Cambridge University Press. doi:10.1017/CBO9781139565875.
   624	
   625	\bibitem[Chaudhry(1997)]{chaudhry1997}
   626	Kiren Aziz Chaudhry (1997). \emph{The Price of Wealth: Economies and Institutions in the Middle East}. Cornell University Press. doi:10.7591/9781501700347.
   627	
   628	\bibitem[\c{C}izak\c{c}a(1996)]{cizakca1996}
   629	Murat \c{C}izak\c{c}a (1996). \emph{A Comparative Evolution of Business Partnerships: The Islamic World and Europe, with Specific Reference to the Ottoman Archives}. Brill.
   630	
   631	\bibitem[Clastres(1987)]{clastres1987}
   632	Pierre Clastres (1987). \emph{Society against the State: Essays in Political Anthropology (1974), trans. Robert Hurley}. Zone Books. doi:10.2307/j.ctv1595m3p.
   633	
   634	\bibitem[Collins(1984)]{collins1984}
   635	Adela Yarbro Collins (1984). \emph{Crisis and Catharsis: The Power of the Apocalypse}. Westminster Press.
   636	
   637	\bibitem[Conklin(1998)]{conklin1998}
   638	James Conklin (1998). The Theory of Sovereign Debt and Spain under Philip II. \emph{Journal of Political Economy} 106(3). doi:10.1086/250019.
   639	
   640	\bibitem[Coppedge et al.(2011)]{coppedge2011}
   641	Michael Coppedge, John Gerring, David Altman, Michael Bernhard, Steven Fish, Allen Hicken, Matthew Kroenig, Staffan I. Lindberg, Kelly McMann, Pamela Paxton, Holli A. Semetko, Svend-Erik Skaaning, Jeffrey Staton, and Jan Teorell (2011). Conceptualizing and Measuring Democracy: A New Approach. \emph{Perspectives on Politics} 9(2). doi:10.1017/S1537592711000880.
   642	
   643	\bibitem[Cox et al.(2010)]{cox2010}
   644	Michael Cox, Gwen Arnold, and Sergio Villamayor Tomas (2010). A Review of Design Principles for Community-based Natural Resource Management. \emph{Ecology and Society} 15(4). doi:10.5751/ES-03704-150438.
   645	
   646	\bibitem[Culpepper(2010)]{culpepper2010}
   647	Pepper D. Culpepper (2010). \emph{Quiet Politics and Business Power: Corporate Control in Europe and Japan}. Cambridge University Press. doi:10.1017/cbo9780511760716.
   648	
   649	\bibitem[Dal B\'o(2006)]{dalbo2006}
   650	Ernesto Dal B\'o (2006). Regulatory Capture: A Review. \emph{Oxford Review of Economic Policy} 22(2). doi:10.1093/oxrep/grj013.
   651	
   652	\bibitem[de Roover(1963)]{deroover1963}
   653	Raymond de Roover (1963). \emph{The Rise and Decline of the Medici Bank, 1397-1494}. Harvard University Press.
   654	
   655	\bibitem[Doyle(1996)]{doyle1996}
   656	William Doyle (1996). \emph{Venality: The Sale of Offices in Eighteenth-Century France}. Oxford University Press. doi:10.1093/acprof:oso/9780198205364.001.0001.
   657	
   658	\bibitem[Drelichman and Voth(2011)]{drelichman2011}
   659	Mauricio Drelichman and Hans-Joachim Voth (2011). Lending to the Borrower from Hell: Debt and Default in the Age of Philip II. \emph{The Economic Journal} 121(557). doi:10.1111/j.1468-0297.2011.02442.x.
   660	
   661	\bibitem[Drelichman and Voth(2014)]{drelichman2014}
   662	Mauricio Drelichman and Hans-Joachim Voth (2014). \emph{Lending to the Borrower from Hell: Debt, Taxes, and Default in the Age of Philip II}. Princeton University Press.
   663	
   664	\bibitem[Ekelund et al.(1996)]{ekelund1996}
   665	Robert B. Ekelund, Robert F. Hebert, Robert D. Tollison, Gary M. Anderson, and Audrey B. Davidson (1996). \emph{Sacred Trust: The Medieval Church as an Economic Firm}. Oxford University Press.
   666	
   667	\bibitem[El-Gamal(2006)]{elgamal2006}
   668	Mahmoud A. El-Gamal (2006). \emph{Islamic Finance: Law, Economics, and Practice}. Cambridge University Press. doi:10.1017/CBO9780511753756.
   669	
   670	\bibitem[Ellickson(1991)]{ellickson1991}
   671	Robert C. Ellickson (1991). \emph{Order without Law: How Neighbors Settle Disputes}. Harvard University Press. doi:10.4159/9780674036437.
   672	
   673	\bibitem[Elster(1983)]{elster1983}
   674	Jon Elster (1983). \emph{Explaining Technical Change: A Case Study in the Philosophy of Science}. Cambridge University Press.
   675	
   676	\bibitem[Esping-Andersen(1985)]{esping1985}
   677	G\"osta Esping-Andersen (1985). \emph{Politics against Markets: The Social Democratic Road to Power}. Princeton University Press. doi:10.1515/9781400886203.
   678	
   679	\bibitem[Evans-Pritchard(1940)]{evanspritchard1940}
   680	E. E. Evans-Pritchard (1940). \emph{The Nuer: A Description of the Modes of Livelihood and Political Institutions of a Nilotic People}. Clarendon Press.
   681	
   682	\bibitem[Faccio(2006)]{faccio2006}
   683	Mara Faccio (2006). Politically Connected Firms. \emph{American Economic Review} 96(1). doi:10.1257/000282806776157704.
   684	
   685	\bibitem[Fisman(2001)]{fisman2001}
   686	Raymond Fisman (2001). Estimating the Value of Political Connections. \emph{American Economic Review} 91(4). doi:10.1257/aer.91.4.1095.
   687	
   688	\bibitem[Fuller(1995)]{fuller1995}
   689	Robert C. Fuller (1995). \emph{Naming the Antichrist: The History of an American Obsession}. Oxford University Press. doi:10.1093/acprof:oso/9780195109795.001.0001.
   690	
   691	\bibitem[Gilens and Page(2014)]{gilens2014}
   692	Martin Gilens and Benjamin I. Page (2014). Testing Theories of American Politics: Elites, Interest Groups, and Average Citizens. \emph{Perspectives on Politics} 12(3). doi:10.1017/S1537592714001595.
   693	
   694	\bibitem[Goodhart(1988)]{goodhart1988}
   695	Charles A. E. Goodhart (1988). \emph{The Evolution of Central Banks}. MIT Press.
   696	
   697	\bibitem[Graeber and Wengrow(2021)]{graeber2021}
   698	David Graeber and David Wengrow (2021). \emph{The Dawn of Everything: A New History of Humanity}. Farrar, Straus and Giroux.
   699	
   700	\bibitem[Gregory(2004)]{gregory2004}
   701	Paul R. Gregory (2004). \emph{The Political Economy of Stalinism: Evidence from the Soviet Secret Archives}. Cambridge University Press. doi:10.1017/cbo9780511615856.
   702	

exec
/usr/local/bin/zsh -lc "sed -n '150,430p' papers/latex/financial-power.tex | nl -ba -v150" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   150	\end{proposition}
   151	
   152	\begin{proof}
   153	The aggregate shares sum to one, since $\sum_i\bar s_i=\sum_k\beta_k\sum_i s^k_i=\sum_k\beta_k=1$, so $H(\bar s)$ is a valid concentration index. For a fixed actor $i$, the identity $\sum_k\beta_k(s^k_i)^2-\bigl(\sum_k\beta_k s^k_i\bigr)^2=\sum_k\beta_k(s^k_i-\bar s_i)^2$ is the usual decomposition of a second moment into a squared mean and a variance; it uses only $\sum_k\beta_k=1$. Summing over $i$ gives
   154	\[
   155	\sum_k\beta_k\sum_i(s^k_i)^2-\sum_i\bar s_i^{\,2}=\sum_i\operatorname{Var}_\beta(s^{\cdot}_i),
   156	\]
   157	which is \eqref{eq:aggregation-gap}. Each variance is nonnegative and vanishes exactly when $s^k_i=\bar s_i$ for every $k$ with $\beta_k>0$.
   158	\end{proof}
   159	
   160	\begin{example}[Separated and fused holdings]
   161	\label{ex:aggregation}
   162	Consider three actors and three equally weighted subdomains: land, credit, and the public budget. In a \emph{separated} configuration actor $k$ holds all of subdomain $k$. Each subdomain then has $H=1$, so the weighted mean of subdomain concentrations is $1$, while aggregate shares are $(1/3,1/3,1/3)$ and $H(\bar s)=1/3$. The gap is $2/3$. In a \emph{fused} configuration one actor holds all three subdomains, every index equals $1$, and the gap is $0$. The numbers are hypothetical; the point is that the aggregate index rates the separated polity as dispersed even though every subdomain is a monopoly.
   163	\end{example}
   164	
   165	The gap measures within-pillar specialization: it is large when different actors dominate different subdomains and zero when the same actors hold the same shares everywhere. It is therefore a within-pillar analogue of the cross-pillar integration that \citet{largo2026hbs} records with $C_{mn,t}$, but it is not that object, and Part VII owns the formal treatment of integration. The practical lesson is that a polity should be coded subdomain by subdomain, with the aggregate reported alongside the gap, since a low aggregate index can conceal monopolies that do not overlap.
   166	
   167	\section{Necessity of the financial pillar}
   168	\label{sec:necessity}
   169	
   170	\subsection{The derivation}
   171	
   172	The scarcity axiom alone does not imply that a collective must have a financial pillar. A group could in principle resolve every conflict by unregulated contest. The derivation therefore needs a second assumption that says what unsettled conflict costs, and it is better to state that assumption openly than to hide it inside the word ``persistence''.
   173	
   174	\begin{assumption}[Scarcity, pillar form]
   175	\label{ass:scarcity}
   176	Time is discrete, $t=1,2,\dots$, and $\mathcal{F}_{t-1}$ denotes the history up to the end of period $t-1$. On the event that the collective exists at the start of period $t$, a conflict in the sense of \cref{def:financial-power:allocation-problem} occurs in period $t$ with conditional probability at least $p>0$ given $\mathcal{F}_{t-1}$.
   177	\end{assumption}
   178	
   179	\begin{assumption}[Dissolution hazard]
   180	\label{ass:hazard}
   181	On the event that a conflict in period $t$ is unsettled, the collective dissolves in period $t$ with conditional probability at least $q>0$ given $\mathcal{F}_{t-1}$ and on the conflict being unsettled. Dissolution means that the collective ceases to make and enforce collective decisions as one body: it breaks into groups that no longer coordinate, or it suffers violence that ends cooperation.
   182	\end{assumption}
   183	
   184	At most one conflict is indexed per period; a period with several conflicts counts once, and \cref{ass:hazard} applies to any period that contains an unsettled conflict. Write $Y_T$ for the number of periods in $1,\dots,T$ with a conflict, $Z_T$ for the number of periods with an unsettled conflict, with the convention $Z_T/Y_T:=0$ when $Y_T=0$, and $S_T$ for the event that the collective survives through period $T$.
   185	
   186	\begin{proposition}[Necessity of the financial pillar]
   187	\label{prop:financial-power:necessity}
   188	Under \cref{ass:scarcity,ass:hazard}, for every horizon $T$ and every integer $k\geq 0$:
   189	\begin{enumerate}
   190	\item[(a)] $\Prob(S_T\cap\{Z_T\geq k\})\leq(1-q)^k$;
   191	\item[(b)] $\Prob(S_T\cap\{Y_T<pT/2\})\leq e^{-pT/8}$;
   192	\item[(c)] if the collective has no settlement procedure at all, so that $Z_T=Y_T$, then $\Prob(S_T)\leq(1-q)^{\lceil pT/2\rceil}+e^{-pT/8}$;
   193	\item[(d)] if $\Prob(S_T)\geq\nu>0$, then
   194	\[
   195	\Prob\Bigl(\frac{Z_T}{Y_T}\geq\frac{2k}{pT}\,\Big|\,S_T\Bigr)\leq\frac{(1-q)^k+e^{-pT/8}}{\nu}.
   196	\]
   197	\end{enumerate}
   198	In particular, a collective without a financial pillar cannot survive with probability bounded away from zero as the horizon grows, and in a collective that does survive with probability at least $\nu$ for every horizon, the share of conflicts settled by a recognized procedure converges to one in conditional probability.
   199	\end{proposition}
   200	
   201	\begin{proof}
   202	(a) Let $\tau_j$ be the period of the $j$-th unsettled conflict, with $\tau_j=\infty$ if there is none, and let $A_j$ be the event that $\tau_j\leq T$ and the collective survives period $\tau_j$. Set $A_0$ to be the sure event. A $j$-th unsettled conflict can occur only if the collective survived the $(j-1)$-th, so $A_j\subseteq A_{j-1}$. Conditional on the history before $\tau_j$ and on the conflict being unsettled, \cref{ass:hazard} gives survival probability at most $1-q$. Hence $\Prob(A_j)\leq(1-q)\Prob(\tau_j\leq T,\ \text{alive at }\tau_j)\leq(1-q)\Prob(A_{j-1})$, and by induction $\Prob(A_k)\leq(1-q)^k$. If the collective survives through $T$ and $Z_T\geq k$, then the $k$-th unsettled conflict occurred by $T$ and was survived, so $S_T\cap\{Z_T\geq k\}\subseteq A_k$.
   203	
   204	(b) Enlarge the probability space with independent uniform variables $U_1,U_2,\dots$ on $[0,1]$. By \cref{ass:scarcity}, the conflict indicator in period $t$ can be represented as $\mathbf{1}\{U_t\leq p_t\}$ for an $\mathcal{F}_{t-1}$-measurable $p_t\geq p$ while the collective exists; after dissolution, define the indicator as $\mathbf{1}\{U_t\leq p\}$. The extended count then satisfies $\tilde Y_T\geq B_T=\sum_{t\leq T}\mathbf{1}\{U_t\leq p\}$, which is binomial with mean $pT$, and $\tilde Y_T=Y_T$ on $S_T$. The multiplicative Chernoff bound for the lower tail of a binomial variable, $\Prob(B_T\leq(1-\delta)pT)\leq\exp(-\delta^2pT/2)$, with $\delta=1/2$ gives $\Prob(S_T\cap\{Y_T<pT/2\})\leq\Prob(B_T<pT/2)\leq e^{-pT/8}$.
   205	
   206	(c) If every conflict is unsettled, then on $S_T\cap\{Y_T\geq pT/2\}$ we have $Z_T\geq\lceil pT/2\rceil$, so by (a) that event has probability at most $(1-q)^{\lceil pT/2\rceil}$. Adding the bound in (b) for the complementary part of $S_T$ gives the claim.
   207	
   208	(d) On $S_T\cap\{Z_T<k\}\cap\{Y_T\geq pT/2\}$ we have $Z_T/Y_T<2k/(pT)$. The event in the numerator of the conditional probability is therefore contained in $(S_T\cap\{Z_T\geq k\})\cup(S_T\cap\{Y_T<pT/2\})$, whose probability is bounded by (a) and (b). Dividing by $\Prob(S_T)\geq\nu$ gives the inequality. Taking $k=\lceil\sqrt T\,\rceil$, the threshold $2k/(pT)$ and the bound both tend to zero as $T\to\infty$, which proves the final statement.
   209	\end{proof}
   210	
   211	The proposition is a conditions-of-persistence result. It says that collectives without a financial pillar do not last; it does not say that any particular collective acquired its pillar because the pillar helps it last. Elster's objection to functional explanation applies with full force here: an account of why an institution exists by reference to its beneficial effects requires a feedback mechanism from effect to cause, and none is asserted \citep{elster1983}. Hempel's objection also applies: from the need for a function nothing follows about which institution supplies it, since many functional equivalents can satisfy the same need \citep{hempel1959,merton1968}. The proposition is accordingly stated about the class of settlement procedures, not about property, markets, treasuries, or banks.
   212	
   213	\begin{example}[Survival without settlement]
   214	\label{ex:survival}
   215	Suppose, purely for illustration, that a band of foragers meets a conflict over some good in at least one week in ten ($p=0.1$), and that each unsettled conflict carries a five percent chance of permanent fission or lethal violence ($q=0.05$). If the band had no settlement procedure at all, \cref{prop:financial-power:necessity}(c) bounds its probability of surviving ten years ($T=520$ weeks) by $0.95^{26}+e^{-6.5}\approx 0.265$, and of surviving fifty years ($T=2600$) by $0.95^{130}+e^{-32.5}\approx 0.0013$. The parameters are invented; the geometric decay is not.
   216	\end{example}
   217	
   218	\subsection{Scope of the assumptions}
   219	
   220	The derivation rests on \cref{ass:hazard}, and its weak point is there. If unsettled conflicts were costless, so that $q=0$, a collective could persist while every carcass went to whoever seized it first, and the proposition would fail. Two replies narrow rather than remove this possibility. A practice in which the first taker keeps the good, known in advance and accepted by the others, is a settlement procedure in the sense of \cref{def:financial-power:settlement}: it applies to a class of situations, its outcome can be anticipated, and members comply with it. The case that escapes the proposition is therefore a collective whose members fight over goods without any shared expectation of the outcome and suffer no risk of dissolution from doing so. We know of no ethnographic description of such a collective, and the hard cases below suggest the opposite: the societies most often cited as lacking authority spend considerable effort settling claims on goods.
   221	
   222	The second weak point is the meaning of dissolution. Among mobile foragers, a camp can split and its members can join other camps without the wider society ending. If every split counted as dissolution, bands would dissolve constantly and the proposition would say little. The relevant collective is the unit that makes collective decisions, which for the Ju/'hoansi is a network of camps linked by kinship and exchange, not a single camp. A split that follows recognized lines of access, with people moving to places where they hold rights through kin, is itself a settlement procedure, since it assigns people to resources by a rule they anticipate. Fission along such lines is exit, and exit is part of the financial pillar when it reassigns access to land and water. For the same reason the proposition says nothing about transient aggregates such as crowds or short-lived coalitions, which make no collective decisions to sustain. Part VI owns the general treatment of exit and voice (Definition 2.5 of \citealt{long2026productive}).
   223	
   224	\subsection{Minimal forms in stateless and consensus societies}
   225	
   226	The societies that anthropology describes as egalitarian, acephalous, or organized against the state are the natural test set. Each exhibits the financial pillar in a form with no office, no treasury, and dispersed control, and none exhibits its absence.
   227	
   228	Among the Ju/'hoansi of the Kalahari, meat from a large animal is distributed according to rules that assign the role of distributor to the owner of the arrow that killed it, and arrows circulate as gifts, so that the distributor is often not the hunter \citep{marshall1976,lee1979}. Distribution follows kinship and camp membership, and a successful hunter who boasts is met with ritualized deprecation of the kill, which Lee describes as ``insulting the meat'' \citep{lee2013}. Wiessner's records of everyday talk show that criticism and complaint about failures to share are frequent and that they bring offenders back into line \citep{wiessner2005}. Each element meets \cref{def:financial-power:settlement}: the rules apply to every kill, their outcome can be anticipated, and compliance is enforced by others. Control shares are close to equal, so $H_{\pF}$ is close to $1/n$ and $H^{*}_{\pF}$ close to zero.
   229	
   230	Woodburn's comparison of immediate-return societies, including the Hadza, Mbuti, !Kung, and Batek, generalizes the point. These societies avoid storage and accumulation, make sharing obligatory, and maintain what Woodburn calls leveling mechanisms that prevent any member from converting a temporary advantage into lasting control \citep{woodburn1982}. The equality of these societies is an outcome that institutions produce and defend, not the absence of institutions. Boehm reaches the same conclusion from a broader comparative sample of foragers: egalitarian bands sustain equality through a reverse dominance hierarchy in which the group collectively sanctions would-be dominants, and enforcement of meat-sharing against hoarders is one of its recurring targets \citep{boehm1999}.
   231	
   232	The Nuer, whom Evans-Pritchard described as living in ordered anarchy without government, allocate cattle through kinship, bridewealth, and compensation for homicide \citep{evanspritchard1940}. The so-called leopard-skin chief has no coercive authority; he mediates feuds and helps arrange compensation in cattle, which the parties accept under the shadow of renewed feud. Here the financial pillar settles not only access to grazing and milk but also the price of peace between lineages, and it does so through a mediator without power to command. In the Amazonian societies that Clastres described, the obligation of the headman runs in the opposite direction from tribute: he is expected to be generous with his goods, and a headman who tries to command loses his followers \citep{clastres1987}. Clastres's thesis is that these societies actively prevent political power from separating from the group. That thesis is consistent with the necessity of the financial pillar and incompatible with any claim that its concentration is inevitable.
   233	
   234	Ostrom's studies of long-enduring common-pool resource institutions give the most direct evidence on how small groups settle conflicting claims without either a state or private property in the usual sense \citep{ostrom1990}. The design principles she identified include clearly defined boundaries of the resource and of its users, appropriation rules matched to local conditions, collective-choice arrangements in which those affected can modify the rules, monitoring, graduated sanctions, accessible conflict-resolution mechanisms, recognition of the users' right to organize, and nesting of small units within larger ones. A later review of empirical studies found the principles well supported, with some refinements \citep{cox2010}. In the vocabulary of this paper, a well-designed commons is an allocation regime with dispersed control and high contestability: users appropriate according to known rules, and those rules are themselves open to collective revision. Ellickson's study of ranchers in Shasta County shows a modern variant, in which neighbors settle damage from straying cattle by informal norms rather than by the formal law that nominally applies \citep{ellickson1991}.
   235	
   236	\begin{table}[t]
   237	\centering
   238	\small
   239	\caption{Minimal forms of the financial pillar in societies without a state. Each row reports the settlement procedure, the actors who hold control, and the strongest reading on which the function is absent.}
   240	\label{tab:minimal}
   241	\begin{tabularx}{\linewidth}{@{}L{2.3cm}YYY@{}}
   242	\toprule
   243	Case & Settlement procedure & Holders of control & Strongest counter-reading \\
   244	\midrule
   245	Ju/'hoansi & Arrow-owner rule for meat, gift exchange, demand sharing & All adults, with distributors rotating as arrows circulate & No office allocates anything, but the rules allocate every kill \\
   246	Immediate-return foragers & Obligatory sharing and avoidance of storage & The camp as a whole through leveling sanctions & Little is stored, but what is acquired is still shared by rule \\
   247	Nuer & Cattle rights, bridewealth, and homicide compensation & Lineages, with a mediator who cannot command & No government exists, yet compensation in cattle settles feuds \\
   248	Amazonian groups & The headman's obligatory generosity & The group, which withholds support from a commanding headman & Power is prevented from separating, not allocation from occurring \\
   249	Ostrom commons & Boundaries, appropriation rules, monitoring, and graduated sanctions & Users acting through collective-choice arrangements & No owner or state controls the resource, but the users' rules do \\
   250	\bottomrule
   251	\end{tabularx}
   252	\end{table}
   253	
   254	\Cref{tab:minimal} summarizes the cases. In every row the function is present and its holders are many. The cases thus support the necessity claim and, at the same time, the claim that concentration is contingent. Two cautions apply. Ethnographies of foragers describe groups observed in marginal environments and under the influence of neighbors and states, and foraging societies differ widely among themselves \citep{kelly1995}. Graeber and Wengrow argue further that many early societies moved between hierarchical and egalitarian arrangements, sometimes seasonally, and deliberately chose among political forms \citep{graeber2021}. Neither caution weakens the necessity claim, which requires only that some settlement procedure exist; both strengthen the claim that its concentration is a matter of choice and circumstance.
   255	
   256	\subsection{Counterexample attempts}
   257	
   258	The strongest is Sahlins's ``original affluent society'' \citep{sahlins1972b}. If foragers' wants are limited and easily satisfied, the argument runs, there is no scarcity and so no allocation problem. The reply is that \cref{ass:scarcity} concerns conflicting claims, not shortage. Foragers who spend few hours obtaining food still divide each large kill among claimants who cannot all receive the best portions, and the elaborate sharing rules recorded by Marshall and Lee exist precisely because claims on particular goods conflict \citep{marshall1976,lee1979}. Sahlins's argument, if accepted, lowers $p$; it does not make it zero.
   259	
   260	A second attempt appeals to markets. In a pure market economy, on this view, nobody allocates: prices do. But prices settle conflicts only against a background of property rules that say who may sell what, and those rules are made, interpreted, and enforced by other pillars. Allocation by price is a settlement procedure of the property-and-exchange mode, and control shares in it are given by the distribution of endowments. The market answer to the guiding question is ``whoever owns,'' which is an answer, not a dissolution of the question.
   261	
   262	A third attempt imagines post-scarcity abundance through automation. It fails twice: no existing governance system satisfies it, and even a society with abundant manufactured goods would allocate land, energy, computation, and attention, which remain finite and contested.
   263	
   264	The case that narrows the claim is the one already identified: a collective in which unsettled conflicts carry no risk of dissolution. The falsifier for the financial pillar's necessity is therefore precise. It is a persistent collective whose members hold conflicting claims on some good and resolve them predominantly without any procedure in the sense of \cref{def:financial-power:settlement}. We found no documented case in the sources reviewed (cutoff October 2026).
   265	
   266	\subsection{Necessity without concentration}
   267	
   268	The necessity of the financial pillar implies nothing about how its control is distributed or how open it is to challenge. The next result makes this exact at the level of the pillar; Part VII proves the corresponding non-implication for all six pillars together.
   269	
   270	\begin{proposition}[Pillar-level non-implication]
   271	\label{prop:financial-power:nonimplication}
   272	Fix $n\geq 2$. For every $h\in[1/n,1]$ there is a control-share vector $s$ on $n$ actors with $H(s)=h$. Consequently, for every $h\in[1/n,1]$ and every $c\in[0,1]$ there is an allocation regime in which the financial pillar exists, $H_{\pF}=h$, and $Q_{\pF}=c$, and the financial term $u_{\pF}=H_{\pF}(1-Q_{\pF})$ takes every value in $[0,1]$.
   273	\end{proposition}
   274	
   275	\begin{proof}
   276	For $a\in[1/n,1]$ let $s(a)$ give share $a$ to one actor and $(1-a)/(n-1)$ to each of the others. Then $H(s(a))=a^2+(1-a)^2/(n-1)$, which is continuous in $a$, equals $1/n$ at $a=1/n$, and equals $1$ at $a=1$. By the intermediate value theorem every $h\in[1/n,1]$ is attained. Contestability is scored from features (disclosure, audit, entry, appeal) that the share vector does not determine, so any $c\in[0,1]$ can be paired with any $h$; existence of the pillar requires only that some settlement procedure operate, which it does under any share vector. Finally $u_{\pF}=h(1-c)$ equals $0$ at $c=1$ and equals $h$ at $c=0$, so taking $h=1$ and letting $c$ range over $[0,1]$ attains every value in $[0,1]$.
   277	\end{proof}
   278	
   279	The proposition is elementary, and its role is to block a common inference. That every polity has someone who controls resources is a structural fact. That some polity's resource control is concentrated and unaccountable is an empirical claim about $H_{\pF}$, $Q_{\pF}$, and the couplings $C_{\pF n}$, which requires evidence of the kind \citet{largo2026hbs} specifies for capture links. The rest of this paper is about that evidence.
   280	
   281	\section{Literature on financial power}
   282	\label{sec:literature}
   283	
   284	Research on resource command and political power has developed along four lines that rarely meet. Each supplies a mechanism the financial pillar needs, and each has a rival literature that limits it.
   285	
   286	The economic theory of regulation asks how resource holders shape the rules that govern them. Stigler's theory of economic regulation treats regulation as a good demanded by industries and supplied by the state, so that regulatory agencies tend to serve the regulated \citep{stigler1971}. Peltzman generalized the model: a regulator balances producer and consumer pressure, so outcomes fall between pure capture and pure public interest \citep{peltzman1976}. Becker showed that competition among pressure groups limits the transfers any one group can extract, because deadweight losses grow with the size of the transfer and mobilize the losers \citep{becker1983}. Laffont and Tirole recast capture as a principal-supervisor-agent problem in which the danger of collusion between the supervisor and the regulated firm shapes the optimal design of incentives \citep{laffont1991}. Grossman and Helpman modeled trade protection as the outcome of contribution schedules offered to an incumbent government \citep{grossman1994}. Dal B\'o surveys the theory and evidence \citep{dalbo2006}, and Carpenter and Moss insist on a demanding definition: capture requires showing that regulation was directed away from the public interest and toward the regulated industry by the industry's own intent and action, not merely that the industry benefited \citep{carpentermoss2014}. That standard is the same one the capture link of \citet{largo2026hbs} encodes.
   287	
   288	Rent-seeking theory measures the costs of the contest itself. Tullock observed that resources spent to obtain or defend monopolies and tariffs are a social cost beyond the usual deadweight triangle \citep{tullock1967}; Krueger named the activity rent seeking and estimated its scale in licensing regimes \citep{krueger1974}; Posner argued that competition for rents can dissipate them entirely \citep{posner1975}. Olson supplied the organizational asymmetry that makes such contests one-sided: small groups with concentrated stakes organize more readily than large groups with diffuse ones \citep{olson1965}. These works explain why concentrated resource control tends to seek conversion into rule-making power. They do not show that the conversion succeeds, and direct studies of influence suggest that it often does not.
   289	
   290	Those studies concern democracies, and they divide sharply. Lindblom argued that business holds a privileged position because governments depend on private investment for the prosperity on which they are judged \citep{lindblom1977}. Przeworski stated the same dependence as a dilemma for electoral socialism: a party that threatens profits risks the investment its program needs \citep{przeworski1985}. Mills described an interlocking economic, political, and military elite in the postwar United States \citep{mills1956}, and Winters defines oligarchy by the political work of wealth defense, which he traces from Athens and Rome to the modern United States \citep{winters2011}. Against these accounts, Ansolabehere, de Figueiredo, and Snyder find that campaign money in the United States is small relative to the value of government policy and behaves more like consumption than investment \citep{ansolabehere2003}, and Baumgartner and colleagues find, in a large sample of issues, that the side with more resources often fails to win \citep{baumgartner2009}. Mizruchi documents the fragmentation of the American corporate elite after the 1970s, which cuts against claims of a unified business class \citep{mizruchi2013}. Gilens and Page's finding that economic elites and organized business interests have substantial independent influence on policy while average citizens have little \citep{gilens2014} is disputed by Branham, Soroka, and Wlezien, who show that the preferences of the affluent and the middle class differ on relatively few issues and that the affluent win only modestly more often when they do differ \citep{branham2017}. Culpepper offers a reconciliation: business power is strongest in quiet politics, on technical issues of low public salience \citep{culpepper2010}.
   291	
   292	Political economists of the state study the relation between rulers and the resources they command. Kornai's soft budget constraint describes a paternalistic state that rescues loss-making enterprises, so that the enterprises' expectations of rescue erode the discipline of the budget \citep{kornai1986,kornai1992}. North, Wallis, and Weingast describe limited-access orders in which the dominant coalition creates rents for its members and so binds them to keep the peace, and open-access orders in which entry into economic and political organization is impersonal \citep{nww2009}. The rentier-state literature, originating with Mahdavy's study of Iran and developed by Beblawi and Luciani, holds that states living on external rents need not bargain with taxpayers \citep{mahdavy1970,beblawiluciani1987}; Ross tests the claim cross-nationally \citep{ross2001,ross2012}, and Haber and Menaldo find that the association between resource wealth and authoritarianism does not survive within-country analysis over long time series \citep{habermenaldo2011}. Levi models rulers as revenue maximizers constrained by their bargaining power, transaction costs, and discount rates, and argues that compliance is quasi-voluntary when taxpayers believe others also pay and the ruler keeps its bargains \citep{levi1988}. Tilly traces European state formation along capital-intensive and coercion-intensive paths, in which rulers obtained the means of war either from merchants and cities or by direct extraction from the land \citep{tilly1990}. This paper owns the financing side of that fiscal-military account; Part V treats its coercive side \citep{long2026coercive}.
   293	
   294	Two normative and sociological works connect these lines to the cross-pillar question. Walzer defines tyranny as the conversion of dominance in one sphere of distribution into dominance in another, as when wealth buys office or office buys wealth \citep{walzer1983}. Bourdieu treats economic, cultural, social, and symbolic capital as convertible into one another at rates that are themselves objects of struggle \citep{bourdieu1989}. Both supply a vocabulary for what the multiplex model measures with the couplings $C_{\pF n}$: the degree to which control of resources carries control of rules, rulings, beliefs, sanctions, and work. Mann's model of ideological, economic, military, and political networks of power is the nearest precedent for a pluralist decomposition of social power \citep{mann1986}; Part IV presents it in full and compares it with the six-pillar scheme \citep[Section 4]{long2026ideological}.
   295	
   296	The capture literature tests resource-to-rule conversion mostly in one regime type, the market democracy, and the literatures on party-states, rentier states, and early modern fiscal states each describe resource command within one regime family. None places the universal allocation function, its necessity, and its regime-specific distribution in a single frame with common measures. That frame is what the six-pillar model provides, and the comparison below applies it.
   297	
   298	\section{Comparative analysis across six regime types}
   299	\label{sec:comparative}
   300	
   301	The six regime types of the series span two institutional dimensions rather than six exclusive categories. Market capitalism and social democracy describe how an economy organizes ownership, bargaining, and allocation; secular democracy describes how a constitution separates, delegates, and reviews authority over resources. Communist party-states, Islamic states, and the Catholic monarchies of early modern Europe combine a position on each dimension with a distinctive source of legitimacy. A single polity can therefore be coded on both dimensions, and most contemporary market-capitalist and social-democratic polities are also secular democracies. Each subsection below examines which institutions hold the financial pillar, how concentrated and contestable control is, how the pillar is coupled to the other five, what preserves accountability, and which capture episodes and checks are documented.
   302	
   303	No polity has yet been coded under a preregistered protocol, so no numerical value of $H_{\pF}$, $Q_{\pF}$, $U_t$, or $\Integ_t$ is reported for any real case. Statements that a value is high or low are hypotheses about what such coding would find.
   304	
   305	\subsection{Market-capitalist societies}
   306	
   307	In market-capitalist societies the financial pillar is held mainly by private owners of capital, by banks and other financial intermediaries, by corporations, and by institutional investors, with a central bank controlling the supply of money and a state controlling a public budget. The dominant settlement mode is property and exchange, supplemented by command allocation through taxation and public spending. Control shares within subdomains can be highly concentrated: Piketty documents long periods in which the return on capital exceeded the growth rate and wealth concentration rose \citep{piketty2014}. Aggregate concentration across all actors is lower than within subdomains, which is the aggregation gap of \cref{prop:financial-power:aggregation-gap} at work.
   308	
   309	The characteristic coupling is $C_{\pF\pP}$, the conversion of resources into influence over rule-making, which \citet{largo2026hbs} calls the wealth-to-rules pathway. Evidence that the pathway operates is substantial. Igan, Mishra, and Tressel find that lenders who lobbied more intensively before the 2008 crisis made riskier loans and performed worse in the crisis \citep{igan2012}. Mian, Sufi, and Trebbi find that campaign contributions from the financial industry predicted congressional votes on the major housing and financial legislation of 2008, alongside constituents' mortgage distress \citep{mian2010}. Kalla and Broockman show experimentally that disclosing a constituent's status as a donor increased access to senior congressional officials \citep{kalla2016}. Bertrand, Bombardini, and Trebbi, and Blanes i Vidal, Draca, and Fons-Rosen, show that lobbyists' value depends heavily on their personal connections to officeholders, a revolving-door effect \citep{bertrand2014,blanes2012}. Faccio finds politically connected firms in many countries, more often where corruption is higher \citep{faccio2006}. Hacker and Pierson attribute the rise of top incomes in the United States to organized political combat over taxation and regulation \citep{hackerpierson2010}, and Bartels finds senators more responsive to affluent constituents \citep{bartels2008}.
   310	
   311	The counter-evidence is as substantial. Access is not outcome: Hall and Deardorff model lobbying as a subsidy of information and labor to legislators who already agree with the lobbyist \citep{hall2006}, which implies influence over agenda and detail more than over direction. The findings of Ansolabehere and colleagues, of Baumgartner and colleagues, and of Branham, Soroka, and Wlezien cited in \cref{sec:literature} show that money is small relative to stakes, that resource advantages often lose, and that the rich win mainly when their preferences coincide with those of the middle class. Mizruchi's account of elite fragmentation suggests that $\Integ_t$ for the American business community has declined rather than risen \citep{mizruchi2013}.
   312	
   313	Accountability in this regime type rests on open entry, antitrust law, disclosure of contributions and lobbying, competitive procurement, judicial review of regulation, a free press, and elections. Contestability is therefore high on paper, and the open empirical question is how much of it binds in quiet, technical domains, where Culpepper finds business power strongest \citep{culpepper2010}. Capture and its checks are both documented. The best documented capture episode in the sources reviewed is pre-crisis financial regulation, where both the lobbying evidence and the outcome evidence point in the same direction. The best documented checks are the frequent defeats of well-funded interests and the electoral reversals of policy that the pluralist literature records.
   314	
   315	The couplings $C_{\pF\pI}$, through sponsorship of research and ownership of media, and $C_{\pF\pJ}$, through the resources that let repeat players litigate, are plausible but less systematically measured. Part III analyzes the contest between repeat players and occasional litigants (Proposition 4.3 of \citealt{long2026judicial}), and Part IV shows that endorsements from captured authorities carry no information (Proposition 2.9 of \citealt{long2026ideological}).
   316	
   317	\subsection{Communist party-states}
   318	
   319	In the communist party-state the financial pillar is held by planners and ministries, by state banks, and by managers of state enterprises appointed through the party's personnel system. The dominant settlement mode is command allocation, with property and exchange confined to permitted margins. Formal concentration is extreme, since the state owns the principal means of production and the party controls appointments to the posts that allocate them. Kornai's account of the classical socialist system makes the party's monopoly of power the defining feature from which the economic features follow \citep{kornai1992}. In the terms of \citet{largo2026hbs}, the control path runs from appointment to allocation rather than from wealth to rules, and the coupling $C_{\pP\pF}$ is near its maximum by design. Part II owns the appointment channel (Definition 2.8 of \citealt{long2026political}); here we record its financial consequences.
   320	
   321	Formal concentration overstates effective concentration. Gregory's study of the Soviet archives shows that the top leadership could not allocate everything and bargained constantly with ministries and enterprises that held better information about their own capacities \citep{gregory2004}. Berliner's interviews with former Soviet managers documented the informal procurement agents who obtained scarce inputs outside the plan, and the networks of favors through which managers met targets \citep{berliner1957}; Ledeneva reconstructed the economy of favors, known as blat, that ran alongside the formal allocation of goods in the late Soviet period \citep{ledeneva1998}. These informal channels lowered effective concentration while also lowering contestability, since favors were by nature unrecorded and unreviewable. Kornai's soft budget constraint completes the picture: enterprises expected rescue from their administrative superiors, so loss did not lead to exit, and the allocation of credit followed bargaining power rather than performance \citep{kornai1986}.
   322	
   323	The reform-era People's Republic of China shows that the regime type admits wide variation. A large private sector emerged and came to produce much of output and employment \citep{lardy2014,naughton2007}. The banking system nevertheless remained dominated by state-owned banks whose senior executives are appointed through the party's personnel system, and Walter and Howie describe the resulting financial structure as serving party priorities \citep{walterhowie2011}. Allen, Qian, and Qian observe that China grew rapidly despite a formal legal and financial system weaker than standard theory would predict, and attribute much of the growth to firms financed through informal and alternative channels \citep{allen2005}. Milhaupt and Zheng argue that ownership is a poor guide to control, because large private firms are also tied to the party-state through their founders' political memberships and their dependence on state support \citep{milhaupt2015}. Cross-nationally, La Porta, L\'opez-de-Silanes, and Shleifer associate government ownership of banks with slower subsequent financial development \citep{laporta2002}, and Shleifer and Vishny model politicians' use of state firms to deliver employment and patronage \citep{shleifer1994}.
   324	
   325	Accountability in the classical system ran through the party's own control organs, so contestability against the party itself was low. Documented capture episodes include the bargaining and soft budgets that Kornai describes, which transferred resources to enterprises and officials with bargaining power. The transition from communism produced the clearest cases of reciprocal capture in the comparative record. Hellman found that early winners from partial reform blocked further reform that would have dissipated their rents \citep{hellman1998}; Hellman, Jones, and Kaufmann defined state capture as firms shaping the basic rules of the game through private payments to officials \citep{hellman2000}; Black, Kraakman, and Tarassova describe insider privatization in Russia \citep{black2000}; and Guriev and Rachinsky document the concentration of Russian industrial ownership among a small number of owners \citep{guriev2005}. Treisman argues that the conventional account of the loans-for-shares auctions overstates their role in that concentration \citep{treisman2010}, a reminder that even the canonical episode is contested. The documented checks within the regime type are the hard budget constraints that reform introduced in some sectors and the competition from non-state firms that limited the rents of state incumbents.
   326	
   327	\subsection{Social democracy and market socialism}
   328	
   329	In social democracies the financial pillar is mixed. Private capital owns most productive assets, but high taxation, a large public budget, public pension funds, and corporatist bargaining among employers, unions, and the state give organized labor and the state substantial shares of decision-relevant control. Korpi's power-resources theory explains the configuration as the product of labor's organizational strength, which allowed it to win through democratic politics what it could not win through ownership \citep{korpi1983}. Esping-Andersen traces how social democratic parties used state power to reduce workers' dependence on the market \citep{esping1985}, and Berman locates the movement's origin in a commitment to the primacy of politics over markets \citep{berman2006}. Hall and Soskice classify the economies that developed from these settlements as coordinated market economies, in which firms solve problems of training, finance, and wage setting through non-market institutions \citep{hallsoskice2001}.
   330	
   331	Social democracy combined high taxation with remarkably concentrated private ownership. H\"ogfeldt shows that Swedish corporate control was held through pyramids and dual-class shares by a few families and foundations, of which the Wallenberg sphere was the largest, and argues that social democratic governments tolerated this concentration as a stable partner for investment and employment \citep{hogfeldt2005}. Subdomain concentration in the ownership of large firms was therefore high, while the public budget, pensions, and wage setting were held by other actors. That is the separated configuration of \cref{ex:aggregation}, with a large aggregation gap.
   332	
   333	The most direct attempt to change who held the financial pillar was the Swedish proposal for wage-earner funds, which would have transferred a growing share of corporate equity to funds controlled by the labor movement. Pontusson's account shows how employers mobilized against the proposal, how the enacted version was diluted, and how the episode revealed the limits of social democratic power over investment \citep{pontusson1992}. Przeworski's dilemma predicts exactly this limit: a democratic government that threatens the returns to capital faces the possibility that investment falls \citep{przeworski1985}. Streeck argues that later decades shifted power from citizens to creditors as states financed themselves through debt \citep{streeck2014}.
   334	
   335	The couplings characteristic of this type are $C_{\pF\pW}$ and $C_{\pF\pP}$, but they take a bargained rather than a captured form: organized capital and organized labor both hold seats in the arenas where wages, pensions, and investment rules are set. Accountability rests on electoral competition, on the countervailing power of unions, and on transparency norms. Scheve and Stasavage show that the high progressive taxation of the twentieth century followed mass mobilization for war and arguments for fair compensation rather than democracy as such \citep{scheve2016}. We found fewer documented capture episodes for this type in the sources reviewed (cutoff October 2026). The main candidate is the entrenchment of concentrated family control that H\"ogfeldt describes, which social democratic governments accepted in exchange for investment \citep{hogfeldt2005}. The documented check is that labor's organized power repeatedly reversed advantages that capital held, which is one of the four findings that \citet{largo2026hbs} lists as undermining a strong capture thesis.
   336	
   337	\subsection{Islamic states}
   338	
   339	Islamic states are polities whose rulers derived legitimacy in substantial part from religious law, and they differ widely among themselves: the early caliphates, the Ottoman Empire, the Safavid and later Iranian states, and modern Saudi Arabia and the Islamic Republic of Iran organized resource command in very different ways. Islam here is a source of political legitimacy in specific historical states, not an essence that determines their economic institutions.
   340	
   341	Classical Islamic law supplied several settlement modes at once. The treasury, the bayt al-m\=al, held public revenues under the ruler's control. The obligatory alms tax, zak\=at, assigned a share of certain kinds of wealth to specified categories of recipients. The waqf, a perpetual endowment, dedicated the yield of an asset to purposes fixed by its founder under a trustee, and the qadi courts supervised its administration. Partnership forms, especially the commenda contract known as qir\=ad or mu\d{d}\=araba, organized long-distance trade \citep{udovitch1970,cizakca1996}. Singer describes how endowments financed mosques, schools, hospitals, and public kitchens across Ottoman and wider Islamic societies \citep{singer2008}. Kuran argues that the waqf provided public goods while protecting wealth from expropriation by rulers, and that its rigidity, together with features of Islamic partnership and inheritance law, limited the development of durable commercial organizations \citep{kuran2001,kuran2004,kuran2011}. The thesis is contested. Rubin attributes the divergence between Western Europe and the Middle East less to the content of Islamic law than to the role of religious authorities in legitimating rulers \citep{rubin2017}, and Kuru locates the cause in an alliance between the ulama and the state that took shape in the eleventh century \citep{kuru2019}. These accounts disagree about causes; they agree that the distribution of the financial pillar among rulers, jurists, endowments, and merchants shaped later development.
   342	
   343	The Ottoman Empire illustrates a fiscal regime built on command allocation and credit. Karaman and Pamuk show that Ottoman central revenues per capita fell behind those of the leading European states in the seventeenth and eighteenth centuries and that the state relied increasingly on tax farming, including life-term tax farms, which converted future revenues into present credit from local and provincial elites \citep{karaman2010}. In a comparative study they relate the different paths of European and Ottoman fiscal development to the interaction of warfare, economic structure, and political regime \citep{karaman2013}. Pamuk's monetary history records the use of debasement as a revenue source in fiscal crises \citep{pamuk2000}. Tax farming dispersed the collection of revenue among many holders, lowering $H_{\pF}$, while coupling it tightly to local political and coercive power.
   344	
   345	Modern Islamic states are mostly rentier states, and their allocation regimes are shaped by oil more than by religious law. Hertog describes the Saudi state as a set of fiefdoms and brokerage networks built around royal patrons, alongside islands of efficient bureaucracy such as the national oil company \citep{hertog2010}. Chaudhry contrasts the institutional erosion that oil wealth produced in Saudi Arabia with the different path of labor-exporting Yemen \citep{chaudhry1997}, and Vitalis reconstructs the corporate and political entanglements of the American oil company in the early Saudi state \citep{vitalis2007}. In the Islamic Republic of Iran, revolutionary foundations known as bonyads control large economic assets outside the ordinary budget, and the Revolutionary Guards developed substantial business interests, including construction and engineering firms \citep{maloney2015,wehrey2009}. That fusion of financial and coercive control is the coupling $C_{\pF\pC}$ in its most direct form; Part V treats the coercive side. El-Gamal argues that much of modern Islamic finance replicates conventional instruments in legally permissible form, so that its religious label says little about how control is distributed \citep{elgamal2006}.
   346	
   347	Accountability varied with the type of state. Qadi supervision of endowments, the jurists' claim to interpret the law independently of rulers, and the commercial courts all provided checks in classical and Ottoman settings, although Kuran records that rulers did at times confiscate endowments \citep{kuran2001}. In modern rentier states the rentier argument predicts weak fiscal bargaining because the state does not depend on taxpayers \citep{beblawiluciani1987,ross2001}, but the within-country evidence of Haber and Menaldo cautions against treating oil as a sufficient cause \citep{habermenaldo2011}. Documented capture episodes include the off-budget concentration of assets in Iran's foundations and security forces; documented checks include the juristic independence that endowment supervision required and the variation across Islamic polities that rules out any single Islamic allocation regime.
   348	
   349	\subsection{Catholic monarchies of early modern Europe}
   350	
   351	In the Catholic monarchies of early modern Europe, royal authority was intertwined with the Church, and the financial pillar was distributed among the crown's fiscal apparatus, private bankers who lent to the crown, the Church with its lands and tithes, and officeholders who had bought their posts. Habsburg Spain, Bourbon France, and the Papal States organized these elements differently, and Gallican and ultramontane traditions disagreed about the Church's relation to royal finance. Catholicism here, like Islam in the preceding subsection, is a source of political legitimacy in specific states, not a determinant of their institutions.
   352	
   353	Habsburg Spain under Philip II is the best studied case of sovereign credit in the period. The crown borrowed heavily from Genoese and other bankers through short-term contracts called asientos and long-term bonds called juros, and it suspended payments on several occasions. Drelichman and Voth show that lending nevertheless continued, that the bankers earned positive returns overall, and that the payment stops are better read as excusable defaults in bad fiscal states, followed by negotiated settlements, than as predation \citep{drelichman2011,drelichman2014}. Conklin models the relationship as a repeated game in which the bankers' capacity to act together disciplined the crown \citep{conklin1998}. The coupling $C_{\pF\pC}$ was strong, since the debt financed war, while $C_{\pF\pP}$ ran through the Cortes of Castile, whose consent was needed for important taxes and which therefore constrained the crown's capacity to pledge revenue. \Cref{prop:financial-power:sovereign-credit} in \cref{sec:mechanisms} gives the formal condition.
   354	
   355	Bourbon France combined a royal fiscal system with extensive sale of offices and tax farming. Doyle describes venality as the sale of offices that became the heritable property of their holders, so that judges and financial officials owned their posts \citep{doyle1996}. Kwass shows how privilege sorted subjects for taxation and how new direct taxes provoked eighteenth-century disputes over liberty and equality \citep{kwass2000}. Velde and Weir analyze the crown's borrowing through life annuities and other instruments before 1789 \citep{velde1992}, and Hoffman, Postel-Vinay, and Rosenthal reconstruct a large private credit market organized by Parisian notaries \citep{hoffman2000}. The essays collected by Hoffman and Norberg compare how fiscal crises interacted with representative institutions across European states \citep{hoffmannorberg1994}. Venality made the financial pillar less concentrated and less contestable at once: offices were dispersed across many holders, but holders could not be removed except by reimbursement, and the coupling between $\pF$ and $\pJ$ was direct because judicial offices were purchased.
   356	
   357	The Papal States and the finances of the papacy give the case of fusion between financial and spiritual authority. Prodi describes the pope as both head of the Church and territorial prince, with a fiscal and administrative apparatus that anticipated features of other early modern states \citep{prodi1987}. De Roover's history of the Medici bank documents its role as depository of the papal Camera \citep{deroover1963}, and Padgett and Ansell show how the Medici built power in Florence through overlapping networks of marriage, business, and patronage \citep{padgett1993}, which is a historical multiplex in exactly the sense of \citet{largo2026hbs}. Ekelund and colleagues interpret the medieval Church as an economic firm that sought rents \citep{ekelund1996}; the interpretation is contested, and we cite it as one reading of the evidence rather than as an established result.
   358	
   359	Accountability in these monarchies rested on representative bodies such as the Cortes and the Parlements, on the repeated-game discipline that lenders imposed, on ecclesiastical immunities that sometimes protected Church wealth from the crown and sometimes protected the crown's allies, and on conflict between crown and Church. Documented capture episodes include the conversion of financial office into judicial office through venality. Documented checks include the Cortes' control over new taxes in Castile and the bankers' capacity to withhold further credit.
   360	
   361	\subsection{Secular democracies}
   362	
   363	Secular democracies distribute authority among elected officials, courts, independent agencies, and private institutions, and justify it without reference to religious law. The financial pillar in such polities includes private holders, as in the first and third types, together with public institutions designed to be insulated from the elected government: an independent central bank, a supreme audit institution, competition authorities, and procurement and disclosure regimes. The distinctive feature of the type is constitutional: it separates the holders of different financial subdomains and places some of them beyond the direct reach of elected officials.
   364	
   365	Central bank independence is the clearest example of delegated financial authority. Alesina and Summers found that more independent central banks were associated with lower and more stable inflation, without a corresponding cost in real growth \citep{alesina1993}. Goodhart traces the evolution of central banks from government bankers to institutions charged with monetary stability and the supervision of banks \citep{goodhart1988}. Delegation raises contestability against elected officials, who can no longer finance spending by printing money, but it concentrates control of the monetary subdomain in a small technocratic body. Whether delegation reduces unaccountable concentration or relocates it is therefore an empirical question about the review that independent agencies themselves face, through legislative oversight, published reasoning, and judicial review.
   366	
   367	Secular democracies also build disclosure and review into the coupling $C_{\pF\pP}$. Lobbying registers, contribution limits, beneficial-ownership registers, and competitive procurement aim to make the wealth-to-rules pathway visible and contestable; \citet{largo2026hbs} lists them among redesign measures. The revolving-door evidence cited above shows that personal connections still carry value \citep{blanes2012,bertrand2014}, and Carpenter and Moss collect designs intended to prevent capture, including procedural requirements, external review, and the deliberate building of countervailing expertise \citep{carpentermoss2014}. Rajan and Zingales show that financial development in many countries reversed between the early twentieth century and the postwar decades, and argue that incumbent firms and financiers oppose financial development when it would admit competitors \citep{rajan2003}. Their result implies that constitutional separation does not by itself prevent incumbents from using political influence to close entry.
   368	
   369	Accountability in this type is the highest on paper, because the review of financial decisions is spread across courts, legislatures, auditors, and the press. The documented capture episodes are those of the first type, since most secular democracies are also market economies, and their characteristic form is quiet influence on technical rules. The documented checks are the binding constraints that independent agencies, courts, and elections impose, including judicial invalidation of regulations and the electoral replacement of governments that have favored concentrated interests. Scheve and Stasavage show that democracies do not automatically tax the rich more heavily \citep{scheve2016}, which is a reminder that constitutional design shapes the distribution of financial control without determining it.
   370	
   371	\subsection{Summary of the comparison}
   372	
   373	\Cref{tab:regimes} collects the comparison. Every row has a financial pillar, which is the necessity claim; the rows differ in who holds it, how it is coupled, and what checks it, which is where the contingent capture claim must be tested.
   374	
   375	\begin{table}[t]
   376	\centering
   377	\small
   378	\caption{The financial pillar across the six regime types. Coupling entries are hypotheses about which pairs a preregistered coding would find strongest, not measured values.}
   379	\label{tab:regimes}
   380	\begin{tabularx}{\linewidth}{@{}L{2.2cm}YL{2.1cm}Y@{}}
   381	\toprule
   382	Regime type & Typical holders of control & Strongest couplings & Main sources of accountability \\
   383	\midrule
   384	Market capitalism & Private owners, banks, corporations, and a central bank & $C_{\pF\pP}$, $C_{\pF\pI}$, $C_{\pF\pJ}$ & Open entry, antitrust, disclosure, courts, and elections \\
   385	Communist party-state & Planners, state banks, and managers appointed by the party & $C_{\pP\pF}$ and $C_{\pF\pC}$ & Mainly the party's own control organs, with informal bargaining \\
   386	Social democracy & Private owners alongside unions, public funds, and the state budget & $C_{\pF\pW}$ and $C_{\pF\pP}$ & Elections, organized labor, and transparency norms \\
   387	Islamic states & Treasuries, endowment trustees, merchants, tax farmers, and rentier states & $C_{\pF\pC}$ and $C_{\pF\pI}$ & Qadi supervision and juristic independence, varying widely by state \\
   388	Catholic monarchies & The crown, its bankers, the Church, and owners of venal offices & $C_{\pF\pC}$ and $C_{\pF\pJ}$ & Representative assemblies, lenders' discipline, and Church-crown conflict \\
   389	Secular democracies & Private holders with independent central banks, auditors, and regulators & $C_{\pF\pP}$ in quiet, technical domains & Delegated review, courts, legislatures, and the press \\
   390	\bottomrule
   391	\end{tabularx}
   392	\end{table}
   393	
   394	Three results of the comparison bear on the series' thesis. The financial pillar is present in every type and in every case examined, held by institutions that have almost nothing else in common. The control path differs by regime as \citet{largo2026hbs} predicts: wealth to rules in market societies, appointment to allocation in party-states, bargaining between organized interests in social democracies, ruler to rent in rentier states, and lender to ruler in early modern fiscal states. And every type has both documented capture episodes and documented checks, so the type alone does not settle whether a polity's financial pillar is captured. That question requires coding a particular polity in a particular period.
   395	
   396	\section{Mechanisms, failure modes and checks}
   397	\label{sec:mechanisms}
   398	
   399	Coordination in the financial pillar becomes capture when three conditions of the capture link hold together \citep{largo2026hbs}: an actor obtains privileged access or discretion over allocation, the privilege weakens the accountability or contestability that would otherwise apply, and material evidence ties the asymmetry to an output such as a rule, a credit decision, a contract, or an exemption. Large holdings, profitable lending, and political donations are not capture by themselves.
   400	
   401	\subsection{Conversion of resources into influence}
   402	
   403	The central mechanism is conversion: the use of control in the financial pillar to obtain favorable outputs in another pillar. Walzer's tyranny and Bourdieu's convertibility of capital name the same phenomenon \citep{walzer1983,bourdieu1989}.
   404	
   405	\begin{definition}[Conversion elasticity]
   406	\label{def:financial-power:conversion}
   407	Let $y^{n}_i$ be a measure of outputs of pillar $n\neq\pF$ that favor actor $i$: rules adopted, rulings won, coverage obtained, sanctions avoided, or labor terms secured. The \emph{conversion elasticity} from the financial pillar to pillar $n$ is
   408	\[
   409	\varepsilon_{\pF\to n}=\frac{\partial\ln\E[y^{n}_i\mid s^{\pF}_i,X_i]}{\partial\ln s^{\pF}_i},
   410	\]
   411	where $X_i$ collects the controls under which the comparison is made, including the actor's preferences and the public salience of the issue. The elasticity is defined where $s^{\pF}_i>0$, the conditional expectation is positive, and it is differentiable in $s^{\pF}_i$.
   412	\end{definition}
   413	
   414	Conversion elasticity and the coupling $C_{\pF n}$ measure different things. The coupling records whether one coalition commands appointments, budgets, sanctions, or agenda in both pillars \citep{largo2026hbs}; the elasticity records whether resource shares buy favorable outputs from actors who may be entirely independent. A wealthy firm lobbying an independent legislature produces positive $\varepsilon_{\pF\to\pP}$ with $C_{\pF\pP}$ near zero. A party-state in which appointment determines credit has high $C_{\pP\pF}$, but the relevant elasticity runs the other way, from appointment rank to allocation, which is the object of hypothesis HF2 in \cref{sec:measurement}. Which direction dominates is the regime-specific control path of \citet{largo2026hbs}.
   415	
   416	A deliberately simple decision model gives conditions under which a resource holder invests in conversion.
   417	
   418	\begin{proposition}[Influence investment]
   419	\label{prop:financial-power:influence}
   420	An actor with financial share $s\in(0,1]$ faces a rule whose adoption is worth $sV$ to it, where $V>0$ is the value of the rule to the whole resource base. By spending $e\geq 0$ the actor makes adoption occur with probability $\pi(e,Q)$, where $Q\in[0,1)$ is the contestability of the receiving pillar and $\pi$ is twice continuously differentiable on $[0,\infty)\times[0,1)$ with $\pi_e>0$, $\pi_{ee}<0$, and $\pi_{eQ}<0$. At $Q=1$ influence has no return and the actor spends nothing. The actor maximizes $sV\pi(e,Q)-e$. If the maximizer $e^*$ is interior, then
   421	\[
   422	\frac{\partial e^*}{\partial s}=-\frac{\pi_e}{s\,\pi_{ee}}>0,\qquad
   423	\frac{\partial e^*}{\partial V}=-\frac{\pi_e}{V\,\pi_{ee}}>0,\qquad
   424	\frac{\partial e^*}{\partial Q}=-\frac{\pi_{eQ}}{\pi_{ee}}<0.
   425	\]
   426	\end{proposition}
   427	
   428	\begin{proof}
   429	An interior maximizer satisfies the first-order condition $sV\pi_e(e^*,Q)=1$, and the second-order condition holds because $sV\pi_{ee}<0$. Write $\Phi(e,s,V,Q)=sV\pi_e(e,Q)-1$. Since $\partial\Phi/\partial e=sV\pi_{ee}\neq 0$, the implicit function theorem gives $e^*$ as a differentiable function of $(s,V,Q)$ near any interior solution, with $\partial e^*/\partial z=-(\partial\Phi/\partial z)/(\partial\Phi/\partial e)$ for each parameter $z$. Here $\partial\Phi/\partial s=V\pi_e$, $\partial\Phi/\partial V=s\pi_e$, and $\partial\Phi/\partial Q=sV\pi_{eQ}$. Substituting gives the three expressions. Their signs follow from $\pi_e>0$, $\pi_{ee}<0$, and $\pi_{eQ}<0$.
   430	\end{proof}

hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '391,530p' papers/latex/financial-power.tex | nl -ba -v391" in /Users/mlong/Documents/Development/the-beast-system
exec
/usr/local/bin/zsh -lc "sed -n '260,390p' papers/latex/financial-power.tex | nl -ba -v260" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   391	\end{tabularx}
   392	\end{table}
   393	
   394	Three results of the comparison bear on the series' thesis. The financial pillar is present in every type and in every case examined, held by institutions that have almost nothing else in common. The control path differs by regime as \citet{largo2026hbs} predicts: wealth to rules in market societies, appointment to allocation in party-states, bargaining between organized interests in social democracies, ruler to rent in rentier states, and lender to ruler in early modern fiscal states. And every type has both documented capture episodes and documented checks, so the type alone does not settle whether a polity's financial pillar is captured. That question requires coding a particular polity in a particular period.
   395	
   396	\section{Mechanisms, failure modes and checks}
   397	\label{sec:mechanisms}
   398	
   399	Coordination in the financial pillar becomes capture when three conditions of the capture link hold together \citep{largo2026hbs}: an actor obtains privileged access or discretion over allocation, the privilege weakens the accountability or contestability that would otherwise apply, and material evidence ties the asymmetry to an output such as a rule, a credit decision, a contract, or an exemption. Large holdings, profitable lending, and political donations are not capture by themselves.
   400	
   401	\subsection{Conversion of resources into influence}
   402	
   403	The central mechanism is conversion: the use of control in the financial pillar to obtain favorable outputs in another pillar. Walzer's tyranny and Bourdieu's convertibility of capital name the same phenomenon \citep{walzer1983,bourdieu1989}.
   404	
   405	\begin{definition}[Conversion elasticity]
   406	\label{def:financial-power:conversion}
   407	Let $y^{n}_i$ be a measure of outputs of pillar $n\neq\pF$ that favor actor $i$: rules adopted, rulings won, coverage obtained, sanctions avoided, or labor terms secured. The \emph{conversion elasticity} from the financial pillar to pillar $n$ is
   408	\[
   409	\varepsilon_{\pF\to n}=\frac{\partial\ln\E[y^{n}_i\mid s^{\pF}_i,X_i]}{\partial\ln s^{\pF}_i},
   410	\]
   411	where $X_i$ collects the controls under which the comparison is made, including the actor's preferences and the public salience of the issue. The elasticity is defined where $s^{\pF}_i>0$, the conditional expectation is positive, and it is differentiable in $s^{\pF}_i$.
   412	\end{definition}
   413	
   414	Conversion elasticity and the coupling $C_{\pF n}$ measure different things. The coupling records whether one coalition commands appointments, budgets, sanctions, or agenda in both pillars \citep{largo2026hbs}; the elasticity records whether resource shares buy favorable outputs from actors who may be entirely independent. A wealthy firm lobbying an independent legislature produces positive $\varepsilon_{\pF\to\pP}$ with $C_{\pF\pP}$ near zero. A party-state in which appointment determines credit has high $C_{\pP\pF}$, but the relevant elasticity runs the other way, from appointment rank to allocation, which is the object of hypothesis HF2 in \cref{sec:measurement}. Which direction dominates is the regime-specific control path of \citet{largo2026hbs}.
   415	
   416	A deliberately simple decision model gives conditions under which a resource holder invests in conversion.
   417	
   418	\begin{proposition}[Influence investment]
   419	\label{prop:financial-power:influence}
   420	An actor with financial share $s\in(0,1]$ faces a rule whose adoption is worth $sV$ to it, where $V>0$ is the value of the rule to the whole resource base. By spending $e\geq 0$ the actor makes adoption occur with probability $\pi(e,Q)$, where $Q\in[0,1)$ is the contestability of the receiving pillar and $\pi$ is twice continuously differentiable on $[0,\infty)\times[0,1)$ with $\pi_e>0$, $\pi_{ee}<0$, and $\pi_{eQ}<0$. At $Q=1$ influence has no return and the actor spends nothing. The actor maximizes $sV\pi(e,Q)-e$. If the maximizer $e^*$ is interior, then
   421	\[
   422	\frac{\partial e^*}{\partial s}=-\frac{\pi_e}{s\,\pi_{ee}}>0,\qquad
   423	\frac{\partial e^*}{\partial V}=-\frac{\pi_e}{V\,\pi_{ee}}>0,\qquad
   424	\frac{\partial e^*}{\partial Q}=-\frac{\pi_{eQ}}{\pi_{ee}}<0.
   425	\]
   426	\end{proposition}
   427	
   428	\begin{proof}
   429	An interior maximizer satisfies the first-order condition $sV\pi_e(e^*,Q)=1$, and the second-order condition holds because $sV\pi_{ee}<0$. Write $\Phi(e,s,V,Q)=sV\pi_e(e,Q)-1$. Since $\partial\Phi/\partial e=sV\pi_{ee}\neq 0$, the implicit function theorem gives $e^*$ as a differentiable function of $(s,V,Q)$ near any interior solution, with $\partial e^*/\partial z=-(\partial\Phi/\partial z)/(\partial\Phi/\partial e)$ for each parameter $z$. Here $\partial\Phi/\partial s=V\pi_e$, $\partial\Phi/\partial V=s\pi_e$, and $\partial\Phi/\partial Q=sV\pi_{eQ}$. Substituting gives the three expressions. Their signs follow from $\pi_e>0$, $\pi_{ee}<0$, and $\pi_{eQ}<0$.
   430	\end{proof}
   431	
   432	\begin{example}[A participation threshold]
   433	\label{ex:threshold}
   434	Let $\pi(e,Q)=(1-Q)(1-e^{-e})$, which satisfies the conditions of \cref{prop:financial-power:influence} for $Q<1$. The objective $sV(1-Q)(1-e^{-e})-e$ is concave in $e$ with derivative $sV(1-Q)e^{-e}-1$, so the optimum is $e^*=\ln\bigl(sV(1-Q)\bigr)$ when $sV(1-Q)>1$ and $e^*=0$ otherwise. Actors with shares below the threshold $\bar s=1/\bigl(V(1-Q)\bigr)$ do not invest at all. Take ten actors and $V=10$. At $Q=0.5$ and equal shares of $0.1$, every actor has $sV(1-Q)=0.5<1$ and total investment is zero. If one actor's share rises to $0.55$ and the other nine hold $0.05$ each, that actor invests $\ln 2.75\approx 1.01$ and the others still invest nothing. If contestability then rises to $Q=0.9$, the large holder's product falls to $0.55$ and its investment returns to zero.
   435	\end{example}
   436	
   437	The example states three things in miniature. Concentration activates conversion, because only holders above a threshold find influence worth buying; this is Olson's asymmetry between concentrated and diffuse interests \citep{olson1965}. Contestability shuts conversion off by lowering its marginal return, which is the financial form of the source's Proposition 2 that checks can interrupt transmission \citep{largo2026hbs}. And the threshold depends on the stake $V$, so conversion concentrates in domains where rules are worth much to few, which is consistent with Culpepper's finding that business power is strongest in quiet, technical politics \citep{culpepper2010}.
   438	
   439	The model has clear limits. It is a single-actor decision problem: other actors' spending does not enter $\pi$, so the competition among groups that Becker emphasizes, and the countermobilization that large transfers provoke, are absent \citep{becker1983}. The sign condition $\pi_{eQ}<0$ is an assumption about how contestability works, not a finding, and it would fail if contestability raised the value of expert lobbying by making the process more procedural. The proposition is therefore a conditional comparative static of the kind \citet{largo2026hbs} uses throughout, and its empirical counterpart is hypothesis HF1.
   440	
   441	\subsection{Credit and the discipline of lenders}
   442	
   443	Sovereign borrowing is the oldest form of coupling between private finance and political power. It can be read as capture, with lenders controlling the state, or as a bargain, with lenders disciplined by their need for repayment and the ruler by its need for future credit. A standard repeated-game condition separates the two readings.
   444	
   445	\begin{proposition}[Sovereign credit]
   446	\label{prop:financial-power:sovereign-credit}
   447	A ruler with discount factor $\delta\in(0,1)$ owes a payment $D>0$ in the current period. Continued access to credit yields a net surplus $g>0$ in every future period. Lenders act together, so that a default not excused by an agreed contingency ends all future lending. Then repayment is the ruler's best response if and only if
   448	\[
   449	D\leq\frac{\delta g}{1-\delta}.
   450	\]
   451	\end{proposition}
   452	
   453	\begin{proof}
   454	Repaying costs $D$ now and preserves the surplus stream, whose present value is $\sum_{t\geq 1}\delta^t g=\delta g/(1-\delta)$. Defaulting saves $D$ and ends the stream. Repayment is a best response exactly when $-D+\delta g/(1-\delta)\geq 0$.
   455	\end{proof}
   456	
   457	The condition explains how early modern lenders protected themselves without controlling legislation. Their security came from the ruler's need for future credit, measured by $g$, and from their own capacity to act together, which made exclusion credible. When a fiscal shock raised $D$ above the bound, a payment stop followed, and a negotiated settlement restored the relationship. Drelichman and Voth read the defaults of Philip II in this way, and Conklin attributes the discipline to the Genoese bankers' ability to coordinate \citep{drelichman2011,conklin1998}. If lenders cannot coordinate, because many small lenders compete to replace any lender who is excluded, the threat of exclusion weakens and the bound no longer protects them. The proposition thus identifies when lending is a bargain rather than capture: lenders receive repayment, not legal privileges unrelated to their loans. That is hypothesis HF3.
   458	
   459	North and Weingast argued that the constitutional settlement in seventeenth-century England improved the crown's capacity to borrow by making its commitments credible \citep{northweingast1989}. In the terms of the proposition, a representative assembly that controls taxation can raise the credibility of repayment by shifting authority over $D$ away from the ruler alone. The same logic connects the Cortes of Castile to the Habsburg debt.
   460	
   461	\subsection{Soft budgets, rents and fusion}
   462	
   463	Three further mechanisms move a financial pillar toward capture. The soft budget constraint arises whenever an allocating authority cannot commit to let loss-making units fail \citep{kornai1986}. Kornai developed the concept for socialist enterprises, where the paternalistic state rescued firms as a matter of course. The analogy with private banks considered too large to fail is plausible, but it extends the concept beyond the evidence that Kornai and \citet{largo2026hbs} cite, and we treat it as a hypothesis rather than a finding. Wherever it holds, rescue expectations transfer resources to units with bargaining power, and the transfer is unreviewable when the rescuing authority is not itself accountable.
   464	
   465	Rentier revenue changes the coupling between the financial pillar and the productive pillar. A state that lives on external rents does not depend on taxpayers and therefore need not bargain with them \citep{mahdavy1970,beblawiluciani1987}. Levi's account of quasi-voluntary compliance identifies what is lost: the reciprocal bargain in which rulers provide services and keep promises in exchange for compliance \citep{levi1988}. The rentier mechanism lowers $Q_{\pF}$ by weakening the fiscal voice of producers. Part VI derives the producers' side of the same mechanism (Proposition 6.6 of \citealt{long2026productive}); the allocation side belongs here. The evidence that the mechanism operates is mixed, as \cref{sec:literature} records.
   466	
   467	Fusion of the financial and coercive pillars in one organization is the most direct route to high $C_{\pF\pC}$. Part V shows that in large collectives sanctioners must be paid or provisioned, or else rewarded by belief (Proposition 3.5 of \citealt{long2026coercive}), which derives the dependency of coercion on resource allocation; fusion places both ends of that dependency in one organization. Business arms of security forces, whether the Revolutionary Guards' firms in Iran \citep{wehrey2009} or the military enterprise of early modern monarchies, give one organization both resources and the means of sanction. The rival explanation is public-goods provision: the same organizations build infrastructure and conduct reconstruction, and their size may reflect capacity rather than capture. Distinguishing the two requires evidence on procurement, competition, and review, not on size.
   468	
   469	\subsection{Checks}
   470	
   471	The checks that interrupt these mechanisms are specific. Open entry, enforced by antitrust and by competitive procurement, raises the number of actors who can contest a holder's position; Rajan and Zingales show that incumbents oppose it for that reason \citep{rajan2003}. A hard budget constraint, under which failing units actually exit, removes the rents of rescue. Disclosure of contributions, lobbying, and beneficial ownership makes the conversion pathway visible, which is a precondition of contesting it. Independent audit and independent central banking separate the review of financial decisions from those who make them, although independence relocates concentration into the reviewing body. And coordinated lenders, organized labor, and representative assemblies supply countervailing power from within the financial pillar itself. Each check raises $Q_{\pF}$ or lowers a coupling; none lowers the necessity of the pillar, which no check can or should remove.
   472	
   473	\section{Measurement and testable hypotheses}
   474	\label{sec:measurement}
   475	
   476	\subsection{Indicators}
   477	
   478	Measurement of the financial pillar should proceed subdomain by subdomain, as \cref{prop:financial-power:aggregation-gap} recommends, and should code contestability separately from concentration. \Cref{tab:indicators} lists indicators drawn from sources that already exist. Cross-national governance indicators, such as the Worldwide Governance Indicators and the V-Dem data, supply partial measures of contestability \citep{kaufmann2010,coppedge2011}; they do not measure control shares and should not be used as proxies for them.
   479	
   480	\begin{table}[t]
   481	\centering
   482	\small
   483	\caption{Indicators for the financial pillar. Concentration indicators enter $H_{\pF}$ by subdomain; contestability indicators enter $Q_{\pF}$.}
   484	\label{tab:indicators}
   485	\begin{tabularx}{\linewidth}{@{}L{2.6cm}YY@{}}
   486	\toprule
   487	Construct & Indicators & Main pitfall \\
   488	\midrule
   489	Ownership concentration & Asset shares, ownership pyramids, and dual-class control & Ownership understates control where party or family ties matter \\
   490	Credit concentration & Bank credit shares by lender and by borrower & State and private banks may follow different rules \\
   491	Budget discretion & Share of spending allocated without formula or tender & Discretion can serve legitimate emergencies \\
   492	Procurement & Concentration of awards by recipient, and the share awarded without competition & Specialized markets have few qualified suppliers \\
   493	Contestability & Entry barriers, audit independence, bankruptcy enforcement, and disclosure regimes & Laws on paper may not bind in practice \\
   494	Conversion & Connected-firm returns, connected lending, and lobbying linked to outcomes & Large firms become connected because they are large \\
   495	\bottomrule
   496	\end{tabularx}
   497	\end{table}
   498	
   499	The capture-link coding of \citet{largo2026hbs} supplies the unit of evidence. A coded link records the actor, the mechanism, the evidence of privileged access, the review that applied, the decision, and the material effect, together with counterevidence. The population of coded events should include all decisions in a preregistered sector, not only scandals, since a sample of scandals selects on the outcome.
   500	
   501	\subsection{Hypotheses}
   502	
   503	\Cref{tab:hypotheses} states seven hypotheses specific to the financial pillar, each refining one of the source hypotheses H1 to H6 and each with a stated falsifier.
   504	
   505	\begin{table}[t]
   506	\centering
   507	\small
   508	\caption{Hypotheses for the financial pillar, each paired with an observation that would falsify it.}
   509	\label{tab:hypotheses}
   510	\begin{tabularx}{\linewidth}{@{}L{1.1cm}YY@{}}
   511	\toprule
   512	Label & Hypothesis & Falsifier \\
   513	\midrule
   514	HF1 & The conversion elasticity $\varepsilon_{\pF\to\pP}$ is higher on technical issues of low salience than on salient ones & Equal or higher elasticity on salient issues, or no elasticity once preferences shared across income groups are controlled \\
   515	HF2 & In party-state command sectors, the appointment rank of an enterprise head predicts credit and inputs after controlling for profitability and plan targets & Profitability predicts allocation better than rank \\
   516	HF3 & Where a ruler needs repeated credit, lenders secure repayment without obtaining legal privileges unrelated to their loans & Lenders obtain legal advantages that do not secure repayment \\
   517	HF4 & Liberalizing entry reduces the rents of connected incumbents & Rents of connected firms persist after entry reform \\
   518	HF5 & A higher share of non-tax revenue lowers fiscal bargaining with taxpayers and raises discretionary allocation & A null effect in within-country panels \\
   519	HF6 & Where one organization holds financial and coercive control, financial contestability falls & Fused organizations face the same procurement competition and audit as others \\
   520	HF7 & Credible bankruptcy of large failing units is associated with lower rents & Rescues are followed by lower, not higher, subsequent rents \\
   521	\bottomrule
   522	\end{tabularx}
   523	\end{table}
   524	
   525	HF1 refines source hypothesis H1 and follows from \cref{prop:financial-power:influence} together with Culpepper's account of quiet politics \citep{culpepper2010}; the alternative falsifier comes from Branham, Soroka, and Wlezien \citep{branham2017}. HF2 specializes source hypothesis H3. HF3 follows from \cref{prop:financial-power:sovereign-credit} and the Habsburg evidence \citep{drelichman2011}. HF4 tests the argument of Rajan and Zingales \citep{rajan2003} and the evidence on connected lending: Khwaja and Mian find that politically connected firms in Pakistan obtained more credit from government banks and defaulted more often \citep{khwaja2005}, and Fisman finds that the market value of firms connected to Suharto fell when rumors of his ill health spread \citep{fisman2001}. HF5 tests the rentier mechanism against the within-country null of Haber and Menaldo \citep{habermenaldo2011}. HF6 states the fusion mechanism with its public-goods rival. HF7 tests the soft budget constraint.
   526	
   527	\subsection{Rival explanations and identification}
   528	
   529	Each hypothesis faces four rival explanations that coding must address. Economies of scale and natural monopoly can produce high concentration without any political cause. Public-goods provision can justify discretion and concentration, which is the source's Proposition 4 and hypothesis H6 \citep{largo2026hbs}. Survivorship can reverse the causal arrow, since firms that grow large for economic reasons attract political connections. And preference alignment can make the wealthy appear influential when they merely agree with the majority \citep{branham2017}. The event-study and latent-variable designs specified by \citet{largo2026hbs} address some of these threats, but each requires assumptions, such as parallel trends before a reform and measurement invariance across regimes, that must be tested rather than assumed. Measurement invariance is the most demanding: a control share in a Soviet ministry and a control share in a private bank may not be the same construct, and if invariance fails the comparison must use regime-specific models.
   530	

 succeeded in 0ms:
   260	A second attempt appeals to markets. In a pure market economy, on this view, nobody allocates: prices do. But prices settle conflicts only against a background of property rules that say who may sell what, and those rules are made, interpreted, and enforced by other pillars. Allocation by price is a settlement procedure of the property-and-exchange mode, and control shares in it are given by the distribution of endowments. The market answer to the guiding question is ``whoever owns,'' which is an answer, not a dissolution of the question.
   261	
   262	A third attempt imagines post-scarcity abundance through automation. It fails twice: no existing governance system satisfies it, and even a society with abundant manufactured goods would allocate land, energy, computation, and attention, which remain finite and contested.
   263	
   264	The case that narrows the claim is the one already identified: a collective in which unsettled conflicts carry no risk of dissolution. The falsifier for the financial pillar's necessity is therefore precise. It is a persistent collective whose members hold conflicting claims on some good and resolve them predominantly without any procedure in the sense of \cref{def:financial-power:settlement}. We found no documented case in the sources reviewed (cutoff October 2026).
   265	
   266	\subsection{Necessity without concentration}
   267	
   268	The necessity of the financial pillar implies nothing about how its control is distributed or how open it is to challenge. The next result makes this exact at the level of the pillar; Part VII proves the corresponding non-implication for all six pillars together.
   269	
   270	\begin{proposition}[Pillar-level non-implication]
   271	\label{prop:financial-power:nonimplication}
   272	Fix $n\geq 2$. For every $h\in[1/n,1]$ there is a control-share vector $s$ on $n$ actors with $H(s)=h$. Consequently, for every $h\in[1/n,1]$ and every $c\in[0,1]$ there is an allocation regime in which the financial pillar exists, $H_{\pF}=h$, and $Q_{\pF}=c$, and the financial term $u_{\pF}=H_{\pF}(1-Q_{\pF})$ takes every value in $[0,1]$.
   273	\end{proposition}
   274	
   275	\begin{proof}
   276	For $a\in[1/n,1]$ let $s(a)$ give share $a$ to one actor and $(1-a)/(n-1)$ to each of the others. Then $H(s(a))=a^2+(1-a)^2/(n-1)$, which is continuous in $a$, equals $1/n$ at $a=1/n$, and equals $1$ at $a=1$. By the intermediate value theorem every $h\in[1/n,1]$ is attained. Contestability is scored from features (disclosure, audit, entry, appeal) that the share vector does not determine, so any $c\in[0,1]$ can be paired with any $h$; existence of the pillar requires only that some settlement procedure operate, which it does under any share vector. Finally $u_{\pF}=h(1-c)$ equals $0$ at $c=1$ and equals $h$ at $c=0$, so taking $h=1$ and letting $c$ range over $[0,1]$ attains every value in $[0,1]$.
   277	\end{proof}
   278	
   279	The proposition is elementary, and its role is to block a common inference. That every polity has someone who controls resources is a structural fact. That some polity's resource control is concentrated and unaccountable is an empirical claim about $H_{\pF}$, $Q_{\pF}$, and the couplings $C_{\pF n}$, which requires evidence of the kind \citet{largo2026hbs} specifies for capture links. The rest of this paper is about that evidence.
   280	
   281	\section{Literature on financial power}
   282	\label{sec:literature}
   283	
   284	Research on resource command and political power has developed along four lines that rarely meet. Each supplies a mechanism the financial pillar needs, and each has a rival literature that limits it.
   285	
   286	The economic theory of regulation asks how resource holders shape the rules that govern them. Stigler's theory of economic regulation treats regulation as a good demanded by industries and supplied by the state, so that regulatory agencies tend to serve the regulated \citep{stigler1971}. Peltzman generalized the model: a regulator balances producer and consumer pressure, so outcomes fall between pure capture and pure public interest \citep{peltzman1976}. Becker showed that competition among pressure groups limits the transfers any one group can extract, because deadweight losses grow with the size of the transfer and mobilize the losers \citep{becker1983}. Laffont and Tirole recast capture as a principal-supervisor-agent problem in which the danger of collusion between the supervisor and the regulated firm shapes the optimal design of incentives \citep{laffont1991}. Grossman and Helpman modeled trade protection as the outcome of contribution schedules offered to an incumbent government \citep{grossman1994}. Dal B\'o surveys the theory and evidence \citep{dalbo2006}, and Carpenter and Moss insist on a demanding definition: capture requires showing that regulation was directed away from the public interest and toward the regulated industry by the industry's own intent and action, not merely that the industry benefited \citep{carpentermoss2014}. That standard is the same one the capture link of \citet{largo2026hbs} encodes.
   287	
   288	Rent-seeking theory measures the costs of the contest itself. Tullock observed that resources spent to obtain or defend monopolies and tariffs are a social cost beyond the usual deadweight triangle \citep{tullock1967}; Krueger named the activity rent seeking and estimated its scale in licensing regimes \citep{krueger1974}; Posner argued that competition for rents can dissipate them entirely \citep{posner1975}. Olson supplied the organizational asymmetry that makes such contests one-sided: small groups with concentrated stakes organize more readily than large groups with diffuse ones \citep{olson1965}. These works explain why concentrated resource control tends to seek conversion into rule-making power. They do not show that the conversion succeeds, and direct studies of influence suggest that it often does not.
   289	
   290	Those studies concern democracies, and they divide sharply. Lindblom argued that business holds a privileged position because governments depend on private investment for the prosperity on which they are judged \citep{lindblom1977}. Przeworski stated the same dependence as a dilemma for electoral socialism: a party that threatens profits risks the investment its program needs \citep{przeworski1985}. Mills described an interlocking economic, political, and military elite in the postwar United States \citep{mills1956}, and Winters defines oligarchy by the political work of wealth defense, which he traces from Athens and Rome to the modern United States \citep{winters2011}. Against these accounts, Ansolabehere, de Figueiredo, and Snyder find that campaign money in the United States is small relative to the value of government policy and behaves more like consumption than investment \citep{ansolabehere2003}, and Baumgartner and colleagues find, in a large sample of issues, that the side with more resources often fails to win \citep{baumgartner2009}. Mizruchi documents the fragmentation of the American corporate elite after the 1970s, which cuts against claims of a unified business class \citep{mizruchi2013}. Gilens and Page's finding that economic elites and organized business interests have substantial independent influence on policy while average citizens have little \citep{gilens2014} is disputed by Branham, Soroka, and Wlezien, who show that the preferences of the affluent and the middle class differ on relatively few issues and that the affluent win only modestly more often when they do differ \citep{branham2017}. Culpepper offers a reconciliation: business power is strongest in quiet politics, on technical issues of low public salience \citep{culpepper2010}.
   291	
   292	Political economists of the state study the relation between rulers and the resources they command. Kornai's soft budget constraint describes a paternalistic state that rescues loss-making enterprises, so that the enterprises' expectations of rescue erode the discipline of the budget \citep{kornai1986,kornai1992}. North, Wallis, and Weingast describe limited-access orders in which the dominant coalition creates rents for its members and so binds them to keep the peace, and open-access orders in which entry into economic and political organization is impersonal \citep{nww2009}. The rentier-state literature, originating with Mahdavy's study of Iran and developed by Beblawi and Luciani, holds that states living on external rents need not bargain with taxpayers \citep{mahdavy1970,beblawiluciani1987}; Ross tests the claim cross-nationally \citep{ross2001,ross2012}, and Haber and Menaldo find that the association between resource wealth and authoritarianism does not survive within-country analysis over long time series \citep{habermenaldo2011}. Levi models rulers as revenue maximizers constrained by their bargaining power, transaction costs, and discount rates, and argues that compliance is quasi-voluntary when taxpayers believe others also pay and the ruler keeps its bargains \citep{levi1988}. Tilly traces European state formation along capital-intensive and coercion-intensive paths, in which rulers obtained the means of war either from merchants and cities or by direct extraction from the land \citep{tilly1990}. This paper owns the financing side of that fiscal-military account; Part V treats its coercive side \citep{long2026coercive}.
   293	
   294	Two normative and sociological works connect these lines to the cross-pillar question. Walzer defines tyranny as the conversion of dominance in one sphere of distribution into dominance in another, as when wealth buys office or office buys wealth \citep{walzer1983}. Bourdieu treats economic, cultural, social, and symbolic capital as convertible into one another at rates that are themselves objects of struggle \citep{bourdieu1989}. Both supply a vocabulary for what the multiplex model measures with the couplings $C_{\pF n}$: the degree to which control of resources carries control of rules, rulings, beliefs, sanctions, and work. Mann's model of ideological, economic, military, and political networks of power is the nearest precedent for a pluralist decomposition of social power \citep{mann1986}; Part IV presents it in full and compares it with the six-pillar scheme \citep[Section 4]{long2026ideological}.
   295	
   296	The capture literature tests resource-to-rule conversion mostly in one regime type, the market democracy, and the literatures on party-states, rentier states, and early modern fiscal states each describe resource command within one regime family. None places the universal allocation function, its necessity, and its regime-specific distribution in a single frame with common measures. That frame is what the six-pillar model provides, and the comparison below applies it.
   297	
   298	\section{Comparative analysis across six regime types}
   299	\label{sec:comparative}
   300	
   301	The six regime types of the series span two institutional dimensions rather than six exclusive categories. Market capitalism and social democracy describe how an economy organizes ownership, bargaining, and allocation; secular democracy describes how a constitution separates, delegates, and reviews authority over resources. Communist party-states, Islamic states, and the Catholic monarchies of early modern Europe combine a position on each dimension with a distinctive source of legitimacy. A single polity can therefore be coded on both dimensions, and most contemporary market-capitalist and social-democratic polities are also secular democracies. Each subsection below examines which institutions hold the financial pillar, how concentrated and contestable control is, how the pillar is coupled to the other five, what preserves accountability, and which capture episodes and checks are documented.
   302	
   303	No polity has yet been coded under a preregistered protocol, so no numerical value of $H_{\pF}$, $Q_{\pF}$, $U_t$, or $\Integ_t$ is reported for any real case. Statements that a value is high or low are hypotheses about what such coding would find.
   304	
   305	\subsection{Market-capitalist societies}
   306	
   307	In market-capitalist societies the financial pillar is held mainly by private owners of capital, by banks and other financial intermediaries, by corporations, and by institutional investors, with a central bank controlling the supply of money and a state controlling a public budget. The dominant settlement mode is property and exchange, supplemented by command allocation through taxation and public spending. Control shares within subdomains can be highly concentrated: Piketty documents long periods in which the return on capital exceeded the growth rate and wealth concentration rose \citep{piketty2014}. Aggregate concentration across all actors is lower than within subdomains, which is the aggregation gap of \cref{prop:financial-power:aggregation-gap} at work.
   308	
   309	The characteristic coupling is $C_{\pF\pP}$, the conversion of resources into influence over rule-making, which \citet{largo2026hbs} calls the wealth-to-rules pathway. Evidence that the pathway operates is substantial. Igan, Mishra, and Tressel find that lenders who lobbied more intensively before the 2008 crisis made riskier loans and performed worse in the crisis \citep{igan2012}. Mian, Sufi, and Trebbi find that campaign contributions from the financial industry predicted congressional votes on the major housing and financial legislation of 2008, alongside constituents' mortgage distress \citep{mian2010}. Kalla and Broockman show experimentally that disclosing a constituent's status as a donor increased access to senior congressional officials \citep{kalla2016}. Bertrand, Bombardini, and Trebbi, and Blanes i Vidal, Draca, and Fons-Rosen, show that lobbyists' value depends heavily on their personal connections to officeholders, a revolving-door effect \citep{bertrand2014,blanes2012}. Faccio finds politically connected firms in many countries, more often where corruption is higher \citep{faccio2006}. Hacker and Pierson attribute the rise of top incomes in the United States to organized political combat over taxation and regulation \citep{hackerpierson2010}, and Bartels finds senators more responsive to affluent constituents \citep{bartels2008}.
   310	
   311	The counter-evidence is as substantial. Access is not outcome: Hall and Deardorff model lobbying as a subsidy of information and labor to legislators who already agree with the lobbyist \citep{hall2006}, which implies influence over agenda and detail more than over direction. The findings of Ansolabehere and colleagues, of Baumgartner and colleagues, and of Branham, Soroka, and Wlezien cited in \cref{sec:literature} show that money is small relative to stakes, that resource advantages often lose, and that the rich win mainly when their preferences coincide with those of the middle class. Mizruchi's account of elite fragmentation suggests that $\Integ_t$ for the American business community has declined rather than risen \citep{mizruchi2013}.
   312	
   313	Accountability in this regime type rests on open entry, antitrust law, disclosure of contributions and lobbying, competitive procurement, judicial review of regulation, a free press, and elections. Contestability is therefore high on paper, and the open empirical question is how much of it binds in quiet, technical domains, where Culpepper finds business power strongest \citep{culpepper2010}. Capture and its checks are both documented. The best documented capture episode in the sources reviewed is pre-crisis financial regulation, where both the lobbying evidence and the outcome evidence point in the same direction. The best documented checks are the frequent defeats of well-funded interests and the electoral reversals of policy that the pluralist literature records.
   314	
   315	The couplings $C_{\pF\pI}$, through sponsorship of research and ownership of media, and $C_{\pF\pJ}$, through the resources that let repeat players litigate, are plausible but less systematically measured. Part III analyzes the contest between repeat players and occasional litigants (Proposition 4.3 of \citealt{long2026judicial}), and Part IV shows that endorsements from captured authorities carry no information (Proposition 2.9 of \citealt{long2026ideological}).
   316	
   317	\subsection{Communist party-states}
   318	
   319	In the communist party-state the financial pillar is held by planners and ministries, by state banks, and by managers of state enterprises appointed through the party's personnel system. The dominant settlement mode is command allocation, with property and exchange confined to permitted margins. Formal concentration is extreme, since the state owns the principal means of production and the party controls appointments to the posts that allocate them. Kornai's account of the classical socialist system makes the party's monopoly of power the defining feature from which the economic features follow \citep{kornai1992}. In the terms of \citet{largo2026hbs}, the control path runs from appointment to allocation rather than from wealth to rules, and the coupling $C_{\pP\pF}$ is near its maximum by design. Part II owns the appointment channel (Definition 2.8 of \citealt{long2026political}); here we record its financial consequences.
   320	
   321	Formal concentration overstates effective concentration. Gregory's study of the Soviet archives shows that the top leadership could not allocate everything and bargained constantly with ministries and enterprises that held better information about their own capacities \citep{gregory2004}. Berliner's interviews with former Soviet managers documented the informal procurement agents who obtained scarce inputs outside the plan, and the networks of favors through which managers met targets \citep{berliner1957}; Ledeneva reconstructed the economy of favors, known as blat, that ran alongside the formal allocation of goods in the late Soviet period \citep{ledeneva1998}. These informal channels lowered effective concentration while also lowering contestability, since favors were by nature unrecorded and unreviewable. Kornai's soft budget constraint completes the picture: enterprises expected rescue from their administrative superiors, so loss did not lead to exit, and the allocation of credit followed bargaining power rather than performance \citep{kornai1986}.
   322	
   323	The reform-era People's Republic of China shows that the regime type admits wide variation. A large private sector emerged and came to produce much of output and employment \citep{lardy2014,naughton2007}. The banking system nevertheless remained dominated by state-owned banks whose senior executives are appointed through the party's personnel system, and Walter and Howie describe the resulting financial structure as serving party priorities \citep{walterhowie2011}. Allen, Qian, and Qian observe that China grew rapidly despite a formal legal and financial system weaker than standard theory would predict, and attribute much of the growth to firms financed through informal and alternative channels \citep{allen2005}. Milhaupt and Zheng argue that ownership is a poor guide to control, because large private firms are also tied to the party-state through their founders' political memberships and their dependence on state support \citep{milhaupt2015}. Cross-nationally, La Porta, L\'opez-de-Silanes, and Shleifer associate government ownership of banks with slower subsequent financial development \citep{laporta2002}, and Shleifer and Vishny model politicians' use of state firms to deliver employment and patronage \citep{shleifer1994}.
   324	
   325	Accountability in the classical system ran through the party's own control organs, so contestability against the party itself was low. Documented capture episodes include the bargaining and soft budgets that Kornai describes, which transferred resources to enterprises and officials with bargaining power. The transition from communism produced the clearest cases of reciprocal capture in the comparative record. Hellman found that early winners from partial reform blocked further reform that would have dissipated their rents \citep{hellman1998}; Hellman, Jones, and Kaufmann defined state capture as firms shaping the basic rules of the game through private payments to officials \citep{hellman2000}; Black, Kraakman, and Tarassova describe insider privatization in Russia \citep{black2000}; and Guriev and Rachinsky document the concentration of Russian industrial ownership among a small number of owners \citep{guriev2005}. Treisman argues that the conventional account of the loans-for-shares auctions overstates their role in that concentration \citep{treisman2010}, a reminder that even the canonical episode is contested. The documented checks within the regime type are the hard budget constraints that reform introduced in some sectors and the competition from non-state firms that limited the rents of state incumbents.
   326	
   327	\subsection{Social democracy and market socialism}
   328	
   329	In social democracies the financial pillar is mixed. Private capital owns most productive assets, but high taxation, a large public budget, public pension funds, and corporatist bargaining among employers, unions, and the state give organized labor and the state substantial shares of decision-relevant control. Korpi's power-resources theory explains the configuration as the product of labor's organizational strength, which allowed it to win through democratic politics what it could not win through ownership \citep{korpi1983}. Esping-Andersen traces how social democratic parties used state power to reduce workers' dependence on the market \citep{esping1985}, and Berman locates the movement's origin in a commitment to the primacy of politics over markets \citep{berman2006}. Hall and Soskice classify the economies that developed from these settlements as coordinated market economies, in which firms solve problems of training, finance, and wage setting through non-market institutions \citep{hallsoskice2001}.
   330	
   331	Social democracy combined high taxation with remarkably concentrated private ownership. H\"ogfeldt shows that Swedish corporate control was held through pyramids and dual-class shares by a few families and foundations, of which the Wallenberg sphere was the largest, and argues that social democratic governments tolerated this concentration as a stable partner for investment and employment \citep{hogfeldt2005}. Subdomain concentration in the ownership of large firms was therefore high, while the public budget, pensions, and wage setting were held by other actors. That is the separated configuration of \cref{ex:aggregation}, with a large aggregation gap.
   332	
   333	The most direct attempt to change who held the financial pillar was the Swedish proposal for wage-earner funds, which would have transferred a growing share of corporate equity to funds controlled by the labor movement. Pontusson's account shows how employers mobilized against the proposal, how the enacted version was diluted, and how the episode revealed the limits of social democratic power over investment \citep{pontusson1992}. Przeworski's dilemma predicts exactly this limit: a democratic government that threatens the returns to capital faces the possibility that investment falls \citep{przeworski1985}. Streeck argues that later decades shifted power from citizens to creditors as states financed themselves through debt \citep{streeck2014}.
   334	
   335	The couplings characteristic of this type are $C_{\pF\pW}$ and $C_{\pF\pP}$, but they take a bargained rather than a captured form: organized capital and organized labor both hold seats in the arenas where wages, pensions, and investment rules are set. Accountability rests on electoral competition, on the countervailing power of unions, and on transparency norms. Scheve and Stasavage show that the high progressive taxation of the twentieth century followed mass mobilization for war and arguments for fair compensation rather than democracy as such \citep{scheve2016}. We found fewer documented capture episodes for this type in the sources reviewed (cutoff October 2026). The main candidate is the entrenchment of concentrated family control that H\"ogfeldt describes, which social democratic governments accepted in exchange for investment \citep{hogfeldt2005}. The documented check is that labor's organized power repeatedly reversed advantages that capital held, which is one of the four findings that \citet{largo2026hbs} lists as undermining a strong capture thesis.
   336	
   337	\subsection{Islamic states}
   338	
   339	Islamic states are polities whose rulers derived legitimacy in substantial part from religious law, and they differ widely among themselves: the early caliphates, the Ottoman Empire, the Safavid and later Iranian states, and modern Saudi Arabia and the Islamic Republic of Iran organized resource command in very different ways. Islam here is a source of political legitimacy in specific historical states, not an essence that determines their economic institutions.
   340	
   341	Classical Islamic law supplied several settlement modes at once. The treasury, the bayt al-m\=al, held public revenues under the ruler's control. The obligatory alms tax, zak\=at, assigned a share of certain kinds of wealth to specified categories of recipients. The waqf, a perpetual endowment, dedicated the yield of an asset to purposes fixed by its founder under a trustee, and the qadi courts supervised its administration. Partnership forms, especially the commenda contract known as qir\=ad or mu\d{d}\=araba, organized long-distance trade \citep{udovitch1970,cizakca1996}. Singer describes how endowments financed mosques, schools, hospitals, and public kitchens across Ottoman and wider Islamic societies \citep{singer2008}. Kuran argues that the waqf provided public goods while protecting wealth from expropriation by rulers, and that its rigidity, together with features of Islamic partnership and inheritance law, limited the development of durable commercial organizations \citep{kuran2001,kuran2004,kuran2011}. The thesis is contested. Rubin attributes the divergence between Western Europe and the Middle East less to the content of Islamic law than to the role of religious authorities in legitimating rulers \citep{rubin2017}, and Kuru locates the cause in an alliance between the ulama and the state that took shape in the eleventh century \citep{kuru2019}. These accounts disagree about causes; they agree that the distribution of the financial pillar among rulers, jurists, endowments, and merchants shaped later development.
   342	
   343	The Ottoman Empire illustrates a fiscal regime built on command allocation and credit. Karaman and Pamuk show that Ottoman central revenues per capita fell behind those of the leading European states in the seventeenth and eighteenth centuries and that the state relied increasingly on tax farming, including life-term tax farms, which converted future revenues into present credit from local and provincial elites \citep{karaman2010}. In a comparative study they relate the different paths of European and Ottoman fiscal development to the interaction of warfare, economic structure, and political regime \citep{karaman2013}. Pamuk's monetary history records the use of debasement as a revenue source in fiscal crises \citep{pamuk2000}. Tax farming dispersed the collection of revenue among many holders, lowering $H_{\pF}$, while coupling it tightly to local political and coercive power.
   344	
   345	Modern Islamic states are mostly rentier states, and their allocation regimes are shaped by oil more than by religious law. Hertog describes the Saudi state as a set of fiefdoms and brokerage networks built around royal patrons, alongside islands of efficient bureaucracy such as the national oil company \citep{hertog2010}. Chaudhry contrasts the institutional erosion that oil wealth produced in Saudi Arabia with the different path of labor-exporting Yemen \citep{chaudhry1997}, and Vitalis reconstructs the corporate and political entanglements of the American oil company in the early Saudi state \citep{vitalis2007}. In the Islamic Republic of Iran, revolutionary foundations known as bonyads control large economic assets outside the ordinary budget, and the Revolutionary Guards developed substantial business interests, including construction and engineering firms \citep{maloney2015,wehrey2009}. That fusion of financial and coercive control is the coupling $C_{\pF\pC}$ in its most direct form; Part V treats the coercive side. El-Gamal argues that much of modern Islamic finance replicates conventional instruments in legally permissible form, so that its religious label says little about how control is distributed \citep{elgamal2006}.
   346	
   347	Accountability varied with the type of state. Qadi supervision of endowments, the jurists' claim to interpret the law independently of rulers, and the commercial courts all provided checks in classical and Ottoman settings, although Kuran records that rulers did at times confiscate endowments \citep{kuran2001}. In modern rentier states the rentier argument predicts weak fiscal bargaining because the state does not depend on taxpayers \citep{beblawiluciani1987,ross2001}, but the within-country evidence of Haber and Menaldo cautions against treating oil as a sufficient cause \citep{habermenaldo2011}. Documented capture episodes include the off-budget concentration of assets in Iran's foundations and security forces; documented checks include the juristic independence that endowment supervision required and the variation across Islamic polities that rules out any single Islamic allocation regime.
   348	
   349	\subsection{Catholic monarchies of early modern Europe}
   350	
   351	In the Catholic monarchies of early modern Europe, royal authority was intertwined with the Church, and the financial pillar was distributed among the crown's fiscal apparatus, private bankers who lent to the crown, the Church with its lands and tithes, and officeholders who had bought their posts. Habsburg Spain, Bourbon France, and the Papal States organized these elements differently, and Gallican and ultramontane traditions disagreed about the Church's relation to royal finance. Catholicism here, like Islam in the preceding subsection, is a source of political legitimacy in specific states, not a determinant of their institutions.
   352	
   353	Habsburg Spain under Philip II is the best studied case of sovereign credit in the period. The crown borrowed heavily from Genoese and other bankers through short-term contracts called asientos and long-term bonds called juros, and it suspended payments on several occasions. Drelichman and Voth show that lending nevertheless continued, that the bankers earned positive returns overall, and that the payment stops are better read as excusable defaults in bad fiscal states, followed by negotiated settlements, than as predation \citep{drelichman2011,drelichman2014}. Conklin models the relationship as a repeated game in which the bankers' capacity to act together disciplined the crown \citep{conklin1998}. The coupling $C_{\pF\pC}$ was strong, since the debt financed war, while $C_{\pF\pP}$ ran through the Cortes of Castile, whose consent was needed for important taxes and which therefore constrained the crown's capacity to pledge revenue. \Cref{prop:financial-power:sovereign-credit} in \cref{sec:mechanisms} gives the formal condition.
   354	
   355	Bourbon France combined a royal fiscal system with extensive sale of offices and tax farming. Doyle describes venality as the sale of offices that became the heritable property of their holders, so that judges and financial officials owned their posts \citep{doyle1996}. Kwass shows how privilege sorted subjects for taxation and how new direct taxes provoked eighteenth-century disputes over liberty and equality \citep{kwass2000}. Velde and Weir analyze the crown's borrowing through life annuities and other instruments before 1789 \citep{velde1992}, and Hoffman, Postel-Vinay, and Rosenthal reconstruct a large private credit market organized by Parisian notaries \citep{hoffman2000}. The essays collected by Hoffman and Norberg compare how fiscal crises interacted with representative institutions across European states \citep{hoffmannorberg1994}. Venality made the financial pillar less concentrated and less contestable at once: offices were dispersed across many holders, but holders could not be removed except by reimbursement, and the coupling between $\pF$ and $\pJ$ was direct because judicial offices were purchased.
   356	
   357	The Papal States and the finances of the papacy give the case of fusion between financial and spiritual authority. Prodi describes the pope as both head of the Church and territorial prince, with a fiscal and administrative apparatus that anticipated features of other early modern states \citep{prodi1987}. De Roover's history of the Medici bank documents its role as depository of the papal Camera \citep{deroover1963}, and Padgett and Ansell show how the Medici built power in Florence through overlapping networks of marriage, business, and patronage \citep{padgett1993}, which is a historical multiplex in exactly the sense of \citet{largo2026hbs}. Ekelund and colleagues interpret the medieval Church as an economic firm that sought rents \citep{ekelund1996}; the interpretation is contested, and we cite it as one reading of the evidence rather than as an established result.
   358	
   359	Accountability in these monarchies rested on representative bodies such as the Cortes and the Parlements, on the repeated-game discipline that lenders imposed, on ecclesiastical immunities that sometimes protected Church wealth from the crown and sometimes protected the crown's allies, and on conflict between crown and Church. Documented capture episodes include the conversion of financial office into judicial office through venality. Documented checks include the Cortes' control over new taxes in Castile and the bankers' capacity to withhold further credit.
   360	
   361	\subsection{Secular democracies}
   362	
   363	Secular democracies distribute authority among elected officials, courts, independent agencies, and private institutions, and justify it without reference to religious law. The financial pillar in such polities includes private holders, as in the first and third types, together with public institutions designed to be insulated from the elected government: an independent central bank, a supreme audit institution, competition authorities, and procurement and disclosure regimes. The distinctive feature of the type is constitutional: it separates the holders of different financial subdomains and places some of them beyond the direct reach of elected officials.
   364	
   365	Central bank independence is the clearest example of delegated financial authority. Alesina and Summers found that more independent central banks were associated with lower and more stable inflation, without a corresponding cost in real growth \citep{alesina1993}. Goodhart traces the evolution of central banks from government bankers to institutions charged with monetary stability and the supervision of banks \citep{goodhart1988}. Delegation raises contestability against elected officials, who can no longer finance spending by printing money, but it concentrates control of the monetary subdomain in a small technocratic body. Whether delegation reduces unaccountable concentration or relocates it is therefore an empirical question about the review that independent agencies themselves face, through legislative oversight, published reasoning, and judicial review.
   366	
   367	Secular democracies also build disclosure and review into the coupling $C_{\pF\pP}$. Lobbying registers, contribution limits, beneficial-ownership registers, and competitive procurement aim to make the wealth-to-rules pathway visible and contestable; \citet{largo2026hbs} lists them among redesign measures. The revolving-door evidence cited above shows that personal connections still carry value \citep{blanes2012,bertrand2014}, and Carpenter and Moss collect designs intended to prevent capture, including procedural requirements, external review, and the deliberate building of countervailing expertise \citep{carpentermoss2014}. Rajan and Zingales show that financial development in many countries reversed between the early twentieth century and the postwar decades, and argue that incumbent firms and financiers oppose financial development when it would admit competitors \citep{rajan2003}. Their result implies that constitutional separation does not by itself prevent incumbents from using political influence to close entry.
   368	
   369	Accountability in this type is the highest on paper, because the review of financial decisions is spread across courts, legislatures, auditors, and the press. The documented capture episodes are those of the first type, since most secular democracies are also market economies, and their characteristic form is quiet influence on technical rules. The documented checks are the binding constraints that independent agencies, courts, and elections impose, including judicial invalidation of regulations and the electoral replacement of governments that have favored concentrated interests. Scheve and Stasavage show that democracies do not automatically tax the rich more heavily \citep{scheve2016}, which is a reminder that constitutional design shapes the distribution of financial control without determining it.
   370	
   371	\subsection{Summary of the comparison}
   372	
   373	\Cref{tab:regimes} collects the comparison. Every row has a financial pillar, which is the necessity claim; the rows differ in who holds it, how it is coupled, and what checks it, which is where the contingent capture claim must be tested.
   374	
   375	\begin{table}[t]
   376	\centering
   377	\small
   378	\caption{The financial pillar across the six regime types. Coupling entries are hypotheses about which pairs a preregistered coding would find strongest, not measured values.}
   379	\label{tab:regimes}
   380	\begin{tabularx}{\linewidth}{@{}L{2.2cm}YL{2.1cm}Y@{}}
   381	\toprule
   382	Regime type & Typical holders of control & Strongest couplings & Main sources of accountability \\
   383	\midrule
   384	Market capitalism & Private owners, banks, corporations, and a central bank & $C_{\pF\pP}$, $C_{\pF\pI}$, $C_{\pF\pJ}$ & Open entry, antitrust, disclosure, courts, and elections \\
   385	Communist party-state & Planners, state banks, and managers appointed by the party & $C_{\pP\pF}$ and $C_{\pF\pC}$ & Mainly the party's own control organs, with informal bargaining \\
   386	Social democracy & Private owners alongside unions, public funds, and the state budget & $C_{\pF\pW}$ and $C_{\pF\pP}$ & Elections, organized labor, and transparency norms \\
   387	Islamic states & Treasuries, endowment trustees, merchants, tax farmers, and rentier states & $C_{\pF\pC}$ and $C_{\pF\pI}$ & Qadi supervision and juristic independence, varying widely by state \\
   388	Catholic monarchies & The crown, its bankers, the Church, and owners of venal offices & $C_{\pF\pC}$ and $C_{\pF\pJ}$ & Representative assemblies, lenders' discipline, and Church-crown conflict \\
   389	Secular democracies & Private holders with independent central banks, auditors, and regulators & $C_{\pF\pP}$ in quiet, technical domains & Delegated review, courts, legislatures, and the press \\
   390	\bottomrule

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '320,395p' papers/latex/financial-power.tex | nl -ba -v320" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   320	
   321	Formal concentration overstates effective concentration. Gregory's study of the Soviet archives shows that the top leadership could not allocate everything and bargained constantly with ministries and enterprises that held better information about their own capacities \citep{gregory2004}. Berliner's interviews with former Soviet managers documented the informal procurement agents who obtained scarce inputs outside the plan, and the networks of favors through which managers met targets \citep{berliner1957}; Ledeneva reconstructed the economy of favors, known as blat, that ran alongside the formal allocation of goods in the late Soviet period \citep{ledeneva1998}. These informal channels lowered effective concentration while also lowering contestability, since favors were by nature unrecorded and unreviewable. Kornai's soft budget constraint completes the picture: enterprises expected rescue from their administrative superiors, so loss did not lead to exit, and the allocation of credit followed bargaining power rather than performance \citep{kornai1986}.
   322	
   323	The reform-era People's Republic of China shows that the regime type admits wide variation. A large private sector emerged and came to produce much of output and employment \citep{lardy2014,naughton2007}. The banking system nevertheless remained dominated by state-owned banks whose senior executives are appointed through the party's personnel system, and Walter and Howie describe the resulting financial structure as serving party priorities \citep{walterhowie2011}. Allen, Qian, and Qian observe that China grew rapidly despite a formal legal and financial system weaker than standard theory would predict, and attribute much of the growth to firms financed through informal and alternative channels \citep{allen2005}. Milhaupt and Zheng argue that ownership is a poor guide to control, because large private firms are also tied to the party-state through their founders' political memberships and their dependence on state support \citep{milhaupt2015}. Cross-nationally, La Porta, L\'opez-de-Silanes, and Shleifer associate government ownership of banks with slower subsequent financial development \citep{laporta2002}, and Shleifer and Vishny model politicians' use of state firms to deliver employment and patronage \citep{shleifer1994}.
   324	
   325	Accountability in the classical system ran through the party's own control organs, so contestability against the party itself was low. Documented capture episodes include the bargaining and soft budgets that Kornai describes, which transferred resources to enterprises and officials with bargaining power. The transition from communism produced the clearest cases of reciprocal capture in the comparative record. Hellman found that early winners from partial reform blocked further reform that would have dissipated their rents \citep{hellman1998}; Hellman, Jones, and Kaufmann defined state capture as firms shaping the basic rules of the game through private payments to officials \citep{hellman2000}; Black, Kraakman, and Tarassova describe insider privatization in Russia \citep{black2000}; and Guriev and Rachinsky document the concentration of Russian industrial ownership among a small number of owners \citep{guriev2005}. Treisman argues that the conventional account of the loans-for-shares auctions overstates their role in that concentration \citep{treisman2010}, a reminder that even the canonical episode is contested. The documented checks within the regime type are the hard budget constraints that reform introduced in some sectors and the competition from non-state firms that limited the rents of state incumbents.
   326	
   327	\subsection{Social democracy and market socialism}
   328	
   329	In social democracies the financial pillar is mixed. Private capital owns most productive assets, but high taxation, a large public budget, public pension funds, and corporatist bargaining among employers, unions, and the state give organized labor and the state substantial shares of decision-relevant control. Korpi's power-resources theory explains the configuration as the product of labor's organizational strength, which allowed it to win through democratic politics what it could not win through ownership \citep{korpi1983}. Esping-Andersen traces how social democratic parties used state power to reduce workers' dependence on the market \citep{esping1985}, and Berman locates the movement's origin in a commitment to the primacy of politics over markets \citep{berman2006}. Hall and Soskice classify the economies that developed from these settlements as coordinated market economies, in which firms solve problems of training, finance, and wage setting through non-market institutions \citep{hallsoskice2001}.
   330	
   331	Social democracy combined high taxation with remarkably concentrated private ownership. H\"ogfeldt shows that Swedish corporate control was held through pyramids and dual-class shares by a few families and foundations, of which the Wallenberg sphere was the largest, and argues that social democratic governments tolerated this concentration as a stable partner for investment and employment \citep{hogfeldt2005}. Subdomain concentration in the ownership of large firms was therefore high, while the public budget, pensions, and wage setting were held by other actors. That is the separated configuration of \cref{ex:aggregation}, with a large aggregation gap.
   332	
   333	The most direct attempt to change who held the financial pillar was the Swedish proposal for wage-earner funds, which would have transferred a growing share of corporate equity to funds controlled by the labor movement. Pontusson's account shows how employers mobilized against the proposal, how the enacted version was diluted, and how the episode revealed the limits of social democratic power over investment \citep{pontusson1992}. Przeworski's dilemma predicts exactly this limit: a democratic government that threatens the returns to capital faces the possibility that investment falls \citep{przeworski1985}. Streeck argues that later decades shifted power from citizens to creditors as states financed themselves through debt \citep{streeck2014}.
   334	
   335	The couplings characteristic of this type are $C_{\pF\pW}$ and $C_{\pF\pP}$, but they take a bargained rather than a captured form: organized capital and organized labor both hold seats in the arenas where wages, pensions, and investment rules are set. Accountability rests on electoral competition, on the countervailing power of unions, and on transparency norms. Scheve and Stasavage show that the high progressive taxation of the twentieth century followed mass mobilization for war and arguments for fair compensation rather than democracy as such \citep{scheve2016}. We found fewer documented capture episodes for this type in the sources reviewed (cutoff October 2026). The main candidate is the entrenchment of concentrated family control that H\"ogfeldt describes, which social democratic governments accepted in exchange for investment \citep{hogfeldt2005}. The documented check is that labor's organized power repeatedly reversed advantages that capital held, which is one of the four findings that \citet{largo2026hbs} lists as undermining a strong capture thesis.
   336	
   337	\subsection{Islamic states}
   338	
   339	Islamic states are polities whose rulers derived legitimacy in substantial part from religious law, and they differ widely among themselves: the early caliphates, the Ottoman Empire, the Safavid and later Iranian states, and modern Saudi Arabia and the Islamic Republic of Iran organized resource command in very different ways. Islam here is a source of political legitimacy in specific historical states, not an essence that determines their economic institutions.
   340	
   341	Classical Islamic law supplied several settlement modes at once. The treasury, the bayt al-m\=al, held public revenues under the ruler's control. The obligatory alms tax, zak\=at, assigned a share of certain kinds of wealth to specified categories of recipients. The waqf, a perpetual endowment, dedicated the yield of an asset to purposes fixed by its founder under a trustee, and the qadi courts supervised its administration. Partnership forms, especially the commenda contract known as qir\=ad or mu\d{d}\=araba, organized long-distance trade \citep{udovitch1970,cizakca1996}. Singer describes how endowments financed mosques, schools, hospitals, and public kitchens across Ottoman and wider Islamic societies \citep{singer2008}. Kuran argues that the waqf provided public goods while protecting wealth from expropriation by rulers, and that its rigidity, together with features of Islamic partnership and inheritance law, limited the development of durable commercial organizations \citep{kuran2001,kuran2004,kuran2011}. The thesis is contested. Rubin attributes the divergence between Western Europe and the Middle East less to the content of Islamic law than to the role of religious authorities in legitimating rulers \citep{rubin2017}, and Kuru locates the cause in an alliance between the ulama and the state that took shape in the eleventh century \citep{kuru2019}. These accounts disagree about causes; they agree that the distribution of the financial pillar among rulers, jurists, endowments, and merchants shaped later development.
   342	
   343	The Ottoman Empire illustrates a fiscal regime built on command allocation and credit. Karaman and Pamuk show that Ottoman central revenues per capita fell behind those of the leading European states in the seventeenth and eighteenth centuries and that the state relied increasingly on tax farming, including life-term tax farms, which converted future revenues into present credit from local and provincial elites \citep{karaman2010}. In a comparative study they relate the different paths of European and Ottoman fiscal development to the interaction of warfare, economic structure, and political regime \citep{karaman2013}. Pamuk's monetary history records the use of debasement as a revenue source in fiscal crises \citep{pamuk2000}. Tax farming dispersed the collection of revenue among many holders, lowering $H_{\pF}$, while coupling it tightly to local political and coercive power.
   344	
   345	Modern Islamic states are mostly rentier states, and their allocation regimes are shaped by oil more than by religious law. Hertog describes the Saudi state as a set of fiefdoms and brokerage networks built around royal patrons, alongside islands of efficient bureaucracy such as the national oil company \citep{hertog2010}. Chaudhry contrasts the institutional erosion that oil wealth produced in Saudi Arabia with the different path of labor-exporting Yemen \citep{chaudhry1997}, and Vitalis reconstructs the corporate and political entanglements of the American oil company in the early Saudi state \citep{vitalis2007}. In the Islamic Republic of Iran, revolutionary foundations known as bonyads control large economic assets outside the ordinary budget, and the Revolutionary Guards developed substantial business interests, including construction and engineering firms \citep{maloney2015,wehrey2009}. That fusion of financial and coercive control is the coupling $C_{\pF\pC}$ in its most direct form; Part V treats the coercive side. El-Gamal argues that much of modern Islamic finance replicates conventional instruments in legally permissible form, so that its religious label says little about how control is distributed \citep{elgamal2006}.
   346	
   347	Accountability varied with the type of state. Qadi supervision of endowments, the jurists' claim to interpret the law independently of rulers, and the commercial courts all provided checks in classical and Ottoman settings, although Kuran records that rulers did at times confiscate endowments \citep{kuran2001}. In modern rentier states the rentier argument predicts weak fiscal bargaining because the state does not depend on taxpayers \citep{beblawiluciani1987,ross2001}, but the within-country evidence of Haber and Menaldo cautions against treating oil as a sufficient cause \citep{habermenaldo2011}. Documented capture episodes include the off-budget concentration of assets in Iran's foundations and security forces; documented checks include the juristic independence that endowment supervision required and the variation across Islamic polities that rules out any single Islamic allocation regime.
   348	
   349	\subsection{Catholic monarchies of early modern Europe}
   350	
   351	In the Catholic monarchies of early modern Europe, royal authority was intertwined with the Church, and the financial pillar was distributed among the crown's fiscal apparatus, private bankers who lent to the crown, the Church with its lands and tithes, and officeholders who had bought their posts. Habsburg Spain, Bourbon France, and the Papal States organized these elements differently, and Gallican and ultramontane traditions disagreed about the Church's relation to royal finance. Catholicism here, like Islam in the preceding subsection, is a source of political legitimacy in specific states, not a determinant of their institutions.
   352	
   353	Habsburg Spain under Philip II is the best studied case of sovereign credit in the period. The crown borrowed heavily from Genoese and other bankers through short-term contracts called asientos and long-term bonds called juros, and it suspended payments on several occasions. Drelichman and Voth show that lending nevertheless continued, that the bankers earned positive returns overall, and that the payment stops are better read as excusable defaults in bad fiscal states, followed by negotiated settlements, than as predation \citep{drelichman2011,drelichman2014}. Conklin models the relationship as a repeated game in which the bankers' capacity to act together disciplined the crown \citep{conklin1998}. The coupling $C_{\pF\pC}$ was strong, since the debt financed war, while $C_{\pF\pP}$ ran through the Cortes of Castile, whose consent was needed for important taxes and which therefore constrained the crown's capacity to pledge revenue. \Cref{prop:financial-power:sovereign-credit} in \cref{sec:mechanisms} gives the formal condition.
   354	
   355	Bourbon France combined a royal fiscal system with extensive sale of offices and tax farming. Doyle describes venality as the sale of offices that became the heritable property of their holders, so that judges and financial officials owned their posts \citep{doyle1996}. Kwass shows how privilege sorted subjects for taxation and how new direct taxes provoked eighteenth-century disputes over liberty and equality \citep{kwass2000}. Velde and Weir analyze the crown's borrowing through life annuities and other instruments before 1789 \citep{velde1992}, and Hoffman, Postel-Vinay, and Rosenthal reconstruct a large private credit market organized by Parisian notaries \citep{hoffman2000}. The essays collected by Hoffman and Norberg compare how fiscal crises interacted with representative institutions across European states \citep{hoffmannorberg1994}. Venality made the financial pillar less concentrated and less contestable at once: offices were dispersed across many holders, but holders could not be removed except by reimbursement, and the coupling between $\pF$ and $\pJ$ was direct because judicial offices were purchased.
   356	
   357	The Papal States and the finances of the papacy give the case of fusion between financial and spiritual authority. Prodi describes the pope as both head of the Church and territorial prince, with a fiscal and administrative apparatus that anticipated features of other early modern states \citep{prodi1987}. De Roover's history of the Medici bank documents its role as depository of the papal Camera \citep{deroover1963}, and Padgett and Ansell show how the Medici built power in Florence through overlapping networks of marriage, business, and patronage \citep{padgett1993}, which is a historical multiplex in exactly the sense of \citet{largo2026hbs}. Ekelund and colleagues interpret the medieval Church as an economic firm that sought rents \citep{ekelund1996}; the interpretation is contested, and we cite it as one reading of the evidence rather than as an established result.
   358	
   359	Accountability in these monarchies rested on representative bodies such as the Cortes and the Parlements, on the repeated-game discipline that lenders imposed, on ecclesiastical immunities that sometimes protected Church wealth from the crown and sometimes protected the crown's allies, and on conflict between crown and Church. Documented capture episodes include the conversion of financial office into judicial office through venality. Documented checks include the Cortes' control over new taxes in Castile and the bankers' capacity to withhold further credit.
   360	
   361	\subsection{Secular democracies}
   362	
   363	Secular democracies distribute authority among elected officials, courts, independent agencies, and private institutions, and justify it without reference to religious law. The financial pillar in such polities includes private holders, as in the first and third types, together with public institutions designed to be insulated from the elected government: an independent central bank, a supreme audit institution, competition authorities, and procurement and disclosure regimes. The distinctive feature of the type is constitutional: it separates the holders of different financial subdomains and places some of them beyond the direct reach of elected officials.
   364	
   365	Central bank independence is the clearest example of delegated financial authority. Alesina and Summers found that more independent central banks were associated with lower and more stable inflation, without a corresponding cost in real growth \citep{alesina1993}. Goodhart traces the evolution of central banks from government bankers to institutions charged with monetary stability and the supervision of banks \citep{goodhart1988}. Delegation raises contestability against elected officials, who can no longer finance spending by printing money, but it concentrates control of the monetary subdomain in a small technocratic body. Whether delegation reduces unaccountable concentration or relocates it is therefore an empirical question about the review that independent agencies themselves face, through legislative oversight, published reasoning, and judicial review.
   366	
   367	Secular democracies also build disclosure and review into the coupling $C_{\pF\pP}$. Lobbying registers, contribution limits, beneficial-ownership registers, and competitive procurement aim to make the wealth-to-rules pathway visible and contestable; \citet{largo2026hbs} lists them among redesign measures. The revolving-door evidence cited above shows that personal connections still carry value \citep{blanes2012,bertrand2014}, and Carpenter and Moss collect designs intended to prevent capture, including procedural requirements, external review, and the deliberate building of countervailing expertise \citep{carpentermoss2014}. Rajan and Zingales show that financial development in many countries reversed between the early twentieth century and the postwar decades, and argue that incumbent firms and financiers oppose financial development when it would admit competitors \citep{rajan2003}. Their result implies that constitutional separation does not by itself prevent incumbents from using political influence to close entry.
   368	
   369	Accountability in this type is the highest on paper, because the review of financial decisions is spread across courts, legislatures, auditors, and the press. The documented capture episodes are those of the first type, since most secular democracies are also market economies, and their characteristic form is quiet influence on technical rules. The documented checks are the binding constraints that independent agencies, courts, and elections impose, including judicial invalidation of regulations and the electoral replacement of governments that have favored concentrated interests. Scheve and Stasavage show that democracies do not automatically tax the rich more heavily \citep{scheve2016}, which is a reminder that constitutional design shapes the distribution of financial control without determining it.
   370	
   371	\subsection{Summary of the comparison}
   372	
   373	\Cref{tab:regimes} collects the comparison. Every row has a financial pillar, which is the necessity claim; the rows differ in who holds it, how it is coupled, and what checks it, which is where the contingent capture claim must be tested.
   374	
   375	\begin{table}[t]
   376	\centering
   377	\small
   378	\caption{The financial pillar across the six regime types. Coupling entries are hypotheses about which pairs a preregistered coding would find strongest, not measured values.}
   379	\label{tab:regimes}
   380	\begin{tabularx}{\linewidth}{@{}L{2.2cm}YL{2.1cm}Y@{}}
   381	\toprule
   382	Regime type & Typical holders of control & Strongest couplings & Main sources of accountability \\
   383	\midrule
   384	Market capitalism & Private owners, banks, corporations, and a central bank & $C_{\pF\pP}$, $C_{\pF\pI}$, $C_{\pF\pJ}$ & Open entry, antitrust, disclosure, courts, and elections \\
   385	Communist party-state & Planners, state banks, and managers appointed by the party & $C_{\pP\pF}$ and $C_{\pF\pC}$ & Mainly the party's own control organs, with informal bargaining \\
   386	Social democracy & Private owners alongside unions, public funds, and the state budget & $C_{\pF\pW}$ and $C_{\pF\pP}$ & Elections, organized labor, and transparency norms \\
   387	Islamic states & Treasuries, endowment trustees, merchants, tax farmers, and rentier states & $C_{\pF\pC}$ and $C_{\pF\pI}$ & Qadi supervision and juristic independence, varying widely by state \\
   388	Catholic monarchies & The crown, its bankers, the Church, and owners of venal offices & $C_{\pF\pC}$ and $C_{\pF\pJ}$ & Representative assemblies, lenders' discipline, and Church-crown conflict \\
   389	Secular democracies & Private holders with independent central banks, auditors, and regulators & $C_{\pF\pP}$ in quiet, technical domains & Delegated review, courts, legislatures, and the press \\
   390	\bottomrule
   391	\end{tabularx}
   392	\end{table}
   393	
   394	Three results of the comparison bear on the series' thesis. The financial pillar is present in every type and in every case examined, held by institutions that have almost nothing else in common. The control path differs by regime as \citet{largo2026hbs} predicts: wealth to rules in market societies, appointment to allocation in party-states, bargaining between organized interests in social democracies, ruler to rent in rentier states, and lender to ruler in early modern fiscal states. And every type has both documented capture episodes and documented checks, so the type alone does not settle whether a polity's financial pillar is captured. That question requires coding a particular polity in a particular period.
   395	

codex
The structure and package declarations are internally coherent so far. I’m now checking every in-file label/reference and citation key, plus environment/brace balance; because you restricted the review to this one source file, I’m treating box warnings as static layout risks rather than claiming compiler-log evidence.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "perl -0777 -ne '
  my "'$s=$_;
  my (%lab,%ref,%bib,%cite,%beg,%end);
  while($s =~ /'"\\\\label\\{(["'^}]+)'"\\}/g){"'$lab{$1}++}
  while($s =~ /'"\\\\(?:[Cc]ref|eqref)\\{(["'^}]+)'"\\}/g){"'$ref{$_}++ for split /,/, $1}
  while($s =~ /'"\\\\bibitem(?:\\[["'^'"\\]]*\\])?\\{(["'^}]+)'"\\}/g){"'$bib{$1}++}
  while($s =~ /'"\\\\cite(?:p|t|alt|alp|author|year|yearpar|num)?(?:\\[["'^'"\\]]*\\])?(?:\\[["'^'"\\]]*\\])?\\{(["'^}]+)'"\\}/g){"'$cite{$_}++ for split /,/, $1}
  while($s =~ /'"\\\\begin\\{(["'^}]+)'"\\}/g){"'$beg{$1}++}
  while($s =~ /'"\\\\end\\{(["'^}]+)'"\\}/g){"'$end{$1}++}
  print "UNDEFINED REFS'"\\n\"; print \""'$_'"\\n\" for grep {"'!$lab{$_}} sort keys %ref;
  print "UNCITED LABEL DUPLICATES'"\\n\"; print \""'$_ $lab{$_}'"\\n\" for grep {"'$lab{$_}>1} sort keys %lab;
  print "UNDEFINED CITES'"\\n\"; print \""'$_'"\\n\" for grep {"'!$bib{$_}} sort keys %cite;
  print "DUPLICATE BIBKEYS'"\\n\"; print \""'$_ $bib{$_}'"\\n\" for grep {"'$bib{$_}>1} sort keys %bib;
  print "ENV MISMATCH COUNTS'"\\n\"; print \""'$_ begin=$beg{$_} end=".($end{$_}//0)."'"\\n\" for grep {("'$beg{$_}//0)!=($end{$_}//0)} sort keys %beg;
  print "COUNTS labels=".(scalar keys %lab)." refs=".(scalar keys %ref)." bib=".(scalar keys %bib)." cites=".(scalar keys %cite)."'"\\n\";
' papers/latex/financial-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
UNDEFINED REFS
UNCITED LABEL DUPLICATES
UNDEFINED CITES
DUPLICATE BIBKEYS
ENV MISMATCH COUNTS
COUNTS labels=31 refs=19 bib=139 cites=139

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'command -v chktex || true' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
/Library/TeX/texbin/chktex

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'chktex -q papers/latex/financial-power.tex' in /Users/mlong/Documents/Development/the-beast-system
 exited 2 in 0ms:
Warning 24 in papers/latex/financial-power.tex line 74: Delete this space to maintain correct pagereferences.
\label{sec:intro}  
^
Warning 24 in papers/latex/financial-power.tex line 89: Delete this space to maintain correct pagereferences.
\label{sec:pillar}  
^
Warning 3 in papers/latex/financial-power.tex line 93: You should enclose the previous parenthesis with `{}'.
The series inherits its formal objects from \citet{largo2026hbs} and does not redefine them. A polity at time~$t$ is a directed multiplex network $G_t=(V_t,E_t)$ whose nodes are organizations or coherent actor groups. Each pillar $m$ in the index set $\Pillars=\{\pF,\pP,\pJ,\pI,\pC,\pW\}$, with $M=|\Pillars|=6$, contributes a layer with adjacency $A^m_t$ and edge weights $a^m_{ij,t}\in[0,1]$ that record the documented capacity of actor~$i$ to constrain a feasible action of actor~$j$ through mechanism~$m$. A many-to-many role map assigns actors to pillars. Actor~$i$ holds a normalized share $s^m_{i,t}$ of decision-relevant control in pillar~$m$, with $\sum_i s^m_{i,t}=1$; concentration is the Herfindahl-Hirschman index $H_{m,t}=\sum_i (s^m_{i,t})^2$ \citep{hirschman1964}; contestability $Q_{m,t}\in[0,1]$ scores transparency, appeal rights, independence, competition, and credible replacement of decision makers. The illustrative index of unaccountable concentration is $U_t=\sum_m \omega_m H_{m,t}(1-Q_{m,t})$ with preregistered weights $\omega_m\geq 0$ summing to one.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ^
Warning 24 in papers/latex/financial-power.tex line 102: Delete this space to maintain correct pagereferences.
\label{def:financial-power:allocation-problem}  
^
Warning 3 in papers/latex/financial-power.tex line 103: You should enclose the previous parenthesis with `{}'.
Let $N$ be a collective of $n\geq 2$ members and $\mathcal{K}$ a finite set of goods, with available stock $\omega\in\mathbb{R}^{\mathcal{K}}_{+}$ at a given date. Each member $i$ holds a claim $c_i\in\mathbb{R}^{\mathcal{K}}_{+}$ on the stock. A \emph{conflict} occurs when the claims on some good $k$ are jointly infeasible, $\sum_{i\in N}c_{ik}>\omega_k$. An \emph{allocation problem} is the task of determining, for each conflict, which feasible assignment $x=(x_i)_{i\in N}$ with $\sum_i x_i\leq\omega$ prevails, together with the related decisions of who may use a good, who may store it, and what is held in reserve.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ^
Warning 13 in papers/latex/financial-power.tex line 106: Intersentence spacing (`\@') should perhaps be used.
Scarcity in this sense is relative to claims, not absolute. A group can be materially comfortable and still face conflicts, because the meat of one animal, the best grazing in a dry season, or the revenue of one year is claimed by more people, or for more purposes, than it can satisfy. This is the scarcity axiom of the series (Ax1: resources are finite and claims on them conflict), whose general statement and refinement belong to Part VII.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                          ^
Warning 24 in papers/latex/financial-power.tex line 109: Delete this space to maintain correct pagereferences.
\label{def:financial-power:settlement}  
^
Warning 24 in papers/latex/financial-power.tex line 116: Delete this space to maintain correct pagereferences.
\label{def:financial-power:settlement-modes}  
^
Warning 24 in papers/latex/financial-power.tex line 123: Delete this space to maintain correct pagereferences.
\label{def:financial-power:allocation-regime}  
^
Warning 24 in papers/latex/financial-power.tex line 143: Delete this space to maintain correct pagereferences.
\label{prop:financial-power:aggregation-gap}  
^
Warning 3 in papers/latex/financial-power.tex line 144: You should enclose the previous parenthesis with `{}'.
Let the financial pillar consist of subdomains $k=1,\dots,K$ with weights $\beta_k\geq 0$, $\sum_k\beta_k=1$, and control-share vectors $s^{k}=(s^{k}_i)_{i\in N}$, each summing to one. Define the aggregate share $\bar s_i=\sum_k\beta_k s^{k}_i$. Then  
                                                                                                                                                       ^
Warning 3 in papers/latex/financial-power.tex line 149: You should enclose the previous parenthesis with `{}'.
where $\operatorname{Var}_\beta(s^{\cdot}_i)=\sum_k\beta_k(s^{k}_i-\bar s_i)^2$ is the $\beta$-weighted variance of actor $i$'s share across subdomains. Equality holds if and only if every actor holds the same share in every subdomain of positive weight.  
                                                                           ^
Warning 3 in papers/latex/financial-power.tex line 153: You should enclose the previous parenthesis with `{}'.
The aggregate shares sum to one, since $\sum_i\bar s_i=\sum_k\beta_k\sum_i s^k_i=\sum_k\beta_k=1$, so $H(\bar s)$ is a valid concentration index. For a fixed actor $i$, the identity $\sum_k\beta_k(s^k_i)^2-\bigl(\sum_k\beta_k s^k_i\bigr)^2=\sum_k\beta_k(s^k_i-\bar s_i)^2$ is the usual decomposition of a second moment into a squared mean and a variance; it uses only $\sum_k\beta_k=1$. Summing over $i$ gives  
                                                                                                                                                                                                          ^
Warning 3 in papers/latex/financial-power.tex line 153: You should enclose the previous parenthesis with `{}'.
The aggregate shares sum to one, since $\sum_i\bar s_i=\sum_k\beta_k\sum_i s^k_i=\sum_k\beta_k=1$, so $H(\bar s)$ is a valid concentration index. For a fixed actor $i$, the identity $\sum_k\beta_k(s^k_i)^2-\bigl(\sum_k\beta_k s^k_i\bigr)^2=\sum_k\beta_k(s^k_i-\bar s_i)^2$ is the usual decomposition of a second moment into a squared mean and a variance; it uses only $\sum_k\beta_k=1$. Summing over $i$ gives  
                                                                                                                                                                                                                                            ^
Warning 3 in papers/latex/financial-power.tex line 153: You should enclose the previous parenthesis with `{}'.
The aggregate shares sum to one, since $\sum_i\bar s_i=\sum_k\beta_k\sum_i s^k_i=\sum_k\beta_k=1$, so $H(\bar s)$ is a valid concentration index. For a fixed actor $i$, the identity $\sum_k\beta_k(s^k_i)^2-\bigl(\sum_k\beta_k s^k_i\bigr)^2=\sum_k\beta_k(s^k_i-\bar s_i)^2$ is the usual decomposition of a second moment into a squared mean and a variance; it uses only $\sum_k\beta_k=1$. Summing over $i$ gives  
                                                                                                                                                                                                                                                                            ^
Warning 3 in papers/latex/financial-power.tex line 155: You should enclose the previous parenthesis with `{}'.
\sum_k\beta_k\sum_i(s^k_i)^2-\sum_i\bar s_i^{\,2}=\sum_i\operatorname{Var}_\beta(s^{\cdot}_i),  
                         ^
Warning 2 in papers/latex/financial-power.tex line 157: Non-breaking space (`~') should have been used.
which is \eqref{eq:aggregation-gap}. Each variance is nonnegative and vanishes exactly when $s^k_i=\bar s_i$ for every $k$ with $\beta_k>0$.  
        ^
Warning 24 in papers/latex/financial-power.tex line 161: Delete this space to maintain correct pagereferences.
\label{ex:aggregation}  
^
Warning 24 in papers/latex/financial-power.tex line 168: Delete this space to maintain correct pagereferences.
\label{sec:necessity}  
^
Warning 24 in papers/latex/financial-power.tex line 175: Delete this space to maintain correct pagereferences.
\label{ass:scarcity}  
^
Warning 24 in papers/latex/financial-power.tex line 180: Delete this space to maintain correct pagereferences.
\label{ass:hazard}  
^
Warning 24 in papers/latex/financial-power.tex line 187: Delete this space to maintain correct pagereferences.
\label{prop:financial-power:necessity}  
^
Warning 3 in papers/latex/financial-power.tex line 190: You should enclose the previous parenthesis with `{}'.
\item[(a)] $\Prob(S_T\cap\{Z_T\geq k\})\leq(1-q)^k$;  
                                               ^
Warning 3 in papers/latex/financial-power.tex line 192: You should enclose the previous parenthesis with `{}'.
\item[(c)] if the collective has no settlement procedure at all, so that $Z_T=Y_T$, then $\Prob(S_T)\leq(1-q)^{\lceil pT/2\rceil}+e^{-pT/8}$;  
                                                                                                            ^
Warning 3 in papers/latex/financial-power.tex line 195: You should enclose the previous parenthesis with `{}'.
\Prob\Bigl(\frac{Z_T}{Y_T}\geq\frac{2k}{pT}\,\Big|\,S_T\Bigr)\leq\frac{(1-q)^k+e^{-pT/8}}{\nu}.  
                                                                           ^
Warning 3 in papers/latex/financial-power.tex line 202: You should enclose the previous parenthesis with `{}'.
(a) Let $\tau_j$ be the period of the $j$-th unsettled conflict, with $\tau_j=\infty$ if there is none, and let $A_j$ be the event that $\tau_j\leq T$ and the collective survives period $\tau_j$. Set $A_0$ to be the sure event. A $j$-th unsettled conflict can occur only if the collective survived the $(j-1)$-th, so $A_j\subseteq A_{j-1}$. Conditional on the history before $\tau_j$ and on the conflict being unsettled, \cref{ass:hazard} gives survival probability at most $1-q$. Hence $\Prob(A_j)\leq(1-q)\Prob(\tau_j\leq T,\ \text{alive at }\tau_j)\leq(1-q)\Prob(A_{j-1})$, and by induction $\Prob(A_k)\leq(1-q)^k$. If the collective survives through $T$ and $Z_T\geq k$, then the $k$-th unsettled conflict occurred by $T$ and was survived, so $S_T\cap\{Z_T\geq k\}\subseteq A_k$.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ^
Warning 3 in papers/latex/financial-power.tex line 206: You should enclose the previous parenthesis with `{}'.
(c) If every conflict is unsettled, then on $S_T\cap\{Y_T\geq pT/2\}$ we have $Z_T\geq\lceil pT/2\rceil$, so by (a) that event has probability at most $(1-q)^{\lceil pT/2\rceil}$. Adding the bound in (b) for the complementary part of $S_T$ gives the claim.  
                                                                                                                                                            ^
Warning 24 in papers/latex/financial-power.tex line 214: Delete this space to maintain correct pagereferences.
\label{ex:survival}  
^
Warning 36 in papers/latex/financial-power.tex line 215: You should put a space in front of parenthesis.
Suppose, purely for illustration, that a band of foragers meets a conflict over some good in at least one week in ten ($p=0.1$), and that each unsettled conflict carries a five percent chance of permanent fission or lethal violence ($q=0.05$). If the band had no settlement procedure at all, \cref{prop:financial-power:necessity}(c) bounds its probability of surviving ten years ($T=520$ weeks) by $0.95^{26}+e^{-6.5}\approx 0.265$, and of surviving fifty years ($T=2600$) by $0.95^{130}+e^{-32.5}\approx 0.0013$. The parameters are invented; the geometric decay is not.  
                                                                                                                                                                                                                                                                                                                                         ^
Warning 26 in papers/latex/financial-power.tex line 230: You ought to remove spaces in front of punctuation.
Woodburn's comparison of immediate-return societies, including the Hadza, Mbuti, !Kung, and Batek, generalizes the point. These societies avoid storage and accumulation, make sharing obligatory, and maintain what Woodburn calls leveling mechanisms that prevent any member from converting a temporary advantage into lasting control \citep{woodburn1982}. The equality of these societies is an outcome that institutions produce and defend, not the absence of institutions. Boehm reaches the same conclusion from a broader comparative sample of foragers: egalitarian bands sustain equality through a reverse dominance hierarchy in which the group collectively sanctions would-be dominants, and enforcement of meat-sharing against hoarders is one of its recurring targets \citep{boehm1999}.  
                                                                                ^
Warning 24 in papers/latex/financial-power.tex line 240: Delete this space to maintain correct pagereferences.
\label{tab:minimal}  
^
Warning 38 in papers/latex/financial-power.tex line 260: You should not use punctuation in front of quotes.
A second attempt appeals to markets. In a pure market economy, on this view, nobody allocates: prices do. But prices settle conflicts only against a background of property rules that say who may sell what, and those rules are made, interpreted, and enforced by other pillars. Allocation by price is a settlement procedure of the property-and-exchange mode, and control shares in it are given by the distribution of endowments. The market answer to the guiding question is ``whoever owns,'' which is an answer, not a dissolution of the question.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ^
Warning 24 in papers/latex/financial-power.tex line 271: Delete this space to maintain correct pagereferences.
\label{prop:financial-power:nonimplication}  
^
Warning 3 in papers/latex/financial-power.tex line 276: You should enclose the previous parenthesis with `{}'.
For $a\in[1/n,1]$ let $s(a)$ give share $a$ to one actor and $(1-a)/(n-1)$ to each of the others. Then $H(s(a))=a^2+(1-a)^2/(n-1)$, which is continuous in $a$, equals $1/n$ at $a=1/n$, and equals $1$ at $a=1$. By the intermediate value theorem every $h\in[1/n,1]$ is attained. Contestability is scored from features (disclosure, audit, entry, appeal) that the share vector does not determine, so any $c\in[0,1]$ can be paired with any $h$; existence of the pillar requires only that some settlement procedure operate, which it does under any share vector. Finally $u_{\pF}=h(1-c)$ equals $0$ at $c=1$ and equals $h$ at $c=0$, so taking $h=1$ and letting $c$ range over $[0,1]$ attains every value in $[0,1]$.  
                                                                                                                        ^
Warning 24 in papers/latex/financial-power.tex line 282: Delete this space to maintain correct pagereferences.
\label{sec:literature}  
^
Warning 24 in papers/latex/financial-power.tex line 299: Delete this space to maintain correct pagereferences.
\label{sec:comparative}  
^
Warning 24 in papers/latex/financial-power.tex line 379: Delete this space to maintain correct pagereferences.
\label{tab:regimes}  
^
Warning 24 in papers/latex/financial-power.tex line 397: Delete this space to maintain correct pagereferences.
\label{sec:mechanisms}  
^
Warning 24 in papers/latex/financial-power.tex line 406: Delete this space to maintain correct pagereferences.
\label{def:financial-power:conversion}  
^
Warning 24 in papers/latex/financial-power.tex line 419: Delete this space to maintain correct pagereferences.
\label{prop:financial-power:influence}  
^
Warning 9 in papers/latex/financial-power.tex line 420: `)' expected, found `]'.
An actor with financial share $s\in(0,1]$ faces a rule whose adoption is worth $sV$ to it, where $V>0$ is the value of the rule to the whole resource base. By spending $e\geq 0$ the actor makes adoption occur with probability $\pi(e,Q)$, where $Q\in[0,1)$ is the contestability of the receiving pillar and $\pi$ is twice continuously differentiable on $[0,\infty)\times[0,1)$ with $\pi_e>0$, $\pi_{ee}<0$, and $\pi_{eQ}<0$. At $Q=1$ influence has no return and the actor spends nothing. The actor maximizes $sV\pi(e,Q)-e$. If the maximizer $e^*$ is interior, then  
                                       ^
Warning 9 in papers/latex/financial-power.tex line 420: `]' expected, found `)'.
An actor with financial share $s\in(0,1]$ faces a rule whose adoption is worth $sV$ to it, where $V>0$ is the value of the rule to the whole resource base. By spending $e\geq 0$ the actor makes adoption occur with probability $\pi(e,Q)$, where $Q\in[0,1)$ is the contestability of the receiving pillar and $\pi$ is twice continuously differentiable on $[0,\infty)\times[0,1)$ with $\pi_e>0$, $\pi_{ee}<0$, and $\pi_{eQ}<0$. At $Q=1$ influence has no return and the actor spends nothing. The actor maximizes $sV\pi(e,Q)-e$. If the maximizer $e^*$ is interior, then  
                                                                                                                                                                                                                                                             ^
Warning 9 in papers/latex/financial-power.tex line 420: `]' expected, found `)'.
An actor with financial share $s\in(0,1]$ faces a rule whose adoption is worth $sV$ to it, where $V>0$ is the value of the rule to the whole resource base. By spending $e\geq 0$ the actor makes adoption occur with probability $\pi(e,Q)$, where $Q\in[0,1)$ is the contestability of the receiving pillar and $\pi$ is twice continuously differentiable on $[0,\infty)\times[0,1)$ with $\pi_e>0$, $\pi_{ee}<0$, and $\pi_{eQ}<0$. At $Q=1$ influence has no return and the actor spends nothing. The actor maximizes $sV\pi(e,Q)-e$. If the maximizer $e^*$ is interior, then  
                                                                                                                                                                                                                                                                                                                                                                          ^
Warning 9 in papers/latex/financial-power.tex line 420: `]' expected, found `)'.
An actor with financial share $s\in(0,1]$ faces a rule whose adoption is worth $sV$ to it, where $V>0$ is the value of the rule to the whole resource base. By spending $e\geq 0$ the actor makes adoption occur with probability $\pi(e,Q)$, where $Q\in[0,1)$ is the contestability of the receiving pillar and $\pi$ is twice continuously differentiable on $[0,\infty)\times[0,1)$ with $\pi_e>0$, $\pi_{ee}<0$, and $\pi_{eQ}<0$. At $Q=1$ influence has no return and the actor spends nothing. The actor maximizes $sV\pi(e,Q)-e$. If the maximizer $e^*$ is interior, then  
                                                                                                                                                                                                                                                                                                                                                                                     ^
Warning 24 in papers/latex/financial-power.tex line 433: Delete this space to maintain correct pagereferences.
\label{ex:threshold}  
^
Warning 24 in papers/latex/financial-power.tex line 446: Delete this space to maintain correct pagereferences.
\label{prop:financial-power:sovereign-credit}  
^
Warning 24 in papers/latex/financial-power.tex line 474: Delete this space to maintain correct pagereferences.
\label{sec:measurement}  
^
Warning 24 in papers/latex/financial-power.tex line 484: Delete this space to maintain correct pagereferences.
\label{tab:indicators}  
^
Warning 24 in papers/latex/financial-power.tex line 509: Delete this space to maintain correct pagereferences.
\label{tab:hypotheses}  
^
Warning 24 in papers/latex/financial-power.tex line 532: Delete this space to maintain correct pagereferences.
\label{sec:revelation}  
^
Warning 8 in papers/latex/financial-power.tex line 536: Wrong length of dash may have been used.
Two passages bear on the financial pillar. The first is Revelation 13:16-17: ``And he causeth all, both small and great, rich and poor, free and bond, to receive a mark in their right hand, or in their foreheads: And that no man might buy or sell, save he that had the mark, or the name of the beast, or the number of his name.'' The image is economic participation conditioned on allegiance. In the vocabulary of this paper, it describes a financial pillar whose settlement procedure for exchange is gated by a test of loyalty administered by the ideological pillar: the coupling $C_{\pF\pI}$ is complete, and contestability for those who fail the test is zero. Part VI formalizes the same condition from the producers' side as a participation gate, access to exchange conditional on allegiance, and treats the passage as its limiting case (Definition 6.7 and Proposition 6.8 of \citealt{long2026productive}). Kraybill reads the passage against the participation of Asian merchants and artisans in trade guilds whose life was bound up with the imperial cult, so that commerce required at least tacit participation in worship \citep{kraybill1996}.  
                                                                        ^
Warning 38 in papers/latex/financial-power.tex line 536: You should not use punctuation in front of quotes.
Two passages bear on the financial pillar. The first is Revelation 13:16-17: ``And he causeth all, both small and great, rich and poor, free and bond, to receive a mark in their right hand, or in their foreheads: And that no man might buy or sell, save he that had the mark, or the name of the beast, or the number of his name.'' The image is economic participation conditioned on allegiance. In the vocabulary of this paper, it describes a financial pillar whose settlement procedure for exchange is gated by a test of loyalty administered by the ideological pillar: the coupling $C_{\pF\pI}$ is complete, and contestability for those who fail the test is zero. Part VI formalizes the same condition from the producers' side as a participation gate, access to exchange conditional on allegiance, and treats the passage as its limiting case (Definition 6.7 and Proposition 6.8 of \citealt{long2026productive}). Kraybill reads the passage against the participation of Asian merchants and artisans in trade guilds whose life was bound up with the imperial cult, so that commerce required at least tacit participation in worship \citep{kraybill1996}.  
                                                                                                                                                                                                                                                                                                                                      ^
Warning 38 in papers/latex/financial-power.tex line 540: You should not use punctuation in front of quotes.
The typological reading names the condition under which the series' structural claim acquires moral weight. The text does not condemn the existence of buying and selling; it condemns a configuration in which access to exchange depends on allegiance and the city's wealth depends on extraction and the trade in persons. That configuration is Proposition~B, the contingent capture of the financial pillar by a coalition that has also captured belief and coercion, not Proposition~A, the existence of an allocation function. The call of Revelation 18:4, ``Come out of her, my people,'' is in this reading an image of exit, one of the checks that Part VI treats. Wink's theology of the powers draws the same distinction: institutions are necessary to human life, become a system of domination when organized around it, and remain open to transformation \citep{wink1992}. The mapping from text to model is an interpretive claim of this series, offered as an aid to comparison; it is not a settled exegetical result. Collins's argument that Revelation responds to a crisis perceived by its author and audience, rather than to an empirically general persecution \citep{collins1984}, is a reminder that the text's images express a judgment about an order, which a comparative political economy cannot simply import as evidence.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ^
Warning 24 in papers/latex/financial-power.tex line 543: Delete this space to maintain correct pagereferences.
\label{sec:objections}  
^
Warning 24 in papers/latex/financial-power.tex line 558: Delete this space to maintain correct pagereferences.
\label{sec:conclusion}  
^
Warning 1 in papers/latex/financial-power.tex line 566: Command terminated with space.
\raggedright  
            ^
Warning 12 in papers/latex/financial-power.tex line 569: Interword spacing (`\ ') should perhaps be used.
Alberto Alesina and Lawrence H. Summers (1993). Central Bank Independence and Macroeconomic Performance: Some Comparative Evidence. \emph{Journal of Money, Credit and Banking} 25(2). doi:10.2307/2077833.  
                                                                                                                                   ^
Warning 12 in papers/latex/financial-power.tex line 569: Interword spacing (`\ ') should perhaps be used.
Alberto Alesina and Lawrence H. Summers (1993). Central Bank Independence and Macroeconomic Performance: Some Comparative Evidence. \emph{Journal of Money, Credit and Banking} 25(2). doi:10.2307/2077833.  
                                                                                                                                                                                      ^
Warning 12 in papers/latex/financial-power.tex line 572: Interword spacing (`\ ') should perhaps be used.
Franklin Allen, Jun Qian, and Meijun Qian (2005). Law, Finance, and Economic Growth in China. \emph{Journal of Financial Economics} 77(1). doi:10.1016/j.jfineco.2004.06.010.  
                                                                                             ^
Warning 12 in papers/latex/financial-power.tex line 572: Interword spacing (`\ ') should perhaps be used.
Franklin Allen, Jun Qian, and Meijun Qian (2005). Law, Finance, and Economic Growth in China. \emph{Journal of Financial Economics} 77(1). doi:10.1016/j.jfineco.2004.06.010.  
                                                                                                                                          ^
Warning 12 in papers/latex/financial-power.tex line 575: Interword spacing (`\ ') should perhaps be used.
Stephen Ansolabehere, John M. de Figueiredo, and James M. Snyder (2003). Why Is There So Little Money in U.S. Politics? \emph{Journal of Economic Perspectives} 17(1). doi:10.1257/089533003321164976.  
                                                                                                                                                                      ^
Warning 12 in papers/latex/financial-power.tex line 578: Interword spacing (`\ ') should perhaps be used.
David E. Aune (1998). \emph{Revelation 17-22}. Word Biblical Commentary 52C, Thomas Nelson.  
                     ^
Warning 8 in papers/latex/financial-power.tex line 578: Wrong length of dash may have been used.
David E. Aune (1998). \emph{Revelation 17-22}. Word Biblical Commentary 52C, Thomas Nelson.  
                                         ^
Warning 12 in papers/latex/financial-power.tex line 581: Interword spacing (`\ ') should perhaps be used.
Larry M. Bartels (2008). \emph{Unequal Democracy: The Political Economy of the New Gilded Age}. Princeton University Press. doi:10.1515/9781400883363.  
                        ^
Warning 12 in papers/latex/financial-power.tex line 581: Interword spacing (`\ ') should perhaps be used.
Larry M. Bartels (2008). \emph{Unequal Democracy: The Political Economy of the New Gilded Age}. Princeton University Press. doi:10.1515/9781400883363.  
                                                                                                                           ^
Warning 12 in papers/latex/financial-power.tex line 587: Interword spacing (`\ ') should perhaps be used.
Richard Bauckham (1993). \emph{The Theology of the Book of Revelation}. Cambridge University Press. doi:10.1017/cbo9780511819858.  
                        ^
Warning 12 in papers/latex/financial-power.tex line 587: Interword spacing (`\ ') should perhaps be used.
Richard Bauckham (1993). \emph{The Theology of the Book of Revelation}. Cambridge University Press. doi:10.1017/cbo9780511819858.  
                                                                                                   ^
Warning 12 in papers/latex/financial-power.tex line 590: Interword spacing (`\ ') should perhaps be used.
Frank R. Baumgartner, Jeffrey M. Berry, Marie Hojnacki, David C. Kimball, and Beth L. Leech (2009). \emph{Lobbying and Policy Change: Who Wins, Who Loses, and Why}. University of Chicago Press. doi:10.7208/chicago/9780226039466.001.0001.  
                                                                                                   ^
Warning 12 in papers/latex/financial-power.tex line 590: Interword spacing (`\ ') should perhaps be used.
Frank R. Baumgartner, Jeffrey M. Berry, Marie Hojnacki, David C. Kimball, and Beth L. Leech (2009). \emph{Lobbying and Policy Change: Who Wins, Who Loses, and Why}. University of Chicago Press. doi:10.7208/chicago/9780226039466.001.0001.  
                                                                                                                                                                                                 ^
Warning 12 in papers/latex/financial-power.tex line 593: Interword spacing (`\ ') should perhaps be used.
Hazem Beblawi and Giacomo Luciani (eds.) (1987). \emph{The Rentier State}. Croom Helm. doi:10.4324/9781315684864.  
                                                ^
Warning 12 in papers/latex/financial-power.tex line 593: Interword spacing (`\ ') should perhaps be used.
Hazem Beblawi and Giacomo Luciani (eds.) (1987). \emph{The Rentier State}. Croom Helm. doi:10.4324/9781315684864.  
                                                                                      ^
Warning 12 in papers/latex/financial-power.tex line 596: Interword spacing (`\ ') should perhaps be used.
Gary S. Becker (1983). A Theory of Competition among Pressure Groups for Political Influence. \emph{The Quarterly Journal of Economics} 98(3). doi:10.2307/1886017.  
                                                                                             ^
Warning 12 in papers/latex/financial-power.tex line 596: Interword spacing (`\ ') should perhaps be used.
Gary S. Becker (1983). A Theory of Competition among Pressure Groups for Political Influence. \emph{The Quarterly Journal of Economics} 98(3). doi:10.2307/1886017.  
                                                                                                                                              ^
Warning 12 in papers/latex/financial-power.tex line 599: Interword spacing (`\ ') should perhaps be used.
Joseph S. Berliner (1957). \emph{Factory and Manager in the USSR}. Harvard University Press. doi:10.4159/harvard.9780674188273.  
                          ^
Warning 12 in papers/latex/financial-power.tex line 599: Interword spacing (`\ ') should perhaps be used.
Joseph S. Berliner (1957). \emph{Factory and Manager in the USSR}. Harvard University Press. doi:10.4159/harvard.9780674188273.  
                                                                                            ^
Warning 12 in papers/latex/financial-power.tex line 602: Interword spacing (`\ ') should perhaps be used.
Sheri Berman (2006). \emph{The Primacy of Politics: Social Democracy and the Making of Europe's Twentieth Century}. Cambridge University Press. doi:10.1017/cbo9780511791109.  
                    ^
Warning 12 in papers/latex/financial-power.tex line 602: Interword spacing (`\ ') should perhaps be used.
Sheri Berman (2006). \emph{The Primacy of Politics: Social Democracy and the Making of Europe's Twentieth Century}. Cambridge University Press. doi:10.1017/cbo9780511791109.  
                                                                                                                                               ^
Warning 12 in papers/latex/financial-power.tex line 605: Interword spacing (`\ ') should perhaps be used.
Marianne Bertrand, Matilde Bombardini, and Francesco Trebbi (2014). Is It Whom You Know or What You Know? An Empirical Assessment of the Lobbying Process. \emph{American Economic Review} 104(12). doi:10.1257/aer.104.12.3885.  
                                                                                                                                                          ^
Warning 12 in papers/latex/financial-power.tex line 605: Interword spacing (`\ ') should perhaps be used.
Marianne Bertrand, Matilde Bombardini, and Francesco Trebbi (2014). Is It Whom You Know or What You Know? An Empirical Assessment of the Lobbying Process. \emph{American Economic Review} 104(12). doi:10.1257/aer.104.12.3885.  
                                                                                                                                                                                                   ^
Warning 12 in papers/latex/financial-power.tex line 608: Interword spacing (`\ ') should perhaps be used.
Bernard Black, Reinier Kraakman, and Anna Tarassova (2000). Russian Privatization and Corporate Governance: What Went Wrong? \emph{Stanford Law Review} 52(6). doi:10.2307/1229501.  
                                                                                                                                                              ^
Warning 12 in papers/latex/financial-power.tex line 611: Interword spacing (`\ ') should perhaps be used.
Jordi Blanes i Vidal, Mirko Draca, and Christian Fons-Rosen (2012). Revolving Door Lobbyists. \emph{American Economic Review} 102(7). doi:10.1257/aer.102.7.3731.  
                                                                                             ^
Warning 12 in papers/latex/financial-power.tex line 611: Interword spacing (`\ ') should perhaps be used.
Jordi Blanes i Vidal, Mirko Draca, and Christian Fons-Rosen (2012). Revolving Door Lobbyists. \emph{American Economic Review} 102(7). doi:10.1257/aer.102.7.3731.  
                                                                                                                                     ^
Warning 12 in papers/latex/financial-power.tex line 614: Interword spacing (`\ ') should perhaps be used.
Christopher Boehm (1999). \emph{Hierarchy in the Forest: The Evolution of Egalitarian Behavior}. Harvard University Press. doi:10.2307/j.ctvjf9xr4.  
                         ^
Warning 12 in papers/latex/financial-power.tex line 614: Interword spacing (`\ ') should perhaps be used.
Christopher Boehm (1999). \emph{Hierarchy in the Forest: The Evolution of Egalitarian Behavior}. Harvard University Press. doi:10.2307/j.ctvjf9xr4.  
                                                                                                                          ^
Warning 12 in papers/latex/financial-power.tex line 617: Interword spacing (`\ ') should perhaps be used.
Pierre Bourdieu (1989). Social Space and Symbolic Power. \emph{Sociological Theory} 7(1). doi:10.2307/202060.  
                                                        ^
Warning 12 in papers/latex/financial-power.tex line 617: Interword spacing (`\ ') should perhaps be used.
Pierre Bourdieu (1989). Social Space and Symbolic Power. \emph{Sociological Theory} 7(1). doi:10.2307/202060.  
                                                                                         ^
Warning 12 in papers/latex/financial-power.tex line 620: Interword spacing (`\ ') should perhaps be used.
J. Alexander Branham, Stuart N. Soroka, and Christopher Wlezien (2017). When Do the Rich Win? \emph{Political Science Quarterly} 132(1). doi:10.1002/polq.12577.  
                                                                                                                                        ^
Warning 12 in papers/latex/financial-power.tex line 623: Interword spacing (`\ ') should perhaps be used.
Daniel Carpenter and David A. Moss (eds.) (2014). \emph{Preventing Regulatory Capture: Special Interest Influence and How to Limit It}. Cambridge University Press. doi:10.1017/CBO9781139565875.  
                                                 ^
Warning 12 in papers/latex/financial-power.tex line 623: Interword spacing (`\ ') should perhaps be used.
Daniel Carpenter and David A. Moss (eds.) (2014). \emph{Preventing Regulatory Capture: Special Interest Influence and How to Limit It}. Cambridge University Press. doi:10.1017/CBO9781139565875.  
                                                                                                                                                                   ^
Warning 12 in papers/latex/financial-power.tex line 626: Interword spacing (`\ ') should perhaps be used.
Kiren Aziz Chaudhry (1997). \emph{The Price of Wealth: Economies and Institutions in the Middle East}. Cornell University Press. doi:10.7591/9781501700347.  
                           ^
Warning 12 in papers/latex/financial-power.tex line 626: Interword spacing (`\ ') should perhaps be used.
Kiren Aziz Chaudhry (1997). \emph{The Price of Wealth: Economies and Institutions in the Middle East}. Cornell University Press. doi:10.7591/9781501700347.  
                                                                                                                                ^
Warning 12 in papers/latex/financial-power.tex line 629: Interword spacing (`\ ') should perhaps be used.
Murat \c{C}izak\c{c}a (1996). \emph{A Comparative Evolution of Business Partnerships: The Islamic World and Europe, with Specific Reference to the Ottoman Archives}. Brill.  
                             ^
Warning 12 in papers/latex/financial-power.tex line 632: Interword spacing (`\ ') should perhaps be used.
Pierre Clastres (1987). \emph{Society against the State: Essays in Political Anthropology (1974), trans. Robert Hurley}. Zone Books. doi:10.2307/j.ctv1595m3p.  
                       ^
Warning 12 in papers/latex/financial-power.tex line 632: Interword spacing (`\ ') should perhaps be used.
Pierre Clastres (1987). \emph{Society against the State: Essays in Political Anthropology (1974), trans. Robert Hurley}. Zone Books. doi:10.2307/j.ctv1595m3p.  
                                                                                                                                    ^
Warning 12 in papers/latex/financial-power.tex line 635: Interword spacing (`\ ') should perhaps be used.
Adela Yarbro Collins (1984). \emph{Crisis and Catharsis: The Power of the Apocalypse}. Westminster Press.  
                            ^
Warning 13 in papers/latex/financial-power.tex line 638: Intersentence spacing (`\@') should perhaps be used.
James Conklin (1998). The Theory of Sovereign Debt and Spain under Philip II. \emph{Journal of Political Economy} 106(3). doi:10.1086/250019.  
                                                                            ^
Warning 12 in papers/latex/financial-power.tex line 638: Interword spacing (`\ ') should perhaps be used.
James Conklin (1998). The Theory of Sovereign Debt and Spain under Philip II. \emph{Journal of Political Economy} 106(3). doi:10.1086/250019.  
                                                                                                                         ^
Warning 12 in papers/latex/financial-power.tex line 641: Interword spacing (`\ ') should perhaps be used.
Michael Coppedge, John Gerring, David Altman, Michael Bernhard, Steven Fish, Allen Hicken, Matthew Kroenig, Staffan I. Lindberg, Kelly McMann, Pamela Paxton, Holli A. Semetko, Svend-Erik Skaaning, Jeffrey Staton, and Jan Teorell (2011). Conceptualizing and Measuring Democracy: A New Approach. \emph{Perspectives on Politics} 9(2). doi:10.1017/S1537592711000880.  
                                                                                                                                                                                                                                                                                                     ^
Warning 12 in papers/latex/financial-power.tex line 641: Interword spacing (`\ ') should perhaps be used.
Michael Coppedge, John Gerring, David Altman, Michael Bernhard, Steven Fish, Allen Hicken, Matthew Kroenig, Staffan I. Lindberg, Kelly McMann, Pamela Paxton, Holli A. Semetko, Svend-Erik Skaaning, Jeffrey Staton, and Jan Teorell (2011). Conceptualizing and Measuring Democracy: A New Approach. \emph{Perspectives on Politics} 9(2). doi:10.1017/S1537592711000880.  
                                                                                                                                                                                                                                                                                                                                           ^
Warning 12 in papers/latex/financial-power.tex line 644: Interword spacing (`\ ') should perhaps be used.
Michael Cox, Gwen Arnold, and Sergio Villamayor Tomas (2010). A Review of Design Principles for Community-based Natural Resource Management. \emph{Ecology and Society} 15(4). doi:10.5751/ES-03704-150438.  
                                                                                                                                            ^
Warning 12 in papers/latex/financial-power.tex line 644: Interword spacing (`\ ') should perhaps be used.
Michael Cox, Gwen Arnold, and Sergio Villamayor Tomas (2010). A Review of Design Principles for Community-based Natural Resource Management. \emph{Ecology and Society} 15(4). doi:10.5751/ES-03704-150438.  
                                                                                                                                                                              ^
Warning 8 in papers/latex/financial-power.tex line 644: Wrong length of dash may have been used.
Michael Cox, Gwen Arnold, and Sergio Villamayor Tomas (2010). A Review of Design Principles for Community-based Natural Resource Management. \emph{Ecology and Society} 15(4). doi:10.5751/ES-03704-150438.  
                                                                                                                                                                                                   ^
Warning 12 in papers/latex/financial-power.tex line 647: Interword spacing (`\ ') should perhaps be used.
Pepper D. Culpepper (2010). \emph{Quiet Politics and Business Power: Corporate Control in Europe and Japan}. Cambridge University Press. doi:10.1017/cbo9780511760716.  
                           ^
Warning 12 in papers/latex/financial-power.tex line 647: Interword spacing (`\ ') should perhaps be used.
Pepper D. Culpepper (2010). \emph{Quiet Politics and Business Power: Corporate Control in Europe and Japan}. Cambridge University Press. doi:10.1017/cbo9780511760716.  
                                                                                                                                        ^
Warning 12 in papers/latex/financial-power.tex line 650: Interword spacing (`\ ') should perhaps be used.
Ernesto Dal B\'o (2006). Regulatory Capture: A Review. \emph{Oxford Review of Economic Policy} 22(2). doi:10.1093/oxrep/grj013.  
                                                      ^
Warning 12 in papers/latex/financial-power.tex line 650: Interword spacing (`\ ') should perhaps be used.
Ernesto Dal B\'o (2006). Regulatory Capture: A Review. \emph{Oxford Review of Economic Policy} 22(2). doi:10.1093/oxrep/grj013.  
                                                                                                     ^
Warning 12 in papers/latex/financial-power.tex line 653: Interword spacing (`\ ') should perhaps be used.
Raymond de Roover (1963). \emph{The Rise and Decline of the Medici Bank, 1397-1494}. Harvard University Press.  
                         ^
Warning 8 in papers/latex/financial-power.tex line 653: Wrong length of dash may have been used.
Raymond de Roover (1963). \emph{The Rise and Decline of the Medici Bank, 1397-1494}. Harvard University Press.  
                                                                             ^
Warning 12 in papers/latex/financial-power.tex line 656: Interword spacing (`\ ') should perhaps be used.
William Doyle (1996). \emph{Venality: The Sale of Offices in Eighteenth-Century France}. Oxford University Press. doi:10.1093/acprof:oso/9780198205364.001.0001.  
                     ^
Warning 12 in papers/latex/financial-power.tex line 656: Interword spacing (`\ ') should perhaps be used.
William Doyle (1996). \emph{Venality: The Sale of Offices in Eighteenth-Century France}. Oxford University Press. doi:10.1093/acprof:oso/9780198205364.001.0001.  
                                                                                                                 ^
Warning 13 in papers/latex/financial-power.tex line 659: Intersentence spacing (`\@') should perhaps be used.
Mauricio Drelichman and Hans-Joachim Voth (2011). Lending to the Borrower from Hell: Debt and Default in the Age of Philip II. \emph{The Economic Journal} 121(557). doi:10.1111/j.1468-0297.2011.02442.x.  
                                                                                                                             ^
Warning 12 in papers/latex/financial-power.tex line 659: Interword spacing (`\ ') should perhaps be used.
Mauricio Drelichman and Hans-Joachim Voth (2011). Lending to the Borrower from Hell: Debt and Default in the Age of Philip II. \emph{The Economic Journal} 121(557). doi:10.1111/j.1468-0297.2011.02442.x.  
                                                                                                                                                                    ^
Warning 8 in papers/latex/financial-power.tex line 659: Wrong length of dash may have been used.
Mauricio Drelichman and Hans-Joachim Voth (2011). Lending to the Borrower from Hell: Debt and Default in the Age of Philip II. \emph{The Economic Journal} 121(557). doi:10.1111/j.1468-0297.2011.02442.x.  
                                                                                                                                                                                       ^
Warning 12 in papers/latex/financial-power.tex line 662: Interword spacing (`\ ') should perhaps be used.
Mauricio Drelichman and Hans-Joachim Voth (2014). \emph{Lending to the Borrower from Hell: Debt, Taxes, and Default in the Age of Philip II}. Princeton University Press.  
                                                 ^
Warning 12 in papers/latex/financial-power.tex line 665: Interword spacing (`\ ') should perhaps be used.
Robert B. Ekelund, Robert F. Hebert, Robert D. Tollison, Gary M. Anderson, and Audrey B. Davidson (1996). \emph{Sacred Trust: The Medieval Church as an Economic Firm}. Oxford University Press.  
                                                                                                         ^
Warning 12 in papers/latex/financial-power.tex line 668: Interword spacing (`\ ') should perhaps be used.
Mahmoud A. El-Gamal (2006). \emph{Islamic Finance: Law, Economics, and Practice}. Cambridge University Press. doi:10.1017/CBO9780511753756.  
                           ^
Warning 12 in papers/latex/financial-power.tex line 668: Interword spacing (`\ ') should perhaps be used.
Mahmoud A. El-Gamal (2006). \emph{Islamic Finance: Law, Economics, and Practice}. Cambridge University Press. doi:10.1017/CBO9780511753756.  
                                                                                                             ^
Warning 12 in papers/latex/financial-power.tex line 671: Interword spacing (`\ ') should perhaps be used.
Robert C. Ellickson (1991). \emph{Order without Law: How Neighbors Settle Disputes}. Harvard University Press. doi:10.4159/9780674036437.  
                           ^
Warning 12 in papers/latex/financial-power.tex line 671: Interword spacing (`\ ') should perhaps be used.
Robert C. Ellickson (1991). \emph{Order without Law: How Neighbors Settle Disputes}. Harvard University Press. doi:10.4159/9780674036437.  
                                                                                                              ^
Warning 12 in papers/latex/financial-power.tex line 674: Interword spacing (`\ ') should perhaps be used.
Jon Elster (1983). \emph{Explaining Technical Change: A Case Study in the Philosophy of Science}. Cambridge University Press.  
                  ^
Warning 12 in papers/latex/financial-power.tex line 677: Interword spacing (`\ ') should perhaps be used.
G\"osta Esping-Andersen (1985). \emph{Politics against Markets: The Social Democratic Road to Power}. Princeton University Press. doi:10.1515/9781400886203.  
                               ^
Warning 12 in papers/latex/financial-power.tex line 677: Interword spacing (`\ ') should perhaps be used.
G\"osta Esping-Andersen (1985). \emph{Politics against Markets: The Social Democratic Road to Power}. Princeton University Press. doi:10.1515/9781400886203.  
                                                                                                                                 ^
Warning 12 in papers/latex/financial-power.tex line 680: Interword spacing (`\ ') should perhaps be used.
E. E. Evans-Pritchard (1940). \emph{The Nuer: A Description of the Modes of Livelihood and Political Institutions of a Nilotic People}. Clarendon Press.  
                             ^
Warning 12 in papers/latex/financial-power.tex line 683: Interword spacing (`\ ') should perhaps be used.
Mara Faccio (2006). Politically Connected Firms. \emph{American Economic Review} 96(1). doi:10.1257/000282806776157704.  
                                                ^
Warning 12 in papers/latex/financial-power.tex line 683: Interword spacing (`\ ') should perhaps be used.
Mara Faccio (2006). Politically Connected Firms. \emph{American Economic Review} 96(1). doi:10.1257/000282806776157704.  
                                                                                       ^
Warning 12 in papers/latex/financial-power.tex line 686: Interword spacing (`\ ') should perhaps be used.
Raymond Fisman (2001). Estimating the Value of Political Connections. \emph{American Economic Review} 91(4). doi:10.1257/aer.91.4.1095.  
                                                                     ^
Warning 12 in papers/latex/financial-power.tex line 686: Interword spacing (`\ ') should perhaps be used.
Raymond Fisman (2001). Estimating the Value of Political Connections. \emph{American Economic Review} 91(4). doi:10.1257/aer.91.4.1095.  
                                                                                                            ^
Warning 12 in papers/latex/financial-power.tex line 689: Interword spacing (`\ ') should perhaps be used.
Robert C. Fuller (1995). \emph{Naming the Antichrist: The History of an American Obsession}. Oxford University Press. doi:10.1093/acprof:oso/9780195109795.001.0001.  
                        ^
Warning 12 in papers/latex/financial-power.tex line 689: Interword spacing (`\ ') should perhaps be used.
Robert C. Fuller (1995). \emph{Naming the Antichrist: The History of an American Obsession}. Oxford University Press. doi:10.1093/acprof:oso/9780195109795.001.0001.  
                                                                                                                     ^
Warning 12 in papers/latex/financial-power.tex line 692: Interword spacing (`\ ') should perhaps be used.
Martin Gilens and Benjamin I. Page (2014). Testing Theories of American Politics: Elites, Interest Groups, and Average Citizens. \emph{Perspectives on Politics} 12(3). doi:10.1017/S1537592714001595.  
                                                                                                                                ^
Warning 12 in papers/latex/financial-power.tex line 692: Interword spacing (`\ ') should perhaps be used.
Martin Gilens and Benjamin I. Page (2014). Testing Theories of American Politics: Elites, Interest Groups, and Average Citizens. \emph{Perspectives on Politics} 12(3). doi:10.1017/S1537592714001595.  
                                                                                                                                                                       ^
Warning 12 in papers/latex/financial-power.tex line 695: Interword spacing (`\ ') should perhaps be used.
Charles A. E. Goodhart (1988). \emph{The Evolution of Central Banks}. MIT Press.  
                              ^
Warning 12 in papers/latex/financial-power.tex line 698: Interword spacing (`\ ') should perhaps be used.
David Graeber and David Wengrow (2021). \emph{The Dawn of Everything: A New History of Humanity}. Farrar, Straus and Giroux.  
                                       ^
Warning 12 in papers/latex/financial-power.tex line 701: Interword spacing (`\ ') should perhaps be used.
Paul R. Gregory (2004). \emph{The Political Economy of Stalinism: Evidence from the Soviet Secret Archives}. Cambridge University Press. doi:10.1017/cbo9780511615856.  
                       ^
Warning 12 in papers/latex/financial-power.tex line 701: Interword spacing (`\ ') should perhaps be used.
Paul R. Gregory (2004). \emph{The Political Economy of Stalinism: Evidence from the Soviet Secret Archives}. Cambridge University Press. doi:10.1017/cbo9780511615856.  
                                                                                                                                        ^
Warning 12 in papers/latex/financial-power.tex line 704: Interword spacing (`\ ') should perhaps be used.
Gene M. Grossman and Elhanan Helpman (1994). Protection for Sale. \emph{American Economic Review} 84(4).  
                                                                 ^
Warning 12 in papers/latex/financial-power.tex line 707: Interword spacing (`\ ') should perhaps be used.
Sergei Guriev and Andrei Rachinsky (2005). The Role of Oligarchs in Russian Capitalism. \emph{Journal of Economic Perspectives} 19(1). doi:10.1257/0895330053147994.  
                                                                                       ^
Warning 12 in papers/latex/financial-power.tex line 707: Interword spacing (`\ ') should perhaps be used.
Sergei Guriev and Andrei Rachinsky (2005). The Role of Oligarchs in Russian Capitalism. \emph{Journal of Economic Perspectives} 19(1). doi:10.1257/0895330053147994.  
                                                                                                                                      ^
Warning 12 in papers/latex/financial-power.tex line 710: Interword spacing (`\ ') should perhaps be used.
Stephen Haber and Victor Menaldo (2011). Do Natural Resources Fuel Authoritarianism? A Reappraisal of the Resource Curse. \emph{American Political Science Review} 105(1). doi:10.1017/S0003055410000584.  
                                                                                                                         ^
Warning 12 in papers/latex/financial-power.tex line 710: Interword spacing (`\ ') should perhaps be used.
Stephen Haber and Victor Menaldo (2011). Do Natural Resources Fuel Authoritarianism? A Reappraisal of the Resource Curse. \emph{American Political Science Review} 105(1). doi:10.1017/S0003055410000584.  
                                                                                                                                                                          ^
Warning 12 in papers/latex/financial-power.tex line 713: Interword spacing (`\ ') should perhaps be used.
Jacob S. Hacker and Paul Pierson (2010). \emph{Winner-Take-All Politics: How Washington Made the Rich Richer and Turned Its Back on the Middle Class}. Simon \& Schuster.  
                                        ^
Warning 12 in papers/latex/financial-power.tex line 716: Interword spacing (`\ ') should perhaps be used.
Richard L. Hall and Alan V. Deardorff (2006). Lobbying as Legislative Subsidy. \emph{American Political Science Review} 100(1). doi:10.1017/s0003055406062010.  
                                                                              ^
Warning 12 in papers/latex/financial-power.tex line 716: Interword spacing (`\ ') should perhaps be used.
Richard L. Hall and Alan V. Deardorff (2006). Lobbying as Legislative Subsidy. \emph{American Political Science Review} 100(1). doi:10.1017/s0003055406062010.  
                                                                                                                               ^
Warning 12 in papers/latex/financial-power.tex line 719: Interword spacing (`\ ') should perhaps be used.
Peter A. Hall and David Soskice (eds.) (2001). \emph{Varieties of Capitalism: The Institutional Foundations of Comparative Advantage}. Oxford University Press. doi:10.1093/0199247757.001.0001.  
                                              ^
Warning 12 in papers/latex/financial-power.tex line 719: Interword spacing (`\ ') should perhaps be used.
Peter A. Hall and David Soskice (eds.) (2001). \emph{Varieties of Capitalism: The Institutional Foundations of Comparative Advantage}. Oxford University Press. doi:10.1093/0199247757.001.0001.  
                                                                                                                                                               ^
Warning 12 in papers/latex/financial-power.tex line 722: Interword spacing (`\ ') should perhaps be used.
Joel S. Hellman (1998). Winners Take All: The Politics of Partial Reform in Postcommunist Transitions. \emph{World Politics} 50(2). doi:10.1017/s0043887100008091.  
                                                                                                      ^
Warning 12 in papers/latex/financial-power.tex line 722: Interword spacing (`\ ') should perhaps be used.
Joel S. Hellman (1998). Winners Take All: The Politics of Partial Reform in Postcommunist Transitions. \emph{World Politics} 50(2). doi:10.1017/s0043887100008091.  
                                                                                                                                   ^
Warning 12 in papers/latex/financial-power.tex line 731: Interword spacing (`\ ') should perhaps be used.
Steffen Hertog (2010). \emph{Princes, Brokers, and Bureaucrats: Oil and the State in Saudi Arabia}. Cornell University Press. doi:10.7591/9780801458774.  
                      ^
Warning 12 in papers/latex/financial-power.tex line 731: Interword spacing (`\ ') should perhaps be used.
Steffen Hertog (2010). \emph{Princes, Brokers, and Bureaucrats: Oil and the State in Saudi Arabia}. Cornell University Press. doi:10.7591/9780801458774.  
                                                                                                                             ^
Warning 12 in papers/latex/financial-power.tex line 734: Interword spacing (`\ ') should perhaps be used.
Albert O. Hirschman (1964). The Paternity of an Index. \emph{American Economic Review} 54(5).  
                                                      ^
Warning 12 in papers/latex/financial-power.tex line 737: Interword spacing (`\ ') should perhaps be used.
Philip T. Hoffman and Kathryn Norberg (eds.) (1994). \emph{Fiscal Crises, Liberty, and Representative Government, 1450-1789}. Stanford University Press. doi:10.1515/9781503619500.  
                                                    ^
Warning 8 in papers/latex/financial-power.tex line 737: Wrong length of dash may have been used.
Philip T. Hoffman and Kathryn Norberg (eds.) (1994). \emph{Fiscal Crises, Liberty, and Representative Government, 1450-1789}. Stanford University Press. doi:10.1515/9781503619500.  
                                                                                                                      ^
Warning 12 in papers/latex/financial-power.tex line 737: Interword spacing (`\ ') should perhaps be used.
Philip T. Hoffman and Kathryn Norberg (eds.) (1994). \emph{Fiscal Crises, Liberty, and Representative Government, 1450-1789}. Stanford University Press. doi:10.1515/9781503619500.  
                                                                                                                                                        ^
Warning 12 in papers/latex/financial-power.tex line 740: Interword spacing (`\ ') should perhaps be used.
Philip T. Hoffman, Gilles Postel-Vinay, and Jean-Laurent Rosenthal (2000). \emph{Priceless Markets: The Political Economy of Credit in Paris, 1660-1870}. University of Chicago Press.  
                                                                          ^
Warning 8 in papers/latex/financial-power.tex line 740: Wrong length of dash may have been used.
Philip T. Hoffman, Gilles Postel-Vinay, and Jean-Laurent Rosenthal (2000). \emph{Priceless Markets: The Political Economy of Credit in Paris, 1660-1870}. University of Chicago Press.  
                                                                                                                                                  ^
Warning 13 in papers/latex/financial-power.tex line 743: Intersentence spacing (`\@') should perhaps be used.
Peter H\"ogfeldt (2005). The History and Politics of Corporate Ownership in Sweden. In \emph{A History of Corporate Governance around the World}, edited by Randall K. Morck, University of Chicago Press / NBER.  
                                                                                                                                                                                                                ^
Warning 12 in papers/latex/financial-power.tex line 746: Interword spacing (`\ ') should perhaps be used.
Deniz Igan, Prachi Mishra, and Thierry Tressel (2012). A Fistful of Dollars: Lobbying and the Financial Crisis. \emph{NBER Macroeconomics Annual} 26.  
                                                                                                               ^
Warning 12 in papers/latex/financial-power.tex line 749: Interword spacing (`\ ') should perhaps be used.
Joshua L. Kalla and David E. Broockman (2016). Campaign Contributions Facilitate Access to Congressional Officials: A Randomized Field Experiment. \emph{American Journal of Political Science} 60(3). doi:10.1111/ajps.12180.  
                                                                                                                                                  ^
Warning 12 in papers/latex/financial-power.tex line 749: Interword spacing (`\ ') should perhaps be used.
Joshua L. Kalla and David E. Broockman (2016). Campaign Contributions Facilitate Access to Congressional Officials: A Randomized Field Experiment. \emph{American Journal of Political Science} 60(3). doi:10.1111/ajps.12180.  
                                                                                                                                                                                                      ^
Warning 8 in papers/latex/financial-power.tex line 752: Wrong length of dash may have been used.
K. K{\i}van\c{c} Karaman and \c{S}evket Pamuk (2010). Ottoman State Finances in European Perspective, 1500-1914. \emph{The Journal of Economic History} 70(3). doi:10.1017/s0022050710000550.  
                                                                                                          ^
Warning 12 in papers/latex/financial-power.tex line 752: Interword spacing (`\ ') should perhaps be used.
K. K{\i}van\c{c} Karaman and \c{S}evket Pamuk (2010). Ottoman State Finances in European Perspective, 1500-1914. \emph{The Journal of Economic History} 70(3). doi:10.1017/s0022050710000550.  
                                                                                                                ^
Warning 12 in papers/latex/financial-power.tex line 752: Interword spacing (`\ ') should perhaps be used.
K. K{\i}van\c{c} Karaman and \c{S}evket Pamuk (2010). Ottoman State Finances in European Perspective, 1500-1914. \emph{The Journal of Economic History} 70(3). doi:10.1017/s0022050710000550.  
                                                                                                                                                              ^
Warning 12 in papers/latex/financial-power.tex line 755: Interword spacing (`\ ') should perhaps be used.
K. K{\i}van\c{c} Karaman and \c{S}evket Pamuk (2013). Different Paths to the Modern State in Europe: The Interaction between Warfare, Economic Structure, and Political Regime. \emph{American Political Science Review} 107(3). doi:10.1017/S0003055413000312.  
                                                                                                                                                                               ^
Warning 12 in papers/latex/financial-power.tex line 755: Interword spacing (`\ ') should perhaps be used.
K. K{\i}van\c{c} Karaman and \c{S}evket Pamuk (2013). Different Paths to the Modern State in Europe: The Interaction between Warfare, Economic Structure, and Political Regime. \emph{American Political Science Review} 107(3). doi:10.1017/S0003055413000312.  
                                                                                                                                                                                                                                ^
Warning 12 in papers/latex/financial-power.tex line 758: Interword spacing (`\ ') should perhaps be used.
Daniel Kaufmann, Aart Kraay, and Massimo Mastruzzi (2010). The Worldwide Governance Indicators: Methodology and Analytical Issues. \emph{Hague Journal on the Rule of Law} 3(2). doi:10.1017/S1876404511200046.  
                                                                                                                                  ^
Warning 12 in papers/latex/financial-power.tex line 758: Interword spacing (`\ ') should perhaps be used.
Daniel Kaufmann, Aart Kraay, and Massimo Mastruzzi (2010). The Worldwide Governance Indicators: Methodology and Analytical Issues. \emph{Hague Journal on the Rule of Law} 3(2). doi:10.1017/S1876404511200046.  
                                                                                                                                                                                ^
Warning 12 in papers/latex/financial-power.tex line 761: Interword spacing (`\ ') should perhaps be used.
Robert L. Kelly (1995). \emph{The Foraging Spectrum: Diversity in Hunter-Gatherer Lifeways}. Smithsonian Institution Press. doi:10.2307/j.ctv2sx9gc9.  
                       ^
Warning 12 in papers/latex/financial-power.tex line 761: Interword spacing (`\ ') should perhaps be used.
Robert L. Kelly (1995). \emph{The Foraging Spectrum: Diversity in Hunter-Gatherer Lifeways}. Smithsonian Institution Press. doi:10.2307/j.ctv2sx9gc9.  
                                                                                                                           ^
Warning 12 in papers/latex/financial-power.tex line 764: Interword spacing (`\ ') should perhaps be used.
Asim Ijaz Khwaja and Atif Mian (2005). Do Lenders Favor Politically Connected Firms? Rent Provision in an Emerging Financial Market. \emph{Quarterly Journal of Economics} 120(4). doi:10.1162/003355305775097524.  
                                                                                                                                    ^
Warning 12 in papers/latex/financial-power.tex line 764: Interword spacing (`\ ') should perhaps be used.
Asim Ijaz Khwaja and Atif Mian (2005). Do Lenders Favor Politically Connected Firms? Rent Provision in an Emerging Financial Market. \emph{Quarterly Journal of Economics} 120(4). doi:10.1162/003355305775097524.  
                                                                                                                                                                                  ^
Warning 12 in papers/latex/financial-power.tex line 767: Interword spacing (`\ ') should perhaps be used.
Craig R. Koester (2014). \emph{Revelation: A New Translation with Introduction and Commentary}. Yale University Press (Anchor Yale Bible 38A). doi:10.12987/9780300211030.  
                        ^
Warning 12 in papers/latex/financial-power.tex line 767: Interword spacing (`\ ') should perhaps be used.
Craig R. Koester (2014). \emph{Revelation: A New Translation with Introduction and Commentary}. Yale University Press (Anchor Yale Bible 38A). doi:10.12987/9780300211030.  
                                                                                                                                              ^
Warning 12 in papers/latex/financial-power.tex line 770: Interword spacing (`\ ') should perhaps be used.
J\'anos Kornai (1986). The Soft Budget Constraint. \emph{Kyklos} 39(1). doi:10.1111/j.1467-6435.1986.tb01252.x.  
                                                  ^
Warning 12 in papers/latex/financial-power.tex line 770: Interword spacing (`\ ') should perhaps be used.
J\'anos Kornai (1986). The Soft Budget Constraint. \emph{Kyklos} 39(1). doi:10.1111/j.1467-6435.1986.tb01252.x.  
                                                                       ^
Warning 8 in papers/latex/financial-power.tex line 770: Wrong length of dash may have been used.
J\'anos Kornai (1986). The Soft Budget Constraint. \emph{Kyklos} 39(1). doi:10.1111/j.1467-6435.1986.tb01252.x.  
                                                                                          ^
Warning 12 in papers/latex/financial-power.tex line 773: Interword spacing (`\ ') should perhaps be used.
J\'anos Kornai (1992). \emph{The Socialist System: The Political Economy of Communism}. Princeton University Press. doi:10.2307/j.ctv1ddczdr.  
                      ^
Warning 12 in papers/latex/financial-power.tex line 773: Interword spacing (`\ ') should perhaps be used.
J\'anos Kornai (1992). \emph{The Socialist System: The Political Economy of Communism}. Princeton University Press. doi:10.2307/j.ctv1ddczdr.  
                                                                                                                   ^
Warning 12 in papers/latex/financial-power.tex line 776: Interword spacing (`\ ') should perhaps be used.
Walter Korpi (1983). \emph{The Democratic Class Struggle}. Routledge \& Kegan Paul.  
                    ^
Warning 12 in papers/latex/financial-power.tex line 779: Interword spacing (`\ ') should perhaps be used.
J. Nelson Kraybill (1996). \emph{Imperial Cult and Commerce in John's Apocalypse}. Sheffield Academic Press (JSNT Supplement 132).  
                          ^
Warning 12 in papers/latex/financial-power.tex line 782: Interword spacing (`\ ') should perhaps be used.
Anne O. Krueger (1974). The Political Economy of the Rent-Seeking Society. \emph{American Economic Review} 64(3).  
                                                                          ^
Warning 12 in papers/latex/financial-power.tex line 785: Interword spacing (`\ ') should perhaps be used.
Timur Kuran (2001). The Provision of Public Goods under Islamic Law: Origins, Impact, and Limitations of the Waqf System. \emph{Law \& Society Review} 35(4). doi:10.2307/3185418.  
                                                                                                                         ^
Warning 12 in papers/latex/financial-power.tex line 785: Interword spacing (`\ ') should perhaps be used.
Timur Kuran (2001). The Provision of Public Goods under Islamic Law: Origins, Impact, and Limitations of the Waqf System. \emph{Law \& Society Review} 35(4). doi:10.2307/3185418.  
                                                                                                                                                             ^
Warning 12 in papers/latex/financial-power.tex line 788: Interword spacing (`\ ') should perhaps be used.
Timur Kuran (2004). Why the Middle East Is Economically Underdeveloped: Historical Mechanisms of Institutional Stagnation. \emph{Journal of Economic Perspectives} 18(3). doi:10.1257/0895330042162421.  
                                                                                                                          ^
Warning 12 in papers/latex/financial-power.tex line 788: Interword spacing (`\ ') should perhaps be used.
Timur Kuran (2004). Why the Middle East Is Economically Underdeveloped: Historical Mechanisms of Institutional Stagnation. \emph{Journal of Economic Perspectives} 18(3). doi:10.1257/0895330042162421.  
                                                                                                                                                                         ^
Warning 12 in papers/latex/financial-power.tex line 791: Interword spacing (`\ ') should perhaps be used.
Timur Kuran (2011). \emph{The Long Divergence: How Islamic Law Held Back the Middle East}. Princeton University Press. doi:10.1515/9781400836017.  
                   ^
Warning 12 in papers/latex/financial-power.tex line 791: Interword spacing (`\ ') should perhaps be used.
Timur Kuran (2011). \emph{The Long Divergence: How Islamic Law Held Back the Middle East}. Princeton University Press. doi:10.1515/9781400836017.  
                                                                                                                      ^
Warning 12 in papers/latex/financial-power.tex line 794: Interword spacing (`\ ') should perhaps be used.
Ahmet T. Kuru (2019). \emph{Islam, Authoritarianism, and Underdevelopment: A Global and Historical Comparison}. Cambridge University Press. doi:10.1017/9781108296892.  
                     ^
Warning 12 in papers/latex/financial-power.tex line 794: Interword spacing (`\ ') should perhaps be used.
Ahmet T. Kuru (2019). \emph{Islam, Authoritarianism, and Underdevelopment: A Global and Historical Comparison}. Cambridge University Press. doi:10.1017/9781108296892.  
                                                                                                                                           ^
Warning 12 in papers/latex/financial-power.tex line 797: Interword spacing (`\ ') should perhaps be used.
Michael Kwass (2000). \emph{Privilege and the Politics of Taxation in Eighteenth-Century France}. Cambridge University Press.  
                     ^
Warning 12 in papers/latex/financial-power.tex line 800: Interword spacing (`\ ') should perhaps be used.
Rafael La Porta, Florencio L\'opez-de-Silanes, and Andrei Shleifer (2002). Government Ownership of Banks. \emph{The Journal of Finance} 57(1). doi:10.1111/1540-6261.00422.  
                                                                                                         ^
Warning 12 in papers/latex/financial-power.tex line 800: Interword spacing (`\ ') should perhaps be used.
Rafael La Porta, Florencio L\'opez-de-Silanes, and Andrei Shleifer (2002). Government Ownership of Banks. \emph{The Journal of Finance} 57(1). doi:10.1111/1540-6261.00422.  
                                                                                                                                              ^
Warning 8 in papers/latex/financial-power.tex line 800: Wrong length of dash may have been used.
Rafael La Porta, Florencio L\'opez-de-Silanes, and Andrei Shleifer (2002). Government Ownership of Banks. \emph{The Journal of Finance} 57(1). doi:10.1111/1540-6261.00422.  
                                                                                                                                                               ^
Warning 12 in papers/latex/financial-power.tex line 803: Interword spacing (`\ ') should perhaps be used.
Jean-Jacques Laffont and Jean Tirole (1991). The Politics of Government Decision-Making: A Theory of Regulatory Capture. \emph{The Quarterly Journal of Economics} 106(4). doi:10.2307/2937958.  
                                                                                                                        ^
Warning 12 in papers/latex/financial-power.tex line 803: Interword spacing (`\ ') should perhaps be used.
Jean-Jacques Laffont and Jean Tirole (1991). The Politics of Government Decision-Making: A Theory of Regulatory Capture. \emph{The Quarterly Journal of Economics} 106(4). doi:10.2307/2937958.  
                                                                                                                                                                          ^
Warning 12 in papers/latex/financial-power.tex line 806: Interword spacing (`\ ') should perhaps be used.
Nicholas R. Lardy (2014). \emph{Markets over Mao: The Rise of Private Business in China}. Peterson Institute for International Economics.  
                         ^
Warning 12 in papers/latex/financial-power.tex line 812: Interword spacing (`\ ') should perhaps be used.
Alena V. Ledeneva (1998). \emph{Russia's Economy of Favours: Blat, Networking and Informal Exchange}. Cambridge University Press.  
                         ^
Warning 12 in papers/latex/financial-power.tex line 815: Interword spacing (`\ ') should perhaps be used.
Richard B. Lee (1979). \emph{The !Kung San: Men, Women, and Work in a Foraging Society}. Cambridge University Press.  
                      ^
Warning 26 in papers/latex/financial-power.tex line 815: You ought to remove spaces in front of punctuation.
Richard B. Lee (1979). \emph{The !Kung San: Men, Women, and Work in a Foraging Society}. Cambridge University Press.  
                                ^
Warning 12 in papers/latex/financial-power.tex line 818: Interword spacing (`\ ') should perhaps be used.
Richard B. Lee (2013). \emph{The Dobe Ju/'hoansi (4th edition)}. Wadsworth/Cengage Learning.  
                      ^
Warning 12 in papers/latex/financial-power.tex line 821: Interword spacing (`\ ') should perhaps be used.
Margaret Levi (1988). \emph{Of Rule and Revenue}. University of California Press. doi:10.1525/9780520909540.  
                     ^
Warning 12 in papers/latex/financial-power.tex line 821: Interword spacing (`\ ') should perhaps be used.
Margaret Levi (1988). \emph{Of Rule and Revenue}. University of California Press. doi:10.1525/9780520909540.  
                                                                                 ^
Warning 12 in papers/latex/financial-power.tex line 824: Interword spacing (`\ ') should perhaps be used.
Charles E. Lindblom (1977). \emph{Politics and Markets: The World's Political-Economic Systems}. Basic Books.  
                           ^
Warning 12 in papers/latex/financial-power.tex line 848: Interword spacing (`\ ') should perhaps be used.
Suzanne Maloney (2015). \emph{Iran's Political Economy since the Revolution}. Cambridge University Press. doi:10.1017/cbo9781139023276.  
                       ^
Warning 12 in papers/latex/financial-power.tex line 848: Interword spacing (`\ ') should perhaps be used.
Suzanne Maloney (2015). \emph{Iran's Political Economy since the Revolution}. Cambridge University Press. doi:10.1017/cbo9781139023276.  
                                                                                                         ^
Warning 12 in papers/latex/financial-power.tex line 851: Interword spacing (`\ ') should perhaps be used.
Michael Mann (1986). \emph{The Sources of Social Power, Volume 1: A History of Power from the Beginning to A.D. 1760}. Cambridge University Press. doi:10.1017/CBO9780511570896.  
                    ^
Warning 12 in papers/latex/financial-power.tex line 851: Interword spacing (`\ ') should perhaps be used.
Michael Mann (1986). \emph{The Sources of Social Power, Volume 1: A History of Power from the Beginning to A.D. 1760}. Cambridge University Press. doi:10.1017/CBO9780511570896.  
                                                                                                                                                  ^
Warning 12 in papers/latex/financial-power.tex line 854: Interword spacing (`\ ') should perhaps be used.
Lorna Marshall (1976). \emph{The !Kung of Nyae Nyae}. Harvard University Press. doi:10.4159/harvard.9780674180574.  
                      ^
Warning 26 in papers/latex/financial-power.tex line 854: You ought to remove spaces in front of punctuation.
Lorna Marshall (1976). \emph{The !Kung of Nyae Nyae}. Harvard University Press. doi:10.4159/harvard.9780674180574.  
                                ^
Warning 12 in papers/latex/financial-power.tex line 854: Interword spacing (`\ ') should perhaps be used.
Lorna Marshall (1976). \emph{The !Kung of Nyae Nyae}. Harvard University Press. doi:10.4159/harvard.9780674180574.  
                                                                               ^
Warning 12 in papers/latex/financial-power.tex line 857: Interword spacing (`\ ') should perhaps be used.
Bernard McGinn (1998). \emph{Antichrist: Two Thousand Years of the Human Fascination with Evil}. Columbia University Press.  
                      ^
Warning 12 in papers/latex/financial-power.tex line 860: Interword spacing (`\ ') should perhaps be used.
Robert K. Merton (1968). \emph{Social Theory and Social Structure (enlarged edition)}. Free Press.  
                        ^
Warning 12 in papers/latex/financial-power.tex line 863: Interword spacing (`\ ') should perhaps be used.
Atif Mian, Amir Sufi, and Francesco Trebbi (2010). The Political Economy of the US Mortgage Default Crisis. \emph{American Economic Review} 100(5). doi:10.1257/aer.100.5.1967.  
                                                                                                           ^
Warning 12 in papers/latex/financial-power.tex line 863: Interword spacing (`\ ') should perhaps be used.
Atif Mian, Amir Sufi, and Francesco Trebbi (2010). The Political Economy of the US Mortgage Default Crisis. \emph{American Economic Review} 100(5). doi:10.1257/aer.100.5.1967.  
                                                                                                                                                   ^
Warning 12 in papers/latex/financial-power.tex line 866: Interword spacing (`\ ') should perhaps be used.
Curtis J. Milhaupt and Wentong Zheng (2015). Beyond Ownership: State Capitalism and the Chinese Firm. \emph{Georgetown Law Journal} 103(3).  
                                                                                                     ^
Warning 12 in papers/latex/financial-power.tex line 869: Interword spacing (`\ ') should perhaps be used.
C. Wright Mills (1956). \emph{The Power Elite}. Oxford University Press.  
                       ^
Warning 12 in papers/latex/financial-power.tex line 872: Interword spacing (`\ ') should perhaps be used.
Mark S. Mizruchi (2013). \emph{The Fracturing of the American Corporate Elite}. Harvard University Press. doi:10.4159/harvard.9780674075368.  
                        ^
Warning 12 in papers/latex/financial-power.tex line 872: Interword spacing (`\ ') should perhaps be used.
Mark S. Mizruchi (2013). \emph{The Fracturing of the American Corporate Elite}. Harvard University Press. doi:10.4159/harvard.9780674075368.  
                                                                                                         ^
Warning 12 in papers/latex/financial-power.tex line 875: Interword spacing (`\ ') should perhaps be used.
Barry Naughton (2007). \emph{The Chinese Economy: Transitions and Growth}. MIT Press.  
                      ^
Warning 12 in papers/latex/financial-power.tex line 878: Interword spacing (`\ ') should perhaps be used.
Douglass C. North and Barry R. Weingast (1989). Constitutions and Commitment: The Evolution of Institutions Governing Public Choice in Seventeenth-Century England. \emph{The Journal of Economic History} 49(4). doi:10.1017/S0022050700009451.  
                                                                                                                                                                   ^
Warning 12 in papers/latex/financial-power.tex line 878: Interword spacing (`\ ') should perhaps be used.
Douglass C. North and Barry R. Weingast (1989). Constitutions and Commitment: The Evolution of Institutions Governing Public Choice in Seventeenth-Century England. \emph{The Journal of Economic History} 49(4). doi:10.1017/S0022050700009451.  
                                                                                                                                                                                                                 ^
Warning 12 in papers/latex/financial-power.tex line 881: Interword spacing (`\ ') should perhaps be used.
Douglass C. North, John Joseph Wallis, and Barry R. Weingast (2009). \emph{Violence and Social Orders: A Conceptual Framework for Interpreting Recorded Human History}. Cambridge University Press. doi:10.1017/CBO9780511575839.  
                                                                    ^
Warning 12 in papers/latex/financial-power.tex line 881: Interword spacing (`\ ') should perhaps be used.
Douglass C. North, John Joseph Wallis, and Barry R. Weingast (2009). \emph{Violence and Social Orders: A Conceptual Framework for Interpreting Recorded Human History}. Cambridge University Press. doi:10.1017/CBO9780511575839.  
                                                                                                                                                                                                   ^
Warning 12 in papers/latex/financial-power.tex line 884: Interword spacing (`\ ') should perhaps be used.
Mancur Olson (1965). \emph{The Logic of Collective Action: Public Goods and the Theory of Groups}. Harvard University Press. doi:10.4159/9780674041660.  
                    ^
Warning 12 in papers/latex/financial-power.tex line 884: Interword spacing (`\ ') should perhaps be used.
Mancur Olson (1965). \emph{The Logic of Collective Action: Public Goods and the Theory of Groups}. Harvard University Press. doi:10.4159/9780674041660.  
                                                                                                                            ^
Warning 12 in papers/latex/financial-power.tex line 887: Interword spacing (`\ ') should perhaps be used.
Elinor Ostrom (1990). \emph{Governing the Commons: The Evolution of Institutions for Collective Action}. Cambridge University Press. doi:10.1017/CBO9780511807763.  
                     ^
Warning 12 in papers/latex/financial-power.tex line 887: Interword spacing (`\ ') should perhaps be used.
Elinor Ostrom (1990). \emph{Governing the Commons: The Evolution of Institutions for Collective Action}. Cambridge University Press. doi:10.1017/CBO9780511807763.  
                                                                                                                                    ^
Warning 8 in papers/latex/financial-power.tex line 890: Wrong length of dash may have been used.
John F. Padgett and Christopher K. Ansell (1993). Robust Action and the Rise of the Medici, 1400-1434. \emph{American Journal of Sociology} 98(6). doi:10.1086/230190.  
                                                                                                ^
Warning 12 in papers/latex/financial-power.tex line 890: Interword spacing (`\ ') should perhaps be used.
John F. Padgett and Christopher K. Ansell (1993). Robust Action and the Rise of the Medici, 1400-1434. \emph{American Journal of Sociology} 98(6). doi:10.1086/230190.  
                                                                                                      ^
Warning 12 in papers/latex/financial-power.tex line 890: Interword spacing (`\ ') should perhaps be used.
John F. Padgett and Christopher K. Ansell (1993). Robust Action and the Rise of the Medici, 1400-1434. \emph{American Journal of Sociology} 98(6). doi:10.1086/230190.  
                                                                                                                                                  ^
Warning 12 in papers/latex/financial-power.tex line 893: Interword spacing (`\ ') should perhaps be used.
\c{S}evket Pamuk (2000). \emph{A Monetary History of the Ottoman Empire}. Cambridge University Press.  
                        ^
Warning 12 in papers/latex/financial-power.tex line 896: Interword spacing (`\ ') should perhaps be used.
Sam Peltzman (1976). Toward a More General Theory of Regulation. \emph{The Journal of Law and Economics} 19(2). doi:10.1086/466865.  
                                                                ^
Warning 12 in papers/latex/financial-power.tex line 896: Interword spacing (`\ ') should perhaps be used.
Sam Peltzman (1976). Toward a More General Theory of Regulation. \emph{The Journal of Law and Economics} 19(2). doi:10.1086/466865.  
                                                                                                               ^
Warning 12 in papers/latex/financial-power.tex line 899: Interword spacing (`\ ') should perhaps be used.
Thomas Piketty (2014). \emph{Capital in the Twenty-First Century}. Harvard University Press (Belknap). doi:10.4159/9780674982918.  
                      ^
Warning 12 in papers/latex/financial-power.tex line 899: Interword spacing (`\ ') should perhaps be used.
Thomas Piketty (2014). \emph{Capital in the Twenty-First Century}. Harvard University Press (Belknap). doi:10.4159/9780674982918.  
                                                                                                      ^
Warning 12 in papers/latex/financial-power.tex line 902: Interword spacing (`\ ') should perhaps be used.
Jonas Pontusson (1992). \emph{The Limits of Social Democracy: Investment Politics in Sweden}. Cornell University Press. doi:10.7591/9781501737541.  
                       ^
Warning 12 in papers/latex/financial-power.tex line 902: Interword spacing (`\ ') should perhaps be used.
Jonas Pontusson (1992). \emph{The Limits of Social Democracy: Investment Politics in Sweden}. Cornell University Press. doi:10.7591/9781501737541.  
                                                                                                                       ^
Warning 12 in papers/latex/financial-power.tex line 905: Interword spacing (`\ ') should perhaps be used.
Richard A. Posner (1975). The Social Costs of Monopoly and Regulation. \emph{Journal of Political Economy} 83(4). doi:10.1086/260357.  
                                                                      ^
Warning 12 in papers/latex/financial-power.tex line 905: Interword spacing (`\ ') should perhaps be used.
Richard A. Posner (1975). The Social Costs of Monopoly and Regulation. \emph{Journal of Political Economy} 83(4). doi:10.1086/260357.  
                                                                                                                 ^
Warning 12 in papers/latex/financial-power.tex line 908: Interword spacing (`\ ') should perhaps be used.
Paolo Prodi (1987). \emph{The Papal Prince: One Body and Two Souls: The Papal Monarchy in Early Modern Europe}. Cambridge University Press.  
                   ^
Warning 12 in papers/latex/financial-power.tex line 911: Interword spacing (`\ ') should perhaps be used.
Adam Przeworski (1985). \emph{Capitalism and Social Democracy}. Cambridge University Press. doi:10.1017/cbo9781139171830.  
                       ^
Warning 12 in papers/latex/financial-power.tex line 911: Interword spacing (`\ ') should perhaps be used.
Adam Przeworski (1985). \emph{Capitalism and Social Democracy}. Cambridge University Press. doi:10.1017/cbo9781139171830.  
                                                                                           ^
Warning 12 in papers/latex/financial-power.tex line 914: Interword spacing (`\ ') should perhaps be used.
Raghuram G. Rajan and Luigi Zingales (2003). The Great Reversals: The Politics of Financial Development in the Twentieth Century. \emph{Journal of Financial Economics} 69(1). doi:10.1016/S0304-405X(03)00125-9.  
                                                                                                                                 ^
Warning 12 in papers/latex/financial-power.tex line 914: Interword spacing (`\ ') should perhaps be used.
Raghuram G. Rajan and Luigi Zingales (2003). The Great Reversals: The Politics of Financial Development in the Twentieth Century. \emph{Journal of Financial Economics} 69(1). doi:10.1016/S0304-405X(03)00125-9.  
                                                                                                                                                                              ^
Warning 8 in papers/latex/financial-power.tex line 914: Wrong length of dash may have been used.
Raghuram G. Rajan and Luigi Zingales (2003). The Great Reversals: The Politics of Financial Development in the Twentieth Century. \emph{Journal of Financial Economics} 69(1). doi:10.1016/S0304-405X(03)00125-9.  
                                                                                                                                                                                                ^
Warning 36 in papers/latex/financial-power.tex line 914: You should put a space in front of parenthesis.
Raghuram G. Rajan and Luigi Zingales (2003). The Great Reversals: The Politics of Financial Development in the Twentieth Century. \emph{Journal of Financial Economics} 69(1). doi:10.1016/S0304-405X(03)00125-9.  
                                                                                                                                                                                                     ^
Warning 8 in papers/latex/financial-power.tex line 914: Wrong length of dash may have been used.
Raghuram G. Rajan and Luigi Zingales (2003). The Great Reversals: The Politics of Financial Development in the Twentieth Century. \emph{Journal of Financial Economics} 69(1). doi:10.1016/S0304-405X(03)00125-9.  
                                                                                                                                                                                                              ^
Warning 12 in papers/latex/financial-power.tex line 917: Interword spacing (`\ ') should perhaps be used.
Michael L. Ross (2001). Does Oil Hinder Democracy? \emph{World Politics} 53(3). doi:10.1353/wp.2001.0011.  
                                                                               ^
Warning 12 in papers/latex/financial-power.tex line 920: Interword spacing (`\ ') should perhaps be used.
Michael L. Ross (2012). \emph{The Oil Curse: How Petroleum Wealth Shapes the Development of Nations}. Princeton University Press. doi:10.1515/9781400841929.  
                       ^
Warning 12 in papers/latex/financial-power.tex line 920: Interword spacing (`\ ') should perhaps be used.
Michael L. Ross (2012). \emph{The Oil Curse: How Petroleum Wealth Shapes the Development of Nations}. Princeton University Press. doi:10.1515/9781400841929.  
                                                                                                                                 ^
Warning 12 in papers/latex/financial-power.tex line 923: Interword spacing (`\ ') should perhaps be used.
Barbara R. Rossing (1999). \emph{The Choice between Two Cities: Whore, Bride, and Empire in the Apocalypse}. Trinity Press International (Harvard Theological Studies 48).  
                          ^
Warning 12 in papers/latex/financial-power.tex line 926: Interword spacing (`\ ') should perhaps be used.
Jared Rubin (2017). \emph{Rulers, Religion, and Riches: Why the West Got Rich and the Middle East Did Not}. Cambridge University Press. doi:10.1017/9781139568272.  
                   ^
Warning 12 in papers/latex/financial-power.tex line 926: Interword spacing (`\ ') should perhaps be used.
Jared Rubin (2017). \emph{Rulers, Religion, and Riches: Why the West Got Rich and the Middle East Did Not}. Cambridge University Press. doi:10.1017/9781139568272.  
                                                                                                                                       ^
Warning 12 in papers/latex/financial-power.tex line 932: Interword spacing (`\ ') should perhaps be used.
Kenneth Scheve and David Stasavage (2016). \emph{Taxing the Rich: A History of Fiscal Fairness in the United States and Europe}. Princeton University Press. doi:10.1515/9781400880379.  
                                          ^
Warning 12 in papers/latex/financial-power.tex line 932: Interword spacing (`\ ') should perhaps be used.
Kenneth Scheve and David Stasavage (2016). \emph{Taxing the Rich: A History of Fiscal Fairness in the United States and Europe}. Princeton University Press. doi:10.1515/9781400880379.  
                                                                                                                                                            ^
Warning 12 in papers/latex/financial-power.tex line 935: Interword spacing (`\ ') should perhaps be used.
Andrei Shleifer and Robert W. Vishny (1994). Politicians and Firms. \emph{The Quarterly Journal of Economics} 109(4). doi:10.2307/2118354.  
                                                                   ^
Warning 12 in papers/latex/financial-power.tex line 935: Interword spacing (`\ ') should perhaps be used.
Andrei Shleifer and Robert W. Vishny (1994). Politicians and Firms. \emph{The Quarterly Journal of Economics} 109(4). doi:10.2307/2118354.  
                                                                                                                     ^
Warning 12 in papers/latex/financial-power.tex line 938: Interword spacing (`\ ') should perhaps be used.
Amy Singer (2008). \emph{Charity in Islamic Societies}. Cambridge University Press.  
                  ^
Warning 12 in papers/latex/financial-power.tex line 941: Interword spacing (`\ ') should perhaps be used.
George J. Stigler (1971). The Theory of Economic Regulation. \emph{The Bell Journal of Economics and Management Science} 2(1). doi:10.2307/3003160.  
                                                            ^
Warning 12 in papers/latex/financial-power.tex line 941: Interword spacing (`\ ') should perhaps be used.
George J. Stigler (1971). The Theory of Economic Regulation. \emph{The Bell Journal of Economics and Management Science} 2(1). doi:10.2307/3003160.  
                                                                                                                              ^
Warning 12 in papers/latex/financial-power.tex line 944: Interword spacing (`\ ') should perhaps be used.
Wolfgang Streeck (2014). \emph{Buying Time: The Delayed Crisis of Democratic Capitalism}. Verso.  
                        ^
Warning 12 in papers/latex/financial-power.tex line 947: Interword spacing (`\ ') should perhaps be used.
Charles Tilly (1990). \emph{Coercion, Capital, and European States, AD 990-1990}. Blackwell.  
                     ^
Warning 8 in papers/latex/financial-power.tex line 947: Wrong length of dash may have been used.
Charles Tilly (1990). \emph{Coercion, Capital, and European States, AD 990-1990}. Blackwell.  
                                                                          ^
Warning 32 in papers/latex/financial-power.tex line 950: Use ` to begin quotation, not '.
Daniel Treisman (2010). 'Loans for Shares' Revisited. \emph{Post-Soviet Affairs} 26(3). doi:10.2747/1060-586X.26.3.207.  
                        ^
Warning 12 in papers/latex/financial-power.tex line 950: Interword spacing (`\ ') should perhaps be used.
Daniel Treisman (2010). 'Loans for Shares' Revisited. \emph{Post-Soviet Affairs} 26(3). doi:10.2747/1060-586X.26.3.207.  
                                                     ^
Warning 12 in papers/latex/financial-power.tex line 950: Interword spacing (`\ ') should perhaps be used.
Daniel Treisman (2010). 'Loans for Shares' Revisited. \emph{Post-Soviet Affairs} 26(3). doi:10.2747/1060-586X.26.3.207.  
                                                                                       ^
Warning 8 in papers/latex/financial-power.tex line 950: Wrong length of dash may have been used.
Daniel Treisman (2010). 'Loans for Shares' Revisited. \emph{Post-Soviet Affairs} 26(3). doi:10.2747/1060-586X.26.3.207.  
                                                                                                        ^
Warning 12 in papers/latex/financial-power.tex line 953: Interword spacing (`\ ') should perhaps be used.
Gordon Tullock (1967). The Welfare Costs of Tariffs, Monopolies, and Theft. \emph{Western Economic Journal} 5(3). doi:10.1111/j.1465-7295.1967.tb01923.x.  
                                                                           ^
Warning 12 in papers/latex/financial-power.tex line 953: Interword spacing (`\ ') should perhaps be used.
Gordon Tullock (1967). The Welfare Costs of Tariffs, Monopolies, and Theft. \emph{Western Economic Journal} 5(3). doi:10.1111/j.1465-7295.1967.tb01923.x.  
                                                                                                                 ^
Warning 8 in papers/latex/financial-power.tex line 953: Wrong length of dash may have been used.
Gordon Tullock (1967). The Welfare Costs of Tariffs, Monopolies, and Theft. \emph{Western Economic Journal} 5(3). doi:10.1111/j.1465-7295.1967.tb01923.x.  
                                                                                                                                    ^
Warning 12 in papers/latex/financial-power.tex line 956: Interword spacing (`\ ') should perhaps be used.
Abraham L. Udovitch (1970). \emph{Partnership and Profit in Medieval Islam}. Princeton University Press. doi:10.1515/9781400820474.  
                           ^
Warning 12 in papers/latex/financial-power.tex line 956: Interword spacing (`\ ') should perhaps be used.
Abraham L. Udovitch (1970). \emph{Partnership and Profit in Medieval Islam}. Princeton University Press. doi:10.1515/9781400820474.  
                                                                                                        ^
Warning 8 in papers/latex/financial-power.tex line 959: Wrong length of dash may have been used.
Fran\c{c}ois R. Velde and David R. Weir (1992). The Financial Market and Government Debt Policy in France, 1746-1793. \emph{The Journal of Economic History} 52(1). doi:10.1017/s002205070001024x.  
                                                                                                               ^
Warning 12 in papers/latex/financial-power.tex line 959: Interword spacing (`\ ') should perhaps be used.
Fran\c{c}ois R. Velde and David R. Weir (1992). The Financial Market and Government Debt Policy in France, 1746-1793. \emph{The Journal of Economic History} 52(1). doi:10.1017/s002205070001024x.  
                                                                                                                     ^
Warning 12 in papers/latex/financial-power.tex line 959: Interword spacing (`\ ') should perhaps be used.
Fran\c{c}ois R. Velde and David R. Weir (1992). The Financial Market and Government Debt Policy in France, 1746-1793. \emph{The Journal of Economic History} 52(1). doi:10.1017/s002205070001024x.  
                                                                                                                                                                   ^
Warning 12 in papers/latex/financial-power.tex line 962: Interword spacing (`\ ') should perhaps be used.
Robert Vitalis (2007). \emph{America's Kingdom: Mythmaking on the Saudi Oil Frontier}. Stanford University Press. doi:10.1515/9781503626119.  
                      ^
Warning 12 in papers/latex/financial-power.tex line 962: Interword spacing (`\ ') should perhaps be used.
Robert Vitalis (2007). \emph{America's Kingdom: Mythmaking on the Saudi Oil Frontier}. Stanford University Press. doi:10.1515/9781503626119.  
                                                                                                                 ^
Warning 12 in papers/latex/financial-power.tex line 965: Interword spacing (`\ ') should perhaps be used.
Carl E. Walter and Fraser J. T. Howie (2011). \emph{Red Capitalism: The Fragile Financial Foundation of China's Extraordinary Rise}. Wiley. doi:10.1002/9781119199083.  
                                             ^
Warning 12 in papers/latex/financial-power.tex line 965: Interword spacing (`\ ') should perhaps be used.
Carl E. Walter and Fraser J. T. Howie (2011). \emph{Red Capitalism: The Fragile Financial Foundation of China's Extraordinary Rise}. Wiley. doi:10.1002/9781119199083.  
                                                                                                                                           ^
Warning 12 in papers/latex/financial-power.tex line 968: Interword spacing (`\ ') should perhaps be used.
Michael Walzer (1983). \emph{Spheres of Justice: A Defense of Pluralism and Equality}. Basic Books.  
                      ^
Warning 13 in papers/latex/financial-power.tex line 971: Intersentence spacing (`\@') should perhaps be used.
Frederic Wehrey, Jerrold D. Green, Brian Nichiporuk, Alireza Nader, Lydia Hansell, Rasool Nafisi, and S. R. Bohandy (2009). The Rise of the Pasdaran: Assessing the Domestic Roles of Iran's Islamic Revolutionary Guards Corps. RAND Corporation, MG-821-OSD.  
                                                                                                                                                                                                                                                             ^
Warning 12 in papers/latex/financial-power.tex line 974: Interword spacing (`\ ') should perhaps be used.
Polly Wiessner (2005). Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity? \emph{Human Nature} 16(2). doi:10.1007/s12110-005-1000-9.  
                                                                                                                              ^
Warning 8 in papers/latex/financial-power.tex line 974: Wrong length of dash may have been used.
Polly Wiessner (2005). Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity? \emph{Human Nature} 16(2). doi:10.1007/s12110-005-1000-9.  
                                                                                                                                                 ^
Warning 8 in papers/latex/financial-power.tex line 974: Wrong length of dash may have been used.
Polly Wiessner (2005). Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity? \emph{Human Nature} 16(2). doi:10.1007/s12110-005-1000-9.  
                                                                                                                                                     ^
Warning 8 in papers/latex/financial-power.tex line 974: Wrong length of dash may have been used.
Polly Wiessner (2005). Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity? \emph{Human Nature} 16(2). doi:10.1007/s12110-005-1000-9.  
                                                                                                                                                          ^
Warning 12 in papers/latex/financial-power.tex line 977: Interword spacing (`\ ') should perhaps be used.
Walter Wink (1992). \emph{Engaging the Powers: Discernment and Resistance in a World of Domination}. Fortress Press. doi:10.2307/j.ctt1tm7j16.  
                   ^
Warning 12 in papers/latex/financial-power.tex line 977: Interword spacing (`\ ') should perhaps be used.
Walter Wink (1992). \emph{Engaging the Powers: Discernment and Resistance in a World of Domination}. Fortress Press. doi:10.2307/j.ctt1tm7j16.  
                                                                                                                    ^
Warning 12 in papers/latex/financial-power.tex line 980: Interword spacing (`\ ') should perhaps be used.
Jeffrey A. Winters (2011). \emph{Oligarchy}. Cambridge University Press. doi:10.1017/cbo9780511793806.  
                          ^
Warning 12 in papers/latex/financial-power.tex line 980: Interword spacing (`\ ') should perhaps be used.
Jeffrey A. Winters (2011). \emph{Oligarchy}. Cambridge University Press. doi:10.1017/cbo9780511793806.  
                                                                        ^
Warning 12 in papers/latex/financial-power.tex line 983: Interword spacing (`\ ') should perhaps be used.
James Woodburn (1982). Egalitarian Societies. \emph{Man (N.S.)} 17(3). doi:10.2307/2801707.  
                                             ^
Warning 12 in papers/latex/financial-power.tex line 983: Interword spacing (`\ ') should perhaps be used.
James Woodburn (1982). Egalitarian Societies. \emph{Man (N.S.)} 17(3). doi:10.2307/2801707.  
                                                                      ^
Warning 17 in papers/latex/financial-power.tex line 987: Number of `(' doesn't match the number of `)'!


Warning 17 in papers/latex/financial-power.tex line 987: Number of `[' doesn't match the number of `]'!



hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "chktex -q papers/latex/financial-power.tex 2>&1 | sed -n 's/"'^Warning '"\\([0-9][0-9]*\\).*/\\1/p' | sort -n | uniq -c" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   1 1
   1 2
  14 3
  20 8
   4 9
 207 12
   5 13
   2 17
  29 24
   3 26
   1 32
   2 36
   3 38

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'chktex -q -n3 -n8 -n9 -n12 -n17 -n24 papers/latex/financial-power.tex' in /Users/mlong/Documents/Development/the-beast-system
 exited 2 in 0ms:
Warning 13 in papers/latex/financial-power.tex line 106: Intersentence spacing (`\@') should perhaps be used.
Scarcity in this sense is relative to claims, not absolute. A group can be materially comfortable and still face conflicts, because the meat of one animal, the best grazing in a dry season, or the revenue of one year is claimed by more people, or for more purposes, than it can satisfy. This is the scarcity axiom of the series (Ax1: resources are finite and claims on them conflict), whose general statement and refinement belong to Part VII.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                          ^
Warning 2 in papers/latex/financial-power.tex line 157: Non-breaking space (`~') should have been used.
which is \eqref{eq:aggregation-gap}. Each variance is nonnegative and vanishes exactly when $s^k_i=\bar s_i$ for every $k$ with $\beta_k>0$.  
        ^
Warning 36 in papers/latex/financial-power.tex line 215: You should put a space in front of parenthesis.
Suppose, purely for illustration, that a band of foragers meets a conflict over some good in at least one week in ten ($p=0.1$), and that each unsettled conflict carries a five percent chance of permanent fission or lethal violence ($q=0.05$). If the band had no settlement procedure at all, \cref{prop:financial-power:necessity}(c) bounds its probability of surviving ten years ($T=520$ weeks) by $0.95^{26}+e^{-6.5}\approx 0.265$, and of surviving fifty years ($T=2600$) by $0.95^{130}+e^{-32.5}\approx 0.0013$. The parameters are invented; the geometric decay is not.  
                                                                                                                                                                                                                                                                                                                                         ^
Warning 26 in papers/latex/financial-power.tex line 230: You ought to remove spaces in front of punctuation.
Woodburn's comparison of immediate-return societies, including the Hadza, Mbuti, !Kung, and Batek, generalizes the point. These societies avoid storage and accumulation, make sharing obligatory, and maintain what Woodburn calls leveling mechanisms that prevent any member from converting a temporary advantage into lasting control \citep{woodburn1982}. The equality of these societies is an outcome that institutions produce and defend, not the absence of institutions. Boehm reaches the same conclusion from a broader comparative sample of foragers: egalitarian bands sustain equality through a reverse dominance hierarchy in which the group collectively sanctions would-be dominants, and enforcement of meat-sharing against hoarders is one of its recurring targets \citep{boehm1999}.  
                                                                                ^
Warning 38 in papers/latex/financial-power.tex line 260: You should not use punctuation in front of quotes.
A second attempt appeals to markets. In a pure market economy, on this view, nobody allocates: prices do. But prices settle conflicts only against a background of property rules that say who may sell what, and those rules are made, interpreted, and enforced by other pillars. Allocation by price is a settlement procedure of the property-and-exchange mode, and control shares in it are given by the distribution of endowments. The market answer to the guiding question is ``whoever owns,'' which is an answer, not a dissolution of the question.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ^
Warning 38 in papers/latex/financial-power.tex line 536: You should not use punctuation in front of quotes.
Two passages bear on the financial pillar. The first is Revelation 13:16-17: ``And he causeth all, both small and great, rich and poor, free and bond, to receive a mark in their right hand, or in their foreheads: And that no man might buy or sell, save he that had the mark, or the name of the beast, or the number of his name.'' The image is economic participation conditioned on allegiance. In the vocabulary of this paper, it describes a financial pillar whose settlement procedure for exchange is gated by a test of loyalty administered by the ideological pillar: the coupling $C_{\pF\pI}$ is complete, and contestability for those who fail the test is zero. Part VI formalizes the same condition from the producers' side as a participation gate, access to exchange conditional on allegiance, and treats the passage as its limiting case (Definition 6.7 and Proposition 6.8 of \citealt{long2026productive}). Kraybill reads the passage against the participation of Asian merchants and artisans in trade guilds whose life was bound up with the imperial cult, so that commerce required at least tacit participation in worship \citep{kraybill1996}.  
                                                                                                                                                                                                                                                                                                                                      ^
Warning 38 in papers/latex/financial-power.tex line 540: You should not use punctuation in front of quotes.
The typological reading names the condition under which the series' structural claim acquires moral weight. The text does not condemn the existence of buying and selling; it condemns a configuration in which access to exchange depends on allegiance and the city's wealth depends on extraction and the trade in persons. That configuration is Proposition~B, the contingent capture of the financial pillar by a coalition that has also captured belief and coercion, not Proposition~A, the existence of an allocation function. The call of Revelation 18:4, ``Come out of her, my people,'' is in this reading an image of exit, one of the checks that Part VI treats. Wink's theology of the powers draws the same distinction: institutions are necessary to human life, become a system of domination when organized around it, and remain open to transformation \citep{wink1992}. The mapping from text to model is an interpretive claim of this series, offered as an aid to comparison; it is not a settled exegetical result. Collins's argument that Revelation responds to a crisis perceived by its author and audience, rather than to an empirically general persecution \citep{collins1984}, is a reminder that the text's images express a judgment about an order, which a comparative political economy cannot simply import as evidence.  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ^
Warning 1 in papers/latex/financial-power.tex line 566: Command terminated with space.
\raggedright  
            ^
Warning 13 in papers/latex/financial-power.tex line 638: Intersentence spacing (`\@') should perhaps be used.
James Conklin (1998). The Theory of Sovereign Debt and Spain under Philip II. \emph{Journal of Political Economy} 106(3). doi:10.1086/250019.  
                                                                            ^
Warning 13 in papers/latex/financial-power.tex line 659: Intersentence spacing (`\@') should perhaps be used.
Mauricio Drelichman and Hans-Joachim Voth (2011). Lending to the Borrower from Hell: Debt and Default in the Age of Philip II. \emph{The Economic Journal} 121(557). doi:10.1111/j.1468-0297.2011.02442.x.  
                                                                                                                             ^
Warning 13 in papers/latex/financial-power.tex line 743: Intersentence spacing (`\@') should perhaps be used.
Peter H\"ogfeldt (2005). The History and Politics of Corporate Ownership in Sweden. In \emph{A History of Corporate Governance around the World}, edited by Randall K. Morck, University of Chicago Press / NBER.  
                                                                                                                                                                                                                ^
Warning 26 in papers/latex/financial-power.tex line 815: You ought to remove spaces in front of punctuation.
Richard B. Lee (1979). \emph{The !Kung San: Men, Women, and Work in a Foraging Society}. Cambridge University Press.  
                                ^
Warning 26 in papers/latex/financial-power.tex line 854: You ought to remove spaces in front of punctuation.
Lorna Marshall (1976). \emph{The !Kung of Nyae Nyae}. Harvard University Press. doi:10.4159/harvard.9780674180574.  
                                ^
Warning 36 in papers/latex/financial-power.tex line 914: You should put a space in front of parenthesis.
Raghuram G. Rajan and Luigi Zingales (2003). The Great Reversals: The Politics of Financial Development in the Twentieth Century. \emph{Journal of Financial Economics} 69(1). doi:10.1016/S0304-405X(03)00125-9.  
                                                                                                                                                                                                     ^
Warning 32 in papers/latex/financial-power.tex line 950: Use ` to begin quotation, not '.
Daniel Treisman (2010). 'Loans for Shares' Revisited. \emph{Post-Soviet Affairs} 26(3). doi:10.2747/1060-586X.26.3.207.  
                        ^
Warning 13 in papers/latex/financial-power.tex line 971: Intersentence spacing (`\@') should perhaps be used.
Frederic Wehrey, Jerrold D. Green, Brian Nichiporuk, Alireza Nader, Lydia Hansell, Rasool Nafisi, and S. R. Bohandy (2009). The Rise of the Pasdaran: Assessing the Domestic Roles of Iran's Islamic Revolutionary Guards Corps. RAND Corporation, MG-821-OSD.  
                                                                                                                                                                                                                                                             ^

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "chktex -q papers/latex/financial-power.tex 2>&1 | sed -n 's/"'^Warning 8 in .* line '"\\([0-9][0-9]*\\):.*/\\1/p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
536
578
644
653
659
737
740
752
770
800
890
914
914
947
950
953
959
974
974
974

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '532,540p;574,580p;640,646p;649,660p;733,744p;748,754p;766,772p;796,802p;886,892p;910,916p;943,960p;970,976p' papers/latex/financial-power.tex | nl -ba" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	\label{sec:revelation}
     2	
     3	The series takes its name from Revelation 13, and its theological vocabulary is typological. The beast of Revelation 13 and the city of Babylon in chapters 17 and 18 are read as images of a recurring configuration of power that claims ultimate loyalty, not as predictions of a particular future state, person, or technology. This is one of several interpretive traditions. Preterist readings locate the text in its first-century setting and read the beast as Roman imperial power and the imperial cult of the province of Asia \citep{collins1984,kraybill1996}. Typological or idealist readings see Rome as a paradigm of a pattern that recurs \citep{bauckham1993}. Futurist readings identify the beast with a coming ruler or system; the history of such identifications is a history of failures, as McGinn and Fuller document \citep{mcginn1998,fuller1995}, and the series excludes them.
     4	
     5	Two passages bear on the financial pillar. The first is Revelation 13:16-17: ``And he causeth all, both small and great, rich and poor, free and bond, to receive a mark in their right hand, or in their foreheads: And that no man might buy or sell, save he that had the mark, or the name of the beast, or the number of his name.'' The image is economic participation conditioned on allegiance. In the vocabulary of this paper, it describes a financial pillar whose settlement procedure for exchange is gated by a test of loyalty administered by the ideological pillar: the coupling $C_{\pF\pI}$ is complete, and contestability for those who fail the test is zero. Part VI formalizes the same condition from the producers' side as a participation gate, access to exchange conditional on allegiance, and treats the passage as its limiting case (Definition 6.7 and Proposition 6.8 of \citealt{long2026productive}). Kraybill reads the passage against the participation of Asian merchants and artisans in trade guilds whose life was bound up with the imperial cult, so that commerce required at least tacit participation in worship \citep{kraybill1996}.
     6	
     7	The second is the lament over Babylon in Revelation 18. The merchants of the earth ``are waxed rich through the abundance of her delicacies'' (18:3), they weep ``for no man buyeth their merchandise any more'' (18:11), and the chapter's list of cargoes ends with ``slaves, and souls of men'' (18:13). Bauckham reads the chapter as an economic critique of Rome's trade empire, in which the wealth of the city depends on the extraction of goods from the provinces and the trade in persons is the last item of the list \citep{bauckham1991}. Koester and Aune give the philological and historical commentary \citep{koester2014,aune1998c}, and Rossing reads the chapter as a choice between two cities, Babylon and the new Jerusalem \citep{rossing1999}. The trade in slaves in 18:13 is literal: it refers to the Roman slave trade, and nothing in this reading equates it with wage labor, taxation, or other forms of economic dependence, which the series distinguishes from chattel slavery.
     8	
     9	The typological reading names the condition under which the series' structural claim acquires moral weight. The text does not condemn the existence of buying and selling; it condemns a configuration in which access to exchange depends on allegiance and the city's wealth depends on extraction and the trade in persons. That configuration is Proposition~B, the contingent capture of the financial pillar by a coalition that has also captured belief and coercion, not Proposition~A, the existence of an allocation function. The call of Revelation 18:4, ``Come out of her, my people,'' is in this reading an image of exit, one of the checks that Part VI treats. Wink's theology of the powers draws the same distinction: institutions are necessary to human life, become a system of domination when organized around it, and remain open to transformation \citep{wink1992}. The mapping from text to model is an interpretive claim of this series, offered as an aid to comparison; it is not a settled exegetical result. Collins's argument that Revelation responds to a crisis perceived by its author and audience, rather than to an empirically general persecution \citep{collins1984}, is a reminder that the text's images express a judgment about an order, which a comparative political economy cannot simply import as evidence.
    10	\bibitem[Ansolabehere et al.(2003)]{ansolabehere2003}
    11	Stephen Ansolabehere, John M. de Figueiredo, and James M. Snyder (2003). Why Is There So Little Money in U.S. Politics? \emph{Journal of Economic Perspectives} 17(1). doi:10.1257/089533003321164976.
    12	
    13	\bibitem[Aune(1998)]{aune1998c}
    14	David E. Aune (1998). \emph{Revelation 17-22}. Word Biblical Commentary 52C, Thomas Nelson.
    15	
    16	\bibitem[Bartels(2008)]{bartels2008}
    17	\bibitem[Coppedge et al.(2011)]{coppedge2011}
    18	Michael Coppedge, John Gerring, David Altman, Michael Bernhard, Steven Fish, Allen Hicken, Matthew Kroenig, Staffan I. Lindberg, Kelly McMann, Pamela Paxton, Holli A. Semetko, Svend-Erik Skaaning, Jeffrey Staton, and Jan Teorell (2011). Conceptualizing and Measuring Democracy: A New Approach. \emph{Perspectives on Politics} 9(2). doi:10.1017/S1537592711000880.
    19	
    20	\bibitem[Cox et al.(2010)]{cox2010}
    21	Michael Cox, Gwen Arnold, and Sergio Villamayor Tomas (2010). A Review of Design Principles for Community-based Natural Resource Management. \emph{Ecology and Society} 15(4). doi:10.5751/ES-03704-150438.
    22	
    23	\bibitem[Culpepper(2010)]{culpepper2010}
    24	\bibitem[Dal B\'o(2006)]{dalbo2006}
    25	Ernesto Dal B\'o (2006). Regulatory Capture: A Review. \emph{Oxford Review of Economic Policy} 22(2). doi:10.1093/oxrep/grj013.
    26	
    27	\bibitem[de Roover(1963)]{deroover1963}
    28	Raymond de Roover (1963). \emph{The Rise and Decline of the Medici Bank, 1397-1494}. Harvard University Press.
    29	
    30	\bibitem[Doyle(1996)]{doyle1996}
    31	William Doyle (1996). \emph{Venality: The Sale of Offices in Eighteenth-Century France}. Oxford University Press. doi:10.1093/acprof:oso/9780198205364.001.0001.
    32	
    33	\bibitem[Drelichman and Voth(2011)]{drelichman2011}
    34	Mauricio Drelichman and Hans-Joachim Voth (2011). Lending to the Borrower from Hell: Debt and Default in the Age of Philip II. \emph{The Economic Journal} 121(557). doi:10.1111/j.1468-0297.2011.02442.x.
    35	
    36	\bibitem[Hirschman(1964)]{hirschman1964}
    37	Albert O. Hirschman (1964). The Paternity of an Index. \emph{American Economic Review} 54(5).
    38	
    39	\bibitem[Hoffman and Norberg(1994)]{hoffmannorberg1994}
    40	Philip T. Hoffman and Kathryn Norberg (eds.) (1994). \emph{Fiscal Crises, Liberty, and Representative Government, 1450-1789}. Stanford University Press. doi:10.1515/9781503619500.
    41	
    42	\bibitem[Hoffman et al.(2000)]{hoffman2000}
    43	Philip T. Hoffman, Gilles Postel-Vinay, and Jean-Laurent Rosenthal (2000). \emph{Priceless Markets: The Political Economy of Credit in Paris, 1660-1870}. University of Chicago Press.
    44	
    45	\bibitem[H\"ogfeldt(2005)]{hogfeldt2005}
    46	Peter H\"ogfeldt (2005). The History and Politics of Corporate Ownership in Sweden. In \emph{A History of Corporate Governance around the World}, edited by Randall K. Morck, University of Chicago Press / NBER.
    47	
    48	\bibitem[Kalla and Broockman(2016)]{kalla2016}
    49	Joshua L. Kalla and David E. Broockman (2016). Campaign Contributions Facilitate Access to Congressional Officials: A Randomized Field Experiment. \emph{American Journal of Political Science} 60(3). doi:10.1111/ajps.12180.
    50	
    51	\bibitem[Karaman and Pamuk(2010)]{karaman2010}
    52	K. K{\i}van\c{c} Karaman and \c{S}evket Pamuk (2010). Ottoman State Finances in European Perspective, 1500-1914. \emph{The Journal of Economic History} 70(3). doi:10.1017/s0022050710000550.
    53	
    54	\bibitem[Karaman and Pamuk(2013)]{karaman2013}
    55	\bibitem[Koester(2014)]{koester2014}
    56	Craig R. Koester (2014). \emph{Revelation: A New Translation with Introduction and Commentary}. Yale University Press (Anchor Yale Bible 38A). doi:10.12987/9780300211030.
    57	
    58	\bibitem[Kornai(1986)]{kornai1986}
    59	J\'anos Kornai (1986). The Soft Budget Constraint. \emph{Kyklos} 39(1). doi:10.1111/j.1467-6435.1986.tb01252.x.
    60	
    61	\bibitem[Kornai(1992)]{kornai1992}
    62	\bibitem[Kwass(2000)]{kwass2000}
    63	Michael Kwass (2000). \emph{Privilege and the Politics of Taxation in Eighteenth-Century France}. Cambridge University Press.
    64	
    65	\bibitem[La Porta et al.(2002)]{laporta2002}
    66	Rafael La Porta, Florencio L\'opez-de-Silanes, and Andrei Shleifer (2002). Government Ownership of Banks. \emph{The Journal of Finance} 57(1). doi:10.1111/1540-6261.00422.
    67	
    68	\bibitem[Laffont and Tirole(1991)]{laffont1991}
    69	\bibitem[Ostrom(1990)]{ostrom1990}
    70	Elinor Ostrom (1990). \emph{Governing the Commons: The Evolution of Institutions for Collective Action}. Cambridge University Press. doi:10.1017/CBO9780511807763.
    71	
    72	\bibitem[Padgett and Ansell(1993)]{padgett1993}
    73	John F. Padgett and Christopher K. Ansell (1993). Robust Action and the Rise of the Medici, 1400-1434. \emph{American Journal of Sociology} 98(6). doi:10.1086/230190.
    74	
    75	\bibitem[Pamuk(2000)]{pamuk2000}
    76	\bibitem[Przeworski(1985)]{przeworski1985}
    77	Adam Przeworski (1985). \emph{Capitalism and Social Democracy}. Cambridge University Press. doi:10.1017/cbo9781139171830.
    78	
    79	\bibitem[Rajan and Zingales(2003)]{rajan2003}
    80	Raghuram G. Rajan and Luigi Zingales (2003). The Great Reversals: The Politics of Financial Development in the Twentieth Century. \emph{Journal of Financial Economics} 69(1). doi:10.1016/S0304-405X(03)00125-9.
    81	
    82	\bibitem[Ross(2001)]{ross2001}
    83	\bibitem[Streeck(2014)]{streeck2014}
    84	Wolfgang Streeck (2014). \emph{Buying Time: The Delayed Crisis of Democratic Capitalism}. Verso.
    85	
    86	\bibitem[Tilly(1990)]{tilly1990}
    87	Charles Tilly (1990). \emph{Coercion, Capital, and European States, AD 990-1990}. Blackwell.
    88	
    89	\bibitem[Treisman(2010)]{treisman2010}
    90	Daniel Treisman (2010). 'Loans for Shares' Revisited. \emph{Post-Soviet Affairs} 26(3). doi:10.2747/1060-586X.26.3.207.
    91	
    92	\bibitem[Tullock(1967)]{tullock1967}
    93	Gordon Tullock (1967). The Welfare Costs of Tariffs, Monopolies, and Theft. \emph{Western Economic Journal} 5(3). doi:10.1111/j.1465-7295.1967.tb01923.x.
    94	
    95	\bibitem[Udovitch(1970)]{udovitch1970}
    96	Abraham L. Udovitch (1970). \emph{Partnership and Profit in Medieval Islam}. Princeton University Press. doi:10.1515/9781400820474.
    97	
    98	\bibitem[Velde and Weir(1992)]{velde1992}
    99	Fran\c{c}ois R. Velde and David R. Weir (1992). The Financial Market and Government Debt Policy in France, 1746-1793. \emph{The Journal of Economic History} 52(1). doi:10.1017/s002205070001024x.
   100	
   101	\bibitem[Wehrey et al.(2009)]{wehrey2009}
   102	Frederic Wehrey, Jerrold D. Green, Brian Nichiporuk, Alireza Nader, Lydia Hansell, Rasool Nafisi, and S. R. Bohandy (2009). The Rise of the Pasdaran: Assessing the Domestic Roles of Iran's Islamic Revolutionary Guards Corps. RAND Corporation, MG-821-OSD.
   103	
   104	\bibitem[Wiessner(2005)]{wiessner2005}
   105	Polly Wiessner (2005). Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity? \emph{Human Nature} 16(2). doi:10.1007/s12110-005-1000-9.
   106	
   107	\bibitem[Wink(1992)]{wink1992}

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "perl -ne 'if(/\\\\\\[/){"'$on=1} if($on){printf "%5d %s",$.,$_} if(/'"\\\\\\]/){"'$on=0}'"' papers/latex/financial-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   57 \title{Financial Power and Resource Command\\[4pt]
   58   {\normalsize Part I of \emph{The Six Pillars of the Beast System}}}
   59 \author{Matthew Long\\
   60   \small The YonedaAI Collaboration, YonedaAI Research Collective\\
   61   \small Chicago, IL\\
   62   \small \texttt{matthew@yonedaai.com} \quad \url{https://yonedaai.com}}
   63 \date{October 2026}
   64 
   65 \begin{document}
   66 
   67 \maketitle
   68 
   69 \begin{abstract}
   70 Every governance system must settle conflicting claims on finite resources. This paper treats that settlement as the financial pillar of a six-function model of governance and asks who controls resources across regime types. From a scarcity axiom and an explicit assumption that unsettled conflicts carry a positive hazard of dissolution, we prove that a collective with no recognized allocation regularity cannot persist with probability bounded away from zero, and that in any collective that does persist the share of conflicts settled by such a regularity tends to one. The result concerns a function, not an institution: in foraging bands the regularity is a sharing norm, and control is dispersed close to the minimum concentration the index allows. We then prove that the necessity of the pillar places no restriction on its concentration or contestability, show that aggregating subdomains understates concentration by exactly the cross-domain variance of control shares, and derive conditional comparative statics under which resource holders convert wealth into influence over rules. A comparison of market-capitalist societies, communist party-states, social democracies, Islamic states, Catholic monarchies and secular democracies finds the same function held by different institutions, with documented capture episodes and documented checks in every type. Seven hypotheses with stated falsifiers make the capture claim testable. Revelation 13 and 18 are read typologically as images of economic participation conditioned on allegiance. The main limitation is that no coded cross-regime dataset yet exists, so the comparative claims remain qualitative.
   71 \end{abstract}
   72 
   73 \section{Introduction}
   74 \label{sec:intro}
   75 
   76 Every polity decides who controls its resources, whether or not it has a treasury, a bank, or a word for property. A foraging camp decides who carves the meat and who receives which portion. A pastoral lineage decides whose cattle pay a bridewealth or a blood debt. A medieval caliphate assigns revenues to a treasury and endowments to trustees, an early modern monarchy pledges future taxes to its bankers, a Soviet ministry allocates steel by plan, and a modern democracy delegates the supply of money to an independent central bank. The institutions differ almost completely. The problem they solve does not.
   77 
   78 This paper is the first of seven Parts of a series whose thesis is that the ideology of governance changes while its institutional functions remain. The series follows the framework of \citet{largo2026hbs}, which models a polity as a directed multiplex network whose layers record distinct mechanisms of constraint, and which asks when concentration and coordination across those layers turn into unaccountable domination. The series uses six pillars: financial power~$\pF$ (who controls the resources), political power~$\pP$ (who makes the laws), judicial power~$\pJ$ (who interprets them), ideological power~$\pI$ (who shapes beliefs), coercive power~$\pC$ (who enforces the rules), and productive power~$\pW$ (who produces the wealth that sustains everything). Part VII \citep{long2026formalized} proves the general claim, called Proposition~A, that every functioning governance system contains all six functions and the dependencies among them, and it proves that this structural necessity does not imply Proposition~B, the contingent and measurable claim that the functions have been captured by a coalition that escapes independent accountability.
   79 
   80 The financial pillar is the one most easily misread. Popular usage equates control of resources with capitalists, bankers, or a single class, and so treats the existence of the pillar as an accusation. The argument here runs the other way. Resource command exists in a hunter-gatherer camp, where it is held by everyone at once through sharing norms; what varies across polities is how concentrated it is, how contestable it is, and how tightly it is coupled to rule-making, adjudication, belief, coercion, and work. A theory that cannot separate the existence of the function from its concentration will find domination everywhere and therefore explain nothing.
   81 
   82 The necessity of the function and the contingency of its concentration can both be proved. From the scarcity axiom of the series and an explicit assumption that unsettled conflict risks dissolution, a collective with no recognized way of settling claims loses its chance of survival geometrically over time, and in a collective that survives almost every conflict is settled by such a procedure (\cref{prop:financial-power:necessity}). The same necessity places no restriction on how concentrated or contestable control is (\cref{prop:financial-power:nonimplication}); this is the pillar-level case of the non-implication that Part VII proves for all six pillars.
   83 
   84 Three further results make the comparison measurable. Aggregate concentration understates the concentration of subdomains such as credit, land, and the public budget by exactly the cross-domain variance of control shares (\cref{prop:financial-power:aggregation-gap}). A resource holder's investment in influence over other pillars rises with its share and falls with the contestability of the receiving pillar (\cref{prop:financial-power:influence}). And lenders to a sovereign are protected by the threat of exclusion from future credit, not by control of legislation, whenever the ruler's future need for credit is large enough (\cref{prop:financial-power:sovereign-credit}). The six regime types of the series are then compared with the same questions and the same standard of evidence, and seven hypotheses are stated together with the observations that would falsify them.
   85 
   86 Two scope commitments govern everything that follows. The phrase ``Beast System'' names the universal six-function structure that Part VII proves present in every governance system; it is never a label for a religion, a people, a profession, a regime, or a person. And the comparison asks how the universal function is distributed in each regime type, not whether a civilization ``has'' it. Because every type has it, the comparison is even-handed by construction, and the evidentiary burden falls entirely on claims of capture.
   87 
   88 \section{The financial pillar in the multiplex network}
   89 \label{sec:pillar}
   90 
   91 \subsection{Shared notation}
   92 
   93 The series inherits its formal objects from \citet{largo2026hbs} and does not redefine them. A polity at time~$t$ is a directed multiplex network $G_t=(V_t,E_t)$ whose nodes are organizations or coherent actor groups. Each pillar $m$ in the index set $\Pillars=\{\pF,\pP,\pJ,\pI,\pC,\pW\}$, with $M=|\Pillars|=6$, contributes a layer with adjacency $A^m_t$ and edge weights $a^m_{ij,t}\in[0,1]$ that record the documented capacity of actor~$i$ to constrain a feasible action of actor~$j$ through mechanism~$m$. A many-to-many role map assigns actors to pillars. Actor~$i$ holds a normalized share $s^m_{i,t}$ of decision-relevant control in pillar~$m$, with $\sum_i s^m_{i,t}=1$; concentration is the Herfindahl-Hirschman index $H_{m,t}=\sum_i (s^m_{i,t})^2$ \citep{hirschman1964}; contestability $Q_{m,t}\in[0,1]$ scores transparency, appeal rights, independence, competition, and credible replacement of decision makers. The illustrative index of unaccountable concentration is $U_t=\sum_m \omega_m H_{m,t}(1-Q_{m,t})$ with preregistered weights $\omega_m\geq 0$ summing to one.
   94 
   95 The remaining objects concern relations between pillars. Cross-pillar integration $C_{mn,t}\in[0,1]$ is the extent to which one coalition commands appointments, budgets, sanctions, or agenda in both $m$ and $n$, and the integration statistic is $\Integ_t=\tfrac{2}{M(M-1)}\sum_{m<n}C_{mn,t}$, the mean over the fifteen pillar pairs. A capture link $(i\to j,m)$ requires privileged access or discretion, a resulting weakening of applicable accountability or contestability, and material evidence tying the asymmetry to an institutional output. All of these objects are due to \citet{largo2026hbs}; the six-pillar version with fifteen pairs follows the series convention.
   96 
   97 The financial pillar corresponds to the source's resource function $R$: command over capital, land, credit, investment, infrastructure, public budgets, and strategic means of production. The source cautions that ownership, scale, or the administration of public goods is not by itself evidence of domination, and that in a party-state the resource function can sit under political authority \citep{largo2026hbs}. The label $\pF$ is written in sans-serif throughout so that it is never confused with the role map.
   98 
   99 \subsection{The allocation problem}
  100 
  101 \begin{definition}[Allocation problem]
  102 \label{def:financial-power:allocation-problem}
  103 Let $N$ be a collective of $n\geq 2$ members and $\mathcal{K}$ a finite set of goods, with available stock $\omega\in\mathbb{R}^{\mathcal{K}}_{+}$ at a given date. Each member $i$ holds a claim $c_i\in\mathbb{R}^{\mathcal{K}}_{+}$ on the stock. A \emph{conflict} occurs when the claims on some good $k$ are jointly infeasible, $\sum_{i\in N}c_{ik}>\omega_k$. An \emph{allocation problem} is the task of determining, for each conflict, which feasible assignment $x=(x_i)_{i\in N}$ with $\sum_i x_i\leq\omega$ prevails, together with the related decisions of who may use a good, who may store it, and what is held in reserve.
  104 \end{definition}
  105 
  106 Scarcity in this sense is relative to claims, not absolute. A group can be materially comfortable and still face conflicts, because the meat of one animal, the best grazing in a dry season, or the revenue of one year is claimed by more people, or for more purposes, than it can satisfy. This is the scarcity axiom of the series (Ax1: resources are finite and claims on them conflict), whose general statement and refinement belong to Part VII.
  107 
  108 \begin{definition}[Settlement]
  109 \label{def:financial-power:settlement}
  110 A conflict is \emph{settled} when it is resolved by a procedure that belongs to the collective's repertoire, meaning that (a) the procedure applies to a class of situations rather than to a single instance, (b) members can anticipate the resulting assignment from a description of the procedure and of the situation, and (c) members comply with the assignment or are held to it by others. A conflict resolved without such a procedure, by unregulated contest whose outcome depends on whoever prevails in the moment, is \emph{unsettled}. The \emph{financial pillar} of a collective is the set of procedures that settle its conflicts, together with the actors who operate them.
  111 \end{definition}
  112 
  113 The definition is deliberately broad on the side of form and narrow on the side of function. A sharing norm, an ownership rule with voluntary exchange, a plan target, a waqf deed, a credit contract, a lottery, and a ritualized contest with known rules all settle conflicts. A brawl over a carcass does not, unless brawls themselves follow rules that the parties recognize. The broad side guards against the error of identifying the function with one institution; the narrow side keeps the definition from being satisfied by anything whatever.
  114 
  115 \begin{definition}[Settlement modes]
  116 \label{def:financial-power:settlement-modes}
  117 A settlement procedure is classified by the source of the assignment it produces: a \emph{sharing norm} assigns goods by a rule of distribution binding on the holder; \emph{property and exchange} assigns goods by prior entitlement and voluntary transfer at agreed terms; \emph{command allocation} assigns goods by the decision of an office; an \emph{endowment} assigns the yield of a dedicated asset to stated purposes under a trustee; \emph{credit} assigns present goods against a promise of future repayment. Real procedures combine modes.
  118 \end{definition}
  119 
  120 The modes are a coding device, not a typology of societies. A Ju/'hoansi camp uses sharing norms and also recognizes ownership of arrows; a market economy uses property and exchange and also command allocation through public budgets; an Ottoman province combined command allocation, endowments, and tax farms that were a form of credit to the treasury.
  121 
  122 \begin{definition}[Allocation regime]
  123 \label{def:financial-power:allocation-regime}
  124 The \emph{allocation regime} of a polity at time $t$ is the tuple consisting of its settlement modes, the actors who hold control shares $s^{\pF}_{i,t}$ in them, the concentration $H_{\pF,t}$, the contestability $Q_{\pF,t}$, and the five couplings $C_{\pF n,t}$ for $n\in\{\pP,\pJ,\pI,\pC,\pW\}$.
  125 \end{definition}
  126 
  127 The control share $s^{\pF}_{i,t}$ is meant to be measured from documents rather than inferred from outcomes. Its observable components include asset shares, shares of bank credit, shares of output produced by state-owned enterprises, shares of the public budget under discretionary control, shares of procurement awards, and rights to collect rent or tribute. Contestability $Q_{\pF,t}$ is scored from open entry, competitive tendering, beneficial-ownership disclosure, independent audit, bankruptcy that actually binds, antitrust enforcement, and the independence of the monetary authority.
  128 
  129 \subsection{Concentration and its normalization}
  130 
  131 The index $H_{\pF,t}$ lies in $[1/n,1]$ for a polity of $n$ actors, with the lower bound attained only at equal shares. Comparisons across polities of different size therefore require normalization. We use
  132 \begin{equation}
  133 \label{eq:hstar}
  134 H^{*}_{\pF,t}=\frac{H_{\pF,t}-1/n}{1-1/n}\in[0,1],\qquad n\geq 2,
  135 \end{equation}
  136 which is zero at equal shares and one when a single actor holds everything. The financial term of the unaccountable-concentration index is $u_{\pF,t}=H_{\pF,t}(1-Q_{\pF,t})$, so that $U_t=\sum_m\omega_m u_{m,t}$ in the notation of \citet{largo2026hbs}. The term is small when control is dispersed or when concentrated control is open to effective challenge, and it approaches one only when one actor holds the resources and nobody can contest how they are used.
  137 
  138 \subsection{Subdomains and the aggregation gap}
  139 
  140 Financial control is not one thing. A polity's credit market, its land, its public budget, and its procurement system may each be held by different actors. Aggregating the subdomains into one share vector loses information in a precise way.
  141 
  142 \begin{proposition}[Aggregation gap]
  143 \label{prop:financial-power:aggregation-gap}
  144 Let the financial pillar consist of subdomains $k=1,\dots,K$ with weights $\beta_k\geq 0$, $\sum_k\beta_k=1$, and control-share vectors $s^{k}=(s^{k}_i)_{i\in N}$, each summing to one. Define the aggregate share $\bar s_i=\sum_k\beta_k s^{k}_i$. Then
  145 \begin{equation}
  146 \label{eq:aggregation-gap}
  147 \sum_{k=1}^{K}\beta_k H(s^{k})-H(\bar s)=\sum_{i\in N}\operatorname{Var}_\beta\bigl(s^{\cdot}_i\bigr)\geq 0,
  148 \end{equation}
  149 where $\operatorname{Var}_\beta(s^{\cdot}_i)=\sum_k\beta_k(s^{k}_i-\bar s_i)^2$ is the $\beta$-weighted variance of actor $i$'s share across subdomains. Equality holds if and only if every actor holds the same share in every subdomain of positive weight.
  150 \end{proposition}
  151 
  152 \begin{proof}
  153 The aggregate shares sum to one, since $\sum_i\bar s_i=\sum_k\beta_k\sum_i s^k_i=\sum_k\beta_k=1$, so $H(\bar s)$ is a valid concentration index. For a fixed actor $i$, the identity $\sum_k\beta_k(s^k_i)^2-\bigl(\sum_k\beta_k s^k_i\bigr)^2=\sum_k\beta_k(s^k_i-\bar s_i)^2$ is the usual decomposition of a second moment into a squared mean and a variance; it uses only $\sum_k\beta_k=1$. Summing over $i$ gives
  154 \[
  155 \sum_k\beta_k\sum_i(s^k_i)^2-\sum_i\bar s_i^{\,2}=\sum_i\operatorname{Var}_\beta(s^{\cdot}_i),
  156 \]
  194 \[
  195 \Prob\Bigl(\frac{Z_T}{Y_T}\geq\frac{2k}{pT}\,\Big|\,S_T\Bigr)\leq\frac{(1-q)^k+e^{-pT/8}}{\nu}.
  196 \]
  408 \[
  409 \varepsilon_{\pF\to n}=\frac{\partial\ln\E[y^{n}_i\mid s^{\pF}_i,X_i]}{\partial\ln s^{\pF}_i},
  410 \]
  421 \[
  422 \frac{\partial e^*}{\partial s}=-\frac{\pi_e}{s\,\pi_{ee}}>0,\qquad
  423 \frac{\partial e^*}{\partial V}=-\frac{\pi_e}{V\,\pi_{ee}}>0,\qquad
  424 \frac{\partial e^*}{\partial Q}=-\frac{\pi_{eQ}}{\pi_{ee}}<0.
  425 \]
  448 \[
  449 D\leq\frac{\delta g}{1-\delta}.
  450 \]

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "rg -n '[0-9]+-[0-9]+' papers/latex/financial-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
134:H^{*}_{\pF,t}=\frac{H_{\pF,t}-1/n}{1-1/n}\in[0,1],\qquad n\geq 2,
536:Two passages bear on the financial pillar. The first is Revelation 13:16-17: ``And he causeth all, both small and great, rich and poor, free and bond, to receive a mark in their right hand, or in their foreheads: And that no man might buy or sell, save he that had the mark, or the name of the beast, or the number of his name.'' The image is economic participation conditioned on allegiance. In the vocabulary of this paper, it describes a financial pillar whose settlement procedure for exchange is gated by a test of loyalty administered by the ideological pillar: the coupling $C_{\pF\pI}$ is complete, and contestability for those who fail the test is zero. Part VI formalizes the same condition from the producers' side as a participation gate, access to exchange conditional on allegiance, and treats the passage as its limiting case (Definition 6.7 and Proposition 6.8 of \citealt{long2026productive}). Kraybill reads the passage against the participation of Asian merchants and artisans in trade guilds whose life was bound up with the imperial cult, so that commerce required at least tacit participation in worship \citep{kraybill1996}.
578:David E. Aune (1998). \emph{Revelation 17-22}. Word Biblical Commentary 52C, Thomas Nelson.
644:Michael Cox, Gwen Arnold, and Sergio Villamayor Tomas (2010). A Review of Design Principles for Community-based Natural Resource Management. \emph{Ecology and Society} 15(4). doi:10.5751/ES-03704-150438.
653:Raymond de Roover (1963). \emph{The Rise and Decline of the Medici Bank, 1397-1494}. Harvard University Press.
659:Mauricio Drelichman and Hans-Joachim Voth (2011). Lending to the Borrower from Hell: Debt and Default in the Age of Philip II. \emph{The Economic Journal} 121(557). doi:10.1111/j.1468-0297.2011.02442.x.
737:Philip T. Hoffman and Kathryn Norberg (eds.) (1994). \emph{Fiscal Crises, Liberty, and Representative Government, 1450-1789}. Stanford University Press. doi:10.1515/9781503619500.
740:Philip T. Hoffman, Gilles Postel-Vinay, and Jean-Laurent Rosenthal (2000). \emph{Priceless Markets: The Political Economy of Credit in Paris, 1660-1870}. University of Chicago Press.
752:K. K{\i}van\c{c} Karaman and \c{S}evket Pamuk (2010). Ottoman State Finances in European Perspective, 1500-1914. \emph{The Journal of Economic History} 70(3). doi:10.1017/s0022050710000550.
770:J\'anos Kornai (1986). The Soft Budget Constraint. \emph{Kyklos} 39(1). doi:10.1111/j.1467-6435.1986.tb01252.x.
800:Rafael La Porta, Florencio L\'opez-de-Silanes, and Andrei Shleifer (2002). Government Ownership of Banks. \emph{The Journal of Finance} 57(1). doi:10.1111/1540-6261.00422.
890:John F. Padgett and Christopher K. Ansell (1993). Robust Action and the Rise of the Medici, 1400-1434. \emph{American Journal of Sociology} 98(6). doi:10.1086/230190.
914:Raghuram G. Rajan and Luigi Zingales (2003). The Great Reversals: The Politics of Financial Development in the Twentieth Century. \emph{Journal of Financial Economics} 69(1). doi:10.1016/S0304-405X(03)00125-9.
947:Charles Tilly (1990). \emph{Coercion, Capital, and European States, AD 990-1990}. Blackwell.
950:Daniel Treisman (2010). 'Loans for Shares' Revisited. \emph{Post-Soviet Affairs} 26(3). doi:10.2747/1060-586X.26.3.207.
953:Gordon Tullock (1967). The Welfare Costs of Tariffs, Monopolies, and Theft. \emph{Western Economic Journal} 5(3). doi:10.1111/j.1465-7295.1967.tb01923.x.
959:Fran\c{c}ois R. Velde and David R. Weir (1992). The Financial Market and Government Debt Policy in France, 1746-1793. \emph{The Journal of Economic History} 52(1). doi:10.1017/s002205070001024x.
974:Polly Wiessner (2005). Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity? \emph{Human Nature} 16(2). doi:10.1007/s12110-005-1000-9.

2026-10-22T16:59:16.369985Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
codex
Found these LaTeX formatting issues:

- **Line 157:** A reference may break awkwardly across lines. Change `which is \eqref{eq:aggregation-gap}` to `which is~\eqref{eq:aggregation-gap}`.
- **Lines 536, 578, 653, 737, 740, 752, 890, 947, 959:** Numeric ranges use hyphens instead of en dashes. Replace `-` with `--`, e.g. `13:16--17`, `1397--1494`, and `1746--1793`. Do not alter hyphens inside DOI strings.
- **Lines 638 and 659:** TeX treats the period after the uppercase Roman numeral in “Philip II.” as abbreviation spacing. Change `Philip II.` to `Philip II\@.` before the following journal title.
- **Line 950:** Straight apostrophes are used as quotation marks. Change `'Loans for Shares'` to ````Loans for Shares''``.

No missing packages, unmatched environments, duplicate labels, undefined internal references, undefined citation keys, or obvious static overfull/underfull-box risks were found.

VERDICT: NEEDS_FIX
hook: Stop
hook: Stop
hook: Stop Completed
hook: Stop Completed
tokens used
98,453
Found these LaTeX formatting issues:

- **Line 157:** A reference may break awkwardly across lines. Change `which is \eqref{eq:aggregation-gap}` to `which is~\eqref{eq:aggregation-gap}`.
- **Lines 536, 578, 653, 737, 740, 752, 890, 947, 959:** Numeric ranges use hyphens instead of en dashes. Replace `-` with `--`, e.g. `13:16--17`, `1397--1494`, and `1746--1793`. Do not alter hyphens inside DOI strings.
- **Lines 638 and 659:** TeX treats the period after the uppercase Roman numeral in “Philip II.” as abbreviation spacing. Change `Philip II.` to `Philip II\@.` before the following journal title.
- **Line 950:** Straight apostrophes are used as quotation marks. Change `'Loans for Shares'` to ````Loans for Shares''``.

No missing packages, unmatched environments, duplicate labels, undefined internal references, undefined citation keys, or obvious static overfull/underfull-box risks were found.

VERDICT: NEEDS_FIX
