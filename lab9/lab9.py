import multiprocessing
import random
import time

def compute_interest(name, principal, years, conn):
    amount=principal
    r=0.07
    random.seed(principal)
    days=years*365
    for _ in range(days):
        b=random.uniform(0.001, 0.009)
        rate_daily=(r+b)/365.0
        amount*=(1+rate_daily)
        time.sleep(0.001)
    print(f"[{name}] Final Amount: {amount:.2f}")
    conn.send(amount)
    other_amount=conn.recv()
    total=amount+other_amount
    print(f"[{name}] Total after consensus: {total:.2f}")
    conn.close()


if __name__=="__main__":
    P1=int(input("Enter last 4 digits of your phone number: "))
    P2=int(input("Enter last 4 digits of your friend's phone number: "))
    years=int(input("Enter number of years: "))
    conn1, conn2=multiprocessing.Pipe()
    nodeA=multiprocessing.Process(
        target=compute_interest,
        args=("Node A", P1, years, conn1)
    )
    nodeB=multiprocessing.Process(
        target=compute_interest,
        args=("Node B", P2, years, conn2)
    )
    nodeA.start()
    nodeB.start()
    nodeA.join()
    nodeB.join()