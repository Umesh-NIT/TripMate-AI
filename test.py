from tools import tavily_tool
from tools import flight_tool
from backend import run_travel_agent
#res = tavily_tool.tavily_search("best hotels in indonesia")
#res = flight_tool.search_flights("Plan a 7 days Japan trip from Bangladesh")
#print(res)
res = run_travel_agent("Plan a 7 days Japan trip from Bangladesh")
print(res)