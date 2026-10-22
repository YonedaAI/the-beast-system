'use client';
import { useEffect, useState } from 'react';

export type Heading = { id: string; text: string; level: number };

export function TableOfContents({ headings }: { headings: Heading[] }) {
  const [activeId, setActiveId] = useState('');
  const [open, setOpen] = useState(false);

  useEffect(() => {
    const onScroll = () => {
      const scrollY = window.scrollY + 100;
      let current = '';
      for (const { id } of headings) {
        const el = document.getElementById(id);
        if (el && el.getBoundingClientRect().top + window.scrollY <= scrollY) current = id;
      }
      setActiveId(current);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    const t = window.setTimeout(onScroll, 50); // content is injected after mount
    onScroll();
    return () => {
      window.removeEventListener('scroll', onScroll);
      window.removeEventListener('resize', onScroll);
      window.clearTimeout(t);
    };
  }, [headings]);

  return (
    <div className={`toc-wrap ${open ? 'toc-open' : ''}`}>
      <button
        type="button"
        className="toc-toggle"
        aria-expanded={open}
        aria-controls="toc-panel"
        onClick={() => setOpen((o) => !o)}
      >
        <span>Contents</span>
        <span className="burger" aria-hidden="true">
          <i />
          <i />
          <i />
        </span>
      </button>
      <nav className="toc-panel" id="toc-panel" aria-label="Table of contents">
        <p className="toc-title">Contents</p>
        {headings.map(({ id, text, level }) => (
          <a
            key={id}
            href={`#${id}`}
            onClick={() => setOpen(false)}
            className={`toc-item ${level === 3 ? 'toc-sub' : ''} ${activeId === id ? 'toc-active' : ''}`}
            aria-current={activeId === id ? 'location' : undefined}
          >
            {text}
          </a>
        ))}
      </nav>
    </div>
  );
}
