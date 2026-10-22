// Server component: the pre-rendered pandoc + KaTeX HTML is emitted into the static page,
// so crawlers see the full paper text.
export function PaperBody({ html }: { html: string }) {
  return <div className="paper-content" dangerouslySetInnerHTML={{ __html: html }} />;
}
