
#exit()
import json
import java.lang.System as JSYS

beginchacter = True
p0 = 0
running = True
die = False

chacter = "2-3"
#chacter = "2-6"
#chacter = "h1-1"
mode = "task1"
count = 11111
team = "fire"
#team = "house"

def stop(event):
    Debug.user("stop")
    global running 
    running = False
    #Env.removeHotkey(Key.F4, KeyModifier.ALT+KeyModifier.CTRL)
    #raise Exception("stop")
    #exit()
def start(event):
    Debug.user("start")
    global running
    running = True
Env.addHotkey(Key.F4, KeyModifier.ALT+KeyModifier.CTRL, stop)
Env.addHotkey(Key.F3, KeyModifier.ALT+KeyModifier.CTRL, start)

r = Region(438,4,928,730)

def saveconfig():
    global configfile,config
    with open(configfile,"w") as f:
        f.write(json.dumps(config))

def killone():
    global beginchacter,p0,running,die,config,team
    JSYS.gc()
    Debug.user("begin killone")
    saveconfig()
    # if not r.exists("1636554266474.png",10):
        # Debug.user("all vitory")
        # match = r.exists("1636618067087.png",30)
        # if match:
            # r.click()
            # wait(1)
            # n = 1
            # while n<5:
                # if r.exists(Pattern("1636618067087.png").similar(0.61),5):
                    # r.click()
                    # wait(1)
                # else:
                    # break
                # n+=1
            # Debug.user(str(n))
            # r.wait(Pattern("1636972077185.png").similar(0.63))
            # r.click()
            # wait(1)
            # r.click(r.getLastMatch().getTarget().right(200))
            # r.wait("1636618478093.png",20)
            # r.click()
            # config["count"] += 1
            # saveconfig()
            # return True 
        # else:
            # raise  Exception("except vitory gifts ,found nothing")           
    r.wait(Pattern("1636554266474.png").similar(0.80),10)
    #wait(2)
    if beginchacter and p0 == 0:
        beginchacter = False
        wait(5)
        scrollm = r.wait(Pattern("1636793815145.png").targetOffset(0,-1),3)
        #r.click(Pattern("1636793815145.png").targetOffset(3,-219))
        if r.exists(Pattern("1637659896820.png").targetOffset(-14,-28),1):
            r.click()
        m = r.exists(Pattern("1636793930028.png").similar(0.85),2)
        if m:
            Debug.user("found event location")
            p0 = m
        else:
            #r.click(Pattern("1636793815145.png").targetOffset(3,-219))
            if r.exists(Pattern("1637070819341.png").targetOffset(-4,61),1):
                r.click()
            m = r.exists(Pattern("1636793930028.png").similar(0.85),2)
            if m:
                Debug.user("found event location")
                p0 = m
        Debug.user("p0:"+str(p0))
        r.click(scrollm)
            
    if not r.exists(Pattern("1636463119063.png").similar(0.65),4):
        if r.exists(Pattern("1636560833523.png").similar(0.80),0):
            Debug.user("found event")
            r.click()
            wait(Pattern("1636463119063.png").similar(0.65))
        else:
            ml = []
            m = r.exists(Pattern("1636562437138.png").similar(0.85),0)
            if m:
                Debug.user("found relive")
                ml.append(m)
            m = r.exists(Pattern("1636637179334.png").similar(0.85),0)
            if m:
                Debug.user("found mega buff")
                ml.append(m)
            m = r.exists(Pattern("1637481122448.png").similar(0.85),0)
            if m:
                Debug.user("found guard buff")
                ml.append(m)
            m = r.exists(Pattern("1636908822382.png").similar(0.85),0)
            if m:
                Debug.user("found fighter buff")
                ml.append(m)
            m = r.exists(Pattern("1636560731374.png").similar(0.63).targetOffset(0,42),0)
            if m:
                Debug.user("found guard")
                ml.append(m)
            m = r.exists(Pattern("1636808764498.png").similar(0.65).targetOffset(0,43),0)
            if m:
                Debug.user("found mega")
                ml.append(m)
            m = r.exists(Pattern("1636810845176.png").similar(0.65).targetOffset(1,47),0)
            if m:
                Debug.user("found figter")
                ml.append(m)
                #r.click(Pattern("1636621973283.png").similar(0.65).targetOffset(-1,48)Pattern("1636799311336.png").similar(0.65).targetOffset(5,46))
            if len(ml) == 0:
                Debug.user("shoud be vitory")
            else:
                if len(ml) == 1:
                    Debug.user("found only one")
                    config["foundone"] += 1
                    capture(r,"foundone"+time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()))
                    #popup("found only one")
                    r.click(ml[0])
                elif len(ml) == 2:
                    Debug.user("found two")
                    Debug.user("p0:"+str(p0))
                    if p0 == 0:
                        r.click(ml[0])
                    else:
                        d1 = ((ml[0].getTarget().getX()-p0.getTarget().getX())**2 + (ml[0].getTarget().getY()-p0.getTarget().getY())**2)**0.5
                        d2 = ((ml[1].getTarget().getX()-p0.getTarget().getX())**2 + (ml[1].getTarget().getY()-p0.getTarget().getY())**2)**0.5
                        Debug.user("d1:"+str(round(d1))+" d2:"+str(round(d2)))
                        if d1 < d2:
                            r.click(ml[0])
                        else:
                            r.click(ml[1])
                else:
                    Debug.user("found three or more,click first one")
                    config["foundmore"] += 1
                    capture(r,"foundmore"+time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()))
                    #popup("found more")
                    r.click(ml[0])
                wait(Pattern("1636463119063.png").similar(0.65))
    if r.exists(Pattern("1636622387871.png").similar(0.85),0):
        Debug.user("found goto")
        if r.exists("1636632905385.png",0):
            Debug.user("found damage")
            config["damage"] += 1
            r.click("1636622387871.png")
            wait(5)
            return False
        elif r.exists("1636637579399.png",0):
            Debug.user("found man")
            config["man"] += 1
            global mode
            if mode == "task":
                answer = popAsk('found man,please deal with it,then click "yes" to continue or "no" to exit',"man")
                if answer:
                    #running = False
                    return False
                else:
                    raise Exception("exit")
            else:
                r.click("1636622387871.png")
                r.wait(Pattern("1638548402726.png").targetOffset(0,-196))
                #if r.exists("1637382643968.png",1):
                if r.exists("1638179643270.png",1):
                    r.click()
                else:
                    r.click(Pattern("1638548402726.png").targetOffset(0,-196))
                m = r.wait(Pattern("1638548495369.png").similar(0.85))
                r.click()
                wait(3)
                r.click(m)
                return False
        elif r.exists("1636649451418.png",0):
            Debug.user("found relive2")
            config["relive"] += 1
            r.click("1636622387871.png")
            wait(3)
            return False
    elif r.exists(Pattern("1636637291045.png").similar(0.85),0):
        Debug.user("found open")
        config["buff"] += 1
        #Debug.user(str(r.getLastMatch()))
        r.click()
        r.wait(Pattern("1636637474771.png").similar(0.85),15)
        r.click()
        wait(3)
        return False       
    elif r.exists(Pattern("1636810941070.png").similar(0.85),0):
        Debug.user("found boom")
        config["boom"] += 1
        r.click()
        r.wait(Pattern("1636637474771.png").similar(0.85),15)
        r.click()
        wait(3)
        return False
    elif r.exists(Pattern("1636812192170.png").similar(0.85),0):
        Debug.user("found jump")
        config["jump"] += 1
        r.click()
        wait(3)
        return False
    elif running and r.exists(Pattern("1636463119063.png").similar(0.85),0):
        Debug.user("found begin")
        config["monster"] += 1
        r.click()
        wait(10)
        r.wait("1636463309639.png",120)
        wait(1)
        r.click()
        wait(10)
        r.mouseMove(r.getLastMatch().getTarget().below(50))
        while running:
            r.wait(Pattern("1638529396165.png").similar(0.81),60)
            if team == "house":
                Debug.user("found ready,begin find skill")
                if r.exists("1636464480508.png",3):
                    Debug.user("click mihouse skill")
                    r.click()
                elif r.exists("1636960610601.png",1):
                    Debug.user("click mihouse")
                    r.click() 
                    if r.exists("1636464480508.png",3):
                        r.click()
                #else:
                #    raise  Exception("mierhouse die?")
               
                if r.exists("1636465531116.png",3):
                    r.click()
                if r.exists("1636537336794.png",3):
                    r.click()
                if die:
                    if r.exists(Pattern("1637065392229.png").similar(0.83),3):
                        r.click(Pattern("1637065392229.png").similar(0.83))
                    elif r.exists(Pattern("1637065432935.png").similar(0.82),1):
                        r.click()
            elif team == "fire":
                Debug.user("found ready,begin find skill")
                tmpr = Region(441,0,925,377)
                if r.exists(Pattern("1637665051380.png").similar(0.80),3):
                    Debug.user("click antoni skill")
                    r.click()
                    wait(1)
                    if tmpr.exists(Pattern("1637665470674.png").targetOffset(-1,-49),0):
                        Debug.user("found antoni target")
                        tmpr.click()
                    else:
                        Debug.user("found label one")
                        tmpr.click(Pattern("1637665565894.png").targetOffset(-35,51))
                elif r.exists(Pattern("1637665117001.png").similar(0.65),1):
                    Debug.user("click antoni")
                    r.click() 
                    if r.exists("1637665051380.png",3):
                        r.click()
                        wait(1)
                        if tmpr.exists(Pattern("1637665470674.png").targetOffset(-1,-49),0):
                            Debug.user("found antoni target")
                            tmpr.click()
                        else:
                            Debug.user("found label one")
                            tmpr.click(Pattern("1637665565894.png").targetOffset(-35,51))
                else:
                    raise  Exception("antoni die?")
               
                if r.exists(Pattern("1637665171551.png").similar(0.80),3):
                    r.click()
                if r.exists(Pattern("1637665202508.png").similar(0.80),3):
                    r.click()
                if die:
                    if r.exists("1636537336794.png",3):
                        r.click()
            if r.exists("1638529453496.png",5):
                r.click()
            else:
                r.click("1638529396165.png")
            wait(1)
            r.mouseMove(r.getLastMatch().getTarget().below(50))
            wait(10)
            Debug.user("begin wait for vitory")
            match = r.waitBest(20,"1636537561346.png",Pattern("1638529396165.png").similar(0.81))
            Debug.user("stop wait for vitory")
            if match:
                index = match.getIndex()
                Debug.user("found battle "+str(index))
                if index == 0:  
                    Debug.user("one vitory")
                    break
            elif r.exists(Pattern("1636617063422.png").similar(0.84),0):
                    Debug.user("someone die")
                    die = True
                    r.click()
                    wait(1)
                    r.mouseMove(r.getLastMatch().getTarget().below(50))
            else:
                raise  Exception("except vitory or ready or die ,found nothing")

        r.click("1636537561346.png")
        r.waitVanish("1636537561346.png")
        wait(1)
        r.click(r.getLastMatch().getTarget().below(50))
        wait(3)

        #if r.exists(Pattern("1636909824055.png").similar(0.85).targetOffset(-198,258),15):
        if r.exists(Pattern("1650338917731.png").targetOffset(197,195),15):
            Debug.user("choose baozang")
            wait(1)
            r.click()
            wait(1)
            r.click()  #sometimes not work,click two
            #r.wait("1638527032741.png")
            r.wait("1650338964661.png")
            r.click()
            wait(1)
            r.mouseMove(r.getLastMatch().getTarget().right(50))     
        elif r.exists(Pattern("1636971270760.png").similar(0.83).targetOffset(6,224),1):
            Debug.user("new skill")
            r.click()
            if r.exists(Pattern("1636909824055.png").similar(0.85).targetOffset(-205,262),15):
                Debug.user("choose baozang")
                wait(1)
                r.click()
                wait(1)
                r.click()  #sometimes not work,click two
                r.wait("1636538088609.png")
                r.click()
        #return False
        else:
            Debug.user("all vitory")
            match = r.exists(Pattern("1638528794517.png").similar(0.61),30)
            if match:
                r.click()
                wait(1)
                n = 1
                while n<5:
                    if r.exists(Pattern("1638528794517.png").similar(0.61),5):
                        r.click()
                        wait(1)
                    else:
                        break
                    n+=1
                Debug.user(str(n))
                r.wait(Pattern("1636972077185.png").similar(0.63))
                r.click()
                wait(1)
                r.click(r.getLastMatch().getTarget().right(200))
                r.wait("1636618478093.png",20)
                r.click()
                config["count"] += 1
                saveconfig()
                return True 
            else:
                raise  Exception("except vitory gifts ,found nothing")           
        return False

def begin():
    global beginchacter,running,die,p0,team
    if r.exists("1637648575958.png"):
        r.click()
        wait("1636458791358.png",10)
    if r.exists("1636458791358.png",0):
        r.click()
        match = r.waitBest(30,"1636562183428.png","1636554266474.png")
        if match:
            index = match.getIndex()
            Debug.user("found entry "+str(index))
            if index == 0:
                if r.exists(Pattern("1637411268783.png").targetOffset(-3,34),0):
                    r.click()
                    wait(2)
                cht = chacter.split("-")
                if cht[0][0] == "h":
                    hero = True
                    cha = cht[0][1]
                else:
                    hero = False
                    cha = cht[0]
                Debug.user("hero:"+str(hero)+",chacter:"+cha)
                if cha == "1":
                    if r.exists("1637411404753.png",1):
                        r.click()
                        #wait(1)
                elif cha == "2":
                    Debug.user("ddddd")
                    if r.exists(Pattern("1636476215257.png").similar(0.60),1):
                        Debug.user("eeeee")
                        r.click()
                wait(1)
                if hero:
                    if not r.exists("1637937985256.png",0):
                        r.click("1637413230484.png")
                else:
                    if r.exists("1637937985256.png",0):
                        r.click("1637413181948.png")
                wait(1)
                    
                r.click("1636476247807.png")
            else:
                while running:
                    if killone():
                        break
    elif r.exists("1636554266474.png",0):
        while running:
            if killone():
                break
                    
    #while running:
    for i in range(count):
        if not running: break
        if chacter == "2-6":
            r.wait(Pattern("1637415818173.png").similar(0.82),10) #2-6
            wait(2)
            r.click(Pattern("1637415818173.png").similar(0.82))
        elif chacter == "2-3" or chacter == "h2-3":
            #r.wait(Pattern("1636970892684.png").similar(0.82),10) #2-3
            #wait(2)
            #r.click(Pattern("1636970892684.png").similar(0.82))
            r.wait(Pattern("1638082420228.png").similar(0.85),10) #2-3
            wait(2)
            r.click(Pattern("1638082420228.png").similar(0.85))  
        elif chacter == "h1-1":
            r.wait(Pattern("1636983307503.png").similar(0.85),10) #hero
            wait(2)
            r.click(Pattern("1636983307503.png").similar(0.85))
        r.wait("1636461252393.png")
        r.click()
        if team == "house":
            r.wait("1636461300696.png",120)
        elif team == "fire":
            r.wait("1637664904162.png",120)
        r.click()
        r.wait("1636461252393.png")
        r.click()
        if r.exists("1636462599754.png",3):
            r.click("1636463058211.png")
        #r.wait("1636554266474.png",10)
        #wait(2)
        beginchacter = True
        die = False
        p0 = 0
        Debug.user("begin chacter")
        while running:
            if killone():
                break
    if running:
        return True
    else:
        return False


Debug.user("all begin")
Settings.WaitScanRate = 1
Settings.ObserveScanRate = 1
configfile = "config.json"
config = {}
try:
    with open(configfile) as f:
        config = json.loads(f.read())
except Exception as e:
    config = {}
    config["man"] = 0
    config["boom"] = 0
    config["damage"] = 0
    config["jump"] = 0
    config["relive"] = 0
    config["buff"] = 0
    config["monster"] = 0
    config["foundone"] = 0
    config["foundmore"] = 0
    config["count"] = 0


while True:
    if begin():
        break
    wait(1)

                




