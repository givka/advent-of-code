# Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
# Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.

class Rocket():
    def __init__(self, name, speed, time, rest):
        self.name = name
        self.speed = speed
        self.time = time
        self.rest = rest
        self.is_resting = False
        self.t = 0
        self.pos = 0
        self.points = 0

    def tick(self):
        if not self.is_resting:
            self.pos += self.speed
            self.t += 1

            if self.t == self.time:
                self.is_resting = True
                self.t = 0
        else:
            self.t += 1

            if self.t == self.rest:
                self.is_resting = False
                self.t = 0


R = []

for l in open("14.in").readlines():
    l = l.strip()
    a, b = [a.strip() for a in l.split("seconds, but then must rest for")]
    name, _, _, speed, _, _, time = a.split()
    rest = b.split()[0]
    R.append(Rocket(name, int(speed), int(time), int(rest)))

#seconds = 1000
seconds = 2503

for i in range(seconds):
    for r in R:
        r.tick()
    r = sorted(R, key=lambda x: x.pos, reverse=True)
    r = [rr for rr in r if rr.pos == r[0].pos]
    for rr in r:
        rr.points += 1

print(max(R, key=lambda x: x.pos).pos)
print(max(R, key=lambda x: x.points).points)
