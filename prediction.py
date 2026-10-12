def prediction(df) :
    
    df[ "Daily return" ] = df[ "Close" ].pct_change()
    average_return = df[ "Daily return" ].mean()
    current_price = df[ "Close" ].iloc[-1]

    predict_price = current_price * ( 1 + average_return )

    print( "----Price Prediction-----" )
    print( "Current Price : " , round(current_price , 2) )
    print( "Daily Average Return : " , round(average_return * 100 , 4 ) , "%" )
    print( "Estimated Price : " , round(predict_price , 2) )

    return predict_price


