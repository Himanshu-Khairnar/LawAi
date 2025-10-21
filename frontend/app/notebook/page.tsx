"use client";

import { useState } from "react";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function NotebookPage() {
  const [content, setContent] = useState("");
  const [summary, setSummary] = useState("");
  const [flashcards, setFlashcards] = useState<any[]>([]);

  const summarize = async () => {
    const res = await fetch("http://127.0.0.1:8000/notebook/1/summarize", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ content }),
    });
    const data = await res.json();
    setSummary(data.summary);
  };

  const generateFlashcards = async () => {
    const res = await fetch("http://127.0.0.1:8000/notebook/1/flashcards", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ content }),
    });
    const data = await res.json();
    setFlashcards(data.flashcards);
  };

  return (
    <div className="max-w-3xl mx-auto mt-10">
      <Card>
        <CardContent className="p-4">
          <h1 className="text-2xl font-semibold mb-3">NotebookLLM 📚</h1>
          <Textarea
            placeholder="Paste your notes here..."
            value={content}
            onChange={(e) => setContent(e.target.value)}
            className="h-40 mb-4"
          />
          <div className="flex gap-2">
            <Button onClick={summarize}>Summarize</Button>
            <Button variant="secondary" onClick={generateFlashcards}>Flashcards</Button>
          </div>

          {summary && (
            <div className="mt-4 bg-gray-100 p-3 rounded">
              <h2 className="font-bold">Summary:</h2>
              <p>{summary}</p>
            </div>
          )}

          {flashcards.length > 0 && (
            <div className="mt-4 bg-gray-50 p-3 rounded">
              <h2 className="font-bold">Flashcards:</h2>
              {flashcards.map((card, i) => (
                <p key={i}>🧠 <b>{card.q}</b> — {card.a}</p>
              ))}
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
