#!/usr/bin/env python2
# DYLAN LLOYD
# VOLUME OF A SOLID OF REVOLUTION

import sys
import argparse
import math
from scipy import integrate
from scipy.optimize import fsolve
from sympy import Symbol, Eq, solve
import numpy

parser = argparse.ArgumentParser(description='Find the volume of the solid of rotation defined. Use * for multiplication and ** to raise a power. Bounds are set equal to the independent variable. Trailing .0\'s must be used for constants, and parentheses must be escaped ( e.g. \(x-2\) ). Answers are accurate to 6 decimals.')
parser.add_argument('var', choices='xy', help='x|y')
parser.add_argument('=', metavar='=', choices='=')
parser.add_argument('equation', help='continous function')
parser.add_argument('a', type=float, help='bound \'a\'')
parser.add_argument('b', type=float, help='bound \'b\'')
parser.add_argument('-axis', choices='xy', help='axis of revolution (default == x)')
parser.add_argument('-o', type=float, help='offset axis by #')
parser.add_argument('-m', choices='ds', help='method (disk/shell)')
parser.add_argument('-g', action='store_true', help='show function graph')
parser.add_argument('-v', action='store_true', help='verbose (for debugging)')
args = parser.parse_args()


y = Symbol('y')
x =  Symbol('x')

class function():
  def __init__(self, var, func, a, b, axis=None, method=None):
    self.var = var
    self.func = func
    self.a = a
    self.b = b
    self.axis = axis
    self.method = method
    if self.axis == None: self.axis = 'x'
    if method == None:
      if self.var == self.axis:
          self.method = 'shell'
      else:
          self.method = 'disk'
    else:
      if self.method == 's': self.method = 'shell'
      if self.method == 'd': self.method = 'disk'
    print self.integrate()

  def integrate(self):
    # y = x about x (disk method)
    if self.method == 'disk' and self.var == 'y':
        print "# y = x about x (disk method)"
        if args.v: print 'integral of', '(' + self.func + ')**2'
        self.func = eval('lambda x: ' + '(' + self.func + ')**2')
        integral = integrate.quad(self.func, self.a, self.b)
        if args.v: print 'integral from', self.a, 'to', self.b, '=', integral[0]
        answer = math.pi * integral[0]
        if args.v: print 'pi*', integral[0], '=', answer
        return answer

    # y = x about y (shell method)
    if self.method == 'shell' and self.var == 'y':
        print "# y = x about y (shell method)"
        if args.v: print 'integral of', 'x(' + self.func + ')'
        self.func = eval('lambda x: ' + 'x*(' + self.func + ')')
        self.integral = integrate.quad(self.func, self.a, self.b)
        if args.v: print 'integral from', self.a, 'to', self.b, '=', self.integral[0]
        answer = 2 * math.pi * self.integral[0]
        if args.v: print '2 *pi*', self.integral[0], '=', answer
        return answer

    # x = y about y (disk method)
    if self.method == 'disk' and self.var == 'y':
        print "# x = y about y (disk method)"
        if args.v: print 'integral of', '(' + self.func + ')**2'
        self.func = eval('lambda y: ' + '(' + self.func + ')**2')
        integral = integrate.quad(self.func, self.a, self.b)
        if args.v: print 'integral from', self.a, 'to', self.b, '=', integral[0]
        answer = math.pi * integral[0]
        if args.v: print 'pi*', integral[0], '=', answer
        return answer

    # x = y about x (shell method)
    if self.method == 'shell' and self.var == 'x':
        print "# x = y about x (shell method)"
        if args.v: print 'integral of', 'y(' + self.func + ')'
        self.func = eval('lambda y: ' + 'y*(' + self.func + ')')
        self.integral = integrate.quad(self.func, self.a, self.b)
        if args.v: print 'integral from', self.a, 'to', self.b, '=', self.integral[0]
        answer = 2 * math.pi * self.integral[0]
        if args.v: print '2 *pi*', self.integral[0], '=', answer
        return answer


  def solve_for_implicit(self):
    if self.var == 'x':
        equation = Eq(eval(self.func), x)
        func = solve(equation, y)
    else:
        equation = Eq(eval(self.func), y)
        print 'eq:', equation
        func = solve(equation, x)
        print func

#  def graph(equation, a, b):
#    x = numpy.arange(a, b, 0.01)
#    func = eval('lambda x: ' + equation)
#    y = func(x)
#    pylab.plot(x, y)
#    pylab.xlabel('x')
#    pylab.ylabel('y')
#    pylab.title(equation)
#    pylab.grid(True)
#    pylab.show()

#####################################################
#####################################################
#####################################################
#####################################################
init = function(args.var, args.equation, args.a, args.b, args.axis, args.m)
#####################################################
#####################################################
#####################################################
exit()
#####################################################


def volume(var, func, a, b, axis=None, method=None):
  if axis == None: axis = 'x'
  if method == 's': method = 'shell'
  if method == 'd': method = 'disk'

  if var == axis and axis == 'x':
      if args.v: print 'x = y about x'
      if not method == 'disk':
          # THIS SHOULD WORK BY INVERSE
          if args.v: print 'using shell method'
          if args.v: print 'integral of', 'x(' + func + ')'
          func = eval('lambda y: ' + 'x*(' + func + ')')
          integral = integrate.quad(func, a, b)
          if args.v: print 'integral from', a, 'to', b, '=', integral[0]
          answer = 2 * math.pi * integral[0]
          if args.v: print '2 *pi*', integral[0], '=', answer
          pass
      else:
          pass

  elif var == axis and axis == 'y':
      if args.v: print 'y = x about y'
      if not method == 'disk':
          # THIS WORKS.
          if args.v: print 'using shell method'
          if args.v: print 'integral of', 'x(' + func + ')'
          func = eval('lambda x: ' + 'x*(' + func + ')')
          integral = integrate.quad(func, a, b)
          if args.v: print 'integral from', a, 'to', b, '=', integral[0]
          answer = 2 * math.pi * integral[0]
          if args.v: print '2 *pi*', integral[0], '=', answer
          pass
      else:
          pass

  elif not var == axis and axis == 'y':
      if args.v: print 'x = y about y'
      # THESE SHOULD WORK BY THEORY OF INVERSE, BUT MAY NEED TO BE SWAPPED.
      if not method == 'shell':
          if args.v: print 'using disk method'
          if args.v: print 'integral of', '(' + func + ')**2'
          func = eval('lambda y: ' + '(' + func + ')**2')
          integral = integrate.quad(func, a, b)
          if args.v: print 'integral from', a, 'to', b, '=', integral[0]
          answer = math.pi * integral[0]
          if args.v: print 'pi*', integral[0], '=', answer
          pass
      else:
          if args.v: print 'using shell method'

          func = solve_for_implicit(func, var)
          func = str(func[0])
          if args.v: print 'solved for implicit and multiplied by y:', 'x(' + str(float(abs(b-a))) + '-(' +func + '))'
          height = eval('lambda x: ' + 'x*(' + str(float(abs(b-a))) + '-(' + func + '))')
          func = eval('lambda x:'  + 'x*(' + str(float(abs(b-a))) + '-' + func + ')')
          height = fsolve(height, float(abs(b-a)))
          # i have no idea what to do with the negative function
          integral = integrate.quad(func, 0, height)
          if args.v: print 'integral from', a, 'to', b, '=', integral[0]
          answer = 2 * math.pi * integral[0]
          if args.v: print '2*pi*', integral[0], '=', answer
          pass

  elif not var == axis and axis == 'x':
      if args.v: print 'y = x about x --',
      if not method == 'shell':
          # THIS WORKS.
          if args.v: print 'using disk method'
          if args.v: print 'integral of', '(' + func + ')**2'
          func = eval('lambda x: ' + '(' + func + ')**2')
          integral = integrate.quad(func, a, b)
          if args.v: print 'integral from', a, 'to', b, '=', integral[0]
          answer = math.pi * integral[0]
          if args.v: print 'pi*', integral[0], '=', answer
          pass
      else:
		  # THIS WORKS.
          if args.v: print 'using shell method', func, var
          print 'hmmm', func
          func = solve_for_implicit(func, x)
          func = str(func[0])
          if args.v: print 'solved for implicit and multiplied by y:', 'y(' + str(float(abs(b-a))) + '-(' +func + '))'
          height = eval('lambda y: ' + 'y*(' + str(float(abs(b-a))) + '-(' + func + '))')
          func = eval('lambda y:'  + 'y*(' + str(float(abs(b-a))) + '-' + func + ')')
          height = fsolve(height, float(abs(b-a)))
          # i have no idea what to do with the negative function
          integral = integrate.quad(func, 0, height)
          if args.v: print 'integral from', a, 'to', b, '=', integral[0]
          answer = 2 * math.pi * integral[0]
          if args.v: print '2*pi*', integral[0], '=', answer
          pass

  return answer



print volume(args.var, args.equation, args.a, args.b, args.axis, args.m)
#if args.g: graph(args.equation, args.a, args.b)
