while(True):
    p=input('''which calculator you want to use:
press 1 for standard calculator
press 2 for scintific calculator\n''')
    if(p=='1'):
        a=float(input('Enter I value:'))
        b=float(input('Enter II value:'))
        c=input('''What you want to d0:
press + for addition
press - for subtraction
press * for multiplication
press / for division\n''')
        if(c=='+'):
            print(a+b)
        elif(c=='-'):
            print(a-b)
        elif(c=='*'):
            print(a*b)
        elif(c=='/'):
            print(a/b)
        else:
            print('invalid entry')
    elif(p=='2'):
        a=input('''which operations you want to do:
press 1 for power of any number
press 2 for trignometric operation
press 3 for logarithmic operation\n''')
        if(a=='1'):
            b=float(input('enter the number:'))
            c=float(input('enter the power:'))
            print(a**b)
        elif(a=='2'):
            from math import sin,cos,tan,pi,asin,acos,atan,radians
            b=input('''which trignometric function to use:
press 1 for trignometric function
press 2 for inverse tignometric function ''')
            if(b=='1'):
                c=input('''for calculating
type sin for sine function
type cos for cosine function
type tan for tan function
type cot for cot function
type sec for sec fnction
type cosec for cosec function\n''')
                d=float(input('enter the angle in degree:'))
                e=radians(d)
                if(c=='sin'):
                    print(sin(e))
                elif(c=='cos'):
                    print(cos(e))
                elif(c=='tan'):
                    print(tan(e))
                elif(c=='cot'):
                    print(1/tan(e))
                elif(c=='sec'):
                    print(1/cos(e))
                elif(c=='cosec'):
                    print(1/sin(e))
                else:
                    print('invalid entry')
            elif(b=='2'):
                c=input('''for calculating
press 1 for inverse of sin
press 2for inverse of cos
press 3 for inverse of tan
press 4 for inverse of cot
press 5 for inverse of sec
press 6 for inverse of cosec\n''')
                d=float(input('enter the angle in degree:'))
                e=radians(d)
                if(c=='1'):
                    print(asin(e))
                elif(c=='2'):
                    print(acos(e))
                elif(c=='3'):
                    print(atan(e))
                elif(c=='4'):
                    print(1/atan(e))
                elif(c=='5'):
                    print(1/acos(e))
                elif(c=='6'):
                    print(1/asin(e))
                else:
                    print('invalid entry')
            else:
                print('invalid entry')
        elif(a=='3'):
            from math import log,log2,log10
            b=input('''decide the base of log
press e for natural base
press 2 for base 2
press 10 for base 10\n''')
            c=float(input('enter the number to find log:'))
            if(b=='e'):
                print(log(c))
            elif(b=='2'):
                print(log2(c))
            elif(b=='10'):
                print(log10(c))
            else:
                print('invalid entry')
    else:
        print('invalid entry')
    d=input('''are you want to use calculator more
press 1 for yes
press any key for exit\n''')
    if(d=='1'):
        continue 
    else:
        break         
        
    
            
            
                
            
                

        
        
        
    
    
    
        
