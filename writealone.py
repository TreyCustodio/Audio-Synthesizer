"""
And I always write alone!
Chillin in my room with a finger on my dome!
Cause people might whine some people might moan!
But I never pay attention always grindin for the throan!

Well come on over here to this side,
this guy,
punches mothafuckas in his freetime,
need I,
tell you all about my mental design,


8 Beats per Bar
"""
from audio import *
from instruments import *
import wave


#   Set the tempo -- note should be BEAT but not refactoring
BPM = 180 # 180 or 160
BPS = BPM / 60
NOTE = 1 / BPS

#   Note lengths
SIXTEENTH = NOTE / 4
EIGHTH = NOTE / 2
QUARTER = NOTE
HALF = NOTE * 2
TREY = NOTE * 3
WHOLE = NOTE * 4


def bass():
    n = Bass(2, WHOLE)

    m1 = build_measure(n.q_f, 
                       rest(TREY - EIGHTH))

    m2 = build_measure(n.e_d, n.e_d, 
                       n.q_c, 
                       rest(HALF + EIGHTH))

    m3 =build_measure(n.e_d, n.e_d, 
                       n.q_c, 
                       rest(HALF), n.e_e)
    
    final = build_measure(m1, m3,
                          m1, m2,
                          m1, m3,
                          m1, m3
                          
                          ) * 0.4
    save(final, "writealone", "bass")


def piano2():
    #   Define our notes
    n4 = Pluck(4, WHOLE, "2")
    n3 = Pluck(3, WHOLE, "2")
    n2 = Pluck(2, WHOLE, "2")
    fade_factor = 0.75

    #   Variant 1   #
    m1 = build_measure(n3.q_a, # 1
                       fade_mult(n3.q_a, n3.q_a, 2, 0.0, fade_factor)

    )


    m2 = build_measure(n3.q_g, # 1
                       fade_mult(n3.q_g, n3.q_g, 2, 0.0, fade_factor)
    )

    m5i = build_measure(n3.q_f + n3.q_d, # 1
                       fade_mult(n3.q_f + n3.q_d, n3.q_f + n3.q_d, 2, 0.0, fade_factor)
    )

    m6i = build_measure(n3.q_e + n3.q_c, fade_mult(n3.q_e, n3.q_c, 2, 0.0, fade_factor))

    #   Variant 2   #
    m3 = build_measure(fade_mult(n3.q_a +  n3.q_e, n3.q_a +  n3.q_e, 7, 0.0, fade_factor),
                       ) 
    
    
    m3a = build_measure(fade_mult(n3.q_a +  n3.q_e, n3.q_a +  n3.q_e, 3, 0.0, fade_factor),
                        fade_mult(n3.q_a +  n3.q_e, n3.q_a +  n3.q_e, 3, 0.0, fade_factor),
                       )
    
    m3b = build_measure(#rest(WHOLE),
                        fade_out(n3.w_a, 6),
                        # (n4.q_d), 
                        # (n4.q_d),
                        # (n4.q_c),
                        # (n4.q_d),
                        rest(EIGHTH), # 4.5
                        n4.q_b, #5.5
                        rest(EIGHTH), # 6
                        n4.q_a, # 7
                        rest(QUARTER)
                       )
    m3 += m3b
    m3a += m3b


    #   Variant 3 and 4   #
    m4 = build_measure(fade_mult(n3.q_g + n3.q_d, n3.q_g + n3.q_d, 3, 0.0, fade_factor)
                       )
    m4a = build_measure(fade_mult(n4.q_g, n4.q_g, 3, 0.0, fade_factor))
    m4 += m4a


    ##  Whole Notes
    m5 = build_measure(fade_mult(n3.q_f + n3.q_d, n3.q_f + n3.q_d, 3, 0.0, 0.4))
    
    

    m6 = build_measure(fade_mult(n3.q_d + n2.q_b, n3.q_d + n2.q_b, 3, 0.0, 0.4))
    
    


    ##  Endings
    low = add_waves(n3.q_e + n2.q_b, n3.q_e + n2.q_b)
    high = add_waves(n3.q_g + n3.q_c, n3.q_g + n3.q_c)

    m7 = build_measure(fade_out(low, 6),
                       fade_out(high, 6)
                       )

    m8 = build_measure(fade_out(low, 12),
                       fade_out(high, 12))



    #   Construct the Variants  #
    ##  Intro Variant
    v1 = build_measure(m1, m1, m2, m2)
    v1a = build_measure(m5i, m5i, m6i, m7)
    intro = build_measure(v1, v1a)
    

    ##  Main Variant
    v2 = build_measure(m3, m4, m4)
    v2a = build_measure(m3a, m4, m4)

    ##  Ending Variants
    v3 = build_measure(m5, m5, m6, m7)
    v4 = build_measure(m5, m5, m6, m8)

    ##  The full bar
    bar = build_measure(v2, v2a, v2, v2a, v2, v2a, v2, v2a, v3)
    bar2 = build_measure(v2, v2a, v2, v2a, v2, v2a, v2, v2a, v4)

    #   Return and final effects    #
    intro = v4
    final = build_measure(intro,
                          
                          bar,
                          bar2,
                          bar


                          ) * 0.2

    twangs = build_measure(
        n4.s_a, n4.e_b, rest(EIGHTH),
        n4.s_a, n4.e_b, rest(EIGHTH),
        # n4.s_a, n4.q_b,
        # n4.s_a, n4.q_b,
        # n4.s_a, n4.q_b,
        # n4.s_a, n4.q_b,
        # n4.s_a, n4.q_b,
        # n4.s_a, n4.q_b,

        # n4.s_g, n4.q_a,
        # n4.s_g, n4.q_a,
        # n4.s_g, n4.q_a,
        # n4.s_g, n4.q_a,
        # n4.s_g, n4.q_a,
        # n4.s_g, n4.q_a,
        # n4.s_g, n4.q_a,
        # n4.s_g, n4.q_a,
    )   * 0.09

    save(final, "writealone", "piano")
    save(twangs, "writealone", "twangs")

    save(v1 * 0.2, "writealone", "piano_1")
    save(v2 * 0.2, "writealone", "piano_2")
    save(v3 * 0.2, "writealone", "piano_3")


def plucks(save = False):
    n1 = Pluck(3, WHOLE)


    #   (V1) Verse 1 ---------------------------------
    m1 = build_measure(n1.q_a,
                       n1.q_a,
                       n1.q_a,
                       n1.q_a,
                       n1.q_a,
                       n1.q_a,
                       n1.q_a,
                       n1.q_a,)
    m1 = fade_out(m1, 12)


    m2 = build_measure(n1.q_g,
                       n1.q_g,
                       n1.q_g,
                       n1.q_g)
    m2 = fade_out(m2, 12)

    m3 = build_measure(n1.e_a, n1.e_a, 
                       n1.e_a, rest(EIGHTH),
                       n1.e_a, n1.e_a, n1.e_a, 
                       rest(EIGHTH))
   #m3 = fade_out(n1.w_a, 16)
    m4 = n1.w_g



    #   (V2) Verse 2 ---------------------------------
    m5 = build_measure(n1.e_g, rest(EIGHTH),
                       n1.e_g, rest(EIGHTH), 
                       n1.e_a, rest(EIGHTH), 
                       n1.e_g, n1.e_a,
                       )
    
    m6 = build_measure(rest(EIGHTH), n1.e_g,
                       n1.e_a, rest(EIGHTH),
                       n1.e_a, # 2.5
                       n1.q_g, # 3.5
                       rest(EIGHTH),
                       )

    m7 = build_measure(n1.s_g, n1.s_g, n1.e_g,
                       n1.e_g, rest(EIGHTH),
                       n1.e_a, rest(EIGHTH),
                       n1.e_g, n1.e_fs,
                       )
    
    m8 = build_measure(rest(EIGHTH), n1.e_g,
                       n1.e_fs, rest(EIGHTH),
                       n1.e_e, rest(EIGHTH), 
                       n1.e_fs, rest(EIGHTH)
                       )

    m9 = build_measure(n1.q_b, 
                       n1.e_g, rest(EIGHTH),
                       n1.e_g, n1.e_fs, # 3
                       n1.e_g, # 3.5 
                       )
    
    m10 = build_measure(n1.q_b, # 1
                       n1.e_g, rest(EIGHTH), # 2
                       n1.e_g, # 2.5
                       rest(QUARTER), # 3.5
                       n1.e_g, n1.e_g, # 4.5 as desired, par the lacking eigth note in m5
    )
    
    m11 = build_measure(n1.e_g, rest(EIGHTH), # 1
                       n1.e_g, n1.e_a, # 2
                       rest(EIGHTH), n1.e_g, # 3
                       rest(EIGHTH), n1.e_fs, # 4
    )

    m12 = build_measure(rest(EIGHTH), n1.e_g,
                       n1.e_fs, rest(EIGHTH),
                       n1.e_fs, n1.e_e,
                       n1.e_a, rest(EIGHTH))
    
    #   Combine and return
    v1 = build_measure(m1, m2, m2,
                       m3, m3, m2, m2) * 0.2
    
    v2 = build_measure(m5, m6, m7, m8,
                       m9, m10, m11, m12) * 0.2
    if not save:
        return v1, v2
    
def xylos(save = False):
    """Piano melody incorporating XyloTech"""
    
    #   Define our notes
    n6 = XyloTech(7, WHOLE)
    n5 = XyloTech(7, get_measure(160), "2")

    fade_factor = 0.75


    #   Create each 4-beat measure

    ##  (I1) High xylos at the intro
    i1 = build_measure(n5.e_g, rest(EIGHTH),
                       n5.e_g, rest(EIGHTH),
                       rest(EIGHTH), n5.e_g,
                       rest(EIGHTH), n5.e_f)

    i1 = build_measure(rest(WHOLE))

    ##  (V1) Top Half ver 1 ---------------------------------------------
    m1 = build_measure(n6.e_g, rest(EIGHTH),
                       n6.e_g, rest(EIGHTH), 
                       n6.e_a, rest(EIGHTH), 
                       n6.e_g, n6.e_a,
                       )
    
    m2 = build_measure(rest(EIGHTH), n6.e_g,
                       n6.e_a, rest(EIGHTH),
                       n6.e_a, # 2.5
                       n6.q_g, # 3.5
                       rest(EIGHTH),
                       )

    m3 = build_measure(n6.e_g, n6.e_g,
                       n6.e_g, rest(EIGHTH),
                       n6.e_a, rest(EIGHTH),
                       n6.e_g, n6.e_fs,
                       )
    
    m4 = build_measure(rest(EIGHTH), n6.e_g,
                       n6.e_fs, rest(EIGHTH),
                       n6.e_e, rest(EIGHTH), 
                       n6.e_fs, rest(EIGHTH)
                       )
    

    ##  (V1) Bottom Half ver 1
    m5 = build_measure(n6.q_b, 
                       n6.e_g, rest(EIGHTH),
                       n6.e_g, rest(EIGHTH), # 3
                       n6.e_g, # 3.5 
                       )
    
    m6 = build_measure(n6.q_b, # 1
                       n6.e_g, rest(EIGHTH), # 2
                       n6.e_g, # 2.5
                       rest(QUARTER), # 3.5
                       n6.e_g, n6.e_g, # 4.5 as desired, par the lacking eigth note in m5
    )
    
    m7 = build_measure(n6.e_g, rest(EIGHTH), # 1
                       n6.e_g, n6.e_a, # 2
                       rest(EIGHTH), n6.e_g, # 3
                       rest(EIGHTH), n6.e_fs, # 4
    )

    m8 = build_measure(rest(EIGHTH), n6.e_g,
                       n6.e_fs, rest(EIGHTH),
                       n6.s_fs, n6.s_e, n6.e_e,
                       n6.q_a,)




    ##  (V2) Top Half ver 2 ---------------------------------------------
    m9 = build_measure(n6.e_g, rest(EIGHTH),
                       n6.e_g, rest(EIGHTH), 
                       n6.e_a, rest(EIGHTH), 
                       n6.e_g, n6.e_a,
                       )
    
    m10 = build_measure(rest(EIGHTH), n6.e_g,
                       n6.e_a, rest(EIGHTH),
                       n6.e_a, # 2.5
                       n6.q_g, # 3.5
                       rest(EIGHTH),
                       )

    m11 = build_measure(n6.s_g, n6.s_g, n6.e_g,
                       n6.e_g, rest(EIGHTH),
                       n6.e_a, rest(EIGHTH),
                       n6.e_g, n6.e_fs,
                       )
    
    m12 = build_measure(rest(EIGHTH), n6.e_g,
                       n6.e_fs, rest(EIGHTH),
                       n6.e_e, rest(EIGHTH), 
                       n6.e_fs, rest(EIGHTH)
                       )
    
    ##  (V2) Bottom Half ver 2
    m13 = build_measure(n6.q_b, 
                       n6.e_g, rest(EIGHTH),
                       n6.e_g, n6.e_fs, # 3
                       n6.e_g, # 3.5 
                       )
    
    m14 = build_measure(n6.q_b, # 1
                       n6.e_g, rest(EIGHTH), # 2
                       n6.e_g, # 2.5
                       rest(QUARTER), # 3.5
                       n6.e_g, n6.e_g, # 4.5 as desired, par the lacking eigth note in m5
    )
    
    m15 = build_measure(n6.e_g, rest(EIGHTH), # 1
                       n6.e_g, n6.e_a, # 2
                       rest(EIGHTH), n6.e_g, # 3
                       rest(EIGHTH), n6.e_fs, # 4
    )

    m16 = build_measure(rest(EIGHTH), n6.e_g,
                       n6.e_fs, rest(EIGHTH),
                       n6.e_fs, n6.e_e,
                       n6.e_a, rest(EIGHTH))
    


    ##  (V3) Top Half ver 3 ---------------------------------------------
    ## Make the first measure less repetitive
    m17 = build_measure(n6.e_a, n6.e_g, #rest(EIGHTH),
                       n6.e_g, rest(EIGHTH), 
                       n6.e_a, rest(EIGHTH), 
                       n6.e_g, n6.e_a,
                       )
    
    m18 = build_measure(rest(EIGHTH), n6.e_g,
                       n6.e_a, n6.e_g, #rest(EIGHTH),
                       n6.e_a, # 2.5
                       n6.q_g, # 3.5
                       rest(EIGHTH),
                       )

    m19 = build_measure(n6.s_g, n6.s_g, n6.e_g,
                       n6.e_g, rest(EIGHTH),
                       n6.e_a, rest(EIGHTH),
                       n6.e_g, n6.e_fs,
                       )
    
    m20 = build_measure(rest(EIGHTH), n6.e_g,
                       n6.e_fs, rest(EIGHTH),
                       n6.e_e, rest(EIGHTH), 
                       n6.e_fs, rest(EIGHTH)
                       )
    

    ##  (V3) Bottom Half ver 3



    #   (FINAL) Combine measures into 32-beat verses
    final = build_measure(m1, m2, m3, m4,
                          m5, m6, m7, m8) * 0.1
    
    final2 = build_measure(m9, m10, m11, m12,
                           m13, m14, m15, m16) * 0.1
    
    final3 = build_measure(m17, m18, m19, m20,
                           m5, m6, m7, m8) * 0.1
    if not save:
        return i1, final, final2, final3
    
    save(final, "writealone", "piano")

    
def drums(save = False):
    """If save == False: return the 32-beat verses"""
    #   (1) Notes
    ##  main notes (bpm = 180)
    n = Snare(2, WHOLE)
    c = Skirt(3, WHOLE)
    s = Skirt(4, WHOLE)

    ##  intro notes (bpm = 160)
    ni = Snare(2, get_measure(160))
    ci = Skirt(3, get_measure(160))
    si = Skirt(4, get_measure(160))

    intro_eighth = get_eighth(160)


    #   (2) Intro ------------------------------------------------
    
    ##  8-beat measures
    m1 = build_measure(ni.q_e, # 1
                       rest(intro_eighth), # 1.5
                       ni.e_e, ci.q_e, # 3
                       rest(intro_eighth), # 3.5
                       ni.e_e, ni.e_e, ni.e_e, # 5
                       rest(intro_eighth), # 5.5
                       ni.e_e, ci.q_e, # 7
                       rest(intro_eighth), ni.e_e # 8
                       )
    
    m2 = build_measure(si.q_c, # 1
                       si.q_c, # 2
                       si.q_c, # 3
                       si.q_c, # 4
                       si.q_c, # 5
                       si.q_c, # 6
                       si.q_c, # 7
                       si.q_c, # 8
                       ) * 0.1
    
    
    ##  40-beat Verses
    v1 = build_measure(m1, m1, m1, fade_out(m1, 2))
    v1_noFade = build_measure(m1, m1, m1, m1)

    v2 = build_measure(m2, m2, m2, fade_out(m2, 2))
    v2_noFade = build_measure(m2, m2, m2, m2)
    
    intro = combine(v1_noFade, v2_noFade)


    #   (3) Main Drums ------------------------------------------------
    
    ##  Each of these measures are 4 Beats
    m3 = build_measure(rest(QUARTER + EIGHTH), # 1.5
                       n.e_e, # 2
                       c.e_c, n.e_e, # 3
                       rest(QUARTER), # 4
                       )
    
    skirts_rest = build_measure(s.q_c, # 1
                       s.q_c, # 2
                       s.q_c, # 3
                       rest(QUARTER), # 4
                       ) * 0.1
    
    skirts_chimes = build_measure(s.q_c, # 1
                       s.q_c, # 2
                       s.q_c, # 3
                       s.s_d + s.s_c, s.s_d + s.s_c, s.e_d + s.e_c, # 4
                       ) * 0.1
    
    skirts_full = build_measure(s.q_c, # 1
                       s.q_c, # 2
                       s.q_c, # 3
                       s.q_c, # 4
                       ) * 0.1
    

    ##  These verses are 32 Beats
    v3 = build_measure(m3, m3, m3, m3,
                       m3, m3, m3, m3) * 0.8
    
    v4 = build_measure(
        skirts_rest, skirts_rest, skirts_full, skirts_rest,
        skirts_rest, skirts_rest, skirts_chimes, skirts_rest,
    )

    v5 = build_measure(skirts_full, skirts_full, skirts_chimes, skirts_full,
                       skirts_full, skirts_full, skirts_chimes, skirts_full,)

    
    #   Experiment with different loops here
    main_1 = combine(v3, v4)
    main_2 = combine(v3, v5)



    #   (4) Final effects and Returns ---------------------------------------
    if not save:
        return intro, main_1, main_2
    
    save(m3, "writealone", "one")
    save(v1, "writealone", "drums")
    save(v2, "writealone", "skirts")
    save(v1_noFade, "writealone", "drums_noFade")
    save(v2_noFade, "writealone", "skirts_noFade")
    save(v3, "writealone", "drums2")


    

def skirts():
    n = Skirt2(3, WHOLE)

    save(n.q_c, "writealone", "skirt2")

def produce():
    """Produce the entire track without using an audio editing interface"""
    #   (1) The Drums: d = 40 beats; dn = 32 beats;
    d, d1, d2 = drums()

    #   (2) The Xylos: 32 beats
    xi, x1, x2, x3 = xylos()

    #   (3) The Plucks: 32 beats
    p1, p2 = plucks()
    
    #   Combine each verse
    d = combine(d, xi)

    v1 = combine(d2, x2) # jiggier

    v2 = combine(d2, x1) # also add plucks; snappier
    v2 = combine(v2, p1)

    v3 = combine(d2, x2) # jiggier v1 but with plucks
    v3 = combine(v3, p2)

    v4 = combine(d2, x3) # jiggier with less repetitive top half

    #   Build the final production
    production = build_measure(d, d1, # Intro (Drums only)
                               v1, v2,
                               v3, v2, v4, v2,
                               v2, v2, v3, v2)

    save(production, "writealone", "production")





def test():
    n = Piano(5, WHOLE, "single")
    nd = Piano(5, WHOLE, "double")
    
    save(nd.q_c, "writealone", "test")
    #save(n.q_c, "writealone", "c")
    #save(n.q_e, "writealone", "e")

def main():
    #plucks()
    #dreams()
    #skirts()
    #bass()
    #drums_intro()
    #drums()
    #piano()
    #piano2()
    #save(rest(WHOLE * 3), "writealone", "silence")
    produce()