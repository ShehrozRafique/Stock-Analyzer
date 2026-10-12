def monthly_analysis(df):

    data = df.copy()

    data [ "Month" ] = data[ "Date" ].dt.to_period("M")
    monthly = data.groupby( "Month" ).agg({

        "Close" : "mean",
        "High"  : "max",
        "Low"   : "min",
        "Volume": "mean"

    })

    print( "----Monthly Analysis----" )
    print(monthly)

    return monthly

def yearly_analysis(df):

    data = df.copy()

    data [ "Year" ] = data[ "Date" ].dt.year
    yearly = data.groupby( "Year" ).agg({

        "Close" : "mean",
        "High"  : "max",
        "Low"   : "min",
        "Volume": "mean"

    })

    print( "----Yearly Analysis----" )
    print(yearly)
    
    return yearly
