import type { Metadata } from 'next';
import PillarDiagram from '@/components/PillarDiagram';
import { PaperCard } from '@/components/PaperCard';
import { CODE_URL, papers } from '@/lib/papers';

const description =
  'The six-pillar framework identifies an invariant structure of human governance, supported by historical observation and given precise expression through mathematics.';

export const metadata: Metadata = {
  description,
  openGraph: {
    title: 'The Six Pillars of the Beast System',
    description,
    url: '/',
    images: [{ url: '/og/og-image.png', width: 1200, height: 630 }],
  },
  twitter: { card: 'summary_large_image', description, images: ['/og/og-image.png'] },
};

const pillars = papers.filter((p) => p.pillar);
const capstone = papers.find((p) => !p.pillar)!;
const totalPages = papers.reduce((n, p) => n + p.pages, 0);

export default function Home() {
  return (
    <>
      <section className="hero">
        <div className="container hero-grid">
          <div>
            <div className="eyebrow">A seven-part research series</div>
            <h1>
              The Six Pillars of the <em>Beast System</em>
            </h1>
            <p className="lede">
              {'The six-pillar framework identifies an invariant structure of human governance, supported by historical observation and given precise expression through mathematics.'}
            </p>
            <p className="thesis">The ideology changes. The institutional functions remain.</p>
            <p className="lede">
              Six functions appear in every governance system: financial, political, judicial, ideological, coercive and
              productive. The series follows them through capitalism, communist party-states, democratic socialism,
              Islamic states, historical Catholic monarchies and secular democracies.
            </p>
            <div className="hero-stats">
              <div className="hero-stat"><b>{papers.length}</b><span>Papers</span></div>
              <div className="hero-stat"><b>6</b><span>Functions</span></div>
              <div className="hero-stat"><b>{totalPages}</b><span>Pages</span></div>
            </div>
            <div className="btn-row">
              <a className="btn btn-primary" href="#papers">Read the papers</a>
              <a className="btn" href={CODE_URL}>Code</a>
            </div>
          </div>
          <PillarDiagram />
        </div>
      </section>

      <section className="section" id="papers">
        <div className="container">
          <h2>The papers</h2>
          <p className="section-intro">
            Parts I to VI each take one function and ask who holds it. Part VII states the structure they share.
          </p>
          <div className="grid">
            {pillars.map((p) => (
              <PaperCard key={p.slug} paper={p} />
            ))}
            <PaperCard paper={capstone} full />
          </div>
        </div>
      </section>

      <section className="section">
        <div className="container">
          <h2>The formalized state</h2>
          <p className="section-intro">
            Part VII presents the Formalized State as a universal abstraction. It proves representation, necessity,
            minimality and uniqueness relative to stated axioms, and shows that having the structure does not imply
            capture.
          </p>
          <div className="six-list">
            {pillars.map((p) => (
              <div key={p.slug} className="six-item" style={{ ['--pc' as string]: p.color }}>
                <span className="pillar-glyph" style={{ color: p.color }} aria-hidden="true">{p.pillar}</span>
                <div>
                  <b>{p.title.split(' and ')[0]}</b>
                  <span>{p.question}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="section" id="scope">
        <div className="container">
          <h2>Scope</h2>
          <p className="scope-note">
            &quot;Beast System&quot; is a typological reading of Revelation 13. Here it names a universal six-function
            structure. It is never a label for a religion, a people, a regime or a person.
          </p>
        </div>
      </section>
    </>
  );
}
