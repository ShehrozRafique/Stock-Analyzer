def outlier(df):

    price = df[ "Close" ]

    q1 = price.quantile(0.25)
    q3 = price.quantile(0.75)

    IQR = q3 - q1

    lower_limit = q1 - 1.5 * IQR
    upper_limit = q3 + 1.5 * IQR

    outliers = df[(price < lower_limit) | (price > upper_limit)]

    print( "----Outlier Analysis----" )
    print( "Q1:" , round(q1,2) )
    print( "Q3:" , round(q3,2) )
    print( "Inter Quantile Range:" , round(IQR,2) )
    print( "Number of Outliers: " , len(outliers) )

    return outliers