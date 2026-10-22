import type { CSSProperties } from 'react';
import type { Metadata } from 'next';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import DOMPurify from 'isomorphic-dompurify';
import * as cheerio from 'cheerio';
import { PaperBody } from './PaperBody';
import { TableOfContents, type Heading } from '@/components/TableOfContents';
import { AUTHOR, CODE_URL, paperContent, papers } from '@/lib/papers';
import { renderMath } from '@/lib/render-math';

type Props = { params: { slug: string } };

export const dynamicParams = false;

export function generateStaticParams() {
  return papers.map((p) => ({ slug: p.slug }));
}

export function generateMetadata({ params }: Props): Metadata {
  const paper = papers.find((p) => p.slug === params.slug);
  if (!paper) return {};
  const title = paper.subtitle ? `${paper.title}: ${paper.subtitle}` : paper.title;
  const og = `/og/${paper.slug}.png`;
  return {
    title,
    description: paper.abstract,
    openGraph: {
      title,
      description: paper.abstract,
      type: 'article',
      url: `/papers/${paper.slug}/`,
      images: [{ url: og, width: 1200, height: 630 }],
    },
    twitter: { card: 'summary_large_image', title, description: paper.abstract, images: [og] },
  };
}

function prepare(slug: string) {
  // sanitize our own HTML first, then render math, so KaTeX's MathML (semantics/annotation) stays intact
  const clean = DOMPurify.sanitize(paperContent(slug), { ADD_ATTR: ['target'], USE_PROFILES: { html: true, svg: true } });
  const html = renderMath(clean);
  const $ = cheerio.load(html, null, false);
  const headings: Heading[] = [];
  $('h2[id], h3[id]').each((_, el) => {
    const $e = $(el);
    const num = $e.find('.header-section-number').text().trim();
    const text = $e.clone().children('.header-section-number').remove().end().text().trim();
    headings.push({ id: $e.attr('id')!, text: num ? `${num} ${text}` : text, level: el.tagName === 'h2' ? 2 : 3 });
  });
  return { html, headings };
}

export default function PaperPage({ params }: Props) {
  const i = papers.findIndex((p) => p.slug === params.slug);
  if (i < 0) notFound();
  const paper = papers[i];
  const prev = papers[i - 1];
  const next = papers[i + 1];
  const { html, headings } = prepare(paper.slug);

  return (
    <>
      <header className="paper-head" style={{ '--pc': paper.color } as CSSProperties}>
        <div className="container">
          <div className="part-tag">{paper.part} of {papers.length}</div>
          <h1>{paper.title}</h1>
          {paper.subtitle && <p className="subtitle">{paper.subtitle}</p>}
          <p className="question">{paper.question}</p>
          <div className="byline">
            <b>{AUTHOR}</b>, The YonedaAI Collaboration, YonedaAI Research Collective, Chicago, IL
          </div>
          <div className="chips">
            <span className="chip">{paper.date}</span>
            <span className="chip">{paper.pages} pages</span>
            <span className="chip">{paper.references} references</span>
            <span className="chip">{paper.category}</span>
          </div>
          <div className="btn-row">
            <a className="btn btn-primary" href={paper.pdf}>Download PDF</a>
            <a className="btn" href={CODE_URL}>Code</a>
          </div>
          <section className="abstract" aria-labelledby="abstract-h">
            <h2 id="abstract-h">Abstract</h2>
            <p>{paper.abstract}</p>
          </section>
        </div>
      </header>

      <div className="container paper-layout" style={{ '--pc': paper.color } as CSSProperties}>
        <aside>
          <TableOfContents headings={headings} />
        </aside>
        <article className="paper-main">
          <PaperBody html={html} />
          <nav className="paper-nav" aria-label="Series navigation">
            {prev ? (
              <Link href={`/papers/${prev.slug}/`} className="prev">
                <small>Previous, {prev.part}</small>
                {prev.title}
              </Link>
            ) : (
              <span />
            )}
            {next ? (
              <Link href={`/papers/${next.slug}/`} className="next">
                <small>Next, {next.part}</small>
                {next.title}
              </Link>
            ) : (
              <Link href="/#papers" className="next">
                <small>Back to</small>
                All papers
              </Link>
            )}
          </nav>
        </article>
      </div>
      <a className="pdf-fab" href={paper.pdf} aria-label={`Download PDF of ${paper.title}`}>PDF</a>
    </>
  );
}
