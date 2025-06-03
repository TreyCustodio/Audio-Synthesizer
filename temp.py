m1 = build_measure(
            b.note(C2, self.s + self.s/2), b.note(D2, self.e + self.s/2),
            b.note(E2, self.s + self.s/2), b.note(Gs2, self.e),
            rest(self.q + self.s/2),
            b.note(A2, self.e), rest(self.e)
            )
        
        m2 = build_measure(
            b.note(C2, self.e), b.note(D2, self.e),
            b.note(E2, self.s + self.s/2), b.note(Gs2, self.e),
            rest(self.q + self.s/2),
            b.note(A2, self.e), rest(self.e)
            )

        m3 = build_measure(
            b.note(C2, self.e), b.note(D2, self.e),
            b.note(E2, self.e), b.note(Gs2, self.e),
            rest(self.q),
            b.note(A2, self.e), rest(self.e)
            )