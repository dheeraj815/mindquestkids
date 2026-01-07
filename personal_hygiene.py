import streamlit as st


def main():
    st.header("🧼 Personal Hygiene")

    questions = [
        {"q": "Why should we wash hands before eating?", "a": "To remove germs",
            "hint": "Clean hands", "exp": "Washing hands removes germs and prevents sickness."},
        {"q": "How often should we brush our teeth?", "a": "Twice a day",
            "hint": "Morning and night", "exp": "Brushing teeth twice a day keeps them healthy."},
        {"q": "Why should we take a bath regularly?", "a": "To stay clean",
            "hint": "Body hygiene", "exp": "Bathing removes dirt and bacteria from our body."},
        {"q": "Why is it important to trim nails?", "a": "To prevent germs",
            "hint": "Fingers and toes", "exp": "Trimmed nails reduce dirt and bacteria."},
        {"q": "What should we use to clean teeth?", "a": "Toothbrush",
            "hint": "Dental tool", "exp": "A toothbrush helps clean teeth effectively."},
        {"q": "Why should we cover mouth while sneezing?", "a": "To prevent spreading germs",
            "hint": "Use hand or tissue", "exp": "Covering mouth prevents germs from spreading."},
        {"q": "Why should we wash fruits before eating?", "a": "To remove dirt and germs",
            "hint": "Clean food", "exp": "Washing fruits removes dirt, chemicals, and germs."},
        {"q": "Why is it important to wear clean clothes?", "a": "To stay healthy",
            "hint": "Fresh clothes", "exp": "Clean clothes prevent infections and skin problems."},
        {"q": "Why should we comb our hair?", "a": "To remove tangles and dirt",
            "hint": "Hair care", "exp": "Combing keeps hair neat and removes dust."},
        {"q": "Why should we not share towels?", "a": "To avoid germs",
            "hint": "Personal item", "exp": "Sharing towels spreads germs and infections."},
        {"q": "Why is it important to wash hands after using toilet?", "a": "To remove germs",
            "hint": "Hygiene habit", "exp": "Hand washing after toilet prevents disease."},
        {"q": "Why should we change underwear daily?", "a": "To stay clean",
            "hint": "Hygiene", "exp": "Daily change prevents infections and odor."},
        {"q": "Why should we keep nails clean?", "a": "To avoid germs",
            "hint": "Fingers and toes", "exp": "Clean nails prevent dirt and germs accumulation."},
        {"q": "Why should we cover mouth while coughing?", "a": "To prevent spreading germs",
            "hint": "Use tissue or elbow", "exp": "Covering mouth avoids spreading infections."},
        {"q": "Why should we wash hands after playing outside?", "a": "To remove dirt and germs",
            "hint": "Outdoor dirt", "exp": "Washing hands removes germs picked up outside."},
        {"q": "Why should we keep shoes clean?", "a": "To prevent dirt",
            "hint": "Footwear", "exp": "Clean shoes prevent dust and germs at home."},
        {"q": "Why should we not bite nails?", "a": "To avoid germs",
            "hint": "Bad habit", "exp": "Biting nails can transfer germs to mouth."},
        {"q": "Why should we cover wounds?", "a": "To prevent infection",
            "hint": "Use bandage", "exp": "Covering wounds keeps them safe from germs."},
        {"q": "Why is it important to wash hair regularly?", "a": "To keep scalp clean",
            "hint": "Prevent lice", "exp": "Clean hair prevents lice and scalp infections."},
        {"q": "Why should we brush tongue?", "a": "To remove bacteria", "hint": "Oral hygiene",
            "exp": "Brushing tongue keeps mouth fresh and bacteria-free."},
        {"q": "Why should we not touch face with dirty hands?", "a": "To prevent germs",
            "hint": "Face hygiene", "exp": "Dirty hands can transfer germs to eyes, nose, mouth."},
        {"q": "Why is bathing important in summer?", "a": "To remove sweat and dirt",
            "hint": "Hot weather", "exp": "Bathing removes sweat and prevents body odor."},
        {"q": "Why should we keep clothes dry?", "a": "To prevent germs",
            "hint": "Avoid dampness", "exp": "Dry clothes prevent bacteria and fungus growth."},
        {"q": "Why should we avoid touching food with dirty hands?", "a": "To prevent sickness",
            "hint": "Hand hygiene", "exp": "Dirty hands can contaminate food and cause illness."},
        {"q": "Why should we wash hands before cooking?", "a": "To keep food clean",
            "hint": "Kitchen hygiene", "exp": "Clean hands prevent food contamination."},
        {"q": "Why is it important to sleep with clean sheets?", "a": "To prevent germs",
            "hint": "Bed hygiene", "exp": "Clean sheets reduce bacteria and skin issues."},
        {"q": "Why should we keep shoes outside the house?", "a": "To prevent dirt inside",
            "hint": "Home cleanliness", "exp": "Shoes outside keep the home clean and germ-free."},
        {"q": "Why should we use soap while washing hands?", "a": "To remove germs",
            "hint": "Hygiene habit", "exp": "Soap removes germs better than water alone."},
        {"q": "Why should we wash hands after touching animals?", "a": "To avoid germs",
            "hint": "Pets", "exp": "Animals can carry germs that can spread to humans."},
        {"q": "Why should we cover mouth while yawning?", "a": "To be polite and clean",
            "hint": "Etiquette", "exp": "Covering mouth prevents spreading germs and shows good manners."},
        {"q": "Why should we use clean towels?", "a": "To avoid germs",
            "hint": "Personal item", "exp": "Dirty towels can spread bacteria and infections."},
        {"q": "Why is it important to wash hands after handling garbage?", "a": "To remove germs",
            "hint": "Sanitation", "exp": "Garbage contains germs that can make us sick."},
        {"q": "Why should we brush teeth after meals?", "a": "To remove food particles",
            "hint": "Dental hygiene", "exp": "Brushing removes food and prevents cavities."},
        {"q": "Why should we not share combs?", "a": "To avoid lice",
            "hint": "Hair hygiene", "exp": "Sharing combs can transfer lice and germs."},
        {"q": "Why should we use tissues while sneezing?", "a": "To stop germs",
            "hint": "Disposable", "exp": "Tissues prevent spreading germs to others."},
        {"q": "Why should we drink clean water?", "a": "To stay healthy", "hint": "No contamination",
            "exp": "Clean water prevents diseases and keeps body healthy."},
        {"q": "Why should we not eat with dirty hands?", "a": "To avoid germs",
            "hint": "Hand hygiene", "exp": "Dirty hands can transfer germs to food causing sickness."},
        {"q": "Why should we keep bathroom clean?", "a": "To prevent germs",
            "hint": "Hygiene habit", "exp": "Clean bathrooms reduce bacteria and infections."},
        {"q": "Why should we keep our mouth clean?", "a": "To prevent bad breath and germs",
            "hint": "Oral care", "exp": "Clean mouth prevents cavities, infections, and bad odor."}
    ]

    if "answers" not in st.session_state:
        st.session_state.answers = {}
    if "scores" not in st.session_state:
        st.session_state.scores = {}

    for i, q in enumerate(questions):
        st.subheader(f"Q{i+1}. {q['q']}")
        st.caption(f"Hint: {q['hint']}")
        st.session_state.answers[i] = st.text_input(
            "Your answer", key=f"personal_hygiene_{i}")

    if st.button("✅ Submit"):
        score = 0
        for i, q in enumerate(questions):
            if st.session_state.answers.get(i, "").strip().lower() == q["a"].lower():
                score += 1
        st.session_state.scores["Personal Hygiene"] = f"{score}/{len(questions)}"
        st.success(f"Score: {score}/{len(questions)}")
        for i, q in enumerate(questions):
            st.info(f"Q{i+1} Explanation: {q['exp']}")

    if st.button("🔄 Restart"):
        st.session_state.answers = {}
        st.rerun()
