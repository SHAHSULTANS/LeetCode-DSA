class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output=[0 for i in range(len(temperatures))]

        stack=[]

        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                stack_index=stack.pop()
                # print(temperatures[stack_index]," ",stack_index," ",i)
                output[stack_index]=i-stack_index

            stack.append(i)

        return output
    
# Next Greater Element – Real World Applications

# 1️⃣ Weather Forecast / Daily Temperatures
#    - Data: daily temperature series
#    - Goal: For each day, find how many days until the next warmer day
#    - Example: [73, 74, 75, 71, 69, 72, 76, 73] → Output: [1,1,1,2,1,1,0]
#    - Used in weather apps for “Next warmer day” prediction

# 2️⃣ Stock Market / Price Alerts
#    - Data: daily stock prices
#    - Goal: For each day, find the next day with a higher stock price
#    - Example: [100, 101, 99, 105] → Output: [1,2,1,0]
#    - Used in trading apps to notify “Wait days until price rises”

# 3️⃣ Product Pricing / E-commerce
#    - Data: historical product prices
#    - Goal: Find when price will next increase
#    - Example: [20, 22, 21] → Output: [1,0,0]
#    - Used in e-commerce apps for price alerts or discount predictions

# 4️⃣ Traffic / Speed Analysis
#    - Data: traffic speed per hour
#    - Goal: For each hour, find the next hour with higher speed
#    - Example: [40, 45, 42, 50] → Output: [1,2,1,0]
#    - Used in smart traffic systems to predict congestion relief

# 5️⃣ Energy / Power Consumption
#    - Data: hourly electricity usage
#    - Goal: For each hour, find when consumption will rise next
#    - Example: [50, 55, 53, 60] → Output: [1,2,1,0]
#    - Used in smart grids to predict peak loads

# 6️⃣ Water Level / Rainfall Prediction
#    - Data: river water levels or rainfall amounts
#    - Goal: For each time, predict next higher level
#    - Example: [10, 12, 11, 15] → Output: [1,2,1,0]
#    - Used in flood monitoring and early warning systems

# 7️⃣ Customer Metrics / Website Traffic
#    - Data: daily website visits
#    - Goal: Find next day with higher traffic
#    - Example: [200, 220, 210, 230] → Output: [1,2,1,0]
#    - Used in analytics to plan server scaling or marketing campaigns

# 🔑 Key Insight:
#    - Any scenario where you want to know "next bigger value" in a series can use Next Greater Element
#    - Stack-based approach makes it O(n), efficient for real-time applications
