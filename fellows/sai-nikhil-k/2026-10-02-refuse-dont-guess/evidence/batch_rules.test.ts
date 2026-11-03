/**
 * batch_rules — run Gavia 0.3.1's own selection code on this reel's real photos.
 *
 * Copied into the gavia clone as desktop/src/lib/batch_rules.test.ts and run
 * with the repo's vitest config (jsdom), so `selectImages` is the shipped
 * function, unmodified, at v0.3.1 (760e465). Inputs are the Commons photos in
 * ../ui/ (see batch_manifest.json), not stubs. Prints one JSON line per case.
 *
 *   REEL=<reel dir> npx vitest run src/lib/batch_rules.test.ts
 */
import { readFileSync } from 'node:fs'
import { join } from 'node:path'
import { zipSync, strToU8 } from 'fflate'
import { it } from 'vitest'
import { MAX_IMAGE_BYTES, describeSkipped, selectImages } from './batch'

const REEL = process.env.REEL as string
const photo = (n: number) => {
  const name = `photo-${String(n).padStart(2, '0')}.jpg`
  return { name, bytes: new Uint8Array(readFileSync(join(REEL, 'ui', n <= 25 ? 'survey' : 'extra', name))) }
}
const asFile = (name: string, bytes: Uint8Array, type: string) =>
  new File([bytes as Uint8Array<ArrayBuffer>], name, { type })
const jpeg = (n: number) => {
  const p = photo(n)
  return asFile(p.name, p.bytes, 'image/jpeg')
}
const range = (a: number, b: number) => Array.from({ length: b - a + 1 }, (_, i) => a + i)

async function report(name: string, files: File[]) {
  const s = await selectImages(files)
  const line = s.ok
    ? { case: name, picked: files.map((f) => f.name).length, ok: true, checked: s.images.length,
        skipped: s.skipped.map((x) => `${x.name}:${x.reason}`), note: describeSkipped(s.skipped) }
    : { case: name, picked: files.length, ok: false, checked: 0, message: s.message }
  console.log(JSON.stringify(line))
}

it('runs the shipped batch rules on the reel photos', async () => {
  const survey = asFile('survey.zip', new Uint8Array(readFileSync(join(REEL, 'ui', 'survey.zip'))), 'application/zip')

  await report('25 photos picked', range(1, 25).map(jpeg))
  await report('26 photos picked', range(1, 26).map(jpeg))
  await report('survey.zip (25 inside)', [survey])
  await report('survey.zip + photo-26.jpg', [survey, jpeg(26)])

  const entries: Record<string, Uint8Array> = {}
  for (const n of range(1, 25)) entries[photo(n).name] = photo(n).bytes
  entries['notes.txt'] = strToU8('Shoreline survey, north bay. 25 photos.')
  entries['__MACOSX/._photo-01.jpg'] = strToU8('resource fork')
  await report('zip of 25 + notes.txt + __MACOSX', [asFile('survey-notes.zip', zipSync(entries), 'application/zip')])

  const thirty: Record<string, Uint8Array> = {}
  for (const n of range(1, 30)) thirty[`photo-${String(n).padStart(2, '0')}.jpg`] = photo(((n - 1) % 26) + 1).bytes
  await report('zip of 30 (25 + 5 repeats)', [asFile('survey-30.zip', zipSync(thirty), 'application/zip')])

  const big = new Uint8Array(MAX_IMAGE_BYTES + 1)
  big.set(photo(1).bytes)
  await report('one photo at 20 MiB + 1 byte', [asFile('photo-big.jpg', big, 'image/jpeg')])
  await report('24 photos + that one', [...range(2, 25).map(jpeg), asFile('photo-big.jpg', big, 'image/jpeg')])
})
