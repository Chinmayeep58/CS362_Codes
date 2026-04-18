import json
import time

def main():
    with open('seed.json', 'r') as f:
        data = json.load(f)

    theta=data['theta']
    clocks=data['clocks']
    queues=data['queues']
    N=len(clocks)

    print(f"Initial clocks: {clocks}")
    print(f"Tolerance theta: {theta}")
    time.sleep(1)

    print("\nClock Alignment")
    T0=clocks[0]
    S=[]
    for i in range(N):
        if abs(clocks[i] - T0)<=theta:
            S.append(i)
    print(f"Trusted subset of nodes: {S}")
    T_target=sum(clocks[i] for i in S) // len(S)
    print(f"Target Time (T_target): {T_target}")
    time.sleep(1)
    T_sync =[]
    for i in range(N):
        if i in S:
            delta=T_target-clocks[i]
        else:
            delta=0
        T_sync.append(clocks[i] + delta)
        print(f"Node {i}: initial={clocks[i]}, delta={delta}, sync={T_sync[-1]}")
        time.sleep(0.2)

    print("\nMessage Ordering")
    V=[[0] * N for _ in range(N)]
    buffers=[[] for _ in range(N)]

    for i in range(N):
        print(f"\n[Node {i}] Processing incoming queue")
        for count, msg in enumerate(queues[i]):
            j=msg['sender']
            v_msg=msg['v_msg']
            print(f"Received msg from Node {j} with V_msg={v_msg}")
            time.sleep(0.1)
            buffers[i].append(msg)
            progress=True
            while progress:
                progress=False
                for b_msg in buffers[i]:
                    sender=b_msg['sender']
                    sender_v_msg=b_msg['v_msg']
                    cond1=(sender_v_msg[sender]==V[i][sender]+1)
                    cond2 = all(sender_v_msg[k]<=V[i][k] for k in range(N) if k!=sender)
                    if cond1 and cond2:
                        print(f"Processing buffered msg from Node {sender}. Conditions met")
                        for k in range(N):
                            V[i][k]=max(V[i][k], sender_v_msg[k])
                        buffers[i].remove(b_msg)
                        progress=True
                        time.sleep(0.1)
                        break 

        if buffers[i]:
            print(f"Messages still stuck in buffer: {len(buffers[i])}")
        print(f"Final Vector Clock for Node {i}: {V[i]}")
        time.sleep(0.5)

    print("\nFinal Payload")
    for i in range(N):
        sum_v=sum(V[i])
        payload=(T_sync[i] * sum_v) % 9973
        print(f"Node {i}: Final Clock={T_sync[i]}, sum(V)={sum_v}, Payload P_i={payload}")
        time.sleep(0.2)

if __name__=='__main__':
    main()