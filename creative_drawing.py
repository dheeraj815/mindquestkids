import streamlit as st


def main():
    st.header("🎨 Creative Drawing")

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
        {"q": "Which two primary colors make green?", "a": "Blue and Yellow",
            "hint": "Think of plants", "exp": "Blue and yellow mix to form green.", "free": True},
        {"q": "Which tool is best for sketching?", "a": "Pencil", "hint": "Erasable",
            "exp": "Pencils allow light sketching and correction.", "free": True},
        {"q": "What element of art means light or dark?", "a": "Value", "hint": "Related to brightness",
            "exp": "Value shows how light or dark a color is.", "free": True},
        {"q": "Which shape has four equal sides?", "a": "Square", "hint": "All sides are same",
            "exp": "A square has four equal sides and four right angles.", "free": True},
        {"q": "Which perspective creates depth in drawing?", "a": "Linear Perspective", "hint": "Vanishing point",
            "exp": "Linear perspective uses lines converging at a point to show depth.", "free": True},
        {"q": "Which tool is used to erase pencil marks?", "a": "Eraser", "hint": "Remove mistakes",
            "exp": "Erasers remove pencil marks from paper.", "free": True},
        {"q": "What is the art of arranging colors called?", "a": "Color Theory", "hint": "Mixing colors",
            "exp": "Color theory helps artists mix and combine colors harmoniously.", "free": True},
        {"q": "Which medium is water-based and transparent?", "a": "Watercolor", "hint": "Dilute with water",
            "exp": "Watercolors are transparent paints diluted with water.", "free": True},
        {"q": "Which type of line shows motion?", "a": "Gesture Line", "hint": "Quick and loose",
            "exp": "Gesture lines are quick, expressive lines showing motion.", "free": True},
        {"q": "Which tool is used to blend colors in pencil drawing?", "a": "Blender",
            "hint": "Smudge softly", "exp": "Blenders help soften and blend pencil strokes.", "free": True},
        {"q": "Which shape has no corners?", "a": "Circle", "hint": "Round",
            "exp": "A circle is a round shape with no corners.", "free": True},
        {"q": "Which element of art describes surface quality?", "a": "Texture", "hint": "Smooth or rough",
            "exp": "Texture describes how a surface feels or appears.", "free": True},
        {"q": "Which tool is used to draw perfect circles?", "a": "Compass",
            "hint": "Pivot point", "exp": "A compass helps draw precise circles.", "free": True},
        {"q": "Which color scheme uses colors opposite on the color wheel?", "a": "Complementary Colors", "hint": "Contrast",
            "exp": "Complementary colors are opposite on the wheel and create strong contrast.", "free": True},
        {"q": "Which technique uses dots to create shading?", "a": "Stippling", "hint": "Dots",
            "exp": "Stippling creates shading by varying dot density.", "free": True},
        {"q": "Which art element shows the path of a moving point?", "a": "Line",
            "hint": "Connect points", "exp": "Lines are paths connecting points in space.", "free": True},
        {"q": "Which tool is used to cut paper precisely?", "a": "Scissors",
            "hint": "Sharp edges", "exp": "Scissors allow precise cutting of paper.", "free": True},
        {"q": "Which drawing style captures realistic subjects?", "a": "Realism", "hint": "True to life",
            "exp": "Realism focuses on accurate, lifelike depictions.", "free": True},
        {"q": "Which medium is thick and dries slowly?", "a": "Oil Paint", "hint": "Slow drying",
            "exp": "Oil paints are thick and take longer to dry.", "free": True},
        {"q": "Which perspective shows objects smaller as they get farther?", "a": "Foreshortening",
            "hint": "Depth illusion", "exp": "Foreshortening creates depth by shrinking distant objects.", "free": True},

        # PRO QUESTIONS (21-50)
        {"q": "Which element of art refers to the area around objects?", "a": "Space",
            "hint": "Positive and negative", "exp": "Space refers to areas around and between objects.", "free": False},
        {"q": "Which drawing tool uses ink and pen tip?", "a": "Fineliner", "hint": "Precision lines",
            "exp": "Fineliners produce precise, clean ink lines.", "free": False},
        {"q": "Which color is made by mixing red and blue?", "a": "Purple",
            "hint": "Violet", "exp": "Red and blue mix to form purple.", "free": False},
        {"q": "Which tool protects hands while erasing charcoal?", "a": "Kneaded Eraser", "hint": "Moldable",
            "exp": "Kneaded erasers can be shaped and lift charcoal without smudging.", "free": False},
        {"q": "Which shading technique uses parallel lines?", "a": "Hatching", "hint": "Lines",
            "exp": "Hatching creates shading with closely spaced parallel lines.", "free": False},
        {"q": "Which element gives drawings a sense of movement?", "a": "Line Direction",
            "hint": "Angle matters", "exp": "Direction of lines can suggest motion in a drawing.", "free": False},
        {"q": "Which color scheme uses shades of one color?", "a": "Monochromatic", "hint": "Single color",
            "exp": "Monochromatic uses tints and shades of a single color.", "free": False},
        {"q": "Which tool sharpens pencils precisely?", "a": "Pencil Sharpener", "hint": "Pointed tip",
            "exp": "Pencil sharpeners make pencils ready for detailed work.", "free": False},
        {"q": "Which type of art uses small pieces of colored paper?", "a": "Collage", "hint": "Cut & paste",
            "exp": "Collage is art made by assembling various materials on a surface.", "free": False},
        {"q": "Which element shows how things feel to touch?", "a": "Texture", "hint": "Rough or smooth",
            "exp": "Texture in art simulates the feel of surfaces.", "free": False},
        {"q": "Which tool mixes paint on a palette?", "a": "Palette Knife", "hint": "Spread & mix",
            "exp": "Palette knives mix paint and create texture.", "free": False},
        {"q": "Which color is made by mixing yellow and red?", "a": "Orange",
            "hint": "Sunset color", "exp": "Yellow and red mix to form orange.", "free": False},
        {"q": "Which drawing style uses exaggerated features for humor?", "a": "Caricature",
            "hint": "Funny faces", "exp": "Caricature exaggerates features to create humor.", "free": False},
        {"q": "Which technique uses overlapping lines for shading?", "a": "Cross-Hatching",
            "hint": "Criss-cross", "exp": "Cross-hatching layers lines at angles for depth.", "free": False},
        {"q": "Which medium is powdered pigment mixed with water?", "a": "Gouache", "hint": "Opaque watercolor",
            "exp": "Gouache is similar to watercolor but more opaque.", "free": False},
        {"q": "Which element defines the edges of objects?", "a": "Contour", "hint": "Outline",
            "exp": "Contours are lines that define shape edges.", "free": False},
        {"q": "Which color scheme uses three colors equally spaced on wheel?", "a": "Triadic Colors",
            "hint": "Triangle pattern", "exp": "Triadic colors are three colors evenly spaced on the color wheel.", "free": False},
        {"q": "Which tool creates soft shading for pencil drawings?", "a": "Tortillon",
            "hint": "Paper stump", "exp": "A tortillon blends pencil for smooth shading.", "free": False},
        {"q": "Which element of art refers to the shape of objects?", "a": "Form",
            "hint": "3D appearance", "exp": "Form describes three-dimensional shapes.", "free": False},
        {"q": "Which drawing style simplifies subjects into basic shapes?", "a": "Abstract",
            "hint": "Not realistic", "exp": "Abstract art uses simplified shapes and colors.", "free": False},
        {"q": "Which technique creates texture using small marks?", "a": "Scumbling", "hint": "Layered strokes",
            "exp": "Scumbling uses light, irregular marks to create texture.", "free": False},
        {"q": "Which color is made by mixing all primary colors?", "a": "Brown",
            "hint": "Neutral tone", "exp": "Mixing red, yellow, and blue creates brown.", "free": False},
        {"q": "Which principle of art creates visual weight?", "a": "Balance", "hint": "Symmetry",
            "exp": "Balance distributes visual elements evenly.", "free": False},
        {"q": "Which medium uses wax sticks?", "a": "Crayon", "hint": "Childhood favorite",
            "exp": "Crayons are wax-based coloring tools.", "free": False},
        {"q": "Which technique layers colors to create new ones?", "a": "Glazing", "hint": "Transparent layers",
            "exp": "Glazing applies thin transparent layers of color.", "free": False},
        {"q": "Which element creates visual interest through differences?", "a": "Contrast",
            "hint": "Opposites", "exp": "Contrast shows differences in value, color, or texture.", "free": False},
        {"q": "Which tool creates fine details in ink drawings?", "a": "Nib Pen",
            "hint": "Dip in ink", "exp": "Nib pens allow precise ink line work.", "free": False},
        {"q": "Which principle repeats elements for unity?", "a": "Pattern", "hint": "Repetition",
            "exp": "Patterns use repeated elements to create rhythm.", "free": False},
        {"q": "Which medium uses oil-based pastels?", "a": "Oil Pastel", "hint": "Buttery texture",
            "exp": "Oil pastels are soft and blend easily.", "free": False},
        {"q": "Which technique removes material to create art?", "a": "Subtractive", "hint": "Carving",
            "exp": "Subtractive methods remove material like in sculpture.", "free": False}
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
                key=f"creative_drawing_{i}",
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
        st.session_state.scores["Creative Drawing"] = f"{score}/{total_available}"
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
