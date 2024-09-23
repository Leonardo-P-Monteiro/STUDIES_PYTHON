
def multiplier_factor(factor):
    
    def multiplicated(number):
        return factor * number

    return multiplicated

duplicator = multiplier_factor(2)
triplicator = multiplier_factor(3)
print(duplicator(2), triplicator(2))
