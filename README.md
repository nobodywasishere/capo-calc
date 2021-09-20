# capo-calc

Inspired by https://deftdigits.com/tools/capo-calculator/.

This tool takes in a set of chords and returns possible capo positions for a guitar to play those chords. This is useful for working around troublesome chords or if you're transcribing.

Simply run the script and pass in the chords:
```
$ ./capo_calc.py A Bm C

Input:   A, Bm, C
Capo  2: G, Am, Bb
Capo  7: D, Em, F
Capo  0: A, Bm, C
```

Currently supports the following chords (possibly more to come):

|    |     |    |     |    |    |     |    |     |    |     |    | 
|----|-----|----|-----|----|----|-----|----|-----|----|-----|----|
| C  | Db  | D  | Eb  | E  | F  | Gb  | G  | Ab  | A  | Bb  | B  |
| Cm | Dbm | Dm | Ebm | Em | Fm | Gbm | Gm | Abm | Am | Bbm | Bm |
| C7 | Db7 | D7 | Eb7 | E7 | F7 | Gb7 | G7 | Ab7 | A7 | Bb7 | B7 |