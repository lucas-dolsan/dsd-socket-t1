from functools import wraps

# Notice: keep in mind that this will change the class type from class to function
def kwargs_only(cls):
    
    @wraps(cls)
    def call(**kwargs):
        return cls(**kwargs)
    
    return call
