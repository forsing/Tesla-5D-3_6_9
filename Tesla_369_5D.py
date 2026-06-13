"""
SRBIN Nikola Tesla, za sva vremena, najveci naucnik sveta.

SERBIAN Nikola Tesla, for all time, the greatest scientist in the world.
"""



"""
Tesla 5D - senzorska konvergencija.

Nemam realan log senzora, pa pravim deterministicku simulaciju tih
kanala i od njih koherencioni omotac za 3-6-9 talas.
"""


import numpy as np

from Tesla_5_common import (
    MNOZIOCI,
    PIRAMIDA,
    ix_senzori,
    fokusni_omotac,
    normalizuj_signal,
    izvod_polja,
    ispisi_i_snimi_model,
)

OSNOVA = "tesla_369_5D"


def simuliraj_5d(nx):
    x = np.linspace(0.0, 1.0, nx)
    phase_error, hall, optical, temp = ix_senzori(x)

    mag_field = np.abs(hall)
    fazna_stabilnost = np.exp(-np.abs(phase_error) / 12.0)
    magnetni_doprinos = normalizuj_signal(mag_field) ** 2
    opticki_lock = np.exp(-np.abs(optical - 0.75) / 0.08)
    temp_stabilnost = np.exp(-np.abs(temp - np.mean(temp)) / 0.45)
    koherencija = 0.35 * fazna_stabilnost + 0.25 * magnetni_doprinos + 0.25 * opticki_lock + 0.15 * temp_stabilnost

    baza = np.zeros(nx)
    for m in MNOZIOCI:
        baza += np.sin(2.0 * np.pi * m * PIRAMIDA * x)

    s = normalizuj_signal(baza * fokusni_omotac(x, sigma=0.20) * koherencija)
    e_x = izvod_polja(x, s)
    detalji = {
        "izvor": "plot_scalar_sync.py",
        "kanali": "Phase_Error_deg, Mag_Field_T, Optical_V, Temp_C",
        "phase_error_abs_mean": f"{np.mean(np.abs(phase_error)):.6f}",
        "optical_mean": f"{np.mean(optical):.6f}",
        "temp_mean": f"{np.mean(temp):.6f}",
    }
    return x, s, e_x, detalji


def main():
    ispisi_i_snimi_model(
        OSNOVA,
        "Tesla Scalar - GRUPA 5D / senzorska konvergencija",
        simuliraj_5d,
        "Model pravi koherencioni omotac iz faznog, magnetnog, optickog i temperaturnog kanala.",
    )


if __name__ == "__main__":
    main()




"""
Tesla Scalar - GRUPA 5D / senzorska konvergencija
CSV: /data/loto7hh_4632_k47.csv| Izvlacenja: 4632 | tezine: talas=0.7 freq=0.3
max S: 1.0000000000 | max |E_x|: 908.2831582539

Brojevi po kombinovanom skoru (tezinski talas + frekvencija):
  26  skor=0.8835781825  freq=0.02680  (pojava=869)
   x  skor=0.7889655172  freq=0.02495  (pojava=809)
  37  skor=0.7701933096  freq=0.02652  (pojava=860)
   y  skor=0.7388062443  freq=0.02427  (pojava=787)
  13  skor=0.6699053646  freq=0.02554  (pojava=828)
   z  skor=0.6647153541  freq=0.02791  (pojava=905)
  35  skor=0.6627860589  freq=0.02600  (pojava=843)
   x  skor=0.6495391779  freq=0.02560  (pojava=830)
  05  skor=0.6376107262  freq=0.02554  (pojava=828)
   y  skor=0.6310974231  freq=0.02655  (pojava=861)
  09  skor=0.6003822057  freq=0.02600  (pojava=843)
   z  skor=0.5986461883  freq=0.02551  (pojava=827)
  08  skor=0.5688137213  freq=0.02810  (pojava=911)
   x  skor=0.5417288447  freq=0.02504  (pojava=812)
  38  skor=0.5267310874  freq=0.02597  (pojava=842)
   y  skor=0.5238633311  freq=0.02424  (pojava=786)
  22  skor=0.5176804093  freq=0.02625  (pojava=851)
   z  skor=0.5021307544  freq=0.02433  (pojava=789)
  12  skor=0.4936267198  freq=0.02498  (pojava=810)
  16  skor=0.4888650770  freq=0.02581  (pojava=837)
  18  skor=0.4867556307  freq=0.02532  (pojava=821)
  03  skor=0.4854452677  freq=0.02547  (pojava=826)
  02  skor=0.4831368285  freq=0.02544  (pojava=825)
  28  skor=0.4784811023  freq=0.02532  (pojava=821)
  10  skor=0.4469033007  freq=0.02606  (pojava=845)
  39  skor=0.4379546407  freq=0.02618  (pojava=849)
  33  skor=0.4372796473  freq=0.02634  (pojava=854)
  20  skor=0.4048844289  freq=0.02375  (pojava=770)
  01  skor=0.3798562486  freq=0.02430  (pojava=788)
  25  skor=0.3720417581  freq=0.02591  (pojava=840)
  29  skor=0.3690401215  freq=0.02618  (pojava=849)
  32  skor=0.3487801939  freq=0.02643  (pojava=857)
  06  skor=0.3410444180  freq=0.02517  (pojava=816)
  19  skor=0.3403868885  freq=0.02510  (pojava=814)
  24  skor=0.3401289933  freq=0.02591  (pojava=840)
  15  skor=0.3260815738  freq=0.02461  (pojava=798)
  34  skor=0.2972231793  freq=0.02692  (pojava=873)
  17  skor=0.1945662926  freq=0.02362  (pojava=766)
  07  skor=0.1613793103  freq=0.02603  (pojava=844)

Predlozene kombinacije (rangirane po skoru kombinacije):
  01. 05 x 12 y 31 z 38  skor_komb=4.2661065475
  02. 04 x 23 y 30 z 37  skor_komb=4.1883411388
  03. 09 x 11 y 27 z 37  skor_komb=3.9406330600
  04. 15 x 23 y 28 z 39  skor_komb=3.9292151083
  05. 02 x 14 y 23 z 38  skor_komb=3.8483108333
  06. 05 x 10 y 29 z 38  skor_komb=3.7300412627
  07. 04 x 13 y 27 z 38  skor_komb=3.6281205260
  08. 01 x 13 y 22 z 34  skor_komb=3.6087380808
  09. 06 x 13 y 22 z 31  skor_komb=3.2783238618
  10. 08 x 17 y 25 z 32  skor_komb=3.0584689060

Sacuvano: /Tesla/tesla_369_5D.txt
"""



"""
Analiza Tesla_369_5D.py
Tesla_369_5D.py je senzorska konvergencija. 
Pretvara četiri senzorska kanala u koherencioni omotač koji oblikuje 3-6-9 talas.

Glavni princip je koherencija na osnovu više senzorskih kanala.

Prate se četiri veličine kroz vreme:
Phase_Error_deg — fazna greška
Mag_Field_T — magnetno polje (hall)
Optical_V — optički napon
Temp_C — temperatura

„uspešna konvergencija” znači: mala fazna greška, stabilno magnetno polje, optika blizu radne tačke 0.75, i stabilna temperatura. 
5D upravo to modelira: tamo gde su svi kanali „mirni”, koherencija je visoka, pa je talas jak.

Ovo je fuzija senzora u jednu meru kvaliteta polja. 
Svaki kanal se pretvori u stabilnost preko eksponencijalne funkcije, 
pa se sve sabere u jedan koherencioni profil.

Funkcija simuliraj_5d(nx) prvo dobije četiri kanala iz ix_senzori(x).
Zatim svaki kanal pretvori u „stabilnost”:
fazna stabilnost = exp(-|phase_error| / 12)
magnetni doprinos = normalizuj(|hall|)²
optički lock = exp(-|optical - 0.75| / 0.08)
temperaturna stabilnost = exp(-|temp - prosek| / 0.45)

Pa ih spoji u jednu meru:
koherencija = 0.35·fazna + 0.25·magnetni + 0.25·opticki + 0.15·temperaturna

Napravi osnovni 3-6-9 talas (kao u 5), 
ali ga onda pomnoži fokusnim omotačem i koherencijom. 
Tamo gde su senzori stabilni, talas ostaje jak; gde nisu, talas se gasi.

Na kraju normalizuje S, računa E_x, i preda zajedničkom pipeline-u.

Fuzija senzora (sensor fusion)
Četiri kanala se kombinuju u jednu meru koherencije, 
sa težinama 0.35 / 0.25 / 0.25 / 0.15.

Eksponencijalna stabilnost
Svaki kanal se preko exp(-|odstupanje|/skala) pretvara u vrednost između 0 i 1. 
Manje odstupanje = veća stabilnost.

Optička radna tačka 0.75
Optika je idealna na 0.75. Odstupanje od te vrednosti smanjuje koherenciju.

Koherencija kao omotač
Za razliku od 5A/5C gde je oblik talasa geometrijski, ovde oblik dolazi iz „kvaliteta senzora”.

Osnovni 3-6-9 nosilac
Sam talas je ravnopravan zbir 3+6+9 (kao 5), a senzori samo moduliraju njegovu jačinu.

Zajednički pipeline
Skor, frekvencija, kombinacije i slike kroz Tesla_5_common.py.

5D pokriva senzorsku/merljivu stranu konvergencije:

5 + 5A + 5B + 5C + 5D + 5E -> Tesla_5final.py

Dok 5B koristi senzore za faznu korekciju, 5D koristi senzore za jačinu/koherenciju talasa. 
To su dva različita načina upotrebe istih senzorskih kanala. 
U txt se vide i kontrolni podaci: phase_error_abs_mean: 6.36, optical_mean: 0.75, temp_mean: 24.0.


Top 10 za 5D:
26, x, 37, y, 13, z, 35, x, 05, 11

Predlozene kombinacije (rangirane po skoru kombinacije):
  01. 05 x 12 y 31 z 38  skor_komb=4.2661065475

Vrh 26 je isti kao kod većine modela, 
ali se 14 ovde penje na drugo mesto, 
a jako su rangirani 13, 05, 11. 
Pošto 5D koristi isti osnovni 3-6-9 nosilac kao 5, 
rezultat je sličniji modelu 5 nego 5C 
— ali ga koherencioni omotač ipak pomera dovoljno da bude koristan, nezavisan glas u 5final.
"""



"""
source ~/tesla_env/bin/activate

Bitne verzije za tesla_env:

Paket	Verzija
python  3.11.13
numpy   2.2.6
scipy   1.15.3
pandas  3.0.3
matplotlib    3.10.9
k-Wave-python 0.6.2
pycharge      2.0.1
jax        0.10.1
jaxlib     0.10.1
jaxtyping  0.3.7
equinox    0.13.8
lineax     0.1.1
optimistix 0.1.0
ml-dtypes
(uz jax)
opencv-python 4.13.0.92
h5py          3.16.0
"""
