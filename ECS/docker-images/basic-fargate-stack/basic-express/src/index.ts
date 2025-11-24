import express, { Request, Response } from "express";

const app = express();
const PORT = Number(process.env.PORT) || 3000;

app.use(express.json());

// Root route
app.get("/", (_req: Request, res: Response) => {
  res.send("🚀 Hello from TypeScript + Express in Docker!");
});

// Health check
app.get("/health", (_req: Request, res: Response) => {
  res.json({ status: "ok", timestamp: new Date().toISOString() });
});

// Start server
app.listen(PORT, () => {
  console.log(`✅ Server running on port ${PORT}`);
});