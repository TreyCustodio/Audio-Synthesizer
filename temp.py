m9 = [
            n.note(F3, e) + n.note(D3, self.e), n.note(G3, e) + n.note(E3, self.e), # 1
            n.note(B3, s) + n.note(G3, s), n.note(A3, e) + n.note(F3, e), # 1.75

            n.note(F3, e) + n.note(D3, self.e), n.note(G3, e) + n.note(E3, self.e), # 2.75
            n.note(F3, s) + n.note(D3, self.s), n.note(B3, e) + n.note(G3, e), # 2.75
            n.note(A3, e) + n.note(F3, e),
        ]

        m10 = [
            n.note(F3, e) + n.note(D3, self.e), n.note(G3, e) + n.note(E3, self.e), # 1
            n.note(B3, s) + n.note(G3, s), n.note(A3, e) + n.note(F3, e), # 1.75

            n.note(B3, e) + n.note(G3, self.e), n.note(A3, s) + n.note(F3, s), n.note(G3, s) + n.note(E3, s), # 2.75
            
            n.note(F3, s) + n.note(D3, self.s), n.note(G3, s) + n.note(E3, s), n.note(A3, s) + n.note(F3, s),
            n.note(D3, s) + n.note(B2, self.s), n.note(E3, s) + n.note(C3, self.s),
            
        ]

        m11 = [
            n.note(F3 , e) + n.note(D3, self.e), n.note(G3, e) + n.note(E3, self.e), # 1
            n.note(G3, e) + n.note(E3, self.e), # 1.5
            n.note(E3, s) + n.note(C3, self.s), n.note(F3, e) + n.note(D3, self.e), # 2.25
            n.note(G3, e) + n.note(E3, self.e), n.note(G3, e) + n.note(E3, self.e), # 3.25
            rest(self.s * 3)
        ]

        m12 = [
            n.note(F3 , e) + n.note(D3, self.e), n.note(G3, e) + n.note(E3, self.e), # 1
            n.note(G3, e) + n.note(E3, self.e), # 1.5
            n.note(E3, s) + n.note(C3, self.s), n.note(F3, e) + n.note(D3, self.e), # 2.25
            n.note(G3, e) + n.note(E3, self.e), n.note(G3, e) + n.note(E3, self.e), # 3.25
            rest(self.s), 
            n.note(D3, s) + n.note(B2, s), n.note(E3, s) + n.note(C3, s),
        ]