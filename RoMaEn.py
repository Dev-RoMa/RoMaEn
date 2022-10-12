import time as tm, sys, subprocess as sp

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
    print("2.- Ip options")
    print("3.- DNS options")
    print("4.- Networking Troubleshooting")
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
            print(" Here you will check your ip")
            print("1.- check your current ip")
            print("2.- see all the ip information")
            print("3.- renew the ip")
            print("4.- exit ip menu ")
            print(" '(^-^)' ")
            try:
                op2=int(input(" Select an Ip option "))
                if op2 == 1:
                    sp.call("ipconfig", shell = True)
                    input("press enter to continue")
                elif op2 == 2:
                    sp.call("ipconfig/all", shell = True)
                    input("press enter to continue")
                elif op2 == 3:
                    sp.call("ipconfig/renew", shell = True)
                    input("press enter to continue")
                elif op2 == 4:
                    print("okay (^w-w^)")
            except:
                print("")
        if op == 3:
            print(" welcome to the DNS options")
            print(" this will check any website u input")
            dnsweb=input("which website do u wanna check? = ")
            sp.call(f"nslookup {dnsweb}", shell = True)
            input("press enter to continue")
        if op == 4:
            print(" welcome to the network troubleshoot")
            print(" here u will be able to do some stuff")
            print(" to your network, like if ur internet is")
            print(" up and such")
            print("1.- ping a website (4 packages) ")
            print("2.- tracert a website (30 packages)")
            try:
                op4 = int(input(" Select an option = "))
                netweb = input(" please insert a website/ip adress = ")
                if op4 == 1:
                    sp.call(f" ping {netweb}", shell = True)
                    input("press enter to continue")
                elif op4 == 2:
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