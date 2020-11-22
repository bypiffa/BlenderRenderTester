# Impoorting Modules
import os
from subprocess import *
import datetime
import platform


commands = []
def completer(text, state):
    options = [i for i in commands if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

try:
    import readline
    readline.parse_and_bind("tab: complete")
    readline.set_completer(completer)
except:
    print("NO TABS, SORRY!")

# Starttttiiinnnggg Remduring
def timestring(tleft):
    #print "tleft", tleft
    
    tleftX = tleft
    
    tleft = int(tleftX)
    
    addend = tleftX - tleft
    
                                   
    valt = str(tleft)
    #print valt , "VALT HERE1"
    if tleft > 60 :
        le = tleft
        tleft = int(tleft / 60)
        le = le - int(tleft * 60)
        
        stleft = "0"*(2-len(str(tleft)))+str(tleft)
        sle = "0"*(2-len(str(le)))+str(le)
        
        valt = stleft+":"+ sle
    
        if tleft > 60 :
            lele = le
            le = tleft
            tleft = int(tleft / 60)
            le = le - int(tleft * 60)
            lele = (lele - le)
            if lele < 0:
                lele = int(lele * -1)
            
            stleft = "0"*(2-len(str(tleft)))+str(tleft)
            sle = "0"*(2-len(str(le)))+str(le)
            slele = "0"*(2-len(str(lele)))+str(lele)
            
            valt = stleft+":"+ sle + ":" + slele
    
            if tleft > 24 :
                le = tleft
                tleft = int(tleft / 24)
                le = le - int(tleft * 24)
                valt = str(tleft)+" DAYS AND "+ str(le) + " HRS"
    return valt + "." + str(int(addend*100))

def to_sec(text):
    text = text.split(":")
    m = float(text[0])
    s = float(text[1])
    
    ret = s + ( m * 60 )
    return ret

# System
system = "Ubuntu 20.04.1 LTS" # EDIT THIS TOO 

# Blender Versions
BlenderVer = {
"2.81":"/home/vcs/Software/BlenderVer/blender-2.81a-linux-glibc217-x86_64/blender",
"2.83":"/home/vcs/Software/BlenderVer/blender-2.83.8-linux64/blender",
"2.90.1":"blender",
"2.92":"/home/vcs/Software/BlenderVer/blender-2.92.0-c4d8f6a4a8dd-linux64/blender"
}

# Blender Demo Files loocation ( oones downlooaded from Blender.org )
BlendFiles = {
"Agent327":"/home/vcs/Desktop/BlenderTestFiles/FromBlenderOrg/Agent327/splash279.blend",
"BlenderMan":"/home/vcs/Desktop/BlenderTestFiles/FromBlenderOrg/BlenderMan/Blenderman.blend",
"FishyCat":"/home/vcs/Desktop/BlenderTestFiles/FromBlenderOrg/FishyCat/fishy_cat.blend",
"PartyTug600AM":"/home/vcs/Desktop/BlenderTestFiles/FromBlenderOrg/PartyTug600AM.blend",
"RacingCar":"/home/vcs/Desktop/BlenderTestFiles/FromBlenderOrg/RacingCar.blend",
"SplashFox":"/home/vcs/Desktop/BlenderTestFiles/FromBlenderOrg/SplashFox.blend",
"Spring":"/home/vcs/Desktop/BlenderTestFiles/FromBlenderOrg/Spring.blend",
"TheJunkShop":"/home/vcs/Desktop/BlenderTestFiles/FromBlenderOrg/TheJunkShop.blend"
}


configurations = []

print("options   - see all available options")
print("configure - configure file for rendering")
print("list      - list configured files")
print("render    - start rendering")
print("exit      - abandon and exit")

# Configuration state
while True:
    
    commands = ["exit", "configure", "render", "options", "list"]
    
    com = input(": ")
    
    if com == "exit":
        exit()
    
    elif com == "options":
        print("Blender Versions:\n")
        for i in BlenderVer:
            print(i)
        print()
        print("Blend Files:\n")
        for i in BlendFiles:
            print(i)
        print()
        
    elif com == "configure":
        commands = ["All"]
        for i in BlenderVer:
            commands.append(i)
        ver      = input("Blender Version : ")
        if ver not in BlenderVer and ver != "All":
            print("Version Chosed not in the list! Use options to see list.")
            continue
        commands = ["All"]
        for i in BlendFiles:
            commands.append(i)
        filename = input("File : ")
        if filename not in BlendFiles and filename != "All":
            print("File Chosed not in the list! Use options to see list.")
            continue
        commands = []
        amount   = input("Amount : ")
        try:
            amount = int(amount)
        except:
            print("Amount should be a number.")
            continue
        
        configurations.append([ver, filename, int(amount)])
    
    elif com == "list":
        for i in configurations:    
            print("Blender Version: "+i[0]+" File: "+i[1]+" Amount: "+str(i[2]))
    
    elif com == "render":
        break
    
    elif len(com) > 0:
        print("Error! Command not found!")
    


for configuration in configurations:
    
    ChooseV = configuration[0]
    ChooseF = configuration[1]
    ChooseT = configuration[2]
    
    
    for version in BlenderVer:
        if ChooseV == version or ChooseV == "All":
            for filename in BlendFiles:
                if ChooseF == filename or ChooseF == "All":
                    
                    times = []
                    openingtime = []
                    savingtime = []
                    
                    
                    for t in range(ChooseT):
                        
                        start = datetime.datetime.now()
                        #os.system(BlenderVer[ChooseV]+" -b "+BlendFiles[ChooseF]+" -f 1")
                        r = Popen(['stdbuf', '-o0',  BlenderVer[version],"-b",BlendFiles[filename],"-f","-1"], stdout=PIPE, universal_newlines=True)
                        
                        print("Rendering", version, filename, "Frame:",  t+1, "..." )    
                        
                        x = r.stdout.readline()[:-1]
                        retopen = 0
                        retsaving = "Crashed"
                        while x:
                            
                            if "Fra:" in x and retopen == 0:
                                opening = datetime.datetime.now()
                                opening = opening - start
                            
                                s = opening.seconds
                                m = opening.microseconds
                                
                                retopen = ((s*1000000)+m)/1000000
                                
                            elif "Saving:" in x:
                                
                                retsaving = x[x.find("Saving:")+8:-1]
                            
                            x = r.stdout.readline()[:-1]
                            #print("FROM BLENDER: "+r.stdout.readline()[:-1])
                        r.kill()
                        #r.wait()
                        
                        
                        end = datetime.datetime.now()
                        
                        rendTime = end - start
                        
                        
                        openingtime.append(retopen)
                        savingtime.append(to_sec(retsaving))
                        
                        # NO RENDERS ABOVE 24 HOURS WILL SHOW THE CORRET TIME
                        
                        s = rendTime.seconds
                        m = rendTime.microseconds
                        
                        ret = ((s*1000000)+m)/1000000
                        print (t+1, "Finished" ,timestring(ret))
                        times.append(ret)

                    maxv = 0
                    for i in times:
                        if i > maxv:
                            maxv = i
                            
                    minv = maxv
                    for i in times:
                        if i < minv:
                            minv = i

                    avat = sum(times)/len(times)

                    try:
                        odata = open("Data_Times.txt")
                        odata = odata.read()
                    except:
                        odata = ""
                     
                    data = open("Data_Times.txt", "w")
                    data.write(odata+"\n\n")
                    
                    
                    dateformat = "%Y/%m/%d"
                    
                    data.write("+-------------------------------------------------------------------------------------------+\n")
                    
                    data.write("| ")
                    t = "Blender "+version
                    data.write(t[:20]+" "*(20-len(t)))
                    data.write(" | ")
                    t = filename
                    data.write(t[:20]+" "*(20-len(t)))
                    data.write(" | ")
                    t = system
                    data.write(t[:20]+" "*(20-len(t)))
                    data.write(" | ")
                    t = datetime.datetime.strftime(datetime.datetime.today(), dateformat)
                    data.write(t[:20]+" "*(20-len(t)))
                    data.write(" |\n")
                    
                    data.write("+-------------------------------------------------------------------------------------------+\n")
                    data.write("+-------------------------------------------------------------------------------------------+\n")
                    data.write("| Descriptor:          | Minimum              | Average              | Maximum              |\n")
                    data.write("+-------------------------------------------------------------------------------------------+\n")
                    
                    data.write("| ")
                    t = "Render Time"
                    data.write(t[:20]+" "*(20-len(t)))
                    data.write(" | ")
                    t = timestring(minv)
                    data.write(t[:20]+" "*(20-len(t)))
                    data.write(" | ")
                    t = timestring(avat)
                    data.write(t[:20]+" "*(20-len(t)))
                    data.write(" | ")
                    t = timestring(maxv)
                    data.write(t[:20]+" "*(20-len(t)))
                    data.write(" |\n")
                    
                    
                    
                    maxv = 0
                    for i in openingtime:
                        if i > maxv:
                            maxv = i
                            
                    minv = maxv
                    for i in openingtime:
                        if i < minv:
                            minv = i

                    avat = sum(openingtime)/len(openingtime)
                    
                    
                    
                    data.write("| ")
                    t = "Opening Blender Time"
                    data.write(t[:20]+" "*(20-len(t)))
                    data.write(" | ")
                    t = timestring(minv)
                    data.write(t[:20]+" "*(20-len(t)))
                    data.write(" | ")
                    t = timestring(avat)
                    data.write(t[:20]+" "*(20-len(t)))
                    data.write(" | ")
                    t = timestring(maxv)
                    data.write(t[:20]+" "*(20-len(t)))
                    data.write(" |\n")
                    
                    maxv = 0
                    for i in savingtime:
                        if i > maxv:
                            maxv = i
                            
                    minv = maxv
                    for i in savingtime:
                        if i < minv:
                            minv = i

                    avat = sum(savingtime)/len(savingtime)
                    
                    
                    
                    data.write("| ")
                    t = "Saving Image Time"
                    data.write(t[:20]+" "*(20-len(t)))
                    data.write(" | ")
                    t = timestring(minv)
                    data.write(t[:20]+" "*(20-len(t)))
                    data.write(" | ")
                    t = timestring(avat)
                    data.write(t[:20]+" "*(20-len(t)))
                    data.write(" | ")
                    t = timestring(maxv)
                    data.write(t[:20]+" "*(20-len(t)))
                    data.write(" |\n")
                    
                    data.write("+-------------------------------------------------------------------------------------------+\n")
                    data.write("+-------------------------------------------------------------------------------------------+\n")
                    data.write("| Frame                | Render Time          | Opening Blender Time | Saving Image Time    |\n")
                    data.write("+-------------------------------------------------------------------------------------------+\n")
                    
                    
                    for num,  frame in enumerate(times):
                    
                        data.write("| ")
                        t = str(num+1)
                        data.write(t[:20]+" "*(20-len(t)))
                        data.write(" | ")
                        t = timestring(frame)
                        data.write(t[:20]+" "*(20-len(t)))
                        data.write(" | ")
                        t = timestring(openingtime[num])
                        data.write(t[:20]+" "*(20-len(t)))
                        data.write(" | ")
                        t = timestring(savingtime[num])
                        data.write(t[:20]+" "*(20-len(t)))
                        data.write(" |\n")
                    
                    data.write("+-------------------------------------------------------------------------------------------+\n")
                    data.close()
                    
                    
                    data = open("Data_Times.txt")
                    data = data.read()
                    
                    data = data.replace(odata, "")
                    print(data)
                    
                    
                    
                    
    
