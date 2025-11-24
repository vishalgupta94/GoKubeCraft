import { md5hash } from "aws-cdk-lib/core/lib/helpers-internal";
import { createHash } from "crypto";
import fs from "fs";
import path from "path";

const INPUT_FILE = "./sample_60mb.json";
const OUTPUT_DIR = "./parts";
const CHUNK_SIZE = 1024 * 1024; // 1 MB

if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR);

const readStream = fs.createReadStream(INPUT_FILE, { highWaterMark: CHUNK_SIZE });
let part = 0;

readStream.on("data", (chunk,) => {
  const partFile = path.join(OUTPUT_DIR, `part_${String(++part).padStart(3, "0")}`);
  
  const hash = createHash("md5");
  hash.update(chunk);

  console.log("index",hash.digest("hex"))

});

readStream.on("end", () => console.log(`✅ Done! Created ${part} parts.`));
readStream.on("error", (err) => console.error("❌ Error:", err));
