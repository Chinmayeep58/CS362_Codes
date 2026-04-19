def time_to_seconds(time):
    h,m,s=map(int,time.split(':'))
    return h*3600+m*60+s

def seconds_to_time(tot_seconds):
    h=int(tot_seconds//3600)
    m=int((tot_seconds%3600)//60)
    s=int(tot_seconds%60)
    return f"{h:02d}:{m:02d}:{s:02d}"

def berkeley(clocks):
    print("berkeley algorithm")
    clock_secs={node:time_to_seconds(t) for node, t in clocks.items()}
    master=clock_secs["master"]
    diff={node:time-master for node, time in clock_secs.items()}
    for node, d in diff.items():
        print(f"{node}:{d:>3} s")
    
    avg_diff=sum(diff.values())/len(diff)
    target_time=master+avg_diff
    for node in clocks:
        adjust=target_time-clock_secs[node]
        new_time=clock_secs[node]+adjust
        print(f"{node}: adjusted by {adjust:>4} s -> new time: {seconds_to_time(new_time)}")

if __name__=="__main__":
    clocks={"master":"10:00:00","node1":"10:00:10","node2":"09:59:50","node3":"10:00:20"}
    berkeley(clocks)