// Six pillars as nodes with the dependency arcs of the Formalized State (Part VII):
// production feeds every other function; allocation feeds production; the other four feed allocation.
const NODES = [
  { id: 'F', label: 'Financial', x: 300, y: 250, color: '#d9b25f' },
  { id: 'W', label: 'Productive', x: 300, y: 450, color: '#4fb286' },
  { id: 'P', label: 'Political', x: 62, y: 210, color: '#e0556a' },
  { id: 'J', label: 'Judicial', x: 538, y: 210, color: '#6f8fe0' },
  { id: 'I', label: 'Ideological', x: 160, y: 62, color: '#b072d8' },
  { id: 'C', label: 'Coercive', x: 440, y: 62, color: '#e8793a' },
];

const R = 30;
const pos = Object.fromEntries(NODES.map((n) => [n.id, n]));

function arc(a: string, b: string, bend: number) {
  const A = pos[a];
  const B = pos[b];
  const dx = B.x - A.x;
  const dy = B.y - A.y;
  const d = Math.hypot(dx, dy);
  const ux = dx / d;
  const uy = dy / d;
  const sx = A.x + ux * (R + 2);
  const sy = A.y + uy * (R + 2);
  const ex = B.x - ux * (R + 8);
  const ey = B.y - uy * (R + 8);
  const mx = (sx + ex) / 2 - uy * bend;
  const my = (sy + ey) / 2 + ux * bend;
  return `M${sx.toFixed(1)} ${sy.toFixed(1)} Q${mx.toFixed(1)} ${my.toFixed(1)} ${ex.toFixed(1)} ${ey.toFixed(1)}`;
}

const FROM_W = [
  ['W', 'P', -55],
  ['W', 'J', 55],
  ['W', 'I', -95],
  ['W', 'C', 95],
] as const;
const INTO_F = [
  ['P', 'F', 0],
  ['J', 'F', 0],
  ['I', 'F', 0],
  ['C', 'F', 0],
] as const;

export default function PillarDiagram() {
  return (
    <div className="diagram">
      <svg
        viewBox="0 0 600 510"
        role="img"
        aria-label="Diagram of the six pillars of governance as six nodes: financial, political, judicial, ideological, coercive and productive. Productive power feeds each of the other five. Financial power feeds productive power, and the political, judicial, ideological and coercive pillars each feed financial power."
      >
        <defs>
          <marker id="arrow-solid" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
            <path d="M0 0L10 5L0 10z" fill="#ec5a72" />
          </marker>
          <marker id="arrow-soft" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M0 0L10 5L0 10z" fill="#8d867b" />
          </marker>
          <radialGradient id="node-glow">
            <stop offset="0" stopColor="#ec5a72" stopOpacity="0.18" />
            <stop offset="1" stopColor="#ec5a72" stopOpacity="0" />
          </radialGradient>
        </defs>
        <circle cx="300" cy="250" r="230" fill="url(#node-glow)" />
        <g fill="none" strokeLinecap="round">
          {FROM_W.map(([a, b, bend]) => (
            <path key={a + b} d={arc(a, b, bend)} stroke="#8d867b" strokeWidth="1.5" strokeDasharray="5 4" markerEnd="url(#arrow-soft)" />
          ))}
          <path d={arc('W', 'F', 20)} stroke="#8d867b" strokeWidth="1.5" strokeDasharray="5 4" markerEnd="url(#arrow-soft)" />
          <path d={arc('F', 'W', 20)} stroke="#ec5a72" strokeWidth="2.2" markerEnd="url(#arrow-solid)" />
          {INTO_F.map(([a, b, bend]) => (
            <path key={a + b} d={arc(a, b, bend)} stroke="#ec5a72" strokeWidth="2.2" markerEnd="url(#arrow-solid)" />
          ))}
        </g>
        {NODES.map((n) => (
          <g key={n.id}>
            <circle cx={n.x} cy={n.y} r={R} fill="#14121a" stroke={n.color} strokeWidth="2.5" />
            <text x={n.x} y={n.y + 8} textAnchor="middle" fontSize="26" fontWeight="700" fontFamily="'KaTeX_SansSerif', Inter, sans-serif" fill={n.color}>
              {n.id}
            </text>
            <text
              x={n.id === 'F' ? n.x + R + 6 : n.x}
              y={n.id === 'W' ? n.y + R + 20 : n.id === 'F' ? n.y + 24 : n.y - R - 10}
              textAnchor={n.id === 'F' ? 'start' : 'middle'}
              fontSize="19"
              fontFamily="Inter, sans-serif"
              fill="currentColor"
              stroke="#0b0a0e"
              strokeWidth="6"
              strokeLinejoin="round"
              paintOrder="stroke"
            >
              {n.label}
            </text>
          </g>
        ))}
      </svg>
    </div>
  );
}
