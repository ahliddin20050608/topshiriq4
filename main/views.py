from django.shortcuts import render
from django.http import HttpResponse

def registration(request):
    return HttpResponse("""<!doctype html>
<html lang="uz">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Ro'yxatdan o'tish — Chiroyli</title>
  <style>
    /* Minimal, modern, responsive registration page */
    :root{
      --bg1:#0f1724; --bg2:#0b1220; --glass: rgba(255,255,255,0.04);
      --accent1:#7b61ff; --accent2:#46e6ff; --white: #eef2ff;
      --muted: rgba(238,242,255,0.65);
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, Arial;
    }
    *{box-sizing:border-box}
    html,body{height:100%;margin:0;background:linear-gradient(180deg,var(--bg1),var(--bg2));color:var(--white);display:flex;align-items:center;justify-content:center;padding:28px}

    .wrap{max-width:980px;width:100%;display:grid;grid-template-columns:520px 1fr;gap:28px;align-items:center}

    /* left - illustration + heading */
    .left{background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));border-radius:16px;padding:32px;border:1px solid var(--glass);backdrop-filter: blur(6px);box-shadow: 0 20px 50px rgba(2,6,23,0.6)}
    .hero-ill{height:220px;border-radius:12px;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,var(--accent1),var(--accent2));color:#071125;font-weight:700;font-size:48px}
    h1{margin:18px 0 6px;font-size:24px}
    p.lead{margin:0;color:var(--muted);line-height:1.5}

    .features{display:flex;gap:12px;margin-top:18px}
    .pill{padding:8px 12px;border-radius:999px;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.02);font-size:13px;color:var(--muted)}

    /* right - form */
    .card{padding:26px;border-radius:14px;background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));border:1px solid var(--glass);backdrop-filter: blur(6px)}
    form{display:grid;gap:12px}

    .row{display:flex;gap:12px}
    .input{position:relative}
    .input input{width:100%;padding:14px 14px;border-radius:10px;border:1px solid rgba(255,255,255,0.06);background:transparent;color:var(--white);outline:none;font-size:15px}
    .input input::placeholder{color:rgba(255,255,255,0.35)}
    label.float{position:absolute;left:14px;top:50%;transform:translateY(-50%);pointer-events:none;color:rgba(255,255,255,0.45);transition:all .12s ease}
    .input input:focus + label.float, .input input:not(:placeholder-shown) + label.float{top:8px;transform:none;font-size:12px;color:var(--accent2)}

    .submit{margin-top:6px;padding:12px;border-radius:10px;border:none;background:linear-gradient(90deg,var(--accent1),var(--accent2));color:#071125;font-weight:700;cursor:pointer;font-size:15px}
    .alt{display:flex;justify-content:space-between;align-items:center;font-size:13px;color:var(--muted);margin-top:8px}

    .socials{display:flex;gap:8px;margin-top:12px}
    .socials button{flex:1;padding:10px;border-radius:10px;border:1px solid rgba(255,255,255,0.04);background:transparent;color:var(--white);font-weight:600;cursor:pointer}

    /* small helper */
    .note{font-size:13px;color:var(--muted)}

    /* responsive */
    @media (max-width:900px){.wrap{grid-template-columns:1fr}.left{order:2}}

    /* subtle micro interactions */
    .input input:focus{box-shadow:0 8px 30px rgba(75,50,240,0.08);border-color:rgba(75,50,240,0.25)}
    .submit:active{transform:translateY(1px)}

  </style>
</head>
<body>
  <div class="wrap">
    <div class="left">
      <div class="hero-ill">R</div>
      <h1>Ro'yxatdan o'ting</h1>
      <p class="lead">Foydalanuvchi profili yarating — xavfsiz, tez va zamonaviy interfeys bilan. Kerakli ma'lumotlarni kiriting va boshlang.</p>

      <div class="features">
        <div class="pill">Tez ishga tushirish</div>
        <div class="pill">Profil rasm</div>
        <div class="pill">Parol kuchliligi</div>
      </div>
    </div>

    <div class="card">
      <!-- Agar Django templating ishlatsangiz, action va csrf token qo'shing -->
      <form action="/register/" method="post" enctype="multipart/form-data" novalidate>

        <div class="row">
          <div class="input" style="flex:1">
            <input id="first_name" name="first_name" type="text" placeholder="Ismingiz" required />
            <label class="float" for="first_name">Ism</label>
          </div>

          <div class="input" style="flex:1">
            <input id="username" name="username" type="text" placeholder="Foydalanuvchi nomi" required />
            <label class="float" for="username">Foydalanuvchi</label>
          </div>
        </div>

        <div class="input">
          <input id="email" name="email" type="email" placeholder="mailto:you@example.com" required />
          <label class="float" for="email">Email</label>
        </div>

        <div class="row">
          <div class="input" style="flex:1">
            <input id="password" name="password" type="password" placeholder="Parol" required />
            <label class="float" for="password">Parol</label>
          </div>

          <div class="input" style="flex:1">
            <input id="password2" name="password2" type="password" placeholder="Parolni takrorlang" required />
            <label class="float" for="password2">Parolni takrorlang</label>
          </div>
        </div>

        <div class="input">
          <input id="avatar" name="avatar" type="file" accept="image/*" />
          <label class="float" for="avatar">Profil rasmi (ixtiyoriy)</label>
        </div>

        <div class="alt"><span class="note">Iltimos, barcha maydonlarni to'ldiring</span><a href="#" style="color:var(--accent2);text-decoration:none">Kirish</a></div>

        <button type="submit" class="submit">Ro'yxatdan o'tish</button>

        <div class="socials">
          <button type="button">Google bilan</button>
          <button type="button">Facebook bilan</button>
        </div>

      </form>
    </div>
  </div>
</body>
</html>


""")