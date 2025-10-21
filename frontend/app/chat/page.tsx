"use client";

import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

export default function ChatPage() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState<{ q: string; a: string }[]>([]);

  const askAI = async () => {
    const token = localStorage.getItem("token");
    const res = await fetch("http://127.0.0.1:8000/chat/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ question }),
    });
    const data = await res.json();
    setMessages([...messages, { q: question, a: data.answer }]);
    setQuestion("");
  };

  return (
    <div className="max-w-3xl mx-auto mt-10">
      <Card>
        <CardContent className="p-4">
          <h1 className="text-xl font-semibold mb-3">JusticeAI Chatbot 💬</h1>
          <div className="h-72 overflow-y-auto border p-3 rounded-md mb-3 bg-gray-50">
            {messages.map((m, i) => (
              <div key={i} className="mb-2">
                <p><b>You:</b> {m.q}</p>
                <p><b>AI:</b> {m.a}</p>
              </div>
            ))}
          </div>
          <div className="flex gap-2">
            <Input
              placeholder="Ask about Indian laws..."
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
            />
            <Button onClick={askAI}>Ask</Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
