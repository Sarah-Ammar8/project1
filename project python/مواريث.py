
def man():
    _wife='لا'
    wife=input('هل يوجد زوجة (نعم-لا) : ')
    #wife=الزوجة
    if wife=='نعم':
        n_wife=int(input('ادخل عدد الزوجات : '))
    # n_wife= عدد الزوجات
    elif wife !='نعم':
        wife=_wife
        n_wife=0

    _father='لا'
    father =(input('هل يوجد أب (نعم-لا) : '))
    # father=الأب
    if father !='نعم':
        father=_father
        n_father=0

    _mother = 'لا'
    mother = input('هل يوجد أم (نعم-لا) : ')
    # mother=الأم
    if mother !='نعم':
        mother=_mother
        n_mother=0

    _grand_m='لا'
    grand_m=input('هل يوجد أم ألأم (نعم-لا) : ')
    #grand_m=الجدة من الام
    if grand_m !='نعم':
        grand_m=_grand_m
        n_grand_m=0

    _grand_f='لا'
    grand_f = input('هل يوجد جد "أب الأب" (نعم-لا) : ')
    # grand_f=الجد من الأب
    if grand_f !='نعم':
        grand_f=_grand_f
        n_grand_f=0

    _grand_f_f='لا'
    grand_f_f = input('هل يوجد جد "أب أب الأب" (نعم-لا) : ')
    # grand_f_f=جد أب الأب
    if grand_f_f !='نعم':
        grand_f_f=_grand_f_f
        n_grand_f_f=0

    _m_f='لا'
    m_f = input('هل يوجد جد أم الأب (نعم-لا) : ')
    # m_f= جد أم الأب
    if m_f !='نعم':
        m_f=_m_f
        n_m_f=0

    _m_m_m='لا'
    m_m_m = input('هل يوجد أم أم الأم (نعم-لا) : ')
    # m_m_m= أم أم الأم
    if m_m_m !='نعم':
        m_m_m=_m_m_m
        n_m_m_m=0

    _m_f_f = 'لا'
    m_f_f = input('هل يوجد جد أم أب الأب (نعم-لا) : ')
    # m_f_f= أم أب الأب
    if m_f_f !='نعم':
        m_f_f=_m_f_f
        n_m_f_f=0

    _m_m_f = 'لا'
    m_m_f = input('هل يوجد أم أم الأب (نعم-لا) : ')
    # m_m_f= أم أم الأب
    if m_m_f !='نعم':
        m_m_f=_m_m_f
        n_m_m_f=0

    _dut='لا'
    dut = input('هل يوجد ابنة (نعم-لا) : ')
    # dut= ابنة
    if dut == 'نعم':
        n_dut = int(input('ادخل عدد البنات : '))
    # n_dut= عدد ابنة
    elif dut !='نعم':
        dut=_dut
        n_dut=0

    _son='لا'
    son = input('هل يوجد ابن (نعم-لا) : ')
    # son=  ابن
    if son == 'نعم':
        n_son = int(input('ادخل عدد الابناء : '))
    # n_son= عدد ابن
    elif son !='نعم':
        son=_son
        n_son=0

    _d_d='لا'
    d_d = input('هل يوجد بنت ابن (نعم-لا) : ')
    # d_d= بنت ابن
    if d_d == 'نعم':
        n_d_d = int(input('ادخل عددهن : '))
    # n_d_d= عدد بنت ابن
    elif d_d !='نعم':
        d_d=_d_d
        n_d_d=0

    _s_d = 'لا'
    s_d = input('هل يوجد ابن ابن (نعم-لا) : ')
    # s_d= ابن ابن
    if s_d == 'نعم':
        n_s_d = int(input('ادخل عددهم : '))
    # n_s_d= عدد ابن ابن
    elif s_d !='نعم':
        s_d=_s_d
        n_s_d=0

    _d_s_d = 'لا'
    d_s_d = input('هل يوجد بنت ابن ابن (نعم-لا) : ')
    # d_s_d= بنت ابن ابن
    if d_s_d == 'نعم':
        n_d_s_d = int(input('ادخل عددهن : '))
    # n_d_s_d= عدد بنت ابن ابن
    elif d_s_d !='نعم':
        d_s_d=_d_s_d
        n_d_s_d=0

    _s_s_d='لا'
    s_s_d = input('هل يوجد ابن ابن ابن (نعم-لا) : ')
    # s_s_d= ابن ابن ابن
    if s_s_d == 'نعم':
        n_s_s_d = int(input('ادخل عددهم : '))
    # n_s_s_d= عدد ابن ابن ابن
    elif s_s_d !='نعم':
        s_s_d=_s_s_d
        n_s_s_d=0

    _sister='لا'
    sister = input('هل يوجد أخت شقيقة (نعم-لا) : ')
    # sister= أخت شقيقة
    if sister == 'نعم':
        n_sister = int(input('ادخل عددهن : '))
    # n_sister=عدد أخت شقيقة
    elif sister !='نعم':
        sister=_sister
        n_sister=0

    _brother='لا'
    brother = input('هل يوجد أخ شقيق (نعم-لا) : ')
    # brother= أخ شقيق
    if brother == 'نعم':
        n_brother = int(input('ادخل عددهم : '))
    # n_brother= عدد أخ شقيق
    elif brother !='نعم':
        brother=_brother
        n_brother=0

    _sister_f='لا'
    sister_f = input('هل يوجد أخت لأب (نعم-لا) : ')
    # sister_f= أخت لأب
    if sister_f == 'نعم':
        n_sister_f = int(input('ادخل عددهن : '))
    # n_sister_f= عدد أخت لأب
    elif sister_f !='نعم':
        sister_f=_sister_f
        n_sister_f=0

    _brother_f='لا'
    brother_f = input('هل يوجد أخ لأب (نعم-لا) : ')
    # brother_f= أخ لأب
    if brother_f == 'نعم':
        n_brother_f = int(input('ادخل عددهم : '))
    # n_brother_f= عدد أخ لأب
    elif brother_f !='نعم':
        brother_f=_brother_f
        n_brother_f=0

    _sister_m='لا'
    sister_m = input('هل يوجد أخت لأم (نعم-لا) : ')
    # sister_m= أخت لأم
    if sister_m == 'نعم':
        n_sister_m = int(input('ادخل عددهن : '))
    # n_sister_m= عدد أخت لأم
    elif sister_m !='نعم':
        sister_m=_sister_m
        n_sister_m=0

    _brother_m='لا'
    brother_m = input('هل يوجد أخ لأم (نعم-لا) : ')
    # brother_m= أخ لأم
    if brother_m == 'نعم':
        n_brother_m = int(input('ادخل عددهم : '))
    # n_brother_m= عدد أخ لأم
    elif brother_m !='نعم':
        brother_m=_brother_m
        n_brother_m=0

    _d_b='لا'
    d_b = input('هل يوجد ابن أخ لأب (نعم-لا) : ')
    # d_b=  ابن أخ لأب
    if d_b == 'نعم':
        n_d_b = int(input('ادخل عددهم : '))
    # n_d_b= عدد ابن أخ لأب
    elif d_b != 'نعم':
        d_b = _d_b
        n_d_b = 0

    _d_b_ = 'لا'
    d_b_ = input('هل يوجد ابن أخ شقيق (نعم-لا) : ')
    # d_b_=  ابن أخ شقيق
    if d_b_ == 'نعم':
        n_d_b_ = int(input('ادخل عددهم : '))
    # n_d_b_= عدد ابن أخ شقيق
    elif d_b_ != 'نعم':
        d_b_ = _d_b_
        n_d_b_ = 0

    _d_d_b='لا'
    d_d_b = input('هل يوجد ابن ابن أخ لأب (نعم-لا) : ')
    # d_d_b= ابن ابن أخ لأب
    if d_d_b == 'نعم':
        n_d_d_b = int(input('ادخل عددهم : '))
    # n_d_d_b=عدد ابن ابن أخ لأب
    elif d_d_b != 'نعم':
        d_d_b = _d_d_b
        n_d_d_b = 0

    _d_d_b_ = 'لا'
    d_d_b_ = input('هل يوجد ابن ابن أخ شقيق (نعم-لا) : ')
    # d_d_b_= ابن ابن أخ شقيق
    if d_d_b_ == 'نعم':
        n_d_d_b_ = int(input('ادخل عددهم : '))
    # n_d_d_b_=  عدد ابن ابن أخ شقيق
    elif d_d_b_ != 'نعم':
        d_d_b_ = _d_d_b_
        n_d_d_b_ = 0

    _uncle_='لا'
    uncle_ = input('هل يوجد عم لأب  (نعم-لا) : ')
    # uncle_= عم لأب
    if uncle_ == 'نعم':
        n_uncle_ = int(input('ادخل عددهم : '))
    # n_uncle_= عدد عم لأب
    elif uncle_ != 'نعم':
        uncle_ = _uncle_
        n_uncle_ = 0

    _uncle = 'لا'
    uncle = input('هل يوجد عم شقيق (نعم-لا) : ')
    # uncle= عم شقيق
    if uncle == 'نعم':
        n_uncle = int(input('ادخل عددهم : '))
    # n_uncle= عدد عم شقيق
    elif uncle != 'نعم':
        uncle = _uncle
        n_uncle = 0

    _cousin='لا'
    cousin = input('هل يوجد ابن عم للأب (نعم-لا) : ')
    # cousin=  ابن عم للأب
    if cousin == 'نعم':
        n_cousin = int(input('ادخل عددهم : '))
    # n_cousin= عدد ابن عم للأب
    elif cousin != 'نعم':
        cousin = _cousin
        n_cousin = 0

    _cousin_='لا'
    cousin_ = input('هل يوجد ابن عم شقيق (نعم-لا) : ')
    # cousin_=  ابن عم شقيق
    if cousin_ == 'نعم':
        n_cousin_ = int(input('ادخل عددهم : '))
    # n_cousin_=  عدد ابن عم شقيق
    elif cousin_ != 'نعم':
        cousin_ = _cousin_
        n_cousin_ = 0

    _cousin_c='لا'
    cousin_c = input('هل يوجد ابن ابن عم للأب (نعم-لا) : ')
    # cousin_c= ابن ابن عم للأب
    if cousin_c == 'نعم':
        n_cousin_c = int(input('ادخل عددهم : '))
    # n_cousin_c= عدد ابن ابن عم للأب
    elif cousin_c != 'نعم':
        cousin_c = _cousin_c
        n_cousin_c = 0

    _cousin_c_='لا'
    cousin_c_ = input('هل يوجد ابن ابن عم شقيق (نعم-لا) : ')
    # cousin_c_= ابن ابن عم شقيق
    if cousin_c_ == 'نعم':
        n_cousin_c_ = int(input('ادخل عددهم : '))
    # n_cousin_c_=عدد ابن ابن عم شقيق
    elif cousin_c_ == '':
        cousin_c_ = _cousin_c_
        n_cousin_c_ = 0

    _uncle_f_f='لا'
    uncle_f_f = input('هل يوجد عم للأب "أخ الجد للأب" (نعم-لا) : ')
    #uncle_f_f= " عم للأب "أخ الجد للأب
    if uncle_f_f == 'نعم':
        n_uncle_f_f = int(input('ادخل عددهم : '))
    # n_uncle_f_f= عدد " عم للأب "أخ الجد للأب
    elif uncle_f_f != 'نعم':
        uncle_f_f = _uncle_f_f
        n_uncle_f_f = 0

    _uncle_f='لا'
    uncle_f = input('هل يوجد عم للأب "شقيق الجد" (نعم-لا) : ')
    #uncle_f= " عم الاب "شقيق الجد
    if uncle_f == 'نعم':
        n_uncle_f = int(input('ادخل عددهم : '))
    # n_uncle_f= عدد " عم الاب "شقيق الجد
    elif uncle_f != 'نعم':
        uncle_f = _uncle_f
        n_uncle_f = 0


    print('************************************************************************')
    print('**التركة = ', money)
    print('**الديون = ', deon)
    print('**التركة بعد تسديد الديون = ', money - deon)
    print('*زوجة: ', wife,'   *العدد: ', n_wife)
    print('أب: ', father)
    print('أم: ', mother)
    print('أم ألأم: ', grand_m)
    print('جد "أب الأب": ', grand_f)
    print('جد "أب أب الأب": ', grand_f_f)
    print('جد أم الأب: ', m_f)
    print('أم أم الأم: ', m_m_m)
    print('أم أب الأب: ', m_f_f)
    print('أم أم الأب: ', m_m_f)
    print()
    print('*ابنة: ', dut, '   *العدد: ', n_dut)
    print('*ابن: ', son, '   *العدد: ', n_son)
    print('*بنت ابن: ', d_d, '   *العدد: ', n_d_d)
    print('*ابن ابن: ', s_d, '   *العدد: ', n_s_d)
    print('*بنت ابن ابن: ', d_s_d, '   *العدد: ', n_d_s_d)
    print('*ابن ابن ابن: ', s_s_d, '   *العدد: ', n_s_s_d)
    print('*أخت شقيقة: ', sister, '   *العدد: ', n_sister)
    print('*أخ شقيق: ', brother, '   *العدد: ', n_brother)
    print('*أخت لأب: ', sister_f, '   *العدد: ', n_sister_f)
    print('*أخ لأب: ', brother_f, '   *العدد: ', n_brother_f)
    print('*أخت لأم: ', sister_m, '   *العدد: ', n_sister_m)
    print('*أخ لأم: ', brother_m, '   *العدد: ', brother_m)
    print('*ابن أخ لأب: ', d_b, '   *العدد: ', n_d_b)
    print('*ابن أخ شقيق: ', d_b_, '   *العدد: ', n_d_b_)
    print('*ابن ابن أخ لأب: ', d_d_b, '   *العدد: ', n_d_d_b)
    print('*ابن ابن أخ شقيق: ', d_d_b_, '   *العدد: ', n_d_d_b_)
    print('*عم لأب: ', uncle_, '   *العدد: ', n_uncle_)
    print('*عم شقيق: ', uncle, '   *العدد: ', n_uncle)
    print('*ابن عم لأب: ', cousin, '   *العدد: ', n_cousin)
    print('*ابن عم شقيق: ', cousin_, '   *العدد: ', n_cousin_)
    print('*ابن ابن عم للأب (نعم-لا): ', cousin_c, '   *العدد: ', n_cousin_c)
    print('*ابن ابن عم شقيق (نعم-لا): ', cousin_c_, '   *العدد: ', n_cousin_c_)
    print('*عم لأب "أخ الجد لأب": ', uncle_f_f, '   *العدد: ', n_uncle_f_f)
    print('*عم لأب "شقيق الجد": ', uncle_f, '   *العدد: ', n_uncle_f)
    print('************************************************************************')

    if wife== 'نعم' and son != 'نعم' :
        if dut != 'نعم' and d_d != 'نعم' and s_d != 'نعم':
            if d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم' and brother != 'نعم':
                if sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم' and brother_m != 'نعم':
                    if d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم' and d_d_b_ != 'نعم':
                        if uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم' and cousin_ != 'نعم':
                            if cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم' and uncle_f != 'نعم':
                                if father!='نعم' and mother!='نعم':
                                    if grand_m != 'نعم' and grand_f != 'نعم' and grand_f_f != 'نعم' and m_f != 'نعم':
                                        if m_m_m != 'نعم' and m_f_f != 'نعم' and m_m_f != 'نعم':
                                            w_wife = (money-deon) / n_wife
                                            print(w_wife, ' = (', n_wife, 'نصيب الزوجة/ات(')

    elif wife == 'نعم':
            # الاصل
            if son == 'نعم' or dut == 'نعم' or d_d == 'نعم' or s_d == 'نعم' or d_d_b == 'نعم' or s_s_d == 'نعم':
                # الفروع
                w_wife = (money-deon)*(1 / 8)
                print(w_wife,' = (',n_wife,'نصيب الزوجة/ات(')

            elif son != 'نعم' and dut != 'نعم' and d_d != 'نعم' and s_d != 'نعم' and d_d_b != 'نعم' and s_s_d != 'نعم':
                w_wife = 1 / 4
                w_wife = (money-deon) * (1 / 4)
                print(w_wife, ' = (', n_wife, 'نصيب الزوجة/ات(')
    elif wife != 'نعم':
        w_wife=0

    if mother=='نعم':
        if dut != 'نعم' and wife != 'نعم' and d_d != 'نعم' :
            if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم' :
                if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم' :
                    if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم' :
                        if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم' :
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم' :
                                if uncle_f != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                    if father != 'نعم' and grand_f != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                        if m_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم' and m_m_f != 'نعم':
                                            if mother != 'نعم':
                                                w_mother = (money-deon)
                                                print(w_mother, 'نصيب الأم = ')
    elif mother == 'نعم':
            # الاصل
            if son != 'نعم' and dut != 'نعم' and d_d != 'نعم' and s_d != 'نعم' and d_d_b != 'نعم' and s_s_d != 'نعم':
                #w_mother = 1 / 3
                w_mother = (money - deon-w_wife) * (1 / 3)
                print(w_mother, 'نصيب الأم = ')
            if grand_m=='نعم':
                w_grand_m=0
                print(w_grand_m, 'نصيب أم الأم = ')
            if m_f=='نعم':
                w_m_f = 0
                print(w_m_f, 'نصيب أم الاب = ')
            if m_m_m=='نعم':
                w_m_m_m = 0
                print(w_m_m_m, 'نصيب أم أم الأم = ')
            if m_f_f=='نعم':
                w_m_f_f = 0
                print(w_m_f_f, 'نصيب أم أب الأب = ')
            if m_m_f=='نعم':
                w_m_m_f = 0
                print(w_m_m_f, 'نصيب أم أم الأب = ')
            if son == 'نعم' or dut == 'نعم' or d_d == 'نعم' or s_d == 'نعم' or d_d_b == 'نعم' or s_s_d == 'نعم':
                # الفروع
                #w_mother = 1 / 6
                w_mother = (money-deon-w_wife)*(1 /6)
                print(w_mother,'نصيب الأم = ')



    if father=='نعم':
        if dut != 'نعم' and wife != 'نعم' and d_d != 'نعم' :
            if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم' :
                if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم' :
                    if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم' :
                        if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم' :
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم' :
                                if uncle_f != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                    if mother != 'نعم' and grand_f != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                        if m_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم' and m_m_f != 'نعم':
                                            w_father = (money-deon)
                                            print(w_father, 'نصيب الأب = ')
    elif father=='نعم':
        if son=='نعم' :
            w_father = (money - deon-w_wife-w_mother) * (1 / 6)
            # w_father= مقدار ورث الاب في وجود فرع وارث ذكر
            print(w_father, 'نصيب الأب = ')
        elif son != 'نعم' and dut != 'نعم' and d_d != 'نعم' and s_d != 'نعم' and d_d_b != 'نعم' and s_s_d != 'نعم':
            w_father = (money - deon-w_wife-w_mother)
            print(w_father, 'نصيب الأب = ')
            #الباقي
        # الذي يحجبهم الأب
        if grand_f == 'نعم':
                w_grand_f = 0
                # w_grand_f=مقدار ورث الجد
                print(w_grand_f, 'نصيب الجد =')
        if grand_f_f == 'نعم':
                w_grand_f_f = 0
                # w_grand_f_f=مقدار ورث أب الجد
                print(w_grand_f_f, 'نصيب أب الجد =')
        if d_b == 'نعم':
                w_d_b = 0
                # w_d_b= مقدار ورث ابن اخ لأب
                print(w_d_b, ' = (', n_d_b, 'نصيب ابن اخ لأب (')
        if d_b_ == 'نعم':
                w_d_b_ = 0
                # w_d_b_= مقدار ورث ابن اخ شقيق
                print(w_d_b_, ' = (', n_d_b_, 'نصيب ابن اخ شقيق (')
        if d_d_b == 'نعم':
                w_d_d_b = 0
                # w_d_d_b= مقدار ورث ابن ابن اخ لأب
                print(w_d_d_b, ' = (', n_d_d_b, 'نصيب ابن ابن اخ لأب (')
        if d_d_b_ == 'نعم':
                w_d_d_b_ = 0
                # w_d_d_b=مقدار ورث ابن ابن اخ شقيق
                print(w_d_d_b_, ' = (', n_d_d_b_, 'نصيب ابن ابن اخ شقيق (')
    elif father!='نعم':
        w_father=0

    if dut == 'نعم' and wife != 'نعم' and d_d != 'نعم':
        if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم':
             if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                  if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                       if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                 if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                     if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                         if grand_f != 'نعم' and m_f != 'نعم':
                                              if son != 'نعم':
                                                  w_dut =(money-deon)/n_dut
                                                  print(w_dut, 'نصيب ورث البنت =')
                                              else:
                                                 w_dut=(money-deon)/(-(n_dut-(n_son/2)))
                                                 print(w_dut, 'نصيب ورث البنت =')
    elif dut== 'نعم' :
        # تحجب
        if sister_m == 'نعم':
                sister_m = 0
                # sister_m= مقدار ورث اخت لأم
                print(w_d_b, ' = (', n_d_b, 'نصيب ابن اخ لأب (')
        if brother_m == 'نعم':
                w_brother_m = 0
                # w_brother_m= مقدار ورث  اخ لأم
                print(w_brother_m, ' = (', n_brother_m, 'نصيب ابن اخ شقيق (')
        if n_dut==1:
            if son!='نعم':
                w_dut=1/2
                print(w_dut, 'نصيب ورث البنت =')
        elif n_dut>1:
            if d_d == 'نعم':
                w_d_d = 0
                # w_d_d= مقدار ورث بنت الابن
                print(w_d_d, ' = (', n_d_d, 'نصيب بنت الابن (')
            if son!='نعم':
                w_dut=2/3
                print(w_dut,' = (', n_dut,'نصيب ورث البنات (')

    if son == 'نعم' and wife != 'نعم' and d_d != 'نعم' and uncle_f_f != 'نعم':
        if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                    if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                        if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' :
                            if uncle_f != 'نعم' and father != 'نعم' and mother != 'نعم':
                                if grand_m != 'نعم' and grand_f != 'نعم' and grand_f_f != 'نعم' and m_f != 'نعم':
                                    if m_m_m != 'نعم' and m_f_f != 'نعم' and m_m_f != 'نعم':
                                        if dut != 'نعم':
                                            w_son = (money-deon) / n_son
                                            print(w_son, ' = (', n_son, 'نصيب الابن/اء(')
                                        else:
                                            w_son = (money-deon) / (n_son - (n_dut / 2))
                                            print(w_son, ' = (', n_son, 'نصيب الابن/اء بوجود البنات(')
    elif son == 'نعم':
        if father=='نعم' or mother=='نعم' or wife=='نعم':
            print(  'الباقي','  = (', n_son, 'نصيب الابن/اء(')
            #الذي يحدبهم الابن
        if d_d == 'نعم':
            w_d_d = 0
            # w_d_d= مقدار ورث الحفيدة او الحفيدات
            print(w_d_d, ' = (', n_d_d, 'نصيب الحفيدة/ات (')
        if s_d == 'نعم':
            w_s_d = 0
            # w_s_d= مقدار ورث الحفيد او الاحفاد
            print(w_s_d, ' = (', n_s_d, 'نصيب الحفيد/الاحفاد (')
        if d_s_d == 'نعم':
            w_d_s_d = 0
            # w_d_s_d= مقدار ورث حفيدات الابناء
            print(w_d_s_d, ' = (', n_d_s_d, 'نصيب حفيدات الابناء (')
        if s_s_d == 'نعم':
            w_s_s_d = 0
            # w_s_s_d=مقدار ورث احفاد الابناء
            print(w_s_s_d, ' = (', n_s_s_d, 'نصيب احفاد الابناء (')
        if brother == 'نعم':
            w_brother = 0
            # w_brother= مقدار ورث الاخ الشقيق
            print(w_brother, ' = (', n_brother, 'نصيب الاخ الشقيق (')
        if sister == 'نعم':
            w_sister = 0
            # w_sister= مقدار ورث الاخت الشقيقة
            print(w_sister, ' = (', n_sister, 'نصيب الاخت الشقيقة (')
        if brother_f == 'نعم':
            w_brother_f = 0
            # w_brother_f= مقدار ورث الاخ لأب
            print(w_brother_f, ' = (', n_brother_f, 'نصيب الاخ الشقيق (')
        if sister_f == 'نعم':
            w_sister_f = 0
            # w_sister= مقدار ورث الاخت لأب
            print(w_sister_f, ' = (', n_sister_f, 'نصيب الاخت لأب (')
        if brother_m == 'نعم':
            w_brother_m = 0
            # w_brother_m= مقدار ورث الاخ لأب
            print(w_brother_m, ' = (', n_brother_m, 'نصيب الاخ لأم (')
        if sister_m == 'نعم':
            w_sister_m = 0
            # w_sister= مقدار ورث الاخت لأب
            print(w_sister_m, ' = (', n_sister_m, 'نصيب الاخت لأم (')
        if uncle == 'نعم':
            w_uncle = 0
            # w_uncle= مقدار ورث العم الشقيق
            print(w_uncle, ' = (', n_uncle, 'نصيب العم الشقيق (')
        if uncle_ == 'نعم':
            w_uncle_ = 0
            # w_uncle_= مقدار ورث العم لأب
            print(w_uncle_, ' = (', n_uncle_, 'نصيب العم لأب (')

    elif son!='نعم':
        w_son=0


    if grand_f=='نعم':
        if dut != 'نعم' and wife != 'نعم' and d_d != 'نعم' :
            if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم' :
                if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم' :
                    if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم' :
                        if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم' :
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم' :
                                if uncle_f != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                    if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                        if m_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم' and m_m_f != 'نعم':
                                            w_grand_f = (money-deon)
                                            print(w_grand_f, 'نصيب الجد = ')
    elif grand_f=='نعم':
        if father!='نعم' and son=='نعم':
            w_grand_f=1/6
            print(w_grand_f, 'نصيب ورث الجد =')

    elif grand_f=='نعم':
        if father!='نعم' and son!= 'نعم' and dut!='نعم':
            w_grand_f='الباقي'
            print(w_grand_f, 'نصيب ورث الجد = ')

    elif grand_f == 'نعم':
        if father != 'نعم' and son != 'نعم' :
            if father=='نعم' or wife=='نعم'  or mother=='نعم' or grand_m=='نعم':
                w_grand_f = 'السدس والباقي'
                print(w_grand_f, 'نصيب ورث الجد = ')
    else:
        w_grand_f=0


    if grand_m=='نعم':
        if dut != 'نعم' and wife != 'نعم' and d_d != 'نعم' :
            if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم' :
                if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم' :
                    if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم' :
                        if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم' :
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم' :
                                if uncle_f != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                    if mother != 'نعم' and father != 'نعم' and grand_f != 'نعم' and grand_f_f != 'نعم':
                                        if m_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم' and m_m_f != 'نعم':
                                            w_grand_m = (money-deon)
                                            print(w_grand_m, 'نصيب الجدة =')

    elif grand_m == 'نعم':
        if mother != 'نعم' and dut== 'نعم':
            # تحجب
            if m_f=='نعم':
                w_m_f = 0
                print(w_m_f, 'نصيب أم الاب = ')
            if m_m_m=='نعم':
                w_m_m_m = 0
                print(w_m_m_m, 'نصيب أم أم الأم = ')
            if m_f_f=='نعم':
                w_m_f_f = 0
                print(w_m_f_f, 'نصيب أم أب الأب = ')
            if m_m_f=='نعم':
                w_m_m_f = 0
                print(w_m_m_f, 'نصيب أم أم الأب = ')
            w_grand_m = 1 / 6
            print(w_grand_m, 'نصيب ورث الجدة =')


    else:
        w_grand_m = 0

    if grand_f_f=='نعم':
        if dut != 'نعم' and wife != 'نعم' and d_d != 'نعم' :
            if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم' :
                if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم' :
                    if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم' :
                        if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم' :
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم' :
                                if uncle_f != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                    if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f != 'نعم':
                                        if m_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم' and m_m_f != 'نعم':
                                            w_grand_f_f = (money-deon)
                                            print(w_grand_f_f, 'نصيب  الجد لأب = ')

    elif grand_f_f == 'نعم':
        if son == 'نعم' and grand_f != 'نعم' and father!='نعم':
            w_grand_f_f = 1/6
            print(w_grand_f_f, 'نصيب الجد لأب =')

        elif dut == 'نعم' and grand_f != 'نعم' and father != 'نعم':
            w_grand_f_f = '1/6 + عصبة'
            print(w_grand_f_f, 'نصيب الجد لأب = ')

        elif dut != 'نعم' and son != 'نعم':
                w_grand_f_f = 'السدس والباقي'
                print(w_grand_f_f, 'نصيب  الجد لأب = ')
    else:
        w_grand_f_f = 0

    if m_f=='نعم':
        if dut != 'نعم' and wife != 'نعم' and d_d != 'نعم' :
            if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم' :
                if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم' :
                    if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم' :
                        if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم' :
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم' :
                                if uncle_f != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                    if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                        if grand_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم' and m_m_f != 'نعم':
                                             w_m_f = (money-deon)
                                             print(w_m_f, 'نصيب ورث أم الأب =')

    elif m_f == 'نعم':
        # تحجب
        if m_m_m == 'نعم':
            w_m_m_m = 0
            print(w_m_m_m, 'نصيب أم أم الأم = ')
        if m_f_f == 'نعم':
            w_m_f_f = 0
            print(w_m_f_f, 'نصيب أم أب الأب = ')
        if m_m_f == 'نعم':
            w_m_m_f = 0
        if mother != 'نعم' and grand_m!= 'نعم':
            print(w_m_m_f, 'نصيب أم أم الأب = ')
            w_m_f = 1/6
            print(w_m_f, 'نصيب ورث أم الأب =')
        elif mother!='نعم' and grand_m=='نعم':
            print( 'نصيب ورث أم الأب = تتشارك مع أم الأم في 1/6')
    elif m_f!='نعم':
        w_m_f=0


    if m_m_m=='نعم':
        if dut != 'نعم' and wife != 'نعم' and d_d != 'نعم' :
            if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم' :
                if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم' :
                    if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم' :
                        if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم' :
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم' :
                                if uncle_f != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                    if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                        if grand_f != 'نعم' and m_f != 'نعم' and m_f_f != 'نعم' and m_m_f != 'نعم':
                                            w_m_m_m = (money-deon)
                                            print(w_m_m_m, 'نصيب أم أم الأم = ')

    elif m_m_m == 'نعم':
        if mother!='نعم' and grand_m!='نعم'  and m_f!='نعم'  and m_f_f!='نعم' and m_f_f!='نعم' :
            w_m_m_m = 1/6
            print(w_m_m_m, 'نصيب أم أم الأم = ')
        elif mother!='نعم' and grand_m!='نعم'  and m_f!='نعم' :
            w_m_f_f = 1/6
            print( 'نصيب أم أم الأم=  تتشارك فيه الجدات ان وجدن (أم أم الأب,أم أب الأب  ) في 1/6')

    elif m_f!='نعم':
        w_m_f=0

    if m_f_f=='نعم':
        if dut != 'نعم' and wife != 'نعم' and d_d != 'نعم' :
            if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم' :
                if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم' :
                    if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم' :
                        if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم' :
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم' :
                                if uncle_f != 'نعم'  and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                    if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                        if grand_f != 'نعم' and m_f != 'نعم' and m_m_m != 'نعم' and m_m_f != 'نعم':
                                            w_m_f_f = (money-deon)
                                            print(w_m_f_f, 'نصيب أم أب الأب = ')

    elif m_f_f!='نعم':
        w_m_f_f=0

    if m_m_f=='نعم':
        if dut != 'نعم' and wife != 'نعم' and d_d != 'نعم' :
            if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم' :
                if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم' :
                    if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم' :
                        if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم' :
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم' :
                                if uncle_f != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                    if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                        if grand_f != 'نعم' and m_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم':
                                            w_m_m_f = (money-deon)
                                            print(w_m_m_f, 'نصيب أم أم الأب = ')

    elif m_m_f!='نعم':
        w_m_m_f=0


    if d_d == 'نعم' and wife != 'نعم' and dut != 'نعم':
        if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم':
             if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                  if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                       if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                 if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                     if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                         if grand_f != 'نعم' and m_f != 'نعم':
                                             if s_d != 'نعم':
                                                 w_d_d = (money-deon) / n_d_d
                                                 print(w_d_d, 'نصيب بنت الابن = ')
                                             else:
                                                 w_d_d = (money-deon) / (-(n_d_d / 2 - (n_s_d)))
                                                 print(w_d_d, 'نصيب بنت الابن = ')

    elif d_d=='نعم':
        #تحجب
        if brother_m=='نعم':
            w_brother_m=0
            print(w_brother_m, ' =(', n_brother_m, 'نصيب الاخوة لأم (')
        if sister_m == 'نعم':
            w_sister_m = 0
            print(w_sister_m, ' =(', n_sister_m, 'نصيب الاخوات لأم (')

        if son != 'نعم' and dut != 'نعم' and s_d != 'نعم':
            if n_d_d==1:
                    w_d_d=1/2
                    print(w_d_d, 'نصيب بنت الابن = ')
            elif n_d_d>1:
                w_d_d = 2 / 3
                print(w_d_d,' =(', n_d_d,'نصيب بنات الابن (')

    elif d_d!='نعم':
        w_d_d=0

    if s_d == 'نعم' and wife != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم':
             if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                  if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                       if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                 if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                     if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                         if grand_f != 'نعم' and m_f != 'نعم':
                                             if d_d != 'نعم':
                                                 w_s_d = (money-deon) / n_s_d
                                                 print(w_s_d, 'نصيب ابن الابن = ')
                                             else:
                                                 w_s_d = (money-deon) / (n_s_d - (n_d_d / 2))
                                                 print(w_s_d, 'نصيب ابن الابن = ')


    elif s_d == 'نعم':
        if son != 'نعم' and dut != 'نعم'  :
            if wife=='نعم' or mother=='نعم' or father=='نعم':
                w_s_d = 'الباقي'
                print(w_s_d, 'نصيب ابن الابن = ')

    elif s_d != 'نعم':
        w_s_d = 0


    if d_s_d == 'نعم' and wife != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم':
             if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                  if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                       if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                 if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                     if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                         if grand_f != 'نعم' and m_f != 'نعم':
                                             if s_s_d != 'نعم':
                                                 w_d_s_d = (money-deon) / n_d_s_d
                                                 print(w_d_s_d, 'نصيب بنت الابن = ')
                                             else:
                                                 w_d_s_d = (money-deon) / (-(n_d_s_d / 2) - n_s_s_d)
                                                 print(w_d_s_d, 'نصيب بنت الابن = ')

    elif d_s_d == 'نعم':
        if son != 'نعم' and dut != 'نعم' and s_d != 'نعم' and d_d!='نعم' and s_s_d!='نعم':
            if n_d_s_d == 1:
                w_d_s_d = 1 / 2
                print(w_d_s_d, 'نصيب بنت الابن = ')
            elif n_d_s_d > 1:
                w_d_s_d = 2 / 3
                print(w_d_s_d, ' =(', n_d_s_d, 'نصيب بنات ابن الابن (')

    elif d_s_d != 'نعم':
        w_d_s_d = 0

    if s_s_d == 'نعم' and wife != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and cousin_c != 'نعم' and sister != 'نعم':
             if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                  if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                       if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                 if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                     if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                         if grand_f != 'نعم' and m_f != 'نعم':
                                             if d_s_d != 'نعم':
                                                 w_s_s_d = (money-deon) / n_s_s_d
                                                 print(w_s_s_d, 'نصيب ابن ابن الابن = ')
                                             else:
                                                 w_s_s_d = (money-deon) / ((n_s_s_d) - (n_d_s_d / 2))
                                                 print(w_s_s_d, 'نصيب ابن ابن الابن = ')

    elif s_s_d == 'نعم':
        if son != 'نعم' and dut != 'نعم' and s_d!='نعم':
            if wife=='نعم' or mother=='نعم' or father=='نعم':
                w_s_s_d = 'الباقي'
                print(w_s_s_d, 'نصيب ابن ابن الابن = ')

    elif s_s_d != 'نعم':
        w_s_s_d = 0

    if sister == 'نعم' and wife != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and cousin_c != 'نعم' and s_s_d != 'نعم':
             if sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                  if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                       if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                 if uncle_f !='نعم'  and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                     if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                         if grand_f != 'نعم' and m_f != 'نعم':
                                             if brother != 'نعم':
                                                 w_sister = (money-deon) / n_sister
                                                 print(w_sister, 'نصيب الاخت الشقيقة = ')
                                             else:
                                                 w_sister = (money-deon) / -((n_sister / 2) - (n_brother))
                                                 print(w_sister, 'نصيب الاخت الشقيقة = ')

    elif sister!='نعم':
        w_sister=0

    if brother == 'نعم' and wife != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and cousin_c != 'نعم' and s_s_d != 'نعم':
             if sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                  if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                       if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                 if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                     if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                         if grand_f != 'نعم' and m_f != 'نعم':
                                             if sister != 'نعم':
                                                 w_brother = (money-deon) / n_brother
                                                 print(w_brother, 'نصيب الاخ الشقيق = ')
                                             else:
                                                 w_brother = (money-deon) / (n_brother - (n_sister / 2))
                                                 print(w_brother, 'نصيب الاخ الشقيق = ')


    elif brother!='نعم':
        w_brother=0

    if sister_f == 'نعم' and wife != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and cousin_c != 'نعم' and sister != 'نعم':
             if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_m != 'نعم':
                  if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                       if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                 if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                     if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                         if grand_f != 'نعم' and m_f != 'نعم':
                                             if brother_f != 'نعم':
                                                 w_sister_f = (money-deon) / n_sister_f
                                                 print(w_sister_f, 'نصيب الاخت لأب = ')
                                             else:
                                                 w_sister_f = (money-deon) / (-((n_sister_f / 2) - n_brother_f))
                                                 print(w_sister_f, 'نصيب الاخت لأب = ')

    elif sister_f!='نعم':
        w_sister_f=0

    if brother_f == 'نعم' and wife != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and cousin_c != 'نعم' and sister != 'نعم':
             if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_m != 'نعم':
                  if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                       if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                 if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                     if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                         if grand_f != 'نعم' and m_f != 'نعم':
                                             if sister_f != 'نعم':
                                                 w_brother_f = (money-deon) / n_brother_f
                                                 print(w_brother_f, 'نصيب الاخ لأب = ')

                                             else:
                                                 w_brother_f = (money-deon) / (n_brother_f - (n_sister / 2))
                                                 print(w_brother_f, 'نصيب الاخ لأب = ')

    elif brother_f!='نعم':
        w_brother_f=0

    if sister_m == 'نعم' and wife != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and cousin_c != 'نعم' and sister != 'نعم':
             if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                  if brother_f != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                       if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                 if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                     if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                         if grand_f != 'نعم' and m_f != 'نعم':
                                             if brother_m != 'نعم':
                                                 w_sister_m = (money-deon) / n_sister_m
                                                 print(w_sister_m, 'نصيب الاخت لأب = ')
                                             else:
                                                 w_sister_m = (money-deon) / -((n_sister_m / 2) - n_brother_m)
                                                 print(w_sister_m, 'نصيب الاخت لأب = ')


    elif sister_m!='نعم':
        w_sister_m=0

    if brother_m == 'نعم' and wife != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and cousin_c != 'نعم' and sister != 'نعم':
             if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                  if brother_f != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                       if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                 if uncle_f != 'نعم'  and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                     if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                         if grand_f != 'نعم' and m_f != 'نعم':
                                             if sister_m != 'نعم':
                                                 w_brother_m = (money-deon) / n_brother_m
                                                 print(w_brother_m, 'نصيب الاخ لأم = ')
                                             else:
                                                 w_brother_m = (money-deon) / (n_brother_m - (n_sister_m / 2))
                                                 print(w_brother_m, 'نصيب الاخ لأم = ')


    elif brother_m!='نعم':
        w_brother_m=0

    if d_b == 'نعم' and wife != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and cousin_c != 'نعم' and sister != 'نعم':
             if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                  if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_d_b != 'نعم':
                       if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                 if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                     if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                         if grand_f != 'نعم' and m_f != 'نعم':
                                             if d_b_ != 'نعم':
                                                 w_d_b = (money-deon) / n_d_b
                                                 print(w_d_b, 'نصيب ابن اخ لأب = ')


    if d_b_ == 'نعم' and wife != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and cousin_c != 'نعم' and sister != 'نعم':
             if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                  if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_d_b != 'نعم':
                       if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                 if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                     if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                         if grand_f != 'نعم' and m_f != 'نعم':
                                             if d_b != 'نعم':
                                                 w_d_b_ = (money-deon) / n_d_b_
                                                 print(w_d_b_, 'نصيب ابن اخ شقيق = ')

    if d_d_b == 'نعم' and wife != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and cousin_c != 'نعم' and sister != 'نعم':
             if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                  if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_b != 'نعم':
                       if d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                 if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                     if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                         if grand_f != 'نعم' and m_f != 'نعم':
                                             if d_d_b_ != 'نعم':
                                                 w_d_d_b = (money-deon) / n_d_d_b
                                                 print(w_d_d_b, 'نصيب ابن ابن اخ لأب = ')

    if d_d_b_ == 'نعم' and wife != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم'  and sister != 'نعم':
             if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                  if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_b != 'نعم':
                       if d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                 if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                     if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                         if grand_f != 'نعم' and m_f != 'نعم':
                                             if d_d_b != 'نعم':
                                                 w_d_d_b_ = (money-deon) / n_d_d_b_
                                                 print(w_d_d_b_, 'نصيب ابن ابن اخ شقيق = ')


    if uncle_ == 'نعم' and wife != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and sister != 'نعم':
             if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                  if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_b != 'نعم':
                       if d_b_ != 'نعم' and d_d_b_ != 'نعم' and d_d_b != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                 if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                     if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                         if grand_f != 'نعم' and m_f != 'نعم':
                                             if uncle != 'نعم':
                                                 w_uncle = (money-deon) / n_uncle
                                                 print(w_uncle, 'نصيب عم شقيق = ')

    if uncle == 'نعم' and wife != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم'  and sister != 'نعم':
             if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                  if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_b != 'نعم':
                       if d_b_ != 'نعم' and d_d_b_ != 'نعم' and d_d_b != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                 if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                     if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                         if grand_f != 'نعم' and m_f != 'نعم':
                                             if uncle_ != 'نعم':
                                                 w_uncle_ = (money-deon) / n_uncle_
                                                 print(w_uncle_, 'نصيب عم لأب = ')


    if cousin == 'نعم' and wife != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم'  and sister != 'نعم':
             if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                  if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_b != 'نعم':
                       if d_b_ != 'نعم' and d_d_b_ != 'نعم' and d_d_b != 'نعم' and uncle != 'نعم':
                            if uncle_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                 if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                     if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                         if grand_f != 'نعم' and m_f != 'نعم':
                                             if cousin_ != 'نعم':
                                                 w_cousin = (money-deon) / n_cousin
                                                 print(w_cousin, 'نصيب ابن عم لأب = ')

    if cousin_ == 'نعم' and wife != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and sister != 'نعم':
             if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                  if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_b != 'نعم':
                       if d_b_ != 'نعم' and d_d_b_ != 'نعم' and d_d_b != 'نعم' and uncle != 'نعم':
                            if uncle_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                 if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                     if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                         if grand_f != 'نعم' and m_f != 'نعم':
                                             if cousin != 'نعم':
                                                 w_cousin_ = (money-deon) / n_cousin_
                                                 print(w_cousin_, 'نصيب ابن عم شقيق = ')

    if cousin_c == 'نعم'  and wife != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_b != 'نعم':
                    if d_b_ != 'نعم' and d_d_b_ != 'نعم' and d_d_b != 'نعم' and uncle != 'نعم':
                        if uncle_ != 'نعم' and cousin != 'نعم' and cousin_ != 'نعم' and uncle_f_f != 'نعم':
                            if uncle_f != 'نعم'  and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if cousin_c_ != 'نعم':
                                            w_cousin_c = (money-deon) / n_cousin_c
                                            print(w_cousin_c, 'نصيب ابن ابن عم لأب = ')

    if cousin_c_ == 'نعم' and wife != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_b != 'نعم':
                    if d_b_ != 'نعم' and d_d_b_ != 'نعم' and d_d_b != 'نعم' and uncle != 'نعم':
                        if uncle_ != 'نعم' and cousin != 'نعم' and cousin_ != 'نعم' and uncle_f_f != 'نعم':
                            if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if cousin_c != 'نعم':
                                            w_cousin_c_ = (money-deon) / n_cousin_c_
                                            print(w_cousin_c_, 'نصيب ابن ابن عم شقيق = ')


    if uncle_f == 'نعم' and cousin_c_ != 'نعم' and wife != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_b != 'نعم':
                    if d_b_ != 'نعم' and d_d_b_ != 'نعم' and d_d_b != 'نعم' and uncle != 'نعم':
                        if uncle_ != 'نعم' and cousin != 'نعم' and cousin_ != 'نعم' :
                            if cousin_c != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if uncle_f_f != 'نعم':
                                            w_uncle_f = (money-deon) / n_uncle_f
                                            print(w_uncle_f, 'نصيب عم لأب = ')

    if uncle_f_f == 'نعم' and cousin_c_ != 'نعم' and wife != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_b != 'نعم':
                    if d_b_ != 'نعم' and d_d_b_ != 'نعم' and d_d_b != 'نعم' and uncle != 'نعم':
                        if uncle_ != 'نعم' and cousin != 'نعم' and cousin_ != 'نعم' :
                            if  cousin_c != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if uncle_f != 'نعم':
                                            w_uncle_f_f = (money-deon) / n_uncle_f_f
                                            print(w_uncle_f_f, 'نصيب عم شقيق = ')
#*************************************************************************
def woman():
    _husband='لا'
    husband = input('هل يوجد زوج (نعم-لا) : ')
    # husband= الزوج
    if husband !='نعم':
        husband=_husband
        n_husband=0

    _father = 'لا'
    father = int(input('هل يوجد أب (نعم-لا) : '))
    # father=الأب
    if father != 'نعم':
        father = _father
        n_father = 0

    _mother = 'لا'
    mother = input('هل يوجد أم (نعم-لا) : ')
    # mother=الأم
    if mother != 'نعم':
        mother = _mother
        n_mother = 0

    _grand_m = 'لا'
    grand_m = input('هل يوجد أم ألأم (نعم-لا) : ')
    # grand_m=الجدة من الام
    if grand_m != 'نعم':
        grand_m = _grand_m
        n_grand_m = 0

    _grand_f = 'لا'
    grand_f = input('هل يوجد جد "أب الأب" (نعم-لا) : ')
    # grand_f=الجد من الأب
    if grand_f != 'نعم':
        grand_f = _grand_f
        n_grand_f = 0

    _grand_f_f = 'لا'
    grand_f_f = input('هل يوجد جد "أب أب الأب" (نعم-لا) : ')
    # grand_f_f=جد أب الأب
    if grand_f_f != 'نعم':
        grand_f_f = _grand_f_f
        n_grand_f_f = 0

    _m_f = 'لا'
    m_f = input('هل يوجد جد أم الأب (نعم-لا) : ')
    # m_f= جد أم الأب
    if m_f != 'نعم':
        m_f = _m_f
        n_m_f = 0

    _m_m_m = 'لا'
    m_m_m = input('هل يوجد أم أم الأم (نعم-لا) : ')
    # m_m_m= أم أم الأم
    if m_m_m != 'نعم':
        m_m_m = _m_m_m
        n_m_m_m = 0

    _m_f_f = 'لا'
    m_f_f = input('هل يوجد جد أم أب الأب (نعم-لا) : ')
    # m_f_f= أم أب الأب
    if m_f_f != 'نعم':
        m_f_f = _m_f_f
        n_m_f_f = 0

    _m_m_f = 'لا'
    m_m_f = input('هل يوجد أم أم الأب (نعم-لا) : ')
    # m_m_f= أم أم الأب
    if m_m_f != 'نعم':
        m_m_f = _m_m_f
        n_m_m_f = 0

    _dut = 'لا'
    dut = input('هل يوجد ابنة (نعم-لا) : ')
    # dut= ابنة
    if dut == 'نعم':
        n_dut = int(input('ادخل عدد البنات : '))
    # n_dut= عدد ابنة
    else:
        dut = _dut
        n_dut = 0

    _son = 'لا'
    son = input('هل يوجد ابن (نعم-لا) : ')
    # son=  ابن
    if son == 'نعم':
        n_son = int(input('ادخل عدد الابناء : '))
    # n_son= عدد ابن
    else:
        son = _son
        n_son = 0

    _d_d = 'لا'
    d_d = input('هل يوجد بنت ابن (نعم-لا) : ')
    # d_d= بنت ابن
    if d_d == 'نعم':
        n_d_d = int(input('ادخل عددهن : '))
    # n_d_d= عدد بنت ابن
    else:
        d_d = _d_d
        n_d_d = 0

    _s_d = 'لا'
    s_d = input('هل يوجد ابن ابن (نعم-لا) : ')
    # s_d= ابن ابن
    if s_d == 'نعم':
        n_s_d = int(input('ادخل عددهم : '))
    # n_s_d= عدد ابن ابن
    else:
        s_d = _s_d
        n_s_d = 0

    _d_s_d = 'لا'
    d_s_d = input('هل يوجد بنت ابن ابن (نعم-لا) : ')
    # d_s_d= بنت ابن ابن
    if d_s_d == 'نعم':
        n_d_s_d = int(input('ادخل عددهن : '))
    # n_d_s_d= عدد بنت ابن ابن
    else:
        d_s_d = _d_s_d
        n_d_s_d = 0

    _s_s_d = 'لا'
    s_s_d = input('هل يوجد ابن ابن ابن (نعم-لا) : ')
    # s_s_d= ابن ابن ابن
    if s_s_d == 'نعم':
        n_s_s_d = int(input('ادخل عددهم : '))
    # n_s_s_d= عدد ابن ابن ابن
    else:
        s_s_d = _s_s_d
        n_s_s_d = 0

    _sister = 'لا'
    sister = input('هل يوجد أخت شقيقة (نعم-لا) : ')
    # sister= أخت شقيقة
    if sister == 'نعم':
        n_sister = int(input('ادخل عددهن : '))
    # n_sister=عدد أخت شقيقة
    else:
        sister = _sister
        n_sister = 0

    _brother = 'لا'
    brother = input('هل يوجد أخ شقيق (نعم-لا) : ')
    # brother= أخ شقيق
    if brother == 'نعم':
        n_brother = int(input('ادخل عددهم : '))
    # n_brother= عدد أخ شقيق
    else:
        brother = _brother
        n_brother = 0

    _sister_f = 'لا'
    sister_f = input('هل يوجد أخت لأب (نعم-لا) : ')
    # sister_f= أخت لأب
    if sister_f == 'نعم':
        n_sister_f = int(input('ادخل عددهن : '))
    # n_sister_f= عدد أخت لأب
    else:
        sister_f = _sister_f
        n_sister_f = 0

    _brother_f = 'لا'
    brother_f = input('هل يوجد أخ لأب (نعم-لا) : ')
    # brother_f= أخ لأب
    if brother_f == 'نعم':
        n_brother_f = int(input('ادخل عددهم : '))
    # n_brother_f= عدد أخ لأب
    else:
        brother_f = _brother_f
        n_brother_f = 0

    _sister_m = 'لا'
    sister_m = input('هل يوجد أخت لأم (نعم-لا) : ')
    # sister_m= أخت لأم
    if sister_m == 'نعم':
        n_sister_m = int(input('ادخل عددهن : '))
    # n_sister_m= عدد أخت لأم
    else:
        sister_m = _sister_m
        n_sister_m = 0

    _brother_m = 'لا'
    brother_m = input('هل يوجد أخ لأم (نعم-لا) : ')
    # brother_m= أخ لأم
    if brother_m == 'نعم':
        n_brother_m = int(input('ادخل عددهم : '))
    # n_brother_m= عدد أخ لأم
    else:
        brother_m = _brother_m
        n_brother_m = 0

    _d_b = 'لا'
    d_b = input('هل يوجد ابن أخ لأب (نعم-لا) : ')
    # d_b=  ابن أخ لأب
    if d_b == 'نعم':
        n_d_b = int(input('ادخل عددهم : '))
    # n_d_b= عدد ابن أخ لأب
    else:
        d_b = _d_b
        n_d_b = 0

    _d_b_ = 'لا'
    d_b_ = input('هل يوجد ابن أخ شقيق (نعم-لا) : ')
    # d_b_=  ابن أخ شقيق
    if d_b_ == 'نعم':
        n_d_b_ = int(input('ادخل عددهم : '))
    # n_d_b_= عدد ابن أخ شقيق
    else:
        d_b_ = _d_b_
        n_d_b_ = 0

    _d_d_b = 'لا'
    d_d_b = input('هل يوجد ابن ابن أخ لأب (نعم-لا) : ')
    # d_d_b= ابن ابن أخ لأب
    if d_d_b == 'نعم':
        n_d_d_b = int(input('ادخل عددهم : '))
    # n_d_d_b=عدد ابن ابن أخ لأب
    else:
        d_d_b = _d_d_b
        n_d_d_b = 0

    _d_d_b_ = 'لا'
    d_d_b_ = input('هل يوجد ابن ابن أخ شقيق (نعم-لا) : ')
    # d_d_b_= ابن ابن أخ شقيق
    if d_d_b_ == 'نعم':
        n_d_d_b_ = int(input('ادخل عددهم : '))
    # n_d_d_b_=  عدد ابن ابن أخ شقيق
    else:
        d_d_b_ = _d_d_b_
        n_d_d_b_ = 0

    _uncle_ = 'لا'
    uncle_ = input('هل يوجد عم لأب  (نعم-لا) : ')
    # uncle_= عم لأب
    if uncle_ == 'نعم':
        n_uncle_ = int(input('ادخل عددهم : '))
    # n_uncle_= عدد عم لأب
    else:
        uncle_ = _uncle_
        n_uncle_ = 0

    _uncle = 'لا'
    uncle = input('هل يوجد عم شقيق (نعم-لا) : ')
    # uncle= عم شقيق
    if uncle == 'نعم':
        n_uncle = int(input('ادخل عددهم : '))
    # n_uncle= عدد عم شقيق
    else:
        uncle = _uncle
        n_uncle = 0

    _cousin = 'لا'
    cousin = input('هل يوجد ابن عم للأب (نعم-لا) : ')
    # cousin=  ابن عم للأب
    if cousin == 'نعم':
        n_cousin = int(input('ادخل عددهم : '))
    # n_cousin= عدد ابن عم للأب
    else:
        cousin = _cousin
        n_cousin = 0

    _cousin_ = 'لا'
    cousin_ = input('هل يوجد ابن عم شقيق (نعم-لا) : ')
    # cousin_=  ابن عم شقيق
    if cousin_ == 'نعم':
        n_cousin_ = int(input('ادخل عددهم : '))
    # n_cousin_=  عدد ابن عم شقيق
    else:
        cousin_ = _cousin_
        n_cousin_ = 0

    _cousin_c = 'لا'
    cousin_c = input('هل يوجد ابن ابن عم للأب (نعم-لا) : ')
    # cousin_c= ابن ابن عم للأب
    if cousin_c == 'نعم':
        n_cousin_c = int(input('ادخل عددهم : '))
    # n_cousin_c= عدد ابن ابن عم للأب
    else:
        cousin_c = _cousin_c
        n_cousin_c = 0

    _cousin_c_ = 'لا'
    cousin_c_ = input('هل يوجد ابن ابن عم شقيق (نعم-لا) : ')
    # cousin_c_= ابن ابن عم شقيق
    if cousin_c_ == 'نعم':
        n_cousin_c_ = int(input('ادخل عددهم : '))
    # n_cousin_c_=عدد ابن ابن عم شقيق
    else:
        cousin_c_ = _cousin_c_
        n_cousin_c_ = 0

    _uncle_f_f = 'لا'
    uncle_f_f = input('هل يوجد عم للأب "أخ الجد للأب" (نعم-لا) : ')
    # uncle_f_f= " عم للأب "أخ الجد للأب
    if uncle_f_f == 'نعم':
        n_uncle_f_f = int(input('ادخل عددهم : '))
    # n_uncle_f_f= عدد " عم للأب "أخ الجد للأب
    else:
        uncle_f_f = _uncle_f_f
        n_uncle_f_f = 0

    _uncle_f = 'لا'
    uncle_f = input('هل يوجد عم للأب "شقيق الجد" (نعم-لا) : ')
    # uncle_f= " عم الاب "شقيق الجد
    if uncle_f == 'نعم':
        n_uncle_f = int(input('ادخل عددهم : '))
    # n_uncle_f= عدد " عم الاب "شقيق الجد
    else:
        uncle_f = _uncle_f
        n_uncle_f = 0

    print('************************************************************************')
    print('**التركة = ', money)
    print('**الديون = ', deon)
    print('**التركة بعد تسديد الديون = ', money-deon)
    print('*زوج: ', husband )
    print('أب: ', father)
    print('أم: ', mother)
    print('أم ألأم: ', grand_m)
    print('جد "أب الأب": ', grand_f)
    print('جد "أب أب الأب": ', grand_f_f)
    print('جد أم الأب: ', m_f)
    print('أم أم الأم: ', m_m_m)
    print('أم أب الأب: ', m_f_f)
    print('أم أم الأب: ', m_m_f)
    print()
    print('*ابنة: ', dut, '   *العدد: ', n_dut)
    print('*ابن: ', son, '   *العدد: ', n_son)
    print('*بنت ابن: ', d_d, '   *العدد: ', n_d_d)
    print('*ابن ابن: ', s_d, '   *العدد: ', n_s_d)
    print('*بنت ابن ابن: ', d_s_d, '   *العدد: ', n_d_s_d)
    print('*ابن ابن ابن: ', s_s_d, '   *العدد: ', n_s_s_d)
    print('*أخت شقيقة: ', sister, '   *العدد: ', n_sister)
    print('*أخ شقيق: ', brother, '   *العدد: ', n_brother)
    print('*أخت لأب: ', sister_f, '   *العدد: ', n_sister_f)
    print('*أخ لأب: ', brother_f, '   *العدد: ', n_brother_f)
    print('*أخت لأم: ', sister_m, '   *العدد: ', n_sister_m)
    print('*أخ لأم: ', brother_m, '   *العدد: ', brother_m)
    print('*ابن أخ لأب: ', d_b, '   *العدد: ', n_d_b)
    print('*ابن أخ شقيق: ', d_b_, '   *العدد: ', n_d_b_)
    print('*ابن ابن أخ لأب: ', d_d_b, '   *العدد: ', n_d_d_b)
    print('*ابن ابن أخ شقيق: ', d_d_b_, '   *العدد: ', n_d_d_b_)
    print('*عم لأب: ', uncle_, '   *العدد: ', n_uncle_)
    print('*عم شقيق: ', uncle, '   *العدد: ', n_uncle)
    print('*ابن عم لأب: ', cousin, '   *العدد: ', n_cousin)
    print('*ابن عم شقيق: ', cousin_, '   *العدد: ', n_cousin_)
    print('*ابن ابن عم للأب (نعم-لا): ', cousin_c, '   *العدد: ', n_cousin_c)
    print('*ابن ابن عم شقيق (نعم-لا): ', cousin_c_, '   *العدد: ', n_cousin_c_)
    print('*عم لأب "أخ الجد لأب": ', uncle_f_f, '   *العدد: ', n_uncle_f_f)
    print('*عم لأب "شقيق الجد": ', uncle_f, '   *العدد: ', n_uncle_f)
    print('************************************************************************')

    if husband == 'نعم':
        if son != 'نعم' and dut != 'نعم' and d_d != 'نعم' and s_d != 'نعم':
            if d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم' and brother != 'نعم':
                if sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم' and brother_m != 'نعم':
                    if d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم' and d_d_b_ != 'نعم':
                        if uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم' and cousin_ != 'نعم':
                            if cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم' and uncle_f != 'نعم':
                                if  father != 'نعم' and mother != 'نعم':
                                    if grand_m != 'نعم' and grand_f != 'نعم' and grand_f_f != 'نعم' and m_f != 'نعم':
                                        if m_m_m != 'نعم' and m_f_f != 'نعم' and m_m_f != 'نعم':
                                            w_husband= (money - deon)
                                            print(w_husband, 'نصيب الزوج = ')

    elif husband == 'نعم':
        # الاصل
        if son == 'نعم' or dut == 'نعم' or d_d == 'نعم' or s_d == 'نعم' or d_d_b == 'نعم' or s_s_d == 'نعم':
            # الفروع
            w_husband = (money - deon) * (1 / 8)
            print(w_husband, 'نصيب الزوج = ')

        elif son != 'نعم' and dut != 'نعم' and d_d != 'نعم' and s_d != 'نعم' and d_d_b != 'نعم' and s_s_d != 'نعم':
            w_husband = 1 / 2
            w_wife = (money - deon) * (1 / 4)
            print(w_husband,'نصيب الزوج = ')
    elif husband != 'نعم':
        w_husband = 0


    if mother == 'نعم':
        if dut != 'نعم' and husband != 'نعم' and d_d != 'نعم':
            if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم':
                if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                    if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                        if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                if uncle_f != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                    if father != 'نعم' and grand_f != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                        if m_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم' and m_m_f != 'نعم':
                                            if mother != 'نعم':
                                                w_mother = (money - deon)
                                                print(w_mother, 'نصيب الأم = ')
    elif mother == 'نعم':
        # الاصل
        if son != 'نعم' and dut != 'نعم' and d_d != 'نعم' and s_d != 'نعم' and d_d_b != 'نعم' and s_s_d != 'نعم':
            # w_mother = 1 / 3
            w_mother = (money - deon - w_wife) * (1 / 3)
            print(w_mother, 'نصيب الأم = ')
        if grand_m == 'نعم':
            w_grand_m = 0
            print(w_grand_m, 'نصيب أم الأم = ')
        if m_f == 'نعم':
            w_m_f = 0
            print(w_m_f, 'نصيب أم الاب = ')
        if m_m_m == 'نعم':
            w_m_m_m = 0
            print(w_m_m_m, 'نصيب أم أم الأم = ')
        if m_f_f == 'نعم':
            w_m_f_f = 0
            print(w_m_f_f, 'نصيب أم أب الأب = ')
        if m_m_f == 'نعم':
            w_m_m_f = 0
            print(w_m_m_f, 'نصيب أم أم الأب = ')
        if son == 'نعم' or dut == 'نعم' or d_d == 'نعم' or s_d == 'نعم' or d_d_b == 'نعم' or s_s_d == 'نعم':
            # الفروع
            # w_mother = 1 / 6
            w_mother = (money - deon - w_wife) * (1 / 6)
            print(w_mother, 'نصيب الأم = ')



    if father == 'نعم':
        if dut != 'نعم' and husband != 'نعم' and d_d != 'نعم':
            if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم':
                if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                    if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                        if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                if uncle_f != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                    if mother != 'نعم' and grand_f != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                        if m_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم' and m_m_f != 'نعم':
                                            w_father = (money - deon)
                                            print(w_father, 'نصيب الأب = ')
    elif father == 'نعم':
        if son == 'نعم':
            w_father = (money - deon - w_wife - w_mother) * (1 / 6)
            # w_father= مقدار ورث الاب في وجود فرع وارث ذكر
            print(w_father, 'نصيب الأب = ')
        elif son != 'نعم' and dut != 'نعم' and d_d != 'نعم' and s_d != 'نعم' and d_d_b != 'نعم' and s_s_d != 'نعم':
            w_father = (money - deon - w_wife - w_mother)
            print(w_father, 'نصيب الأب = ')
            # الباقي
        # الذي يحجبهم الأب
        if grand_f == 'نعم':
            w_grand_f = 0
            # w_grand_f=مقدار ورث الجد
            print(w_grand_f, 'نصيب الجد =')
        if grand_f_f == 'نعم':
            w_grand_f_f = 0
            # w_grand_f_f=مقدار ورث أب الجد
            print(w_grand_f_f, 'نصيب أب الجد =')
        if d_b == 'نعم':
            w_d_b = 0
            # w_d_b= مقدار ورث ابن اخ لأب
            print(w_d_b, ' = (', n_d_b, 'نصيب ابن اخ لأب (')
        if d_b_ == 'نعم':
            w_d_b_ = 0
            # w_d_b_= مقدار ورث ابن اخ شقيق
            print(w_d_b_, ' = (', n_d_b_, 'نصيب ابن اخ شقيق (')
        if d_d_b == 'نعم':
            w_d_d_b = 0
            # w_d_d_b= مقدار ورث ابن ابن اخ لأب
            print(w_d_d_b, ' = (', n_d_d_b, 'نصيب ابن ابن اخ لأب (')
        if d_d_b_ == 'نعم':
            w_d_d_b_ = 0
            # w_d_d_b=مقدار ورث ابن ابن اخ شقيق
            print(w_d_d_b_, ' = (', n_d_d_b_, 'نصيب ابن ابن اخ شقيق (')
    elif father != 'نعم':
        w_father = 0

    if dut == 'نعم' and husband != 'نعم' and d_d != 'نعم':
        if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                    if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                        if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                            if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if son != 'نعم':
                                            w_dut = (money - deon) / n_dut
                                            print(w_dut, 'نصيب ورث البنت =')
                                        else:
                                            w_dut = (money - deon) / (-(n_dut - (n_son / 2)))
                                            print(w_dut, 'نصيب ورث البنت =')
    elif dut == 'نعم':
        # تحجب
        if sister_m == 'نعم':
            sister_m = 0
            # sister_m= مقدار ورث اخت لأم
            print(w_d_b, ' = (', n_d_b, 'نصيب ابن اخ لأب (')
        if brother_m == 'نعم':
            w_brother_m = 0
            # w_brother_m= مقدار ورث  اخ لأم
            print(w_brother_m, ' = (', n_brother_m, 'نصيب ابن اخ شقيق (')
        if n_dut == 1:
            if son != 'نعم':
                w_dut = 1 / 2
                print(w_dut, 'نصيب ورث البنت =')
        elif n_dut > 1:
            if d_d == 'نعم':
                w_d_d = 0
                # w_d_d= مقدار ورث بنت الابن
                print(w_d_d, ' = (', n_d_d, 'نصيب بنت الابن (')
            if son != 'نعم':
                w_dut = 2 / 3
                print(w_dut, ' = (', n_dut, 'نصيب ورث البنات (')

    if son == 'نعم' and husband != 'نعم' and d_d != 'نعم' and uncle_f_f != 'نعم':
        if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                    if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                        if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم':
                            if uncle_f != 'نعم' and father != 'نعم' and mother != 'نعم':
                                if grand_m != 'نعم' and grand_f != 'نعم' and grand_f_f != 'نعم' and m_f != 'نعم':
                                    if m_m_m != 'نعم' and m_f_f != 'نعم' and m_m_f != 'نعم':
                                        if dut != 'نعم':
                                            w_son = (money - deon) / n_son
                                            print(w_son, ' = (', n_son, 'نصيب الابن/اء(')
                                        else:
                                            w_son = (money - deon) / (n_son - (n_dut / 2))
                                            print(w_son, ' = (', n_son, 'نصيب الابن/اء بوجود البنات(')
    elif son == 'نعم':
        if father=='نعم' or mother=='نعم' or husband=='نعم':
            print(  'الباقي','  = (', n_son, 'نصيب الابن/اء(')
        # الذي يحدبهم الابن
        if d_d == 'نعم':
            w_d_d = 0
            # w_d_d= مقدار ورث الحفيدة او الحفيدات
            print(w_d_d, ' = (', n_d_d, 'نصيب الحفيدة/ات (')
        if s_d == 'نعم':
            w_s_d = 0
            # w_s_d= مقدار ورث الحفيد او الاحفاد
            print(w_s_d, ' = (', n_s_d, 'نصيب الحفيد/الاحفاد (')
        if d_s_d == 'نعم':
            w_d_s_d = 0
            # w_d_s_d= مقدار ورث حفيدات الابناء
            print(w_d_s_d, ' = (', n_d_s_d, 'نصيب حفيدات الابناء (')
        if s_s_d == 'نعم':
            w_s_s_d = 0
            # w_s_s_d=مقدار ورث احفاد الابناء
            print(w_s_s_d, ' = (', n_s_s_d, 'نصيب احفاد الابناء (')
        if brother == 'نعم':
            w_brother = 0
            # w_brother= مقدار ورث الاخ الشقيق
            print(w_brother, ' = (', n_brother, 'نصيب الاخ الشقيق (')
        if sister == 'نعم':
            w_sister = 0
            # w_sister= مقدار ورث الاخت الشقيقة
            print(w_sister, ' = (', n_sister, 'نصيب الاخت الشقيقة (')
        if brother_f == 'نعم':
            w_brother_f = 0
            # w_brother_f= مقدار ورث الاخ لأب
            print(w_brother_f, ' = (', n_brother_f, 'نصيب الاخ الشقيق (')
        if sister_f == 'نعم':
            w_sister_f = 0
            # w_sister= مقدار ورث الاخت لأب
            print(w_sister_f, ' = (', n_sister_f, 'نصيب الاخت لأب (')
        if brother_m == 'نعم':
            w_brother_m = 0
            # w_brother_m= مقدار ورث الاخ لأب
            print(w_brother_m, ' = (', n_brother_m, 'نصيب الاخ لأم (')
        if sister_m == 'نعم':
            w_sister_m = 0
            # w_sister= مقدار ورث الاخت لأب
            print(w_sister_m, ' = (', n_sister_m, 'نصيب الاخت لأم (')
        if uncle == 'نعم':
            w_uncle = 0
            # w_uncle= مقدار ورث العم الشقيق
            print(w_uncle, ' = (', n_uncle, 'نصيب العم الشقيق (')
        if uncle_ == 'نعم':
            w_uncle_ = 0
            # w_uncle_= مقدار ورث العم لأب
            print(w_uncle_, ' = (', n_uncle_, 'نصيب العم لأب (')

    elif son != 'نعم':
        w_son = 0

    if grand_f == 'نعم':
        if dut != 'نعم' and husband != 'نعم' and d_d != 'نعم':
            if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم':
                if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                    if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                        if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                if uncle_f != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                    if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                        if m_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم' and m_m_f != 'نعم':
                                            w_grand_f = (money - deon)
                                            print(w_grand_f, 'نصيب الجد = ')
    elif grand_f == 'نعم':
        if father != 'نعم' and son == 'نعم':
            w_grand_f = 1 / 6
            print(w_grand_f, 'نصيب ورث الجد =')

    elif grand_f == 'نعم':
        if father != 'نعم' and son != 'نعم' and dut != 'نعم':
            w_grand_f = 'الباقي'
            print(w_grand_f, 'نصيب ورث الجد = ')

    elif grand_f == 'نعم':
        if father != 'نعم' and son != 'نعم':
            if father == 'نعم' or husband == 'نعم' or mother == 'نعم' or grand_m == 'نعم':
                w_grand_f = 'السدس والباقي'
                print(w_grand_f, 'نصيب ورث الجد = ')
    else:
        w_grand_f = 0

    if grand_m == 'نعم':
        if dut != 'نعم' and husband != 'نعم' and d_d != 'نعم':
            if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم':
                if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                    if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                        if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                if uncle_f != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                    if mother != 'نعم' and father != 'نعم' and grand_f != 'نعم' and grand_f_f != 'نعم':
                                        if m_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم' and m_m_f != 'نعم':
                                            w_grand_m = (money - deon)
                                            print(w_grand_m, 'نصيب الجدة =')

    elif grand_m == 'نعم':
        if mother != 'نعم' and dut == 'نعم':
            # تحجب
            if m_f == 'نعم':
                w_m_f = 0
                print(w_m_f, 'نصيب أم الاب = ')
            if m_m_m == 'نعم':
                w_m_m_m = 0
                print(w_m_m_m, 'نصيب أم أم الأم = ')
            if m_f_f == 'نعم':
                w_m_f_f = 0
                print(w_m_f_f, 'نصيب أم أب الأب = ')
            if m_m_f == 'نعم':
                w_m_m_f = 0
                print(w_m_m_f, 'نصيب أم أم الأب = ')
            w_grand_m = 1 / 6
            print(w_grand_m, 'نصيب ورث الجدة =')


    else:
        w_grand_m = 0

    if grand_f_f == 'نعم':
        if dut != 'نعم' and husband != 'نعم' and d_d != 'نعم':
            if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم':
                if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                    if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                        if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                if uncle_f != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                    if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f != 'نعم':
                                        if m_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم' and m_m_f != 'نعم':
                                            w_grand_f_f = (money - deon)
                                            print(w_grand_f_f, 'نصيب  الجد لأب = ')

    elif grand_f_f == 'نعم':
        if son == 'نعم' and grand_f != 'نعم' and father != 'نعم':
            w_grand_f_f = 1 / 6
            print(w_grand_f_f, 'نصيب الجد لأب =')

        elif dut == 'نعم' and grand_f != 'نعم' and father != 'نعم':
            w_grand_f_f = '1/6 + عصبة'
            print(w_grand_f_f, 'نصيب الجد لأب = ')

        elif dut != 'نعم' and son != 'نعم':
            w_grand_f_f = 'السدس والباقي'
            print(w_grand_f_f, 'نصيب  الجد لأب = ')
    else:
        w_grand_f_f = 0

    if m_f == 'نعم':
        if dut != 'نعم' and husband != 'نعم' and d_d != 'نعم':
            if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم':
                if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                    if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                        if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                if uncle_f != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                    if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                        if grand_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم' and m_m_f != 'نعم':
                                            w_m_f = (money - deon)
                                            print(w_m_f, 'نصيب ورث أم الأب =')

    elif m_f == 'نعم':
        # تحجب
        if m_m_m == 'نعم':
            w_m_m_m = 0
            print(w_m_m_m, 'نصيب أم أم الأم = ')
        if m_f_f == 'نعم':
            w_m_f_f = 0
            print(w_m_f_f, 'نصيب أم أب الأب = ')
        if m_m_f == 'نعم':
            w_m_m_f = 0
        if mother != 'نعم' and grand_m != 'نعم':
            print(w_m_m_f, 'نصيب أم أم الأب = ')
            w_m_f = 1 / 6
            print(w_m_f, 'نصيب ورث أم الأب =')
        elif mother != 'نعم' and grand_m == 'نعم':
            print('نصيب ورث أم الأب = تتشارك مع أم الأم في 1/6')
    elif m_f != 'نعم':
        w_m_f = 0

    if m_m_m == 'نعم':
        if dut != 'نعم' and husband != 'نعم' and d_d != 'نعم':
            if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم':
                if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                    if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                        if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                if uncle_f != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                    if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                        if grand_f != 'نعم' and m_f != 'نعم' and m_f_f != 'نعم' and m_m_f != 'نعم':
                                            w_m_m_m = (money - deon)
                                            print(w_m_m_m, 'نصيب أم أم الأم = ')

    elif m_m_m == 'نعم':
        if mother != 'نعم' and grand_m != 'نعم' and m_f != 'نعم' and m_f_f != 'نعم' and m_f_f != 'نعم':
            w_m_m_m = 1 / 6
            print(w_m_m_m, 'نصيب أم أم الأم = ')
        elif mother != 'نعم' and grand_m != 'نعم' and m_f != 'نعم':
            w_m_f_f = 1 / 6
            print('نصيب أم أم الأم=  تتشارك فيه الجدات ان وجدن (أم أم الأب,أم أب الأب  ) في 1/6')

    elif m_f != 'نعم':
        w_m_f = 0

    if m_f_f == 'نعم':
        if dut != 'نعم' and husband != 'نعم' and d_d != 'نعم':
            if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم':
                if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                    if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                        if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                if uncle_f != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                    if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                        if grand_f != 'نعم' and m_f != 'نعم' and m_m_m != 'نعم' and m_m_f != 'نعم':
                                            w_m_f_f = (money - deon)
                                            print(w_m_f_f, 'نصيب أم أب الأب = ')

    elif m_f_f != 'نعم':
        w_m_f_f = 0

    if m_m_f == 'نعم':
        if dut != 'نعم' and husband != 'نعم' and d_d != 'نعم':
            if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم':
                if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                    if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                        if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                            if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                if uncle_f != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                                    if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                        if grand_f != 'نعم' and m_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم':
                                            w_m_m_f = (money - deon)
                                            print(w_m_m_f, 'نصيب أم أم الأب = ')

    elif m_m_f != 'نعم':
        w_m_m_f = 0

    if d_d == 'نعم' and husband != 'نعم' and dut != 'نعم':
        if s_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                    if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                        if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                            if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if s_d != 'نعم':
                                            w_d_d = (money - deon) / n_d_d
                                            print(w_d_d, 'نصيب بنت الابن = ')
                                        else:
                                            w_d_d = (money - deon) / (-(n_d_d / 2 - (n_s_d)))
                                            print(w_d_d, 'نصيب بنت الابن = ')

    elif d_d == 'نعم':
        # تحجب
        if brother_m == 'نعم':
            w_brother_m = 0
            print(w_brother_m, ' =(', n_brother_m, 'نصيب الاخوة لأم (')
        if sister_m == 'نعم':
            w_sister_m = 0
            print(w_sister_m, ' =(', n_sister_m, 'نصيب الاخوات لأم (')

        if son != 'نعم' and dut != 'نعم' and s_d != 'نعم':
            if n_d_d == 1:
                w_d_d = 1 / 2
                print(w_d_d, 'نصيب بنت الابن = ')
            elif n_d_d > 1:
                w_d_d = 2 / 3
                print(w_d_d, ' =(', n_d_d, 'نصيب بنات الابن (')

    elif d_d != 'نعم':
        w_d_d = 0

    if s_d == 'نعم' and husband != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and d_s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                    if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                        if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                            if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if d_d != 'نعم':
                                            w_s_d = (money - deon) / n_s_d
                                            print(w_s_d, 'نصيب ابن الابن = ')
                                        else:
                                            w_s_d = (money - deon) / (n_s_d - (n_d_d / 2))
                                            print(w_s_d, 'نصيب ابن الابن = ')


    elif s_d == 'نعم':
        if son != 'نعم' and dut != 'نعم':
            if husband == 'نعم' or mother == 'نعم' or father == 'نعم':
                w_s_d = 'الباقي'
                print(w_s_d, 'نصيب ابن الابن = ')

    elif s_d != 'نعم':
        w_s_d = 0

    if d_s_d == 'نعم' and husband != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and s_s_d != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                    if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                        if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                            if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if s_s_d != 'نعم':
                                            w_d_s_d = (money - deon) / n_d_s_d
                                            print(w_d_s_d, 'نصيب بنت الابن = ')
                                        else:
                                            w_d_s_d = (money - deon) / (-(n_d_s_d / 2) - n_s_s_d)
                                            print(w_d_s_d, 'نصيب بنت الابن = ')

    elif d_s_d == 'نعم':
        if son != 'نعم' and dut != 'نعم' and s_d != 'نعم' and d_d != 'نعم' and s_s_d != 'نعم':
            if n_d_s_d == 1:
                w_d_s_d = 1 / 2
                print(w_d_s_d, 'نصيب بنت الابن = ')
            elif n_d_s_d > 1:
                w_d_s_d = 2 / 3
                print(w_d_s_d, ' =(', n_d_s_d, 'نصيب بنات ابن الابن (')

    elif d_s_d != 'نعم':
        w_d_s_d = 0

    if s_s_d == 'نعم' and husband != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and cousin_c != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                    if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                        if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                            if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if d_s_d != 'نعم':
                                            w_s_s_d = (money - deon) / n_s_s_d
                                            print(w_s_s_d, 'نصيب ابن ابن الابن = ')
                                        else:
                                            w_s_s_d = (money - deon) / ((n_s_s_d) - (n_d_s_d / 2))
                                            print(w_s_s_d, 'نصيب ابن ابن الابن = ')

    elif s_s_d == 'نعم':
        if son != 'نعم' and dut != 'نعم' and s_d != 'نعم':
            if husband == 'نعم' or mother == 'نعم' or father == 'نعم':
                w_s_s_d = 'الباقي'
                print(w_s_s_d, 'نصيب ابن ابن الابن = ')

    elif s_s_d != 'نعم':
        w_s_s_d = 0

    if sister == 'نعم' and husband != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and cousin_c != 'نعم' and s_s_d != 'نعم':
            if sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                    if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                        if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                            if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if brother != 'نعم':
                                            w_sister = (money - deon) / n_sister
                                            print(w_sister, 'نصيب الاخت الشقيقة = ')
                                        else:
                                            w_sister = (money - deon) / -((n_sister / 2) - (n_brother))
                                            print(w_sister, 'نصيب الاخت الشقيقة = ')

    elif sister != 'نعم':
        w_sister = 0

    if brother == 'نعم' and husband != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and cousin_c != 'نعم' and s_s_d != 'نعم':
            if sister_f != 'نعم' and brother_f != 'نعم' and sister_m != 'نعم':
                if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                    if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                        if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                            if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if sister != 'نعم':
                                            w_brother = (money - deon) / n_brother
                                            print(w_brother, 'نصيب الاخ الشقيق = ')
                                        else:
                                            w_brother = (money - deon) / (n_brother - (n_sister / 2))
                                            print(w_brother, 'نصيب الاخ الشقيق = ')


    elif brother != 'نعم':
        w_brother = 0

    if sister_f == 'نعم' and husband != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and cousin_c != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_m != 'نعم':
                if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                    if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                        if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                            if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if brother_f != 'نعم':
                                            w_sister_f = (money - deon) / n_sister_f
                                            print(w_sister_f, 'نصيب الاخت لأب = ')
                                        else:
                                            w_sister_f = (money - deon) / (-((n_sister_f / 2) - n_brother_f))
                                            print(w_sister_f, 'نصيب الاخت لأب = ')

    elif sister_f != 'نعم':
        w_sister_f = 0

    if brother_f == 'نعم' and husband != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and cousin_c != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_m != 'نعم':
                if brother_m != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                    if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                        if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                            if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if sister_f != 'نعم':
                                            w_brother_f = (money - deon) / n_brother_f
                                            print(w_brother_f, 'نصيب الاخ لأب = ')

                                        else:
                                            w_brother_f = (money - deon) / (n_brother_f - (n_sister / 2))
                                            print(w_brother_f, 'نصيب الاخ لأب = ')

    elif brother_f != 'نعم':
        w_brother_f = 0

    if sister_m == 'نعم' and husband != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and cousin_c != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                if brother_f != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                    if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                        if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                            if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if brother_m != 'نعم':
                                            w_sister_m = (money - deon) / n_sister_m
                                            print(w_sister_m, 'نصيب الاخت لأب = ')
                                        else:
                                            w_sister_m = (money - deon) / -((n_sister_m / 2) - n_brother_m)
                                            print(w_sister_m, 'نصيب الاخت لأب = ')


    elif sister_m != 'نعم':
        w_sister_m = 0

    if brother_m == 'نعم' and husband != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and cousin_c != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                if brother_f != 'نعم' and d_b != 'نعم' and d_b_ != 'نعم' and d_d_b != 'نعم':
                    if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                        if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                            if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if sister_m != 'نعم':
                                            w_brother_m = (money - deon) / n_brother_m
                                            print(w_brother_m, 'نصيب الاخ لأم = ')
                                        else:
                                            w_brother_m = (money - deon) / (n_brother_m - (n_sister_m / 2))
                                            print(w_brother_m, 'نصيب الاخ لأم = ')


    elif brother_m != 'نعم':
        w_brother_m = 0

    if d_b == 'نعم' and husband != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and cousin_c != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_d_b != 'نعم':
                    if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                        if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                            if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if d_b_ != 'نعم':
                                            w_d_b = (money - deon) / n_d_b
                                            print(w_d_b, 'نصيب ابن اخ لأب = ')

    if d_b_ == 'نعم' and husband != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and cousin_c != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_d_b != 'نعم':
                    if d_d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                        if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                            if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if d_b != 'نعم':
                                            w_d_b_ = (money - deon) / n_d_b_
                                            print(w_d_b_, 'نصيب ابن اخ شقيق = ')

    if d_d_b == 'نعم' and husband != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and cousin_c != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_b != 'نعم':
                    if d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                        if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                            if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if d_d_b_ != 'نعم':
                                            w_d_d_b = (money - deon) / n_d_d_b
                                            print(w_d_d_b, 'نصيب ابن ابن اخ لأب = ')

    if d_d_b_ == 'نعم' and husband != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_b != 'نعم':
                    if d_b_ != 'نعم' and uncle_ != 'نعم' and uncle != 'نعم' and cousin != 'نعم':
                        if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                            if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if d_d_b != 'نعم':
                                            w_d_d_b_ = (money - deon) / n_d_d_b_
                                            print(w_d_d_b_, 'نصيب ابن ابن اخ شقيق = ')

    if uncle_ == 'نعم' and husband != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_b != 'نعم':
                    if d_b_ != 'نعم' and d_d_b_ != 'نعم' and d_d_b != 'نعم' and cousin != 'نعم':
                        if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                            if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if uncle != 'نعم':
                                            w_uncle = (money - deon) / n_uncle
                                            print(w_uncle, 'نصيب عم شقيق = ')

    if uncle == 'نعم' and husband != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_b != 'نعم':
                    if d_b_ != 'نعم' and d_d_b_ != 'نعم' and d_d_b != 'نعم' and cousin != 'نعم':
                        if cousin_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                            if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if uncle_ != 'نعم':
                                            w_uncle_ = (money - deon) / n_uncle_
                                            print(w_uncle_, 'نصيب عم لأب = ')

    if cousin == 'نعم' and husband != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_b != 'نعم':
                    if d_b_ != 'نعم' and d_d_b_ != 'نعم' and d_d_b != 'نعم' and uncle != 'نعم':
                        if uncle_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                            if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if cousin_ != 'نعم':
                                            w_cousin = (money - deon) / n_cousin
                                            print(w_cousin, 'نصيب ابن عم لأب = ')

    if cousin_ == 'نعم' and husband != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_b != 'نعم':
                    if d_b_ != 'نعم' and d_d_b_ != 'نعم' and d_d_b != 'نعم' and uncle != 'نعم':
                        if uncle_ != 'نعم' and cousin_c != 'نعم' and cousin_c_ != 'نعم' and uncle_f_f != 'نعم':
                            if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if cousin != 'نعم':
                                            w_cousin_ = (money - deon) / n_cousin_
                                            print(w_cousin_, 'نصيب ابن عم شقيق = ')

    if cousin_c == 'نعم' and husband != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_b != 'نعم':
                    if d_b_ != 'نعم' and d_d_b_ != 'نعم' and d_d_b != 'نعم' and uncle != 'نعم':
                        if uncle_ != 'نعم' and cousin != 'نعم' and cousin_ != 'نعم' and uncle_f_f != 'نعم':
                            if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if cousin_c_ != 'نعم':
                                            w_cousin_c = (money - deon) / n_cousin_c
                                            print(w_cousin_c, 'نصيب ابن ابن عم لأب = ')

    if cousin_c_ == 'نعم' and husband != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_b != 'نعم':
                    if d_b_ != 'نعم' and d_d_b_ != 'نعم' and d_d_b != 'نعم' and uncle != 'نعم':
                        if uncle_ != 'نعم' and cousin != 'نعم' and cousin_ != 'نعم' and uncle_f_f != 'نعم':
                            if uncle_f != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if cousin_c != 'نعم':
                                            w_cousin_c_ = (money - deon) / n_cousin_c_
                                            print(w_cousin_c_, 'نصيب ابن ابن عم شقيق = ')

    if uncle_f == 'نعم' and cousin_c_ != 'نعم' and husband != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_b != 'نعم':
                    if d_b_ != 'نعم' and d_d_b_ != 'نعم' and d_d_b != 'نعم' and uncle != 'نعم':
                        if uncle_ != 'نعم' and cousin != 'نعم' and cousin_ != 'نعم':
                            if cousin_c != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if uncle_f_f != 'نعم':
                                            w_uncle_f = (money - deon) / n_uncle_f
                                            print(w_uncle_f, 'نصيب عم لأب = ')

    if uncle_f_f == 'نعم' and cousin_c_ != 'نعم' and husband != 'نعم' and dut != 'نعم':
        if d_d != 'نعم' and s_d != 'نعم' and sister != 'نعم':
            if brother != 'نعم' and s_s_d != 'نعم' and d_s_d != 'نعم' and sister_f != 'نعم':
                if brother_f != 'نعم' and brother_m != 'نعم' and sister_m != 'نعم' and d_b != 'نعم':
                    if d_b_ != 'نعم' and d_d_b_ != 'نعم' and d_d_b != 'نعم' and uncle != 'نعم':
                        if uncle_ != 'نعم' and cousin != 'نعم' and cousin_ != 'نعم':
                            if cousin_c != 'نعم' and m_m_m != 'نعم' and m_f_f != 'نعم''نعم':
                                if mother != 'نعم' and father != 'نعم' and grand_m != 'نعم' and grand_f_f != 'نعم':
                                    if grand_f != 'نعم' and m_f != 'نعم':
                                        if uncle_f != 'نعم':
                                            w_uncle_f_f = (money - deon) / n_uncle_f_f
                                            print(w_uncle_f_f, 'نصيب عم شقيق = ')
#***********************************************************************
def choose():
    name='sara'
    m_w=input(' جنس المتوفي (ذكر- انثى) : ')
    global money
    money=int(input(' مقدار التركة : '))
    # maney=التركة
    global deon
    deon=int(input(' الديون  : '))
    #deon=الديون
    close=int(input('هل تريد الاستمرار في البرنامج (ادخل الرقم "1") او الخروج (ادخل الرفم "0"): '))
    if close==1:
        if m_w== 'ذكر' :
            man()
        elif m_w== 'انثى' :
            woman()
    elif close==0 :
        for i in range(1):
            print('Thank you ',name,' user the programming.'\
                  'شكرا ', name, 'لاستخدامك للبرنامج.')


def user():
    name=input('Enter your name '\
               '(ادخل اسمك/ي): ')
    password=int(input('Enter passward integer  '\
                       '(ادخل كلمة مرور): '))
    assert_password=int(input('Enter assert password'\
                        '(ادخل تأكيد كلمة المرور): '))
    if password==assert_password :
        print('********************************************************')
        print('Welcome '+name,' in ')
        print(' اهلا بك/ي ' ,name,\
              ' في برنامج حاسبة المواريث.')
        print('********************************************************')
    print()

    for i in range(1):
            if password!=assert_password:
                print('********************************************************')
                print('Soory ',name,'you enter false assert password\n'\
                      'عذرا ',name,' ادخلت تأكيد المرور خاطئ.')
                print('********************************************************')
                break
            elif password == assert_password:
                print('قال تعالى:  ﴿۞ لِّلرِّجَالِ نَصِيبٌ مِّمَّا تَرَكَ الْوَالِدَانِ' \
                      '\n' \
                      ' وَالْأَقْرَبُونَ وَلِلنِّسَاءِ نَصِيبٌ مِّمَّا تَرَكَ الْوَالِدَانِ وَالْأَقْرَبُونَ مِمَّا قَلَّ مِنْهُ أَوْ كَثُرَ ۚ نَصِيبًا مَّفْرُوضًا (7)' \
                      '\n' \
                      ' وَإِذَا حَضَرَ الْقِسْمَةَ أُولُو الْقُرْبَىٰ وَالْيَتَامَىٰ وَالْمَسَاكِينُ فَارْزُقُوهُم مِّنْهُ وَقُولُوا لَهُمْ قَوْلًا مَّعْرُوفًا (8) ' \
                      '\n' \
                      'وَلْيَخْشَ الَّذِينَ لَوْ تَرَكُوا مِنْ خَلْفِهِمْ ذُرِّيَّةً ضِعَافًا خَافُوا عَلَيْهِمْ فَلْيَتَّقُوا اللَّهَ وَلْيَقُولُوا قَوْلًا ' \
                      '\n' \
                      'سَدِيدًا (9) إِنَّ الَّذِينَ يَأْكُلُونَ أَمْوَالَ الْيَتَامَىٰ ظُلْمًا إِنَّمَا يَأْكُلُونَ فِي بُطُونِهِمْ نَارًا ۖ وَسَيَصْلَوْنَ' \
                      '\n' \
                      ' سَعِيرًا (10) يُوصِيكُمُ اللَّهُ فِي أَوْلَادِكُمْ ۖ لِلذَّكَرِ مِثْلُ حَظِّ الْأُنثَيَيْنِ ۚ فَإِن كُنَّ نِسَاءً فَوْقَ اثْنَتَيْنِ' \
                      '\n' \
                      ' فَلَهُنَّ ثُلُثَا مَا تَرَكَ ۖ وَإِن كَانَتْ وَاحِدَةً فَلَهَا النِّصْفُ ۚ وَلِأَبَوَيْهِ لِكُلِّ وَاحِدٍ مِّنْهُمَا السُّدُسُ مِمَّا تَرَكَ' \
                      '\n' \
                      ' إِن كَانَ لَهُ وَلَدٌ ۚ فَإِن لَّمْ يَكُن لَّهُ وَلَدٌ وَوَرِثَهُ أَبَوَاهُ فَلِأُمِّهِ الثُّلُثُ ۚ فَإِن كَانَ لَهُ إِخْوَةٌ فَلِأُمِّهِ ' \
                      '\n' \
                      'السُّدُسُ ۚ مِن بَعْدِ وَصِيَّةٍ يُوصِي بِهَا أَوْ دَيْنٍ ۗ آبَاؤُكُمْ وَأَبْنَاؤُكُمْ لَا تَدْرُونَ أَيُّهُمْ أَقْرَبُ لَكُمْ نَفْعًا ' \
                      '\n' \
                      'ۚ فَرِيضَةً مِّنَ اللَّهِ ۗ إِنَّ اللَّهَ كَانَ عَلِيمًا حَكِيمًا (11) وَلَكُمْ نِصْفُ مَا تَرَكَ أَزْوَاجُكُمْ إِن لَّمْ يَكُن' \
                      '\n' \
                      ' لَّهُنَّ وَلَدٌ ۚ فَإِن كَانَ لَهُنَّ وَلَدٌ فَلَكُمُ الرُّبُعُ مِمَّا تَرَكْنَ ۚ مِن بَعْدِ وَصِيَّةٍ يُوصِينَ بِهَا أَوْ دَيْنٍ ۚ وَلَهُنَّ ' \
                      '\n' \
                      'الرُّبُعُ مِمَّا تَرَكْتُمْ إِن لَّمْ يَكُن لَّكُمْ وَلَدٌ ۚ فَإِن كَانَ لَكُمْ وَلَدٌ فَلَهُنَّ الثُّمُنُ مِمَّا تَرَكْتُم ۚ مِّن بَعْدِ' \
                      '\n' \
                      ' وَصِيَّةٍ تُوصُونَ بِهَا أَوْ دَيْنٍ ۗ وَإِن كَانَ رَجُلٌ يُورَثُ كَلَالَةً أَوِ امْرَأَةٌ وَلَهُ أَخٌ أَوْ أُخْتٌ فَلِكُلِّ وَاحِدٍ' \
                      '\n' \
                      ' مِّنْهُمَا السُّدُسُ ۚ فَإِن كَانُوا أَكْثَرَ مِن ذَٰلِكَ فَهُمْ شُرَكَاءُ فِي الثُّلُثِ ۚ مِن بَعْدِ وَصِيَّةٍ يُوصَىٰ بِهَا أَوْ' \
                      '\n' \
                      ' دَيْنٍ غَيْرَ مُضَارٍّ ۚ وَصِيَّةً مِّنَ اللَّهِ ۗ وَاللَّهُ عَلِيمٌ حَلِيمٌ (12) تِلْكَ حُدُودُ اللَّهِ ۚ وَمَن يُطِعِ اللَّهَ' \
                      '\n' \
                      ' وَرَسُولَهُ يُدْخِلْهُ جَنَّاتٍ تَجْرِي مِن تَحْتِهَا الْأَنْهَارُ خَالِدِينَ فِيهَا ۚ وَذَٰلِكَ الْفَوْزُ الْعَظِيمُ (13) ' \
                      '\n' \
                      'وَمَن يَعْصِ اللَّهَ وَرَسُولَهُ وَيَتَعَدَّ حُدُودَهُ يُدْخِلْهُ نَارًا خَالِدًا فِيهَا وَلَهُ عَذَابٌ مُّهِينٌ (14) ﴾' \
                      '\n' \
                      '[النساء:7-14].')
                print()
                print('﴿لِلرِّجَالِ ‌نَصِيبٌ مِمَّا اكْتَسَبُوا وَلِلنِّسَاءِ نَصِيبٌ مِمَّا اكْتَسَبْنَ﴾ [النساء:32].')
                print()
                print(
                    '﴿وَإِنْ كَانُوا إِخْوَةً ‌رِجَالًا ‌وَنِسَاءً فَلِلذَّكَرِ مِثْلُ حَظِّ الْأُنْثَيَيْنِ﴾ [النساء:176].')
                print()
                print('***********************************************************************************')
                print()
                choose()
user()