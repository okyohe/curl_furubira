import fs from "fs/promises";
import path from "path";
import dotenv from "dotenv";
import OpenAI from "openai";

// 環境変数を読み込む
dotenv.config();

// APIキーの確認
if (!process.env.OPENAI_API_KEY) {
  console.error("エラー: OPENAI_API_KEY が設定されていません。");
  process.exit(1);
}

// OpenAI API の設定
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

// **ファイルがあるディレクトリのパス**
const directoryPath =
  "C:\\Users\\yhwca\\OneDrive\\デスクトップ\\curl_furubira_photo";

// **ファイル名を翻訳して短縮する関数**
async function shortenAndTranslate(filename) {
  try {
    const response = await openai.chat.completions.create({
      model: "gpt-4o",
      messages: [
        {
          role: "system",
          content:
            "You are a helpful assistant that translates Japanese file names into concise and meaningful English. " +
            "Keep numbers and underscores (_) unchanged. Do not translate file extensions (e.g., .jpg, .png, .txt). " +
            "Remove unnecessary words like 'アーティスティック'. Keep it short and simple.",
        },
        {
          role: "user",
          content: `Translate the following filename: "${filename}"`,
        },
      ],
      max_tokens: 20,
      temperature: 0.5,
    });

    console.log("APIレスポンス: ", response);

    // GPTの出力を取得（空白トリム）
    const translated =
      response.choices?.[0]?.message?.content?.trim() || filename;

    // **ファイル名として適切な形式に整形**
    const sanitized = translated
      .replace(/[^a-zA-Z0-9_\-.]/g, "_") // 記号をアンダースコアに
      .replace(/_{2,}/g, "_") // 連続するアンダースコアを1つに
      .toLowerCase(); // 小文字に統一

    return { original: filename, translated: sanitized };
  } catch (error) {
    console.error("OpenAI APIエラー: ", error);
    return { original: filename, translated: filename }; // エラー時は元のファイル名を返す
  }
}

// **ファイル名を変更する関数**
async function renameFile(originalName, newName) {
  try {
    const oldPath = path.join(directoryPath, originalName);
    const newPath = path.join(directoryPath, newName);

    // **既に同じ名前のファイルが存在する場合、別の名前にする**
    let uniqueNewPath = newPath;
    let counter = 1;
    while (await fileExists(uniqueNewPath)) {
      const ext = path.extname(newName); // 拡張子
      const baseName = path.basename(newName, ext); // 拡張子なしの名前
      uniqueNewPath = path.join(directoryPath, `${baseName}_${counter}${ext}`);
      counter++;
    }

    // **ファイル名を変更**
    await fs.rename(oldPath, uniqueNewPath);
    console.log(`✅ ${originalName} → ${path.basename(uniqueNewPath)}`);
    return { original: originalName, translated: path.basename(uniqueNewPath) };
  } catch (err) {
    console.error(`❌ ファイル名変更エラー: ${originalName} → ${newName}`, err);
    return { original: originalName, translated: originalName };
  }
}

// **ファイルの存在チェック**
async function fileExists(filePath) {
  try {
    await fs.access(filePath);
    return true;
  } catch {
    return false;
  }
}

// **メイン処理**
async function processFiles() {
  try {
    // **ディレクトリ内のファイル一覧を取得**
    const files = await fs.readdir(directoryPath);

    // **各ファイル名を翻訳して短縮（並列処理）**
    const translatedFiles = await Promise.all(files.map(shortenAndTranslate));

    // **ファイル名を実際に変更**
    const renamedFiles = await Promise.all(
      translatedFiles.map(({ original, translated }) =>
        renameFile(original, translated)
      )
    );

    // **変更前後のファイル名をJSONに保存**
    const jsonFilePath = path.join(directoryPath, "translatedFilenames.json");
    await fs.writeFile(jsonFilePath, JSON.stringify(renamedFiles, null, 2));

    console.log("✅ すべてのファイル名が変更され、JSONに保存されました。");
  } catch (err) {
    console.error("❌ 処理中にエラーが発生しました: ", err);
  }
}

// **スクリプトを実行**
processFiles();
