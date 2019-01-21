# Main loop to control tier 1 tasks
# Updates every 60sec

from Data_Collection import data_collection
import sched, time, datetime

s = sched.scheduler(time.time, time.sleep)
def Loop(sc):
    # Intro
    now1 = datetime.datetime.now()
    print("*Doing stuff*", now1)

    # Tasks
    data_collection()
    
    #

    # Outro
    now = datetime.datetime.now()
    print("*Done with stuff*")
    now2= datetime.datetime.now()
    #
    print("Time elapsed", now2-now1)
    print("\n")
    s.enter(1,1, Loop, (sc,))

#s.enter(1, 1, Loop, (s,))
#s.run()