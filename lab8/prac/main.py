import json
import time

def main():
    with open('./seed.json','r') as file:
        data=json.load(file)

    theta=data['theta']
    clocks=data['clocks']
    queues=data['queues']
    n=len(clocks)

    print(f"initials clocks: {clocks}")
    print(f"tolerance theta: {theta}")
    time.sleep(1)
    print("\nclock alignment")
    t0=clocks[0]
    nodes=[]
    for c in range(n):
        if abs(clocks[c]-t0)<=theta:
            nodes.append(c)
    print(f"trusted set of nodes: {nodes}")
    target= sum(clocks[i] for i in nodes) //len(nodes)
    print(f"target time is: {target}")
    time.sleep(1)
    sync=[]
    for i in range(n):
        if i in nodes:
            delta=target-clocks[i]
        else:
            delta=0
        sync.append(clocks[i]+delta)
        print(f"node {i}: initial={clocks[i]}, delta={delta}, sync={sync[-1]}")
        time.sleep(0.2)
    print("\nmessage ordering")
    v=[[0]*n for i in range(n)]
    buff=[[] for i in range(n)]
    for i in range(n):
        print(f"\n node {i} processing incoming queue")
        for count, msg in enumerate(queues[i]):
            j=msg['sender']
            v_msg=msg['v_msg']
            print(f"received msg from node {j} with v_msg: {v_msg}")
            buff[i].append(msg)
            progress=True
            while progress:
                progress=False
                for b in buff[i]:
                    sender=b['sender']
                    sender_msg=b['v_msg']
                    cond1=(sender_msg[sender]==v[i][sender]+1)
                    cond2=all(sender_msg[k]<=v[i][k] for k in range(n) if k!=sender)
                    if cond1 and cond2:
                        print(f"processing buffered msg from node {sender}. conditions met")
                        for k in range(n):
                            v[i][k]=max(v[i][k],sender_msg[k])
                        buff[i].remove(b)
                        progress=True
                        break
        if buff[i]:
            print(f"messages still stuck in buffer: {len(buff[i])}")
        print(f"final vector clock for node {i}: {v[i]}")
    print("\nfinal payload")
    for i in range(n):
        vsum=sum(v[i])
        payload=(sync[i]*vsum)%9973
        print(f"node {i}: final clock: {sync[i]}, sum: {vsum}, payload: {payload}")

if __name__=="__main__":
    main()
    