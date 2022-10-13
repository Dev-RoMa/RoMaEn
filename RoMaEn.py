import time as tm, sys, subprocess as sp, logging as log

log.basicConfig(filename='DNS_history.log', encoding='utf-8', level=log.DEBUG)

twidth = 20

print("welcome ! \(^-^)~")
print("welcome to RoMa Essentials")
print("This is a pack of my most")
print("used tools")


# setup toolbar
sys.stdout.write("[%s]" % (" " * twidth))
sys.stdout.flush()
sys.stdout.write("\b" * (twidth+1))

for i in range(twidth):
    tm.sleep(0.25)
    sys.stdout.write("/")
    sys.stdout.flush()

sys.stdout.write("]\n")

while True:
    print("1.- Storage Check")
    print("2.- Networking Troubleshooting")    
    print("5.- Leet Translator")
    print("6.- File Finder")
    print("7.- Package Installer")
    print("8.- Fun Tools")
    print("9.- Exit :C")
    try:
        op = int(input(" Select an option = "))
        if op == 1:
            print("your hard drives are = ")
            sp.call("wmic logicaldisk get name", shell=True)
            input("press enter to continue")
            
        if op == 2:
            print(" welcome to Network ")
            print(" 1.- Ip options ")
            print(" 2.- DNS options ")
            print(" 3.- troubleshoot ")
            print(" 4.- leave Network Options ")
            op2=int(input("options = "))
            if op2 == 1:                
                print(" Here you will check your ip")
                print("1.- check your current ip")
                print("2.- see all the ip information")
                print("3.- renew the ip")
                print("4.- check your DNS ")
                print("5.- check your MAC")
                print("6.- exit ip menu ")
                print(" '(^-^)' ")
                try:
                    op2_2=int(input(" Select an Ip option "))
                    if op2_2 == 1:
                        sp.call("ipconfig | findstr IP", shell = True)
                        input("press enter to continue")
                        print(" Here u have more info regarding your ip")
                        print(" 1.- DNS ")
                        print(" 2.- MAC Adress ")
                        print(" 3.- fuck go back ")
                        try:
                            op2_21 = int(input("1.- Desired Option "))
                            if op2_21 == 1:
                                sp.call(" ipconfig | findstr DNS", shell = True)
                            elif op2_21 ==2:
                                sp.call (" getmac ", shell = True)
                            elif op2_21 ==3:
                                print(" okay (^-^)")
                                input("press enter")
                                op == 2
                        except:
                            print("")
                    elif op2_2 == 2:
                        sp.call("ipconfig/all", shell = True)
                        input("press enter to continue")
                    elif op2_2 == 3:
                        print(" do you want to refresh ur interface? ")
                        print("1.- yes\n2.- no")
                        try:
                            interfaceRenew = int(input(" option = "))
                        except:
                            print("")
                        if interfaceRenew == 1:
                            isRenewLocked == True
                        else:
                            isRenewLocked == False
                        sp.call("ipconfig/renew", shell = True)
                        isRenewLocked = ""
                        if isRenewLocked == True:
                            sp.call("ipconfig/release")
                            sp.call('ipconfig/renew "Wi-Fi"')
                        else:
                            sp.call("ipconfig/release")
                            sp.call("ipconfig/renew")
                        input("press enter to continue")
                    elif op2_2 == 4:
                        sp.call(" ipconfig | findstr DNS", shell = True)
                        input("press enter to continue")
                    elif op2_2 == 5:
                        sp.call (" getmac ", shell = True)
                        input("press enter to continue")
                    elif op2_2 == 6:
                        print("okay (^w-w^)")
                except:
                    print("")

            elif op2 == 2:
                print(" welcome to the DNS options")
                print(" 1.- Check your DNS history ")
                print(" 2.- Check website DNS ")
                print(" 3.- Exit DNS options ")
                try:
                    op2_3 = int(input(" option = "))
                    if op2_3 == 1:
                        print(" do you want to save all this info?")
                        try:
                            op2_3_1 = int(input("1.- yes\n2.- no \n Option = "))
                        except:
                            print("yes or no")
                        if op2_3_1 == 1:
                            sp.call("ipconfig/displaydns | clip", shell = True)
                            log.debug()
                            input("press enter ")
                        elif op2_3_1 == 2:
                            sp.call("ipconfig/displaydns", shell = True)
                            input("press enter ")
                        else:
                            print("")
                    if op2_3 == 2:
                        print(" this will check any website u input")
                        dnsweb=input("which website do u wanna check? = ")
                        sp.call(f"nslookup {dnsweb}", shell = True)
                        input("press enter to continue")
                        print("welcome to DNS options")                                                
                except:
                    print("")

            elif op2 == 3:
                print(" welcome to the network troubleshoot")
                print(" here u will be able to do some stuff")
                print(" to your network, like if ur internet is")
                print(" up and such")
                print("1.- ping a website (4 packages) ")
                print("2.- tracert a website (30 packages)")
                try:
                    op4 = int(input(" Select an option = "))
                    if op4 == 1:
                        netweb = input(" please insert a website/ip adress = ")
                        sp.call(f" ping {netweb}", shell = True)
                        input("press enter to continue")
                    elif op4 == 2:
                        netweb = input(" please insert a website/ip adress = ")
                        sp.call(f"tracert {netweb}", shell = True)
                        input("press enter to continue")
                except:
                    print("")
        if op == 5:
            print("leet")
        if op == 6:
            print("finder")
        if op == 7:
            print("installer")
        if op == 8:
            print("fun")
        if op == 9:
            print("bye o/")
            break
    except:
        print("")

#sp.call("ipconfig/all")
#sp.call("ipconfig/renew")