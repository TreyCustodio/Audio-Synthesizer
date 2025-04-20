from beat import *

def main(bpm=160):
    a = sine_wave(100, get_quarter(160))
    print()
    x = XyloHorn(5, get_measure(bpm), "2")

    duration = get_half(bpm)
    meas = get_measure(bpm)
    quar = get_quarter(bpm)
    eight = get_eighth(bpm)

    n1 = build_measure(slur(C1, A5, duration))
    n1 = envelope(n1, 0.001 * duration, 0.2 * duration, 0.5, 0.3 * duration)

    n2 = build_measure(slur(C1, A5, quar))
    n2 = envelope(n2, 0.001 * quar, 0.2 * quar, 0.5, 0.3 * quar)

    n3 = build_measure(slur(A4, C1, eight))
    n3 = envelope(n3, 0.001 * eight, 0.2 * eight, 0.5, 0.3 * eight)

    final = build_measure(n1, rest(meas), n2, n2, rest(quar), n2, n2, rest(quar), n3, n3, n3,  rest(eight), n2, rest(quar), n3, n3, n3, rest(eight), n3, n3, n3, rest(eight), n2, rest(quar))
    final2 = build_measure(n1, rest(meas), n2, n2, rest(quar), n2, n2, rest(quar), n3, rest(eight), n3, rest(eight), n3, rest(eight), n3, rest(eight), n2, rest(quar), n3, n3, n3, rest(eight), n3, n3, n3, rest(eight), n2, rest(quar))
    
    
    final = build_measure(final2, final)
    save(final, "beats", "slur")