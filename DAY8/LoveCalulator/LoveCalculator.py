def calculate_love_score(name1, name2):
    # Convert names to lowercase
    combined_names = (name1 + name2).lower()
    
    # Count letters for TRUE
    t = combined_names.count("t")
    r = combined_names.count("r")
    u = combined_names.count("u")
    e = combined_names.count("e")
    true_score = t + r + u + e
    
    # Count letters for LOVE
    l = combined_names.count("l")
    o = combined_names.count("o")
    v = combined_names.count("v")
    e2 = combined_names.count("e")
    love_score = l + o + v + e2
    
    # Combine into final love score
    final_score = int(str(true_score) + str(love_score))
    
    # ✅ Correct printing
    print(f"Love score of {name1} and {name2} is: {final_score}")


# Example test calls
calculate_love_score("Angela Yu", "Jack Bauer")       # Expected: 53
calculate_love_score("Kanye West", "Kim Kardashian")  # Expected: 42
