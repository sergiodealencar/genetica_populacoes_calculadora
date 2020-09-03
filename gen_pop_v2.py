import math
print('''\n--- Frequency Calculations of Autosomal Recessive Disease using Hardy-Weinberg Equations ---\n''')

opt = (int(input('''What information do you have? Select one of the following options:\n
\t1: Dominant allele frequency (A)
\t2: Recessive allele frequency (a)
\t3: Homozygous Dominant frequency (AA)
\t4: Homozygous Recessive frequency (aa)
\t5: Disease frequency in the population of interest
\t6: Proportion of population that has the disease
\n\tOption: ''')))

if opt == 1:
    freqA = float(input('\nWhat is the frequency of the dominant allele (in %)? '))
    freqA2 = freqA/100
    freqa = 1 - freqA2
    hom_AA = freqA2 * freqA2
    hom_aa = freqa * freqa
    het_freq = 2 * freqA2 * freqa
    # print('\nThe dominant allele frequency (A) is {:.1f}%' .format(freqA2 * 100))
    print('\nThe recessive allele frequency (a) is {:.1f}%' .format(freqa * 100))
    print('The dominant homozygous frequency (AA) is {:.1f}%' .format(hom_AA * 100))
    print('The recessive homozygous frequency (aa) is {:.1f}%' .format(hom_aa * 100))
    print('The heterozygous frequency (Aa) is {:.1f}%' .format(het_freq*100))

elif opt == 2:
    freqa = float(input('\nWhat is the frequency of the recessive allele (in %)? '))
    freqa2 = freqa/100
    freqA = 1 - freqa2
    hom_AA = freqA * freqA
    hom_aa = freqa2 * freqa2
    het_freq = 2 * freqA * freqa2
    print('\nThe dominant allele frequency (A) is {:.1f}%' .format(freqA * 100))
    # print('The recessive allele frequency (a) is {:.1f}%' .format(freqa2 * 100))
    print('The dominant homozygous frequency (AA) is {:.1f}%' .format(hom_AA * 100))
    print('The recessive homozygous frequency (aa) is {:.1f}%' .format(hom_aa * 100))
    print('The heterozygous frequency (Aa) is {:.1f}%' .format(het_freq*100))

elif opt == 3:
    homAA = float(input('\nWhat is the frequency of the homozygous dominant genotype (AA) (in %)? '))
    homAA2 = homAA/100
    freqA = math.sqrt(homAA2)
    freqa = 1 - freqA
    hom_aa = freqa * freqa
    het_freq = 2 * freqA * freqa
    print('\nThe dominant allele frequency (A) is {:.1f}%' .format(freqA * 100))
    print('The recessive allele frequency (a) is {:.1f}%' .format(freqa * 100))
    # print('The dominant homozygous frequency (AA) is {:.1f}%' .format(hom_AA * 100))
    print('The homozygous recessive frequency (aa) is {:.1f}%' .format(hom_aa * 100))
    print('The heterozygous frequency (Aa) is {:.1f}%' .format(het_freq*100))

elif opt == 4:
    homaa = float(input('\nWhat is the frequency of the homozygous recessive genotype (aa) (in %)? '))
    homaa2 = homaa/100
    freqa = math.sqrt(homaa2)
    freqA = 1 - freqa
    hom_AA = freqA * freqA
    het_freq = 2 * freqA * freqa
    print('\nThe dominant allele frequency (A) is {:.1f}%' .format(freqA * 100))
    print('The recessive allele frequency (a) is {:.1f}%' .format(freqa * 100))
    print('The dominant homozygous frequency (AA) is {:.1f}%' .format(hom_AA * 100))
    # print('The homozygous recessive frequency (aa) is {:.1f}%' .format(hom_aa * 100))
    print('The heterozygous frequency (Aa) is {:.1f}%' .format(het_freq * 100))

elif opt == 5:
    freq_dis = float(input('\nWhat is the frequency of the disease in the population of interest (example: 6.4%)? '))
    freq_dis2 = freq_dis/100
    q = math.sqrt(freq_dis2)
    p = 1 - q
    hom_p2 = p * p
    hom_q2 = q * q
    het_freq = 2 * p * q
    print('\nThe dominant allele frequency (A) is {:.1f}%' .format(p * 100))
    print('The recessive allele frequency (a) is {:.1f}%' .format(q * 100))
    print('The homozygous dominant frequency (AA) is {:.1f}%' .format(hom_p2*100))
    print('The homozygous recessive frequency (aa) is {:.1f}%' .format(hom_q2*100))
    print('The heterozygous frequency (Aa) is {:.1f}%' .format(het_freq*100))

elif opt == 6:
    freq_dis0 = input('\nWhat is the frequency of the disease in the population of interest (example: 1 in 7200)? ')
    list = freq_dis0.split(" in ")
    numer = float(list[0])
    denom = float(list[1])
    freq_dis2 = float(numer / denom)
    q = math.sqrt(freq_dis2)
    p = 1 - q
    hom_p2 = p * p
    hom_q2 = q * q
    het_freq = 2 * p * q
    print('\nThe dominant allele frequency (A) is {:.1f}%' .format(p * 100))
    print('The recessive allele frequency (a) is {:.1f}%' .format(q * 100))
    print('The homozygous dominant frequency (AA) is {:.1f}%' .format(hom_p2*100))
    print('The homozygous recessive frequency (aa) is {:.1f}%' .format(hom_q2*100))
    print('The heterozygous frequency (Aa) is {:.1f}%' .format(het_freq*100))







opt2 = input('\nWould you like to know the probability that a couple will have a child with this disease (yes/no)? ')
if opt2 == ('yes'):
    opt3 = input('\nIs the mother or the father affected by the disease (yes/no)? ')
    if opt3 == ('yes'):
        prob = (0.5 * het_freq) * 100
        print('\nThe probability that their child will have the disease is {:.2f}%. \nIn case the other member of the couple is known to not be a carrier of the recessive allele, the probability will be 0%'.format(prob))
    else:
        prob = ((0.5 * het_freq) * (0.5 * het_freq)) * 100
        prob2 = ((0.5 * het_freq) * 0.5) * 100
        prob3 = 25
        print('\nThe probability that their child will have the disease is {:.2f}%. \nIn case one of the members of the couple is known to be a carrier of the recessive allele, the probability will be {:.2f}%.\nIn case both mother and father are known to be carriers of the recessive allele, the probability will be {:.2f}%.' .format(prob, prob2, prob3))
else:
    print('\n--- END ---')




