from collections import deque, Counter

with open("input", "r") as file:
    inp = file.read()

# 16777216 = 2 ** 24
PRUNE = 0b111111111111111111111111

_CACHE = {}
def secret(v, n=1):
    i = 0
    seq = deque()
    price_map = {}
    while i < n:
        if v in _CACHE:
            v_, p, d = _CACHE[v]
        else:
            v_ = (v ^ (v << 6)) & PRUNE
            v_ = (v_ ^ (v_ >> 5)) & PRUNE
            v_ = (v_ ^ (v_ << 11)) & PRUNE
            p = v_ % 10
            d = (v_ % 10 - v % 10)
            _CACHE[v] = v_, p, d
        v = v_
        seq.append(d)
        if i >= 3:
            k = tuple(seq)
            if k not in price_map:
                price_map[k] = p
            seq.popleft()
        i += 1
    return v, price_map

allsecrets = 0
psum = Counter()
for row in inp.strip().split("\n"):
    v_, pmap = secret(int(row), 2000)
    allsecrets += v_
    psum += pmap
bananamax = max(psum.values())

print(allsecrets)
print(bananamax)
