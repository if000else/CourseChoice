import pickle
class A():
    def __init__(self,name):
        self.name = name

    def ttt(*args):
        print(len(args))
        print(args[1])
a = A("Dongfang")
setattr(a,"age",18)
setattr(a,"sex","man")
# b = A("Yizhong")
pickle.dump(a,open('pictest.db','wb'))
# a= pickle.load(open("pictest.pkl",'rb'))
print()
