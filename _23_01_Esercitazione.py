import humanize
humanize.intcomma (123456)
humanize.intword(123455913) 
humanize.intword(12345591313) 
humanize.naturalsize(1000000) 
humanize.scientific(500)
import datetime as dt
humanize.naturaldelta(dt.timedelta(seconds=2)) 
'2 seconds'