####################################################################
# Main.py.                                                         #
# This file simulates the entire model of passenger arrivals and   #
# train arrivals.                                                  #
# After the simulation, this program will return some important    #
# statistics results:                                              #
#     (1) avg_time: The average waiting time of all passengers.    #
#     (2) worst_time: The longest waiting time in this simulation. #
####################################################################

import random
from Train import Train
from Station import Station
from Passenger import Passenger

# 全局变量
time_sum = 0  # 所有乘客的等待时间总和
worst_time = -1  # 最长等待时间
total_passengers = 0  # 总乘客数
clock = 0  # 全局时钟

def main(train_plan):
    global clock, time_sum, worst_time, total_passengers
    
    # 创建所有车站
    stations = ["Station A", "Station B", "Station C", "Station D", "Station E"]
    station_objects = {name: Station(name) for name in stations}

    # 模拟一天的列车和乘客流动
    while clock < 24 * 60:  # 假设一天有 1440 分钟
        # 为每个车站生成乘客

        print(f"当前时间: {clock}")  # 调试输出，查看全局时钟

        for station in station_objects.values():
            station.generate_passenger(0.1, clock)  # 假设生成乘客的概率是 0.1

        # 检查是否有列车到达，并根据列车计划创建列车
        for train_time, train_size in train_plan:
            if clock == train_time:
                train = Train(clock, train_size)  # 创建列车
                # 让列车到站并乘客下车、上车
                for station in station_objects.values():
                    # 处理列车在每个车站的乘客
                    time_sum_at_station, worst_time_at_station, passengers_taken = train.take_from(station, clock)
                    time_sum += time_sum_at_station
                    worst_time = max(worst_time, worst_time_at_station)
                    total_passengers += passengers_taken
                    # 列车到站后检查是否需要将乘客从车上移除
                    train.check_departure(station)
                
        # 时间增加
        clock += 1

    # 计算平均等待时间
    if total_passengers > 0:
        avg_time = time_sum / total_passengers
    else:
        avg_time = 0

    # 输出结果
    print(f"模拟结束：\n平均等待时间: {avg_time:.2f} 分钟\n最长等待时间: {worst_time} 分钟\n总乘客数: {total_passengers}")

# 示例列车计划：[(列车到达时间, 列车最大载客量), ...]
train_plan = [
    (300, 50),  # 300分钟时，列车到达，最大载客量为50
    (600, 50),
    (900, 50),
    (1200, 50)
]

# 运行主函数进行模拟
if __name__ == "__main__":
    main(train_plan)
