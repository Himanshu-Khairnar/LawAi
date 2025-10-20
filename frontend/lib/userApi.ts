export const BASE_URL = "http://127.0.0.1:8000/";

export async function getUsers() {
  const res = await fetch(`${BASE_URL}/user`);
  return res.json();
}
