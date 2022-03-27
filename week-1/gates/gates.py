def nand(a, b):
  return not (a and b)

def not_(a):
  return nand(a, a)

def and_(a, b):
  return nand(nand(a, b), nand(a, b))

def or_(a, b):
  return nand(nand(a, a), nand(b, b))

def xor(a, b):
  return and_(or_(a, b), nand(a, b))

def mux(a, b, sel):
  return or_(and_(not_(sel), a), and_(sel, b))

def dmux(a, sel):
  return and_(not_(sel), a), and_(sel, a)

def multi_not(a):
  return [not_(a[i]) for i in range(len(a))]

def multi_and(a, b):
  assert(len(a) == len(b))
  return [and_(a[i], b[i]) for i in range(len(a))]

def multi_or(a, b):
  assert(len(a) == len(b))
  return [or_(a[i], b[i]) for i in range(len(a))]

def half_adder(a, b):
  carry = and_(a, b)
  sum_ = xor(a, b)
  return carry, sum_

def full_adder(a, b, c):
  carry = or_(and_(c, or_(a, b)), and_(and_(a, b), not_(c)))
  sum_ = or_(and_(xor(a, b), not_(c)), and_(c, not_(xor(a, b))))
  return carry, sum_
