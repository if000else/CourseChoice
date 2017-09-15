import pickle
class A():
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(" %s is talking"%self.name)
class B():
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(" %s is talking"%self.name)
# a = A("alex")
# b = B("rockie")
# obj_list = []
# obj_list.append(a)
# obj_list.append(b)
# with open('objs.db','wb') as f:
#     pickle.dump(obj_list,f)
with open("objs.db",'rb') as f:
    obj = pickle.load(f)
print(obj[1].talk())