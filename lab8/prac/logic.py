class Process:
    def __init__(self, pid, tot_process):
        self.pid=pid
        self.lamport=0
        self.vector=[0]*tot_process

    def internal_event(self,event_name):
        self.lamport+=1
        self.vector[self.pid]+=1
        self.display(f"Internal ({event_name})")
        
    def send_event(self,event_name):
        self.lamport+=1
        self.vector[self.pid]+=1
        self.display(f"send ({event_name})")
        return self.lamport, list(self.vector)

    def receive_event(self,event_name, msg_lamport, msg_vector):
        self.lamport=max(self.lamport,msg_lamport)+1
        for k in range(len(self.vector)):
            self.vector[k]=max(self.vector[k],msg_vector[k])
        self.vector[self.pid]+=1
        self.display(f"receive ({event_name})")

    def display(self,action):
        print(f"P{self.pid} {action:<22} Lamport: {self.lamport} Vector: {self.vector}")

if __name__=="__main__":
    p0=Process(pid=0,tot_process=3)
    p1=Process(pid=1,tot_process=3)
    p2=Process(pid=2,tot_process=3)
    p0.internal_event("create order")
    l1,v1=p0.send_event("to p1")
    p1.receive_event("from p0",l1,v1)
    l2,v2=p1.send_event("to p2")
    p2.receive_event("from p1",l2,v2)
    p0.internal_event("send email")