import fs from 'node:fs';
import path from 'node:path';
import papersJson from '../papers.json';

export type Paper = {
  slug: string;
  part: string;
  pillar: string;
  color: string;
  title: string;
  subtitle: string;
  question: string;
  abstract: string;
  abstractHtml: string;
  pages: number;
  references: number;
  date: string;
  pdf: string;
  cover: string;
  coverCard: string;
  category: string;
  hasCode: boolean;
};

export const papers = papersJson as Paper[];

export const SITE_TITLE = 'The Formalized State';
export const SITE_SERIES = 'The Six Pillars of the Beast System';
export const AUTHOR = 'Matthew Long';
export const GITHUB = 'https://github.com/YonedaAI/the-beast-system';
export const CODE_URL = `${GITHUB}/tree/main/model`;

export function paperContent(slug: string): string {
  return fs.readFileSync(path.join(process.cwd(), 'content', `${slug}.html`), 'utf8');
}

export function excerpt(text: string, n = 150): string {
  if (text.length <= n) return text;
  const cut = text.slice(0, n);
  return cut.slice(0, cut.lastIndexOf(' ')) + '...';
}
