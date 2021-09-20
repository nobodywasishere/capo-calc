#!/usr/bin/env python

import sys

# All chords supported
# Must be grouped together in 12, in order
chords = [ 
    'C',  'Db',  'D',  'Eb',  'E',  'F',  'Gb',  'G',  'Ab',  'A',  'Bb',  'B', 
    'Cm', 'Dbm', 'Dm', 'Ebm', 'Em', 'Fm', 'Gbm', 'Gm', 'Abm', 'Am', 'Bbm', 'Bm', 
    'C7', 'Db7', 'D7', 'Eb7', 'E7', 'F7', 'Gb7', 'G7', 'Ab7', 'A7', 'Bb7', 'B7'
]

# The higher the weight the less easy it is to play
chord_weights = {
    0: [ 
        'C', 'D', 'E', 'G', 'A', 
        'Dm', 'Em', 'Am', 
        'C7', 'D7', 'E7', 'G7', 'A7', 'B7' 
    ],
    1: [ 
        'F',  'Bb', 
        'Fm', 'Bbm',
        'F7', 'Bb7' 
    ],
    2: [ 'Gb', 'Gbm', 'Gb7', 'B', 'Bm' ],
    3: [ 'Gm', 'Cm' ],
    6: [ 'Ab', 'Abm', 'Ab7', 'Db', 'Dbm', 'Db7' ],
    9: [ 'Eb', 'Ebm', 'Eb7' ]
}

if __name__=="__main__":
    input_chords = sys.argv[1:]

    capo_outputs = []

    # Find the chords for each capo position
    for pos in range(0, 12):
        capo = []
        for chord in input_chords:
            try:
                chord_index = chords.index(chord)
            except:
                print(f'{chord} is not a chord')
                exit(1)
            chord_ord   = int(chord_index / 12)
            chord_pos   = chord_index % 12 
            capo.append(chords[chord_ord * 12 + (chord_index - pos) % 12])
        capo_outputs.append(capo)

    capo_scores = []

    # Score each capo position
    for pos in range(0, 12):
        score = 0
        for chord in capo_outputs[pos]:
            for key in chord_weights:
                if chord in chord_weights[key]:
                    score += key
                    continue
        capo_scores.append([score, pos, capo_outputs[pos]])

    # Sort all the capo positions by score
    capo_scores.sort(key=lambda x: x[0])

    # Print out the lowest three scores
    print(f'Input:   {", ".join(input_chords)}')
    for score in capo_scores[:3]:
        print(f'Capo {score[1]:2d}: {", ".join(score[2])}')

