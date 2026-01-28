const tg = window.Telegram.WebApp;
tg.expand();

document.getElementById("btn").onclick = async () => {
  const res = await fetch("https://TON_BACKEND.railway.app/api/ping");
  const data = await res.json();
  alert(data.message);
};
