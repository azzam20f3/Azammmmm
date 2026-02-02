import random

def display_welcome():
    """Menampilkan pesan selamat datang"""
    print("\n" + "="*50)
    print("        SELAMAT DATANG DI GAME BATU GUNTING KERTAS")
    print("="*50 + "\n")

def get_computer_choice():
    """Komputer memilih secara acak"""
    return random.choice(["batu", "gunting", "kertas"])

def get_player_choice():
    """Mendapatkan pilihan pemain dengan validasi"""
    valid_choices = ["batu", "gunting", "kertas"]
    
    while True:
        choice = input("\nPilih (batu/gunting/kertas): ").lower().strip()
        
        if choice not in valid_choices:
            print("❌ Input tidak valid! Silakan pilih: batu, gunting, atau kertas")
            continue
        
        return choice

def determine_winner(player, computer):
    """Menentukan pemenang permainan"""
    if player == computer:
        return "seri"
    
    # Aturan kemenangan
    winning_moves = {
        "batu": "gunting",      # Batu mengalahkan gunting
        "gunting": "kertas",    # Gunting mengalahkan kertas
        "kertas": "batu"        # Kertas mengalahkan batu
    }
    
    if winning_moves[player] == computer:
        return "menang"
    else:
        return "kalah"

def display_result(player, computer, result):
    """Menampilkan hasil permainan"""
    print("\n" + "-"*50)
    print(f"Pilihan Anda       : {player.upper()}")
    print(f"Pilihan Komputer   : {computer.upper()}")
    print("-"*50)
    
    if result == "menang":
        print("✅ ANDA MENANG! 🎉")
    elif result == "kalah":
        print("❌ ANDA KALAH! 😢")
    else:
        print("🤝 SERI!")
    print("-"*50)
    
    return result

def play_single_game():
    """Bermain satu game"""
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    display_result(player_choice, computer_choice, result)
    return result

def play_best_of_three():
    """Mode Best of 3"""
    print("\n" + "="*50)
    print("           MODE BEST OF 3")
    print("="*50)
    
    player_wins = 0
    computer_wins = 0
    game_count = 1
    
    while player_wins < 2 and computer_wins < 2:
        print(f"\n🎮 GAME {game_count}")
        print(f"Skor: Anda {player_wins} - Komputer {computer_wins}")
        
        result = play_single_game()
        
        if result == "menang":
            player_wins += 1
        elif result == "kalah":
            computer_wins += 1
        
        game_count += 1
    
    print("\n" + "="*50)
    print("           HASIL AKHIR BEST OF 3")
    print("="*50)
    print(f"Skor Akhir: Anda {player_wins} - Komputer {computer_wins}")
    
    if player_wins > computer_wins:
        print("🏆 SELAMAT! ANDA MEMENANGKAN BEST OF 3! 🏆")
    else:
        print("😔 KOMPUTER MEMENANGKAN BEST OF 3!")
    print("="*50)

def play_custom_rounds():
    """Mode bermain dengan jumlah round custom"""
    while True:
        try:
            rounds = int(input("\nBerapa banyak round yang ingin Anda mainkan? (1-10): "))
            if 1 <= rounds <= 10:
                break
            else:
                print("❌ Silakan masukkan angka antara 1-10")
        except ValueError:
            print("❌ Input tidak valid! Silakan masukkan angka")
    
    print("\n" + "="*50)
    print(f"           MODE {rounds} ROUND")
    print("="*50)
    
    player_wins = 0
    computer_wins = 0
    seri = 0
    
    for game_num in range(1, rounds + 1):
        print(f"\n🎮 GAME {game_num}/{rounds}")
        print(f"Skor: Menang={player_wins}, Kalah={computer_wins}, Seri={seri}")
        
        result = play_single_game()
        
        if result == "menang":
            player_wins += 1
        elif result == "kalah":
            computer_wins += 1
        else:
            seri += 1
    
    print("\n" + "="*50)
    print(f"           HASIL AKHIR {rounds} ROUND")
    print("="*50)
    print(f"Kemenangan Anda    : {player_wins}")
    print(f"Kekalahan Anda     : {computer_wins}")
    print(f"Seri              : {seri}")
    
    win_rate = (player_wins / rounds) * 100
    print(f"Win Rate          : {win_rate:.1f}%")
    print("="*50)

def show_menu():
    """Menampilkan menu pilihan mode permainan"""
    print("\n" + "="*50)
    print("           PILIH MODE PERMAINAN")
    print("="*50)
    print("1. Single Game (1 Putaran)")
    print("2. Best of 3 (3 Putaran)")
    print("3. Custom Rounds (1-10 Putaran)")
    print("4. Keluar")
    print("="*50)
    
    while True:
        choice = input("\nPilih mode (1/2/3/4): ").strip()
        if choice in ["1", "2", "3", "4"]:
            return choice
        print("❌ Pilihan tidak valid! Pilih 1, 2, 3, atau 4")

def main():
    """Fungsi utama program"""
    display_welcome()
    
    while True:
        mode = show_menu()
        
        if mode == "1":
            play_single_game()
        elif mode == "2":
            play_best_of_three()
        elif mode == "3":
            play_custom_rounds()
        elif mode == "4":
            print("\n👋 Terima kasih telah bermain! Sampai jumpa lagi!")
            break
        
        # Opsi untuk bermain ulang
        while True:
            play_again = input("\n\nApakah Anda ingin bermain lagi? (ya/tidak): ").lower().strip()
            if play_again in ["ya", "tidak", "y", "n"]:
                break
            print("❌ Silakan masukkan 'ya' atau 'tidak'")
        
        if play_again in ["tidak", "n"]:
            print("\n👋 Terima kasih telah bermain! Sampai jumpa lagi!")
            break

if __name__ == "__main__":
    main()
