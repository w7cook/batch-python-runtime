class Env :
    
    def __init__(self, var, value, env) :
        self.var = var
        self.value = value
        self.env = env
    
    def lookup(self, var) :
        if self.var == var :
            return self.value
        else :
            return self.env.lookup(var)

    def change(self, var, value) :
        if self.var == var :
            self.value = value
        else :
            self.env.change(var, value)

class Closure :
    
    def __init__(self, env, param, code) :
        self.env = env
        self.param = param
        self.code = code
    
    """
    def __call__(self, *args) :
        temp_env = self.env
        pairs = zip(self.params, args)
        for p in pairs :
            temp_env = Env(p[0], p[1], temp_env)
        return self.code.interp(None, temp_env)
    """
    def __call__(self, arg) :
        new_env = Env(self.param, arg, self.env)
        return self.code.interp(None, new_env)

