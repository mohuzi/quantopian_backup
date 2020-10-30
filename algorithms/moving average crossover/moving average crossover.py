"""
This is a template algorithm on Quantopian for you to adapt and fill in.
"""
from quantopian.algorithm import attach_pipeline, pipeline_output
from quantopian.pipeline import Pipeline
from quantopian.pipeline.data.builtin import USEquityPricing
from quantopian.pipeline.factors import AverageDollarVolume
 
def initialize(context):
    """
    Called once at the start of the algorithm.
    """   
    # Rebalance every day, 1 hour after market open.
    schedule_function(my_rebalance, date_rules.every_day(), time_rules.market_open(hours=1))
     
    # Record tracking variables at the end of each day.
    schedule_function(my_record_vars, date_rules.every_day(), time_rules.market_close())
     
    # Create our dynamic stock selector.
    attach_pipeline(my_pipeline(context), 'my_pipeline')
         
def my_pipeline(context):
    """
    A function to create our dynamic stock selector (pipeline). Documentation on
    pipeline can be found here: https://www.quantopian.com/help#pipeline-title
    """
    pipe = Pipeline()
     
    # Create a dollar volume factor.
    dollar_volume = AverageDollarVolume(window_length=1)
    pipe.add(dollar_volume, 'dollar_volume')
 
    # Pick the top 1% of stocks ranked by dollar volume.
    high_dollar_volume = dollar_volume.percentile_between(99, 100)
    pipe.set_screen(high_dollar_volume)
     
    return pipe
 
def before_trading_start(context, data):
    """
    Called every day before market open.
    """
    context.output = pipeline_output('my_pipeline')
  
    # These are the securities that we are interested in trading each day.
    context.security_list = context.output.index
     
def my_assign_weights(context, data):
    """
    Assign weights to securities that we want to order.
    """
    pass
 
def my_rebalance(context,data):
    """
    Execute orders according to our schedule_function() timing. 
    """
    pass
 
def my_record_vars(context, data):
    """
    Plot variables at the end of each day.
    """
    pass
 
def handle_data(context,data):
    """
    Called every minute.
    """
    pass
