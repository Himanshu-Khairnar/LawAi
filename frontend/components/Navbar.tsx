"use client";

import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";

export function Navbar() {
  const router = useRouter();
  const pathname = usePathname();

  const handleLogout = () => {
    localStorage.removeItem("token");
    router.push("/login");
  };

  return (
    <nav className="bg-white shadow-sm p-4 flex justify-between items-center">
      <h1 className="text-xl font-semibold text-blue-700">⚖️ JusticeAI</h1>
      <div className="flex gap-4">
        <Link href="/chat" className={pathname === "/chat" ? "font-bold" : ""}>Chat</Link>
        <Link href="/notebook" className={pathname === "/notebook" ? "font-bold" : ""}>Notebook</Link>
        <Button onClick={handleLogout} variant="destructive" size="sm">Logout</Button>
      </div>
    </nav>
  );
}
