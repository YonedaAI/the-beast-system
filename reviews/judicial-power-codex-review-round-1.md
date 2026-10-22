---
reviewer: codex (OpenAI) gpt-5.6-sol
type: formatting
paper: judicial-power
round: 1
date: 2026-10-22T15:26:55Z
---
Reading additional input from stdin...
2026-10-22T15:47:26.161114Z ERROR codex_models_manager::cache: failed to load models cache: missing field `base_instructions` at line 139 column 5
OpenAI Codex v0.145.0
--------
workdir: /Users/mlong/Documents/Development/the-beast-system
model: gpt-5.6-sol
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a1644b-b91c-76e2-b638-0ddb9cfbc11b
--------
user
Read ONLY the file papers/latex/judicial-power.tex (do not explore other files or directories). Review it for LaTeX formatting issues: compilation errors, missing packages, broken references, inconsistent styling, overfull/underfull boxes, spacing problems. List all issues with line numbers and concrete fixes. End your response with a VERDICT line — exactly one of: VERDICT: PASS (no issues remain) or VERDICT: NEEDS_FIX (issues listed above must be fixed).
warning: Under-development features enabled: chronicle. Under-development features are incomplete and may behave unpredictably. To suppress this warning, set `suppress_unstable_features_warning = true` in /Users/mlong/.codex/config.toml.
warning: clamping SessionEnd hook timeout to 3s in /Users/mlong/.codex/plugins/cache/openai-codex/codex/1.0.6/hooks/hooks.json
2026-10-22T15:47:27.692462Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server linear: OAuth token refresh failed: Server returned error response: invalid_grant: Grant not found
2026-10-22T15:47:28.837703Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server resend: OAuth token refresh failed: Server returned error response: invalid_grant: Refresh token has been revoked
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
I’ll inspect only the specified `.tex` file, using line-numbered reads and no repository exploration.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'nl -ba papers/latex/judicial-power.tex' in /Users/mlong/Documents/Development/the-beast-system
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
    20	\usepackage[round,authoryear]{natbib}
    21	\usepackage{enumitem}
    22	\usepackage[hidelinks]{hyperref}
    23	\usepackage{cleveref}
    24	
    25	\newtheorem{theorem}{Theorem}[section]
    26	\newtheorem{proposition}[theorem]{Proposition}
    27	\newtheorem{lemma}[theorem]{Lemma}
    28	\newtheorem{corollary}[theorem]{Corollary}
    29	\theoremstyle{definition}
    30	\newtheorem{definition}[theorem]{Definition}
    31	\newtheorem{assumption}[theorem]{Assumption}
    32	\theoremstyle{remark}
    33	\newtheorem{remark}[theorem]{Remark}
    34	
    35	\newcommand{\pF}{\mathsf{F}}
    36	\newcommand{\pP}{\mathsf{P}}
    37	\newcommand{\pJ}{\mathsf{J}}
    38	\newcommand{\pI}{\mathsf{I}}
    39	\newcommand{\pC}{\mathsf{C}}
    40	\newcommand{\pW}{\mathsf{W}}
    41	\newcommand{\Mset}{\mathcal{M}}
    42	\newcommand{\Integ}{\mathcal{I}}
    43	\newcommand{\Read}{\mathcal{R}}
    44	\newcommand{\Qadd}{Q^{+}_{\pJ,t}}
    45	\newcommand{\Qchain}{Q^{\times}_{\pJ,t}}
    46	
    47	\title{Judicial Power and Legal Interpretation\\[4pt]
    48	  {\normalsize Part III of \emph{The Six Pillars of the Beast System}}}
    49	\author{Matthew Long\\
    50	  \small The YonedaAI Collaboration, YonedaAI Research Collective\\
    51	  \small Chicago, IL\\
    52	  \small \texttt{matthew@yonedaai.com}\quad \url{https://yonedaai.com}}
    53	\date{October 2026}
    54	
    55	\begin{document}
    56	\maketitle
    57	
    58	\begin{abstract}
    59	Every governance system must decide who interprets its laws. General rules cannot settle particular disputes by themselves, because every rule admits more than one reasonable reading at its edges. This paper derives the judicial function from that fact. Under three explicit assumptions (open texture produces disputes that the parties cannot settle alone, self-help is costly to the collective, and exit is costly), any collective that persists indefinitely resolves all but finitely many such disputes through a determination procedure that neither party controls. The derivation requires a function, not an office. Leopard-skin chiefs, Barotse moots, Ju/'hoansi talking-out, qadi courts, the Parlement of Paris and modern constitutional courts all perform it. Two results narrow the claim. When exit is costless the forcing argument fails, which matches the thin adjudication of immediate-return foragers. When rules are executed by code, interpretation relocates to the classification of inputs instead of disappearing. The paper then operationalizes judicial contestability as a chain of disclosure, access, independence and compliance by the powerful, and proves that the probability that a captured ruling persists depends on the product of these links. An additive index can therefore score a judiciary well while a single broken link leaves capture unchecked. A comparison of six regime types, from market capitalism to historical Catholic monarchies, finds the function everywhere and finds wide variation in its concentration and coupling to other pillars. Eight hypotheses with stated falsifiers make the capture claims testable. No numerical concentration scores are reported for real cases.
    60	\end{abstract}
    61	
    62	\section{Introduction}
    63	
    64	Every governance system answers the question of who interprets its laws. The answer may be a supreme court, a council of jurists, a royal chancery, a party committee or an old man with a leopard skin who walks between two feuding lineages. This paper argues that some answer is unavoidable and that the variety of answers is where the political economy of judicial power lies.
    65	
    66	The argument belongs to a seven-part series on the six functions that organized governance requires: control of resources ($\pF$), rule-making ($\pP$), interpretation ($\pJ$), legitimation ($\pI$), coercion ($\pC$) and production ($\pW$) \citep{long2026financial,long2026political,long2026ideological,long2026coercive,long2026productive,long2026formalized}. The series adopts the vocabulary and the multiplex-network model of \citet{largo2026hbs}, which named the configuration the Hierarchy of the Beast System after the imagery of Revelation 13. The source paper used five functions and placed adjudication inside a single legal-administrative function. The series splits that function. Part II treats the making and changing of general rules; this Part treats their application to particular cases. The name ``Beast System'' refers throughout to the universal six-function structure, never to a religion, people, profession, regime or person.
    67	
    68	The series keeps two propositions apart. Proposition A says that every functioning governance system contains the six functions and the dependencies among them; Part VII proves it as a theorem from six working axioms. Proposition B says that in some systems the functions become concentrated and coordinated so that independent accountability fails. Proposition B is contingent and measurable, and Part VII proves that A does not imply B.
    69	
    70	The judicial piece of Proposition A is a theorem. A collective that persists with general rules, recurrent disputes, and costly self-help and exit must dispose of all but finitely many of its unresolved disputes through a procedure that neither party controls (\cref{thm:judicial-power:necessity}). The judicial piece of Proposition B is a claim about measurement. A captured ruling persists with a probability that depends on the product of four review links, disclosure, access, independence and compliance, so an additive index of judicial independence can rate a judiciary well while one broken link leaves capture unchecked (\cref{prop:judicial-power:chain}).
    71	
    72	The comparison is even-handed by construction. Since every regime type has the judicial function, the question is never whether a civilization has a Beast System. The question is how the function is distributed: which institutions hold it, how concentrated it is, how tightly it is coupled to the other five functions, and what keeps it accountable. Differentiation of judges, lawyers and courts is not evidence of capture \citep{largo2026hbs}. Capture is a claim about particular links, and it carries a burden of evidence.
    73	
    74	\section{The judicial layer}
    75	\label{sec:layer}
    76	
    77	\subsection{Shared objects}
    78	
    79	The series inherits its formal objects from \citet{largo2026hbs}. A polity at time $t$ is a directed multiplex network $G_t=(V_t,E_t)$ whose nodes are organizations or coherent actor groups. Each pillar $m\in\Mset=\{\pF,\pP,\pJ,\pI,\pC,\pW\}$ has a layer with adjacency $A^m_t$ and edge weights $a^m_{ij,t}\in[0,1]$, the documented capacity of actor $i$ to constrain a feasible action of actor $j$ through mechanism $m$. A role map assigns actors to pillars, many to many. Actor $i$ holds a control share $s^m_{i,t}$ in pillar $m$, with $\sum_i s^m_{i,t}=1$, and concentration is the Herfindahl index $H_{m,t}=\sum_i (s^m_{i,t})^2$.
    80	
    81	Accountability and integration are measured separately. Contestability $Q_{m,t}\in[0,1]$ summarizes transparency, appeal rights, independence, competition and credible replacement, and the illustrative index of unaccountable concentration is $U_t=\sum_m \omega_m H_{m,t}(1-Q_{m,t})$ with preregistered weights. Cross-pillar integration $C_{mn,t}\in[0,1]$ is the extent to which one coalition commands appointments, budgets, sanctions or agenda in both $m$ and $n$, and the integration statistic is $\Integ_t=\frac{2}{M(M-1)}\sum_{m<n}C_{mn,t}$ with $M=6$. A capture link $(i\to j,m)$ requires privileged access or discretion, a weakening of applicable accountability, and material evidence tying the asymmetry to an institutional output. The source's strong classification requires both high $U_t$ and high $\Integ_t$ \citep{largo2026hbs}. Following the source, pillar indices are superscripts on quantities attached to actors or edges and subscripts on quantities attached to a whole pillar, and the time subscript is dropped when the period is clear from context.
    82	
    83	The judicial layer $A^{\pJ}_t$ records one kind of constraint: the capacity of one actor to fix what a general rule requires of another actor in a particular case. A court that orders a firm to pay damages, a qadi who assigns custody, an inquisitor who declares a proposition heretical and a party committee that tells a judge how to decide all hold edges in this layer. The weight of an edge does not depend on whether the actor is called a court. It depends on whether the actor's determinations are acted upon.
    84	
    85	The boundary with rule-making follows H.\,L.\,A. Hart's distinction among secondary rules \citep{hart1961}. Hart argued that a regime of primary obligations alone suffers three defects: uncertainty about which rules exist, a static character, and the inefficiency of leaving disputes about violations to diffuse social pressure. The remedies are a rule of recognition, rules of change and rules of adjudication. The series assigns the rule of change to Part II \citep{long2026political}, the rule of recognition to Part IV \citep{long2026ideological}, and the rule of adjudication to the judicial pillar. The boundary classifies acts rather than institutions: making or changing a general rule is rule-making, and fixing what a rule requires in a particular case is interpretation. A body that performs both kinds of act, as a king in council does, appears in both layers, and the coupling $C_{\pP\pJ,t}$ records how far one coalition controls both.
    86	
    87	\subsection{Rules, cases and open texture}
    88	
    89	\begin{definition}[Rule system with open texture]
    90	\label{def:judicial-power:open-texture}
    91	A rule system is a tuple $(X,\mathcal{V},R,\Read)$ in which $X$ is a set of cases, $\mathcal{V}$ a set of verdicts with at least two elements, $R$ a set of general rules, and $\Read$ assigns to each rule $r\in R$ a nonempty set $\Read(r)$ of admissible readings $\rho:X\to\mathcal{V}$. The open set of $r$ is
    92	\[
    93	O(r)=\{x\in X : \rho(x)\neq\rho'(x)\text{ for some }\rho,\rho'\in\Read(r)\}.
    94	\]
    95	A rule has open texture when $O(r)\neq\emptyset$.
    96	\end{definition}
    97	
    98	An admissible reading is one that competent members of the collective would accept as a good-faith reading of the rule. The set is fixed by the collective's own interpretive practice, not by the analyst. Hart used the phrase ``open texture'' for the fact that general terms have a core of settled application and a penumbra where reasonable users disagree \citep{hart1961}. The open set is that penumbra, expressed as the cases on which admissible readings diverge.
    99	
   100	The series' third working axiom, owned by Part VII, states that rules are general, cases are particular, and disputes arise. In the present vocabulary the pillar-level statement is that some rule has a nonempty open set and that cases in it occur repeatedly. The axiom is an empirical claim about rule-governed collectives. It would fail for a collective whose every rule was applied identically by every member to every case that arose.
   101	
   102	\begin{definition}[Dispute and residual dispute]
   103	\label{def:judicial-power:dispute}
   104	A dispute is a tuple $(x,r,a,b)$ in which $x\in O(r)$, members $a\neq b$ each endorse an admissible reading of $r$ and the two readings assign different verdicts to $x$, and each member strictly prefers the verdict of its own reading. A dispute is residual if unassisted bargaining between $a$ and $b$ fails to produce a verdict that both act on.
   105	\end{definition}
   106	
   107	The definition excludes disputes that bargaining resolves. Most disagreements end that way, and nothing in the argument below requires them to be rare. It requires only that some fail. Bargaining failure has familiar sources: each party believes its own reading is the right one, private information about the facts, the absence of a credible commitment to abide by a compromise, and indivisible stakes such as custody or honor.
   108	
   109	\subsection{Determination procedures}
   110	
   111	\begin{definition}[Determination procedure and implemented adjudication]
   112	\label{def:judicial-power:determination}
   113	A disposition of a residual dispute takes one of four forms. In a determination, a verdict is produced by a procedure that neither party controls alone, and both parties act on it. In self-help, one party imposes its verdict by force, or the dispute escalates into feud. In exit, one party leaves the collective. Abandonment is every other disposition: the parties stop pursuing the dispute without a verdict that both act on, and the grievance remains. Adjudication is implemented in a collective when infinitely many residual disputes are disposed of by determination over an unbounded horizon.
   114	\end{definition}
   115	
   116	The class of determination procedures is wide on purpose. It includes a judge's ruling, a mediator's proposal that both parties accept, the verdict of a council, an oath, an ordeal, a lot, and the output of a program to which both parties have submitted. Martin Shapiro argued that the triad of two disputants and a third party is the prototype of courts in every society, and that courts differ mainly in how far the third party departs from consent toward imposition \citep{shapiro1981}. The definition follows Shapiro by locating the function in the triadic structure rather than in an office. It departs from him only in counting impersonal procedures such as lots and programs as third parties, because they have the property that matters here: neither disputant controls the outcome.
   117	
   118	Control shares in the judicial layer are assigned by the last word. For each final determination, the last word belongs to the actor that decided it, unless another actor directed the decision or reversed it, in which case it belongs to that actor. A lower court's judgment that is never appealed, or that an apex court declines to review, is attributed to the lower court; the bare possibility of reversal does not count. Direction counts only when it is documented, for example by an instruction, an approval requirement or a review by a body outside the bench. A multimember court is a single node, since the source's nodes are organizations, and a determination that requires the concurrence of two bodies is split equally between them. Actor $i$'s control share $s^{\pJ}_{i,t}$ is its stake-weighted share of the last words in period $t$. A party committee that instructs judges in politically salient cases therefore holds judicial control share in those cases even though it signs no judgment. Anticipatory deference, in which judges decide as a committee would wish without being told, does not enter $s^{\pJ}_{i,t}$; it appears as a low value of the independence component defined below.
   119	
   120	\subsection{Judicial contestability and ruler-boundness}
   121	
   122	The source defines $Q_{m,t}$ as a composite of transparency, appeal rights, institutional independence, effective competition and credible replacement \citep{largo2026hbs}. For the judicial layer these ingredients form a sequence. A determination can be corrected only if its defect is visible, if an affected party can bring a challenge, if the forum that hears the challenge is independent of the party that benefited, and if the powerful party obeys the corrected determination.
   123	
   124	\begin{definition}[Judicial contestability components]
   125	\label{def:judicial-power:qj}
   126	The judicial contestability vector at time $t$ is $\mathbf{q}_t=(q^{\mathrm{dis}}_t,q^{\mathrm{acc}}_t,q^{\mathrm{ind}}_t,q^{\mathrm{cmp}}_t)\in[0,1]^4$. Its components are the probabilities of four successive stages in the correction of a defective determination, each conditional on the stages before it. Disclosure $q^{\mathrm{dis}}_t$ is the probability that the defect and the facts bearing on the determination's integrity are publicly recorded. Access $q^{\mathrm{acc}}_t$ is the probability that, given disclosure, an adversely affected party brings a challenge, including an appeal, given the cost of counsel and the availability of a forum. Independence $q^{\mathrm{ind}}_t$ is the probability that, given a challenge, the reviewing forum decides on the merits rather than at the direction of the beneficiary, which depends on tenure security and on appointment insulation, that is, on the appointment channel by which a coalition fills judicial offices \citep{long2026political}. Compliance $q^{\mathrm{cmp}}_t$ is the probability that, given an adverse ruling on review, the beneficiary complies with it. Two aggregates are used:
   127	\[
   128	\Qadd=\sum_{k} w_k q^{k}_t,\quad \textstyle\sum_k w_k=1,\ w_k\ge 0, \qquad\qquad \Qchain=\prod_{k} q^{k}_t .
   129	\]
   130	\end{definition}
   131	
   132	The additive aggregate is the form of most published indices. The multiplicative aggregate is the review-chain form, which \cref{prop:judicial-power:chain} shows governs the persistence of captured outcomes. The two are ordered.
   133	
   134	\begin{lemma}[Ordering of the aggregates]
   135	\label{lem:judicial-power:ordering}
   136	For every $\mathbf{q}_t\in[0,1]^4$ and every weight vector, $\Qchain\le\min_k q^k_t\le\Qadd$. Consequently, the judicial term $\omega_{\pJ}H_{\pJ,t}(1-Q_{\pJ,t})$ of $U_t$ is at least as large when $Q_{\pJ,t}$ is measured by $\Qchain$ as when it is measured by $\Qadd$.
   137	\end{lemma}
   138	
   139	\begin{proof}
   140	A product of numbers in $[0,1]$ is no larger than any of its factors, so $\Qchain\le\min_k q^k_t$. A weighted average with nonnegative weights summing to one is no smaller than the smallest averaged value, so $\min_k q^k_t\le\Qadd$. The second claim follows because $\omega_{\pJ}H_{\pJ,t}\ge 0$ and $1-Q_{\pJ,t}$ decreases in $Q_{\pJ,t}$.
   141	\end{proof}
   142	
   143	The bounds in the lemma are attained in opposite cases. When every component is equal, the minimum and the additive aggregate coincide; when one stage fails and the others work, the chain aggregate is zero while the additive aggregate stays high. Dispersion among the components is therefore what separates the two measures.
   144	
   145	\begin{definition}[Ruler-boundness and the two-tier judicial layer]
   146	\label{def:judicial-power:boundness}
   147	Ruler-boundness $\beta_t$ is the compliance component $q^{\mathrm{cmp}}_t$ restricted to rulings against members of the governing coalition: the probability that the coalition complies with an adverse final determination. A judicial layer is two-tier when the set of cases is partitioned into an ordinary class and a politically salient class, and the contestability vector differs between them.
   148	\end{definition}
   149	
   150	Ruler-boundness gives a working form to a distinction that Brian Tamanaha draws between the rule of law and rule by law \citep{tamanaha2004}. Under rule by law, law is an instrument that rulers use to govern others; under the rule of law, rulers are themselves bound. A regime can have an effective judicial function for ordinary disputes and low ruler-boundness at once. Randall Peerenboom's account of Chinese legal reform describes a thin rule of law of this partial kind \citep{peerenboom2002}, and Kathryn Hendley's study of everyday law in Russia documents courts that decide ordinary disputes routinely while politically salient cases follow a different logic \citep{hendley2017}.
   151	
   152	\begin{definition}[Judicial capture link]
   153	\label{def:judicial-power:capture}
   154	A judicial capture link is a capture link $(i\to j,\pJ)$ in the sense of \citet{largo2026hbs} whose three conditions take the following form in the judicial layer. Actor $i$ has privileged access to or discretion over determinations affecting $j$, for example through control of the appointment, promotion, remuneration or election funding of the deciding judges, through ex parte communication, or through control of which forum hears the case. The privilege weakens at least one component of the contestability vector $\mathbf{q}_t$. Material evidence ties the asymmetry to determinations, for example a difference in outcomes between cases in which the privilege is present and comparable cases in which it is absent.
   155	\end{definition}
   156	
   157	\subsection{Review chains}
   158	
   159	The source's second proposition holds that effective independent review and voice should reduce the probability that attempted capture yields persistent outcomes \citep{largo2026hbs}. For the judicial layer the structure of review can be stated precisely.
   160	
   161	\begin{proposition}[Review chain]
   162	\label{prop:judicial-power:chain}
   163	Suppose an attempted capture produces a favorable determination with probability $q_0\in(0,1]$, and the determination is reversed only if the four stages of \cref{def:judicial-power:qj} all succeed, with the conditional probabilities given there. Then the probability that the captured outcome persists is
   164	\[
   165	P_{\mathrm{persist}}=q_0\big(1-\Qchain\big),\qquad \Qchain=q^{\mathrm{dis}}_tq^{\mathrm{acc}}_tq^{\mathrm{ind}}_tq^{\mathrm{cmp}}_t.
   166	\]
   167	Three consequences follow. If any link is zero, then $P_{\mathrm{persist}}=q_0$ whatever the other links. Raising link $k$ by $\Delta\in(0,1-q^k_t]$ reduces $P_{\mathrm{persist}}$ by $q_0\Delta\prod_{j\neq k}q^j_t$, so the marginal effect of link $k$ is $-\partial P_{\mathrm{persist}}/\partial q^k_t=q_0\prod_{j\neq k}q^j_t$; when every link is positive, this marginal effect is largest for the link with the smallest value. For any weights $w_k>0$ there are contestability vectors with the same additive aggregate $\Qadd$ and different persistence probabilities, including a vector with $\Qadd=1-\min_k w_k$ and $P_{\mathrm{persist}}=q_0$.
   168	\end{proposition}
   169	
   170	\begin{proof}
   171	Reversal is the intersection of four events, and the components are the probabilities of each event conditional on the preceding ones, so by the chain rule of probability the probability of reversal given a captured determination is the product $\Qchain$. Persistence therefore has probability $q_0(1-\Qchain)$. If some $q^k_t=0$, the product is zero. Raising $q^k_t$ by $\Delta$ raises the product by $\Delta\prod_{j\neq k}q^j_t$, which reduces $P_{\mathrm{persist}}$ by $q_0\Delta\prod_{j\neq k}q^j_t$. The marginal effect is the derivative of this linear expression in $\Delta$. When all links are positive, $\prod_{j\neq k}q^j_t=\Qchain/q^k_t$, which is largest for the smallest $q^k_t$. For the last claim, let $k^{*}$ be a link with the smallest weight, set $q^{k^{*}}_t=0$ and every other link to one. Then $\Qadd=1-w_{k^{*}}$ and $\Qchain=0$, so $P_{\mathrm{persist}}=q_0$. Setting every link to $1-w_{k^{*}}$ gives the same additive aggregate and a strictly positive product, hence, because $q_0>0$, a strictly smaller persistence probability.
   172	\end{proof}
   173	
   174	The proposition explains why judicial-independence indices built by addition can mislead. A judiciary with published reasons, open access and independent judges scores well on an additive index, but if the governing coalition ignores adverse rulings, the review chain is broken at its last link and captured outcomes persist. The multiplicative form also implies that reform yields the most where the chain is weakest. The comparison in \cref{sec:comparative} below suggests that the weakest link is often access in market-capitalist systems, compliance in the political tier of party-states, and independence in backsliding democracies.
   175	
   176	The product is exact because each component is defined conditionally on the stages before it; no independence assumption is involved. Dependence matters for measurement. Published indicators usually record marginal frequencies, such as the share of decisions published or the share of rulings against the government, rather than conditional ones. If the stages tend to succeed or fail together, the product of marginal frequencies understates the true probability of reversal. Tests of the review-chain claim should therefore estimate the conditional components from case histories, as hypothesis HJ8 requires.
   177	
   178	\subsection{Two-tier judicial layers}
   179	
   180	\begin{proposition}[Aggregation hides the political tier]
   181	\label{prop:judicial-power:dualstate}
   182	For a two-tier judicial layer in which the politically salient tier carries a share $\varphi\in(0,1)$ of stake-weighted cases and has chain contestability $Q^{\times}_{\Pi}$, while the ordinary tier has $Q^{\times}_{O}$, define the stake-weighted contestability $\bar Q^{\times}=(1-\varphi)Q^{\times}_O+\varphi Q^{\times}_\Pi$. For every $\varepsilon\in(0,1)$ there is a two-tier layer with $\varphi\in(0,\varepsilon]$, $\bar Q^{\times}\ge 1-\varepsilon$ and $Q^{\times}_\Pi=0$.
   183	\end{proposition}
   184	
   185	\begin{proof}
   186	Given $\varepsilon$, take $\varphi=\varepsilon$, $Q^{\times}_O=1$ and $Q^{\times}_\Pi=0$. Then $\bar Q^{\times}=1-\varepsilon$.
   187	\end{proof}
   188	
   189	The proof is elementary, and the point is about measurement. Surveys of business users, caseload statistics and appeal rates are dominated by the ordinary tier. They can report a well-functioning judiciary in a regime whose courts never bind the ruling coalition. Control shares and concentration should also be computed tier by tier, because the last word in the political tier may rest with an actor that holds none in the ordinary tier. Measurements intended to test Proposition B must therefore be tier-specific, and hypothesis HJ3 in \cref{sec:measurement} makes the tiers an object of test.
   190	
   191	\section{Necessity of the judicial function}
   192	\label{sec:necessity}
   193	
   194	\subsection{The necessity theorem}
   195	
   196	The argument for necessity is a conditions-of-persistence argument. It does not explain why any particular court exists. It shows that a collective with general rules cannot persist indefinitely without performing the function that courts perform, provided three assumptions hold.
   197	
   198	\begin{assumption}[Recurrent residual disputes]
   199	\label{ass:arrival}
   200	On the event that the collective persists for all time, infinitely many residual disputes arise, and each reaches a disposition at some finite time.
   201	\end{assumption}
   202	
   203	\begin{assumption}[Costly self-help and exit]
   204	\label{ass:cost}
   205	There is $\kappa\in(0,1]$ such that, conditional on the history up to the disposition of any residual dispute, a disposition by self-help, by exit or by abandonment ends the collective's persistence with probability at least $\kappa$.
   206	\end{assumption}
   207	
   208	\Cref{ass:arrival} is the third axiom in operational form together with a positive rate of bargaining failure. \Cref{ass:cost} bundles three claims. Self-help between members tends toward feud, which in segmentary societies can split the group along lineage lines. Exit by one party removes a member and, when the parties are heads of kin groups, a segment of the collective. Abandonment leaves a grievance that tends to return as self-help or exit. The assumption does not say that every feud destroys the group. It says that each abandoned or forcibly settled dispute carries a risk to the collective's continuation as a single decision-making unit, and that the risk is bounded below.
   209	
   210	\begin{theorem}[Necessity of adjudication]
   211	\label{thm:judicial-power:necessity}
   212	Under \cref{ass:arrival,ass:cost}, the event that the collective persists for all time is contained, up to a null set, in the event that adjudication is implemented. If the collective persists with positive probability, the fraction of residual disputes disposed of by determination converges to one almost surely on the persistence event.
   213	\end{theorem}
   214	
   215	\begin{proof}
   216	Let $\Pi$ be the event that the collective persists for all time and let $N$ be the number of residual disputes disposed of by self-help, exit or abandonment before the collective ends, with $N=\infty$ allowed. For $n\ge 1$ let $S_n$ be the event that at least $n$ such dispositions occur and the collective survives each of the first $n$. By \cref{ass:cost}, conditional on $S_{n-1}$ and on the occurrence of an $n$-th such disposition, survival through it has probability at most $1-\kappa$. Induction gives $\Pr(S_n)\le(1-\kappa)^n$. Since $\Pi\cap\{N\ge n\}\subseteq S_n$, we have $\Pr(\Pi\cap\{N=\infty\})\le\inf_n (1-\kappa)^n=0$. Hence, almost surely on $\Pi$, only finitely many residual disputes are disposed of other than by determination. By \cref{ass:arrival}, infinitely many residual disputes arise on $\Pi$, and each reaches exactly one of the four dispositions of \cref{def:judicial-power:determination}, so infinitely many are disposed of by determination and adjudication is implemented. Index residual disputes in order of disposition, breaking ties arbitrarily. If $D_k$ and $N_k$ count determinations and other dispositions among the first $k$ residual disputes so indexed, then on $\Pi$ the count $N_k$ is eventually constant while $D_k+N_k=k$, so $D_k/k\to 1$.
   217	\end{proof}
   218	
   219	The theorem says nothing about who determines. A single mediator, a rotating council, a lottery and a hierarchy of appellate courts all satisfy it. It also says nothing about the quality of determinations. A collective may persist with determinations that are biased, slow or cruel, so long as the parties act on them. The necessity is of a function, and the function is minimal: a procedure that neither disputant controls, whose output both act on.
   220	
   221	\begin{remark}
   222	The proof needs only a conditional lower bound on the dissolution hazard, not independence across disputes, a stationary arrival rate, or any account of how determination procedures arise. A selection story is consistent with the theorem but not required by it.
   223	\end{remark}
   224	
   225	\subsection{Minimal forms in stateless and consensus societies}
   226	
   227	The theorem predicts that collectives without states still adjudicate, and that their procedures need not resemble courts. The ethnographic record bears this out (\cref{tab:minimal}), with a qualification that the next subsection makes precise.
   228	
   229	\begin{table}[t]
   230	\centering
   231	\small
   232	\caption{Minimal forms of the judicial function in stateless and consensus societies. Each row names the determination procedure, its source of compliance, and the strongest reading that the function is absent.}
   233	\label{tab:minimal}
   234	\begin{tabularx}{\textwidth}{L{2.3cm}YYY}
   235	\toprule
   236	Case & Determination procedure & Source of compliance & Strongest counter-reading \\
   237	\midrule
   238	Nuer & The leopard-skin chief mediates blood-feud compensation in cattle between lineages & Consent of the parties backed by the threat of renewed feud & The chief has no power to compel, so the settlement is a bargain rather than a judgment \\
   239	Barotse & Judges in a council apply the standard of the reasonable man to the conduct of litigants & Kinship obligations and the authority of the council & The Lozi had a kingdom, so the case shows a court rather than a stateless procedure \\
   240	Arusha & Councils of elders and lineage moots negotiate settlements between disputants & Pressure from kin groups and the prospect of continued relations & Outcomes reflect relative bargaining strength, so the procedure is negotiation \\
   241	Ju/'hoansi & Kin and camp members talk disputes out in public, and parties often move to another camp & Ridicule, gossip and the value of continued sharing relations & Exit by moving camp resolves many disputes with no third party at all \\
   242	Reverse dominance hierarchies & The camp acts as a moral community that judges would-be dominants and deviants & Criticism, ostracism, exile and in extreme cases execution & The judging group is also the sanctioning group, so the functions are fused \\
   243	Commons institutions & Users or their officials hold low-cost local arenas to resolve conflicts over the rules & Graduated sanctions and monitoring by users & The arenas are designed institutions, so they show possibility rather than necessity \\
   244	\bottomrule
   245	\end{tabularx}
   246	\end{table}
   247	
   248	Among the Nuer, whom E.\,E. Evans-Pritchard described as living in an ordered anarchy without government, a killing set off a feud between lineages unless compensation in cattle was arranged through the leopard-skin chief \citep{evanspritchard1940}. The chief could not compel either side. His role was to offer sanctuary to the killer, to negotiate the payment and to perform the rites that ended the feud. Evans-Pritchard's own emphasis on the absence of government is the strongest counter-reading: the chief decided nothing that the parties had not accepted. Under \cref{def:judicial-power:determination}, however, consent does not disqualify a procedure. What matters is that the settlement was produced through a third party whom neither lineage controlled, and that both acted on it. The source of compliance was the parties' preference for settlement over a continuing feud, which is the sanction-side dependency discussed in \cref{subsec:dependencies}.
   249	
   250	Max Gluckman's study of the Barotse shows a fuller judicial form, with judges who measured litigants against the conduct expected of a reasonable person in their position \citep{gluckman1955}. The case is a contrast rather than a hard case, since the Lozi had a kingdom. P.\,H. Gulliver's Arusha are closer to the stateless baseline \citep{gulliver1963}. Gulliver described dispute settlement through negotiation in moots and councils in which the relative strength of the parties' supporters shaped the outcome. That description invites the reading that no adjudication took place, only bargaining. The reply is that a dispute that reaches a moot is residual in the sense of \cref{def:judicial-power:dispute}: unassisted bargaining between the principals has failed, and the moot supplies a forum and participants who are not principals. A determination produced by a forum in which strength matters is a biased determination, not the absence of one.
   251	
   252	Even the societies most often cited as lacking hierarchy have a judging procedure: the camp's collective talk. Richard Lee's ethnography of the Ju/'hoansi of the Kalahari records disputes handled by public talk among kin and camp members, together with frequent movement between camps \citep{lee2013}. Polly Wiessner's study of norm enforcement among the Ju/'hoansi finds that criticism and talk were the main instruments by which norm violations were addressed \citep{wiessner2005}. Christopher Boehm's comparative work on foragers describes the same pattern from the side of the group, in which a coalition of subordinates judges and sanctions anyone who tries to dominate \citep{boehm1999}. James Woodburn adds that the egalitarianism of immediate-return societies is produced by leveling institutions, not by the absence of institutions \citep{woodburn1982}. The same body judges and sanctions, so $C_{\pJ\pC}$ is high in these societies, but neither disputant controls the procedure and the function is present.
   253	
   254	Elinor Ostrom's design principles for long-enduring commons institutions include rapid access to low-cost local arenas for resolving conflicts among users and between users and officials \citep{ostrom1990}. Michael Cox and coauthors' review of studies testing the principles found broad empirical support for them as a set \citep{cox2010}. Ostrom's cases are designed institutions, so they show that successful self-governance includes adjudication rather than proving that it must. With the stateless cases, they show the judicial function wherever general rules govern repeated interaction.
   255	
   256	\subsection{Counterexample attempts}
   257	
   258	The strongest counterexample to \cref{thm:judicial-power:necessity} is a collective that resolves residual disputes by exit. Woodburn's immediate-return societies and the Ju/'hoansi practice of moving between camps come close. When exit is costless the theorem's forcing argument fails, and the failure is a genuine limit on the claim.
   259	
   260	\begin{proposition}[Exit substitution]
   261	\label{prop:judicial-power:exit}
   262	Suppose \cref{ass:arrival} holds and a disposition by self-help or abandonment ends persistence with probability at least $\kappa>0$, but a disposition by exit carries no risk to persistence and is always available. Then there are collectives that persist with probability one and in which no residual dispute is disposed of by determination.
   263	\end{proposition}
   264	
   265	\begin{proof}
   266	Consider a regional population divided among bands. Let every residual dispute be disposed of by one party moving to another band, which by hypothesis does not affect the persistence of the regional collective. The collective never incurs the hazard attached to self-help or abandonment, so it persists with probability one, and no determination occurs.
   267	\end{proof}
   268	
   269	The proposition narrows the claim. Adjudication is forced where exit is costly. Where exit is cheap, the judicial function can be thin, and the ethnography of immediate-return foragers is consistent with that prediction: talk, ridicule and departure do much of the work that courts do elsewhere \citep{woodburn1982,lee2013}. Two qualifications keep the narrowing in proportion. The cheap-exit condition is rare: it requires mobile residence, no stored wealth, and access to other groups on the same terms, which Woodburn identified as distinctive of a small set of societies. The ethnographies of these societies also record talk-based mediation alongside exit \citep{lee2013,wiessner2005}, so the function is thin rather than absent.
   270	
   271	The second counterexample attempt is a rule system that leaves no room for interpretation because a program executes it. If rules are code, the program decides, and no judge is needed.
   272	
   273	\begin{proposition}[Relocation of interpretation]
   274	\label{prop:judicial-power:relocation}
   275	Let a rule $r$ over cases $X$ be executed by a program $c:Z\to\mathcal{V}$ applied to recorded inputs $z=\zeta(x)$, where an encoding $\zeta:X\to Z$ records a case for the program. Let $\mathcal{E}(r)$ be the nonempty set of admissible encodings, those that competent members would accept as recording cases faithfully for the rule's purpose, and let the code-level open set be
   276	\[
   277	O_c(r)=\{x\in X : c(\zeta(x))\neq c(\zeta'(x))\text{ for some }\zeta,\zeta'\in\mathcal{E}(r)\}.
   278	\]
   279	Suppose the parties have agreed in advance that the verdict $c(\zeta_0(x))$ settles every case $x$ in a set $X_0\subseteq X$, for a designated $\zeta_0\in\mathcal{E}(r)$, and that neither party alone controls $c$ or $\zeta_0$ on $X_0$. Outside $X_0$ both the rule and the program have standing, so the admissible positions there are $\Read^{*}(r)=\Read(r)\cup\{c\circ\zeta:\zeta\in\mathcal{E}(r)\}$, with open set $O^{*}(r)$ computed from $\Read^{*}(r)$ as in \cref{def:judicial-power:open-texture}. Then $O(r)\cup O_c(r)\subseteq O^{*}(r)$, and $O^{*}(r)$ also contains every case at which some $\rho\in\Read(r)$ and some $c\circ\zeta$ with $\zeta\in\mathcal{E}(r)$ disagree. The following hold.
   280	\begin{enumerate}[label=(\roman*)]
   281	\item On $X_0$ the program with encoding $\zeta_0$ is a determination procedure in the sense of \cref{def:judicial-power:determination}.
   282	\item For every case $x\in O^{*}(r)\setminus X_0$ there are admissible positions with different verdicts, so disputes can arise at $x$, and those in which bargaining fails are residual disputes subject to \cref{thm:judicial-power:necessity}.
   283	\item $O_c(r)=\emptyset$ if and only if every admissible encoding yields the same verdict under $c$ for every case.
   284	\end{enumerate}
   285	\end{proposition}
   286	
   287	\begin{proof}
   288	For (i), on $X_0$ the program produces the verdict, neither party alone controls the program or the encoding by hypothesis, and both parties have agreed in advance to act on the verdict. The inclusion $O(r)\cup O_c(r)\subseteq O^{*}(r)$ holds because $\Read^{*}(r)$ contains both $\Read(r)$ and $\{c\circ\zeta:\zeta\in\mathcal{E}(r)\}$, and a case at which some reading $\rho\in\Read(r)$ and some program reading $c\circ\zeta$ disagree lies in $O^{*}(r)$ by definition. For (ii), the pair $(r,\Read^{*}(r))$ is a rule system in the sense of \cref{def:judicial-power:open-texture}, so a case in $O^{*}(r)\setminus X_0$ admits two admissible positions with different verdicts, and two members whose interests favor different verdicts can each endorse one, which is a dispute under \cref{def:judicial-power:dispute}. The parties have not agreed that the program settles such a case, so a dispute there in which bargaining fails is residual, and \cref{thm:judicial-power:necessity} applies. Claim (iii) restates the definition of $O_c(r)$.
   289	\end{proof}
   290	
   291	Encoding moves the open set from the terms of the rule to the recording of cases and to the gap between rule and program: whether a delivery occurred, whether a price feed was accurate, whether a reported event matched the contract's description. A deterministic program removes open texture only if every admissible encoding agrees, which is rare for rules about the world rather than about the program's own state. Unforeseen cases also fall outside $X_0$ almost by definition. Systems that execute agreements automatically therefore acquire arbiters, oracles, governance votes or forks, each of which is a determination procedure. Interpretation relocates; it does not vanish.
   292	
   293	The third counterexample attempt is pure self-help, a society in which wronged parties retaliate and nothing more. Evans-Pritchard's model of balanced opposition among Nuer lineages is the classic candidate. The reply is that the Nuer did not leave feuds to run indefinitely. Compensation through the leopard-skin chief ended them \citep{evanspritchard1940}. A society of pure self-help without any procedure for ending feuds would violate \cref{ass:cost} at every dispute, and the theorem predicts that it would not persist as a single collective. The falsifier for the necessity claim follows: a persistent collective with costly exit in which residual disputes about rule application are always settled by force of the parties or left open, without the collective dissolving.
   294	
   295	\subsection{Dependencies of the judicial function}
   296	\label{subsec:dependencies}
   297	
   298	A determination settles a dispute only if the losing party acts on it. Alexander Hamilton made the point about the federal judiciary in 1788: the judiciary ``may truly be said to have neither FORCE nor WILL, but merely judgment,'' and depends on the executive arm for the efficacy of its judgments \citep{hamilton1788}. The dependency is weaker than Hamilton's phrasing suggests.
   299	
   300	\begin{proposition}[Disjunctive dependency]
   301	\label{prop:judicial-power:disjunctive}
   302	Suppose the losing party in a determination gains $g>0$ by defying it, and complies if and only if $\ell+\sigma\ge g$, where $\ell\ge 0$ is the value it places on the procedure's legitimacy, including internalized obligation and reputation, and $\sigma\ge 0$ is the expected sanction for defiance. Then an effective determination requires $\ell>0$ or $\sigma>0$. Neither $\ell>0$ nor $\sigma>0$ is required by itself.
   303	\end{proposition}
   304	
   305	\begin{proof}
   306	If $\ell=\sigma=0$, then $\ell+\sigma=0<g$ and the loser defies, so the determination is not effective. For the second claim, a determination with $\ell\ge g$ and $\sigma=0$ is effective without sanction, and a determination with $\sigma\ge g$ and $\ell=0$ is effective without legitimacy.
   307	\end{proof}
   308	
   309	The judicial function therefore depends on the legitimation pillar or on the coercion pillar, and on neither specifically. In \cref{prop:judicial-power:disjunctive}, $\ell$ is the value a party places on complying because it regards the procedure as rightful, which Part IV calls normative legitimacy \citep{long2026ideological}, and $\sigma$ is the expected sanction for defiance, which Part V analyzes \citep{long2026coercive}. The Nuer settlement and the Ju/'hoansi talking-out rest mainly on legitimacy and the value of continued relations, while an imposed verdict in a party-state's political case rests mainly on sanction. Hamilton's executive arm is one source of $\sigma$. The reservoir of public support that James Gibson and coauthors measured for the United States Supreme Court is a source of $\ell$ \citep{gibson2003}.
   310	
   311	Because the dependency is disjunctive, it cannot be represented as two separate arcs into the judicial node. In the dependency digraph among the six functions that Part VII studies \citep{long2026formalized}, the arcs from legitimation and coercion into interpretation form a single or-condition, a hyperedge, and a proof that the digraph is strongly connected must treat them that way.
   312	
   313	The judicial function also feeds the other pillars. Interpretation changes rules through precedent, which enters rule-making through the rule of change. Reasoned judgments are public acts that shape common beliefs about what the rules are, which enters legitimation through the rule of recognition.
   314	
   315	\subsection{Functionalist objections}
   316	
   317	Carl Hempel warned that from the premise that a system needs some function one cannot infer that a particular institution exists, because functional equivalents may meet the need \citep{hempel1959}. \Cref{thm:judicial-power:necessity} respects the warning. Its conclusion is the existence of some determination procedure, and the minimal forms in \cref{tab:minimal} are exactly the functional equivalents that Hempel had in mind. Jon Elster argued that a functional explanation of an institution by its beneficial effects is legitimate only when a feedback mechanism links the effects back to the institution's persistence \citep{elster1983}. The theorem does not explain why any collective has a court. It states a condition that every persisting collective with costly exit satisfies. Robert Merton's distinction between manifest and latent functions, and his insistence on functional alternatives \citep{merton1968}, apply in the same way: courts have many latent functions, including legitimation and social control, and the theorem concerns none of them.
   318	
   319	\subsection{Necessity without capture}
   320	
   321	\begin{corollary}[Necessity does not imply capture]
   322	\label{cor:judicial-power:nonimplication}
   323	For every value $c\in[0,1]$ there are collectives that satisfy the hypotheses of \cref{thm:judicial-power:necessity}, implement adjudication, and have chain contestability $\Qchain=c$.
   324	\end{corollary}
   325	
   326	\begin{proof}
   327	\Cref{ass:arrival,ass:cost} constrain the arrival of residual disputes and the hazard attached to resolving them other than by determination. Neither refers to disclosure, access, independence or compliance. Take a collective satisfying both assumptions in which every residual dispute is resolved by determination, and assign its review links any values whose product is $c$, for example $q^{\mathrm{dis}}_t=q^{\mathrm{acc}}_t=q^{\mathrm{ind}}_t=1$ and $q^{\mathrm{cmp}}_t=c$. The hypotheses of the theorem still hold, adjudication is implemented, and $\Qchain=c$.
   328	\end{proof}
   329	
   330	The corollary is the judicial instance of the series claim that Proposition A does not imply Proposition B, which Part VII proves in general. The necessity theorem fixes that some determination procedure exists. It leaves the contestability of that procedure, and hence the persistence of captured rulings under \cref{prop:judicial-power:chain}, entirely open.
   331	
   332	\section{Literature on judicial power}
   333	\label{sec:literature}
   334	
   335	\subsection{Accounts of judicial independence}
   336	
   337	The literature on judicial power divides over one question: why would anyone who holds power allow a body to tell them what the law requires? The answers fall into four families, and the comparative analysis in \cref{sec:comparative} draws on all of them.
   338	
   339	The first family treats independent courts as a device that serves the powerful. William Landes and Richard Posner argued that an independent judiciary makes legislative deals durable, because judges who enforce statutes as enacted protect the bargains that interest groups purchased from earlier legislatures \citep{landes1975}. J.\,Mark Ramseyer argued that politicians tolerate independent courts when they expect to lose office, because a court that binds the next government protects them \citep{ramseyer1994}. Matthew Stephenson formalized the insurance logic as a repeated game between parties that alternate in power \citep{stephenson2003}, and Keith Whittington showed that politically fragmented coalitions in the United States have repeatedly supported the exercise of judicial review against their own legislative partners \citep{whittington2005}. Ran Hirschl's hegemonic preservation thesis is a sharper version: elites facing electoral decline transfer power to courts whose judges share their commitments, as he argued for Israel, Canada, New Zealand and South Africa \citep{hirschl2001,hirschl2004}. The insurance and preservation accounts agree that independence is chosen for strategic reasons. They differ on whom it protects.
   340	
   341	The second family studies courts under authoritarian rule. Tom Ginsburg and Tamir Moustafa collected evidence that authoritarian rulers use courts for social control, for legitimation, to commit credibly to investors, to discipline their own administrators and to resolve disputes within the ruling coalition \citep{ginsburg2008}. Moustafa's study of Egypt's Supreme Constitutional Court shows a regime that empowered a court to reassure investors and then found the court supporting challenges to the regime \citep{moustafa2007}. Gretchen Helmke's study of Argentina showed that judges without secure tenure rule against outgoing governments when they expect a change in power, a pattern she called strategic defection \citep{helmke2005}. These works establish that courts matter under authoritarianism and that their independence varies by case type and by the political calendar.
   342	
   343	The third family asks what makes judges' rulings stick. Georg Vanberg's study of the German Federal Constitutional Court argues that public support protects a court against noncompliance when the public can observe whether the government complies \citep{vanberg2005}. Gibson and coauthors found that the United States Supreme Court's legitimacy survived its controversial decision in the 2000 presidential election, which they attributed to a reservoir of goodwill \citep{gibson2003}. Alec Stone Sweet showed how European constitutional courts became co-legislators whose anticipated rulings shape the drafting of statutes \citep{stonesweet2000}. Mark Tushnet compared strong-form review, in which courts have the last word, with weak-form review, in which legislatures can respond, and argued that weak-form systems can protect social rights without judicial supremacy \citep{tushnet2008}.
   344	
   345	The fourth family concerns who uses courts and who wins. Marc Galanter distinguished repeat players, who litigate many similar cases, from one-shotters, and argued that repeat players come out ahead because they can play for favorable rules as well as for immediate outcomes \citep{galanter1974}. Charles Epp showed that rights revolutions depended on a support structure of lawyers, organizations and funding rather than on constitutional text alone \citep{epp1998}. Adam Bonica and Maya Sen placed judges and lawyers on a common ideological scale and found that selection channels shape the ideological composition of the American judiciary \citep{bonica2017}.
   346	
   347	Comparative legal history supplies evidence of a different kind, from religious, ecclesiastical and royal courts that the political science literature seldom examines. Wael Hallaq's work on Islamic law describes a judicial order in which state-appointed qadis applied a law developed by jurists who were not state officials \citep{hallaq2005,hallaq2009}. Harold Berman argued that the papal reforms of the late eleventh century produced the first modern Western legal system and a plurality of jurisdictions that limited every authority, including the Church \citep{berman1983}. Richard Kagan's study of litigation in Castile, David Bell's study of barristers in Paris, and Irene Fosi's study of papal justice show courts in early modern Catholic monarchies used by large numbers of ordinary litigants \citep{kagan1981,bell1994,fosi2011}. The socialist-legality literature, from Harold Berman's interpretation of Soviet law to Stanley Lubman's and Carl Minzner's studies of China, traces courts embedded in party rule \citep{berman1963,lubman1999,minzner2011}.
   348	
   349	The strategic accounts explain why independence varies but take the existence of courts for granted. The legal-historical accounts document courts in many regimes but rarely compare them on common dimensions. A shared vocabulary, the judicial layer and its contestability vector, lets both be read as answers to one question: how is the universal judicial function coupled to the other five?
   350	
   351	\subsection{The insurance model}
   352	
   353	Why would a governing coalition allow courts to bind it? The insurance account answers that independence is a hedge against losing power \citep{landes1975,ramseyer1994,stephenson2003}.
   354	
   355	\begin{proposition}[Insurance model]
   356	\label{prop:judicial-power:insurance}
   357	An incumbent chooses court independence $\iota\in[0,1]$, which persists into the next period. In each period the office holder can take an abusive action that yields it $g>0$ and costs the other side $L>0$, and the court blocks the action with probability $\iota$. The incumbent loses office before the next period with probability $\pi\in[0,1]$ and discounts the future by $\delta\in(0,1]$. Let
   358	\[
   359	\pi^{*}=\frac{g(1+\delta)}{\delta(g+L)}.
   360	\]
   361	The incumbent's expected payoff is maximized at $\iota^{*}=1$ if $\pi>\pi^{*}$, at $\iota^{*}=0$ if $\pi<\pi^{*}$, and by every $\iota\in[0,1]$ if $\pi=\pi^{*}$. The threshold $\pi^{*}$ decreases in $L$ and $\delta$ and increases in $g$. If $g\ge\delta L$, then $\pi^{*}\ge 1$ and independence is never strictly optimal.
   362	\end{proposition}
   363	
   364	\begin{proof}
   365	The incumbent's payoff is
   366	\[
   367	\Phi(\iota)=(1-\iota)g+\delta\big[(1-\pi)(1-\iota)g-\pi(1-\iota)L\big]=(1-\iota)\big[g(1+\delta)-\delta\pi(g+L)\big].
   368	\]
   369	$\Phi$ is linear in $\iota$ with slope $-\big[g(1+\delta)-\delta\pi(g+L)\big]$, which is positive when $\pi>\pi^{*}$, negative when $\pi<\pi^{*}$ and zero when $\pi=\pi^{*}$. The comparative statics follow from differentiating $\pi^{*}$: $\partial\pi^{*}/\partial L=-g(1+\delta)/[\delta(g+L)^2]<0$, $\partial\pi^{*}/\partial\delta=-g/[\delta^{2}(g+L)]<0$, and $\partial\pi^{*}/\partial g=(1+\delta)L/[\delta(g+L)^2]>0$. Finally, $\pi^{*}\ge 1$ if and only if $g(1+\delta)\ge\delta(g+L)$, which simplifies to $g\ge\delta L$.
   370	\end{proof}
   371	
   372	The model's assumptions do the work, and they should be stated plainly. Independence chosen today must persist, which requires that institutional change be costly; Landes and Posner's account relies on the same stickiness \citep{landes1975}. The court must bind whoever holds office, which excludes a court that binds only the opposition. The model is linear, which produces an all-or-nothing choice; a convex cost of independence would produce interior solutions with the same comparative statics. In the vocabulary of \cref{sec:layer}, $\iota$ is the independence component $q^{\mathrm{ind}}_t$, and when the incumbent appoints the judges through the appointment channel, keeping $\iota$ low is the same as keeping $C_{\pP\pJ}$ high.
   373	
   374	The result says that independence is more likely where the incumbent expects to lose power, where abuse by the other side would be costly, and where the incumbent is patient. It fits the variation across party-states and secular democracies described in \cref{sec:comparative}: a ruling party with a low $\pi$ has little reason to grant independence, and a fragmented democracy with a high $\pi$ has strong reason. Ramseyer used the same logic to explain why Japanese courts were less independent than American ones during a long period of single-party dominance \citep{ramseyer1994}.
   375	
   376	\begin{remark}[Strategic defection]
   377	Helmke's account of Argentine judges adds a judge-side version of the same logic \citep{helmke2005}. Assume that a judge without secure tenure is sanctioned, with loss $s>0$, only by whichever side holds power after the ruling takes effect and only if the ruling went against that side; that the case sets the incumbent against the side that would replace it; and that the merits are balanced. Ruling against the incumbent then risks $(1-\pi)s$, and ruling for it risks $\pi s$, so the judge rules against the incumbent when $\pi>1/2$. De facto independence from the incumbent rises as the incumbent's hold weakens, even when de jure independence is unchanged. The Argentine court that had favored the Menem government began to rule against it as its hold weakened, which fits this prediction.
   378	\end{remark}
   379	
   380	\subsection{Repeat players and legal aid}
   381	
   382	Galanter's argument about repeat players can be stated as a contest. A repeat player litigates many similar cases and values a favorable ruling both for the case at hand and for the precedent it sets. A one-shotter values only the case at hand.
   383	
   384	\begin{proposition}[Repeat-player contest]
   385	\label{prop:judicial-power:repeat}
   386	A repeat player $R$ and a one-shotter $O$ contest a case by spending $e_R,e_O\ge 0$, and $R$ wins with probability $p_R=me_R/(me_R+e_O)$, where $m>0$ is the relative merit of $R$'s position. $O$ values winning at $v>0$. $R$ litigates $n\ge 1$ similar cases, and a favorable ruling is worth $v$ in the present case plus $\theta v$ in each of the $n-1$ future cases through precedent, with $\theta\in[0,1]$. In the unique equilibrium with positive spending,
   387	\[
   388	p_R=\frac{m(1+\theta(n-1))}{m(1+\theta(n-1))+1}.
   389	\]
   390	With equal merits ($m=1$), $p_R>1/2$ if and only if $\theta(n-1)>0$. The probability $p_R$ is nondecreasing in $n$ and $\theta$, strictly increasing in $n$ when $\theta>0$, and strictly increasing in $\theta$ when $n>1$. If legal aid reimburses a fraction $\lambda\in[0,1)$ of $O$'s spending, the equilibrium becomes
   391	\[
   392	p_R=\frac{m(1+\theta(n-1))(1-\lambda)}{m(1+\theta(n-1))(1-\lambda)+1},
   393	\]
   394	and with equal merits the advantage is eliminated exactly when $\lambda=\theta(n-1)/(1+\theta(n-1))$.
   395	\end{proposition}
   396	
   397	\begin{proof}
   398	Let $v_R=v(1+\theta(n-1))$. Consider first a lottery contest in which players $1$ and $2$ value the prize at $A>0$ and $B>0$, choose efforts $x_1,x_2\ge 0$ at unit cost, and player $1$ wins with probability $x_1/(x_1+x_2)$. Player $1$ maximizes $Ax_1/(x_1+x_2)-x_1$ and player $2$ maximizes $Bx_2/(x_1+x_2)-x_2$. Each objective is strictly concave in the player's own effort when the other's effort is positive, and the first-order conditions are
   399	\[
   400	\frac{A\,x_2}{(x_1+x_2)^2}=1,\qquad \frac{B\,x_1}{(x_1+x_2)^2}=1 .
   401	\]
   402	Dividing gives $x_1/x_2=A/B$, so player $1$ wins with probability $A/(A+B)$, and substituting back gives the unique positive solution $x_1=A^2B/(A+B)^2$, $x_2=AB^2/(A+B)^2$.
   403	
   404	In the litigation contest, write $x_1=me_R$ and $x_2=e_O$. Then $R$'s payoff is $v_Rx_1/(x_1+x_2)-x_1/m$, which is $1/m$ times $mv_Rx_1/(x_1+x_2)-x_1$, so $R$ behaves as player $1$ with $A=mv_R$, and $O$ behaves as player $2$ with $B=v$. Hence $p_R=mv_R/(mv_R+v)$, which is the first expression. With reimbursement at rate $\lambda$, $O$'s payoff is $vx_2/(x_1+x_2)-(1-\lambda)x_2$, which is $(1-\lambda)$ times the payoff of a player with valuation $B=v/(1-\lambda)$ and unit cost; substituting gives the second expression. With $m=1$ the second expression equals $1/2$ exactly when $(1+\theta(n-1))(1-\lambda)=1$, which gives the stated $\lambda$. Finally, $p_R$ is strictly increasing in $1+\theta(n-1)$, which is nondecreasing in $n$ and $\theta$, strictly increasing in $n$ when $\theta>0$, and strictly increasing in $\theta$ when $n>1$.
   405	\end{proof}
   406	
   407	Repeat litigants win more often than one-shot litigants with equally good cases whenever rulings set precedent, because a repeat litigant bids for future cases as well as the case at hand. Legal aid removes the advantage only when the subsidy to the one-shotter matches the share of the repeat litigant's stake that comes from future cases, $\lambda=\theta(n-1)/[1+\theta(n-1)]$. Since that share rises with the repeat litigant's caseload and with the precedential weight of rulings, modest legal-aid budgets leave repeat players ahead in forums whose rulings bind later cases. \citet{galanter1974} identifies further advantages, including expertise, economies of scale and informal relations with court personnel, which add to the precedent effect modeled here and raise the subsidy needed to equalize access.
   408	
   409	The model gives one reason why resource shares buy favorable rulings, a relation Part I measures for every pillar \citep{long2026financial}, and it locates the remedy in the access component $q^{\mathrm{acc}}_t$. It is also the core of the coupling $C_{\pJ\pW}$. Workers, tenants and consumers are usually one-shotters facing repeat players, so access to courts determines whether producers can contest the rules that govern their work, which is the judicial form of the source's hypothesis about worker voice \citep{largo2026hbs}.
   410	
   411	\section{Comparative analysis across six regime types}
   412	\label{sec:comparative}
   413	
   414	\subsection{Coding conventions}
   415	
   416	Qualitative coding is the only defensible form of comparison at present, because no preregistered coding of $H$, $Q$, $U_t$ or $\Integ_t$ exists for any real polity, and the series does not report numbers without one \citep{largo2026hbs}. Each regime type is therefore compared on five questions: which institutions hold the judicial function; how concentrated control over final determinations is ($H_{\pJ,t}$) and how contestable it is ($\mathbf{q}_t$); how strongly the judicial function is coupled to the other five pillars; what preserves accountability; and which capture episodes and checks are documented.
   417	
   418	The six types are ideal types, and real polities mix them. The United States is both a market-capitalist society and a secular democracy; Sweden is both a social democracy and a secular democracy. The comparison assigns each case to the type whose distinctive pathway it best illustrates. The market-capitalist section concentrates on the channel from private resources to courts, and the secular-democracy section on the design of the relation between courts and elected bodies.
   419	
   420	\subsection{Market-capitalist societies}
   421	
   422	In market-capitalist societies the judicial function is held by courts of general jurisdiction staffed by appointed or elected judges, by a large private legal profession, by administrative tribunals and by private arbitration. The United States is the principal illustration. Federal judges are nominated by the President and confirmed by the Senate, many state judges are elected, and since \citet{marbury1803} courts have reviewed the constitutionality of statutes. Hamilton's defense of life tenure in \emph{Federalist} No.~78 rests on the claim that ``the interpretation of the laws is the proper and peculiar province of the courts'' \citep{hamilton1788}.
   423	
   424	Concentration has two levels. Across ordinary litigation, control over final determinations is spread across thousands of judges, so $H_{\pJ,t}$ is low. For constitutional questions a single court holds the last word, and concentration at the apex is high. Disclosure is high, because opinions are published with reasons. Independence is protected by tenure and salary guarantees for federal judges and is weaker for elected state judges who must raise campaign funds. Compliance by government with adverse rulings is high, and Gibson and coauthors attribute part of it to diffuse public support \citep{gibson2003}. Access is the weakest link. Litigation is costly, and the advantage of organized repeat players is the core of Galanter's argument \citep{galanter1974}.
   425	
   426	The distinctive coupling runs from resources to adjudication, the pair $C_{\pF\pJ}$ that Part I treats \citep{long2026financial}. Three channels are documented. Repeat players who can invest in rule-shaping litigation obtain favorable precedents (\cref{prop:judicial-power:repeat}). Rights litigation depends on a support structure of funded organizations \citep{epp1998}. Campaign spending in judicial elections ties litigants to judges directly.
   427	
   428	Judicial doctrine also shapes the channel from resources to rule-making. In \citet{citizensunited2010} the Supreme Court held the federal ban on independent expenditures by corporations and unions unconstitutional. The ruling changed the rules governing the path from $\pF$ to $\pP$, so the judicial pillar acted as a gatekeeper between two others. It is coupling, not capture: the decision was reached through the ordinary procedure, and capture requires privileged access and a weakened check.
   429	
   430	The clearest documented episode of capture risk is \citet{caperton2009}. While Massey's appeal of a large jury verdict was pending, Massey's chairman spent about three million dollars supporting Brent Benjamin's 2004 campaign for the West Virginia Supreme Court of Appeals. Benjamin won, declined to recuse himself, and joined the majority that reversed the verdict. The United States Supreme Court held that ``in all the circumstances of this case, due process requires recusal.'' Under \cref{def:judicial-power:capture} the facts establish privileged access and a threat to independence, but the Court did not find actual bias; it found a serious risk of it. The episode documents a capture risk and a check that operated through appeal, which is the pattern \cref{prop:judicial-power:chain} predicts when the access and independence links of the review chain hold.
   431	
   432	Outside the resource channel, market-capitalist adjudication is loosely coupled to the other pillars, with one exception in production. The coupling with legitimation runs through law schools, the bar and the public reputation of courts, professional institutions that no single coalition commands. The coupling with coercion is moderate: prosecutors decide which disputes reach the courts, and the enforcement of judgments depends on executive agencies, as Hamilton observed \citep{hamilton1788}. The exception is the arbitration clause in employment and consumer contracts, which moves disputes from public courts to private forums whose awards set no public precedent. Firms that draft such clauses are repeat players in Galanter's sense \citep{galanter1974}, so the clauses raise $C_{\pJ\pW}$ on terms set by one side.
   433	
   434	\subsection{Communist party-states}
   435	
   436	In communist party-states the judicial function is held by courts, by the procuracy, by party bodies that oversee legal work, and by a bar organized under state discipline. Harold Berman's interpretation of Soviet law described a procuracy that combined criminal prosecution with general supervision of the legality of administrative acts \citep{berman1963}. That combination puts prosecution and legality review in one organ, so $C_{\pJ\pC}$ is high by design. Eugene Huskey's history of the Soviet bar traces how advocates were organized into collegia subject to state control between 1917 and 1939 \citep{huskey1986}. In the People's Republic of China, Lubman's study of legal reform after Mao describes courts that operate inside a structure of party supervision, with judicial decisions in sensitive cases subject to review by bodies outside the bench \citep{lubman1999}.
   437	
   438	Concentration depends on the type of case. For ordinary civil and commercial disputes, determinations are made by many courts with little party involvement, and concentration is low. For politically salient cases, the last word rests with party organs, and concentration at the level of the ruling coalition is high. This is the two-tier structure of \cref{def:judicial-power:boundness}. The appointment of judges and procurators through the party's personnel system makes $C_{\pP\pJ}$ high, a coupling Part II codes through its appointment channel. Disclosure is limited for political cases. Access has grown in some areas: Peerenboom documents administrative litigation in which citizens sue government agencies \citep{peerenboom2002}. Compliance by the ruling coalition with adverse determinations is low in the political tier, so ruler-boundness is low.
   439	
   440	Ginsburg and Moustafa's list of authoritarian court functions fits the party-state well: courts discipline lower officials, resolve commercial disputes and give legal form to repression \citep{ginsburg2008}. Peter Solomon's study of Soviet criminal justice under Stalin documents courts that operated under campaign directives and pressure from party and state bodies, so that the volume and severity of prosecution followed political priorities \citep{solomon1996}. That is the strongest documented case of judicial capture in the sense of \cref{def:judicial-power:capture}: privileged direction of determinations by the party, the elimination of independent review, and material evidence in the archival record linking directives to outcomes.
   441	
   442	The party-state also contains checks, and they are documented. Kathryn Hendley's study of labor law in the late Soviet period examines how far law mattered in employment relations as legal reform began \citep{hendley1996}. Peerenboom argues that Chinese reform produced a thin rule of law in which legal rules increasingly bind officials in ordinary matters \citep{peerenboom2002}. Minzner identifies a reversal after the mid-2000s, in which the party shifted emphasis from courts toward mediation, petitioning and the maintenance of stability, and retreated from legal professionalism \citep{minzner2011}. The trajectory shows that the coupling between rule-making and adjudication in a party-state is a variable that leaders adjust, not a fixed property of the regime. The insurance model of \cref{prop:judicial-power:insurance} predicts this: a ruling party that expects to stay in power gains little from independent courts.
   443	
   444	The party-state also couples adjudication to legitimation and production, because it treats law as an instrument of education and of economic administration. Berman described Soviet law as parental, in the sense that courts were charged with educating citizens in the values of the regime as well as deciding their disputes \citep{berman1963}, which raises $C_{\pJ\pI}$. The same legal order handled labor disputes and disputes between state enterprises, so that the enforcement of plan discipline passed through adjudicative bodies \citep{berman1963,hendley1996}, which raises $C_{\pJ\pW}$.
   445	
   446	\subsection{Social democracy and democratic socialism}
   447	
   448	In social democracies the judicial function is spread across ordinary courts, specialized administrative and labor courts, ombudsmen, and parliamentary bodies that review the constitutionality of legislation. The Nordic countries illustrate a model of restrained judicial review. Sweden's Instrument of Government directs that a court which finds that a provision conflicts with a rule of fundamental law shall not apply it \citep{swedenig}. A reform in 2010 removed an earlier requirement that the conflict be manifest before a court could set a statute aside \citep{jonssoncornell2016}.
   449	
   450	Finland's constitution assigns primary review of legislative proposals to Parliament's Constitutional Law Committee, and allows courts to give primacy to the Constitution only when applying an act would be in evident conflict with it \citep{finlandconst}. Constitutional interpretation is thus shared between a parliamentary committee and the courts, which raises $C_{\pP\pJ}$ by design. Tushnet's weak-form review describes this arrangement \citep{tushnet2008}.
   451	
   452	Germany shows a different social-market pattern. Its Federal Constitutional Court exercises strong-form review, and Vanberg's study shows that its ability to obtain compliance depends on public support and on the visibility of the government's response \citep{vanberg2005}. Stone Sweet's account of constitutional courts as co-legislators draws heavily on the German and French experience \citep{stonesweet2000}. The social-democratic family therefore contains both the weakest and some of the strongest forms of constitutional review among democracies.
   453	
   454	Concentration of ordinary adjudication is low. Disclosure is high, and the ombudsman adds a channel of review outside the courts. Sweden's Parliamentary Ombudsmen are elected by the Riksdag to supervise the application of laws in public activities \citep{swedenig}. Access is supported by legal aid and by the low cost of administrative appeals. Independence is protected by constitutional prohibitions on interference: the Instrument of Government provides that neither the Riksdag nor any public authority may determine how a court shall adjudicate an individual case \citep{swedenig}. Compliance by government is high.
   455	
   456	The distinctive coupling is $C_{\pJ\pW}$, through corporatist labor adjudication. The Swedish Labour Court sits with neutral members and with members representing employer and employee interests, most of whom are appointed on the nomination of the principal labor-market organizations, and its judgment is final \citep{arbetsdomstolen}. This design gives the organized parties of production a place inside the judicial function. It also creates a recognizable risk: a forum whose members are nominated by organizations may favor those organizations over outsiders. The European Court of Human Rights addressed that risk for a related Swedish tribunal in \citet{langborger1989}, finding a violation of the right to an independent and impartial tribunal when lay assessors in a housing and tenancy court were nominated by organizations whose interests ran against the applicant's. The European Commission of Human Rights later declined to find a violation in a Labour Court case in which the nominating organizations had no common interest opposed to the applicant's \citep{stallarholmens1990}. The two rulings mark the line between coupling and capture with some precision: organizational nomination is compatible with impartiality unless the nominators share an interest in the outcome.
   457	
   458	Bo Rothstein's study of Swedish social reform emphasizes that the implementation of universal programs depends on bureaucratic organization and on citizens' trust in impartial administration \citep{rothstein1996}. That is the legitimation coupling $C_{\pJ\pI}$ in its social-democratic form: the authority of courts and ombudsmen rests on a shared belief in impartial application. We found no documented case of systematic judicial capture by an economic coalition in the Nordic sources reviewed. The risks identified in the literature are of another kind: legislative supremacy weakens the counter-majoritarian check when a governing majority is durable, and corporatist adjudication can close the forum to actors outside the organized parties.
   459	
   460	\subsection{Islamic states}
   461	
   462	Islamic states derive political legitimacy from religious law, but the institutions that interpret it have varied widely across schools, dynasties and centuries. Hallaq describes the classical arrangement as a division of labor \citep{hallaq2009}. Rulers appointed qadis to decide cases. Jurists who were not state officials developed the law, and muftis issued nonbinding opinions, fatwas, that litigants and judges consulted \citep{masud1996}. Rulers also held a jurisdiction for the redress of grievances, the \emph{mazalim}, which al-Mawardi's eleventh-century treatise on government discusses alongside the qadi's office \citep{mawardi1996}. Hallaq's further claim that the jurists' independent authority confined rulers to administrative regulation is a contested thesis \citep{hallaq2009,hallaq2013}. Sami Zubaida emphasizes the long interplay of state power and religious law \citep{zubaida2003}, and Joseph Schacht's older synthesis, which presents the classical law as largely detached from practice, is read critically by later scholarship \citep{schacht1964}.
   463	
   464	Court records contradict the older image of Islamic adjudication as unpredictable. Max Weber used the term ``kadi justice'' for an ideal type of adjudication guided by substantive considerations of the individual case rather than by general rules \citep{weber1978}. Haim Gerber tested that characterization against Ottoman court records and rejected it for the courts he examined \citep{gerber1994}. Ronald Jennings's study of the seventeenth-century court of Kayseri shows regular procedure, extensive records and wide use by ordinary inhabitants \citep{jennings1978}.
   465	
   466	Ottoman law also shows a ruler's legislation reconciled with jurists' law through interpretation rather than by command. Colin Imber's study of Ebu's-su'ud, the Ottoman chief mufti in the mid-sixteenth century, shows sultanic law, the \emph{kanun}, brought into harmony with jurists' law through juristic opinion \citep{imber1997}. Brinkley Messick's study of Yemen traces how the transmission of authoritative texts structured judicial power in a different Muslim society \citep{messick1993}.
   467	
   468	Concentration in the classical and Ottoman pattern was moderate. Qadis were numerous and appointed by the ruler, which made $C_{\pP\pJ}$ substantial, but the law they applied was developed by a scholarly class with its own institutions of training, the madrasas that George Makdisi studied \citep{makdisi1981}. The same scholars taught, issued opinions and judged, so the legitimation coupling $C_{\pJ\pI}$ was high through the ulama. Plurality of schools and the availability of independent muftis supplied contestability: a litigant could seek an opinion from a jurist outside the court.
   469	
   470	Saudi Arabia couples uncodified juristic interpretation to royal appointment and royal enforcement. Its Basic Law of Governance declares the judiciary an independent authority subject to no authority other than the Islamic Shari'ah and requires courts to apply the Shari'ah as drawn from the Qur'an and the Sunna. The same law provides that judges are appointed and their service terminated by royal order on the proposal of the supreme judicial council, assigns the implementation of judgments to the King or his deputy, and declares the King the ultimate source of the state's authorities \citep{saudibasic}. Frank Vogel's study describes a judiciary that applies largely uncodified Islamic law through judges' own interpretation, alongside royal regulations and the Board of Grievances as an administrative jurisdiction \citep{vogel2000}, and Nathan Brown's comparison of courts in Egypt and the Gulf places the Saudi system within a regional range of arrangements \citep{brown1997}. In this design $C_{\pP\pJ}$ runs through royal appointment, and $C_{\pJ\pC}$ through royal enforcement of judgments.
   471	
   472	Iran's constitution builds judicial review into rule-making by assigning the interpretation of all legislation to a council of jurists. The jurists of the Guardian Council decide whether all laws and regulations conform to Islamic criteria \citep{iranconst}. The Council has twelve members: six jurists in Islamic law selected by the Leader, and six jurists elected by the parliament from among nominees of the head of the judiciary. Every bill passed by parliament goes to the Council, which must review it within ten days. Islamic compatibility is decided by a majority of the six religious jurists, constitutional compatibility by a majority of all members. The Council also supervises elections. Hirschl treats Iran as a leading case of constitutional theocracy, in which religious interpretation is constitutionalized and assigned to a council \citep{hirschl2010}.
   473	
   474	The ordinary judiciary is tied to the same apex. The Leader appoints the head of the judiciary for five years. The constitution also provides that judges cannot be removed except after trial and proof of guilt, and that citizens may seek annulment of unlawful regulations in the Court of Administrative Justice \citep{iranconst}.
   475	
   476	The Iranian design concentrates interpretation at the apex and couples it to rule-making and legitimation. The Leader's appointments reach both the Guardian Council and the judiciary, and the Council's religious jurists decide whether legislation is valid. Asghar Schirazi documents repeated conflict between parliament and the Guardian Council in the 1980s, which led to the creation of the Expediency Council to resolve deadlocks between them \citep{schirazi1997}. Wilfried Buchta describes the Council's use of its electoral supervision to screen candidates \citep{buchta2000}. The vetting of bills and the screening of candidates are rule-making acts, a veto over legislation and over entry, and Part II codes them that way \citep{long2026political}. The judgments on which they rest, whether a bill conforms to Islamic criteria and to the Constitution, are interpretive determinations. One body performing both kinds of act is fusion, with high $C_{\pP\pJ}$.
   477	
   478	Fusion is not yet capture. A capture finding under \cref{def:judicial-power:capture} would require evidence that particular screening decisions followed privileged access and had material effect, and no such coding is attempted here. The system also contains checks: senior clerical authorities outside the state, whose plurality Muhammad Qasim Zaman documents across Muslim societies \citep{zaman2002}, and the constitutional provisions on judicial tenure and administrative review.
   479	
   480	\subsection{Catholic monarchies in early modern Europe}
   481	
   482	In the Catholic monarchies of early modern Europe the judicial function was divided among royal courts, the courts of the Church, the Inquisition, municipal and seigneurial courts, and, in the Papal State, tribunals under a ruler who was also head of the Church. Berman's account of the papal reforms of the late eleventh century places the origin of this plurality in the separation of an ecclesiastical legal order from the secular ones \citep{berman1983}. James Brundage and Richard Helmholz describe the canon law and the church courts that applied it to marriage, testaments, clerical discipline and sin \citep{brundage1995,helmholz1996}. Overlapping jurisdictions produced constant conflict over which court could hear a case, and that conflict was itself a check: litigants could sometimes choose their forum, and each jurisdiction watched the others.
   483	
   484	In Habsburg Castile the royal chanceries at Valladolid and Granada heard appeals from across the kingdom, and Kagan's study documents a large volume of litigation by ordinary subjects in the sixteenth and seventeenth centuries \citep{kagan1981}. Access was therefore substantial for those who could pay. The Spanish Inquisition, a tribunal under royal control that judged offenses against the faith, coupled adjudication with the legitimation pillar as tightly as any institution in this comparison. Henry Kamen's revisionist history argues that its scale and severity were smaller than its later reputation suggested \citep{kamen1997}, and the quantitative studies collected by Gustav Henningsen and John Tedeschi make the trial records available for testing such claims \citep{henningsen1986}. James Given's study of the medieval inquisition in Languedoc shows inquisitors using records and interrogation as techniques of power \citep{given1997}. Inquisitorial courts handed those they condemned to death to the secular authorities for execution, so the coercion coupling $C_{\pJ\pC}$ ran through the royal arm \citep{kamen1997}.
   485	
   486	In the Crown of Aragon the Justicia was an officer charged with defending the kingdom's laws against royal encroachment. J.\,H. Elliott's history of imperial Spain recounts how Philip II's pursuit of his former secretary Antonio P\'erez, who had taken refuge under Aragonese jurisdiction, led to unrest in 1591 and to the execution of the Justicia \citep{elliott1963}. The episode is a documented case of a ruler overriding a jurisdictional check by force, in which the coercion pillar removed a judicial constraint on the political one.
   487	
   488	In Bourbon France, venal officeholding gave the parlements independence from the crown and tied adjudication to private wealth. Judicial offices were purchased and heritable property, so the crown could not remove judges without compensating them \citep{doyle1996}. That security allowed the Parlement of Paris to remonstrate against royal edicts. The crown answered with the formal session called the lit de justice, which compelled registration, and in 1771 with Chancellor Maupeou's suppression and reconstruction of the parlements, which was reversed in 1774 \citep{swann1995}. Registration and remonstrance are rule-making acts in the series' classification \citep{long2026political}; the parlements' judicial power lay in their appellate jurisdiction.
   489	
   490	In that capacity the parlements contested the Church's authority. Dale Van Kley shows them intervening in the 1750s against clergy who refused sacraments to Jansenists \citep{vankley1996}, a case in which the judicial pillar checked the legitimation pillar. The property right that insulated judges from the monarch also entrenched a corporate interest in the offices themselves \citep{doyle1996}, a coupling of adjudication to resources ($C_{\pF\pJ}$). David Bell shows the Paris barristers acquiring a political voice in the same period \citep{bell1994}.
   491	
   492	The Papal State fused functions at its apex. Paolo Prodi described the pope as both spiritual head and temporal prince, ``one body and two souls'' in his subtitle \citep{prodi1987}. Fosi's study of papal justice between 1500 and 1750 shows a system of tribunals and a practice of petitioning the pope for justice that gave subjects a route around local courts \citep{fosi2011}. Petitioning raised access while concentrating final authority in the ruler. Across the Catholic monarchies, concentration was moderate, $C_{\pJ\pI}$ was high in ecclesiastical and inquisitorial courts, $C_{\pP\pJ}$ varied with the crown's success in subordinating rival jurisdictions, and contestability depended heavily on the competition among jurisdictions.
   493	
   494	\subsection{Secular democracies}
   495	
   496	In secular democracies the judicial function is held by constitutional or supreme courts, ordinary and administrative courts, judicial councils, and international courts. The defining design question is the relation between courts and elected bodies. Constitutional courts in France and Germany became co-legislators whose anticipated rulings shape legislation \citep{stonesweet2000}. Hirschl's hegemonic preservation thesis holds that constitutionalization in Israel, Canada, New Zealand and South Africa transferred power to courts at moments when established elites faced electoral threats \citep{hirschl2001,hirschl2004}. The thesis is contested on timing and motive, and it is stated below as a hypothesis with a falsifier.
   497	
   498	Rafael La Porta and coauthors coded constitutional provisions on judicial independence and constitutional review across countries and related them to economic and political freedom \citep{laporta2004}. Lars Feld and Stefan Voigt distinguished de jure from de facto independence and found that the de facto measure, not the de jure measure, was associated with economic growth in their sample \citep{feld2003}. The distinction is the central measurement problem of this Part: constitutional guarantees are not the same as observed independence.
   499	
   500	Concentration of ordinary adjudication is low in secular democracies, and concentration at the constitutional apex is high. Disclosure and access are generally high. Independence and compliance depend on the political environment. Vanberg's public-support mechanism explains why governments comply with courts whose rulings voters observe \citep{vanberg2005}, and Whittington's account explains why fragmented coalitions sustain judicial review \citep{whittington2005}. When a governing coalition becomes dominant, both mechanisms weaken.
   501	
   502	The documented capture episodes in this regime type are court-packing and court-curbing by elected governments. Steven Levitsky and Lucan Way identify the judiciary as one of the arenas in which competitive authoritarian incumbents tilt the field against opponents \citep{levitsky2010}. Argentina provides a documented case. In 1990 the government of Carlos Menem enlarged the Supreme Court from five to nine members, and the resulting court became known for an ``automatic majority'' that favored the government's interests \citep{hevia2008}. Helmke's study of the same court shows the reverse movement: as the government's hold weakened, justices began to rule against it \citep{helmke2005}. The two observations together illustrate both halves of the series' thesis. The judicial function persisted throughout; its coupling to the political pillar rose and fell with the political calendar.
   503	
   504	The couplings $C_{\pJ\pI}$, $C_{\pJ\pC}$ and $C_{\pJ\pW}$ are generally lower in secular democracies than in the other types, because law schools, prosecutors and labor organizations are governed separately from the courts. Low coupling is not guaranteed. Judicial councils dominated by the governing party, prosecutors who answer to the executive, and legal-aid systems with inadequate funding each raise one of the couplings, and each is a target of the indicators in \cref{sec:measurement}.
   505	
   506	\subsection{Summary}
   507	
   508	\Cref{tab:regimes} codes the six patterns qualitatively; its entries are not measurements.
   509	
   510	\begin{table}[p]
   511	\centering
   512	\small
   513	\caption{The judicial function across six regime types. Concentration and coupling are qualitative codings of the patterns described in the text, not numerical estimates.}
   514	\label{tab:regimes}
   515	\begin{tabularx}{\textwidth}{L{2.2cm}YYYY}
   516	\toprule
   517	Regime type & Principal holders of the judicial function & Concentration and contestability & Strongest coupling to other pillars & Documented check or capture episode \\
   518	\midrule
   519	Market-capitalist societies & Appointed and elected judges, a large private bar, administrative tribunals and private arbitration & Low concentration in ordinary cases and high concentration at the constitutional apex, with access as the weakest link & Resources to adjudication through repeat players, funded litigation and judicial campaign finance & The recusal ruling in \emph{Caperton} checked a capture risk created by campaign spending \\
   520	\addlinespace
   521	Communist party-states & Courts, the procuracy, party bodies supervising legal work, and a state-disciplined bar & Low concentration in ordinary cases and high concentration in politically salient cases, with low ruler-boundness & Rule-making to adjudication through party appointment, and coercion through the procuracy & Stalin-era courts followed campaign directives, while later reform raised legality in ordinary cases \\
   522	\addlinespace
   523	Social democracy and democratic socialism & Ordinary and administrative courts, labor courts, ombudsmen and parliamentary review committees & Low concentration, high disclosure and compliance, and restrained constitutional review in Nordic systems & Production to adjudication through labor courts with members nominated by labor-market organizations & The \emph{Langborger} ruling held that interested nominating bodies can defeat impartiality \\
   524	\addlinespace
   525	Islamic states & Qadis and muftis historically, and in modern states codified courts, royal or clerical councils and administrative courts & Moderate concentration in classical practice and high concentration at the apex in modern Iran and Saudi Arabia & Legitimation to adjudication through the ulama, and rule-making through royal or clerical appointment & Iran's Guardian Council screens legislation and candidates, while plural schools and independent muftis supplied historical checks \\
   526	\addlinespace
   527	Historical Catholic monarchies & Royal courts, parlements and chanceries, church courts, the Inquisition and papal tribunals & Moderate concentration with contestability supplied by competition among jurisdictions & Legitimation to adjudication through church courts and the Inquisition, and resources through venal offices & Maupeou's suppression of the parlements in 1771 was reversed in 1774 \\
   528	\addlinespace
   529	Secular democracies & Constitutional and supreme courts, ordinary and administrative courts, judicial councils and international courts & Low concentration in ordinary cases and high concentration at the constitutional apex, with compliance resting on public support & Rule-making to adjudication through appointment and through review that acts as co-legislation & The enlargement of the Argentine Supreme Court in 1990 produced a court aligned with the government \\
   530	\bottomrule
   531	\end{tabularx}
   532	\end{table}
   533	
   534	Every regime type has the judicial function, as \cref{thm:judicial-power:necessity} requires. The types differ little in the concentration of ordinary adjudication, which is low almost everywhere. They differ in the concentration of politically salient adjudication and in the pillar to which interpretation is most tightly coupled: resources in market capitalism, rule-making and coercion in the party-state, production in corporatist social democracy, legitimation in religious states and Catholic monarchies, and rule-making through appointment in secular democracies. Each type also contains both documented capture episodes and documented checks. Capture varies within regime types, as Proposition B's contingency predicts, rather than marking the boundary between them.
   535	
   536	\section{Mechanisms, failure modes and checks}
   537	\label{sec:mechanisms}
   538	
   539	\subsection{Judicial capture}
   540	
   541	\Cref{def:judicial-power:capture} separates three things that public debate often merges. A judge appointed by a party is not thereby captured, because appointment is the ordinary channel through which every regime staffs its courts. A ruling that favors a powerful litigant is not thereby captured, because the powerful litigant may have had the better case. Capture requires a privilege, a weakened check and an outcome linked to the privilege. \emph{Caperton} establishes the first two conditions for one case and leaves the third unresolved. Stalin-era criminal justice establishes all three for a whole system.
   542	
   543	\subsection{Failure modes}
   544	
   545	Interpretation fails as a check in four ways, one for each link of the review chain, and the formal results of \cref{sec:layer,sec:literature} identify the conditions under which each failure occurs. Disclosure fails when proceedings are sealed, reasons go unpublished or financial ties between litigants and judges stay hidden; the chain then never starts. Access fails when one side can outspend the other, and \cref{prop:judicial-power:repeat} shows that repeat players win more often for that reason even when merits are equal. Independence fails when the incumbent expects to stay in power, and \cref{prop:judicial-power:insurance} shows that such an incumbent gains nothing from granting it. Compliance fails when the governing coalition ignores adverse rulings, and \cref{prop:judicial-power:chain} shows that no strength elsewhere in the chain repairs that failure. A regime can also confine all four failures to the politically salient tier, where caseload statistics do not see them (\cref{prop:judicial-power:dualstate}).
   546	
   547	Each failure has a characteristic check. Publication duties and recusal rules protect disclosure. Legal aid, collective litigation and limits on forced arbitration protect access. Tenure security, insulated appointment and a plurality of forums protect independence. Public support that makes defiance costly, the mechanism Vanberg identified \citep{vanberg2005}, and enforcement agencies that answer to courts rather than to the beneficiary protect compliance. \Cref{sec:comparative} documents checks of each kind in every regime type, which is why capture there appears as a variable rather than a constant.
   548	
   549	\subsection{Coupling pathways and checks}
   550	
   551	The legitimation pathway runs through the body that produces authoritative readings of the law and the beliefs that support them. When the same coalition trains the jurists, licenses the lawyers, appoints the judges and controls the doctrine that justifies the regime, $C_{\pJ\pI}$ is high. The ulama in classical Islamic societies, the canonists and inquisitors of Catholic Europe, and the party's legal theorists in socialist states each occupied this position in different degrees. High $C_{\pJ\pI}$ is not capture. It becomes capture when interpretive dissent loses its institutional footing, so that no independent jurist, school or faculty can contest the authoritative reading. The historical check was plurality: of schools in Islamic law, of jurisdictions in Catholic Europe, of faculties and bar associations in modern democracies.
   552	
   553	The coercion pathway runs through the organs that bring cases and enforce judgments. When the same organ prosecutes, supervises legality and directs judges, as the Soviet procuracy and party legal organs could, $C_{\pJ\pC}$ is high and the judicial pillar loses the ability to restrain coercion. The check is separation of prosecution from adjudication and of both from the police, with judicial control over detention. The sanctioning apparatus belongs to Part V, which shows that sanctions can deter rule violations equally well whether or not they also fall more heavily on a coalition's opponents \citep{long2026coercive}. Independent adjudication is the check that ties sanctions to conduct rather than allegiance, and by \cref{prop:judicial-power:disjunctive} a judiciary with strong public legitimacy needs less coercive backing to do so.
   554	
   555	The production pathway runs through access. When workers, tenants and consumers cannot afford to litigate while employers, landlords and lenders litigate routinely, courts apply rules that the organized side has shaped. Beyond the access checks listed above, the Swedish Labour Court shows that corporatist representation of producers inside the court is a second kind of check, and the \emph{Langborger} line of cases shows its limit \citep{langborger1989,stallarholmens1990}.
   556	
   557	\section{Measurement and hypotheses}
   558	\label{sec:measurement}
   559	
   560	\subsection{Indicators}
   561	
   562	Each component of the contestability vector has observable indicators. \Cref{tab:indicators} lists them. Formal guarantees and observed functioning must be measured separately, as the source insists and as Feld and Voigt's distinction between de jure and de facto independence requires \citep{largo2026hbs,feld2003}.
   563	
   564	\begin{table}[t]
   565	\centering
   566	\small
   567	\caption{Indicators for the components of judicial contestability. Each component needs both a formal indicator and an indicator of observed functioning.}
   568	\label{tab:indicators}
   569	\begin{tabularx}{\textwidth}{L{2.4cm}YY}
   570	\toprule
   571	Component & Formal indicators & Indicators of observed functioning \\
   572	\midrule
   573	Disclosure & A legal duty to publish reasoned decisions and rules on recusal and conflict disclosure & The share of decisions published with reasons, and disclosed financial ties between litigants and judges \\
   574	Access & The availability of legal aid, the right of appeal, and limits on court fees & Legal-aid coverage, the cost of litigation relative to income, and appeal rates by litigant type \\
   575	Independence & Appointment rules, tenure security and salary protection, as coded by La Porta and coauthors & The rate of rulings against the government and judges' turnover after changes of government \\
   576	Compliance & Constitutional duties of officials to execute judgments & The share of adverse rulings against government bodies that are executed within a stated period \\
   577	\bottomrule
   578	\end{tabularx}
   579	\end{table}
   580	
   581	Cross-national expert surveys supply indicators for independence and compliance in modern states. The Varieties of Democracy project codes judicial constraints on the executive, high court independence and government compliance with the judiciary \citep{coppedge2011}. The Worldwide Governance Indicators include a rule-of-law aggregate built from many sources \citep{kaufmann2011}. La Porta and coauthors and Feld and Voigt supply formal and de facto independence codings \citep{laporta2004,feld2003}.
   582	
   583	For historical regimes the evidence lies in court records: the registers of Ottoman qadi courts \citep{jennings1978}, the registers of the French parlements \citep{swann1995}, the records of inquisitorial trials \citep{henningsen1986} and the petitions to papal tribunals \citep{fosi2011}. Each archive carries selection problems. Records survive unevenly, and the cases that reached a court were already selected by the cost of bringing them.
   584	
   585	Measurement invariance is the main threat to comparison. An expert's judgment that a court is independent may mean different things for a constitutional court in a democracy and for a qadi court in a sixteenth-century city. The source recommends testing invariance and using regime-specific models when it fails \citep{largo2026hbs}. For the judicial layer the safest comparisons are within regime types over time, and across regime types on narrowly defined events, such as the execution of adverse judgments against state bodies.
   586	
   587	\subsection{Hypotheses}
   588	
   589	The following hypotheses refine the source's general hypotheses for the judicial pillar. Each states a falsifier. None is tested in this paper.
   590	
   591	\begin{description}[font=\normalfont\itshape,leftmargin=1.5em,style=nextline]
   592	\item[HJ1, insurance.] Judicial independence, measured de facto, is greater where control of government is more fragmented or electoral turnover is more likely (\cref{prop:judicial-power:insurance}). Falsifier: no association between de facto independence and measures of electoral uncertainty in a country panel, after controlling for income and legal origin.
   593	\item[HJ2, hegemonic preservation.] The empowerment of constitutional courts follows declines in the electoral prospects of established elites \citep{hirschl2004}. Falsifier: the timing of constitutional empowerment is unrelated to prior electoral decline across cases of new constitutionalism.
   594	\item[HJ3, two tiers.] In party-states and competitive authoritarian regimes, contestability is higher for commercial and ordinary civil cases than for politically salient cases (\cref{prop:judicial-power:dualstate}). Falsifier: rates of rulings against state bodies and of compliance with them are equal across case types once case merits are controlled.
   595	\item[HJ4, repeat players.] In comparable cases repeat litigants win more often than one-shotters, and the gap narrows when legal aid expands (\cref{prop:judicial-power:repeat}). Falsifier: no gap after controlling for case merit, or no narrowing after an expansion of legal aid.
   596	\item[HJ5, juristic autonomy.] Where religious jurists hold interpretive authority independent of state salaries and appointments, the share of law produced by ruler's decree is smaller than where jurists are state employees \citep{hallaq2009}. Falsifier: no difference in the share of decree-made law between periods or states that differ in jurists' independence.
   597	\item[HJ6, venality.] Venal judicial offices protect judges against removal by the crown and also entrench corporate privilege \citep{doyle1996}. Falsifier: the frequency of remonstrance and of successful resistance to royal legislation does not differ between venal and non-venal courts or periods.
   598	\item[HJ7, fusion.] The integration $C_{\pP\pJ}$ and the unaccountable concentration of the judicial layer rise together when judges are appointed and removable by the executive or the ruling party, and judges' reputational concerns limit the rise \citep{helmke2005}. Falsifier: changes in appointment and removal rules leave rates of rulings against the government unchanged.
   599	\item[HJ8, review chains.] The probability that a documented capture link persists after disclosure is predicted better by the weakest component of the contestability vector than by an additive index (\cref{prop:judicial-power:chain}). Falsifier: an additive index predicts persistence as well as or better than the minimum component in out-of-sample tests.
   600	\end{description}
   601	
   602	HJ1, HJ3 and HJ7 can be tested with existing cross-national data. HJ4 requires case-level data with measures of merit, which exist for some court systems. HJ2, HJ5 and HJ6 require historical research designs, and their falsifiers depend on archival coding that has not yet been done on comparable terms.
   603	
   604	\section{Judgment in the Book of Revelation}
   605	\label{sec:revelation}
   606	
   607	The series reads Revelation typologically. The beast is a recurring pattern of power that claims ultimate allegiance, and Babylon is the idolatrous city of every age. The reading does not identify any present-day government, party, institution, technology or person with the beast or its mark. Futurist identifications have a long record of failure, which Robert Fuller and Bernard McGinn document \citep{fuller1995,mcginn1994}, and historicist identifications of the papacy or of any other institution with the beast belong to the history of polemic, not to analysis. The theological interpretation is the project's own and is offered as an analogy that aids comparison, not as an exegetical result. Part VII owns the shared reading; this section applies it to the judicial pillar.
   608	
   609	Revelation 13 describes political authority, war-making, worship and economic exclusion, but no court. The dragon gives the first beast ``his power, and his seat, and great authority'' (Rev 13:2), and the second beast ``causeth all, both small and great, rich and poor, free and bond, to receive a mark in their right hand, or in their foreheads: And that no man might buy or sell, save he that had the mark'' (Rev 13:16 and 13:17) \citep{kjv}. Those who would not worship the image are to be killed (Rev 13:15). In the vocabulary of this paper, the passage describes an order in which a person's standing is fixed by a mark of allegiance rather than by the application of a general rule to a particular case. There is no procedure by which the excluded can contest their exclusion. Typologically, the judicial function has been absorbed into the legitimation and coercion functions, so that $C_{\pJ\pI}$ and $C_{\pJ\pC}$ are at their maximum and contestability is zero. It is the limiting case of capture in \cref{prop:judicial-power:chain}, with every link broken: sanctions follow allegiance alone.
   610	
   611	The rest of the book does not imagine a world without judgment. It relocates judgment. The souls under the altar cry out, ``How long, O Lord, holy and true, dost thou not judge and avenge our blood on them that dwell on the earth?'' (Rev 6:10). Their complaint is the absence of a just forum. The response comes in a refrain: ``true and righteous are thy judgments'' (Rev 16:7), and ``true and righteous are his judgments: for he hath judged the great whore'' (Rev 19:2). After the fall of Babylon, John sees thrones, and ``judgment was given unto them,'' to those who had not worshipped the beast or received its mark (Rev 20:4) \citep{kjv}. The judicial function passes from the imperial order to a court that the text presents as just.
   612	
   613	The commentators agree that the beasts had a Roman referent, which is the historical anchor that the typological reading generalizes. Richard Bauckham reads Rome as the paradigm of the beast and frames the book's conflict as one between worship of the beast and faithful witness \citep{bauckham1993}. Adela Yarbro Collins reads the book as a response to a crisis that its audience perceived, whose rhetoric works through catharsis \citep{collins1984}. Craig Koester's commentary situates the beasts in the imperial politics and civic cults of Roman Asia \citep{koester2014}. J.\,Nelson Kraybill shows how participation in commerce in the province was bound up with the imperial cult \citep{kraybill1996}, which gives the mark's economic exclusion its historical referent. Elisabeth Sch\"ussler Fiorenza's reading of the book as a work about justice and judgment puts the judicial theme at its center \citep{schussler1985}.
   614	
   615	The typology maps onto the series' two propositions. The text presupposes Proposition A: judgment is a permanent function, and the question is who exercises it. The warning attaches to Proposition B: an order in which allegiance replaces adjudication, and in which those excluded have no forum. The typology does not tell us which regimes approach that limit. Only the measurement program of \cref{sec:measurement} can do that, and its results will not track the boundaries of religions or ideologies.
   616	
   617	\section{Objections and scope conditions}
   618	\label{sec:objections}
   619	
   620	The first objection is that the necessity result is empty, because a function defined so broadly that a lottery counts as a court must exist everywhere. The reply is that the definitions exclude real possibilities. A collective in which every rule application is uncontested, or in which every residual dispute ends in force, departure or abandonment, has no judicial function under them, and \cref{prop:judicial-power:exit} shows that such a collective can persist when exit is free. The theorem's content lies in \cref{ass:cost}, an empirical claim about the cost of feud and exit, and societies in which exit is costless are the test cases. The result predicts thin adjudication in them.
   621	
   622	The second objection comes from legal realism and its descendants in political science: courts are political actors whose decisions reflect judges' preferences, so the distinction between making rules and interpreting them is a fiction. Shapiro's own account of courts as political actors is the strongest version \citep{shapiro1981}. The reply is that the split between rule-making and interpretation in this series is functional, not motivational. Whatever moves judges, the activity of fixing what a general rule requires in a particular case is distinct from the activity of making the general rule. When the two are performed by the same actor, the series records fusion through $C_{\pP\pJ}$. Realism about judicial motives strengthens the case for measuring the couplings; it does not dissolve the function.
   623	
   624	The third objection is that comparing qadi courts, inquisitorial tribunals and constitutional courts imposes modern categories on institutions that understood themselves differently. The reply has two parts. The comparison concerns the function each performed, which the institutions' own records allow us to observe: who brought cases, who decided them, how the decisions were enforced and whether they could be challenged. And the comparison does not import modern evaluative standards into the coding. Weber's ideal type of ``kadi justice'' is a cautionary example of what happens when a comparative category is applied without testing it against court records, and Gerber's test of that type against Ottoman records shows how the error is corrected \citep{weber1978,gerber1994}.
   625	
   626	Four scope conditions limit the results. The necessity theorem applies to collectives with recurrent residual disputes and costly self-help and exit, and it says nothing about the quality of adjudication. The formal models are stylized, and their assumptions can fail, especially the persistence of chosen independence in the insurance model and the contest form of the repeat-player model. The comparative codings are qualitative and rest on secondary scholarship, so they illustrate pathways rather than measure them. The hypotheses are stated and not tested.
   627	
   628	\section{Conclusion}
   629	
   630	Every governance system that persists with general rules and costly exit has a procedure for deciding particular disputes that neither party controls. That is the judicial pillar in its minimal form, and it is present among the Nuer and in the Parlement of Paris, in the qadi court of Kayseri and in the Swedish Labour Court. The function is universal; its holders, concentration and couplings are not.
   631	
   632	Judicial power becomes capture when privileged access to determinations weakens a link in the chain of disclosure, access, independence and compliance, and the outcomes follow the privilege. Because the chain is multiplicative, a single broken link suffices, and additive indices can hide it. Each of the six regime types contains documented episodes of capture and documented checks against it. The ideology that legitimates a regime does not settle whether its courts bind its rulers. What settles it is the strength of the weakest link, which is a measurable property of particular institutions at particular times.
   633	
   634	\begin{thebibliography}{99}
   635	\small
   636	
   637	\bibitem[Arbetsdomstolen(2026)]{arbetsdomstolen}
   638	Arbetsdomstolen (Swedish Labour Court). 2026. ``In English.'' \url{https://www.arbetsdomstolen.se/sv/en/in-english/}. Accessed 22 October 2026.
   639	
   640	\bibitem[Bauckham(1993)]{bauckham1993}
   641	Bauckham, Richard. 1993. \emph{The Theology of the Book of Revelation}. Cambridge: Cambridge University Press. doi:10.1017/cbo9780511819858.
   642	
   643	\bibitem[Bell(1994)]{bell1994}
   644	Bell, David A. 1994. \emph{Lawyers and Citizens: The Making of a Political Elite in Old Regime France}. New York: Oxford University Press. doi:10.1093/oso/9780195076707.001.0001.
   645	
   646	\bibitem[Berman(1963)]{berman1963}
   647	Berman, Harold J. 1963. \emph{Justice in the U.S.S.R.: An Interpretation of Soviet Law}. Cambridge, MA: Harvard University Press.
   648	
   649	\bibitem[Berman(1983)]{berman1983}
   650	Berman, Harold J. 1983. \emph{Law and Revolution: The Formation of the Western Legal Tradition}. Cambridge, MA: Harvard University Press. doi:10.4159/9780674020863.
   651	
   652	\bibitem[Boehm(1999)]{boehm1999}
   653	Boehm, Christopher. 1999. \emph{Hierarchy in the Forest: The Evolution of Egalitarian Behavior}. Cambridge, MA: Harvard University Press. doi:10.2307/j.ctvjf9xr4.
   654	
   655	\bibitem[Bonica and Sen(2017)]{bonica2017}
   656	Bonica, Adam, and Maya Sen. 2017. ``A Common-Space Scaling of the American Judiciary and Legal Profession.'' \emph{Political Analysis} 25(1): 114-121. doi:10.1017/pan.2016.10.
   657	
   658	\bibitem[Brown(1997)]{brown1997}
   659	Brown, Nathan J. 1997. \emph{The Rule of Law in the Arab World: Courts in Egypt and the Gulf}. Cambridge: Cambridge University Press. doi:10.1017/cbo9780511583278.
   660	
   661	\bibitem[Brundage(1995)]{brundage1995}
   662	Brundage, James A. 1995. \emph{Medieval Canon Law}. London: Longman. doi:10.4324/9781315844596.
   663	
   664	\bibitem[Buchta(2000)]{buchta2000}
   665	Buchta, Wilfried. 2000. \emph{Who Rules Iran? The Structure of Power in the Islamic Republic}. Washington, DC: Washington Institute for Near East Policy and Konrad Adenauer Stiftung.
   666	
   667	\bibitem[{\emph{Caperton v.\ A.\,T.\ Massey Coal Co.}}(2009)]{caperton2009}
   668	\emph{Caperton v.\ A.\,T.\ Massey Coal Co.}, 556 U.S. 868 (2009). Supreme Court of the United States, No.~08-22, decided 8 June 2009. \url{https://www.law.cornell.edu/supremecourt/text/08-22}.
   669	
   670	\bibitem[{\emph{Citizens United v.\ FEC}}(2010)]{citizensunited2010}
   671	\emph{Citizens United v.\ Federal Election Commission}, 558 U.S. 310 (2010). Supreme Court of the United States, No.~08-205, decided 21 January 2010. \url{https://www.law.cornell.edu/supremecourt/text/08-205}.
   672	
   673	\bibitem[Collins(1984)]{collins1984}
   674	Collins, Adela Yarbro. 1984. \emph{Crisis and Catharsis: The Power of the Apocalypse}. Philadelphia: Westminster Press.
   675	
   676	\bibitem[Coppedge et~al.(2011)]{coppedge2011}
   677	Coppedge, Michael, John Gerring, David Altman, Michael Bernhard, Steven Fish, Allen Hicken, Matthew Kroenig, Staffan I. Lindberg, Kelly McMann, Pamela Paxton, Holli A. Semetko, Svend-Erik Skaaning, Jeffrey Staton, and Jan Teorell. 2011. ``Conceptualizing and Measuring Democracy: A New Approach.'' \emph{Perspectives on Politics} 9(2): 247-267. doi:10.1017/S1537592711000880.
   678	
   679	\bibitem[Cox et~al.(2010)]{cox2010}
   680	Cox, Michael, Gwen Arnold, and Sergio Villamayor Tomas. 2010. ``A Review of Design Principles for Community-based Natural Resource Management.'' \emph{Ecology and Society} 15(4): 38. doi:10.5751/ES-03704-150438.
   681	
   682	\bibitem[Doyle(1996)]{doyle1996}
   683	Doyle, William. 1996. \emph{Venality: The Sale of Offices in Eighteenth-Century France}. Oxford: Oxford University Press. doi:10.1093/acprof:oso/9780198205364.001.0001.
   684	
   685	\bibitem[Elliott(1963)]{elliott1963}
   686	Elliott, J.\,H. 1963. \emph{Imperial Spain 1469-1716}. London: Edward Arnold.
   687	
   688	\bibitem[Elster(1983)]{elster1983}
   689	Elster, Jon. 1983. \emph{Explaining Technical Change: A Case Study in the Philosophy of Science}. Cambridge: Cambridge University Press.
   690	
   691	\bibitem[Epp(1998)]{epp1998}
   692	Epp, Charles R. 1998. \emph{The Rights Revolution: Lawyers, Activists, and Supreme Courts in Comparative Perspective}. Chicago: University of Chicago Press. doi:10.7208/chicago/9780226772424.001.0001.
   693	
   694	\bibitem[Evans-Pritchard(1940)]{evanspritchard1940}
   695	Evans-Pritchard, E.\,E. 1940. \emph{The Nuer: A Description of the Modes of Livelihood and Political Institutions of a Nilotic People}. Oxford: Clarendon Press.
   696	
   697	\bibitem[Feld and Voigt(2003)]{feld2003}
   698	Feld, Lars P., and Stefan Voigt. 2003. ``Economic Growth and Judicial Independence: Cross-Country Evidence Using a New Set of Indicators.'' \emph{European Journal of Political Economy} 19(3): 497-527. doi:10.1016/s0176-2680(03)00017-x.
   699	
   700	\bibitem[{Finland}(1999)]{finlandconst}
   701	Finland. 1999. \emph{The Constitution of Finland}, English translation as amended to 2011. Constitute Project. \url{https://www.constituteproject.org/constitution/Finland_2011}.
   702	
   703	\bibitem[Fosi(2011)]{fosi2011}
   704	Fosi, Irene. 2011. \emph{Papal Justice: Subjects and Courts in the Papal State, 1500-1750}. Washington, DC: Catholic University of America Press. doi:10.2307/j.ctt2852kt.
   705	
   706	\bibitem[Fuller(1995)]{fuller1995}
   707	Fuller, Robert C. 1995. \emph{Naming the Antichrist: The History of an American Obsession}. New York: Oxford University Press. doi:10.1093/acprof:oso/9780195109795.001.0001.
   708	
   709	\bibitem[Galanter(1974)]{galanter1974}
   710	Galanter, Marc. 1974. ``Why the `Haves' Come Out Ahead: Speculations on the Limits of Legal Change.'' \emph{Law \& Society Review} 9(1): 95-160. doi:10.2307/3053023.
   711	
   712	\bibitem[Gerber(1994)]{gerber1994}
   713	Gerber, Haim. 1994. \emph{State, Society, and Law in Islam: Ottoman Law in Comparative Perspective}. Albany: State University of New York Press.
   714	
   715	\bibitem[Gibson et~al.(2003)]{gibson2003}
   716	Gibson, James L., Gregory A. Caldeira, and Lester Kenyatta Spence. 2003. ``The Supreme Court and the US Presidential Election of 2000: Wounds, Self-Inflicted or Otherwise?'' \emph{British Journal of Political Science} 33(4): 535-556. doi:10.1017/S0007123403000243.
   717	
   718	\bibitem[Ginsburg and Moustafa(2008)]{ginsburg2008}
   719	Ginsburg, Tom, and Tamir Moustafa, eds. 2008. \emph{Rule by Law: The Politics of Courts in Authoritarian Regimes}. Cambridge: Cambridge University Press. doi:10.1017/CBO9780511814822.
   720	
   721	\bibitem[Given(1997)]{given1997}
   722	Given, James B. 1997. \emph{Inquisition and Medieval Society: Power, Discipline, and Resistance in Languedoc}. Ithaca: Cornell University Press. doi:10.7591/9781501724954.
   723	
   724	\bibitem[Gluckman(1955)]{gluckman1955}
   725	Gluckman, Max. 1955. \emph{The Judicial Process among the Barotse of Northern Rhodesia}. Manchester: Manchester University Press.
   726	
   727	\bibitem[Gulliver(1963)]{gulliver1963}
   728	Gulliver, P.\,H. 1963. \emph{Social Control in an African Society: A Study of the Arusha, Agricultural Masai of Northern Tanganyika}. London: Routledge and Kegan Paul.
   729	
   730	\bibitem[Hallaq(2005)]{hallaq2005}
   731	Hallaq, Wael B. 2005. \emph{The Origins and Evolution of Islamic Law}. Cambridge: Cambridge University Press. doi:10.1017/cbo9780511818783.
   732	
   733	\bibitem[Hallaq(2009)]{hallaq2009}
   734	Hallaq, Wael B. 2009. \emph{An Introduction to Islamic Law}. Cambridge: Cambridge University Press. doi:10.1017/cbo9780511801044.
   735	
   736	\bibitem[Hallaq(2013)]{hallaq2013}
   737	Hallaq, Wael B. 2013. \emph{The Impossible State: Islam, Politics, and Modernity's Moral Predicament}. New York: Columbia University Press.
   738	
   739	\bibitem[Hamilton(1788)]{hamilton1788}
   740	Hamilton, Alexander. 1788. ``The Federalist No.~78: The Judiciary Department.'' \url{https://avalon.law.yale.edu/18th_century/fed78.asp}.
   741	
   742	\bibitem[Hart(1961)]{hart1961}
   743	Hart, H.\,L.\,A. 1961. \emph{The Concept of Law}. Oxford: Clarendon Press. Third edition 2012, Oxford University Press. doi:10.1093/he/9780199644704.001.0001.
   744	
   745	\bibitem[Helmholz(1996)]{helmholz1996}
   746	Helmholz, R.\,H. 1996. \emph{The Spirit of Classical Canon Law}. Athens: University of Georgia Press.
   747	
   748	\bibitem[Helmke(2005)]{helmke2005}
   749	Helmke, Gretchen. 2005. \emph{Courts under Constraints: Judges, Generals, and Presidents in Argentina}. Cambridge: Cambridge University Press. doi:10.1017/cbo9780511510144.
   750	
   751	\bibitem[Hempel(1959)]{hempel1959}
   752	Hempel, Carl G. 1959. ``The Logic of Functional Analysis.'' In \emph{Symposium on Sociological Theory}, edited by Llewellyn Gross, 271-307. New York: Harper and Row.
   753	
   754	\bibitem[Hendley(1996)]{hendley1996}
   755	Hendley, Kathryn. 1996. \emph{Trying to Make Law Matter: Legal Reform and Labor Law in the Soviet Union}. Ann Arbor: University of Michigan Press. doi:10.3998/mpub.14759.
   756	
   757	\bibitem[Hendley(2017)]{hendley2017}
   758	Hendley, Kathryn. 2017. \emph{Everyday Law in Russia}. Ithaca: Cornell University Press. doi:10.7591/9781501708107.
   759	
   760	\bibitem[Henningsen and Tedeschi(1986)]{henningsen1986}
   761	Henningsen, Gustav, and John Tedeschi, eds. 1986. \emph{The Inquisition in Early Modern Europe: Studies on Sources and Methods}. DeKalb: Northern Illinois University Press.
   762	
   763	\bibitem[Hevia(2008)]{hevia2008}
   764	Hevia, Mart\'in. 2008. ``A Short Political History of the Argentine Supreme Court.'' \emph{TheCourt.ca}, Osgoode Hall Law School, 29 February 2008. \url{https://www.yorku.ca/osgoode/thecourt/2008/02/29/a-short-political-history-of-the-argentine-supreme-court/}.
   765	
   766	\bibitem[Hirschl(2001)]{hirschl2001}
   767	Hirschl, Ran. 2001. ``The Political Origins of Judicial Empowerment through Constitutionalization: Lessons from Israel's Constitutional Revolution.'' \emph{Comparative Politics} 33(3): 315-335. doi:10.2307/422406.
   768	
   769	\bibitem[Hirschl(2004)]{hirschl2004}
   770	Hirschl, Ran. 2004. \emph{Towards Juristocracy: The Origins and Consequences of the New Constitutionalism}. Cambridge, MA: Harvard University Press. doi:10.2307/j.ctv15d81nb.
   771	
   772	\bibitem[Hirschl(2010)]{hirschl2010}
   773	Hirschl, Ran. 2010. \emph{Constitutional Theocracy}. Cambridge, MA: Harvard University Press. doi:10.2307/j.ctvjghxd5.
   774	
   775	\bibitem[Huskey(1986)]{huskey1986}
   776	Huskey, Eugene. 1986. \emph{Russian Lawyers and the Soviet State: The Origins and Development of the Soviet Bar, 1917-1939}. Princeton: Princeton University Press. doi:10.1515/9781400854516.
   777	
   778	\bibitem[Imber(1997)]{imber1997}
   779	Imber, Colin. 1997. \emph{Ebu's-su'ud: The Islamic Legal Tradition}. Stanford: Stanford University Press.
   780	
   781	\bibitem[{Iran}(1989)]{iranconst}
   782	Islamic Republic of Iran. 1979, revised 1989. \emph{Constitution of the Islamic Republic of Iran}, English translation. Constitute Project. \url{https://www.constituteproject.org/constitution/Iran_1989}.
   783	
   784	\bibitem[Jennings(1978)]{jennings1978}
   785	Jennings, Ronald C. 1978. ``Kadi, Court, and Legal Procedure in 17th C. Ottoman Kayseri.'' \emph{Studia Islamica} 48: 133-172. doi:10.2307/1595357.
   786	
   787	\bibitem[Jonsson~Cornell et~al.(2016)]{jonssoncornell2016}
   788	Jonsson Cornell, Anna, Thomas Bull, Lars Karlander, and Anna-Sara Lind. 2016. ``Developments in Swedish Constitutional Law: The Year 2015 in Review.'' \emph{I-CONnect}, 2 November 2016. \url{https://www.iconnectblog.com/developments-in-swedish-constitutional-law-the-year-of-2015-in-review/}.
   789	
   790	\bibitem[Kagan(1981)]{kagan1981}
   791	Kagan, Richard L. 1981. \emph{Lawsuits and Litigants in Castile, 1500-1700}. Chapel Hill: University of North Carolina Press.
   792	
   793	\bibitem[Kamen(1997)]{kamen1997}
   794	Kamen, Henry. 1997. \emph{The Spanish Inquisition: A Historical Revision}. New Haven: Yale University Press.
   795	
   796	\bibitem[Kaufmann et~al.(2011)]{kaufmann2011}
   797	Kaufmann, Daniel, Aart Kraay, and Massimo Mastruzzi. 2011. ``The Worldwide Governance Indicators: Methodology and Analytical Issues.'' \emph{Hague Journal on the Rule of Law} 3(2): 220-246. doi:10.1017/S1876404511200046.
   798	
   799	\bibitem[{King James Bible}(1611)]{kjv}
   800	\emph{The Holy Bible, King James Version}. 1611. Project Gutenberg eBook no.~10. \url{https://www.gutenberg.org/ebooks/10}.
   801	
   802	\bibitem[Koester(2014)]{koester2014}
   803	Koester, Craig R. 2014. \emph{Revelation: A New Translation with Introduction and Commentary}. Anchor Yale Bible 38A. New Haven: Yale University Press. doi:10.12987/9780300211030.
   804	
   805	\bibitem[Kraybill(1996)]{kraybill1996}
   806	Kraybill, J.\,Nelson. 1996. \emph{Imperial Cult and Commerce in John's Apocalypse}. Sheffield: Sheffield Academic Press.
   807	
   808	\bibitem[La~Porta et~al.(2004)]{laporta2004}
   809	La Porta, Rafael, Florencio L\'opez-de-Silanes, Cristian Pop-Eleches, and Andrei Shleifer. 2004. ``Judicial Checks and Balances.'' \emph{Journal of Political Economy} 112(2): 445-470.
   810	
   811	\bibitem[Landes and Posner(1975)]{landes1975}
   812	Landes, William M., and Richard A. Posner. 1975. ``The Independent Judiciary in an Interest-Group Perspective.'' \emph{Journal of Law and Economics} 18(3): 875-901. doi:10.1086/466849.
   813	
   814	\bibitem[{\emph{Langborger v.\ Sweden}}(1989)]{langborger1989}
   815	\emph{Langborger v.\ Sweden}, application no.~11179/84. European Court of Human Rights, judgment of 22 June 1989, Series A no.~155. \url{https://lagen.nu/dom/echr/001-57515}.
   816	
   817	\bibitem[Largo(2026)]{largo2026hbs}
   818	Largo, Mateo. 2026. ``The Hierarchy of the Beast System: Institutional Power, Elite Coordination, and Economic Dependency Across Political Regimes.'' Working paper, 14 October 2026.
   819	
   820	\bibitem[Lee(2013)]{lee2013}
   821	Lee, Richard B. 2013. \emph{The Dobe Ju/'hoansi}. 4th edition. Belmont, CA: Wadsworth, Cengage Learning.
   822	
   823	\bibitem[Levitsky and Way(2010)]{levitsky2010}
   824	Levitsky, Steven, and Lucan A. Way. 2010. \emph{Competitive Authoritarianism: Hybrid Regimes after the Cold War}. Cambridge: Cambridge University Press. doi:10.1017/CBO9780511781353.
   825	
   826	\bibitem[Long(2026a)]{long2026coercive}
   827	Long, Matthew. 2026a. ``Coercive Power and Enforcement.'' Part V of \emph{The Six Pillars of the Beast System}. Working paper, October 2026.
   828	
   829	\bibitem[Long(2026b)]{long2026financial}
   830	Long, Matthew. 2026b. ``Financial Power and Resource Command.'' Part I of \emph{The Six Pillars of the Beast System}. Working paper, October 2026.
   831	
   832	\bibitem[Long(2026c)]{long2026formalized}
   833	Long, Matthew. 2026c. ``The Formalized State: The Hierarchy of the Beast System.'' Part VII of \emph{The Six Pillars of the Beast System}. Working paper, in preparation.
   834	
   835	\bibitem[Long(2026d)]{long2026ideological}
   836	Long, Matthew. 2026d. ``Ideological Power and Legitimation.'' Part IV of \emph{The Six Pillars of the Beast System}. Working paper, October 2026.
   837	
   838	\bibitem[Long(2026e)]{long2026political}
   839	Long, Matthew. 2026e. ``Political Power and Rule Making.'' Part II of \emph{The Six Pillars of the Beast System}. Working paper, October 2026.
   840	
   841	\bibitem[Long(2026f)]{long2026productive}
   842	Long, Matthew. 2026f. ``Productive Power and Social Reproduction.'' Part VI of \emph{The Six Pillars of the Beast System}. Working paper, October 2026.
   843	
   844	\bibitem[Lubman(1999)]{lubman1999}
   845	Lubman, Stanley B. 1999. \emph{Bird in a Cage: Legal Reform in China after Mao}. Stanford: Stanford University Press.
   846	
   847	\bibitem[Makdisi(1981)]{makdisi1981}
   848	Makdisi, George. 1981. \emph{The Rise of Colleges: Institutions of Learning in Islam and the West}. Edinburgh: Edinburgh University Press. doi:10.1515/9781474470643.
   849	
   850	\bibitem[{\emph{Marbury v.\ Madison}}(1803)]{marbury1803}
   851	\emph{Marbury v.\ Madison}, 5 U.S. (1 Cranch) 137 (1803). Supreme Court of the United States.
   852	
   853	\bibitem[Masud et~al.(1996)]{masud1996}
   854	Masud, Muhammad Khalid, Brinkley Messick, and David S. Powers, eds. 1996. \emph{Islamic Legal Interpretation: Muftis and Their Fatwas}. Cambridge, MA: Harvard University Press.
   855	
   856	\bibitem[al-Mawardi(1996)]{mawardi1996}
   857	al-Mawardi, Abu al-Hasan. 1996. \emph{The Ordinances of Government} (\emph{al-Ahkam al-Sultaniyya}). Translated by Wafaa H. Wahba. Reading: Garnet Publishing.
   858	
   859	\bibitem[McGinn(1994)]{mcginn1994}
   860	McGinn, Bernard. 1994. \emph{Antichrist: Two Thousand Years of the Human Fascination with Evil}. San Francisco: HarperSanFrancisco. Reprinted 2000, Columbia University Press.
   861	
   862	\bibitem[Merton(1968)]{merton1968}
   863	Merton, Robert K. 1968. \emph{Social Theory and Social Structure}. Enlarged edition. New York: Free Press.
   864	
   865	\bibitem[Messick(1993)]{messick1993}
   866	Messick, Brinkley. 1993. \emph{The Calligraphic State: Textual Domination and History in a Muslim Society}. Berkeley: University of California Press. doi:10.1525/9780520917828.
   867	
   868	\bibitem[Minzner(2011)]{minzner2011}
   869	Minzner, Carl F. 2011. ``China's Turn against Law.'' \emph{American Journal of Comparative Law} 59(4): 935-984. doi:10.5131/ajcl.2011.0006.
   870	
   871	\bibitem[Moustafa(2007)]{moustafa2007}
   872	Moustafa, Tamir. 2007. \emph{The Struggle for Constitutional Power: Law, Politics, and Economic Development in Egypt}. Cambridge: Cambridge University Press. doi:10.1017/cbo9780511511202.
   873	
   874	\bibitem[Ostrom(1990)]{ostrom1990}
   875	Ostrom, Elinor. 1990. \emph{Governing the Commons: The Evolution of Institutions for Collective Action}. Cambridge: Cambridge University Press. doi:10.1017/CBO9780511807763.
   876	
   877	\bibitem[Peerenboom(2002)]{peerenboom2002}
   878	Peerenboom, Randall. 2002. \emph{China's Long March toward Rule of Law}. Cambridge: Cambridge University Press. doi:10.1017/cbo9780511493737.
   879	
   880	\bibitem[Prodi(1987)]{prodi1987}
   881	Prodi, Paolo. 1987. \emph{The Papal Prince: One Body and Two Souls: The Papal Monarchy in Early Modern Europe}. Translated by Susan Haskins. Cambridge: Cambridge University Press.
   882	
   883	\bibitem[Ramseyer(1994)]{ramseyer1994}
   884	Ramseyer, J.\,Mark. 1994. ``The Puzzling (In)Dependence of Courts: A Comparative Approach.'' \emph{Journal of Legal Studies} 23(2): 721-747. doi:10.1086/467943.
   885	
   886	\bibitem[Rothstein(1996)]{rothstein1996}
   887	Rothstein, Bo. 1996. \emph{The Social Democratic State: The Swedish Model and the Bureaucratic Problem of Social Reforms}. Pittsburgh: University of Pittsburgh Press.
   888	
   889	\bibitem[{Saudi Arabia}(1992)]{saudibasic}
   890	Kingdom of Saudi Arabia. 1992. \emph{Basic Law of Governance}, English translation as amended to 2013. Constitute Project. \url{https://www.constituteproject.org/constitution/Saudi_Arabia_2013}.
   891	
   892	\bibitem[Schacht(1964)]{schacht1964}
   893	Schacht, Joseph. 1964. \emph{An Introduction to Islamic Law}. Oxford: Clarendon Press.
   894	
   895	\bibitem[Schirazi(1997)]{schirazi1997}
   896	Schirazi, Asghar. 1997. \emph{The Constitution of Iran: Politics and the State in the Islamic Republic}. London: I.\,B. Tauris.
   897	
   898	\bibitem[Sch\"ussler~Fiorenza(1985)]{schussler1985}
   899	Sch\"ussler Fiorenza, Elisabeth. 1985. \emph{The Book of Revelation: Justice and Judgment}. Philadelphia: Fortress Press.
   900	
   901	\bibitem[Shapiro(1981)]{shapiro1981}
   902	Shapiro, Martin. 1981. \emph{Courts: A Comparative and Political Analysis}. Chicago: University of Chicago Press. doi:10.7208/chicago/9780226161341.001.0001.
   903	
   904	\bibitem[Solomon(1996)]{solomon1996}
   905	Solomon, Peter H., Jr. 1996. \emph{Soviet Criminal Justice under Stalin}. Cambridge: Cambridge University Press.
   906	
   907	\bibitem[{\emph{Stallarholmens v.\ Sweden}}(1990)]{stallarholmens1990}
   908	\emph{Stallarholmens Pl\aa tslageri o Ventilation Handelsbolag v.\ Sweden}, application no.~12733/87. European Commission of Human Rights, decision of 7 September 1990. \url{https://lagen.nu/dom/echr/001-727}.
   909	
   910	\bibitem[Stephenson(2003)]{stephenson2003}
   911	Stephenson, Matthew C. 2003. ``When the Devil Turns\ldots: The Political Foundations of Independent Judicial Review.'' \emph{Journal of Legal Studies} 32(1): 59-89. doi:10.1086/342038.
   912	
   913	\bibitem[Stone~Sweet(2000)]{stonesweet2000}
   914	Stone Sweet, Alec. 2000. \emph{Governing with Judges: Constitutional Politics in Europe}. Oxford: Oxford University Press. doi:10.1093/0198297718.001.0001.
   915	
   916	\bibitem[Swann(1995)]{swann1995}
   917	Swann, Julian. 1995. \emph{Politics and the Parlement of Paris under Louis XV, 1754-1774}. Cambridge: Cambridge University Press. doi:10.1017/cbo9780511661013.
   918	
   919	\bibitem[{Sweden}(1974)]{swedenig}
   920	Sweden. 1974. \emph{The Instrument of Government}, English translation as amended to 2012. Constitute Project. \url{https://www.constituteproject.org/constitution/Sweden_2012}.
   921	
   922	\bibitem[Tamanaha(2004)]{tamanaha2004}
   923	Tamanaha, Brian Z. 2004. \emph{On the Rule of Law: History, Politics, Theory}. Cambridge: Cambridge University Press. doi:10.1017/CBO9780511812378.
   924	
   925	\bibitem[Tushnet(2008)]{tushnet2008}
   926	Tushnet, Mark. 2008. \emph{Weak Courts, Strong Rights: Judicial Review and Social Welfare Rights in Comparative Constitutional Law}. Princeton: Princeton University Press. doi:10.1515/9781400828159.
   927	
   928	\bibitem[Van~Kley(1996)]{vankley1996}
   929	Van Kley, Dale K. 1996. \emph{The Religious Origins of the French Revolution: From Calvin to the Civil Constitution, 1560-1791}. New Haven: Yale University Press.
   930	
   931	\bibitem[Vanberg(2005)]{vanberg2005}
   932	Vanberg, Georg. 2005. \emph{The Politics of Constitutional Review in Germany}. Cambridge: Cambridge University Press. doi:10.1017/cbo9780511510427.
   933	
   934	\bibitem[Vogel(2000)]{vogel2000}
   935	Vogel, Frank E. 2000. \emph{Islamic Law and the Legal System of Saudi Arabia}. Leiden: Brill. doi:10.1163/9789047400165.
   936	
   937	\bibitem[Weber(1978)]{weber1978}
   938	Weber, Max. 1978. \emph{Economy and Society: An Outline of Interpretive Sociology}. Edited by Guenther Roth and Claus Wittich. Berkeley: University of California Press.
   939	
   940	\bibitem[Whittington(2005)]{whittington2005}
   941	Whittington, Keith E. 2005. ``\thinspace`Interpose Your Friendly Hand': Political Supports for the Exercise of Judicial Review by the United States Supreme Court.'' \emph{American Political Science Review} 99(4): 583-596. doi:10.1017/s0003055405051890.
   942	
   943	\bibitem[Wiessner(2005)]{wiessner2005}
   944	Wiessner, Polly. 2005. ``Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity?'' \emph{Human Nature} 16(2): 115-145. doi:10.1007/s12110-005-1000-9.
   945	
   946	\bibitem[Woodburn(1982)]{woodburn1982}
   947	Woodburn, James. 1982. ``Egalitarian Societies.'' \emph{Man}, new series, 17(3): 431-451. doi:10.2307/2801707.
   948	
   949	\bibitem[Zaman(2002)]{zaman2002}
   950	Zaman, Muhammad Qasim. 2002. \emph{The Ulama in Contemporary Islam: Custodians of Change}. Princeton: Princeton University Press. doi:10.2307/j.ctt7rh2s.
   951	
   952	\bibitem[Zubaida(2003)]{zubaida2003}
   953	Zubaida, Sami. 2003. \emph{Law and Power in the Islamic World}. London: I.\,B. Tauris. doi:10.5040/9780755612208.
   954	
   955	\end{thebibliography}
   956	
   957	\end{document}

hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '401,680p' papers/latex/judicial-power.tex | nl -ba -v 401" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   401	\]
   402	Dividing gives $x_1/x_2=A/B$, so player $1$ wins with probability $A/(A+B)$, and substituting back gives the unique positive solution $x_1=A^2B/(A+B)^2$, $x_2=AB^2/(A+B)^2$.
   403	
   404	In the litigation contest, write $x_1=me_R$ and $x_2=e_O$. Then $R$'s payoff is $v_Rx_1/(x_1+x_2)-x_1/m$, which is $1/m$ times $mv_Rx_1/(x_1+x_2)-x_1$, so $R$ behaves as player $1$ with $A=mv_R$, and $O$ behaves as player $2$ with $B=v$. Hence $p_R=mv_R/(mv_R+v)$, which is the first expression. With reimbursement at rate $\lambda$, $O$'s payoff is $vx_2/(x_1+x_2)-(1-\lambda)x_2$, which is $(1-\lambda)$ times the payoff of a player with valuation $B=v/(1-\lambda)$ and unit cost; substituting gives the second expression. With $m=1$ the second expression equals $1/2$ exactly when $(1+\theta(n-1))(1-\lambda)=1$, which gives the stated $\lambda$. Finally, $p_R$ is strictly increasing in $1+\theta(n-1)$, which is nondecreasing in $n$ and $\theta$, strictly increasing in $n$ when $\theta>0$, and strictly increasing in $\theta$ when $n>1$.
   405	\end{proof}
   406	
   407	Repeat litigants win more often than one-shot litigants with equally good cases whenever rulings set precedent, because a repeat litigant bids for future cases as well as the case at hand. Legal aid removes the advantage only when the subsidy to the one-shotter matches the share of the repeat litigant's stake that comes from future cases, $\lambda=\theta(n-1)/[1+\theta(n-1)]$. Since that share rises with the repeat litigant's caseload and with the precedential weight of rulings, modest legal-aid budgets leave repeat players ahead in forums whose rulings bind later cases. \citet{galanter1974} identifies further advantages, including expertise, economies of scale and informal relations with court personnel, which add to the precedent effect modeled here and raise the subsidy needed to equalize access.
   408	
   409	The model gives one reason why resource shares buy favorable rulings, a relation Part I measures for every pillar \citep{long2026financial}, and it locates the remedy in the access component $q^{\mathrm{acc}}_t$. It is also the core of the coupling $C_{\pJ\pW}$. Workers, tenants and consumers are usually one-shotters facing repeat players, so access to courts determines whether producers can contest the rules that govern their work, which is the judicial form of the source's hypothesis about worker voice \citep{largo2026hbs}.
   410	
   411	\section{Comparative analysis across six regime types}
   412	\label{sec:comparative}
   413	
   414	\subsection{Coding conventions}
   415	
   416	Qualitative coding is the only defensible form of comparison at present, because no preregistered coding of $H$, $Q$, $U_t$ or $\Integ_t$ exists for any real polity, and the series does not report numbers without one \citep{largo2026hbs}. Each regime type is therefore compared on five questions: which institutions hold the judicial function; how concentrated control over final determinations is ($H_{\pJ,t}$) and how contestable it is ($\mathbf{q}_t$); how strongly the judicial function is coupled to the other five pillars; what preserves accountability; and which capture episodes and checks are documented.
   417	
   418	The six types are ideal types, and real polities mix them. The United States is both a market-capitalist society and a secular democracy; Sweden is both a social democracy and a secular democracy. The comparison assigns each case to the type whose distinctive pathway it best illustrates. The market-capitalist section concentrates on the channel from private resources to courts, and the secular-democracy section on the design of the relation between courts and elected bodies.
   419	
   420	\subsection{Market-capitalist societies}
   421	
   422	In market-capitalist societies the judicial function is held by courts of general jurisdiction staffed by appointed or elected judges, by a large private legal profession, by administrative tribunals and by private arbitration. The United States is the principal illustration. Federal judges are nominated by the President and confirmed by the Senate, many state judges are elected, and since \citet{marbury1803} courts have reviewed the constitutionality of statutes. Hamilton's defense of life tenure in \emph{Federalist} No.~78 rests on the claim that ``the interpretation of the laws is the proper and peculiar province of the courts'' \citep{hamilton1788}.
   423	
   424	Concentration has two levels. Across ordinary litigation, control over final determinations is spread across thousands of judges, so $H_{\pJ,t}$ is low. For constitutional questions a single court holds the last word, and concentration at the apex is high. Disclosure is high, because opinions are published with reasons. Independence is protected by tenure and salary guarantees for federal judges and is weaker for elected state judges who must raise campaign funds. Compliance by government with adverse rulings is high, and Gibson and coauthors attribute part of it to diffuse public support \citep{gibson2003}. Access is the weakest link. Litigation is costly, and the advantage of organized repeat players is the core of Galanter's argument \citep{galanter1974}.
   425	
   426	The distinctive coupling runs from resources to adjudication, the pair $C_{\pF\pJ}$ that Part I treats \citep{long2026financial}. Three channels are documented. Repeat players who can invest in rule-shaping litigation obtain favorable precedents (\cref{prop:judicial-power:repeat}). Rights litigation depends on a support structure of funded organizations \citep{epp1998}. Campaign spending in judicial elections ties litigants to judges directly.
   427	
   428	Judicial doctrine also shapes the channel from resources to rule-making. In \citet{citizensunited2010} the Supreme Court held the federal ban on independent expenditures by corporations and unions unconstitutional. The ruling changed the rules governing the path from $\pF$ to $\pP$, so the judicial pillar acted as a gatekeeper between two others. It is coupling, not capture: the decision was reached through the ordinary procedure, and capture requires privileged access and a weakened check.
   429	
   430	The clearest documented episode of capture risk is \citet{caperton2009}. While Massey's appeal of a large jury verdict was pending, Massey's chairman spent about three million dollars supporting Brent Benjamin's 2004 campaign for the West Virginia Supreme Court of Appeals. Benjamin won, declined to recuse himself, and joined the majority that reversed the verdict. The United States Supreme Court held that ``in all the circumstances of this case, due process requires recusal.'' Under \cref{def:judicial-power:capture} the facts establish privileged access and a threat to independence, but the Court did not find actual bias; it found a serious risk of it. The episode documents a capture risk and a check that operated through appeal, which is the pattern \cref{prop:judicial-power:chain} predicts when the access and independence links of the review chain hold.
   431	
   432	Outside the resource channel, market-capitalist adjudication is loosely coupled to the other pillars, with one exception in production. The coupling with legitimation runs through law schools, the bar and the public reputation of courts, professional institutions that no single coalition commands. The coupling with coercion is moderate: prosecutors decide which disputes reach the courts, and the enforcement of judgments depends on executive agencies, as Hamilton observed \citep{hamilton1788}. The exception is the arbitration clause in employment and consumer contracts, which moves disputes from public courts to private forums whose awards set no public precedent. Firms that draft such clauses are repeat players in Galanter's sense \citep{galanter1974}, so the clauses raise $C_{\pJ\pW}$ on terms set by one side.
   433	
   434	\subsection{Communist party-states}
   435	
   436	In communist party-states the judicial function is held by courts, by the procuracy, by party bodies that oversee legal work, and by a bar organized under state discipline. Harold Berman's interpretation of Soviet law described a procuracy that combined criminal prosecution with general supervision of the legality of administrative acts \citep{berman1963}. That combination puts prosecution and legality review in one organ, so $C_{\pJ\pC}$ is high by design. Eugene Huskey's history of the Soviet bar traces how advocates were organized into collegia subject to state control between 1917 and 1939 \citep{huskey1986}. In the People's Republic of China, Lubman's study of legal reform after Mao describes courts that operate inside a structure of party supervision, with judicial decisions in sensitive cases subject to review by bodies outside the bench \citep{lubman1999}.
   437	
   438	Concentration depends on the type of case. For ordinary civil and commercial disputes, determinations are made by many courts with little party involvement, and concentration is low. For politically salient cases, the last word rests with party organs, and concentration at the level of the ruling coalition is high. This is the two-tier structure of \cref{def:judicial-power:boundness}. The appointment of judges and procurators through the party's personnel system makes $C_{\pP\pJ}$ high, a coupling Part II codes through its appointment channel. Disclosure is limited for political cases. Access has grown in some areas: Peerenboom documents administrative litigation in which citizens sue government agencies \citep{peerenboom2002}. Compliance by the ruling coalition with adverse determinations is low in the political tier, so ruler-boundness is low.
   439	
   440	Ginsburg and Moustafa's list of authoritarian court functions fits the party-state well: courts discipline lower officials, resolve commercial disputes and give legal form to repression \citep{ginsburg2008}. Peter Solomon's study of Soviet criminal justice under Stalin documents courts that operated under campaign directives and pressure from party and state bodies, so that the volume and severity of prosecution followed political priorities \citep{solomon1996}. That is the strongest documented case of judicial capture in the sense of \cref{def:judicial-power:capture}: privileged direction of determinations by the party, the elimination of independent review, and material evidence in the archival record linking directives to outcomes.
   441	
   442	The party-state also contains checks, and they are documented. Kathryn Hendley's study of labor law in the late Soviet period examines how far law mattered in employment relations as legal reform began \citep{hendley1996}. Peerenboom argues that Chinese reform produced a thin rule of law in which legal rules increasingly bind officials in ordinary matters \citep{peerenboom2002}. Minzner identifies a reversal after the mid-2000s, in which the party shifted emphasis from courts toward mediation, petitioning and the maintenance of stability, and retreated from legal professionalism \citep{minzner2011}. The trajectory shows that the coupling between rule-making and adjudication in a party-state is a variable that leaders adjust, not a fixed property of the regime. The insurance model of \cref{prop:judicial-power:insurance} predicts this: a ruling party that expects to stay in power gains little from independent courts.
   443	
   444	The party-state also couples adjudication to legitimation and production, because it treats law as an instrument of education and of economic administration. Berman described Soviet law as parental, in the sense that courts were charged with educating citizens in the values of the regime as well as deciding their disputes \citep{berman1963}, which raises $C_{\pJ\pI}$. The same legal order handled labor disputes and disputes between state enterprises, so that the enforcement of plan discipline passed through adjudicative bodies \citep{berman1963,hendley1996}, which raises $C_{\pJ\pW}$.
   445	
   446	\subsection{Social democracy and democratic socialism}
   447	
   448	In social democracies the judicial function is spread across ordinary courts, specialized administrative and labor courts, ombudsmen, and parliamentary bodies that review the constitutionality of legislation. The Nordic countries illustrate a model of restrained judicial review. Sweden's Instrument of Government directs that a court which finds that a provision conflicts with a rule of fundamental law shall not apply it \citep{swedenig}. A reform in 2010 removed an earlier requirement that the conflict be manifest before a court could set a statute aside \citep{jonssoncornell2016}.
   449	
   450	Finland's constitution assigns primary review of legislative proposals to Parliament's Constitutional Law Committee, and allows courts to give primacy to the Constitution only when applying an act would be in evident conflict with it \citep{finlandconst}. Constitutional interpretation is thus shared between a parliamentary committee and the courts, which raises $C_{\pP\pJ}$ by design. Tushnet's weak-form review describes this arrangement \citep{tushnet2008}.
   451	
   452	Germany shows a different social-market pattern. Its Federal Constitutional Court exercises strong-form review, and Vanberg's study shows that its ability to obtain compliance depends on public support and on the visibility of the government's response \citep{vanberg2005}. Stone Sweet's account of constitutional courts as co-legislators draws heavily on the German and French experience \citep{stonesweet2000}. The social-democratic family therefore contains both the weakest and some of the strongest forms of constitutional review among democracies.
   453	
   454	Concentration of ordinary adjudication is low. Disclosure is high, and the ombudsman adds a channel of review outside the courts. Sweden's Parliamentary Ombudsmen are elected by the Riksdag to supervise the application of laws in public activities \citep{swedenig}. Access is supported by legal aid and by the low cost of administrative appeals. Independence is protected by constitutional prohibitions on interference: the Instrument of Government provides that neither the Riksdag nor any public authority may determine how a court shall adjudicate an individual case \citep{swedenig}. Compliance by government is high.
   455	
   456	The distinctive coupling is $C_{\pJ\pW}$, through corporatist labor adjudication. The Swedish Labour Court sits with neutral members and with members representing employer and employee interests, most of whom are appointed on the nomination of the principal labor-market organizations, and its judgment is final \citep{arbetsdomstolen}. This design gives the organized parties of production a place inside the judicial function. It also creates a recognizable risk: a forum whose members are nominated by organizations may favor those organizations over outsiders. The European Court of Human Rights addressed that risk for a related Swedish tribunal in \citet{langborger1989}, finding a violation of the right to an independent and impartial tribunal when lay assessors in a housing and tenancy court were nominated by organizations whose interests ran against the applicant's. The European Commission of Human Rights later declined to find a violation in a Labour Court case in which the nominating organizations had no common interest opposed to the applicant's \citep{stallarholmens1990}. The two rulings mark the line between coupling and capture with some precision: organizational nomination is compatible with impartiality unless the nominators share an interest in the outcome.
   457	
   458	Bo Rothstein's study of Swedish social reform emphasizes that the implementation of universal programs depends on bureaucratic organization and on citizens' trust in impartial administration \citep{rothstein1996}. That is the legitimation coupling $C_{\pJ\pI}$ in its social-democratic form: the authority of courts and ombudsmen rests on a shared belief in impartial application. We found no documented case of systematic judicial capture by an economic coalition in the Nordic sources reviewed. The risks identified in the literature are of another kind: legislative supremacy weakens the counter-majoritarian check when a governing majority is durable, and corporatist adjudication can close the forum to actors outside the organized parties.
   459	
   460	\subsection{Islamic states}
   461	
   462	Islamic states derive political legitimacy from religious law, but the institutions that interpret it have varied widely across schools, dynasties and centuries. Hallaq describes the classical arrangement as a division of labor \citep{hallaq2009}. Rulers appointed qadis to decide cases. Jurists who were not state officials developed the law, and muftis issued nonbinding opinions, fatwas, that litigants and judges consulted \citep{masud1996}. Rulers also held a jurisdiction for the redress of grievances, the \emph{mazalim}, which al-Mawardi's eleventh-century treatise on government discusses alongside the qadi's office \citep{mawardi1996}. Hallaq's further claim that the jurists' independent authority confined rulers to administrative regulation is a contested thesis \citep{hallaq2009,hallaq2013}. Sami Zubaida emphasizes the long interplay of state power and religious law \citep{zubaida2003}, and Joseph Schacht's older synthesis, which presents the classical law as largely detached from practice, is read critically by later scholarship \citep{schacht1964}.
   463	
   464	Court records contradict the older image of Islamic adjudication as unpredictable. Max Weber used the term ``kadi justice'' for an ideal type of adjudication guided by substantive considerations of the individual case rather than by general rules \citep{weber1978}. Haim Gerber tested that characterization against Ottoman court records and rejected it for the courts he examined \citep{gerber1994}. Ronald Jennings's study of the seventeenth-century court of Kayseri shows regular procedure, extensive records and wide use by ordinary inhabitants \citep{jennings1978}.
   465	
   466	Ottoman law also shows a ruler's legislation reconciled with jurists' law through interpretation rather than by command. Colin Imber's study of Ebu's-su'ud, the Ottoman chief mufti in the mid-sixteenth century, shows sultanic law, the \emph{kanun}, brought into harmony with jurists' law through juristic opinion \citep{imber1997}. Brinkley Messick's study of Yemen traces how the transmission of authoritative texts structured judicial power in a different Muslim society \citep{messick1993}.
   467	
   468	Concentration in the classical and Ottoman pattern was moderate. Qadis were numerous and appointed by the ruler, which made $C_{\pP\pJ}$ substantial, but the law they applied was developed by a scholarly class with its own institutions of training, the madrasas that George Makdisi studied \citep{makdisi1981}. The same scholars taught, issued opinions and judged, so the legitimation coupling $C_{\pJ\pI}$ was high through the ulama. Plurality of schools and the availability of independent muftis supplied contestability: a litigant could seek an opinion from a jurist outside the court.
   469	
   470	Saudi Arabia couples uncodified juristic interpretation to royal appointment and royal enforcement. Its Basic Law of Governance declares the judiciary an independent authority subject to no authority other than the Islamic Shari'ah and requires courts to apply the Shari'ah as drawn from the Qur'an and the Sunna. The same law provides that judges are appointed and their service terminated by royal order on the proposal of the supreme judicial council, assigns the implementation of judgments to the King or his deputy, and declares the King the ultimate source of the state's authorities \citep{saudibasic}. Frank Vogel's study describes a judiciary that applies largely uncodified Islamic law through judges' own interpretation, alongside royal regulations and the Board of Grievances as an administrative jurisdiction \citep{vogel2000}, and Nathan Brown's comparison of courts in Egypt and the Gulf places the Saudi system within a regional range of arrangements \citep{brown1997}. In this design $C_{\pP\pJ}$ runs through royal appointment, and $C_{\pJ\pC}$ through royal enforcement of judgments.
   471	
   472	Iran's constitution builds judicial review into rule-making by assigning the interpretation of all legislation to a council of jurists. The jurists of the Guardian Council decide whether all laws and regulations conform to Islamic criteria \citep{iranconst}. The Council has twelve members: six jurists in Islamic law selected by the Leader, and six jurists elected by the parliament from among nominees of the head of the judiciary. Every bill passed by parliament goes to the Council, which must review it within ten days. Islamic compatibility is decided by a majority of the six religious jurists, constitutional compatibility by a majority of all members. The Council also supervises elections. Hirschl treats Iran as a leading case of constitutional theocracy, in which religious interpretation is constitutionalized and assigned to a council \citep{hirschl2010}.
   473	
   474	The ordinary judiciary is tied to the same apex. The Leader appoints the head of the judiciary for five years. The constitution also provides that judges cannot be removed except after trial and proof of guilt, and that citizens may seek annulment of unlawful regulations in the Court of Administrative Justice \citep{iranconst}.
   475	
   476	The Iranian design concentrates interpretation at the apex and couples it to rule-making and legitimation. The Leader's appointments reach both the Guardian Council and the judiciary, and the Council's religious jurists decide whether legislation is valid. Asghar Schirazi documents repeated conflict between parliament and the Guardian Council in the 1980s, which led to the creation of the Expediency Council to resolve deadlocks between them \citep{schirazi1997}. Wilfried Buchta describes the Council's use of its electoral supervision to screen candidates \citep{buchta2000}. The vetting of bills and the screening of candidates are rule-making acts, a veto over legislation and over entry, and Part II codes them that way \citep{long2026political}. The judgments on which they rest, whether a bill conforms to Islamic criteria and to the Constitution, are interpretive determinations. One body performing both kinds of act is fusion, with high $C_{\pP\pJ}$.
   477	
   478	Fusion is not yet capture. A capture finding under \cref{def:judicial-power:capture} would require evidence that particular screening decisions followed privileged access and had material effect, and no such coding is attempted here. The system also contains checks: senior clerical authorities outside the state, whose plurality Muhammad Qasim Zaman documents across Muslim societies \citep{zaman2002}, and the constitutional provisions on judicial tenure and administrative review.
   479	
   480	\subsection{Catholic monarchies in early modern Europe}
   481	
   482	In the Catholic monarchies of early modern Europe the judicial function was divided among royal courts, the courts of the Church, the Inquisition, municipal and seigneurial courts, and, in the Papal State, tribunals under a ruler who was also head of the Church. Berman's account of the papal reforms of the late eleventh century places the origin of this plurality in the separation of an ecclesiastical legal order from the secular ones \citep{berman1983}. James Brundage and Richard Helmholz describe the canon law and the church courts that applied it to marriage, testaments, clerical discipline and sin \citep{brundage1995,helmholz1996}. Overlapping jurisdictions produced constant conflict over which court could hear a case, and that conflict was itself a check: litigants could sometimes choose their forum, and each jurisdiction watched the others.
   483	
   484	In Habsburg Castile the royal chanceries at Valladolid and Granada heard appeals from across the kingdom, and Kagan's study documents a large volume of litigation by ordinary subjects in the sixteenth and seventeenth centuries \citep{kagan1981}. Access was therefore substantial for those who could pay. The Spanish Inquisition, a tribunal under royal control that judged offenses against the faith, coupled adjudication with the legitimation pillar as tightly as any institution in this comparison. Henry Kamen's revisionist history argues that its scale and severity were smaller than its later reputation suggested \citep{kamen1997}, and the quantitative studies collected by Gustav Henningsen and John Tedeschi make the trial records available for testing such claims \citep{henningsen1986}. James Given's study of the medieval inquisition in Languedoc shows inquisitors using records and interrogation as techniques of power \citep{given1997}. Inquisitorial courts handed those they condemned to death to the secular authorities for execution, so the coercion coupling $C_{\pJ\pC}$ ran through the royal arm \citep{kamen1997}.
   485	
   486	In the Crown of Aragon the Justicia was an officer charged with defending the kingdom's laws against royal encroachment. J.\,H. Elliott's history of imperial Spain recounts how Philip II's pursuit of his former secretary Antonio P\'erez, who had taken refuge under Aragonese jurisdiction, led to unrest in 1591 and to the execution of the Justicia \citep{elliott1963}. The episode is a documented case of a ruler overriding a jurisdictional check by force, in which the coercion pillar removed a judicial constraint on the political one.
   487	
   488	In Bourbon France, venal officeholding gave the parlements independence from the crown and tied adjudication to private wealth. Judicial offices were purchased and heritable property, so the crown could not remove judges without compensating them \citep{doyle1996}. That security allowed the Parlement of Paris to remonstrate against royal edicts. The crown answered with the formal session called the lit de justice, which compelled registration, and in 1771 with Chancellor Maupeou's suppression and reconstruction of the parlements, which was reversed in 1774 \citep{swann1995}. Registration and remonstrance are rule-making acts in the series' classification \citep{long2026political}; the parlements' judicial power lay in their appellate jurisdiction.
   489	
   490	In that capacity the parlements contested the Church's authority. Dale Van Kley shows them intervening in the 1750s against clergy who refused sacraments to Jansenists \citep{vankley1996}, a case in which the judicial pillar checked the legitimation pillar. The property right that insulated judges from the monarch also entrenched a corporate interest in the offices themselves \citep{doyle1996}, a coupling of adjudication to resources ($C_{\pF\pJ}$). David Bell shows the Paris barristers acquiring a political voice in the same period \citep{bell1994}.
   491	
   492	The Papal State fused functions at its apex. Paolo Prodi described the pope as both spiritual head and temporal prince, ``one body and two souls'' in his subtitle \citep{prodi1987}. Fosi's study of papal justice between 1500 and 1750 shows a system of tribunals and a practice of petitioning the pope for justice that gave subjects a route around local courts \citep{fosi2011}. Petitioning raised access while concentrating final authority in the ruler. Across the Catholic monarchies, concentration was moderate, $C_{\pJ\pI}$ was high in ecclesiastical and inquisitorial courts, $C_{\pP\pJ}$ varied with the crown's success in subordinating rival jurisdictions, and contestability depended heavily on the competition among jurisdictions.
   493	
   494	\subsection{Secular democracies}
   495	
   496	In secular democracies the judicial function is held by constitutional or supreme courts, ordinary and administrative courts, judicial councils, and international courts. The defining design question is the relation between courts and elected bodies. Constitutional courts in France and Germany became co-legislators whose anticipated rulings shape legislation \citep{stonesweet2000}. Hirschl's hegemonic preservation thesis holds that constitutionalization in Israel, Canada, New Zealand and South Africa transferred power to courts at moments when established elites faced electoral threats \citep{hirschl2001,hirschl2004}. The thesis is contested on timing and motive, and it is stated below as a hypothesis with a falsifier.
   497	
   498	Rafael La Porta and coauthors coded constitutional provisions on judicial independence and constitutional review across countries and related them to economic and political freedom \citep{laporta2004}. Lars Feld and Stefan Voigt distinguished de jure from de facto independence and found that the de facto measure, not the de jure measure, was associated with economic growth in their sample \citep{feld2003}. The distinction is the central measurement problem of this Part: constitutional guarantees are not the same as observed independence.
   499	
   500	Concentration of ordinary adjudication is low in secular democracies, and concentration at the constitutional apex is high. Disclosure and access are generally high. Independence and compliance depend on the political environment. Vanberg's public-support mechanism explains why governments comply with courts whose rulings voters observe \citep{vanberg2005}, and Whittington's account explains why fragmented coalitions sustain judicial review \citep{whittington2005}. When a governing coalition becomes dominant, both mechanisms weaken.
   501	
   502	The documented capture episodes in this regime type are court-packing and court-curbing by elected governments. Steven Levitsky and Lucan Way identify the judiciary as one of the arenas in which competitive authoritarian incumbents tilt the field against opponents \citep{levitsky2010}. Argentina provides a documented case. In 1990 the government of Carlos Menem enlarged the Supreme Court from five to nine members, and the resulting court became known for an ``automatic majority'' that favored the government's interests \citep{hevia2008}. Helmke's study of the same court shows the reverse movement: as the government's hold weakened, justices began to rule against it \citep{helmke2005}. The two observations together illustrate both halves of the series' thesis. The judicial function persisted throughout; its coupling to the political pillar rose and fell with the political calendar.
   503	
   504	The couplings $C_{\pJ\pI}$, $C_{\pJ\pC}$ and $C_{\pJ\pW}$ are generally lower in secular democracies than in the other types, because law schools, prosecutors and labor organizations are governed separately from the courts. Low coupling is not guaranteed. Judicial councils dominated by the governing party, prosecutors who answer to the executive, and legal-aid systems with inadequate funding each raise one of the couplings, and each is a target of the indicators in \cref{sec:measurement}.
   505	
   506	\subsection{Summary}
   507	
   508	\Cref{tab:regimes} codes the six patterns qualitatively; its entries are not measurements.
   509	
   510	\begin{table}[p]
   511	\centering
   512	\small
   513	\caption{The judicial function across six regime types. Concentration and coupling are qualitative codings of the patterns described in the text, not numerical estimates.}
   514	\label{tab:regimes}
   515	\begin{tabularx}{\textwidth}{L{2.2cm}YYYY}
   516	\toprule
   517	Regime type & Principal holders of the judicial function & Concentration and contestability & Strongest coupling to other pillars & Documented check or capture episode \\
   518	\midrule
   519	Market-capitalist societies & Appointed and elected judges, a large private bar, administrative tribunals and private arbitration & Low concentration in ordinary cases and high concentration at the constitutional apex, with access as the weakest link & Resources to adjudication through repeat players, funded litigation and judicial campaign finance & The recusal ruling in \emph{Caperton} checked a capture risk created by campaign spending \\
   520	\addlinespace
   521	Communist party-states & Courts, the procuracy, party bodies supervising legal work, and a state-disciplined bar & Low concentration in ordinary cases and high concentration in politically salient cases, with low ruler-boundness & Rule-making to adjudication through party appointment, and coercion through the procuracy & Stalin-era courts followed campaign directives, while later reform raised legality in ordinary cases \\
   522	\addlinespace
   523	Social democracy and democratic socialism & Ordinary and administrative courts, labor courts, ombudsmen and parliamentary review committees & Low concentration, high disclosure and compliance, and restrained constitutional review in Nordic systems & Production to adjudication through labor courts with members nominated by labor-market organizations & The \emph{Langborger} ruling held that interested nominating bodies can defeat impartiality \\
   524	\addlinespace
   525	Islamic states & Qadis and muftis historically, and in modern states codified courts, royal or clerical councils and administrative courts & Moderate concentration in classical practice and high concentration at the apex in modern Iran and Saudi Arabia & Legitimation to adjudication through the ulama, and rule-making through royal or clerical appointment & Iran's Guardian Council screens legislation and candidates, while plural schools and independent muftis supplied historical checks \\
   526	\addlinespace
   527	Historical Catholic monarchies & Royal courts, parlements and chanceries, church courts, the Inquisition and papal tribunals & Moderate concentration with contestability supplied by competition among jurisdictions & Legitimation to adjudication through church courts and the Inquisition, and resources through venal offices & Maupeou's suppression of the parlements in 1771 was reversed in 1774 \\
   528	\addlinespace
   529	Secular democracies & Constitutional and supreme courts, ordinary and administrative courts, judicial councils and international courts & Low concentration in ordinary cases and high concentration at the constitutional apex, with compliance resting on public support & Rule-making to adjudication through appointment and through review that acts as co-legislation & The enlargement of the Argentine Supreme Court in 1990 produced a court aligned with the government \\
   530	\bottomrule
   531	\end{tabularx}
   532	\end{table}
   533	
   534	Every regime type has the judicial function, as \cref{thm:judicial-power:necessity} requires. The types differ little in the concentration of ordinary adjudication, which is low almost everywhere. They differ in the concentration of politically salient adjudication and in the pillar to which interpretation is most tightly coupled: resources in market capitalism, rule-making and coercion in the party-state, production in corporatist social democracy, legitimation in religious states and Catholic monarchies, and rule-making through appointment in secular democracies. Each type also contains both documented capture episodes and documented checks. Capture varies within regime types, as Proposition B's contingency predicts, rather than marking the boundary between them.
   535	
   536	\section{Mechanisms, failure modes and checks}
   537	\label{sec:mechanisms}
   538	
   539	\subsection{Judicial capture}
   540	
   541	\Cref{def:judicial-power:capture} separates three things that public debate often merges. A judge appointed by a party is not thereby captured, because appointment is the ordinary channel through which every regime staffs its courts. A ruling that favors a powerful litigant is not thereby captured, because the powerful litigant may have had the better case. Capture requires a privilege, a weakened check and an outcome linked to the privilege. \emph{Caperton} establishes the first two conditions for one case and leaves the third unresolved. Stalin-era criminal justice establishes all three for a whole system.
   542	
   543	\subsection{Failure modes}
   544	
   545	Interpretation fails as a check in four ways, one for each link of the review chain, and the formal results of \cref{sec:layer,sec:literature} identify the conditions under which each failure occurs. Disclosure fails when proceedings are sealed, reasons go unpublished or financial ties between litigants and judges stay hidden; the chain then never starts. Access fails when one side can outspend the other, and \cref{prop:judicial-power:repeat} shows that repeat players win more often for that reason even when merits are equal. Independence fails when the incumbent expects to stay in power, and \cref{prop:judicial-power:insurance} shows that such an incumbent gains nothing from granting it. Compliance fails when the governing coalition ignores adverse rulings, and \cref{prop:judicial-power:chain} shows that no strength elsewhere in the chain repairs that failure. A regime can also confine all four failures to the politically salient tier, where caseload statistics do not see them (\cref{prop:judicial-power:dualstate}).
   546	
   547	Each failure has a characteristic check. Publication duties and recusal rules protect disclosure. Legal aid, collective litigation and limits on forced arbitration protect access. Tenure security, insulated appointment and a plurality of forums protect independence. Public support that makes defiance costly, the mechanism Vanberg identified \citep{vanberg2005}, and enforcement agencies that answer to courts rather than to the beneficiary protect compliance. \Cref{sec:comparative} documents checks of each kind in every regime type, which is why capture there appears as a variable rather than a constant.
   548	
   549	\subsection{Coupling pathways and checks}
   550	
   551	The legitimation pathway runs through the body that produces authoritative readings of the law and the beliefs that support them. When the same coalition trains the jurists, licenses the lawyers, appoints the judges and controls the doctrine that justifies the regime, $C_{\pJ\pI}$ is high. The ulama in classical Islamic societies, the canonists and inquisitors of Catholic Europe, and the party's legal theorists in socialist states each occupied this position in different degrees. High $C_{\pJ\pI}$ is not capture. It becomes capture when interpretive dissent loses its institutional footing, so that no independent jurist, school or faculty can contest the authoritative reading. The historical check was plurality: of schools in Islamic law, of jurisdictions in Catholic Europe, of faculties and bar associations in modern democracies.
   552	
   553	The coercion pathway runs through the organs that bring cases and enforce judgments. When the same organ prosecutes, supervises legality and directs judges, as the Soviet procuracy and party legal organs could, $C_{\pJ\pC}$ is high and the judicial pillar loses the ability to restrain coercion. The check is separation of prosecution from adjudication and of both from the police, with judicial control over detention. The sanctioning apparatus belongs to Part V, which shows that sanctions can deter rule violations equally well whether or not they also fall more heavily on a coalition's opponents \citep{long2026coercive}. Independent adjudication is the check that ties sanctions to conduct rather than allegiance, and by \cref{prop:judicial-power:disjunctive} a judiciary with strong public legitimacy needs less coercive backing to do so.
   554	
   555	The production pathway runs through access. When workers, tenants and consumers cannot afford to litigate while employers, landlords and lenders litigate routinely, courts apply rules that the organized side has shaped. Beyond the access checks listed above, the Swedish Labour Court shows that corporatist representation of producers inside the court is a second kind of check, and the \emph{Langborger} line of cases shows its limit \citep{langborger1989,stallarholmens1990}.
   556	
   557	\section{Measurement and hypotheses}
   558	\label{sec:measurement}
   559	
   560	\subsection{Indicators}
   561	
   562	Each component of the contestability vector has observable indicators. \Cref{tab:indicators} lists them. Formal guarantees and observed functioning must be measured separately, as the source insists and as Feld and Voigt's distinction between de jure and de facto independence requires \citep{largo2026hbs,feld2003}.
   563	
   564	\begin{table}[t]
   565	\centering
   566	\small
   567	\caption{Indicators for the components of judicial contestability. Each component needs both a formal indicator and an indicator of observed functioning.}
   568	\label{tab:indicators}
   569	\begin{tabularx}{\textwidth}{L{2.4cm}YY}
   570	\toprule
   571	Component & Formal indicators & Indicators of observed functioning \\
   572	\midrule
   573	Disclosure & A legal duty to publish reasoned decisions and rules on recusal and conflict disclosure & The share of decisions published with reasons, and disclosed financial ties between litigants and judges \\
   574	Access & The availability of legal aid, the right of appeal, and limits on court fees & Legal-aid coverage, the cost of litigation relative to income, and appeal rates by litigant type \\
   575	Independence & Appointment rules, tenure security and salary protection, as coded by La Porta and coauthors & The rate of rulings against the government and judges' turnover after changes of government \\
   576	Compliance & Constitutional duties of officials to execute judgments & The share of adverse rulings against government bodies that are executed within a stated period \\
   577	\bottomrule
   578	\end{tabularx}
   579	\end{table}
   580	
   581	Cross-national expert surveys supply indicators for independence and compliance in modern states. The Varieties of Democracy project codes judicial constraints on the executive, high court independence and government compliance with the judiciary \citep{coppedge2011}. The Worldwide Governance Indicators include a rule-of-law aggregate built from many sources \citep{kaufmann2011}. La Porta and coauthors and Feld and Voigt supply formal and de facto independence codings \citep{laporta2004,feld2003}.
   582	
   583	For historical regimes the evidence lies in court records: the registers of Ottoman qadi courts \citep{jennings1978}, the registers of the French parlements \citep{swann1995}, the records of inquisitorial trials \citep{henningsen1986} and the petitions to papal tribunals \citep{fosi2011}. Each archive carries selection problems. Records survive unevenly, and the cases that reached a court were already selected by the cost of bringing them.
   584	
   585	Measurement invariance is the main threat to comparison. An expert's judgment that a court is independent may mean different things for a constitutional court in a democracy and for a qadi court in a sixteenth-century city. The source recommends testing invariance and using regime-specific models when it fails \citep{largo2026hbs}. For the judicial layer the safest comparisons are within regime types over time, and across regime types on narrowly defined events, such as the execution of adverse judgments against state bodies.
   586	
   587	\subsection{Hypotheses}
   588	
   589	The following hypotheses refine the source's general hypotheses for the judicial pillar. Each states a falsifier. None is tested in this paper.
   590	
   591	\begin{description}[font=\normalfont\itshape,leftmargin=1.5em,style=nextline]
   592	\item[HJ1, insurance.] Judicial independence, measured de facto, is greater where control of government is more fragmented or electoral turnover is more likely (\cref{prop:judicial-power:insurance}). Falsifier: no association between de facto independence and measures of electoral uncertainty in a country panel, after controlling for income and legal origin.
   593	\item[HJ2, hegemonic preservation.] The empowerment of constitutional courts follows declines in the electoral prospects of established elites \citep{hirschl2004}. Falsifier: the timing of constitutional empowerment is unrelated to prior electoral decline across cases of new constitutionalism.
   594	\item[HJ3, two tiers.] In party-states and competitive authoritarian regimes, contestability is higher for commercial and ordinary civil cases than for politically salient cases (\cref{prop:judicial-power:dualstate}). Falsifier: rates of rulings against state bodies and of compliance with them are equal across case types once case merits are controlled.
   595	\item[HJ4, repeat players.] In comparable cases repeat litigants win more often than one-shotters, and the gap narrows when legal aid expands (\cref{prop:judicial-power:repeat}). Falsifier: no gap after controlling for case merit, or no narrowing after an expansion of legal aid.
   596	\item[HJ5, juristic autonomy.] Where religious jurists hold interpretive authority independent of state salaries and appointments, the share of law produced by ruler's decree is smaller than where jurists are state employees \citep{hallaq2009}. Falsifier: no difference in the share of decree-made law between periods or states that differ in jurists' independence.
   597	\item[HJ6, venality.] Venal judicial offices protect judges against removal by the crown and also entrench corporate privilege \citep{doyle1996}. Falsifier: the frequency of remonstrance and of successful resistance to royal legislation does not differ between venal and non-venal courts or periods.
   598	\item[HJ7, fusion.] The integration $C_{\pP\pJ}$ and the unaccountable concentration of the judicial layer rise together when judges are appointed and removable by the executive or the ruling party, and judges' reputational concerns limit the rise \citep{helmke2005}. Falsifier: changes in appointment and removal rules leave rates of rulings against the government unchanged.
   599	\item[HJ8, review chains.] The probability that a documented capture link persists after disclosure is predicted better by the weakest component of the contestability vector than by an additive index (\cref{prop:judicial-power:chain}). Falsifier: an additive index predicts persistence as well as or better than the minimum component in out-of-sample tests.
   600	\end{description}
   601	
   602	HJ1, HJ3 and HJ7 can be tested with existing cross-national data. HJ4 requires case-level data with measures of merit, which exist for some court systems. HJ2, HJ5 and HJ6 require historical research designs, and their falsifiers depend on archival coding that has not yet been done on comparable terms.
   603	
   604	\section{Judgment in the Book of Revelation}
   605	\label{sec:revelation}
   606	
   607	The series reads Revelation typologically. The beast is a recurring pattern of power that claims ultimate allegiance, and Babylon is the idolatrous city of every age. The reading does not identify any present-day government, party, institution, technology or person with the beast or its mark. Futurist identifications have a long record of failure, which Robert Fuller and Bernard McGinn document \citep{fuller1995,mcginn1994}, and historicist identifications of the papacy or of any other institution with the beast belong to the history of polemic, not to analysis. The theological interpretation is the project's own and is offered as an analogy that aids comparison, not as an exegetical result. Part VII owns the shared reading; this section applies it to the judicial pillar.
   608	
   609	Revelation 13 describes political authority, war-making, worship and economic exclusion, but no court. The dragon gives the first beast ``his power, and his seat, and great authority'' (Rev 13:2), and the second beast ``causeth all, both small and great, rich and poor, free and bond, to receive a mark in their right hand, or in their foreheads: And that no man might buy or sell, save he that had the mark'' (Rev 13:16 and 13:17) \citep{kjv}. Those who would not worship the image are to be killed (Rev 13:15). In the vocabulary of this paper, the passage describes an order in which a person's standing is fixed by a mark of allegiance rather than by the application of a general rule to a particular case. There is no procedure by which the excluded can contest their exclusion. Typologically, the judicial function has been absorbed into the legitimation and coercion functions, so that $C_{\pJ\pI}$ and $C_{\pJ\pC}$ are at their maximum and contestability is zero. It is the limiting case of capture in \cref{prop:judicial-power:chain}, with every link broken: sanctions follow allegiance alone.
   610	
   611	The rest of the book does not imagine a world without judgment. It relocates judgment. The souls under the altar cry out, ``How long, O Lord, holy and true, dost thou not judge and avenge our blood on them that dwell on the earth?'' (Rev 6:10). Their complaint is the absence of a just forum. The response comes in a refrain: ``true and righteous are thy judgments'' (Rev 16:7), and ``true and righteous are his judgments: for he hath judged the great whore'' (Rev 19:2). After the fall of Babylon, John sees thrones, and ``judgment was given unto them,'' to those who had not worshipped the beast or received its mark (Rev 20:4) \citep{kjv}. The judicial function passes from the imperial order to a court that the text presents as just.
   612	
   613	The commentators agree that the beasts had a Roman referent, which is the historical anchor that the typological reading generalizes. Richard Bauckham reads Rome as the paradigm of the beast and frames the book's conflict as one between worship of the beast and faithful witness \citep{bauckham1993}. Adela Yarbro Collins reads the book as a response to a crisis that its audience perceived, whose rhetoric works through catharsis \citep{collins1984}. Craig Koester's commentary situates the beasts in the imperial politics and civic cults of Roman Asia \citep{koester2014}. J.\,Nelson Kraybill shows how participation in commerce in the province was bound up with the imperial cult \citep{kraybill1996}, which gives the mark's economic exclusion its historical referent. Elisabeth Sch\"ussler Fiorenza's reading of the book as a work about justice and judgment puts the judicial theme at its center \citep{schussler1985}.
   614	
   615	The typology maps onto the series' two propositions. The text presupposes Proposition A: judgment is a permanent function, and the question is who exercises it. The warning attaches to Proposition B: an order in which allegiance replaces adjudication, and in which those excluded have no forum. The typology does not tell us which regimes approach that limit. Only the measurement program of \cref{sec:measurement} can do that, and its results will not track the boundaries of religions or ideologies.
   616	
   617	\section{Objections and scope conditions}
   618	\label{sec:objections}
   619	
   620	The first objection is that the necessity result is empty, because a function defined so broadly that a lottery counts as a court must exist everywhere. The reply is that the definitions exclude real possibilities. A collective in which every rule application is uncontested, or in which every residual dispute ends in force, departure or abandonment, has no judicial function under them, and \cref{prop:judicial-power:exit} shows that such a collective can persist when exit is free. The theorem's content lies in \cref{ass:cost}, an empirical claim about the cost of feud and exit, and societies in which exit is costless are the test cases. The result predicts thin adjudication in them.
   621	
   622	The second objection comes from legal realism and its descendants in political science: courts are political actors whose decisions reflect judges' preferences, so the distinction between making rules and interpreting them is a fiction. Shapiro's own account of courts as political actors is the strongest version \citep{shapiro1981}. The reply is that the split between rule-making and interpretation in this series is functional, not motivational. Whatever moves judges, the activity of fixing what a general rule requires in a particular case is distinct from the activity of making the general rule. When the two are performed by the same actor, the series records fusion through $C_{\pP\pJ}$. Realism about judicial motives strengthens the case for measuring the couplings; it does not dissolve the function.
   623	
   624	The third objection is that comparing qadi courts, inquisitorial tribunals and constitutional courts imposes modern categories on institutions that understood themselves differently. The reply has two parts. The comparison concerns the function each performed, which the institutions' own records allow us to observe: who brought cases, who decided them, how the decisions were enforced and whether they could be challenged. And the comparison does not import modern evaluative standards into the coding. Weber's ideal type of ``kadi justice'' is a cautionary example of what happens when a comparative category is applied without testing it against court records, and Gerber's test of that type against Ottoman records shows how the error is corrected \citep{weber1978,gerber1994}.
   625	
   626	Four scope conditions limit the results. The necessity theorem applies to collectives with recurrent residual disputes and costly self-help and exit, and it says nothing about the quality of adjudication. The formal models are stylized, and their assumptions can fail, especially the persistence of chosen independence in the insurance model and the contest form of the repeat-player model. The comparative codings are qualitative and rest on secondary scholarship, so they illustrate pathways rather than measure them. The hypotheses are stated and not tested.
   627	
   628	\section{Conclusion}
   629	
   630	Every governance system that persists with general rules and costly exit has a procedure for deciding particular disputes that neither party controls. That is the judicial pillar in its minimal form, and it is present among the Nuer and in the Parlement of Paris, in the qadi court of Kayseri and in the Swedish Labour Court. The function is universal; its holders, concentration and couplings are not.
   631	
   632	Judicial power becomes capture when privileged access to determinations weakens a link in the chain of disclosure, access, independence and compliance, and the outcomes follow the privilege. Because the chain is multiplicative, a single broken link suffices, and additive indices can hide it. Each of the six regime types contains documented episodes of capture and documented checks against it. The ideology that legitimates a regime does not settle whether its courts bind its rulers. What settles it is the strength of the weakest link, which is a measurable property of particular institutions at particular times.
   633	
   634	\begin{thebibliography}{99}
   635	\small
   636	
   637	\bibitem[Arbetsdomstolen(2026)]{arbetsdomstolen}
   638	Arbetsdomstolen (Swedish Labour Court). 2026. ``In English.'' \url{https://www.arbetsdomstolen.se/sv/en/in-english/}. Accessed 22 October 2026.
   639	
   640	\bibitem[Bauckham(1993)]{bauckham1993}
   641	Bauckham, Richard. 1993. \emph{The Theology of the Book of Revelation}. Cambridge: Cambridge University Press. doi:10.1017/cbo9780511819858.
   642	
   643	\bibitem[Bell(1994)]{bell1994}
   644	Bell, David A. 1994. \emph{Lawyers and Citizens: The Making of a Political Elite in Old Regime France}. New York: Oxford University Press. doi:10.1093/oso/9780195076707.001.0001.
   645	
   646	\bibitem[Berman(1963)]{berman1963}
   647	Berman, Harold J. 1963. \emph{Justice in the U.S.S.R.: An Interpretation of Soviet Law}. Cambridge, MA: Harvard University Press.
   648	
   649	\bibitem[Berman(1983)]{berman1983}
   650	Berman, Harold J. 1983. \emph{Law and Revolution: The Formation of the Western Legal Tradition}. Cambridge, MA: Harvard University Press. doi:10.4159/9780674020863.
   651	
   652	\bibitem[Boehm(1999)]{boehm1999}
   653	Boehm, Christopher. 1999. \emph{Hierarchy in the Forest: The Evolution of Egalitarian Behavior}. Cambridge, MA: Harvard University Press. doi:10.2307/j.ctvjf9xr4.
   654	
   655	\bibitem[Bonica and Sen(2017)]{bonica2017}
   656	Bonica, Adam, and Maya Sen. 2017. ``A Common-Space Scaling of the American Judiciary and Legal Profession.'' \emph{Political Analysis} 25(1): 114-121. doi:10.1017/pan.2016.10.
   657	
   658	\bibitem[Brown(1997)]{brown1997}
   659	Brown, Nathan J. 1997. \emph{The Rule of Law in the Arab World: Courts in Egypt and the Gulf}. Cambridge: Cambridge University Press. doi:10.1017/cbo9780511583278.
   660	
   661	\bibitem[Brundage(1995)]{brundage1995}
   662	Brundage, James A. 1995. \emph{Medieval Canon Law}. London: Longman. doi:10.4324/9781315844596.
   663	
   664	\bibitem[Buchta(2000)]{buchta2000}
   665	Buchta, Wilfried. 2000. \emph{Who Rules Iran? The Structure of Power in the Islamic Republic}. Washington, DC: Washington Institute for Near East Policy and Konrad Adenauer Stiftung.
   666	
   667	\bibitem[{\emph{Caperton v.\ A.\,T.\ Massey Coal Co.}}(2009)]{caperton2009}
   668	\emph{Caperton v.\ A.\,T.\ Massey Coal Co.}, 556 U.S. 868 (2009). Supreme Court of the United States, No.~08-22, decided 8 June 2009. \url{https://www.law.cornell.edu/supremecourt/text/08-22}.
   669	
   670	\bibitem[{\emph{Citizens United v.\ FEC}}(2010)]{citizensunited2010}
   671	\emph{Citizens United v.\ Federal Election Commission}, 558 U.S. 310 (2010). Supreme Court of the United States, No.~08-205, decided 21 January 2010. \url{https://www.law.cornell.edu/supremecourt/text/08-205}.
   672	
   673	\bibitem[Collins(1984)]{collins1984}
   674	Collins, Adela Yarbro. 1984. \emph{Crisis and Catharsis: The Power of the Apocalypse}. Philadelphia: Westminster Press.
   675	
   676	\bibitem[Coppedge et~al.(2011)]{coppedge2011}
   677	Coppedge, Michael, John Gerring, David Altman, Michael Bernhard, Steven Fish, Allen Hicken, Matthew Kroenig, Staffan I. Lindberg, Kelly McMann, Pamela Paxton, Holli A. Semetko, Svend-Erik Skaaning, Jeffrey Staton, and Jan Teorell. 2011. ``Conceptualizing and Measuring Democracy: A New Approach.'' \emph{Perspectives on Politics} 9(2): 247-267. doi:10.1017/S1537592711000880.
   678	
   679	\bibitem[Cox et~al.(2010)]{cox2010}
   680	Cox, Michael, Gwen Arnold, and Sergio Villamayor Tomas. 2010. ``A Review of Design Principles for Community-based Natural Resource Management.'' \emph{Ecology and Society} 15(4): 38. doi:10.5751/ES-03704-150438.

exec
/usr/local/bin/zsh -lc "sed -n '140,400p' papers/latex/judicial-power.tex | nl -ba -v 140" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   140	A product of numbers in $[0,1]$ is no larger than any of its factors, so $\Qchain\le\min_k q^k_t$. A weighted average with nonnegative weights summing to one is no smaller than the smallest averaged value, so $\min_k q^k_t\le\Qadd$. The second claim follows because $\omega_{\pJ}H_{\pJ,t}\ge 0$ and $1-Q_{\pJ,t}$ decreases in $Q_{\pJ,t}$.
   141	\end{proof}
   142	
   143	The bounds in the lemma are attained in opposite cases. When every component is equal, the minimum and the additive aggregate coincide; when one stage fails and the others work, the chain aggregate is zero while the additive aggregate stays high. Dispersion among the components is therefore what separates the two measures.
   144	
   145	\begin{definition}[Ruler-boundness and the two-tier judicial layer]
   146	\label{def:judicial-power:boundness}
   147	Ruler-boundness $\beta_t$ is the compliance component $q^{\mathrm{cmp}}_t$ restricted to rulings against members of the governing coalition: the probability that the coalition complies with an adverse final determination. A judicial layer is two-tier when the set of cases is partitioned into an ordinary class and a politically salient class, and the contestability vector differs between them.
   148	\end{definition}
   149	
   150	Ruler-boundness gives a working form to a distinction that Brian Tamanaha draws between the rule of law and rule by law \citep{tamanaha2004}. Under rule by law, law is an instrument that rulers use to govern others; under the rule of law, rulers are themselves bound. A regime can have an effective judicial function for ordinary disputes and low ruler-boundness at once. Randall Peerenboom's account of Chinese legal reform describes a thin rule of law of this partial kind \citep{peerenboom2002}, and Kathryn Hendley's study of everyday law in Russia documents courts that decide ordinary disputes routinely while politically salient cases follow a different logic \citep{hendley2017}.
   151	
   152	\begin{definition}[Judicial capture link]
   153	\label{def:judicial-power:capture}
   154	A judicial capture link is a capture link $(i\to j,\pJ)$ in the sense of \citet{largo2026hbs} whose three conditions take the following form in the judicial layer. Actor $i$ has privileged access to or discretion over determinations affecting $j$, for example through control of the appointment, promotion, remuneration or election funding of the deciding judges, through ex parte communication, or through control of which forum hears the case. The privilege weakens at least one component of the contestability vector $\mathbf{q}_t$. Material evidence ties the asymmetry to determinations, for example a difference in outcomes between cases in which the privilege is present and comparable cases in which it is absent.
   155	\end{definition}
   156	
   157	\subsection{Review chains}
   158	
   159	The source's second proposition holds that effective independent review and voice should reduce the probability that attempted capture yields persistent outcomes \citep{largo2026hbs}. For the judicial layer the structure of review can be stated precisely.
   160	
   161	\begin{proposition}[Review chain]
   162	\label{prop:judicial-power:chain}
   163	Suppose an attempted capture produces a favorable determination with probability $q_0\in(0,1]$, and the determination is reversed only if the four stages of \cref{def:judicial-power:qj} all succeed, with the conditional probabilities given there. Then the probability that the captured outcome persists is
   164	\[
   165	P_{\mathrm{persist}}=q_0\big(1-\Qchain\big),\qquad \Qchain=q^{\mathrm{dis}}_tq^{\mathrm{acc}}_tq^{\mathrm{ind}}_tq^{\mathrm{cmp}}_t.
   166	\]
   167	Three consequences follow. If any link is zero, then $P_{\mathrm{persist}}=q_0$ whatever the other links. Raising link $k$ by $\Delta\in(0,1-q^k_t]$ reduces $P_{\mathrm{persist}}$ by $q_0\Delta\prod_{j\neq k}q^j_t$, so the marginal effect of link $k$ is $-\partial P_{\mathrm{persist}}/\partial q^k_t=q_0\prod_{j\neq k}q^j_t$; when every link is positive, this marginal effect is largest for the link with the smallest value. For any weights $w_k>0$ there are contestability vectors with the same additive aggregate $\Qadd$ and different persistence probabilities, including a vector with $\Qadd=1-\min_k w_k$ and $P_{\mathrm{persist}}=q_0$.
   168	\end{proposition}
   169	
   170	\begin{proof}
   171	Reversal is the intersection of four events, and the components are the probabilities of each event conditional on the preceding ones, so by the chain rule of probability the probability of reversal given a captured determination is the product $\Qchain$. Persistence therefore has probability $q_0(1-\Qchain)$. If some $q^k_t=0$, the product is zero. Raising $q^k_t$ by $\Delta$ raises the product by $\Delta\prod_{j\neq k}q^j_t$, which reduces $P_{\mathrm{persist}}$ by $q_0\Delta\prod_{j\neq k}q^j_t$. The marginal effect is the derivative of this linear expression in $\Delta$. When all links are positive, $\prod_{j\neq k}q^j_t=\Qchain/q^k_t$, which is largest for the smallest $q^k_t$. For the last claim, let $k^{*}$ be a link with the smallest weight, set $q^{k^{*}}_t=0$ and every other link to one. Then $\Qadd=1-w_{k^{*}}$ and $\Qchain=0$, so $P_{\mathrm{persist}}=q_0$. Setting every link to $1-w_{k^{*}}$ gives the same additive aggregate and a strictly positive product, hence, because $q_0>0$, a strictly smaller persistence probability.
   172	\end{proof}
   173	
   174	The proposition explains why judicial-independence indices built by addition can mislead. A judiciary with published reasons, open access and independent judges scores well on an additive index, but if the governing coalition ignores adverse rulings, the review chain is broken at its last link and captured outcomes persist. The multiplicative form also implies that reform yields the most where the chain is weakest. The comparison in \cref{sec:comparative} below suggests that the weakest link is often access in market-capitalist systems, compliance in the political tier of party-states, and independence in backsliding democracies.
   175	
   176	The product is exact because each component is defined conditionally on the stages before it; no independence assumption is involved. Dependence matters for measurement. Published indicators usually record marginal frequencies, such as the share of decisions published or the share of rulings against the government, rather than conditional ones. If the stages tend to succeed or fail together, the product of marginal frequencies understates the true probability of reversal. Tests of the review-chain claim should therefore estimate the conditional components from case histories, as hypothesis HJ8 requires.
   177	
   178	\subsection{Two-tier judicial layers}
   179	
   180	\begin{proposition}[Aggregation hides the political tier]
   181	\label{prop:judicial-power:dualstate}
   182	For a two-tier judicial layer in which the politically salient tier carries a share $\varphi\in(0,1)$ of stake-weighted cases and has chain contestability $Q^{\times}_{\Pi}$, while the ordinary tier has $Q^{\times}_{O}$, define the stake-weighted contestability $\bar Q^{\times}=(1-\varphi)Q^{\times}_O+\varphi Q^{\times}_\Pi$. For every $\varepsilon\in(0,1)$ there is a two-tier layer with $\varphi\in(0,\varepsilon]$, $\bar Q^{\times}\ge 1-\varepsilon$ and $Q^{\times}_\Pi=0$.
   183	\end{proposition}
   184	
   185	\begin{proof}
   186	Given $\varepsilon$, take $\varphi=\varepsilon$, $Q^{\times}_O=1$ and $Q^{\times}_\Pi=0$. Then $\bar Q^{\times}=1-\varepsilon$.
   187	\end{proof}
   188	
   189	The proof is elementary, and the point is about measurement. Surveys of business users, caseload statistics and appeal rates are dominated by the ordinary tier. They can report a well-functioning judiciary in a regime whose courts never bind the ruling coalition. Control shares and concentration should also be computed tier by tier, because the last word in the political tier may rest with an actor that holds none in the ordinary tier. Measurements intended to test Proposition B must therefore be tier-specific, and hypothesis HJ3 in \cref{sec:measurement} makes the tiers an object of test.
   190	
   191	\section{Necessity of the judicial function}
   192	\label{sec:necessity}
   193	
   194	\subsection{The necessity theorem}
   195	
   196	The argument for necessity is a conditions-of-persistence argument. It does not explain why any particular court exists. It shows that a collective with general rules cannot persist indefinitely without performing the function that courts perform, provided three assumptions hold.
   197	
   198	\begin{assumption}[Recurrent residual disputes]
   199	\label{ass:arrival}
   200	On the event that the collective persists for all time, infinitely many residual disputes arise, and each reaches a disposition at some finite time.
   201	\end{assumption}
   202	
   203	\begin{assumption}[Costly self-help and exit]
   204	\label{ass:cost}
   205	There is $\kappa\in(0,1]$ such that, conditional on the history up to the disposition of any residual dispute, a disposition by self-help, by exit or by abandonment ends the collective's persistence with probability at least $\kappa$.
   206	\end{assumption}
   207	
   208	\Cref{ass:arrival} is the third axiom in operational form together with a positive rate of bargaining failure. \Cref{ass:cost} bundles three claims. Self-help between members tends toward feud, which in segmentary societies can split the group along lineage lines. Exit by one party removes a member and, when the parties are heads of kin groups, a segment of the collective. Abandonment leaves a grievance that tends to return as self-help or exit. The assumption does not say that every feud destroys the group. It says that each abandoned or forcibly settled dispute carries a risk to the collective's continuation as a single decision-making unit, and that the risk is bounded below.
   209	
   210	\begin{theorem}[Necessity of adjudication]
   211	\label{thm:judicial-power:necessity}
   212	Under \cref{ass:arrival,ass:cost}, the event that the collective persists for all time is contained, up to a null set, in the event that adjudication is implemented. If the collective persists with positive probability, the fraction of residual disputes disposed of by determination converges to one almost surely on the persistence event.
   213	\end{theorem}
   214	
   215	\begin{proof}
   216	Let $\Pi$ be the event that the collective persists for all time and let $N$ be the number of residual disputes disposed of by self-help, exit or abandonment before the collective ends, with $N=\infty$ allowed. For $n\ge 1$ let $S_n$ be the event that at least $n$ such dispositions occur and the collective survives each of the first $n$. By \cref{ass:cost}, conditional on $S_{n-1}$ and on the occurrence of an $n$-th such disposition, survival through it has probability at most $1-\kappa$. Induction gives $\Pr(S_n)\le(1-\kappa)^n$. Since $\Pi\cap\{N\ge n\}\subseteq S_n$, we have $\Pr(\Pi\cap\{N=\infty\})\le\inf_n (1-\kappa)^n=0$. Hence, almost surely on $\Pi$, only finitely many residual disputes are disposed of other than by determination. By \cref{ass:arrival}, infinitely many residual disputes arise on $\Pi$, and each reaches exactly one of the four dispositions of \cref{def:judicial-power:determination}, so infinitely many are disposed of by determination and adjudication is implemented. Index residual disputes in order of disposition, breaking ties arbitrarily. If $D_k$ and $N_k$ count determinations and other dispositions among the first $k$ residual disputes so indexed, then on $\Pi$ the count $N_k$ is eventually constant while $D_k+N_k=k$, so $D_k/k\to 1$.
   217	\end{proof}
   218	
   219	The theorem says nothing about who determines. A single mediator, a rotating council, a lottery and a hierarchy of appellate courts all satisfy it. It also says nothing about the quality of determinations. A collective may persist with determinations that are biased, slow or cruel, so long as the parties act on them. The necessity is of a function, and the function is minimal: a procedure that neither disputant controls, whose output both act on.
   220	
   221	\begin{remark}
   222	The proof needs only a conditional lower bound on the dissolution hazard, not independence across disputes, a stationary arrival rate, or any account of how determination procedures arise. A selection story is consistent with the theorem but not required by it.
   223	\end{remark}
   224	
   225	\subsection{Minimal forms in stateless and consensus societies}
   226	
   227	The theorem predicts that collectives without states still adjudicate, and that their procedures need not resemble courts. The ethnographic record bears this out (\cref{tab:minimal}), with a qualification that the next subsection makes precise.
   228	
   229	\begin{table}[t]
   230	\centering
   231	\small
   232	\caption{Minimal forms of the judicial function in stateless and consensus societies. Each row names the determination procedure, its source of compliance, and the strongest reading that the function is absent.}
   233	\label{tab:minimal}
   234	\begin{tabularx}{\textwidth}{L{2.3cm}YYY}
   235	\toprule
   236	Case & Determination procedure & Source of compliance & Strongest counter-reading \\
   237	\midrule
   238	Nuer & The leopard-skin chief mediates blood-feud compensation in cattle between lineages & Consent of the parties backed by the threat of renewed feud & The chief has no power to compel, so the settlement is a bargain rather than a judgment \\
   239	Barotse & Judges in a council apply the standard of the reasonable man to the conduct of litigants & Kinship obligations and the authority of the council & The Lozi had a kingdom, so the case shows a court rather than a stateless procedure \\
   240	Arusha & Councils of elders and lineage moots negotiate settlements between disputants & Pressure from kin groups and the prospect of continued relations & Outcomes reflect relative bargaining strength, so the procedure is negotiation \\
   241	Ju/'hoansi & Kin and camp members talk disputes out in public, and parties often move to another camp & Ridicule, gossip and the value of continued sharing relations & Exit by moving camp resolves many disputes with no third party at all \\
   242	Reverse dominance hierarchies & The camp acts as a moral community that judges would-be dominants and deviants & Criticism, ostracism, exile and in extreme cases execution & The judging group is also the sanctioning group, so the functions are fused \\
   243	Commons institutions & Users or their officials hold low-cost local arenas to resolve conflicts over the rules & Graduated sanctions and monitoring by users & The arenas are designed institutions, so they show possibility rather than necessity \\
   244	\bottomrule
   245	\end{tabularx}
   246	\end{table}
   247	
   248	Among the Nuer, whom E.\,E. Evans-Pritchard described as living in an ordered anarchy without government, a killing set off a feud between lineages unless compensation in cattle was arranged through the leopard-skin chief \citep{evanspritchard1940}. The chief could not compel either side. His role was to offer sanctuary to the killer, to negotiate the payment and to perform the rites that ended the feud. Evans-Pritchard's own emphasis on the absence of government is the strongest counter-reading: the chief decided nothing that the parties had not accepted. Under \cref{def:judicial-power:determination}, however, consent does not disqualify a procedure. What matters is that the settlement was produced through a third party whom neither lineage controlled, and that both acted on it. The source of compliance was the parties' preference for settlement over a continuing feud, which is the sanction-side dependency discussed in \cref{subsec:dependencies}.
   249	
   250	Max Gluckman's study of the Barotse shows a fuller judicial form, with judges who measured litigants against the conduct expected of a reasonable person in their position \citep{gluckman1955}. The case is a contrast rather than a hard case, since the Lozi had a kingdom. P.\,H. Gulliver's Arusha are closer to the stateless baseline \citep{gulliver1963}. Gulliver described dispute settlement through negotiation in moots and councils in which the relative strength of the parties' supporters shaped the outcome. That description invites the reading that no adjudication took place, only bargaining. The reply is that a dispute that reaches a moot is residual in the sense of \cref{def:judicial-power:dispute}: unassisted bargaining between the principals has failed, and the moot supplies a forum and participants who are not principals. A determination produced by a forum in which strength matters is a biased determination, not the absence of one.
   251	
   252	Even the societies most often cited as lacking hierarchy have a judging procedure: the camp's collective talk. Richard Lee's ethnography of the Ju/'hoansi of the Kalahari records disputes handled by public talk among kin and camp members, together with frequent movement between camps \citep{lee2013}. Polly Wiessner's study of norm enforcement among the Ju/'hoansi finds that criticism and talk were the main instruments by which norm violations were addressed \citep{wiessner2005}. Christopher Boehm's comparative work on foragers describes the same pattern from the side of the group, in which a coalition of subordinates judges and sanctions anyone who tries to dominate \citep{boehm1999}. James Woodburn adds that the egalitarianism of immediate-return societies is produced by leveling institutions, not by the absence of institutions \citep{woodburn1982}. The same body judges and sanctions, so $C_{\pJ\pC}$ is high in these societies, but neither disputant controls the procedure and the function is present.
   253	
   254	Elinor Ostrom's design principles for long-enduring commons institutions include rapid access to low-cost local arenas for resolving conflicts among users and between users and officials \citep{ostrom1990}. Michael Cox and coauthors' review of studies testing the principles found broad empirical support for them as a set \citep{cox2010}. Ostrom's cases are designed institutions, so they show that successful self-governance includes adjudication rather than proving that it must. With the stateless cases, they show the judicial function wherever general rules govern repeated interaction.
   255	
   256	\subsection{Counterexample attempts}
   257	
   258	The strongest counterexample to \cref{thm:judicial-power:necessity} is a collective that resolves residual disputes by exit. Woodburn's immediate-return societies and the Ju/'hoansi practice of moving between camps come close. When exit is costless the theorem's forcing argument fails, and the failure is a genuine limit on the claim.
   259	
   260	\begin{proposition}[Exit substitution]
   261	\label{prop:judicial-power:exit}
   262	Suppose \cref{ass:arrival} holds and a disposition by self-help or abandonment ends persistence with probability at least $\kappa>0$, but a disposition by exit carries no risk to persistence and is always available. Then there are collectives that persist with probability one and in which no residual dispute is disposed of by determination.
   263	\end{proposition}
   264	
   265	\begin{proof}
   266	Consider a regional population divided among bands. Let every residual dispute be disposed of by one party moving to another band, which by hypothesis does not affect the persistence of the regional collective. The collective never incurs the hazard attached to self-help or abandonment, so it persists with probability one, and no determination occurs.
   267	\end{proof}
   268	
   269	The proposition narrows the claim. Adjudication is forced where exit is costly. Where exit is cheap, the judicial function can be thin, and the ethnography of immediate-return foragers is consistent with that prediction: talk, ridicule and departure do much of the work that courts do elsewhere \citep{woodburn1982,lee2013}. Two qualifications keep the narrowing in proportion. The cheap-exit condition is rare: it requires mobile residence, no stored wealth, and access to other groups on the same terms, which Woodburn identified as distinctive of a small set of societies. The ethnographies of these societies also record talk-based mediation alongside exit \citep{lee2013,wiessner2005}, so the function is thin rather than absent.
   270	
   271	The second counterexample attempt is a rule system that leaves no room for interpretation because a program executes it. If rules are code, the program decides, and no judge is needed.
   272	
   273	\begin{proposition}[Relocation of interpretation]
   274	\label{prop:judicial-power:relocation}
   275	Let a rule $r$ over cases $X$ be executed by a program $c:Z\to\mathcal{V}$ applied to recorded inputs $z=\zeta(x)$, where an encoding $\zeta:X\to Z$ records a case for the program. Let $\mathcal{E}(r)$ be the nonempty set of admissible encodings, those that competent members would accept as recording cases faithfully for the rule's purpose, and let the code-level open set be
   276	\[
   277	O_c(r)=\{x\in X : c(\zeta(x))\neq c(\zeta'(x))\text{ for some }\zeta,\zeta'\in\mathcal{E}(r)\}.
   278	\]
   279	Suppose the parties have agreed in advance that the verdict $c(\zeta_0(x))$ settles every case $x$ in a set $X_0\subseteq X$, for a designated $\zeta_0\in\mathcal{E}(r)$, and that neither party alone controls $c$ or $\zeta_0$ on $X_0$. Outside $X_0$ both the rule and the program have standing, so the admissible positions there are $\Read^{*}(r)=\Read(r)\cup\{c\circ\zeta:\zeta\in\mathcal{E}(r)\}$, with open set $O^{*}(r)$ computed from $\Read^{*}(r)$ as in \cref{def:judicial-power:open-texture}. Then $O(r)\cup O_c(r)\subseteq O^{*}(r)$, and $O^{*}(r)$ also contains every case at which some $\rho\in\Read(r)$ and some $c\circ\zeta$ with $\zeta\in\mathcal{E}(r)$ disagree. The following hold.
   280	\begin{enumerate}[label=(\roman*)]
   281	\item On $X_0$ the program with encoding $\zeta_0$ is a determination procedure in the sense of \cref{def:judicial-power:determination}.
   282	\item For every case $x\in O^{*}(r)\setminus X_0$ there are admissible positions with different verdicts, so disputes can arise at $x$, and those in which bargaining fails are residual disputes subject to \cref{thm:judicial-power:necessity}.
   283	\item $O_c(r)=\emptyset$ if and only if every admissible encoding yields the same verdict under $c$ for every case.
   284	\end{enumerate}
   285	\end{proposition}
   286	
   287	\begin{proof}
   288	For (i), on $X_0$ the program produces the verdict, neither party alone controls the program or the encoding by hypothesis, and both parties have agreed in advance to act on the verdict. The inclusion $O(r)\cup O_c(r)\subseteq O^{*}(r)$ holds because $\Read^{*}(r)$ contains both $\Read(r)$ and $\{c\circ\zeta:\zeta\in\mathcal{E}(r)\}$, and a case at which some reading $\rho\in\Read(r)$ and some program reading $c\circ\zeta$ disagree lies in $O^{*}(r)$ by definition. For (ii), the pair $(r,\Read^{*}(r))$ is a rule system in the sense of \cref{def:judicial-power:open-texture}, so a case in $O^{*}(r)\setminus X_0$ admits two admissible positions with different verdicts, and two members whose interests favor different verdicts can each endorse one, which is a dispute under \cref{def:judicial-power:dispute}. The parties have not agreed that the program settles such a case, so a dispute there in which bargaining fails is residual, and \cref{thm:judicial-power:necessity} applies. Claim (iii) restates the definition of $O_c(r)$.
   289	\end{proof}
   290	
   291	Encoding moves the open set from the terms of the rule to the recording of cases and to the gap between rule and program: whether a delivery occurred, whether a price feed was accurate, whether a reported event matched the contract's description. A deterministic program removes open texture only if every admissible encoding agrees, which is rare for rules about the world rather than about the program's own state. Unforeseen cases also fall outside $X_0$ almost by definition. Systems that execute agreements automatically therefore acquire arbiters, oracles, governance votes or forks, each of which is a determination procedure. Interpretation relocates; it does not vanish.
   292	
   293	The third counterexample attempt is pure self-help, a society in which wronged parties retaliate and nothing more. Evans-Pritchard's model of balanced opposition among Nuer lineages is the classic candidate. The reply is that the Nuer did not leave feuds to run indefinitely. Compensation through the leopard-skin chief ended them \citep{evanspritchard1940}. A society of pure self-help without any procedure for ending feuds would violate \cref{ass:cost} at every dispute, and the theorem predicts that it would not persist as a single collective. The falsifier for the necessity claim follows: a persistent collective with costly exit in which residual disputes about rule application are always settled by force of the parties or left open, without the collective dissolving.
   294	
   295	\subsection{Dependencies of the judicial function}
   296	\label{subsec:dependencies}
   297	
   298	A determination settles a dispute only if the losing party acts on it. Alexander Hamilton made the point about the federal judiciary in 1788: the judiciary ``may truly be said to have neither FORCE nor WILL, but merely judgment,'' and depends on the executive arm for the efficacy of its judgments \citep{hamilton1788}. The dependency is weaker than Hamilton's phrasing suggests.
   299	
   300	\begin{proposition}[Disjunctive dependency]
   301	\label{prop:judicial-power:disjunctive}
   302	Suppose the losing party in a determination gains $g>0$ by defying it, and complies if and only if $\ell+\sigma\ge g$, where $\ell\ge 0$ is the value it places on the procedure's legitimacy, including internalized obligation and reputation, and $\sigma\ge 0$ is the expected sanction for defiance. Then an effective determination requires $\ell>0$ or $\sigma>0$. Neither $\ell>0$ nor $\sigma>0$ is required by itself.
   303	\end{proposition}
   304	
   305	\begin{proof}
   306	If $\ell=\sigma=0$, then $\ell+\sigma=0<g$ and the loser defies, so the determination is not effective. For the second claim, a determination with $\ell\ge g$ and $\sigma=0$ is effective without sanction, and a determination with $\sigma\ge g$ and $\ell=0$ is effective without legitimacy.
   307	\end{proof}
   308	
   309	The judicial function therefore depends on the legitimation pillar or on the coercion pillar, and on neither specifically. In \cref{prop:judicial-power:disjunctive}, $\ell$ is the value a party places on complying because it regards the procedure as rightful, which Part IV calls normative legitimacy \citep{long2026ideological}, and $\sigma$ is the expected sanction for defiance, which Part V analyzes \citep{long2026coercive}. The Nuer settlement and the Ju/'hoansi talking-out rest mainly on legitimacy and the value of continued relations, while an imposed verdict in a party-state's political case rests mainly on sanction. Hamilton's executive arm is one source of $\sigma$. The reservoir of public support that James Gibson and coauthors measured for the United States Supreme Court is a source of $\ell$ \citep{gibson2003}.
   310	
   311	Because the dependency is disjunctive, it cannot be represented as two separate arcs into the judicial node. In the dependency digraph among the six functions that Part VII studies \citep{long2026formalized}, the arcs from legitimation and coercion into interpretation form a single or-condition, a hyperedge, and a proof that the digraph is strongly connected must treat them that way.
   312	
   313	The judicial function also feeds the other pillars. Interpretation changes rules through precedent, which enters rule-making through the rule of change. Reasoned judgments are public acts that shape common beliefs about what the rules are, which enters legitimation through the rule of recognition.
   314	
   315	\subsection{Functionalist objections}
   316	
   317	Carl Hempel warned that from the premise that a system needs some function one cannot infer that a particular institution exists, because functional equivalents may meet the need \citep{hempel1959}. \Cref{thm:judicial-power:necessity} respects the warning. Its conclusion is the existence of some determination procedure, and the minimal forms in \cref{tab:minimal} are exactly the functional equivalents that Hempel had in mind. Jon Elster argued that a functional explanation of an institution by its beneficial effects is legitimate only when a feedback mechanism links the effects back to the institution's persistence \citep{elster1983}. The theorem does not explain why any collective has a court. It states a condition that every persisting collective with costly exit satisfies. Robert Merton's distinction between manifest and latent functions, and his insistence on functional alternatives \citep{merton1968}, apply in the same way: courts have many latent functions, including legitimation and social control, and the theorem concerns none of them.
   318	
   319	\subsection{Necessity without capture}
   320	
   321	\begin{corollary}[Necessity does not imply capture]
   322	\label{cor:judicial-power:nonimplication}
   323	For every value $c\in[0,1]$ there are collectives that satisfy the hypotheses of \cref{thm:judicial-power:necessity}, implement adjudication, and have chain contestability $\Qchain=c$.
   324	\end{corollary}
   325	
   326	\begin{proof}
   327	\Cref{ass:arrival,ass:cost} constrain the arrival of residual disputes and the hazard attached to resolving them other than by determination. Neither refers to disclosure, access, independence or compliance. Take a collective satisfying both assumptions in which every residual dispute is resolved by determination, and assign its review links any values whose product is $c$, for example $q^{\mathrm{dis}}_t=q^{\mathrm{acc}}_t=q^{\mathrm{ind}}_t=1$ and $q^{\mathrm{cmp}}_t=c$. The hypotheses of the theorem still hold, adjudication is implemented, and $\Qchain=c$.
   328	\end{proof}
   329	
   330	The corollary is the judicial instance of the series claim that Proposition A does not imply Proposition B, which Part VII proves in general. The necessity theorem fixes that some determination procedure exists. It leaves the contestability of that procedure, and hence the persistence of captured rulings under \cref{prop:judicial-power:chain}, entirely open.
   331	
   332	\section{Literature on judicial power}
   333	\label{sec:literature}
   334	
   335	\subsection{Accounts of judicial independence}
   336	
   337	The literature on judicial power divides over one question: why would anyone who holds power allow a body to tell them what the law requires? The answers fall into four families, and the comparative analysis in \cref{sec:comparative} draws on all of them.
   338	
   339	The first family treats independent courts as a device that serves the powerful. William Landes and Richard Posner argued that an independent judiciary makes legislative deals durable, because judges who enforce statutes as enacted protect the bargains that interest groups purchased from earlier legislatures \citep{landes1975}. J.\,Mark Ramseyer argued that politicians tolerate independent courts when they expect to lose office, because a court that binds the next government protects them \citep{ramseyer1994}. Matthew Stephenson formalized the insurance logic as a repeated game between parties that alternate in power \citep{stephenson2003}, and Keith Whittington showed that politically fragmented coalitions in the United States have repeatedly supported the exercise of judicial review against their own legislative partners \citep{whittington2005}. Ran Hirschl's hegemonic preservation thesis is a sharper version: elites facing electoral decline transfer power to courts whose judges share their commitments, as he argued for Israel, Canada, New Zealand and South Africa \citep{hirschl2001,hirschl2004}. The insurance and preservation accounts agree that independence is chosen for strategic reasons. They differ on whom it protects.
   340	
   341	The second family studies courts under authoritarian rule. Tom Ginsburg and Tamir Moustafa collected evidence that authoritarian rulers use courts for social control, for legitimation, to commit credibly to investors, to discipline their own administrators and to resolve disputes within the ruling coalition \citep{ginsburg2008}. Moustafa's study of Egypt's Supreme Constitutional Court shows a regime that empowered a court to reassure investors and then found the court supporting challenges to the regime \citep{moustafa2007}. Gretchen Helmke's study of Argentina showed that judges without secure tenure rule against outgoing governments when they expect a change in power, a pattern she called strategic defection \citep{helmke2005}. These works establish that courts matter under authoritarianism and that their independence varies by case type and by the political calendar.
   342	
   343	The third family asks what makes judges' rulings stick. Georg Vanberg's study of the German Federal Constitutional Court argues that public support protects a court against noncompliance when the public can observe whether the government complies \citep{vanberg2005}. Gibson and coauthors found that the United States Supreme Court's legitimacy survived its controversial decision in the 2000 presidential election, which they attributed to a reservoir of goodwill \citep{gibson2003}. Alec Stone Sweet showed how European constitutional courts became co-legislators whose anticipated rulings shape the drafting of statutes \citep{stonesweet2000}. Mark Tushnet compared strong-form review, in which courts have the last word, with weak-form review, in which legislatures can respond, and argued that weak-form systems can protect social rights without judicial supremacy \citep{tushnet2008}.
   344	
   345	The fourth family concerns who uses courts and who wins. Marc Galanter distinguished repeat players, who litigate many similar cases, from one-shotters, and argued that repeat players come out ahead because they can play for favorable rules as well as for immediate outcomes \citep{galanter1974}. Charles Epp showed that rights revolutions depended on a support structure of lawyers, organizations and funding rather than on constitutional text alone \citep{epp1998}. Adam Bonica and Maya Sen placed judges and lawyers on a common ideological scale and found that selection channels shape the ideological composition of the American judiciary \citep{bonica2017}.
   346	
   347	Comparative legal history supplies evidence of a different kind, from religious, ecclesiastical and royal courts that the political science literature seldom examines. Wael Hallaq's work on Islamic law describes a judicial order in which state-appointed qadis applied a law developed by jurists who were not state officials \citep{hallaq2005,hallaq2009}. Harold Berman argued that the papal reforms of the late eleventh century produced the first modern Western legal system and a plurality of jurisdictions that limited every authority, including the Church \citep{berman1983}. Richard Kagan's study of litigation in Castile, David Bell's study of barristers in Paris, and Irene Fosi's study of papal justice show courts in early modern Catholic monarchies used by large numbers of ordinary litigants \citep{kagan1981,bell1994,fosi2011}. The socialist-legality literature, from Harold Berman's interpretation of Soviet law to Stanley Lubman's and Carl Minzner's studies of China, traces courts embedded in party rule \citep{berman1963,lubman1999,minzner2011}.
   348	
   349	The strategic accounts explain why independence varies but take the existence of courts for granted. The legal-historical accounts document courts in many regimes but rarely compare them on common dimensions. A shared vocabulary, the judicial layer and its contestability vector, lets both be read as answers to one question: how is the universal judicial function coupled to the other five?
   350	
   351	\subsection{The insurance model}
   352	
   353	Why would a governing coalition allow courts to bind it? The insurance account answers that independence is a hedge against losing power \citep{landes1975,ramseyer1994,stephenson2003}.
   354	
   355	\begin{proposition}[Insurance model]
   356	\label{prop:judicial-power:insurance}
   357	An incumbent chooses court independence $\iota\in[0,1]$, which persists into the next period. In each period the office holder can take an abusive action that yields it $g>0$ and costs the other side $L>0$, and the court blocks the action with probability $\iota$. The incumbent loses office before the next period with probability $\pi\in[0,1]$ and discounts the future by $\delta\in(0,1]$. Let
   358	\[
   359	\pi^{*}=\frac{g(1+\delta)}{\delta(g+L)}.
   360	\]
   361	The incumbent's expected payoff is maximized at $\iota^{*}=1$ if $\pi>\pi^{*}$, at $\iota^{*}=0$ if $\pi<\pi^{*}$, and by every $\iota\in[0,1]$ if $\pi=\pi^{*}$. The threshold $\pi^{*}$ decreases in $L$ and $\delta$ and increases in $g$. If $g\ge\delta L$, then $\pi^{*}\ge 1$ and independence is never strictly optimal.
   362	\end{proposition}
   363	
   364	\begin{proof}
   365	The incumbent's payoff is
   366	\[
   367	\Phi(\iota)=(1-\iota)g+\delta\big[(1-\pi)(1-\iota)g-\pi(1-\iota)L\big]=(1-\iota)\big[g(1+\delta)-\delta\pi(g+L)\big].
   368	\]
   369	$\Phi$ is linear in $\iota$ with slope $-\big[g(1+\delta)-\delta\pi(g+L)\big]$, which is positive when $\pi>\pi^{*}$, negative when $\pi<\pi^{*}$ and zero when $\pi=\pi^{*}$. The comparative statics follow from differentiating $\pi^{*}$: $\partial\pi^{*}/\partial L=-g(1+\delta)/[\delta(g+L)^2]<0$, $\partial\pi^{*}/\partial\delta=-g/[\delta^{2}(g+L)]<0$, and $\partial\pi^{*}/\partial g=(1+\delta)L/[\delta(g+L)^2]>0$. Finally, $\pi^{*}\ge 1$ if and only if $g(1+\delta)\ge\delta(g+L)$, which simplifies to $g\ge\delta L$.
   370	\end{proof}
   371	
   372	The model's assumptions do the work, and they should be stated plainly. Independence chosen today must persist, which requires that institutional change be costly; Landes and Posner's account relies on the same stickiness \citep{landes1975}. The court must bind whoever holds office, which excludes a court that binds only the opposition. The model is linear, which produces an all-or-nothing choice; a convex cost of independence would produce interior solutions with the same comparative statics. In the vocabulary of \cref{sec:layer}, $\iota$ is the independence component $q^{\mathrm{ind}}_t$, and when the incumbent appoints the judges through the appointment channel, keeping $\iota$ low is the same as keeping $C_{\pP\pJ}$ high.
   373	
   374	The result says that independence is more likely where the incumbent expects to lose power, where abuse by the other side would be costly, and where the incumbent is patient. It fits the variation across party-states and secular democracies described in \cref{sec:comparative}: a ruling party with a low $\pi$ has little reason to grant independence, and a fragmented democracy with a high $\pi$ has strong reason. Ramseyer used the same logic to explain why Japanese courts were less independent than American ones during a long period of single-party dominance \citep{ramseyer1994}.
   375	
   376	\begin{remark}[Strategic defection]
   377	Helmke's account of Argentine judges adds a judge-side version of the same logic \citep{helmke2005}. Assume that a judge without secure tenure is sanctioned, with loss $s>0$, only by whichever side holds power after the ruling takes effect and only if the ruling went against that side; that the case sets the incumbent against the side that would replace it; and that the merits are balanced. Ruling against the incumbent then risks $(1-\pi)s$, and ruling for it risks $\pi s$, so the judge rules against the incumbent when $\pi>1/2$. De facto independence from the incumbent rises as the incumbent's hold weakens, even when de jure independence is unchanged. The Argentine court that had favored the Menem government began to rule against it as its hold weakened, which fits this prediction.
   378	\end{remark}
   379	
   380	\subsection{Repeat players and legal aid}
   381	
   382	Galanter's argument about repeat players can be stated as a contest. A repeat player litigates many similar cases and values a favorable ruling both for the case at hand and for the precedent it sets. A one-shotter values only the case at hand.
   383	
   384	\begin{proposition}[Repeat-player contest]
   385	\label{prop:judicial-power:repeat}
   386	A repeat player $R$ and a one-shotter $O$ contest a case by spending $e_R,e_O\ge 0$, and $R$ wins with probability $p_R=me_R/(me_R+e_O)$, where $m>0$ is the relative merit of $R$'s position. $O$ values winning at $v>0$. $R$ litigates $n\ge 1$ similar cases, and a favorable ruling is worth $v$ in the present case plus $\theta v$ in each of the $n-1$ future cases through precedent, with $\theta\in[0,1]$. In the unique equilibrium with positive spending,
   387	\[
   388	p_R=\frac{m(1+\theta(n-1))}{m(1+\theta(n-1))+1}.
   389	\]
   390	With equal merits ($m=1$), $p_R>1/2$ if and only if $\theta(n-1)>0$. The probability $p_R$ is nondecreasing in $n$ and $\theta$, strictly increasing in $n$ when $\theta>0$, and strictly increasing in $\theta$ when $n>1$. If legal aid reimburses a fraction $\lambda\in[0,1)$ of $O$'s spending, the equilibrium becomes
   391	\[
   392	p_R=\frac{m(1+\theta(n-1))(1-\lambda)}{m(1+\theta(n-1))(1-\lambda)+1},
   393	\]
   394	and with equal merits the advantage is eliminated exactly when $\lambda=\theta(n-1)/(1+\theta(n-1))$.
   395	\end{proposition}
   396	
   397	\begin{proof}
   398	Let $v_R=v(1+\theta(n-1))$. Consider first a lottery contest in which players $1$ and $2$ value the prize at $A>0$ and $B>0$, choose efforts $x_1,x_2\ge 0$ at unit cost, and player $1$ wins with probability $x_1/(x_1+x_2)$. Player $1$ maximizes $Ax_1/(x_1+x_2)-x_1$ and player $2$ maximizes $Bx_2/(x_1+x_2)-x_2$. Each objective is strictly concave in the player's own effort when the other's effort is positive, and the first-order conditions are
   399	\[
   400	\frac{A\,x_2}{(x_1+x_2)^2}=1,\qquad \frac{B\,x_1}{(x_1+x_2)^2}=1 .

hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '256,400p' papers/latex/judicial-power.tex | nl -ba -v 256" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   256	\subsection{Counterexample attempts}
   257	
   258	The strongest counterexample to \cref{thm:judicial-power:necessity} is a collective that resolves residual disputes by exit. Woodburn's immediate-return societies and the Ju/'hoansi practice of moving between camps come close. When exit is costless the theorem's forcing argument fails, and the failure is a genuine limit on the claim.
   259	
   260	\begin{proposition}[Exit substitution]
   261	\label{prop:judicial-power:exit}
   262	Suppose \cref{ass:arrival} holds and a disposition by self-help or abandonment ends persistence with probability at least $\kappa>0$, but a disposition by exit carries no risk to persistence and is always available. Then there are collectives that persist with probability one and in which no residual dispute is disposed of by determination.
   263	\end{proposition}
   264	
   265	\begin{proof}
   266	Consider a regional population divided among bands. Let every residual dispute be disposed of by one party moving to another band, which by hypothesis does not affect the persistence of the regional collective. The collective never incurs the hazard attached to self-help or abandonment, so it persists with probability one, and no determination occurs.
   267	\end{proof}
   268	
   269	The proposition narrows the claim. Adjudication is forced where exit is costly. Where exit is cheap, the judicial function can be thin, and the ethnography of immediate-return foragers is consistent with that prediction: talk, ridicule and departure do much of the work that courts do elsewhere \citep{woodburn1982,lee2013}. Two qualifications keep the narrowing in proportion. The cheap-exit condition is rare: it requires mobile residence, no stored wealth, and access to other groups on the same terms, which Woodburn identified as distinctive of a small set of societies. The ethnographies of these societies also record talk-based mediation alongside exit \citep{lee2013,wiessner2005}, so the function is thin rather than absent.
   270	
   271	The second counterexample attempt is a rule system that leaves no room for interpretation because a program executes it. If rules are code, the program decides, and no judge is needed.
   272	
   273	\begin{proposition}[Relocation of interpretation]
   274	\label{prop:judicial-power:relocation}
   275	Let a rule $r$ over cases $X$ be executed by a program $c:Z\to\mathcal{V}$ applied to recorded inputs $z=\zeta(x)$, where an encoding $\zeta:X\to Z$ records a case for the program. Let $\mathcal{E}(r)$ be the nonempty set of admissible encodings, those that competent members would accept as recording cases faithfully for the rule's purpose, and let the code-level open set be
   276	\[
   277	O_c(r)=\{x\in X : c(\zeta(x))\neq c(\zeta'(x))\text{ for some }\zeta,\zeta'\in\mathcal{E}(r)\}.
   278	\]
   279	Suppose the parties have agreed in advance that the verdict $c(\zeta_0(x))$ settles every case $x$ in a set $X_0\subseteq X$, for a designated $\zeta_0\in\mathcal{E}(r)$, and that neither party alone controls $c$ or $\zeta_0$ on $X_0$. Outside $X_0$ both the rule and the program have standing, so the admissible positions there are $\Read^{*}(r)=\Read(r)\cup\{c\circ\zeta:\zeta\in\mathcal{E}(r)\}$, with open set $O^{*}(r)$ computed from $\Read^{*}(r)$ as in \cref{def:judicial-power:open-texture}. Then $O(r)\cup O_c(r)\subseteq O^{*}(r)$, and $O^{*}(r)$ also contains every case at which some $\rho\in\Read(r)$ and some $c\circ\zeta$ with $\zeta\in\mathcal{E}(r)$ disagree. The following hold.
   280	\begin{enumerate}[label=(\roman*)]
   281	\item On $X_0$ the program with encoding $\zeta_0$ is a determination procedure in the sense of \cref{def:judicial-power:determination}.
   282	\item For every case $x\in O^{*}(r)\setminus X_0$ there are admissible positions with different verdicts, so disputes can arise at $x$, and those in which bargaining fails are residual disputes subject to \cref{thm:judicial-power:necessity}.
   283	\item $O_c(r)=\emptyset$ if and only if every admissible encoding yields the same verdict under $c$ for every case.
   284	\end{enumerate}
   285	\end{proposition}
   286	
   287	\begin{proof}
   288	For (i), on $X_0$ the program produces the verdict, neither party alone controls the program or the encoding by hypothesis, and both parties have agreed in advance to act on the verdict. The inclusion $O(r)\cup O_c(r)\subseteq O^{*}(r)$ holds because $\Read^{*}(r)$ contains both $\Read(r)$ and $\{c\circ\zeta:\zeta\in\mathcal{E}(r)\}$, and a case at which some reading $\rho\in\Read(r)$ and some program reading $c\circ\zeta$ disagree lies in $O^{*}(r)$ by definition. For (ii), the pair $(r,\Read^{*}(r))$ is a rule system in the sense of \cref{def:judicial-power:open-texture}, so a case in $O^{*}(r)\setminus X_0$ admits two admissible positions with different verdicts, and two members whose interests favor different verdicts can each endorse one, which is a dispute under \cref{def:judicial-power:dispute}. The parties have not agreed that the program settles such a case, so a dispute there in which bargaining fails is residual, and \cref{thm:judicial-power:necessity} applies. Claim (iii) restates the definition of $O_c(r)$.
   289	\end{proof}
   290	
   291	Encoding moves the open set from the terms of the rule to the recording of cases and to the gap between rule and program: whether a delivery occurred, whether a price feed was accurate, whether a reported event matched the contract's description. A deterministic program removes open texture only if every admissible encoding agrees, which is rare for rules about the world rather than about the program's own state. Unforeseen cases also fall outside $X_0$ almost by definition. Systems that execute agreements automatically therefore acquire arbiters, oracles, governance votes or forks, each of which is a determination procedure. Interpretation relocates; it does not vanish.
   292	
   293	The third counterexample attempt is pure self-help, a society in which wronged parties retaliate and nothing more. Evans-Pritchard's model of balanced opposition among Nuer lineages is the classic candidate. The reply is that the Nuer did not leave feuds to run indefinitely. Compensation through the leopard-skin chief ended them \citep{evanspritchard1940}. A society of pure self-help without any procedure for ending feuds would violate \cref{ass:cost} at every dispute, and the theorem predicts that it would not persist as a single collective. The falsifier for the necessity claim follows: a persistent collective with costly exit in which residual disputes about rule application are always settled by force of the parties or left open, without the collective dissolving.
   294	
   295	\subsection{Dependencies of the judicial function}
   296	\label{subsec:dependencies}
   297	
   298	A determination settles a dispute only if the losing party acts on it. Alexander Hamilton made the point about the federal judiciary in 1788: the judiciary ``may truly be said to have neither FORCE nor WILL, but merely judgment,'' and depends on the executive arm for the efficacy of its judgments \citep{hamilton1788}. The dependency is weaker than Hamilton's phrasing suggests.
   299	
   300	\begin{proposition}[Disjunctive dependency]
   301	\label{prop:judicial-power:disjunctive}
   302	Suppose the losing party in a determination gains $g>0$ by defying it, and complies if and only if $\ell+\sigma\ge g$, where $\ell\ge 0$ is the value it places on the procedure's legitimacy, including internalized obligation and reputation, and $\sigma\ge 0$ is the expected sanction for defiance. Then an effective determination requires $\ell>0$ or $\sigma>0$. Neither $\ell>0$ nor $\sigma>0$ is required by itself.
   303	\end{proposition}
   304	
   305	\begin{proof}
   306	If $\ell=\sigma=0$, then $\ell+\sigma=0<g$ and the loser defies, so the determination is not effective. For the second claim, a determination with $\ell\ge g$ and $\sigma=0$ is effective without sanction, and a determination with $\sigma\ge g$ and $\ell=0$ is effective without legitimacy.
   307	\end{proof}
   308	
   309	The judicial function therefore depends on the legitimation pillar or on the coercion pillar, and on neither specifically. In \cref{prop:judicial-power:disjunctive}, $\ell$ is the value a party places on complying because it regards the procedure as rightful, which Part IV calls normative legitimacy \citep{long2026ideological}, and $\sigma$ is the expected sanction for defiance, which Part V analyzes \citep{long2026coercive}. The Nuer settlement and the Ju/'hoansi talking-out rest mainly on legitimacy and the value of continued relations, while an imposed verdict in a party-state's political case rests mainly on sanction. Hamilton's executive arm is one source of $\sigma$. The reservoir of public support that James Gibson and coauthors measured for the United States Supreme Court is a source of $\ell$ \citep{gibson2003}.
   310	
   311	Because the dependency is disjunctive, it cannot be represented as two separate arcs into the judicial node. In the dependency digraph among the six functions that Part VII studies \citep{long2026formalized}, the arcs from legitimation and coercion into interpretation form a single or-condition, a hyperedge, and a proof that the digraph is strongly connected must treat them that way.
   312	
   313	The judicial function also feeds the other pillars. Interpretation changes rules through precedent, which enters rule-making through the rule of change. Reasoned judgments are public acts that shape common beliefs about what the rules are, which enters legitimation through the rule of recognition.
   314	
   315	\subsection{Functionalist objections}
   316	
   317	Carl Hempel warned that from the premise that a system needs some function one cannot infer that a particular institution exists, because functional equivalents may meet the need \citep{hempel1959}. \Cref{thm:judicial-power:necessity} respects the warning. Its conclusion is the existence of some determination procedure, and the minimal forms in \cref{tab:minimal} are exactly the functional equivalents that Hempel had in mind. Jon Elster argued that a functional explanation of an institution by its beneficial effects is legitimate only when a feedback mechanism links the effects back to the institution's persistence \citep{elster1983}. The theorem does not explain why any collective has a court. It states a condition that every persisting collective with costly exit satisfies. Robert Merton's distinction between manifest and latent functions, and his insistence on functional alternatives \citep{merton1968}, apply in the same way: courts have many latent functions, including legitimation and social control, and the theorem concerns none of them.
   318	
   319	\subsection{Necessity without capture}
   320	
   321	\begin{corollary}[Necessity does not imply capture]
   322	\label{cor:judicial-power:nonimplication}
   323	For every value $c\in[0,1]$ there are collectives that satisfy the hypotheses of \cref{thm:judicial-power:necessity}, implement adjudication, and have chain contestability $\Qchain=c$.
   324	\end{corollary}
   325	
   326	\begin{proof}
   327	\Cref{ass:arrival,ass:cost} constrain the arrival of residual disputes and the hazard attached to resolving them other than by determination. Neither refers to disclosure, access, independence or compliance. Take a collective satisfying both assumptions in which every residual dispute is resolved by determination, and assign its review links any values whose product is $c$, for example $q^{\mathrm{dis}}_t=q^{\mathrm{acc}}_t=q^{\mathrm{ind}}_t=1$ and $q^{\mathrm{cmp}}_t=c$. The hypotheses of the theorem still hold, adjudication is implemented, and $\Qchain=c$.
   328	\end{proof}
   329	
   330	The corollary is the judicial instance of the series claim that Proposition A does not imply Proposition B, which Part VII proves in general. The necessity theorem fixes that some determination procedure exists. It leaves the contestability of that procedure, and hence the persistence of captured rulings under \cref{prop:judicial-power:chain}, entirely open.
   331	
   332	\section{Literature on judicial power}
   333	\label{sec:literature}
   334	
   335	\subsection{Accounts of judicial independence}
   336	
   337	The literature on judicial power divides over one question: why would anyone who holds power allow a body to tell them what the law requires? The answers fall into four families, and the comparative analysis in \cref{sec:comparative} draws on all of them.
   338	
   339	The first family treats independent courts as a device that serves the powerful. William Landes and Richard Posner argued that an independent judiciary makes legislative deals durable, because judges who enforce statutes as enacted protect the bargains that interest groups purchased from earlier legislatures \citep{landes1975}. J.\,Mark Ramseyer argued that politicians tolerate independent courts when they expect to lose office, because a court that binds the next government protects them \citep{ramseyer1994}. Matthew Stephenson formalized the insurance logic as a repeated game between parties that alternate in power \citep{stephenson2003}, and Keith Whittington showed that politically fragmented coalitions in the United States have repeatedly supported the exercise of judicial review against their own legislative partners \citep{whittington2005}. Ran Hirschl's hegemonic preservation thesis is a sharper version: elites facing electoral decline transfer power to courts whose judges share their commitments, as he argued for Israel, Canada, New Zealand and South Africa \citep{hirschl2001,hirschl2004}. The insurance and preservation accounts agree that independence is chosen for strategic reasons. They differ on whom it protects.
   340	
   341	The second family studies courts under authoritarian rule. Tom Ginsburg and Tamir Moustafa collected evidence that authoritarian rulers use courts for social control, for legitimation, to commit credibly to investors, to discipline their own administrators and to resolve disputes within the ruling coalition \citep{ginsburg2008}. Moustafa's study of Egypt's Supreme Constitutional Court shows a regime that empowered a court to reassure investors and then found the court supporting challenges to the regime \citep{moustafa2007}. Gretchen Helmke's study of Argentina showed that judges without secure tenure rule against outgoing governments when they expect a change in power, a pattern she called strategic defection \citep{helmke2005}. These works establish that courts matter under authoritarianism and that their independence varies by case type and by the political calendar.
   342	
   343	The third family asks what makes judges' rulings stick. Georg Vanberg's study of the German Federal Constitutional Court argues that public support protects a court against noncompliance when the public can observe whether the government complies \citep{vanberg2005}. Gibson and coauthors found that the United States Supreme Court's legitimacy survived its controversial decision in the 2000 presidential election, which they attributed to a reservoir of goodwill \citep{gibson2003}. Alec Stone Sweet showed how European constitutional courts became co-legislators whose anticipated rulings shape the drafting of statutes \citep{stonesweet2000}. Mark Tushnet compared strong-form review, in which courts have the last word, with weak-form review, in which legislatures can respond, and argued that weak-form systems can protect social rights without judicial supremacy \citep{tushnet2008}.
   344	
   345	The fourth family concerns who uses courts and who wins. Marc Galanter distinguished repeat players, who litigate many similar cases, from one-shotters, and argued that repeat players come out ahead because they can play for favorable rules as well as for immediate outcomes \citep{galanter1974}. Charles Epp showed that rights revolutions depended on a support structure of lawyers, organizations and funding rather than on constitutional text alone \citep{epp1998}. Adam Bonica and Maya Sen placed judges and lawyers on a common ideological scale and found that selection channels shape the ideological composition of the American judiciary \citep{bonica2017}.
   346	
   347	Comparative legal history supplies evidence of a different kind, from religious, ecclesiastical and royal courts that the political science literature seldom examines. Wael Hallaq's work on Islamic law describes a judicial order in which state-appointed qadis applied a law developed by jurists who were not state officials \citep{hallaq2005,hallaq2009}. Harold Berman argued that the papal reforms of the late eleventh century produced the first modern Western legal system and a plurality of jurisdictions that limited every authority, including the Church \citep{berman1983}. Richard Kagan's study of litigation in Castile, David Bell's study of barristers in Paris, and Irene Fosi's study of papal justice show courts in early modern Catholic monarchies used by large numbers of ordinary litigants \citep{kagan1981,bell1994,fosi2011}. The socialist-legality literature, from Harold Berman's interpretation of Soviet law to Stanley Lubman's and Carl Minzner's studies of China, traces courts embedded in party rule \citep{berman1963,lubman1999,minzner2011}.
   348	
   349	The strategic accounts explain why independence varies but take the existence of courts for granted. The legal-historical accounts document courts in many regimes but rarely compare them on common dimensions. A shared vocabulary, the judicial layer and its contestability vector, lets both be read as answers to one question: how is the universal judicial function coupled to the other five?
   350	
   351	\subsection{The insurance model}
   352	
   353	Why would a governing coalition allow courts to bind it? The insurance account answers that independence is a hedge against losing power \citep{landes1975,ramseyer1994,stephenson2003}.
   354	
   355	\begin{proposition}[Insurance model]
   356	\label{prop:judicial-power:insurance}
   357	An incumbent chooses court independence $\iota\in[0,1]$, which persists into the next period. In each period the office holder can take an abusive action that yields it $g>0$ and costs the other side $L>0$, and the court blocks the action with probability $\iota$. The incumbent loses office before the next period with probability $\pi\in[0,1]$ and discounts the future by $\delta\in(0,1]$. Let
   358	\[
   359	\pi^{*}=\frac{g(1+\delta)}{\delta(g+L)}.
   360	\]
   361	The incumbent's expected payoff is maximized at $\iota^{*}=1$ if $\pi>\pi^{*}$, at $\iota^{*}=0$ if $\pi<\pi^{*}$, and by every $\iota\in[0,1]$ if $\pi=\pi^{*}$. The threshold $\pi^{*}$ decreases in $L$ and $\delta$ and increases in $g$. If $g\ge\delta L$, then $\pi^{*}\ge 1$ and independence is never strictly optimal.
   362	\end{proposition}
   363	
   364	\begin{proof}
   365	The incumbent's payoff is
   366	\[
   367	\Phi(\iota)=(1-\iota)g+\delta\big[(1-\pi)(1-\iota)g-\pi(1-\iota)L\big]=(1-\iota)\big[g(1+\delta)-\delta\pi(g+L)\big].
   368	\]
   369	$\Phi$ is linear in $\iota$ with slope $-\big[g(1+\delta)-\delta\pi(g+L)\big]$, which is positive when $\pi>\pi^{*}$, negative when $\pi<\pi^{*}$ and zero when $\pi=\pi^{*}$. The comparative statics follow from differentiating $\pi^{*}$: $\partial\pi^{*}/\partial L=-g(1+\delta)/[\delta(g+L)^2]<0$, $\partial\pi^{*}/\partial\delta=-g/[\delta^{2}(g+L)]<0$, and $\partial\pi^{*}/\partial g=(1+\delta)L/[\delta(g+L)^2]>0$. Finally, $\pi^{*}\ge 1$ if and only if $g(1+\delta)\ge\delta(g+L)$, which simplifies to $g\ge\delta L$.
   370	\end{proof}
   371	
   372	The model's assumptions do the work, and they should be stated plainly. Independence chosen today must persist, which requires that institutional change be costly; Landes and Posner's account relies on the same stickiness \citep{landes1975}. The court must bind whoever holds office, which excludes a court that binds only the opposition. The model is linear, which produces an all-or-nothing choice; a convex cost of independence would produce interior solutions with the same comparative statics. In the vocabulary of \cref{sec:layer}, $\iota$ is the independence component $q^{\mathrm{ind}}_t$, and when the incumbent appoints the judges through the appointment channel, keeping $\iota$ low is the same as keeping $C_{\pP\pJ}$ high.
   373	
   374	The result says that independence is more likely where the incumbent expects to lose power, where abuse by the other side would be costly, and where the incumbent is patient. It fits the variation across party-states and secular democracies described in \cref{sec:comparative}: a ruling party with a low $\pi$ has little reason to grant independence, and a fragmented democracy with a high $\pi$ has strong reason. Ramseyer used the same logic to explain why Japanese courts were less independent than American ones during a long period of single-party dominance \citep{ramseyer1994}.
   375	
   376	\begin{remark}[Strategic defection]
   377	Helmke's account of Argentine judges adds a judge-side version of the same logic \citep{helmke2005}. Assume that a judge without secure tenure is sanctioned, with loss $s>0$, only by whichever side holds power after the ruling takes effect and only if the ruling went against that side; that the case sets the incumbent against the side that would replace it; and that the merits are balanced. Ruling against the incumbent then risks $(1-\pi)s$, and ruling for it risks $\pi s$, so the judge rules against the incumbent when $\pi>1/2$. De facto independence from the incumbent rises as the incumbent's hold weakens, even when de jure independence is unchanged. The Argentine court that had favored the Menem government began to rule against it as its hold weakened, which fits this prediction.
   378	\end{remark}
   379	
   380	\subsection{Repeat players and legal aid}
   381	
   382	Galanter's argument about repeat players can be stated as a contest. A repeat player litigates many similar cases and values a favorable ruling both for the case at hand and for the precedent it sets. A one-shotter values only the case at hand.
   383	
   384	\begin{proposition}[Repeat-player contest]
   385	\label{prop:judicial-power:repeat}
   386	A repeat player $R$ and a one-shotter $O$ contest a case by spending $e_R,e_O\ge 0$, and $R$ wins with probability $p_R=me_R/(me_R+e_O)$, where $m>0$ is the relative merit of $R$'s position. $O$ values winning at $v>0$. $R$ litigates $n\ge 1$ similar cases, and a favorable ruling is worth $v$ in the present case plus $\theta v$ in each of the $n-1$ future cases through precedent, with $\theta\in[0,1]$. In the unique equilibrium with positive spending,
   387	\[
   388	p_R=\frac{m(1+\theta(n-1))}{m(1+\theta(n-1))+1}.
   389	\]
   390	With equal merits ($m=1$), $p_R>1/2$ if and only if $\theta(n-1)>0$. The probability $p_R$ is nondecreasing in $n$ and $\theta$, strictly increasing in $n$ when $\theta>0$, and strictly increasing in $\theta$ when $n>1$. If legal aid reimburses a fraction $\lambda\in[0,1)$ of $O$'s spending, the equilibrium becomes
   391	\[
   392	p_R=\frac{m(1+\theta(n-1))(1-\lambda)}{m(1+\theta(n-1))(1-\lambda)+1},
   393	\]
   394	and with equal merits the advantage is eliminated exactly when $\lambda=\theta(n-1)/(1+\theta(n-1))$.
   395	\end{proposition}
   396	
   397	\begin{proof}
   398	Let $v_R=v(1+\theta(n-1))$. Consider first a lottery contest in which players $1$ and $2$ value the prize at $A>0$ and $B>0$, choose efforts $x_1,x_2\ge 0$ at unit cost, and player $1$ wins with probability $x_1/(x_1+x_2)$. Player $1$ maximizes $Ax_1/(x_1+x_2)-x_1$ and player $2$ maximizes $Bx_2/(x_1+x_2)-x_2$. Each objective is strictly concave in the player's own effort when the other's effort is positive, and the first-order conditions are
   399	\[
   400	\frac{A\,x_2}{(x_1+x_2)^2}=1,\qquad \frac{B\,x_1}{(x_1+x_2)^2}=1 .

exec
/usr/local/bin/zsh -lc "sed -n '401,556p' papers/latex/judicial-power.tex | nl -ba -v 401" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   401	\]
   402	Dividing gives $x_1/x_2=A/B$, so player $1$ wins with probability $A/(A+B)$, and substituting back gives the unique positive solution $x_1=A^2B/(A+B)^2$, $x_2=AB^2/(A+B)^2$.
   403	
   404	In the litigation contest, write $x_1=me_R$ and $x_2=e_O$. Then $R$'s payoff is $v_Rx_1/(x_1+x_2)-x_1/m$, which is $1/m$ times $mv_Rx_1/(x_1+x_2)-x_1$, so $R$ behaves as player $1$ with $A=mv_R$, and $O$ behaves as player $2$ with $B=v$. Hence $p_R=mv_R/(mv_R+v)$, which is the first expression. With reimbursement at rate $\lambda$, $O$'s payoff is $vx_2/(x_1+x_2)-(1-\lambda)x_2$, which is $(1-\lambda)$ times the payoff of a player with valuation $B=v/(1-\lambda)$ and unit cost; substituting gives the second expression. With $m=1$ the second expression equals $1/2$ exactly when $(1+\theta(n-1))(1-\lambda)=1$, which gives the stated $\lambda$. Finally, $p_R$ is strictly increasing in $1+\theta(n-1)$, which is nondecreasing in $n$ and $\theta$, strictly increasing in $n$ when $\theta>0$, and strictly increasing in $\theta$ when $n>1$.
   405	\end{proof}
   406	
   407	Repeat litigants win more often than one-shot litigants with equally good cases whenever rulings set precedent, because a repeat litigant bids for future cases as well as the case at hand. Legal aid removes the advantage only when the subsidy to the one-shotter matches the share of the repeat litigant's stake that comes from future cases, $\lambda=\theta(n-1)/[1+\theta(n-1)]$. Since that share rises with the repeat litigant's caseload and with the precedential weight of rulings, modest legal-aid budgets leave repeat players ahead in forums whose rulings bind later cases. \citet{galanter1974} identifies further advantages, including expertise, economies of scale and informal relations with court personnel, which add to the precedent effect modeled here and raise the subsidy needed to equalize access.
   408	
   409	The model gives one reason why resource shares buy favorable rulings, a relation Part I measures for every pillar \citep{long2026financial}, and it locates the remedy in the access component $q^{\mathrm{acc}}_t$. It is also the core of the coupling $C_{\pJ\pW}$. Workers, tenants and consumers are usually one-shotters facing repeat players, so access to courts determines whether producers can contest the rules that govern their work, which is the judicial form of the source's hypothesis about worker voice \citep{largo2026hbs}.
   410	
   411	\section{Comparative analysis across six regime types}
   412	\label{sec:comparative}
   413	
   414	\subsection{Coding conventions}
   415	
   416	Qualitative coding is the only defensible form of comparison at present, because no preregistered coding of $H$, $Q$, $U_t$ or $\Integ_t$ exists for any real polity, and the series does not report numbers without one \citep{largo2026hbs}. Each regime type is therefore compared on five questions: which institutions hold the judicial function; how concentrated control over final determinations is ($H_{\pJ,t}$) and how contestable it is ($\mathbf{q}_t$); how strongly the judicial function is coupled to the other five pillars; what preserves accountability; and which capture episodes and checks are documented.
   417	
   418	The six types are ideal types, and real polities mix them. The United States is both a market-capitalist society and a secular democracy; Sweden is both a social democracy and a secular democracy. The comparison assigns each case to the type whose distinctive pathway it best illustrates. The market-capitalist section concentrates on the channel from private resources to courts, and the secular-democracy section on the design of the relation between courts and elected bodies.
   419	
   420	\subsection{Market-capitalist societies}
   421	
   422	In market-capitalist societies the judicial function is held by courts of general jurisdiction staffed by appointed or elected judges, by a large private legal profession, by administrative tribunals and by private arbitration. The United States is the principal illustration. Federal judges are nominated by the President and confirmed by the Senate, many state judges are elected, and since \citet{marbury1803} courts have reviewed the constitutionality of statutes. Hamilton's defense of life tenure in \emph{Federalist} No.~78 rests on the claim that ``the interpretation of the laws is the proper and peculiar province of the courts'' \citep{hamilton1788}.
   423	
   424	Concentration has two levels. Across ordinary litigation, control over final determinations is spread across thousands of judges, so $H_{\pJ,t}$ is low. For constitutional questions a single court holds the last word, and concentration at the apex is high. Disclosure is high, because opinions are published with reasons. Independence is protected by tenure and salary guarantees for federal judges and is weaker for elected state judges who must raise campaign funds. Compliance by government with adverse rulings is high, and Gibson and coauthors attribute part of it to diffuse public support \citep{gibson2003}. Access is the weakest link. Litigation is costly, and the advantage of organized repeat players is the core of Galanter's argument \citep{galanter1974}.
   425	
   426	The distinctive coupling runs from resources to adjudication, the pair $C_{\pF\pJ}$ that Part I treats \citep{long2026financial}. Three channels are documented. Repeat players who can invest in rule-shaping litigation obtain favorable precedents (\cref{prop:judicial-power:repeat}). Rights litigation depends on a support structure of funded organizations \citep{epp1998}. Campaign spending in judicial elections ties litigants to judges directly.
   427	
   428	Judicial doctrine also shapes the channel from resources to rule-making. In \citet{citizensunited2010} the Supreme Court held the federal ban on independent expenditures by corporations and unions unconstitutional. The ruling changed the rules governing the path from $\pF$ to $\pP$, so the judicial pillar acted as a gatekeeper between two others. It is coupling, not capture: the decision was reached through the ordinary procedure, and capture requires privileged access and a weakened check.
   429	
   430	The clearest documented episode of capture risk is \citet{caperton2009}. While Massey's appeal of a large jury verdict was pending, Massey's chairman spent about three million dollars supporting Brent Benjamin's 2004 campaign for the West Virginia Supreme Court of Appeals. Benjamin won, declined to recuse himself, and joined the majority that reversed the verdict. The United States Supreme Court held that ``in all the circumstances of this case, due process requires recusal.'' Under \cref{def:judicial-power:capture} the facts establish privileged access and a threat to independence, but the Court did not find actual bias; it found a serious risk of it. The episode documents a capture risk and a check that operated through appeal, which is the pattern \cref{prop:judicial-power:chain} predicts when the access and independence links of the review chain hold.
   431	
   432	Outside the resource channel, market-capitalist adjudication is loosely coupled to the other pillars, with one exception in production. The coupling with legitimation runs through law schools, the bar and the public reputation of courts, professional institutions that no single coalition commands. The coupling with coercion is moderate: prosecutors decide which disputes reach the courts, and the enforcement of judgments depends on executive agencies, as Hamilton observed \citep{hamilton1788}. The exception is the arbitration clause in employment and consumer contracts, which moves disputes from public courts to private forums whose awards set no public precedent. Firms that draft such clauses are repeat players in Galanter's sense \citep{galanter1974}, so the clauses raise $C_{\pJ\pW}$ on terms set by one side.
   433	
   434	\subsection{Communist party-states}
   435	
   436	In communist party-states the judicial function is held by courts, by the procuracy, by party bodies that oversee legal work, and by a bar organized under state discipline. Harold Berman's interpretation of Soviet law described a procuracy that combined criminal prosecution with general supervision of the legality of administrative acts \citep{berman1963}. That combination puts prosecution and legality review in one organ, so $C_{\pJ\pC}$ is high by design. Eugene Huskey's history of the Soviet bar traces how advocates were organized into collegia subject to state control between 1917 and 1939 \citep{huskey1986}. In the People's Republic of China, Lubman's study of legal reform after Mao describes courts that operate inside a structure of party supervision, with judicial decisions in sensitive cases subject to review by bodies outside the bench \citep{lubman1999}.
   437	
   438	Concentration depends on the type of case. For ordinary civil and commercial disputes, determinations are made by many courts with little party involvement, and concentration is low. For politically salient cases, the last word rests with party organs, and concentration at the level of the ruling coalition is high. This is the two-tier structure of \cref{def:judicial-power:boundness}. The appointment of judges and procurators through the party's personnel system makes $C_{\pP\pJ}$ high, a coupling Part II codes through its appointment channel. Disclosure is limited for political cases. Access has grown in some areas: Peerenboom documents administrative litigation in which citizens sue government agencies \citep{peerenboom2002}. Compliance by the ruling coalition with adverse determinations is low in the political tier, so ruler-boundness is low.
   439	
   440	Ginsburg and Moustafa's list of authoritarian court functions fits the party-state well: courts discipline lower officials, resolve commercial disputes and give legal form to repression \citep{ginsburg2008}. Peter Solomon's study of Soviet criminal justice under Stalin documents courts that operated under campaign directives and pressure from party and state bodies, so that the volume and severity of prosecution followed political priorities \citep{solomon1996}. That is the strongest documented case of judicial capture in the sense of \cref{def:judicial-power:capture}: privileged direction of determinations by the party, the elimination of independent review, and material evidence in the archival record linking directives to outcomes.
   441	
   442	The party-state also contains checks, and they are documented. Kathryn Hendley's study of labor law in the late Soviet period examines how far law mattered in employment relations as legal reform began \citep{hendley1996}. Peerenboom argues that Chinese reform produced a thin rule of law in which legal rules increasingly bind officials in ordinary matters \citep{peerenboom2002}. Minzner identifies a reversal after the mid-2000s, in which the party shifted emphasis from courts toward mediation, petitioning and the maintenance of stability, and retreated from legal professionalism \citep{minzner2011}. The trajectory shows that the coupling between rule-making and adjudication in a party-state is a variable that leaders adjust, not a fixed property of the regime. The insurance model of \cref{prop:judicial-power:insurance} predicts this: a ruling party that expects to stay in power gains little from independent courts.
   443	
   444	The party-state also couples adjudication to legitimation and production, because it treats law as an instrument of education and of economic administration. Berman described Soviet law as parental, in the sense that courts were charged with educating citizens in the values of the regime as well as deciding their disputes \citep{berman1963}, which raises $C_{\pJ\pI}$. The same legal order handled labor disputes and disputes between state enterprises, so that the enforcement of plan discipline passed through adjudicative bodies \citep{berman1963,hendley1996}, which raises $C_{\pJ\pW}$.
   445	
   446	\subsection{Social democracy and democratic socialism}
   447	
   448	In social democracies the judicial function is spread across ordinary courts, specialized administrative and labor courts, ombudsmen, and parliamentary bodies that review the constitutionality of legislation. The Nordic countries illustrate a model of restrained judicial review. Sweden's Instrument of Government directs that a court which finds that a provision conflicts with a rule of fundamental law shall not apply it \citep{swedenig}. A reform in 2010 removed an earlier requirement that the conflict be manifest before a court could set a statute aside \citep{jonssoncornell2016}.
   449	
   450	Finland's constitution assigns primary review of legislative proposals to Parliament's Constitutional Law Committee, and allows courts to give primacy to the Constitution only when applying an act would be in evident conflict with it \citep{finlandconst}. Constitutional interpretation is thus shared between a parliamentary committee and the courts, which raises $C_{\pP\pJ}$ by design. Tushnet's weak-form review describes this arrangement \citep{tushnet2008}.
   451	
   452	Germany shows a different social-market pattern. Its Federal Constitutional Court exercises strong-form review, and Vanberg's study shows that its ability to obtain compliance depends on public support and on the visibility of the government's response \citep{vanberg2005}. Stone Sweet's account of constitutional courts as co-legislators draws heavily on the German and French experience \citep{stonesweet2000}. The social-democratic family therefore contains both the weakest and some of the strongest forms of constitutional review among democracies.
   453	
   454	Concentration of ordinary adjudication is low. Disclosure is high, and the ombudsman adds a channel of review outside the courts. Sweden's Parliamentary Ombudsmen are elected by the Riksdag to supervise the application of laws in public activities \citep{swedenig}. Access is supported by legal aid and by the low cost of administrative appeals. Independence is protected by constitutional prohibitions on interference: the Instrument of Government provides that neither the Riksdag nor any public authority may determine how a court shall adjudicate an individual case \citep{swedenig}. Compliance by government is high.
   455	
   456	The distinctive coupling is $C_{\pJ\pW}$, through corporatist labor adjudication. The Swedish Labour Court sits with neutral members and with members representing employer and employee interests, most of whom are appointed on the nomination of the principal labor-market organizations, and its judgment is final \citep{arbetsdomstolen}. This design gives the organized parties of production a place inside the judicial function. It also creates a recognizable risk: a forum whose members are nominated by organizations may favor those organizations over outsiders. The European Court of Human Rights addressed that risk for a related Swedish tribunal in \citet{langborger1989}, finding a violation of the right to an independent and impartial tribunal when lay assessors in a housing and tenancy court were nominated by organizations whose interests ran against the applicant's. The European Commission of Human Rights later declined to find a violation in a Labour Court case in which the nominating organizations had no common interest opposed to the applicant's \citep{stallarholmens1990}. The two rulings mark the line between coupling and capture with some precision: organizational nomination is compatible with impartiality unless the nominators share an interest in the outcome.
   457	
   458	Bo Rothstein's study of Swedish social reform emphasizes that the implementation of universal programs depends on bureaucratic organization and on citizens' trust in impartial administration \citep{rothstein1996}. That is the legitimation coupling $C_{\pJ\pI}$ in its social-democratic form: the authority of courts and ombudsmen rests on a shared belief in impartial application. We found no documented case of systematic judicial capture by an economic coalition in the Nordic sources reviewed. The risks identified in the literature are of another kind: legislative supremacy weakens the counter-majoritarian check when a governing majority is durable, and corporatist adjudication can close the forum to actors outside the organized parties.
   459	
   460	\subsection{Islamic states}
   461	
   462	Islamic states derive political legitimacy from religious law, but the institutions that interpret it have varied widely across schools, dynasties and centuries. Hallaq describes the classical arrangement as a division of labor \citep{hallaq2009}. Rulers appointed qadis to decide cases. Jurists who were not state officials developed the law, and muftis issued nonbinding opinions, fatwas, that litigants and judges consulted \citep{masud1996}. Rulers also held a jurisdiction for the redress of grievances, the \emph{mazalim}, which al-Mawardi's eleventh-century treatise on government discusses alongside the qadi's office \citep{mawardi1996}. Hallaq's further claim that the jurists' independent authority confined rulers to administrative regulation is a contested thesis \citep{hallaq2009,hallaq2013}. Sami Zubaida emphasizes the long interplay of state power and religious law \citep{zubaida2003}, and Joseph Schacht's older synthesis, which presents the classical law as largely detached from practice, is read critically by later scholarship \citep{schacht1964}.
   463	
   464	Court records contradict the older image of Islamic adjudication as unpredictable. Max Weber used the term ``kadi justice'' for an ideal type of adjudication guided by substantive considerations of the individual case rather than by general rules \citep{weber1978}. Haim Gerber tested that characterization against Ottoman court records and rejected it for the courts he examined \citep{gerber1994}. Ronald Jennings's study of the seventeenth-century court of Kayseri shows regular procedure, extensive records and wide use by ordinary inhabitants \citep{jennings1978}.
   465	
   466	Ottoman law also shows a ruler's legislation reconciled with jurists' law through interpretation rather than by command. Colin Imber's study of Ebu's-su'ud, the Ottoman chief mufti in the mid-sixteenth century, shows sultanic law, the \emph{kanun}, brought into harmony with jurists' law through juristic opinion \citep{imber1997}. Brinkley Messick's study of Yemen traces how the transmission of authoritative texts structured judicial power in a different Muslim society \citep{messick1993}.
   467	
   468	Concentration in the classical and Ottoman pattern was moderate. Qadis were numerous and appointed by the ruler, which made $C_{\pP\pJ}$ substantial, but the law they applied was developed by a scholarly class with its own institutions of training, the madrasas that George Makdisi studied \citep{makdisi1981}. The same scholars taught, issued opinions and judged, so the legitimation coupling $C_{\pJ\pI}$ was high through the ulama. Plurality of schools and the availability of independent muftis supplied contestability: a litigant could seek an opinion from a jurist outside the court.
   469	
   470	Saudi Arabia couples uncodified juristic interpretation to royal appointment and royal enforcement. Its Basic Law of Governance declares the judiciary an independent authority subject to no authority other than the Islamic Shari'ah and requires courts to apply the Shari'ah as drawn from the Qur'an and the Sunna. The same law provides that judges are appointed and their service terminated by royal order on the proposal of the supreme judicial council, assigns the implementation of judgments to the King or his deputy, and declares the King the ultimate source of the state's authorities \citep{saudibasic}. Frank Vogel's study describes a judiciary that applies largely uncodified Islamic law through judges' own interpretation, alongside royal regulations and the Board of Grievances as an administrative jurisdiction \citep{vogel2000}, and Nathan Brown's comparison of courts in Egypt and the Gulf places the Saudi system within a regional range of arrangements \citep{brown1997}. In this design $C_{\pP\pJ}$ runs through royal appointment, and $C_{\pJ\pC}$ through royal enforcement of judgments.
   471	
   472	Iran's constitution builds judicial review into rule-making by assigning the interpretation of all legislation to a council of jurists. The jurists of the Guardian Council decide whether all laws and regulations conform to Islamic criteria \citep{iranconst}. The Council has twelve members: six jurists in Islamic law selected by the Leader, and six jurists elected by the parliament from among nominees of the head of the judiciary. Every bill passed by parliament goes to the Council, which must review it within ten days. Islamic compatibility is decided by a majority of the six religious jurists, constitutional compatibility by a majority of all members. The Council also supervises elections. Hirschl treats Iran as a leading case of constitutional theocracy, in which religious interpretation is constitutionalized and assigned to a council \citep{hirschl2010}.
   473	
   474	The ordinary judiciary is tied to the same apex. The Leader appoints the head of the judiciary for five years. The constitution also provides that judges cannot be removed except after trial and proof of guilt, and that citizens may seek annulment of unlawful regulations in the Court of Administrative Justice \citep{iranconst}.
   475	
   476	The Iranian design concentrates interpretation at the apex and couples it to rule-making and legitimation. The Leader's appointments reach both the Guardian Council and the judiciary, and the Council's religious jurists decide whether legislation is valid. Asghar Schirazi documents repeated conflict between parliament and the Guardian Council in the 1980s, which led to the creation of the Expediency Council to resolve deadlocks between them \citep{schirazi1997}. Wilfried Buchta describes the Council's use of its electoral supervision to screen candidates \citep{buchta2000}. The vetting of bills and the screening of candidates are rule-making acts, a veto over legislation and over entry, and Part II codes them that way \citep{long2026political}. The judgments on which they rest, whether a bill conforms to Islamic criteria and to the Constitution, are interpretive determinations. One body performing both kinds of act is fusion, with high $C_{\pP\pJ}$.
   477	
   478	Fusion is not yet capture. A capture finding under \cref{def:judicial-power:capture} would require evidence that particular screening decisions followed privileged access and had material effect, and no such coding is attempted here. The system also contains checks: senior clerical authorities outside the state, whose plurality Muhammad Qasim Zaman documents across Muslim societies \citep{zaman2002}, and the constitutional provisions on judicial tenure and administrative review.
   479	
   480	\subsection{Catholic monarchies in early modern Europe}
   481	
   482	In the Catholic monarchies of early modern Europe the judicial function was divided among royal courts, the courts of the Church, the Inquisition, municipal and seigneurial courts, and, in the Papal State, tribunals under a ruler who was also head of the Church. Berman's account of the papal reforms of the late eleventh century places the origin of this plurality in the separation of an ecclesiastical legal order from the secular ones \citep{berman1983}. James Brundage and Richard Helmholz describe the canon law and the church courts that applied it to marriage, testaments, clerical discipline and sin \citep{brundage1995,helmholz1996}. Overlapping jurisdictions produced constant conflict over which court could hear a case, and that conflict was itself a check: litigants could sometimes choose their forum, and each jurisdiction watched the others.
   483	
   484	In Habsburg Castile the royal chanceries at Valladolid and Granada heard appeals from across the kingdom, and Kagan's study documents a large volume of litigation by ordinary subjects in the sixteenth and seventeenth centuries \citep{kagan1981}. Access was therefore substantial for those who could pay. The Spanish Inquisition, a tribunal under royal control that judged offenses against the faith, coupled adjudication with the legitimation pillar as tightly as any institution in this comparison. Henry Kamen's revisionist history argues that its scale and severity were smaller than its later reputation suggested \citep{kamen1997}, and the quantitative studies collected by Gustav Henningsen and John Tedeschi make the trial records available for testing such claims \citep{henningsen1986}. James Given's study of the medieval inquisition in Languedoc shows inquisitors using records and interrogation as techniques of power \citep{given1997}. Inquisitorial courts handed those they condemned to death to the secular authorities for execution, so the coercion coupling $C_{\pJ\pC}$ ran through the royal arm \citep{kamen1997}.
   485	
   486	In the Crown of Aragon the Justicia was an officer charged with defending the kingdom's laws against royal encroachment. J.\,H. Elliott's history of imperial Spain recounts how Philip II's pursuit of his former secretary Antonio P\'erez, who had taken refuge under Aragonese jurisdiction, led to unrest in 1591 and to the execution of the Justicia \citep{elliott1963}. The episode is a documented case of a ruler overriding a jurisdictional check by force, in which the coercion pillar removed a judicial constraint on the political one.
   487	
   488	In Bourbon France, venal officeholding gave the parlements independence from the crown and tied adjudication to private wealth. Judicial offices were purchased and heritable property, so the crown could not remove judges without compensating them \citep{doyle1996}. That security allowed the Parlement of Paris to remonstrate against royal edicts. The crown answered with the formal session called the lit de justice, which compelled registration, and in 1771 with Chancellor Maupeou's suppression and reconstruction of the parlements, which was reversed in 1774 \citep{swann1995}. Registration and remonstrance are rule-making acts in the series' classification \citep{long2026political}; the parlements' judicial power lay in their appellate jurisdiction.
   489	
   490	In that capacity the parlements contested the Church's authority. Dale Van Kley shows them intervening in the 1750s against clergy who refused sacraments to Jansenists \citep{vankley1996}, a case in which the judicial pillar checked the legitimation pillar. The property right that insulated judges from the monarch also entrenched a corporate interest in the offices themselves \citep{doyle1996}, a coupling of adjudication to resources ($C_{\pF\pJ}$). David Bell shows the Paris barristers acquiring a political voice in the same period \citep{bell1994}.
   491	
   492	The Papal State fused functions at its apex. Paolo Prodi described the pope as both spiritual head and temporal prince, ``one body and two souls'' in his subtitle \citep{prodi1987}. Fosi's study of papal justice between 1500 and 1750 shows a system of tribunals and a practice of petitioning the pope for justice that gave subjects a route around local courts \citep{fosi2011}. Petitioning raised access while concentrating final authority in the ruler. Across the Catholic monarchies, concentration was moderate, $C_{\pJ\pI}$ was high in ecclesiastical and inquisitorial courts, $C_{\pP\pJ}$ varied with the crown's success in subordinating rival jurisdictions, and contestability depended heavily on the competition among jurisdictions.
   493	
   494	\subsection{Secular democracies}
   495	
   496	In secular democracies the judicial function is held by constitutional or supreme courts, ordinary and administrative courts, judicial councils, and international courts. The defining design question is the relation between courts and elected bodies. Constitutional courts in France and Germany became co-legislators whose anticipated rulings shape legislation \citep{stonesweet2000}. Hirschl's hegemonic preservation thesis holds that constitutionalization in Israel, Canada, New Zealand and South Africa transferred power to courts at moments when established elites faced electoral threats \citep{hirschl2001,hirschl2004}. The thesis is contested on timing and motive, and it is stated below as a hypothesis with a falsifier.
   497	
   498	Rafael La Porta and coauthors coded constitutional provisions on judicial independence and constitutional review across countries and related them to economic and political freedom \citep{laporta2004}. Lars Feld and Stefan Voigt distinguished de jure from de facto independence and found that the de facto measure, not the de jure measure, was associated with economic growth in their sample \citep{feld2003}. The distinction is the central measurement problem of this Part: constitutional guarantees are not the same as observed independence.
   499	
   500	Concentration of ordinary adjudication is low in secular democracies, and concentration at the constitutional apex is high. Disclosure and access are generally high. Independence and compliance depend on the political environment. Vanberg's public-support mechanism explains why governments comply with courts whose rulings voters observe \citep{vanberg2005}, and Whittington's account explains why fragmented coalitions sustain judicial review \citep{whittington2005}. When a governing coalition becomes dominant, both mechanisms weaken.
   501	
   502	The documented capture episodes in this regime type are court-packing and court-curbing by elected governments. Steven Levitsky and Lucan Way identify the judiciary as one of the arenas in which competitive authoritarian incumbents tilt the field against opponents \citep{levitsky2010}. Argentina provides a documented case. In 1990 the government of Carlos Menem enlarged the Supreme Court from five to nine members, and the resulting court became known for an ``automatic majority'' that favored the government's interests \citep{hevia2008}. Helmke's study of the same court shows the reverse movement: as the government's hold weakened, justices began to rule against it \citep{helmke2005}. The two observations together illustrate both halves of the series' thesis. The judicial function persisted throughout; its coupling to the political pillar rose and fell with the political calendar.
   503	
   504	The couplings $C_{\pJ\pI}$, $C_{\pJ\pC}$ and $C_{\pJ\pW}$ are generally lower in secular democracies than in the other types, because law schools, prosecutors and labor organizations are governed separately from the courts. Low coupling is not guaranteed. Judicial councils dominated by the governing party, prosecutors who answer to the executive, and legal-aid systems with inadequate funding each raise one of the couplings, and each is a target of the indicators in \cref{sec:measurement}.
   505	
   506	\subsection{Summary}
   507	
   508	\Cref{tab:regimes} codes the six patterns qualitatively; its entries are not measurements.
   509	
   510	\begin{table}[p]
   511	\centering
   512	\small
   513	\caption{The judicial function across six regime types. Concentration and coupling are qualitative codings of the patterns described in the text, not numerical estimates.}
   514	\label{tab:regimes}
   515	\begin{tabularx}{\textwidth}{L{2.2cm}YYYY}
   516	\toprule
   517	Regime type & Principal holders of the judicial function & Concentration and contestability & Strongest coupling to other pillars & Documented check or capture episode \\
   518	\midrule
   519	Market-capitalist societies & Appointed and elected judges, a large private bar, administrative tribunals and private arbitration & Low concentration in ordinary cases and high concentration at the constitutional apex, with access as the weakest link & Resources to adjudication through repeat players, funded litigation and judicial campaign finance & The recusal ruling in \emph{Caperton} checked a capture risk created by campaign spending \\
   520	\addlinespace
   521	Communist party-states & Courts, the procuracy, party bodies supervising legal work, and a state-disciplined bar & Low concentration in ordinary cases and high concentration in politically salient cases, with low ruler-boundness & Rule-making to adjudication through party appointment, and coercion through the procuracy & Stalin-era courts followed campaign directives, while later reform raised legality in ordinary cases \\
   522	\addlinespace
   523	Social democracy and democratic socialism & Ordinary and administrative courts, labor courts, ombudsmen and parliamentary review committees & Low concentration, high disclosure and compliance, and restrained constitutional review in Nordic systems & Production to adjudication through labor courts with members nominated by labor-market organizations & The \emph{Langborger} ruling held that interested nominating bodies can defeat impartiality \\
   524	\addlinespace
   525	Islamic states & Qadis and muftis historically, and in modern states codified courts, royal or clerical councils and administrative courts & Moderate concentration in classical practice and high concentration at the apex in modern Iran and Saudi Arabia & Legitimation to adjudication through the ulama, and rule-making through royal or clerical appointment & Iran's Guardian Council screens legislation and candidates, while plural schools and independent muftis supplied historical checks \\
   526	\addlinespace
   527	Historical Catholic monarchies & Royal courts, parlements and chanceries, church courts, the Inquisition and papal tribunals & Moderate concentration with contestability supplied by competition among jurisdictions & Legitimation to adjudication through church courts and the Inquisition, and resources through venal offices & Maupeou's suppression of the parlements in 1771 was reversed in 1774 \\
   528	\addlinespace
   529	Secular democracies & Constitutional and supreme courts, ordinary and administrative courts, judicial councils and international courts & Low concentration in ordinary cases and high concentration at the constitutional apex, with compliance resting on public support & Rule-making to adjudication through appointment and through review that acts as co-legislation & The enlargement of the Argentine Supreme Court in 1990 produced a court aligned with the government \\
   530	\bottomrule
   531	\end{tabularx}
   532	\end{table}
   533	
   534	Every regime type has the judicial function, as \cref{thm:judicial-power:necessity} requires. The types differ little in the concentration of ordinary adjudication, which is low almost everywhere. They differ in the concentration of politically salient adjudication and in the pillar to which interpretation is most tightly coupled: resources in market capitalism, rule-making and coercion in the party-state, production in corporatist social democracy, legitimation in religious states and Catholic monarchies, and rule-making through appointment in secular democracies. Each type also contains both documented capture episodes and documented checks. Capture varies within regime types, as Proposition B's contingency predicts, rather than marking the boundary between them.
   535	
   536	\section{Mechanisms, failure modes and checks}
   537	\label{sec:mechanisms}
   538	
   539	\subsection{Judicial capture}
   540	
   541	\Cref{def:judicial-power:capture} separates three things that public debate often merges. A judge appointed by a party is not thereby captured, because appointment is the ordinary channel through which every regime staffs its courts. A ruling that favors a powerful litigant is not thereby captured, because the powerful litigant may have had the better case. Capture requires a privilege, a weakened check and an outcome linked to the privilege. \emph{Caperton} establishes the first two conditions for one case and leaves the third unresolved. Stalin-era criminal justice establishes all three for a whole system.
   542	
   543	\subsection{Failure modes}
   544	
   545	Interpretation fails as a check in four ways, one for each link of the review chain, and the formal results of \cref{sec:layer,sec:literature} identify the conditions under which each failure occurs. Disclosure fails when proceedings are sealed, reasons go unpublished or financial ties between litigants and judges stay hidden; the chain then never starts. Access fails when one side can outspend the other, and \cref{prop:judicial-power:repeat} shows that repeat players win more often for that reason even when merits are equal. Independence fails when the incumbent expects to stay in power, and \cref{prop:judicial-power:insurance} shows that such an incumbent gains nothing from granting it. Compliance fails when the governing coalition ignores adverse rulings, and \cref{prop:judicial-power:chain} shows that no strength elsewhere in the chain repairs that failure. A regime can also confine all four failures to the politically salient tier, where caseload statistics do not see them (\cref{prop:judicial-power:dualstate}).
   546	
   547	Each failure has a characteristic check. Publication duties and recusal rules protect disclosure. Legal aid, collective litigation and limits on forced arbitration protect access. Tenure security, insulated appointment and a plurality of forums protect independence. Public support that makes defiance costly, the mechanism Vanberg identified \citep{vanberg2005}, and enforcement agencies that answer to courts rather than to the beneficiary protect compliance. \Cref{sec:comparative} documents checks of each kind in every regime type, which is why capture there appears as a variable rather than a constant.
   548	
   549	\subsection{Coupling pathways and checks}
   550	
   551	The legitimation pathway runs through the body that produces authoritative readings of the law and the beliefs that support them. When the same coalition trains the jurists, licenses the lawyers, appoints the judges and controls the doctrine that justifies the regime, $C_{\pJ\pI}$ is high. The ulama in classical Islamic societies, the canonists and inquisitors of Catholic Europe, and the party's legal theorists in socialist states each occupied this position in different degrees. High $C_{\pJ\pI}$ is not capture. It becomes capture when interpretive dissent loses its institutional footing, so that no independent jurist, school or faculty can contest the authoritative reading. The historical check was plurality: of schools in Islamic law, of jurisdictions in Catholic Europe, of faculties and bar associations in modern democracies.
   552	
   553	The coercion pathway runs through the organs that bring cases and enforce judgments. When the same organ prosecutes, supervises legality and directs judges, as the Soviet procuracy and party legal organs could, $C_{\pJ\pC}$ is high and the judicial pillar loses the ability to restrain coercion. The check is separation of prosecution from adjudication and of both from the police, with judicial control over detention. The sanctioning apparatus belongs to Part V, which shows that sanctions can deter rule violations equally well whether or not they also fall more heavily on a coalition's opponents \citep{long2026coercive}. Independent adjudication is the check that ties sanctions to conduct rather than allegiance, and by \cref{prop:judicial-power:disjunctive} a judiciary with strong public legitimacy needs less coercive backing to do so.
   554	
   555	The production pathway runs through access. When workers, tenants and consumers cannot afford to litigate while employers, landlords and lenders litigate routinely, courts apply rules that the organized side has shaped. Beyond the access checks listed above, the Swedish Labour Court shows that corporatist representation of producers inside the court is a second kind of check, and the \emph{Langborger} line of cases shows its limit \citep{langborger1989,stallarholmens1990}.
   556	

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '360,480p' papers/latex/judicial-power.tex | nl -ba -v 360" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   360	\]
   361	The incumbent's expected payoff is maximized at $\iota^{*}=1$ if $\pi>\pi^{*}$, at $\iota^{*}=0$ if $\pi<\pi^{*}$, and by every $\iota\in[0,1]$ if $\pi=\pi^{*}$. The threshold $\pi^{*}$ decreases in $L$ and $\delta$ and increases in $g$. If $g\ge\delta L$, then $\pi^{*}\ge 1$ and independence is never strictly optimal.
   362	\end{proposition}
   363	
   364	\begin{proof}
   365	The incumbent's payoff is
   366	\[
   367	\Phi(\iota)=(1-\iota)g+\delta\big[(1-\pi)(1-\iota)g-\pi(1-\iota)L\big]=(1-\iota)\big[g(1+\delta)-\delta\pi(g+L)\big].
   368	\]
   369	$\Phi$ is linear in $\iota$ with slope $-\big[g(1+\delta)-\delta\pi(g+L)\big]$, which is positive when $\pi>\pi^{*}$, negative when $\pi<\pi^{*}$ and zero when $\pi=\pi^{*}$. The comparative statics follow from differentiating $\pi^{*}$: $\partial\pi^{*}/\partial L=-g(1+\delta)/[\delta(g+L)^2]<0$, $\partial\pi^{*}/\partial\delta=-g/[\delta^{2}(g+L)]<0$, and $\partial\pi^{*}/\partial g=(1+\delta)L/[\delta(g+L)^2]>0$. Finally, $\pi^{*}\ge 1$ if and only if $g(1+\delta)\ge\delta(g+L)$, which simplifies to $g\ge\delta L$.
   370	\end{proof}
   371	
   372	The model's assumptions do the work, and they should be stated plainly. Independence chosen today must persist, which requires that institutional change be costly; Landes and Posner's account relies on the same stickiness \citep{landes1975}. The court must bind whoever holds office, which excludes a court that binds only the opposition. The model is linear, which produces an all-or-nothing choice; a convex cost of independence would produce interior solutions with the same comparative statics. In the vocabulary of \cref{sec:layer}, $\iota$ is the independence component $q^{\mathrm{ind}}_t$, and when the incumbent appoints the judges through the appointment channel, keeping $\iota$ low is the same as keeping $C_{\pP\pJ}$ high.
   373	
   374	The result says that independence is more likely where the incumbent expects to lose power, where abuse by the other side would be costly, and where the incumbent is patient. It fits the variation across party-states and secular democracies described in \cref{sec:comparative}: a ruling party with a low $\pi$ has little reason to grant independence, and a fragmented democracy with a high $\pi$ has strong reason. Ramseyer used the same logic to explain why Japanese courts were less independent than American ones during a long period of single-party dominance \citep{ramseyer1994}.
   375	
   376	\begin{remark}[Strategic defection]
   377	Helmke's account of Argentine judges adds a judge-side version of the same logic \citep{helmke2005}. Assume that a judge without secure tenure is sanctioned, with loss $s>0$, only by whichever side holds power after the ruling takes effect and only if the ruling went against that side; that the case sets the incumbent against the side that would replace it; and that the merits are balanced. Ruling against the incumbent then risks $(1-\pi)s$, and ruling for it risks $\pi s$, so the judge rules against the incumbent when $\pi>1/2$. De facto independence from the incumbent rises as the incumbent's hold weakens, even when de jure independence is unchanged. The Argentine court that had favored the Menem government began to rule against it as its hold weakened, which fits this prediction.
   378	\end{remark}
   379	
   380	\subsection{Repeat players and legal aid}
   381	
   382	Galanter's argument about repeat players can be stated as a contest. A repeat player litigates many similar cases and values a favorable ruling both for the case at hand and for the precedent it sets. A one-shotter values only the case at hand.
   383	
   384	\begin{proposition}[Repeat-player contest]
   385	\label{prop:judicial-power:repeat}
   386	A repeat player $R$ and a one-shotter $O$ contest a case by spending $e_R,e_O\ge 0$, and $R$ wins with probability $p_R=me_R/(me_R+e_O)$, where $m>0$ is the relative merit of $R$'s position. $O$ values winning at $v>0$. $R$ litigates $n\ge 1$ similar cases, and a favorable ruling is worth $v$ in the present case plus $\theta v$ in each of the $n-1$ future cases through precedent, with $\theta\in[0,1]$. In the unique equilibrium with positive spending,
   387	\[
   388	p_R=\frac{m(1+\theta(n-1))}{m(1+\theta(n-1))+1}.
   389	\]
   390	With equal merits ($m=1$), $p_R>1/2$ if and only if $\theta(n-1)>0$. The probability $p_R$ is nondecreasing in $n$ and $\theta$, strictly increasing in $n$ when $\theta>0$, and strictly increasing in $\theta$ when $n>1$. If legal aid reimburses a fraction $\lambda\in[0,1)$ of $O$'s spending, the equilibrium becomes
   391	\[
   392	p_R=\frac{m(1+\theta(n-1))(1-\lambda)}{m(1+\theta(n-1))(1-\lambda)+1},
   393	\]
   394	and with equal merits the advantage is eliminated exactly when $\lambda=\theta(n-1)/(1+\theta(n-1))$.
   395	\end{proposition}
   396	
   397	\begin{proof}
   398	Let $v_R=v(1+\theta(n-1))$. Consider first a lottery contest in which players $1$ and $2$ value the prize at $A>0$ and $B>0$, choose efforts $x_1,x_2\ge 0$ at unit cost, and player $1$ wins with probability $x_1/(x_1+x_2)$. Player $1$ maximizes $Ax_1/(x_1+x_2)-x_1$ and player $2$ maximizes $Bx_2/(x_1+x_2)-x_2$. Each objective is strictly concave in the player's own effort when the other's effort is positive, and the first-order conditions are
   399	\[
   400	\frac{A\,x_2}{(x_1+x_2)^2}=1,\qquad \frac{B\,x_1}{(x_1+x_2)^2}=1 .
   401	\]
   402	Dividing gives $x_1/x_2=A/B$, so player $1$ wins with probability $A/(A+B)$, and substituting back gives the unique positive solution $x_1=A^2B/(A+B)^2$, $x_2=AB^2/(A+B)^2$.
   403	
   404	In the litigation contest, write $x_1=me_R$ and $x_2=e_O$. Then $R$'s payoff is $v_Rx_1/(x_1+x_2)-x_1/m$, which is $1/m$ times $mv_Rx_1/(x_1+x_2)-x_1$, so $R$ behaves as player $1$ with $A=mv_R$, and $O$ behaves as player $2$ with $B=v$. Hence $p_R=mv_R/(mv_R+v)$, which is the first expression. With reimbursement at rate $\lambda$, $O$'s payoff is $vx_2/(x_1+x_2)-(1-\lambda)x_2$, which is $(1-\lambda)$ times the payoff of a player with valuation $B=v/(1-\lambda)$ and unit cost; substituting gives the second expression. With $m=1$ the second expression equals $1/2$ exactly when $(1+\theta(n-1))(1-\lambda)=1$, which gives the stated $\lambda$. Finally, $p_R$ is strictly increasing in $1+\theta(n-1)$, which is nondecreasing in $n$ and $\theta$, strictly increasing in $n$ when $\theta>0$, and strictly increasing in $\theta$ when $n>1$.
   405	\end{proof}
   406	
   407	Repeat litigants win more often than one-shot litigants with equally good cases whenever rulings set precedent, because a repeat litigant bids for future cases as well as the case at hand. Legal aid removes the advantage only when the subsidy to the one-shotter matches the share of the repeat litigant's stake that comes from future cases, $\lambda=\theta(n-1)/[1+\theta(n-1)]$. Since that share rises with the repeat litigant's caseload and with the precedential weight of rulings, modest legal-aid budgets leave repeat players ahead in forums whose rulings bind later cases. \citet{galanter1974} identifies further advantages, including expertise, economies of scale and informal relations with court personnel, which add to the precedent effect modeled here and raise the subsidy needed to equalize access.
   408	
   409	The model gives one reason why resource shares buy favorable rulings, a relation Part I measures for every pillar \citep{long2026financial}, and it locates the remedy in the access component $q^{\mathrm{acc}}_t$. It is also the core of the coupling $C_{\pJ\pW}$. Workers, tenants and consumers are usually one-shotters facing repeat players, so access to courts determines whether producers can contest the rules that govern their work, which is the judicial form of the source's hypothesis about worker voice \citep{largo2026hbs}.
   410	
   411	\section{Comparative analysis across six regime types}
   412	\label{sec:comparative}
   413	
   414	\subsection{Coding conventions}
   415	
   416	Qualitative coding is the only defensible form of comparison at present, because no preregistered coding of $H$, $Q$, $U_t$ or $\Integ_t$ exists for any real polity, and the series does not report numbers without one \citep{largo2026hbs}. Each regime type is therefore compared on five questions: which institutions hold the judicial function; how concentrated control over final determinations is ($H_{\pJ,t}$) and how contestable it is ($\mathbf{q}_t$); how strongly the judicial function is coupled to the other five pillars; what preserves accountability; and which capture episodes and checks are documented.
   417	
   418	The six types are ideal types, and real polities mix them. The United States is both a market-capitalist society and a secular democracy; Sweden is both a social democracy and a secular democracy. The comparison assigns each case to the type whose distinctive pathway it best illustrates. The market-capitalist section concentrates on the channel from private resources to courts, and the secular-democracy section on the design of the relation between courts and elected bodies.
   419	
   420	\subsection{Market-capitalist societies}
   421	
   422	In market-capitalist societies the judicial function is held by courts of general jurisdiction staffed by appointed or elected judges, by a large private legal profession, by administrative tribunals and by private arbitration. The United States is the principal illustration. Federal judges are nominated by the President and confirmed by the Senate, many state judges are elected, and since \citet{marbury1803} courts have reviewed the constitutionality of statutes. Hamilton's defense of life tenure in \emph{Federalist} No.~78 rests on the claim that ``the interpretation of the laws is the proper and peculiar province of the courts'' \citep{hamilton1788}.
   423	
   424	Concentration has two levels. Across ordinary litigation, control over final determinations is spread across thousands of judges, so $H_{\pJ,t}$ is low. For constitutional questions a single court holds the last word, and concentration at the apex is high. Disclosure is high, because opinions are published with reasons. Independence is protected by tenure and salary guarantees for federal judges and is weaker for elected state judges who must raise campaign funds. Compliance by government with adverse rulings is high, and Gibson and coauthors attribute part of it to diffuse public support \citep{gibson2003}. Access is the weakest link. Litigation is costly, and the advantage of organized repeat players is the core of Galanter's argument \citep{galanter1974}.
   425	
   426	The distinctive coupling runs from resources to adjudication, the pair $C_{\pF\pJ}$ that Part I treats \citep{long2026financial}. Three channels are documented. Repeat players who can invest in rule-shaping litigation obtain favorable precedents (\cref{prop:judicial-power:repeat}). Rights litigation depends on a support structure of funded organizations \citep{epp1998}. Campaign spending in judicial elections ties litigants to judges directly.
   427	
   428	Judicial doctrine also shapes the channel from resources to rule-making. In \citet{citizensunited2010} the Supreme Court held the federal ban on independent expenditures by corporations and unions unconstitutional. The ruling changed the rules governing the path from $\pF$ to $\pP$, so the judicial pillar acted as a gatekeeper between two others. It is coupling, not capture: the decision was reached through the ordinary procedure, and capture requires privileged access and a weakened check.
   429	
   430	The clearest documented episode of capture risk is \citet{caperton2009}. While Massey's appeal of a large jury verdict was pending, Massey's chairman spent about three million dollars supporting Brent Benjamin's 2004 campaign for the West Virginia Supreme Court of Appeals. Benjamin won, declined to recuse himself, and joined the majority that reversed the verdict. The United States Supreme Court held that ``in all the circumstances of this case, due process requires recusal.'' Under \cref{def:judicial-power:capture} the facts establish privileged access and a threat to independence, but the Court did not find actual bias; it found a serious risk of it. The episode documents a capture risk and a check that operated through appeal, which is the pattern \cref{prop:judicial-power:chain} predicts when the access and independence links of the review chain hold.
   431	
   432	Outside the resource channel, market-capitalist adjudication is loosely coupled to the other pillars, with one exception in production. The coupling with legitimation runs through law schools, the bar and the public reputation of courts, professional institutions that no single coalition commands. The coupling with coercion is moderate: prosecutors decide which disputes reach the courts, and the enforcement of judgments depends on executive agencies, as Hamilton observed \citep{hamilton1788}. The exception is the arbitration clause in employment and consumer contracts, which moves disputes from public courts to private forums whose awards set no public precedent. Firms that draft such clauses are repeat players in Galanter's sense \citep{galanter1974}, so the clauses raise $C_{\pJ\pW}$ on terms set by one side.
   433	
   434	\subsection{Communist party-states}
   435	
   436	In communist party-states the judicial function is held by courts, by the procuracy, by party bodies that oversee legal work, and by a bar organized under state discipline. Harold Berman's interpretation of Soviet law described a procuracy that combined criminal prosecution with general supervision of the legality of administrative acts \citep{berman1963}. That combination puts prosecution and legality review in one organ, so $C_{\pJ\pC}$ is high by design. Eugene Huskey's history of the Soviet bar traces how advocates were organized into collegia subject to state control between 1917 and 1939 \citep{huskey1986}. In the People's Republic of China, Lubman's study of legal reform after Mao describes courts that operate inside a structure of party supervision, with judicial decisions in sensitive cases subject to review by bodies outside the bench \citep{lubman1999}.
   437	
   438	Concentration depends on the type of case. For ordinary civil and commercial disputes, determinations are made by many courts with little party involvement, and concentration is low. For politically salient cases, the last word rests with party organs, and concentration at the level of the ruling coalition is high. This is the two-tier structure of \cref{def:judicial-power:boundness}. The appointment of judges and procurators through the party's personnel system makes $C_{\pP\pJ}$ high, a coupling Part II codes through its appointment channel. Disclosure is limited for political cases. Access has grown in some areas: Peerenboom documents administrative litigation in which citizens sue government agencies \citep{peerenboom2002}. Compliance by the ruling coalition with adverse determinations is low in the political tier, so ruler-boundness is low.
   439	
   440	Ginsburg and Moustafa's list of authoritarian court functions fits the party-state well: courts discipline lower officials, resolve commercial disputes and give legal form to repression \citep{ginsburg2008}. Peter Solomon's study of Soviet criminal justice under Stalin documents courts that operated under campaign directives and pressure from party and state bodies, so that the volume and severity of prosecution followed political priorities \citep{solomon1996}. That is the strongest documented case of judicial capture in the sense of \cref{def:judicial-power:capture}: privileged direction of determinations by the party, the elimination of independent review, and material evidence in the archival record linking directives to outcomes.
   441	
   442	The party-state also contains checks, and they are documented. Kathryn Hendley's study of labor law in the late Soviet period examines how far law mattered in employment relations as legal reform began \citep{hendley1996}. Peerenboom argues that Chinese reform produced a thin rule of law in which legal rules increasingly bind officials in ordinary matters \citep{peerenboom2002}. Minzner identifies a reversal after the mid-2000s, in which the party shifted emphasis from courts toward mediation, petitioning and the maintenance of stability, and retreated from legal professionalism \citep{minzner2011}. The trajectory shows that the coupling between rule-making and adjudication in a party-state is a variable that leaders adjust, not a fixed property of the regime. The insurance model of \cref{prop:judicial-power:insurance} predicts this: a ruling party that expects to stay in power gains little from independent courts.
   443	
   444	The party-state also couples adjudication to legitimation and production, because it treats law as an instrument of education and of economic administration. Berman described Soviet law as parental, in the sense that courts were charged with educating citizens in the values of the regime as well as deciding their disputes \citep{berman1963}, which raises $C_{\pJ\pI}$. The same legal order handled labor disputes and disputes between state enterprises, so that the enforcement of plan discipline passed through adjudicative bodies \citep{berman1963,hendley1996}, which raises $C_{\pJ\pW}$.
   445	
   446	\subsection{Social democracy and democratic socialism}
   447	
   448	In social democracies the judicial function is spread across ordinary courts, specialized administrative and labor courts, ombudsmen, and parliamentary bodies that review the constitutionality of legislation. The Nordic countries illustrate a model of restrained judicial review. Sweden's Instrument of Government directs that a court which finds that a provision conflicts with a rule of fundamental law shall not apply it \citep{swedenig}. A reform in 2010 removed an earlier requirement that the conflict be manifest before a court could set a statute aside \citep{jonssoncornell2016}.
   449	
   450	Finland's constitution assigns primary review of legislative proposals to Parliament's Constitutional Law Committee, and allows courts to give primacy to the Constitution only when applying an act would be in evident conflict with it \citep{finlandconst}. Constitutional interpretation is thus shared between a parliamentary committee and the courts, which raises $C_{\pP\pJ}$ by design. Tushnet's weak-form review describes this arrangement \citep{tushnet2008}.
   451	
   452	Germany shows a different social-market pattern. Its Federal Constitutional Court exercises strong-form review, and Vanberg's study shows that its ability to obtain compliance depends on public support and on the visibility of the government's response \citep{vanberg2005}. Stone Sweet's account of constitutional courts as co-legislators draws heavily on the German and French experience \citep{stonesweet2000}. The social-democratic family therefore contains both the weakest and some of the strongest forms of constitutional review among democracies.
   453	
   454	Concentration of ordinary adjudication is low. Disclosure is high, and the ombudsman adds a channel of review outside the courts. Sweden's Parliamentary Ombudsmen are elected by the Riksdag to supervise the application of laws in public activities \citep{swedenig}. Access is supported by legal aid and by the low cost of administrative appeals. Independence is protected by constitutional prohibitions on interference: the Instrument of Government provides that neither the Riksdag nor any public authority may determine how a court shall adjudicate an individual case \citep{swedenig}. Compliance by government is high.
   455	
   456	The distinctive coupling is $C_{\pJ\pW}$, through corporatist labor adjudication. The Swedish Labour Court sits with neutral members and with members representing employer and employee interests, most of whom are appointed on the nomination of the principal labor-market organizations, and its judgment is final \citep{arbetsdomstolen}. This design gives the organized parties of production a place inside the judicial function. It also creates a recognizable risk: a forum whose members are nominated by organizations may favor those organizations over outsiders. The European Court of Human Rights addressed that risk for a related Swedish tribunal in \citet{langborger1989}, finding a violation of the right to an independent and impartial tribunal when lay assessors in a housing and tenancy court were nominated by organizations whose interests ran against the applicant's. The European Commission of Human Rights later declined to find a violation in a Labour Court case in which the nominating organizations had no common interest opposed to the applicant's \citep{stallarholmens1990}. The two rulings mark the line between coupling and capture with some precision: organizational nomination is compatible with impartiality unless the nominators share an interest in the outcome.
   457	
   458	Bo Rothstein's study of Swedish social reform emphasizes that the implementation of universal programs depends on bureaucratic organization and on citizens' trust in impartial administration \citep{rothstein1996}. That is the legitimation coupling $C_{\pJ\pI}$ in its social-democratic form: the authority of courts and ombudsmen rests on a shared belief in impartial application. We found no documented case of systematic judicial capture by an economic coalition in the Nordic sources reviewed. The risks identified in the literature are of another kind: legislative supremacy weakens the counter-majoritarian check when a governing majority is durable, and corporatist adjudication can close the forum to actors outside the organized parties.
   459	
   460	\subsection{Islamic states}
   461	
   462	Islamic states derive political legitimacy from religious law, but the institutions that interpret it have varied widely across schools, dynasties and centuries. Hallaq describes the classical arrangement as a division of labor \citep{hallaq2009}. Rulers appointed qadis to decide cases. Jurists who were not state officials developed the law, and muftis issued nonbinding opinions, fatwas, that litigants and judges consulted \citep{masud1996}. Rulers also held a jurisdiction for the redress of grievances, the \emph{mazalim}, which al-Mawardi's eleventh-century treatise on government discusses alongside the qadi's office \citep{mawardi1996}. Hallaq's further claim that the jurists' independent authority confined rulers to administrative regulation is a contested thesis \citep{hallaq2009,hallaq2013}. Sami Zubaida emphasizes the long interplay of state power and religious law \citep{zubaida2003}, and Joseph Schacht's older synthesis, which presents the classical law as largely detached from practice, is read critically by later scholarship \citep{schacht1964}.
   463	
   464	Court records contradict the older image of Islamic adjudication as unpredictable. Max Weber used the term ``kadi justice'' for an ideal type of adjudication guided by substantive considerations of the individual case rather than by general rules \citep{weber1978}. Haim Gerber tested that characterization against Ottoman court records and rejected it for the courts he examined \citep{gerber1994}. Ronald Jennings's study of the seventeenth-century court of Kayseri shows regular procedure, extensive records and wide use by ordinary inhabitants \citep{jennings1978}.
   465	
   466	Ottoman law also shows a ruler's legislation reconciled with jurists' law through interpretation rather than by command. Colin Imber's study of Ebu's-su'ud, the Ottoman chief mufti in the mid-sixteenth century, shows sultanic law, the \emph{kanun}, brought into harmony with jurists' law through juristic opinion \citep{imber1997}. Brinkley Messick's study of Yemen traces how the transmission of authoritative texts structured judicial power in a different Muslim society \citep{messick1993}.
   467	
   468	Concentration in the classical and Ottoman pattern was moderate. Qadis were numerous and appointed by the ruler, which made $C_{\pP\pJ}$ substantial, but the law they applied was developed by a scholarly class with its own institutions of training, the madrasas that George Makdisi studied \citep{makdisi1981}. The same scholars taught, issued opinions and judged, so the legitimation coupling $C_{\pJ\pI}$ was high through the ulama. Plurality of schools and the availability of independent muftis supplied contestability: a litigant could seek an opinion from a jurist outside the court.
   469	
   470	Saudi Arabia couples uncodified juristic interpretation to royal appointment and royal enforcement. Its Basic Law of Governance declares the judiciary an independent authority subject to no authority other than the Islamic Shari'ah and requires courts to apply the Shari'ah as drawn from the Qur'an and the Sunna. The same law provides that judges are appointed and their service terminated by royal order on the proposal of the supreme judicial council, assigns the implementation of judgments to the King or his deputy, and declares the King the ultimate source of the state's authorities \citep{saudibasic}. Frank Vogel's study describes a judiciary that applies largely uncodified Islamic law through judges' own interpretation, alongside royal regulations and the Board of Grievances as an administrative jurisdiction \citep{vogel2000}, and Nathan Brown's comparison of courts in Egypt and the Gulf places the Saudi system within a regional range of arrangements \citep{brown1997}. In this design $C_{\pP\pJ}$ runs through royal appointment, and $C_{\pJ\pC}$ through royal enforcement of judgments.
   471	
   472	Iran's constitution builds judicial review into rule-making by assigning the interpretation of all legislation to a council of jurists. The jurists of the Guardian Council decide whether all laws and regulations conform to Islamic criteria \citep{iranconst}. The Council has twelve members: six jurists in Islamic law selected by the Leader, and six jurists elected by the parliament from among nominees of the head of the judiciary. Every bill passed by parliament goes to the Council, which must review it within ten days. Islamic compatibility is decided by a majority of the six religious jurists, constitutional compatibility by a majority of all members. The Council also supervises elections. Hirschl treats Iran as a leading case of constitutional theocracy, in which religious interpretation is constitutionalized and assigned to a council \citep{hirschl2010}.
   473	
   474	The ordinary judiciary is tied to the same apex. The Leader appoints the head of the judiciary for five years. The constitution also provides that judges cannot be removed except after trial and proof of guilt, and that citizens may seek annulment of unlawful regulations in the Court of Administrative Justice \citep{iranconst}.
   475	
   476	The Iranian design concentrates interpretation at the apex and couples it to rule-making and legitimation. The Leader's appointments reach both the Guardian Council and the judiciary, and the Council's religious jurists decide whether legislation is valid. Asghar Schirazi documents repeated conflict between parliament and the Guardian Council in the 1980s, which led to the creation of the Expediency Council to resolve deadlocks between them \citep{schirazi1997}. Wilfried Buchta describes the Council's use of its electoral supervision to screen candidates \citep{buchta2000}. The vetting of bills and the screening of candidates are rule-making acts, a veto over legislation and over entry, and Part II codes them that way \citep{long2026political}. The judgments on which they rest, whether a bill conforms to Islamic criteria and to the Constitution, are interpretive determinations. One body performing both kinds of act is fusion, with high $C_{\pP\pJ}$.
   477	
   478	Fusion is not yet capture. A capture finding under \cref{def:judicial-power:capture} would require evidence that particular screening decisions followed privileged access and had material effect, and no such coding is attempted here. The system also contains checks: senior clerical authorities outside the state, whose plurality Muhammad Qasim Zaman documents across Muslim societies \citep{zaman2002}, and the constitutional provisions on judicial tenure and administrative review.
   479	
   480	\subsection{Catholic monarchies in early modern Europe}

codex
I’ve completed the full-file read. I’m now cross-checking every citation/reference target and the document structure from that same file; I’ll distinguish definite LaTeX defects from layout risks that cannot be confirmed without compiling.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "perl -ne 'while (/\\\\(?:citep|citet)\\{(["'^}]*)'"\\}/g) { for (split /,/, "'$1) { s/''^'"\\s+|\\s+"'$//g; print "CITE'"\\t"'$_'"\\t"'$.'"\\n\" } } while (/\\\\(?:[Cc]ref)\\{(["'^}]*)'"\\}/g) { for (split /,/, "'$1) { s/''^'"\\s+|\\s+"'$//g; print "REF'"\\t"'$_'"\\t"'$.'"\\n\" } } while (/\\\\bibitem(?:\\[["'^]]*'"\\])?\\{(["'^}]*)'"\\}/g) { print \"BIB\\t"'$1'"\\t"'$.'"\\n\" } while (/\\\\label\\{(["'^}]*)'"\\}/g) { print \"LABEL\\t"'$1'"\\t"'$.'"\\n\" }' papers/latex/judicial-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
CITE	long2026financial	66
CITE	long2026political	66
CITE	long2026ideological	66
CITE	long2026coercive	66
CITE	long2026productive	66
CITE	long2026formalized	66
CITE	largo2026hbs	66
REF	thm:judicial-power:necessity	70
REF	prop:judicial-power:chain	70
CITE	largo2026hbs	72
LABEL	sec:layer	75
CITE	largo2026hbs	79
CITE	largo2026hbs	81
CITE	hart1961	85
CITE	long2026political	85
CITE	long2026ideological	85
LABEL	def:judicial-power:open-texture	90
CITE	hart1961	98
LABEL	def:judicial-power:dispute	103
LABEL	def:judicial-power:determination	112
CITE	shapiro1981	116
CITE	largo2026hbs	122
LABEL	def:judicial-power:qj	125
CITE	long2026political	126
REF	prop:judicial-power:chain	132
LABEL	lem:judicial-power:ordering	135
LABEL	def:judicial-power:boundness	146
CITE	tamanaha2004	150
CITE	peerenboom2002	150
CITE	hendley2017	150
LABEL	def:judicial-power:capture	153
CITE	largo2026hbs	154
CITE	largo2026hbs	159
LABEL	prop:judicial-power:chain	162
REF	def:judicial-power:qj	163
REF	sec:comparative	174
LABEL	prop:judicial-power:dualstate	181
REF	sec:measurement	189
LABEL	sec:necessity	192
LABEL	ass:arrival	199
LABEL	ass:cost	204
REF	ass:arrival	208
REF	ass:cost	208
LABEL	thm:judicial-power:necessity	211
REF	ass:arrival	212
REF	ass:cost	212
REF	ass:cost	216
REF	ass:arrival	216
REF	def:judicial-power:determination	216
REF	tab:minimal	227
LABEL	tab:minimal	233
CITE	evanspritchard1940	248
REF	def:judicial-power:determination	248
REF	subsec:dependencies	248
CITE	gluckman1955	250
CITE	gulliver1963	250
REF	def:judicial-power:dispute	250
CITE	lee2013	252
CITE	wiessner2005	252
CITE	boehm1999	252
CITE	woodburn1982	252
CITE	ostrom1990	254
CITE	cox2010	254
REF	thm:judicial-power:necessity	258
LABEL	prop:judicial-power:exit	261
REF	ass:arrival	262
CITE	woodburn1982	269
CITE	lee2013	269
CITE	lee2013	269
CITE	wiessner2005	269
LABEL	prop:judicial-power:relocation	274
REF	def:judicial-power:open-texture	279
REF	def:judicial-power:determination	281
REF	thm:judicial-power:necessity	282
REF	def:judicial-power:open-texture	288
REF	def:judicial-power:dispute	288
REF	thm:judicial-power:necessity	288
CITE	evanspritchard1940	293
REF	ass:cost	293
LABEL	subsec:dependencies	296
CITE	hamilton1788	298
LABEL	prop:judicial-power:disjunctive	301
CITE	long2026ideological	309
CITE	long2026coercive	309
CITE	gibson2003	309
REF	prop:judicial-power:disjunctive	309
CITE	long2026formalized	311
CITE	hempel1959	317
CITE	elster1983	317
CITE	merton1968	317
REF	thm:judicial-power:necessity	317
REF	tab:minimal	317
LABEL	cor:judicial-power:nonimplication	322
REF	thm:judicial-power:necessity	323
REF	ass:arrival	327
REF	ass:cost	327
REF	prop:judicial-power:chain	330
LABEL	sec:literature	333
REF	sec:comparative	337
CITE	landes1975	339
CITE	ramseyer1994	339
CITE	stephenson2003	339
CITE	whittington2005	339
CITE	hirschl2001	339
CITE	hirschl2004	339
CITE	ginsburg2008	341
CITE	moustafa2007	341
CITE	helmke2005	341
CITE	vanberg2005	343
CITE	gibson2003	343
CITE	stonesweet2000	343
CITE	tushnet2008	343
CITE	galanter1974	345
CITE	epp1998	345
CITE	bonica2017	345
CITE	hallaq2005	347
CITE	hallaq2009	347
CITE	berman1983	347
CITE	kagan1981	347
CITE	bell1994	347
CITE	fosi2011	347
CITE	berman1963	347
CITE	lubman1999	347
CITE	minzner2011	347
CITE	landes1975	353
CITE	ramseyer1994	353
CITE	stephenson2003	353
LABEL	prop:judicial-power:insurance	356
CITE	landes1975	372
REF	sec:layer	372
CITE	ramseyer1994	374
REF	sec:comparative	374
CITE	helmke2005	377
LABEL	prop:judicial-power:repeat	385
CITE	galanter1974	407
CITE	long2026financial	409
CITE	largo2026hbs	409
LABEL	sec:comparative	412
CITE	largo2026hbs	416
CITE	marbury1803	422
CITE	hamilton1788	422
CITE	gibson2003	424
CITE	galanter1974	424
CITE	long2026financial	426
CITE	epp1998	426
REF	prop:judicial-power:repeat	426
CITE	citizensunited2010	428
CITE	caperton2009	430
REF	def:judicial-power:capture	430
REF	prop:judicial-power:chain	430
CITE	hamilton1788	432
CITE	galanter1974	432
CITE	berman1963	436
CITE	huskey1986	436
CITE	lubman1999	436
CITE	peerenboom2002	438
REF	def:judicial-power:boundness	438
CITE	ginsburg2008	440
CITE	solomon1996	440
REF	def:judicial-power:capture	440
CITE	hendley1996	442
CITE	peerenboom2002	442
CITE	minzner2011	442
REF	prop:judicial-power:insurance	442
CITE	berman1963	444
CITE	berman1963	444
CITE	hendley1996	444
CITE	swedenig	448
CITE	jonssoncornell2016	448
CITE	finlandconst	450
CITE	tushnet2008	450
CITE	vanberg2005	452
CITE	stonesweet2000	452
CITE	swedenig	454
CITE	swedenig	454
CITE	arbetsdomstolen	456
CITE	langborger1989	456
CITE	stallarholmens1990	456
CITE	rothstein1996	458
CITE	hallaq2009	462
CITE	masud1996	462
CITE	mawardi1996	462
CITE	hallaq2009	462
CITE	hallaq2013	462
CITE	zubaida2003	462
CITE	schacht1964	462
CITE	weber1978	464
CITE	gerber1994	464
CITE	jennings1978	464
CITE	imber1997	466
CITE	messick1993	466
CITE	makdisi1981	468
CITE	saudibasic	470
CITE	vogel2000	470
CITE	brown1997	470
CITE	iranconst	472
CITE	hirschl2010	472
CITE	iranconst	474
CITE	schirazi1997	476
CITE	buchta2000	476
CITE	long2026political	476
CITE	zaman2002	478
REF	def:judicial-power:capture	478
CITE	berman1983	482
CITE	brundage1995	482
CITE	helmholz1996	482
CITE	kagan1981	484
CITE	kamen1997	484
CITE	henningsen1986	484
CITE	given1997	484
CITE	kamen1997	484
CITE	elliott1963	486
CITE	doyle1996	488
CITE	swann1995	488
CITE	long2026political	488
CITE	vankley1996	490
CITE	doyle1996	490
CITE	bell1994	490
CITE	prodi1987	492
CITE	fosi2011	492
CITE	stonesweet2000	496
CITE	hirschl2001	496
CITE	hirschl2004	496
CITE	laporta2004	498
CITE	feld2003	498
CITE	vanberg2005	500
CITE	whittington2005	500
CITE	levitsky2010	502
CITE	hevia2008	502
CITE	helmke2005	502
REF	sec:measurement	504
REF	tab:regimes	508
LABEL	tab:regimes	514
REF	thm:judicial-power:necessity	534
LABEL	sec:mechanisms	537
REF	def:judicial-power:capture	541
REF	sec:layer	545
REF	sec:literature	545
REF	prop:judicial-power:repeat	545
REF	prop:judicial-power:insurance	545
REF	prop:judicial-power:chain	545
REF	prop:judicial-power:dualstate	545
CITE	vanberg2005	547
REF	sec:comparative	547
CITE	long2026coercive	553
REF	prop:judicial-power:disjunctive	553
CITE	langborger1989	555
CITE	stallarholmens1990	555
LABEL	sec:measurement	558
CITE	largo2026hbs	562
CITE	feld2003	562
REF	tab:indicators	562
LABEL	tab:indicators	568
CITE	coppedge2011	581
CITE	kaufmann2011	581
CITE	laporta2004	581
CITE	feld2003	581
CITE	jennings1978	583
CITE	swann1995	583
CITE	henningsen1986	583
CITE	fosi2011	583
CITE	largo2026hbs	585
REF	prop:judicial-power:insurance	592
CITE	hirschl2004	593
REF	prop:judicial-power:dualstate	594
REF	prop:judicial-power:repeat	595
CITE	hallaq2009	596
CITE	doyle1996	597
CITE	helmke2005	598
REF	prop:judicial-power:chain	599
LABEL	sec:revelation	605
CITE	fuller1995	607
CITE	mcginn1994	607
CITE	kjv	609
REF	prop:judicial-power:chain	609
CITE	kjv	611
CITE	bauckham1993	613
CITE	collins1984	613
CITE	koester2014	613
CITE	kraybill1996	613
CITE	schussler1985	613
REF	sec:measurement	615
LABEL	sec:objections	618
REF	prop:judicial-power:exit	620
REF	ass:cost	620
CITE	shapiro1981	622
CITE	weber1978	624
CITE	gerber1994	624
BIB	arbetsdomstolen	637
BIB	bauckham1993	640
BIB	bell1994	643
BIB	berman1963	646
BIB	berman1983	649
BIB	boehm1999	652
BIB	bonica2017	655
BIB	brown1997	658
BIB	brundage1995	661
BIB	buchta2000	664
BIB	caperton2009	667
BIB	citizensunited2010	670
BIB	collins1984	673
BIB	coppedge2011	676
BIB	cox2010	679
BIB	doyle1996	682
BIB	elliott1963	685
BIB	elster1983	688
BIB	epp1998	691
BIB	evanspritchard1940	694
BIB	feld2003	697
BIB	finlandconst	700
BIB	fosi2011	703
BIB	fuller1995	706
BIB	galanter1974	709
BIB	gerber1994	712
BIB	gibson2003	715
BIB	ginsburg2008	718
BIB	given1997	721
BIB	gluckman1955	724
BIB	gulliver1963	727
BIB	hallaq2005	730
BIB	hallaq2009	733
BIB	hallaq2013	736
BIB	hamilton1788	739
BIB	hart1961	742
BIB	helmholz1996	745
BIB	helmke2005	748
BIB	hempel1959	751
BIB	hendley1996	754
BIB	hendley2017	757
BIB	henningsen1986	760
BIB	hevia2008	763
BIB	hirschl2001	766
BIB	hirschl2004	769
BIB	hirschl2010	772
BIB	huskey1986	775
BIB	imber1997	778
BIB	iranconst	781
BIB	jennings1978	784
BIB	jonssoncornell2016	787
BIB	kagan1981	790
BIB	kamen1997	793
BIB	kaufmann2011	796
BIB	kjv	799
BIB	koester2014	802
BIB	kraybill1996	805
BIB	laporta2004	808
BIB	landes1975	811
BIB	langborger1989	814
BIB	largo2026hbs	817
BIB	lee2013	820
BIB	levitsky2010	823
BIB	long2026coercive	826
BIB	long2026financial	829
BIB	long2026formalized	832
BIB	long2026ideological	835
BIB	long2026political	838
BIB	long2026productive	841
BIB	lubman1999	844
BIB	makdisi1981	847
BIB	marbury1803	850
BIB	masud1996	853
BIB	mawardi1996	856
BIB	mcginn1994	859
BIB	merton1968	862
BIB	messick1993	865
BIB	minzner2011	868
BIB	moustafa2007	871
BIB	ostrom1990	874
BIB	peerenboom2002	877
BIB	prodi1987	880
BIB	ramseyer1994	883
BIB	rothstein1996	886
BIB	saudibasic	889
BIB	schacht1964	892
BIB	schirazi1997	895
BIB	schussler1985	898
BIB	shapiro1981	901
BIB	solomon1996	904
BIB	stallarholmens1990	907
BIB	stephenson2003	910
BIB	stonesweet2000	913
BIB	swann1995	916
BIB	swedenig	919
BIB	tamanaha2004	922
BIB	tushnet2008	925
BIB	vankley1996	928
BIB	vanberg2005	931
BIB	vogel2000	934
BIB	weber1978	937
BIB	whittington2005	940
BIB	wiessner2005	943
BIB	woodburn1982	946
BIB	zaman2002	949
BIB	zubaida2003	952

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "rg -n '[0-9]-[0-9]' papers/latex/judicial-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
656:Bonica, Adam, and Maya Sen. 2017. ``A Common-Space Scaling of the American Judiciary and Legal Profession.'' \emph{Political Analysis} 25(1): 114-121. doi:10.1017/pan.2016.10.
668:\emph{Caperton v.\ A.\,T.\ Massey Coal Co.}, 556 U.S. 868 (2009). Supreme Court of the United States, No.~08-22, decided 8 June 2009. \url{https://www.law.cornell.edu/supremecourt/text/08-22}.
671:\emph{Citizens United v.\ Federal Election Commission}, 558 U.S. 310 (2010). Supreme Court of the United States, No.~08-205, decided 21 January 2010. \url{https://www.law.cornell.edu/supremecourt/text/08-205}.
677:Coppedge, Michael, John Gerring, David Altman, Michael Bernhard, Steven Fish, Allen Hicken, Matthew Kroenig, Staffan I. Lindberg, Kelly McMann, Pamela Paxton, Holli A. Semetko, Svend-Erik Skaaning, Jeffrey Staton, and Jan Teorell. 2011. ``Conceptualizing and Measuring Democracy: A New Approach.'' \emph{Perspectives on Politics} 9(2): 247-267. doi:10.1017/S1537592711000880.
680:Cox, Michael, Gwen Arnold, and Sergio Villamayor Tomas. 2010. ``A Review of Design Principles for Community-based Natural Resource Management.'' \emph{Ecology and Society} 15(4): 38. doi:10.5751/ES-03704-150438.
686:Elliott, J.\,H. 1963. \emph{Imperial Spain 1469-1716}. London: Edward Arnold.
698:Feld, Lars P., and Stefan Voigt. 2003. ``Economic Growth and Judicial Independence: Cross-Country Evidence Using a New Set of Indicators.'' \emph{European Journal of Political Economy} 19(3): 497-527. doi:10.1016/s0176-2680(03)00017-x.
704:Fosi, Irene. 2011. \emph{Papal Justice: Subjects and Courts in the Papal State, 1500-1750}. Washington, DC: Catholic University of America Press. doi:10.2307/j.ctt2852kt.
710:Galanter, Marc. 1974. ``Why the `Haves' Come Out Ahead: Speculations on the Limits of Legal Change.'' \emph{Law \& Society Review} 9(1): 95-160. doi:10.2307/3053023.
716:Gibson, James L., Gregory A. Caldeira, and Lester Kenyatta Spence. 2003. ``The Supreme Court and the US Presidential Election of 2000: Wounds, Self-Inflicted or Otherwise?'' \emph{British Journal of Political Science} 33(4): 535-556. doi:10.1017/S0007123403000243.
752:Hempel, Carl G. 1959. ``The Logic of Functional Analysis.'' In \emph{Symposium on Sociological Theory}, edited by Llewellyn Gross, 271-307. New York: Harper and Row.
767:Hirschl, Ran. 2001. ``The Political Origins of Judicial Empowerment through Constitutionalization: Lessons from Israel's Constitutional Revolution.'' \emph{Comparative Politics} 33(3): 315-335. doi:10.2307/422406.
776:Huskey, Eugene. 1986. \emph{Russian Lawyers and the Soviet State: The Origins and Development of the Soviet Bar, 1917-1939}. Princeton: Princeton University Press. doi:10.1515/9781400854516.
785:Jennings, Ronald C. 1978. ``Kadi, Court, and Legal Procedure in 17th C. Ottoman Kayseri.'' \emph{Studia Islamica} 48: 133-172. doi:10.2307/1595357.
791:Kagan, Richard L. 1981. \emph{Lawsuits and Litigants in Castile, 1500-1700}. Chapel Hill: University of North Carolina Press.
797:Kaufmann, Daniel, Aart Kraay, and Massimo Mastruzzi. 2011. ``The Worldwide Governance Indicators: Methodology and Analytical Issues.'' \emph{Hague Journal on the Rule of Law} 3(2): 220-246. doi:10.1017/S1876404511200046.
809:La Porta, Rafael, Florencio L\'opez-de-Silanes, Cristian Pop-Eleches, and Andrei Shleifer. 2004. ``Judicial Checks and Balances.'' \emph{Journal of Political Economy} 112(2): 445-470.
812:Landes, William M., and Richard A. Posner. 1975. ``The Independent Judiciary in an Interest-Group Perspective.'' \emph{Journal of Law and Economics} 18(3): 875-901. doi:10.1086/466849.
815:\emph{Langborger v.\ Sweden}, application no.~11179/84. European Court of Human Rights, judgment of 22 June 1989, Series A no.~155. \url{https://lagen.nu/dom/echr/001-57515}.
869:Minzner, Carl F. 2011. ``China's Turn against Law.'' \emph{American Journal of Comparative Law} 59(4): 935-984. doi:10.5131/ajcl.2011.0006.
884:Ramseyer, J.\,Mark. 1994. ``The Puzzling (In)Dependence of Courts: A Comparative Approach.'' \emph{Journal of Legal Studies} 23(2): 721-747. doi:10.1086/467943.
908:\emph{Stallarholmens Pl\aa tslageri o Ventilation Handelsbolag v.\ Sweden}, application no.~12733/87. European Commission of Human Rights, decision of 7 September 1990. \url{https://lagen.nu/dom/echr/001-727}.
911:Stephenson, Matthew C. 2003. ``When the Devil Turns\ldots: The Political Foundations of Independent Judicial Review.'' \emph{Journal of Legal Studies} 32(1): 59-89. doi:10.1086/342038.
917:Swann, Julian. 1995. \emph{Politics and the Parlement of Paris under Louis XV, 1754-1774}. Cambridge: Cambridge University Press. doi:10.1017/cbo9780511661013.
929:Van Kley, Dale K. 1996. \emph{The Religious Origins of the French Revolution: From Calvin to the Civil Constitution, 1560-1791}. New Haven: Yale University Press.
941:Whittington, Keith E. 2005. ``\thinspace`Interpose Your Friendly Hand': Political Supports for the Exercise of Judicial Review by the United States Supreme Court.'' \emph{American Political Science Review} 99(4): 583-596. doi:10.1017/s0003055405051890.
944:Wiessner, Polly. 2005. ``Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity?'' \emph{Human Nature} 16(2): 115-145. doi:10.1007/s12110-005-1000-9.
947:Woodburn, James. 1982. ``Egalitarian Societies.'' \emph{Man}, new series, 17(3): 431-451. doi:10.2307/2801707.

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "rg -n 'doi:' papers/latex/judicial-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
641:Bauckham, Richard. 1993. \emph{The Theology of the Book of Revelation}. Cambridge: Cambridge University Press. doi:10.1017/cbo9780511819858.
644:Bell, David A. 1994. \emph{Lawyers and Citizens: The Making of a Political Elite in Old Regime France}. New York: Oxford University Press. doi:10.1093/oso/9780195076707.001.0001.
650:Berman, Harold J. 1983. \emph{Law and Revolution: The Formation of the Western Legal Tradition}. Cambridge, MA: Harvard University Press. doi:10.4159/9780674020863.
653:Boehm, Christopher. 1999. \emph{Hierarchy in the Forest: The Evolution of Egalitarian Behavior}. Cambridge, MA: Harvard University Press. doi:10.2307/j.ctvjf9xr4.
656:Bonica, Adam, and Maya Sen. 2017. ``A Common-Space Scaling of the American Judiciary and Legal Profession.'' \emph{Political Analysis} 25(1): 114-121. doi:10.1017/pan.2016.10.
659:Brown, Nathan J. 1997. \emph{The Rule of Law in the Arab World: Courts in Egypt and the Gulf}. Cambridge: Cambridge University Press. doi:10.1017/cbo9780511583278.
662:Brundage, James A. 1995. \emph{Medieval Canon Law}. London: Longman. doi:10.4324/9781315844596.
677:Coppedge, Michael, John Gerring, David Altman, Michael Bernhard, Steven Fish, Allen Hicken, Matthew Kroenig, Staffan I. Lindberg, Kelly McMann, Pamela Paxton, Holli A. Semetko, Svend-Erik Skaaning, Jeffrey Staton, and Jan Teorell. 2011. ``Conceptualizing and Measuring Democracy: A New Approach.'' \emph{Perspectives on Politics} 9(2): 247-267. doi:10.1017/S1537592711000880.
680:Cox, Michael, Gwen Arnold, and Sergio Villamayor Tomas. 2010. ``A Review of Design Principles for Community-based Natural Resource Management.'' \emph{Ecology and Society} 15(4): 38. doi:10.5751/ES-03704-150438.
683:Doyle, William. 1996. \emph{Venality: The Sale of Offices in Eighteenth-Century France}. Oxford: Oxford University Press. doi:10.1093/acprof:oso/9780198205364.001.0001.
692:Epp, Charles R. 1998. \emph{The Rights Revolution: Lawyers, Activists, and Supreme Courts in Comparative Perspective}. Chicago: University of Chicago Press. doi:10.7208/chicago/9780226772424.001.0001.
698:Feld, Lars P., and Stefan Voigt. 2003. ``Economic Growth and Judicial Independence: Cross-Country Evidence Using a New Set of Indicators.'' \emph{European Journal of Political Economy} 19(3): 497-527. doi:10.1016/s0176-2680(03)00017-x.
704:Fosi, Irene. 2011. \emph{Papal Justice: Subjects and Courts in the Papal State, 1500-1750}. Washington, DC: Catholic University of America Press. doi:10.2307/j.ctt2852kt.
707:Fuller, Robert C. 1995. \emph{Naming the Antichrist: The History of an American Obsession}. New York: Oxford University Press. doi:10.1093/acprof:oso/9780195109795.001.0001.
710:Galanter, Marc. 1974. ``Why the `Haves' Come Out Ahead: Speculations on the Limits of Legal Change.'' \emph{Law \& Society Review} 9(1): 95-160. doi:10.2307/3053023.
716:Gibson, James L., Gregory A. Caldeira, and Lester Kenyatta Spence. 2003. ``The Supreme Court and the US Presidential Election of 2000: Wounds, Self-Inflicted or Otherwise?'' \emph{British Journal of Political Science} 33(4): 535-556. doi:10.1017/S0007123403000243.
719:Ginsburg, Tom, and Tamir Moustafa, eds. 2008. \emph{Rule by Law: The Politics of Courts in Authoritarian Regimes}. Cambridge: Cambridge University Press. doi:10.1017/CBO9780511814822.
722:Given, James B. 1997. \emph{Inquisition and Medieval Society: Power, Discipline, and Resistance in Languedoc}. Ithaca: Cornell University Press. doi:10.7591/9781501724954.
731:Hallaq, Wael B. 2005. \emph{The Origins and Evolution of Islamic Law}. Cambridge: Cambridge University Press. doi:10.1017/cbo9780511818783.
734:Hallaq, Wael B. 2009. \emph{An Introduction to Islamic Law}. Cambridge: Cambridge University Press. doi:10.1017/cbo9780511801044.
743:Hart, H.\,L.\,A. 1961. \emph{The Concept of Law}. Oxford: Clarendon Press. Third edition 2012, Oxford University Press. doi:10.1093/he/9780199644704.001.0001.
749:Helmke, Gretchen. 2005. \emph{Courts under Constraints: Judges, Generals, and Presidents in Argentina}. Cambridge: Cambridge University Press. doi:10.1017/cbo9780511510144.
755:Hendley, Kathryn. 1996. \emph{Trying to Make Law Matter: Legal Reform and Labor Law in the Soviet Union}. Ann Arbor: University of Michigan Press. doi:10.3998/mpub.14759.
758:Hendley, Kathryn. 2017. \emph{Everyday Law in Russia}. Ithaca: Cornell University Press. doi:10.7591/9781501708107.
767:Hirschl, Ran. 2001. ``The Political Origins of Judicial Empowerment through Constitutionalization: Lessons from Israel's Constitutional Revolution.'' \emph{Comparative Politics} 33(3): 315-335. doi:10.2307/422406.
770:Hirschl, Ran. 2004. \emph{Towards Juristocracy: The Origins and Consequences of the New Constitutionalism}. Cambridge, MA: Harvard University Press. doi:10.2307/j.ctv15d81nb.
773:Hirschl, Ran. 2010. \emph{Constitutional Theocracy}. Cambridge, MA: Harvard University Press. doi:10.2307/j.ctvjghxd5.
776:Huskey, Eugene. 1986. \emph{Russian Lawyers and the Soviet State: The Origins and Development of the Soviet Bar, 1917-1939}. Princeton: Princeton University Press. doi:10.1515/9781400854516.
785:Jennings, Ronald C. 1978. ``Kadi, Court, and Legal Procedure in 17th C. Ottoman Kayseri.'' \emph{Studia Islamica} 48: 133-172. doi:10.2307/1595357.
797:Kaufmann, Daniel, Aart Kraay, and Massimo Mastruzzi. 2011. ``The Worldwide Governance Indicators: Methodology and Analytical Issues.'' \emph{Hague Journal on the Rule of Law} 3(2): 220-246. doi:10.1017/S1876404511200046.
803:Koester, Craig R. 2014. \emph{Revelation: A New Translation with Introduction and Commentary}. Anchor Yale Bible 38A. New Haven: Yale University Press. doi:10.12987/9780300211030.
812:Landes, William M., and Richard A. Posner. 1975. ``The Independent Judiciary in an Interest-Group Perspective.'' \emph{Journal of Law and Economics} 18(3): 875-901. doi:10.1086/466849.
824:Levitsky, Steven, and Lucan A. Way. 2010. \emph{Competitive Authoritarianism: Hybrid Regimes after the Cold War}. Cambridge: Cambridge University Press. doi:10.1017/CBO9780511781353.
848:Makdisi, George. 1981. \emph{The Rise of Colleges: Institutions of Learning in Islam and the West}. Edinburgh: Edinburgh University Press. doi:10.1515/9781474470643.
866:Messick, Brinkley. 1993. \emph{The Calligraphic State: Textual Domination and History in a Muslim Society}. Berkeley: University of California Press. doi:10.1525/9780520917828.
869:Minzner, Carl F. 2011. ``China's Turn against Law.'' \emph{American Journal of Comparative Law} 59(4): 935-984. doi:10.5131/ajcl.2011.0006.
872:Moustafa, Tamir. 2007. \emph{The Struggle for Constitutional Power: Law, Politics, and Economic Development in Egypt}. Cambridge: Cambridge University Press. doi:10.1017/cbo9780511511202.
875:Ostrom, Elinor. 1990. \emph{Governing the Commons: The Evolution of Institutions for Collective Action}. Cambridge: Cambridge University Press. doi:10.1017/CBO9780511807763.
878:Peerenboom, Randall. 2002. \emph{China's Long March toward Rule of Law}. Cambridge: Cambridge University Press. doi:10.1017/cbo9780511493737.
884:Ramseyer, J.\,Mark. 1994. ``The Puzzling (In)Dependence of Courts: A Comparative Approach.'' \emph{Journal of Legal Studies} 23(2): 721-747. doi:10.1086/467943.
902:Shapiro, Martin. 1981. \emph{Courts: A Comparative and Political Analysis}. Chicago: University of Chicago Press. doi:10.7208/chicago/9780226161341.001.0001.
911:Stephenson, Matthew C. 2003. ``When the Devil Turns\ldots: The Political Foundations of Independent Judicial Review.'' \emph{Journal of Legal Studies} 32(1): 59-89. doi:10.1086/342038.
914:Stone Sweet, Alec. 2000. \emph{Governing with Judges: Constitutional Politics in Europe}. Oxford: Oxford University Press. doi:10.1093/0198297718.001.0001.
917:Swann, Julian. 1995. \emph{Politics and the Parlement of Paris under Louis XV, 1754-1774}. Cambridge: Cambridge University Press. doi:10.1017/cbo9780511661013.
923:Tamanaha, Brian Z. 2004. \emph{On the Rule of Law: History, Politics, Theory}. Cambridge: Cambridge University Press. doi:10.1017/CBO9780511812378.
926:Tushnet, Mark. 2008. \emph{Weak Courts, Strong Rights: Judicial Review and Social Welfare Rights in Comparative Constitutional Law}. Princeton: Princeton University Press. doi:10.1515/9781400828159.
932:Vanberg, Georg. 2005. \emph{The Politics of Constitutional Review in Germany}. Cambridge: Cambridge University Press. doi:10.1017/cbo9780511510427.
935:Vogel, Frank E. 2000. \emph{Islamic Law and the Legal System of Saudi Arabia}. Leiden: Brill. doi:10.1163/9789047400165.
941:Whittington, Keith E. 2005. ``\thinspace`Interpose Your Friendly Hand': Political Supports for the Exercise of Judicial Review by the United States Supreme Court.'' \emph{American Political Science Review} 99(4): 583-596. doi:10.1017/s0003055405051890.
944:Wiessner, Polly. 2005. ``Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity?'' \emph{Human Nature} 16(2): 115-145. doi:10.1007/s12110-005-1000-9.
947:Woodburn, James. 1982. ``Egalitarian Societies.'' \emph{Man}, new series, 17(3): 431-451. doi:10.2307/2801707.
950:Zaman, Muhammad Qasim. 2002. \emph{The Ulama in Contemporary Islam: Custodians of Change}. Princeton: Princeton University Press. doi:10.2307/j.ctt7rh2s.
953:Zubaida, Sami. 2003. \emph{Law and Power in the Islamic World}. London: I.\,B. Tauris. doi:10.5040/9780755612208.

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "rg -n '&|#|%' papers/latex/judicial-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
16:\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
236:Case & Determination procedure & Source of compliance & Strongest counter-reading \\
238:Nuer & The leopard-skin chief mediates blood-feud compensation in cattle between lineages & Consent of the parties backed by the threat of renewed feud & The chief has no power to compel, so the settlement is a bargain rather than a judgment \\
239:Barotse & Judges in a council apply the standard of the reasonable man to the conduct of litigants & Kinship obligations and the authority of the council & The Lozi had a kingdom, so the case shows a court rather than a stateless procedure \\
240:Arusha & Councils of elders and lineage moots negotiate settlements between disputants & Pressure from kin groups and the prospect of continued relations & Outcomes reflect relative bargaining strength, so the procedure is negotiation \\
241:Ju/'hoansi & Kin and camp members talk disputes out in public, and parties often move to another camp & Ridicule, gossip and the value of continued sharing relations & Exit by moving camp resolves many disputes with no third party at all \\
242:Reverse dominance hierarchies & The camp acts as a moral community that judges would-be dominants and deviants & Criticism, ostracism, exile and in extreme cases execution & The judging group is also the sanctioning group, so the functions are fused \\
243:Commons institutions & Users or their officials hold low-cost local arenas to resolve conflicts over the rules & Graduated sanctions and monitoring by users & The arenas are designed institutions, so they show possibility rather than necessity \\
517:Regime type & Principal holders of the judicial function & Concentration and contestability & Strongest coupling to other pillars & Documented check or capture episode \\
519:Market-capitalist societies & Appointed and elected judges, a large private bar, administrative tribunals and private arbitration & Low concentration in ordinary cases and high concentration at the constitutional apex, with access as the weakest link & Resources to adjudication through repeat players, funded litigation and judicial campaign finance & The recusal ruling in \emph{Caperton} checked a capture risk created by campaign spending \\
521:Communist party-states & Courts, the procuracy, party bodies supervising legal work, and a state-disciplined bar & Low concentration in ordinary cases and high concentration in politically salient cases, with low ruler-boundness & Rule-making to adjudication through party appointment, and coercion through the procuracy & Stalin-era courts followed campaign directives, while later reform raised legality in ordinary cases \\
523:Social democracy and democratic socialism & Ordinary and administrative courts, labor courts, ombudsmen and parliamentary review committees & Low concentration, high disclosure and compliance, and restrained constitutional review in Nordic systems & Production to adjudication through labor courts with members nominated by labor-market organizations & The \emph{Langborger} ruling held that interested nominating bodies can defeat impartiality \\
525:Islamic states & Qadis and muftis historically, and in modern states codified courts, royal or clerical councils and administrative courts & Moderate concentration in classical practice and high concentration at the apex in modern Iran and Saudi Arabia & Legitimation to adjudication through the ulama, and rule-making through royal or clerical appointment & Iran's Guardian Council screens legislation and candidates, while plural schools and independent muftis supplied historical checks \\
527:Historical Catholic monarchies & Royal courts, parlements and chanceries, church courts, the Inquisition and papal tribunals & Moderate concentration with contestability supplied by competition among jurisdictions & Legitimation to adjudication through church courts and the Inquisition, and resources through venal offices & Maupeou's suppression of the parlements in 1771 was reversed in 1774 \\
529:Secular democracies & Constitutional and supreme courts, ordinary and administrative courts, judicial councils and international courts & Low concentration in ordinary cases and high concentration at the constitutional apex, with compliance resting on public support & Rule-making to adjudication through appointment and through review that acts as co-legislation & The enlargement of the Argentine Supreme Court in 1990 produced a court aligned with the government \\
571:Component & Formal indicators & Indicators of observed functioning \\
573:Disclosure & A legal duty to publish reasoned decisions and rules on recusal and conflict disclosure & The share of decisions published with reasons, and disclosed financial ties between litigants and judges \\
574:Access & The availability of legal aid, the right of appeal, and limits on court fees & Legal-aid coverage, the cost of litigation relative to income, and appeal rates by litigant type \\
575:Independence & Appointment rules, tenure security and salary protection, as coded by La Porta and coauthors & The rate of rulings against the government and judges' turnover after changes of government \\
576:Compliance & Constitutional duties of officials to execute judgments & The share of adverse rulings against government bodies that are executed within a stated period \\
710:Galanter, Marc. 1974. ``Why the `Haves' Come Out Ahead: Speculations on the Limits of Legal Change.'' \emph{Law \& Society Review} 9(1): 95-160. doi:10.2307/3053023.

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "perl -0777 -ne 'while (/\\\\(?:citep|citet)\\{(["'^}]*)'"\\}/g) {"'$c{$_}=1 for split /'"\\s*,\\s*/, "'$1} while (/'"\\\\bibitem(?:\\[["'^]]*'"\\])?\\{(["'^}]*)'"\\}/g) {"'$b{$1}=1} while (/'"\\\\(?:[Cc]ref)\\{(["'^}]*)'"\\}/g) {"'$r{$_}=1 for split /'"\\s*,\\s*/, "'$1} while (/'"\\\\label\\{(["'^}]*)'"\\}/g) {"'$l{$1}=1} print "Missing citations:'"\\n\"; print \""'$_'"\\n\" for grep {"'!$b{$_}} sort keys %c; print "Missing references:'"\\n\"; print \""'$_'"\\n\" for grep {"'!$l{$_}} sort keys %r; print "Duplicate bib keys:'"\\n\"; while (/\\\\bibitem(?:\\[["'^]]*'"\\])?\\{(["'^}]*)'"\\}/g) {"'$bc{$1}++} print "$_'"\\n\" for grep {"'$bc{$_}>1} sort keys %bc; print "Duplicate labels:'"\\n\"; while (/\\\\label\\{(["'^}]*)'"\\}/g) {"'$lc{$1}++} print "$_'"\\n\" for grep {"'$lc{$_}>1} sort keys %lc'"' papers/latex/judicial-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
Missing citations:
Missing references:
Duplicate bib keys:
Duplicate labels:

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "perl -ne 'while (/\\\\(begin|end)\\{(["'^}]*)'"\\}/g) { if ("'$1 eq "begin") { push @s, [$2,$.] } elsif (!@s) { print "Unmatched end {$2} at $.'"\\n\" } else { "'$x=pop @s; print "Mismatch: begin {$x->[0]} at $x->[1], end {$2} at $.'"\\n\" if "'$x->[0] ne $2 } } END { print "Unclosed begin {$$_[0]} at $$_[1]'"\\n\" for @s }' papers/latex/judicial-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "perl -ne '"'$x=$_; $x =~ s/'"\\\\[{}]//g; for "'$c (split //,$x) { if ($c eq "{") { push @s,$. } elsif ($c eq "}") { if (@s) { pop @s } else { print "Extra closing brace at $.'"\\n\" } } } END { print \"Unclosed opening brace from line "'$_'"\\n\" for @s }' papers/latex/judicial-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "rg -c '"'^'"\\\\bibitem' papers/latex/judicial-power.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
106

codex
- Line 634: `\begin{thebibliography}{99}` declares space for only two-digit numeric labels, but the file contains 106 entries. Although currently masked by author–year mode, change it to `\begin{thebibliography}{999}` for correct, robust formatting.

- Lines 656, 677, 686, 698, 704, 710, 716, 752, 767, 776, 785, 791, 797, 809, 812, 869, 884, 911, 917, 929, 941, 944, and 947: numeric page/year ranges use hyphens. Use TeX en dashes—for example, `114--121`, `1469--1716`, and `1500--1750`. Do not alter hyphens within DOIs, URLs, or docket numbers.

- Lines 641, 644, 650, 653, 656, 659, 662, 677, 680, 683, 692, 698, 704, 707, 710, 716, 719, 722, 731, 734, 743, 749, 755, 758, 767, 770, 773, 776, 785, 797, 803, 812, 824, 848, 866, 869, 872, 875, 878, 884, 902, 911, 914, 917, 923, 926, 932, 935, 941, 944, 947, 950, and 953: DOI identifiers are plain, unbreakable text while ordinary URLs use `\url`. For consistent hyperlinking and safer line breaking, replace forms such as `doi:10.1017/...` with `\url{https://doi.org/10.1017/...}`. The already-loaded `hyperref` package is sufficient.

No unmatched braces/environments, missing citation keys, duplicate labels, broken cross-references, or missing packages were found by source inspection. A compilation log was not produced because the review was restricted to reading this file, so actual overfull/underfull warnings could not be measured.

VERDICT: NEEDS_FIX
hook: Stop
hook: Stop
hook: Stop Completed
hook: Stop Completed
tokens used
76,267
- Line 634: `\begin{thebibliography}{99}` declares space for only two-digit numeric labels, but the file contains 106 entries. Although currently masked by author–year mode, change it to `\begin{thebibliography}{999}` for correct, robust formatting.

- Lines 656, 677, 686, 698, 704, 710, 716, 752, 767, 776, 785, 791, 797, 809, 812, 869, 884, 911, 917, 929, 941, 944, and 947: numeric page/year ranges use hyphens. Use TeX en dashes—for example, `114--121`, `1469--1716`, and `1500--1750`. Do not alter hyphens within DOIs, URLs, or docket numbers.

- Lines 641, 644, 650, 653, 656, 659, 662, 677, 680, 683, 692, 698, 704, 707, 710, 716, 719, 722, 731, 734, 743, 749, 755, 758, 767, 770, 773, 776, 785, 797, 803, 812, 824, 848, 866, 869, 872, 875, 878, 884, 902, 911, 914, 917, 923, 926, 932, 935, 941, 944, 947, 950, and 953: DOI identifiers are plain, unbreakable text while ordinary URLs use `\url`. For consistent hyperlinking and safer line breaking, replace forms such as `doi:10.1017/...` with `\url{https://doi.org/10.1017/...}`. The already-loaded `hyperref` package is sufficient.

No unmatched braces/environments, missing citation keys, duplicate labels, broken cross-references, or missing packages were found by source inspection. A compilation log was not produced because the review was restricted to reading this file, so actual overfull/underfull warnings could not be measured.

VERDICT: NEEDS_FIX
