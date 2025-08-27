    def bass_a(self):
        """Tough pick here between G2 and Gs2"""
        b = self.bass1
        b2 = self.bass2

        m1 = [
            b.n(Gs2, self.w),
        ]

        m2 = [
            b.n(Gs2, self.w),
        ]

        m3 = [
            b.n(Gs2, self.e), rest(self.e),
            rest(self.e), b.n(Gs2, self.e),
            rest(self.e), rest(self.e),
            rest(self.e), rest(self.e), 
        ]

        m4 = [
            b.n(Gs2, self.e), rest(self.e),
            rest(self.e), b.n(Gs2, self.e) + b.n(F3, self.e, amp=0.4),
            rest(self.e), b.n(Fs2, self.e + self.q),
        ]

        v0 = [rest(self.w*4)]
        v1 = m1 + m2 + m3 + m4
        return v0 + v0 + v1 + v1 + v1 + v1 + v1 + v1 + v1 + v1 + v1 + v1 + v1 + v1
    
    def bass_b(self):
        b = self.bass1
        amp = 0.5

        m1 = [rest(self.w)]
        m2 = [
            rest(self.w),
            ]

        m3 = [
            b.n(Gs2, self.w, amp, fade=True, fade_amount=14),
        ]

        m4 = [
            b.n(Gs2, self.w, amp, fade=True, fade_amount=14),
        ]

        v0 = [rest(self.w*4)]
        v1 = m1 + m2 + m3 + m4
        return v0 + v0 + v1 + v1 + v1 + v1 + v1 + v1 + v1 + v1 + v1 + v1 + v1 + v1