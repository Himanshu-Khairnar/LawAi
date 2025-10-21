"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Card, CardHeader, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");
  const router = useRouter();

  const register = async () => {
    const res = await fetch("http://127.0.0.1:8000/users/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, email, password }),
    });
    if (res.ok) alert("Registered successfully! Now login.");
  };

  const login = async () => {
    const res = await fetch("http://127.0.0.1:8000/users/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });
    const data = await res.json();
    if (data.access_token) {
      localStorage.setItem("token", data.access_token);
      router.push("/chat");
    }
  };

  return (
    <div className="flex justify-center items-center h-[80vh]">
      <Card className="w-[400px]">
        <CardHeader>
          <h2 className="text-center text-2xl font-semibold">Login / Register</h2>
        </CardHeader>
        <CardContent className="flex flex-col gap-3">
          <Input placeholder="Name" onChange={(e) => setName(e.target.value)} />
          <Input placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
          <Input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
          <div className="flex gap-2">
            <Button onClick={register} className="w-1/2">Register</Button>
            <Button onClick={login} className="w-1/2" variant="secondary">Login</Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
