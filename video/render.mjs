import fs from "node:fs";
import path from "node:path";
import {bundle} from "@remotion/bundler";
import {renderMedia, selectComposition} from "@remotion/renderer";

const [, , manifestArg, outputArg] = process.argv;
if (!manifestArg || !outputArg) {
  throw new Error("Usage: node render.mjs <manifest.json> <output.mp4>");
}

const manifestPath = path.resolve(manifestArg);
const outputPath = path.resolve(outputArg);
const inputProps = JSON.parse(fs.readFileSync(manifestPath, "utf8"));
const browserExecutable = [
  process.env.HORIZON_BROWSER_EXECUTABLE,
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
  "/usr/bin/google-chrome",
  "/usr/bin/chromium",
].find((candidate) => candidate && fs.existsSync(candidate));
const serveUrl = await bundle({
  entryPoint: path.resolve("src/index.ts"),
  publicDir: path.resolve("public"),
});
const selected = await selectComposition({
  serveUrl,
  id: "HorizonDaily",
  inputProps,
  browserExecutable,
});
const composition = {
  ...selected,
  width: inputProps.width,
  height: inputProps.height,
  fps: inputProps.fps,
  durationInFrames: inputProps.totalFrames,
};
let lastPercent = -1;

await renderMedia({
  composition,
  serveUrl,
  codec: "h264",
  outputLocation: outputPath,
  inputProps,
  browserExecutable,
  chromiumOptions: {
    enableMultiProcessOnLinux: true
  },
  onProgress: ({progress}) => {
    const percent = Math.round(progress * 100);
    if (percent !== lastPercent) {
      lastPercent = percent;
      process.stdout.write("\rRendering " + percent + "%");
    }
  },
});
process.stdout.write("\nRendered " + outputPath + "\n");
