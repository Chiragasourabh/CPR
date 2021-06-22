def CPR(HIGH,LOW,OPEN,CLOSE,method="TRADITIONAL"):
    if method=="TRADITIONAL":
        PP = (HIGH + LOW + CLOSE) / 3
        R1 = PP * 2 - LOW
        S1 = PP * 2 - HIGH
        R2 = PP + (HIGH - LOW)
        S2 = PP - (HIGH - LOW)
        R3 = PP * 2 + (HIGH - 2 * LOW)
        S3 = PP * 2 - (2 * HIGH - LOW)
        R4 = PP * 3 + (HIGH - 3 * LOW)
        S4 = PP * 3 - (3 * HIGH - LOW)
        R5 = PP * 4 + (HIGH - 4 * LOW)
        S5 = PP * 4 - (4 * HIGH - LOW)
        return {"PP":PP,"R1":R1,"S1":S1,"R2":R2,"S2":S2,"R3":R3,"S3":S3,"R4":R4,"S4":S4,"R5":R5,"S5":S5}

    elif method=="FIBONACCI":
        PP = (HIGH + LOW + CLOSE) / 3
        R1 = PP + 0.382 * (HIGH - LOW)
        S1 = PP - 0.382 * (HIGH - LOW)
        R2 = PP + 0.618 * (HIGH - LOW)
        S2 = PP - 0.618 * (HIGH - LOW)
        R3 = PP + (HIGH - LOW)
        S3 = PP - (HIGH - LOW)
        return {"PP":PP,"R1":R1,"S1":S1,"R2":R2,"S2":S2,"R3":R3,"S3":S3}
        
    # elif method=="WOODIE":
    #     PP = (HIGH + LOW + 2 * OPENcurr) / 4
    #     R1 = 2 * PP - LOW
    #     S1 = 2 * PP - HIGH
    #     R2 = PP + (HIGH - LOW)
    #     S2 = PP - (HIGH - LOW)
    #     R3 =  HIGH + 2 * (PP -  LOW)
    #     S3 =  LOW - 2 * (HIGH - PP)
    #     R4 = R3 + (HIGH - LOW)
    #     S4 = S3 - (HIGH - LOW)
    #     return {"PP":PP,"R1":R1,"S1":S1,"R2":R2,"S2":S2,"R3":R3,"S3":S3,"R4":R4,"S4":S4}

    elif method =="CLASSIC":
        PP = (HIGH + LOW + CLOSE) / 3    
        R1 = 2 * PP - LOW    
        S1 = 2 * PP - HIGH    
        R2 = PP + (HIGH - LOW)    
        S2 = PP - (HIGH - LOW)    
        R3 = PP + 2 * (HIGH - LOW)    
        S3 = PP - 2 * (HIGH - LOW)    
        R4 = PP + 3 * (HIGH - LOW)    
        S4 = PP - 3 * (HIGH - LOW)
        return {"PP":PP,"R1":R1,"S1":S1,"R2":R2,"S2":S2,"R3":R3,"S3":S3,"R4":R4,"S4":S4}

    elif method =="DEMARK":
        if OPEN == CLOSE:
            X = HIGH + LOW + 2 * CLOSE    
        elif CLOSE >  OPEN:
            X = 2 * HIGH + LOW + CLOSE
        else:
            X = 2 * LOW + HIGH + CLOSE    
        PP = X / 4    
        R1 = X / 2 - LOW    
        S1 = X / 2 - HIGH
        return {"PP":PP,"R1":R1,"S1":S1}

    elif method =="CAMARILLA":
        PP = (HIGH + LOW + CLOSE) / 3    
        R1 = CLOSE + 1.1 * (HIGH - LOW) / 12    
        S1 = CLOSE - 1.1 * (HIGH - LOW) / 12    
        R2 = CLOSE + 1.1 * (HIGH - LOW) / 6    
        S2 = CLOSE - 1.1 * (HIGH - LOW) / 6    
        R3 = CLOSE + 1.1 * (HIGH - LOW) / 4    
        S3 = CLOSE - 1.1 * (HIGH - LOW) / 4    
        R4 = CLOSE + 1.1 * (HIGH - LOW) / 2    
        S4 = CLOSE - 1.1 * (HIGH - LOW) / 2
        return {"PP":PP,"R1":R1,"S1":S1,"R2":R2,"S2":S2,"R3":R3,"S3":S3,"R4":R4,"S4":S4}
    else:
        return {"message":"Invalid method"}
        