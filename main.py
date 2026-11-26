#!/usr/bin/env python3
"""The Moon Gets One Star -- entry builder (Akun 2, @wantorieta15).

Entry (113 chars, one line, no trailing newline):
"One star. Every full moon my neighbor turns into a werewolf and howls
till dawn. The Moon just hangs there, smug."

Why this line (pola pemenang rank 1-2 bounty satu-baris sekeluarga,
ditarik via API make.fun 26 Nov 2026 dan diverifikasi dari artifact.txt):
- Laugh Sprint #1 (777.695): adegan konkret + sensorik (cokelat di
  pantry, lampu mati) lalu twist di fragmen akhir ("like a raccoon
  with a mortgage").
- Laugh Sprint #2 (776.452): setup satu adegan (meal-prep Minggu) +
  twist yang membalik setup (sereal di atas sink Senin).
- Zero Use #1 (779.634): kekuatan absurd + batasan spesifik, ditutup
  daftar yang memuncak di item paling memalukan ("at my own wedding").
- Zero Use #2 (725.027): setup singkat + twist "sudah terpakai".
Formula juara: SATU adegan konkret + satu keluhan spesifik + twist di
fragmen terakhir, nada deadpan, tanpa "!", tanpa menjelaskan lelucon.
Entri ini mengikuti formula itu: adegan tunggal (tetangga jadi
werewolf tiap bulan purnama, melolong sampai subuh) + twist akhir
("The Moon just hangs there, smug") -- keluhan yang HANYA bisa
ditujukan ke Bulan (tanpa Bulan, tidak ada werewolf), bukan lelucon
generik yang bisa ditukar ke produk lain. Bukan kawah/keju/terang
(juri menghukum lelucon obvious itu), bukan pasang surut (sudah
dipakai ramai di lapangan bounty ini + dipakai entri Akun 2 di bounty
"The Moon Finally Answers Back").

Kandidat yang kalah (semua 106-114 karakter, kemiripan maks vs juara
0,24-0,32): C1 cahaya pinjaman Matahari (kuat, tapi twist "takes
credit" lebih abstrak, kalah cepat tawa dibanding adegan werewolf);
C3 janji purnama yang ghosting (dekat dengan sudut "takes two weeks
off" yang sudah ada di lapangan); C4 bola golf Apollo (spesifik,
tapi tahun 1969 salah -- golf Apollo 14 itu 1971 -- dan "tourists"
melemahkan suara reviewer); C5 HOA + werewolf (dua lelucon ditumpuk,
punchline "glowing" lebih lemah dari "smug").

Kemiripan terukur (SequenceMatcher autojunk=False): vs juara maks
0,299 (Laugh#1), rerata ~0,225 -- formula disalin, kata tidak
disalin. Akun 1 (@walta-exchange) belum submit saat build ini
(cek API submissions 26 Nov 14:5x WITA: tidak ada di 50 terbaru),
jadi teks Akun 1 belum bisa dibandingkan langsung; sudut werewolf
dipilih agar jelas berbeda dari tema pasang/terang yang umum.

Writes exactly one line to <MAKEFUN_OUTPUT_DIR>/entry.txt (default
/output). Pure stdlib. No network, no Pillow, no temp files.
"""

import hashlib
import os

ENTRY = "One star. Every full moon my neighbor turns into a werewolf and howls till dawn. The Moon just hangs there, smug."

EXPECTED_SHA256 = "8915d2ade592ce64c5b4608f2864e417da41b8bfb3b0b03e5bb3a4fc0e719c4c"
EXPECTED_BYTES = 113
EXPECTED_CHARS = 113


def build_entry():
    """Return the entry text, exactly as written by the builder."""
    return ENTRY


def validate_entry(text):
    """Check the entry: one line, 1-120 chars, no '!', sha256 matches."""
    if not isinstance(text, str):
        raise ValueError("entry must be str")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 120:
        raise ValueError(f"entry must be 1-120 chars, got {len(text)}")
    if "!" in text:
        raise ValueError("entry must not contain '!' (deadpan tone)")
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    if digest != EXPECTED_SHA256:
        raise ValueError(f"entry sha256 mismatch: {digest} != {EXPECTED_SHA256}")
    return digest


def write_entry():
    """Write the entry directly to <out_dir>/entry.txt (no temp files)."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = build_entry()
    validate_entry(text)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        raw = f.read()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED_SHA256:
        raise ValueError(f"written entry sha256 mismatch: {digest}")
    if len(raw) != EXPECTED_BYTES:
        raise ValueError(f"written entry must be {EXPECTED_BYTES} bytes, got {len(raw)}")
    return path


def main():
    path = write_entry()
    with open(path, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    print(f"wrote {path} sha256={digest} bytes={EXPECTED_BYTES} chars={EXPECTED_CHARS}")


if __name__ == "__main__":
    main()
