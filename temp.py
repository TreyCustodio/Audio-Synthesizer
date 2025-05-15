m1 = build_measure(f.q_d,
                           f.s_d, f.s_e,
                           f.s_f, f.s_g,
                           f.s_a, rest(self.sighth))
        
        m2 = build_measure(f.s_d, f.s_e,
                           f.s_f, f.s_g,
                           f.q_a,
                           f.q_g,
                           )
        
        m3 = build_measure(f.q_c,
                           f.s_c, f.s_d,
                           f.s_e, f.s_f,
                           f.s_g, rest(self.sighth))
        
        m4 = build_measure(f.s_c, f.s_d,
                           f.s_e, f.s_f,
                           f.q_g,
                           f.q_f,
                           )