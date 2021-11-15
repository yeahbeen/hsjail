
#exit()
import java.lang.System as JSYS
def stop(event):
    Env.removeHotkey(Key.F4, KeyModifier.ALT+KeyModifier.CTRL)
    raise Exception("stop")
    #exit()

Env.addHotkey(Key.F4, KeyModifier.ALT+KeyModifier.CTRL, stop)

r = Region(438,4,928,730)
begin = 0
p0 = 0
def killone():
    global begin,p0
    JSYS.gc()
    Debug.user("begin killone")
    if begin == 0:
        begin = 1
        wait(3)
        r.click(Pattern("1636793815145.png").targetOffset(3,-219))
        m = r.exists(Pattern("1636793930028.png").similar(0.85),1)
        if m:
            Debug.user("found event location")
            p0 = m
        else:
            r.click(Pattern("1636793815145.png").targetOffset(3,-219))
            m = r.exists(Pattern("1636793930028.png").similar(0.85),1)
            if m:
                Debug.user("found event location")
                p0 = m
        Debug.user("p0:"+str(p0))
            
    if not r.exists(Pattern("1636463119063.png").similar(0.65),5):
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
            m = r.exists(Pattern("1636895148499.png").similar(0.86),0)
            if m:
                Debug.user("found guard buff")
                ml.append(m)
            m = r.exists(Pattern("1636908822382.png").similar(0.85),0)
            if m:
                Debug.user("found fighter buff")
                ml.append(m)
            m = r.exists(Pattern("1636560731374.png").similar(0.65).targetOffset(0,42),0)
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
                    r.click(ml[0])
                elif len(ml) == 2:
                    Debug.user("found two")
                    Debug.user("p0:"+str(p0))
                    if p0 == 0:
                        r.click(ml[0])
                    else:
                        d1 = ((ml[0].getTarget().getX()-p0.getTarget().getX())**2 + (ml[0].getTarget().getY()-p0.getTarget().getY())**2)**0.5
                        d2 = ((ml[1].getTarget().getX()-p0.getTarget().getX())**2 + (ml[1].getTarget().getY()-p0.getTarget().getY())**2)**0.5
                        Debug.user("d1:"+str(d1)+" d2:"+str(d2))
                        if d1 < d2:
                            r.click(ml[0])
                        else:
                            r.click(ml[1])
                else:
                    Debug.user("found three or more,click first one")
                    r.click(ml[0])
                wait(Pattern("1636463119063.png").similar(0.65))
    if r.exists(Pattern("1636622387871.png").similar(0.85),0):
        Debug.user("found goto")
        if r.exists("1636632905385.png",0):
            Debug.user("found damage")
            r.click("1636622387871.png")
            wait(5)
            return False
        elif r.exists("1636637579399.png",0):
            Debug.user("found man")
            r.click("1636622387871.png")
            r.click(Pattern("1636637656821.png").targetOffset(-3,-192))
            m = r.wait("1636637686408.png")
            r.click()
            wait(3)
            r.click(m.getTarget())
            return False
        elif r.exists("1636649451418.png",0):
            Debug.user("found relive2")
            r.click("1636622387871.png")
            wait(3)
            return False
    elif r.exists(Pattern("1636637291045.png").similar(0.85),0):
        Debug.user("found open")
        #Debug.user(str(r.getLastMatch()))
        r.click()
        r.wait(Pattern("1636637474771.png").similar(0.85),15)
        r.click()
        wait(3)
        return False       
    elif r.exists(Pattern("1636810941070.png").similar(0.85),0):
        Debug.user("found boom")
        r.click()
        r.wait(Pattern("1636637474771.png").similar(0.85),15)
        r.click()
        wait(3)
        return False
    elif r.exists(Pattern("1636812192170.png").similar(0.85),0):
        Debug.user("found jump")
        r.click()
        wait(3)
        return False
    elif r.exists(Pattern("1636463119063.png").similar(0.85),0):
        Debug.user("found begin")
      #  Debug.user(str(r.getLastMatch()))
        r.click()
        wait(10)
        r.wait("1636463309639.png",120)
        r.click()
        wait(10)
        r.mouseMove(r.getLastMatch().getTarget().below(50))
        while True:
            #match = r.waitBest(60,"1636464480508.png","1636627652819.png")
            #if match:
            #    index = match.getIndex()
            #    Debug.user("found skill "+str(index)) 
            #    if index == 0:      
           #         r.click("1636464480508.png")
           #     else:
           #         r.click("1636627652819.png")
           #         wait(1)
           #         r.click(Pattern("1636627827835.png").targetOffset(-40,49))
           #         r.click("1636464480508.png")
          #  else:
           #     raise  Exception("except 2 skill,found nothing")
            r.wait(Pattern("1636617301631.png").similar(0.83),60)
            Debug.user("found ready,begin find skill")
            if r.exists("1636464480508.png",3):
                Debug.user("click mihouse skill")
                r.click()
            elif r.exists("1636960610601.png",1):
                Debug.user("click mihouse")
                r.click() 
                if r.exists("1636464480508.png",3):
                    r.click()
            else:
                raise  Exception("mierhouse die?")
                
           
            r.wait("1636465531116.png")
            r.click()
            if r.exists("1636537336794.png",3):
                r.click()
            if r.exists("1636537375582.png",3):
                r.click()
            else:
                r.click("1636617301631.png")
            wait(1)
            r.mouseMove(r.getLastMatch().getTarget().below(50))
            wait(10)
            Debug.user("begin wait for vitory")
            match = r.waitBest(20,"1636537561346.png",Pattern("1636617301631.png").similar(0.83))
            Debug.user("stop wait for vitory")
            if match:
                index = match.getIndex()
                Debug.user("found battle "+str(index))
                if index == 0:  
                    Debug.user("one vitory")
                    break
            elif r.exists(Pattern("1636617063422.png").similar(0.85),0):
                    Debug.user("someone die")
                    r.click()
                    wait(1)
                    r.mouseMove(r.getLastMatch().getTarget().below(50))
            else:
                #Debug.user("may be icewall")
                raise  Exception("except vitory or ready or die ,found nothing")

        r.click("1636537561346.png")
        r.waitVanish("1636537561346.png")
        wait(1)
        r.click(r.getLastMatch().getTarget().below(50))
        wait(3)

        if r.exists(Pattern("1636909824055.png").similar(0.85).targetOffset(-6,254),15):
            Debug.user("choose baozang")
            wait(1)
            r.click()
            wait(1)
            r.click()  #sometimes not work,click two
            r.wait("1636538088609.png")
            r.click()
        elif r.exists(Pattern("1636971270760.png").similar(0.83).targetOffset(6,224),1):
            Debug.user("new skill")
            r.click()
            if r.exists(Pattern("1636909824055.png").similar(0.85).targetOffset(-2,258),15):
                Debug.user("choose baozang")
                wait(1)
                r.click()
                wait(1)
                r.click()  #sometimes not work,click two
                r.wait("1636538088609.png")
                r.click()
            
        return False
    else:
        Debug.user("all vitory")
        match = r.exists("1636618067087.png",100)
        if match:
            r.click()
            while r.exists(Pattern("1636618067087.png").similar(0.61),3):
                r.click()
                wait(1)
            r.wait(Pattern("1636972077185.png").similar(0.65))
            r.click()
            wait(1)
            r.click(r.getLastMatch().getTarget().right(200))
            r.wait("1636618478093.png",20)
            r.click()    
            return True 
        else:
            raise  Exception("except vitory gifts ,found nothing")           


Debug.user("all begin")
Settings.WaitScanRate = 1
Settings.ObserveScanRate = 1
if r.exists("1636458791358.png",0):
    r.click()
    match = r.waitBest(30,"1636562183428.png","1636554266474.png")
    if match:
        index = match.getIndex()
        Debug.user("found entry "+str(index))
        if index == 0:
            if not r.exists("1636476191033.png",1):
                r.click("1636476215257.png")
            r.click("1636476247807.png")
        else:
            begin = 1
            while True:
                if killone():
                    break
                
        while True:
           # r.wait(Pattern("1636476713676.png").similar(0.82),10) #2-6
            #r.wait(Pattern("1636970892684.png").similar(0.82),10) #2-3
           # wait(2)
           # r.click(Pattern("1636970892684.png").similar(0.82))
            r.wait(Pattern("1636983307503.png").similar(0.85),10) #hero
            wait(2)
            r.click(Pattern("1636983307503.png").similar(0.85))
            r.wait("1636461252393.png")
            r.click()
            r.wait("1636461300696.png",120)
            r.click()
            r.wait("1636461252393.png")
            r.click()
            if r.exists("1636462599754.png",3):
                r.click("1636463058211.png")
            wait(5)
            begin = 0
            while True:
                if killone():
                    break
                




