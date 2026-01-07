import streamlit as st


def main():
    st.header("🐾 Animal Sound Explorer")

    # Show account type
    if st.session_state.is_pro:
        st.success("👑 PRO Member - All 50 questions unlocked!")
    else:
        st.info("🎁 FREE Plan - 20 questions available. Upgrade to PRO for 30 more!")

    # ALL 50 QUESTIONS
    all_questions = [
        # FREE QUESTIONS (1-20)
        {"q": "Which animal says 'Moo'?", "a": "Cow", "hint": "Gives milk",
            "exp": "Cows make a 'Moo' sound.", "tier": "free"},
        {"q": "Which animal says 'Meow'?", "a": "Cat", "hint": "Likes milk",
            "exp": "Cats make a 'Meow' sound.", "tier": "free"},
        {"q": "Which animal says 'Woof'?", "a": "Dog",
            "hint": "Man's best friend", "exp": "Dogs bark 'Woof'.", "tier": "free"},
        {"q": "Which animal says 'Neigh'?", "a": "Horse", "hint": "Runs fast",
            "exp": "Horses neigh to communicate.", "tier": "free"},
        {"q": "Which animal says 'Oink'?", "a": "Pig", "hint": "Pink and muddy",
            "exp": "Pigs make an 'Oink' sound.", "tier": "free"},
        {"q": "Which animal says 'Quack'?", "a": "Duck",
            "hint": "Swims on water", "exp": "Ducks say 'Quack'.", "tier": "free"},
        {"q": "Which animal says 'Baa'?", "a": "Sheep", "hint": "Gives wool",
            "exp": "Sheep make a 'Baa' sound.", "tier": "free"},
        {"q": "Which animal says 'Roar'?", "a": "Lion", "hint": "King of jungle",
            "exp": "Lions roar loudly to mark territory.", "tier": "free"},
        {"q": "Which animal says 'Hiss'?", "a": "Snake", "hint": "Slithers",
            "exp": "Snakes hiss as a warning.", "tier": "free"},
        {"q": "Which animal says 'Coo'?", "a": "Pigeon", "hint": "Urban bird",
            "exp": "Pigeons make a soft 'Coo' sound.", "tier": "free"},
        {"q": "Which animal says 'Chirp'?", "a": "Bird", "hint": "Flies in sky",
            "exp": "Small birds chirp to communicate.", "tier": "free"},
        {"q": "Which animal says 'Buzz'?", "a": "Bee", "hint": "Makes honey",
            "exp": "Bees buzz when flying.", "tier": "free"},
        {"q": "Which animal says 'Croak'?", "a": "Frog", "hint": "Lives in water",
            "exp": "Frogs croak to attract mates.", "tier": "free"},
        {"q": "Which animal says 'Trumpet'?", "a": "Elephant", "hint": "Has a trunk",
            "exp": "Elephants trumpet to communicate.", "tier": "free"},
        {"q": "Which animal says 'Howl'?", "a": "Wolf", "hint": "Lives in packs",
            "exp": "Wolves howl to communicate with pack.", "tier": "free"},
        {"q": "Which animal says 'Cluck'?", "a": "Hen", "hint": "Lays eggs",
            "exp": "Hens cluck as part of communication.", "tier": "free"},
        {"q": "Which animal says 'Squeak'?", "a": "Mouse", "hint": "Small rodent",
            "exp": "Mice make a squeaking sound.", "tier": "free"},
        {"q": "Which animal says 'Growl'?", "a": "Bear", "hint": "Hibernates",
            "exp": "Bears growl when threatened.", "tier": "free"},
        {"q": "Which animal says 'Snort'?", "a": "Pig", "hint": "Oinks too",
            "exp": "Pigs snort and oink.", "tier": "free"},
        {"q": "Which animal says 'Whinny'?", "a": "Horse", "hint": "Neighs too",
            "exp": "Horses whinny when excited.", "tier": "free"},

        # PRO QUESTIONS (21-50)
        {"q": "Which animal says 'Screech'?", "a": "Owl", "hint": "Nocturnal bird",
            "exp": "Owls screech during night.", "tier": "pro"},
        {"q": "Which animal says 'Gurgle'?", "a": "Turkey", "hint": "Thanksgiving bird",
            "exp": "Turkeys gurgle to communicate.", "tier": "pro"},
        {"q": "Which animal says 'Honk'?", "a": "Goose", "hint": "Migrates in V",
            "exp": "Geese honk during flight.", "tier": "pro"},
        {"q": "Which animal says 'Bleat'?", "a": "Goat", "hint": "Eats grass",
            "exp": "Goats bleat to communicate.", "tier": "pro"},
        {"q": "Which animal says 'Yelp'?", "a": "Dog", "hint": "High pitched",
            "exp": "Dogs yelp when hurt or scared.", "tier": "pro"},
        {"q": "Which animal says 'Ribbit'?", "a": "Frog", "hint": "Jumps",
            "exp": "Frogs ribbit near water.", "tier": "pro"},
        {"q": "Which animal says 'Snarl'?", "a": "Dog", "hint": "Warning sound",
            "exp": "Dogs snarl to warn others.", "tier": "pro"},
        {"q": "Which animal says 'Chatter'?", "a": "Monkey", "hint": "Lives in trees",
            "exp": "Monkeys chatter in groups.", "tier": "pro"},
        {"q": "Which animal says 'Hoot'?", "a": "Owl", "hint": "Nocturnal",
            "exp": "Owls hoot to mark territory.", "tier": "pro"},
        {"q": "Which animal says 'Screech'?", "a": "Parrot", "hint": "Can mimic",
            "exp": "Parrots can screech loudly.", "tier": "pro"},
        {"q": "Which animal says 'Grunt'?", "a": "Pig", "hint": "Snorts too",
            "exp": "Pigs grunt to communicate.", "tier": "pro"},
        {"q": "Which animal says 'Caw'?", "a": "Crow", "hint": "Black bird",
            "exp": "Crows caw to communicate.", "tier": "pro"},
        {"q": "Which animal says 'Chirp'?", "a": "Cricket", "hint": "Insect",
            "exp": "Crickets chirp at night.", "tier": "pro"},
        {"q": "Which animal says 'Bark'?", "a": "Dog", "hint": "Woof too",
            "exp": "Dogs bark to alert.", "tier": "pro"},
        {"q": "Which animal says 'Purr'?", "a": "Cat", "hint": "Happy sound",
            "exp": "Cats purr when content.", "tier": "pro"},
        {"q": "Which animal says 'Bellow'?", "a": "Bull", "hint": "Loud roar",
            "exp": "Bulls bellow when angry.", "tier": "pro"},
        {"q": "Which animal says 'Whistle'?", "a": "Dolphin", "hint": "Marine mammal",
            "exp": "Dolphins whistle underwater.", "tier": "pro"},
        {"q": "Which animal says 'Squawk'?", "a": "Parrot", "hint": "Loud bird",
            "exp": "Parrots squawk to communicate.", "tier": "pro"},
        {"q": "Which animal says 'Cackle'?", "a": "Hyena", "hint": "Laughs",
            "exp": "Hyenas cackle or laugh.", "tier": "pro"},
        {"q": "Which animal says 'Gobble'?", "a": "Turkey",
            "hint": "Male turkey", "exp": "Male turkeys gobble.", "tier": "pro"},
        {"q": "Which animal says 'Wail'?", "a": "Whale", "hint": "Ocean giant",
            "exp": "Whales wail underwater.", "tier": "pro"},
        {"q": "Which animal says 'Whimper'?", "a": "Dog", "hint": "Sad sound",
            "exp": "Dogs whimper when sad.", "tier": "pro"},
        {"q": "Which animal says 'Trill'?", "a": "Canary", "hint": "Singing bird",
            "exp": "Canaries trill beautifully.", "tier": "pro"},
        {"q": "Which animal says 'Cackle'?", "a": "Chicken", "hint": "After laying egg",
            "exp": "Chickens cackle after laying.", "tier": "pro"},
        {"q": "Which animal says 'Yap'?", "a": "Dog", "hint": "Small dog",
            "exp": "Small dogs yap frequently.", "tier": "pro"},
        {"q": "Which animal says 'Bugle'?", "a": "Elk", "hint": "Deer family",
            "exp": "Elk bugle during mating.", "tier": "pro"},
        {"q": "Which animal says 'Sing'?", "a": "Nightingale", "hint": "Beautiful song",
            "exp": "Nightingales sing melodiously.", "tier": "pro"},
        {"q": "Which animal says 'Click'?", "a": "Dolphin", "hint": "Echolocation",
            "exp": "Dolphins click for navigation.", "tier": "pro"},
        {"q": "Which animal says 'Warble'?", "a": "Songbird", "hint": "Musical sound",
            "exp": "Songbirds warble in trees.", "tier": "pro"},
        {"q": "Which animal says 'Yowl'?", "a": "Cat", "hint": "Fighting sound",
            "exp": "Cats yowl when fighting.", "tier": "pro"},
    ]

    # Filter questions based on membership
    if st.session_state.is_pro:
        questions = all_questions  # All 50 questions
    else:
        questions = [q for q in all_questions if q["tier"]
                     == "free"]  # Only 20 free

    # Initialize session state
    if "answers" not in st.session_state:
        st.session_state.answers = {}
    if "scores" not in st.session_state:
        st.session_state.scores = {}

    # Display questions
    for i, q in enumerate(questions):
        st.subheader(f"Q{i+1}. {q['q']}")
        st.caption(f"💡 Hint: {q['hint']}")
        st.session_state.answers[i] = st.text_input(
            "Your answer",
            key=f"animal_sound_{i}",
            placeholder="Type your answer here..."
        )

    # PRO Upgrade prompt for free users
    if not st.session_state.is_pro:
        st.markdown("---")
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%); 
                    padding: 30px; border-radius: 20px; text-align: center; 
                    box-shadow: 0 10px 40px rgba(255,215,0,0.3);">
            <h2 style="color: #000; margin-bottom: 15px;">🔒 30 More Questions Locked!</h2>
            <p style="color: #000; font-size: 18px; font-weight: 600; margin-bottom: 20px;">
                Unlock all 50 questions and boost your learning!
            </p>
            <a href="?page=👑 Upgrade to PRO" style="background: #000; color: #FFD700; 
               padding: 15px 40px; border-radius: 30px; text-decoration: none; 
               font-weight: 700; font-size: 18px; display: inline-block;">
                👑 UPGRADE TO PRO NOW
            </a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Submit button
    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button("✅ SUBMIT ANSWERS", use_container_width=True):
            score = 0
            for i, q in enumerate(questions):
                if st.session_state.answers.get(i, "").strip().lower() == q["a"].lower():
                    score += 1

            st.session_state.scores["Animal Sound Explorer"] = f"{score}/{len(questions)}"

            # Show results
            percentage = (score / len(questions)) * 100
            st.success(
                f"🎉 Your Score: {score}/{len(questions)} ({percentage:.0f}%)")

            if percentage == 100:
                st.balloons()
                st.success("🌟 PERFECT SCORE! You're an Animal Expert!")
            elif percentage >= 80:
                st.success("🎯 Excellent! Keep up the great work!")
            elif percentage >= 60:
                st.info("💪 Good job! Practice makes perfect!")
            else:
                st.info("📚 Keep learning! You're getting better!")

            # Show explanations
            st.markdown("---")
            st.markdown("### 📖 Answer Explanations")
            for i, q in enumerate(questions):
                user_answer = st.session_state.answers.get(i, "").strip()
                is_correct = user_answer.lower() == q["a"].lower()

                if is_correct:
                    st.success(f"Q{i+1}. ✅ Correct! {q['exp']}")
                else:
                    st.error(
                        f"Q{i+1}. ❌ Wrong. Correct answer: **{q['a']}**. {q['exp']}")

    with col2:
        if st.button("🔄 RESTART", use_container_width=True):
            st.session_state.answers = {}
            st.rerun()
