---
reviewer: codex (OpenAI) gpt-5.6-sol
type: formatting
paper: ideological-power
round: 3
date: 2026-10-22T17:14:44Z
---
Reading additional input from stdin...
OpenAI Codex v0.145.0
--------
workdir: /Users/mlong/Documents/Development/the-beast-system
model: gpt-5.6-sol
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a1649b-a69d-7043-a6ee-28931c740350
--------
user
Read only papers/latex/ideological-power.tex and its .log (papers/latex/ideological-power.log). Do not explore other files or run builds. Review it for LaTeX formatting issues: compilation errors, missing packages, broken references, inconsistent styling, overfull/underfull boxes, spacing problems. House rules that are intentional and not issues: page and number ranges use a single hyphen or the word 'to' (no en dashes), DOIs are plain text, the preamble skeleton packages are fixed. List all issues with line numbers and concrete fixes. Output the findings list and the VERDICT line only. End with exactly one of: VERDICT: PASS (no issues remain) or VERDICT: NEEDS_FIX (issues listed above must be fixed).
warning: Under-development features enabled: chronicle. Under-development features are incomplete and may behave unpredictably. To suppress this warning, set `suppress_unstable_features_warning = true` in /Users/mlong/.codex/config.toml.
warning: clamping SessionEnd hook timeout to 3s in /Users/mlong/.codex/plugins/cache/openai-codex/codex/1.0.6/hooks/hooks.json
2026-10-22T17:14:45.453262Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server linear: OAuth token refresh failed: Server returned error response: invalid_grant: Grant not found
2026-10-22T17:14:45.815888Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server resend: OAuth token refresh failed: Server returned error response: invalid_grant: Refresh token has been revoked
warning: Exceeded skills context budget of 2%. All skill descriptions were removed and 16 additional skills were not included in the model-visible skills list.
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
I’ll inspect only the specified `.tex` and `.log`, without building or accessing anything else.
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'nl -ba papers/latex/ideological-power.log' in /Users/mlong/Documents/Development/the-beast-system
exec
/usr/local/bin/zsh -lc 'nl -ba papers/latex/ideological-power.tex' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	This is pdfTeX, Version 3.141592653-2.6-1.40.29 (TeX Live 2026) (preloaded format=pdflatex 2026.3.22)  22 OCT 2026 12:14
     2	entering extended mode
     3	 restricted \write18 enabled.
     4	 %&-line parsing enabled.
     5	**ideological-power.tex
     6	(./ideological-power.tex
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
   215	(/usr/local/texlive/2026/texmf-dist/tex/latex/xcolor/xcolor.sty
   216	Package: xcolor 2024/09/29 v3.02 LaTeX color extensions (UK)
   217	
   218	(/usr/local/texlive/2026/texmf-dist/tex/latex/graphics-cfg/color.cfg
   219	File: color.cfg 2016/01/02 v1.6 sample color configuration
   220	)
   221	Package xcolor Info: Driver file: pdftex.def on input line 274.
   222	
   223	(/usr/local/texlive/2026/texmf-dist/tex/latex/graphics-def/pdftex.def
   224	File: pdftex.def 2025/09/29 v1.2d Graphics/color driver for pdftex
   225	)
   226	(/usr/local/texlive/2026/texmf-dist/tex/latex/graphics/mathcolor.ltx)
   227	Package xcolor Info: Model `cmy' substituted by `cmy0' on input line 1349.
   228	Package xcolor Info: Model `hsb' substituted by `rgb' on input line 1353.
   229	Package xcolor Info: Model `RGB' extended on input line 1365.
   230	Package xcolor Info: Model `HTML' substituted by `rgb' on input line 1367.
   231	Package xcolor Info: Model `Hsb' substituted by `hsb' on input line 1368.
   232	Package xcolor Info: Model `tHsb' substituted by `hsb' on input line 1369.
   233	Package xcolor Info: Model `HSB' substituted by `hsb' on input line 1370.
   234	Package xcolor Info: Model `Gray' substituted by `gray' on input line 1371.
   235	Package xcolor Info: Model `wave' substituted by `hsb' on input line 1372.
   236	)
   237	(/usr/local/texlive/2026/texmf-dist/tex/latex/pgf/frontendlayer/tikz.sty
   238	(/usr/local/texlive/2026/texmf-dist/tex/latex/pgf/basiclayer/pgf.sty
   239	(/usr/local/texlive/2026/texmf-dist/tex/latex/pgf/utilities/pgfrcs.sty
   240	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/utilities/pgfutil-common.te
   241	x
   242	\pgfutil@everybye=\toks32
   243	\pgfutil@tempdima=\dimen167
   244	\pgfutil@tempdimb=\dimen168
   245	)
   246	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/utilities/pgfutil-latex.def
   247	\pgfutil@abb=\box56
   248	) (/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/utilities/pgfrcs.code.tex
   249	(/usr/local/texlive/2026/texmf-dist/tex/generic/pgf/pgf.revision.tex)
   250	Package: pgfrcs 2025-08-29 v3.1.11a (3.1.11a)
   251	))
   252	Package: pgf 2025-08-29 v3.1.11a (3.1.11a)
   253	
   254	(/usr/local/texlive/2026/texmf-dist/tex/latex/pgf/basiclayer/pgfcore.sty
   255	(/usr/local/texlive/2026/texmf-dist/tex/latex/graphics/graphicx.sty
   256	Package: graphicx 2024/12/31 v1.2e Enhanced LaTeX Graphics (DPC,SPQR)
   257	
   258	(/usr/local/texlive/2026/texmf-dist/tex/latex/graphics/graphics.sty
   259	Package: graphics 2024/08/06 v1.4g Standard LaTeX Graphics (DPC,SPQR)
   260	
   261	(/usr/local/texlive/2026/texmf-dist/tex/latex/graphics/trig.sty
   262	Package: trig 2023/12/02 v1.11 sin cos tan (DPC)
   263	)
   264	(/usr/local/texlive/2026/texmf-dist/tex/latex/graphics-cfg/graphics.cfg
   265	File: graphics.cfg 2016/06/04 v1.11 sample graphics configuration
   266	)
   267	Package graphics Info: Driver file: pdftex.def on input line 106.
   268	)
   269	\Gin@req@height=\dimen169
   270	\Gin@req@width=\dimen170
   271	)
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
   572	(/usr/local/texlive/2026/texmf-dist/tex/latex/natbib/natbib.sty
   573	Package: natbib 2010/09/13 8.31b (PWD, AO)
   574	\bibhang=\skip60
   575	\bibsep=\skip61
   576	LaTeX Info: Redefining \cite on input line 694.
   577	\c@NAT@ctr=\count327
   578	)
   579	(/usr/local/texlive/2026/texmf-dist/tex/latex/hyperref/hyperref.sty
   580	Package: hyperref 2026-01-29 v7.01p Hypertext links for LaTeX
   581	
   582	(/usr/local/texlive/2026/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty
   583	Package: kvsetkeys 2022-10-05 v1.19 Key value parser (HO)
   584	)
   585	(/usr/local/texlive/2026/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty
   586	Package: kvdefinekeys 2019-12-19 v1.6 Define keys (HO)
   587	)
   588	(/usr/local/texlive/2026/texmf-dist/tex/generic/pdfescape/pdfescape.sty
   589	Package: pdfescape 2019/12/09 v1.15 Implements pdfTeX's escape features (HO)
   590	
   591	(/usr/local/texlive/2026/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty
   592	Package: ltxcmds 2023-12-04 v1.26 LaTeX kernel commands for general use (HO)
   593	)
   594	(/usr/local/texlive/2026/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty
   595	Package: pdftexcmds 2020-06-27 v0.33 Utility functions of pdfTeX for LuaTeX (HO
   596	)
   597	
   598	(/usr/local/texlive/2026/texmf-dist/tex/generic/infwarerr/infwarerr.sty
   599	Package: infwarerr 2019/12/03 v1.5 Providing info/warning/error messages (HO)
   600	)
   601	Package pdftexcmds Info: \pdf@primitive is available.
   602	Package pdftexcmds Info: \pdf@ifprimitive is available.
   603	Package pdftexcmds Info: \pdfdraftmode found.
   604	))
   605	(/usr/local/texlive/2026/texmf-dist/tex/latex/hycolor/hycolor.sty
   606	Package: hycolor 2020-01-27 v1.10 Color options for hyperref/bookmark (HO)
   607	)
   608	(/usr/local/texlive/2026/texmf-dist/tex/latex/hyperref/nameref.sty
   609	Package: nameref 2026-01-29 v2.58 Cross-referencing by name of section
   610	
   611	(/usr/local/texlive/2026/texmf-dist/tex/latex/refcount/refcount.sty
   612	Package: refcount 2019/12/15 v3.6 Data extraction from label references (HO)
   613	)
   614	(/usr/local/texlive/2026/texmf-dist/tex/generic/gettitlestring/gettitlestring.s
   615	ty
   616	Package: gettitlestring 2019/12/15 v1.6 Cleanup title references (HO)
   617	 (/usr/local/texlive/2026/texmf-dist/tex/latex/kvoptions/kvoptions.sty
   618	Package: kvoptions 2022-06-15 v3.15 Key value format for package options (HO)
   619	))
   620	\c@section@level=\count328
   621	)
   622	(/usr/local/texlive/2026/texmf-dist/tex/generic/stringenc/stringenc.sty
   623	Package: stringenc 2019/11/29 v1.12 Convert strings between diff. encodings (HO
   624	)
   625	)
   626	\@linkdim=\dimen295
   627	\Hy@linkcounter=\count329
   628	\Hy@pagecounter=\count330
   629	
   630	(/usr/local/texlive/2026/texmf-dist/tex/latex/hyperref/pd1enc.def
   631	File: pd1enc.def 2026-01-29 v7.01p Hyperref: PDFDocEncoding definition (HO)
   632	Now handling font encoding PD1 ...
   633	... no UTF-8 mapping file for font encoding PD1
   634	)
   635	(/usr/local/texlive/2026/texmf-dist/tex/generic/intcalc/intcalc.sty
   636	Package: intcalc 2019/12/15 v1.3 Expandable calculations with integers (HO)
   637	)
   638	\Hy@SavedSpaceFactor=\count331
   639	
   640	(/usr/local/texlive/2026/texmf-dist/tex/latex/hyperref/puenc.def
   641	File: puenc.def 2026-01-29 v7.01p Hyperref: PDF Unicode definition (HO)
   642	Now handling font encoding PU ...
   643	... no UTF-8 mapping file for font encoding PU
   644	)
   645	Package hyperref Info: Hyper figures OFF on input line 4201.
   646	Package hyperref Info: Link nesting OFF on input line 4206.
   647	Package hyperref Info: Hyper index ON on input line 4209.
   648	Package hyperref Info: Plain pages OFF on input line 4216.
   649	Package hyperref Info: Backreferencing OFF on input line 4221.
   650	Package hyperref Info: Implicit mode ON; LaTeX internals redefined.
   651	Package hyperref Info: Bookmarks ON on input line 4468.
   652	\c@Hy@tempcnt=\count332
   653	
   654	(/usr/local/texlive/2026/texmf-dist/tex/latex/url/url.sty
   655	\Urlmuskip=\muskip18
   656	Package: url 2013/09/16  ver 3.4  Verb mode for urls, etc.
   657	)
   658	LaTeX Info: Redefining \url on input line 4807.
   659	\XeTeXLinkMargin=\dimen296
   660	
   661	(/usr/local/texlive/2026/texmf-dist/tex/generic/bitset/bitset.sty
   662	Package: bitset 2019/12/09 v1.3 Handle bit-vector datatype (HO)
   663	
   664	(/usr/local/texlive/2026/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty
   665	Package: bigintcalc 2019/12/15 v1.5 Expandable calculations on big integers (HO
   666	)
   667	))
   668	\Fld@menulength=\count333
   669	\Field@Width=\dimen297
   670	\Fld@charsize=\dimen298
   671	Package hyperref Info: Hyper figures OFF on input line 6084.
   672	Package hyperref Info: Link nesting OFF on input line 6089.
   673	Package hyperref Info: Hyper index ON on input line 6092.
   674	Package hyperref Info: backreferencing OFF on input line 6099.
   675	Package hyperref Info: Link coloring OFF on input line 6104.
   676	Package hyperref Info: Link coloring with OCG OFF on input line 6109.
   677	Package hyperref Info: PDF/A mode OFF on input line 6114.
   678	\Hy@abspage=\count334
   679	\c@Item=\count335
   680	\c@Hfootnote=\count336
   681	)
   682	Package hyperref Info: Driver (autodetected): hpdftex.
   683	
   684	(/usr/local/texlive/2026/texmf-dist/tex/latex/hyperref/hpdftex.def
   685	File: hpdftex.def 2026-01-29 v7.01p Hyperref driver for pdfTeX
   686	\Fld@listcount=\count337
   687	\c@bookmark@seq@number=\count338
   688	
   689	(/usr/local/texlive/2026/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
   690	Package: rerunfilecheck 2025-06-21 v1.11 Rerun checks for auxiliary files (HO)
   691	
   692	(/usr/local/texlive/2026/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty
   693	Package: uniquecounter 2019/12/15 v1.4 Provide unlimited unique counter (HO)
   694	)
   695	Package uniquecounter Info: New unique counter `rerunfilecheck' on input line 2
   696	84.
   697	)
   698	\Hy@SectionHShift=\skip62
   699	) (/usr/local/texlive/2026/texmf-dist/tex/latex/cleveref/cleveref.sty
   700	Package: cleveref 2018/03/27 v0.21.4 Intelligent cross-referencing
   701	Package cleveref Info: `hyperref' support loaded on input line 2370.
   702	LaTeX Info: Redefining \cref on input line 2370.
   703	LaTeX Info: Redefining \Cref on input line 2370.
   704	LaTeX Info: Redefining \crefrange on input line 2370.
   705	LaTeX Info: Redefining \Crefrange on input line 2370.
   706	LaTeX Info: Redefining \cpageref on input line 2370.
   707	LaTeX Info: Redefining \Cpageref on input line 2370.
   708	LaTeX Info: Redefining \cpagerefrange on input line 2370.
   709	LaTeX Info: Redefining \Cpagerefrange on input line 2370.
   710	LaTeX Info: Redefining \labelcref on input line 2370.
   711	LaTeX Info: Redefining \labelcpageref on input line 2370.
   712	Package cleveref Info: `amsthm' support loaded on input line 3026.
   713	)
   714	==> First Aid for cleveref.sty applied!
   715	\c@theorem=\count339
   716	LaTeX Font Info:    Trying to load font information for T1+lmr on input line 54
   717	.
   718	(/usr/local/texlive/2026/texmf-dist/tex/latex/lm/t1lmr.fd
   719	File: t1lmr.fd 2015/05/01 v1.6.1 Font defs for Latin Modern
   720	)
   721	(/usr/local/texlive/2026/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def
   722	File: l3backend-pdftex.def 2025-10-09 L3 backend support: PDF output (pdfTeX)
   723	\l__color_backend_stack_int=\count340
   724	)
   725	(/private/tmp/claude-501/-Users-mlong-Documents-Development-the-beast-system/53
   726	a4f9b6-b8c1-4df4-96d8-300f973de288/scratchpad/ip-build/ideological-power.aux)
   727	\openout1 = `ideological-power.aux'.
   728	
   729	LaTeX Font Info:    Checking defaults for OML/cmm/m/it on input line 54.
   730	LaTeX Font Info:    ... okay on input line 54.
   731	LaTeX Font Info:    Checking defaults for OMS/cmsy/m/n on input line 54.
   732	LaTeX Font Info:    ... okay on input line 54.
   733	LaTeX Font Info:    Checking defaults for OT1/cmr/m/n on input line 54.
   734	LaTeX Font Info:    ... okay on input line 54.
   735	LaTeX Font Info:    Checking defaults for T1/cmr/m/n on input line 54.
   736	LaTeX Font Info:    ... okay on input line 54.
   737	LaTeX Font Info:    Checking defaults for TS1/cmr/m/n on input line 54.
   738	LaTeX Font Info:    ... okay on input line 54.
   739	LaTeX Font Info:    Checking defaults for OMX/cmex/m/n on input line 54.
   740	LaTeX Font Info:    ... okay on input line 54.
   741	LaTeX Font Info:    Checking defaults for U/cmr/m/n on input line 54.
   742	LaTeX Font Info:    ... okay on input line 54.
   743	LaTeX Font Info:    Checking defaults for PD1/pdf/m/n on input line 54.
   744	LaTeX Font Info:    ... okay on input line 54.
   745	LaTeX Font Info:    Checking defaults for PU/pdf/m/n on input line 54.
   746	LaTeX Font Info:    ... okay on input line 54.
   747	LaTeX Info: Redefining \microtypecontext on input line 54.
   748	Package microtype Info: Applying patch `item' on input line 54.
   749	Package microtype Info: Applying patch `toc' on input line 54.
   750	Package microtype Info: Applying patch `eqnum' on input line 54.
   751	Package microtype Info: Applying patch `footnote' on input line 54.
   752	Package microtype Info: Applying patch `verbatim' on input line 54.
   753	LaTeX Info: Redefining \microtypesetup on input line 54.
   754	Package microtype Info: Generating PDF output.
   755	Package microtype Info: Character protrusion enabled (level 2).
   756	Package microtype Info: Using default protrusion set `alltext'.
   757	Package microtype Info: Automatic font expansion enabled (level 2),
   758	(microtype)             stretch: 20, shrink: 20, step: 1, non-selected.
   759	Package microtype Info: Using default expansion set `alltext-nott'.
   760	Package microtype Info: Patching command `\showhyphens'.
   761	Package microtype Info: No adjustment of tracking.
   762	Package microtype Info: No adjustment of interword spacing.
   763	Package microtype Info: No adjustment of character kerning.
   764	
   765	(/usr/local/texlive/2026/texmf-dist/tex/latex/microtype/mt-cmr.cfg
   766	File: mt-cmr.cfg 2013/05/19 v2.2 microtype config. file: Computer Modern Roman 
   767	(RS)
   768	)
   769	*geometry* driver: auto-detecting
   770	*geometry* detected driver: pdftex
   771	*geometry* verbose mode - [ preamble ] result:
   772	* driver: pdftex
   773	* paper: letterpaper
   774	* layout: <same size as paper>
   775	* layoutoffset:(h,v)=(0.0pt,0.0pt)
   776	* modes: 
   777	* h-part:(L,W,R)=(72.26999pt, 469.75502pt, 72.26999pt)
   778	* v-part:(T,H,B)=(72.26999pt, 650.43001pt, 72.26999pt)
   779	* \paperwidth=614.295pt
   780	* \paperheight=794.96999pt
   781	* \textwidth=469.75502pt
   782	* \textheight=650.43001pt
   783	* \oddsidemargin=0.0pt
   784	* \evensidemargin=0.0pt
   785	* \topmargin=-37.0pt
   786	* \headheight=12.0pt
   787	* \headsep=25.0pt
   788	* \topskip=11.0pt
   789	* \footskip=30.0pt
   790	* \marginparwidth=59.0pt
   791	* \marginparsep=10.0pt
   792	* \columnsep=10.0pt
   793	* \skip\footins=10.0pt plus 4.0pt minus 2.0pt
   794	* \hoffset=0.0pt
   795	* \voffset=0.0pt
   796	* \mag=1000
   797	* \@twocolumnfalse
   798	* \@twosidefalse
   799	* \@mparswitchfalse
   800	* \@reversemarginfalse
   801	* (1in=72.27pt=25.4mm, 1cm=28.453pt)
   802	
   803	(/usr/local/texlive/2026/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
   804	[Loading MPS to PDF converter (version 2006.09.02).]
   805	\scratchcounter=\count341
   806	\scratchdimen=\dimen299
   807	\scratchbox=\box69
   808	\nofMPsegments=\count342
   809	\nofMParguments=\count343
   810	\everyMPshowfont=\toks46
   811	\MPscratchCnt=\count344
   812	\MPscratchDim=\dimen300
   813	\MPnumerator=\count345
   814	\makeMPintoPDFobject=\count346
   815	\everyMPtoPDFconversion=\toks47
   816	) (/usr/local/texlive/2026/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
   817	Package: epstopdf-base 2020-01-24 v2.11 Base part for package epstopdf
   818	Package epstopdf-base Info: Redefining graphics rule for `.eps' on input line 4
   819	85.
   820	
   821	(/usr/local/texlive/2026/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg
   822	File: epstopdf-sys.cfg 2010/07/13 v1.3 Configuration of (r)epstopdf for TeX Liv
   823	e
   824	))
   825	Package hyperref Info: Link coloring OFF on input line 54.
   826	
   827	(/private/tmp/claude-501/-Users-mlong-Documents-Development-the-beast-system/53
   828	a4f9b6-b8c1-4df4-96d8-300f973de288/scratchpad/ip-build/ideological-power.out)
   829	(/private/tmp/claude-501/-Users-mlong-Documents-Development-the-beast-system/53
   830	a4f9b6-b8c1-4df4-96d8-300f973de288/scratchpad/ip-build/ideological-power.out)
   831	\@outlinefile=\write4
   832	\openout4 = `ideological-power.out'.
   833	
   834	LaTeX Font Info:    Trying to load font information for OT1+lmr on input line 5
   835	6.
   836	
   837	(/usr/local/texlive/2026/texmf-dist/tex/latex/lm/ot1lmr.fd
   838	File: ot1lmr.fd 2015/05/01 v1.6.1 Font defs for Latin Modern
   839	)
   840	LaTeX Font Info:    Trying to load font information for OML+lmm on input line 5
   841	6.
   842	
   843	(/usr/local/texlive/2026/texmf-dist/tex/latex/lm/omllmm.fd
   844	File: omllmm.fd 2015/05/01 v1.6.1 Font defs for Latin Modern
   845	)
   846	LaTeX Font Info:    Trying to load font information for OMS+lmsy on input line 
   847	56.
   848	
   849	(/usr/local/texlive/2026/texmf-dist/tex/latex/lm/omslmsy.fd
   850	File: omslmsy.fd 2015/05/01 v1.6.1 Font defs for Latin Modern
   851	)
   852	LaTeX Font Info:    Trying to load font information for OMX+lmex on input line 
   853	56.
   854	
   855	(/usr/local/texlive/2026/texmf-dist/tex/latex/lm/omxlmex.fd
   856	File: omxlmex.fd 2015/05/01 v1.6.1 Font defs for Latin Modern
   857	)
   858	LaTeX Font Info:    External font `lmex10' loaded for size
   859	(Font)              <12> on input line 56.
   860	LaTeX Font Info:    External font `lmex10' loaded for size
   861	(Font)              <8> on input line 56.
   862	LaTeX Font Info:    External font `lmex10' loaded for size
   863	(Font)              <6> on input line 56.
   864	LaTeX Font Info:    Trying to load font information for U+msa on input line 56.
   865	
   866	
   867	(/usr/local/texlive/2026/texmf-dist/tex/latex/amsfonts/umsa.fd
   868	File: umsa.fd 2013/01/14 v3.01 AMS symbols A
   869	)
   870	(/usr/local/texlive/2026/texmf-dist/tex/latex/microtype/mt-msa.cfg
   871	File: mt-msa.cfg 2006/02/04 v1.1 microtype config. file: AMS symbols (a) (RS)
   872	)
   873	LaTeX Font Info:    Trying to load font information for U+msb on input line 56.
   874	
   875	
   876	(/usr/local/texlive/2026/texmf-dist/tex/latex/amsfonts/umsb.fd
   877	File: umsb.fd 2013/01/14 v3.01 AMS symbols B
   878	)
   879	(/usr/local/texlive/2026/texmf-dist/tex/latex/microtype/mt-msb.cfg
   880	File: mt-msb.cfg 2005/06/01 v1.0 microtype config. file: AMS symbols (b) (RS)
   881	)
   882	LaTeX Font Info:    Trying to load font information for T1+lmtt on input line 5
   883	6.
   884	
   885	(/usr/local/texlive/2026/texmf-dist/tex/latex/lm/t1lmtt.fd
   886	File: t1lmtt.fd 2015/05/01 v1.6.1 Font defs for Latin Modern
   887	)
   888	Package microtype Info: Loading generic protrusion settings for font family
   889	(microtype)             `lmtt' (encoding: T1).
   890	(microtype)             For optimal results, create family-specific settings.
   891	(microtype)             See the microtype manual for details.
   892	LaTeX Font Info:    External font `lmex10' loaded for size
   893	(Font)              <10> on input line 56.
   894	LaTeX Font Info:    External font `lmex10' loaded for size
   895	(Font)              <7> on input line 56.
   896	LaTeX Font Info:    External font `lmex10' loaded for size
   897	(Font)              <5> on input line 56.
   898	LaTeX Font Info:    External font `lmex10' loaded for size
   899	(Font)              <10.95> on input line 66.
   900	LaTeX Font Info:    Trying to load font information for OT1+lmss on input line 
   901	66.
   902	
   903	(/usr/local/texlive/2026/texmf-dist/tex/latex/lm/ot1lmss.fd
   904	File: ot1lmss.fd 2015/05/01 v1.6.1 Font defs for Latin Modern
   905	)
   906	Package microtype Info: Loading generic protrusion settings for font family
   907	(microtype)             `lmss' (encoding: OT1).
   908	(microtype)             For optimal results, create family-specific settings.
   909	(microtype)             See the microtype manual for details.
   910	 [1
   911	
   912	{/usr/local/texlive/2026/texmf-var/fonts/map/pdftex/updmap/pdftex.map}{/usr/loc
   913	al/texlive/2026/texmf-dist/fonts/enc/dvips/lm/lm-ec.enc}{/usr/local/texlive/202
   914	6/texmf-dist/fonts/enc/dvips/lm/lm-mathsy.enc}{/usr/local/texlive/2026/texmf-di
   915	st/fonts/enc/dvips/lm/lm-rm.enc}] [2{/usr/local/texlive/2026/texmf-dist/fonts/e
   916	nc/dvips/lm/lm-mathit.enc}] [3{/usr/local/texlive/2026/texmf-dist/fonts/enc/dvi
   917	ps/lm/lm-mathex.enc}] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15] [16
   918	] [17] [18]
   919	[19] [20] [21] [22] [23] [24] [25] [26] [27] [28] [29] [30] [31] [32] [33]
   920	[34] [35] [36]
   921	(/private/tmp/claude-501/-Users-mlong-Documents-Development-the-beast-system/53
   922	a4f9b6-b8c1-4df4-96d8-300f973de288/scratchpad/ip-build/ideological-power.aux)
   923	 ***********
   924	LaTeX2e <2025-11-01>
   925	L3 programming layer <2026-01-19>
   926	 ***********
   927	Package rerunfilecheck Info: File `ideological-power.out' has not changed.
   928	(rerunfilecheck)             Checksum: 176B9E8A59F505980886727E92B557A2;9611.
   929	 ) 
   930	Here is how much of TeX's memory you used:
   931	 26377 strings out of 467525
   932	 487338 string characters out of 5418982
   933	 926507 words of memory out of 5000000
   934	 54256 multiletter control sequences out of 15000+600000
   935	 753631 words of font info for 293 fonts, out of 8000000 for 9000
   936	 1141 hyphenation exceptions out of 8191
   937	 102i,13n,107p,1717b,855s stack positions out of 10000i,1000n,20000p,200000b,200000s
   938	</usr/local/texlive/2026/texmf-dist/fonts/type1/public/lm/lmbx10.pfb></usr/lo
   939	cal/texlive/2026/texmf-dist/fonts/type1/public/lm/lmbx12.pfb></usr/local/texliv
   940	e/2026/texmf-dist/fonts/type1/public/lm/lmex10.pfb></usr/local/texlive/2026/tex
   941	mf-dist/fonts/type1/public/lm/lmmi10.pfb></usr/local/texlive/2026/texmf-dist/fo
   942	nts/type1/public/lm/lmmi6.pfb></usr/local/texlive/2026/texmf-dist/fonts/type1/p
   943	ublic/lm/lmmi8.pfb></usr/local/texlive/2026/texmf-dist/fonts/type1/public/lm/lm
   944	r10.pfb></usr/local/texlive/2026/texmf-dist/fonts/type1/public/lm/lmr12.pfb></u
   945	sr/local/texlive/2026/texmf-dist/fonts/type1/public/lm/lmr17.pfb></usr/local/te
   946	xlive/2026/texmf-dist/fonts/type1/public/lm/lmr6.pfb></usr/local/texlive/2026/t
   947	exmf-dist/fonts/type1/public/lm/lmr8.pfb></usr/local/texlive/2026/texmf-dist/fo
   948	nts/type1/public/lm/lmri10.pfb></usr/local/texlive/2026/texmf-dist/fonts/type1/
   949	public/lm/lmss10.pfb></usr/local/texlive/2026/texmf-dist/fonts/type1/public/lm/
   950	lmss8.pfb></usr/local/texlive/2026/texmf-dist/fonts/type1/public/lm/lmsy10.pfb>
   951	</usr/local/texlive/2026/texmf-dist/fonts/type1/public/lm/lmsy6.pfb></usr/local
   952	/texlive/2026/texmf-dist/fonts/type1/public/lm/lmsy8.pfb></usr/local/texlive/20
   953	26/texmf-dist/fonts/type1/public/lm/lmtt10.pfb></usr/local/texlive/2026/texmf-d
   954	ist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>
   955	Output written on /private/tmp/claude-501/-Users-mlong-Documents-Development-th
   956	e-beast-system/53a4f9b6-b8c1-4df4-96d8-300f973de288/scratchpad/ip-build/ideolog
   957	ical-power.pdf (36 pages, 476809 bytes).
   958	PDF statistics:
   959	 1299 PDF objects out of 1440 (max. 8388607)
   960	 1119 compressed objects within 12 object streams
   961	 239 named destinations out of 1000 (max. 500000)
   962	 66445 words of extra memory for PDF output out of 74296 (max. 10000000)
   963	

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
    12	\usepackage{xcolor}
    13	\usepackage{tikz}
    14	\usepackage{booktabs,tabularx,array}
    15	\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
    16	\newcolumntype{Y}{>{\raggedright\arraybackslash}X}
    17	\usepackage[round,authoryear]{natbib}
    18	\usepackage[hidelinks]{hyperref}
    19	\usepackage{cleveref}
    20	
    21	\newtheorem{theorem}{Theorem}[section]
    22	\newtheorem{proposition}[theorem]{Proposition}
    23	\newtheorem{lemma}[theorem]{Lemma}
    24	\newtheorem{corollary}[theorem]{Corollary}
    25	\theoremstyle{definition}
    26	\newtheorem{definition}[theorem]{Definition}
    27	\newtheorem{assumption}[theorem]{Assumption}
    28	\theoremstyle{remark}
    29	\newtheorem{remark}[theorem]{Remark}
    30	
    31	\crefname{assumption}{Assumption}{Assumptions}
    32	
    33	% Pillar labels (sans serif) and shared objects; notation follows the series notation file.
    34	\newcommand{\pF}{\mathsf{F}}
    35	\newcommand{\pP}{\mathsf{P}}
    36	\newcommand{\pJ}{\mathsf{J}}
    37	\newcommand{\pI}{\mathsf{I}}
    38	\newcommand{\pC}{\mathsf{C}}
    39	\newcommand{\pW}{\mathsf{W}}
    40	\newcommand{\Pil}{\mathcal{M}}
    41	\newcommand{\Int}{\mathcal{I}}
    42	\newcommand{\Auth}{\mathcal{K}}
    43	\newcommand{\E}{\mathbb{E}}
    44	\newcommand{\Prob}{\Pr}
    45	
    46	\title{Ideological Power and Legitimation\\[4pt]
    47	  {\normalsize Part IV of \emph{The Six Pillars of the Beast System}}}
    48	\author{Matthew Long\\
    49	  \small The YonedaAI Collaboration, YonedaAI Research Collective\\
    50	  \small Chicago, IL\\
    51	  \small \texttt{matthew@yonedaai.com} $\cdot$ \url{https://yonedaai.com}}
    52	\date{October 2026}
    53	
    54	\begin{document}
    55	\maketitle
    56	
    57	\begin{abstract}
    58	Every governance system must settle who shapes the beliefs on which cooperation depends. This paper treats that question as the ideological pillar of a six-pillar model of governance and asks two things of it: whether the pillar is necessary, and when it becomes an instrument of capture. From a coordination axiom, together with membership turnover and the cross-cultural variability of rules, we derive that every persistent collective implements a recognition function: a recurring public practice that makes the operative rules common knowledge. The derivation establishes the necessity of a function, not of any institution, and it does not establish that belief in the rightness of rules is necessary. Stateless and egalitarian societies implement the function through talk, ridicule, ritual and kinship idiom, without a designated office. A Bayesian endorsement model then shows that a captured authority's endorsement carries no information, that independent authorities raise expected public confidence in sound rules and lower it for unsound ones, and that coordinated control of several authorities lowers the probability that an error is disclosed below the level reached by independent control with the same average independence. We compare how academia, religious institutions, media, schools and medical and scientific bodies hold the function in market-capitalist, communist party-state, social-democratic, Islamic, Catholic-monarchical and secular-democratic regimes, and we state hypotheses with falsifiers. The comparative codings are qualitative and drawn from secondary literature; no concentration or integration index is estimated for any real polity.
    59	\end{abstract}
    60	
    61	\section{Introduction}
    62	\label{sec:intro}
    63	
    64	Every polity has to answer the question of who shapes the beliefs. People cooperate under rules only when they know which rules are in force, which officials hold office, and what others expect of them. Those beliefs do not arise unaided. Someone teaches the young, recites the genealogy, preaches the sermon, accredits the physician, edits the newspaper, peer-reviews the article and announces the verdict. This paper studies that activity as one of six functions that, on the argument of this series, every functioning governance system performs.
    65	
    66	The series rests on a single claim: the ideology changes; the institutional functions remain. Six questions recur in every governance system. Who controls the resources ($\pF$)? Who makes the laws ($\pP$)? Who interprets them ($\pJ$)? Who shapes the beliefs ($\pI$)? Who enforces the rules ($\pC$)? Who produces the wealth that sustains everything ($\pW$)? The framework adapts the five-function Hierarchy of the Beast System developed by \citet{largo2026hbs}, whose rule function is split here into rule-making and adjudication. The name comes from Revelation 13, which describes a system binding authority, allegiance and economic participation. In this series the name designates the universal six-function structure itself. It is never a label for any religion, people, profession, regime or person.
    67	
    68	Proposition A of the series states that every functioning governance system contains the six functions together with dependency relations among them; Part VII proves it from axioms about collective life. Proposition B states that the functions become concentrated or coordinated so that independent accountability fails: unaccountable concentration $U_t$ and cross-pillar integration $\Int_t$ are both high and capture links are documented \citep{largo2026hbs}. Proposition A does not imply Proposition B, and Part VII proves the non-implication. The distinction matters for every pillar. The existence of a pillar is a structural fact; its capture is a contingent condition that must be measured.
    69	
    70	The ideological pillar poses these tasks in a sharp form. Its institutions include universities, churches, mosques and seminaries, newsrooms, schools, academies of science and medical bodies. These institutions command trust because they are expected to report what they find rather than what rulers prefer. They can check capture by disclosing errors and refusing endorsement. They can also enable capture by lending credibility to rules that serve a narrow coalition. Nothing in this paper implies that expertise, medicine, science or any faith is fraudulent. The source framework says plainly that a hospital is not a propaganda organ and a professor is not an agent of command \citep{largo2026hbs}. The analytical question is when the independence that gives these authorities their value is preserved, and when it is lost.
    71	
    72	Every persistent collective with membership turnover and locally variable rules implements a recurring public practice that makes its operative rules common knowledge (Theorem~\ref{thm:ideological-power:necessity}). Entrants do not know the local rules at entry, because rules vary across societies; coordination requires common knowledge of the rules, and private instruction cannot supply it (Lemma~\ref{lem:ideological-power:public-signal}). The derivation establishes the necessity of recognizing the rules. It does not establish the necessity of believing them rightful.
    73	
    74	Independent authorities raise public confidence in sound rules and lower it in unsound ones, while a captured authority's endorsement conveys no information (Proposition~\ref{prop:ideological-power:credibility}). When one coalition controls the appointment of several authorities, an error is less likely to be disclosed than when the same authorities are appointed independently with the same average independence (Proposition~\ref{prop:ideological-power:disclosure}). These results organize a comparison of six regime types and a set of hypotheses, each with a stated falsifier.
    75	
    76	The comparison asks how the universal function is distributed, not whether a regime has it. Every regime type has it. This is what makes the comparison even-handed by construction: a Catholic monarchy, an Islamic state, a party-state and a liberal democracy each have teachers, preachers, censors or editors, and accrediting bodies, and each can be asked the same questions about concentration, coupling and contestability.
    77	
    78	\section{The ideological layer of the multiplex network}
    79	\label{sec:layer}
    80	
    81	\subsection{Shared objects}
    82	
    83	We use the formal objects of the source framework without redefining them \citep{largo2026hbs}. The polity at time $t$ is a directed multiplex network $G_t=(V_t,E_t)$ whose nodes are organizations or coherent actor groups. The series has six layers $A^m_t$, one for each pillar $m\in\Pil=\{\pF,\pP,\pJ,\pI,\pC,\pW\}$, so $M=|\Pil|=6$. An edge weight $a^m_{ij,t}\in[0,1]$ records the documented capacity of actor $i$ to constrain a feasible action of actor $j$ through mechanism $m$. A many-to-many role map assigns actors to pillars. Each actor holds a control share $s^m_{i,t}$ of decision-relevant control in pillar $m$, with $\sum_i s^m_{i,t}=1$, and pillar concentration is the Herfindahl-Hirschman index $H_{m,t}=\sum_i (s^m_{i,t})^2$.
    84	
    85	Concentration is dangerous only where it escapes review, and the source framework measures review separately. Contestability $Q_{m,t}\in[0,1]$ summarizes transparency, appeal rights, independence, competition and credible replacement of decision makers. The illustrative index of unaccountable concentration is $U_t=\sum_m \omega_m H_{m,t}(1-Q_{m,t})$ with preregistered weights $\omega_m\geq 0$ summing to one.
    86	
    87	Integration across pillars is a separate quantity from concentration within them. Cross-pillar integration $C_{mn,t}\in[0,1]$ measures how far one coalition commands appointments, budgets, sanctions or agenda in both $m$ and $n$, and the integration statistic is
    88	\begin{equation}
    89	\label{eq:integration}
    90	\Int_t=\frac{2}{M(M-1)}\sum_{m<n} C_{mn,t}=\frac{1}{15}\sum_{m<n} C_{mn,t}.
    91	\end{equation}
    92	A capture link $(i\to j,m)$ is influence that meets three conditions: privileged access or discretion, a resulting weakening of applicable accountability or contestability, and material evidence tying the asymmetry to an institutional output. In the aggregate state vector $x_t=(F_t,P_t,J_t,I^{cap}_t,C_t,W_t)$ the ideological capacity is written $I^{cap}_t$. The pillar label is the sans-serif $\pI$ and the integration statistic is the calligraphic $\Int_t$; the two are never interchanged.
    93	
    94	For the ideological layer, an edge $a^{\pI}_{ij,t}$ records actor $i$'s documented capacity to constrain $j$ by shaping what $j$ or $j$'s audience believes about rules, officials or facts. Accrediting a university, licensing a physician, listing a book on an index of prohibited titles, issuing a juristic opinion on a ruler's decree, withdrawing a broadcast license and retracting an article are examples. Persuasion with no constraining capacity, such as an op-ed that readers may ignore at no cost, is not an edge in this layer.
    95	
    96	\subsection{Legitimation and legitimating authorities}
    97	
    98	Let $R_t$ denote the rule system in force in a collective at time $t$, in the sense of Definition 2.1 of Part II: the general prescriptions that members are expected to follow and that officials, where they exist, apply. The rule system includes rules that designate who holds office and rules that specify sanctions.
    99	
   100	\begin{definition}[Legitimation function]
   101	\label{def:ideological-power:legitimation}
   102	The \emph{legitimation function} of a collective is the class of practices that produce, transmit and validate the beliefs about $R_t$, about who holds authority under $R_t$, and about relevant facts, on which members' coordination depends. A practice belongs to the class if it regularly changes members' beliefs about these matters and if members rely on the changed beliefs when deciding whether to comply or cooperate.
   103	\end{definition}
   104	
   105	The definition names a function, not an institution. A campfire conversation, a liturgy, a curriculum, an evening news broadcast, a peer-reviewed journal and a pharmacopoeia can all belong to the class. Two contents of the function, which the literature often merges, need to be kept apart.
   106	
   107	\begin{definition}[Recognition and normative legitimacy]
   108	\label{def:ideological-power:recognition}
   109	A belief system supports \emph{recognition} of $R_t$ when members can identify which rules are in force and who is entitled to make, apply and enforce them. Following \citet{hart1961}, the criteria members use for this identification form the collective's \emph{rule of recognition}. A belief system supports \emph{normative legitimacy} when, in addition, members regard the rules or the officials as rightful, so that the reason for compliance includes that judgment and not only the expectation of sanction or the convenience of conformity.
   110	\end{definition}
   111	
   112	Hart introduced the rule of recognition as the remedy for the uncertainty of a regime of primary rules alone; the rules of change and of adjudication remedy its static character and its inefficiency \citep{hart1961}. In the series, Part II treats the rule of change, the procedure by which a collective alters its rules (Definition 3.6 of Part II), and Part III the rule of adjudication. This Part treats the rule of recognition, which is the minimal content of the ideological function. Normative legitimacy is the richer content that \citet{weber1978} analyzed in his types of legitimate domination; Part II applies those types to the question of who makes rules.
   113	
   114	\begin{definition}[Legitimating authority]
   115	\label{def:ideological-power:authority}
   116	A \emph{legitimating authority} is an actor whose public statements about $R_t$, about officials or about facts relevant to compliance move other members' beliefs, because members expect those statements to track the truth or the tradition rather than the speaker's interest. We write $\Auth_t$ for the set of legitimating authorities at time $t$.
   117	\end{definition}
   118	
   119	Clergy and ulama, teachers and universities, academies and journals, newsrooms, professional and medical associations, regulatory agencies in their certifying role, and the propaganda departments of ruling parties are legitimating authorities under this definition. The definition does not require that an authority be accurate; it requires that its audience treats it as tracking something other than its own interest. That expectation is the asset that capture spends.
   120	
   121	Healthcare and science enter this Part only in their knowledge-producing and standard-setting role. Clinical guidelines, drug approval, accreditation of medical schools and the publication of trial results shape what patients, physicians and governments believe. The delivery of care is production and belongs to Part VI. The cultural authority of medicine, which \citet{starr1982} traced in the United States, and the professional autonomy that \citet{freidson1970} analyzed are objects of this layer because they govern whose statements about health count.
   122	
   123	\subsection{Knowledge, common knowledge and public transmission}
   124	
   125	Coordination depends on more than each member knowing the rules. Each must know that the others know, and so on. The standard formalism makes the requirement precise \citep{lewis1969,aumann1976}.
   126	
   127	\begin{definition}[Knowledge and common knowledge]
   128	\label{def:ideological-power:public-signal}
   129	Let $\Omega$ be a set of states and $N$ a finite set of members. Each member $i\in N$ has an information partition $\mathcal{P}_i$ of $\Omega$; $\mathcal{P}_i(\omega)$ is the cell containing $\omega$. For an event $E\subseteq\Omega$, member $i$ \emph{knows} $E$ at $\omega$ if $\mathcal{P}_i(\omega)\subseteq E$, and $K_iE=\{\omega:\mathcal{P}_i(\omega)\subseteq E\}$. Write $K E=\bigcap_{i\in N}K_iE$ for mutual knowledge. The event $E$ is \emph{common knowledge} at $\omega$ if $\omega\in K^nE$ for every $n\geq 1$, where $K^1E=KE$ and $K^{n+1}E=K(K^nE)$. An event $F$ is \emph{public} (evident to all) if $F\subseteq K_iF$ for every $i\in N$: whenever $F$ occurs, every member knows that it has occurred. A transmission of $R_t$ is \emph{public} if it generates a public event $F$ with $F\subseteq K_iE$ for every $i$, where $E$ is the event that $R_t$ is in force; otherwise it is \emph{private}.
   130	\end{definition}
   131	
   132	Rituals, assemblies and broadcasts that everyone watches together are the familiar sources of public events. \citet{chwe2001} argued that a central purpose of ritual and public ceremony is to generate common knowledge, and \citet{schelling1960} showed how shared salience selects among equilibria of coordination games. The following lemma states the logical core.
   133	
   134	\begin{lemma}[Public and private transmission]
   135	\label{lem:ideological-power:public-signal}
   136	Let $E\subseteq\Omega$ be an event.
   137	\begin{enumerate}
   138	\item[(a)] If $F$ is a public event and $F\subseteq K_iE$ for every $i\in N$, then $E$ is common knowledge at every $\omega\in F$.
   139	\item[(b)] Conversely, if $E$ is common knowledge at $\omega$, then the set $F^\ast$ of states at which $E$ is common knowledge is a public event containing $\omega$, and $F^\ast\subseteq K_iE$ for every $i$.
   140	\item[(c)] Mutual knowledge does not imply common knowledge: there are partitions and a state at which every member knows $E$ but some member does not know that another knows $E$.
   141	\end{enumerate}
   142	\end{lemma}
   143	
   144	\begin{proof}
   145	Each operator $K_i$ is monotone: if $A\subseteq B$ then $K_iA\subseteq K_iB$, because a cell contained in $A$ is contained in $B$.
   146	
   147	(a) We show $F\subseteq K^nE$ for all $n$ by induction. For $n=1$, $F\subseteq K_iE$ for every $i$ gives $F\subseteq KE$. Suppose $F\subseteq K^nE$. For each $i$, publicity and monotonicity give $F\subseteq K_iF\subseteq K_i(K^nE)$. Intersecting over $i$ yields $F\subseteq K^{n+1}E$.
   148	
   149	(b) Let $F^\ast=\bigcap_{n\geq1}K^nE$. Since $K^1E\subseteq K_iE$, $F^\ast\subseteq K_iE$. Take $\omega'\in F^\ast$ and any $i$. For each $n$, $\omega'\in K^{n+1}E\subseteq K_i(K^nE)$, so $\mathcal{P}_i(\omega')\subseteq K^nE$ for every $n$, hence $\mathcal{P}_i(\omega')\subseteq F^\ast$. Thus $\omega'\in K_iF^\ast$, and $F^\ast$ is public.
   150	
   151	(c) Let $\Omega=\{\omega_1,\omega_2,\omega_3\}$, $N=\{1,2\}$ and $E=\{\omega_1,\omega_2\}$. Member 1 is told privately whether $E$ holds: $\mathcal{P}_1=\{\{\omega_1,\omega_2\},\{\omega_3\}\}$. Member 2 is told only at $\omega_1$: $\mathcal{P}_2=\{\{\omega_1\},\{\omega_2,\omega_3\}\}$. At $\omega_1$ both members know $E$. But $K_2E=\{\omega_1\}$ and $K_1K_2E=\emptyset$, because member 1's cell $\{\omega_1,\omega_2\}$ is not contained in $\{\omega_1\}$. Member 1 knows the rule but does not know that member 2 knows it.
   152	\end{proof}
   153	
   154	Part (b) is a form of Aumann's characterization of common knowledge \citep{aumann1976}. Together, (a) and (b) say that common knowledge of the rules is available exactly when some public event certifies them. Part (c) shows why private instruction, however thorough, does not suffice. A teacher who instructs each pupil separately produces knowledge; an assembly in which pupils see one another being instructed produces common knowledge.
   155	
   156	\begin{remark}
   157	Common knowledge is an idealization. \citet{rubinstein1992} showed in the electronic mail game that any finite number of levels of mutual knowledge can fail to support coordination that common knowledge would support. \citet{monderer1989} showed that an approximate notion, common $p$-belief, restores continuity: equilibria that require common knowledge are approximated by equilibria under common $p$-belief for $p$ close to one. The arguments below go through with public events replaced by events that each member believes with probability at least $p$ whenever they occur. We state them for common knowledge to keep the logic visible.
   158	\end{remark}
   159	
   160	\subsection{Concentration and contestability in the ideological layer}
   161	
   162	The control share $s^{\pI}_{i,t}$ is a share of decision-relevant control over authoritative outputs: appointment and removal of authorities, accreditation and licensing, the content of curricula, approval of doctrinal or scientific standards, and the reach of broadcast and print channels. Belief itself is not a fixed quantity to be divided, so $s^{\pI}$ is defined over these outputs and not over minds. Concentration $H^{\pI}_t:=H_{\pI,t}$ is high when one organization appoints the clergy, writes the curriculum, licenses the presses and certifies the professions; it is low when these decisions are spread across organizations with separate appointment and funding.
   163	
   164	\begin{definition}[Components of ideological contestability]
   165	\label{def:ideological-power:qi}
   166	The ideological contestability $Q^{\pI}_t:=Q_{\pI,t}$ is a preregistered aggregate, with values in $[0,1]$, of five components:
   167	(i) \emph{plurality}: the number and audience reach of legitimating authorities whose appointment and funding are independent of one another;
   168	(ii) \emph{independence}: tenure protection, editorial autonomy, academic freedom and juristic or doctrinal autonomy of authorities from the governing coalition;
   169	(iii) \emph{disclosure}: publication of the funding, sponsorship and conflicts of interest of authorities;
   170	(iv) \emph{reviewability}: procedures by which an authority's statements can be challenged, replicated, corrected or retracted, including peer review, rights of reply and public correction;
   171	(v) \emph{exit}: the ability of audiences to turn to rival authorities without legal or material sanction, the ideological case of exit in Hirschman's sense, leaving an organization rather than voicing complaint within it, which Part VI defines (Definition 2.5 of Part VI).
   172	\end{definition}
   173	
   174	The components are not new. They restate the source framework's contestability for the ideological layer and match the checks it lists for its knowledge mechanism: independent epidemiology, investigative reporting, protected academic freedom and professional resistance \citep{largo2026hbs}. Their value lies in making the aggregate auditable: each component can be coded from documents, and a disagreement about $Q^{\pI}$ can be traced to a disagreement about one of them.
   175	
   176	Ideological concentration alone cannot produce a strong classification under the source criterion, which needs both high $U_t$ and high $\Int_t$. The bound is elementary but worth stating. If every pair not involving $\pI$ has $C_{mn,t}=0$, then by \eqref{eq:integration} $\Int_t=\frac{1}{15}\sum_{n\neq\pI}C_{\pI n,t}\leq 5/15=1/3$. A polity whose governing coalition controls every belief-producing institution but none of the other five pillars shows ideological fusion, not system-wide integration. Capture of belief becomes system-wide only through coupling to appointments, budgets or sanctions in other pillars, which is why Section~\ref{sec:mechanisms} studies the couplings.
   177	
   178	The value of a single authority to its audience depends on how independent it is of whoever controls it. Section~\ref{sec:mechanisms} models this dependence with an independence parameter $\lambda\in[0,1]$, the probability that an authority reports its own findings rather than the position of a controlling coalition. The components of $Q^{\pI}$ are the institutional means of raising $\lambda$.
   179	
   180	\section{Necessity of the legitimation function}
   181	\label{sec:necessity}
   182	
   183	\subsection{Assumptions}
   184	
   185	The series derives each pillar from an axiom about collective life. Part VII owns the axiom set and proves the general necessity theorem. The ideological pillar rests on the coordination axiom. We state it with the auxiliary assumptions that the derivation needs, and we mark which assumptions are empirical.
   186	
   187	Fix a collective $G$ with members $N_t$ at time $t$ and rule system $R_t$. Say that $G$ \emph{functions} at $t$ if members cooperate on the basis of $R_t$: they comply with its rules and recognize its office holders at least often enough for the collective to make and carry out collective decisions. Let $E_t\subseteq\Omega$ be the event that $R_t$ is the rule system in force at $t$. Information changes over time, so member $i$ has a partition $\mathcal{P}_{i,s}$ and knowledge operator $K_{i,s}$ at each date $s$. Write $\tau_i$ for $i$'s entry date. For $s<\tau_i$ we set $\mathcal{P}_{i,s}=\{\Omega\}$, the trivial partition: before entry a person knows nothing about the local rules beyond what is true in every state. Common knowledge at date $s$ means common knowledge under the date-$s$ partition profile $(\mathcal{P}_{j,s})_j$.
   188	
   189	\begin{assumption}[Ax4, coordination]
   190	\label{ax:coordination}
   191	If $G$ functions at $t$, then there is a set $N^\ast_t\subseteq N_t$ of members, large enough that cooperation among them sustains the collective, such that $E_t$ is common knowledge among $N^\ast_t$ at the true state at date $t$.
   192	\end{assumption}
   193	
   194	\begin{assumption}[Turnover]
   195	\label{ax:turnover}
   196	There is a horizon $L$ such that for every $t$ at least one member of $N^\ast_{t+L}$ entered the collective during $[t,t+L]$.
   197	\end{assumption}
   198	
   199	\begin{assumption}[Non-innateness]
   200	\label{ax:noninnate}
   201	At entry, an entrant cannot tell which rule system will be in force at any later date: for every entrant $e$, every date $s\geq\tau_e$ and the true state $\omega$, $\mathcal{P}_{e,\tau_e}(\omega)\not\subseteq E_s$.
   202	\end{assumption}
   203	
   204	The coordination axiom is the series' Ax4 in the precise form that \citet{lewis1969} gave to conventions: a convention is a regularity sustained because it is common knowledge that others conform. Turnover is universal in human collectives, whose members are born and die, marry in and out, and join and leave; the assumption adds only that some entrants join the cooperating core within a bounded time. Non-innateness is an empirical claim with strong support. Rule systems differ widely across human societies, as every ethnography in Table~\ref{tab:minimal} shows, so an entrant cannot read the local rules off a genetic or otherwise fixed endowment. The assumption fails for social insects, whose coordination rules are largely fixed by development, and that failure marks the scope of the theorem.
   205	
   206	\begin{lemma}[Renewal]
   207	\label{lem:ideological-power:renewal}
   208	Under Assumptions~\ref{ax:turnover} and \ref{ax:noninnate}, for every $t$ there is a member $e\in N^\ast_{t+L}$ with $t\leq\tau_e\leq t+L$ who does not know $E_{t+L}$ at date $\tau_e$.
   209	\end{lemma}
   210	
   211	\begin{proof}
   212	Assumption~\ref{ax:turnover} supplies $e\in N^\ast_{t+L}$ with $\tau_e\in[t,t+L]$. Since $t+L\geq\tau_e$, Assumption~\ref{ax:noninnate} gives $\mathcal{P}_{e,\tau_e}(\omega)\not\subseteq E_{t+L}$, that is $\omega\notin K_{e,\tau_e}E_{t+L}$.
   213	\end{proof}
   214	
   215	Renewal can also arise without entry. If the rule system changes within the window through the rule of change, the procedure by which a collective alters its rules (Definition 3.6 of Part II), and the change was not announced before the window began, then some member did not know the new rule system at the window's start. The theorem below holds with that case in place of Assumptions~\ref{ax:turnover} and \ref{ax:noninnate}.
   216	
   217	\subsection{The necessity lemma}
   218	
   219	\begin{theorem}[Necessity of recognition]
   220	\label{thm:ideological-power:necessity}
   221	Let $G$ satisfy Assumptions~\ref{ax:coordination}, \ref{ax:turnover} and \ref{ax:noninnate} and function at every date of an interval longer than $L$. Then within every window $[t,t+L]$ inside the interval:
   222	\begin{enumerate}
   223	\item[(i)] the partition of at least one member $e\in N^\ast_{t+L}$ is refined between $\tau_e$ and $t+L$ by information bearing on the rule system, from a cell not contained in $E_{t+L}$ to a cell contained in it; and
   224	\item[(ii)] the partition profile of $N^\ast_{t+L}$ changes during the window from one under which $E_{t+L}$ is not common knowledge at the true state to one under which it is, so that at date $t+L$ there is an event, public under the date-$(t+L)$ profile, that contains the true state and is contained in $\bigcap_{i\in N^\ast_{t+L}}K_{i,t+L}E_{t+L}$.
   225	\end{enumerate}
   226	The practices that produce these refinements belong to the legitimation function of Definition~\ref{def:ideological-power:legitimation}. Hence the legitimation function is implemented in $G$, at least in the form of recognition.
   227	\end{theorem}
   228	
   229	\begin{proof}
   230	Fix a window $[t,t+L]$ inside the interval and let $\omega$ be the true state. By Assumption~\ref{ax:coordination}, $E_{t+L}$ is common knowledge among $N^\ast_{t+L}$ at $\omega$ at date $t+L$. By Lemma~\ref{lem:ideological-power:public-signal}(b), applied to the date-$(t+L)$ profile, the set $F^\ast$ of states at which $E_{t+L}$ is common knowledge under that profile is public under it, contains $\omega$, and satisfies $F^\ast\subseteq K_{i,t+L}E_{t+L}$ for every $i\in N^\ast_{t+L}$.
   231	
   232	By Lemma~\ref{lem:ideological-power:renewal}, some $e\in N^\ast_{t+L}$ with $\tau_e\in[t,t+L]$ has $\omega\notin K_{e,\tau_e}E_{t+L}$. Since $\omega\in F^\ast\subseteq K_{e,t+L}E_{t+L}$, $e$'s cell at $\omega$ shrank between $\tau_e$ and $t+L$ from a set not contained in $E_{t+L}$ to a set contained in it, which is (i).
   233	
   234	Under the date-$\tau_e$ profile, $E_{t+L}$ is not common knowledge among $N^\ast_{t+L}$ at $\omega$, because $e$ does not know it and common knowledge implies mutual knowledge. Under the date-$(t+L)$ profile it is, with $F^\ast$ as the certifying public event. The change lies entirely in the refinement of members' partitions within the window, which is (ii). The practices that produced the refinement regularly change members' beliefs about the rule system, and members rely on the resulting common knowledge to coordinate, which is the defining property in Definition~\ref{def:ideological-power:legitimation}. Since the argument applies to every window of length $L$, such practices recur.
   235	\end{proof}
   236	
   237	The theorem is modest in its mathematics and specific in its content. Its mathematical core is the characterization of common knowledge by public events. Its empirical content sits in the three assumptions, all of which the proof uses, which is where the series' standard of proof requires it to sit: the necessity claim is derived from stated premises about collective life, and it can fail if the premises fail. Part VII states the general theorem for all six pillars and the non-implication of Proposition B; the present result is the pillar-level piece for $\pI$.
   238	
   239	\begin{remark}[What the theorem does not show]
   240	\label{rem:ideological-power:scope}
   241	The theorem shows that recognition is necessary. It does not show that normative legitimacy is necessary. A collective in which members know which rules are in force and comply from fear or habit satisfies every assumption above. Comparative research on autocracies treats legitimation as one of three supports of stable rule, alongside repression and co-optation, and finds that the mix varies \citep{gerschewski2013}. \citet{wintrobe1998} modeled dictators who trade off loyalty against repression, and \citet{weber1978} acknowledged that obedience can rest on fear or interest as well as on belief in legitimacy. Normative legitimacy is a frequent and valuable content of the ideological function, but it is a contingent one. This narrowing matters for the comparison: a regime with low normative legitimacy still has a fully implemented ideological pillar, because it still must make its rules, sanctions and officials common knowledge.
   242	\end{remark}
   243	
   244	\subsection{Minimal forms in stateless and consensus societies}
   245	
   246	The strongest test of a necessity claim is the set of societies described as having no state, no chiefs with coercive power, or radical equality. The theorem predicts that each implements recognition through some public practice, even with no designated office.
   247	
   248	\begin{proposition}[Minimal form; empirical]
   249	\label{prop:ideological-power:minimal-form}
   250	In each of the stateless, egalitarian or consensus-based societies of Table~\ref{tab:minimal}, the legitimation function is implemented by public practices without a designated office, and decision-relevant control over those practices is widely dispersed, so that $H^{\pI}$ is low and $Q^{\pI}$ is high.
   251	\end{proposition}
   252	
   253	This is an empirical proposition, supported by the ethnographic record rather than proved. The support is summarized in Table~\ref{tab:minimal} and discussed below.
   254	
   255	\begin{table}[t]
   256	\centering
   257	\small
   258	\caption{Minimal forms of the legitimation function in stateless and egalitarian societies. Each row names the public practices that make rules and expectations common knowledge and the strongest reading that the function is absent.}
   259	\label{tab:minimal}
   260	\begin{tabularx}{\textwidth}{@{}L{2.4cm}YY@{}}
   261	\toprule
   262	Case & Public practices that carry recognition & Strongest counter-reading and reply \\
   263	\midrule
   264	Ju/'hoansi & Camp talk, joking and criticism heard by all, the leveling custom of insulting the meat, and the healing dance \citep{lee1979,lee2013,marshall1976,wiessner2005} & No office holds authority. Reply: the function is carried by talk that everyone hears, which is exactly a public event. \\
   265	Nuer & Lineage idiom shared across segments, ritual specialists whose standing is religious rather than political, and prophets \citep{evanspritchard1940} & Evans-Pritchard stressed the absence of government. Reply: the function is present while the office is absent. \\
   266	Amazonian chiefdoms & The chief's duty of public speech, which recalls traditional norms, and myth shared by the group \citep{clastres1987} & The chief commands nothing. Reply: the chief's speech is a public recitation of norms without power to command. \\
   267	Mobile foragers & Moral talk and gossip that circulate shared norms and identify would-be dominators \citep{boehm1999,boehm2012} & Equality might seem to require no shared ideology. Reply: the egalitarian ethos is itself a shared and enforced belief. \\
   268	Immediate-return societies & Public leveling practices such as obligatory sharing and mockery of self-promotion \citep{woodburn1982} & Ritual is egalitarian and unspecialized. Reply: unspecialized is not absent. \\
   269	Commons users & Rules known to appropriators, collective-choice meetings and public monitoring \citep{ostrom1990} & Users may coordinate by self-interest alone. Reply: Ostrom's design principles include rules that users know and can change. \\
   270	\bottomrule
   271	\end{tabularx}
   272	\end{table}
   273	
   274	The Ju/'hoansi are the case most often cited as lacking hierarchy. Their norms of sharing, modesty and restraint are sustained by talk. \citet{wiessner2005} recorded conversations in Ju/'hoansi camps and found that criticism of norm violations was mostly verbal and directed at behavior such as stinginess and self-aggrandizement. Talk in a small camp has the structure of a public event: speakers and listeners are co-present, and each sees who else hears. \citet{lee1979} and \citet{lee2013} describe the custom of deprecating a successful hunter's kill, which teaches the hunter and everyone listening that boasting will not be tolerated. No one holds an office of teacher or censor. The function is distributed across the whole adult population, so $H^{\pI}$ is close to its minimum and exit to another camp keeps $Q^{\pI}$ high.
   275	
   276	The Nuer were described by \citet{evanspritchard1940} as an ordered anarchy without government. The ideological function is present in the lineage idiom that tells every Nuer how segments relate and which obligations follow, and in ritual specialists such as the leopard-skin chief, whose standing derived from a ritual relation to the earth rather than from any power to command. The case confirms that the function can exist without an office that issues orders.
   277	
   278	\citet{clastres1987} described Amazonian chiefs whose authority rested on generosity and speech. The chief's daily discourse recalls the traditional norms of the group; it is a public recitation, not a command, and a chief who tries to command loses his following. Clastres read these societies as actively preventing the political function from separating from society. The reading is consistent with Theorem~\ref{thm:ideological-power:necessity}: the function exists, its holder has no power to enforce it, and concentration is prevented by design. Clastres' evidence has been criticized as selective, and the case should be read with that caution.
   279	
   280	\citet{boehm1999} argued that mobile foragers maintain equality through a reverse dominance hierarchy in which the group as a whole suppresses would-be dominators by gossip, ridicule, ostracism and, in extreme cases, killing. The sanctions belong to Part V. The shared moral understanding that identifies what counts as domination belongs here. \citet{woodburn1982} made the parallel point for immediate-return societies: equality there is an institutional outcome produced by leveling practices, not the absence of institutions.
   281	
   282	\citet{ostrom1990} showed that long-enduring commons are governed by rules that users know, can modify and monitor. The design principles are institutional, not ideological, but each presupposes that the operative rules are common knowledge among appropriators. \citet{graeber2021} added that some societies alternated seasonally between hierarchical and egalitarian arrangements, each publicly marked. Their claims are contested and are cited here only for the narrow point that political arrangements were publicly recognized as such.
   283	
   284	These cases come with standard caveats. Contact-era ethnography observed groups in marginal environments, sometimes idealized them, and generalized from few cases \citep{kelly1995}. None of these caveats affects the narrow claim of Proposition~\ref{prop:ideological-power:minimal-form}. Each caveat would matter if the claim were that these societies show the original condition of humanity; the claim is only that they show the function without the office.
   285	
   286	\subsection{Counterexample attempts}
   287	
   288	The most serious attempt to defeat the necessity claim is coordination by force alone. On this view a sufficiently strong coercive apparatus needs no shared beliefs; it needs soldiers and prisons. The reply is that force itself depends on common knowledge. A sanction rule deters only if the people it targets know it, and a coercive organization holds together only if its members expect one another to carry out orders. \citet{kuran1991} showed that regimes resting on public displays of support can collapse suddenly when private opposition becomes common knowledge, which is evidence that rulers depend on controlling what is common knowledge even when they rely on force. \citet{svolik2012} treats the control of information among elites as a central problem of authoritarian rule. The attempt fails for recognition. It succeeds against a stronger thesis, that normative legitimacy is necessary, which Remark~\ref{rem:ideological-power:scope} has already abandoned.
   289	
   290	A second attempt holds that markets coordinate through prices without shared beliefs. Prices do economize on information. But exchange presupposes common knowledge of property conventions: who owns what, what counts as payment, and which contracts are binding. Those conventions are part of $R_t$, and they are taught, displayed and defended. \citet{hayek1973} himself stressed that the order of a market society rests on rules of just conduct that people follow without being able to state them; following a rule one cannot state is compatible with common knowledge of the practice it supports.
   291	
   292	A third attempt notes that in a small face-to-face group everyone observes everyone, so common knowledge arises from co-presence without any practice designed to produce it. This is correct and is the minimal form, not a counterexample. Co-present talk is a practice that produces public events.
   293	
   294	A fourth attempt points to coordination without beliefs in animal societies. The non-innateness assumption excludes it, and the exclusion is principled: where rules are fixed by development, no transmission is needed. The theorem is a claim about human governance, where rules vary.
   295	
   296	The falsifier follows from the assumptions. The necessity claim would be refuted by a persistent human collective, with turnover and with rules that differ from its neighbors', in which entrants come to coordinate on the local rules without any practice that informs them of the rules and without any public event that certifies them. We know of no such case in the sources reviewed.
   297	
   298	\subsection{Function and institution}
   299	
   300	Two classic errors of functionalism must be avoided. \citet{hempel1959} showed that from the premise that a function is needed one cannot infer that a particular institution exists, because functional equivalents may meet the need. Theorem~\ref{thm:ideological-power:necessity} respects this limit: it asserts that some practice in a class is implemented, and the class includes campfire talk and state broadcasting alike. \citet{elster1983} argued that explaining an institution by its beneficial effects requires a feedback mechanism from effect to institution. The theorem is not such an explanation. It is a condition of persistence: collectives that lack the function do not function, whatever the reason the function arose. It does not explain why a given regime has a ministry of religious affairs or a public broadcaster, and the comparative sections never use it for that purpose. \citet{merton1968} supplies the remaining vocabulary: the manifest function of a university is teaching and research, and its latent function in the ideological layer may include certifying elites, which is a separate empirical question.
   301	
   302	\section{Literature on ideological power}
   303	\label{sec:literature}
   304	
   305	\subsection{Consent and coercion}
   306	
   307	The modern study of ideological power begins with the observation that rule rests on consent as well as force. \citet{gramsci1971} called the organization of consent through civil society hegemony and argued that in societies with dense churches, schools, associations and presses, rulers depend on these institutions as much as on the state's coercive apparatus. \citet{althusser1971} sharpened the contrast into a distinction between repressive and ideological state apparatuses, the latter including churches, schools, families, the media and cultural institutions, and he argued that in mature capitalism the school had displaced the church as the dominant ideological apparatus. Both accounts treat ideological institutions as functional supports of a ruling class. That functional reading is precisely what \citet{elster1983} criticized, and it is what the present paper avoids: we claim the necessity of a function, not that any given apparatus exists because it serves a class.
   308	
   309	\citet{weber1978} placed belief at the center of domination by distinguishing traditional, charismatic and rational-legal grounds of legitimacy. Part II uses the Weberian types to analyze who makes rules. This Part takes from Weber only the distinction between compliance grounded in belief and compliance grounded in fear or interest, which becomes the distinction between normative legitimacy and recognition in Definition~\ref{def:ideological-power:recognition}.
   310	
   311	\subsection{Faces of power and networks of meaning}
   312	
   313	\citet{bachrach1962} argued that power is exercised not only in decisions but also in non-decisions, by keeping issues off the agenda. \citet{lukes2005} added a third dimension: the power to shape preferences so that conflicts of interest never surface. Part II owns agenda control, the power to determine which proposals reach a decision, as an object of rule-making (Definition 2.9 of Part II). The third dimension belongs here, because shaping preferences is shaping beliefs. The difficulty Lukes acknowledged is measurement: claims about preferences that people would hold but for ideological influence require a counterfactual that is hard to observe. The endorsement model of Section~\ref{sec:mechanisms} sidesteps the problem by studying a narrower and observable quantity, the information content of an authority's statements.
   314	
   315	\citet{mann1986,mann1993} gave the most developed comparative-historical account. He distinguished ideological, economic, military and political networks of power and treated none as primary. Ideological power, in his account, derives from the human need for meaning, norms and aesthetic and ritual practice, and it can be transcendent, organizing a community across political boundaries as the world religions did, or immanent, reinforcing the morale of an existing group. Mann's framework is the closest predecessor of the six-pillar model. It lacks a separate judicial pillar and a separate pillar for the producing population, and it has no measure of capture; Part VII compares the frameworks in detail. Its value here is the distinction between transcendent and immanent ideological power, which maps onto the difference between authorities whose appointment and revenue lie outside the polity, such as a transnational church, and authorities created by the polity itself.
   316	
   317	\citet{bourdieu1989,bourdieu1991} described symbolic power as the power to constitute the given by stating it, effective to the degree that it is misrecognized as something other than power. His account of the convertibility of economic, cultural and symbolic capital anticipates the cross-pillar coupling $C_{\pF\pI}$, which Part I treats as its pair. \citet{bourdieu1977} applied the account to schooling, arguing that educational systems reproduce class structure while appearing meritocratic.
   318	
   319	\subsection{The public sphere and the media}
   320	
   321	\citet{habermas1989} traced the rise of a bourgeois public sphere of rational-critical debate in eighteenth-century Europe and its later refeudalization, as mass media and organized interests turned a reasoning public into an audience. \citet{fraser1990} argued that the bourgeois public sphere excluded women, workers and others, who formed subaltern counterpublics of their own. Both accounts bear on the plurality component of $Q^{\pI}$: a public sphere is contestable to the degree that counterpublics can form and be heard.
   322	
   323	The political economy of the media divides on the question of supply and demand. \citet{herman1988} proposed a propaganda model in which ownership, advertising, reliance on official sources, organized flak and a dominant ideology filter news in favor of elite interests. The model predicts that owner and advertiser interests shape content. \citet{gentzkow2006} showed instead that slant can arise from demand: outlets that wish to appear accurate tilt reports toward their audience's prior beliefs, so slant can exist without any owner's design. \citet{djankov2003} assembled cross-country data on media ownership and found that the largest media firms were typically controlled by governments or by private families, and that state ownership was associated with weaker press freedom and political rights. \citet{besley2006} modeled media capture by government and showed that capture is harder when there are more independent outlets and when bribing them is costly, which links plurality directly to accountability. \citet{hallin2004} classified Western media systems into liberal, democratic corporatist and polarized pluralist models, differing in the strength of commercial media, the degree of political parallelism, journalistic professionalization and the role of the state.
   324	
   325	Persuasion effects are measurable. \citet{dellavigna2007} exploited the staggered entry of a cable news channel into United States towns and found an effect on presidential vote shares. \citet{enikolopov2011} found that access to the one national television channel independent of the government in Russia's 1999 parliamentary election reduced votes for the government's party and raised votes for opposition parties. These studies establish that the ideological layer has real edges: control of a channel changes political behavior.
   326	
   327	Authoritarian information control has its own literature. \citet{king2013} analyzed censorship of Chinese social media and found that posts criticizing the state were often left standing while posts with potential for collective action were removed. \citet{stockmann2013} found that commercialized Chinese media were perceived as more credible than official outlets and could therefore carry the party's messages more persuasively. \citet{guriev2019,guriev2022} described a shift from rule by fear to rule by spin, in which leaders manipulate information while simulating democratic forms; Part II treats this as a strategy of rule-makers. \citet{kuran1991} analyzed preference falsification, in which citizens publicly support regimes they privately oppose, and explained why the revolutions of 1989 surprised observers.
   328	
   329	Digital platforms add a layer of intermediaries between authorities and audiences. \citet{gillespie2019} argued that moderation of what users may post is not incidental to platforms but constitutive of them, so platform firms make continual decisions about which speech reaches whom. \citet{allcott2017} found that fabricated news stories circulated widely on social media before the 2016 United States election, while estimated exposure per adult was modest. \citet{guess2023} replaced the algorithmic feeds of consenting Facebook and Instagram users with reverse-chronological feeds for three months during the 2020 campaign and found large changes in what users saw but no detectable change in polarization or political attitudes. \citet{roberts2018} showed that Chinese censorship works less through fear than through friction and flooding, which make unwanted information costly to find rather than impossible. Platforms are thus channels whose control shares and contestability can be coded like those of broadcasters, with the difference that ranking and moderation decisions are made at very large scale by few organizations.
   330	
   331	\subsection{Professions and expert authority}
   332	
   333	Professions convert knowledge into authority. \citet{larson1977} described the professional project as an effort to secure market closure and social standing through control of training and credentials. \citet{abbott1988} treated professions as competitors for jurisdiction over tasks. \citet{freidson1970} argued that medicine's autonomy, its control over the content of its own work, made it the model profession, and \citet{starr1982} traced how American medicine converted cultural authority into economic power and professional sovereignty. These accounts explain why expert authority is valuable to rulers: experts certify that a rule is sound in terms the public trusts.
   334	
   335	Evidence on sponsorship qualifies that trust without destroying it. \citet{bekelman2003} reviewed studies of financial conflicts of interest in biomedical research and found that industry sponsorship was associated with conclusions favorable to sponsors. \citet{lexchin2003} reached a similar conclusion for pharmaceutical sponsorship, and the Cochrane review by \citet{lundh2017} found that industry-sponsored drug and device studies more often reported favorable results and conclusions than studies with other sponsors. \citet{oreskes2010} documented campaigns in which a small number of scientists, with industry support, manufactured doubt about the harms of tobacco and about environmental science. Against these findings stand accounts of why science remains trustworthy. \citet{oreskes2019} located the reliability of science in its social process of critical vetting by a diverse community, and \citet{carpenter2010} showed that the United States Food and Drug Administration built autonomy on its reputation for scientific judgment. \citet{slaughter2004} documented the growing market orientation of universities, which raises the coupling between the financial and ideological pillars. Read together, this literature supports the model of Definition~\ref{def:ideological-power:endorsement}: expert authorities are informative to the degree that their judgments are independent of their sponsors, and institutions such as disclosure, review and reputation exist to secure that independence.
   336	
   337	\subsection{Religion and the state}
   338	
   339	The relation between religious authority and political rule is the oldest problem of the ideological pillar. \citet{stepan2000} proposed the twin tolerations as the condition for democracy: elected institutions free from religious veto, and religious citizens free to worship and to advance their views in public. \citet{casanova1994} documented the deprivatization of religion, its return to public life in several countries from the 1980s. \citet{philpott2007} argued that religious actors' political behavior depends on their institutional independence from the state and on their political theology. \citet{fox2008} coded religion-state arrangements worldwide. \citet{kuru2009} distinguished passive secularism, which allows public religious expression, from assertive secularism, which excludes it.
   340	
   341	Two debates concern Islamic and Catholic polities directly. \citet{kuru2019} argued that an alliance between ulama and the state, formed in the eleventh century, helps explain authoritarianism and underdevelopment in many Muslim-majority countries. \citet{rubin2017} argued that rulers who depended on religious authorities for legitimacy faced different incentives from rulers who depended on economic elites, and that the difference shaped economic divergence. Both arguments are contested, and the series cites them as positions, not settled findings. For Catholic Europe, \citet{grzymala2023} argued that the medieval Church served as a template and rival for state building, and \citet{grzymala2015} showed that churches whose moral authority is fused with national identity can shape policy through institutional access rather than partisan politics.
   342	
   343	\subsection{Relation to prior work}
   344	
   345	Coordination theory \citep{lewis1969,schelling1960,aumann1976,chwe2001} explains why some practice must make rules common knowledge. The political economy of media and expertise \citep{besley2006,gentzkow2006,carpenter2010} explains why the value of a statement depends on the independence of its source. Comparative work on religion, media and education describes how the institutions vary. No existing framework combines the three: none derives the function from an axiom, states when its institutions check or enable capture, and compares regimes on the same measures. The source framework provides the measures \citep{largo2026hbs}. The present paper adds the derivation and the pillar-level model and applies both to six regime types.
   346	
   347	\section{Comparative analysis across six regime types}
   348	\label{sec:comparative}
   349	
   350	Every regime type implements the ideological function; they differ in which institutions hold it, how tightly one coalition controls their appointments and revenue, and which other pillars that coalition also commands. The comparison below codes these differences qualitatively from secondary sources. No numerical value of $H^{\pI}$, $Q^{\pI}$, $U_t$ or $\Int_t$ is reported for any polity, because no preregistered coding exists.
   351	
   352	The couplings of the ideological pillar to finance, rule-making and adjudication ($C_{\pF\pI}$, $C_{\pP\pI}$, $C_{\pJ\pI}$) are analyzed primarily in Parts I, II and III; this paper treats the couplings to coercion and production ($C_{\pI\pC}$, $C_{\pI\pW}$).
   353	
   354	\subsection{Market-capitalist societies}
   355	
   356	In market-capitalist societies the ideological function is held by many organizations with separate ownership and funding: privately owned media firms financed by advertising and subscriptions, public and private universities, foundations and think tanks, professional associations, scientific journals, regulatory agencies in their certifying role, and religious bodies organized as voluntary associations. Control over authoritative outputs is spread across these organizations, so $H^{\pI}$ is moderate overall, but it varies by sector. Ownership of the largest media firms is often concentrated in a few families \citep{djankov2003}, while accreditation of physicians or approval of drugs may rest with a single professional body or agency.
   357	
   358	The distinctive coupling is between the financial and ideological pillars. Advertising finances news, endowments and grants finance universities, and industry finances a large share of clinical research. \citet{herman1988} built their propaganda model on this coupling. \citet{slaughter2004} documented the movement of universities toward market revenue, and \citet{starr1982} described how medical authority was converted into economic power and later confronted corporate organization of care. Part I treats $C_{\pF\pI}$ as its pair and measures the conversion of financial control into favorable outputs of other pillars by a conversion elasticity (Definition 6.1 of Part I); here the question is what the coupling does to the independence parameter $\lambda$ of Definition~\ref{def:ideological-power:endorsement}.
   359	
   360	The documented capture episodes are sectoral. Systematic reviews associate industry sponsorship with conclusions favorable to sponsors \citep{bekelman2003,lexchin2003,lundh2017}. \citet{oreskes2010} documented organized efforts to manufacture doubt about tobacco harms and environmental hazards. Each case meets the three conditions of a capture link: privileged access through funding, weakened contestability through selective publication or orchestrated doubt, and material evidence linking the asymmetry to an output, whether a published conclusion or a delayed regulation.
   361	
   362	Platform firms now hold part of the function in this regime type. A few companies decide, through ranking and moderation, which statements by journalists, scientists and clergy reach large audiences \citep{gillespie2019}. In the terms of Section~\ref{sec:layer}, they hold a large share of control over reach, one of the outputs that defines $s^{\pI}$, so they raise measured concentration even when the number of speakers grows. The evidence on their persuasive effect is mixed: fabricated stories spread widely \citep{allcott2017}, but an experimental change of feed ranking during an election left attitudes unchanged \citep{guess2023}. Control over reach is established; its translation into belief is an open empirical question.
   363	
   364	The documented checks are also sectoral. Competition among outlets makes media capture costly \citep{besley2006}. Demand-side slant \citep{gentzkow2006} is a rival explanation for partisan coverage that does not require owner control, so evidence of slant is not by itself evidence of capture. Disclosure rules, peer review, replication and the reputational autonomy of regulators \citep{carpenter2010} raise $\lambda$. The capture episodes above were themselves discovered through litigation, journalism and meta-research, which is what source hypothesis H4 predicts: higher rates of documented error discovery can signal stronger accountability rather than more capture \citep{largo2026hbs}.
   365	
   366	\subsection{Communist party-states}
   367	
   368	In communist party-states the ruling party claims the ideological function as part of its leading role. Party propaganda departments, state newspapers and broadcasters, party schools, academies of sciences, writers' and artists' unions and a compulsory curriculum in Marxism-Leninism hold the function. \citet{kenez1985} described how the Bolsheviks built a propaganda state in their first decade, combining agitation, literacy campaigns and new media under party direction. \citet{brooks2000} showed how the Soviet press under Stalin organized public culture as a ritual in which achievements were presented as gifts from the leadership and citizens were expected to express gratitude.
   369	
   370	Concentration is high by design. Appointments of editors, rectors and academy presidents pass through the party's appointment channel, the map from a coalition to the offices it fills in each pillar (Definition 2.8 of Part II), so $C_{\pP\pI}$ is high and $H^{\pI}$ approaches its maximum in the formal structure. Coupling to the coercive pillar is strong: censorship offices and security services enforce the boundaries of permissible expression, and Part V treats the security services themselves. \citet{althusser1971}'s concept of ideological state apparatuses, developed within Marxism, describes this configuration more literally than it describes the societies Althusser had in mind.
   371	
   372	Formal structure overstates actual control. \citet{lane1995} found commonalities and divisions within the Soviet ruling elite in its last decade, and divisions within the elite reduce the effective concentration of control over authoritative outputs. \citet{kuran1991} explained the sudden collapse of East European regimes in 1989 as the release of privately held opposition that public displays had concealed. In the People's Republic of China, \citet{king2013} found that censors removed posts with potential for collective action more consistently than posts criticizing officials, which shows a discriminating rather than total control of expression. \citet{stockmann2013} found that commercialized media, perceived as more credible than official outlets, could carry party messages more effectively. That finding is an instance of Proposition~\ref{prop:ideological-power:credibility}: perceived independence raises the information value of a statement, so a ruling party can gain by permitting outlets that appear independent while retaining control over their limits. \citet{guriev2019} described the same logic for informational autocracies in general. Platforms extend the party's reach rather than escaping it: domestic platform firms operate under party supervision, and \citet{roberts2018} found that censorship relies mainly on friction and flooding, so that most users never meet the information that determined users can still find.
   373	
   374	Public benefits are part of the record. The early Soviet literacy campaigns that \citet{kenez1985} described expanded the population that could read, including what the party did not print. Source Proposition 4, that public benefit is compatible with hierarchy, applies here as elsewhere \citep{largo2026hbs}. The documented checks are weak in formal terms: there is no lawful independent press and no protected academic freedom. They consist of elite factions, professional norms within the sciences, and the preference falsification that makes displayed support an unreliable guide to private belief.
   375	
   376	\subsection{Democratic socialism and social democracy}
   377	
   378	In social democracies the ideological function is held by a mix of public and private institutions in which public institutions have a large role. Public service broadcasters, public universities, state-funded schools, the press of political parties and labor movements, and, in several Nordic countries, established Lutheran churches are the main holders. \citet{hallin2004} placed the media systems of Northern and Central Europe in their democratic corporatist model, in which mass-circulation commercial media coexisted with media tied to organized social and political groups, journalism was highly professionalized, and the state intervened actively through press subsidies and public broadcasting while legal norms limited its control over content.
   379	
   380	Concentration in broadcasting can be high, because a public broadcaster may hold a large audience share. Contestability then depends on the governance of that broadcaster: who appoints its board, how its budget is set, and whether editors are protected. Coupling to the political pillar runs through these appointment and budget channels, and Part II treats $C_{\pP\pI}$ as its pair. Coupling to the productive pillar is distinctive in this regime type. Unions and labor parties historically ran newspapers, educational associations and adult education, so the beliefs of the producing population were shaped partly by organizations that the producers themselves controlled. \citet{berman2006} argued that social democracy's defining idea was the primacy of politics over markets, an ideological commitment advanced through party organization. \citet{esping1990} argued that universal welfare programs build cross-class support for the welfare state, and \citet{rothstein1996} analyzed how the Swedish model depended on the administrative implementation of reforms. Universal programs thus have an ideological consequence: they produce shared beliefs about entitlement that sustain the programs themselves.
   381	
   382	The capture risk in this regime type is that a long-governing party turns public institutions into party instruments. The documented checks are structural. Hallin and Mancini describe the professional autonomy of journalists and the coexistence of public and commercial media, and the boards of public broadcasters in several countries are composed to represent multiple parties and social groups \citep{hallin2004}. Established churches in these states coexist with religious freedom, and \citet{fox2008} shows that state support of religion is common among democracies and does not by itself indicate control of belief.
   383	
   384	\subsection{Islamic states}
   385	
   386	Islamic states form a diverse class: the early and Abbasid caliphates, the Ottoman empire, Safavid and modern Iran, and Saudi Arabia differ in doctrine, in the organization of religious scholars and in the relation of scholars to rulers. The common feature is that political legitimacy is derived in part from religious law, which makes the ulama, the scholars of that law, central holders of the ideological function. Madrasas, mosques and their sermons, juristic opinions, and in modern states ministries of religious affairs and state seminaries are the main institutions.
   387	
   388	The history of the class contains a separation of religious authority from rule that is directly relevant to independence. \citet{crone1986} argued that early caliphs claimed religious authority as deputies of God and that this authority passed to the scholars over the first centuries of Islam; the failure of the caliph's inquisition, the \emph{mihna}, to impose a doctrine on the scholars marked the transition. The case is a documented check: scholars refused an endorsement that the ruler demanded, and the ruler's successors abandoned the demand. \citet{makdisi1981} traced the madrasa as an endowed college of law, financed by charitable endowments that gave scholars a revenue base distinct from the ruler's treasury. \citet{berkey1992} showed that in medieval Cairo the transmission of knowledge remained personal, from teacher to student, even as ruling elites endowed madrasas, which coupled patronage to scholarship without placing scholarly authorization under the patrons' control. \citet{crone2004} surveyed six centuries of medieval Islamic political thought, which itself records a range of views on the obligations of rulers to scholars and law.
   389	
   390	Later states increased the coupling. In the Ottoman empire the learned hierarchy was organized as a career of salaried officials under the chief jurist, the \c{S}eyh\"ulislam, and \citet{imber1997} showed how the chief jurist Ebu's-su'ud harmonized sultanic law with the sharia; $C_{\pP\pI}$ was correspondingly high, while \citet{barkey2008} emphasized the empire's reliance on brokered intermediaries and its accommodation of diversity. In Saudi Arabia, \citet{commins2006} and \citet{alrasheed2002} describe an alliance between the ruling dynasty and the Wahhabi religious establishment, in which scholars legitimated the dynasty and received authority over religious education and public morals. In Iran, \citet{arjomand1988} analyzed how the revolution of 1979 created a clerical state, building on a doctrine of guardianship by the jurist that \citet{khomeini1981} had set out, and \citet{menashri1992} traced the relation between education and state ideology in modern Iran. Here the fusion of religious and political authority raises $C_{\pP\pI}$ and $C_{\pJ\pI}$ toward their maximum, although the Shia clergy's older tradition of plural, independently followed authorities remains a source of internal diversity.
   391	
   392	The medieval checks on rulers were juristic pluralism across schools of law, endowed revenue, and scholarly reputation built on teacher-to-student authorization. \citet{gellner1981} stressed a further division, between urban scripturalist scholarship and rural forms of religious authority, which kept any single body from monopolizing religious legitimacy.
   393	
   394	In the modern period the main check has been the fragmentation of religious authority. \citet{eickelman1992} and \citet{eickelman1996} showed that mass higher education and new media multiplied the people able to claim religious authority, and \citet{zaman2002} showed that the ulama adapted to this competition and remained influential.
   395	
   396	Whether alliances between ulama and states caused authoritarianism \citep{kuru2019}, or whether legitimacy bargains between rulers and religious authorities shaped economic paths \citep{rubin2017}, remains an open debate. Across the class, concentration and coupling range from low, where scholars held endowed and plural authority, to very high, where religious authority was absorbed into the state. The class is defined by its source of legitimacy, not by a single configuration.
   397	
   398	\subsection{Catholic monarchies}
   399	
   400	In the Catholic monarchies of early modern Europe, Habsburg Spain, Bourbon France and the Papal States, the ideological function was shared between the Church and the crown. The Church supplied doctrine, clergy, sacraments, universities and religious orders; the crown supplied patronage, appointment rights and the coercive backing of religious courts. \citet{hsia1998} described the Catholic renewal after the Council of Trent, including the expansion of Jesuit colleges, which made the Society of Jesus one of the largest educational networks of the period. \citet{fragnito2001} and her collaborators documented the work of the Roman congregations that maintained the Index of Prohibited Books and licensed printing in Italy. \citet{eisenstein1979} argued that print transformed the conditions of religious and scholarly authority, which made licensing and indexing central instruments of control.
   401	
   402	The configuration varied. In the Papal States temporal and spiritual authority were held by the same sovereign, so $C_{\pP\pI}$ reached its maximum. In Habsburg Spain the Inquisition operated under royal as well as papal authority and coupled the ideological pillar to the judicial and coercive pillars. \citet{kamen1997} argued that the Inquisition's scale and severity were smaller than the black legend held and that it served local and royal interests as much as doctrinal ones; that revision is itself debated, and the quantitative studies of trial records collected by \citet{henningsen1986} supply the evidence on which the debate turns. In Bourbon France, \citet{burke1992} showed how the image of Louis XIV was manufactured by artists, writers and academies working for the crown, and \citet{bossuet1990} supplied the scriptural theory of divine-right monarchy. \citet{kantorowicz1957} traced the older political theology of the king's two bodies on which such theories drew.
   403	
   404	The transnational Church was also a check on crowns, because its appointment and revenue lay partly outside any single kingdom. In Mann's terms its ideological power was transcendent \citep{mann1986}, and \citet{grzymala2023} argued that rivalry between the papacy and rulers shaped European state building. Within France, \citet{vankley1996} traced how conflicts between Jansenists, the Gallican tradition, the papacy and the crown, with the parlements often siding with the Jansenists, eroded the sacral authority of the monarchy before 1789. These were counter-publics in Fraser's sense \citep{fraser1990}, operating inside a confessional state.
   405	
   406	\subsection{Secular democracies}
   407	
   408	In secular democracies the ideological function is distributed among a legally free press, universities with academic freedom, scientific academies and journals, professional bodies, civil society organizations and religious communities that are either separated from the state or established on plural terms. The model is the public sphere that \citet{habermas1989} reconstructed, with its later commercialization, and the counterpublics that \citet{fraser1990} added. Constitutional speech protections and independent courts, analyzed in Part III, set the legal boundary of the layer.
   409	
   410	Concentration is low in law and variable in fact. Media markets can be concentrated, and the liberal model of \citet{hallin2004} relies on commercial media with weak public broadcasting. Coupling to the financial pillar runs through advertising and research funding, as in the market-capitalist case. Coupling to the political pillar runs through appointments to public science agencies, school curricula and the governance of public broadcasting. The relation to religion differs across democracies. \citet{kuru2009} contrasted the passive secularism of the United States, which permits public religious expression, with the assertive secularism of France and Turkey, where the state excludes religion from public institutions; in Turkey the state's directorate of religious affairs administers mosques and appoints their imams, which shows that state control of religious authority is compatible with a secular constitution. \citet{grzymala2015} found that churches whose moral authority is fused with national identity, as in Ireland and Poland, influenced policy through institutional access, while \citet{casanova1994} showed that religions entered public debate as participants rather than as state authorities.
   411	
   412	Platform intermediaries raise the same question in secular democracies as in market economies, with one addition: their moderation decisions are taken by private firms under speech protections that bind governments but not, in most jurisdictions, the firms themselves \citep{gillespie2019}. Contestability over reach therefore depends on competition among platforms and on their own appeal procedures more than on courts.
   413	
   414	The capture risk in secular democracies is less fusion than conversion: financial power converted into credibility through sponsorship, or political power converted into control of a public broadcaster. The documented checks are the twin tolerations \citep{stepan2000}, judicial protection of expression, the plurality of outlets that makes media capture costly \citep{besley2006}, and the social process of critical scrutiny that \citet{oreskes2019} identified in science.
   415	
   416	\subsection{Summary across regimes}
   417	
   418	Table~\ref{tab:regimes} summarizes the comparison. Each regime type implements the ideological function, as Theorem~\ref{thm:ideological-power:necessity} requires. The types differ in which institutions hold the function, how concentrated control over authoritative outputs is, which other pillars it is coupled to, and what keeps authorities independent.
   419	
   420	\begin{table}[t]
   421	\centering
   422	\small
   423	\caption{The ideological function across six regime types. Entries are qualitative codings from the sources cited in the text; no index value is estimated for any polity.}
   424	\label{tab:regimes}
   425	\begin{tabularx}{\textwidth}{@{}L{2.3cm}YYY@{}}
   426	\toprule
   427	Regime type & Main holders & Concentration and coupling & Main sources of contestability \\
   428	\midrule
   429	Market capitalism & Private media, universities, journals, professions and certifying agencies & Moderate concentration that varies by sector, with strong financial coupling & Competition among outlets, disclosure, peer review and regulator reputation \\
   430	Communist party-state & Party propaganda organs, state media, party schools and academies & High formal concentration, with strong political and coercive coupling & Elite factions, professional norms and hidden private opinion \\
   431	Social democracy & Public broadcasters, public universities, labor and party press, established churches & Concentration high in some channels, with strong productive coupling through labor organizations & Plural boards, protected journalism and coexisting commercial media \\
   432	Islamic states & Ulama, madrasas, mosques, chief jurists and religious ministries & Ranges from low under endowed plural scholarship to very high under clerical rule & Juristic pluralism, endowed revenue and fragmentation of authority \\
   433	Catholic monarchies & Church hierarchy, orders, universities, Inquisition, Index and court culture & High crown and Church coupling, with full fusion in the Papal States & Partial independence of the transnational Church and theological conflict \\
   434	Secular democracies & Free press, universities, academies, civil society and religious bodies & Low legal concentration, with moderate financial and political coupling & Speech protections, plurality of outlets and scientific scrutiny \\
   435	\bottomrule
   436	\end{tabularx}
   437	\end{table}
   438	
   439	\section{Mechanisms, failure modes and checks}
   440	\label{sec:mechanisms}
   441	
   442	\subsection{From coordination to capture}
   443	
   444	Coordination in the ideological pillar becomes capture when a coalition gains control over what authorities say and that control weakens the review that would otherwise expose it. The source framework's capture link supplies the test \citep{largo2026hbs}. In the ideological layer its three conditions take a specific form. Privileged access means that a coalition funds, appoints, licenses or can dismiss an authority, or controls the channel through which it speaks. Weakened accountability means that the access is used to remove or evade review: findings are withheld, dissenting scholars are dismissed, sponsorship is concealed, presses are licensed selectively, or rival authorities are suppressed. Material evidence means documents, such as internal correspondence, censorship directives, appointment records or trial registries, that tie the access to a specific output, such as a published conclusion, a juristic opinion, a curriculum change or a broadcast.
   445	
   446	The same test says what is not capture. A church whose doctrine agrees with a government's policy is not thereby captured. Industry-funded research that is disclosed, preregistered and reproduced is not captured. A ruler's endowment of a college is patronage, which becomes capture only if it is used to control what the college certifies. A ministry of education is part of the differentiated structure that Proposition A predicts, and source Proposition 1 holds that differentiation is not integration \citep{largo2026hbs}. Public goods are a rival explanation for many configurations of the pillar: a public broadcaster or a state seminary may exist because it supplies information or instruction that markets or voluntary bodies would undersupply.
   447	
   448	\subsection{Endorsement and independence}
   449	
   450	The value of a legitimating authority to its audience depends on whether its statements track something other than the interest of whoever controls it. A simple model captures this.
   451	
   452	\begin{definition}[Endorsement model]
   453	\label{def:ideological-power:endorsement}
   454	A rule or policy is \emph{sound} ($\theta=G$) or \emph{unsound} ($\theta=B$), with public prior $\pi=\Prob(\theta=G)\in(0,1)$. An authority observes a private signal $s\in\{0,1\}$ with $\Prob(s=1\mid G)=\Prob(s=0\mid B)=q\in(\tfrac12,1)$. With probability $\lambda\in[0,1]$ the authority is \emph{independent} and endorses ($e=1$) if and only if $s=1$. With probability $1-\lambda$ it is \emph{captured} and endorses regardless of $s$. The public observes $e$ but neither $s$ nor the authority's type, knows $(\pi,q,\lambda)$, and forms the posterior $\mu=\Prob(G\mid e)$. Write $\mu_1(\lambda)=\Prob(G\mid e=1)$ and $\mu_0=\Prob(G\mid s=0)=\pi(1-q)/\bigl(\pi(1-q)+(1-\pi)q\bigr)$. For $\lambda\in(0,1]$, $\mu_0=\Prob(G\mid e=0)$; at $\lambda=0$ a refusal has probability zero and $\mu_0$ is the continuous extension.
   455	\end{definition}
   456	
   457	The parameter $\lambda$ summarizes what the components of $Q^{\pI}$ secure for a single authority. A tenured faculty, an endowed seminary, a juristic school with its own revenue, a regulator with a reputation to protect \citep{carpenter2010}, or an editor who cannot be dismissed for a story all raise $\lambda$.
   458	
   459	\begin{proposition}[Credibility and sorting]
   460	\label{prop:ideological-power:credibility}
   461	In the endorsement model:
   462	\begin{enumerate}
   463	\item[(a)] $\mu_1(0)=\pi$: a captured authority's endorsement carries no information.
   464	\item[(b)] $\mu_1(\lambda)$ is strictly increasing in $\lambda$, and $\mu_0<\pi$ does not depend on $\lambda$.
   465	\item[(c)] $\E[\mu\mid G]$ is strictly increasing and $\E[\mu\mid B]$ is strictly decreasing in $\lambda$.
   466	\end{enumerate}
   467	\end{proposition}
   468	
   469	\begin{proof}
   470	Let $a=\Prob(s=0)=\pi(1-q)+(1-\pi)q$. A refusal occurs only when the authority is independent and $s=0$, so $\Prob(e=0)=\lambda a$ and, for $\lambda>0$, $\Prob(G\mid e=0)=\Prob(G\mid s=0)=\pi(1-q)/a=\mu_0$, which does not depend on $\lambda$. Since $q>\tfrac12$, $\mu_0<\pi$.
   471	
   472	(a) and (b). By Bayes' rule,
   473	\[
   474	\mu_1(\lambda)=\frac{\pi\bigl(1-\lambda(1-q)\bigr)}{\pi\bigl(1-\lambda(1-q)\bigr)+(1-\pi)(1-\lambda q)}
   475	=\Bigl(1+\tfrac{1-\pi}{\pi}\,r(\lambda)\Bigr)^{-1},\qquad r(\lambda)=\frac{1-\lambda q}{1-\lambda(1-q)}.
   476	\]
   477	At $\lambda=0$, $r=1$ and $\mu_1=\pi$. Differentiating, $r'(\lambda)=(1-2q)/(1-\lambda(1-q))^2<0$, so $\mu_1$ is strictly increasing.
   478	
   479	(c) Posteriors are a martingale, so $\E[\mu]=\pi$, and $\E[\mu\,\mathbf{1}_G]=\E[\mu\,\Prob(G\mid e)]=\E[\mu^2]$. Hence $\E[\mu\mid G]=\E[\mu^2]/\pi$ and $\E[\mu\mid B]=(\pi-\E[\mu^2])/(1-\pi)$. It suffices to show that $\E[\mu^2]$ is strictly increasing in $\lambda$. From the martingale identity, $\Prob(e=1)\mu_1=\pi-\lambda a\mu_0$, so $\mu_1=(\pi-\lambda a\mu_0)/(1-\lambda a)$ and
   480	\[
   481	\E[\mu^2]=\frac{(\pi-\lambda a\mu_0)^2}{1-\lambda a}+\lambda a\mu_0^2 .
   482	\]
   483	Differentiating and substituting $\mu_1$,
   484	\[
   485	\frac{d\,\E[\mu^2]}{d\lambda}=a\mu_1\bigl(\mu_1-2\mu_0\bigr)+a\mu_0^2=a\,(\mu_1-\mu_0)^2 .
   486	\]
   487	By (b), $\mu_1(\lambda)\geq\pi>\mu_0$ for every $\lambda$, and $a>0$, so the derivative is strictly positive.
   488	\end{proof}
   489	
   490	Part (a) is the formal version of an old observation: praise from a courtier who must praise is worthless. Part (c) carries the argument further. Independent authorities are an asset to a coalition whose rules are sound and a liability to one whose rules are not. The same institution that lends credibility to a sound public-health rule exposes an unsound one. This is the precise sense in which healthcare, science and religious institutions can either check or enable capture: their independence is what makes their endorsement worth having, and it is also what makes them dangerous to a coalition that needs endorsement for an unsound rule. The next subsection turns the result into a comparative static for a governing coalition.
   491	
   492	
   493	\subsection{The control and credibility trade-off}
   494	
   495	A governing coalition values public confidence in its rules and also values control over authorities for its own sake, because control lets it direct authoritative outputs toward other ends. Independence is largely fixed in advance, by charters, endowments, tenure rules and appointment procedures, before the coalition knows whether the rules it will later need endorsed are sound. We therefore model the choice of $\lambda$ as an act of institutional design taken before $\theta$ is realized and observed by the public. Because the choice precedes $\theta$, it carries no information about $\theta$, and the public's prior remains $\pi$.
   496	
   497	\begin{proposition}[Control and credibility]
   498	\label{prop:ideological-power:tradeoff}
   499	Before $\theta$ is realized, a coalition chooses a publicly observed independence $\lambda\in[\lambda_{\min},1]$, where $\lambda_{\min}\in[0,1)$ is the independence that existing institutions guarantee whatever the coalition does. Its expected payoff is
   500	\[
   501	W(\lambda;\rho)=\pi\,\beta_G\,\E[\mu\mid G](\lambda)+(1-\pi)\,\beta_B\,\E[\mu\mid B](\lambda)+\rho\,(1-\lambda),
   502	\]
   503	where $\beta_G,\beta_B\geq0$ are the values the coalition places on public confidence when its rule is sound and unsound, and $\rho\geq0$ is the value of control. Let $\Delta=\beta_G-\beta_B$ and $S(\lambda)=\E[\mu^2](\lambda)$. Then:
   504	\begin{enumerate}
   505	\item[(a)] $W(\lambda;\rho)=\Delta\,S(\lambda)+\beta_B\pi+\rho(1-\lambda)$, and $S$ is strictly increasing and strictly convex.
   506	\item[(b)] If $\Delta<0$, or if $\Delta=0$ and $\rho>0$, the unique choice is $\lambda=\lambda_{\min}$.
   507	\item[(c)] If $\Delta>0$, every maximizer lies in $\{\lambda_{\min},1\}$, and $\lambda=1$ is the unique maximizer if and only if $\Delta\bigl(S(1)-S(\lambda_{\min})\bigr)>\rho\,(1-\lambda_{\min})$.
   508	\item[(d)] For fixed $\Delta$, every maximizer at a higher $\rho$ is weakly below every maximizer at a lower $\rho$.
   509	\end{enumerate}
   510	\end{proposition}
   511	
   512	\begin{proof}
   513	(a) By the identities in the proof of Proposition~\ref{prop:ideological-power:credibility}, $\pi\E[\mu\mid G]=S$ and $(1-\pi)\E[\mu\mid B]=\pi-S$. Substituting gives the expression for $W$. The same proof gives $S'(\lambda)=a(\mu_1(\lambda)-\mu_0)^2>0$. Since $\mu_1$ is strictly increasing and $\mu_1>\mu_0$, $S'$ is strictly increasing, so $S$ is strictly convex.
   514	
   515	(b) If $\Delta<0$, $\Delta S$ is strictly decreasing and $\rho(1-\lambda)$ is nonincreasing, so $W$ is strictly decreasing. If $\Delta=0$ and $\rho>0$, $W$ is strictly decreasing through its last term. In both cases $\lambda_{\min}$ is the unique maximizer.
   516	
   517	(c) If $\Delta>0$, $W$ is the sum of a strictly convex function and a linear one, hence strictly convex on $[\lambda_{\min},1]$, and a strictly convex function on a compact interval attains its maximum only at endpoints. Comparing the endpoints, $W(1)>W(\lambda_{\min})$ if and only if $\Delta(S(1)-S(\lambda_{\min}))>\rho(1-\lambda_{\min})$.
   518	
   519	(d) Let $\rho<\rho'$, let $\lambda$ maximize $W(\cdot;\rho)$ and $\lambda'$ maximize $W(\cdot;\rho')$. Optimality gives $W(\lambda;\rho)\geq W(\lambda';\rho)$ and $W(\lambda';\rho')\geq W(\lambda;\rho')$. Adding the two inequalities, the terms in $S$ cancel and what remains is $(\lambda'-\lambda)(\rho-\rho')\geq0$. Since $\rho-\rho'<0$, $\lambda'\leq\lambda$.
   520	\end{proof}
   521	
   522	The proposition is a conditional comparative static, and its key parameter is alignment. A coalition values independent authorities only when it gains more from public confidence in sound rules than in unsound ones ($\Delta>0$), which is the case when its interests run with the public's: a government that wants a vaccine taken because it works, not because a contract depends on it. A coalition whose gains do not depend on soundness ($\Delta\leq0$), such as one that profits from compliance with whatever rule it issues, pushes independence to the floor. The floor $\lambda_{\min}$, set by endowments, tenure, constitutional protection and transnational appointment, therefore protects the public exactly where alignment fails. Because $S$ is convex, the choice is all or nothing: aligned coalitions with a small value of control grant full independence, and the rest grant the minimum. Intermediate independence in the record reflects floors and constraints, not interior optima.
   523	
   524	Interim capture is different. After institutions are set and the public has formed a conjecture $\hat\lambda$, a coalition that has learned $\theta$ may be able to lower actual independence covertly, by pressuring editors or steering grants, without the public revising $\hat\lambda$.
   525	
   526	\begin{proposition}[Covert capture]
   527	\label{prop:ideological-power:covert}
   528	Suppose the public's posterior after an endorsement is $\mu_1(\hat\lambda)$ for a fixed conjecture $\hat\lambda>0$, while actual independence is $\lambda$. Then for $\theta\in\{G,B\}$,
   529	\[
   530	\E[\mu\mid\theta]=\mu_1(\hat\lambda)-\lambda\,\Prob(s=0\mid\theta)\bigl(\mu_1(\hat\lambda)-\mu_0\bigr),
   531	\]
   532	which is strictly decreasing in $\lambda$ for both types. The gain from a unit reduction of $\lambda$ is $q(\mu_1(\hat\lambda)-\mu_0)$ when the rule is unsound and $(1-q)(\mu_1(\hat\lambda)-\mu_0)$ when it is sound, so it is larger by the factor $q/(1-q)>1$ for a coalition whose rule is unsound.
   533	\end{proposition}
   534	
   535	\begin{proof}
   536	Given $\theta$, a refusal occurs with probability $\lambda\Prob(s=0\mid\theta)$ and yields the posterior $\mu_0$; otherwise the authority endorses and the public's posterior is $\mu_1(\hat\lambda)$. Taking the expectation gives the formula. Since $\mu_1(\hat\lambda)\geq\pi>\mu_0$ by Proposition~\ref{prop:ideological-power:credibility}(b), and $\Prob(s=0\mid B)=q$ and $\Prob(s=0\mid G)=1-q$ are positive, the expression is strictly decreasing in $\lambda$ with the stated slopes.
   537	\end{proof}
   538	
   539	Covert capture always raises expected confidence in the short run, because the public cannot discount what it does not see. Its value is greater for coalitions whose rules are unsound, since independent authorities would refuse them more often. If covert capture has a cost, coalitions with unsound rules will therefore pay it more often, and restrictions on independent authorities should follow adverse findings. Hypothesis HI7 in Section~\ref{sec:measurement} tests that prediction. If instead the coalition chose $\lambda$ openly after learning $\theta$, the choice would itself signal $\theta$ and the analysis would become a signaling game, which this paper does not solve. Commercialized but party-guided media in China \citep{stockmann2013} and the simulated democratic forms of informational autocracies \citep{guriev2019} fit the covert pattern: control is exercised while the appearance of independence is maintained.
   540	
   541	The covert case points to the main channel of deception. After an endorsement the public's posterior is $\mu_1(\hat\lambda)$, while the true probability that the rule is sound given an endorsement is $\mu_1(\lambda)$.
   542	
   543	\begin{corollary}[Deception gap]
   544	\label{cor:ideological-power:gap}
   545	The public overestimates the soundness of an endorsed rule, $\mu_1(\hat\lambda)>\mu_1(\lambda)$, if and only if $\hat\lambda>\lambda$. The gap $\mu_1(\hat\lambda)-\mu_1(\lambda)$ is strictly increasing in $\hat\lambda$ and strictly decreasing in $\lambda$.
   546	\end{corollary}
   547	
   548	\begin{proof}
   549	Immediate from the strict monotonicity of $\mu_1$ in Proposition~\ref{prop:ideological-power:credibility}(b).
   550	\end{proof}
   551	
   552	Capture misleads exactly when audiences overestimate independence. Disclosure rules, conflict-of-interest registries and the publication of appointment and funding records exist to bring $\hat\lambda$ into line with $\lambda$. They do not make authorities independent; they make their dependence visible, which removes the gap.
   553	
   554	\subsection{Correlated control and the discovery of error}
   555	
   556	Most polities have many legitimating authorities. Whether they detect and disclose an error depends on how many of them are independent, and on whether their independence is correlated. Integration across pillars, in the source's sense, typically works by correlation: when one coalition appoints the editors, the rectors and the chief jurists, they are captured together or not at all.
   557	
   558	\begin{proposition}[Disclosure under correlated control]
   559	\label{prop:ideological-power:disclosure}
   560	Let $K\geq2$ authorities each be independent with probability $\lambda\in(0,1)$, with an arbitrary joint distribution of independence across authorities, and let $N$ be the number of independent authorities. Given the set of independent authorities, each independently discovers and discloses a given error with probability $p\in(0,1)$; captured authorities never disclose. Let $D=\Prob(\text{at least one disclosure})$.
   561	\begin{enumerate}
   562	\item[(a)] For every joint distribution, $\lambda\bigl(1-(1-p)^K\bigr)\leq D\leq 1-(1-p)^{\lambda K}$.
   563	\item[(b)] The lower bound is attained if and only if independence is all or nothing, $N\in\{0,K\}$ almost surely, which is the case of perfectly correlated control.
   564	\item[(c)] If independence is drawn independently across authorities, $D=1-(1-\lambda p)^K$, which lies strictly above the lower bound.
   565	\end{enumerate}
   566	\end{proposition}
   567	
   568	\begin{proof}
   569	Conditional on $N$, no disclosure occurs with probability $(1-p)^N$, so $D=1-\E[g(N)]$ with $g(x)=(1-p)^x$, a strictly convex function. By linearity of expectation $\E[N]=\lambda K$.
   570	
   571	(a) For the upper bound, Jensen's inequality gives $\E[g(N)]\geq g(\E N)=(1-p)^{\lambda K}$. For the lower bound, strict convexity places $g$ below its chord on $[0,K]$: $g(x)\leq(1-x/K)g(0)+(x/K)g(K)$, with equality only at $x\in\{0,K\}$. Taking expectations, $\E[g(N)]\leq(1-\lambda)+\lambda(1-p)^K$, so $D\geq\lambda(1-(1-p)^K)$.
   572	
   573	(b) The chord inequality is strict for $x\in(0,K)$, so equality in expectation requires $\Prob(N\in\{0,K\})=1$. Conversely, if $N\in\{0,K\}$ almost surely then $\Prob(N=K)=\lambda$ and $D=\lambda(1-(1-p)^K)$.
   574	
   575	(c) If independence is independent across authorities, $N$ is binomial with parameters $K$ and $\lambda$, and $\E[(1-p)^N]=(1-\lambda+\lambda(1-p))^K=(1-\lambda p)^K$. Since $K\geq2$ and $\lambda\in(0,1)$, $\Prob(0<N<K)>0$, so by (b) the bound is strict.
   576	\end{proof}
   577	
   578	\begin{corollary}[Integration lowers discovery]
   579	\label{cor:ideological-power:integration}
   580	Holding fixed the number of authorities and the average probability that each is independent, a change in appointment structure that makes the independence of authorities perfectly correlated lowers the probability that an error is disclosed from $1-(1-\lambda p)^K$ to $\lambda(1-(1-p)^K)$.
   581	\end{corollary}
   582	
   583	The corollary separates two things that are often merged. Concentration $H^{\pI}$ concerns how many authorities there are and how control is shared among them. Integration concerns whether control over them moves together, which is what high $C_{\pP\pI}$ or $C_{\pF\pI}$ produces when one coalition appoints or funds all of them. A polity can have many universities, newspapers and juristic schools, and so low measured concentration, and still have low discovery if one coalition appoints their heads. The upper bound in (a) is attained only when $\lambda K$ is an integer and $N=\lambda K$ almost surely; otherwise the maximum is reached by a distribution on $\lfloor\lambda K\rfloor$ and $\lceil\lambda K\rceil$. The bound adds a design point: discovery is highest when the number of independent authorities is least variable, which plural appointment by rival bodies secures better than independent chance. This refines source hypothesis H4 on epistemic checks and source Proposition 2 on the interruption of transmission \citep{largo2026hbs}.
   584	
   585	\subsection{Fragility of displayed legitimacy}
   586	
   587	Ideological control often aims at public displays: attendance, applause, signatures, votes in uncontested elections. The beliefs those displays reveal are a separate matter. A threshold model, of the kind \citet{granovetter1978} introduced for collective behavior and \citet{kuran1991} applied to preference falsification, shows how far the two can diverge.
   588	
   589	\begin{proposition}[Fragility]
   590	\label{prop:ideological-power:fragility}
   591	Let $n$ members have thresholds $\tau_i\in[0,1]$: member $i$ expresses dissent publicly when the share of members already doing so is at least $\tau_i$. Let $\Phi(x)=\frac1n\#\{i:\tau_i\leq x\}$ and $x_0=0$, $x_{k+1}=\Phi(x_k)$.
   592	\begin{enumerate}
   593	\item[(a)] The sequence $(x_k)$ is nondecreasing and reaches, within $n+1$ steps, the smallest fixed point $x^\ast$ of $\Phi$.
   594	\item[(b)] There are threshold profiles $\tau$ and $\tau'$ that differ only in one member's threshold, by $1/n$, with $x^\ast(\tau)=1$ and $x^\ast(\tau')=0$.
   595	\end{enumerate}
   596	\end{proposition}
   597	
   598	\begin{proof}
   599	(a) $\Phi$ is nondecreasing. Since $x_1=\Phi(0)\geq0=x_0$, induction gives $x_{k+1}=\Phi(x_k)\geq\Phi(x_{k-1})=x_k$. The sequence takes values in $\{0,1/n,\dots,1\}$, so it is constant from some step $k\leq n$ on, at a fixed point $\bar x$. If $y$ is any fixed point, then $x_0\leq y$, and $x_k\leq y$ implies $x_{k+1}=\Phi(x_k)\leq\Phi(y)=y$, so $\bar x\leq y$.
   600	
   601	(b) Let $\tau_i=(i-1)/n$ for $i=1,\dots,n$. Then $\Phi(k/n)=(k+1)/n$ for $k<n$, so $x_k=k/n$ and $x^\ast=1$. Let $\tau'$ agree with $\tau$ except $\tau'_1=1/n$. No member has threshold $0$, so $\Phi'(0)=0$ and $x^\ast(\tau')=0$.
   602	\end{proof}
   603	
   604	Two populations whose private dispositions are almost identical can display opposite public states. Displayed support is therefore not a sufficient statistic for private belief, and the gap is largest where expression is costly, which is where $Q^{\pI}$ is low. The result explains why regimes that control the ideological layer can appear stable and then collapse quickly, as \citet{kuran1991} argued for 1989. It also constrains measurement: in polities with low contestability, attendance, applause and uncontested votes cannot validate claims about normative legitimacy.
   605	
   606	\subsection{Coupling of belief to coercion and production}
   607	
   608	The series assigns two of the fifteen cross-pillar pairs to this Part for primary treatment.
   609	
   610	The coupling $C_{\pI\pC}$ runs in both directions. Control of belief needs enforcement when it goes beyond persuasion: heresy and blasphemy prosecutions, censorship offices, the licensing of presses and the dismissal of dissenting teachers all require a sanctioning apparatus. The Spanish Inquisition joined doctrinal judgment to coercive power \citep{kamen1997}, and the censorship offices of party-states worked with the security services. Coercion in turn needs belief. Soldiers and police carry out orders when they expect others to do so, and Proposition~\ref{prop:ideological-power:fragility} shows how quickly that expectation can fail. \citet{greitens2016} and the other sources of Part V analyze the coercive institutions themselves, and Part V shows that the refusal of manifestly unlawful orders, one of its checks on coercion, depends on the legitimating beliefs studied here. For the ideological layer, $C_{\pI\pC}$ is the extent to which one coalition both decides what may be said and commands the organizations that punish saying otherwise. It is high where religious courts or security services enforce doctrine and low where independent courts protect expression.
   611	
   612	The coupling $C_{\pI\pW}$ concerns the beliefs of the producing population and the institutions that shape them. Belief-producing specialists need a surplus to live on, a dependency of the ideological on the productive pillar that Part VII derives in general. In the other direction, beliefs shape work and compliance. \citet{levi1988} showed that taxpayers' compliance is quasi-voluntary: it depends on their belief that others comply and that rulers keep their bargains. \citet{becker2009} found that Protestant regions of Prussia had higher literacy, which they attributed to the religious emphasis on reading scripture, and that literacy rather than a work ethic accounts for much of their economic advantage. \citet{gellner1983} argued that industrial economies require a standardized literate culture that only a mass education system can supply, which makes control of schooling central to modern states. \citet{bourdieu1977} argued that schooling also reproduces class position under the appearance of merit. The coupling is high where one coalition controls both the conditions of work and the institutions that teach workers what to expect of it, and low where producers have authorities of their own, such as the labor press and educational associations of social democracies. Part VI treats everyday resistance \citep{scott1985}, which shows that producers do not simply absorb dominant beliefs, and its latent-veto result, that producers can threaten a system's persistence by withdrawing the production it needs (Proposition 3.5 of Part VI), explains why rulers need producers to believe that compliance is expected of everyone.
   613	
   614	\subsection{Checks}
   615	
   616	Each component of $Q^{\pI}$ maps onto a parameter of the models above. Independence raises $\lambda$ and, through the institutional floor $\lambda_{\min}$, protects the public when the coalition's interests are not aligned with soundness (Proposition~\ref{prop:ideological-power:tradeoff}) and when it would capture authorities covertly (Proposition~\ref{prop:ideological-power:covert}). Disclosure aligns the public's estimate $\hat\lambda$ with the truth and closes the deception gap (Corollary~\ref{cor:ideological-power:gap}). Plurality with separate appointment raises the number of authorities and lowers the correlation of their capture (Proposition~\ref{prop:ideological-power:disclosure}). Reviewability raises the discovery probability $p$. Exit lets audiences abandon authorities that lose credibility, which gives authorities a reputational reason to remain independent, the mechanism behind both the demand-side account of \citet{gentzkow2006} and the regulator reputation of \citet{carpenter2010}.
   617	
   618	The historical record shows each check operating. Scholars refused the Abbasid caliph's doctrinal demand \citep{crone1986}. Endowments gave madrasas a revenue base of their own \citep{makdisi1981}. The transnational Church limited the claims of crowns \citep{grzymala2023}, and Jansenist and Gallican counter-publics eroded royal sacrality \citep{vankley1996}. Competition among outlets raises the cost of media capture \citep{besley2006}, and meta-research exposed sponsorship bias in clinical research \citep{lundh2017}. These are the forms that source Proposition 2, that checks can interrupt the transmission of concentrated power, takes in the ideological layer \citep{largo2026hbs}.
   619	
   620	\section{Measurement}
   621	\label{sec:measurement}
   622	
   623	The constructs of this Part are measurable from documents. Table~\ref{tab:indicators} lists indicators for each. All are subject to the source's requirements: weights and thresholds are preregistered, the population of events is defined before data collection rather than drawn from scandals, and measurement invariance is tested before indicators are compared across regime types \citep{largo2026hbs}.
   624	
   625	\begin{table}[t]
   626	\centering
   627	\small
   628	\caption{Indicators for the ideological layer. Each construct can be coded from public documents or existing datasets.}
   629	\label{tab:indicators}
   630	\begin{tabularx}{\textwidth}{@{}L{3.1cm}YL{3.4cm}@{}}
   631	\toprule
   632	Construct & Indicator & Data or design \\
   633	\midrule
   634	Concentration $H^{\pI}$ & Shares of appointments, accreditation decisions and audience reach held by each organization & Ownership data \citep{djankov2003} and appointment records \\
   635	Independence & Tenure protection, editorial autonomy and academic and juristic freedom & Expert-coded indicators \citep{coppedge2011} \\
   636	Disclosure & Share of trials, articles and broadcasts with published funding and conflict statements & Trial registries and journal policies \\
   637	Reviewability & Rates of correction, retraction and successful replication & Retraction and replication records \\
   638	Exit & Legal penalties for unlicensed publication, apostasy or blasphemy & Religion and state coding \citep{fox2008} \\
   639	Censorship practice & What is removed and what is left standing & Audit and observational designs \citep{king2013} \\
   640	Correlated control & Share of authority heads appointed by the same body & Appointment registers and party lists \\
   641	Coupling $C_{\pI\pC}$ & Prosecutions and sanctions for expression and the bodies that order them & Court and security records \\
   642	Platform reach & Shares of ranked and moderated reach held by each platform & Platform disclosures and feed experiments \citep{guess2023} \\
   643	\bottomrule
   644	\end{tabularx}
   645	\end{table}
   646	
   647	The hypotheses below refine the source's hypotheses for this pillar. Each has a stated falsifier. Several are drawn directly from the propositions of Section~\ref{sec:mechanisms}; the others restate claims from the literature in testable form.
   648	
   649	\begin{table}[t]
   650	\centering
   651	\small
   652	\caption{Hypotheses for the ideological pillar, with the observation that would count against each.}
   653	\label{tab:hypotheses}
   654	\begin{tabularx}{\textwidth}{@{}L{3.0cm}YY@{}}
   655	\toprule
   656	Hypothesis & Prediction & Falsifier \\
   657	\midrule
   658	HI1 State media ownership & Greater state ownership of media is associated with weaker accountability outcomes \citep{djankov2003}. & No association after controls, or public broadcasters with plural governance behaving like state-owned media. \\
   659	HI2 Demand and supply of slant & Slant tracks audience composition more than owner identity \citep{gentzkow2006}. & Changes of owner that shift content with audience composition held constant. \\
   660	HI3 Sponsorship and disclosure & Disclosure and registration rules narrow the gap between sponsored and unsponsored conclusions \citep{lundh2017}. & A gap that does not narrow after such rules are introduced. \\
   661	HI4 Correlated control & With average independence fixed, systems where one body appoints most authorities show less documented error correction. & Equal or higher correction under common appointment. \\
   662	HI5 Fragmentation of authority & Mass education and new media raise the number of recognized religious and scholarly authorities \citep{eickelman1996,eisenstein1979}. & No rise in recognized claimants after such expansions. \\
   663	HI6 Credibility premium & Outlets perceived as independent persuade more than official outlets \citep{stockmann2013,enikolopov2011}. & No difference in persuasive effect. \\
   664	HI7 Attacks follow adverse findings & Restrictions on independent authorities follow findings unfavorable to the governing coalition (Proposition~\ref{prop:ideological-power:covert}). & Restrictions unrelated in timing to prior adverse findings. \\
   665	HI8 Hidden opinion & The gap between displayed and privately reported support is larger where contestability is lower \citep{kuran1991}. & No relation between contestability and the gap. \\
   666	\bottomrule
   667	\end{tabularx}
   668	\end{table}
   669	
   670	Three identification problems deserve emphasis. Discovery and capture are confounded: a high rate of documented error may mean many errors or strong review, so HI4 must compare correction given comparable exposure, as source hypothesis H4 already notes. Selection of cases from scandals biases every estimate toward finding capture, which is why the population must be preregistered. And indicators of displayed support are invalid where contestability is low, by Proposition~\ref{prop:ideological-power:fragility}, so private measures such as list experiments are needed. None of these problems is peculiar to any regime type, and each applies with equal force to all six.
   671	
   672	\section{A typological reading of Revelation 13}
   673	\label{sec:revelation}
   674	
   675	\subsection{Method}
   676	
   677	The measurement program above states what evidence would show capture of the ideological pillar. The series pairs it with a normative image of capture drawn from Revelation 13, read typologically. On this reading the beast is a recurring pattern of power that claims ultimate loyalty, and Babylon is the city that organizes commerce and worship around that claim in any age. \citet{bauckham1993} read Rome as the paradigm of such power, and \citet{beale1999} defended an idealist reading that treats the images as transhistorical. The contextual reading anchors the images in the Roman province of Asia, its imperial cult and its trade \citep{koester2014,friesen2001,kraybill1996}. Futurist readings, which take the text to predict a specific future order or person, are excluded by the series' guardrails. Their reception history shows why: \citet{fuller1995} and \citet{boyer1992} document repeated identifications of the beast with contemporary figures, each of which failed. Historicist readings that identified the papacy with the beast belonged to the polemics of the Reformation, as the reception histories of \citet{emmerson1992}, \citet{mcginn1998} and \citet{kovacs2004} document. Any identification of a church, a faith, a profession or a regime with the beast is excluded here for the same reason. What follows is an interpretive claim of this project, offered as an analogy that aids comparison, not as a settled exegetical result.
   678	
   679	\subsection{The second beast as legitimating authority}
   680	
   681	Revelation 13 presents two beasts. The first, from the sea, holds authority and makes war. The second rises from the land and does not rule. In the King James text it ``had two horns like a lamb, and he spake as a dragon'' (13:11). It ``exerciseth all the power of the first beast before him, and causeth the earth and them which dwell therein to worship the first beast'' (13:12), and it ``deceiveth them that dwell on the earth by the means of those miracles which he had power to do'' (13:14). Later chapters name it ``the false prophet that wrought miracles before him'' (19:20).
   682	
   683	The second beast performs the function this paper studies. It produces belief in the authority of the first beast, and it does so through public signs performed ``in the sight of men'' (13:13), which are public events in the sense of Definition~\ref{def:ideological-power:public-signal}. The contextual reading identifies it with the agents of the imperial cult in Asia. \citet{price1984} showed that the cult in Asia Minor was organized largely by the cities and their elites, who used it to represent imperial power within their own civic religion, and \citet{friesen2001} examined its provincial institutions. The legitimation of Roman rule was thus supplied locally, by elites who gained standing from it. In the vocabulary of Section~\ref{sec:mechanisms}, it rested on privileged access exchanged for endorsement.
   684	
   685	The mismatch between the lamb's horns and the dragon's voice is the typological image of the deception gap in Corollary~\ref{cor:ideological-power:gap}. An authority that appears independent and gentle, so that its audience assigns it high $\hat\lambda$, speaks entirely for the ruler, so that its true $\lambda$ is zero. The text calls the result deception. The model calls it a posterior that exceeds the truth by an amount that grows with the gap between perceived and actual independence.
   686	
   687	\subsection{Image, enforcement and exchange}
   688	
   689	The second beast makes an image that speaks and causes ``that as many as would not worship the image of the beast should be killed'' (13:15). The image joins legitimation to coercion, which is the coupling $C_{\pI\pC}$ at its maximum. The text then joins both to economic participation: the second beast causes all ``to receive a mark in their right hand, or in their foreheads: And that no man might buy or sell, save he that had the mark'' (13:16 to 13:17). Displayed allegiance becomes the condition of exchange, which couples the ideological pillar to the financial and productive pillars that Parts I and VI analyze. \citet{kraybill1996} argued that for Christians in Asia, participation in trade guilds and commerce carried obligations to honor the imperial cult, so the image had a concrete social referent. In Revelation 18 the merchants of Babylon ``were the great men of the earth; for by thy sorceries were all nations deceived'' (18:23), an image of commerce and deception bound together that \citet{bauckham1993} reads as part of an economic critique of Rome.
   690	
   691	Proposition~\ref{prop:ideological-power:fragility} supplies a reading of compelled worship. Worship enforced on pain of death is a display whose relation to private belief is unknown, and the text treats it as such: the faithful in Revelation are those who refuse the display. \citet{collins1984} read the book as a response to a crisis perceived by a minority community, and its images express that community's experience of a public culture in which displayed loyalty was demanded.
   692	
   693	\subsection{Scope of the reading}
   694	
   695	The normative warning in the text attaches to Proposition B, not to Proposition A. Revelation does not condemn teaching, worship, scholarship or the existence of authorities that shape belief; it is itself an act of witness that seeks to shape belief. Its target is a configuration in which legitimating authority is fused with rule and coercion, independence is zero, and exit from the displayed allegiance is closed. In the terms of this paper, that is $\lambda=0$, $Q^{\pI}$ near zero, and high $C_{\pP\pI}$, $C_{\pI\pC}$ and coupling to exchange. \citet{ellul1977} read the beasts as political power and its propaganda, and \citet{wink1992} described the powers as institutions whose spirituality can become a domination system. Both readings are compatible with the structural interpretation adopted here, on which any authority, religious or secular, can occupy the position of the second beast when its speech is captured by rule. No church, university, newsroom or medical body occupies that position by virtue of what it is.
   696	
   697	\section{Objections and scope conditions}
   698	\label{sec:objections}
   699	
   700	\subsection{Vacuity}
   701	
   702	If the legitimation function were defined so broadly that any social activity belonged to it, the necessity claim would be empty. The definition excludes much. A practice belongs to the class only if it regularly changes members' beliefs about rules, officials or relevant facts and if members rely on the changed beliefs to coordinate. Private reflection, idiosyncratic opinion and persuasion without effect on compliance are excluded. The theorem can fail if its assumptions fail, and Section~\ref{sec:necessity} names the observation that would refute it. A claim with a stated falsifier is not vacuous.
   703	
   704	\subsection{Ideology critique}
   705	
   706	A Marxian critic may object that the paper treats legitimation too neutrally, as coordination, when its historical role has been to secure acceptance of domination. The endorsement model answers part of the objection. It identifies when legitimation misleads, through captured endorsement and the deception gap, and it predicts that coalitions with unsound rules push independence to its floor. What the model does not do is presume that every legitimating belief is false. That presumption would require the counterfactual preferences that \citet{lukes2005} acknowledged are hard to observe, and it would make the framework unable to distinguish a sound public-health rule from an unsound one. The difference between the two is the substance of Proposition~\ref{prop:ideological-power:credibility}.
   707	
   708	\subsection{Expertise and faith}
   709	
   710	A defender of science, medicine or religion may object that classing these institutions as ideological power disparages them. The classification concerns the function they perform for coordination, not the truth of what they teach. A physician who certifies that a vaccine is safe, a jurist who explains a rule of inheritance and a priest who instructs a congregation each change beliefs that others rely on. The results of this paper give independent authorities their value: their endorsement is informative because it is independent, and they protect the public precisely when a coalition's rule is unsound. The source framework's caution applies throughout: a hospital is not a propaganda organ and a professor is not an agent of command \citep{largo2026hbs}. The paper is silent on the truth of any faith's claims, and the theological reading of Section~\ref{sec:revelation} rests on a distinction that Revelation itself draws between witness and enforced display.
   711	
   712	\subsection{Measurement of belief}
   713	
   714	Belief is internal, while the control share $s^{\pI}$ is defined over observable outputs such as appointments, accreditation and reach. A critic may object that control over outputs is not control over minds. The objection is correct and is the reason the definition is restricted to outputs. Persuasion studies \citep{dellavigna2007,enikolopov2011} show that control over channels changes behavior, which is the evidence that edges in this layer are real. Whether a given share of outputs translates into a given share of influence is an empirical question that the indicators of Table~\ref{tab:indicators} are designed to address.
   715	
   716	\subsection{Scope conditions}
   717	
   718	The comparative claims are qualitative codings from secondary literature. Nothing in Section~\ref{sec:comparative} estimates the frequency of capture in any regime type, and the historical illustrations are not a sample. They show how the function is held in each type; they do not show how often it is captured.
   719	
   720	The regime types are ideal types with large internal variation. The comparative sections record that variation for Islamic states and Catholic monarchies in particular, and it holds for the other four types as well.
   721	
   722	The formal models are deliberately simple. They treat soundness as binary, independence as a probability and disclosure as independent across authorities given their type. Richer models would change magnitudes. The directions established by the proofs depend only on the monotonicity and convexity properties used there.
   723	
   724	\section{Conclusion}
   725	\label{sec:conclusion}
   726	
   727	Every persistent human collective with turnover and locally variable rules implements a recognition function: a recurring public practice that makes its rules common knowledge. That much follows from the coordination axiom, and the stateless societies of the ethnographic record show the function carried by talk, ridicule, ritual and kinship idiom without any office. Belief in the rightness of rules does not follow, and regimes vary widely in how much of it they command.
   728	
   729	The question that separates regimes is therefore not whether they have an ideological pillar but how independent its authorities are. A captured authority's endorsement carries no information. Independence helps coalitions with sound rules and hurts coalitions with unsound ones, so the institutional floor of independence, secured by endowments, tenure, constitutional protection or transnational appointment, protects the public in the cases where protection matters. Coordinated control of many authorities lowers the chance that an error is disclosed even when their average independence is unchanged, which is why integration across pillars, and not concentration within one, is the condition to measure.
   730	
   731	The six regime types distribute the function differently. Market economies couple it to finance, party-states to appointment and coercion, social democracies to labor organizations, Islamic states and Catholic monarchies to religious authorities whose independence from rulers varied from substantial to nil, and secular democracies to a legally plural public sphere. The comparative codings remain qualitative, and the hypotheses of Section~\ref{sec:measurement} state what evidence would overturn them. The existence of the pillar is universal, as Proposition A holds; its capture is a contingent and measurable condition, as Proposition B holds, and the first does not entail the second.
   732	
   733	\begin{thebibliography}{200}
   734	\small
   735	\raggedright
   736	
   737	\bibitem[Abbott(1988)]{abbott1988}
   738	Abbott, Andrew (1988). \emph{The System of Professions: An Essay on the Division of Expert Labor}. University of Chicago Press. doi:10.7208/chicago/9780226189666.001.0001.
   739	
   740	\bibitem[Al-Rasheed(2002)]{alrasheed2002}
   741	Al-Rasheed, Madawi (2002). \emph{A History of Saudi Arabia}. Cambridge University Press. doi:10.1017/cbo9780511993510.
   742	
   743	\bibitem[Allcott and Gentzkow(2017)]{allcott2017}
   744	Allcott, Hunt and Matthew Gentzkow (2017). Social Media and Fake News in the 2016 Election. \emph{Journal of Economic Perspectives} 31(2):211-236. doi:10.1257/jep.31.2.211.
   745	
   746	\bibitem[Althusser(1971)]{althusser1971}
   747	Althusser, Louis (1971). Ideology and Ideological State Apparatuses (Notes towards an Investigation). In \emph{Lenin and Philosophy and Other Essays}. Monthly Review Press.
   748	
   749	\bibitem[Arjomand(1988)]{arjomand1988}
   750	Arjomand, Said Amir (1988). \emph{The Turban for the Crown: The Islamic Revolution in Iran}. Oxford University Press.
   751	
   752	\bibitem[Aumann(1976)]{aumann1976}
   753	Aumann, Robert J. (1976). Agreeing to Disagree. \emph{The Annals of Statistics} 4(6):1236-1239. doi:10.1214/aos/1176343654.
   754	
   755	\bibitem[Bachrach and Baratz(1962)]{bachrach1962}
   756	Bachrach, Peter and Morton S. Baratz (1962). Two Faces of Power. \emph{American Political Science Review} 56(4):947-952. doi:10.2307/1952796.
   757	
   758	\bibitem[Barkey(2008)]{barkey2008}
   759	Barkey, Karen (2008). \emph{Empire of Difference: The Ottomans in Comparative Perspective}. Cambridge University Press. doi:10.1017/cbo9780511790645.
   760	
   761	\bibitem[Bauckham(1993)]{bauckham1993}
   762	Bauckham, Richard (1993). \emph{The Theology of the Book of Revelation}. Cambridge University Press. doi:10.1017/cbo9780511819858.
   763	
   764	\bibitem[Beale(1999)]{beale1999}
   765	Beale, G. K. (1999). \emph{The Book of Revelation: A Commentary on the Greek Text}. Eerdmans (NIGTC).
   766	
   767	\bibitem[Becker and Woessmann(2009)]{becker2009}
   768	Becker, Sascha O. and Ludger Woessmann (2009). Was Weber Wrong? A Human Capital Theory of Protestant Economic History. \emph{The Quarterly Journal of Economics} 124(2):531-596. doi:10.1162/qjec.2009.124.2.531.
   769	
   770	\bibitem[Bekelman et~al.(2003)]{bekelman2003}
   771	Bekelman, Justin E., Yan Li and Cary P. Gross (2003). Scope and Impact of Financial Conflicts of Interest in Biomedical Research: A Systematic Review. \emph{JAMA} 289(4):454-465. doi:10.1001/jama.289.4.454.
   772	
   773	\bibitem[Berkey(1992)]{berkey1992}
   774	Berkey, Jonathan (1992). \emph{The Transmission of Knowledge in Medieval Cairo: A Social History of Islamic Education}. Princeton University Press. doi:10.1515/9781400862580.
   775	
   776	\bibitem[Berman(2006)]{berman2006}
   777	Berman, Sheri (2006). \emph{The Primacy of Politics: Social Democracy and the Making of Europe's Twentieth Century}. Cambridge University Press. doi:10.1017/cbo9780511791109.
   778	
   779	\bibitem[Besley and Prat(2006)]{besley2006}
   780	Besley, Timothy and Andrea Prat (2006). Handcuffs for the Grabbing Hand? Media Capture and Government Accountability. \emph{American Economic Review} 96(3):720-736. doi:10.1257/aer.96.3.720.
   781	
   782	\bibitem[Boehm(1999)]{boehm1999}
   783	Boehm, Christopher (1999). \emph{Hierarchy in the Forest: The Evolution of Egalitarian Behavior}. Harvard University Press. doi:10.2307/j.ctvjf9xr4.
   784	
   785	\bibitem[Boehm(2012)]{boehm2012}
   786	Boehm, Christopher (2012). \emph{Moral Origins: The Evolution of Virtue, Altruism, and Shame}. Basic Books.
   787	
   788	\bibitem[Bossuet(1990)]{bossuet1990}
   789	Bossuet, Jacques-B\'enigne (1990). \emph{Politics Drawn from the Very Words of Holy Scripture} (1709), ed. Riley. Cambridge University Press.
   790	
   791	\bibitem[Bourdieu(1989)]{bourdieu1989}
   792	Bourdieu, Pierre (1989). Social Space and Symbolic Power. \emph{Sociological Theory} 7(1):14-25. doi:10.2307/202060.
   793	
   794	\bibitem[Bourdieu(1991)]{bourdieu1991}
   795	Bourdieu, Pierre (1991). \emph{Language and Symbolic Power}. Harvard University Press.
   796	
   797	\bibitem[Bourdieu and Passeron(1977)]{bourdieu1977}
   798	Bourdieu, Pierre and Jean-Claude Passeron (1977). \emph{Reproduction in Education, Society and Culture}. Sage.
   799	
   800	\bibitem[Boyer(1992)]{boyer1992}
   801	Boyer, Paul (1992). \emph{When Time Shall Be No More: Prophecy Belief in Modern American Culture}. Harvard University Press (Belknap). doi:10.2307/jj.41480279.
   802	
   803	\bibitem[Brooks(2000)]{brooks2000}
   804	Brooks, Jeffrey (2000). \emph{Thank You, Comrade Stalin! Soviet Public Culture from Revolution to Cold War}. Princeton University Press.
   805	
   806	\bibitem[Burke(1992)]{burke1992}
   807	Burke, Peter (1992). \emph{The Fabrication of Louis XIV}. Yale University Press.
   808	
   809	\bibitem[Carpenter(2010)]{carpenter2010}
   810	Carpenter, Daniel P. (2010). \emph{Reputation and Power: Organizational Image and Pharmaceutical Regulation at the FDA}. Princeton University Press. doi:10.1515/9781400835119.
   811	
   812	\bibitem[Casanova(1994)]{casanova1994}
   813	Casanova, Jos\'e (1994). \emph{Public Religions in the Modern World}. University of Chicago Press. doi:10.7208/chicago/9780226190204.001.0001.
   814	
   815	\bibitem[Chwe(2001)]{chwe2001}
   816	Chwe, Michael Suk-Young (2001). \emph{Rational Ritual: Culture, Coordination, and Common Knowledge}. Princeton University Press. doi:10.23943/princeton/9780691158280.001.0001.
   817	
   818	\bibitem[Clastres(1987)]{clastres1987}
   819	Clastres, Pierre (1987). \emph{Society against the State: Essays in Political Anthropology} (1974), trans. Robert Hurley. Zone Books. doi:10.2307/j.ctv1595m3p.
   820	
   821	\bibitem[Collins(1984)]{collins1984}
   822	Collins, Adela Yarbro (1984). \emph{Crisis and Catharsis: The Power of the Apocalypse}. Westminster Press.
   823	
   824	\bibitem[Commins(2006)]{commins2006}
   825	Commins, David (2006). \emph{The Wahhabi Mission and Saudi Arabia}. I. B. Tauris. doi:10.5040/9780755609444.
   826	
   827	\bibitem[Coppedge et~al.(2011)]{coppedge2011}
   828	Coppedge, Michael, John Gerring, David Altman, et al. (2011). Conceptualizing and Measuring Democracy: A New Approach. \emph{Perspectives on Politics} 9(2):247-267. doi:10.1017/S1537592711000880.
   829	
   830	\bibitem[Crone(2004)]{crone2004}
   831	Crone, Patricia (2004). \emph{God's Rule: Government and Islam: Six Centuries of Medieval Islamic Political Thought}. Columbia University Press.
   832	
   833	\bibitem[Crone and Hinds(1986)]{crone1986}
   834	Crone, Patricia and Martin Hinds (1986). \emph{God's Caliph: Religious Authority in the First Centuries of Islam}. Cambridge University Press.
   835	
   836	\bibitem[DellaVigna and Kaplan(2007)]{dellavigna2007}
   837	DellaVigna, Stefano and Ethan Kaplan (2007). The Fox News Effect: Media Bias and Voting. \emph{The Quarterly Journal of Economics} 122(3):1187-1234. doi:10.1162/qjec.122.3.1187.
   838	
   839	\bibitem[Djankov et~al.(2003)]{djankov2003}
   840	Djankov, Simeon, Caralee McLiesh, Tatiana Nenova and Andrei Shleifer (2003). Who Owns the Media? \emph{The Journal of Law and Economics} 46(2):341-382. doi:10.1086/377116.
   841	
   842	\bibitem[Eickelman(1992)]{eickelman1992}
   843	Eickelman, Dale F. (1992). Mass Higher Education and the Religious Imagination in Contemporary Arab Societies. \emph{American Ethnologist} 19(4):643-655. doi:10.1525/ae.1992.19.4.02a00010.
   844	
   845	\bibitem[Eickelman and Piscatori(1996)]{eickelman1996}
   846	Eickelman, Dale F. and James Piscatori (1996). \emph{Muslim Politics}. Princeton University Press. doi:10.1515/9780691187785.
   847	
   848	\bibitem[Eisenstein(1979)]{eisenstein1979}
   849	Eisenstein, Elizabeth L. (1979). \emph{The Printing Press as an Agent of Change}. Cambridge University Press. doi:10.1017/cbo9781107049963.
   850	
   851	\bibitem[Ellul(1977)]{ellul1977}
   852	Ellul, Jacques (1977). \emph{Apocalypse: The Book of Revelation}. Seabury Press.
   853	
   854	\bibitem[Elster(1983)]{elster1983}
   855	Elster, Jon (1983). \emph{Explaining Technical Change: A Case Study in the Philosophy of Science}. Cambridge University Press.
   856	
   857	\bibitem[Emmerson and McGinn(1992)]{emmerson1992}
   858	Emmerson, Richard K. and Bernard McGinn (eds.) (1992). \emph{The Apocalypse in the Middle Ages}. Cornell University Press.
   859	
   860	\bibitem[Enikolopov et~al.(2011)]{enikolopov2011}
   861	Enikolopov, Ruben, Maria Petrova and Ekaterina Zhuravskaya (2011). Media and Political Persuasion: Evidence from Russia. \emph{American Economic Review} 101(7):3253-3285. doi:10.1257/aer.101.7.3253.
   862	
   863	\bibitem[Esping-Andersen(1990)]{esping1990}
   864	Esping-Andersen, G\"osta (1990). \emph{The Three Worlds of Welfare Capitalism}. Princeton University Press.
   865	
   866	\bibitem[Evans-Pritchard(1940)]{evanspritchard1940}
   867	Evans-Pritchard, E. E. (1940). \emph{The Nuer: A Description of the Modes of Livelihood and Political Institutions of a Nilotic People}. Clarendon Press.
   868	
   869	\bibitem[Fox(2008)]{fox2008}
   870	Fox, Jonathan (2008). \emph{A World Survey of Religion and the State}. Cambridge University Press. doi:10.1017/cbo9780511993039.
   871	
   872	\bibitem[Fragnito(2001)]{fragnito2001}
   873	Fragnito, Gigliola (2001). \emph{Church, Censorship and Culture in Early Modern Italy}. Cambridge University Press.
   874	
   875	\bibitem[Fraser(1990)]{fraser1990}
   876	Fraser, Nancy (1990). Rethinking the Public Sphere: A Contribution to the Critique of Actually Existing Democracy. \emph{Social Text} 25/26:56-80. doi:10.2307/466240.
   877	
   878	\bibitem[Freidson(1970)]{freidson1970}
   879	Freidson, Eliot (1970). \emph{Profession of Medicine: A Study of the Sociology of Applied Knowledge}. Dodd, Mead.
   880	
   881	\bibitem[Friesen(2001)]{friesen2001}
   882	Friesen, Steven J. (2001). \emph{Imperial Cults and the Apocalypse of John: Reading Revelation in the Ruins}. Oxford University Press. doi:10.1093/0195131533.001.0001.
   883	
   884	\bibitem[Fuller(1995)]{fuller1995}
   885	Fuller, Robert C. (1995). \emph{Naming the Antichrist: The History of an American Obsession}. Oxford University Press. doi:10.1093/acprof:oso/9780195109795.001.0001.
   886	
   887	\bibitem[Gellner(1981)]{gellner1981}
   888	Gellner, Ernest (1981). \emph{Muslim Society}. Cambridge University Press.
   889	
   890	\bibitem[Gellner(1983)]{gellner1983}
   891	Gellner, Ernest (1983). \emph{Nations and Nationalism}. Cornell University Press.
   892	
   893	\bibitem[Gentzkow and Shapiro(2006)]{gentzkow2006}
   894	Gentzkow, Matthew and Jesse M. Shapiro (2006). Media Bias and Reputation. \emph{Journal of Political Economy} 114(2):280-316. doi:10.1086/499414.
   895	
   896	\bibitem[Gerschewski(2013)]{gerschewski2013}
   897	Gerschewski, Johannes (2013). The Three Pillars of Stability: Legitimation, Repression, and Co-optation in Autocratic Regimes. \emph{Democratization} 20(1):13-38. doi:10.1080/13510347.2013.738860.
   898	
   899	\bibitem[Gillespie(2019)]{gillespie2019}
   900	Gillespie, Tarleton (2019). \emph{Custodians of the Internet: Platforms, Content Moderation, and the Hidden Decisions That Shape Social Media}. Yale University Press. doi:10.12987/9780300235029.
   901	
   902	\bibitem[Graeber and Wengrow(2021)]{graeber2021}
   903	Graeber, David and David Wengrow (2021). \emph{The Dawn of Everything: A New History of Humanity}. Farrar, Straus and Giroux.
   904	
   905	\bibitem[Gramsci(1971)]{gramsci1971}
   906	Gramsci, Antonio (1971). \emph{Selections from the Prison Notebooks}, ed. and trans. Hoare and Nowell Smith. International Publishers.
   907	
   908	\bibitem[Granovetter(1978)]{granovetter1978}
   909	Granovetter, Mark (1978). Threshold Models of Collective Behavior. \emph{American Journal of Sociology} 83:1420-1443. doi:10.1086/226707.
   910	
   911	\bibitem[Greitens(2016)]{greitens2016}
   912	Greitens, Sheena Chestnut (2016). \emph{Dictators and Their Secret Police: Coercive Institutions and State Violence}. Cambridge University Press. doi:10.1017/cbo9781316489031.
   913	
   914	\bibitem[Grzymala-Busse(2015)]{grzymala2015}
   915	Grzymala-Busse, Anna (2015). \emph{Nations under God: How Churches Use Moral Authority to Influence Policy}. Princeton University Press. doi:10.1515/9781400866458.
   916	
   917	\bibitem[Grzymala-Busse(2023)]{grzymala2023}
   918	Grzymala-Busse, Anna (2023). \emph{Sacred Foundations: The Religious and Medieval Roots of the European State}. Princeton University Press. doi:10.1515/9780691245133.
   919	
   920	\bibitem[Guess et~al.(2023)]{guess2023}
   921	Guess, Andrew M., Neil Malhotra, Jennifer Pan, et al. (2023). How Do Social Media Feed Algorithms Affect Attitudes and Behavior in an Election Campaign? \emph{Science} 381(6656):398-404. doi:10.1126/science.abp9364.
   922	
   923	\bibitem[Guriev and Treisman(2019)]{guriev2019}
   924	Guriev, Sergei and Daniel Treisman (2019). Informational Autocrats. \emph{Journal of Economic Perspectives} 33(4):100-127. doi:10.1257/jep.33.4.100.
   925	
   926	\bibitem[Guriev and Treisman(2022)]{guriev2022}
   927	Guriev, Sergei and Daniel Treisman (2022). \emph{Spin Dictators: The Changing Face of Tyranny in the 21st Century}. Princeton University Press. doi:10.1515/9780691224466.
   928	
   929	\bibitem[Habermas(1989)]{habermas1989}
   930	Habermas, J\"urgen (1989). \emph{The Structural Transformation of the Public Sphere} (1962), trans. Burger and Lawrence. MIT Press.
   931	
   932	\bibitem[Hallin and Mancini(2004)]{hallin2004}
   933	Hallin, Daniel C. and Paolo Mancini (2004). \emph{Comparing Media Systems: Three Models of Media and Politics}. Cambridge University Press. doi:10.1017/CBO9780511790867.
   934	
   935	\bibitem[Hart(1961)]{hart1961}
   936	Hart, H. L. A. (1961). \emph{The Concept of Law}. Clarendon Press (3rd ed. 2012, Oxford University Press). doi:10.1093/he/9780199644704.001.0001.
   937	
   938	\bibitem[Hayek(1973)]{hayek1973}
   939	Hayek, Friedrich A. (1973). \emph{Law, Legislation and Liberty, Volume 1: Rules and Order}. University of Chicago Press. doi:10.7208/chicago/9780226321233.001.0001.
   940	
   941	\bibitem[Hempel(1959)]{hempel1959}
   942	Hempel, Carl G. (1959). The Logic of Functional Analysis. In Llewellyn Gross (ed.), \emph{Symposium on Sociological Theory}. Harper \& Row.
   943	
   944	\bibitem[Henningsen and Tedeschi(1986)]{henningsen1986}
   945	Henningsen, Gustav and John Tedeschi (eds.) (1986). \emph{The Inquisition in Early Modern Europe: Studies on Sources and Methods}. Northern Illinois University Press.
   946	
   947	\bibitem[Herman and Chomsky(1988)]{herman1988}
   948	Herman, Edward S. and Noam Chomsky (1988). \emph{Manufacturing Consent: The Political Economy of the Mass Media}. Pantheon Books.
   949	
   950	\bibitem[Hsia(1998)]{hsia1998}
   951	Hsia, R. Po-chia (1998). \emph{The World of Catholic Renewal 1540-1770}. Cambridge University Press.
   952	
   953	\bibitem[Imber(1997)]{imber1997}
   954	Imber, Colin (1997). \emph{Ebu's-su'ud: The Islamic Legal Tradition}. Stanford University Press.
   955	
   956	\bibitem[Kamen(1997)]{kamen1997}
   957	Kamen, Henry (1997). \emph{The Spanish Inquisition: A Historical Revision}. Yale University Press.
   958	
   959	\bibitem[Kantorowicz(1957)]{kantorowicz1957}
   960	Kantorowicz, Ernst H. (1957). \emph{The King's Two Bodies: A Study in Mediaeval Political Theology}. Princeton University Press. doi:10.1515/9781400880782.
   961	
   962	\bibitem[Kelly(1995)]{kelly1995}
   963	Kelly, Robert L. (1995). \emph{The Foraging Spectrum: Diversity in Hunter-Gatherer Lifeways}. Smithsonian Institution Press. doi:10.2307/j.ctv2sx9gc9.
   964	
   965	\bibitem[Kenez(1985)]{kenez1985}
   966	Kenez, Peter (1985). \emph{The Birth of the Propaganda State: Soviet Methods of Mass Mobilization, 1917-1929}. Cambridge University Press. doi:10.1017/cbo9780511572623.
   967	
   968	\bibitem[Khomeini(1981)]{khomeini1981}
   969	Khomeini, Ruhollah (1981). \emph{Islam and Revolution: Writings and Declarations of Imam Khomeini}, including \emph{Islamic Government} (1970), trans. Hamid Algar. Mizan Press.
   970	
   971	\bibitem[King et~al.(2013)]{king2013}
   972	King, Gary, Jennifer Pan and Margaret E. Roberts (2013). How Censorship in China Allows Government Criticism but Silences Collective Expression. \emph{American Political Science Review} 107(2):326-343. doi:10.1017/S0003055413000014.
   973	
   974	\bibitem[Koester(2014)]{koester2014}
   975	Koester, Craig R. (2014). \emph{Revelation: A New Translation with Introduction and Commentary}. Yale University Press (Anchor Yale Bible 38A). doi:10.12987/9780300211030.
   976	
   977	\bibitem[Kovacs and Rowland(2004)]{kovacs2004}
   978	Kovacs, Judith and Christopher Rowland (2004). \emph{Revelation: The Apocalypse of Jesus Christ}. Blackwell (Blackwell Bible Commentaries). doi:10.1002/9780470773512.
   979	
   980	\bibitem[Kraybill(1996)]{kraybill1996}
   981	Kraybill, J. Nelson (1996). \emph{Imperial Cult and Commerce in John's Apocalypse}. Sheffield Academic Press (JSNT Supplement 132).
   982	
   983	\bibitem[Kuran(1991)]{kuran1991}
   984	Kuran, Timur (1991). Now Out of Never: The Element of Surprise in the East European Revolution of 1989. \emph{World Politics} 44(1):7-48. doi:10.2307/2010422.
   985	
   986	\bibitem[Kuru(2009)]{kuru2009}
   987	Kuru, Ahmet T. (2009). \emph{Secularism and State Policies toward Religion: The United States, France, and Turkey}. Cambridge University Press. doi:10.1017/cbo9780511815096.
   988	
   989	\bibitem[Kuru(2019)]{kuru2019}
   990	Kuru, Ahmet T. (2019). \emph{Islam, Authoritarianism, and Underdevelopment: A Global and Historical Comparison}. Cambridge University Press. doi:10.1017/9781108296892.
   991	
   992	\bibitem[Lane and Ross(1995)]{lane1995}
   993	Lane, David and Cameron Ross (1995). The CPSU Ruling Elite 1981-1991: Commonalities and Divisions. \emph{Communist and Post-Communist Studies} 28(3):339-360. doi:10.1016/0967-067X(95)00020-U.
   994	
   995	\bibitem[Largo(2026)]{largo2026hbs}
   996	Largo, Mateo (2026). The Hierarchy of the Beast System: Institutional Power, Elite Coordination, and Economic Dependency Across Political Regimes. Unpublished working paper, 14 October 2026.
   997	
   998	\bibitem[Larson(1977)]{larson1977}
   999	Larson, Magali Sarfatti (1977). \emph{The Rise of Professionalism: A Sociological Analysis}. University of California Press. doi:10.1525/9780520323070.
  1000	
  1001	\bibitem[Lee(1979)]{lee1979}
  1002	Lee, Richard B. (1979). \emph{The !Kung San: Men, Women, and Work in a Foraging Society}. Cambridge University Press.
  1003	
  1004	\bibitem[Lee(2013)]{lee2013}
  1005	Lee, Richard B. (2013). \emph{The Dobe Ju/'hoansi}, 4th edition. Wadsworth/Cengage Learning.
  1006	
  1007	\bibitem[Levi(1988)]{levi1988}
  1008	Levi, Margaret (1988). \emph{Of Rule and Revenue}. University of California Press. doi:10.1525/9780520909540.
  1009	
  1010	\bibitem[Lewis(1969)]{lewis1969}
  1011	Lewis, David K. (1969). \emph{Convention: A Philosophical Study}. Harvard University Press.
  1012	
  1013	\bibitem[Lexchin et~al.(2003)]{lexchin2003}
  1014	Lexchin, Joel, Lisa A. Bero, Benjamin Djulbegovic and Otavio Clark (2003). Pharmaceutical Industry Sponsorship and Research Outcome and Quality: Systematic Review. \emph{BMJ} 326(7400):1167-1170. doi:10.1136/bmj.326.7400.1167.
  1015	
  1016	\bibitem[Lukes(2005)]{lukes2005}
  1017	Lukes, Steven (2005). \emph{Power: A Radical View}. Palgrave Macmillan. doi:10.1007/978-0-230-80257-5.
  1018	
  1019	\bibitem[Lundh et~al.(2017)]{lundh2017}
  1020	Lundh, Andreas, Joel Lexchin, Barbara Mintzes, Jeppe B. Schroll and Lisa Bero (2017). Industry Sponsorship and Research Outcome. \emph{Cochrane Database of Systematic Reviews}. doi:10.1002/14651858.MR000033.pub3.
  1021	
  1022	\bibitem[Makdisi(1981)]{makdisi1981}
  1023	Makdisi, George (1981). \emph{The Rise of Colleges: Institutions of Learning in Islam and the West}. Edinburgh University Press. doi:10.1515/9781474470643.
  1024	
  1025	\bibitem[Mann(1986)]{mann1986}
  1026	Mann, Michael (1986). \emph{The Sources of Social Power, Volume 1: A History of Power from the Beginning to A.D. 1760}. Cambridge University Press. doi:10.1017/CBO9780511570896.
  1027	
  1028	\bibitem[Mann(1993)]{mann1993}
  1029	Mann, Michael (1993). \emph{The Sources of Social Power, Volume 2: The Rise of Classes and Nation-States, 1760-1914}. Cambridge University Press. doi:10.1017/CBO9780511570902.
  1030	
  1031	\bibitem[Marshall(1976)]{marshall1976}
  1032	Marshall, Lorna (1976). \emph{The !Kung of Nyae Nyae}. Harvard University Press. doi:10.4159/harvard.9780674180574.
  1033	
  1034	\bibitem[McGinn(1998)]{mcginn1998}
  1035	McGinn, Bernard (1998). \emph{Antichrist: Two Thousand Years of the Human Fascination with Evil}. Columbia University Press.
  1036	
  1037	\bibitem[Menashri(1992)]{menashri1992}
  1038	Menashri, David (1992). \emph{Education and the Making of Modern Iran}. Cornell University Press.
  1039	
  1040	\bibitem[Merton(1968)]{merton1968}
  1041	Merton, Robert K. (1968). \emph{Social Theory and Social Structure}, enlarged edition. Free Press.
  1042	
  1043	\bibitem[Monderer and Samet(1989)]{monderer1989}
  1044	Monderer, Dov and Dov Samet (1989). Approximating Common Knowledge with Common Beliefs. \emph{Games and Economic Behavior} 1:170-190. doi:10.1016/0899-8256(89)90017-1.
  1045	
  1046	\bibitem[Oreskes(2019)]{oreskes2019}
  1047	Oreskes, Naomi (2019). \emph{Why Trust Science?} Princeton University Press. doi:10.1515/9780691222370.
  1048	
  1049	\bibitem[Oreskes and Conway(2010)]{oreskes2010}
  1050	Oreskes, Naomi and Erik M. Conway (2010). \emph{Merchants of Doubt}. Bloomsbury Press.
  1051	
  1052	\bibitem[Ostrom(1990)]{ostrom1990}
  1053	Ostrom, Elinor (1990). \emph{Governing the Commons: The Evolution of Institutions for Collective Action}. Cambridge University Press. doi:10.1017/CBO9780511807763.
  1054	
  1055	\bibitem[Philpott(2007)]{philpott2007}
  1056	Philpott, Daniel (2007). Explaining the Political Ambivalence of Religion. \emph{American Political Science Review} 101(3):505-525. doi:10.1017/s0003055407070372.
  1057	
  1058	\bibitem[Price(1984)]{price1984}
  1059	Price, S. R. F. (1984). \emph{Rituals and Power: The Roman Imperial Cult in Asia Minor}. Cambridge University Press.
  1060	
  1061	\bibitem[Roberts(2018)]{roberts2018}
  1062	Roberts, Margaret E. (2018). \emph{Censored: Distraction and Diversion Inside China's Great Firewall}. Princeton University Press. doi:10.2307/j.ctvc77b21.
  1063	
  1064	\bibitem[Rothstein(1996)]{rothstein1996}
  1065	Rothstein, Bo (1996). \emph{The Social Democratic State: The Swedish Model and the Bureaucratic Problem of Social Reforms}. University of Pittsburgh Press. doi:10.2307/jj.13110785.
  1066	
  1067	\bibitem[Rubin(2017)]{rubin2017}
  1068	Rubin, Jared (2017). \emph{Rulers, Religion, and Riches: Why the West Got Rich and the Middle East Did Not}. Cambridge University Press. doi:10.1017/9781139568272.
  1069	
  1070	\bibitem[Rubinstein(1992)]{rubinstein1992}
  1071	Rubinstein, Ariel (1992). The Electronic Mail Game: Strategic Behavior under ``Almost Common Knowledge''. In \emph{Knowledge, Belief, and Strategic Interaction}. Cambridge University Press. doi:10.1017/cbo9780511983474.019.
  1072	
  1073	\bibitem[Schelling(1960)]{schelling1960}
  1074	Schelling, Thomas C. (1960). \emph{The Strategy of Conflict}. Harvard University Press.
  1075	
  1076	\bibitem[Scott(1985)]{scott1985}
  1077	Scott, James C. (1985). \emph{Weapons of the Weak: Everyday Forms of Peasant Resistance}. Yale University Press. doi:10.12987/9780300153620.
  1078	
  1079	\bibitem[Slaughter and Rhoades(2004)]{slaughter2004}
  1080	Slaughter, Sheila and Gary Rhoades (2004). \emph{Academic Capitalism and the New Economy: Markets, State, and Higher Education}. Johns Hopkins University Press. doi:10.56021/9780801879494.
  1081	
  1082	\bibitem[Starr(1982)]{starr1982}
  1083	Starr, Paul (1982). \emph{The Social Transformation of American Medicine}. Basic Books.
  1084	
  1085	\bibitem[Stepan(2000)]{stepan2000}
  1086	Stepan, Alfred (2000). Religion, Democracy, and the Twin Tolerations. \emph{Journal of Democracy} 11(4):37-57. doi:10.1353/jod.2000.0088.
  1087	
  1088	\bibitem[Stockmann(2013)]{stockmann2013}
  1089	Stockmann, Daniela (2013). \emph{Media Commercialization and Authoritarian Rule in China}. Cambridge University Press. doi:10.1017/cbo9781139087742.
  1090	
  1091	\bibitem[Svolik(2012)]{svolik2012}
  1092	Svolik, Milan W. (2012). \emph{The Politics of Authoritarian Rule}. Cambridge University Press. doi:10.1017/CBO9781139176040.
  1093	
  1094	\bibitem[Van Kley(1996)]{vankley1996}
  1095	Van Kley, Dale K. (1996). \emph{The Religious Origins of the French Revolution: From Calvin to the Civil Constitution, 1560-1791}. Yale University Press.
  1096	
  1097	\bibitem[Weber(1978)]{weber1978}
  1098	Weber, Max (1978). \emph{Economy and Society: An Outline of Interpretive Sociology}. University of California Press. doi:10.4159/9780674240827.
  1099	
  1100	\bibitem[Wiessner(2005)]{wiessner2005}
  1101	Wiessner, Polly (2005). Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity? \emph{Human Nature} 16(2):115-145. doi:10.1007/s12110-005-1000-9.
  1102	
  1103	\bibitem[Wink(1992)]{wink1992}
  1104	Wink, Walter (1992). \emph{Engaging the Powers: Discernment and Resistance in a World of Domination}. Fortress Press. doi:10.2307/j.ctt1tm7j16.
  1105	
  1106	\bibitem[Wintrobe(1998)]{wintrobe1998}
  1107	Wintrobe, Ronald (1998). \emph{The Political Economy of Dictatorship}. Cambridge University Press. doi:10.1017/cbo9781139174916.
  1108	
  1109	\bibitem[Woodburn(1982)]{woodburn1982}
  1110	Woodburn, James (1982). Egalitarian Societies. \emph{Man (N.S.)} 17(3):431-451. doi:10.2307/2801707.
  1111	
  1112	\bibitem[Zaman(2002)]{zaman2002}
  1113	Zaman, Muhammad Qasim (2002). \emph{The Ulama in Contemporary Islam: Custodians of Change}. Princeton University Press. doi:10.2307/j.ctt7rh2s.
  1114	
  1115	\end{thebibliography}
  1116	
  1117	\end{document}

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'rg -n -i "(''^!|error|warning|undefined|multiply defined|overfull|underfull|missing|rerun|citation|reference|label|badness|font warning|package .* warning)" papers/latex/ideological-power.log papers/latex/ideological-power.tex' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
papers/latex/ideological-power.log:599:Package: infwarerr 2019/12/03 v1.5 Providing info/warning/error messages (HO)
papers/latex/ideological-power.log:612:Package: refcount 2019/12/15 v3.6 Data extraction from label references (HO)
papers/latex/ideological-power.log:616:Package: gettitlestring 2019/12/15 v1.6 Cleanup title references (HO)
papers/latex/ideological-power.log:689:(/usr/local/texlive/2026/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
papers/latex/ideological-power.log:690:Package: rerunfilecheck 2025-06-21 v1.11 Rerun checks for auxiliary files (HO)
papers/latex/ideological-power.log:695:Package uniquecounter Info: New unique counter `rerunfilecheck' on input line 2
papers/latex/ideological-power.log:710:LaTeX Info: Redefining \labelcref on input line 2370.
papers/latex/ideological-power.log:711:LaTeX Info: Redefining \labelcpageref on input line 2370.
papers/latex/ideological-power.log:927:Package rerunfilecheck Info: File `ideological-power.out' has not changed.
papers/latex/ideological-power.log:928:(rerunfilecheck)             Checksum: 176B9E8A59F505980886727E92B557A2;9611.
papers/latex/ideological-power.tex:33:% Pillar labels (sans serif) and shared objects; notation follows the series notation file.
papers/latex/ideological-power.tex:58:Every governance system must settle who shapes the beliefs on which cooperation depends. This paper treats that question as the ideological pillar of a six-pillar model of governance and asks two things of it: whether the pillar is necessary, and when it becomes an instrument of capture. From a coordination axiom, together with membership turnover and the cross-cultural variability of rules, we derive that every persistent collective implements a recognition function: a recurring public practice that makes the operative rules common knowledge. The derivation establishes the necessity of a function, not of any institution, and it does not establish that belief in the rightness of rules is necessary. Stateless and egalitarian societies implement the function through talk, ridicule, ritual and kinship idiom, without a designated office. A Bayesian endorsement model then shows that a captured authority's endorsement carries no information, that independent authorities raise expected public confidence in sound rules and lower it for unsound ones, and that coordinated control of several authorities lowers the probability that an error is disclosed below the level reached by independent control with the same average independence. We compare how academia, religious institutions, media, schools and medical and scientific bodies hold the function in market-capitalist, communist party-state, social-democratic, Islamic, Catholic-monarchical and secular-democratic regimes, and we state hypotheses with falsifiers. The comparative codings are qualitative and drawn from secondary literature; no concentration or integration index is estimated for any real polity.
papers/latex/ideological-power.tex:62:\label{sec:intro}
papers/latex/ideological-power.tex:66:The series rests on a single claim: the ideology changes; the institutional functions remain. Six questions recur in every governance system. Who controls the resources ($\pF$)? Who makes the laws ($\pP$)? Who interprets them ($\pJ$)? Who shapes the beliefs ($\pI$)? Who enforces the rules ($\pC$)? Who produces the wealth that sustains everything ($\pW$)? The framework adapts the five-function Hierarchy of the Beast System developed by \citet{largo2026hbs}, whose rule function is split here into rule-making and adjudication. The name comes from Revelation 13, which describes a system binding authority, allegiance and economic participation. In this series the name designates the universal six-function structure itself. It is never a label for any religion, people, profession, regime or person.
papers/latex/ideological-power.tex:70:The ideological pillar poses these tasks in a sharp form. Its institutions include universities, churches, mosques and seminaries, newsrooms, schools, academies of science and medical bodies. These institutions command trust because they are expected to report what they find rather than what rulers prefer. They can check capture by disclosing errors and refusing endorsement. They can also enable capture by lending credibility to rules that serve a narrow coalition. Nothing in this paper implies that expertise, medicine, science or any faith is fraudulent. The source framework says plainly that a hospital is not a propaganda organ and a professor is not an agent of command \citep{largo2026hbs}. The analytical question is when the independence that gives these authorities their value is preserved, and when it is lost.
papers/latex/ideological-power.tex:74:Independent authorities raise public confidence in sound rules and lower it in unsound ones, while a captured authority's endorsement conveys no information (Proposition~\ref{prop:ideological-power:credibility}). When one coalition controls the appointment of several authorities, an error is less likely to be disclosed than when the same authorities are appointed independently with the same average independence (Proposition~\ref{prop:ideological-power:disclosure}). These results organize a comparison of six regime types and a set of hypotheses, each with a stated falsifier.
papers/latex/ideological-power.tex:79:\label{sec:layer}
papers/latex/ideological-power.tex:89:\label{eq:integration}
papers/latex/ideological-power.tex:92:A capture link $(i\to j,m)$ is influence that meets three conditions: privileged access or discretion, a resulting weakening of applicable accountability or contestability, and material evidence tying the asymmetry to an institutional output. In the aggregate state vector $x_t=(F_t,P_t,J_t,I^{cap}_t,C_t,W_t)$ the ideological capacity is written $I^{cap}_t$. The pillar label is the sans-serif $\pI$ and the integration statistic is the calligraphic $\Int_t$; the two are never interchanged.
papers/latex/ideological-power.tex:101:\label{def:ideological-power:legitimation}
papers/latex/ideological-power.tex:108:\label{def:ideological-power:recognition}
papers/latex/ideological-power.tex:115:\label{def:ideological-power:authority}
papers/latex/ideological-power.tex:128:\label{def:ideological-power:public-signal}
papers/latex/ideological-power.tex:135:\label{lem:ideological-power:public-signal}
papers/latex/ideological-power.tex:165:\label{def:ideological-power:qi}
papers/latex/ideological-power.tex:181:\label{sec:necessity}
papers/latex/ideological-power.tex:190:\label{ax:coordination}
papers/latex/ideological-power.tex:195:\label{ax:turnover}
papers/latex/ideological-power.tex:200:\label{ax:noninnate}
papers/latex/ideological-power.tex:207:\label{lem:ideological-power:renewal}
papers/latex/ideological-power.tex:220:\label{thm:ideological-power:necessity}
papers/latex/ideological-power.tex:240:\label{rem:ideological-power:scope}
papers/latex/ideological-power.tex:249:\label{prop:ideological-power:minimal-form}
papers/latex/ideological-power.tex:259:\label{tab:minimal}
papers/latex/ideological-power.tex:266:Amazonian chiefdoms & The chief's duty of public speech, which recalls traditional norms, and myth shared by the group \citep{clastres1987} & The chief commands nothing. Reply: the chief's speech is a public recitation of norms without power to command. \\
papers/latex/ideological-power.tex:278:\citet{clastres1987} described Amazonian chiefs whose authority rested on generosity and speech. The chief's daily discourse recalls the traditional norms of the group; it is a public recitation, not a command, and a chief who tries to command loses his following. Clastres read these societies as actively preventing the political function from separating from society. The reading is consistent with Theorem~\ref{thm:ideological-power:necessity}: the function exists, its holder has no power to enforce it, and concentration is prevented by design. Clastres' evidence has been criticized as selective, and the case should be read with that caution.
papers/latex/ideological-power.tex:300:Two classic errors of functionalism must be avoided. \citet{hempel1959} showed that from the premise that a function is needed one cannot infer that a particular institution exists, because functional equivalents may meet the need. Theorem~\ref{thm:ideological-power:necessity} respects this limit: it asserts that some practice in a class is implemented, and the class includes campfire talk and state broadcasting alike. \citet{elster1983} argued that explaining an institution by its beneficial effects requires a feedback mechanism from effect to institution. The theorem is not such an explanation. It is a condition of persistence: collectives that lack the function do not function, whatever the reason the function arose. It does not explain why a given regime has a ministry of religious affairs or a public broadcaster, and the comparative sections never use it for that purpose. \citet{merton1968} supplies the remaining vocabulary: the manifest function of a university is teaching and research, and its latent function in the ideological layer may include certifying elites, which is a separate empirical question.
papers/latex/ideological-power.tex:303:\label{sec:literature}
papers/latex/ideological-power.tex:313:\citet{bachrach1962} argued that power is exercised not only in decisions but also in non-decisions, by keeping issues off the agenda. \citet{lukes2005} added a third dimension: the power to shape preferences so that conflicts of interest never surface. Part II owns agenda control, the power to determine which proposals reach a decision, as an object of rule-making (Definition 2.9 of Part II). The third dimension belongs here, because shaping preferences is shaping beliefs. The difficulty Lukes acknowledged is measurement: claims about preferences that people would hold but for ideological influence require a counterfactual that is hard to observe. The endorsement model of Section~\ref{sec:mechanisms} sidesteps the problem by studying a narrower and observable quantity, the information content of an authority's statements.
papers/latex/ideological-power.tex:327:Authoritarian information control has its own literature. \citet{king2013} analyzed censorship of Chinese social media and found that posts criticizing the state were often left standing while posts with potential for collective action were removed. \citet{stockmann2013} found that commercialized Chinese media were perceived as more credible than official outlets and could therefore carry the party's messages more persuasively. \citet{guriev2019,guriev2022} described a shift from rule by fear to rule by spin, in which leaders manipulate information while simulating democratic forms; Part II treats this as a strategy of rule-makers. \citet{kuran1991} analyzed preference falsification, in which citizens publicly support regimes they privately oppose, and explained why the revolutions of 1989 surprised observers.
papers/latex/ideological-power.tex:348:\label{sec:comparative}
papers/latex/ideological-power.tex:364:The documented checks are also sectoral. Competition among outlets makes media capture costly \citep{besley2006}. Demand-side slant \citep{gentzkow2006} is a rival explanation for partisan coverage that does not require owner control, so evidence of slant is not by itself evidence of capture. Disclosure rules, peer review, replication and the reputational autonomy of regulators \citep{carpenter2010} raise $\lambda$. The capture episodes above were themselves discovered through litigation, journalism and meta-research, which is what source hypothesis H4 predicts: higher rates of documented error discovery can signal stronger accountability rather than more capture \citep{largo2026hbs}.
papers/latex/ideological-power.tex:374:Public benefits are part of the record. The early Soviet literacy campaigns that \citet{kenez1985} described expanded the population that could read, including what the party did not print. Source Proposition 4, that public benefit is compatible with hierarchy, applies here as elsewhere \citep{largo2026hbs}. The documented checks are weak in formal terms: there is no lawful independent press and no protected academic freedom. They consist of elite factions, professional norms within the sciences, and the preference falsification that makes displayed support an unreliable guide to private belief.
papers/latex/ideological-power.tex:424:\label{tab:regimes}
papers/latex/ideological-power.tex:440:\label{sec:mechanisms}
papers/latex/ideological-power.tex:453:\label{def:ideological-power:endorsement}
papers/latex/ideological-power.tex:460:\label{prop:ideological-power:credibility}
papers/latex/ideological-power.tex:498:\label{prop:ideological-power:tradeoff}
papers/latex/ideological-power.tex:527:\label{prop:ideological-power:covert}
papers/latex/ideological-power.tex:544:\label{cor:ideological-power:gap}
papers/latex/ideological-power.tex:554:\subsection{Correlated control and the discovery of error}
papers/latex/ideological-power.tex:556:Most polities have many legitimating authorities. Whether they detect and disclose an error depends on how many of them are independent, and on whether their independence is correlated. Integration across pillars, in the source's sense, typically works by correlation: when one coalition appoints the editors, the rectors and the chief jurists, they are captured together or not at all.
papers/latex/ideological-power.tex:559:\label{prop:ideological-power:disclosure}
papers/latex/ideological-power.tex:560:Let $K\geq2$ authorities each be independent with probability $\lambda\in(0,1)$, with an arbitrary joint distribution of independence across authorities, and let $N$ be the number of independent authorities. Given the set of independent authorities, each independently discovers and discloses a given error with probability $p\in(0,1)$; captured authorities never disclose. Let $D=\Prob(\text{at least one disclosure})$.
papers/latex/ideological-power.tex:579:\label{cor:ideological-power:integration}
papers/latex/ideological-power.tex:580:Holding fixed the number of authorities and the average probability that each is independent, a change in appointment structure that makes the independence of authorities perfectly correlated lowers the probability that an error is disclosed from $1-(1-\lambda p)^K$ to $\lambda(1-(1-p)^K)$.
papers/latex/ideological-power.tex:587:Ideological control often aims at public displays: attendance, applause, signatures, votes in uncontested elections. The beliefs those displays reveal are a separate matter. A threshold model, of the kind \citet{granovetter1978} introduced for collective behavior and \citet{kuran1991} applied to preference falsification, shows how far the two can diverge.
papers/latex/ideological-power.tex:590:\label{prop:ideological-power:fragility}
papers/latex/ideological-power.tex:621:\label{sec:measurement}
papers/latex/ideological-power.tex:629:\label{tab:indicators}
papers/latex/ideological-power.tex:653:\label{tab:hypotheses}
papers/latex/ideological-power.tex:661:HI4 Correlated control & With average independence fixed, systems where one body appoints most authorities show less documented error correction. & Equal or higher correction under common appointment. \\
papers/latex/ideological-power.tex:670:Three identification problems deserve emphasis. Discovery and capture are confounded: a high rate of documented error may mean many errors or strong review, so HI4 must compare correction given comparable exposure, as source hypothesis H4 already notes. Selection of cases from scandals biases every estimate toward finding capture, which is why the population must be preregistered. And indicators of displayed support are invalid where contestability is low, by Proposition~\ref{prop:ideological-power:fragility}, so private measures such as list experiments are needed. None of these problems is peculiar to any regime type, and each applies with equal force to all six.
papers/latex/ideological-power.tex:673:\label{sec:revelation}
papers/latex/ideological-power.tex:695:The normative warning in the text attaches to Proposition B, not to Proposition A. Revelation does not condemn teaching, worship, scholarship or the existence of authorities that shape belief; it is itself an act of witness that seeks to shape belief. Its target is a configuration in which legitimating authority is fused with rule and coercion, independence is zero, and exit from the displayed allegiance is closed. In the terms of this paper, that is $\lambda=0$, $Q^{\pI}$ near zero, and high $C_{\pP\pI}$, $C_{\pI\pC}$ and coupling to exchange. \citet{ellul1977} read the beasts as political power and its propaganda, and \citet{wink1992} described the powers as institutions whose spirituality can become a domination system. Both readings are compatible with the structural interpretation adopted here, on which any authority, religious or secular, can occupy the position of the second beast when its speech is captured by rule. No church, university, newsroom or medical body occupies that position by virtue of what it is.
papers/latex/ideological-power.tex:698:\label{sec:objections}
papers/latex/ideological-power.tex:706:A Marxian critic may object that the paper treats legitimation too neutrally, as coordination, when its historical role has been to secure acceptance of domination. The endorsement model answers part of the objection. It identifies when legitimation misleads, through captured endorsement and the deception gap, and it predicts that coalitions with unsound rules push independence to its floor. What the model does not do is presume that every legitimating belief is false. That presumption would require the counterfactual preferences that \citet{lukes2005} acknowledged are hard to observe, and it would make the framework unable to distinguish a sound public-health rule from an unsound one. The difference between the two is the substance of Proposition~\ref{prop:ideological-power:credibility}.
papers/latex/ideological-power.tex:725:\label{sec:conclusion}
papers/latex/ideological-power.tex:729:The question that separates regimes is therefore not whether they have an ideological pillar but how independent its authorities are. A captured authority's endorsement carries no information. Independence helps coalitions with sound rules and hurts coalitions with unsound ones, so the institutional floor of independence, secured by endowments, tenure, constitutional protection or transnational appointment, protects the public in the cases where protection matters. Coordinated control of many authorities lowers the chance that an error is disclosed even when their average independence is unchanged, which is why integration across pillars, and not concentration within one, is the condition to measure.

hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '550,749p' papers/latex/ideological-power.tex | nl -ba -v550" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   550	\end{proof}
   551	
   552	Capture misleads exactly when audiences overestimate independence. Disclosure rules, conflict-of-interest registries and the publication of appointment and funding records exist to bring $\hat\lambda$ into line with $\lambda$. They do not make authorities independent; they make their dependence visible, which removes the gap.
   553	
   554	\subsection{Correlated control and the discovery of error}
   555	
   556	Most polities have many legitimating authorities. Whether they detect and disclose an error depends on how many of them are independent, and on whether their independence is correlated. Integration across pillars, in the source's sense, typically works by correlation: when one coalition appoints the editors, the rectors and the chief jurists, they are captured together or not at all.
   557	
   558	\begin{proposition}[Disclosure under correlated control]
   559	\label{prop:ideological-power:disclosure}
   560	Let $K\geq2$ authorities each be independent with probability $\lambda\in(0,1)$, with an arbitrary joint distribution of independence across authorities, and let $N$ be the number of independent authorities. Given the set of independent authorities, each independently discovers and discloses a given error with probability $p\in(0,1)$; captured authorities never disclose. Let $D=\Prob(\text{at least one disclosure})$.
   561	\begin{enumerate}
   562	\item[(a)] For every joint distribution, $\lambda\bigl(1-(1-p)^K\bigr)\leq D\leq 1-(1-p)^{\lambda K}$.
   563	\item[(b)] The lower bound is attained if and only if independence is all or nothing, $N\in\{0,K\}$ almost surely, which is the case of perfectly correlated control.
   564	\item[(c)] If independence is drawn independently across authorities, $D=1-(1-\lambda p)^K$, which lies strictly above the lower bound.
   565	\end{enumerate}
   566	\end{proposition}
   567	
   568	\begin{proof}
   569	Conditional on $N$, no disclosure occurs with probability $(1-p)^N$, so $D=1-\E[g(N)]$ with $g(x)=(1-p)^x$, a strictly convex function. By linearity of expectation $\E[N]=\lambda K$.
   570	
   571	(a) For the upper bound, Jensen's inequality gives $\E[g(N)]\geq g(\E N)=(1-p)^{\lambda K}$. For the lower bound, strict convexity places $g$ below its chord on $[0,K]$: $g(x)\leq(1-x/K)g(0)+(x/K)g(K)$, with equality only at $x\in\{0,K\}$. Taking expectations, $\E[g(N)]\leq(1-\lambda)+\lambda(1-p)^K$, so $D\geq\lambda(1-(1-p)^K)$.
   572	
   573	(b) The chord inequality is strict for $x\in(0,K)$, so equality in expectation requires $\Prob(N\in\{0,K\})=1$. Conversely, if $N\in\{0,K\}$ almost surely then $\Prob(N=K)=\lambda$ and $D=\lambda(1-(1-p)^K)$.
   574	
   575	(c) If independence is independent across authorities, $N$ is binomial with parameters $K$ and $\lambda$, and $\E[(1-p)^N]=(1-\lambda+\lambda(1-p))^K=(1-\lambda p)^K$. Since $K\geq2$ and $\lambda\in(0,1)$, $\Prob(0<N<K)>0$, so by (b) the bound is strict.
   576	\end{proof}
   577	
   578	\begin{corollary}[Integration lowers discovery]
   579	\label{cor:ideological-power:integration}
   580	Holding fixed the number of authorities and the average probability that each is independent, a change in appointment structure that makes the independence of authorities perfectly correlated lowers the probability that an error is disclosed from $1-(1-\lambda p)^K$ to $\lambda(1-(1-p)^K)$.
   581	\end{corollary}
   582	
   583	The corollary separates two things that are often merged. Concentration $H^{\pI}$ concerns how many authorities there are and how control is shared among them. Integration concerns whether control over them moves together, which is what high $C_{\pP\pI}$ or $C_{\pF\pI}$ produces when one coalition appoints or funds all of them. A polity can have many universities, newspapers and juristic schools, and so low measured concentration, and still have low discovery if one coalition appoints their heads. The upper bound in (a) is attained only when $\lambda K$ is an integer and $N=\lambda K$ almost surely; otherwise the maximum is reached by a distribution on $\lfloor\lambda K\rfloor$ and $\lceil\lambda K\rceil$. The bound adds a design point: discovery is highest when the number of independent authorities is least variable, which plural appointment by rival bodies secures better than independent chance. This refines source hypothesis H4 on epistemic checks and source Proposition 2 on the interruption of transmission \citep{largo2026hbs}.
   584	
   585	\subsection{Fragility of displayed legitimacy}
   586	
   587	Ideological control often aims at public displays: attendance, applause, signatures, votes in uncontested elections. The beliefs those displays reveal are a separate matter. A threshold model, of the kind \citet{granovetter1978} introduced for collective behavior and \citet{kuran1991} applied to preference falsification, shows how far the two can diverge.
   588	
   589	\begin{proposition}[Fragility]
   590	\label{prop:ideological-power:fragility}
   591	Let $n$ members have thresholds $\tau_i\in[0,1]$: member $i$ expresses dissent publicly when the share of members already doing so is at least $\tau_i$. Let $\Phi(x)=\frac1n\#\{i:\tau_i\leq x\}$ and $x_0=0$, $x_{k+1}=\Phi(x_k)$.
   592	\begin{enumerate}
   593	\item[(a)] The sequence $(x_k)$ is nondecreasing and reaches, within $n+1$ steps, the smallest fixed point $x^\ast$ of $\Phi$.
   594	\item[(b)] There are threshold profiles $\tau$ and $\tau'$ that differ only in one member's threshold, by $1/n$, with $x^\ast(\tau)=1$ and $x^\ast(\tau')=0$.
   595	\end{enumerate}
   596	\end{proposition}
   597	
   598	\begin{proof}
   599	(a) $\Phi$ is nondecreasing. Since $x_1=\Phi(0)\geq0=x_0$, induction gives $x_{k+1}=\Phi(x_k)\geq\Phi(x_{k-1})=x_k$. The sequence takes values in $\{0,1/n,\dots,1\}$, so it is constant from some step $k\leq n$ on, at a fixed point $\bar x$. If $y$ is any fixed point, then $x_0\leq y$, and $x_k\leq y$ implies $x_{k+1}=\Phi(x_k)\leq\Phi(y)=y$, so $\bar x\leq y$.
   600	
   601	(b) Let $\tau_i=(i-1)/n$ for $i=1,\dots,n$. Then $\Phi(k/n)=(k+1)/n$ for $k<n$, so $x_k=k/n$ and $x^\ast=1$. Let $\tau'$ agree with $\tau$ except $\tau'_1=1/n$. No member has threshold $0$, so $\Phi'(0)=0$ and $x^\ast(\tau')=0$.
   602	\end{proof}
   603	
   604	Two populations whose private dispositions are almost identical can display opposite public states. Displayed support is therefore not a sufficient statistic for private belief, and the gap is largest where expression is costly, which is where $Q^{\pI}$ is low. The result explains why regimes that control the ideological layer can appear stable and then collapse quickly, as \citet{kuran1991} argued for 1989. It also constrains measurement: in polities with low contestability, attendance, applause and uncontested votes cannot validate claims about normative legitimacy.
   605	
   606	\subsection{Coupling of belief to coercion and production}
   607	
   608	The series assigns two of the fifteen cross-pillar pairs to this Part for primary treatment.
   609	
   610	The coupling $C_{\pI\pC}$ runs in both directions. Control of belief needs enforcement when it goes beyond persuasion: heresy and blasphemy prosecutions, censorship offices, the licensing of presses and the dismissal of dissenting teachers all require a sanctioning apparatus. The Spanish Inquisition joined doctrinal judgment to coercive power \citep{kamen1997}, and the censorship offices of party-states worked with the security services. Coercion in turn needs belief. Soldiers and police carry out orders when they expect others to do so, and Proposition~\ref{prop:ideological-power:fragility} shows how quickly that expectation can fail. \citet{greitens2016} and the other sources of Part V analyze the coercive institutions themselves, and Part V shows that the refusal of manifestly unlawful orders, one of its checks on coercion, depends on the legitimating beliefs studied here. For the ideological layer, $C_{\pI\pC}$ is the extent to which one coalition both decides what may be said and commands the organizations that punish saying otherwise. It is high where religious courts or security services enforce doctrine and low where independent courts protect expression.
   611	
   612	The coupling $C_{\pI\pW}$ concerns the beliefs of the producing population and the institutions that shape them. Belief-producing specialists need a surplus to live on, a dependency of the ideological on the productive pillar that Part VII derives in general. In the other direction, beliefs shape work and compliance. \citet{levi1988} showed that taxpayers' compliance is quasi-voluntary: it depends on their belief that others comply and that rulers keep their bargains. \citet{becker2009} found that Protestant regions of Prussia had higher literacy, which they attributed to the religious emphasis on reading scripture, and that literacy rather than a work ethic accounts for much of their economic advantage. \citet{gellner1983} argued that industrial economies require a standardized literate culture that only a mass education system can supply, which makes control of schooling central to modern states. \citet{bourdieu1977} argued that schooling also reproduces class position under the appearance of merit. The coupling is high where one coalition controls both the conditions of work and the institutions that teach workers what to expect of it, and low where producers have authorities of their own, such as the labor press and educational associations of social democracies. Part VI treats everyday resistance \citep{scott1985}, which shows that producers do not simply absorb dominant beliefs, and its latent-veto result, that producers can threaten a system's persistence by withdrawing the production it needs (Proposition 3.5 of Part VI), explains why rulers need producers to believe that compliance is expected of everyone.
   613	
   614	\subsection{Checks}
   615	
   616	Each component of $Q^{\pI}$ maps onto a parameter of the models above. Independence raises $\lambda$ and, through the institutional floor $\lambda_{\min}$, protects the public when the coalition's interests are not aligned with soundness (Proposition~\ref{prop:ideological-power:tradeoff}) and when it would capture authorities covertly (Proposition~\ref{prop:ideological-power:covert}). Disclosure aligns the public's estimate $\hat\lambda$ with the truth and closes the deception gap (Corollary~\ref{cor:ideological-power:gap}). Plurality with separate appointment raises the number of authorities and lowers the correlation of their capture (Proposition~\ref{prop:ideological-power:disclosure}). Reviewability raises the discovery probability $p$. Exit lets audiences abandon authorities that lose credibility, which gives authorities a reputational reason to remain independent, the mechanism behind both the demand-side account of \citet{gentzkow2006} and the regulator reputation of \citet{carpenter2010}.
   617	
   618	The historical record shows each check operating. Scholars refused the Abbasid caliph's doctrinal demand \citep{crone1986}. Endowments gave madrasas a revenue base of their own \citep{makdisi1981}. The transnational Church limited the claims of crowns \citep{grzymala2023}, and Jansenist and Gallican counter-publics eroded royal sacrality \citep{vankley1996}. Competition among outlets raises the cost of media capture \citep{besley2006}, and meta-research exposed sponsorship bias in clinical research \citep{lundh2017}. These are the forms that source Proposition 2, that checks can interrupt the transmission of concentrated power, takes in the ideological layer \citep{largo2026hbs}.
   619	
   620	\section{Measurement}
   621	\label{sec:measurement}
   622	
   623	The constructs of this Part are measurable from documents. Table~\ref{tab:indicators} lists indicators for each. All are subject to the source's requirements: weights and thresholds are preregistered, the population of events is defined before data collection rather than drawn from scandals, and measurement invariance is tested before indicators are compared across regime types \citep{largo2026hbs}.
   624	
   625	\begin{table}[t]
   626	\centering
   627	\small
   628	\caption{Indicators for the ideological layer. Each construct can be coded from public documents or existing datasets.}
   629	\label{tab:indicators}
   630	\begin{tabularx}{\textwidth}{@{}L{3.1cm}YL{3.4cm}@{}}
   631	\toprule
   632	Construct & Indicator & Data or design \\
   633	\midrule
   634	Concentration $H^{\pI}$ & Shares of appointments, accreditation decisions and audience reach held by each organization & Ownership data \citep{djankov2003} and appointment records \\
   635	Independence & Tenure protection, editorial autonomy and academic and juristic freedom & Expert-coded indicators \citep{coppedge2011} \\
   636	Disclosure & Share of trials, articles and broadcasts with published funding and conflict statements & Trial registries and journal policies \\
   637	Reviewability & Rates of correction, retraction and successful replication & Retraction and replication records \\
   638	Exit & Legal penalties for unlicensed publication, apostasy or blasphemy & Religion and state coding \citep{fox2008} \\
   639	Censorship practice & What is removed and what is left standing & Audit and observational designs \citep{king2013} \\
   640	Correlated control & Share of authority heads appointed by the same body & Appointment registers and party lists \\
   641	Coupling $C_{\pI\pC}$ & Prosecutions and sanctions for expression and the bodies that order them & Court and security records \\
   642	Platform reach & Shares of ranked and moderated reach held by each platform & Platform disclosures and feed experiments \citep{guess2023} \\
   643	\bottomrule
   644	\end{tabularx}
   645	\end{table}
   646	
   647	The hypotheses below refine the source's hypotheses for this pillar. Each has a stated falsifier. Several are drawn directly from the propositions of Section~\ref{sec:mechanisms}; the others restate claims from the literature in testable form.
   648	
   649	\begin{table}[t]
   650	\centering
   651	\small
   652	\caption{Hypotheses for the ideological pillar, with the observation that would count against each.}
   653	\label{tab:hypotheses}
   654	\begin{tabularx}{\textwidth}{@{}L{3.0cm}YY@{}}
   655	\toprule
   656	Hypothesis & Prediction & Falsifier \\
   657	\midrule
   658	HI1 State media ownership & Greater state ownership of media is associated with weaker accountability outcomes \citep{djankov2003}. & No association after controls, or public broadcasters with plural governance behaving like state-owned media. \\
   659	HI2 Demand and supply of slant & Slant tracks audience composition more than owner identity \citep{gentzkow2006}. & Changes of owner that shift content with audience composition held constant. \\
   660	HI3 Sponsorship and disclosure & Disclosure and registration rules narrow the gap between sponsored and unsponsored conclusions \citep{lundh2017}. & A gap that does not narrow after such rules are introduced. \\
   661	HI4 Correlated control & With average independence fixed, systems where one body appoints most authorities show less documented error correction. & Equal or higher correction under common appointment. \\
   662	HI5 Fragmentation of authority & Mass education and new media raise the number of recognized religious and scholarly authorities \citep{eickelman1996,eisenstein1979}. & No rise in recognized claimants after such expansions. \\
   663	HI6 Credibility premium & Outlets perceived as independent persuade more than official outlets \citep{stockmann2013,enikolopov2011}. & No difference in persuasive effect. \\
   664	HI7 Attacks follow adverse findings & Restrictions on independent authorities follow findings unfavorable to the governing coalition (Proposition~\ref{prop:ideological-power:covert}). & Restrictions unrelated in timing to prior adverse findings. \\
   665	HI8 Hidden opinion & The gap between displayed and privately reported support is larger where contestability is lower \citep{kuran1991}. & No relation between contestability and the gap. \\
   666	\bottomrule
   667	\end{tabularx}
   668	\end{table}
   669	
   670	Three identification problems deserve emphasis. Discovery and capture are confounded: a high rate of documented error may mean many errors or strong review, so HI4 must compare correction given comparable exposure, as source hypothesis H4 already notes. Selection of cases from scandals biases every estimate toward finding capture, which is why the population must be preregistered. And indicators of displayed support are invalid where contestability is low, by Proposition~\ref{prop:ideological-power:fragility}, so private measures such as list experiments are needed. None of these problems is peculiar to any regime type, and each applies with equal force to all six.
   671	
   672	\section{A typological reading of Revelation 13}
   673	\label{sec:revelation}
   674	
   675	\subsection{Method}
   676	
   677	The measurement program above states what evidence would show capture of the ideological pillar. The series pairs it with a normative image of capture drawn from Revelation 13, read typologically. On this reading the beast is a recurring pattern of power that claims ultimate loyalty, and Babylon is the city that organizes commerce and worship around that claim in any age. \citet{bauckham1993} read Rome as the paradigm of such power, and \citet{beale1999} defended an idealist reading that treats the images as transhistorical. The contextual reading anchors the images in the Roman province of Asia, its imperial cult and its trade \citep{koester2014,friesen2001,kraybill1996}. Futurist readings, which take the text to predict a specific future order or person, are excluded by the series' guardrails. Their reception history shows why: \citet{fuller1995} and \citet{boyer1992} document repeated identifications of the beast with contemporary figures, each of which failed. Historicist readings that identified the papacy with the beast belonged to the polemics of the Reformation, as the reception histories of \citet{emmerson1992}, \citet{mcginn1998} and \citet{kovacs2004} document. Any identification of a church, a faith, a profession or a regime with the beast is excluded here for the same reason. What follows is an interpretive claim of this project, offered as an analogy that aids comparison, not as a settled exegetical result.
   678	
   679	\subsection{The second beast as legitimating authority}
   680	
   681	Revelation 13 presents two beasts. The first, from the sea, holds authority and makes war. The second rises from the land and does not rule. In the King James text it ``had two horns like a lamb, and he spake as a dragon'' (13:11). It ``exerciseth all the power of the first beast before him, and causeth the earth and them which dwell therein to worship the first beast'' (13:12), and it ``deceiveth them that dwell on the earth by the means of those miracles which he had power to do'' (13:14). Later chapters name it ``the false prophet that wrought miracles before him'' (19:20).
   682	
   683	The second beast performs the function this paper studies. It produces belief in the authority of the first beast, and it does so through public signs performed ``in the sight of men'' (13:13), which are public events in the sense of Definition~\ref{def:ideological-power:public-signal}. The contextual reading identifies it with the agents of the imperial cult in Asia. \citet{price1984} showed that the cult in Asia Minor was organized largely by the cities and their elites, who used it to represent imperial power within their own civic religion, and \citet{friesen2001} examined its provincial institutions. The legitimation of Roman rule was thus supplied locally, by elites who gained standing from it. In the vocabulary of Section~\ref{sec:mechanisms}, it rested on privileged access exchanged for endorsement.
   684	
   685	The mismatch between the lamb's horns and the dragon's voice is the typological image of the deception gap in Corollary~\ref{cor:ideological-power:gap}. An authority that appears independent and gentle, so that its audience assigns it high $\hat\lambda$, speaks entirely for the ruler, so that its true $\lambda$ is zero. The text calls the result deception. The model calls it a posterior that exceeds the truth by an amount that grows with the gap between perceived and actual independence.
   686	
   687	\subsection{Image, enforcement and exchange}
   688	
   689	The second beast makes an image that speaks and causes ``that as many as would not worship the image of the beast should be killed'' (13:15). The image joins legitimation to coercion, which is the coupling $C_{\pI\pC}$ at its maximum. The text then joins both to economic participation: the second beast causes all ``to receive a mark in their right hand, or in their foreheads: And that no man might buy or sell, save he that had the mark'' (13:16 to 13:17). Displayed allegiance becomes the condition of exchange, which couples the ideological pillar to the financial and productive pillars that Parts I and VI analyze. \citet{kraybill1996} argued that for Christians in Asia, participation in trade guilds and commerce carried obligations to honor the imperial cult, so the image had a concrete social referent. In Revelation 18 the merchants of Babylon ``were the great men of the earth; for by thy sorceries were all nations deceived'' (18:23), an image of commerce and deception bound together that \citet{bauckham1993} reads as part of an economic critique of Rome.
   690	
   691	Proposition~\ref{prop:ideological-power:fragility} supplies a reading of compelled worship. Worship enforced on pain of death is a display whose relation to private belief is unknown, and the text treats it as such: the faithful in Revelation are those who refuse the display. \citet{collins1984} read the book as a response to a crisis perceived by a minority community, and its images express that community's experience of a public culture in which displayed loyalty was demanded.
   692	
   693	\subsection{Scope of the reading}
   694	
   695	The normative warning in the text attaches to Proposition B, not to Proposition A. Revelation does not condemn teaching, worship, scholarship or the existence of authorities that shape belief; it is itself an act of witness that seeks to shape belief. Its target is a configuration in which legitimating authority is fused with rule and coercion, independence is zero, and exit from the displayed allegiance is closed. In the terms of this paper, that is $\lambda=0$, $Q^{\pI}$ near zero, and high $C_{\pP\pI}$, $C_{\pI\pC}$ and coupling to exchange. \citet{ellul1977} read the beasts as political power and its propaganda, and \citet{wink1992} described the powers as institutions whose spirituality can become a domination system. Both readings are compatible with the structural interpretation adopted here, on which any authority, religious or secular, can occupy the position of the second beast when its speech is captured by rule. No church, university, newsroom or medical body occupies that position by virtue of what it is.
   696	
   697	\section{Objections and scope conditions}
   698	\label{sec:objections}
   699	
   700	\subsection{Vacuity}
   701	
   702	If the legitimation function were defined so broadly that any social activity belonged to it, the necessity claim would be empty. The definition excludes much. A practice belongs to the class only if it regularly changes members' beliefs about rules, officials or relevant facts and if members rely on the changed beliefs to coordinate. Private reflection, idiosyncratic opinion and persuasion without effect on compliance are excluded. The theorem can fail if its assumptions fail, and Section~\ref{sec:necessity} names the observation that would refute it. A claim with a stated falsifier is not vacuous.
   703	
   704	\subsection{Ideology critique}
   705	
   706	A Marxian critic may object that the paper treats legitimation too neutrally, as coordination, when its historical role has been to secure acceptance of domination. The endorsement model answers part of the objection. It identifies when legitimation misleads, through captured endorsement and the deception gap, and it predicts that coalitions with unsound rules push independence to its floor. What the model does not do is presume that every legitimating belief is false. That presumption would require the counterfactual preferences that \citet{lukes2005} acknowledged are hard to observe, and it would make the framework unable to distinguish a sound public-health rule from an unsound one. The difference between the two is the substance of Proposition~\ref{prop:ideological-power:credibility}.
   707	
   708	\subsection{Expertise and faith}
   709	
   710	A defender of science, medicine or religion may object that classing these institutions as ideological power disparages them. The classification concerns the function they perform for coordination, not the truth of what they teach. A physician who certifies that a vaccine is safe, a jurist who explains a rule of inheritance and a priest who instructs a congregation each change beliefs that others rely on. The results of this paper give independent authorities their value: their endorsement is informative because it is independent, and they protect the public precisely when a coalition's rule is unsound. The source framework's caution applies throughout: a hospital is not a propaganda organ and a professor is not an agent of command \citep{largo2026hbs}. The paper is silent on the truth of any faith's claims, and the theological reading of Section~\ref{sec:revelation} rests on a distinction that Revelation itself draws between witness and enforced display.
   711	
   712	\subsection{Measurement of belief}
   713	
   714	Belief is internal, while the control share $s^{\pI}$ is defined over observable outputs such as appointments, accreditation and reach. A critic may object that control over outputs is not control over minds. The objection is correct and is the reason the definition is restricted to outputs. Persuasion studies \citep{dellavigna2007,enikolopov2011} show that control over channels changes behavior, which is the evidence that edges in this layer are real. Whether a given share of outputs translates into a given share of influence is an empirical question that the indicators of Table~\ref{tab:indicators} are designed to address.
   715	
   716	\subsection{Scope conditions}
   717	
   718	The comparative claims are qualitative codings from secondary literature. Nothing in Section~\ref{sec:comparative} estimates the frequency of capture in any regime type, and the historical illustrations are not a sample. They show how the function is held in each type; they do not show how often it is captured.
   719	
   720	The regime types are ideal types with large internal variation. The comparative sections record that variation for Islamic states and Catholic monarchies in particular, and it holds for the other four types as well.
   721	
   722	The formal models are deliberately simple. They treat soundness as binary, independence as a probability and disclosure as independent across authorities given their type. Richer models would change magnitudes. The directions established by the proofs depend only on the monotonicity and convexity properties used there.
   723	
   724	\section{Conclusion}
   725	\label{sec:conclusion}
   726	
   727	Every persistent human collective with turnover and locally variable rules implements a recognition function: a recurring public practice that makes its rules common knowledge. That much follows from the coordination axiom, and the stateless societies of the ethnographic record show the function carried by talk, ridicule, ritual and kinship idiom without any office. Belief in the rightness of rules does not follow, and regimes vary widely in how much of it they command.
   728	
   729	The question that separates regimes is therefore not whether they have an ideological pillar but how independent its authorities are. A captured authority's endorsement carries no information. Independence helps coalitions with sound rules and hurts coalitions with unsound ones, so the institutional floor of independence, secured by endowments, tenure, constitutional protection or transnational appointment, protects the public in the cases where protection matters. Coordinated control of many authorities lowers the chance that an error is disclosed even when their average independence is unchanged, which is why integration across pillars, and not concentration within one, is the condition to measure.
   730	
   731	The six regime types distribute the function differently. Market economies couple it to finance, party-states to appointment and coercion, social democracies to labor organizations, Islamic states and Catholic monarchies to religious authorities whose independence from rulers varied from substantial to nil, and secular democracies to a legally plural public sphere. The comparative codings remain qualitative, and the hypotheses of Section~\ref{sec:measurement} state what evidence would overturn them. The existence of the pillar is universal, as Proposition A holds; its capture is a contingent and measurable condition, as Proposition B holds, and the first does not entail the second.
   732	
   733	\begin{thebibliography}{200}
   734	\small
   735	\raggedright
   736	
   737	\bibitem[Abbott(1988)]{abbott1988}
   738	Abbott, Andrew (1988). \emph{The System of Professions: An Essay on the Division of Expert Labor}. University of Chicago Press. doi:10.7208/chicago/9780226189666.001.0001.
   739	
   740	\bibitem[Al-Rasheed(2002)]{alrasheed2002}
   741	Al-Rasheed, Madawi (2002). \emph{A History of Saudi Arabia}. Cambridge University Press. doi:10.1017/cbo9780511993510.
   742	
   743	\bibitem[Allcott and Gentzkow(2017)]{allcott2017}
   744	Allcott, Hunt and Matthew Gentzkow (2017). Social Media and Fake News in the 2016 Election. \emph{Journal of Economic Perspectives} 31(2):211-236. doi:10.1257/jep.31.2.211.
   745	
   746	\bibitem[Althusser(1971)]{althusser1971}
   747	Althusser, Louis (1971). Ideology and Ideological State Apparatuses (Notes towards an Investigation). In \emph{Lenin and Philosophy and Other Essays}. Monthly Review Press.
   748	
   749	\bibitem[Arjomand(1988)]{arjomand1988}

exec
/usr/local/bin/zsh -lc "sed -n '150,349p' papers/latex/ideological-power.tex | nl -ba -v150" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   150	
   151	(c) Let $\Omega=\{\omega_1,\omega_2,\omega_3\}$, $N=\{1,2\}$ and $E=\{\omega_1,\omega_2\}$. Member 1 is told privately whether $E$ holds: $\mathcal{P}_1=\{\{\omega_1,\omega_2\},\{\omega_3\}\}$. Member 2 is told only at $\omega_1$: $\mathcal{P}_2=\{\{\omega_1\},\{\omega_2,\omega_3\}\}$. At $\omega_1$ both members know $E$. But $K_2E=\{\omega_1\}$ and $K_1K_2E=\emptyset$, because member 1's cell $\{\omega_1,\omega_2\}$ is not contained in $\{\omega_1\}$. Member 1 knows the rule but does not know that member 2 knows it.
   152	\end{proof}
   153	
   154	Part (b) is a form of Aumann's characterization of common knowledge \citep{aumann1976}. Together, (a) and (b) say that common knowledge of the rules is available exactly when some public event certifies them. Part (c) shows why private instruction, however thorough, does not suffice. A teacher who instructs each pupil separately produces knowledge; an assembly in which pupils see one another being instructed produces common knowledge.
   155	
   156	\begin{remark}
   157	Common knowledge is an idealization. \citet{rubinstein1992} showed in the electronic mail game that any finite number of levels of mutual knowledge can fail to support coordination that common knowledge would support. \citet{monderer1989} showed that an approximate notion, common $p$-belief, restores continuity: equilibria that require common knowledge are approximated by equilibria under common $p$-belief for $p$ close to one. The arguments below go through with public events replaced by events that each member believes with probability at least $p$ whenever they occur. We state them for common knowledge to keep the logic visible.
   158	\end{remark}
   159	
   160	\subsection{Concentration and contestability in the ideological layer}
   161	
   162	The control share $s^{\pI}_{i,t}$ is a share of decision-relevant control over authoritative outputs: appointment and removal of authorities, accreditation and licensing, the content of curricula, approval of doctrinal or scientific standards, and the reach of broadcast and print channels. Belief itself is not a fixed quantity to be divided, so $s^{\pI}$ is defined over these outputs and not over minds. Concentration $H^{\pI}_t:=H_{\pI,t}$ is high when one organization appoints the clergy, writes the curriculum, licenses the presses and certifies the professions; it is low when these decisions are spread across organizations with separate appointment and funding.
   163	
   164	\begin{definition}[Components of ideological contestability]
   165	\label{def:ideological-power:qi}
   166	The ideological contestability $Q^{\pI}_t:=Q_{\pI,t}$ is a preregistered aggregate, with values in $[0,1]$, of five components:
   167	(i) \emph{plurality}: the number and audience reach of legitimating authorities whose appointment and funding are independent of one another;
   168	(ii) \emph{independence}: tenure protection, editorial autonomy, academic freedom and juristic or doctrinal autonomy of authorities from the governing coalition;
   169	(iii) \emph{disclosure}: publication of the funding, sponsorship and conflicts of interest of authorities;
   170	(iv) \emph{reviewability}: procedures by which an authority's statements can be challenged, replicated, corrected or retracted, including peer review, rights of reply and public correction;
   171	(v) \emph{exit}: the ability of audiences to turn to rival authorities without legal or material sanction, the ideological case of exit in Hirschman's sense, leaving an organization rather than voicing complaint within it, which Part VI defines (Definition 2.5 of Part VI).
   172	\end{definition}
   173	
   174	The components are not new. They restate the source framework's contestability for the ideological layer and match the checks it lists for its knowledge mechanism: independent epidemiology, investigative reporting, protected academic freedom and professional resistance \citep{largo2026hbs}. Their value lies in making the aggregate auditable: each component can be coded from documents, and a disagreement about $Q^{\pI}$ can be traced to a disagreement about one of them.
   175	
   176	Ideological concentration alone cannot produce a strong classification under the source criterion, which needs both high $U_t$ and high $\Int_t$. The bound is elementary but worth stating. If every pair not involving $\pI$ has $C_{mn,t}=0$, then by \eqref{eq:integration} $\Int_t=\frac{1}{15}\sum_{n\neq\pI}C_{\pI n,t}\leq 5/15=1/3$. A polity whose governing coalition controls every belief-producing institution but none of the other five pillars shows ideological fusion, not system-wide integration. Capture of belief becomes system-wide only through coupling to appointments, budgets or sanctions in other pillars, which is why Section~\ref{sec:mechanisms} studies the couplings.
   177	
   178	The value of a single authority to its audience depends on how independent it is of whoever controls it. Section~\ref{sec:mechanisms} models this dependence with an independence parameter $\lambda\in[0,1]$, the probability that an authority reports its own findings rather than the position of a controlling coalition. The components of $Q^{\pI}$ are the institutional means of raising $\lambda$.
   179	
   180	\section{Necessity of the legitimation function}
   181	\label{sec:necessity}
   182	
   183	\subsection{Assumptions}
   184	
   185	The series derives each pillar from an axiom about collective life. Part VII owns the axiom set and proves the general necessity theorem. The ideological pillar rests on the coordination axiom. We state it with the auxiliary assumptions that the derivation needs, and we mark which assumptions are empirical.
   186	
   187	Fix a collective $G$ with members $N_t$ at time $t$ and rule system $R_t$. Say that $G$ \emph{functions} at $t$ if members cooperate on the basis of $R_t$: they comply with its rules and recognize its office holders at least often enough for the collective to make and carry out collective decisions. Let $E_t\subseteq\Omega$ be the event that $R_t$ is the rule system in force at $t$. Information changes over time, so member $i$ has a partition $\mathcal{P}_{i,s}$ and knowledge operator $K_{i,s}$ at each date $s$. Write $\tau_i$ for $i$'s entry date. For $s<\tau_i$ we set $\mathcal{P}_{i,s}=\{\Omega\}$, the trivial partition: before entry a person knows nothing about the local rules beyond what is true in every state. Common knowledge at date $s$ means common knowledge under the date-$s$ partition profile $(\mathcal{P}_{j,s})_j$.
   188	
   189	\begin{assumption}[Ax4, coordination]
   190	\label{ax:coordination}
   191	If $G$ functions at $t$, then there is a set $N^\ast_t\subseteq N_t$ of members, large enough that cooperation among them sustains the collective, such that $E_t$ is common knowledge among $N^\ast_t$ at the true state at date $t$.
   192	\end{assumption}
   193	
   194	\begin{assumption}[Turnover]
   195	\label{ax:turnover}
   196	There is a horizon $L$ such that for every $t$ at least one member of $N^\ast_{t+L}$ entered the collective during $[t,t+L]$.
   197	\end{assumption}
   198	
   199	\begin{assumption}[Non-innateness]
   200	\label{ax:noninnate}
   201	At entry, an entrant cannot tell which rule system will be in force at any later date: for every entrant $e$, every date $s\geq\tau_e$ and the true state $\omega$, $\mathcal{P}_{e,\tau_e}(\omega)\not\subseteq E_s$.
   202	\end{assumption}
   203	
   204	The coordination axiom is the series' Ax4 in the precise form that \citet{lewis1969} gave to conventions: a convention is a regularity sustained because it is common knowledge that others conform. Turnover is universal in human collectives, whose members are born and die, marry in and out, and join and leave; the assumption adds only that some entrants join the cooperating core within a bounded time. Non-innateness is an empirical claim with strong support. Rule systems differ widely across human societies, as every ethnography in Table~\ref{tab:minimal} shows, so an entrant cannot read the local rules off a genetic or otherwise fixed endowment. The assumption fails for social insects, whose coordination rules are largely fixed by development, and that failure marks the scope of the theorem.
   205	
   206	\begin{lemma}[Renewal]
   207	\label{lem:ideological-power:renewal}
   208	Under Assumptions~\ref{ax:turnover} and \ref{ax:noninnate}, for every $t$ there is a member $e\in N^\ast_{t+L}$ with $t\leq\tau_e\leq t+L$ who does not know $E_{t+L}$ at date $\tau_e$.
   209	\end{lemma}
   210	
   211	\begin{proof}
   212	Assumption~\ref{ax:turnover} supplies $e\in N^\ast_{t+L}$ with $\tau_e\in[t,t+L]$. Since $t+L\geq\tau_e$, Assumption~\ref{ax:noninnate} gives $\mathcal{P}_{e,\tau_e}(\omega)\not\subseteq E_{t+L}$, that is $\omega\notin K_{e,\tau_e}E_{t+L}$.
   213	\end{proof}
   214	
   215	Renewal can also arise without entry. If the rule system changes within the window through the rule of change, the procedure by which a collective alters its rules (Definition 3.6 of Part II), and the change was not announced before the window began, then some member did not know the new rule system at the window's start. The theorem below holds with that case in place of Assumptions~\ref{ax:turnover} and \ref{ax:noninnate}.
   216	
   217	\subsection{The necessity lemma}
   218	
   219	\begin{theorem}[Necessity of recognition]
   220	\label{thm:ideological-power:necessity}
   221	Let $G$ satisfy Assumptions~\ref{ax:coordination}, \ref{ax:turnover} and \ref{ax:noninnate} and function at every date of an interval longer than $L$. Then within every window $[t,t+L]$ inside the interval:
   222	\begin{enumerate}
   223	\item[(i)] the partition of at least one member $e\in N^\ast_{t+L}$ is refined between $\tau_e$ and $t+L$ by information bearing on the rule system, from a cell not contained in $E_{t+L}$ to a cell contained in it; and
   224	\item[(ii)] the partition profile of $N^\ast_{t+L}$ changes during the window from one under which $E_{t+L}$ is not common knowledge at the true state to one under which it is, so that at date $t+L$ there is an event, public under the date-$(t+L)$ profile, that contains the true state and is contained in $\bigcap_{i\in N^\ast_{t+L}}K_{i,t+L}E_{t+L}$.
   225	\end{enumerate}
   226	The practices that produce these refinements belong to the legitimation function of Definition~\ref{def:ideological-power:legitimation}. Hence the legitimation function is implemented in $G$, at least in the form of recognition.
   227	\end{theorem}
   228	
   229	\begin{proof}
   230	Fix a window $[t,t+L]$ inside the interval and let $\omega$ be the true state. By Assumption~\ref{ax:coordination}, $E_{t+L}$ is common knowledge among $N^\ast_{t+L}$ at $\omega$ at date $t+L$. By Lemma~\ref{lem:ideological-power:public-signal}(b), applied to the date-$(t+L)$ profile, the set $F^\ast$ of states at which $E_{t+L}$ is common knowledge under that profile is public under it, contains $\omega$, and satisfies $F^\ast\subseteq K_{i,t+L}E_{t+L}$ for every $i\in N^\ast_{t+L}$.
   231	
   232	By Lemma~\ref{lem:ideological-power:renewal}, some $e\in N^\ast_{t+L}$ with $\tau_e\in[t,t+L]$ has $\omega\notin K_{e,\tau_e}E_{t+L}$. Since $\omega\in F^\ast\subseteq K_{e,t+L}E_{t+L}$, $e$'s cell at $\omega$ shrank between $\tau_e$ and $t+L$ from a set not contained in $E_{t+L}$ to a set contained in it, which is (i).
   233	
   234	Under the date-$\tau_e$ profile, $E_{t+L}$ is not common knowledge among $N^\ast_{t+L}$ at $\omega$, because $e$ does not know it and common knowledge implies mutual knowledge. Under the date-$(t+L)$ profile it is, with $F^\ast$ as the certifying public event. The change lies entirely in the refinement of members' partitions within the window, which is (ii). The practices that produced the refinement regularly change members' beliefs about the rule system, and members rely on the resulting common knowledge to coordinate, which is the defining property in Definition~\ref{def:ideological-power:legitimation}. Since the argument applies to every window of length $L$, such practices recur.
   235	\end{proof}
   236	
   237	The theorem is modest in its mathematics and specific in its content. Its mathematical core is the characterization of common knowledge by public events. Its empirical content sits in the three assumptions, all of which the proof uses, which is where the series' standard of proof requires it to sit: the necessity claim is derived from stated premises about collective life, and it can fail if the premises fail. Part VII states the general theorem for all six pillars and the non-implication of Proposition B; the present result is the pillar-level piece for $\pI$.
   238	
   239	\begin{remark}[What the theorem does not show]
   240	\label{rem:ideological-power:scope}
   241	The theorem shows that recognition is necessary. It does not show that normative legitimacy is necessary. A collective in which members know which rules are in force and comply from fear or habit satisfies every assumption above. Comparative research on autocracies treats legitimation as one of three supports of stable rule, alongside repression and co-optation, and finds that the mix varies \citep{gerschewski2013}. \citet{wintrobe1998} modeled dictators who trade off loyalty against repression, and \citet{weber1978} acknowledged that obedience can rest on fear or interest as well as on belief in legitimacy. Normative legitimacy is a frequent and valuable content of the ideological function, but it is a contingent one. This narrowing matters for the comparison: a regime with low normative legitimacy still has a fully implemented ideological pillar, because it still must make its rules, sanctions and officials common knowledge.
   242	\end{remark}
   243	
   244	\subsection{Minimal forms in stateless and consensus societies}
   245	
   246	The strongest test of a necessity claim is the set of societies described as having no state, no chiefs with coercive power, or radical equality. The theorem predicts that each implements recognition through some public practice, even with no designated office.
   247	
   248	\begin{proposition}[Minimal form; empirical]
   249	\label{prop:ideological-power:minimal-form}
   250	In each of the stateless, egalitarian or consensus-based societies of Table~\ref{tab:minimal}, the legitimation function is implemented by public practices without a designated office, and decision-relevant control over those practices is widely dispersed, so that $H^{\pI}$ is low and $Q^{\pI}$ is high.
   251	\end{proposition}
   252	
   253	This is an empirical proposition, supported by the ethnographic record rather than proved. The support is summarized in Table~\ref{tab:minimal} and discussed below.
   254	
   255	\begin{table}[t]
   256	\centering
   257	\small
   258	\caption{Minimal forms of the legitimation function in stateless and egalitarian societies. Each row names the public practices that make rules and expectations common knowledge and the strongest reading that the function is absent.}
   259	\label{tab:minimal}
   260	\begin{tabularx}{\textwidth}{@{}L{2.4cm}YY@{}}
   261	\toprule
   262	Case & Public practices that carry recognition & Strongest counter-reading and reply \\
   263	\midrule
   264	Ju/'hoansi & Camp talk, joking and criticism heard by all, the leveling custom of insulting the meat, and the healing dance \citep{lee1979,lee2013,marshall1976,wiessner2005} & No office holds authority. Reply: the function is carried by talk that everyone hears, which is exactly a public event. \\
   265	Nuer & Lineage idiom shared across segments, ritual specialists whose standing is religious rather than political, and prophets \citep{evanspritchard1940} & Evans-Pritchard stressed the absence of government. Reply: the function is present while the office is absent. \\
   266	Amazonian chiefdoms & The chief's duty of public speech, which recalls traditional norms, and myth shared by the group \citep{clastres1987} & The chief commands nothing. Reply: the chief's speech is a public recitation of norms without power to command. \\
   267	Mobile foragers & Moral talk and gossip that circulate shared norms and identify would-be dominators \citep{boehm1999,boehm2012} & Equality might seem to require no shared ideology. Reply: the egalitarian ethos is itself a shared and enforced belief. \\
   268	Immediate-return societies & Public leveling practices such as obligatory sharing and mockery of self-promotion \citep{woodburn1982} & Ritual is egalitarian and unspecialized. Reply: unspecialized is not absent. \\
   269	Commons users & Rules known to appropriators, collective-choice meetings and public monitoring \citep{ostrom1990} & Users may coordinate by self-interest alone. Reply: Ostrom's design principles include rules that users know and can change. \\
   270	\bottomrule
   271	\end{tabularx}
   272	\end{table}
   273	
   274	The Ju/'hoansi are the case most often cited as lacking hierarchy. Their norms of sharing, modesty and restraint are sustained by talk. \citet{wiessner2005} recorded conversations in Ju/'hoansi camps and found that criticism of norm violations was mostly verbal and directed at behavior such as stinginess and self-aggrandizement. Talk in a small camp has the structure of a public event: speakers and listeners are co-present, and each sees who else hears. \citet{lee1979} and \citet{lee2013} describe the custom of deprecating a successful hunter's kill, which teaches the hunter and everyone listening that boasting will not be tolerated. No one holds an office of teacher or censor. The function is distributed across the whole adult population, so $H^{\pI}$ is close to its minimum and exit to another camp keeps $Q^{\pI}$ high.
   275	
   276	The Nuer were described by \citet{evanspritchard1940} as an ordered anarchy without government. The ideological function is present in the lineage idiom that tells every Nuer how segments relate and which obligations follow, and in ritual specialists such as the leopard-skin chief, whose standing derived from a ritual relation to the earth rather than from any power to command. The case confirms that the function can exist without an office that issues orders.
   277	
   278	\citet{clastres1987} described Amazonian chiefs whose authority rested on generosity and speech. The chief's daily discourse recalls the traditional norms of the group; it is a public recitation, not a command, and a chief who tries to command loses his following. Clastres read these societies as actively preventing the political function from separating from society. The reading is consistent with Theorem~\ref{thm:ideological-power:necessity}: the function exists, its holder has no power to enforce it, and concentration is prevented by design. Clastres' evidence has been criticized as selective, and the case should be read with that caution.
   279	
   280	\citet{boehm1999} argued that mobile foragers maintain equality through a reverse dominance hierarchy in which the group as a whole suppresses would-be dominators by gossip, ridicule, ostracism and, in extreme cases, killing. The sanctions belong to Part V. The shared moral understanding that identifies what counts as domination belongs here. \citet{woodburn1982} made the parallel point for immediate-return societies: equality there is an institutional outcome produced by leveling practices, not the absence of institutions.
   281	
   282	\citet{ostrom1990} showed that long-enduring commons are governed by rules that users know, can modify and monitor. The design principles are institutional, not ideological, but each presupposes that the operative rules are common knowledge among appropriators. \citet{graeber2021} added that some societies alternated seasonally between hierarchical and egalitarian arrangements, each publicly marked. Their claims are contested and are cited here only for the narrow point that political arrangements were publicly recognized as such.
   283	
   284	These cases come with standard caveats. Contact-era ethnography observed groups in marginal environments, sometimes idealized them, and generalized from few cases \citep{kelly1995}. None of these caveats affects the narrow claim of Proposition~\ref{prop:ideological-power:minimal-form}. Each caveat would matter if the claim were that these societies show the original condition of humanity; the claim is only that they show the function without the office.
   285	
   286	\subsection{Counterexample attempts}
   287	
   288	The most serious attempt to defeat the necessity claim is coordination by force alone. On this view a sufficiently strong coercive apparatus needs no shared beliefs; it needs soldiers and prisons. The reply is that force itself depends on common knowledge. A sanction rule deters only if the people it targets know it, and a coercive organization holds together only if its members expect one another to carry out orders. \citet{kuran1991} showed that regimes resting on public displays of support can collapse suddenly when private opposition becomes common knowledge, which is evidence that rulers depend on controlling what is common knowledge even when they rely on force. \citet{svolik2012} treats the control of information among elites as a central problem of authoritarian rule. The attempt fails for recognition. It succeeds against a stronger thesis, that normative legitimacy is necessary, which Remark~\ref{rem:ideological-power:scope} has already abandoned.
   289	
   290	A second attempt holds that markets coordinate through prices without shared beliefs. Prices do economize on information. But exchange presupposes common knowledge of property conventions: who owns what, what counts as payment, and which contracts are binding. Those conventions are part of $R_t$, and they are taught, displayed and defended. \citet{hayek1973} himself stressed that the order of a market society rests on rules of just conduct that people follow without being able to state them; following a rule one cannot state is compatible with common knowledge of the practice it supports.
   291	
   292	A third attempt notes that in a small face-to-face group everyone observes everyone, so common knowledge arises from co-presence without any practice designed to produce it. This is correct and is the minimal form, not a counterexample. Co-present talk is a practice that produces public events.
   293	
   294	A fourth attempt points to coordination without beliefs in animal societies. The non-innateness assumption excludes it, and the exclusion is principled: where rules are fixed by development, no transmission is needed. The theorem is a claim about human governance, where rules vary.
   295	
   296	The falsifier follows from the assumptions. The necessity claim would be refuted by a persistent human collective, with turnover and with rules that differ from its neighbors', in which entrants come to coordinate on the local rules without any practice that informs them of the rules and without any public event that certifies them. We know of no such case in the sources reviewed.
   297	
   298	\subsection{Function and institution}
   299	
   300	Two classic errors of functionalism must be avoided. \citet{hempel1959} showed that from the premise that a function is needed one cannot infer that a particular institution exists, because functional equivalents may meet the need. Theorem~\ref{thm:ideological-power:necessity} respects this limit: it asserts that some practice in a class is implemented, and the class includes campfire talk and state broadcasting alike. \citet{elster1983} argued that explaining an institution by its beneficial effects requires a feedback mechanism from effect to institution. The theorem is not such an explanation. It is a condition of persistence: collectives that lack the function do not function, whatever the reason the function arose. It does not explain why a given regime has a ministry of religious affairs or a public broadcaster, and the comparative sections never use it for that purpose. \citet{merton1968} supplies the remaining vocabulary: the manifest function of a university is teaching and research, and its latent function in the ideological layer may include certifying elites, which is a separate empirical question.
   301	
   302	\section{Literature on ideological power}
   303	\label{sec:literature}
   304	
   305	\subsection{Consent and coercion}
   306	
   307	The modern study of ideological power begins with the observation that rule rests on consent as well as force. \citet{gramsci1971} called the organization of consent through civil society hegemony and argued that in societies with dense churches, schools, associations and presses, rulers depend on these institutions as much as on the state's coercive apparatus. \citet{althusser1971} sharpened the contrast into a distinction between repressive and ideological state apparatuses, the latter including churches, schools, families, the media and cultural institutions, and he argued that in mature capitalism the school had displaced the church as the dominant ideological apparatus. Both accounts treat ideological institutions as functional supports of a ruling class. That functional reading is precisely what \citet{elster1983} criticized, and it is what the present paper avoids: we claim the necessity of a function, not that any given apparatus exists because it serves a class.
   308	
   309	\citet{weber1978} placed belief at the center of domination by distinguishing traditional, charismatic and rational-legal grounds of legitimacy. Part II uses the Weberian types to analyze who makes rules. This Part takes from Weber only the distinction between compliance grounded in belief and compliance grounded in fear or interest, which becomes the distinction between normative legitimacy and recognition in Definition~\ref{def:ideological-power:recognition}.
   310	
   311	\subsection{Faces of power and networks of meaning}
   312	
   313	\citet{bachrach1962} argued that power is exercised not only in decisions but also in non-decisions, by keeping issues off the agenda. \citet{lukes2005} added a third dimension: the power to shape preferences so that conflicts of interest never surface. Part II owns agenda control, the power to determine which proposals reach a decision, as an object of rule-making (Definition 2.9 of Part II). The third dimension belongs here, because shaping preferences is shaping beliefs. The difficulty Lukes acknowledged is measurement: claims about preferences that people would hold but for ideological influence require a counterfactual that is hard to observe. The endorsement model of Section~\ref{sec:mechanisms} sidesteps the problem by studying a narrower and observable quantity, the information content of an authority's statements.
   314	
   315	\citet{mann1986,mann1993} gave the most developed comparative-historical account. He distinguished ideological, economic, military and political networks of power and treated none as primary. Ideological power, in his account, derives from the human need for meaning, norms and aesthetic and ritual practice, and it can be transcendent, organizing a community across political boundaries as the world religions did, or immanent, reinforcing the morale of an existing group. Mann's framework is the closest predecessor of the six-pillar model. It lacks a separate judicial pillar and a separate pillar for the producing population, and it has no measure of capture; Part VII compares the frameworks in detail. Its value here is the distinction between transcendent and immanent ideological power, which maps onto the difference between authorities whose appointment and revenue lie outside the polity, such as a transnational church, and authorities created by the polity itself.
   316	
   317	\citet{bourdieu1989,bourdieu1991} described symbolic power as the power to constitute the given by stating it, effective to the degree that it is misrecognized as something other than power. His account of the convertibility of economic, cultural and symbolic capital anticipates the cross-pillar coupling $C_{\pF\pI}$, which Part I treats as its pair. \citet{bourdieu1977} applied the account to schooling, arguing that educational systems reproduce class structure while appearing meritocratic.
   318	
   319	\subsection{The public sphere and the media}
   320	
   321	\citet{habermas1989} traced the rise of a bourgeois public sphere of rational-critical debate in eighteenth-century Europe and its later refeudalization, as mass media and organized interests turned a reasoning public into an audience. \citet{fraser1990} argued that the bourgeois public sphere excluded women, workers and others, who formed subaltern counterpublics of their own. Both accounts bear on the plurality component of $Q^{\pI}$: a public sphere is contestable to the degree that counterpublics can form and be heard.
   322	
   323	The political economy of the media divides on the question of supply and demand. \citet{herman1988} proposed a propaganda model in which ownership, advertising, reliance on official sources, organized flak and a dominant ideology filter news in favor of elite interests. The model predicts that owner and advertiser interests shape content. \citet{gentzkow2006} showed instead that slant can arise from demand: outlets that wish to appear accurate tilt reports toward their audience's prior beliefs, so slant can exist without any owner's design. \citet{djankov2003} assembled cross-country data on media ownership and found that the largest media firms were typically controlled by governments or by private families, and that state ownership was associated with weaker press freedom and political rights. \citet{besley2006} modeled media capture by government and showed that capture is harder when there are more independent outlets and when bribing them is costly, which links plurality directly to accountability. \citet{hallin2004} classified Western media systems into liberal, democratic corporatist and polarized pluralist models, differing in the strength of commercial media, the degree of political parallelism, journalistic professionalization and the role of the state.
   324	
   325	Persuasion effects are measurable. \citet{dellavigna2007} exploited the staggered entry of a cable news channel into United States towns and found an effect on presidential vote shares. \citet{enikolopov2011} found that access to the one national television channel independent of the government in Russia's 1999 parliamentary election reduced votes for the government's party and raised votes for opposition parties. These studies establish that the ideological layer has real edges: control of a channel changes political behavior.
   326	
   327	Authoritarian information control has its own literature. \citet{king2013} analyzed censorship of Chinese social media and found that posts criticizing the state were often left standing while posts with potential for collective action were removed. \citet{stockmann2013} found that commercialized Chinese media were perceived as more credible than official outlets and could therefore carry the party's messages more persuasively. \citet{guriev2019,guriev2022} described a shift from rule by fear to rule by spin, in which leaders manipulate information while simulating democratic forms; Part II treats this as a strategy of rule-makers. \citet{kuran1991} analyzed preference falsification, in which citizens publicly support regimes they privately oppose, and explained why the revolutions of 1989 surprised observers.
   328	
   329	Digital platforms add a layer of intermediaries between authorities and audiences. \citet{gillespie2019} argued that moderation of what users may post is not incidental to platforms but constitutive of them, so platform firms make continual decisions about which speech reaches whom. \citet{allcott2017} found that fabricated news stories circulated widely on social media before the 2016 United States election, while estimated exposure per adult was modest. \citet{guess2023} replaced the algorithmic feeds of consenting Facebook and Instagram users with reverse-chronological feeds for three months during the 2020 campaign and found large changes in what users saw but no detectable change in polarization or political attitudes. \citet{roberts2018} showed that Chinese censorship works less through fear than through friction and flooding, which make unwanted information costly to find rather than impossible. Platforms are thus channels whose control shares and contestability can be coded like those of broadcasters, with the difference that ranking and moderation decisions are made at very large scale by few organizations.
   330	
   331	\subsection{Professions and expert authority}
   332	
   333	Professions convert knowledge into authority. \citet{larson1977} described the professional project as an effort to secure market closure and social standing through control of training and credentials. \citet{abbott1988} treated professions as competitors for jurisdiction over tasks. \citet{freidson1970} argued that medicine's autonomy, its control over the content of its own work, made it the model profession, and \citet{starr1982} traced how American medicine converted cultural authority into economic power and professional sovereignty. These accounts explain why expert authority is valuable to rulers: experts certify that a rule is sound in terms the public trusts.
   334	
   335	Evidence on sponsorship qualifies that trust without destroying it. \citet{bekelman2003} reviewed studies of financial conflicts of interest in biomedical research and found that industry sponsorship was associated with conclusions favorable to sponsors. \citet{lexchin2003} reached a similar conclusion for pharmaceutical sponsorship, and the Cochrane review by \citet{lundh2017} found that industry-sponsored drug and device studies more often reported favorable results and conclusions than studies with other sponsors. \citet{oreskes2010} documented campaigns in which a small number of scientists, with industry support, manufactured doubt about the harms of tobacco and about environmental science. Against these findings stand accounts of why science remains trustworthy. \citet{oreskes2019} located the reliability of science in its social process of critical vetting by a diverse community, and \citet{carpenter2010} showed that the United States Food and Drug Administration built autonomy on its reputation for scientific judgment. \citet{slaughter2004} documented the growing market orientation of universities, which raises the coupling between the financial and ideological pillars. Read together, this literature supports the model of Definition~\ref{def:ideological-power:endorsement}: expert authorities are informative to the degree that their judgments are independent of their sponsors, and institutions such as disclosure, review and reputation exist to secure that independence.
   336	
   337	\subsection{Religion and the state}
   338	
   339	The relation between religious authority and political rule is the oldest problem of the ideological pillar. \citet{stepan2000} proposed the twin tolerations as the condition for democracy: elected institutions free from religious veto, and religious citizens free to worship and to advance their views in public. \citet{casanova1994} documented the deprivatization of religion, its return to public life in several countries from the 1980s. \citet{philpott2007} argued that religious actors' political behavior depends on their institutional independence from the state and on their political theology. \citet{fox2008} coded religion-state arrangements worldwide. \citet{kuru2009} distinguished passive secularism, which allows public religious expression, from assertive secularism, which excludes it.
   340	
   341	Two debates concern Islamic and Catholic polities directly. \citet{kuru2019} argued that an alliance between ulama and the state, formed in the eleventh century, helps explain authoritarianism and underdevelopment in many Muslim-majority countries. \citet{rubin2017} argued that rulers who depended on religious authorities for legitimacy faced different incentives from rulers who depended on economic elites, and that the difference shaped economic divergence. Both arguments are contested, and the series cites them as positions, not settled findings. For Catholic Europe, \citet{grzymala2023} argued that the medieval Church served as a template and rival for state building, and \citet{grzymala2015} showed that churches whose moral authority is fused with national identity can shape policy through institutional access rather than partisan politics.
   342	
   343	\subsection{Relation to prior work}
   344	
   345	Coordination theory \citep{lewis1969,schelling1960,aumann1976,chwe2001} explains why some practice must make rules common knowledge. The political economy of media and expertise \citep{besley2006,gentzkow2006,carpenter2010} explains why the value of a statement depends on the independence of its source. Comparative work on religion, media and education describes how the institutions vary. No existing framework combines the three: none derives the function from an axiom, states when its institutions check or enable capture, and compares regimes on the same measures. The source framework provides the measures \citep{largo2026hbs}. The present paper adds the derivation and the pillar-level model and applies both to six regime types.
   346	
   347	\section{Comparative analysis across six regime types}
   348	\label{sec:comparative}
   349	

exec
/usr/local/bin/zsh -lc "sed -n '350,549p' papers/latex/ideological-power.tex | nl -ba -v350" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   350	Every regime type implements the ideological function; they differ in which institutions hold it, how tightly one coalition controls their appointments and revenue, and which other pillars that coalition also commands. The comparison below codes these differences qualitatively from secondary sources. No numerical value of $H^{\pI}$, $Q^{\pI}$, $U_t$ or $\Int_t$ is reported for any polity, because no preregistered coding exists.
   351	
   352	The couplings of the ideological pillar to finance, rule-making and adjudication ($C_{\pF\pI}$, $C_{\pP\pI}$, $C_{\pJ\pI}$) are analyzed primarily in Parts I, II and III; this paper treats the couplings to coercion and production ($C_{\pI\pC}$, $C_{\pI\pW}$).
   353	
   354	\subsection{Market-capitalist societies}
   355	
   356	In market-capitalist societies the ideological function is held by many organizations with separate ownership and funding: privately owned media firms financed by advertising and subscriptions, public and private universities, foundations and think tanks, professional associations, scientific journals, regulatory agencies in their certifying role, and religious bodies organized as voluntary associations. Control over authoritative outputs is spread across these organizations, so $H^{\pI}$ is moderate overall, but it varies by sector. Ownership of the largest media firms is often concentrated in a few families \citep{djankov2003}, while accreditation of physicians or approval of drugs may rest with a single professional body or agency.
   357	
   358	The distinctive coupling is between the financial and ideological pillars. Advertising finances news, endowments and grants finance universities, and industry finances a large share of clinical research. \citet{herman1988} built their propaganda model on this coupling. \citet{slaughter2004} documented the movement of universities toward market revenue, and \citet{starr1982} described how medical authority was converted into economic power and later confronted corporate organization of care. Part I treats $C_{\pF\pI}$ as its pair and measures the conversion of financial control into favorable outputs of other pillars by a conversion elasticity (Definition 6.1 of Part I); here the question is what the coupling does to the independence parameter $\lambda$ of Definition~\ref{def:ideological-power:endorsement}.
   359	
   360	The documented capture episodes are sectoral. Systematic reviews associate industry sponsorship with conclusions favorable to sponsors \citep{bekelman2003,lexchin2003,lundh2017}. \citet{oreskes2010} documented organized efforts to manufacture doubt about tobacco harms and environmental hazards. Each case meets the three conditions of a capture link: privileged access through funding, weakened contestability through selective publication or orchestrated doubt, and material evidence linking the asymmetry to an output, whether a published conclusion or a delayed regulation.
   361	
   362	Platform firms now hold part of the function in this regime type. A few companies decide, through ranking and moderation, which statements by journalists, scientists and clergy reach large audiences \citep{gillespie2019}. In the terms of Section~\ref{sec:layer}, they hold a large share of control over reach, one of the outputs that defines $s^{\pI}$, so they raise measured concentration even when the number of speakers grows. The evidence on their persuasive effect is mixed: fabricated stories spread widely \citep{allcott2017}, but an experimental change of feed ranking during an election left attitudes unchanged \citep{guess2023}. Control over reach is established; its translation into belief is an open empirical question.
   363	
   364	The documented checks are also sectoral. Competition among outlets makes media capture costly \citep{besley2006}. Demand-side slant \citep{gentzkow2006} is a rival explanation for partisan coverage that does not require owner control, so evidence of slant is not by itself evidence of capture. Disclosure rules, peer review, replication and the reputational autonomy of regulators \citep{carpenter2010} raise $\lambda$. The capture episodes above were themselves discovered through litigation, journalism and meta-research, which is what source hypothesis H4 predicts: higher rates of documented error discovery can signal stronger accountability rather than more capture \citep{largo2026hbs}.
   365	
   366	\subsection{Communist party-states}
   367	
   368	In communist party-states the ruling party claims the ideological function as part of its leading role. Party propaganda departments, state newspapers and broadcasters, party schools, academies of sciences, writers' and artists' unions and a compulsory curriculum in Marxism-Leninism hold the function. \citet{kenez1985} described how the Bolsheviks built a propaganda state in their first decade, combining agitation, literacy campaigns and new media under party direction. \citet{brooks2000} showed how the Soviet press under Stalin organized public culture as a ritual in which achievements were presented as gifts from the leadership and citizens were expected to express gratitude.
   369	
   370	Concentration is high by design. Appointments of editors, rectors and academy presidents pass through the party's appointment channel, the map from a coalition to the offices it fills in each pillar (Definition 2.8 of Part II), so $C_{\pP\pI}$ is high and $H^{\pI}$ approaches its maximum in the formal structure. Coupling to the coercive pillar is strong: censorship offices and security services enforce the boundaries of permissible expression, and Part V treats the security services themselves. \citet{althusser1971}'s concept of ideological state apparatuses, developed within Marxism, describes this configuration more literally than it describes the societies Althusser had in mind.
   371	
   372	Formal structure overstates actual control. \citet{lane1995} found commonalities and divisions within the Soviet ruling elite in its last decade, and divisions within the elite reduce the effective concentration of control over authoritative outputs. \citet{kuran1991} explained the sudden collapse of East European regimes in 1989 as the release of privately held opposition that public displays had concealed. In the People's Republic of China, \citet{king2013} found that censors removed posts with potential for collective action more consistently than posts criticizing officials, which shows a discriminating rather than total control of expression. \citet{stockmann2013} found that commercialized media, perceived as more credible than official outlets, could carry party messages more effectively. That finding is an instance of Proposition~\ref{prop:ideological-power:credibility}: perceived independence raises the information value of a statement, so a ruling party can gain by permitting outlets that appear independent while retaining control over their limits. \citet{guriev2019} described the same logic for informational autocracies in general. Platforms extend the party's reach rather than escaping it: domestic platform firms operate under party supervision, and \citet{roberts2018} found that censorship relies mainly on friction and flooding, so that most users never meet the information that determined users can still find.
   373	
   374	Public benefits are part of the record. The early Soviet literacy campaigns that \citet{kenez1985} described expanded the population that could read, including what the party did not print. Source Proposition 4, that public benefit is compatible with hierarchy, applies here as elsewhere \citep{largo2026hbs}. The documented checks are weak in formal terms: there is no lawful independent press and no protected academic freedom. They consist of elite factions, professional norms within the sciences, and the preference falsification that makes displayed support an unreliable guide to private belief.
   375	
   376	\subsection{Democratic socialism and social democracy}
   377	
   378	In social democracies the ideological function is held by a mix of public and private institutions in which public institutions have a large role. Public service broadcasters, public universities, state-funded schools, the press of political parties and labor movements, and, in several Nordic countries, established Lutheran churches are the main holders. \citet{hallin2004} placed the media systems of Northern and Central Europe in their democratic corporatist model, in which mass-circulation commercial media coexisted with media tied to organized social and political groups, journalism was highly professionalized, and the state intervened actively through press subsidies and public broadcasting while legal norms limited its control over content.
   379	
   380	Concentration in broadcasting can be high, because a public broadcaster may hold a large audience share. Contestability then depends on the governance of that broadcaster: who appoints its board, how its budget is set, and whether editors are protected. Coupling to the political pillar runs through these appointment and budget channels, and Part II treats $C_{\pP\pI}$ as its pair. Coupling to the productive pillar is distinctive in this regime type. Unions and labor parties historically ran newspapers, educational associations and adult education, so the beliefs of the producing population were shaped partly by organizations that the producers themselves controlled. \citet{berman2006} argued that social democracy's defining idea was the primacy of politics over markets, an ideological commitment advanced through party organization. \citet{esping1990} argued that universal welfare programs build cross-class support for the welfare state, and \citet{rothstein1996} analyzed how the Swedish model depended on the administrative implementation of reforms. Universal programs thus have an ideological consequence: they produce shared beliefs about entitlement that sustain the programs themselves.
   381	
   382	The capture risk in this regime type is that a long-governing party turns public institutions into party instruments. The documented checks are structural. Hallin and Mancini describe the professional autonomy of journalists and the coexistence of public and commercial media, and the boards of public broadcasters in several countries are composed to represent multiple parties and social groups \citep{hallin2004}. Established churches in these states coexist with religious freedom, and \citet{fox2008} shows that state support of religion is common among democracies and does not by itself indicate control of belief.
   383	
   384	\subsection{Islamic states}
   385	
   386	Islamic states form a diverse class: the early and Abbasid caliphates, the Ottoman empire, Safavid and modern Iran, and Saudi Arabia differ in doctrine, in the organization of religious scholars and in the relation of scholars to rulers. The common feature is that political legitimacy is derived in part from religious law, which makes the ulama, the scholars of that law, central holders of the ideological function. Madrasas, mosques and their sermons, juristic opinions, and in modern states ministries of religious affairs and state seminaries are the main institutions.
   387	
   388	The history of the class contains a separation of religious authority from rule that is directly relevant to independence. \citet{crone1986} argued that early caliphs claimed religious authority as deputies of God and that this authority passed to the scholars over the first centuries of Islam; the failure of the caliph's inquisition, the \emph{mihna}, to impose a doctrine on the scholars marked the transition. The case is a documented check: scholars refused an endorsement that the ruler demanded, and the ruler's successors abandoned the demand. \citet{makdisi1981} traced the madrasa as an endowed college of law, financed by charitable endowments that gave scholars a revenue base distinct from the ruler's treasury. \citet{berkey1992} showed that in medieval Cairo the transmission of knowledge remained personal, from teacher to student, even as ruling elites endowed madrasas, which coupled patronage to scholarship without placing scholarly authorization under the patrons' control. \citet{crone2004} surveyed six centuries of medieval Islamic political thought, which itself records a range of views on the obligations of rulers to scholars and law.
   389	
   390	Later states increased the coupling. In the Ottoman empire the learned hierarchy was organized as a career of salaried officials under the chief jurist, the \c{S}eyh\"ulislam, and \citet{imber1997} showed how the chief jurist Ebu's-su'ud harmonized sultanic law with the sharia; $C_{\pP\pI}$ was correspondingly high, while \citet{barkey2008} emphasized the empire's reliance on brokered intermediaries and its accommodation of diversity. In Saudi Arabia, \citet{commins2006} and \citet{alrasheed2002} describe an alliance between the ruling dynasty and the Wahhabi religious establishment, in which scholars legitimated the dynasty and received authority over religious education and public morals. In Iran, \citet{arjomand1988} analyzed how the revolution of 1979 created a clerical state, building on a doctrine of guardianship by the jurist that \citet{khomeini1981} had set out, and \citet{menashri1992} traced the relation between education and state ideology in modern Iran. Here the fusion of religious and political authority raises $C_{\pP\pI}$ and $C_{\pJ\pI}$ toward their maximum, although the Shia clergy's older tradition of plural, independently followed authorities remains a source of internal diversity.
   391	
   392	The medieval checks on rulers were juristic pluralism across schools of law, endowed revenue, and scholarly reputation built on teacher-to-student authorization. \citet{gellner1981} stressed a further division, between urban scripturalist scholarship and rural forms of religious authority, which kept any single body from monopolizing religious legitimacy.
   393	
   394	In the modern period the main check has been the fragmentation of religious authority. \citet{eickelman1992} and \citet{eickelman1996} showed that mass higher education and new media multiplied the people able to claim religious authority, and \citet{zaman2002} showed that the ulama adapted to this competition and remained influential.
   395	
   396	Whether alliances between ulama and states caused authoritarianism \citep{kuru2019}, or whether legitimacy bargains between rulers and religious authorities shaped economic paths \citep{rubin2017}, remains an open debate. Across the class, concentration and coupling range from low, where scholars held endowed and plural authority, to very high, where religious authority was absorbed into the state. The class is defined by its source of legitimacy, not by a single configuration.
   397	
   398	\subsection{Catholic monarchies}
   399	
   400	In the Catholic monarchies of early modern Europe, Habsburg Spain, Bourbon France and the Papal States, the ideological function was shared between the Church and the crown. The Church supplied doctrine, clergy, sacraments, universities and religious orders; the crown supplied patronage, appointment rights and the coercive backing of religious courts. \citet{hsia1998} described the Catholic renewal after the Council of Trent, including the expansion of Jesuit colleges, which made the Society of Jesus one of the largest educational networks of the period. \citet{fragnito2001} and her collaborators documented the work of the Roman congregations that maintained the Index of Prohibited Books and licensed printing in Italy. \citet{eisenstein1979} argued that print transformed the conditions of religious and scholarly authority, which made licensing and indexing central instruments of control.
   401	
   402	The configuration varied. In the Papal States temporal and spiritual authority were held by the same sovereign, so $C_{\pP\pI}$ reached its maximum. In Habsburg Spain the Inquisition operated under royal as well as papal authority and coupled the ideological pillar to the judicial and coercive pillars. \citet{kamen1997} argued that the Inquisition's scale and severity were smaller than the black legend held and that it served local and royal interests as much as doctrinal ones; that revision is itself debated, and the quantitative studies of trial records collected by \citet{henningsen1986} supply the evidence on which the debate turns. In Bourbon France, \citet{burke1992} showed how the image of Louis XIV was manufactured by artists, writers and academies working for the crown, and \citet{bossuet1990} supplied the scriptural theory of divine-right monarchy. \citet{kantorowicz1957} traced the older political theology of the king's two bodies on which such theories drew.
   403	
   404	The transnational Church was also a check on crowns, because its appointment and revenue lay partly outside any single kingdom. In Mann's terms its ideological power was transcendent \citep{mann1986}, and \citet{grzymala2023} argued that rivalry between the papacy and rulers shaped European state building. Within France, \citet{vankley1996} traced how conflicts between Jansenists, the Gallican tradition, the papacy and the crown, with the parlements often siding with the Jansenists, eroded the sacral authority of the monarchy before 1789. These were counter-publics in Fraser's sense \citep{fraser1990}, operating inside a confessional state.
   405	
   406	\subsection{Secular democracies}
   407	
   408	In secular democracies the ideological function is distributed among a legally free press, universities with academic freedom, scientific academies and journals, professional bodies, civil society organizations and religious communities that are either separated from the state or established on plural terms. The model is the public sphere that \citet{habermas1989} reconstructed, with its later commercialization, and the counterpublics that \citet{fraser1990} added. Constitutional speech protections and independent courts, analyzed in Part III, set the legal boundary of the layer.
   409	
   410	Concentration is low in law and variable in fact. Media markets can be concentrated, and the liberal model of \citet{hallin2004} relies on commercial media with weak public broadcasting. Coupling to the financial pillar runs through advertising and research funding, as in the market-capitalist case. Coupling to the political pillar runs through appointments to public science agencies, school curricula and the governance of public broadcasting. The relation to religion differs across democracies. \citet{kuru2009} contrasted the passive secularism of the United States, which permits public religious expression, with the assertive secularism of France and Turkey, where the state excludes religion from public institutions; in Turkey the state's directorate of religious affairs administers mosques and appoints their imams, which shows that state control of religious authority is compatible with a secular constitution. \citet{grzymala2015} found that churches whose moral authority is fused with national identity, as in Ireland and Poland, influenced policy through institutional access, while \citet{casanova1994} showed that religions entered public debate as participants rather than as state authorities.
   411	
   412	Platform intermediaries raise the same question in secular democracies as in market economies, with one addition: their moderation decisions are taken by private firms under speech protections that bind governments but not, in most jurisdictions, the firms themselves \citep{gillespie2019}. Contestability over reach therefore depends on competition among platforms and on their own appeal procedures more than on courts.
   413	
   414	The capture risk in secular democracies is less fusion than conversion: financial power converted into credibility through sponsorship, or political power converted into control of a public broadcaster. The documented checks are the twin tolerations \citep{stepan2000}, judicial protection of expression, the plurality of outlets that makes media capture costly \citep{besley2006}, and the social process of critical scrutiny that \citet{oreskes2019} identified in science.
   415	
   416	\subsection{Summary across regimes}
   417	
   418	Table~\ref{tab:regimes} summarizes the comparison. Each regime type implements the ideological function, as Theorem~\ref{thm:ideological-power:necessity} requires. The types differ in which institutions hold the function, how concentrated control over authoritative outputs is, which other pillars it is coupled to, and what keeps authorities independent.
   419	
   420	\begin{table}[t]
   421	\centering
   422	\small
   423	\caption{The ideological function across six regime types. Entries are qualitative codings from the sources cited in the text; no index value is estimated for any polity.}
   424	\label{tab:regimes}
   425	\begin{tabularx}{\textwidth}{@{}L{2.3cm}YYY@{}}
   426	\toprule
   427	Regime type & Main holders & Concentration and coupling & Main sources of contestability \\
   428	\midrule
   429	Market capitalism & Private media, universities, journals, professions and certifying agencies & Moderate concentration that varies by sector, with strong financial coupling & Competition among outlets, disclosure, peer review and regulator reputation \\
   430	Communist party-state & Party propaganda organs, state media, party schools and academies & High formal concentration, with strong political and coercive coupling & Elite factions, professional norms and hidden private opinion \\
   431	Social democracy & Public broadcasters, public universities, labor and party press, established churches & Concentration high in some channels, with strong productive coupling through labor organizations & Plural boards, protected journalism and coexisting commercial media \\
   432	Islamic states & Ulama, madrasas, mosques, chief jurists and religious ministries & Ranges from low under endowed plural scholarship to very high under clerical rule & Juristic pluralism, endowed revenue and fragmentation of authority \\
   433	Catholic monarchies & Church hierarchy, orders, universities, Inquisition, Index and court culture & High crown and Church coupling, with full fusion in the Papal States & Partial independence of the transnational Church and theological conflict \\
   434	Secular democracies & Free press, universities, academies, civil society and religious bodies & Low legal concentration, with moderate financial and political coupling & Speech protections, plurality of outlets and scientific scrutiny \\
   435	\bottomrule
   436	\end{tabularx}
   437	\end{table}
   438	
   439	\section{Mechanisms, failure modes and checks}
   440	\label{sec:mechanisms}
   441	
   442	\subsection{From coordination to capture}
   443	
   444	Coordination in the ideological pillar becomes capture when a coalition gains control over what authorities say and that control weakens the review that would otherwise expose it. The source framework's capture link supplies the test \citep{largo2026hbs}. In the ideological layer its three conditions take a specific form. Privileged access means that a coalition funds, appoints, licenses or can dismiss an authority, or controls the channel through which it speaks. Weakened accountability means that the access is used to remove or evade review: findings are withheld, dissenting scholars are dismissed, sponsorship is concealed, presses are licensed selectively, or rival authorities are suppressed. Material evidence means documents, such as internal correspondence, censorship directives, appointment records or trial registries, that tie the access to a specific output, such as a published conclusion, a juristic opinion, a curriculum change or a broadcast.
   445	
   446	The same test says what is not capture. A church whose doctrine agrees with a government's policy is not thereby captured. Industry-funded research that is disclosed, preregistered and reproduced is not captured. A ruler's endowment of a college is patronage, which becomes capture only if it is used to control what the college certifies. A ministry of education is part of the differentiated structure that Proposition A predicts, and source Proposition 1 holds that differentiation is not integration \citep{largo2026hbs}. Public goods are a rival explanation for many configurations of the pillar: a public broadcaster or a state seminary may exist because it supplies information or instruction that markets or voluntary bodies would undersupply.
   447	
   448	\subsection{Endorsement and independence}
   449	
   450	The value of a legitimating authority to its audience depends on whether its statements track something other than the interest of whoever controls it. A simple model captures this.
   451	
   452	\begin{definition}[Endorsement model]
   453	\label{def:ideological-power:endorsement}
   454	A rule or policy is \emph{sound} ($\theta=G$) or \emph{unsound} ($\theta=B$), with public prior $\pi=\Prob(\theta=G)\in(0,1)$. An authority observes a private signal $s\in\{0,1\}$ with $\Prob(s=1\mid G)=\Prob(s=0\mid B)=q\in(\tfrac12,1)$. With probability $\lambda\in[0,1]$ the authority is \emph{independent} and endorses ($e=1$) if and only if $s=1$. With probability $1-\lambda$ it is \emph{captured} and endorses regardless of $s$. The public observes $e$ but neither $s$ nor the authority's type, knows $(\pi,q,\lambda)$, and forms the posterior $\mu=\Prob(G\mid e)$. Write $\mu_1(\lambda)=\Prob(G\mid e=1)$ and $\mu_0=\Prob(G\mid s=0)=\pi(1-q)/\bigl(\pi(1-q)+(1-\pi)q\bigr)$. For $\lambda\in(0,1]$, $\mu_0=\Prob(G\mid e=0)$; at $\lambda=0$ a refusal has probability zero and $\mu_0$ is the continuous extension.
   455	\end{definition}
   456	
   457	The parameter $\lambda$ summarizes what the components of $Q^{\pI}$ secure for a single authority. A tenured faculty, an endowed seminary, a juristic school with its own revenue, a regulator with a reputation to protect \citep{carpenter2010}, or an editor who cannot be dismissed for a story all raise $\lambda$.
   458	
   459	\begin{proposition}[Credibility and sorting]
   460	\label{prop:ideological-power:credibility}
   461	In the endorsement model:
   462	\begin{enumerate}
   463	\item[(a)] $\mu_1(0)=\pi$: a captured authority's endorsement carries no information.
   464	\item[(b)] $\mu_1(\lambda)$ is strictly increasing in $\lambda$, and $\mu_0<\pi$ does not depend on $\lambda$.
   465	\item[(c)] $\E[\mu\mid G]$ is strictly increasing and $\E[\mu\mid B]$ is strictly decreasing in $\lambda$.
   466	\end{enumerate}
   467	\end{proposition}
   468	
   469	\begin{proof}
   470	Let $a=\Prob(s=0)=\pi(1-q)+(1-\pi)q$. A refusal occurs only when the authority is independent and $s=0$, so $\Prob(e=0)=\lambda a$ and, for $\lambda>0$, $\Prob(G\mid e=0)=\Prob(G\mid s=0)=\pi(1-q)/a=\mu_0$, which does not depend on $\lambda$. Since $q>\tfrac12$, $\mu_0<\pi$.
   471	
   472	(a) and (b). By Bayes' rule,
   473	\[
   474	\mu_1(\lambda)=\frac{\pi\bigl(1-\lambda(1-q)\bigr)}{\pi\bigl(1-\lambda(1-q)\bigr)+(1-\pi)(1-\lambda q)}
   475	=\Bigl(1+\tfrac{1-\pi}{\pi}\,r(\lambda)\Bigr)^{-1},\qquad r(\lambda)=\frac{1-\lambda q}{1-\lambda(1-q)}.
   476	\]
   477	At $\lambda=0$, $r=1$ and $\mu_1=\pi$. Differentiating, $r'(\lambda)=(1-2q)/(1-\lambda(1-q))^2<0$, so $\mu_1$ is strictly increasing.
   478	
   479	(c) Posteriors are a martingale, so $\E[\mu]=\pi$, and $\E[\mu\,\mathbf{1}_G]=\E[\mu\,\Prob(G\mid e)]=\E[\mu^2]$. Hence $\E[\mu\mid G]=\E[\mu^2]/\pi$ and $\E[\mu\mid B]=(\pi-\E[\mu^2])/(1-\pi)$. It suffices to show that $\E[\mu^2]$ is strictly increasing in $\lambda$. From the martingale identity, $\Prob(e=1)\mu_1=\pi-\lambda a\mu_0$, so $\mu_1=(\pi-\lambda a\mu_0)/(1-\lambda a)$ and
   480	\[
   481	\E[\mu^2]=\frac{(\pi-\lambda a\mu_0)^2}{1-\lambda a}+\lambda a\mu_0^2 .
   482	\]
   483	Differentiating and substituting $\mu_1$,
   484	\[
   485	\frac{d\,\E[\mu^2]}{d\lambda}=a\mu_1\bigl(\mu_1-2\mu_0\bigr)+a\mu_0^2=a\,(\mu_1-\mu_0)^2 .
   486	\]
   487	By (b), $\mu_1(\lambda)\geq\pi>\mu_0$ for every $\lambda$, and $a>0$, so the derivative is strictly positive.
   488	\end{proof}
   489	
   490	Part (a) is the formal version of an old observation: praise from a courtier who must praise is worthless. Part (c) carries the argument further. Independent authorities are an asset to a coalition whose rules are sound and a liability to one whose rules are not. The same institution that lends credibility to a sound public-health rule exposes an unsound one. This is the precise sense in which healthcare, science and religious institutions can either check or enable capture: their independence is what makes their endorsement worth having, and it is also what makes them dangerous to a coalition that needs endorsement for an unsound rule. The next subsection turns the result into a comparative static for a governing coalition.
   491	
   492	
   493	\subsection{The control and credibility trade-off}
   494	
   495	A governing coalition values public confidence in its rules and also values control over authorities for its own sake, because control lets it direct authoritative outputs toward other ends. Independence is largely fixed in advance, by charters, endowments, tenure rules and appointment procedures, before the coalition knows whether the rules it will later need endorsed are sound. We therefore model the choice of $\lambda$ as an act of institutional design taken before $\theta$ is realized and observed by the public. Because the choice precedes $\theta$, it carries no information about $\theta$, and the public's prior remains $\pi$.
   496	
   497	\begin{proposition}[Control and credibility]
   498	\label{prop:ideological-power:tradeoff}
   499	Before $\theta$ is realized, a coalition chooses a publicly observed independence $\lambda\in[\lambda_{\min},1]$, where $\lambda_{\min}\in[0,1)$ is the independence that existing institutions guarantee whatever the coalition does. Its expected payoff is
   500	\[
   501	W(\lambda;\rho)=\pi\,\beta_G\,\E[\mu\mid G](\lambda)+(1-\pi)\,\beta_B\,\E[\mu\mid B](\lambda)+\rho\,(1-\lambda),
   502	\]
   503	where $\beta_G,\beta_B\geq0$ are the values the coalition places on public confidence when its rule is sound and unsound, and $\rho\geq0$ is the value of control. Let $\Delta=\beta_G-\beta_B$ and $S(\lambda)=\E[\mu^2](\lambda)$. Then:
   504	\begin{enumerate}
   505	\item[(a)] $W(\lambda;\rho)=\Delta\,S(\lambda)+\beta_B\pi+\rho(1-\lambda)$, and $S$ is strictly increasing and strictly convex.
   506	\item[(b)] If $\Delta<0$, or if $\Delta=0$ and $\rho>0$, the unique choice is $\lambda=\lambda_{\min}$.
   507	\item[(c)] If $\Delta>0$, every maximizer lies in $\{\lambda_{\min},1\}$, and $\lambda=1$ is the unique maximizer if and only if $\Delta\bigl(S(1)-S(\lambda_{\min})\bigr)>\rho\,(1-\lambda_{\min})$.
   508	\item[(d)] For fixed $\Delta$, every maximizer at a higher $\rho$ is weakly below every maximizer at a lower $\rho$.
   509	\end{enumerate}
   510	\end{proposition}
   511	
   512	\begin{proof}
   513	(a) By the identities in the proof of Proposition~\ref{prop:ideological-power:credibility}, $\pi\E[\mu\mid G]=S$ and $(1-\pi)\E[\mu\mid B]=\pi-S$. Substituting gives the expression for $W$. The same proof gives $S'(\lambda)=a(\mu_1(\lambda)-\mu_0)^2>0$. Since $\mu_1$ is strictly increasing and $\mu_1>\mu_0$, $S'$ is strictly increasing, so $S$ is strictly convex.
   514	
   515	(b) If $\Delta<0$, $\Delta S$ is strictly decreasing and $\rho(1-\lambda)$ is nonincreasing, so $W$ is strictly decreasing. If $\Delta=0$ and $\rho>0$, $W$ is strictly decreasing through its last term. In both cases $\lambda_{\min}$ is the unique maximizer.
   516	
   517	(c) If $\Delta>0$, $W$ is the sum of a strictly convex function and a linear one, hence strictly convex on $[\lambda_{\min},1]$, and a strictly convex function on a compact interval attains its maximum only at endpoints. Comparing the endpoints, $W(1)>W(\lambda_{\min})$ if and only if $\Delta(S(1)-S(\lambda_{\min}))>\rho(1-\lambda_{\min})$.
   518	
   519	(d) Let $\rho<\rho'$, let $\lambda$ maximize $W(\cdot;\rho)$ and $\lambda'$ maximize $W(\cdot;\rho')$. Optimality gives $W(\lambda;\rho)\geq W(\lambda';\rho)$ and $W(\lambda';\rho')\geq W(\lambda;\rho')$. Adding the two inequalities, the terms in $S$ cancel and what remains is $(\lambda'-\lambda)(\rho-\rho')\geq0$. Since $\rho-\rho'<0$, $\lambda'\leq\lambda$.
   520	\end{proof}
   521	
   522	The proposition is a conditional comparative static, and its key parameter is alignment. A coalition values independent authorities only when it gains more from public confidence in sound rules than in unsound ones ($\Delta>0$), which is the case when its interests run with the public's: a government that wants a vaccine taken because it works, not because a contract depends on it. A coalition whose gains do not depend on soundness ($\Delta\leq0$), such as one that profits from compliance with whatever rule it issues, pushes independence to the floor. The floor $\lambda_{\min}$, set by endowments, tenure, constitutional protection and transnational appointment, therefore protects the public exactly where alignment fails. Because $S$ is convex, the choice is all or nothing: aligned coalitions with a small value of control grant full independence, and the rest grant the minimum. Intermediate independence in the record reflects floors and constraints, not interior optima.
   523	
   524	Interim capture is different. After institutions are set and the public has formed a conjecture $\hat\lambda$, a coalition that has learned $\theta$ may be able to lower actual independence covertly, by pressuring editors or steering grants, without the public revising $\hat\lambda$.
   525	
   526	\begin{proposition}[Covert capture]
   527	\label{prop:ideological-power:covert}
   528	Suppose the public's posterior after an endorsement is $\mu_1(\hat\lambda)$ for a fixed conjecture $\hat\lambda>0$, while actual independence is $\lambda$. Then for $\theta\in\{G,B\}$,
   529	\[
   530	\E[\mu\mid\theta]=\mu_1(\hat\lambda)-\lambda\,\Prob(s=0\mid\theta)\bigl(\mu_1(\hat\lambda)-\mu_0\bigr),
   531	\]
   532	which is strictly decreasing in $\lambda$ for both types. The gain from a unit reduction of $\lambda$ is $q(\mu_1(\hat\lambda)-\mu_0)$ when the rule is unsound and $(1-q)(\mu_1(\hat\lambda)-\mu_0)$ when it is sound, so it is larger by the factor $q/(1-q)>1$ for a coalition whose rule is unsound.
   533	\end{proposition}
   534	
   535	\begin{proof}
   536	Given $\theta$, a refusal occurs with probability $\lambda\Prob(s=0\mid\theta)$ and yields the posterior $\mu_0$; otherwise the authority endorses and the public's posterior is $\mu_1(\hat\lambda)$. Taking the expectation gives the formula. Since $\mu_1(\hat\lambda)\geq\pi>\mu_0$ by Proposition~\ref{prop:ideological-power:credibility}(b), and $\Prob(s=0\mid B)=q$ and $\Prob(s=0\mid G)=1-q$ are positive, the expression is strictly decreasing in $\lambda$ with the stated slopes.
   537	\end{proof}
   538	
   539	Covert capture always raises expected confidence in the short run, because the public cannot discount what it does not see. Its value is greater for coalitions whose rules are unsound, since independent authorities would refuse them more often. If covert capture has a cost, coalitions with unsound rules will therefore pay it more often, and restrictions on independent authorities should follow adverse findings. Hypothesis HI7 in Section~\ref{sec:measurement} tests that prediction. If instead the coalition chose $\lambda$ openly after learning $\theta$, the choice would itself signal $\theta$ and the analysis would become a signaling game, which this paper does not solve. Commercialized but party-guided media in China \citep{stockmann2013} and the simulated democratic forms of informational autocracies \citep{guriev2019} fit the covert pattern: control is exercised while the appearance of independence is maintained.
   540	
   541	The covert case points to the main channel of deception. After an endorsement the public's posterior is $\mu_1(\hat\lambda)$, while the true probability that the rule is sound given an endorsement is $\mu_1(\lambda)$.
   542	
   543	\begin{corollary}[Deception gap]
   544	\label{cor:ideological-power:gap}
   545	The public overestimates the soundness of an endorsed rule, $\mu_1(\hat\lambda)>\mu_1(\lambda)$, if and only if $\hat\lambda>\lambda$. The gap $\mu_1(\hat\lambda)-\mu_1(\lambda)$ is strictly increasing in $\hat\lambda$ and strictly decreasing in $\lambda$.
   546	\end{corollary}
   547	
   548	\begin{proof}
   549	Immediate from the strict monotonicity of $\mu_1$ in Proposition~\ref{prop:ideological-power:credibility}(b).

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '280,449p' papers/latex/ideological-power.tex | nl -ba -v280" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   280	\citet{boehm1999} argued that mobile foragers maintain equality through a reverse dominance hierarchy in which the group as a whole suppresses would-be dominators by gossip, ridicule, ostracism and, in extreme cases, killing. The sanctions belong to Part V. The shared moral understanding that identifies what counts as domination belongs here. \citet{woodburn1982} made the parallel point for immediate-return societies: equality there is an institutional outcome produced by leveling practices, not the absence of institutions.
   281	
   282	\citet{ostrom1990} showed that long-enduring commons are governed by rules that users know, can modify and monitor. The design principles are institutional, not ideological, but each presupposes that the operative rules are common knowledge among appropriators. \citet{graeber2021} added that some societies alternated seasonally between hierarchical and egalitarian arrangements, each publicly marked. Their claims are contested and are cited here only for the narrow point that political arrangements were publicly recognized as such.
   283	
   284	These cases come with standard caveats. Contact-era ethnography observed groups in marginal environments, sometimes idealized them, and generalized from few cases \citep{kelly1995}. None of these caveats affects the narrow claim of Proposition~\ref{prop:ideological-power:minimal-form}. Each caveat would matter if the claim were that these societies show the original condition of humanity; the claim is only that they show the function without the office.
   285	
   286	\subsection{Counterexample attempts}
   287	
   288	The most serious attempt to defeat the necessity claim is coordination by force alone. On this view a sufficiently strong coercive apparatus needs no shared beliefs; it needs soldiers and prisons. The reply is that force itself depends on common knowledge. A sanction rule deters only if the people it targets know it, and a coercive organization holds together only if its members expect one another to carry out orders. \citet{kuran1991} showed that regimes resting on public displays of support can collapse suddenly when private opposition becomes common knowledge, which is evidence that rulers depend on controlling what is common knowledge even when they rely on force. \citet{svolik2012} treats the control of information among elites as a central problem of authoritarian rule. The attempt fails for recognition. It succeeds against a stronger thesis, that normative legitimacy is necessary, which Remark~\ref{rem:ideological-power:scope} has already abandoned.
   289	
   290	A second attempt holds that markets coordinate through prices without shared beliefs. Prices do economize on information. But exchange presupposes common knowledge of property conventions: who owns what, what counts as payment, and which contracts are binding. Those conventions are part of $R_t$, and they are taught, displayed and defended. \citet{hayek1973} himself stressed that the order of a market society rests on rules of just conduct that people follow without being able to state them; following a rule one cannot state is compatible with common knowledge of the practice it supports.
   291	
   292	A third attempt notes that in a small face-to-face group everyone observes everyone, so common knowledge arises from co-presence without any practice designed to produce it. This is correct and is the minimal form, not a counterexample. Co-present talk is a practice that produces public events.
   293	
   294	A fourth attempt points to coordination without beliefs in animal societies. The non-innateness assumption excludes it, and the exclusion is principled: where rules are fixed by development, no transmission is needed. The theorem is a claim about human governance, where rules vary.
   295	
   296	The falsifier follows from the assumptions. The necessity claim would be refuted by a persistent human collective, with turnover and with rules that differ from its neighbors', in which entrants come to coordinate on the local rules without any practice that informs them of the rules and without any public event that certifies them. We know of no such case in the sources reviewed.
   297	
   298	\subsection{Function and institution}
   299	
   300	Two classic errors of functionalism must be avoided. \citet{hempel1959} showed that from the premise that a function is needed one cannot infer that a particular institution exists, because functional equivalents may meet the need. Theorem~\ref{thm:ideological-power:necessity} respects this limit: it asserts that some practice in a class is implemented, and the class includes campfire talk and state broadcasting alike. \citet{elster1983} argued that explaining an institution by its beneficial effects requires a feedback mechanism from effect to institution. The theorem is not such an explanation. It is a condition of persistence: collectives that lack the function do not function, whatever the reason the function arose. It does not explain why a given regime has a ministry of religious affairs or a public broadcaster, and the comparative sections never use it for that purpose. \citet{merton1968} supplies the remaining vocabulary: the manifest function of a university is teaching and research, and its latent function in the ideological layer may include certifying elites, which is a separate empirical question.
   301	
   302	\section{Literature on ideological power}
   303	\label{sec:literature}
   304	
   305	\subsection{Consent and coercion}
   306	
   307	The modern study of ideological power begins with the observation that rule rests on consent as well as force. \citet{gramsci1971} called the organization of consent through civil society hegemony and argued that in societies with dense churches, schools, associations and presses, rulers depend on these institutions as much as on the state's coercive apparatus. \citet{althusser1971} sharpened the contrast into a distinction between repressive and ideological state apparatuses, the latter including churches, schools, families, the media and cultural institutions, and he argued that in mature capitalism the school had displaced the church as the dominant ideological apparatus. Both accounts treat ideological institutions as functional supports of a ruling class. That functional reading is precisely what \citet{elster1983} criticized, and it is what the present paper avoids: we claim the necessity of a function, not that any given apparatus exists because it serves a class.
   308	
   309	\citet{weber1978} placed belief at the center of domination by distinguishing traditional, charismatic and rational-legal grounds of legitimacy. Part II uses the Weberian types to analyze who makes rules. This Part takes from Weber only the distinction between compliance grounded in belief and compliance grounded in fear or interest, which becomes the distinction between normative legitimacy and recognition in Definition~\ref{def:ideological-power:recognition}.
   310	
   311	\subsection{Faces of power and networks of meaning}
   312	
   313	\citet{bachrach1962} argued that power is exercised not only in decisions but also in non-decisions, by keeping issues off the agenda. \citet{lukes2005} added a third dimension: the power to shape preferences so that conflicts of interest never surface. Part II owns agenda control, the power to determine which proposals reach a decision, as an object of rule-making (Definition 2.9 of Part II). The third dimension belongs here, because shaping preferences is shaping beliefs. The difficulty Lukes acknowledged is measurement: claims about preferences that people would hold but for ideological influence require a counterfactual that is hard to observe. The endorsement model of Section~\ref{sec:mechanisms} sidesteps the problem by studying a narrower and observable quantity, the information content of an authority's statements.
   314	
   315	\citet{mann1986,mann1993} gave the most developed comparative-historical account. He distinguished ideological, economic, military and political networks of power and treated none as primary. Ideological power, in his account, derives from the human need for meaning, norms and aesthetic and ritual practice, and it can be transcendent, organizing a community across political boundaries as the world religions did, or immanent, reinforcing the morale of an existing group. Mann's framework is the closest predecessor of the six-pillar model. It lacks a separate judicial pillar and a separate pillar for the producing population, and it has no measure of capture; Part VII compares the frameworks in detail. Its value here is the distinction between transcendent and immanent ideological power, which maps onto the difference between authorities whose appointment and revenue lie outside the polity, such as a transnational church, and authorities created by the polity itself.
   316	
   317	\citet{bourdieu1989,bourdieu1991} described symbolic power as the power to constitute the given by stating it, effective to the degree that it is misrecognized as something other than power. His account of the convertibility of economic, cultural and symbolic capital anticipates the cross-pillar coupling $C_{\pF\pI}$, which Part I treats as its pair. \citet{bourdieu1977} applied the account to schooling, arguing that educational systems reproduce class structure while appearing meritocratic.
   318	
   319	\subsection{The public sphere and the media}
   320	
   321	\citet{habermas1989} traced the rise of a bourgeois public sphere of rational-critical debate in eighteenth-century Europe and its later refeudalization, as mass media and organized interests turned a reasoning public into an audience. \citet{fraser1990} argued that the bourgeois public sphere excluded women, workers and others, who formed subaltern counterpublics of their own. Both accounts bear on the plurality component of $Q^{\pI}$: a public sphere is contestable to the degree that counterpublics can form and be heard.
   322	
   323	The political economy of the media divides on the question of supply and demand. \citet{herman1988} proposed a propaganda model in which ownership, advertising, reliance on official sources, organized flak and a dominant ideology filter news in favor of elite interests. The model predicts that owner and advertiser interests shape content. \citet{gentzkow2006} showed instead that slant can arise from demand: outlets that wish to appear accurate tilt reports toward their audience's prior beliefs, so slant can exist without any owner's design. \citet{djankov2003} assembled cross-country data on media ownership and found that the largest media firms were typically controlled by governments or by private families, and that state ownership was associated with weaker press freedom and political rights. \citet{besley2006} modeled media capture by government and showed that capture is harder when there are more independent outlets and when bribing them is costly, which links plurality directly to accountability. \citet{hallin2004} classified Western media systems into liberal, democratic corporatist and polarized pluralist models, differing in the strength of commercial media, the degree of political parallelism, journalistic professionalization and the role of the state.
   324	
   325	Persuasion effects are measurable. \citet{dellavigna2007} exploited the staggered entry of a cable news channel into United States towns and found an effect on presidential vote shares. \citet{enikolopov2011} found that access to the one national television channel independent of the government in Russia's 1999 parliamentary election reduced votes for the government's party and raised votes for opposition parties. These studies establish that the ideological layer has real edges: control of a channel changes political behavior.
   326	
   327	Authoritarian information control has its own literature. \citet{king2013} analyzed censorship of Chinese social media and found that posts criticizing the state were often left standing while posts with potential for collective action were removed. \citet{stockmann2013} found that commercialized Chinese media were perceived as more credible than official outlets and could therefore carry the party's messages more persuasively. \citet{guriev2019,guriev2022} described a shift from rule by fear to rule by spin, in which leaders manipulate information while simulating democratic forms; Part II treats this as a strategy of rule-makers. \citet{kuran1991} analyzed preference falsification, in which citizens publicly support regimes they privately oppose, and explained why the revolutions of 1989 surprised observers.
   328	
   329	Digital platforms add a layer of intermediaries between authorities and audiences. \citet{gillespie2019} argued that moderation of what users may post is not incidental to platforms but constitutive of them, so platform firms make continual decisions about which speech reaches whom. \citet{allcott2017} found that fabricated news stories circulated widely on social media before the 2016 United States election, while estimated exposure per adult was modest. \citet{guess2023} replaced the algorithmic feeds of consenting Facebook and Instagram users with reverse-chronological feeds for three months during the 2020 campaign and found large changes in what users saw but no detectable change in polarization or political attitudes. \citet{roberts2018} showed that Chinese censorship works less through fear than through friction and flooding, which make unwanted information costly to find rather than impossible. Platforms are thus channels whose control shares and contestability can be coded like those of broadcasters, with the difference that ranking and moderation decisions are made at very large scale by few organizations.
   330	
   331	\subsection{Professions and expert authority}
   332	
   333	Professions convert knowledge into authority. \citet{larson1977} described the professional project as an effort to secure market closure and social standing through control of training and credentials. \citet{abbott1988} treated professions as competitors for jurisdiction over tasks. \citet{freidson1970} argued that medicine's autonomy, its control over the content of its own work, made it the model profession, and \citet{starr1982} traced how American medicine converted cultural authority into economic power and professional sovereignty. These accounts explain why expert authority is valuable to rulers: experts certify that a rule is sound in terms the public trusts.
   334	
   335	Evidence on sponsorship qualifies that trust without destroying it. \citet{bekelman2003} reviewed studies of financial conflicts of interest in biomedical research and found that industry sponsorship was associated with conclusions favorable to sponsors. \citet{lexchin2003} reached a similar conclusion for pharmaceutical sponsorship, and the Cochrane review by \citet{lundh2017} found that industry-sponsored drug and device studies more often reported favorable results and conclusions than studies with other sponsors. \citet{oreskes2010} documented campaigns in which a small number of scientists, with industry support, manufactured doubt about the harms of tobacco and about environmental science. Against these findings stand accounts of why science remains trustworthy. \citet{oreskes2019} located the reliability of science in its social process of critical vetting by a diverse community, and \citet{carpenter2010} showed that the United States Food and Drug Administration built autonomy on its reputation for scientific judgment. \citet{slaughter2004} documented the growing market orientation of universities, which raises the coupling between the financial and ideological pillars. Read together, this literature supports the model of Definition~\ref{def:ideological-power:endorsement}: expert authorities are informative to the degree that their judgments are independent of their sponsors, and institutions such as disclosure, review and reputation exist to secure that independence.
   336	
   337	\subsection{Religion and the state}
   338	
   339	The relation between religious authority and political rule is the oldest problem of the ideological pillar. \citet{stepan2000} proposed the twin tolerations as the condition for democracy: elected institutions free from religious veto, and religious citizens free to worship and to advance their views in public. \citet{casanova1994} documented the deprivatization of religion, its return to public life in several countries from the 1980s. \citet{philpott2007} argued that religious actors' political behavior depends on their institutional independence from the state and on their political theology. \citet{fox2008} coded religion-state arrangements worldwide. \citet{kuru2009} distinguished passive secularism, which allows public religious expression, from assertive secularism, which excludes it.
   340	
   341	Two debates concern Islamic and Catholic polities directly. \citet{kuru2019} argued that an alliance between ulama and the state, formed in the eleventh century, helps explain authoritarianism and underdevelopment in many Muslim-majority countries. \citet{rubin2017} argued that rulers who depended on religious authorities for legitimacy faced different incentives from rulers who depended on economic elites, and that the difference shaped economic divergence. Both arguments are contested, and the series cites them as positions, not settled findings. For Catholic Europe, \citet{grzymala2023} argued that the medieval Church served as a template and rival for state building, and \citet{grzymala2015} showed that churches whose moral authority is fused with national identity can shape policy through institutional access rather than partisan politics.
   342	
   343	\subsection{Relation to prior work}
   344	
   345	Coordination theory \citep{lewis1969,schelling1960,aumann1976,chwe2001} explains why some practice must make rules common knowledge. The political economy of media and expertise \citep{besley2006,gentzkow2006,carpenter2010} explains why the value of a statement depends on the independence of its source. Comparative work on religion, media and education describes how the institutions vary. No existing framework combines the three: none derives the function from an axiom, states when its institutions check or enable capture, and compares regimes on the same measures. The source framework provides the measures \citep{largo2026hbs}. The present paper adds the derivation and the pillar-level model and applies both to six regime types.
   346	
   347	\section{Comparative analysis across six regime types}
   348	\label{sec:comparative}
   349	
   350	Every regime type implements the ideological function; they differ in which institutions hold it, how tightly one coalition controls their appointments and revenue, and which other pillars that coalition also commands. The comparison below codes these differences qualitatively from secondary sources. No numerical value of $H^{\pI}$, $Q^{\pI}$, $U_t$ or $\Int_t$ is reported for any polity, because no preregistered coding exists.
   351	
   352	The couplings of the ideological pillar to finance, rule-making and adjudication ($C_{\pF\pI}$, $C_{\pP\pI}$, $C_{\pJ\pI}$) are analyzed primarily in Parts I, II and III; this paper treats the couplings to coercion and production ($C_{\pI\pC}$, $C_{\pI\pW}$).
   353	
   354	\subsection{Market-capitalist societies}
   355	
   356	In market-capitalist societies the ideological function is held by many organizations with separate ownership and funding: privately owned media firms financed by advertising and subscriptions, public and private universities, foundations and think tanks, professional associations, scientific journals, regulatory agencies in their certifying role, and religious bodies organized as voluntary associations. Control over authoritative outputs is spread across these organizations, so $H^{\pI}$ is moderate overall, but it varies by sector. Ownership of the largest media firms is often concentrated in a few families \citep{djankov2003}, while accreditation of physicians or approval of drugs may rest with a single professional body or agency.
   357	
   358	The distinctive coupling is between the financial and ideological pillars. Advertising finances news, endowments and grants finance universities, and industry finances a large share of clinical research. \citet{herman1988} built their propaganda model on this coupling. \citet{slaughter2004} documented the movement of universities toward market revenue, and \citet{starr1982} described how medical authority was converted into economic power and later confronted corporate organization of care. Part I treats $C_{\pF\pI}$ as its pair and measures the conversion of financial control into favorable outputs of other pillars by a conversion elasticity (Definition 6.1 of Part I); here the question is what the coupling does to the independence parameter $\lambda$ of Definition~\ref{def:ideological-power:endorsement}.
   359	
   360	The documented capture episodes are sectoral. Systematic reviews associate industry sponsorship with conclusions favorable to sponsors \citep{bekelman2003,lexchin2003,lundh2017}. \citet{oreskes2010} documented organized efforts to manufacture doubt about tobacco harms and environmental hazards. Each case meets the three conditions of a capture link: privileged access through funding, weakened contestability through selective publication or orchestrated doubt, and material evidence linking the asymmetry to an output, whether a published conclusion or a delayed regulation.
   361	
   362	Platform firms now hold part of the function in this regime type. A few companies decide, through ranking and moderation, which statements by journalists, scientists and clergy reach large audiences \citep{gillespie2019}. In the terms of Section~\ref{sec:layer}, they hold a large share of control over reach, one of the outputs that defines $s^{\pI}$, so they raise measured concentration even when the number of speakers grows. The evidence on their persuasive effect is mixed: fabricated stories spread widely \citep{allcott2017}, but an experimental change of feed ranking during an election left attitudes unchanged \citep{guess2023}. Control over reach is established; its translation into belief is an open empirical question.
   363	
   364	The documented checks are also sectoral. Competition among outlets makes media capture costly \citep{besley2006}. Demand-side slant \citep{gentzkow2006} is a rival explanation for partisan coverage that does not require owner control, so evidence of slant is not by itself evidence of capture. Disclosure rules, peer review, replication and the reputational autonomy of regulators \citep{carpenter2010} raise $\lambda$. The capture episodes above were themselves discovered through litigation, journalism and meta-research, which is what source hypothesis H4 predicts: higher rates of documented error discovery can signal stronger accountability rather than more capture \citep{largo2026hbs}.
   365	
   366	\subsection{Communist party-states}
   367	
   368	In communist party-states the ruling party claims the ideological function as part of its leading role. Party propaganda departments, state newspapers and broadcasters, party schools, academies of sciences, writers' and artists' unions and a compulsory curriculum in Marxism-Leninism hold the function. \citet{kenez1985} described how the Bolsheviks built a propaganda state in their first decade, combining agitation, literacy campaigns and new media under party direction. \citet{brooks2000} showed how the Soviet press under Stalin organized public culture as a ritual in which achievements were presented as gifts from the leadership and citizens were expected to express gratitude.
   369	
   370	Concentration is high by design. Appointments of editors, rectors and academy presidents pass through the party's appointment channel, the map from a coalition to the offices it fills in each pillar (Definition 2.8 of Part II), so $C_{\pP\pI}$ is high and $H^{\pI}$ approaches its maximum in the formal structure. Coupling to the coercive pillar is strong: censorship offices and security services enforce the boundaries of permissible expression, and Part V treats the security services themselves. \citet{althusser1971}'s concept of ideological state apparatuses, developed within Marxism, describes this configuration more literally than it describes the societies Althusser had in mind.
   371	
   372	Formal structure overstates actual control. \citet{lane1995} found commonalities and divisions within the Soviet ruling elite in its last decade, and divisions within the elite reduce the effective concentration of control over authoritative outputs. \citet{kuran1991} explained the sudden collapse of East European regimes in 1989 as the release of privately held opposition that public displays had concealed. In the People's Republic of China, \citet{king2013} found that censors removed posts with potential for collective action more consistently than posts criticizing officials, which shows a discriminating rather than total control of expression. \citet{stockmann2013} found that commercialized media, perceived as more credible than official outlets, could carry party messages more effectively. That finding is an instance of Proposition~\ref{prop:ideological-power:credibility}: perceived independence raises the information value of a statement, so a ruling party can gain by permitting outlets that appear independent while retaining control over their limits. \citet{guriev2019} described the same logic for informational autocracies in general. Platforms extend the party's reach rather than escaping it: domestic platform firms operate under party supervision, and \citet{roberts2018} found that censorship relies mainly on friction and flooding, so that most users never meet the information that determined users can still find.
   373	
   374	Public benefits are part of the record. The early Soviet literacy campaigns that \citet{kenez1985} described expanded the population that could read, including what the party did not print. Source Proposition 4, that public benefit is compatible with hierarchy, applies here as elsewhere \citep{largo2026hbs}. The documented checks are weak in formal terms: there is no lawful independent press and no protected academic freedom. They consist of elite factions, professional norms within the sciences, and the preference falsification that makes displayed support an unreliable guide to private belief.
   375	
   376	\subsection{Democratic socialism and social democracy}
   377	
   378	In social democracies the ideological function is held by a mix of public and private institutions in which public institutions have a large role. Public service broadcasters, public universities, state-funded schools, the press of political parties and labor movements, and, in several Nordic countries, established Lutheran churches are the main holders. \citet{hallin2004} placed the media systems of Northern and Central Europe in their democratic corporatist model, in which mass-circulation commercial media coexisted with media tied to organized social and political groups, journalism was highly professionalized, and the state intervened actively through press subsidies and public broadcasting while legal norms limited its control over content.
   379	
   380	Concentration in broadcasting can be high, because a public broadcaster may hold a large audience share. Contestability then depends on the governance of that broadcaster: who appoints its board, how its budget is set, and whether editors are protected. Coupling to the political pillar runs through these appointment and budget channels, and Part II treats $C_{\pP\pI}$ as its pair. Coupling to the productive pillar is distinctive in this regime type. Unions and labor parties historically ran newspapers, educational associations and adult education, so the beliefs of the producing population were shaped partly by organizations that the producers themselves controlled. \citet{berman2006} argued that social democracy's defining idea was the primacy of politics over markets, an ideological commitment advanced through party organization. \citet{esping1990} argued that universal welfare programs build cross-class support for the welfare state, and \citet{rothstein1996} analyzed how the Swedish model depended on the administrative implementation of reforms. Universal programs thus have an ideological consequence: they produce shared beliefs about entitlement that sustain the programs themselves.
   381	
   382	The capture risk in this regime type is that a long-governing party turns public institutions into party instruments. The documented checks are structural. Hallin and Mancini describe the professional autonomy of journalists and the coexistence of public and commercial media, and the boards of public broadcasters in several countries are composed to represent multiple parties and social groups \citep{hallin2004}. Established churches in these states coexist with religious freedom, and \citet{fox2008} shows that state support of religion is common among democracies and does not by itself indicate control of belief.
   383	
   384	\subsection{Islamic states}
   385	
   386	Islamic states form a diverse class: the early and Abbasid caliphates, the Ottoman empire, Safavid and modern Iran, and Saudi Arabia differ in doctrine, in the organization of religious scholars and in the relation of scholars to rulers. The common feature is that political legitimacy is derived in part from religious law, which makes the ulama, the scholars of that law, central holders of the ideological function. Madrasas, mosques and their sermons, juristic opinions, and in modern states ministries of religious affairs and state seminaries are the main institutions.
   387	
   388	The history of the class contains a separation of religious authority from rule that is directly relevant to independence. \citet{crone1986} argued that early caliphs claimed religious authority as deputies of God and that this authority passed to the scholars over the first centuries of Islam; the failure of the caliph's inquisition, the \emph{mihna}, to impose a doctrine on the scholars marked the transition. The case is a documented check: scholars refused an endorsement that the ruler demanded, and the ruler's successors abandoned the demand. \citet{makdisi1981} traced the madrasa as an endowed college of law, financed by charitable endowments that gave scholars a revenue base distinct from the ruler's treasury. \citet{berkey1992} showed that in medieval Cairo the transmission of knowledge remained personal, from teacher to student, even as ruling elites endowed madrasas, which coupled patronage to scholarship without placing scholarly authorization under the patrons' control. \citet{crone2004} surveyed six centuries of medieval Islamic political thought, which itself records a range of views on the obligations of rulers to scholars and law.
   389	
   390	Later states increased the coupling. In the Ottoman empire the learned hierarchy was organized as a career of salaried officials under the chief jurist, the \c{S}eyh\"ulislam, and \citet{imber1997} showed how the chief jurist Ebu's-su'ud harmonized sultanic law with the sharia; $C_{\pP\pI}$ was correspondingly high, while \citet{barkey2008} emphasized the empire's reliance on brokered intermediaries and its accommodation of diversity. In Saudi Arabia, \citet{commins2006} and \citet{alrasheed2002} describe an alliance between the ruling dynasty and the Wahhabi religious establishment, in which scholars legitimated the dynasty and received authority over religious education and public morals. In Iran, \citet{arjomand1988} analyzed how the revolution of 1979 created a clerical state, building on a doctrine of guardianship by the jurist that \citet{khomeini1981} had set out, and \citet{menashri1992} traced the relation between education and state ideology in modern Iran. Here the fusion of religious and political authority raises $C_{\pP\pI}$ and $C_{\pJ\pI}$ toward their maximum, although the Shia clergy's older tradition of plural, independently followed authorities remains a source of internal diversity.
   391	
   392	The medieval checks on rulers were juristic pluralism across schools of law, endowed revenue, and scholarly reputation built on teacher-to-student authorization. \citet{gellner1981} stressed a further division, between urban scripturalist scholarship and rural forms of religious authority, which kept any single body from monopolizing religious legitimacy.
   393	
   394	In the modern period the main check has been the fragmentation of religious authority. \citet{eickelman1992} and \citet{eickelman1996} showed that mass higher education and new media multiplied the people able to claim religious authority, and \citet{zaman2002} showed that the ulama adapted to this competition and remained influential.
   395	
   396	Whether alliances between ulama and states caused authoritarianism \citep{kuru2019}, or whether legitimacy bargains between rulers and religious authorities shaped economic paths \citep{rubin2017}, remains an open debate. Across the class, concentration and coupling range from low, where scholars held endowed and plural authority, to very high, where religious authority was absorbed into the state. The class is defined by its source of legitimacy, not by a single configuration.
   397	
   398	\subsection{Catholic monarchies}
   399	
   400	In the Catholic monarchies of early modern Europe, Habsburg Spain, Bourbon France and the Papal States, the ideological function was shared between the Church and the crown. The Church supplied doctrine, clergy, sacraments, universities and religious orders; the crown supplied patronage, appointment rights and the coercive backing of religious courts. \citet{hsia1998} described the Catholic renewal after the Council of Trent, including the expansion of Jesuit colleges, which made the Society of Jesus one of the largest educational networks of the period. \citet{fragnito2001} and her collaborators documented the work of the Roman congregations that maintained the Index of Prohibited Books and licensed printing in Italy. \citet{eisenstein1979} argued that print transformed the conditions of religious and scholarly authority, which made licensing and indexing central instruments of control.
   401	
   402	The configuration varied. In the Papal States temporal and spiritual authority were held by the same sovereign, so $C_{\pP\pI}$ reached its maximum. In Habsburg Spain the Inquisition operated under royal as well as papal authority and coupled the ideological pillar to the judicial and coercive pillars. \citet{kamen1997} argued that the Inquisition's scale and severity were smaller than the black legend held and that it served local and royal interests as much as doctrinal ones; that revision is itself debated, and the quantitative studies of trial records collected by \citet{henningsen1986} supply the evidence on which the debate turns. In Bourbon France, \citet{burke1992} showed how the image of Louis XIV was manufactured by artists, writers and academies working for the crown, and \citet{bossuet1990} supplied the scriptural theory of divine-right monarchy. \citet{kantorowicz1957} traced the older political theology of the king's two bodies on which such theories drew.
   403	
   404	The transnational Church was also a check on crowns, because its appointment and revenue lay partly outside any single kingdom. In Mann's terms its ideological power was transcendent \citep{mann1986}, and \citet{grzymala2023} argued that rivalry between the papacy and rulers shaped European state building. Within France, \citet{vankley1996} traced how conflicts between Jansenists, the Gallican tradition, the papacy and the crown, with the parlements often siding with the Jansenists, eroded the sacral authority of the monarchy before 1789. These were counter-publics in Fraser's sense \citep{fraser1990}, operating inside a confessional state.
   405	
   406	\subsection{Secular democracies}
   407	
   408	In secular democracies the ideological function is distributed among a legally free press, universities with academic freedom, scientific academies and journals, professional bodies, civil society organizations and religious communities that are either separated from the state or established on plural terms. The model is the public sphere that \citet{habermas1989} reconstructed, with its later commercialization, and the counterpublics that \citet{fraser1990} added. Constitutional speech protections and independent courts, analyzed in Part III, set the legal boundary of the layer.
   409	
   410	Concentration is low in law and variable in fact. Media markets can be concentrated, and the liberal model of \citet{hallin2004} relies on commercial media with weak public broadcasting. Coupling to the financial pillar runs through advertising and research funding, as in the market-capitalist case. Coupling to the political pillar runs through appointments to public science agencies, school curricula and the governance of public broadcasting. The relation to religion differs across democracies. \citet{kuru2009} contrasted the passive secularism of the United States, which permits public religious expression, with the assertive secularism of France and Turkey, where the state excludes religion from public institutions; in Turkey the state's directorate of religious affairs administers mosques and appoints their imams, which shows that state control of religious authority is compatible with a secular constitution. \citet{grzymala2015} found that churches whose moral authority is fused with national identity, as in Ireland and Poland, influenced policy through institutional access, while \citet{casanova1994} showed that religions entered public debate as participants rather than as state authorities.
   411	
   412	Platform intermediaries raise the same question in secular democracies as in market economies, with one addition: their moderation decisions are taken by private firms under speech protections that bind governments but not, in most jurisdictions, the firms themselves \citep{gillespie2019}. Contestability over reach therefore depends on competition among platforms and on their own appeal procedures more than on courts.
   413	
   414	The capture risk in secular democracies is less fusion than conversion: financial power converted into credibility through sponsorship, or political power converted into control of a public broadcaster. The documented checks are the twin tolerations \citep{stepan2000}, judicial protection of expression, the plurality of outlets that makes media capture costly \citep{besley2006}, and the social process of critical scrutiny that \citet{oreskes2019} identified in science.
   415	
   416	\subsection{Summary across regimes}
   417	
   418	Table~\ref{tab:regimes} summarizes the comparison. Each regime type implements the ideological function, as Theorem~\ref{thm:ideological-power:necessity} requires. The types differ in which institutions hold the function, how concentrated control over authoritative outputs is, which other pillars it is coupled to, and what keeps authorities independent.
   419	
   420	\begin{table}[t]
   421	\centering
   422	\small
   423	\caption{The ideological function across six regime types. Entries are qualitative codings from the sources cited in the text; no index value is estimated for any polity.}
   424	\label{tab:regimes}
   425	\begin{tabularx}{\textwidth}{@{}L{2.3cm}YYY@{}}
   426	\toprule
   427	Regime type & Main holders & Concentration and coupling & Main sources of contestability \\
   428	\midrule
   429	Market capitalism & Private media, universities, journals, professions and certifying agencies & Moderate concentration that varies by sector, with strong financial coupling & Competition among outlets, disclosure, peer review and regulator reputation \\
   430	Communist party-state & Party propaganda organs, state media, party schools and academies & High formal concentration, with strong political and coercive coupling & Elite factions, professional norms and hidden private opinion \\
   431	Social democracy & Public broadcasters, public universities, labor and party press, established churches & Concentration high in some channels, with strong productive coupling through labor organizations & Plural boards, protected journalism and coexisting commercial media \\
   432	Islamic states & Ulama, madrasas, mosques, chief jurists and religious ministries & Ranges from low under endowed plural scholarship to very high under clerical rule & Juristic pluralism, endowed revenue and fragmentation of authority \\
   433	Catholic monarchies & Church hierarchy, orders, universities, Inquisition, Index and court culture & High crown and Church coupling, with full fusion in the Papal States & Partial independence of the transnational Church and theological conflict \\
   434	Secular democracies & Free press, universities, academies, civil society and religious bodies & Low legal concentration, with moderate financial and political coupling & Speech protections, plurality of outlets and scientific scrutiny \\
   435	\bottomrule
   436	\end{tabularx}
   437	\end{table}
   438	
   439	\section{Mechanisms, failure modes and checks}
   440	\label{sec:mechanisms}
   441	
   442	\subsection{From coordination to capture}
   443	
   444	Coordination in the ideological pillar becomes capture when a coalition gains control over what authorities say and that control weakens the review that would otherwise expose it. The source framework's capture link supplies the test \citep{largo2026hbs}. In the ideological layer its three conditions take a specific form. Privileged access means that a coalition funds, appoints, licenses or can dismiss an authority, or controls the channel through which it speaks. Weakened accountability means that the access is used to remove or evade review: findings are withheld, dissenting scholars are dismissed, sponsorship is concealed, presses are licensed selectively, or rival authorities are suppressed. Material evidence means documents, such as internal correspondence, censorship directives, appointment records or trial registries, that tie the access to a specific output, such as a published conclusion, a juristic opinion, a curriculum change or a broadcast.
   445	
   446	The same test says what is not capture. A church whose doctrine agrees with a government's policy is not thereby captured. Industry-funded research that is disclosed, preregistered and reproduced is not captured. A ruler's endowment of a college is patronage, which becomes capture only if it is used to control what the college certifies. A ministry of education is part of the differentiated structure that Proposition A predicts, and source Proposition 1 holds that differentiation is not integration \citep{largo2026hbs}. Public goods are a rival explanation for many configurations of the pillar: a public broadcaster or a state seminary may exist because it supplies information or instruction that markets or voluntary bodies would undersupply.
   447	
   448	\subsection{Endorsement and independence}
   449	

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '449,620p' papers/latex/ideological-power.tex | nl -ba -v449" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   449	
   450	The value of a legitimating authority to its audience depends on whether its statements track something other than the interest of whoever controls it. A simple model captures this.
   451	
   452	\begin{definition}[Endorsement model]
   453	\label{def:ideological-power:endorsement}
   454	A rule or policy is \emph{sound} ($\theta=G$) or \emph{unsound} ($\theta=B$), with public prior $\pi=\Prob(\theta=G)\in(0,1)$. An authority observes a private signal $s\in\{0,1\}$ with $\Prob(s=1\mid G)=\Prob(s=0\mid B)=q\in(\tfrac12,1)$. With probability $\lambda\in[0,1]$ the authority is \emph{independent} and endorses ($e=1$) if and only if $s=1$. With probability $1-\lambda$ it is \emph{captured} and endorses regardless of $s$. The public observes $e$ but neither $s$ nor the authority's type, knows $(\pi,q,\lambda)$, and forms the posterior $\mu=\Prob(G\mid e)$. Write $\mu_1(\lambda)=\Prob(G\mid e=1)$ and $\mu_0=\Prob(G\mid s=0)=\pi(1-q)/\bigl(\pi(1-q)+(1-\pi)q\bigr)$. For $\lambda\in(0,1]$, $\mu_0=\Prob(G\mid e=0)$; at $\lambda=0$ a refusal has probability zero and $\mu_0$ is the continuous extension.
   455	\end{definition}
   456	
   457	The parameter $\lambda$ summarizes what the components of $Q^{\pI}$ secure for a single authority. A tenured faculty, an endowed seminary, a juristic school with its own revenue, a regulator with a reputation to protect \citep{carpenter2010}, or an editor who cannot be dismissed for a story all raise $\lambda$.
   458	
   459	\begin{proposition}[Credibility and sorting]
   460	\label{prop:ideological-power:credibility}
   461	In the endorsement model:
   462	\begin{enumerate}
   463	\item[(a)] $\mu_1(0)=\pi$: a captured authority's endorsement carries no information.
   464	\item[(b)] $\mu_1(\lambda)$ is strictly increasing in $\lambda$, and $\mu_0<\pi$ does not depend on $\lambda$.
   465	\item[(c)] $\E[\mu\mid G]$ is strictly increasing and $\E[\mu\mid B]$ is strictly decreasing in $\lambda$.
   466	\end{enumerate}
   467	\end{proposition}
   468	
   469	\begin{proof}
   470	Let $a=\Prob(s=0)=\pi(1-q)+(1-\pi)q$. A refusal occurs only when the authority is independent and $s=0$, so $\Prob(e=0)=\lambda a$ and, for $\lambda>0$, $\Prob(G\mid e=0)=\Prob(G\mid s=0)=\pi(1-q)/a=\mu_0$, which does not depend on $\lambda$. Since $q>\tfrac12$, $\mu_0<\pi$.
   471	
   472	(a) and (b). By Bayes' rule,
   473	\[
   474	\mu_1(\lambda)=\frac{\pi\bigl(1-\lambda(1-q)\bigr)}{\pi\bigl(1-\lambda(1-q)\bigr)+(1-\pi)(1-\lambda q)}
   475	=\Bigl(1+\tfrac{1-\pi}{\pi}\,r(\lambda)\Bigr)^{-1},\qquad r(\lambda)=\frac{1-\lambda q}{1-\lambda(1-q)}.
   476	\]
   477	At $\lambda=0$, $r=1$ and $\mu_1=\pi$. Differentiating, $r'(\lambda)=(1-2q)/(1-\lambda(1-q))^2<0$, so $\mu_1$ is strictly increasing.
   478	
   479	(c) Posteriors are a martingale, so $\E[\mu]=\pi$, and $\E[\mu\,\mathbf{1}_G]=\E[\mu\,\Prob(G\mid e)]=\E[\mu^2]$. Hence $\E[\mu\mid G]=\E[\mu^2]/\pi$ and $\E[\mu\mid B]=(\pi-\E[\mu^2])/(1-\pi)$. It suffices to show that $\E[\mu^2]$ is strictly increasing in $\lambda$. From the martingale identity, $\Prob(e=1)\mu_1=\pi-\lambda a\mu_0$, so $\mu_1=(\pi-\lambda a\mu_0)/(1-\lambda a)$ and
   480	\[
   481	\E[\mu^2]=\frac{(\pi-\lambda a\mu_0)^2}{1-\lambda a}+\lambda a\mu_0^2 .
   482	\]
   483	Differentiating and substituting $\mu_1$,
   484	\[
   485	\frac{d\,\E[\mu^2]}{d\lambda}=a\mu_1\bigl(\mu_1-2\mu_0\bigr)+a\mu_0^2=a\,(\mu_1-\mu_0)^2 .
   486	\]
   487	By (b), $\mu_1(\lambda)\geq\pi>\mu_0$ for every $\lambda$, and $a>0$, so the derivative is strictly positive.
   488	\end{proof}
   489	
   490	Part (a) is the formal version of an old observation: praise from a courtier who must praise is worthless. Part (c) carries the argument further. Independent authorities are an asset to a coalition whose rules are sound and a liability to one whose rules are not. The same institution that lends credibility to a sound public-health rule exposes an unsound one. This is the precise sense in which healthcare, science and religious institutions can either check or enable capture: their independence is what makes their endorsement worth having, and it is also what makes them dangerous to a coalition that needs endorsement for an unsound rule. The next subsection turns the result into a comparative static for a governing coalition.
   491	
   492	
   493	\subsection{The control and credibility trade-off}
   494	
   495	A governing coalition values public confidence in its rules and also values control over authorities for its own sake, because control lets it direct authoritative outputs toward other ends. Independence is largely fixed in advance, by charters, endowments, tenure rules and appointment procedures, before the coalition knows whether the rules it will later need endorsed are sound. We therefore model the choice of $\lambda$ as an act of institutional design taken before $\theta$ is realized and observed by the public. Because the choice precedes $\theta$, it carries no information about $\theta$, and the public's prior remains $\pi$.
   496	
   497	\begin{proposition}[Control and credibility]
   498	\label{prop:ideological-power:tradeoff}
   499	Before $\theta$ is realized, a coalition chooses a publicly observed independence $\lambda\in[\lambda_{\min},1]$, where $\lambda_{\min}\in[0,1)$ is the independence that existing institutions guarantee whatever the coalition does. Its expected payoff is
   500	\[
   501	W(\lambda;\rho)=\pi\,\beta_G\,\E[\mu\mid G](\lambda)+(1-\pi)\,\beta_B\,\E[\mu\mid B](\lambda)+\rho\,(1-\lambda),
   502	\]
   503	where $\beta_G,\beta_B\geq0$ are the values the coalition places on public confidence when its rule is sound and unsound, and $\rho\geq0$ is the value of control. Let $\Delta=\beta_G-\beta_B$ and $S(\lambda)=\E[\mu^2](\lambda)$. Then:
   504	\begin{enumerate}
   505	\item[(a)] $W(\lambda;\rho)=\Delta\,S(\lambda)+\beta_B\pi+\rho(1-\lambda)$, and $S$ is strictly increasing and strictly convex.
   506	\item[(b)] If $\Delta<0$, or if $\Delta=0$ and $\rho>0$, the unique choice is $\lambda=\lambda_{\min}$.
   507	\item[(c)] If $\Delta>0$, every maximizer lies in $\{\lambda_{\min},1\}$, and $\lambda=1$ is the unique maximizer if and only if $\Delta\bigl(S(1)-S(\lambda_{\min})\bigr)>\rho\,(1-\lambda_{\min})$.
   508	\item[(d)] For fixed $\Delta$, every maximizer at a higher $\rho$ is weakly below every maximizer at a lower $\rho$.
   509	\end{enumerate}
   510	\end{proposition}
   511	
   512	\begin{proof}
   513	(a) By the identities in the proof of Proposition~\ref{prop:ideological-power:credibility}, $\pi\E[\mu\mid G]=S$ and $(1-\pi)\E[\mu\mid B]=\pi-S$. Substituting gives the expression for $W$. The same proof gives $S'(\lambda)=a(\mu_1(\lambda)-\mu_0)^2>0$. Since $\mu_1$ is strictly increasing and $\mu_1>\mu_0$, $S'$ is strictly increasing, so $S$ is strictly convex.
   514	
   515	(b) If $\Delta<0$, $\Delta S$ is strictly decreasing and $\rho(1-\lambda)$ is nonincreasing, so $W$ is strictly decreasing. If $\Delta=0$ and $\rho>0$, $W$ is strictly decreasing through its last term. In both cases $\lambda_{\min}$ is the unique maximizer.
   516	
   517	(c) If $\Delta>0$, $W$ is the sum of a strictly convex function and a linear one, hence strictly convex on $[\lambda_{\min},1]$, and a strictly convex function on a compact interval attains its maximum only at endpoints. Comparing the endpoints, $W(1)>W(\lambda_{\min})$ if and only if $\Delta(S(1)-S(\lambda_{\min}))>\rho(1-\lambda_{\min})$.
   518	
   519	(d) Let $\rho<\rho'$, let $\lambda$ maximize $W(\cdot;\rho)$ and $\lambda'$ maximize $W(\cdot;\rho')$. Optimality gives $W(\lambda;\rho)\geq W(\lambda';\rho)$ and $W(\lambda';\rho')\geq W(\lambda;\rho')$. Adding the two inequalities, the terms in $S$ cancel and what remains is $(\lambda'-\lambda)(\rho-\rho')\geq0$. Since $\rho-\rho'<0$, $\lambda'\leq\lambda$.
   520	\end{proof}
   521	
   522	The proposition is a conditional comparative static, and its key parameter is alignment. A coalition values independent authorities only when it gains more from public confidence in sound rules than in unsound ones ($\Delta>0$), which is the case when its interests run with the public's: a government that wants a vaccine taken because it works, not because a contract depends on it. A coalition whose gains do not depend on soundness ($\Delta\leq0$), such as one that profits from compliance with whatever rule it issues, pushes independence to the floor. The floor $\lambda_{\min}$, set by endowments, tenure, constitutional protection and transnational appointment, therefore protects the public exactly where alignment fails. Because $S$ is convex, the choice is all or nothing: aligned coalitions with a small value of control grant full independence, and the rest grant the minimum. Intermediate independence in the record reflects floors and constraints, not interior optima.
   523	
   524	Interim capture is different. After institutions are set and the public has formed a conjecture $\hat\lambda$, a coalition that has learned $\theta$ may be able to lower actual independence covertly, by pressuring editors or steering grants, without the public revising $\hat\lambda$.
   525	
   526	\begin{proposition}[Covert capture]
   527	\label{prop:ideological-power:covert}
   528	Suppose the public's posterior after an endorsement is $\mu_1(\hat\lambda)$ for a fixed conjecture $\hat\lambda>0$, while actual independence is $\lambda$. Then for $\theta\in\{G,B\}$,
   529	\[
   530	\E[\mu\mid\theta]=\mu_1(\hat\lambda)-\lambda\,\Prob(s=0\mid\theta)\bigl(\mu_1(\hat\lambda)-\mu_0\bigr),
   531	\]
   532	which is strictly decreasing in $\lambda$ for both types. The gain from a unit reduction of $\lambda$ is $q(\mu_1(\hat\lambda)-\mu_0)$ when the rule is unsound and $(1-q)(\mu_1(\hat\lambda)-\mu_0)$ when it is sound, so it is larger by the factor $q/(1-q)>1$ for a coalition whose rule is unsound.
   533	\end{proposition}
   534	
   535	\begin{proof}
   536	Given $\theta$, a refusal occurs with probability $\lambda\Prob(s=0\mid\theta)$ and yields the posterior $\mu_0$; otherwise the authority endorses and the public's posterior is $\mu_1(\hat\lambda)$. Taking the expectation gives the formula. Since $\mu_1(\hat\lambda)\geq\pi>\mu_0$ by Proposition~\ref{prop:ideological-power:credibility}(b), and $\Prob(s=0\mid B)=q$ and $\Prob(s=0\mid G)=1-q$ are positive, the expression is strictly decreasing in $\lambda$ with the stated slopes.
   537	\end{proof}
   538	
   539	Covert capture always raises expected confidence in the short run, because the public cannot discount what it does not see. Its value is greater for coalitions whose rules are unsound, since independent authorities would refuse them more often. If covert capture has a cost, coalitions with unsound rules will therefore pay it more often, and restrictions on independent authorities should follow adverse findings. Hypothesis HI7 in Section~\ref{sec:measurement} tests that prediction. If instead the coalition chose $\lambda$ openly after learning $\theta$, the choice would itself signal $\theta$ and the analysis would become a signaling game, which this paper does not solve. Commercialized but party-guided media in China \citep{stockmann2013} and the simulated democratic forms of informational autocracies \citep{guriev2019} fit the covert pattern: control is exercised while the appearance of independence is maintained.
   540	
   541	The covert case points to the main channel of deception. After an endorsement the public's posterior is $\mu_1(\hat\lambda)$, while the true probability that the rule is sound given an endorsement is $\mu_1(\lambda)$.
   542	
   543	\begin{corollary}[Deception gap]
   544	\label{cor:ideological-power:gap}
   545	The public overestimates the soundness of an endorsed rule, $\mu_1(\hat\lambda)>\mu_1(\lambda)$, if and only if $\hat\lambda>\lambda$. The gap $\mu_1(\hat\lambda)-\mu_1(\lambda)$ is strictly increasing in $\hat\lambda$ and strictly decreasing in $\lambda$.
   546	\end{corollary}
   547	
   548	\begin{proof}
   549	Immediate from the strict monotonicity of $\mu_1$ in Proposition~\ref{prop:ideological-power:credibility}(b).
   550	\end{proof}
   551	
   552	Capture misleads exactly when audiences overestimate independence. Disclosure rules, conflict-of-interest registries and the publication of appointment and funding records exist to bring $\hat\lambda$ into line with $\lambda$. They do not make authorities independent; they make their dependence visible, which removes the gap.
   553	
   554	\subsection{Correlated control and the discovery of error}
   555	
   556	Most polities have many legitimating authorities. Whether they detect and disclose an error depends on how many of them are independent, and on whether their independence is correlated. Integration across pillars, in the source's sense, typically works by correlation: when one coalition appoints the editors, the rectors and the chief jurists, they are captured together or not at all.
   557	
   558	\begin{proposition}[Disclosure under correlated control]
   559	\label{prop:ideological-power:disclosure}
   560	Let $K\geq2$ authorities each be independent with probability $\lambda\in(0,1)$, with an arbitrary joint distribution of independence across authorities, and let $N$ be the number of independent authorities. Given the set of independent authorities, each independently discovers and discloses a given error with probability $p\in(0,1)$; captured authorities never disclose. Let $D=\Prob(\text{at least one disclosure})$.
   561	\begin{enumerate}
   562	\item[(a)] For every joint distribution, $\lambda\bigl(1-(1-p)^K\bigr)\leq D\leq 1-(1-p)^{\lambda K}$.
   563	\item[(b)] The lower bound is attained if and only if independence is all or nothing, $N\in\{0,K\}$ almost surely, which is the case of perfectly correlated control.
   564	\item[(c)] If independence is drawn independently across authorities, $D=1-(1-\lambda p)^K$, which lies strictly above the lower bound.
   565	\end{enumerate}
   566	\end{proposition}
   567	
   568	\begin{proof}
   569	Conditional on $N$, no disclosure occurs with probability $(1-p)^N$, so $D=1-\E[g(N)]$ with $g(x)=(1-p)^x$, a strictly convex function. By linearity of expectation $\E[N]=\lambda K$.
   570	
   571	(a) For the upper bound, Jensen's inequality gives $\E[g(N)]\geq g(\E N)=(1-p)^{\lambda K}$. For the lower bound, strict convexity places $g$ below its chord on $[0,K]$: $g(x)\leq(1-x/K)g(0)+(x/K)g(K)$, with equality only at $x\in\{0,K\}$. Taking expectations, $\E[g(N)]\leq(1-\lambda)+\lambda(1-p)^K$, so $D\geq\lambda(1-(1-p)^K)$.
   572	
   573	(b) The chord inequality is strict for $x\in(0,K)$, so equality in expectation requires $\Prob(N\in\{0,K\})=1$. Conversely, if $N\in\{0,K\}$ almost surely then $\Prob(N=K)=\lambda$ and $D=\lambda(1-(1-p)^K)$.
   574	
   575	(c) If independence is independent across authorities, $N$ is binomial with parameters $K$ and $\lambda$, and $\E[(1-p)^N]=(1-\lambda+\lambda(1-p))^K=(1-\lambda p)^K$. Since $K\geq2$ and $\lambda\in(0,1)$, $\Prob(0<N<K)>0$, so by (b) the bound is strict.
   576	\end{proof}
   577	
   578	\begin{corollary}[Integration lowers discovery]
   579	\label{cor:ideological-power:integration}
   580	Holding fixed the number of authorities and the average probability that each is independent, a change in appointment structure that makes the independence of authorities perfectly correlated lowers the probability that an error is disclosed from $1-(1-\lambda p)^K$ to $\lambda(1-(1-p)^K)$.
   581	\end{corollary}
   582	
   583	The corollary separates two things that are often merged. Concentration $H^{\pI}$ concerns how many authorities there are and how control is shared among them. Integration concerns whether control over them moves together, which is what high $C_{\pP\pI}$ or $C_{\pF\pI}$ produces when one coalition appoints or funds all of them. A polity can have many universities, newspapers and juristic schools, and so low measured concentration, and still have low discovery if one coalition appoints their heads. The upper bound in (a) is attained only when $\lambda K$ is an integer and $N=\lambda K$ almost surely; otherwise the maximum is reached by a distribution on $\lfloor\lambda K\rfloor$ and $\lceil\lambda K\rceil$. The bound adds a design point: discovery is highest when the number of independent authorities is least variable, which plural appointment by rival bodies secures better than independent chance. This refines source hypothesis H4 on epistemic checks and source Proposition 2 on the interruption of transmission \citep{largo2026hbs}.
   584	
   585	\subsection{Fragility of displayed legitimacy}
   586	
   587	Ideological control often aims at public displays: attendance, applause, signatures, votes in uncontested elections. The beliefs those displays reveal are a separate matter. A threshold model, of the kind \citet{granovetter1978} introduced for collective behavior and \citet{kuran1991} applied to preference falsification, shows how far the two can diverge.
   588	
   589	\begin{proposition}[Fragility]
   590	\label{prop:ideological-power:fragility}
   591	Let $n$ members have thresholds $\tau_i\in[0,1]$: member $i$ expresses dissent publicly when the share of members already doing so is at least $\tau_i$. Let $\Phi(x)=\frac1n\#\{i:\tau_i\leq x\}$ and $x_0=0$, $x_{k+1}=\Phi(x_k)$.
   592	\begin{enumerate}
   593	\item[(a)] The sequence $(x_k)$ is nondecreasing and reaches, within $n+1$ steps, the smallest fixed point $x^\ast$ of $\Phi$.
   594	\item[(b)] There are threshold profiles $\tau$ and $\tau'$ that differ only in one member's threshold, by $1/n$, with $x^\ast(\tau)=1$ and $x^\ast(\tau')=0$.
   595	\end{enumerate}
   596	\end{proposition}
   597	
   598	\begin{proof}
   599	(a) $\Phi$ is nondecreasing. Since $x_1=\Phi(0)\geq0=x_0$, induction gives $x_{k+1}=\Phi(x_k)\geq\Phi(x_{k-1})=x_k$. The sequence takes values in $\{0,1/n,\dots,1\}$, so it is constant from some step $k\leq n$ on, at a fixed point $\bar x$. If $y$ is any fixed point, then $x_0\leq y$, and $x_k\leq y$ implies $x_{k+1}=\Phi(x_k)\leq\Phi(y)=y$, so $\bar x\leq y$.
   600	
   601	(b) Let $\tau_i=(i-1)/n$ for $i=1,\dots,n$. Then $\Phi(k/n)=(k+1)/n$ for $k<n$, so $x_k=k/n$ and $x^\ast=1$. Let $\tau'$ agree with $\tau$ except $\tau'_1=1/n$. No member has threshold $0$, so $\Phi'(0)=0$ and $x^\ast(\tau')=0$.
   602	\end{proof}
   603	
   604	Two populations whose private dispositions are almost identical can display opposite public states. Displayed support is therefore not a sufficient statistic for private belief, and the gap is largest where expression is costly, which is where $Q^{\pI}$ is low. The result explains why regimes that control the ideological layer can appear stable and then collapse quickly, as \citet{kuran1991} argued for 1989. It also constrains measurement: in polities with low contestability, attendance, applause and uncontested votes cannot validate claims about normative legitimacy.
   605	
   606	\subsection{Coupling of belief to coercion and production}
   607	
   608	The series assigns two of the fifteen cross-pillar pairs to this Part for primary treatment.
   609	
   610	The coupling $C_{\pI\pC}$ runs in both directions. Control of belief needs enforcement when it goes beyond persuasion: heresy and blasphemy prosecutions, censorship offices, the licensing of presses and the dismissal of dissenting teachers all require a sanctioning apparatus. The Spanish Inquisition joined doctrinal judgment to coercive power \citep{kamen1997}, and the censorship offices of party-states worked with the security services. Coercion in turn needs belief. Soldiers and police carry out orders when they expect others to do so, and Proposition~\ref{prop:ideological-power:fragility} shows how quickly that expectation can fail. \citet{greitens2016} and the other sources of Part V analyze the coercive institutions themselves, and Part V shows that the refusal of manifestly unlawful orders, one of its checks on coercion, depends on the legitimating beliefs studied here. For the ideological layer, $C_{\pI\pC}$ is the extent to which one coalition both decides what may be said and commands the organizations that punish saying otherwise. It is high where religious courts or security services enforce doctrine and low where independent courts protect expression.
   611	
   612	The coupling $C_{\pI\pW}$ concerns the beliefs of the producing population and the institutions that shape them. Belief-producing specialists need a surplus to live on, a dependency of the ideological on the productive pillar that Part VII derives in general. In the other direction, beliefs shape work and compliance. \citet{levi1988} showed that taxpayers' compliance is quasi-voluntary: it depends on their belief that others comply and that rulers keep their bargains. \citet{becker2009} found that Protestant regions of Prussia had higher literacy, which they attributed to the religious emphasis on reading scripture, and that literacy rather than a work ethic accounts for much of their economic advantage. \citet{gellner1983} argued that industrial economies require a standardized literate culture that only a mass education system can supply, which makes control of schooling central to modern states. \citet{bourdieu1977} argued that schooling also reproduces class position under the appearance of merit. The coupling is high where one coalition controls both the conditions of work and the institutions that teach workers what to expect of it, and low where producers have authorities of their own, such as the labor press and educational associations of social democracies. Part VI treats everyday resistance \citep{scott1985}, which shows that producers do not simply absorb dominant beliefs, and its latent-veto result, that producers can threaten a system's persistence by withdrawing the production it needs (Proposition 3.5 of Part VI), explains why rulers need producers to believe that compliance is expected of everyone.
   613	
   614	\subsection{Checks}
   615	
   616	Each component of $Q^{\pI}$ maps onto a parameter of the models above. Independence raises $\lambda$ and, through the institutional floor $\lambda_{\min}$, protects the public when the coalition's interests are not aligned with soundness (Proposition~\ref{prop:ideological-power:tradeoff}) and when it would capture authorities covertly (Proposition~\ref{prop:ideological-power:covert}). Disclosure aligns the public's estimate $\hat\lambda$ with the truth and closes the deception gap (Corollary~\ref{cor:ideological-power:gap}). Plurality with separate appointment raises the number of authorities and lowers the correlation of their capture (Proposition~\ref{prop:ideological-power:disclosure}). Reviewability raises the discovery probability $p$. Exit lets audiences abandon authorities that lose credibility, which gives authorities a reputational reason to remain independent, the mechanism behind both the demand-side account of \citet{gentzkow2006} and the regulator reputation of \citet{carpenter2010}.
   617	
   618	The historical record shows each check operating. Scholars refused the Abbasid caliph's doctrinal demand \citep{crone1986}. Endowments gave madrasas a revenue base of their own \citep{makdisi1981}. The transnational Church limited the claims of crowns \citep{grzymala2023}, and Jansenist and Gallican counter-publics eroded royal sacrality \citep{vankley1996}. Competition among outlets raises the cost of media capture \citep{besley2006}, and meta-research exposed sponsorship bias in clinical research \citep{lundh2017}. These are the forms that source Proposition 2, that checks can interrupt the transmission of concentrated power, takes in the ideological layer \citep{largo2026hbs}.
   619	
   620	\section{Measurement}

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '733,900p' papers/latex/ideological-power.tex | nl -ba -v733" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   733	\begin{thebibliography}{200}
   734	\small
   735	\raggedright
   736	
   737	\bibitem[Abbott(1988)]{abbott1988}
   738	Abbott, Andrew (1988). \emph{The System of Professions: An Essay on the Division of Expert Labor}. University of Chicago Press. doi:10.7208/chicago/9780226189666.001.0001.
   739	
   740	\bibitem[Al-Rasheed(2002)]{alrasheed2002}
   741	Al-Rasheed, Madawi (2002). \emph{A History of Saudi Arabia}. Cambridge University Press. doi:10.1017/cbo9780511993510.
   742	
   743	\bibitem[Allcott and Gentzkow(2017)]{allcott2017}
   744	Allcott, Hunt and Matthew Gentzkow (2017). Social Media and Fake News in the 2016 Election. \emph{Journal of Economic Perspectives} 31(2):211-236. doi:10.1257/jep.31.2.211.
   745	
   746	\bibitem[Althusser(1971)]{althusser1971}
   747	Althusser, Louis (1971). Ideology and Ideological State Apparatuses (Notes towards an Investigation). In \emph{Lenin and Philosophy and Other Essays}. Monthly Review Press.
   748	
   749	\bibitem[Arjomand(1988)]{arjomand1988}
   750	Arjomand, Said Amir (1988). \emph{The Turban for the Crown: The Islamic Revolution in Iran}. Oxford University Press.
   751	
   752	\bibitem[Aumann(1976)]{aumann1976}
   753	Aumann, Robert J. (1976). Agreeing to Disagree. \emph{The Annals of Statistics} 4(6):1236-1239. doi:10.1214/aos/1176343654.
   754	
   755	\bibitem[Bachrach and Baratz(1962)]{bachrach1962}
   756	Bachrach, Peter and Morton S. Baratz (1962). Two Faces of Power. \emph{American Political Science Review} 56(4):947-952. doi:10.2307/1952796.
   757	
   758	\bibitem[Barkey(2008)]{barkey2008}
   759	Barkey, Karen (2008). \emph{Empire of Difference: The Ottomans in Comparative Perspective}. Cambridge University Press. doi:10.1017/cbo9780511790645.
   760	
   761	\bibitem[Bauckham(1993)]{bauckham1993}
   762	Bauckham, Richard (1993). \emph{The Theology of the Book of Revelation}. Cambridge University Press. doi:10.1017/cbo9780511819858.
   763	
   764	\bibitem[Beale(1999)]{beale1999}
   765	Beale, G. K. (1999). \emph{The Book of Revelation: A Commentary on the Greek Text}. Eerdmans (NIGTC).
   766	
   767	\bibitem[Becker and Woessmann(2009)]{becker2009}
   768	Becker, Sascha O. and Ludger Woessmann (2009). Was Weber Wrong? A Human Capital Theory of Protestant Economic History. \emph{The Quarterly Journal of Economics} 124(2):531-596. doi:10.1162/qjec.2009.124.2.531.
   769	
   770	\bibitem[Bekelman et~al.(2003)]{bekelman2003}
   771	Bekelman, Justin E., Yan Li and Cary P. Gross (2003). Scope and Impact of Financial Conflicts of Interest in Biomedical Research: A Systematic Review. \emph{JAMA} 289(4):454-465. doi:10.1001/jama.289.4.454.
   772	
   773	\bibitem[Berkey(1992)]{berkey1992}
   774	Berkey, Jonathan (1992). \emph{The Transmission of Knowledge in Medieval Cairo: A Social History of Islamic Education}. Princeton University Press. doi:10.1515/9781400862580.
   775	
   776	\bibitem[Berman(2006)]{berman2006}
   777	Berman, Sheri (2006). \emph{The Primacy of Politics: Social Democracy and the Making of Europe's Twentieth Century}. Cambridge University Press. doi:10.1017/cbo9780511791109.
   778	
   779	\bibitem[Besley and Prat(2006)]{besley2006}
   780	Besley, Timothy and Andrea Prat (2006). Handcuffs for the Grabbing Hand? Media Capture and Government Accountability. \emph{American Economic Review} 96(3):720-736. doi:10.1257/aer.96.3.720.
   781	
   782	\bibitem[Boehm(1999)]{boehm1999}
   783	Boehm, Christopher (1999). \emph{Hierarchy in the Forest: The Evolution of Egalitarian Behavior}. Harvard University Press. doi:10.2307/j.ctvjf9xr4.
   784	
   785	\bibitem[Boehm(2012)]{boehm2012}
   786	Boehm, Christopher (2012). \emph{Moral Origins: The Evolution of Virtue, Altruism, and Shame}. Basic Books.
   787	
   788	\bibitem[Bossuet(1990)]{bossuet1990}
   789	Bossuet, Jacques-B\'enigne (1990). \emph{Politics Drawn from the Very Words of Holy Scripture} (1709), ed. Riley. Cambridge University Press.
   790	
   791	\bibitem[Bourdieu(1989)]{bourdieu1989}
   792	Bourdieu, Pierre (1989). Social Space and Symbolic Power. \emph{Sociological Theory} 7(1):14-25. doi:10.2307/202060.
   793	
   794	\bibitem[Bourdieu(1991)]{bourdieu1991}
   795	Bourdieu, Pierre (1991). \emph{Language and Symbolic Power}. Harvard University Press.
   796	
   797	\bibitem[Bourdieu and Passeron(1977)]{bourdieu1977}
   798	Bourdieu, Pierre and Jean-Claude Passeron (1977). \emph{Reproduction in Education, Society and Culture}. Sage.
   799	
   800	\bibitem[Boyer(1992)]{boyer1992}
   801	Boyer, Paul (1992). \emph{When Time Shall Be No More: Prophecy Belief in Modern American Culture}. Harvard University Press (Belknap). doi:10.2307/jj.41480279.
   802	
   803	\bibitem[Brooks(2000)]{brooks2000}
   804	Brooks, Jeffrey (2000). \emph{Thank You, Comrade Stalin! Soviet Public Culture from Revolution to Cold War}. Princeton University Press.
   805	
   806	\bibitem[Burke(1992)]{burke1992}
   807	Burke, Peter (1992). \emph{The Fabrication of Louis XIV}. Yale University Press.
   808	
   809	\bibitem[Carpenter(2010)]{carpenter2010}
   810	Carpenter, Daniel P. (2010). \emph{Reputation and Power: Organizational Image and Pharmaceutical Regulation at the FDA}. Princeton University Press. doi:10.1515/9781400835119.
   811	
   812	\bibitem[Casanova(1994)]{casanova1994}
   813	Casanova, Jos\'e (1994). \emph{Public Religions in the Modern World}. University of Chicago Press. doi:10.7208/chicago/9780226190204.001.0001.
   814	
   815	\bibitem[Chwe(2001)]{chwe2001}
   816	Chwe, Michael Suk-Young (2001). \emph{Rational Ritual: Culture, Coordination, and Common Knowledge}. Princeton University Press. doi:10.23943/princeton/9780691158280.001.0001.
   817	
   818	\bibitem[Clastres(1987)]{clastres1987}
   819	Clastres, Pierre (1987). \emph{Society against the State: Essays in Political Anthropology} (1974), trans. Robert Hurley. Zone Books. doi:10.2307/j.ctv1595m3p.
   820	
   821	\bibitem[Collins(1984)]{collins1984}
   822	Collins, Adela Yarbro (1984). \emph{Crisis and Catharsis: The Power of the Apocalypse}. Westminster Press.
   823	
   824	\bibitem[Commins(2006)]{commins2006}
   825	Commins, David (2006). \emph{The Wahhabi Mission and Saudi Arabia}. I. B. Tauris. doi:10.5040/9780755609444.
   826	
   827	\bibitem[Coppedge et~al.(2011)]{coppedge2011}
   828	Coppedge, Michael, John Gerring, David Altman, et al. (2011). Conceptualizing and Measuring Democracy: A New Approach. \emph{Perspectives on Politics} 9(2):247-267. doi:10.1017/S1537592711000880.
   829	
   830	\bibitem[Crone(2004)]{crone2004}
   831	Crone, Patricia (2004). \emph{God's Rule: Government and Islam: Six Centuries of Medieval Islamic Political Thought}. Columbia University Press.
   832	
   833	\bibitem[Crone and Hinds(1986)]{crone1986}
   834	Crone, Patricia and Martin Hinds (1986). \emph{God's Caliph: Religious Authority in the First Centuries of Islam}. Cambridge University Press.
   835	
   836	\bibitem[DellaVigna and Kaplan(2007)]{dellavigna2007}
   837	DellaVigna, Stefano and Ethan Kaplan (2007). The Fox News Effect: Media Bias and Voting. \emph{The Quarterly Journal of Economics} 122(3):1187-1234. doi:10.1162/qjec.122.3.1187.
   838	
   839	\bibitem[Djankov et~al.(2003)]{djankov2003}
   840	Djankov, Simeon, Caralee McLiesh, Tatiana Nenova and Andrei Shleifer (2003). Who Owns the Media? \emph{The Journal of Law and Economics} 46(2):341-382. doi:10.1086/377116.
   841	
   842	\bibitem[Eickelman(1992)]{eickelman1992}
   843	Eickelman, Dale F. (1992). Mass Higher Education and the Religious Imagination in Contemporary Arab Societies. \emph{American Ethnologist} 19(4):643-655. doi:10.1525/ae.1992.19.4.02a00010.
   844	
   845	\bibitem[Eickelman and Piscatori(1996)]{eickelman1996}
   846	Eickelman, Dale F. and James Piscatori (1996). \emph{Muslim Politics}. Princeton University Press. doi:10.1515/9780691187785.
   847	
   848	\bibitem[Eisenstein(1979)]{eisenstein1979}
   849	Eisenstein, Elizabeth L. (1979). \emph{The Printing Press as an Agent of Change}. Cambridge University Press. doi:10.1017/cbo9781107049963.
   850	
   851	\bibitem[Ellul(1977)]{ellul1977}
   852	Ellul, Jacques (1977). \emph{Apocalypse: The Book of Revelation}. Seabury Press.
   853	
   854	\bibitem[Elster(1983)]{elster1983}
   855	Elster, Jon (1983). \emph{Explaining Technical Change: A Case Study in the Philosophy of Science}. Cambridge University Press.
   856	
   857	\bibitem[Emmerson and McGinn(1992)]{emmerson1992}
   858	Emmerson, Richard K. and Bernard McGinn (eds.) (1992). \emph{The Apocalypse in the Middle Ages}. Cornell University Press.
   859	
   860	\bibitem[Enikolopov et~al.(2011)]{enikolopov2011}
   861	Enikolopov, Ruben, Maria Petrova and Ekaterina Zhuravskaya (2011). Media and Political Persuasion: Evidence from Russia. \emph{American Economic Review} 101(7):3253-3285. doi:10.1257/aer.101.7.3253.
   862	
   863	\bibitem[Esping-Andersen(1990)]{esping1990}
   864	Esping-Andersen, G\"osta (1990). \emph{The Three Worlds of Welfare Capitalism}. Princeton University Press.
   865	
   866	\bibitem[Evans-Pritchard(1940)]{evanspritchard1940}
   867	Evans-Pritchard, E. E. (1940). \emph{The Nuer: A Description of the Modes of Livelihood and Political Institutions of a Nilotic People}. Clarendon Press.
   868	
   869	\bibitem[Fox(2008)]{fox2008}
   870	Fox, Jonathan (2008). \emph{A World Survey of Religion and the State}. Cambridge University Press. doi:10.1017/cbo9780511993039.
   871	
   872	\bibitem[Fragnito(2001)]{fragnito2001}
   873	Fragnito, Gigliola (2001). \emph{Church, Censorship and Culture in Early Modern Italy}. Cambridge University Press.
   874	
   875	\bibitem[Fraser(1990)]{fraser1990}
   876	Fraser, Nancy (1990). Rethinking the Public Sphere: A Contribution to the Critique of Actually Existing Democracy. \emph{Social Text} 25/26:56-80. doi:10.2307/466240.
   877	
   878	\bibitem[Freidson(1970)]{freidson1970}
   879	Freidson, Eliot (1970). \emph{Profession of Medicine: A Study of the Sociology of Applied Knowledge}. Dodd, Mead.
   880	
   881	\bibitem[Friesen(2001)]{friesen2001}
   882	Friesen, Steven J. (2001). \emph{Imperial Cults and the Apocalypse of John: Reading Revelation in the Ruins}. Oxford University Press. doi:10.1093/0195131533.001.0001.
   883	
   884	\bibitem[Fuller(1995)]{fuller1995}
   885	Fuller, Robert C. (1995). \emph{Naming the Antichrist: The History of an American Obsession}. Oxford University Press. doi:10.1093/acprof:oso/9780195109795.001.0001.
   886	
   887	\bibitem[Gellner(1981)]{gellner1981}
   888	Gellner, Ernest (1981). \emph{Muslim Society}. Cambridge University Press.
   889	
   890	\bibitem[Gellner(1983)]{gellner1983}
   891	Gellner, Ernest (1983). \emph{Nations and Nationalism}. Cornell University Press.
   892	
   893	\bibitem[Gentzkow and Shapiro(2006)]{gentzkow2006}
   894	Gentzkow, Matthew and Jesse M. Shapiro (2006). Media Bias and Reputation. \emph{Journal of Political Economy} 114(2):280-316. doi:10.1086/499414.
   895	
   896	\bibitem[Gerschewski(2013)]{gerschewski2013}
   897	Gerschewski, Johannes (2013). The Three Pillars of Stability: Legitimation, Repression, and Co-optation in Autocratic Regimes. \emph{Democratization} 20(1):13-38. doi:10.1080/13510347.2013.738860.
   898	
   899	\bibitem[Gillespie(2019)]{gillespie2019}
   900	Gillespie, Tarleton (2019). \emph{Custodians of the Internet: Platforms, Content Moderation, and the Hidden Decisions That Shape Social Media}. Yale University Press. doi:10.12987/9780300235029.

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '901,1070p' papers/latex/ideological-power.tex | nl -ba -v901" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   901	
   902	\bibitem[Graeber and Wengrow(2021)]{graeber2021}
   903	Graeber, David and David Wengrow (2021). \emph{The Dawn of Everything: A New History of Humanity}. Farrar, Straus and Giroux.
   904	
   905	\bibitem[Gramsci(1971)]{gramsci1971}
   906	Gramsci, Antonio (1971). \emph{Selections from the Prison Notebooks}, ed. and trans. Hoare and Nowell Smith. International Publishers.
   907	
   908	\bibitem[Granovetter(1978)]{granovetter1978}
   909	Granovetter, Mark (1978). Threshold Models of Collective Behavior. \emph{American Journal of Sociology} 83:1420-1443. doi:10.1086/226707.
   910	
   911	\bibitem[Greitens(2016)]{greitens2016}
   912	Greitens, Sheena Chestnut (2016). \emph{Dictators and Their Secret Police: Coercive Institutions and State Violence}. Cambridge University Press. doi:10.1017/cbo9781316489031.
   913	
   914	\bibitem[Grzymala-Busse(2015)]{grzymala2015}
   915	Grzymala-Busse, Anna (2015). \emph{Nations under God: How Churches Use Moral Authority to Influence Policy}. Princeton University Press. doi:10.1515/9781400866458.
   916	
   917	\bibitem[Grzymala-Busse(2023)]{grzymala2023}
   918	Grzymala-Busse, Anna (2023). \emph{Sacred Foundations: The Religious and Medieval Roots of the European State}. Princeton University Press. doi:10.1515/9780691245133.
   919	
   920	\bibitem[Guess et~al.(2023)]{guess2023}
   921	Guess, Andrew M., Neil Malhotra, Jennifer Pan, et al. (2023). How Do Social Media Feed Algorithms Affect Attitudes and Behavior in an Election Campaign? \emph{Science} 381(6656):398-404. doi:10.1126/science.abp9364.
   922	
   923	\bibitem[Guriev and Treisman(2019)]{guriev2019}
   924	Guriev, Sergei and Daniel Treisman (2019). Informational Autocrats. \emph{Journal of Economic Perspectives} 33(4):100-127. doi:10.1257/jep.33.4.100.
   925	
   926	\bibitem[Guriev and Treisman(2022)]{guriev2022}
   927	Guriev, Sergei and Daniel Treisman (2022). \emph{Spin Dictators: The Changing Face of Tyranny in the 21st Century}. Princeton University Press. doi:10.1515/9780691224466.
   928	
   929	\bibitem[Habermas(1989)]{habermas1989}
   930	Habermas, J\"urgen (1989). \emph{The Structural Transformation of the Public Sphere} (1962), trans. Burger and Lawrence. MIT Press.
   931	
   932	\bibitem[Hallin and Mancini(2004)]{hallin2004}
   933	Hallin, Daniel C. and Paolo Mancini (2004). \emph{Comparing Media Systems: Three Models of Media and Politics}. Cambridge University Press. doi:10.1017/CBO9780511790867.
   934	
   935	\bibitem[Hart(1961)]{hart1961}
   936	Hart, H. L. A. (1961). \emph{The Concept of Law}. Clarendon Press (3rd ed. 2012, Oxford University Press). doi:10.1093/he/9780199644704.001.0001.
   937	
   938	\bibitem[Hayek(1973)]{hayek1973}
   939	Hayek, Friedrich A. (1973). \emph{Law, Legislation and Liberty, Volume 1: Rules and Order}. University of Chicago Press. doi:10.7208/chicago/9780226321233.001.0001.
   940	
   941	\bibitem[Hempel(1959)]{hempel1959}
   942	Hempel, Carl G. (1959). The Logic of Functional Analysis. In Llewellyn Gross (ed.), \emph{Symposium on Sociological Theory}. Harper \& Row.
   943	
   944	\bibitem[Henningsen and Tedeschi(1986)]{henningsen1986}
   945	Henningsen, Gustav and John Tedeschi (eds.) (1986). \emph{The Inquisition in Early Modern Europe: Studies on Sources and Methods}. Northern Illinois University Press.
   946	
   947	\bibitem[Herman and Chomsky(1988)]{herman1988}
   948	Herman, Edward S. and Noam Chomsky (1988). \emph{Manufacturing Consent: The Political Economy of the Mass Media}. Pantheon Books.
   949	
   950	\bibitem[Hsia(1998)]{hsia1998}
   951	Hsia, R. Po-chia (1998). \emph{The World of Catholic Renewal 1540-1770}. Cambridge University Press.
   952	
   953	\bibitem[Imber(1997)]{imber1997}
   954	Imber, Colin (1997). \emph{Ebu's-su'ud: The Islamic Legal Tradition}. Stanford University Press.
   955	
   956	\bibitem[Kamen(1997)]{kamen1997}
   957	Kamen, Henry (1997). \emph{The Spanish Inquisition: A Historical Revision}. Yale University Press.
   958	
   959	\bibitem[Kantorowicz(1957)]{kantorowicz1957}
   960	Kantorowicz, Ernst H. (1957). \emph{The King's Two Bodies: A Study in Mediaeval Political Theology}. Princeton University Press. doi:10.1515/9781400880782.
   961	
   962	\bibitem[Kelly(1995)]{kelly1995}
   963	Kelly, Robert L. (1995). \emph{The Foraging Spectrum: Diversity in Hunter-Gatherer Lifeways}. Smithsonian Institution Press. doi:10.2307/j.ctv2sx9gc9.
   964	
   965	\bibitem[Kenez(1985)]{kenez1985}
   966	Kenez, Peter (1985). \emph{The Birth of the Propaganda State: Soviet Methods of Mass Mobilization, 1917-1929}. Cambridge University Press. doi:10.1017/cbo9780511572623.
   967	
   968	\bibitem[Khomeini(1981)]{khomeini1981}
   969	Khomeini, Ruhollah (1981). \emph{Islam and Revolution: Writings and Declarations of Imam Khomeini}, including \emph{Islamic Government} (1970), trans. Hamid Algar. Mizan Press.
   970	
   971	\bibitem[King et~al.(2013)]{king2013}
   972	King, Gary, Jennifer Pan and Margaret E. Roberts (2013). How Censorship in China Allows Government Criticism but Silences Collective Expression. \emph{American Political Science Review} 107(2):326-343. doi:10.1017/S0003055413000014.
   973	
   974	\bibitem[Koester(2014)]{koester2014}
   975	Koester, Craig R. (2014). \emph{Revelation: A New Translation with Introduction and Commentary}. Yale University Press (Anchor Yale Bible 38A). doi:10.12987/9780300211030.
   976	
   977	\bibitem[Kovacs and Rowland(2004)]{kovacs2004}
   978	Kovacs, Judith and Christopher Rowland (2004). \emph{Revelation: The Apocalypse of Jesus Christ}. Blackwell (Blackwell Bible Commentaries). doi:10.1002/9780470773512.
   979	
   980	\bibitem[Kraybill(1996)]{kraybill1996}
   981	Kraybill, J. Nelson (1996). \emph{Imperial Cult and Commerce in John's Apocalypse}. Sheffield Academic Press (JSNT Supplement 132).
   982	
   983	\bibitem[Kuran(1991)]{kuran1991}
   984	Kuran, Timur (1991). Now Out of Never: The Element of Surprise in the East European Revolution of 1989. \emph{World Politics} 44(1):7-48. doi:10.2307/2010422.
   985	
   986	\bibitem[Kuru(2009)]{kuru2009}
   987	Kuru, Ahmet T. (2009). \emph{Secularism and State Policies toward Religion: The United States, France, and Turkey}. Cambridge University Press. doi:10.1017/cbo9780511815096.
   988	
   989	\bibitem[Kuru(2019)]{kuru2019}
   990	Kuru, Ahmet T. (2019). \emph{Islam, Authoritarianism, and Underdevelopment: A Global and Historical Comparison}. Cambridge University Press. doi:10.1017/9781108296892.
   991	
   992	\bibitem[Lane and Ross(1995)]{lane1995}
   993	Lane, David and Cameron Ross (1995). The CPSU Ruling Elite 1981-1991: Commonalities and Divisions. \emph{Communist and Post-Communist Studies} 28(3):339-360. doi:10.1016/0967-067X(95)00020-U.
   994	
   995	\bibitem[Largo(2026)]{largo2026hbs}
   996	Largo, Mateo (2026). The Hierarchy of the Beast System: Institutional Power, Elite Coordination, and Economic Dependency Across Political Regimes. Unpublished working paper, 14 October 2026.
   997	
   998	\bibitem[Larson(1977)]{larson1977}
   999	Larson, Magali Sarfatti (1977). \emph{The Rise of Professionalism: A Sociological Analysis}. University of California Press. doi:10.1525/9780520323070.
  1000	
  1001	\bibitem[Lee(1979)]{lee1979}
  1002	Lee, Richard B. (1979). \emph{The !Kung San: Men, Women, and Work in a Foraging Society}. Cambridge University Press.
  1003	
  1004	\bibitem[Lee(2013)]{lee2013}
  1005	Lee, Richard B. (2013). \emph{The Dobe Ju/'hoansi}, 4th edition. Wadsworth/Cengage Learning.
  1006	
  1007	\bibitem[Levi(1988)]{levi1988}
  1008	Levi, Margaret (1988). \emph{Of Rule and Revenue}. University of California Press. doi:10.1525/9780520909540.
  1009	
  1010	\bibitem[Lewis(1969)]{lewis1969}
  1011	Lewis, David K. (1969). \emph{Convention: A Philosophical Study}. Harvard University Press.
  1012	
  1013	\bibitem[Lexchin et~al.(2003)]{lexchin2003}
  1014	Lexchin, Joel, Lisa A. Bero, Benjamin Djulbegovic and Otavio Clark (2003). Pharmaceutical Industry Sponsorship and Research Outcome and Quality: Systematic Review. \emph{BMJ} 326(7400):1167-1170. doi:10.1136/bmj.326.7400.1167.
  1015	
  1016	\bibitem[Lukes(2005)]{lukes2005}
  1017	Lukes, Steven (2005). \emph{Power: A Radical View}. Palgrave Macmillan. doi:10.1007/978-0-230-80257-5.
  1018	
  1019	\bibitem[Lundh et~al.(2017)]{lundh2017}
  1020	Lundh, Andreas, Joel Lexchin, Barbara Mintzes, Jeppe B. Schroll and Lisa Bero (2017). Industry Sponsorship and Research Outcome. \emph{Cochrane Database of Systematic Reviews}. doi:10.1002/14651858.MR000033.pub3.
  1021	
  1022	\bibitem[Makdisi(1981)]{makdisi1981}
  1023	Makdisi, George (1981). \emph{The Rise of Colleges: Institutions of Learning in Islam and the West}. Edinburgh University Press. doi:10.1515/9781474470643.
  1024	
  1025	\bibitem[Mann(1986)]{mann1986}
  1026	Mann, Michael (1986). \emph{The Sources of Social Power, Volume 1: A History of Power from the Beginning to A.D. 1760}. Cambridge University Press. doi:10.1017/CBO9780511570896.
  1027	
  1028	\bibitem[Mann(1993)]{mann1993}
  1029	Mann, Michael (1993). \emph{The Sources of Social Power, Volume 2: The Rise of Classes and Nation-States, 1760-1914}. Cambridge University Press. doi:10.1017/CBO9780511570902.
  1030	
  1031	\bibitem[Marshall(1976)]{marshall1976}
  1032	Marshall, Lorna (1976). \emph{The !Kung of Nyae Nyae}. Harvard University Press. doi:10.4159/harvard.9780674180574.
  1033	
  1034	\bibitem[McGinn(1998)]{mcginn1998}
  1035	McGinn, Bernard (1998). \emph{Antichrist: Two Thousand Years of the Human Fascination with Evil}. Columbia University Press.
  1036	
  1037	\bibitem[Menashri(1992)]{menashri1992}
  1038	Menashri, David (1992). \emph{Education and the Making of Modern Iran}. Cornell University Press.
  1039	
  1040	\bibitem[Merton(1968)]{merton1968}
  1041	Merton, Robert K. (1968). \emph{Social Theory and Social Structure}, enlarged edition. Free Press.
  1042	
  1043	\bibitem[Monderer and Samet(1989)]{monderer1989}
  1044	Monderer, Dov and Dov Samet (1989). Approximating Common Knowledge with Common Beliefs. \emph{Games and Economic Behavior} 1:170-190. doi:10.1016/0899-8256(89)90017-1.
  1045	
  1046	\bibitem[Oreskes(2019)]{oreskes2019}
  1047	Oreskes, Naomi (2019). \emph{Why Trust Science?} Princeton University Press. doi:10.1515/9780691222370.
  1048	
  1049	\bibitem[Oreskes and Conway(2010)]{oreskes2010}
  1050	Oreskes, Naomi and Erik M. Conway (2010). \emph{Merchants of Doubt}. Bloomsbury Press.
  1051	
  1052	\bibitem[Ostrom(1990)]{ostrom1990}
  1053	Ostrom, Elinor (1990). \emph{Governing the Commons: The Evolution of Institutions for Collective Action}. Cambridge University Press. doi:10.1017/CBO9780511807763.
  1054	
  1055	\bibitem[Philpott(2007)]{philpott2007}
  1056	Philpott, Daniel (2007). Explaining the Political Ambivalence of Religion. \emph{American Political Science Review} 101(3):505-525. doi:10.1017/s0003055407070372.
  1057	
  1058	\bibitem[Price(1984)]{price1984}
  1059	Price, S. R. F. (1984). \emph{Rituals and Power: The Roman Imperial Cult in Asia Minor}. Cambridge University Press.
  1060	
  1061	\bibitem[Roberts(2018)]{roberts2018}
  1062	Roberts, Margaret E. (2018). \emph{Censored: Distraction and Diversion Inside China's Great Firewall}. Princeton University Press. doi:10.2307/j.ctvc77b21.
  1063	
  1064	\bibitem[Rothstein(1996)]{rothstein1996}
  1065	Rothstein, Bo (1996). \emph{The Social Democratic State: The Swedish Model and the Bureaucratic Problem of Social Reforms}. University of Pittsburgh Press. doi:10.2307/jj.13110785.
  1066	
  1067	\bibitem[Rubin(2017)]{rubin2017}
  1068	Rubin, Jared (2017). \emph{Rulers, Religion, and Riches: Why the West Got Rich and the Middle East Did Not}. Cambridge University Press. doi:10.1017/9781139568272.
  1069	
  1070	\bibitem[Rubinstein(1992)]{rubinstein1992}

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '1071,1240p' papers/latex/ideological-power.tex | nl -ba -v1071" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
  1071	Rubinstein, Ariel (1992). The Electronic Mail Game: Strategic Behavior under ``Almost Common Knowledge''. In \emph{Knowledge, Belief, and Strategic Interaction}. Cambridge University Press. doi:10.1017/cbo9780511983474.019.
  1072	
  1073	\bibitem[Schelling(1960)]{schelling1960}
  1074	Schelling, Thomas C. (1960). \emph{The Strategy of Conflict}. Harvard University Press.
  1075	
  1076	\bibitem[Scott(1985)]{scott1985}
  1077	Scott, James C. (1985). \emph{Weapons of the Weak: Everyday Forms of Peasant Resistance}. Yale University Press. doi:10.12987/9780300153620.
  1078	
  1079	\bibitem[Slaughter and Rhoades(2004)]{slaughter2004}
  1080	Slaughter, Sheila and Gary Rhoades (2004). \emph{Academic Capitalism and the New Economy: Markets, State, and Higher Education}. Johns Hopkins University Press. doi:10.56021/9780801879494.
  1081	
  1082	\bibitem[Starr(1982)]{starr1982}
  1083	Starr, Paul (1982). \emph{The Social Transformation of American Medicine}. Basic Books.
  1084	
  1085	\bibitem[Stepan(2000)]{stepan2000}
  1086	Stepan, Alfred (2000). Religion, Democracy, and the Twin Tolerations. \emph{Journal of Democracy} 11(4):37-57. doi:10.1353/jod.2000.0088.
  1087	
  1088	\bibitem[Stockmann(2013)]{stockmann2013}
  1089	Stockmann, Daniela (2013). \emph{Media Commercialization and Authoritarian Rule in China}. Cambridge University Press. doi:10.1017/cbo9781139087742.
  1090	
  1091	\bibitem[Svolik(2012)]{svolik2012}
  1092	Svolik, Milan W. (2012). \emph{The Politics of Authoritarian Rule}. Cambridge University Press. doi:10.1017/CBO9781139176040.
  1093	
  1094	\bibitem[Van Kley(1996)]{vankley1996}
  1095	Van Kley, Dale K. (1996). \emph{The Religious Origins of the French Revolution: From Calvin to the Civil Constitution, 1560-1791}. Yale University Press.
  1096	
  1097	\bibitem[Weber(1978)]{weber1978}
  1098	Weber, Max (1978). \emph{Economy and Society: An Outline of Interpretive Sociology}. University of California Press. doi:10.4159/9780674240827.
  1099	
  1100	\bibitem[Wiessner(2005)]{wiessner2005}
  1101	Wiessner, Polly (2005). Norm Enforcement among the Ju/'hoansi Bushmen: A Case of Strong Reciprocity? \emph{Human Nature} 16(2):115-145. doi:10.1007/s12110-005-1000-9.
  1102	
  1103	\bibitem[Wink(1992)]{wink1992}
  1104	Wink, Walter (1992). \emph{Engaging the Powers: Discernment and Resistance in a World of Domination}. Fortress Press. doi:10.2307/j.ctt1tm7j16.
  1105	
  1106	\bibitem[Wintrobe(1998)]{wintrobe1998}
  1107	Wintrobe, Ronald (1998). \emph{The Political Economy of Dictatorship}. Cambridge University Press. doi:10.1017/cbo9781139174916.
  1108	
  1109	\bibitem[Woodburn(1982)]{woodburn1982}
  1110	Woodburn, James (1982). Egalitarian Societies. \emph{Man (N.S.)} 17(3):431-451. doi:10.2307/2801707.
  1111	
  1112	\bibitem[Zaman(2002)]{zaman2002}
  1113	Zaman, Muhammad Qasim (2002). \emph{The Ulama in Contemporary Islam: Custodians of Change}. Princeton University Press. doi:10.2307/j.ctt7rh2s.
  1114	
  1115	\end{thebibliography}
  1116	
  1117	\end{document}

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '350,369p' papers/latex/ideological-power.tex | nl -ba -v350" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   350	Every regime type implements the ideological function; they differ in which institutions hold it, how tightly one coalition controls their appointments and revenue, and which other pillars that coalition also commands. The comparison below codes these differences qualitatively from secondary sources. No numerical value of $H^{\pI}$, $Q^{\pI}$, $U_t$ or $\Int_t$ is reported for any polity, because no preregistered coding exists.
   351	
   352	The couplings of the ideological pillar to finance, rule-making and adjudication ($C_{\pF\pI}$, $C_{\pP\pI}$, $C_{\pJ\pI}$) are analyzed primarily in Parts I, II and III; this paper treats the couplings to coercion and production ($C_{\pI\pC}$, $C_{\pI\pW}$).
   353	
   354	\subsection{Market-capitalist societies}
   355	
   356	In market-capitalist societies the ideological function is held by many organizations with separate ownership and funding: privately owned media firms financed by advertising and subscriptions, public and private universities, foundations and think tanks, professional associations, scientific journals, regulatory agencies in their certifying role, and religious bodies organized as voluntary associations. Control over authoritative outputs is spread across these organizations, so $H^{\pI}$ is moderate overall, but it varies by sector. Ownership of the largest media firms is often concentrated in a few families \citep{djankov2003}, while accreditation of physicians or approval of drugs may rest with a single professional body or agency.
   357	
   358	The distinctive coupling is between the financial and ideological pillars. Advertising finances news, endowments and grants finance universities, and industry finances a large share of clinical research. \citet{herman1988} built their propaganda model on this coupling. \citet{slaughter2004} documented the movement of universities toward market revenue, and \citet{starr1982} described how medical authority was converted into economic power and later confronted corporate organization of care. Part I treats $C_{\pF\pI}$ as its pair and measures the conversion of financial control into favorable outputs of other pillars by a conversion elasticity (Definition 6.1 of Part I); here the question is what the coupling does to the independence parameter $\lambda$ of Definition~\ref{def:ideological-power:endorsement}.
   359	
   360	The documented capture episodes are sectoral. Systematic reviews associate industry sponsorship with conclusions favorable to sponsors \citep{bekelman2003,lexchin2003,lundh2017}. \citet{oreskes2010} documented organized efforts to manufacture doubt about tobacco harms and environmental hazards. Each case meets the three conditions of a capture link: privileged access through funding, weakened contestability through selective publication or orchestrated doubt, and material evidence linking the asymmetry to an output, whether a published conclusion or a delayed regulation.
   361	
   362	Platform firms now hold part of the function in this regime type. A few companies decide, through ranking and moderation, which statements by journalists, scientists and clergy reach large audiences \citep{gillespie2019}. In the terms of Section~\ref{sec:layer}, they hold a large share of control over reach, one of the outputs that defines $s^{\pI}$, so they raise measured concentration even when the number of speakers grows. The evidence on their persuasive effect is mixed: fabricated stories spread widely \citep{allcott2017}, but an experimental change of feed ranking during an election left attitudes unchanged \citep{guess2023}. Control over reach is established; its translation into belief is an open empirical question.
   363	
   364	The documented checks are also sectoral. Competition among outlets makes media capture costly \citep{besley2006}. Demand-side slant \citep{gentzkow2006} is a rival explanation for partisan coverage that does not require owner control, so evidence of slant is not by itself evidence of capture. Disclosure rules, peer review, replication and the reputational autonomy of regulators \citep{carpenter2010} raise $\lambda$. The capture episodes above were themselves discovered through litigation, journalism and meta-research, which is what source hypothesis H4 predicts: higher rates of documented error discovery can signal stronger accountability rather than more capture \citep{largo2026hbs}.
   365	
   366	\subsection{Communist party-states}
   367	
   368	In communist party-states the ruling party claims the ideological function as part of its leading role. Party propaganda departments, state newspapers and broadcasters, party schools, academies of sciences, writers' and artists' unions and a compulsory curriculum in Marxism-Leninism hold the function. \citet{kenez1985} described how the Bolsheviks built a propaganda state in their first decade, combining agitation, literacy campaigns and new media under party direction. \citet{brooks2000} showed how the Soviet press under Stalin organized public culture as a ritual in which achievements were presented as gifts from the leadership and citizens were expected to express gratitude.
   369	

codex
- None.

VERDICT: PASS
hook: Stop
hook: Stop
hook: Stop Completed
hook: Stop Completed
tokens used
69,706
- None.

VERDICT: PASS
