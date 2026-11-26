#!/usr/bin/env python3
"""The Moon Gets One Star -- entry builder (Akun 2, @wantorieta15).

REVISI (26 Nov 2026, reviser; builder HEAD 767dd41). Keputusan: PERTAHANKAN
teks builder -- tidak ada kandidat pengganti yang jelas lebih kuat.

Teks final (113 karakter, satu baris, tanpa newline di akhir):
"One star. Every full moon my neighbor turns into a werewolf and howls
till dawn. The Moon just hangs there, smug."

Kenapa dipertahankan (formula pemenang rank 1-2 keluarga satu-baris):
- Laugh Sprint #1 (777.695): satu adegan konkret + sensorik, twist di
  fragmen akhir ("like a raccoon with a mortgage").
- Laugh Sprint #2 (776.452): setup satu adegan, twist membalik setup.
- Zero Use #1 (779.634): absurd + batasan spesifik, ditutup item paling
  memalukan ("at my own wedding").
- Zero Use #2 (725.027): setup singkat + twist "sudah terpakai".
Formula juara: SATU adegan konkret + satu keluhan spesifik + punchline
di kata-kata terakhir, nada deadpan, tanpa "!". Teks ini memenuhi
ketiganya: adegan tunggal (tetangga jadi werewolf tiap purnama, melolong
sampai subuh) + keluhan yang HANYA bisa ditujukan ke Bulan (tanpa Bulan,
tidak ada werewolf) + punchline di kata terakhir ("smug").

Kandidat pengganti yang ditimbang reviser dan DITOLAK:
- "It turns my neighbor into a werewolf once a month and never once
  apologized for the howling." -- punchline "never once apologized"
  bagus, tapi "It" ambigu (Bulan baru jelas di kalimat kedua builder)
  dan adegannya kurang hidup dibanding "howls till dawn".
- "Full moon again, my neighbor is a werewolf howling till dawn, and
  the Moon acts like it did nothing." -- punchline "acts like it did
  nothing" kalah tajam dari satu kata "smug"; ritme juga lebih datar.
- Sudut pasang surut / cahaya pinjaman / kawah-keju: DITOLAK -- pasang
  dipakai Akun 1 di bounty ini; kawah/keju/terang dihukum juri sebagai
  lelucon obvious; cahaya pinjaman twist-nya lebih abstrak.
Jadi tidak ada pengganti yang JELAS lebih kuat -- teks builder bertahan.

Beda dari Akun 1 (WAJIB: dua akun tidak boleh sama):
Akun 1 (@walta-exchange, submission 01a216ab-4dbe-773e-a7ba-9354b5600e2d,
106 karakter): "One star. It pulls the tides, ruins my sleep, then
vanishes for a week every month like I wouldn't notice."
Sudut Akun 1 = pasang + insomnia + Bulan menghilang; sudut Akun 2 =
werewolf tetangga + Bulan yang smug menonton. Kemiripan
SequenceMatcher (autojunk=False) Akun 2 vs Akun 1 = 0,2192 (rendah,
hanya berbagi pembuka "One star." + struktur review). Guard di
validate_entry() menolak bila teks sama persis dengan teks Akun 1.

Kemiripan vs pemenang (SequenceMatcher, autojunk=False; diukur builder
dari teks juara via API make.fun, tetap berlaku karena teks tidak
berubah): maks 0,299 (vs Laugh Sprint #1), rerata ~0,225 -- formula
disalin, kata tidak disalin.

Anchor: makefun anchor drand round 34291009. Wallet Akun 2:
adbmHyC8x5ZRYrQFBSi9uuaXpFRVs4CQQBsoEY5zGzk (terverifikasi di
.makefun/freshness.json sebelum revisi ditulis).

Writes exactly one line to <MAKEFUN_OUTPUT_DIR>/entry.txt (default
/output). Pure stdlib. No network, no Pillow, no temp files.
"""

import hashlib
import os

ENTRY = "One star. Every full moon my neighbor turns into a werewolf and howls till dawn. The Moon just hangs there, smug."

A1_ENTRY = "One star. It pulls the tides, ruins my sleep, then vanishes for a week every month like I wouldn't notice."

EXPECTED_SHA256 = "8915d2ade592ce64c5b4608f2864e417da41b8bfb3b0b03e5bb3a4fc0e719c4c"
EXPECTED_BYTES = 113
EXPECTED_CHARS = 113


def build_entry():
    """Return the entry text, exactly as written (kept from builder)."""
    return ENTRY


def validate_entry(text):
    """Check the entry: one line, 1-120 chars, no '!', not Akun 1's text, sha256 matches."""
    if not isinstance(text, str):
        raise ValueError("entry must be str")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 120:
        raise ValueError(f"entry must be 1-120 chars, got {len(text)}")
    if "!" in text:
        raise ValueError("entry must not contain '!' (deadpan tone)")
    if text == A1_ENTRY:
        raise ValueError("entry must differ from Akun 1 entry")
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
