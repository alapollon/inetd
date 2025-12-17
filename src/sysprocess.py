import collections, contextlib, select, types

class Task(object):
    def __init__(self, *args):
        self.function=args[0] 
        self.sendvalue=args[1]
        self.callstack=[]
        
    def peek(self):
        _top=self.callstack[-1]
        return type(_top)
    def run(self):
        try: 
            product=self.function.send(self.sendvalue)
            if isinstance(product, SystemCall):
                return 
            if isinstance(product, types.GeneratorType):
                signal=product
                integration=self.sendvalue
                while integrtion == :
                    self.callstack.append(next(signal));
                        
        except:    
                 
def __init__(self):
    self.task_queue=collections.deque()
    self.read_waiting={}
    self.write_waiting={}
    self.numtasks=0
    
    
def new(self, new_task):
    newtask=Task(new_task)
    self.s