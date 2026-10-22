import type { Metadata, Viewport } from 'next';
import { Cormorant_Garamond, Inter } from 'next/font/google';
import Link from 'next/link';
import 'katex/dist/katex.min.css';
import './globals.css';
import { AUTHOR, CODE_URL, GITHUB, SITE_TITLE } from '@/lib/papers';

const display = Cormorant_Garamond({ subsets: ['latin'], weight: ['500', '600', '700'], style: ['normal', 'italic'], variable: '--font-display', display: 'swap' });
const body = Inter({ subsets: ['latin'], variable: '--font-body', display: 'swap' });

const siteUrl = process.env.SITE_URL || 'https://the-beast-system.vercel.app';
const description =
  'The six-pillar framework identifies an invariant structure of human governance, supported by historical observation and given precise expression through mathematics.';

export const metadata: Metadata = {
  metadataBase: new URL(siteUrl),
  title: { default: SITE_TITLE, template: `%s | ${SITE_TITLE}` },
  description,
  authors: [{ name: AUTHOR }],
  openGraph: {
    type: 'website',
    siteName: SITE_TITLE,
    title: SITE_TITLE,
    description,
    images: [{ url: '/og/og-image.png', width: 1200, height: 630 }],
  },
  twitter: { card: 'summary_large_image', title: SITE_TITLE, description, images: ['/og/og-image.png'] },
};

export const viewport: Viewport = { themeColor: '#0b0a0e' };

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`${display.variable} ${body.variable}`}>
      <body>
        <header className="site-header">
          <div className="site-header-inner">
            <Link href="/" className="site-title">
              The Six Pillars of the <span>Beast System</span>
            </Link>
            <nav className="site-nav" aria-label="Main">
              <Link href="/#papers">Papers</Link>
              <Link href="/#scope">Scope</Link>
              <a href={CODE_URL}>Code</a>
              <a href={GITHUB}>GitHub</a>
            </nav>
          </div>
        </header>
        <main>{children}</main>
        <footer className="site-footer">
          <div className="site-footer-inner">
            <div>
              <strong>{AUTHOR}</strong>
              <br />
              The YonedaAI Collaboration, YonedaAI Research Collective
              <br />
              Chicago, IL
            </div>
            <div>
              <a href={GITHUB}>github.com/YonedaAI/the-beast-system</a>
            </div>
            <div>October 2026</div>
          </div>
        </footer>
      </body>
    </html>
  );
}
