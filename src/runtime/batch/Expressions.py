from Helper import *
import operator

class Seq :
    
    def __init__(self, statement, rest) :
        self.statement = statement
        self.rest = rest
    
    def interp(self, out, env) :
        self.statement.interp(out, env)
        return self.rest.interp(out, env)
    
    def __str__(self) :
        return "(Seq " + str(self.statement) + ", " + str(self.rest) + ")"

class Let :
    
    def __init__(self, var, value, statement) :
        self.var = var
        self.value = value
        self.statement = statement
    
    def interp(self, out, env) :
        return self.statement.interp(out, Env(self.var, self.value.interp(out, env), env))
    
    def __str__(self) :
        return "(Let " + str(self.var) + " = " + str(self.value) + " in " + str(self.statement) + ")"

class For :
    
    def __init__(self, label, listexpr, block) :
        self.label = label
        self.listexpr = listexpr
        self.block = block
    
    def interp(self, out, env) :
        l=self.listexpr.interp(out, env)
        out[self.label] = []
        for x in l :
            temp_dict = {} 
            self.block.interp(temp_dict, Env(self.label, x, env))
            out[self.label].append(temp_dict)
        return None
    
    def __str__(self) :
        return "(For " + str(self.label) + " in " + str(self.listexpr) + " do " + str(self.block) + ")"

class Fun :

    def __init__(self, param, code) :
        self.param = param
        self.code = code
    
    def interp(self, out, env) :
        return Closure(env, self.param, self.code)
    
    def __str__(self) :
        return "(Fun " + "(" + str(self.param) + ")" + "{" + str(self.code) + "})"

class Or :
    
    def __init__(self, a, b) :
        self.a = a
        self.b = b
    
    def interp(self, out, env) :
        return self.a.interp(out, env) or self.b.interp(out, env)
    
    def __str__(self) :
        return "(or " + str(self.a) + " " + str(self.b) + ")"

class And :
    
    def __init__(self, a, b) :
        self.a = a
        self.b = b
    
    def interp(self, out, env) :
        return self.a.interp(out, env) and self.b.interp(out, env)
    
    def __str__(self) :
        return "(and " + str(self.a) + " " + str(self.b) + ")"

class Not :
    
    def __init__(self, a) :
        self.a = a
    
    def interp(self, out, env) :
        return not self.a.interp(out, env)
    
    def __str__(self) :
        return "(not " + str(self.a) + ")"

class BinOp :
    
    op_dict = {
            '=='    :   operator.eq,
            '!='    :   operator.not_,
            '<'     :   operator.lt,
            '<='    :   operator.le,
            '>'     :   operator.gt,
            '>='    :   operator.ge,
            '+'     :   operator.add,
            '-'     :   operator.sub,
            '*'     :   operator.mul,
            '/'     :   operator.div
    }
    
    def __init__(self, op, a, b) :
        self.op = op
        self.a = a
        self.b = b
    
    def interp(self, out, env) :
        aval = self.a.interp(out, env)
        bval = self.b.interp(out, env)
        if type(aval) is unicode or type(bval) is unicode :
            return BinOp.op_dict[self.op](unicode(aval), unicode(bval))
        return BinOp.op_dict[self.op](aval, bval)
    
    def __str__(self) :
        return "(" + str(self.op) + " " + str(self.a) + " " + str(self.b) + ")"

class Assign :
    
    op_dict = {
            '='     :   lambda x, y : y,
            '+='    :   operator.add,
            '-='    :   operator.sub,
            '*='    :   operator.mul,
            '/='    :   operator.div,
            '|='    :   operator.or_,
            '&='    :   operator.and_
    }
    
    def __init__(self, base, op, expr) :
        self.base = base
        self.op = op
        self.expr = expr
    
    def interp(self, out, env) :
        value = op_dict[self.op](self.base.interp(out, env), self.expr.interp(out, env))
        self.base.assign(out, env, value)
        return value
    
    def __str__(self) :
        return "(" + self.op + " " + str(self.base) + " " + str(self.expr) + ")"

class Var :
    
    def __init__(self, var) :
        self.var = var
    
    def interp(self, out, env) :
        # Quick hack...
        if (self.var == unicode("skip")) :
            return None
        return env.lookup(self.var)
    
    def assign(self, out, env, value) :
        env.change(self.var, value)
    
    def __str__(self) :
        return "(Var " + str(self.var) + ")"

class Out :
    
    def __init__(self, label, expr) :
        self.label = label
        self.expr = expr
    
    def interp(self, out, env) :
        value = self.expr.interp(out, env)
        out[self.label] = value
        return value
    
    def __str__(self) :
        return "(Out " + str(self.label) + " " + str(self.expr) + ")"

class Prop :
    
    def __init__(self, base, prop) :
        self.base = base
        self.prop = prop
    
    def interp(self, out, env) :
        return getattr(self.base.interp(out, env), self.prop)
    
    def assign(self, out, value) :
        setattr(self.base.interp(out, env), self.prop, value)
        
    def __str__(self) :
        return "(Prop " + str(self.base) + "." + str(self.prop) + ")"

class Call :
    
    def __init__(self, base, func, args) :
        self.base = base
        self.func = func
        self.args = args
    
    def interp(self, out, env) :
        real_args = []
        for a in self.args :
            real_args.append(a.interp(out, env))
        return getattr(self.base.interp(out, env), self.func)(*real_args)
    
    def __str__(self) :
        return "(Call " + str(self.base) + "." + str(self.func) + "(" + str(self.args) + "))"

class If :
    
    def __init__(self, c, t, e) :
        self.c = c
        self.t = t
        self.e = e
    
    def interp(self, out, env) :
        if self.c.interp(out, env) == True :
            return self.t.interp(out, env)
        elif self.e != None :
            return self.e.interp(out, env)
        else :
            return None
    
    def __str__(self) :
        return "(If " + str(self.c) + " " + str(self.t) + " " + str(self.e) + ")"

class Data :
    
    def __init__(self, v) :
        self.v = v
    
    def interp(self, out, env) :
        return self.v
    
    def __str__(self) :
        return "(Data " + str(self.v) + ")"
