# Uvod v Operacijski Sistem Linux

## Osnovne Funkcionalnosti Operacijskih Sistemov

- **Upravljanje s procesi** (ang. process management)
- **Upravljanje z napravami** (ang. device management)
- **Upravljanje s pomnilnikom** (ang. memory management)
- **Upravljanje z zbirčnimi sistemi** (ang. file management)
- **Upravljanje z omrežjem** (ang. network management)

---

## Vsebina

1. **Predmet Operacijski Sistemi**
2. **Uvod v Operacijske Sisteme**
3. **Operacijski Sistem Linux**
   - Pregled operacijskega sistema Linux
   - Linux jedro
   - Linux distribucije
   - Linux vmesnik ukazne vrstice

---

## Uvod v Operacijski Sistem Linux

- Linux je varianta operacijskega sistema UNIX.
- UNIX je eden najstarejših operacijskih sistemov, znan po zanesljivosti in varnosti (od leta 1969).
- UNIX je bil razvit za delo s terminali in je zasnovan za delo v omrežjih.
- Veliko strežnikov po svetu (npr. YouTube, Google) uporablja različice sistema UNIX.
- Linux je odprtokodna in brezplačna sistemska programska oprema.

---

## Zgodovinski Razvoj Linuxa
- **Linus Torvalds** je razvil prvo verzijo Linuxa (0.01) leta 1991.
  - Temelji na idejah iz sistema MINIX (UNIX sistem).
  - Monolitski sistem z 9300 vrsticami kode v C-ju in 950 vrsticami v asemblerju.
- **Linux 1.0 (1994)**:
  - 165,000 vrstic kode v C-ju.
  - Novi zbirčni sistem, TCP/IP protokoli, gonilniki.
- **Linux 2.0 (1996)**:
  - 470,000 vrstic kode v C-ju.
  - Podpora 64-bitnih arhitektur, simetrično multiprogramiranje, novi omrežni protokoli.

---

## Linux Jedro (ang. Linux Kernel)

- Jedro Linuxa je nadzornik operacijskega sistema.
- Odgovorno za dodeljevanje pomnilnika in procesorskega časa.
- Verzija jedra je označena kot **A.B.C-D**:
  - **A**: Glavna verzija.
  - **B**: Velika sprememba (ang. major revision).
  - **C**: Mala sprememba (ang. minor revision).
  - **D**: Popravki hroščev ali varnostni popravki (ang. bug fix/security patch).

---

## Linux Distribucije

- Linux distribucija je operacijski sistem, zgrajen na osnovi Linux jedra in sistema za upravljanje s paketi.
- Trenutno obstaja več kot 600 distribucij (300 v aktivnem razvoju).
- **Popularne distribucije**:
  - **Debian**: Nekomercialna distribucija, vzdrževana s strani prostovoljcev.
  - **Ubuntu**: Popularna namizna in strežniška distribucija, izhaja iz Debiana.
  - **Fedora**: Distribucija, sponzorirana od podjetja Red Hat.
  - **Arch**: Namenjena zahtevnejšim uporabnikom.

---

## Terminal

- Terminal je vmesnik ukazne vrstice, ki omogoča interakcijo z operacijskim sistemom.

---

## Pregledovalniki in Urejevalniki Tekstov v Linuxu

- **Vim**:
  - Urejevalnik v ukazni vrstici.
  - Ni prijazen za začetnike, a zelo priljubljen med naprednimi uporabniki.
  - [Tutorial](ftp://ftp.vim.org/pub/vim/doc/book/vimbook-OPL.pdf)
- **Emacs**:
  - Urejevalnik z grafičnim in ukaznim vmesnikom.
  - Izjemno kompleksen in prilagodljiv.
  - [Tutorial](https://www.gnu.org/software/emacs/)
- **Nano**:
  - Urejevalnik v ukazni vrstici, prijazen za začetnike.
  - [Tutorial](http://goo.gl/efkYSa)
- **Gedit** (GNOME Text Editor):
  - Urejevalnik v grafičnem okolju.
  - [Tutorial](https://help.gnome.org/users/gedit/stable/)

---

## Dodatno

- Oglejte si predlagane urejevalnike in izberite tistega, ki vam najbolj ustreza.