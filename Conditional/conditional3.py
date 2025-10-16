# Switch Statement

day = 5

def get_month_str(month: int) -> str:
    match(month):
        case 1:
            return "january"
        case 2:
            return "February"
        case 3:
            return "March"
        case 4:
            return "April"
        case 5:
            return "May"
        case 6:
            return "June"
        case 7:
            return "July"
        case 8:
            return "August"
        case 9:
            return "September"
        case 10:
            return "Octomber"
        case 11:
            return "November"
        case 12:
            return "December"
        case _:
            return "Invalid"

        
print(get_month_str(50))
print(get_month_str(-2))
print(get_month_str(1.0))
print(get_month_str(3.4))
print(get_month_str(5))