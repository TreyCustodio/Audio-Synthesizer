from audio import *
from instruments import *

"""
Following the audio module's framework,
this module contains everything relevant to
the production of hip hop beats.
Please enjoy.

Author - Trey Custodio
2/27/2025"""

        


#   Set the tempo
BPM = 160
BPS = BPM / 60
NOTE = 1/BPS

#   Note lengths
SIXTEENTH = NOTE / 4
EIGHTH = NOTE / 2
QUARTER = NOTE
HALF = NOTE * 2
TREY = NOTE * 3
WHOLE = NOTE * 4


def dreamy():
    """Intro Plucks"""
    #   (1) Define the Notes
    notes = Pluck(4, WHOLE)
    
    #   (2) Craft the Measures
    m1 = build_measure(rest(QUARTER),
                       notes.s_d, notes.s_e, notes.e_g,
                        notes.e_a, notes.e_a,
                        notes.e_a, rest(EIGHTH)
                       )
    


    m2 = build_measure(notes.s_a, notes.s_a, notes.s_a, notes.s_b, # 1
                       rest(EIGHTH), # 1.5
                       notes.s_a, notes.s_a, notes.s_a, notes.s_b, # 2.5
                       rest(EIGHTH), # 3
                       notes.s_a, notes.s_a, notes.e_a # 4
                        )
    




    
    #   (3) Combine the Measures
    return build_measure(m1, m2 * 0.8)

def dreamy_2():
    """Unused / Deprecated"""
    #   (1) Define the Notes
    notes = Dreamy(4, WHOLE)
    
    #   (2) Craft the Measures
    m1 = build_measure(rest(QUARTER), # 1
                       notes.s_a, notes.s_a, notes.s_a, notes.s_b, # 2
                       rest(EIGHTH), # 2.5
                       notes.s_a, notes.s_a, notes.s_a, notes.s_b, # 3.5
                       rest(EIGHTH), # 4
                        )
    
    m2 = build_measure(rest(HALF), # 2
                       notes.s_a, notes.s_a, notes.e_a, # 3
                       rest(QUARTER)
                       )

    m3 = build_measure(rest(TREY),
                       notes.s_a, notes.s_a, notes.e_a,
                       )
    
    m4 = build_measure(rest(HALF),
                       notes.q_b,
                       rest(QUARTER))
    
    #   (3) Combine the Measures
    return build_measure(m1, m2, m3 * 0.6, m4 * 0.6)

def dreamy_3():
    """End of 4th measure"""
    snares = Pluck(4, WHOLE)
    dreams = Pluck(4, WHOLE)

    #snares = Dreamy(4, WHOLE)
    #   (2) Create the Measures

    #   Measure 1
    m1 = build_measure(snares.q_a, # 1 / 4
                       
                       snares.s_f,
                       snares.s_f,
                       snares.e_f, # 2 / 4

                       snares.q_a # 3 / 4

                       )
    

    #   Measure 2
    m2 = build_measure(snares.e_e, # 3.5 / 8
                       snares.q_a, # 4.5 / 8

                       snares.e_e, # 5 / 8
                       snares.q_a, # 6 / 8

                       snares.e_e,
                       rest(EIGHTH), # 7 / 8
                       )

    #   Measure 3
    m3 = build_measure(snares.q_a,
                       
                       snares.s_f, snares.s_f, snares.e_g,

                       snares.q_a,

                       snares.e_f,
                       snares.e_f
                       )

    #   Measure 4
    m4 = build_measure(snares.e_e, # 0.5 / 4
                       snares.q_a, # 1.5 / 4

                       snares.e_e, # 2 / 4
                       snares.q_a, # 3 / 4

                       snares.e_e, # 3.5 / 4
                       snares.e_e, # 4 / 4

                       )

    #   Measure 5
    m5 = build_measure(snares.q_a, # 1 / 4
                       snares.q_g, # 2 / 4

                       # These lines could be a different instrument
                       dreams.s_a, dreams.s_a, dreams.s_a, dreams.s_b, # 3 / 4
                       rest(EIGHTH), # 3.5 / 4
                       dreams.s_a, dreams.s_a, dreams.s_a, dreams.s_b, # 4.5
                       rest(EIGHTH), # 5 / 4
                       
                       )
    
    #   Measure 6
    m6 = build_measure(
                       snares.q_f,
                       snares.q_a,
                       dreams.s_a, dreams.s_a, dreams.e_a,
                       )
    
    #   Measure 7
    m7 = build_measure(
                       snares.e_e, snares.e_e, # 1 / 4
                       snares.e_c, # 1.5 / 4
                       snares.q_a, # 2.5 / 4
                       snares.e_c, # 3 / 4
                       snares.q_a # 4 / 4
                       )
    
    #   Measure 8
    m8 = build_measure(
                       snares.s_a, snares.s_a, snares.e_g, # 1 / 4
                       snares.q_a, # 2 / 4
                       snares.q_a, # 3 / 4
                       snares.s_a, snares.s_a, snares.e_g, # 4 / 4
                        )

    #   (3) Combine the measures

    return build_measure(m1, m2, m3, m4, m5, m6, m7, m8)

def dreamy_4():
    """Loop for verse 1"""
    snares = Pluck(4, WHOLE)

    #   (2) Create the Measures

    #   Measure 1
    m1 = build_measure(snares.q_a, # 1 / 4
                       
                       snares.s_f,
                       snares.s_f,
                       snares.e_f, # 2 / 4

                       snares.q_a # 3 / 4

                       )
    

    #   Measure 2
    m2 = build_measure(snares.e_e, # 3.5 / 8
                       snares.q_a, # 4.5 / 8

                       snares.e_e, # 5 / 8
                       snares.q_a, # 6 / 8

                       snares.e_e,
                       rest(EIGHTH), # 7 / 8
                       )

    #   Measure 3
    m3 = build_measure(snares.q_a, # 8
                       
                       snares.s_f, snares.s_f, snares.e_g, # 9

                       snares.q_a, # 10

                       snares.e_f,
                       snares.e_f # 11
                       )

    #   Measure 4
    m4 = build_measure(snares.e_e, # 11.5
                       snares.q_a, # 12.5

                       snares.e_e, # 13
                       snares.q_a, # 14

                       snares.e_e, # 
                       snares.e_e, # 15

                       )

    #   Measure 5
    m5 = build_measure(snares.q_a, # 16
                       )
    
    return build_measure(m1, m2, m3, m4, m5)

def dreamy_5():
    """2 1/16 notes leading into verse 2"""
    notes = Pluck(4, WHOLE)
    
    m1 = build_measure(notes.e_g, notes.e_f)
    return add_waves(rest(WHOLE + TREY), m1)

def dreamy_6():
    """Loop for verse 2"""
    snares = Pluck(4, WHOLE)

    
    #   Measure 6
    m6 = build_measure(snares.q_a, # 1 / 4
                       
                       snares.s_e,
                       snares.s_e,
                       snares.e_e, # 2 / 4

                       snares.q_b # 3 / 4

                       )
    

    #   Measure 7
    m7 = build_measure(snares.e_d, # 3.5 / 8
                       snares.q_b, # 4.5 / 8

                       snares.e_d, # 5 / 8
                       snares.q_b, # 6 / 8

                       snares.e_d,
                       rest(EIGHTH), # 7 / 8
                       )

    #   Measure 8
    m8 = build_measure(#snares.q_b,
                       rest(SIXTEENTH * 2),
                       rest(EIGHTH),
                       snares.s_e, snares.s_e, snares.e_f,

                       snares.q_b,

                       snares.e_e,
                       snares.e_e
                       )

    #   Measure 9
    m9 = build_measure(snares.e_d, # 0.5 / 4
                       snares.q_b, # 1.5 / 4

                       snares.e_d, # 2 / 4
                       snares.q_b, # 3 / 4

                       snares.e_d, # 3.5 / 4
                       snares.e_d, # 4 / 4

                       )

    #   Measure 10
    m10 = build_measure(snares.q_a, # 1 / 4
                       )
    
    
    return build_measure(
                         m6, m7, m8, m9, m10
                         )

def dreamy_7():
    n = Pluck(4, WHOLE)

    m1 = build_measure(
        n.e_a, n.e_a, # 1
        n.e_g, # 1.5
        n.q_f, # 2.5
        n.e_f, n.e_f, # 3.5
        n.q_e, # 4.5
        n.q_e, # 5.5
        n.s_e, n.s_f, n.e_e, # 6.5
        n.e_d, # 7
        n.e_c, n.e_d # 8
    )

    m2 = build_measure(
        n.e_a, n.e_a, # 1
        n.e_g, # 1.5
        n.q_f, # 2.5

        n.s_g, n.s_f, n.s_e, n.s_f,
        #n.e_f, n.e_f, # 3.5

        n.q_e, # 4.5
        n.q_e, # 5.5
        n.s_e, n.s_f, n.e_e, # 6.5
        n.e_d, # 7
        n.q_d # 8
    )
    
    return build_measure(m1, m2)

def dreamy_8():
    """The first iteration of plucks with a pause in the middle"""
    snares = Pluck(4, WHOLE)

    #   (2) Create the Measures

    #   Measure 1
    m1 = build_measure(snares.q_a, # 1 / 4
                       
                       snares.s_f,
                       snares.s_f,
                       snares.e_f, # 2 / 4

                       snares.q_a # 3 / 4

                       )
    

    #   Measure 2
    m2 = build_measure(snares.e_e, # 3.5 / 8
                       snares.q_a, # 4.5 / 8

                       snares.e_e, # 5 / 8
                       snares.q_a, # 6 / 8

                       snares.e_e,
                       rest(EIGHTH), # 7 / 8
                       )

    #   Measure 3
    m3 = build_measure(#snares.q_a, # 8
                       rest(SIXTEENTH * 2),
                       rest(EIGHTH),
                       snares.s_f, snares.s_f, snares.e_g, # 9

                       snares.q_a, # 10

                       snares.e_f,
                       snares.e_f # 11
                       )

    #   Measure 4
    m4 = build_measure(snares.e_e, # 11.5
                       snares.q_a, # 12.5

                       snares.e_e, # 13
                       snares.q_a, # 14

                       snares.e_e, # 
                       snares.e_e, # 15

                       )

    #   Measure 5
    m5 = build_measure(snares.q_a, # 16
                       )
    
    return build_measure(m1, m2, m3, m4, m5)

def strings_1():
    #   (1) Get each note
    bas = Bass(3, WHOLE)

    #   (2) Create Each Measure

    #   Measure 1
    m1 = build_measure(bas.q_c,
                       bas.q_c,
                       bas.e_d,bas.e_c,
                       rest(QUARTER))

    m2 = build_measure(rest(EIGHTH), bas.e_c,
                       bas.e_e, bas.e_c,
                       bas.e_c,
                       bas.q_d, rest(EIGHTH)
                       )
    
    m3 = build_measure(bas.e_e, bas.e_d, 
                       bas.e_c, rest(EIGHTH),
                       bas.e_c, rest(EIGHTH),
                       bas.e_d, bas.e_c)
    
    m4 = rest(WHOLE)

    #   (3) Final effects and return
    return build_measure(m1, m2, m3, m4)


def strings_chorus():
    #   (1) Create the notes
    plucks = Pluck(4, WHOLE)


    #   (2) Create the measures

    #   Measure 1
    m1 = build_measure(plucks.s_a, plucks.s_g, plucks.e_g, 
                       plucks.q_f,
                       plucks.e_g, plucks.e_g,
                       plucks.e_g, plucks.e_a
                       )
    
    

    #   Measure 2
    m2 = build_measure(rest(QUARTER),
                       plucks.e_g, plucks.e_g,
                       plucks.e_g, plucks.e_a,
                       plucks.e_g, plucks.e_g
                       )


    #   Measure 3
    m3 = build_measure(plucks.e_g, plucks.e_a, 
                       rest(QUARTER), 
                       plucks.q_f, 
                       plucks.q_f
                       )

    
    #   Measure 4
    m4 = build_measure(plucks.s_g, plucks.s_a, plucks.e_g, 
                       plucks.s_g, plucks.s_g, plucks.e_g, 
                       plucks.e_g, plucks.e_a,
                       plucks.e_g, plucks.e_a
                       )


    #   Measure 5
    m5 = build_measure(rest(QUARTER),
                       plucks.s_g, plucks.s_a, plucks.e_g,
                       plucks.e_g, plucks.e_g,
                       plucks.q_a
                       )
    

    #   Measure 6
    m6 = build_measure(plucks.e_f, plucks.e_f,
                       plucks.e_g, plucks.s_g, plucks.s_g,
                       plucks.s_g, plucks.s_g, plucks.s_a, plucks.s_a,
                       rest(QUARTER))
    
   

    #   Measure 7
    m7 = build_measure(plucks.s_e, plucks.s_c, plucks.s_a, plucks.s_g,
                       plucks.e_g, plucks.s_a, plucks.s_g,
                       plucks.s_e, plucks.s_e, plucks.s_a, rest(SIXTEENTH),
                       rest(QUARTER))

    

    #   Measure 8
    m8 = rest(WHOLE)


    #   (3) Combine the measures
    combined = build_measure(m1, m2, m3, m4, m5, m6, m7, m8)
    return combined

def bass():
    n = Bass(3, WHOLE)

    m1 = build_measure(n.q_a,
                       n.q_a,
                       n.q_a,
                       n.q_a
                       )
    
    return build_measure(m1, m1, m1, m1) * 0.2

def symbol():
    notes = Symbol(2, WHOLE)

    m1 = build_measure(notes.q_a,
                       rest(QUARTER),
                       #notes.q_a,
                       notes.q_a,
                       rest(QUARTER),
                       #notes.q_a
                       )
    
    group = build_measure(m1, m1, m1, m1)
    rests = build_measure(rest(WHOLE), rest(WHOLE), rest(WHOLE), rest(WHOLE), rest(QUARTER * 8))

    
    return  build_measure(group, group, group,
                          rests,
                          )* 0.3

def symbol_loop():
    notes = Symbol(2, WHOLE)

    m1 = build_measure(notes.q_a,
                       notes.q_a,
                       notes.q_a,
                       notes.q_a
                       )
    
    group = build_measure(m1, m1, m1, m1)

    return group * 0.3

def skirts_loop():
    n = Skirt(3, WHOLE)
    
    m1 = build_measure(n.e_a,
                       n.e_a,
                       n.e_a,
                       n.e_a,
                       n.e_a,
                       n.e_a,
                       n.e_a,
                       n.e_a,)
    
    m2 = build_measure(n.e_a,
                       n.e_a,
                       n.e_a,
                       n.e_a,
                       n.e_a,
                       n.e_a,
                       n.e_b,
                       rest(EIGHTH),
    )

    m3 = build_measure(n.e_a,
                       n.s_g, n.s_g, n.e_f, # 1.5
                       n.e_a,
                       n.s_g, n.s_g, n.e_f, # 3
                       n.e_a, n.e_a, n.e_a, n.e_a # 4

    )

    m4 = build_measure(n.e_a, n.e_a, # 1
                       n.e_a, n.e_a, 
                       n.e_b, # 2.5
                       rest(EIGHTH)

                       
                       )
    
    final = build_measure(m1, m2, m3, m4) * 0.1
    final = build_measure(final, final, final, final, final)

    return final

def skirts_single():
    n = Skirt(3, WHOLE)
    
    m1 = build_measure(n.e_a,
                       n.e_a,
                       n.e_a,
                       n.e_a,
                       n.e_a,
                       n.e_a,
                       n.e_a,
                       n.e_a,)
    
    m2 = build_measure(n.e_a,
                       n.e_a,
                       n.e_a,
                       n.e_a,
                       n.e_a,
                       n.e_a,
                       n.e_b,
                       rest(EIGHTH),
    )

    m3 = build_measure(n.e_a,
                       n.s_g, n.s_g, n.e_f, # 1.5
                       n.e_a,
                       n.s_g, n.s_g, n.e_f, # 3
                       n.e_a, n.e_a, n.e_a, n.e_a # 4

    )

    m4 = build_measure(n.e_a, n.e_a, # 1
                       n.e_a, n.e_a, 
                       n.e_b, # 2.5
                       rest(EIGHTH)

                       
                       )
    
    final = build_measure(m1, m2, m3, m4) * 0.1
    return final
    
def drums_1():

    #   (1) Create the Notes
    snares = Snare(3, WHOLE)


    #   (2) Create the Measures

    #   Measure 1
    m1 = build_measure(snares.q_a, # 1
                       
                       snares.s_f,
                       snares.s_f,
                       snares.e_f, # 2

                       snares.q_a) # 3
    

    #   Measure 2
    m2 = build_measure(snares.e_e, 
                       snares.q_a, # 4.5

                       snares.e_e, # 5
                       snares.q_a, # 6

                       snares.e_e, # 6.5
                       rest(EIGHTH), # 7
                       )

    #   Measure 3
    m3 = build_measure(snares.q_a,
                       
                       snares.s_f, snares.s_f, snares.e_g,

                       snares.q_a,

                       snares.e_f,
                       snares.e_f
                       )

    #   Measure 4
    m4 = build_measure(snares.e_e, # 0.5 / 4
                       snares.q_a, # 1.5 / 4

                       snares.e_e, # 2 / 4
                       snares.q_a, # 3 / 4

                       snares.e_e, # 3.5 / 4
                       snares.e_e, # 4 / 4

                       )

    #   Measure 5
    m5 = build_measure(snares.q_a, # 1 / 4
                       snares.q_g, # 2 / 4
                       rest(HALF)
                       
                       )
    
    #   Measure 6
    m6 = build_measure(rest(QUARTER),
                       snares.q_f,
                       snares.q_a,
                       rest(QUARTER))
    
    #   Measure 7
    m7 = build_measure(
                       snares.e_e, snares.e_e, # 1 / 4
                       snares.e_c, # 1.5 / 4
                       snares.q_a, # 2.5 / 4
                       snares.e_c, # 3 / 4
                       snares.q_a # 4 / 4
                       )
    
    #   Measure 8
    m8 = build_measure(
                       snares.s_a, snares.s_a, snares.e_g, # 1 / 4
                       snares.q_a, # 2 / 4
                       snares.q_a, # 3 / 4
                       snares.s_a, snares.s_a, snares.e_g, # 4 / 4
                        )

    #   (3) Combine the measures

    return build_measure(m1, m2, m3, m4, m5, m6, m7, m8) * 0.8

def drums_2():
    """Intro drums"""
    #   (1) Create the Notes
    snares = Snare(3, WHOLE)

    #   (2) Create the measures
    m1 = build_measure(snares.q_g, 
                       rest(TREY))
    
    m2 = build_measure(
                       snares.q_f,
                       snares.q_a,
                       snares.q_a,
                       snares.q_a,
                       #rest(QUARTER)
                       )
    
    m3 = build_measure(snares.e_e, snares.e_e, # 1 / 4
                       snares.e_c, # 1.5 / 4
                       snares.q_a, # 2.5 / 4
                       snares.e_c, # 3 / 4
                       snares.q_a
                       )
    
    m4 = build_measure(snares.s_a, snares.s_a, snares.e_g, # 1 / 4
                       snares.q_a, # 2 /4
                       snares.q_a, # 3 /4
                       snares.s_a, snares.s_a, snares.e_g,
                        )
    
    #   (3) Combine the measures
    return build_measure(m1, m2, m3, m4) * 0.8


def drums_3():
    """Main loop of the drums"""
    #   (1) Create the Notes
    snares = Snare(3, WHOLE)


    #   (2) Create the Measures

    #   Measure 1
    m1 = build_measure(snares.q_a,
                       
                       snares.s_f,
                       snares.s_f,
                       snares.e_f,

                       snares.q_a)
    

    #   Measure 2
    m2 = build_measure(snares.e_e, 
                       snares.q_a,

                       snares.e_e,
                       snares.q_a,

                       snares.e_e,
                       rest(EIGHTH),
                       )

    #   Measure 3
    m3 = build_measure(snares.q_a,
                       
                       snares.s_f, snares.s_f, snares.e_g,

                       snares.q_a,

                       snares.e_f,
                       snares.e_f
                       )

    #   Measure 4
    m4 = build_measure(snares.e_e, # 0.5 / 4
                       snares.q_a, # 1.5 / 4

                       snares.e_e, # 2 / 4
                       snares.q_a, # 3 / 4

                       snares.e_e, # 3.5 / 4
                       snares.e_e, # 4 / 4

                       )

    #   Measure 5
    m5 = build_measure(snares.q_a, # 1 / 4
                    #    snares.q_g, # 2 / 4
                    #    rest(HALF)
                       
                       )
    
    return build_measure(m1, m2, m3, m4, m5) * 0.8

def drums_4():
    """Solo section at end of each verse"""
    #   (1) Create the Notes
    snares = Snare(3, WHOLE)


    #   (2) Create the Measures

    #   Measure 1
    m1 = build_measure(snares.q_a, # 1
                       
                       snares.s_f,
                       snares.s_f,
                       snares.e_f, # 2

                       snares.q_a) # 3
    

    #   Measure 2
    m2 = build_measure(snares.e_e, # 3.5
                       snares.q_a, # 4.5

                       snares.e_e, # 5
                       snares.q_a, # 6

                       snares.e_e, # 6.5
                       rest(QUARTER + EIGHTH),

                       )


    return build_measure(m1, m2)

def drums_5():
    """The first iteration of the drums with a pause in the middle"""
    #   (1) Create the Notes
    snares = Snare(3, WHOLE)


    #   (2) Create the Measures

    #   Measure 1
    m1 = build_measure(snares.q_a,
                       
                       snares.s_f,
                       snares.s_f,
                       snares.e_f,

                       snares.q_a)
    

    #   Measure 2
    m2 = build_measure(snares.e_e, 
                       snares.q_a,

                       snares.e_e,
                       snares.q_a,

                       snares.e_e,
                       rest(EIGHTH),
                       )

    #   Measure 3
    m3 = build_measure(rest(SIXTEENTH * 2),
                       rest(EIGHTH),
                       snares.s_f, snares.s_f, snares.e_g,

                       snares.q_a,

                       snares.e_f,
                       snares.e_f
                       )

    #   Measure 4
    m4 = build_measure(snares.e_e, # 0.5 / 4
                       snares.q_a, # 1.5 / 4

                       snares.e_e, # 2 / 4
                       snares.q_a, # 3 / 4

                       snares.e_e, # 3.5 / 4
                       snares.e_e, # 4 / 4

                       )

    #   Measure 5
    m5 = build_measure(snares.q_a, # 1 / 4
                    #    snares.q_g, # 2 / 4
                    #    rest(HALF)
                       
                       )
    
    return build_measure(m1, m2, m3, m4, m5) * 0.8


def synths_1():
    n = Piano(5, WHOLE)

    m1 = build_measure(
        rest(QUARTER + QUARTER + QUARTER + EIGHTH + QUARTER + EIGHTH + QUARTER + EIGHTH + EIGHTH),
        n.s_a, n.s_g, n.e_a,
        rest(WHOLE + TREY)
    )

    final = m1

    final *= 0.4
    return final

def synths_2():
    n = Piano(5, WHOLE)

    m2 = build_measure(
        n.s_g, n.s_f, n.s_f,
        rest(SIXTEENTH)
    )

    final = m2

    final *= 0.4
    return final

def synths_3():
    """Synths 1 but without the rest at the end"""
    
    n = Piano(5, WHOLE)

    m1 = build_measure(
        rest(QUARTER + QUARTER + QUARTER + EIGHTH + QUARTER + EIGHTH + QUARTER + EIGHTH + EIGHTH),
        n.s_a, n.s_g, n.e_a,
    )

    final = m1

    final *= 0.4
    return final

def synths_loop():
    n = Piano(5, WHOLE)

    m1 = build_measure(n.e_a, n.e_a,
                       n.e_a, n.e_f,
                       n.e_f, n.e_f,
                       n.e_e, n.e_e,
                       n.e_e, n.e_e,
                       n.e_e, n.e_e,
                       n.e_f, n.e_e,
                       n.e_d, n.e_d,

    )
    
    final = m1


    final *= 0.4
    return final

def synths_loop2():
    n = Piano(5, WHOLE)

    m1 = build_measure(n.e_a, n.s_d, n.s_e,
                       n.e_a, n.e_f,
                       n.e_f, n.e_f,
                       n.e_e, n.e_e,
                       n.e_e, n.e_e,
                       n.e_e, n.s_d, n.s_e,
                       n.e_f, n.e_e,
                       n.e_d, n.e_d,

    )
    
    final = m1


    final *= 0.4
    return final


def synths_loop3():
    n = Piano(5, WHOLE)

    m1 = build_measure(n.s_d, n.s_e, n.e_a,
                       n.e_a, n.e_f,
                       n.e_f, n.e_f,
                       n.e_e, n.e_e,
                       n.e_e, n.e_e,
                       n.e_e, n.s_d, n.s_e,
                       n.e_f, n.e_e,
                       n.e_d, n.e_d,

    )
    
    final = m1


    final *= 0.4
    return final

"""
(2) Auxillary Functions
"""
def basses():
    """generate the bass"""
    b1 = bass()
    save(b1,"hip-hop-snare", "bass")


def dreams():
    # d = dreamy()
    # d2 = dreamy_2()
    d3 = dreamy_3()
    d4 = dreamy_4()
    d5 = dreamy_5()
    d6 = dreamy_6()
    d7 = dreamy_7()
    d8 = dreamy_8() # replace with d3

    v1 = build_measure(d8, d4, d4, d3,
                         d4, d4, d6, d3, d5)
    
    v2 = build_measure(d4, d7, d6, d3,
                         d7, d6, d7, d3, d5)

    full = build_measure(v1, v2) * 0.6

    #   Components of each verse
    # save(d, "hip-hop-snare", "dreamy")
    # save(d2, "hip-hop-snare", "dreamy2")
    # save(d3, "hip-hop-snare", "dreamy3")
    # save(d4, "hip-hop-snare", "dreamy4")
    # save(d5, "hip-hop-snare", "dreamy5")
    # save(d6, "hip-hop-snare", "dreamy6")
    #save(d7, "hip-hop-snare", "dreamy7")

    #   Full Verses
    save(v1, "hip-hop-snare", "dreams_v1")
    save(v2, "hip-hop-snare", "dreams_v2")
    save(full, "hip-hop-snare", "dreams_full")

    return full


def symbols():
    s1 = symbol()
    s2 = symbol_loop()

    #s1 += bass()
    save(s1, "hip-hop-snare", "symbol" )
    save(s2, "hip-hop-snare", "symbol_loop")


def drums():
    #   Full Drum Beat
    one = drums_1()
    two = drums_2()
    three = drums_3()
    four = drums_4()
    five = drums_5()

    v1 = build_measure(two, five, five, five, one,
                       three, three, three, one, four)
    
    #   Original V2
    # v2 = build_measure(three, three, three, one,
    #                    three, three, three, one, four)

    #   Messy V2
    v2 = build_measure(four, three, three, three, three,
                       four, three, three, three, three)

    full = build_measure(v1, v2)* 0.6

    # save(one, "hip-hop-snare", "drums_1")
    # save(two, "hip-hop-snare", "drums_2")
    # save(three, "hip-hop-snare", "drums_3")
    # save(four, "hip-hop-snare", "drums_4")
    #save(five, "hip-hop-snare", "drums_5")
    #save(v1, "hip-hop-snare", "drums_v1")
    #save(v2, "hip-hop-snare", "drums_v2")
    save(full, "hip-hop-snare", "drums_full")

def skirts():
    loop = skirts_loop()
    single = skirts_single()

    save(loop, "hip-hop-snare", "skirt_loop")
    save(single, "hip-hop-snare", "skirt_single")



def synths():
    loop = synths_loop()
    loop2 = synths_loop2()
    loop3 = synths_loop3()

    s1 = synths_1()
    s2 = synths_2()
    s3 = synths_3()
    
    # v1 = build_measure(s1, s2, loop, loop2,
    #                    s1, s2, loop3, loop2,
    #                    rest(WHOLE + TREY),

    #                    s3, s1, s2, loop, loop3,
    #                    s1, s2, loop2, loop3,
    #                    rest(WHOLE + TREY + (WHOLE*4))

    #                    )
    
    v1 = build_measure(s1, s2, loop, loop2, loop3, loop2, loop3, loop2,
                       s1, s2, loop3, loop2,
                       rest(WHOLE + TREY),

                       s3, s1, s2, loop, loop3,
                       s1, s2, loop2, loop3,
                       rest(WHOLE + TREY + (WHOLE*4))

                       )
    
    v2 = build_measure(s1, s2, loop2, loop3,
                       s1, s2, loop, loop2,
                       rest(WHOLE + TREY),
                       s3, loop2, loop3,
                       s1, s2, loop3, loop2,
                       s1, s2, #s1, s2
                       )
    
    

    full = build_measure(v1, v2)
    # high twang then into loop
    save(loop, "hip-hop-snare", "synths_loop")
    save(loop2, "hip-hop-snare", "synths_loop2")
    save(s1, "hip-hop-snare", "synths_1")
    save(full, "hip-hop-snare", "synths_full")

def silence(duration):
    r = rest(duration)
    
    save(r, "hip-hop-snare", "silence")

"""
(3) Main Function / Driver Code ---------------------
"""
def main():
    #drums()
    dreams()
    #symbols()
    #skirts()
    synths()
    #silence(WHOLE*4)