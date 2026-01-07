import streamlit as st


def main():
    st.header("📝 Daily Quiz")

    # Pro status
    if "is_pro" not in st.session_state:
        st.session_state.is_pro = False

    # Initialize answers and scores
    if "answers" not in st.session_state:
        st.session_state.answers = {}
    if "scores" not in st.session_state:
        st.session_state.scores = {}

    # Toggle pro status with better visibility
    col1, col2, col3 = st.columns([2, 1, 1])

    with col2:
        if st.session_state.is_pro:
            st.success("👑 PRO Member")
        else:
            st.info("🎁 FREE User")

    with col3:
        if st.session_state.is_pro:
            if st.button("⬇️ Downgrade", use_container_width=True):
                st.session_state.is_pro = False
                st.rerun()
        else:
            if st.button("⬆️ Upgrade Pro", use_container_width=True):
                st.session_state.is_pro = True
                st.balloons()
                st.rerun()

    questions = [
        # FREE QUESTIONS (1-20)
        {"q": "What is 5 + 3?", "a": "8", "hint": "Basic addition",
            "exp": "5 + 3 = 8.", "free": True},
        {"q": "What is the capital of France?", "a": "Paris", "hint": "City of lights",
            "exp": "The capital of France is Paris.", "free": True},
        {"q": "What color do you get by mixing red and yellow?", "a": "Orange",
            "hint": "Warm color", "exp": "Red + Yellow = Orange.", "free": True},
        {"q": "What is 12 ÷ 4?", "a": "3", "hint": "Division",
            "exp": "12 ÷ 4 = 3.", "free": True},
        {"q": "Which animal is known as the King of the Jungle?", "a": "Lion",
            "hint": "Roars", "exp": "The lion is called King of the Jungle.", "free": True},
        {"q": "What planet do we live on?", "a": "Earth", "hint": "Blue planet",
            "exp": "Humans live on planet Earth.", "free": True},
        {"q": "What is the opposite of hot?", "a": "Cold", "hint": "Temperature",
            "exp": "The opposite of hot is cold.", "free": True},
        {"q": "How many days are there in a week?", "a": "7", "hint": "A full week",
            "exp": "There are 7 days in a week.", "free": True},
        {"q": "Which fruit is yellow and long?", "a": "Banana",
            "hint": "Monkeys love it", "exp": "Bananas are yellow and long.", "free": True},
        {"q": "What is 7 - 4?", "a": "3", "hint": "Subtraction",
            "exp": "7 - 4 = 3.", "free": True},
        {"q": "Which gas do we breathe in to live?", "a": "Oxygen",
            "hint": "Essential for life", "exp": "Humans need oxygen to survive.", "free": True},
        {"q": "Which shape has 4 equal sides?", "a": "Square", "hint": "Geometric shape",
            "exp": "A square has four equal sides.", "free": True},
        {"q": "What do bees make?", "a": "Honey", "hint": "Sweet",
            "exp": "Bees produce honey.", "free": True},
        {"q": "What is the color of the sky on a clear day?", "a": "Blue",
            "hint": "Look up", "exp": "The sky appears blue on a clear day.", "free": True},
        {"q": "Which animal has a trunk?", "a": "Elephant", "hint": "Big ears too",
            "exp": "Elephants have a trunk and large ears.", "free": True},
        {"q": "What is 9 x 2?", "a": "18", "hint": "Multiplication",
            "exp": "9 x 2 = 18.", "free": True},
        {"q": "Which animal says 'Meow'?", "a": "Cat",
            "hint": "Loves milk", "exp": "Cats say 'Meow'.", "free": True},
        {"q": "What is 15 ÷ 5?", "a": "3", "hint": "Division",
            "exp": "15 ÷ 5 = 3.", "free": True},
        {"q": "Which vegetable is orange and crunchy?", "a": "Carrot",
            "hint": "Rabbits love it", "exp": "Carrots are orange and crunchy.", "free": True},
        {"q": "What is the opposite of day?", "a": "Night", "hint": "When sun goes down",
            "exp": "The opposite of day is night.", "free": True},

        # PRO QUESTIONS (21-50)
        {"q": "Which planet is called the Red Planet?", "a": "Mars",
            "hint": "Reddish color", "exp": "Mars is known as the Red Planet.", "free": False},
        {"q": "What is 6 + 7?", "a": "13", "hint": "Addition",
            "exp": "6 + 7 = 13.", "free": False},
        {"q": "Which animal hops and croaks?", "a": "Frog",
            "hint": "Lives near water", "exp": "Frogs hop and croak.", "free": False},
        {"q": "Which fruit is red and round?", "a": "Apple", "hint": "Keeps doctor away",
            "exp": "Apples are red and round.", "free": False},
        {"q": "What is 10 - 6?", "a": "4", "hint": "Subtraction",
            "exp": "10 - 6 = 4.", "free": False},
        {"q": "Which bird can talk?", "a": "Parrot", "hint": "Colorful feathers",
            "exp": "Parrots can mimic human speech.", "free": False},
        {"q": "What is 8 x 3?", "a": "24", "hint": "Multiplication",
            "exp": "8 x 3 = 24.", "free": False},
        {"q": "Which animal is known for building dams?", "a": "Beaver",
            "hint": "Lives near water", "exp": "Beavers build dams to make ponds.", "free": False},
        {"q": "Which gas do humans exhale?", "a": "Carbon dioxide", "hint": "Opposite of oxygen",
            "exp": "Humans breathe out carbon dioxide.", "free": False},
        {"q": "What is 20 ÷ 4?", "a": "5", "hint": "Division",
            "exp": "20 ÷ 4 = 5.", "free": False},
        {"q": "Which planet is closest to the Sun?", "a": "Mercury", "hint": "Small and fast",
            "exp": "Mercury is the nearest planet to the Sun.", "free": False},
        {"q": "Which animal has stripes and lives in Africa?", "a": "Zebra",
            "hint": "Looks like a horse", "exp": "Zebras have black and white stripes.", "free": False},
        {"q": "What is 11 + 9?", "a": "20", "hint": "Addition",
            "exp": "11 + 9 = 20.", "free": False},
        {"q": "Which animal says 'Woof'?", "a": "Dog",
            "hint": "Man's best friend", "exp": "Dogs bark 'Woof'.", "free": False},
        {"q": "Which fruit is green outside and red inside?", "a": "Watermelon",
            "hint": "Summer fruit", "exp": "Watermelons have green skin and red flesh.", "free": False},
        {"q": "What is 14 - 7?", "a": "7", "hint": "Subtraction",
            "exp": "14 - 7 = 7.", "free": False},
        {"q": "Which animal is known for changing colors?", "a": "Chameleon", "hint": "Camouflage",
            "exp": "Chameleons change colors to blend with surroundings.", "free": False},
        {"q": "Which shape has three sides?", "a": "Triangle", "hint": "Geometric shape",
            "exp": "A triangle has three sides.", "free": False},
        {"q": "Which planet is known as the Blue Planet?", "a": "Earth", "hint": "We live here",
            "exp": "Earth is called the Blue Planet because of its oceans.", "free": False},
        {"q": "Which animal is the fastest land animal?", "a": "Cheetah", "hint": "Spotted",
            "exp": "Cheetahs are the fastest land animals.", "free": False},
        {"q": "What is 7 x 7?", "a": "49", "hint": "Multiplication",
            "exp": "7 x 7 = 49.", "free": False},
        {"q": "Which bird lays the largest eggs?", "a": "Ostrich", "hint": "Cannot fly",
            "exp": "Ostriches lay the largest eggs among birds.", "free": False},
        {"q": "What is 16 + 8?", "a": "24", "hint": "Addition",
            "exp": "16 + 8 = 24.", "free": False},
        {"q": "Which animal lives in the Arctic?", "a": "Polar bear", "hint": "White fur",
            "exp": "Polar bears live in Arctic regions.", "free": False},
        {"q": "What is 25 - 10?", "a": "15", "hint": "Subtraction",
            "exp": "25 - 10 = 15.", "free": False},
        {"q": "Which insect makes silk?", "a": "Silkworm", "hint": "Caterpillar",
            "exp": "Silkworms produce silk threads.", "free": False},
        {"q": "What is 6 x 6?", "a": "36", "hint": "Multiplication",
            "exp": "6 x 6 = 36.", "free": False},
        {"q": "Which animal has eight legs?", "a": "Spider", "hint": "Spins webs",
            "exp": "Spiders are arachnids with eight legs.", "free": False},
        {"q": "What is 30 ÷ 6?", "a": "5", "hint": "Division",
            "exp": "30 ÷ 6 = 5.", "free": False},
        {"q": "Which metal is liquid at room temperature?", "a": "Mercury", "hint": "Used in thermometers",
            "exp": "Mercury is the only metal that's liquid at room temperature.", "free": False}
    ]

    # Show quiz info
    st.markdown("---")
    free_count = sum(1 for q in questions if q["free"])
    pro_count = sum(1 for q in questions if not q["free"])

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📚 Total Questions", len(questions))
    with col2:
        st.metric("🎁 FREE Questions", free_count)
    with col3:
        st.metric("👑 PRO Questions", pro_count)

    st.markdown("---")

    # Display questions
    for i, q in enumerate(questions):
        # Check if question is locked
        is_locked = not q["free"] and not st.session_state.is_pro

        if is_locked:
            # Show locked question
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%); 
                        padding: 20px; border-radius: 15px; margin: 15px 0;
                        border-left: 6px solid #FF6B6B;">
                <h3 style="color: #000; margin: 0;">Q{i+1}. 🔒 PRO Question Locked</h3>
                <p style="color: #000; margin-top: 10px; font-size: 16px;">
                    ⭐ Upgrade to PRO to unlock this question and 29 more!
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Show unlocked question
            if q["free"]:
                badge = "🎁 FREE"
                color = "#4CAF50"
            else:
                badge = "👑 PRO"
                color = "#FFD700"

            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #ffffff 0%, #f8f9ff 100%);
                        padding: 20px; border-radius: 15px; margin: 15px 0;
                        border-left: 6px solid {color};
                        box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h3 style="color: #667eea; margin: 0;">Q{i+1}. {q['q']}</h3>
                    <span style="background: {color}; color: {'#000' if not q['free'] else '#fff'}; 
                                 padding: 5px 15px; border-radius: 20px; font-weight: 700;
                                 font-size: 12px;">{badge}</span>
                </div>
                <p style="color: #888; margin-top: 10px;">💡 Hint: {q['hint']}</p>
            </div>
            """, unsafe_allow_html=True)

            st.session_state.answers[i] = st.text_input(
                "Your answer",
                key=f"daily_quiz_{i}",
                placeholder="Type your answer here...",
                label_visibility="collapsed"
            )

    # Submit button
    st.markdown("---")
    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("✅ Submit Quiz", use_container_width=True):
            score = 0
            available_questions = [i for i, q in enumerate(
                questions) if q["free"] or st.session_state.is_pro]

            for i in available_questions:
                q = questions[i]
                user_answer = st.session_state.answers.get(i, "").strip()
                if user_answer.lower() == q["a"].lower():
                    score += 1

            total_available = len(available_questions)
            st.session_state.scores["Daily Quiz"] = f"{score}/{total_available}"

            # Show overall score
            percentage = int((score / total_available) * 100)

            if percentage >= 80:
                st.success(
                    f"🎉 Excellent! Score: {score}/{total_available} ({percentage}%)")
                st.balloons()
            elif percentage >= 60:
                st.info(
                    f"👍 Good job! Score: {score}/{total_available} ({percentage}%)")
            else:
                st.warning(
                    f"💪 Keep practicing! Score: {score}/{total_available} ({percentage}%)")

            # Show detailed results
            st.markdown("---")
            st.subheader("📊 Detailed Results")

            for i in available_questions:
                q = questions[i]
                user_answer = st.session_state.answers.get(i, "").strip()
                is_correct = user_answer.lower() == q["a"].lower()

                if is_correct:
                    st.success(f"✓ Q{i+1}: Correct! {q['exp']}")
                else:
                    st.error(
                        f"✗ Q{i+1}: Wrong! Correct answer: **{q['a']}**. {q['exp']}")

    with col2:
        if st.button("🔄 Restart Quiz", use_container_width=True):
            st.session_state.answers = {}
            st.success("Quiz restarted! Answer the questions again.")
            st.rerun()

    # Show stats at bottom
    st.markdown("---")
    if st.session_state.is_pro:
        st.success(
            "📊 You have access to all 50 questions! Enjoy the full quiz experience! 🎉")
    else:
        st.info(
            f"📊 FREE Plan: {free_count}/{len(questions)} questions available. Upgrade to PRO for {pro_count} more questions!")

        # Upgrade prompt
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
                    padding: 25px; border-radius: 15px; margin-top: 20px;
                    text-align: center; color: #000;">
            <h3 style="margin: 0 0 10px 0;">👑 Upgrade to PRO Today!</h3>
            <p style="font-size: 16px; margin: 0;">
                Get access to all 50 questions + exclusive features!<br>
                Click "Upgrade Pro" button above to unlock everything! ⬆️
            </p>
        </div>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
