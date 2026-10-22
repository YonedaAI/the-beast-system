import Link from 'next/link';
import Image from 'next/image';
import type { CSSProperties } from 'react';
import { excerpt, type Paper } from '@/lib/papers';

export function PaperCard({ paper, full = false }: { paper: Paper; full?: boolean }) {
  return (
    <article className={`card ${full ? 'card-full' : ''}`} style={{ '--pc': paper.color } as CSSProperties}>
      <Link href={`/papers/${paper.slug}/`} className="card-media" aria-hidden="true" tabIndex={-1}>
        <Image src={paper.coverCard} alt="" width={640} height={828} unoptimized />
      </Link>
      <div className="card-body">
        <div className="card-part">
          {paper.pillar && <span className="pillar-glyph" aria-hidden="true">{paper.pillar}</span>}
          {paper.part}
        </div>
        <h3>
          <Link href={`/papers/${paper.slug}/`}>{paper.title}</Link>
        </h3>
        {paper.subtitle && <p className="card-sub">{paper.subtitle}</p>}
        <p className="card-q">{paper.question}</p>
        <p className="card-abs">{excerpt(paper.abstract, full ? 320 : 150)}</p>
        <div className="card-meta">{paper.pages} pages · {paper.references} references</div>
        <div className="card-actions">
          <Link className="btn btn-read" href={`/papers/${paper.slug}/`}>Read</Link>
          <a className="btn" href={paper.pdf}>PDF</a>
        </div>
      </div>
    </article>
  );
}
