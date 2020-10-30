# To run an algorithm in Quantopian, you need two functions: initialize and 
# handle_data.


def initialize(context):
    # This initialize function sets any data or variables that you'll use in
    # your algorithm.  For instance, you'll want to define the security (or 
    # securities) you want to backtest.  You'll also want to define any 
    # parameters or values you're going to use.

    # In our example, we're looking at Apple.  If you re-type this line 
    # yourself, you'll see the auto-complete that is available for the 
    # security ID.
    context.stock = sid(24)


def handle_data(context, data):
    # This handle_data function is where the real work is done.  Our data is
    # minute-level tick data, and each minute is called a frame.  This function
    # runs on each frame of the data.
    
    # We will be working with Apple only
    stock = context.stock
    
    # And we will need Apple current and historic data
    stock_data = data[stock]
    
    # We will need average price data
    mavg_short = stock_data.mavg(5)
    mavg_long = stock_data.mavg(30)
    
    # And the current price of the stock
    current_price = stock_data.price

    # In order to make market decisions we need to know how much cash we have
    cash = context.portfolio.cash
   

    # This is the meat of the algorithm, placed in this if statement.
    if mavg_short > mavg_long and cash > current_price:
        
        # When buying we need to know how many shares we can buy
        number_of_shares = int(cash/current_price)
        # int() helps us get a integer value, we can't buy half a share you know
        
        # Finally, we place the buy order
        order(stock, number_of_shares)
    elif mavg_short < mavg_long:
        # Before we sell we need to know how many shares we have
        number_of_shares = context.portfolio.positions[stock.sid].amount
        
        # Now we can sell
        order(stock, -number_of_shares) # When selling we need to pass a negative number of shares
