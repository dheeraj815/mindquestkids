import streamlit as st


def main():
    st.header("🥗 Healthy Eating")

    # Pro status
    if "is_pro" not in st.session_state:
        st.session_state.is_pro = False

    # Toggle pro (for demo purposes)
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.session_state.is_pro:
            st.success("👑 PRO User")
            if st.button("Logout Pro"):
                st.session_state.is_pro = False
                st.rerun()
        else:
            if st.button("🔓 Unlock Pro"):
                st.session_state.is_pro = True
                st.rerun()

    questions = [
        # FREE QUESTIONS (1-20)
        {"q": "Which vitamin do oranges provide?", "a": "Vitamin C", "hint": "Citrus fruit",
            "exp": "Oranges are rich in Vitamin C, which boosts immunity.", "free": True},
        {"q": "Which food is a good source of protein?", "a": "Eggs",
            "hint": "Comes from chickens", "exp": "Eggs provide high-quality protein.", "free": True},
        {"q": "Which food is rich in calcium?", "a": "Milk", "hint": "Drink for strong bones",
            "exp": "Milk contains calcium important for bones and teeth.", "free": True},
        {"q": "Which nutrient gives us energy?", "a": "Carbohydrates", "hint": "Rice, bread",
            "exp": "Carbohydrates provide energy for daily activities.", "free": True},
        {"q": "Which food is high in fiber?", "a": "Apple", "hint": "Keeps you full",
            "exp": "Apples are rich in fiber which aids digestion.", "free": True},
        {"q": "Which vitamin is important for eyesight?", "a": "Vitamin A", "hint": "Carrots help",
            "exp": "Vitamin A, found in carrots, helps maintain healthy eyes.", "free": True},
        {"q": "Which food is a healthy fat?", "a": "Avocado", "hint": "Green and creamy",
            "exp": "Avocados contain healthy monounsaturated fats.", "free": True},
        {"q": "Which drink is best for hydration?", "a": "Water",
            "hint": "Clear liquid", "exp": "Water keeps the body hydrated.", "free": True},
        {"q": "Which food helps build muscles?", "a": "Chicken", "hint": "High protein",
            "exp": "Chicken is a protein-rich food helping muscle growth.", "free": True},
        {"q": "Which fruit is yellow and sweet?", "a": "Banana", "hint": "Monkeys love it",
            "exp": "Bananas provide energy and nutrients.", "free": True},
        {"q": "Which food is rich in iron?", "a": "Spinach", "hint": "Green leafy vegetable",
            "exp": "Spinach contains iron which helps in blood formation.", "free": True},
        {"q": "Which food is good for strong bones?", "a": "Cheese", "hint": "Dairy product",
            "exp": "Cheese is rich in calcium for strong bones.", "free": True},
        {"q": "Which food is a whole grain?", "a": "Oats", "hint": "Breakfast cereal",
            "exp": "Oats are a healthy whole grain.", "free": True},
        {"q": "Which food is high in sugar?", "a": "Candy", "hint": "Sweet treat",
            "exp": "Candy contains high sugar which should be eaten in moderation.", "free": True},
        {"q": "Which vitamin helps prevent scurvy?", "a": "Vitamin C",
            "hint": "Found in citrus", "exp": "Vitamin C prevents scurvy.", "free": True},
        {"q": "Which food is a good source of omega-3?", "a": "Salmon", "hint": "Fish",
            "exp": "Salmon contains omega-3 fatty acids important for brain and heart health.", "free": True},
        {"q": "Which drink contains caffeine?", "a": "Tea", "hint": "Hot beverage",
            "exp": "Tea contains caffeine which can provide alertness.", "free": True},
        {"q": "Which food is a healthy snack?", "a": "Nuts", "hint": "Almonds, walnuts",
            "exp": "Nuts are nutritious and make a healthy snack.", "free": True},
        {"q": "Which vitamin helps with blood clotting?", "a": "Vitamin K", "hint": "Found in leafy greens",
            "exp": "Vitamin K is essential for blood clotting.", "free": True},
        {"q": "Which fruit is red and juicy?", "a": "Apple", "hint": "Keeps the doctor away",
            "exp": "Apples are red, juicy, and nutritious.", "free": True},

        # PRO QUESTIONS (21-50)
        {"q": "Which nutrient helps in growth?", "a": "Protein", "hint": "Meat, eggs",
            "exp": "Protein helps in growth and repair of the body.", "free": False},
        {"q": "Which food is rich in antioxidants?", "a": "Blueberries", "hint": "Small and blue",
            "exp": "Blueberries are rich in antioxidants which protect cells.", "free": False},
        {"q": "Which drink is best instead of soda?", "a": "Water", "hint": "No sugar",
            "exp": "Water is a healthier choice than sugary drinks.", "free": False},
        {"q": "Which food is high in vitamin D?", "a": "Egg yolk", "hint": "Inside eggs",
            "exp": "Egg yolks provide vitamin D important for bones.", "free": False},
        {"q": "Which food helps in digestion?", "a": "Yogurt", "hint": "Contains probiotics",
            "exp": "Yogurt contains probiotics which aid digestion.", "free": False},
        {"q": "Which food is good for strong teeth?", "a": "Cheese", "hint": "Dairy product",
            "exp": "Cheese provides calcium for healthy teeth.", "free": False},
        {"q": "Which food should be eaten in moderation?", "a": "Fried food", "hint": "Oily and crunchy",
            "exp": "Fried foods are high in fats and should be eaten in moderation.", "free": False},
        {"q": "Which fruit is rich in potassium?", "a": "Banana", "hint": "Yellow",
            "exp": "Bananas are rich in potassium which helps muscles and nerves.", "free": False},
        {"q": "Which food is gluten-free?", "a": "Rice", "hint": "Staple food",
            "exp": "Rice does not contain gluten.", "free": False},
        {"q": "Which vitamin helps in wound healing?", "a": "Vitamin C",
            "hint": "Found in citrus fruits", "exp": "Vitamin C aids in healing wounds.", "free": False},
        {"q": "Which food is a source of complex carbs?", "a": "Brown rice", "hint": "Healthy grain",
            "exp": "Brown rice provides complex carbohydrates for energy.", "free": False},
        {"q": "Which food is high in saturated fat?", "a": "Butter", "hint": "Used in cooking",
            "exp": "Butter contains saturated fat which should be eaten in moderation.", "free": False},
        {"q": "Which food contains probiotics?", "a": "Yogurt", "hint": "Dairy product",
            "exp": "Yogurt contains live beneficial bacteria.", "free": False},
        {"q": "Which food is rich in fiber?", "a": "Lentils", "hint": "Legume",
            "exp": "Lentils are high in fiber which supports digestion.", "free": False},
        {"q": "Which fruit is tropical and sweet?", "a": "Mango", "hint": "King of fruits",
            "exp": "Mangoes are tropical fruits rich in vitamins.", "free": False},
        {"q": "Which food is a healthy breakfast option?", "a": "Oats", "hint": "Cooked with milk or water",
            "exp": "Oats provide energy and fiber for breakfast.", "free": False},
        {"q": "Which food is a source of vitamin B12?", "a": "Fish", "hint": "Seafood",
            "exp": "Fish contains vitamin B12 important for blood and nerves.", "free": False},
        {"q": "Which food is high in sugar?", "a": "Chocolate", "hint": "Sweet treat",
            "exp": "Chocolate contains sugar which should be eaten in moderation.", "free": False},
        {"q": "Which food is rich in iron?", "a": "Red meat", "hint": "Beef",
            "exp": "Red meat provides iron which helps make red blood cells.", "free": False},
        {"q": "Which drink is best for breakfast?", "a": "Milk", "hint": "White liquid",
            "exp": "Milk provides calcium and protein, ideal for breakfast.", "free": False},
        {"q": "Which food helps lower cholesterol?", "a": "Oats", "hint": "Soluble fiber",
            "exp": "Oats contain soluble fiber that helps lower cholesterol.", "free": False},
        {"q": "Which vegetable is rich in vitamin C?", "a": "Bell pepper",
            "hint": "Colorful", "exp": "Bell peppers are rich in vitamin C.", "free": False},
        {"q": "Which food is a complete protein?", "a": "Quinoa", "hint": "Ancient grain",
            "exp": "Quinoa contains all essential amino acids.", "free": False},
        {"q": "Which mineral helps prevent anemia?", "a": "Iron", "hint": "In red meat",
            "exp": "Iron prevents anemia by helping make red blood cells.", "free": False},
        {"q": "Which food is fermented and healthy?", "a": "Kimchi", "hint": "Korean food",
            "exp": "Kimchi is fermented and contains beneficial probiotics.", "free": False},
        {"q": "Which nut is highest in protein?", "a": "Peanut", "hint": "Used in butter",
            "exp": "Peanuts are high in protein among nuts.", "free": False},
        {"q": "Which food supports brain health?", "a": "Walnuts", "hint": "Brain-shaped",
            "exp": "Walnuts contain omega-3s that support brain function.", "free": False},
        {"q": "Which vitamin is called sunshine vitamin?", "a": "Vitamin D", "hint": "From sunlight",
            "exp": "Vitamin D is produced when skin is exposed to sunlight.", "free": False},
        {"q": "Which food is alkaline-forming?", "a": "Lemon", "hint": "Citrus fruit",
            "exp": "Despite being acidic, lemons have an alkaline effect in the body.", "free": False},
        {"q": "Which food is prebiotic?", "a": "Garlic", "hint": "Strong flavor",
            "exp": "Garlic contains prebiotics that feed good gut bacteria.", "free": False}
    ]

    if "answers" not in st.session_state:
        st.session_state.answers = {}
    if "scores" not in st.session_state:
        st.session_state.scores = {}

    for i, q in enumerate(questions):
        # Check if question is locked
        is_locked = not q["free"] and not st.session_state.is_pro

        if is_locked:
            st.subheader(f"Q{i+1}. 🔒 Pro Question")
            st.warning("⭐ Upgrade to Pro to unlock this question!")
        else:
            st.subheader(f"Q{i+1}. {q['q']}")
            st.caption(f"💡 Hint: {q['hint']}")
            st.session_state.answers[i] = st.text_input(
                "Your answer",
                key=f"healthy_eating_{i}",
                disabled=is_locked
            )

    if st.button("✅ Submit"):
        score = 0
        available_questions = [i for i, q in enumerate(
            questions) if q["free"] or st.session_state.is_pro]

        for i in available_questions:
            q = questions[i]
            if st.session_state.answers.get(i, "").strip().lower() == q["a"].lower():
                score += 1

        total_available = len(available_questions)
        st.session_state.scores["Healthy Eating"] = f"{score}/{total_available}"
        st.success(f"Score: {score}/{total_available}")

        for i in available_questions:
            q = questions[i]
            user_answer = st.session_state.answers.get(i, "").strip()
            is_correct = user_answer.lower() == q["a"].lower()

            if is_correct:
                st.success(f"Q{i+1} ✓ Correct! {q['exp']}")
            else:
                st.error(
                    f"Q{i+1} ✗ Wrong! Correct answer: {q['a']}. {q['exp']}")

    if st.button("🔄 Restart"):
        st.session_state.answers = {}
        st.rerun()

    # Show stats
    st.divider()
    if st.session_state.is_pro:
        st.info("📊 You have access to all 50 questions!")
    else:
        st.info(
            "📊 Free: 20/50 questions available. Upgrade to Pro for 30 more questions!")


if __name__ == "__main__":
    main()
