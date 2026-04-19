import multiprocessing
import random
import time

def compute_interest(node, principal, years, conn):
    amount=principal
    r=0.07
    random.seed(principal)
    days=years*365
    for i in range(days):
        b=random.uniform(0.001,0.009)
        rate_daily=(r+b)/365.0
        amount*=(1+rate_daily)
        time.sleep(0.001)
    print(f"{node} final amount: {amount:.2f}")
    conn.send(amount)
    other_amt=conn.recv()
    tot=amount+other_amt
    print(f"{node} total amount is: {tot}")
    conn.close()

def main():
    p1=int(input("enter the last 4 digits of ur phone: "))
    p2=int(input("enter last 4 digits of ur friend's phone: "))
    years=int(input("enter number of years: "))
    conn1, conn2=multiprocessing.Pipe()
    nodea=multiprocessing.Process(target=compute_interest, args=("node a",p1,years,conn1))
    nodeb=multiprocessing.Process(target=compute_interest, args=("node b",p2,years,conn2))
    nodea.start()
    nodeb.start()
    nodea.join()
    nodeb.join()

if __name__=="__main__":
    main()