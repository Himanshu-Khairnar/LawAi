'use client'
import { useEffect, useState } from "react";

import { getUsers } from "@/lib/userApi";

export default function Home() {
  const [data, setData] = useState([]);

  useEffect(() => {
    getUsers().then((res) => setData(res.users));
    console.log(data);
    
  }, []);

  return (
    <div className="p-10">
      <h1 className="text-2xl font-bold text-blue-700">LawAI Project</h1>
      <p className="mt-4">Connected Users:</p>
      <ul className="mt-2">
        {data?.map((user, idx) => (
          <li key={idx} className="text-gray-700">{user}</li>
        ))}
      </ul>
    </div>
  );
}
