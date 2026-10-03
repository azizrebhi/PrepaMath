import { readFileSync } from 'fs';

function stripRedundantHeadings(content, chunkType, number) {
  const escType = chunkType.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const escNumber = number ? number.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") : "";
  const headingPattern = `#{0,3}\\s*\\*{0,3}\\s*${escType}s?\\s*${escNumber}\\s*\\*{0,3}`;
  let cleaned = content.replace(new RegExp(`^(?:p\\.\\d+\\s+)?${headingPattern}\\s*\\n+`, "i"), "");
  cleaned = cleaned.replace(
    new RegExp(`(---\\s*Solution\\s*\\([^)]*\\)\\s*---\\s*\\n+)${headingPattern}\\s*\\n+`, "i"),
    "$1"
  );
  return cleaned;
}
function stripPageReferences(content) {
  return content.replace(/^\s*\*{0,2}Démonstration\*{0,2}\s+page\s+\d+\.?\s*$/gim, "");
}
function stripRunningHeaderArtifacts(content) {
  return content.replace(
    /^\s*\*{0,3}#{0,3}\*{0,3}\s*(?:I|II|III|IV|VI|VII|VIII|IX)\s+[A-ZÀ-Ý][^\n]*?\*{0,3}\s*$/gm,
    ""
  );
}
function fixDisplayOnlyTags(content) {
  return content.replace(/\\tag\{([^}]*)\}/g, "\\quad ($1)");
}
function styleSolutionMarker(content) {
  return content.replace(/---\s*Solution\s*\([^)]*\)\s*---/gi, "\n#### Solution\n");
}
function cleanChunkContent(content, chunkType, number) {
  let cleaned = stripRedundantHeadings(content, chunkType, number);
  cleaned = stripPageReferences(cleaned);
  cleaned = stripRunningHeaderArtifacts(cleaned);
  cleaned = fixDisplayOnlyTags(cleaned);
  cleaned = styleSolutionMarker(cleaned);
  return cleaned;
}

const exemple = readFileSync('../backend/scratch/exemple_raw.txt', 'utf-8');
console.log('=== Exemple (chunk_type="Exemple", heading says "Exemples") ===');
console.log(cleanChunkContent(exemple, 'Exemple', null));

const prop4 = readFileSync('../backend/scratch/chunk12_full.txt', 'utf-8');
console.log('\n=== Proposition 4 (has Démonstration page + Solution marker) ===');
console.log(cleanChunkContent(prop4, 'Proposition', '4'));
