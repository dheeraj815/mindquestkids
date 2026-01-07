import streamlit as st


def main():
    st.header("💡 Creativity Lab")

    questions = [
        {"q": "What color do you get when you mix red and blue?", "a": "Purple",
            "hint": "Red + Blue", "exp": "Mixing red and blue gives purple."},
        {"q": "Which material is best for making paper crafts?", "a": "Paper",
            "hint": "Sheets", "exp": "Paper is ideal for origami, cards, and crafts."},
        {"q": "Which tool helps in drawing straight lines?", "a": "Ruler",
            "hint": "Measure and guide", "exp": "Rulers help draw straight lines accurately."},
        {"q": "Which material can be molded to make shapes?", "a": "Clay",
            "hint": "Soft and malleable", "exp": "Clay can be shaped into sculptures."},
        {"q": "Which tool is used to cut paper?", "a": "Scissors",
            "hint": "Two blades", "exp": "Scissors are used to cut paper safely."},
        {"q": "Which color is made by mixing blue and yellow?", "a": "Green",
            "hint": "Plants", "exp": "Mixing blue and yellow produces green."},
        {"q": "Which art form uses threads to create patterns?", "a": "Embroidery",
            "hint": "Sewing", "exp": "Embroidery creates designs using thread."},
        {"q": "Which tool is used to erase pencil marks?", "a": "Eraser",
            "hint": "Correct mistakes", "exp": "Erasers remove pencil marks."},
        {"q": "Which material can be folded to make airplanes?", "a": "Paper",
            "hint": "Origami planes", "exp": "Paper is used to fold into planes."},
        {"q": "Which color is made by mixing red and yellow?", "a": "Orange",
            "hint": "Sunset color", "exp": "Red + Yellow = Orange."},
        {"q": "Which tool is used to paint?", "a": "Brush",
            "hint": "Hold in hand", "exp": "Paintbrushes are used to apply paint."},
        {"q": "Which material can be cut with a knife?", "a": "Clay",
            "hint": "Soft and moldable", "exp": "Clay can be cut to shape sculptures."},
        {"q": "Which color is made by mixing all primary colors?", "a": "Brown",
            "hint": "Red + Blue + Yellow", "exp": "Mixing all primary colors yields brown."},
        {"q": "Which tool is used to stick paper together?", "a": "Glue",
            "hint": "Sticky", "exp": "Glue joins papers or objects."},
        {"q": "Which art form uses paints on a surface?", "a": "Painting",
            "hint": "Canvas or paper", "exp": "Painting applies color to create images."},
        {"q": "Which material is used to make models?", "a": "Clay",
            "hint": "Shapeable", "exp": "Clay is ideal for making 3D models."},
        {"q": "Which tool is used to draw circles?", "a": "Compass",
            "hint": "Round shapes", "exp": "A compass draws perfect circles."},
        {"q": "Which material is sticky and comes in sticks?", "a": "Glue stick",
            "hint": "Paper crafts", "exp": "Glue sticks are safe for children to use."},
        {"q": "Which art form uses colors and brushes?", "a": "Painting",
            "hint": "Canvas", "exp": "Painting involves brushes and colors."},
        {"q": "Which tool helps in cutting straight paper lines?", "a": "Scissors",
            "hint": "Two blades", "exp": "Scissors cut paper along straight edges."},
        {"q": "Which color is made by mixing blue and red?", "a": "Purple",
            "hint": "Mix primary colors", "exp": "Blue + Red = Purple."},
        {"q": "Which material can be rolled and shaped?", "a": "Clay",
            "hint": "Soft", "exp": "Clay can be molded into shapes."},
        {"q": "Which tool helps to measure paper edges?", "a": "Ruler",
            "hint": "Straight lines", "exp": "Rulers measure and guide paper cutting."},
        {"q": "Which color is bright and made by mixing red and yellow?",
            "a": "Orange", "hint": "Sunset", "exp": "Red + Yellow = Orange."},
        {"q": "Which tool helps erase pen mistakes?", "a": "Correction pen",
            "hint": "White liquid", "exp": "Correction pen covers pen errors."},
        {"q": "Which material is soft and colorful for kids?", "a": "Playdough",
            "hint": "Moldable", "exp": "Playdough is safe and moldable for kids."},
        {"q": "Which art form uses thread and needles?", "a": "Embroidery",
            "hint": "Decorative sewing", "exp": "Embroidery creates designs with threads."},
        {"q": "Which color is made by mixing blue and yellow?", "a": "Green",
            "hint": "Nature color", "exp": "Blue + Yellow = Green."},
        {"q": "Which tool is used to mix colors?", "a": "Palette",
            "hint": "Hold paints", "exp": "Palettes help mix and hold colors."},
        {"q": "Which material is used for origami?", "a": "Paper",
            "hint": "Foldable", "exp": "Paper is folded to make origami."},
        {"q": "Which tool cuts shapes from paper?", "a": "Scissors",
            "hint": "Crafting", "exp": "Scissors cut out shapes."},
        {"q": "Which material is used to stick decorations?", "a": "Glue",
            "hint": "Sticky", "exp": "Glue attaches paper or decorations."},
        {"q": "Which color is made by mixing red and blue?", "a": "Purple",
            "hint": "Primary colors", "exp": "Red + Blue = Purple."},
        {"q": "Which tool holds brushes and paint?", "a": "Palette", "hint": "Mix colors",
            "exp": "Palettes are used for holding and mixing paints."},
        {"q": "Which art form uses pencils to draw?", "a": "Sketching",
            "hint": "Pencil", "exp": "Sketching creates outlines using pencils."},
        {"q": "Which material is soft and safe for modeling?", "a": "Playdough",
            "hint": "Kids use it", "exp": "Playdough can be shaped without risk."},
        {"q": "Which color is made by mixing blue and yellow?", "a": "Green",
            "hint": "Grass color", "exp": "Blue + Yellow = Green."},
        {"q": "Which tool is used to make paper stick to paper?", "a": "Glue stick",
            "hint": "Child-safe", "exp": "Glue sticks safely attach papers."},
        {"q": "Which art form uses needles and threads?", "a": "Embroidery",
            "hint": "Decorative sewing", "exp": "Embroidery creates designs using thread."}
    ]

    if "answers" not in st.session_state:
        st.session_state.answers = {}
    if "scores" not in st.session_state:
        st.session_state.scores = {}

    for i, q in enumerate(questions):
        st.subheader(f"Q{i+1}. {q['q']}")
        st.caption(f"Hint: {q['hint']}")
        st.session_state.answers[i] = st.text_input(
            "Your answer", key=f"creativity_lab_{i}")

    if st.button("✅ Submit"):
        score = 0
        for i, q in enumerate(questions):
            if st.session_state.answers.get(i, "").strip().lower() == q["a"].lower():
                score += 1
        st.session_state.scores["Creativity Lab"] = f"{score}/{len(questions)}"
        st.success(f"Score: {score}/{len(questions)}")
        for i, q in enumerate(questions):
            st.info(f"Q{i+1} Explanation: {q['exp']}")

    if st.button("🔄 Restart"):
        st.session_state.answers = {}
        st.rerun()
