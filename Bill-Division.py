n, d = map(int, input().split())
Cost = list(map(int, input().split()))
ChargeBill = int(input())
Cost.pop(d)
ActualBill= sum(Cost)/2
print(int(ChargeBill-ActualBill) if ChargeBill > ActualBill else "Bon Appetit")