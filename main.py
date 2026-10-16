"""Run this file from the project folder to display the example KPIs."""

from kpi.warehouse import capacity_utilization, picking_accuracy, throughput


def main():
    print("Throughput:", throughput(120, 4), "units/hour")
    print("Capacity utilization:", capacity_utilization(20, 24), "%")
    print("Picking accuracy:", picking_accuracy(98, 100), "%")


if __name__ == "__main__":
    main()
