# Initial Player Info
ign = input("In-game name (IGN): ")
rank = input("Current rank: ")

# Hero Roster (Parallel Lists)
hero_names = ["Layla", "Tigreal", "Gusion", "Kagura", "Chou"]
hero_roles = ["Marksman", "Tank", "Assassin", "Mage", "Fighter"]

# Display Roster
print("\n==============================================")
print("   MOBILE LEGENDS -- HERO ROSTER")
print("==============================================")
for i in range(len(hero_names)):
    print(f" {i + 1}. {hero_names[i]:<11} [{hero_roles[i]}]")
print("==============================================\n")

# Parallel lists to store logged match data
logged_heroes = []
logged_kdas = []
logged_results = []
logged_tags = []

total_wins = 0
total_losses = 0

# Match Entry Loop
for match_num in range(1, 5):
    print(f"--- MATCH {match_num} ---")
    hero_choice = int(input("Hero number (0 to skip): "))
    
    if hero_choice == 0:
        print()
        continue
    
    # Identify the chosen hero using basic indexing (subtract 1 because lists are 0-indexed)
    chosen_hero = hero_names[hero_choice - 1]
    
    kills = int(input("Kills: "))
    deaths = int(input("Deaths: "))
    assists = int(input("Assists: "))
    result = input("Result (W/L): ")
    
    # Prevent Division by Zero
    if deaths == 0:
        denominator = 1
    else:
        denominator = deaths
        
    # Calculate KDA
    kda = (kills + assists) / denominator
    
    # Determine the tag
    result_upper = result.upper()
    if kda >= 5 and result_upper == 'W':
        tag = "DOMINATION!"
    elif kda >= 5 and result_upper == 'L':
        tag = "Carried Hard"
    elif kda < 5 and result_upper == 'W':
        tag = "Team Effort"
    else:
        tag = "Better Luck Next Game"
        
    # Track Win/Loss counts
    if result_upper == 'W':
        total_wins += 1
        result_str = "WIN"
    else:
        total_losses += 1
        result_str = "LOSS"
        
    # Save the match data to our parallel lists
    logged_heroes.append(chosen_hero)
    logged_kdas.append(kda)
    logged_results.append(result_str)
    logged_tags.append(tag)
    
    print()

# Generate the Match Log
print("=================================================")
print(f"     {ign} -- MATCH LOG ({rank})")
print("=================================================")

matches_played = len(logged_heroes)

if matches_played > 0:
    best_match_idx = 0
    highest_kda = -1.0
    
    # Loop through logged data to display matches and find the best KDA
    for i in range(matches_played):
        
        # Format the hero display string first for clean padding
        hero_display = f"[{i + 1}] {logged_heroes[i]}"
        kda_display = f"KDA: {logged_kdas[i]:.2f}"
        
        # Print the individual match row
        print(f"{hero_display:<15} | {kda_display:<10} | {logged_results[i]:<4} | {logged_tags[i]}")
        
        # Check if this is the best match
        if logged_kdas[i] > highest_kda:
            highest_kda = logged_kdas[i]
            best_match_idx = i
            
    print("-------------------------------------------------")
    print(f"Matches Played : {matches_played}")
    print(f"Wins : {total_wins}  |  Losses : {total_losses}")
    
    # Calculate and display whole-number win rate
    win_rate = int((total_wins / matches_played) * 100)
    print(f"Win Rate       : {win_rate}%")
    
    # Display the best match
    best_hero = f"[{best_match_idx + 1}] {logged_heroes[best_match_idx]}"
    print(f"Best Match     : {best_hero}  (KDA: {highest_kda:.2f})")

else:
    print("No matches were played.")

print("=================================================")