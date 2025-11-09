import random
import time
import os
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(0.02)
    print()

def save_match_result(player_team, score_player, score_comp, result):
    with open("match_history.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | "
                f"Team: {player_team} | Result: {score_player}-{score_comp} | {result}\n")

def show_team_photo(team_name):
    clear_screen()
    team_photos = {
        "Real Madrid": """
        ╔═════════════════════════╗
        ║      REAL MADRID CF     ║
        ║         ⚪⚪⚪           ║
        ║        ⚪👤⚪           ║
        ║         ⚪⚪⚪           ║
        ║    🇪🇸 Los Blancos     ║
        ╚═════════════════════════╝
        """,
        "Barcelona": """
        ╔═════════════════════════╗
        ║      FC BARCELONA       ║
        ║         🔵🔴🔵         ║
        ║        🔴👤🔴         ║
        ║         🔵🔴🔵         ║
        ║     🏆 Mes Que Un Club  ║
        ╚═════════════════════════╝
        """,
        "Manchester United": """
        ╔═════════════════════════╗
        ║   MANCHESTER UNITED     ║
        ║         🔴🔴🔴         ║
        ║        🔴👤🔴         ║
        ║         🔴⚪🔴         ║
        ║      👹 Red Devils      ║
        ╚═════════════════════════╝
        """,
        "Liverpool": """
        ╔═════════════════════════╗
        ║      LIVERPOOL FC       ║
        ║         🔴🔴🔴         ║
        ║        🔴👤🔴         ║
        ║         🔴🔴🔴         ║
        ║   🔴 You'll Never Walk  ║
        ║         Alone 🔴        ║
        ╚═════════════════════════╝
        """
    }
    print(team_photos.get(team_name, team_photos["Real Madrid"]))
    time.sleep(2)

def show_celebration():
    clear_screen()
    frames = [
        """
        ╔══════════════════════════════╗
        ║        GOAL CELEBRATION!     ║
        ║        \\O/  🎉              ║
        ║         |   🎊              ║
        ║        / \\  💥              ║
        ║    WHAT A STRIKE! ⚽        ║
        ╚══════════════════════════════╝
        """,
        """
        ╔══════════════════════════════╗
        ║        GOAL CELEBRATION!     ║
        ║       🎉  ⚽  🎊            ║
        ║         \\ /                 ║
        ║          O   💥             ║
        ║         / \\                 ║
        ║    INCREDIBLE FINISH!       ║
        ╚══════════════════════════════╝
        """
    ]
    for frame in frames:
        clear_screen()
        print(frame)
        time.sleep(0.5)

def show_goalkeeper():
    clear_screen()
    frames = [
        """
        ╔══════════════════════════════╗
        ║        GOALKEEPER SAVE!      ║
        ║           ___                ║
        ║          /   \\   🧤        ║
        ║         |  🥅  |             ║
        ║          \\___/             ║
        ║      UNLUCKY! GREAT SAVE     ║
        ╚══════════════════════════════╝
        """,
        """
        ╔══════════════════════════════╗
        ║        GOALKEEPER SAVE!      ║
        ║           ___     🧤        ║
        ║          / 🥅 \\             ║
        ║         |       |            ║
        ║          \\___/             ║
        ║      INCREDIBLE STOP!        ║
        ╚══════════════════════════════╝
        """
    ]
    for frame in frames:
        clear_screen()
        print(frame)
        time.sleep(0.5)

def goal_animation(player, team_name):
    if player == "Player":
        show_celebration()
        print_slow("⚽ GOOOAAALLL!!! ⚽")
        print_slow(f"🎉 {team_name} scores a stunning goal! 💥")
    else:
        show_goalkeeper()
        print_slow("⚽ GOAL AGAINST! ⚽")
        print_slow("😮 Computer finds the net with a perfect strike!")

def crowd_cheer():
    cheers = [
        "👥 Crowd: OLE OLE OLEEEE!",
        "🔥 Fans are going wild in the stands!",
        "🎤 What a move! What a moment!",
        "💫 Stadium echoing with chants!",
        "📢 GOAL! GOAL! GOAL!"
    ]
    print(random.choice(cheers))

def get_player_input(prompt, max_value=10):
    while True:
        try:
            value = input(prompt)
            if value.lower() in ['q', 'quit', 'exit']:
                print("👋 Thanks for playing!")
                exit()
            value = int(value)
            if 1 <= value <= max_value:
                return value
            else:
                print(f"😅 Please enter 1-{max_value}!")
        except ValueError:
            print("😅 Please enter a number!")

def choose_team():
    teams = ["Real Madrid", "Barcelona", "Manchester United", "Liverpool"]
    print("\n🏆 CHOOSE YOUR TEAM:")
    for i, team in enumerate(teams, 1):
        print(f"{i}. {team}")
    
    choice = get_player_input("Enter team number (1-4): ", 4)
    selected_team = teams[choice-1]
    show_team_photo(selected_team)
    return selected_team

def choose_difficulty():
    print("\n🎯 Choose difficulty:")
    print("1. Easy 🟢")
    print("2. Medium 🟡") 
    print("3. Hard 🔴")
    
    while True:
        choice = input("Enter 1, 2 or 3: ")
        if choice == '1':
            return 10, "Easy 🟢"
        elif choice == '2':
            return 7, "Medium 🟡"
        elif choice == '3':
            return 5, "Hard 🔴"
        else:
            print("Please enter 1, 2, or 3!")

def hand_football():
    clear_screen()
    print_slow("⚽ Welcome to HAND FOOTBALL 🏆")
    print_slow("🎮 LIVE MATCH EXPERIENCE!")
    
    player_team = choose_team()
    limit, difficulty = choose_difficulty()
    
    rounds = 10
    score_player = 0
    score_comp = 0
    ball = "Player"

    for round_no in range(1, rounds + 1):
        clear_screen()
        print(f"\n{'='*40}")
        print(f"⚡ ROUND {round_no} | Score: {score_player}-{score_comp}")
        print(f"🎯 Your Team: {player_team}")
        print(f"🤖 Computer Team: Opponent")
        print(f"🏃 Possession: {ball}")
        print(f"{'='*40}")

        if ball == "Player":
            player = get_player_input("Your attack (1-10): ")
            comp = random.randint(1, limit)
            print(f"🤖 Computer defends with {comp}")

            if player == comp:
                score_player += 1
                goal_animation("Player", player_team)
                crowd_cheer()
            elif abs(player - comp) == 1:
                ball = "Computer"
                show_goalkeeper()
                print("🌀 Possession changes to Computer!")
            else:
                print("➡️ Shot missed! Continue...")

        else:
            comp = random.randint(1, limit)
            player = get_player_input("Your defense (1-10): ")
            print(f"🤖 Computer attacks with {comp}")

            if player == comp:
                score_comp += 1
                goal_animation("Computer", player_team)
                crowd_cheer()
            elif abs(player - comp) == 1:
                ball = "Player"
                show_goalkeeper()
                print("🌀 Possession switches to You!")
            else:
                print("➡️ Attack defended! No score.")

        print(f"\n📊 Score: {player_team} {score_player} - {score_comp} Opponent")
        time.sleep(2)

        if score_player == 5 or score_comp == 5:
            break

    clear_screen()
    print("\n🏁 FINAL WHISTLE 🏁")
    print(f"FINAL: {player_team} {score_player} - {score_comp} Opponent")

    if score_player > score_comp:
        show_celebration()
        print_slow(f"🏆 {player_team} WINS! LEGENDARY! 🔥")
        save_match_result(player_team, score_player, score_comp, "WIN")
    elif score_player < score_comp:
        print_slow("😢 Computer wins. Better luck next time.")
        save_match_result(player_team, score_player, score_comp, "LOSS")
    else:
        print_slow("🤝 Draw! Going to GOLDEN GOAL ⚡")
        golden_goal(ball, limit, player_team)

    replay = input("\n🔄 Play again? (y/n): ").lower()
    if replay == 'y':
        hand_football()
    else:
        print("👋 Thanks for playing!")

def golden_goal(ball, limit, player_team):
    print_slow("\n⚡ GOLDEN GOAL - Next goal wins!")
    
    while True:
        print(f"\nPossession: {ball}")
        
        if ball == "Player":
            player = get_player_input("Golden attack (1-10): ")
            comp = random.randint(1, limit)
            print(f"🤖 Computer defends with {comp}")

            if player == comp:
                show_celebration()
                print_slow("🏆 GOLDEN GOAL! YOU WIN! 🎉")
                save_match_result(player_team, 1, 0, "GOLDEN GOAL WIN")
                break
            elif abs(player - comp) == 1:
                ball = "Computer"
                show_goalkeeper()
            else:
                if random.random() < 0.5:
                    ball = "Computer"

        else:
            comp = random.randint(1, limit)
            player = get_player_input("Golden defense (1-10): ")
            print(f"🤖 Computer attacks with {comp}")

            if player == comp:
                show_goalkeeper()
                ball = "Player"
            elif abs(player - comp) == 1:
                pass
            else:
                show_goalkeeper()
                print_slow("😩 COMPUTER SCORES! You lose.")
                save_match_result(player_team, 0, 1, "GOLDEN GOAL LOSS")
                break

if __name__ == "__main__":
    try:
        hand_football()
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for playing!")
