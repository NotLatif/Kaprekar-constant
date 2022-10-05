#kaprekar bruteforce
def main(order):
    results = {}

    if order == 1:
        results = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[]}

    most_passes = 0
    passes_data = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0}
    unnecessary_calculations = {}
    
    #1. scegliere un numero di 4 cifre in cui almeno 1 è diversa dalle altre
    for x in range(1000,10000):
        digits = str(x)

        #escludere i numeri fatti di cifre uguali
        if digits == len(digits) * digits[0]:
            continue

        res = digits
        passes = 0
        #ripetere finchè il risultato è 6174
        while res != "6174":
            passes += 1

            #A. ordinare le cifre prima in ordine decrescente poi in ordine crescente
            digitList = [*res]
            while len(digitList) < 4:
                digitList.insert(0, '0')

            desc = int("".join(sorted(digitList)[::-1]))
            asc = int("".join(sorted(digitList)))
            
            #B. sottrarre il primo numero dal secondo
            res = str(desc-asc)
        
        n = int("".join(sorted(str(x))))
        if n not in unnecessary_calculations:
            unnecessary_calculations[n] = 1
        else:
            unnecessary_calculations[n] += 1
        
        #aggiungere il numero ai risultati con la quantità di passaggi
        if order == 0:
            results[x] = passes
        elif order == 1:
            results[passes].append(x)

        if passes > most_passes:
            most_passes = passes

        passes_data[passes] += 1

    # output
    with open('results.txt', 'w') as f:
        f.write(f"Most passes: {most_passes}\n")
        for x in passes_data:
            f.write(f"# of results with {x} passes: {passes_data[x]}\n")

        f.write(f"# of times a number was calculated\n")
        for x in unnecessary_calculations:
            f.write(f"\t{x}: {unnecessary_calculations[x]}\n")


        if order == 0:
            #results = {number : passes}
            f.write("String of digits made with all the number of passes needed\n")
            for x in results:
                f.write(f"{results[x]}")
            f.write("\n")

            for x in results:
                f.write(f"{x} ({results[x]} passes)\n")
        
        elif order == 1:
            #results = {passes : [numbers]}
            for x in results:
                f.write(f"Numbers with {x} passes ({len(results[x])}):\n")
                for num in results[x]:
                    f.write(f"\t{num} [{x}]\n")


    print('ok, outputs in the `resutlts.txt` file')


if __name__ == '__main__':
    # different modes also give more/less data
    # 0: ordered by choosen number (crescent)
    # 1: ordered by passes (crescent) then choosen number (crescent)
    
    output_order = 1
    main(output_order)

    # Observations I found
    # 1.
        # each permutation of a number requires the same number of passes to get the result 6174 (easy to find with mode 1)
        #   it is obvious since the algorythm orders your number before doing any operation on it
        #   eg: choosing 4952 is equal to choosing 9254
        #       since both numbers become desc = 9542; asc = 2459 which obviously lead to the same result in the same # of passes
        #   a number can be calculated at most 4! times (4 factorial = 24) 
        #   eg:
        #       1234 has 4! permutations, which means it could be written in 24 ways (since order does not matter)
        #       2233 has 4!/(2!2!) permutations, which means it could be written in 6 ways [2233, 2332, 3322, 3223, 3232, 2323]
        #           which all lead to the same calculations
