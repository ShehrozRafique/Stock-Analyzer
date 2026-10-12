from api import get_stockdata
from data import process_data, save_data, load_data
from stats import show_stats
from price_analysis import price_change , daily_return , highest_price , lowest_price , best_tradeday , Bad_tradeday
from volume_analysis import volume_analysis , highest_volume_day , lowest_volume_day
from trend_analysis import moving_average , detect_trend , daily_movements
from outlier_analysis import outlier
from monthly_analysis import monthly_analysis , yearly_analysis
from visualizing import closing_PriceChart , Volume_Chart , moving_average_chart , daily_returnChart , boxplot
from prediction import prediction
from report import generateReport

def main():

    print("Welcome to the Stock Data Fetcher!")
    symbol = input("Enter the stock symbol: ").upper()
    api_data = get_stockdata(symbol)

    if api_data is None:

        return

    df = process_data(api_data)
    if df is None:

        return

    save_data(df)

    print("\n Data loaded ")
    print("Number of records : ", len(df) )

    while True:

        print("1. Display Data ")
        print("2. Basic Stats ")
        print("3. Price Analysis ")
        print("4. Volume Analysis ")
        print("5. Trend Analysis ")
        print("6. Outlier Analysis ")
        print("7. Monthly Analysis ")
        print("8. Yearly Analysis ")
        print("9. Charts ")
        print("10. Prediction ")
        print("11. Generate Report ")
        print("12. Exit ")

        choice = input("Enter your Choice : ")

        if choice == "1" :

            print(df.head(20)) 

        elif choice == "2" :

            show_stats(df)       

        elif choice == "3" :

            price_change(df)
            daily_return(df)
            highest_price(df)
            lowest_price(df)
            best_tradeday(df)
            Bad_tradeday(df)

        elif choice == "4" :

            volume_analysis(df)
            highest_volume_day(df)
            lowest_volume_day(df)

        elif choice == "5" :

            moving_average(df)
            detect_trend(df)
            daily_movements(df)

        elif choice == "6" :

            outlier(df)

        elif choice == "7" :

            monthly_analysis(df)

        elif choice == "8" :

            yearly_analysis(df)

        elif choice == "9" :

            closing_PriceChart(df)
            Volume_Chart(df)
            moving_average_chart(df)
            daily_returnChart(df)
            boxplot(df)

        elif choice == "10" :

            prediction(df)

        elif choice == "11" :

            prediction_price = prediction(df)
            generateReport(df, symbol, prediction_price)
            
        elif choice == "12" :

            break

        else:

            print( "Inavalid Choice" )
    
main()