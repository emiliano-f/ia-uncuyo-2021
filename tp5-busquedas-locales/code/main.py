from hill_climbing_std import HillClimbingStd

def main():
    bot: HillClimbingStd = HillClimbingStd(8, 20)
    print(bot.board, bot.get_fn())
    print(bot.think(), bot.get_fn())

if __name__ == "__main__":
    main()
