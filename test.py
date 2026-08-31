from tools import tavily_tool
from tools import flight_tool

#res = tavily_tool.tavily_search("best hotels in indonesia")
res = flight_tool.search_flights("Plan a 7 days Japan trip from Bangladesh")
print(res)