## Exercise

###a) Create a folder on your laptop called "polynomial" and initialize it as a git repo. Create a public empty repo on your github called "polynomial". 
# In your local git folder, add a remote called "origin" pointing to the github repo you just created. 
# Create a file called "polynomial.py" with the following code:

###python
class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)


poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)
###```

### add and commit this file with the following message "cs 506 exercise part a". Push these changes to github.

### b) Write an `evaluate` method to each class that can evaluate the polynomial for a given value of `X`.

### ```python
### poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
### print(poly.evaluate(-1))
### ```

###This should return the **integer** solution when `X = -1`.

### When you're done with this part, add and commit the changes with the message "cs 506 exercise part b".

### c) Provide the link to this github repo in the [following form](https://forms.gle/gbPLms6LBHXhUtif6)