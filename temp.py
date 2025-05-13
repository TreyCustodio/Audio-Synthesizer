m2 = build_measure(n3.w_a, rest(self.quarter + self.eighth),
                           n3.e_e, n3.e_f, rest(self.eighth),
                           n3.q_g,
                           #delaycombo(delaycombo(n3.q_g, n3.q_a, wait), n3.q_b, self.half - self.sixteenth / 2),
                           n3.w_b, rest(self.quarter + self.eighth),

                           n3.e_e, n3.e_f, rest(self.eighth),
                           #delaycombo(n3.q_g, n3.q_a, wait),
                           n3.q_b,
                           n3.w_g, rest(self.quarter + self.eighth),

                           n3.e_e, n3.e_f, rest(self.eighth),
                           n3.q_d,
                           #delaycombo(delaycombo(n3.q_g, n3.q_a, wait), n3.q_f, self.half - self.sixteenth / 2),
                           n3.w_c,
                           n3.create_note(D2, self.whole)
                           )