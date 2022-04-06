from functools import wraps

def kwargs_only(cls):
    
    @wraps(cls)
    def call(**kwargs):
        return cls(**kwargs)
    
    return call
