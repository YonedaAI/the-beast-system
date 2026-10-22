// Series metadata shared by the content scripts.
export const SERIES = [
  { slug: 'financial-power', part: 'Part I', roman: 'I', pillar: 'F', title: 'Financial Power and Resource Command', subtitle: '', question: 'Who controls the resources?', color: '#d9b25f' },
  { slug: 'political-power', part: 'Part II', roman: 'II', pillar: 'P', title: 'Political Power and Rule Making', subtitle: '', question: 'Who makes the laws?', color: '#e0556a' },
  { slug: 'judicial-power', part: 'Part III', roman: 'III', pillar: 'J', title: 'Judicial Power and Legal Interpretation', subtitle: '', question: 'Who interprets the laws?', color: '#6f8fe0' },
  { slug: 'ideological-power', part: 'Part IV', roman: 'IV', pillar: 'I', title: 'Ideological Power and Legitimation', subtitle: '', question: 'Who shapes the beliefs?', color: '#b072d8' },
  { slug: 'coercive-power', part: 'Part V', roman: 'V', pillar: 'C', title: 'Coercive Power and Enforcement', subtitle: '', question: 'Who enforces the rules?', color: '#e8793a' },
  { slug: 'productive-power', part: 'Part VI', roman: 'VI', pillar: 'W', title: 'Productive Power and Social Reproduction', subtitle: '', question: 'Who produces the wealth?', color: '#4fb286' },
  { slug: 'formalized-state', part: 'Part VII', roman: 'VII', pillar: '', title: 'The Formalized State', subtitle: 'The Hierarchy of the Beast System', question: 'What structure do all six functions share?', color: '#ece6dc' },
];
export const SLUGS = SERIES.map((s) => s.slug);
