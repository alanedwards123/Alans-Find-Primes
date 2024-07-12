# build array of test numbers

primelist = []

# assume all numbers are prime to start with

for primebuilder in range(100) :
    primelist.append(primebuilder)
    
# outerloop i the test number, innerloop is the testing divisor, 1 up to the test number

for outerloop in range(100) :
    for innerloop in range(1, outerloop) :
        if innerloop == 1 :
            continue

        primeresult = outerloop % innerloop

        if primeresult == 0 : # if the test divided by the tester has remainder zero number is not a prime so remove it from the prime list
            primelist.remove(outerloop)

            break
    
print (primelist)
   