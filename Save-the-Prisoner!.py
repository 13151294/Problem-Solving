for i in range(int(input())):
    Seats, Candy, Start = map(int, input().split())
    EndSeats = (Start + Candy - 1) % Seats
    print(EndSeats if (EndSeats != 0) else Seats)
