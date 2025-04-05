 #   (v4) Dirtier Xylophone; Tone Shifted -2 full tones
    m25 = build_measure(n6.e_g, rest(EIGHTH),
                       n6.e_g, rest(EIGHTH), 
                       n6.e_a, rest(EIGHTH), 
                       n6.e_g, n6.e_a,
                       )
    
    m26 = build_measure(rest(EIGHTH), n6.e_g,
                       n6.e_a, rest(EIGHTH),
                       n6.e_a, # 2.5
                       n6.q_g, # 3.5
                       rest(EIGHTH),
                       )

    m27 = build_measure(n6.s_g, n6.s_g, n6.e_g,
                       n6.e_g, rest(EIGHTH),
                       n6.e_a, rest(EIGHTH),
                       n6.e_g, n6.e_fs,
                       )
    
    m28 = build_measure(rest(EIGHTH), n6.e_g,
                       n6.e_fs, rest(EIGHTH),
                       n6.e_e, rest(EIGHTH), 
                       n6.e_fs, rest(EIGHTH)
                       )
    
    ##  (V4) Bottom Half ver 4
    m29 = build_measure(n6.q_b, 
                       n6.e_g, rest(EIGHTH),
                       n6.e_g, n6.e_fs, # 3
                       n6.e_g, # 3.5 
                       )
    
    m30 = build_measure(n6.q_b, # 1
                       n6.e_g, rest(EIGHTH), # 2
                       n6.e_g, # 2.5
                       rest(QUARTER), # 3.5
                       n6.e_g, n6.e_g, # 4.5 as desired, par the lacking eigth note in m5
    )
    
    m31 = build_measure(n6.e_g, rest(EIGHTH), # 1
                       n6.e_g, n6.e_a, # 2
                       rest(EIGHTH), n6.e_g, # 3
                       rest(EIGHTH), n6.e_fs, # 4
    )

    m32 = build_measure(rest(EIGHTH), n6.e_g,
                       n6.e_fs, rest(EIGHTH),
                       n6.e_fs, n6.e_e,
                       n6.e_a, rest(EIGHTH))