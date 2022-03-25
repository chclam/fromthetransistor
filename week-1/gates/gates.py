def nand(a, b):
  return not (a and b)

def not_(a):
  return nand(a, a)

def and_(a, b):
  return nand(nand(a, b), nand(a, b))

def or_(a, b):
  return nand(nand(a, a), nand(b, b))

def xor(a, b):
  return and_(or_(a, b), not_(and_(a, b)))

def mux(a, b, sel):
  return or_(and_(not_(sel), a), and_(sel, b))

def dmux(a, sel):
  return and_(not_(sel), a), and_(sel, a)
